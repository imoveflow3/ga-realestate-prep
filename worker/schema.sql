-- One row per buyer. `paid` is set by the Stripe webhook, never by the client.
CREATE TABLE IF NOT EXISTS users (
  id          TEXT PRIMARY KEY,
  email       TEXT NOT NULL UNIQUE,
  paid        INTEGER NOT NULL DEFAULT 0,
  stripe_id     TEXT,
  google_sub    TEXT,
  password_hash TEXT,
  name          TEXT,
  phone         TEXT,
  email_verified INTEGER NOT NULL DEFAULT 0,
  terms_at      INTEGER,
  created_at  INTEGER NOT NULL,
  paid_at     INTEGER
);

-- Signed cookies carry the session id; this table lets us revoke one.
CREATE TABLE IF NOT EXISTS sessions (
  id          TEXT PRIMARY KEY,
  user_id     TEXT NOT NULL,
  created_at  INTEGER NOT NULL,
  expires_at  INTEGER NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(id)
);
CREATE INDEX IF NOT EXISTS sessions_user ON sessions(user_id);

-- Six-digit sign-in codes. Hashed, single use, short lived, rate limited.
CREATE TABLE IF NOT EXISTS login_codes (
  email       TEXT PRIMARY KEY,
  code_hash   TEXT NOT NULL,
  expires_at  INTEGER NOT NULL,
  attempts    INTEGER NOT NULL DEFAULT 0,
  sent_at     INTEGER NOT NULL
);

-- The whole progress record, as the app already stores it, one row per user.
CREATE TABLE IF NOT EXISTS progress (
  user_id     TEXT PRIMARY KEY,
  data        TEXT NOT NULL,
  updated_at  INTEGER NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Every payment we have seen, so a replayed webhook cannot double-credit.
CREATE TABLE IF NOT EXISTS stripe_events (
  id          TEXT PRIMARY KEY,
  seen_at     INTEGER NOT NULL
);

-- Failed sign-in attempts per address, so a password cannot be guessed at
-- speed. Cleared on success.
CREATE TABLE IF NOT EXISTS auth_attempts (
  email       TEXT PRIMARY KEY,
  fails       INTEGER NOT NULL DEFAULT 0,
  locked_till INTEGER NOT NULL DEFAULT 0
);

-- Single-use, hashed, expiring tokens. `kind` is 'verify' for proving an
-- address, 'reset' for setting a new password, 'change' for moving an account
-- to a new address. Hashed because a leaked table must not be a set of keys.
CREATE TABLE IF NOT EXISTS tokens (
  hash        TEXT PRIMARY KEY,
  user_id     TEXT NOT NULL,
  kind        TEXT NOT NULL,
  payload     TEXT,
  expires_at  INTEGER NOT NULL,
  created_at  INTEGER NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(id)
);
CREATE INDEX IF NOT EXISTS tokens_user ON tokens(user_id, kind);

-- How often an address has asked for a verification email, a reset, or an
-- SMS code. One row per address per action.
CREATE TABLE IF NOT EXISTS sends (
  key         TEXT PRIMARY KEY,
  count       INTEGER NOT NULL DEFAULT 0,
  window_from INTEGER NOT NULL,
  last_at     INTEGER NOT NULL
);
