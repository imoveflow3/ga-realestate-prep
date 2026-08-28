#!/usr/bin/env python3
"""Assemble the question banks into greprep/banks/*.json.

Sources live in tools/_national_*.py and tools/_georgia_*.py so the questions
stay readable and diffable in Python. This script stamps stable ids, balances
which position holds the correct answer, and validates before writing.
"""
import collections
import hashlib
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, ROOT)

import _national_a, _national_b, _national_c      # noqa: E402
import _national_hard_a, _national_hard_b         # noqa: E402
import _georgia_a, _georgia_b, _georgia_hard      # noqa: E402
import _comp_a, _comp_b                           # noqa: E402
from greprep import topics                        # noqa: E402

OUT = os.path.join(ROOT, "greprep", "banks")

SOURCES = {
    "national": [_national_a.ROWS, _national_b.ROWS, _national_c.ROWS,
                 _national_hard_a.ROWS, _national_hard_b.ROWS],
    "georgia": [_georgia_a.ROWS, _georgia_b.ROWS, _georgia_hard.ROWS],
    "comprehensive": [_comp_a.ROWS, _comp_b.ROWS],
}


def stable_id(portion, row):
    h = hashlib.sha1(row["q"].encode("utf-8")).hexdigest()[:8]
    return "%s-%s" % (portion[:3], h)


def rebalance(row, rng):
    """Shuffle the choices so the answer key is not clustered in one position."""
    correct = row["choices"][row["answer"]]
    opts = list(row["choices"])
    rng.shuffle(opts)
    row["choices"] = opts
    row["answer"] = opts.index(correct)
    return row


def build(portion):
    rows = []
    for chunk in SOURCES[portion]:
        rows.extend(chunk)
    out, seen_q, seen_id = [], set(), set()
    for row in rows:
        r = dict(row)
        q = r["q"].strip()
        if q in seen_q:
            raise SystemExit("duplicate question text: %s" % q[:70])
        seen_q.add(q)
        r["id"] = stable_id(portion, r)
        if r["id"] in seen_id:
            raise SystemExit("id collision: %s" % r["id"])
        seen_id.add(r["id"])
        r["portion"] = portion
        r.setdefault("difficulty", 1)          # unmarked questions are the core tier
        if r["difficulty"] not in topics.DIFFICULTY:
            raise SystemExit("bad difficulty on: %s" % q[:70])
        if r["topic"] not in topics.TOPICS:
            raise SystemExit("unknown topic %s" % r["topic"])
        if len(r["choices"]) != 4 or not (0 <= r["answer"] < 4):
            raise SystemExit("malformed choices: %s" % q[:70])
        if len(set(r["choices"])) != 4:
            raise SystemExit("duplicate choice text: %s" % q[:70])
        for field in ("concept", "explain"):
            if not r.get(field, "").strip():
                raise SystemExit("missing %s: %s" % (field, q[:70]))
        rebalance(r, random.Random(r["id"]))
        out.append(r)
    return out


def main():
    if not os.path.isdir(OUT):
        os.makedirs(OUT)
    grand = 0
    seen_across = {}
    for portion in ("national", "georgia", "comprehensive"):
        rows = build(portion)
        for r in rows:                      # the same stem must not appear in two banks
            key = r["q"].strip().lower()
            if key in seen_across:
                raise SystemExit("stem duplicated across %s and %s: %s"
                                 % (seen_across[key], portion, r["q"][:70]))
            seen_across[key] = portion
        path = os.path.join(OUT, portion + ".json")
        with open(path, "w") as f:
            json.dump(rows, f, indent=1, sort_keys=True)
        by_topic = collections.Counter(r["topic"] for r in rows)
        pos = collections.Counter(r["answer"] for r in rows)
        diff = collections.Counter(r["difficulty"] for r in rows)
        grand += len(rows)
        print("%s: %d questions -> %s" % (portion, len(rows), os.path.relpath(path, ROOT)))
        for k in topics.portion_topics(portion):
            hard = sum(1 for r in rows if r["topic"] == k and r["difficulty"] == 2)
            tail = ("drill weight %d" % topics.weight(k) if k in topics.PRACTICE_ONLY
                    else "exam weight %d" % topics.weight(k))
            print("    %-28s %3d  (%d hard, %s)" % (topics.label(k), by_topic[k], hard, tail))
        print("    answer position spread: %s" % dict(sorted(pos.items())))
        print("    difficulty: %d core / %d hard" % (diff[1], diff[2]))
        thin = [topics.label(k) for k in topics.portion_topics(portion) if by_topic[k] < 5]
        if thin:
            print("    NOTE thin topics (<5): %s" % ", ".join(thin))
    print("total static questions: %d" % grand)


if __name__ == "__main__":
    main()
