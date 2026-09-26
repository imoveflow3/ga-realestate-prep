/* HMAC helpers. Everything the gate depends on is signed or hashed here. */

const enc = new TextEncoder();

async function hmacKey(secret) {
  return crypto.subtle.importKey(
    'raw', enc.encode(secret), { name: 'HMAC', hash: 'SHA-256' }, false,
    ['sign', 'verify']);
}

export function hex(buf) {
  return [...new Uint8Array(buf)].map(b => b.toString(16).padStart(2, '0')).join('');
}

export function b64url(buf) {
  let s = btoa(String.fromCharCode(...new Uint8Array(buf)));
  return s.replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
}

export async function sign(secret, message) {
  const key = await hmacKey(secret);
  return b64url(await crypto.subtle.sign('HMAC', key, enc.encode(message)));
}

/* Constant time: a byte-by-byte comparison here would leak the signature one
   character at a time to anyone willing to measure. */
export function timingSafeEqual(a, b) {
  if (typeof a !== 'string' || typeof b !== 'string' || a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i++) diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return diff === 0;
}

export async function hmacHex(secret, message) {
  const key = await hmacKey(secret);
  return hex(await crypto.subtle.sign('HMAC', key, enc.encode(message)));
}

export async function sha256hex(message) {
  return hex(await crypto.subtle.digest('SHA-256', enc.encode(message)));
}

export function randomId(bytes = 24) {
  return b64url(crypto.getRandomValues(new Uint8Array(bytes)));
}

/* Six digits, drawn from the CSPRNG rather than Math.random. */
export function randomCode() {
  const n = crypto.getRandomValues(new Uint32Array(1))[0] % 1000000;
  return String(n).padStart(6, '0');
}
