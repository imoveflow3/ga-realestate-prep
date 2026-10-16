#!/usr/bin/env bash
# Switch the site from Stripe test mode to real payments.
#
#   cd ~/ga-realestate-prep/worker && ./go-live.sh
#
# Before running: in Stripe, turn Test mode OFF, then
#   1. Developers -> API keys: copy the Secret key (sk_live_...)
#   2. Developers -> Webhooks -> Add destination, events:
#        checkout.session.completed, invoice.paid,
#        customer.subscription.updated, customer.subscription.deleted
#      URL: https://study.realestateexamprep.workers.dev/api/stripe-webhook
#      then copy its Signing secret (whsec_...)
#   3. Settings -> Billing -> Customer portal: Save/Activate (live)
set -euo pipefail
cd "$(dirname "$0")"

echo "This switches the site to REAL payments and clears test-mode data:"
echo "  - test purchases and test affiliate earnings are deleted"
echo "  - accounts marked paid by test cards go back to unpaid (owner access is kept)"
echo "Affiliate codes are kept; Stripe re-creates each one the first time it is used."
read -r -p "Type LIVE to continue: " ok
[ "$ok" = "LIVE" ] || { echo "Stopped. Nothing changed."; exit 1; }

echo
echo "Paste your LIVE secret key (sk_live_...) when asked:"
npx wrangler secret put STRIPE_SECRET_KEY
echo
echo "Paste your LIVE webhook signing secret (whsec_...) when asked:"
npx wrangler secret put STRIPE_WEBHOOK_SECRET

echo
echo "Clearing test-mode data..."
npx wrangler d1 execute ga-prep --remote --command "
  DELETE FROM referrals;
  DELETE FROM stripe_events;
  UPDATE users SET paid = 0, stripe_id = NULL, plan = NULL, paid_at = NULL
   WHERE role != 'admin';
  UPDATE affiliates SET promo_id = NULL;"

echo
npm run deploy
echo
echo "Done. Real payments are on. Make one small real purchase yourself to check,"
echo "then refund it from the Stripe dashboard."
