#!/usr/bin/env bash
# Bring an existing database up to date with schema.sql.
#
#   ./migrate.sh            # the local development database
#   ./migrate.sh --remote   # the deployed one
#
# schema.sql is all CREATE TABLE IF NOT EXISTS, which is right for a fresh
# database and silently wrong for one that already has the table: the whole
# statement is skipped, so columns added later never appear. This looks at
# what is actually there and adds only what is missing.
set -euo pipefail
cd "$(dirname "$0")"

WHERE="--local"
[ "${1:-}" = "--remote" ] && WHERE="--remote"

# column name -> the definition to add it with. SQLite will not take a
# non-constant default on ADD COLUMN, so every one of these is constant.
COLUMNS="
name|TEXT
phone|TEXT
email_verified|INTEGER NOT NULL DEFAULT 0
terms_at|INTEGER
role|TEXT NOT NULL DEFAULT 'user'
google_sub|TEXT
password_hash|TEXT
stripe_id|TEXT
paid_at|INTEGER
"

HAVE=$(npx wrangler d1 execute ga-prep $WHERE --command "PRAGMA table_info(users);" --json 2>/dev/null \
       | python3 -c "import sys,json;print(' '.join(c['name'] for c in json.load(sys.stdin)[0]['results']))")

if [ -z "$HAVE" ]; then
  echo "No users table yet. Create the schema first:"
  echo "    npx wrangler d1 execute ga-prep $WHERE --file=./schema.sql"
  exit 1
fi

ADDED=0
echo "$COLUMNS" | while IFS='|' read -r COL DEF; do
  [ -z "$COL" ] && continue
  case " $HAVE " in
    *" $COL "*) ;;
    *)
      echo "  adding users.$COL"
      npx wrangler d1 execute ga-prep $WHERE \
        --command "ALTER TABLE users ADD COLUMN $COL $DEF;" >/dev/null 2>&1
      ADDED=$((ADDED+1))
      ;;
  esac
done

# the tables added after the first release are safe to re-run as-is
npx wrangler d1 execute ga-prep $WHERE --file=./schema.sql >/dev/null 2>&1

echo "Done. users now has:"
npx wrangler d1 execute ga-prep $WHERE --command "PRAGMA table_info(users);" --json 2>/dev/null \
  | python3 -c "import sys,json;print('  '+', '.join(c['name'] for c in json.load(sys.stdin)[0]['results']))"
