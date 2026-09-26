#!/usr/bin/env python3
"""Bundle the whole app into one self-contained HTML page.

Run:  python3 tools/build_online.py
Writes online/ga-real-estate.html -- no server, no network, one file.

Math generators are pre-rolled here rather than ported to JavaScript, so the
online problems are produced by exactly the same Python that the local app
uses. Progress lives in the browser's localStorage instead of data/progress.json.
"""
import datetime
import io
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)

from greprep import mathgen, questions, topics          # noqa: E402

ONLINE = os.path.join(HERE, "online")
OUT = os.path.join(ONLINE, "ga-real-estate.html")      # fragment, for the Artifact host
DOCS = os.path.join(HERE, "docs")                      # GitHub Pages serves from here
OUT_STANDALONE = os.path.join(DOCS, "index.html")      # full document, for any static host

SITE = "https://imoveflow3.github.io/ga-realestate-prep/"
TITLE = "Georgia Real Estate Exam Prep \u2014 free salesperson practice tests"
BLURB = ("Free practice for the Georgia real estate salesperson licensing exam. "
         "%(q)d exam-style questions scored National and Georgia separately, "
         "real estate math worked step by step, study notes with %(v)d defined "
         "terms, and a study plan built around your test date. No signup, "
         "works offline.")

ASSETS = "assets/"                      # icons and the link-preview card


def head(questions, terms):
    """The <head> for the standalone build: findable, shareable, installable."""
    blurb = BLURB % {"q": questions, "v": terms}
    return """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="color-scheme" content="light dark">
<title>%(title)s</title>
<meta name="description" content="%(blurb)s">
<link rel="canonical" href="%(site)s">
<meta name="theme-color" content="#1a6459" media="(prefers-color-scheme:light)">
<meta name="theme-color" content="#0e1319" media="(prefers-color-scheme:dark)">

<meta property="og:type" content="website">
<meta property="og:site_name" content="Georgia Real Estate Exam Prep">
<meta property="og:title" content="Pass the Georgia salesperson exam. Free.">
<meta property="og:description" content="%(blurb)s">
<meta property="og:url" content="%(site)s">
<meta property="og:image" content="%(site)s%(a)scard.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Georgia Real Estate Exam Prep">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Pass the Georgia salesperson exam. Free.">
<meta name="twitter:description" content="%(blurb)s">
<meta name="twitter:image" content="%(site)s%(a)scard.png">

<link rel="icon" href="%(a)sicon-192.png" sizes="192x192">
<link rel="icon" href="%(a)sicon-512.png" sizes="512x512">
<link rel="apple-touch-icon" href="%(a)sicon-180.png">
<link rel="manifest" href="manifest.webmanifest">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="GA Prep">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">

<script type="application/ld+json">%(jsonld)s</script>
""" % {"title": TITLE, "blurb": blurb, "site": SITE, "a": ASSETS,
       "jsonld": json.dumps({
           "@context": "https://schema.org",
           "@type": "LearningResource",
           "name": "Georgia Real Estate Exam Prep",
           "description": blurb,
           "url": SITE,
           "inLanguage": "en-US",
           "isAccessibleForFree": True,
           "learningResourceType": "Practice test",
           "educationalLevel": "Professional licensing",
           "teaches": "Georgia real estate salesperson licensing exam",
           "about": {"@type": "Thing",
                     "name": "Georgia real estate salesperson licence"},
           "offers": {"@type": "Offer", "price": "0",
                      "priceCurrency": "USD"},
       }, separators=(",", ":"))}


MANIFEST = {
    "name": "Georgia Real Estate Exam Prep",
    "short_name": "GA Prep",
    "description": ("Free practice tests, math and study notes for the Georgia "
                    "real estate salesperson licensing exam."),
    "start_url": ".",
    "scope": ".",
    "display": "standalone",
    "orientation": "portrait-primary",
    "background_color": "#0e1319",
    "theme_color": "#1a6459",
    "categories": ["education", "books"],
    "icons": [
        {"src": ASSETS + "icon-192.png", "sizes": "192x192", "type": "image/png",
         "purpose": "any"},
        {"src": ASSETS + "icon-512.png", "sizes": "512x512", "type": "image/png",
         "purpose": "any"},
        {"src": ASSETS + "icon-512.png", "sizes": "512x512", "type": "image/png",
         "purpose": "maskable"},
    ],
}

# Network-first for the page itself so a new build reaches people the next time
# they are online; cache-first for the icons, which never change under a name.
# Anything stale is dropped on activate, so the app can never pin itself to an
# old version -- the failure mode that makes offline caching worse than none.
SW = """/* Generated by tools/build_online.py -- do not edit docs/sw.js by hand. */
var CACHE = 'ga-prep-%(version)s';
var SHELL = ['./', './index.html', './manifest.webmanifest',
             './assets/icon-192.png', './assets/icon-512.png', './assets/icon-180.png'];

self.addEventListener('install', function(e){
  self.skipWaiting();
  e.waitUntil(caches.open(CACHE).then(function(c){
    return Promise.all(SHELL.map(function(u){
      return c.add(new Request(u, {cache: 'reload'}))['catch'](function(){});
    }));
  }));
});

self.addEventListener('activate', function(e){
  e.waitUntil(caches.keys().then(function(keys){
    return Promise.all(keys.map(function(k){
      return k === CACHE ? null : caches['delete'](k);
    }));
  }).then(function(){ return self.clients.claim(); }));
});

self.addEventListener('fetch', function(e){
  var req = e.request;
  if (req.method !== 'GET') return;
  var url = new URL(req.url);
  if (url.origin !== self.location.origin) return;

  if (req.mode === 'navigate' || (req.headers.get('accept') || '').indexOf('text/html') > -1){
    e.respondWith(
      fetch(req).then(function(res){
        var copy = res.clone();
        caches.open(CACHE).then(function(c){ c.put('./index.html', copy); });
        return res;
      })['catch'](function(){
        return caches.match('./index.html').then(function(hit){
          return hit || caches.match('./');
        });
      }));
    return;
  }
  e.respondWith(caches.match(req).then(function(hit){
    return hit || fetch(req).then(function(res){
      if (res && res.status === 200){
        var copy = res.clone();
        caches.open(CACHE).then(function(c){ c.put(req, copy); });
      }
      return res;
    });
  }));
});
"""

ROBOTS = """User-agent: *
Allow: /

Sitemap: %ssitemap.xml
""" % SITE

SITEMAP = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>%s</loc><lastmod>%s</lastmod><changefreq>monthly</changefreq>
    <priority>1.0</priority></url>
</urlset>
"""

VARIANTS = 70          # distinct pre-rolled problems per math generator


def roll(key, target):
    """Roll `target` distinct problems from one generator."""
    rnd = random.Random(abs(hash(key)) % (2 ** 32))
    state = random.getstate()
    random.setstate(rnd.getstate())
    seen, out = set(), []
    try:
        for _ in range(target * 30):
            if len(out) >= target:
                break
            q = mathgen.make(key)
            sig = q["q"] + "|" + "|".join(q["choices"])
            if sig in seen:
                continue
            seen.add(sig)
            out.append([q["q"], q["choices"], q["answer"], q["steps"]])
    finally:
        random.setstate(state)
    return out


def build_math():
    packed = {}
    for key in mathgen.ORDER:
        label, concept = mathgen.TOPICS[key]
        packed[key] = {"label": label, "concept": concept,
                       "closing": key in mathgen.CLOSING,
                       "q": roll(key, VARIANTS)}
    return packed


def default_profile():
    """What a brand-new visitor starts with: nothing.

    This used to carry the local app's own exam settings into the bundle, which
    was fine while one person used it and wrong the moment the page went
    public -- every visitor inherited somebody else's test date and a study
    plan counting down to it. The app asks for a date on first run instead.
    """
    return {}


def build_data():
    return {
        "profile_default": default_profile(),
        "portions": topics.PORTIONS,
        "topics": topics.catalog(),
        "banks": {"national": questions.bank("national"),
                  "georgia": questions.bank("georgia"),
                  "comprehensive": questions.bank("comprehensive")},
        "math": build_math(),
        "spq": 75,
        "exam": {"national": 80, "georgia": 52},
        "study": json.load(io.open(os.path.join(HERE, "greprep", "banks", "study.json"),
                                   encoding="utf-8")),
        "practice_only": sorted(topics.PRACTICE_ONLY),
        "difficulties": list(questions.DIFFICULTIES),
        "harder_share": questions.HARDER_SHARE,
    }


def read(name):
    with open(os.path.join(ONLINE, name)) as f:
        return f.read()


def write(path, text):
    with io.open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    if not os.path.isdir(DOCS):
        os.makedirs(DOCS)
    data = build_data()
    blob = json.dumps(data, separators=(",", ":"), ensure_ascii=False)
    # a closing script tag inside embedded JSON would end the <script> early
    blob = blob.replace("</", "<\\/")

    study_n = len(data["study"]["topics"])
    vocab_n = sum(len(t["vocab"]) for t in data["study"]["topics"].values())
    fixed_n = sum(len(v) for v in data["banks"].values())
    stamp = datetime.date.today().isoformat()

    html = (read("shell.html")
            .replace("__CSS__", read("style.css"))
            .replace("__DATA__", blob)
            .replace("__BUILD__", stamp)
            .replace("__ENGINE__", read("engine.js"))
            .replace("__UI__", read("ui.js")))
    with io.open(OUT, "w", encoding="utf-8") as f:
        f.write(html)

    # The Artifact host supplies <!doctype>/<head>/<body>; a plain web server does
    # not, so ship a second, fully standalone copy for GitHub Pages and friends.
    # everything before the first <header ...> is head content (title, links, styles)
    marker = "<header"
    if marker not in html:
        raise SystemExit("shell.html no longer starts its body with a <header> element")
    cut = html.index(marker)
    # the fragment carries its own <title> for the Artifact host; the standalone
    # head already has the long, searchable one, and two titles is one too many
    shell_head = html[:cut].replace(
        "<title>Georgia Real Estate Prep</title>\n", "", 1)
    standalone = (head(fixed_n, vocab_n) + shell_head +
                  "</head>\n<body>\n" + html[cut:] + "\n</body>\n</html>\n")
    write(OUT_STANDALONE, standalone)

    assets = os.path.join(DOCS, "assets")
    for name in ("icon-192.png", "icon-512.png", "icon-180.png", "card.png"):
        if not os.path.exists(os.path.join(assets, name)):
            raise SystemExit("missing docs/assets/%s -- run tools/make_icons.py" % name)
    write(os.path.join(DOCS, "manifest.webmanifest"),
          json.dumps(MANIFEST, indent=2) + "\n")
    write(os.path.join(DOCS, "sw.js"), SW % {"version": stamp})
    write(os.path.join(DOCS, "robots.txt"), ROBOTS)
    write(os.path.join(DOCS, "sitemap.xml"), SITEMAP % (SITE, stamp))

    math_n = sum(len(v["q"]) for v in data["math"].values())
    hard_n = sum(1 for rows in data["banks"].values() for r in rows
                 if r.get("difficulty", 1) == 2)
    exam_n = sum(1 for rows in data["banks"].values() for r in rows
                 if r.get("difficulty", 1) == 3)
    print("wrote %s" % os.path.relpath(OUT, HERE))
    print("wrote %s  (%.2f MB standalone)"
          % (os.path.relpath(OUT_STANDALONE, HERE),
             os.path.getsize(OUT_STANDALONE) / 1e6))
    print("wrote manifest.webmanifest, sw.js, robots.txt, sitemap.xml  (build %s)"
          % stamp)
    print("  %.2f MB  |  %d written (%d hard, %d exam) + %d pre-rolled math = %d questions"
          % (os.path.getsize(OUT) / 1e6, fixed_n, hard_n, exam_n, math_n,
             fixed_n + math_n))
    print("  study notes: %d topics, %d vocab terms" % (study_n, vocab_n))


if __name__ == "__main__":
    main()
