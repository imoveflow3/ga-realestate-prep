/* Email and password.

   PBKDF2-HMAC-SHA256 through WebCrypto, which is what a Worker has: no
   bcrypt, no scrypt, no Argon2. The iteration count is stored alongside the
   hash so it can be raised later without locking anyone out -- an old hash
   still verifies at the count it was made with, and is rewritten on the next
   successful login.

   Note this costs real CPU. On Cloudflare's free plan the per-request CPU
   budget is 10ms and 100k iterations will exceed it; Google sign-in has no
   such cost. See SETUP.md. */

import { b64url, timingSafeEqual } from './crypto.js';

const ITERATIONS = 100000;
const KEY_BITS = 256;
const SALT_BYTES = 16;
/* No minimum length, by choice. Empty is still refused -- a blank password
   is a form that did not get filled in, not a password somebody picked --
   and the upper bound stays so a single request cannot ask the worker to
   hash a megabyte. */
export const MIN_LENGTH = 0;

const enc = new TextEncoder();

async function derive(password, salt, iterations) {
  const key = await crypto.subtle.importKey(
    'raw', enc.encode(password), 'PBKDF2', false, ['deriveBits']);
  const bits = await crypto.subtle.deriveBits(
    { name: 'PBKDF2', salt, iterations, hash: 'SHA-256' }, key, KEY_BITS);
  return b64url(bits);
}

export async function hash(password) {
  const salt = crypto.getRandomValues(new Uint8Array(SALT_BYTES));
  const digest = await derive(password, salt, ITERATIONS);
  return `pbkdf2$${ITERATIONS}$${b64url(salt)}$${digest}`;
}

function parse(stored) {
  const parts = String(stored || '').split('$');
  if (parts.length !== 4 || parts[0] !== 'pbkdf2') return null;
  const iterations = Number(parts[1]);
  if (!Number.isFinite(iterations) || iterations < 1000) return null;
  const raw = parts[2].replace(/-/g, '+').replace(/_/g, '/');
  let salt;
  try {
    salt = Uint8Array.from(atob(raw + '==='.slice((raw.length + 3) % 4)),
                           c => c.charCodeAt(0));
  } catch (e) { return null; }
  return { iterations, salt, digest: parts[3] };
}

/* Always does the work, even when there is no account, so the time taken
   cannot be used to find out which addresses are registered. */
export async function verify(password, stored) {
  const parsed = parse(stored);
  const target = parsed || {
    iterations: ITERATIONS,
    salt: new Uint8Array(SALT_BYTES),
    digest: 'x'.repeat(43),
  };
  const digest = await derive(password, target.salt, target.iterations);
  const ok = timingSafeEqual(digest, target.digest);
  return { ok: !!parsed && ok, stale: !!parsed && parsed.iterations < ITERATIONS };
}

export function problemWith(password) {
  const p = String(password || '');
  if (!p.length) return 'Choose a password.';
  if (p.length > 200) return 'That is longer than 200 characters.';
  if (/^\s|\s$/.test(p)) return 'Remove the space at the start or end.';
  return null;
}
