#!/usr/bin/env python3
"""Assemble the study notes into greprep/banks/study.json.

Validates that every topic in the exam outline has notes, and that every note
points at a topic that actually exists.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, ROOT)

import _study_nat_a, _study_nat_b, _study_nat_c      # noqa: E402
import _study_ga, _study_comp                        # noqa: E402
import _checks_a, _checks_b, _checks_c               # noqa: E402
from greprep import topics                           # noqa: E402

OUT = os.path.join(ROOT, "greprep", "banks", "study.json")

SOURCES = [
    {"name": "Georgia Real Estate InfoBase",
     "by": "Georgia Real Estate Commission",
     "url": "https://grec.state.ga.us/information-research/infobase-main/",
     "note": "The Commission's own reference text. Every Georgia-specific fact in "
             "these notes was checked against it."},
    {"name": "O.C.G.A. Title 43 Chapter 40",
     "by": "Georgia General Assembly",
     "url": "https://law.justia.com/codes/georgia/title-43/chapter-40/",
     "note": "The Georgia real estate licence law itself."},
    {"name": "O.C.G.A. Title 10 Chapter 6A (BRRETA)",
     "by": "Georgia General Assembly",
     "url": "https://law.justia.com/codes/georgia/title-10/chapter-6a/",
     "note": "Brokerage Relationships in Real Estate Transactions Act, quoted in "
             "InfoBase chapter 9."},
    {"name": "Fair Housing Act and HUD guidance",
     "by": "U.S. Department of Housing and Urban Development",
     "url": "https://www.hud.gov/program_offices/fair_housing_equal_opp",
     "note": "Protected classes, accommodations, and enforcement."},
    {"name": "TRID / Regulation Z and RESPA",
     "by": "Consumer Financial Protection Bureau",
     "url": "https://www.consumerfinance.gov/rules-policy/regulations/",
     "note": "Loan Estimate and Closing Disclosure timing, and settlement rules."},
    {"name": "EPA lead-based paint and radon guidance",
     "by": "U.S. Environmental Protection Agency",
     "url": "https://www.epa.gov/lead",
     "note": "Pre-1978 disclosure duties and environmental hazards."},
]


def merged_checks():
    """Merge the section checks and fail loudly on a heading that does not exist."""
    out = {}
    for mod in (_checks_a, _checks_b, _checks_c):
        for topic, per_section in mod.CHECKS.items():
            for heading, qs in per_section.items():
                out.setdefault(topic, {})
                if heading in out[topic]:
                    raise SystemExit("duplicate checks for %s / %s" % (topic, heading))
                for q in qs:
                    if len(q["choices"]) < 2 or not (0 <= q["answer"] < len(q["choices"])):
                        raise SystemExit("bad check in %s / %s" % (topic, heading))
                    if len(set(q["choices"])) != len(q["choices"]):
                        raise SystemExit("repeated choice in %s / %s" % (topic, heading))
                    if not q["why"].strip():
                        raise SystemExit("check with no explanation: %s" % q["q"][:50])
                out[topic][heading] = qs
    return out


def main():
    merged = {}
    for mod in (_study_nat_a, _study_nat_b, _study_nat_c, _study_ga, _study_comp):
        for key, note in mod.STUDY.items():
            if key in merged:
                raise SystemExit("duplicate study entry: %s" % key)
            if key not in topics.TOPICS:
                raise SystemExit("study note for unknown topic: %s" % key)
            merged[key] = note

    missing = [k for k in topics.ORDER if k not in merged]
    if missing:
        raise SystemExit("no study notes for: %s" % ", ".join(missing))

    checks = merged_checks()
    out, totals = {}, {"sections": 0, "vocab": 0, "examples": 0, "words": 0, "checks": 0}
    for key in topics.ORDER:                      # keep exam order
        n = merged[key]
        for field in ("summary", "sections", "vocab", "examples"):
            if not n.get(field):
                raise SystemExit("%s is missing %s" % (key, field))
        words = len(n["summary"].split())
        for s in n["sections"]:
            if not s.get("h"):
                raise SystemExit("%s has a section with no heading" % key)
            words += len(" ".join(s.get("p", []) + s.get("l", [])).split())
        for term, definition in n["vocab"]:
            if not term.strip() or not definition.strip():
                raise SystemExit("%s has an empty vocab entry" % key)
        for ex in n["examples"]:
            for f in ("t", "s", "w", "k"):
                if not ex.get(f):
                    raise SystemExit("%s has an incomplete example" % key)
        # attach each section's checks, and refuse to ship a mismatched heading
        heads = set(sec["h"] for sec in n["sections"])
        for heading in (checks.get(key) or {}):
            if heading not in heads:
                raise SystemExit("checks reference a missing section: %s / %s"
                                 % (key, heading))
        for sec in n["sections"]:
            qs = (checks.get(key) or {}).get(sec["h"], [])
            sec["check"] = qs
            totals["checks"] += len(qs)
        portion, label, weight, blurb = topics.TOPICS[key]
        out[key] = {
            "topic": key, "portion": portion, "label": label, "blurb": blurb,
            "exam_questions": weight, "counts_on_exam": topics.counts_on_exam(key),
            "summary": n["summary"], "sections": n["sections"],
            "vocab": [list(v) for v in n["vocab"]], "examples": n["examples"],
            "ga": n.get("ga", []), "traps": n.get("traps", []),
        }
        totals["sections"] += len(n["sections"])
        totals["vocab"] += len(n["vocab"])
        totals["examples"] += len(n["examples"])
        totals["words"] += words

    payload = {"topics": out, "sources": SOURCES}
    with open(OUT, "w") as f:
        json.dump(payload, f, indent=1, sort_keys=True)

    print("wrote %s" % os.path.relpath(OUT, ROOT))
    print("  %d topics | %d sections | %d vocab terms | %d worked examples | ~%s words"
          % (len(out), totals["sections"], totals["vocab"], totals["examples"],
             "{:,}".format(totals["words"])))
    print("  %d section checks" % totals["checks"])
    bare = [(k, sec["h"]) for k in out for sec in out[k]["sections"] if not sec["check"]]
    if bare:
        print("  NOTE %d sections have no check:" % len(bare))
        for k, h in bare:
            print("     %s / %s" % (k, h))
    thin = [k for k in out if len(out[k]["vocab"]) < 5]
    if thin:
        print("  NOTE thin vocab (<5): %s" % ", ".join(thin))


if __name__ == "__main__":
    main()
