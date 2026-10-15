/* Stripe: a weekly, monthly or yearly subscription, and a webhook we can trust.

   The client is never allowed to say "I paid". It says "start a checkout",
   and the only thing that flips `paid` to 1 is a webhook whose signature we
   have verified against the endpoint secret, or a Checkout Session we have
   fetched back from Stripe's own API. */

import { hmacHex, timingSafeEqual } from './crypto.js';
import { now } from './auth.js';

const API = 'https://api.stripe.com/v1';
const TOLERANCE_SECONDS = 300;

async function stripe(env, path, { method = 'GET', form } = {}) {
  const init = {
    method,
    headers: {
      Authorization: `Bearer ${env.STRIPE_SECRET_KEY}`,
      'Stripe-Version': '2024-06-20',
    },
  };
  if (form) {
    init.headers['Content-Type'] = 'application/x-www-form-urlencoded';
    init.body = new URLSearchParams(form).toString();
  }
  const res = await fetch(`${API}${path}`, init);
  const body = await res.json();
  if (!res.ok) {
    const msg = (body && body.error && body.error.message) || `Stripe ${res.status}`;
    throw new Error(msg);
  }
  return body;
}

/* The plans on sale. The prices shown on the payment page come from
   tools/build_paid.py PLANS -- keep the two in step. Prices are sent to
   Stripe inline, so there is nothing to set up in the Stripe dashboard. */
export const PLANS = {
  weekly:  { cents: 900,   interval: 'week',  name: 'Weekly' },
  monthly: { cents: 2400,  interval: 'month', name: 'Monthly' },
  yearly:  { cents: 14900, interval: 'year',  name: 'Yearly' },
};

/* Statuses that mean the subscription is being paid for. past_due keeps
   access while Stripe retries a failed card; anything else (canceled,
   unpaid, incomplete_expired, paused) does not. */
export function subscriptionActive(status) {
  return status === 'active' || status === 'trialing' || status === 'past_due';
}

export async function createCheckout(env, { email, origin, userId, plan }) {
  const p = PLANS[plan];
  if (!p) throw new Error('Unknown plan.');
  const product = env.PRODUCT_NAME || 'Real Estate Exam Prep';
  const form = {
    mode: 'subscription',
    'line_items[0][quantity]': '1',
    'line_items[0][price_data][currency]': 'usd',
    'line_items[0][price_data][unit_amount]': String(p.cents),
    'line_items[0][price_data][recurring][interval]': p.interval,
    'line_items[0][price_data][product_data][name]': `${product} \u2014 ${p.name}`,
    'metadata[plan]': plan,
    'subscription_data[metadata][plan]': plan,
    success_url: `${origin}/activate?session_id={CHECKOUT_SESSION_ID}`,
    cancel_url: `${origin}/auth?pay=1&checkout=cancelled`,
    allow_promotion_codes: 'true',
  };
  if (email) form.customer_email = email;
  // our own account id travels with the payment and comes back on the webhook
  if (userId) {
    form.client_reference_id = userId;
    form['subscription_data[metadata][user_id]'] = userId;
  }
  const session = await stripe(env, '/checkout/sessions', { method: 'POST', form });
  return session.url;
}

/* Stripe's own page for cancelling, switching plan or changing the card. */
export async function createPortal(env, { customer, origin }) {
  const session = await stripe(env, '/billing_portal/sessions', {
    method: 'POST', form: { customer, return_url: `${origin}/` } });
  return session.url;
}

export async function fetchCheckout(env, id) {
  return stripe(env, `/checkout/sessions/${encodeURIComponent(id)}`);
}

/* Stripe signs `${timestamp}.${raw body}`. The raw bytes matter -- reparsing
   and re-serialising the JSON would change them and every signature would
   fail. */
export async function verifyWebhook(env, rawBody, header) {
  if (!header) return { error: 'no signature' };
  let timestamp = null;
  const candidates = [];
  for (const part of header.split(',')) {
    const [k, v] = part.split('=');
    if (k === 't') timestamp = v;
    else if (k === 'v1') candidates.push(v);
  }
  if (!timestamp || !candidates.length) return { error: 'malformed signature' };
  if (Math.abs(now() - Number(timestamp)) > TOLERANCE_SECONDS) {
    return { error: 'signature too old' };
  }
  const expected = await hmacHex(env.STRIPE_WEBHOOK_SECRET, `${timestamp}.${rawBody}`);
  if (!candidates.some(c => timingSafeEqual(c, expected))) {
    return { error: 'signature mismatch' };
  }
  try {
    return { event: JSON.parse(rawBody) };
  } catch (e) {
    return { error: 'bad json' };
  }
}
