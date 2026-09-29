/* The gate.

   Public: the sales page, and the handful of endpoints needed to buy or sign
   in. Everything else -- the app itself and every question in it -- is served
   only to a signed-in session whose user row says paid = 1. */

import GATED from '../assets/gated.js';
import { createCheckout, fetchCheckout, verifyWebhook } from './stripe.js';
import * as google from './google.js';
import * as password from './password.js';
import {
  currentUser, createSession, endSession, cookieHeader, readCookie,
  normalizeEmail, findOrCreateUser, issueLoginCode, verifyLoginCode, now,
} from './auth.js';

const SECURITY = {
  'X-Content-Type-Options': 'nosniff',
  'Referrer-Policy': 'strict-origin-when-cross-origin',
  'X-Frame-Options': 'DENY',
};

const json = (data, status = 200, headers = {}) =>
  new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json; charset=utf-8',
               'Cache-Control': 'no-store', ...SECURITY, ...headers },
  });

const html = (body, status = 200, headers = {}) =>
  new Response(body, {
    status,
    headers: { 'Content-Type': 'text/html; charset=utf-8',
               'Cache-Control': 'no-store', ...SECURITY, ...headers },
  });

const redirect = (to, headers = {}) =>
  new Response(null, { status: 302, headers: { Location: to, ...headers } });

async function readJson(request) {
  try { return await request.json(); } catch (e) { return {}; }
}

async function sendCode(env, email, code) {
  if (!env.RESEND_API_KEY) return { error: 'email-not-configured' };
  const res = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: { Authorization: `Bearer ${env.RESEND_API_KEY}`,
               'Content-Type': 'application/json' },
    body: JSON.stringify({
      from: env.FROM_EMAIL || 'login@example.com',
      to: [email],
      subject: `${code} is your sign-in code`,
      text: `Your sign-in code for Georgia Real Estate Exam Prep is ${code}.\n` +
            `It expires in 15 minutes. If you did not ask for it, ignore this.`,
    }),
  });
  return res.ok ? {} : { error: 'email-send-failed' };
}

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const path = url.pathname.replace(/\/+$/, '') || '/';
    const origin = env.SITE_URL || url.origin;

    if (!env.SESSION_SECRET) {
      return html('<h1>Not configured</h1><p>SESSION_SECRET is not set. ' +
                  'Run <code>wrangler secret put SESSION_SECRET</code>.</p>', 500);
    }

    /* ---------------------------------------------------- Stripe webhook */
    if (path === '/api/stripe-webhook' && request.method === 'POST') {
      const raw = await request.text();
      const { event, error } = await verifyWebhook(
        env, raw, request.headers.get('Stripe-Signature'));
      if (error) return json({ error }, 400);

      const seen = await env.DB.prepare('SELECT id FROM stripe_events WHERE id = ?')
        .bind(event.id).first();
      if (seen) return json({ ok: true, duplicate: true });
      await env.DB.prepare('INSERT INTO stripe_events (id, seen_at) VALUES (?, ?)')
        .bind(event.id, now()).run();

      if (event.type === 'checkout.session.completed') {
        const s = event.data.object;
        if (s.payment_status === 'paid') {
          /* client_reference_id is the account we created at sign-in. Trust
             it over the address Stripe collected, which may be a different
             one the buyer typed at the till. */
          let userId = s.client_reference_id || null;
          if (userId) {
            const known = await env.DB.prepare('SELECT id FROM users WHERE id = ?')
              .bind(userId).first();
            if (!known) userId = null;
          }
          if (!userId) {
            const email = normalizeEmail(s.customer_details?.email || s.customer_email);
            if (email) userId = (await findOrCreateUser(env, email)).id;
          }
          if (userId) {
            await env.DB.prepare(
              'UPDATE users SET paid = 1, stripe_id = ?, paid_at = ? WHERE id = ?'
            ).bind(s.customer || s.id, now(), userId).run();
          }
        }
      }
      return json({ ok: true });
    }

    /* --------------------------------------------------------- buy flow */
    if (path === '/api/checkout' && request.method === 'POST') {
      if (!env.STRIPE_SECRET_KEY) return json({ error: 'Payments are not set up yet.' }, 503);
      /* Signing in comes first, so the payment attaches to an account we
         already know rather than to whatever address Stripe collects. */
      const who = await currentUser(request, env);
      if (!who) return json({ error: 'sign in first', signin: '/api/auth/google' }, 401);
      if (who.paid) return json({ url: `${origin}/app` });
      try {
        const link = await createCheckout(env, {
          email: who.email, origin, userId: who.id,
        });
        return json({ url: link });
      } catch (e) {
        return json({ error: e.message }, 502);
      }
    }

    /* -------------------------------------------- email and password ---- */
    const LOCK_AFTER = 8;          // failed attempts before a cool-off
    const LOCK_SECONDS = 900;

    async function attemptState(email) {
      const row = await env.DB.prepare(
        'SELECT fails, locked_till FROM auth_attempts WHERE email = ?').bind(email).first();
      return row || { fails: 0, locked_till: 0 };
    }
    async function noteFailure(email) {
      const st = await attemptState(email);
      const fails = st.fails + 1;
      const until = fails >= LOCK_AFTER ? now() + LOCK_SECONDS : 0;
      await env.DB.prepare(
        `INSERT INTO auth_attempts (email, fails, locked_till) VALUES (?, ?, ?)
         ON CONFLICT(email) DO UPDATE SET fails = excluded.fails,
                                          locked_till = excluded.locked_till`
      ).bind(email, fails, until).run();
    }
    async function clearFailures(email) {
      await env.DB.prepare('DELETE FROM auth_attempts WHERE email = ?').bind(email).run();
    }

    if (path === '/api/auth/signup' && request.method === 'POST') {
      const body = await readJson(request);
      const email = normalizeEmail(body.email);
      if (!email) return json({ error: 'That does not look like an email address.' }, 400);
      const bad = password.problemWith(body.password);
      if (bad) return json({ error: bad }, 400);

      const existing = await env.DB.prepare(
        'SELECT id, password_hash FROM users WHERE email = ?').bind(email).first();
      if (existing && existing.password_hash) {
        return json({ error: 'There is already an account on that address. ' +
                             'Log in instead.' }, 409);
      }
      const hashed = await password.hash(body.password);
      let user;
      if (existing) {
        /* Bought through Google first, now adding a password: same account. */
        user = { id: existing.id };
        await env.DB.prepare('UPDATE users SET password_hash = ? WHERE id = ?')
          .bind(hashed, user.id).run();
      } else {
        user = await findOrCreateUser(env, email);
        await env.DB.prepare('UPDATE users SET password_hash = ? WHERE id = ?')
          .bind(hashed, user.id).run();
      }
      const fresh = await env.DB.prepare('SELECT paid FROM users WHERE id = ?')
        .bind(user.id).first();
      const { cookie } = await createSession(env, user.id);
      return json({ ok: true, paid: !!(fresh && fresh.paid) }, 200,
                  { 'Set-Cookie': cookie });
    }

    if (path === '/api/auth/login' && request.method === 'POST') {
      const body = await readJson(request);
      const email = normalizeEmail(body.email);
      if (!email) return json({ error: 'That does not look like an email address.' }, 400);

      const st = await attemptState(email);
      if (st.locked_till > now()) {
        return json({ error: 'Too many attempts. Try again in fifteen minutes, ' +
                             'or use Continue with Google.' }, 429);
      }
      const row = await env.DB.prepare(
        'SELECT id, paid, password_hash FROM users WHERE email = ?').bind(email).first();
      /* The check runs even with no account so the reply takes the same time
         either way, and says the same thing either way. */
      const checked = await password.verify(body.password, row && row.password_hash);
      if (!checked.ok) {
        await noteFailure(email);
        return json({ error: 'That email and password do not match.' }, 401);
      }
      if (checked.stale) {
        await env.DB.prepare('UPDATE users SET password_hash = ? WHERE id = ?')
          .bind(await password.hash(body.password), row.id).run();
      }
      await clearFailures(email);
      const { cookie } = await createSession(env, row.id);
      return json({ ok: true, paid: !!row.paid }, 200, { 'Set-Cookie': cookie });
    }

    /* ------------------------------------------------- sign in with Google */
    if (path === '/api/auth/google') {
      if (!google.configured(env)) {
        return html('<h1>Google sign-in is not set up yet</h1><p>Set ' +
                    'GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET.</p>', 503);
      }
      const started = await google.startUrl(env, url, url.searchParams.get('next'));
      return redirect(started.url, { 'Set-Cookie': started.cookie });
    }

    if (path === '/api/auth/google/callback') {
      const clear = google.clearStateCookie();
      if (!google.configured(env)) return redirect('/?auth=unavailable');
      if (url.searchParams.get('error')) {
        return redirect('/?auth=cancelled', { 'Set-Cookie': clear });
      }
      const checked = await google.checkState(
        env, url.searchParams.get('state'), google.readStateCookie(request));
      if (checked.error) return redirect('/?auth=expired', { 'Set-Cookie': clear });

      const got = await google.exchange(env, url, url.searchParams.get('code'));
      if (got.error) return redirect('/?auth=failed', { 'Set-Cookie': clear });

      const email = normalizeEmail(got.email);
      if (!email) return redirect('/?auth=failed', { 'Set-Cookie': clear });
      const user = await findOrCreateUser(env, email);
      const { cookie } = await createSession(env, user.id);
      /* Two cookies on one response: the new session, and the state cookie
         being cleared. Headers.append, because set() would drop one. */
      const out = redirect(user.paid ? '/app' : '/?pay=1');
      out.headers.append('Set-Cookie', cookie);
      out.headers.append('Set-Cookie', clear);
      return out;
    }

    /* Straight off a successful payment: verify the session with Stripe
       rather than believing the query string, then sign them in. */
    if (path === '/activate') {
      const id = url.searchParams.get('session_id');
      if (!id) return redirect('/');
      try {
        const s = await fetchCheckout(env, id);
        if (s.payment_status !== 'paid') return redirect('/?checkout=incomplete');
        let user = null;
        if (s.client_reference_id) {
          const row = await env.DB.prepare('SELECT id, email, paid FROM users WHERE id = ?')
            .bind(s.client_reference_id).first();
          if (row) user = { id: row.id, email: row.email, paid: !!row.paid };
        }
        if (!user) {
          const email = normalizeEmail(s.customer_details?.email || s.customer_email);
          if (!email) return redirect('/?checkout=incomplete');
          user = await findOrCreateUser(env, email);
        }
        await env.DB.prepare(
          'UPDATE users SET paid = 1, stripe_id = ?, paid_at = COALESCE(paid_at, ?) WHERE id = ?'
        ).bind(s.customer || s.id, now(), user.id).run();
        const { cookie } = await createSession(env, user.id);
        return redirect('/app?welcome=1', { 'Set-Cookie': cookie });
      } catch (e) {
        return redirect('/?checkout=error');
      }
    }

    /* ---------------------------------------------------------- sign in */
    if (path === '/api/login/start' && request.method === 'POST') {
      const body = await readJson(request);
      const email = normalizeEmail(body.email);
      if (!email) return json({ error: 'That does not look like an email address.' }, 400);

      const known = await env.DB.prepare('SELECT paid FROM users WHERE email = ?')
        .bind(email).first();
      /* Same answer either way: whether an address has bought is not something
         a stranger gets to probe for. */
      if (!known || !known.paid) {
        return json({ ok: true, sent: true });
      }
      const issued = await issueLoginCode(env, email);
      if (issued.error) return json({ error: issued.error }, 429);
      const sent = await sendCode(env, email, issued.code);
      if (sent.error) {
        /* The code was issued before we knew the send would fail, so it is
           sitting there rate-limiting a retry for a minute. Clear it. */
        await env.DB.prepare('DELETE FROM login_codes WHERE email = ?').bind(email).run();
        if (sent.error === 'email-not-configured') {
          return json({ error: 'Email sign-in is not switched on yet. ' +
                               'Use the link in your Stripe receipt, or contact support.' }, 503);
        }
        return json({ error: 'Could not send that email. Try again shortly.' }, 502);
      }
      return json({ ok: true, sent: true });
    }

    if (path === '/api/login/verify' && request.method === 'POST') {
      const body = await readJson(request);
      const email = normalizeEmail(body.email);
      if (!email) return json({ error: 'That does not look like an email address.' }, 400);
      const check = await verifyLoginCode(env, email, body.code);
      if (check.error) return json({ error: check.error }, 401);
      const user = await env.DB.prepare('SELECT id, paid FROM users WHERE email = ?')
        .bind(email).first();
      if (!user || !user.paid) return json({ error: 'No access on that address.' }, 403);
      const { cookie } = await createSession(env, user.id);
      return json({ ok: true }, 200, { 'Set-Cookie': cookie });
    }

    if (path === '/api/logout' && request.method === 'POST') {
      const me = await currentUser(request, env);
      if (me) await endSession(env, me.sessionId);
      return json({ ok: true }, 200, { 'Set-Cookie': cookieHeader('', 0) });
    }

    if (path === '/api/me') {
      const me = await currentUser(request, env);
      return json(me ? { signedIn: true, paid: me.paid, email: me.email }
                     : { signedIn: false, paid: false });
    }

    /* ------------------------------------------------------ gated below */
    const me = await currentUser(request, env);
    const gated = path === '/app' || path === '/api/bundle' || path === '/api/progress';

    if (gated && (!me || !me.paid)) {
      if (path === '/app') return redirect('/?gate=1');
      return json({ error: 'payment required' }, 402);
    }

    if (path === '/app') return html(GATED.appHtml);

    if (path === '/api/bundle') return json(GATED.data);

    if (path === '/api/progress') {
      if (request.method === 'GET') {
        const row = await env.DB.prepare('SELECT data FROM progress WHERE user_id = ?')
          .bind(me.id).first();
        return json(row ? JSON.parse(row.data) : null);
      }
      if (request.method === 'PUT') {
        const body = await request.text();
        if (body.length > 2_000_000) return json({ error: 'too large' }, 413);
        try { JSON.parse(body); } catch (e) { return json({ error: 'bad json' }, 400); }
        await env.DB.prepare(
          `INSERT INTO progress (user_id, data, updated_at) VALUES (?, ?, ?)
           ON CONFLICT(user_id) DO UPDATE SET data = excluded.data,
                                              updated_at = excluded.updated_at`
        ).bind(me.id, body, now()).run();
        return json({ ok: true });
      }
      return json({ error: 'method not allowed' }, 405);
    }

    /* ------------------------------------------------- everything public */
    const PAGES = { '/': '/index.html', '/buy': '/buy.html',
                    '/terms': '/terms.html', '/privacy': '/privacy.html' };
    const wanted = PAGES[path]
      ? new Request(new URL(PAGES[path], url.origin), request)
      : request;
    const asset = await env.ASSETS.fetch(wanted);
    if (asset.status !== 404) {
      const out = new Response(asset.body, asset);
      for (const [k, v] of Object.entries(SECURITY)) out.headers.set(k, v);
      return out;
    }
    return redirect('/');
  },
};
