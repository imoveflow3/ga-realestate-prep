"""Local JSON persistence for profile, attempts, and per-topic history."""
import json
import os
import tempfile
import time
import uuid

from . import topics

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
DATA_FILE = os.path.join(DATA_DIR, "progress.json")

EMPTY = {"version": 1, "profile": {}, "attempts": [],
         "topics": {}, "items": {}, "generators": {}}


def load():
    if not os.path.exists(DATA_FILE):
        return json.loads(json.dumps(EMPTY))
    try:
        with open(DATA_FILE) as f:
            data = json.load(f)
    except ValueError:
        os.rename(DATA_FILE, DATA_FILE + ".corrupt-%d" % int(time.time()))
        return json.loads(json.dumps(EMPTY))
    for k, v in EMPTY.items():
        data.setdefault(k, json.loads(json.dumps(v)))
    return data


def save(data):
    """Atomic write so an interrupted save cannot corrupt your history."""
    if not os.path.isdir(DATA_DIR):
        os.makedirs(DATA_DIR)
    fd, tmp = tempfile.mkstemp(dir=DATA_DIR, prefix=".progress-", suffix=".json")
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(data, f, indent=1)
        os.rename(tmp, DATA_FILE)
    except Exception:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise


def _bump(bucket, key, correct):
    rec = bucket.setdefault(key, {"seen": 0, "correct": 0, "last": 0})
    rec["seen"] += 1
    rec["last"] = time.time()
    if correct:
        rec["correct"] += 1
    return rec


def record_attempt(data, portion, mode, answers, elapsed, weak_spot=False):
    """answers: [{qid, topic, generator, correct, seconds}]"""
    now = time.time()
    correct = sum(1 for a in answers if a.get("correct"))
    per_topic = {}
    for a in answers:
        tkey = a.get("topic") or "unknown"
        slot = per_topic.setdefault(tkey, [0, 0])
        slot[0] += 1
        slot[1] += 1 if a.get("correct") else 0
        _bump(data["topics"], tkey, a.get("correct"))
        qid = a.get("qid") or ""
        if qid and not qid.startswith("math:"):
            _bump(data["items"], qid, a.get("correct"))
        gen = a.get("generator")
        if gen:
            _bump(data["generators"], gen, a.get("correct"))
    attempt = {
        "id": uuid.uuid4().hex[:12],
        "portion": portion,
        "mode": mode,
        "weak_spot": bool(weak_spot),
        "at": now,
        "count": len(answers),
        "correct": correct,
        "pct": (correct / float(len(answers))) if answers else 0.0,
        "seconds": round(float(elapsed), 1),
        "topics": {k: {"seen": v[0], "correct": v[1]} for k, v in per_topic.items()},
    }
    data["attempts"].append(attempt)
    return attempt


def topic_report(data):
    """Per-topic accuracy and priority, weakest first."""
    rows = []
    for key in topics.ORDER:
        portion, lab, w, blurb = topics.TOPICS[key]
        rec = data["topics"].get(key)
        seen = rec.get("seen", 0) if rec else 0
        corr = rec.get("correct", 0) if rec else 0
        from . import questions
        rows.append({
            "topic": key, "portion": portion, "label": lab, "blurb": blurb,
            "exam_questions": w,
            "seen": seen, "correct": corr,
            "pct": (corr / float(seen)) if seen else None,
            "priority": round(questions.topic_priority(rec, w), 4),
        })
    rows.sort(key=lambda r: -r["priority"])
    return rows


def portion_stats(data):
    out = {}
    for portion in ("national", "georgia", "comprehensive"):
        rows = [a for a in data["attempts"] if a["portion"] == portion]
        if not rows:
            out[portion] = {"attempts": 0, "pct": None, "recent_pct": None, "trend": None}
            continue
        tq = sum(r["count"] for r in rows) or 1
        tc = sum(r["correct"] for r in rows)
        recent = rows[-3:]
        rq = sum(r["count"] for r in recent) or 1
        rc = sum(r["correct"] for r in recent)
        trend = None
        if len(rows) >= 2:
            half = rows[:max(1, len(rows) // 2)]
            hq = sum(r["count"] for r in half) or 1
            hc = sum(r["correct"] for r in half)
            trend = (rc / float(rq)) - (hc / float(hq))
        out[portion] = {"attempts": len(rows), "questions": tq,
                        "pct": tc / float(tq), "recent_pct": rc / float(rq),
                        "trend": trend, "last": rows[-1]["at"]}
    return out


def trend_series(data):
    """Per-topic accuracy over successive attempts, for the dashboard chart."""
    series = {}
    for att in data["attempts"]:
        for tkey, v in (att.get("topics") or {}).items():
            if not v.get("seen"):
                continue
            series.setdefault(tkey, []).append({
                "at": att["at"],
                "pct": v["correct"] / float(v["seen"]),
                "seen": v["seen"],
            })
    return series


def generator_report(data):
    from . import mathgen
    rows = []
    for key in mathgen.ORDER:
        lab, concept = mathgen.TOPICS[key]
        rec = data["generators"].get(key)
        seen = rec.get("seen", 0) if rec else 0
        corr = rec.get("correct", 0) if rec else 0
        rows.append({"key": key, "label": lab, "concept": concept,
                     "seen": seen, "correct": corr,
                     "pct": (corr / float(seen)) if seen else None})
    rows.sort(key=lambda r: (r["pct"] if r["pct"] is not None else 0.5, -r["seen"]))
    return rows
