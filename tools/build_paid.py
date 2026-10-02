#!/usr/bin/env python3
"""Build the paid site: a public sales page, and the app behind the gate.

Run:  python3 tools/build_paid.py

Writes
  worker/public/index.html    sales page  -- carries no question bank
  worker/public/terms.html    terms and refund policy
  worker/public/privacy.html  privacy policy
  worker/public/assets/*      icons and the link-preview card
  worker/assets/gated.js      {appHtml, data} -- imported by the Worker and
                              served only to a paid, signed-in session

The split is the whole point: nothing under public/ contains a question, an
answer key or an explanation. The Worker holds those and hands them out after
it has checked the session against the database.
"""
import datetime
import io
import json
import os
import shutil
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)

import tools.build_online as online                      # noqa: E402

ONLINE = os.path.join(HERE, "online")
WORKER = os.path.join(HERE, "worker")
PUBLIC = os.path.join(WORKER, "public")
GATED = os.path.join(WORKER, "assets")

from tools import siteconfig                             # noqa: E402

PRICE_CENTS = siteconfig.PRICE_CENTS
SUPPORT_EMAIL = siteconfig.support_email()
PAID_SITE = siteconfig.paid_site()
SAMPLE_COUNT = 0        # the sales page hands out nothing
LAYOUT = "minimal"      # "minimal" = sign up / sign in / pay only;
                        # "full" = the long welcome page

from tools._homecopy import (ICONS, FEATURES, AUDIENCE, WHY, STEPS,  # noqa: E402
                             HONEST)


# The markers that mean a question actually shipped. "steps" is deliberately
# not here: the how-it-works copy uses that key too, and a check that cries
# wolf is a check nobody reads.
LEAK_MARKERS = ('"choices"', '"answer":', '"explain":', '"concept":',
                '"vocab"', '"sections"', '"exam_questions"')


def assert_no_leak(path, label):
    """A public page may not contain a question, an answer or a note."""
    with io.open(path, encoding="utf-8") as f:
        text = f.read()
    found = [m for m in LEAK_MARKERS if m in text]
    if found:
        raise SystemExit("LEAK: %s (%s) contains %s"
                         % (label, os.path.relpath(path, HERE), ", ".join(found)))
    return len(text)


def read(name):
    with io.open(os.path.join(ONLINE, name), encoding="utf-8") as f:
        return f.read()


def write(path, text):
    with io.open(path, "w", encoding="utf-8") as f:
        f.write(text)


def build_app_html(css, data_free_shell):
    """The app, with the question bank cut out of it.

    engine.js and ui.js both run against a global DATA at load time, so they
    are parked inside __BOOT__ and only run once the bundle has arrived.
    """
    boot = (
        "<script>window.__SYNC__=true;window.__PAID__=true;"
        "window.__BOOT__=function(){\n"
        + read("engine.js") + "\n;\n" + read("ui.js") + "\n};</script>\n"
        "<script>(function(){\n"
        "  function fail(m){\n"
        "    document.body.innerHTML='<div style=\"max-width:32rem;margin:18vh auto;"
        "padding:0 1.5rem;font:16px/1.6 system-ui,sans-serif\">'+m+'</div>';\n"
        "  }\n"
        "  fetch('/api/bundle',{credentials:'same-origin'}).then(function(r){\n"
        "    if(r.status===402||r.status===401){location.href='/?gate=1';throw 0;}\n"
        "    if(!r.ok) throw new Error('bundle');\n"
        "    return r.json();\n"
        "  }).then(function(d){\n"
        "    window.DATA=d;\n"
        "    return fetch('/api/progress',{credentials:'same-origin'})\n"
        "      .then(function(r){return r.ok?r.json():null;})['catch'](function(){return null;});\n"
        "  }).then(function(p){\n"
        "    window.__SERVER_PROGRESS__=p;\n"
        "    window.__BOOT__();\n"
        "  })['catch'](function(e){\n"
        "    if(e!==0) fail('<h2>Could not load your questions.</h2>"
        "<p>Check your connection and refresh. If it keeps happening, "
        "<a href=\"/\">go back to the home page</a>.</p>');\n"
        "  });\n"
        "})();</script>\n")

    shell = (data_free_shell
             .replace("<script>const DATA=__DATA__;</script>\n", "")
             .replace("<script>__ENGINE__</script>\n", "")
             .replace("<script>__UI__</script>\n", boot)
             .replace("__CSS__", css))
    marker = "<header"
    cut = shell.index(marker)
    head = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width,initial-scale=1,'
            'viewport-fit=cover">\n<meta name="color-scheme" content="light dark">\n'
            '<meta name="robots" content="noindex">\n'
            '<link rel="icon" href="/assets/icon-192.png" sizes="192x192">\n'
            '<link rel="apple-touch-icon" href="/assets/icon-180.png">\n')
    return head + shell[:cut] + "</head>\n<body>\n" + shell[cut:] + "\n</body>\n</html>\n"


def ONLINE_HEAD(title, desc, canonical):
    return online.head(0, 0, site=PAID_SITE, title=title, blurb=desc,
                       canonical=canonical, price_cents=PRICE_CENTS,
                       manifest=None)


def legal_page(title, body, css, stamp, slug, desc):
    """A legal page is a public page: it gets a description, a canonical and
       an icon like every other one, not a bare <title>."""
    paras = "\n".join("<p>%s</p>" % p for p in body)
    full = "%s \u2014 Georgia Real Estate Exam Prep" % title
    return (ONLINE_HEAD(full, desc, PAID_SITE + slug) +
            """<style>%s</style></head><body>
<a class="skip" href="#main">Skip to the text</a>
<main id="main" style="padding-top:2.5rem">
<div class="card reading"><h1>%s</h1>%s
<p class="muted">Last updated %s. <a href="/">Back to the home page</a>.</p></div>
</main></body></html>
""" % (css, title, paras, stamp))


def main():
    for d in (PUBLIC, GATED, os.path.join(PUBLIC, "assets")):
        if not os.path.isdir(d):
            os.makedirs(d)

    stamp = datetime.date.today().isoformat()
    css = read("style.css")
    data = online.build_data()
    data["profile_default"] = {}

    # ---- gated: the app and everything in it -------------------------------
    app_html = build_app_html(css, read("shell.html").replace("__BUILD__", stamp))
    payload = json.dumps({"appHtml": app_html, "data": data},
                         separators=(",", ":"), ensure_ascii=False)
    write(os.path.join(GATED, "gated.js"),
          "/* Generated by tools/build_paid.py -- do not edit. */\n"
          "export default JSON.parse(%s);\n" % json.dumps(payload))

    # ---- public: the sales page -------------------------------------------
    totals = {
        "total": sum(len(v) for v in data["banks"].values())
                 + sum(len(v["q"]) for v in data["math"].values()),
        "terms": sum(len(t["vocab"]) for t in data["study"]["topics"].values()),
        "topics": len(data["study"]["topics"]),
    }
    home = {
        "price": PRICE_CENTS,
        "totals": totals,
        "features": [{"icon": i, "name": n,
                      "desc": d % {"terms": totals["terms"]} if "%(" in d else d}
                     for i, n, d in FEATURES],
        "icons": ICONS,
        "audience": AUDIENCE,
        "why": WHY,
        "steps": STEPS,
        "honest": HONEST,
    }
    shell = read("home.html")
    homejs = read("home.js")
    head = online.head(sum(len(v) for v in data["banks"].values()), totals["terms"])

    def public_page(name, page, title, desc, preview=False, noindex=False,
                    canonical=None, social=None):
        blob = json.dumps(dict(home, page=page, preview=preview,
                                    layout=LAYOUT),
                          separators=(",", ":"),
                          ensure_ascii=False).replace("</", "<\\/")
        body = (shell.replace("__CSS__", css)
                     .replace("__HOME__", blob)
                     .replace("__HOMEJS__", homejs)
                     .replace("__SUPPORT__", SUPPORT_EMAIL)
                     .replace("__BUILD__", stamp))
        cut = body.index("<header")
        """A paid page that borrows the free site's <head> tells search
           engines it is a copy of a free thing, and tells a reader it costs
           nothing. Each page describes itself instead."""
        h = online.head(
            sum(len(v) for v in data["banks"].values()), totals["terms"],
            site=PAID_SITE, title=title, blurb=desc,
            canonical=canonical or (PAID_SITE if name == "index.html"
                                    else PAID_SITE + name.replace(".html", "")),
            price_cents=PRICE_CENTS, noindex=noindex,
            social=social or title, manifest=None)
        page_html = (h + body[:cut].replace(
                        "<title>Georgia Real Estate Exam Prep</title>\n", "")
                     + "</head>\n<body>\n" + body[cut:] + "\n</body>\n</html>\n")
        write(os.path.join(PUBLIC, name), page_html)
        return len(page_html)

    sell = ("Practice for the Georgia real estate salesperson licensing exam: "
            "%d exam-style questions scored National and Georgia separately, "
            "real estate math worked step by step, study notes covering %d "
            "topics with %d defined terms, and a study plan built around your "
            "test date. One payment of $%d, nothing renews."
            % (totals["total"], totals["topics"], totals["terms"],
               PRICE_CENTS // 100))

    welcome_n = public_page(
        "index.html", "welcome",
        "Georgia Real Estate Exam Prep \u2014 %d practice questions" % totals["total"],
        sell,
        social="Pass the Georgia salesperson exam.")
    # In the minimal layout the home page already is the sales page, so this
    # one is the same offer at a second address. Point it home rather than
    # competing with itself in search results.
    buy_n = public_page(
        "buy.html", "buy",
        "Get access \u2014 Georgia Real Estate Exam Prep",
        sell, noindex=True, canonical=PAID_SITE)

    # Nobody should arrive at a sign-in form from a search engine.
    public_page("auth.html", "auth",
                "Create your account \u2014 Georgia Real Estate Exam Prep",
                "Create an account or log in to your Georgia exam prep.",
                noindex=True, canonical=PAID_SITE)

    # A single self-contained file carrying both pages, for looking at the
    # design before any of it is deployed. Nothing in it calls a server.
    public_page("preview.html", "welcome",
                "Preview \u2014 Georgia Real Estate Exam Prep",
                "Preview of the Georgia salesperson exam prep site.",
                preview=True, noindex=True, canonical=PAID_SITE)

    write(os.path.join(PUBLIC, "terms.html"), legal_page(
        "Terms and refunds", [
            "This site sells one thing: lifetime access to a practice question "
            "bank and study notes for the Georgia real estate salesperson "
            "licensing exam, for a single payment of $%d." % (PRICE_CENTS // 100),
            "<b>Refunds.</b> Email %s within 14 days of your purchase and you "
            "will be refunded in full. You do not have to give a reason."
            % SUPPORT_EMAIL,
            "<b>What you may do.</b> Use the material to study, on as many of "
            "your own devices as you like. Accounts are for one person.",
            "<b>What you may not do.</b> Republish, resell, or redistribute the "
            "questions, notes or explanations. They are original work.",
            "<b>No guarantee.</b> This is practice material. Nobody can promise "
            "you a pass, and nothing here is legal advice or an official "
            "statement of Georgia law. Verify current rules at grec.state.ga.us.",
            "<b>Not affiliated.</b> This site is not connected to, endorsed by, "
            "or approved by the Georgia Real Estate Commission, PSI, or any "
            "real estate school. It is not a substitute for the 75-hour "
            "pre-licence course Georgia requires.",
            "<b>Access.</b> Access is intended to last indefinitely. If the "
            "site ever shuts down, you will be given notice and a way to export "
            "your progress. You can export it yourself at any time from "
            "Account settings, without asking.",
            "<b>Who runs this.</b> %s. Questions and complaints go to %s, "
            "which is read by a person." % (siteconfig.operator(), SUPPORT_EMAIL),
        ], css, stamp, "terms",
           "The terms of use and refund policy for Georgia Real Estate Exam Prep."))

    write(os.path.join(PUBLIC, "privacy.html"), legal_page(
        "Privacy", [
            "<b>What is collected.</b> Your email address, so you can sign in "
            "and so we know what you bought. Your name and mobile number, "
            "because the sign-up form asks for them -- the name is used to "
            "greet you, the number is kept so an account can be recovered, and "
            "neither is required to be real for the site to work. Your study "
            "progress: scores, which questions you have answered, and your "
            "plan settings. The date you agreed to the terms.",
            "<b>What is not.</b> No postal address, no date of birth, no "
            "licence number, no card details, no tracking pixels, no "
            "advertising, and no analytics of any kind. Nothing is collected "
            "about you from anywhere other than this site.",
            "<b>Your password.</b> Stored only as a PBKDF2-SHA256 hash with a "
            "salt unique to your account. It cannot be read back, by anybody, "
            "including whoever runs this site.",
            "<b>Payments.</b> Card details are handled entirely by Stripe and "
            "never touch this site. We store only Stripe's reference for your "
            "payment.",
            "<b>Sharing.</b> Your data is not sold, rented, or shared. Stripe "
            "processes the payment; an email provider delivers your sign-in "
            "code. Nobody else sees any of it.",
            "<b>Taking it with you.</b> Account settings has an Export "
            "button that hands you every row held about you as a JSON file. "
            "No request, no waiting.",
            "<b>Deleting it.</b> Account settings has a Delete account button. "
            "It removes your account, your progress, and your sessions "
            "immediately and permanently, and it cannot be undone. You can "
            "also email %s and ask, if you would rather. Deleting your account "
            "does not refund a payment -- ask for that separately, and see the "
            "refund terms." % SUPPORT_EMAIL,
            "<b>Cookies.</b> One, holding your signed-in session. No tracking "
            "cookies, so there is no banner to click.",
            "<b>Children.</b> This is study material for a professional "
            "licence. It is not directed at anyone under 16, and no account "
            "should be created for one.",
            "<b>Changes.</b> If what is collected ever changes, this page "
            "changes with it and the date below moves.",
        ], css, stamp, "privacy",
           "What Georgia Real Estate Exam Prep collects, what it does not, "
           "and how to export or delete it."))

    # A crawler should find the sales page and nothing else. /app is behind
    # the gate anyway, but saying so costs one line and saves the crawl.
    write(os.path.join(PUBLIC, "robots.txt"),
          "User-agent: *\n"
          "Allow: /$\n"
          "Allow: /terms\n"
          "Allow: /privacy\n"
          "Disallow: /app\n"
          "Disallow: /auth\n"
          "Disallow: /buy\n"
          "Disallow: /preview\n"
          "Disallow: /api/\n"
          "\n"
          "Sitemap: %ssitemap.xml\n" % PAID_SITE)

    write(os.path.join(PUBLIC, "sitemap.xml"),
          '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + "".join('  <url><loc>%s%s</loc><lastmod>%s</lastmod>'
                    '<changefreq>%s</changefreq><priority>%s</priority></url>\n'
                    % (PAID_SITE, slug, stamp, freq, pri)
                    for slug, freq, pri in (("", "weekly", "1.0"),
                                            ("terms", "yearly", "0.3"),
                                            ("privacy", "yearly", "0.3")))
          + "</urlset>\n")

    write(os.path.join(PUBLIC, "404.html"), legal_page(
        "Page not found", [
            "There is nothing at that address. It may have been a typo, or a "
            "link that pointed somewhere this site never had.",
            "<a class=\"btn\" href=\"/\" style=\"display:inline-flex\">"
            "Go to the home page</a>",
            "<span class=\"muted\">If you followed a link from inside the "
            "site and landed here, that is a bug worth telling us about: "
            "<a href=\"mailto:%s\">%s</a>.</span>" % (SUPPORT_EMAIL, SUPPORT_EMAIL),
        ], css, stamp, "404",
           "That page does not exist on Georgia Real Estate Exam Prep."))

    src = os.path.join(HERE, "docs", "assets")
    for name in os.listdir(src):
        shutil.copy2(os.path.join(src, name), os.path.join(PUBLIC, "assets", name))

    for name, label in (("index.html", "welcome page"), ("buy.html", "buy page"),
                        ("auth.html", "auth page"),
                        ("preview.html", "preview"), ("terms.html", "terms"),
                        ("privacy.html", "privacy")):
        assert_no_leak(os.path.join(PUBLIC, name), label)

    gsize = os.path.getsize(os.path.join(GATED, "gated.js"))
    psize = os.path.getsize(os.path.join(PUBLIC, "index.html"))
    bsize = os.path.getsize(os.path.join(PUBLIC, "buy.html"))
    print("gated  worker/assets/gated.js    %.2f MB  (app + %d questions)"
          % (gsize / 1e6, totals["total"]))
    print("public worker/public/index.html   %.0f KB  (welcome, for new users)"
          % (psize / 1e3))
    print("public worker/public/buy.html     %.0f KB  (payment)" % (bsize / 1e3))
    print("       worker/public/preview.html %.0f KB  (both pages, no server needed)"
          % (os.path.getsize(os.path.join(PUBLIC, "preview.html")) / 1e3))
    print("public worker/public/terms.html, privacy.html, assets/")
    print("price  $%d one-time   support %s" % (PRICE_CENTS // 100, SUPPORT_EMAIL))
    print("leak   every public page checked: no questions, answers or notes")
    print("seo    robots.txt, sitemap.xml, 404.html; app and auth noindex")
    siteconfig.check()


if __name__ == "__main__":
    main()
