/* Stripe: one $19 charge, and a webhook we can trust.

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

export async function createCheckout(env, { email, origin, userId }) {
  const form = {
    mode: 'payment',
    'line_items[0][quantity]': '1',
    'line_items[0][price_data][currency]': 'usd',
    'line_items[0][price_data][unit_amount]': String(env.PRICE_CENTS || '1900'),
    'line_items[0][price_data][product_data][name]':
      env.PRODUCT_NAME || 'Georgia Real Estate Exam Prep',
    'line_items[0][price_data][product_data][description]':
      'Lifetime access. One payment, no subscription.',
    success_url: `${origin}/activate?session_id={CHECKOUT_SESSION_ID}`,
    cancel_url: `${origin}/?checkout=cancelled`,
    allow_promotion_codes: 'true',
  };
  if (email) form.customer_email = email;
  // our own account id travels with the payment and comes back on the webhook
  if (userId) form.client_reference_id = userId;
  const session = await stripe(env, '/checkout/sessions', { method: 'POST', form });
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
