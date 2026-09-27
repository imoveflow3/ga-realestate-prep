/* Sign in with Google.

   Authorization-code flow rather than the one-tap ID-token flow: the token
   comes back to us straight from Google's own endpoint over TLS, so there is
   no JWT signature to verify ourselves. Less code, and no hand-rolled RS256
   in the path that decides who gets in.

   The account is identified by the Google address, and identification happens
   BEFORE payment. That removes the mismatch you get when somebody pays with
   one address and signs in with another. */

import { randomId, sign, timingSafeEqual } from './crypto.js';
import { now } from './auth.js';

const AUTH_URL = 'https://accounts.google.com/o/oauth2/v2/auth';
const TOKEN_URL = 'https://oauth2.googleapis.com/token';
const STATE_COOKIE = 'ga_oauth';
const STATE_TTL = 600;                 // ten minutes to finish signing in

export function configured(env) {
  return !!(env.GOOGLE_CLIENT_ID && env.GOOGLE_CLIENT_SECRET);
}

function redirectUri(env, url) {
  return `${env.SITE_URL || url.origin}/api/auth/google/callback`;
}

/* The state is random, signed, and pinned to a cookie. Without it a third
   party could walk somebody through a login they did not start. */
export async function startUrl(env, url, next) {
  const nonce = randomId(18);
  const payload = `${nonce}.${now() + STATE_TTL}.${next || ''}`;
  const sig = await sign(env.SESSION_SECRET, payload);
  const state = `${payload}.${sig}`;

  const params = new URLSearchParams({
    client_id: env.GOOGLE_CLIENT_ID,
    redirect_uri: redirectUri(env, url),
    response_type: 'code',
    scope: 'openid email',
    state,
    prompt: 'select_account',
    access_type: 'online',
  });
  const cookie = [
    `${STATE_COOKIE}=${nonce}`, 'Path=/', 'HttpOnly', 'Secure',
    'SameSite=Lax', `Max-Age=${STATE_TTL}`,
  ].join('; ');
  return { url: `${AUTH_URL}?${params}`, cookie };
}

export function readStateCookie(request) {
  const raw = request.headers.get('Cookie') || '';
  for (const part of raw.split(/;\s*/)) {
    const eq = part.indexOf('=');
    if (eq > 0 && part.slice(0, eq) === STATE_COOKIE) return part.slice(eq + 1);
  }
  return null;
}

export function clearStateCookie() {
  return `${STATE_COOKIE}=; Path=/; HttpOnly; Secure; SameSite=Lax; Max-Age=0`;
}

export async function checkState(env, state, cookieNonce) {
  if (!state || !cookieNonce) return { error: 'missing state' };
  const parts = state.split('.');
  if (parts.length < 4) return { error: 'malformed state' };
  const sig = parts.pop();
  const payload = parts.join('.');
  const expected = await sign(env.SESSION_SECRET, payload);
  if (!timingSafeEqual(sig, expected)) return { error: 'bad state signature' };

  const [nonce, expires, next] = parts;
  if (!timingSafeEqual(nonce, cookieNonce)) return { error: 'state does not match' };
  if (Number(expires) < now()) return { error: 'sign-in took too long' };
  return { next: next || '' };
}

/* Google hands back an id_token: three base64url segments, the middle one
   the claims. We read it rather than verify it, because this response came
   from Google's token endpoint over TLS in a request we made. */
function claimsOf(idToken) {
  const parts = String(idToken || '').split('.');
  if (parts.length !== 3) return null;
  try {
    const pad = parts[1].replace(/-/g, '+').replace(/_/g, '/');
    return JSON.parse(atob(pad + '==='.slice((pad.length + 3) % 4)));
  } catch (e) {
    return null;
  }
}

export async function exchange(env, url, code) {
  const res = await fetch(TOKEN_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({
      code,
      client_id: env.GOOGLE_CLIENT_ID,
      client_secret: env.GOOGLE_CLIENT_SECRET,
      redirect_uri: redirectUri(env, url),
      grant_type: 'authorization_code',
    }).toString(),
  });
  const body = await res.json();
  if (!res.ok) return { error: body.error_description || body.error || 'token exchange failed' };

  const claims = claimsOf(body.id_token);
  if (!claims || !claims.email) return { error: 'no email came back from Google' };
  if (claims.email_verified === false) {
    return { error: 'that Google account has an unverified email address' };
  }
  if (claims.aud !== env.GOOGLE_CLIENT_ID) return { error: 'token was not issued for this app' };
  return { email: String(claims.email).trim().toLowerCase(), sub: claims.sub };
}
