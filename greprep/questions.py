"""Question provider: static banks + generated math + selection strategies."""
import json
import os
import random

from . import mathgen, topics

BANK_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "banks")
_BANKS = {}


def bank(portion):
    if portion not in _BANKS:
        with open(os.path.join(BANK_DIR, portion + ".json")) as f:
            _BANKS[portion] = json.load(f)
    return _BANKS[portion]


PORTION_BANKS = ("national", "georgia", "comprehensive")


def all_rows():
    out = []
    for p in PORTION_BANKS:
        out.extend(bank(p))
    return out


def by_id(qid):
    for r in all_rows():
        if r["id"] == qid:
            return r
    return None


def bank_summary():
    out = {}
    for portion in PORTION_BANKS:
        rows = bank(portion)
        per = {}
        for r in rows:
            per[r["topic"]] = per.get(r["topic"], 0) + 1
        out[portion] = {
            "total": len(rows), "by_topic": per,
            "core": sum(1 for r in rows if r.get("difficulty", 1) == 1),
            "hard": sum(1 for r in rows if r.get("difficulty", 1) == 2),
        }
    out["math_generators"] = len(mathgen.GENERATORS)
    return out


# Share of a 'harder' quiz drawn from the hard tier. The default mode, because
# the core tier alone is easier than the real exam.
HARDER_SHARE = 0.65

DIFFICULTIES = ("harder", "any", "core", "hard")


def _tier(rows, level):
    return [r for r in rows if r.get("difficulty", 1) == level]


def by_difficulty(rows, difficulty):
    """difficulty: 'harder' | 'any' | 'core' | 'hard'.

    Falls back to the full set rather than returning nothing, so a thin topic
    never yields an empty quiz.
    """
    if difficulty == "core":
        return _tier(rows, 1) or rows
    if difficulty == "hard":
        return _tier(rows, 2) or rows
    return rows


# ------------------------------------------------------------------ scoring
def topic_priority(rec, weight):
    """Higher = study this more. Blends exam weight with your miss rate."""
    seen = rec.get("seen", 0) if rec else 0
    correct = rec.get("correct", 0) if rec else 0
    if not seen:
        # never attempted: unknown, so treat as moderately weak
        accuracy = 0.5
        confidence = 0.0
    else:
        accuracy = correct / float(seen)
        confidence = min(1.0, seen / 12.0)
    miss = 1.0 - accuracy
    # unattempted topics get a nudge so they surface, but proven weakness wins
    return (0.35 + 0.65 * confidence) * miss * (1.0 + weight / 10.0)


def weak_weights(progress_topics, declared=None):
    """{topic_key: selection weight} -- weak and heavily-weighted topics dominate.

    Topics you flagged as weak get a boost, so weak-spot mode is useful on day
    one before there is any miss history. The boost shrinks once real data
    exists, letting measured performance take over.
    """
    declared = set(declared or [])
    w = {}
    for key in topics.ORDER:
        rec = (progress_topics or {}).get(key)
        score = 0.05 + topic_priority(rec, topics.weight(key))
        if key in declared:
            seen = rec.get("seen", 0) if rec else 0
            score += 0.60 if seen < 10 else 0.20
        w[key] = score
    return w


# ---------------------------------------------------------------- selection
def _order(rows, missed_ids, rng):
    """Questions you have missed before come first, then everything else."""
    missed = [r for r in rows if r["id"] in missed_ids]
    other = [r for r in rows if r["id"] not in missed_ids]
    rng.shuffle(missed)
    rng.shuffle(other)
    return missed + other


def _pick_from_topic(pool, topic, n, missed_ids, rng, difficulty="any"):
    rows = [r for r in pool if r["topic"] == topic]
    if not rows or n <= 0:
        return []

    if difficulty == "harder":
        # fill a hard quota first, then top up from the core tier
        want_hard = int(round(n * HARDER_SHARE))
        hard = _order(_tier(rows, 2), missed_ids, rng)[:want_hard]
        used = set(r["id"] for r in hard)
        rest = _order([r for r in rows if r["id"] not in used], missed_ids, rng)
        return (hard + rest)[:n]

    return _order(by_difficulty(rows, difficulty), missed_ids, rng)[:n]


def _allocate(counts, total, rng):
    """Turn float weights into integer question counts summing to `total`."""
    keys = [k for k in counts if counts[k] > 0]
    if not keys:
        return {}
    tot = float(sum(counts[k] for k in keys))
    out = {k: int(total * counts[k] / tot) for k in keys}
    short = total - sum(out.values())
    # distribute the remainder by weight, largest first
    for k in sorted(keys, key=lambda x: -counts[x]):
        if short <= 0:
            break
        out[k] += 1
        short -= 1
    return out


def select(portion, count, weak_spot=False, progress=None, topic=None, rng=None,
           difficulty="any", sub=None):
    """Build a quiz.

    `portion` is 'national', 'georgia', 'comprehensive', 'math', or 'mixed'.
    `difficulty` is 'any', 'core', or 'hard'; it filters the written banks and
    is ignored by the math generators, whose difficulty is inherent.
    """
    rng = rng or random.Random()
    progress = progress or {}
    missed_ids = set()
    for qid, rec in (progress.get("items") or {}).items():
        if rec.get("seen", 0) > rec.get("correct", 0):
            missed_ids.add(qid)

    if sub:
        # Drilling one "little topic". Take everything written for it first,
        # then generated problems if it is a math subtopic, then related
        # questions from the parent topic so a short drill is still a full set.
        rows = all_rows()
        pool = [r for r in rows if r.get("sub") == sub]
        rng.shuffle(pool)
        out = pool[:count]
        if len(out) < count:
            gens = [k for k in mathgen.ORDER
                    if sub.endswith("|" + mathgen.TOPICS[k][0])]
            if gens:
                out += mathgen.batch(count - len(out), gens)
        if len(out) < count:
            parent = sub.split("|", 1)[0]
            have = set(r["id"] for r in out)
            rest = [r for r in rows
                    if r["topic"] == parent and r["id"] not in have]
            rng.shuffle(rest)
            out += rest[:count - len(out)]
        return out[:count]

    if portion == "math":
        kinds = [topic] if topic in mathgen.GENERATORS else None
        if weak_spot:
            gt = progress.get("generators") or {}
            scored = []
            for k in mathgen.ORDER:
                rec = gt.get(k)
                scored.append((topic_priority(rec, 5), k))
            scored.sort(reverse=True)
            kinds = [k for _, k in scored[:max(4, len(scored) // 2)]]
        return mathgen.batch(count, kinds)

    if portion == "mixed":
        n_nat = int(round(count * 80 / 132.0))
        return (select("national", n_nat, weak_spot, progress, None, rng, difficulty) +
                select("georgia", count - n_nat, weak_spot, progress, None, rng, difficulty))

    pool = bank(portion)
    if topic:
        chosen = _pick_from_topic(pool, topic, count, missed_ids, rng, difficulty)
        out = list(chosen)
        if topic == "national/math":
            out += mathgen.batch(max(0, count - len(out)))
        elif topic == "comp/closing-math":
            # deliberately blend written debit/credit items with generated
            # arithmetic, since the topic tests both direction and arithmetic
            keep = max(1, count // 2)
            out = out[:keep] + mathgen.batch(count - keep, list(mathgen.CLOSING))
        return out[:count]

    if weak_spot:
        declared = (progress.get("profile") or {}).get("declared_weak")
        weights = weak_weights(progress.get("topics"), declared)
        weights = {k: v for k, v in weights.items() if k in topics.portion_topics(portion)}
    else:
        weights = {k: float(topics.weight(k)) for k in topics.portion_topics(portion)}

    plan = _allocate(weights, count, rng)
    out = []
    for tkey, n in plan.items():
        got = _pick_from_topic(pool, tkey, n, missed_ids, rng, difficulty)
        # the two math topics can always be topped up procedurally
        if len(got) < n and tkey == "national/math":
            got += mathgen.batch(n - len(got))
        elif len(got) < n and tkey == "comp/closing-math":
            got += mathgen.batch(n - len(got), list(mathgen.CLOSING))
        out.extend(got)

    if len(out) < count:
        need = count - len(out)
        if portion == "national":
            out.extend(mathgen.batch(need))
        elif portion == "comprehensive":
            out.extend(mathgen.batch(need, list(mathgen.CLOSING)))
        else:
            rest = [r for r in pool if r not in out]
            rng.shuffle(rest)
            out.extend(rest[:need])

    rng.shuffle(out)
    return out[:count]


def mock_exam(rng=None, difficulty="any"):
    """A full-length practice exam: 80 national + 52 Georgia, exam-weighted.

    The comprehensive subtest is a drill, not a section of the real exam, so it
    is deliberately excluded here.
    """
    rng = rng or random.Random()
    nat = select("national", 80, rng=rng, difficulty=difficulty)
    ga = select("georgia", 52, rng=rng, difficulty=difficulty)
    return nat + ga
