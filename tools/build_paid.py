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
import random
import shutil
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)

import tools.build_online as online                      # noqa: E402

ONLINE = os.path.join(HERE, "online")
WORKER = os.path.join(HERE, "worker")
PUBLIC = os.path.join(WORKER, "public")
GATED = os.path.join(WORKER, "assets")

PRICE_CENTS = 1900
SUPPORT_EMAIL = "support@example.com"          # change before you take money
SAMPLE_COUNT = 3

ICONS = {
    "quiz":  '<rect x="3.5" y="3.5" width="17" height="17" rx="4"/>'
             '<path d="M8.6 12.2l2.3 2.4 4.5-5"/>',
    "book":  '<path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5Z"/>'
             '<path d="M4 20.5A2.5 2.5 0 0 1 6.5 18H20v3H6.5"/>',
    "math":  '<rect x="4" y="3" width="16" height="18" rx="3"/>'
             '<path d="M8 8h8M8 12h3M8 16h3M15 12v4M13 14h4"/>',
    "cards": '<rect x="3" y="7" width="13" height="13" rx="2.5"/>'
             '<path d="M7.5 4h11A2.5 2.5 0 0 1 21 6.5v11"/>',
    "target": '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="3.4"/>'
              '<path d="M12 1.6v2.6M12 19.8v2.6M22.4 12h-2.6M4.2 12H1.6"/>',
    "note":  '<path d="M5 3.5h14v17l-3.2-2.2-3.4 2.2-3.4-2.2L5.8 20.5Z"/>'
             '<path d="M9 8.5h6M9 12.5h6"/>',
}

FEATURES = [
    ("quiz", "Practice quizzes",
     "Timed sets that mirror the real split, scored National and Georgia "
     "separately because that is how you pass or fail."),
    ("book", "Study notes",
     "%(terms)d terms defined in plain sentences, with a short check-yourself "
     "quiz after every section."),
    ("math", "Math, worked out",
     "Every calculation broken into steps you can follow -- prorations, "
     "commissions, points, loan-to-value, area."),
    ("cards", "Vocabulary drill",
     "You read the definition and name the term. Categories unlock as you "
     "pass them, and a flashcard deck brings back whatever slipped."),
    ("target", "Weak-spot targeting",
     "The narrow sub-topics dragging your score down, each with its own "
     "drill, plus a week-by-week plan built around your test date."),
    ("note", "Your notebook",
     "Every question you get wrong, kept with the right answer and the "
     "reason, synced to your account and waiting on any device."),
]


def faq(price):
    return [
        ["What exactly do I get for $%d?" % (price // 100),
         "Everything: the full question bank, the study notes, the maths with "
         "worked solutions, the vocabulary drill, the weak-spot targeting and "
         "the study planner. There is no higher tier and nothing else to buy."],
        ["Is it a subscription?",
         "No. One payment, and the account is yours. Nothing renews and there "
         "is nothing to cancel."],
        ["What if it is not for me?",
         "Email within 14 days of buying and you get a full refund, no "
         "argument. The address is in the footer."],
        ["Where do the Georgia rules come from?",
         "The Georgia Real Estate Commission's own InfoBase and the Georgia "
         "Code, read chapter by chapter, rather than a commercial cram guide. "
         "That matters where the guides are wrong -- continuing education in "
         "Georgia is 24 hours per four-year renewal, not the 36 that national "
         "study guides tend to quote."],
        ["Does my progress follow me between devices?",
         "Yes. Your scores, your notebook and your plan live on your account, "
         "so signing in on a phone picks up where the laptop left off."],
        ["Is this official?",
         "No. It is not affiliated with, endorsed by, or connected to the "
         "Georgia Real Estate Commission, PSI, or any school. It is practice "
         "material, not legal advice, and it is no substitute for the 75-hour "
         "pre-licence course Georgia requires before you may sit the exam."],
    ]


def read(name):
    with io.open(os.path.join(ONLINE, name), encoding="utf-8") as f:
        return f.read()


def write(path, text):
    with io.open(path, "w", encoding="utf-8") as f:
        f.write(text)


def pick_samples(bank, n):
    """A few real questions for the sales page -- enough to prove it, not
    enough to be worth stealing."""
    pool = [q for q in bank
            if q.get("explain") and len(q["explain"]) > 90
            and len(q["q"]) < 190 and q.get("difficulty", 1) >= 2]
    rnd = random.Random(20260926)
    rnd.shuffle(pool)
    keep = ("q", "choices", "answer", "explain", "concept", "portion", "difficulty")
    return [{k: q[k] for k in keep if k in q} for q in pool[:n]]


def build_app_html(css, data_free_shell):
    """The app, with the question bank cut out of it.

    engine.js and ui.js both run against a global DATA at load time, so they
    are parked inside __BOOT__ and only run once the bundle has arrived.
    """
    boot = (
        "<script>window.__SYNC__=true;window.__BOOT__=function(){\n"
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


def legal_page(title, body, css, stamp):
    paras = "\n".join("<p>%s</p>" % p for p in body)
    return ("""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light dark"><title>%s</title>
<style>%s</style></head><body>
<main id="main" style="padding-top:2.5rem">
<div class="card reading"><h1>%s</h1>%s
<p class="muted">Last updated %s. <a href="/">Back to the home page</a>.</p></div>
</main></body></html>
""" % (title, css, title, paras, stamp))


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
        "exam": data["exam"],
        "topics": [{"label": t["label"], "portion": t["portion"],
                    "exam_questions": t["exam_questions"]}
                   for t in data["topics"] if t["counts_on_exam"]],
        "samples": pick_samples(data["banks"]["national"]
                                + data["banks"]["georgia"], SAMPLE_COUNT),
        "features": [{"icon": i, "name": n, "desc": d % {"terms": totals["terms"]}
                      if "%(" in d else d}
                     for i, n, d in FEATURES],
        "faq": faq(PRICE_CENTS),
        "icons": ICONS,
    }
    blob = json.dumps(home, separators=(",", ":"), ensure_ascii=False).replace("</", "<\\/")
    page = (read("home.html")
            .replace("__CSS__", css)
            .replace("__HOME__", blob)
            .replace("__HOMEJS__", read("home.js"))
            .replace("__SUPPORT__", SUPPORT_EMAIL)
            .replace("__BUILD__", stamp))
    cut = page.index("<header")
    head = online.head(sum(len(v) for v in data["banks"].values()), totals["terms"])
    head = head.replace("<title>Georgia Real Estate Exam Prep — free salesperson "
                        "practice tests</title>",
                        "<title>Georgia Real Estate Exam Prep — %d practice "
                        "questions, $%d once</title>"
                        % (totals["total"], PRICE_CENTS // 100))
    page = (head + page[:cut].replace(
        "<title>Georgia Real Estate Exam Prep</title>\n", "")
        + "</head>\n<body>\n" + page[cut:] + "\n</body>\n</html>\n")
    write(os.path.join(PUBLIC, "index.html"), page)

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
            "your progress.",
        ], css, stamp))

    write(os.path.join(PUBLIC, "privacy.html"), legal_page(
        "Privacy", [
            "<b>What is collected.</b> Your email address, so you can sign in "
            "and so we know what you bought, and your study progress -- scores, "
            "which questions you have answered, and your plan settings.",
            "<b>What is not.</b> No name, no address, no tracking pixels, no "
            "advertising, and no analytics of any kind.",
            "<b>Payments.</b> Card details are handled entirely by Stripe and "
            "never touch this site. We store only Stripe's reference for your "
            "payment.",
            "<b>Sharing.</b> Your data is not sold, rented, or shared. Stripe "
            "processes the payment; an email provider delivers your sign-in "
            "code. Nobody else sees any of it.",
            "<b>Deleting it.</b> Email %s and your account and every row of "
            "your progress will be deleted. That is permanent." % SUPPORT_EMAIL,
            "<b>Cookies.</b> One, holding your signed-in session. No tracking "
            "cookies, so there is no banner to click.",
        ], css, stamp))

    src = os.path.join(HERE, "docs", "assets")
    for name in os.listdir(src):
        shutil.copy2(os.path.join(src, name), os.path.join(PUBLIC, "assets", name))

    gsize = os.path.getsize(os.path.join(GATED, "gated.js"))
    psize = os.path.getsize(os.path.join(PUBLIC, "index.html"))
    print("gated  worker/assets/gated.js    %.2f MB  (app + %d questions)"
          % (gsize / 1e6, totals["total"]))
    print("public worker/public/index.html   %.2f MB  (sales page)" % (psize / 1e6))
    print("public worker/public/terms.html, privacy.html, assets/")
    print("price  $%d one-time   support %s" % (PRICE_CENTS // 100, SUPPORT_EMAIL))


if __name__ == "__main__":
    main()
