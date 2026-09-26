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

## 5. Sign-in emails

Buyers land straight in the app after paying without needing email. They only
need a code when they come back on a different device, so this is required
before you sell to anyone.

Make a free account at <https://resend.com>, verify a domain you own (or use
their test sender to start), then:

```bash
wrangler secret put RESEND_API_KEY
```

Set `FROM_EMAIL` in `wrangler.toml` to an address on that verified domain.

## 6. Before you take real money

- [ ] Change `SUPPORT_EMAIL` in `tools/build_paid.py` — it is
      `support@example.com` right now and it is printed on your terms and
      privacy pages.
- [ ] Buy it yourself end to end in test mode: card `4242 4242 4242 4242`, any
      future expiry, any CVC. Check you land in the app, close the tab, and
      sign back in from a different browser.
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
| Sales page, 3 sample questions | ✅ | | |
| Terms, privacy | ✅ | | |
| The app at `/app` | | | ✅ |
| All 1,454 questions | | | ✅ |
| Study notes, 436 terms | | | ✅ |
| Your saved progress | | | ✅ |

`paid` is read from the database on every single request. It is never taken
from the cookie, the URL, or anything else the browser can edit.
