-- One row per buyer. `paid` is set by the Stripe webhook, never by the client.
CREATE TABLE IF NOT EXISTS users (
  id          TEXT PRIMARY KEY,
  email       TEXT NOT NULL UNIQUE,
  paid        INTEGER NOT NULL DEFAULT 0,
  stripe_id   TEXT,
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
