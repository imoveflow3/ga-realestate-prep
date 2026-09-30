/* Account fields, verification tokens, and the send limits that stop any of
   it being used as a free email cannon.

   Tokens are random, stored only as a hash, single use, and expiring. A
   leaked tokens table should be a list of useless strings. */

import { randomId, sha256hex, timingSafeEqual } from './crypto.js';
import { now } from './auth.js';

export const VERIFY_HOURS = 48;
export const RESET_MINUTES = 60;

/* Per-address, per-action: three in an hour, and one a minute. */
const SEND_MAX = 3;
const SEND_WINDOW = 3600;
const SEND_GAP = 60;

export async function maySend(env, email, action) {
  const key = `${action}:${email}`;
  const row = await env.DB.prepare(
    'SELECT count, window_from, last_at FROM sends WHERE key = ?').bind(key).first();
  const t = now();
  if (row) {
    if (t - row.last_at < SEND_GAP) {
      return { error: 'One was just sent. Give it a minute before asking again.' };
    }
    if (t - row.window_from < SEND_WINDOW && row.count >= SEND_MAX) {
      return { error: 'That has been requested a few times already. ' +
                      'Try again in an hour, or use Continue with Google.' };
    }
  }
  const fresh = !row || (t - row.window_from >= SEND_WINDOW);
  await env.DB.prepare(
    `INSERT INTO sends (key, count, window_from, last_at) VALUES (?, ?, ?, ?)
     ON CONFLICT(key) DO UPDATE SET count = excluded.count,
                                    window_from = excluded.window_from,
                                    last_at = excluded.last_at`
  ).bind(key, fresh ? 1 : row.count + 1, fresh ? t : row.window_from, t).run();
  return { ok: true };
}

export async function issueToken(env, userId, kind, minutes, payload) {
  const raw = randomId(32);
  const hash = await sha256hex(`${kind}:${raw}:${env.SESSION_SECRET}`);
  await env.DB.prepare('DELETE FROM tokens WHERE user_id = ? AND kind = ?')
    .bind(userId, kind).run();
  await env.DB.prepare(
    `INSERT INTO tokens (hash, user_id, kind, payload, expires_at, created_at)
     VALUES (?, ?, ?, ?, ?, ?)`
  ).bind(hash, userId, kind, payload || null, now() + minutes * 60, now()).run();
  return raw;
}

export async function useToken(env, kind, raw) {
  if (!raw) return { error: 'missing' };
  const hash = await sha256hex(`${kind}:${raw}:${env.SESSION_SECRET}`);
  const row = await env.DB.prepare(
    'SELECT user_id, payload, expires_at FROM tokens WHERE hash = ? AND kind = ?'
  ).bind(hash, kind).first();
  if (!row) return { error: 'That link is not valid.' };
  await env.DB.prepare('DELETE FROM tokens WHERE hash = ?').bind(hash).run();
  if (row.expires_at < now()) return { error: 'That link has expired.' };
  return { userId: row.user_id, payload: row.payload };
}

/* ------------------------------------------------------------- fields ---- */

export function cleanName(raw) {
  const n = String(raw || '').replace(/\s+/g, ' ').trim();
  if (n.length < 2) return { error: 'Put in your full name.' };
  if (n.length > 80) return { error: 'That name is too long.' };
  return { value: n };
}

/* Stored as digits with a leading +, so the same number typed three ways is
   the same number. Display formatting is the interface's problem. */
export function cleanPhone(raw, required) {
  const s = String(raw || '').trim();
  if (!s) {
    return required ? { error: 'Put in a mobile number.' } : { value: null };
  }
  const digits = s.replace(/[^\d+]/g, '');
  const plus = digits.startsWith('+');
  const bare = digits.replace(/\D/g, '');
  if (bare.length === 10 && !plus) return { value: '+1' + bare };   // US default
  if (bare.length === 11 && bare.startsWith('1')) return { value: '+' + bare };
  if (plus && bare.length >= 8 && bare.length <= 15) return { value: '+' + bare };
  return { error: 'That does not look like a mobile number. ' +
                  'US numbers are ten digits.' };
}
