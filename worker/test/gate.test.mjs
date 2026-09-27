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
const SENT = { code: null, to: null };
const realFetch = globalThis.fetch;
globalThis.fetch = async (input, init = {}) => {
  const url = typeof input === 'string' ? input : input.url;
  if (url.startsWith('https://api.resend.com/')) {
    const body = JSON.parse(init.body);
    SENT.to = body.to[0];
    SENT.code = (body.text.match(/\b(\d{6})\b/) || [])[1] || null;
    return new Response('{"id":"stub"}', { status: 200 });
  }
  if (url.startsWith('https://api.stripe.com/v1/checkout/sessions/')) {
    return new Response(JSON.stringify({
      payment_status: 'paid', customer: 'cus_activate',
      customer_details: { email: 'activated@example.com' } }), { status: 200 });
  }
  if (url === 'https://api.stripe.com/v1/checkout/sessions') {
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
  assert.equal(res.headers.get('Location'), '/?gate=1');
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
  assert.deepEqual(me, { signedIn: false, paid: false });
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

await it('checkout hands back a Stripe URL and grants nothing by itself', async () => {
  const res = await worker.fetch(req('/api/checkout', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: 'new@example.com' }) }), env, {});
  assert.equal(res.status, 200);
  assert.ok((await res.json()).url.startsWith('https://checkout.stripe.com/'));
  const u = db._tables.users.find(u => u.email === 'new@example.com');
  assert.ok(!u || !u.paid, 'starting checkout granted access');
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

await it('the extensionless public pages resolve to real files', async () => {
  for (const [asked, file] of [['/', '/index.html'], ['/buy', '/buy.html'],
                               ['/terms', '/terms.html'], ['/privacy', '/privacy.html']]) {
    const res = await worker.fetch(req(asked), env, {});
    assert.equal(res.status, 200, asked + ' did not resolve');
    assert.equal(await res.text(), file, asked + ' served the wrong file');
  }
});

await it('an unknown path goes home rather than 404ing into nothing', async () => {
  const res = await worker.fetch(req('/nope'), env, {});
  assert.ok([200, 302].includes(res.status));
});

globalThis.fetch = realFetch;
console.log(`\n${PASS} passed, ${FAIL} failed\n`);
process.exit(FAIL ? 1 : 0);
