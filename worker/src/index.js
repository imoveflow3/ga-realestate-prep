/* The gate.

   Public: the sales page, and the handful of endpoints needed to buy or sign
   in. Everything else -- the app itself and every question in it -- is served
   only to a signed-in session whose user row says paid = 1. */

import GATED from '../assets/gated.js';
import { createCheckout, fetchCheckout, verifyWebhook } from './stripe.js';
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
        const email = normalizeEmail(s.customer_details?.email || s.customer_email);
        if (email && s.payment_status === 'paid') {
          const user = await findOrCreateUser(env, email);
          await env.DB.prepare(
            'UPDATE users SET paid = 1, stripe_id = ?, paid_at = ? WHERE id = ?'
          ).bind(s.customer || s.id, now(), user.id).run();
        }
      }
      return json({ ok: true });
    }

    /* --------------------------------------------------------- buy flow */
    if (path === '/api/checkout' && request.method === 'POST') {
      if (!env.STRIPE_SECRET_KEY) return json({ error: 'Payments are not set up yet.' }, 503);
      const body = await readJson(request);
      try {
        const link = await createCheckout(env, {
          email: normalizeEmail(body.email) || undefined, origin,
        });
        return json({ url: link });
      } catch (e) {
        return json({ error: e.message }, 502);
      }
    }

    /* Straight off a successful payment: verify the session with Stripe
       rather than believing the query string, then sign them in. */
    if (path === '/activate') {
      const id = url.searchParams.get('session_id');
      if (!id) return redirect('/');
      try {
        const s = await fetchCheckout(env, id);
        const email = normalizeEmail(s.customer_details?.email || s.customer_email);
        if (s.payment_status !== 'paid' || !email) return redirect('/?checkout=incomplete');
        const user = await findOrCreateUser(env, email);
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
    const asset = await env.ASSETS.fetch(request);
    if (asset.status !== 404) {
      const out = new Response(asset.body, asset);
      for (const [k, v] of Object.entries(SECURITY)) out.headers.set(k, v);
      return out;
    }
    return redirect('/');
  },
};
