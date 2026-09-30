-- Empty every account and everything hanging off one, leaving the schema
-- alone. Local development only: `npm run db:reset`.
--
-- Order matters only for readability here (D1 does not enforce the foreign
-- keys), but children first is the habit worth keeping.
DELETE FROM progress;
DELETE FROM sessions;
DELETE FROM tokens;
DELETE FROM login_codes;
DELETE FROM auth_attempts;
DELETE FROM sends;
DELETE FROM stripe_events;
DELETE FROM users;
