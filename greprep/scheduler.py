"""Study schedule generator.

You give it an exam date (and optionally a date you want to be "done" by).
It divides the runway into three phases, allocates study effort across topics
using the real exam weighting -- 80 national questions vs 52 Georgia -- and
pushes your weakest topics to the front.
"""
import datetime
import math

from . import questions, topics

NATIONAL_Q = 80
GEORGIA_Q = 52
TOTAL_Q = NATIONAL_Q + GEORGIA_Q


def _date(value):
    if not value:
        return None
    if isinstance(value, datetime.date):
        return value
    try:
        return datetime.datetime.strptime(str(value)[:10], "%Y-%m-%d").date()
    except ValueError:
        return None


def portion_share():
    return {"national": NATIONAL_Q / float(TOTAL_Q),
            "georgia": GEORGIA_Q / float(TOTAL_Q)}


def priorities(progress, declared_weak=None):
    """Rank every topic. Declared weak areas get a boost until data exists."""
    declared = set(declared_weak or [])
    rows = []
    for key in topics.ORDER:
        if key in topics.PRACTICE_ONLY:
            continue          # the comprehensive subtest is a drill, not an exam section
        portion, label, weight, blurb = topics.TOPICS[key]
        rec = (progress.get("topics") or {}).get(key)
        score = questions.topic_priority(rec, weight)
        if key in declared:
            score += 0.45 if not rec else 0.20
        seen = rec.get("seen", 0) if rec else 0
        corr = rec.get("correct", 0) if rec else 0
        rows.append({
            "topic": key, "portion": portion, "label": label, "blurb": blurb,
            "exam_questions": weight, "declared_weak": key in declared,
            "seen": seen, "pct": (corr / float(seen)) if seen else None,
            "score": round(score, 4),
        })
    rows.sort(key=lambda r: -r["score"])
    return rows


def _phase_plan(n_weeks):
    """Return a phase label per week index."""
    if n_weeks <= 1:
        return ["Drill & mock"]
    if n_weeks == 2:
        return ["Weak-area drill", "Mock exams & review"]
    if n_weeks == 3:
        return ["Weak-area drill", "Full coverage", "Mock exams & review"]
    build = max(1, int(round(n_weeks * 0.45)))
    drill = max(1, int(round(n_weeks * 0.35)))
    final = max(1, n_weeks - build - drill)
    return (["Build coverage"] * build + ["Weak-area drill"] * drill +
            ["Mock exams & review"] * final)[:n_weeks]


def generate(progress, exam_date, mastery_date=None, declared_weak=None,
             hours_per_week=8, today=None):
    today = today or datetime.date.today()
    exam = _date(exam_date)
    mastery = _date(mastery_date) or exam
    if exam and mastery and mastery > exam:
        mastery = exam

    ranked = priorities(progress, declared_weak)
    share = portion_share()

    if not exam:
        return {"error": "Set an exam date to generate a schedule."}

    days_to_exam = (exam - today).days
    days_to_mastery = (mastery - today).days if mastery else days_to_exam
    plan_days = max(1, days_to_mastery)
    n_weeks = max(1, int(math.ceil(plan_days / 7.0)))
    phases = _phase_plan(n_weeks)

    # how many topics to feature per week, and which
    weak_first = [r for r in ranked]
    nat = [r for r in weak_first if r["portion"] == "national"]
    ga = [r for r in weak_first if r["portion"] == "georgia"]

    weeks = []
    cursor = today
    n_focus_nat = max(2, int(round(3 * share["national"])) + 1)
    n_focus_ga = max(2, int(round(3 * share["georgia"])) + 1)
    nat_i = ga_i = 0

    for i in range(n_weeks):
        start = cursor
        end = min(mastery or exam, start + datetime.timedelta(days=6))
        phase = phases[i]

        if phase == "Mock exams & review":
            focus = (nat[:2] + ga[:2])          # weakest overall, revisited
            tasks = [
                "Take one FULL mock exam (132 questions, National + Georgia).",
                "Review every miss and write the rule in your own words.",
                "Run Weak-spot mode twice on whatever the mock exposes.",
                "Do one 15-question math sprint daily.",
                "One 20-question Comprehensive set for vocabulary and judgment calls.",
            ]
        elif phase == "Weak-area drill":
            focus = []
            for _ in range(n_focus_nat):
                focus.append(nat[nat_i % len(nat)]); nat_i += 1
            for _ in range(n_focus_ga):
                focus.append(ga[ga_i % len(ga)]); ga_i += 1
            tasks = [
                "Weak-spot quiz, 20 questions, once per study day.",
                "Two 20-question topic quizzes on the focus topics below.",
                "Math practice mode: 10 problems daily, read every solution.",
                "Comprehensive subtest: 15 questions, situational judgment focus.",
            ]
        else:
            focus = []
            for _ in range(n_focus_nat):
                focus.append(nat[nat_i % len(nat)]); nat_i += 1
            for _ in range(n_focus_ga):
                focus.append(ga[ga_i % len(ga)]); ga_i += 1
            tasks = [
                "One 20-question quiz per focus topic below.",
                "One 25-question National quiz to keep breadth.",
                "Math practice mode: 10 problems, 3x this week.",
                "One Comprehensive set (vocabulary, judgment, closing math).",
            ]

        # split the week's question budget the way the exam splits
        weekly_q = int(hours_per_week * 25)      # ~25 questions per study hour
        weeks.append({
            "week": i + 1,
            "phase": phase,
            "start": start.isoformat(),
            "end": end.isoformat(),
            "target_questions": weekly_q,
            "national_questions": int(round(weekly_q * share["national"])),
            "georgia_questions": int(round(weekly_q * share["georgia"])),
            "focus": [{"topic": r["topic"], "label": r["label"],
                       "portion": r["portion"], "why": _why(r)} for r in focus],
            "tasks": tasks,
        })
        cursor = end + datetime.timedelta(days=1)
        if mastery and cursor > mastery:
            break

    buffer_days = (exam - mastery).days if mastery else 0
    return {
        "exam_date": exam.isoformat(),
        "mastery_date": mastery.isoformat() if mastery else None,
        "today": today.isoformat(),
        "days_to_exam": days_to_exam,
        "days_to_mastery": days_to_mastery,
        "buffer_days": buffer_days,
        "weeks": weeks,
        "weighting": {"national": NATIONAL_Q, "georgia": GEORGIA_Q,
                      "national_pct": round(share["national"] * 100, 1),
                      "georgia_pct": round(share["georgia"] * 100, 1)},
        "ranked": ranked[:8],
        "buffer_plan": _buffer_plan(buffer_days),
    }


def _why(row):
    if row["pct"] is not None and row["seen"] >= 4:
        return "you are at %d%% here (%d questions), worth %d on the exam" % (
            round(row["pct"] * 100), row["seen"], row["exam_questions"])
    if row["declared_weak"]:
        return "you flagged this as a weak area; worth %d on the exam" % row["exam_questions"]
    if not row["seen"]:
        return "no data yet -- worth %d questions on the exam" % row["exam_questions"]
    return "only %d questions attempted; worth %d on the exam" % (
        row["seen"], row["exam_questions"])


def _buffer_plan(days):
    if days <= 0:
        return []
    out = ["Light review only -- no new material."]
    if days >= 2:
        out.append("One 132-question mock exam, timed, at your real exam time of day.")
    if days >= 3:
        out.append("Re-read every explanation you missed on the last two mocks.")
    out.append("Day before: 20-question math sprint, then stop. Sleep beats cramming.")
    return out
