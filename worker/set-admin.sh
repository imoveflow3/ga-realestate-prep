#!/usr/bin/env bash
# Mark an address as an administrator for local development.
#
#   ./set-admin.sh you@gmail.com
#
# Writes ADMIN_EMAILS into .dev.vars. The role is applied the next time that
# address signs in, so run this, then sign in (or sign in again).
#
# In production the same value is a plain var, not a secret -- put it in
# wrangler.toml under [vars], or:
#   wrangler secret put ADMIN_EMAILS
set -euo pipefail
cd "$(dirname "$0")"

if [ $# -lt 1 ]; then
  echo "Usage: ./set-admin.sh you@example.com [another@example.com ...]" >&2
  exit 1
fi

LIST=$(printf '%s,' "$@" | sed 's/,$//')
touch .dev.vars
grep -v '^ADMIN_EMAILS=' .dev.vars > .dev.vars.tmp || true
mv .dev.vars.tmp .dev.vars
echo "ADMIN_EMAILS=$LIST" >> .dev.vars
chmod 600 .dev.vars

echo "Administrators: $LIST"
echo
echo "Restart the dev server, then sign in with that address:"
echo "    npx wrangler dev --port 8787 --local"
