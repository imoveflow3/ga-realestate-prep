#!/usr/bin/env bash
# Put a Google OAuth client into local development, without the secret ever
# going through a chat window or a shell history file.
#
#   ./set-google.sh                       -- type the two values in
#   ./set-google.sh ~/Downloads/client_secret_*.json   -- read them from the
#                                            file Google lets you download
#
# It writes .dev.vars, which is gitignored and read only by `wrangler dev`.
# For production the same two values go in as secrets instead:
#   wrangler secret put GOOGLE_CLIENT_ID
#   wrangler secret put GOOGLE_CLIENT_SECRET
set -euo pipefail
cd "$(dirname "$0")"

# Two ways in. Either hand it the JSON Google lets you download from the
# client page -- which is easier and avoids a paste that silently fails --
# or answer the two prompts.
if [ $# -ge 1 ]; then
  SRC="$1"
  if [ ! -f "$SRC" ]; then
    echo "No such file: $SRC" >&2
    exit 1
  fi
  CLIENT_ID=$(python3 -c "
import json,sys
d=json.load(open(sys.argv[1]))
d=d.get('web') or d.get('installed') or d
print(d.get('client_id',''))
" "$SRC")
  CLIENT_SECRET=$(python3 -c "
import json,sys
d=json.load(open(sys.argv[1]))
d=d.get('web') or d.get('installed') or d
print(d.get('client_secret',''))
" "$SRC")
  if [ -z "$CLIENT_SECRET" ]; then
    echo "That file has no client_secret in it. If the client type is not" >&2
    echo "'Web application', Google does not issue one -- create a Web" >&2
    echo "application client instead." >&2
    exit 1
  fi
  echo "Read the client from $(basename "$SRC")."
else
  printf 'Client ID     : '
  read -r CLIENT_ID
  printf 'Client secret : '
  read -rs CLIENT_SECRET        # -s: not echoed to the screen
  echo
fi

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
