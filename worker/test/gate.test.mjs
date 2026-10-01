/* Does the gate actually hold?

   The two ways this can be wrong are opposite and both fatal: nobody can get
   in, or everybody gets in free. These exercise the real router against a
   stubbed database and a stubbed Stripe. */

import assert from 'node:assert/strict';
import worker from '../src/index.js';
import { makeDB } from './d1stub.js';
import { hmacHex } from '../src/crypto.js';

const ORIGIN = 'https://prep.test';

/* Nothing here is allowed to touch the network. The email provider is
   intercepted so the test can read the code it would have sent, and Stripe
   answers with the shape the Worker expects. */
const SENT = { code: null, to: null, verifyToken: null, resetToken: null };
const GOOGLE = { email: 'gmail.user@gmail.com', verified: true };
let LAST_CHECKOUT = new URLSearchParams();
const realFetch = globalThis.fetch;
globalThis.fetch = async (input, init = {}) => {
  const url = typeof input === 'string' ? input : input.url;
  if (url.startsWith('https://api.resend.com/')) {
    const body = JSON.parse(init.body);
    SENT.to = body.to[0];
    SENT.code = (body.text.match(/\b(\d{6})\b/) || [])[1] || null;
    SENT.verifyToken = (body.text.match(/\/auth\/verify\?token=([\w-]+)/) || [])[1]
                       || SENT.verifyToken;
    SENT.resetToken = (body.text.match(/\/auth\?reset=([\w-]+)/) || [])[1]
                      || SENT.resetToken;
    SENT.subject = body.subject;
    return new Response('{"id":"stub"}', { status: 200 });
  }
  if (url === 'https://oauth2.googleapis.com/token') {
    const sent = new URLSearchParams(init.body);
    if (sent.get('code') !== 'good-code') {
      return new Response(JSON.stringify({error: 'invalid_grant'}), {status: 400});
    }
    const claims = btoa(JSON.stringify({
      email: GOOGLE.email, email_verified: GOOGLE.verified,
      aud: 'test-client-id', sub: 'sub-123',
    })).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
    return new Response(JSON.stringify({id_token: 'h.' + claims + '.s'}), {status: 200});
  }
  if (url.startsWith('https://api.stripe.com/v1/checkout/sessions/')) {
    return new Response(JSON.stringify({
      payment_status: 'paid', customer: 'cus_activate',
      customer_details: { email: 'activated@example.com' } }), { status: 200 });
  }
  if (url === 'https://api.stripe.com/v1/checkout/sessions') {
    LAST_CHECKOUT = new URLSearchParams(init.body);
    return new Response(JSON.stringify({ url: 'https://checkout.stripe.com/c/pay/stub' }),
                        { status: 200 });
  }
  throw new Error('test tried to reach the network: ' + url);
};
let PASS = 0, FAIL = 0;

async function it(name, fn) {
  try { await fn(); PASS++; console.log('  ok   ' + name); }
  catch (e) { FAIL++; console.log('  FAIL ' + name + '\n       ' + e.message); }
}

function makeEnv(db) {
  return {
    DB: db,
    SESSION_SECRET: 'test-secret-do-not-use',
    STRIPE_SECRET_KEY: 'sk_test_x',
    STRIPE_WEBHOOK_SECRET: 'whsec_test',
    SITE_URL: ORIGIN,
    RESEND_API_KEY: 're_test',
    ADMIN_EMAILS: 'boss@example.com, Second.Admin@Example.com',
    GOOGLE_CLIENT_ID: 'test-client-id',
    GOOGLE_CLIENT_SECRET: 'test-client-secret',
    FROM_EMAIL: 'login@prep.test',
    PRICE_CENTS: '1900',
    ASSETS: { fetch: async (r) => new Response(new URL(r.url).pathname, {
      status: 200, headers: { 'Content-Type': 'text/html' } }) },
  };
}

const req = (path, init = {}) => new Request(ORIGIN + path, init);
const cookieOf = res => (res.headers.get('Set-Cookie') || '').split(';')[0];

async function signedWebhook(env, body) {
  const t = Math.floor(Date.now() / 1000);
  const sig = await hmacHex(env.STRIPE_WEBHOOK_SECRET, `${t}.${body}`);
  return { 'Stripe-Signature': `t=${t},v1=${sig}`, 'Content-Type': 'application/json' };
}

console.log('\nGATE');

const db = makeDB();
const env = makeEnv(db);

await it('a stranger asking for /app is bounced to the sales page', async () => {
  const res = await worker.fetch(req('/app'), env, {});
  assert.equal(res.status, 302);
  assert.equal(res.headers.get('Location'), '/auth?gate=1');
});

await it('a stranger asking for the question bank gets 402, not questions', async () => {
  const res = await worker.fetch(req('/api/bundle'), env, {});
  assert.equal(res.status, 402);
  const body = await res.text();
  assert.ok(!body.includes('"choices"'), 'bundle leaked to an unpaid caller');
});

await it('a stranger cannot read or write progress', async () => {
  assert.equal((await worker.fetch(req('/api/progress'), env, {})).status, 402);
  assert.equal((await worker.fetch(req('/api/progress', {
    method: 'PUT', body: '{"attempts":[]}' }), env, {})).status, 402);
});

await it('/api/me says not signed in', async () => {
  const me = await (await worker.fetch(req('/api/me'), env, {})).json();
  assert.deepEqual(me, { signedIn: false, paid: false, verified: false, google: true });
});

await it('a forged webhook signature is rejected and grants nothing', async () => {
  const body = JSON.stringify({ id: 'evt_forged', type: 'checkout.session.completed',
    data: { object: { payment_status: 'paid', customer_email: 'thief@example.com' } } });
  const res = await worker.fetch(req('/api/stripe-webhook', {
    method: 'POST', body, headers: { 'Stripe-Signature': 't=1,v1=deadbeef' } }), env, {});
  assert.equal(res.status, 400);
  assert.equal(db._tables.users.length, 0, 'a forged webhook created a user');
});

await it('a stale but correctly signed webhook is rejected', async () => {
  const body = JSON.stringify({ id: 'evt_stale', type: 'checkout.session.completed',
    data: { object: { payment_status: 'paid', customer_email: 'old@example.com' } } });
  const t = Math.floor(Date.now() / 1000) - 4000;
  const sig = await hmacHex(env.STRIPE_WEBHOOK_SECRET, `${t}.${body}`);
  const res = await worker.fetch(req('/api/stripe-webhook', {
    method: 'POST', body, headers: { 'Stripe-Signature': `t=${t},v1=${sig}` } }), env, {});
  assert.equal(res.status, 400);
});

let buyerCookie = null;

await it('a genuine webhook marks the buyer paid', async () => {
  const body = JSON.stringify({ id: 'evt_1', type: 'checkout.session.completed',
    data: { object: { payment_status: 'paid', customer: 'cus_1',
                      customer_details: { email: 'Buyer@Example.com ' } } } });
  const res = await worker.fetch(req('/api/stripe-webhook', {
    method: 'POST', body, headers: await signedWebhook(env, body) }), env, {});
  assert.equal(res.status, 200);
  const u = db._tables.users.find(u => u.email === 'buyer@example.com');
  assert.ok(u && u.paid === 1, 'buyer not marked paid');
});

await it('the same webhook replayed does not double-credit', async () => {
  const body = JSON.stringify({ id: 'evt_1', type: 'checkout.session.completed',
    data: { object: { payment_status: 'paid', customer_details: { email: 'buyer@example.com' } } } });
  const res = await worker.fetch(req('/api/stripe-webhook', {
    method: 'POST', body, headers: await signedWebhook(env, body) }), env, {});
  assert.deepEqual(await res.json(), { ok: true, duplicate: true });
  assert.equal(db._tables.users.length, 1);
});

await it('signing in needs the real code', async () => {
  const start = await worker.fetch(req('/api/login/start', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: 'buyer@example.com' }) }), env, {});
  assert.equal(start.status, 200, 'sending the code failed');
  assert.ok(SENT.code, 'no code reached the email provider');

  const wrong = await worker.fetch(req('/api/login/verify', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: 'buyer@example.com', code: '000000' }) }), env, {});
  assert.equal(wrong.status, 401);
  assert.equal(wrong.headers.get('Set-Cookie'), null, 'a wrong code set a cookie');

  const right = await worker.fetch(req('/api/login/verify', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: 'buyer@example.com', code: SENT.code }) }), env, {});
  assert.equal(right.status, 200);
  buyerCookie = cookieOf(right);
  assert.ok(buyerCookie.startsWith('ga_session='), 'no session cookie issued');
});

await it('a used code cannot be used twice', async () => {
  const again = await worker.fetch(req('/api/login/verify', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: 'buyer@example.com', code: SENT.code }) }), env, {});
  assert.equal(again.status, 401);
});

await it('the buyer now gets the app and the bundle', async () => {
  const app = await worker.fetch(req('/app', { headers: { Cookie: buyerCookie } }), env, {});
  assert.equal(app.status, 200);
  assert.ok((await app.text()).includes('__BOOT__'), 'app html not served');

  const bundle = await worker.fetch(req('/api/bundle', { headers: { Cookie: buyerCookie } }), env, {});
  assert.equal(bundle.status, 200);
  const data = await bundle.json();
  assert.ok(data.banks.national.length > 100, 'bundle came back empty');
  assert.deepEqual(data.profile_default, {}, 'personal profile shipped to buyers');
});

await it('a tampered session cookie is worthless', async () => {
  const [name, value] = buyerCookie.split('=');
  const id = value.slice(0, value.lastIndexOf('.'));
  const forged = `${name}=${id}.AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA`;
  const res = await worker.fetch(req('/api/bundle', { headers: { Cookie: forged } }), env, {});
  assert.equal(res.status, 402, 'a forged signature got through');
});

await it('progress round-trips and stays with the right user', async () => {
  const payload = JSON.stringify({ attempts: [{ count: 20 }], profile: { hours_per_week: 10 } });
  const put = await worker.fetch(req('/api/progress', {
    method: 'PUT', headers: { Cookie: buyerCookie, 'Content-Type': 'application/json' },
    body: payload }), env, {});
  assert.equal(put.status, 200);
  const got = await (await worker.fetch(req('/api/progress', {
    headers: { Cookie: buyerCookie } }), env, {})).json();
  assert.equal(got.attempts[0].count, 20);
  assert.equal(got.profile.hours_per_week, 10);
});

await it('a second, unpaid account cannot read the first one', async () => {
  const { findOrCreateUser, createSession } = await import('../src/auth.js');
  const freeloader = await findOrCreateUser(env, 'free@example.com');
  const { cookie } = await createSession(env, freeloader.id);
  const c = cookie.split(';')[0];
  assert.equal((await worker.fetch(req('/api/bundle', { headers: { Cookie: c } }), env, {})).status, 402);
  assert.equal((await worker.fetch(req('/api/progress', { headers: { Cookie: c } }), env, {})).status, 402);
  assert.equal((await worker.fetch(req('/app', { headers: { Cookie: c } }), env, {})).status, 302);
});

await it('signing out kills the session', async () => {
  const out = await worker.fetch(req('/api/logout', {
    method: 'POST', headers: { Cookie: buyerCookie } }), env, {});
  assert.equal(out.status, 200);
  assert.equal((await worker.fetch(req('/api/bundle', {
    headers: { Cookie: buyerCookie } }), env, {})).status, 402);
});

await it('login never reveals whether an address has bought', async () => {
  const unknown = await worker.fetch(req('/api/login/start', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: 'nobody@example.com' }) }), env, {});
  assert.equal(unknown.status, 200);
  assert.deepEqual(await unknown.json(), { ok: true, sent: true });
});

await it('an oversized progress body is refused', async () => {
  const { findOrCreateUser, createSession } = await import('../src/auth.js');
  const u = db._tables.users.find(u => u.email === 'buyer@example.com');
  const { cookie } = await createSession(env, u.id);
  const c = cookie.split(';')[0];
  const huge = JSON.stringify({ blob: 'x'.repeat(2_100_000) });
  const res = await worker.fetch(req('/api/progress', {
    method: 'PUT', headers: { Cookie: c, 'Content-Type': 'application/json' },
    body: huge }), env, {});
  assert.equal(res.status, 413);
});

/* The contract changed when sign-in moved in front of payment: you cannot
   start a checkout as a stranger any more, and asking for one must not
   quietly create an account out of whatever address was posted. */
await it('an anonymous checkout is refused and creates nothing', async () => {
  const before = db._tables.users.length;
  const res = await worker.fetch(req('/api/checkout', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: 'new@example.com' }) }), env, {});
  assert.equal(res.status, 401);
  assert.equal((await res.json()).signin, '/api/auth/google');
  assert.equal(db._tables.users.length, before, 'a posted address became an account');
});

await it('returning from a real checkout signs you straight in', async () => {
  const res = await worker.fetch(req('/activate?session_id=cs_test_1'), env, {});
  assert.equal(res.status, 302);
  assert.equal(res.headers.get('Location'), '/app?welcome=1');
  const c = cookieOf(res);
  const bundle = await worker.fetch(req('/api/bundle', { headers: { Cookie: c } }), env, {});
  assert.equal(bundle.status, 200, 'a fresh buyer could not reach the bundle');
});

await it('/activate without a session_id just goes home', async () => {
  const res = await worker.fetch(req('/activate'), env, {});
  assert.equal(res.status, 302);
  assert.equal(res.headers.get('Location'), '/');
});

/* This used to assert that the Worker rewrote /auth to /auth.html, which it
   did, and which was wrong -- the real asset server bounces .html back to the
   clean path and the two fought in a loop. A stub that answers whatever it is
   asked can only ever confirm the code does what the code does. The check
   that matters is that the path is passed through untouched; the loop itself
   is caught by scripts/smoke.mjs against a running server. */
await it('public paths are handed to the asset server unchanged', async () => {
  for (const asked of ['/', '/buy', '/auth', '/terms', '/privacy']) {
    const res = await worker.fetch(req(asked), env, {});
    assert.equal(res.status, 200, asked + ' did not resolve');
    assert.equal(await res.text(), asked, asked + ' was rewritten before dispatch');
  }
});

await it('an unknown path goes home rather than 404ing into nothing', async () => {
  const res = await worker.fetch(req('/nope'), env, {});
  assert.ok([200, 302].includes(res.status));
});


console.log('\nGOOGLE SIGN-IN');

await it('starting sign-in redirects to Google with a signed state', async () => {
  const res = await worker.fetch(req('/api/auth/google'), env, {});
  assert.equal(res.status, 302);
  const to = new URL(res.headers.get('Location'));
  assert.equal(to.origin + to.pathname, 'https://accounts.google.com/o/oauth2/v2/auth');
  assert.equal(to.searchParams.get('client_id'), 'test-client-id');
  assert.equal(to.searchParams.get('scope'), 'openid email');
  assert.ok(to.searchParams.get('state'), 'no state');
  assert.ok((res.headers.get('Set-Cookie') || '').startsWith('ga_oauth='),
            'no state cookie pinned');
});

/* Walks the real redirect, keeping the state cookie, like a browser would. */
async function signInWithGoogle(code = 'good-code', tamper = null) {
  const start = await worker.fetch(req('/api/auth/google'), env, {});
  const stateCookie = (start.headers.get('Set-Cookie') || '').split(';')[0];
  let state = new URL(start.headers.get('Location')).searchParams.get('state');
  if (tamper) state = tamper(state);
  return worker.fetch(req(`/api/auth/google/callback?code=${code}&state=${encodeURIComponent(state)}`,
                          { headers: { Cookie: stateCookie } }), env, {});
}

await it('a forged state is refused', async () => {
  const res = await signInWithGoogle('good-code', (s) => s.slice(0, -4) + 'AAAA');
  assert.equal(res.headers.get('Location'), '/?auth=expired');
  const cookies = res.headers.getSetCookie ? res.headers.getSetCookie() : [];
  assert.ok(!cookies.some(c => c.startsWith('ga_session=') && c.length > 20),
            'a forged state still issued a session');
});

await it('a state with no matching cookie is refused', async () => {
  const start = await worker.fetch(req('/api/auth/google'), env, {});
  const state = new URL(start.headers.get('Location')).searchParams.get('state');
  const res = await worker.fetch(
    req(`/api/auth/google/callback?code=good-code&state=${encodeURIComponent(state)}`), env, {});
  assert.equal(res.headers.get('Location'), '/?auth=expired');
});

await it('Google refusing the code grants nothing', async () => {
  const res = await signInWithGoogle('bad-code');
  assert.equal(res.headers.get('Location'), '/?auth=failed');
});

await it('an unverified Google address is refused', async () => {
  GOOGLE.verified = false;
  const res = await signInWithGoogle();
  GOOGLE.verified = true;
  assert.equal(res.headers.get('Location'), '/?auth=failed');
});

let gCookie = null;

await it('a real sign-in creates the account but does not pay for it', async () => {
  const res = await signInWithGoogle();
  assert.equal(res.status, 302);
  assert.equal(res.headers.get('Location'), '/?pay=1', 'unpaid user was let in');
  const all = res.headers.getSetCookie ? res.headers.getSetCookie() : [];
  gCookie = (all.find(c => c.startsWith('ga_session=')) || '').split(';')[0];
  assert.ok(gCookie, 'no session cookie');
  const u = db._tables.users.find(u => u.email === 'gmail.user@gmail.com');
  assert.ok(u, 'no account created');
  assert.equal(u.paid, 0, 'signing in marked them paid');
});

await it('signed in but unpaid still cannot reach the questions', async () => {
  assert.equal((await worker.fetch(req('/api/bundle', {
    headers: { Cookie: gCookie } }), env, {})).status, 402);
  const app = await worker.fetch(req('/app', { headers: { Cookie: gCookie } }), env, {});
  assert.equal(app.status, 302);
});

await it('/api/me reports signed in, not paid', async () => {
  const me = await (await worker.fetch(req('/api/me', {
    headers: { Cookie: gCookie } }), env, {})).json();
  assert.deepEqual(me, { signedIn: true, paid: false, verified: true, google: true,
                         email: 'gmail.user@gmail.com', name: '', role: 'user' });
});

await it('checkout refuses a stranger and points them at Google', async () => {
  const res = await worker.fetch(req('/api/checkout', { method: 'POST' }), env, {});
  assert.equal(res.status, 401);
  assert.equal((await res.json()).signin, '/api/auth/google');
});

await it('checkout for a signed-in user carries their account id', async () => {
  const res = await worker.fetch(req('/api/checkout', {
    method: 'POST', headers: { Cookie: gCookie } }), env, {});
  assert.equal(res.status, 200);
  assert.ok((await res.json()).url.startsWith('https://checkout.stripe.com/'));
  assert.ok(LAST_CHECKOUT.get('client_reference_id'), 'account id not sent to Stripe');
});

await it('the webhook pays the account the checkout was started from', async () => {
  const u = db._tables.users.find(u => u.email === 'gmail.user@gmail.com');
  const body = JSON.stringify({ id: 'evt_g1', type: 'checkout.session.completed',
    data: { object: { payment_status: 'paid', client_reference_id: u.id,
                      customer: 'cus_g',
                      /* deliberately a different address at the till */
                      customer_details: { email: 'someone.else@example.com' } } } });
  const res = await worker.fetch(req('/api/stripe-webhook', {
    method: 'POST', body, headers: await signedWebhook(env, body) }), env, {});
  assert.equal(res.status, 200);
  assert.equal(u.paid, 1, 'the signed-in account was not marked paid');
  const stray = db._tables.users.find(x => x.email === 'someone.else@example.com');
  assert.ok(!stray, 'a second account was created from the till address');
});

await it('and now they get in', async () => {
  const bundle = await worker.fetch(req('/api/bundle', {
    headers: { Cookie: gCookie } }), env, {});
  assert.equal(bundle.status, 200);
  assert.ok((await bundle.json()).banks.national.length > 100);
});


console.log('\nEMAIL AND PASSWORD');

const PW = 'a long enough passphrase';

await it('a short password is refused', async () => {
  const res = await worker.fetch(req('/api/auth/signup', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: 'pw@example.com', name: 'Test Person',
                           phone: '4045551234', password: 'tiny', password2: 'tiny',
                           terms: true }) }), env, {});
  assert.equal(res.status, 400);
  assert.ok((await res.json()).fields.password, 'the error did not name the field');
  assert.ok(!db._tables.users.find(u => u.email === 'pw@example.com'),
            'a rejected signup still made an account');
});

let pwCookie = null;

await it('signing up creates an account, signs you in, and pays for nothing', async () => {
  const res = await worker.fetch(req('/api/auth/signup', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: 'PW@Example.com ', name: 'Test Person',
                           phone: '(404) 555-1234', password: PW, password2: PW,
                           terms: true }) }), env, {});
  assert.equal(res.status, 200);
  assert.deepEqual(await res.json(), { ok: true, paid: false, verified: false });
  pwCookie = cookieOf(res);
  const u = db._tables.users.find(u => u.email === 'pw@example.com');
  assert.ok(u, 'no account');
  assert.equal(u.paid, 0, 'signing up marked them paid');
  assert.ok(u.password_hash.startsWith('pbkdf2$'), 'password not hashed');
  assert.ok(!u.password_hash.includes(PW), 'password stored in the clear');
});

await it('a signed-up user still cannot reach the questions', async () => {
  assert.equal((await worker.fetch(req('/api/bundle', {
    headers: { Cookie: pwCookie } }), env, {})).status, 402);
});

await it('signing up twice on the same address is refused', async () => {
  const res = await worker.fetch(req('/api/auth/signup', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: 'pw@example.com', name: 'Test Person',
                           phone: '4045551234', password: PW, password2: PW,
                           terms: true }) }), env, {});
  assert.equal(res.status, 409);
});

await it('the wrong password is refused and sets no cookie', async () => {
  const res = await worker.fetch(req('/api/auth/login', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: 'pw@example.com', password: 'not the one' }) }), env, {});
  assert.equal(res.status, 401);
  assert.equal(res.headers.get('Set-Cookie'), null);
});

await it('an unknown address answers exactly like a wrong password', async () => {
  const unknown = await worker.fetch(req('/api/auth/login', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: 'nobody-here@example.com', password: PW }) }), env, {});
  const wrong = await worker.fetch(req('/api/auth/login', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: 'pw@example.com', password: 'nope' }) }), env, {});
  assert.equal(unknown.status, wrong.status);
  assert.deepEqual(await unknown.json(), await wrong.json());
});

await it('guessing gets locked out', async () => {
  for (let i = 0; i < 8; i++) {
    await worker.fetch(req('/api/auth/login', {
      method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email: 'pw@example.com', password: 'guess' + i }) }), env, {});
  }
  const res = await worker.fetch(req('/api/auth/login', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: 'pw@example.com', password: PW }) }), env, {});
  assert.equal(res.status, 429, 'the right password still worked after 8 failures');
});

await it('the right password works once the lock is cleared', async () => {
  db._tables.auth_attempts = [];
  const res = await worker.fetch(req('/api/auth/login', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: 'pw@example.com', password: PW }) }), env, {});
  assert.equal(res.status, 200);
  assert.equal((await res.json()).verified, false, 'signing up must not self-verify');
  assert.ok(cookieOf(res).startsWith('ga_session='));
  assert.equal(db._tables.auth_attempts.length, 0, 'failures not cleared on success');
});

await it('a Google account can add a password and stay one account', async () => {
  const before = db._tables.users.length;
  const res = await worker.fetch(req('/api/auth/signup', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: 'gmail.user@gmail.com', name: 'Gmail Person',
                           phone: '4045559999', password: PW, password2: PW,
                           terms: true }) }), env, {});
  assert.equal(res.status, 200);
  assert.equal((await res.json()).paid, true, 'lost their paid status');
  assert.equal(db._tables.users.length, before, 'a duplicate account was made');
});


console.log('\nSIGN-UP FIELDS, VERIFICATION AND RESET');

const FULL = { name: 'Zamir Bracey', phone: '(404) 555-0182',
               password: 'a long enough passphrase', password2: 'a long enough passphrase',
               terms: true };

function signup(extra) {
  return worker.fetch(req('/api/auth/signup', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(Object.assign({}, FULL, extra)) }), env, {});
}

await it('every missing field is named, and named separately', async () => {
  const res = await worker.fetch(req('/api/auth/signup', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: 'nope', name: 'x', phone: '12',
                           password: 'short', password2: 'other', terms: false })
  }), env, {});
  assert.equal(res.status, 400);
  const f = (await res.json()).fields;
  for (const k of ['email', 'name', 'phone', 'password', 'terms']) {
    assert.ok(f[k], 'no message for ' + k);
  }
});

await it('mismatched passwords are caught on the second field', async () => {
  const res = await signup({ email: 'mismatch@example.com', password2: 'something else' });
  assert.equal(res.status, 400);
  assert.ok((await res.json()).fields.password2);
});

await it('the terms box is not optional', async () => {
  const res = await signup({ email: 'noterms@example.com', terms: false });
  assert.equal(res.status, 400);
  assert.ok((await res.json()).fields.terms);
});

let newCookie = null;

await it('a full sign-up stores name and a normalised phone', async () => {
  const res = await signup({ email: 'zamir@example.com' });
  assert.equal(res.status, 200);
  const body = await res.json();
  assert.equal(body.verified, false, 'a new account must not be self-verified');
  newCookie = cookieOf(res);
  const u = db._tables.users.find(u => u.email === 'zamir@example.com');
  assert.equal(u.name, 'Zamir Bracey');
  assert.equal(u.phone, '+14045550182', 'phone not normalised to E.164');
  assert.ok(u.terms_at, 'terms acceptance not recorded');
  assert.equal(u.email_verified, 0);
});

await it('the account endpoint returns the fields and never the password', async () => {
  const me = await (await worker.fetch(req('/api/account', {
    headers: { Cookie: newCookie } }), env, {})).json();
  assert.equal(me.name, 'Zamir Bracey');
  assert.equal(me.phone, '+14045550182');
  assert.equal(me.verified, false);
  assert.ok(!('password_hash' in me) && !JSON.stringify(me).includes('pbkdf2'),
            'the account endpoint leaked credential material');
});

await it('name and phone can be corrected, bad ones cannot', async () => {
  const bad = await worker.fetch(req('/api/account', {
    method: 'PUT', headers: { Cookie: newCookie, 'Content-Type': 'application/json' },
    body: JSON.stringify({ name: 'Z', phone: '123' }) }), env, {});
  assert.equal(bad.status, 400);
  const f = (await bad.json()).fields;
  assert.ok(f.name && f.phone);

  const ok = await worker.fetch(req('/api/account', {
    method: 'PUT', headers: { Cookie: newCookie, 'Content-Type': 'application/json' },
    body: JSON.stringify({ name: 'Zamir B', phone: '+1 404 555 0199' }) }), env, {});
  assert.equal(ok.status, 200);
  assert.equal(db._tables.users.find(u => u.email === 'zamir@example.com').phone,
               '+14045550199');
});

await it('a stranger cannot read anybody\u2019s account', async () => {
  assert.equal((await worker.fetch(req('/api/account'), env, {})).status, 401);
});

await it('the verification link proves the address, once', async () => {
  const u = db._tables.users.find(u => u.email === 'zamir@example.com');
  const raw = SENT.verifyToken;
  assert.ok(raw, 'no verification link was sent at sign-up');
  const res = await worker.fetch(req('/auth/verify?token=' + raw), env, {});
  assert.equal(res.status, 302);
  assert.equal(res.headers.get('Location'), '/auth?verify=ok');
  assert.equal(u.email_verified, 1);

  const again = await worker.fetch(req('/auth/verify?token=' + raw), env, {});
  assert.equal(again.headers.get('Location'), '/auth?verify=bad',
               'a verification link worked twice');
});

await it('a forged verification token does nothing', async () => {
  const res = await worker.fetch(req('/auth/verify?token=not-a-real-token'), env, {});
  assert.equal(res.headers.get('Location'), '/auth?verify=bad');
});

await it('forgot-password answers the same for a stranger and a customer', async () => {
  db._tables.sends = [];
  const known = await worker.fetch(req('/api/auth/forgot', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: 'zamir@example.com' }) }), env, {});
  db._tables.sends = [];
  const unknown = await worker.fetch(req('/api/auth/forgot', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: 'ghost@example.com' }) }), env, {});
  assert.equal(known.status, unknown.status);
  assert.deepEqual(await known.json(), await unknown.json());
});

await it('a reset sets the password and signs every old session out', async () => {
  db._tables.sends = [];
  await worker.fetch(req('/api/auth/forgot', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: 'zamir@example.com' }) }), env, {});
  const token = SENT.resetToken;
  assert.ok(token, 'no reset link was sent');
  const u2 = db._tables.users.find(u => u.email === 'zamir@example.com');
  const before = db._tables.sessions.filter(s => s.user_id === u2.id).length;
  assert.ok(before >= 1, 'no session to invalidate');

  const res = await worker.fetch(req('/api/auth/reset', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ token: token, password: 'a brand new passphrase',
                           password2: 'a brand new passphrase' }) }), env, {});
  assert.equal(res.status, 200);
  /* Exactly one session for them afterwards: the fresh one. A reset is often
     somebody shutting an intruder out, so the old ones must not survive. */
  assert.equal(db._tables.sessions.filter(s => s.user_id === u2.id).length, 1,
               'old sessions survived a reset');

  const relog = await worker.fetch(req('/api/auth/login', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: 'zamir@example.com', password: 'a brand new passphrase' })
  }), env, {});
  assert.equal(relog.status, 200, 'the new password does not work');
});

await it('a used reset token cannot be replayed', async () => {
  const res = await worker.fetch(req('/api/auth/reset', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ token: SENT.resetToken, password: 'yet another passphrase',
                           password2: 'yet another passphrase' }) }), env, {});
  assert.equal(res.status, 400);
});

await it('resend is rate limited rather than a free email cannon', async () => {
  db._tables.sends = [];
  const u = db._tables.users.find(u => u.email === 'pw@example.com');
  const { createSession } = await import('../src/auth.js');
  const { cookie } = await createSession(env, u.id);
  const c = cookie.split(';')[0];
  const first = await worker.fetch(req('/api/auth/resend', {
    method: 'POST', headers: { Cookie: c } }), env, {});
  assert.equal(first.status, 200);
  const second = await worker.fetch(req('/api/auth/resend', {
    method: 'POST', headers: { Cookie: c } }), env, {});
  assert.equal(second.status, 429, 'a second resend went straight out');
});


console.log('\nADMIN ROLE');

function signupAs(email, extra) {
  return worker.fetch(req('/api/auth/signup', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(Object.assign({
      email, name: 'A Person', phone: '4045550001',
      password: 'a long enough passphrase', password2: 'a long enough passphrase',
      terms: true }, extra || {})) }), env, {});
}

await it('an ordinary sign-up is an ordinary user', async () => {
  const res = await signupAs('ordinary@example.com');
  assert.equal(res.status, 200);
  const me = await (await worker.fetch(req('/api/me', {
    headers: { Cookie: cookieOf(res) } }), env, {})).json();
  assert.equal(me.role, 'user');
});

await it('asking to be an admin in the sign-up body does nothing', async () => {
  const res = await signupAs('sneaky@example.com', { role: 'admin', isAdmin: true });
  const me = await (await worker.fetch(req('/api/me', {
    headers: { Cookie: cookieOf(res) } }), env, {})).json();
  assert.equal(me.role, 'user', 'the client talked itself into being an admin');
  assert.equal(db._tables.users.find(u => u.email === 'sneaky@example.com').role, 'user');
});

await it('the configured address is an admin from the moment it signs up', async () => {
  const res = await signupAs('boss@example.com');
  const me = await (await worker.fetch(req('/api/me', {
    headers: { Cookie: cookieOf(res) } }), env, {})).json();
  assert.equal(me.role, 'admin');
});

await it('the list is matched without regard to case', async () => {
  const res = await signupAs('second.admin@example.com');
  const me = await (await worker.fetch(req('/api/me', {
    headers: { Cookie: cookieOf(res) } }), env, {})).json();
  assert.equal(me.role, 'admin');
});

await it('an existing account is promoted on its next sign-in', async () => {
  const u = db._tables.users.find(x => x.email === 'ordinary@example.com');
  assert.equal(u.role, 'user');
  env.ADMIN_EMAILS = 'boss@example.com, ordinary@example.com';
  const res = await worker.fetch(req('/api/auth/login', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: 'ordinary@example.com',
                           password: 'a long enough passphrase' }) }), env, {});
  assert.equal(res.status, 200);
  const me = await (await worker.fetch(req('/api/me', {
    headers: { Cookie: cookieOf(res) } }), env, {})).json();
  assert.equal(me.role, 'admin');
});

await it('and demoted again when taken off the list', async () => {
  env.ADMIN_EMAILS = 'boss@example.com';
  const res = await worker.fetch(req('/api/auth/login', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: 'ordinary@example.com',
                           password: 'a long enough passphrase' }) }), env, {});
  const me = await (await worker.fetch(req('/api/me', {
    headers: { Cookie: cookieOf(res) } }), env, {})).json();
  assert.equal(me.role, 'user');
});

await it('editing the cookie cannot make anybody an admin', async () => {
  const res = await signupAs('forger@example.com');
  const real = cookieOf(res);
  /* The role never travels in the cookie -- it is read from the row every
     time -- so the only thing a tampered cookie can do is stop working. */
  const forged = real.replace('ga_session=', 'ga_session=') + 'admin';
  const me = await (await worker.fetch(req('/api/me', {
    headers: { Cookie: forged } }), env, {})).json();
  assert.ok(!me.signedIn || me.role === 'user',
            'a tampered cookie produced an admin');
});

await it('no route hands out the role', async () => {
  /* Poke at every name an admin endpoint might plausibly have, as an
     ordinary signed-in user, and check that none of them changes what that
     user is. Matching on the response body is useless here -- the asset stub
     echoes the path, and "/api/admin" contains the word. What matters is the
     row afterwards. */
  const res = await signupAs('prodder@example.com');
  const c = cookieOf(res);
  const row = () => db._tables.users.find(u => u.email === 'prodder@example.com').role;
  assert.equal(row(), 'user');

  for (const path of ['/api/admin', '/api/role', '/api/users', '/api/promote',
                      '/api/account', '/api/me']) {
    for (const method of ['GET', 'POST', 'PUT']) {
      await worker.fetch(req(path, {
        method,
        headers: { Cookie: c, 'Content-Type': 'application/json' },
        body: method === 'GET' ? undefined
                               : JSON.stringify({ role: 'admin', isAdmin: true,
                                                  name: 'Still Ordinary',
                                                  phone: '4045550002' })
      }), env, {});
      assert.equal(row(), 'user', path + ' ' + method + ' changed the role');
    }
  }
});

globalThis.fetch = realFetch;
console.log(`\n${PASS} passed, ${FAIL} failed\n`);
process.exit(FAIL ? 1 : 0);
