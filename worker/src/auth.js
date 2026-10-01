/* Sessions, sign-in codes, and the one question that matters on every gated
   route: is this request from somebody who has actually paid?

   Paid status is read from the database on every request. It is never taken
   from the cookie, the client, or anything the browser can edit. */

import { sign, timingSafeEqual, sha256hex, randomId, randomCode } from './crypto.js';

const COOKIE = 'ga_session';
const SESSION_DAYS = 120;
const CODE_MINUTES = 15;
const CODE_MAX_ATTEMPTS = 6;
const CODE_RESEND_SECONDS = 60;

export const now = () => Math.floor(Date.now() / 1000);

export function cookieHeader(value, maxAge) {
  const bits = [
    `${COOKIE}=${value}`,
    'Path=/',
    'HttpOnly',
    'Secure',
    'SameSite=Lax',
    `Max-Age=${maxAge}`,
  ];
  return bits.join('; ');
}

export function readCookie(request) {
  const raw = request.headers.get('Cookie') || '';
  for (const part of raw.split(/;\s*/)) {
    const eq = part.indexOf('=');
    if (eq > 0 && part.slice(0, eq) === COOKIE) return part.slice(eq + 1);
  }
  return null;
}

export async function createSession(env, userId) {
  const id = randomId();
  const t = now();
  await env.DB.prepare(
    'INSERT INTO sessions (id, user_id, created_at, expires_at) VALUES (?, ?, ?, ?)'
  ).bind(id, userId, t, t + SESSION_DAYS * 86400).run();
  const sig = await sign(env.SESSION_SECRET, id);
  return { cookie: cookieHeader(`${id}.${sig}`, SESSION_DAYS * 86400), id };
}

/* Returns the user row, or null. Checks the signature first so a forged id
   never reaches the database. */
export async function currentUser(request, env) {
  const raw = readCookie(request);
  if (!raw) return null;
  const dot = raw.lastIndexOf('.');
  if (dot < 1) return null;
  const id = raw.slice(0, dot), sig = raw.slice(dot + 1);
  const expected = await sign(env.SESSION_SECRET, id);
  if (!timingSafeEqual(sig, expected)) return null;

  const row = await env.DB.prepare(
    `SELECT u.id, u.email, u.paid, u.email_verified, u.name, u.role, s.expires_at
       FROM sessions s JOIN users u ON u.id = s.user_id
      WHERE s.id = ?`
  ).bind(id).first();
  if (!row || row.expires_at < now()) return null;
  /* The role is read from the database on every request, never from the
     cookie. A cookie the browser holds is a cookie the browser can edit. */
  return { id: row.id, email: row.email, paid: !!row.paid,
           verified: !!row.email_verified, name: row.name || '',
           role: row.role === 'admin' ? 'admin' : 'user',
           isAdmin: row.role === 'admin', sessionId: id };
}

export async function endSession(env, sessionId) {
  if (sessionId) await env.DB.prepare('DELETE FROM sessions WHERE id = ?').bind(sessionId).run();
}

export function normalizeEmail(raw) {
  const e = String(raw || '').trim().toLowerCase();
  return /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(e) ? e : null;
}

export async function findOrCreateUser(env, email) {
  const found = await env.DB.prepare('SELECT id, email, paid FROM users WHERE email = ?')
    .bind(email).first();
  if (found) return { id: found.id, email: found.email, paid: !!found.paid };
  const id = randomId(16);
  await env.DB.prepare(
    'INSERT INTO users (id, email, paid, created_at) VALUES (?, ?, 0, ?)'
  ).bind(id, email, now()).run();
  return { id, email, paid: false };
}

/* Issues a code, or refuses if one was sent less than a minute ago. The code
   is stored hashed: a leaked database should not hand out logins. */
export async function issueLoginCode(env, email) {
  const existing = await env.DB.prepare(
    'SELECT sent_at FROM login_codes WHERE email = ?').bind(email).first();
  if (existing && now() - existing.sent_at < CODE_RESEND_SECONDS) {
    return { error: 'A code was just sent. Wait a minute before asking for another.' };
  }
  const code = randomCode();
  const hash = await sha256hex(`${email}:${code}:${env.SESSION_SECRET}`);
  await env.DB.prepare(
    `INSERT INTO login_codes (email, code_hash, expires_at, attempts, sent_at)
     VALUES (?, ?, ?, 0, ?)
     ON CONFLICT(email) DO UPDATE SET
       code_hash = excluded.code_hash, expires_at = excluded.expires_at,
       attempts = 0, sent_at = excluded.sent_at`
  ).bind(email, hash, now() + CODE_MINUTES * 60, now()).run();
  return { code };
}

export async function verifyLoginCode(env, email, code) {
  const row = await env.DB.prepare(
    'SELECT code_hash, expires_at, attempts FROM login_codes WHERE email = ?'
  ).bind(email).first();
  if (!row) return { error: 'Ask for a code first.' };
  if (row.expires_at < now()) return { error: 'That code has expired. Ask for a new one.' };
  if (row.attempts >= CODE_MAX_ATTEMPTS) {
    return { error: 'Too many tries. Ask for a new code.' };
  }
  const hash = await sha256hex(`${email}:${String(code).trim()}:${env.SESSION_SECRET}`);
  if (!timingSafeEqual(hash, row.code_hash)) {
    await env.DB.prepare('UPDATE login_codes SET attempts = attempts + 1 WHERE email = ?')
      .bind(email).run();
    return { error: 'That code is not right.' };
  }
  await env.DB.prepare('DELETE FROM login_codes WHERE email = ?').bind(email).run();
  return { ok: true };
}
