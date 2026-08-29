#!/usr/bin/env python3
"""Bundle the whole app into one self-contained HTML page.

Run:  python3 tools/build_online.py
Writes online/ga-real-estate.html -- no server, no network, one file.

Math generators are pre-rolled here rather than ported to JavaScript, so the
online problems are produced by exactly the same Python that the local app
uses. Progress lives in the browser's localStorage instead of data/progress.json.
"""
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

# An emoji favicon, so the standalone build has a tab icon without a binary asset.
FAVICON = ("data:image/svg+xml,"
           "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E"
           "%3Ctext y='.9em' font-size='90'%3E%F0%9F%8F%A1%3C/text%3E%3C/svg%3E")

STANDALONE_HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light dark">
<meta name="description" content="Practice quizzes, a comprehensive subtest, real estate math with worked solutions, and a study plan for the Georgia salesperson licensing exam.">
<meta name="robots" content="noindex">
<link rel="icon" href="%s">
<link rel="apple-touch-icon" href="%s">
""" % (FAVICON, FAVICON)

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
    """Carry the local app's exam settings into the online build."""
    path = os.path.join(HERE, "data", "progress.json")
    if not os.path.exists(path):
        return {}
    try:
        with open(path) as f:
            return json.load(f).get("profile", {}) or {}
    except ValueError:
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


def main():
    if not os.path.isdir(DOCS):
        os.makedirs(DOCS)
    data = build_data()
    blob = json.dumps(data, separators=(",", ":"), ensure_ascii=False)
    # a closing script tag inside embedded JSON would end the <script> early
    blob = blob.replace("</", "<\\/")

    html = (read("shell.html")
            .replace("__CSS__", read("style.css"))
            .replace("__DATA__", blob)
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
    standalone = html[:cut] + "</head>\n<body>\n" + html[cut:]
    standalone = STANDALONE_HEAD + standalone + "\n</body>\n</html>\n"
    with io.open(OUT_STANDALONE, "w", encoding="utf-8") as f:
        f.write(standalone)

    math_n = sum(len(v["q"]) for v in data["math"].values())
    fixed_n = sum(len(v) for v in data["banks"].values())
    hard_n = sum(1 for rows in data["banks"].values() for r in rows
                 if r.get("difficulty", 1) == 2)
    study_n = len(data["study"]["topics"])
    vocab_n = sum(len(t["vocab"]) for t in data["study"]["topics"].values())
    print("wrote %s" % os.path.relpath(OUT, HERE))
    print("wrote %s  (%.2f MB standalone)"
          % (os.path.relpath(OUT_STANDALONE, HERE),
             os.path.getsize(OUT_STANDALONE) / 1e6))
    print("  %.2f MB  |  %d written (%d hard) + %d pre-rolled math = %d questions"
          % (os.path.getsize(OUT) / 1e6, fixed_n, hard_n, math_n, fixed_n + math_n))
    print("  study notes: %d topics, %d vocab terms" % (study_n, vocab_n))


if __name__ == "__main__":
    main()
