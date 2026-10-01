# Turning this on

Four accounts, about half an hour. Two of them I cannot create for you: they
want your legal name, tax details and a bank account.

Until step 6 you are in Stripe **test mode**, so nothing is real money and you
can pay yourself with `4242 4242 4242 4242`.

---

## 1. Cloudflare (hosting + database)

```bash
npm install -g wrangler
wrangler login
```

```bash
cd worker
wrangler d1 create ga-prep
```

It prints a `database_id`. Paste it into `wrangler.toml`, replacing
`PASTE_YOUR_DATABASE_ID_HERE`. Then create the tables:

```bash
npm run db:init
```

## 2. Stripe (taking the money)

Make an account at <https://dashboard.stripe.com/register>. You will need your
legal name, address, tax ID and a bank account — this is the part I cannot do
for you, and Stripe will not let anyone else do it either.

Leave the **Test mode** toggle ON for now. From Developers → API keys, copy the
**secret** key (starts `sk_test_`), then:

```bash
wrangler secret put STRIPE_SECRET_KEY
wrangler secret put SESSION_SECRET      # paste any long random string
```

For `SESSION_SECRET`, generate one and keep it safe — changing it later signs
everybody out:

```bash
node -e "console.log(require('crypto').randomBytes(32).toString('base64url'))"
```

## 3. First deploy

```bash
npm run deploy
```

It prints your URL, something like `https://ga-prep.<you>.workers.dev`. Put
that into `wrangler.toml` as `SITE_URL`, and deploy once more so Stripe gets
sent back to the right place.

## 4. The webhook

This is what actually flips someone to "paid". In Stripe → Developers →
Webhooks → Add endpoint:

- **URL**: `https://YOUR-URL/api/stripe-webhook`
- **Event**: `checkout.session.completed`

Copy the signing secret it shows (`whsec_…`) and:

```bash
wrangler secret put STRIPE_WEBHOOK_SECRET
npm run deploy
```

## 5. Google sign-in

This is how people get in, so it has to be set up before you sell anything.

At <https://console.cloud.google.com/apis/credentials>: create a project, then
**Create credentials -> OAuth client ID -> Web application**.

- **Authorised JavaScript origin**: `https://YOUR-URL`
- **Authorised redirect URI**: `https://YOUR-URL/api/auth/google/callback`

You will also be asked to fill in the OAuth consent screen: app name, your
support email, and links to `/privacy` and `/terms` (both already exist on
your site). While the app is in *Testing* only addresses you list can sign in,
which is what you want until you have bought it yourself. Publishing it opens
it to everyone; for `openid email` scopes only, Google does not require a
review.

Then:

```bash
wrangler secret put GOOGLE_CLIENT_ID
wrangler secret put GOOGLE_CLIENT_SECRET
npm run deploy
```

### A note on passwords and the free plan

Email-and-password sign-in hashes with PBKDF2 at 100,000 iterations, which is
the point of it -- a stolen database should not hand out logins. That costs
real CPU, and Cloudflare's free plan allows about 10ms per request, which this
will exceed. Signing up or logging in with a password may fail there.

Three ways out, in the order I would pick them:

1. Leave it. Google sign-in has no such cost and is the button most people
   press anyway; the password form is the fallback.
2. Move to the Workers Paid plan ($5/month), which raises the CPU limit well
   past what this needs.
3. Lower `ITERATIONS` in `src/password.js`. This works and I would not do it:
   it makes every stored password cheaper to crack, forever, to save $5.

Google sign-in, the six-digit email code, and everything behind the paywall
are unaffected either way.

## 6. Sign-in emails (optional fallback)

Google sign-in covers the normal path. The six-digit email code is still
wired up as a fallback for anyone without a Google account; it is not shown on
the site by default, so this is optional.

Make a free account at <https://resend.com>, verify a domain you own (or use
their test sender to start), then:

```bash
wrangler secret put RESEND_API_KEY
```

Set `FROM_EMAIL` in `wrangler.toml` to an address on that verified domain.

## 7. Before you take real money

- [ ] Change `SUPPORT_EMAIL` in `tools/build_paid.py` — it is
      `support@example.com` right now and it is printed on your terms and
      privacy pages.
- [ ] Buy it yourself end to end in test mode: sign in with Google first,
      then card `4242 4242 4242 4242`, any future expiry, any CVC. Check you
      land in the app, close the tab, and sign back in from another browser.
- [ ] Read `/terms` and `/privacy` on your own site and make sure you agree
      with what they say, because they are now promises you have made.
- [ ] Turn off Stripe test mode, swap `STRIPE_SECRET_KEY` and
      `STRIPE_WEBHOOK_SECRET` for the live ones (`sk_live_…`, new `whsec_…`),
      and redeploy.
- [ ] Ask an accountant about sales tax. Several states treat access to a
      digital product as taxable, and Stripe Tax can handle it, but whether
      you owe it is not something I can tell you.

## Day to day

```bash
npm run build     # rebuild the sales page and the gated bundle
npm test          # 20 checks on the gate: forged cookies, unpaid access, replayed webhooks
npm run deploy    # build, test, ship
```

Anything that changes a question, a note or the styling means a rebuild and a
redeploy — the bundle is compiled into the Worker.

## Who can see what

| | Public | Needs an account | Needs to have paid |
|---|---|---|---|
| Sales page | ✅ | | |
| Terms, privacy | ✅ | | |
| The app at `/app` | | | ✅ |
| All 1,454 questions | | | ✅ |
| Study notes, 436 terms | | | ✅ |
| Your saved progress | | | ✅ |

`paid` is read from the database on every single request. It is never taken
from the cookie, the URL, or anything else the browser can edit.

---

# What the server needs

## Secrets (`wrangler secret put NAME`)

| Name | What it is | Without it |
|---|---|---|
| `SESSION_SECRET` | Any long random string. Signs session cookies and hashes tokens. | The Worker refuses every request. |
| `STRIPE_SECRET_KEY` | Stripe API key (`sk_test_…`, then `sk_live_…`). | Checkout returns 503. |
| `STRIPE_WEBHOOK_SECRET` | The endpoint's signing secret (`whsec_…`). | Payments never mark anyone paid. |
| `GOOGLE_CLIENT_ID` | OAuth client id. | Continue with Google shows "not set up". |
| `GOOGLE_CLIENT_SECRET` | OAuth client secret. | Same. |
| `RESEND_API_KEY` | Email provider key. | No verification, reset or sign-in emails. Unverified accounts are then **not** held at the gate, because there would be no way through it. |

Changing `SESSION_SECRET` signs everybody out and voids every outstanding
verification and reset link. Generate it once:

```bash
node -e "console.log(require('crypto').randomBytes(32).toString('base64url'))"
```

## Plain settings (`[vars]` in wrangler.toml)

`SITE_URL`, `FROM_EMAIL`, `PRICE_CENTS`, `PRODUCT_NAME`.

## Database

One D1 database bound as `DB`. `schema.sql` creates it all:

| Table | Holds |
|---|---|
| `users` | id, email, name, phone, password hash, `email_verified`, `terms_at`, `paid`, Stripe and Google ids |
| `sessions` | signed-in sessions, so one can be revoked |
| `progress` | the whole study record, one row per user |
| `tokens` | hashed, single-use, expiring links for verification and password reset |
| `sends` | how often an address has asked for an email, for rate limiting |
| `auth_attempts` | failed logins per address, for lockout |
| `login_codes` | six-digit sign-in codes, hashed |
| `stripe_events` | events already handled, so a replay cannot double-credit |

```bash
cd worker
wrangler d1 execute ga-prep --remote --file=./schema.sql
```

Re-running it is safe: every statement is `IF NOT EXISTS`. **Adding columns to
an existing database is not** — `CREATE TABLE IF NOT EXISTS` will skip a
`users` table that already exists and leave the new columns off. If you have
already created the database, run these once:

```sql
ALTER TABLE users ADD COLUMN name TEXT;
ALTER TABLE users ADD COLUMN phone TEXT;
ALTER TABLE users ADD COLUMN email_verified INTEGER NOT NULL DEFAULT 0;
ALTER TABLE users ADD COLUMN terms_at INTEGER;
```

## Administrators

`ADMIN_EMAILS` is a comma-separated list of addresses. An address on it is
given the `admin` role when its account is created, and again on every
sign-in, so adding somebody takes effect the next time they log in and
removing somebody takes effect the same way. Case does not matter.

```bash
cd worker && ./set-admin.sh you@gmail.com            # local
wrangler secret put ADMIN_EMAILS                      # production
```

There is deliberately no endpoint that grants the role. Editing the list is
the only way in, and the role is read from the database on every request --
never from the cookie, which the browser could edit. Tested: a sign-up body
asking for `role: admin` is ignored, a tampered cookie grants nothing, and
poking every plausible admin URL as an ordinary user leaves their row alone.

## What is stored, and what is not

Stored against the account: email, name, phone, when the terms were accepted,
whether the address is confirmed, and the whole study record — lessons read,
quiz results, accuracy, flags, bookmarks, preferences, streak.

Never stored: the password itself. Only a PBKDF2 hash with a per-account salt.
Never sent to the browser: hashes, tokens, or any other account's anything.
`/api/account` returns one user's own row and is refused without a session.
