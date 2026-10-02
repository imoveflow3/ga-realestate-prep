-- Empty every account and everything hanging off one, leaving the schema
-- alone. Local development only: `npm run db:reset`.
--
-- Order matters. D1 does enforce the foreign keys: deleting a user that still
-- has a token or a session row fails with SQLITE_CONSTRAINT. Children first.
DELETE FROM progress;
DELETE FROM sessions;
DELETE FROM tokens;
DELETE FROM login_codes;
DELETE FROM auth_attempts;
DELETE FROM sends;
DELETE FROM stripe_events;
DELETE FROM users;
