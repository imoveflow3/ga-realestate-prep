#!/usr/bin/env python3
"""Replace the free GitHub Pages app with a pointer to the paid site.

Run this ONLY after the Worker is live and you have bought your own product
end to end. Until then the free site is the only working thing you have, and
taking it down early leaves you with nothing.

    python3 tools/retire_free_site.py https://ga-prep.you.workers.dev

It rewrites docs/index.html as a short page that explains where the app went
and links to it, and deletes the question bank from everything public. The
git history still contains it -- if that matters, make the repo private.
"""
import datetime
import io
import os
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(HERE, "docs")

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>Georgia Real Estate Exam Prep</title>
<meta name="description" content="Practice tests, worked real estate math and
study notes for the Georgia salesperson licensing exam.">
<link rel="canonical" href="%(url)s">
<meta http-equiv="refresh" content="3;url=%(url)s">
<link rel="icon" href="assets/icon-192.png" sizes="192x192">
<style>
:root{color-scheme:light dark;--bg:#eef1f6;--panel:#fff;--ink:#0e1720;
  --ink-2:#48596c;--accent:#0d7365;--line:#e1e8ef}
@media (prefers-color-scheme:dark){:root{--bg:#0a0e14;--panel:#141b24;
  --ink:#e7edf4;--ink-2:#a7b5c6;--accent:#4fd1b8;--line:#242f3c}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);min-height:100vh;
  display:grid;place-items:center;padding:1.5rem;
  font:17px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
.box{background:var(--panel);border:1px solid var(--line);border-radius:14px;
  padding:2.5rem 2rem;max-width:34rem;box-shadow:0 12px 40px -12px rgba(0,0,0,.2)}
h1{margin:0 0 .6rem;font-size:1.9rem;line-height:1.15;letter-spacing:-.02em}
p{margin:0 0 1rem;color:var(--ink-2)}
a.go{display:inline-block;background:var(--accent);color:var(--bg);
  text-decoration:none;font-weight:600;padding:.75rem 1.4rem;border-radius:10px}
small{color:var(--ink-2);opacity:.8;font-size:.85rem}
</style>
</head>
<body>
<div class="box">
  <h1>This has moved.</h1>
  <p>The Georgia salesperson exam prep app now lives at its own address, with
     accounts so your progress follows you between devices.</p>
  <p><a class="go" href="%(url)s">Go to the app</a></p>
  <p><small>Taking you there automatically in a moment. Updated %(date)s.</small></p>
</div>
</body>
</html>
"""


def main():
    if len(sys.argv) != 2 or not sys.argv[1].startswith("http"):
        raise SystemExit("usage: python3 tools/retire_free_site.py https://your-worker-url")
    url = sys.argv[1].rstrip("/")
    page = PAGE % {"url": url, "date": datetime.date.today().isoformat()}

    target = os.path.join(DOCS, "index.html")
    before = os.path.getsize(target) if os.path.exists(target) else 0
    with io.open(target, "w", encoding="utf-8") as f:
        f.write(page)

    # the offline cache would happily keep serving the old app forever
    for name in ("sw.js", "manifest.webmanifest"):
        p = os.path.join(DOCS, name)
        if os.path.exists(p):
            os.remove(p)

    with io.open(os.path.join(DOCS, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % url)

    print("docs/index.html  %.2f MB -> %.2f KB" % (before / 1e6, len(page) / 1e3))
    print("removed docs/sw.js and docs/manifest.webmanifest")
    print("\nNow:  git add -A && git commit -m 'Point the old address at the app'"
          " && git push")
    print("Note: the question bank is still in this repo's git history. If that"
          "\n      matters, make the repository private on GitHub.")


if __name__ == "__main__":
    main()
