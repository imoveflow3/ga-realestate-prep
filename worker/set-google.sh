#!/usr/bin/env bash
# Put a Google OAuth client into local development, without the secret ever
# going through a chat window or a shell history file.
#
#   ./set-google.sh
#
# It writes .dev.vars, which is gitignored and read only by `wrangler dev`.
# For production the same two values go in as secrets instead:
#   wrangler secret put GOOGLE_CLIENT_ID
#   wrangler secret put GOOGLE_CLIENT_SECRET
set -euo pipefail
cd "$(dirname "$0")"

printf 'Client ID     : '
read -r CLIENT_ID
printf 'Client secret : '
read -rs CLIENT_SECRET          # -s: not echoed to the screen
echo

if [ -z "$CLIENT_ID" ] || [ -z "$CLIENT_SECRET" ]; then
  echo "Both values are needed. Nothing was written." >&2
  exit 1
fi
case "$CLIENT_ID" in
  *.apps.googleusercontent.com) ;;
  *) echo "That does not look like a Google client ID (it should end in" \
          ".apps.googleusercontent.com). Nothing was written." >&2; exit 1 ;;
esac

touch .dev.vars
# drop any previous pair, then append the new one
grep -v '^GOOGLE_CLIENT_ID=' .dev.vars | grep -v '^GOOGLE_CLIENT_SECRET=' > .dev.vars.tmp || true
mv .dev.vars.tmp .dev.vars
{
  echo "GOOGLE_CLIENT_ID=$CLIENT_ID"
  echo "GOOGLE_CLIENT_SECRET=$CLIENT_SECRET"
} >> .dev.vars
chmod 600 .dev.vars

echo
echo "Written to .dev.vars (gitignored, chmod 600)."
echo "Restart the dev server to pick it up:"
echo "    npx wrangler dev --port 8787 --local"
