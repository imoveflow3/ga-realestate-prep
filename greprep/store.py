"""Local JSON persistence for profile, attempts, and per-topic history."""
import datetime
import json
import os
import tempfile
import time
import uuid

from . import topics

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
DATA_FILE = os.path.join(DATA_DIR, "progress.json")

EMPTY = {"version": 1, "profile": {}, "attempts": [],
         "topics": {}, "subs": {}, "items": {}, "generators": {}, "misses": {}}

# Generated math problems have unique ids, so cap how many of each generator's
# misses the notebook keeps or it would grow without limit.
MATH_MISS_CAP = 6


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


def backfill_misses(data):
    """Rebuild notebook entries from quizzes taken before the notebook existed.

    `items` records seen/correct per question id, so which questions were missed
    is recoverable. Which wrong choice was picked never was, so recovered entries
    are flagged rather than guessed at. Generated math ids are one-off and cannot
    be rebuilt.
    """
    if data.get("backfilled"):
        return 0
    from . import questions
    index = {r["id"]: r for r in questions.all_rows()}
    misses = data.setdefault("misses", {})
    added = 0
    for qid, rec in (data.get("items") or {}).items():
        missed = rec.get("seen", 0) - rec.get("correct", 0)
        if missed <= 0 or qid in misses:
            continue
        q = index.get(qid)
        if not q:
            continue
        misses[qid] = {
            "qid": qid, "topic": q["topic"], "sub": q.get("sub"),
            "portion": q.get("portion"), "generator": None,
            "difficulty": q.get("difficulty", 1),
            "q": q["q"], "choices": q["choices"], "answer": q["answer"],
            "chose": None, "concept": q.get("concept", ""),
            "explain": q.get("explain", ""), "steps": [],
            "at": rec.get("last") or time.time(), "times": missed,
            "cleared": 0, "recovered": True,
        }
        added += 1
    data["backfilled"] = 1
    return added


def _note_miss(data, a):
    q = a.get("q")
    if not q:
        return
    misses = data.setdefault("misses", {})
    prev = misses.get(q["id"])
    misses[q["id"]] = {
        "qid": q["id"], "topic": q["topic"], "sub": q.get("sub"),
        "portion": q.get("portion"), "generator": q.get("generator"),
        "difficulty": q.get("difficulty", 1),
        "q": q["q"], "choices": q["choices"], "answer": q["answer"],
        "chose": a.get("choice"),
        "concept": q.get("concept", ""), "explain": q.get("explain", ""),
        "steps": q.get("steps") or [],
        "at": time.time(),
        "times": (prev.get("times", 1) + 1) if prev else 1,
        "cleared": 0,
    }
    if q.get("generator"):
        mine = [k for k, v in misses.items()
                if v.get("generator") == q["generator"] and not v.get("cleared")]
        mine.sort(key=lambda k: misses[k]["at"])
        while len(mine) > MATH_MISS_CAP:
            del misses[mine.pop(0)]


def _clear_miss(data, a):
    rec = (data.get("misses") or {}).get(a.get("qid"))
    if rec and not rec.get("cleared"):
        rec["cleared"] = time.time()


def record_attempt(data, portion, mode, answers, elapsed, weak_spot=False):
    """answers: [{qid, topic, sub, generator, correct, seconds, q}]"""
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
        sub = a.get("sub")
        if sub:
            _bump(data["subs"], sub, a.get("correct"))
        gen = a.get("generator")
        if gen:
            _bump(data["generators"], gen, a.get("correct"))
        if a.get("correct"):
            _clear_miss(data, a)
        else:
            _note_miss(data, a)
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


def _slice_stats(rows):
    """rows: [{'seen','correct'}] in attempt order -> totals, recent, and trend."""
    qs = sum(r["seen"] for r in rows)
    corr = sum(r["correct"] for r in rows)
    recent = rows[-3:]
    rq = sum(r["seen"] for r in recent)
    rc = sum(r["correct"] for r in recent)
    trend = None
    if len(rows) >= 2:
        half = rows[:max(1, len(rows) // 2)]
        hq = sum(r["seen"] for r in half)
        hc = sum(r["correct"] for r in half)
        if hq and rq:
            trend = (rc / float(rq)) - (hc / float(hq))
    return {"sets": len(rows), "qs": qs, "correct": corr,
            "pct": (corr / float(qs)) if qs else None,
            "recent_pct": (rc / float(rq)) if rq else None,
            "trend": trend}


def topic_table(data):
    """One row per topic, in exam order, with per-attempt history folded in."""
    hist = {}
    for att in data["attempts"]:
        for tkey, v in (att.get("topics") or {}).items():
            if v.get("seen"):
                hist.setdefault(tkey, []).append(v)
    rows = []
    for key in topics.ORDER:
        portion, label, weight, blurb = topics.TOPICS[key]
        st = _slice_stats(hist.get(key, []))
        st.update({"topic": key, "portion": portion, "label": label,
                   "exam_questions": weight,
                   "counts_on_exam": topics.counts_on_exam(key)})
        rows.append(st)
    return rows


def section_table(data):
    """One row per section, folding every attempt that touched it."""
    names = {"national": "National", "georgia": "Georgia state",
             "comprehensive": "Comprehensive"}
    out = []
    for portion in ("national", "georgia", "comprehensive"):
        keys = set(topics.portion_topics(portion))
        rows = []
        for att in data["attempts"]:
            seen = corr = 0
            for tkey, v in (att.get("topics") or {}).items():
                if tkey in keys:
                    seen += v["seen"]
                    corr += v["correct"]
            if seen:
                rows.append({"seen": seen, "correct": corr})
        st = _slice_stats(rows)
        st.update({"portion": portion, "name": names[portion],
                   "scored": topics.PORTIONS[portion].get("scored", 0)})
        out.append(st)
    return out


def headline(data):
    """The readout strip: standing on the two scored portions only."""
    keys = set(topics.portion_topics("national")) | set(topics.portion_topics("georgia"))
    rows = []
    for att in data["attempts"]:
        seen = corr = 0
        for tkey, v in (att.get("topics") or {}).items():
            if tkey in keys:
                seen += v["seen"]
                corr += v["correct"]
        if seen:
            rows.append({"seen": seen, "correct": corr})
    st = _slice_stats(rows)
    answered = sum(a["count"] for a in data["attempts"])
    days = None
    exam = (data.get("profile") or {}).get("exam_date")
    if exam:
        try:
            d = datetime.datetime.strptime(str(exam)[:10], "%Y-%m-%d").date()
            days = (d - datetime.date.today()).days
        except ValueError:
            days = None
    return {"exam_pct": st["recent_pct"], "trend": st["trend"],
            "sets": len(data["attempts"]), "answered": answered,
            "days_out": days,
            "passing": st["recent_pct"] is not None and st["recent_pct"] >= 0.75}


def miss_report(data, open_only=False):
    """The notebook: every question you have got wrong, grouped later by topic."""
    rows = []
    for rec in (data.get("misses") or {}).values():
        if open_only and rec.get("cleared"):
            continue
        tkey = rec.get("topic")
        if tkey not in topics.TOPICS:
            continue
        portion, label, weight, blurb = topics.TOPICS[tkey]
        sub = rec.get("sub")
        row = dict(rec)
        row.setdefault("recovered", False)
        row.update({"topic_label": label, "portion": portion,
                    "subtopic": sub.split("|", 1)[1] if sub else None,
                    "exam_questions": weight,
                    "counts_on_exam": topics.counts_on_exam(tkey)})
        rows.append(row)
    rows.sort(key=lambda r: (bool(r.get("cleared")), -r.get("times", 1),
                             -r.get("at", 0)))
    return rows


def miss_counts(data):
    open_n = cleared = 0
    for rec in (data.get("misses") or {}).values():
        if rec.get("cleared"):
            cleared += 1
        else:
            open_n += 1
    return {"open": open_n, "cleared": cleared, "total": open_n + cleared}


def sub_report(data, min_seen=2, limit=None):
    """The 'little topics': every subtopic you have actually answered, weakest first.

    Ties break on how much the PARENT topic is worth on the exam, so a weak
    subtopic inside Contracts outranks one inside Land use.
    """
    rows = []
    for key, rec in (data.get("subs") or {}).items():
        seen = rec.get("seen", 0)
        if seen < min_seen:
            continue
        topic, _, label = key.partition("|")
        if topic not in topics.TOPICS:
            continue
        portion, tlabel, weight, blurb = topics.TOPICS[topic]
        corr = rec.get("correct", 0)
        rows.append({"sub": key, "label": label, "topic": topic,
                     "topic_label": tlabel, "portion": portion,
                     "exam_questions": weight,
                     "counts_on_exam": topics.counts_on_exam(topic),
                     "seen": seen, "correct": corr, "pct": corr / float(seen)})
    rows.sort(key=lambda r: (r["pct"], -r["exam_questions"]))
    return rows[:limit] if limit else rows


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
