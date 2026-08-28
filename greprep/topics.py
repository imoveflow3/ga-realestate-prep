"""Exam structure: portions, topics, and how many questions each is worth.

Counts mirror the PSI Georgia salesperson exam: 80 scored national questions
and 52 scored state questions (152 total including unscored pretest items).
The per-topic counts are the published content outline weights; they drive
both the mock-exam blueprint and the study scheduler's priorities.
"""

PORTIONS = {
    "national": {
        "name": "National",
        "blurb": "Principles and practices tested in every state.",
        "scored": 80,
        "minutes": 150,
    },
    "georgia": {
        "name": "Georgia state",
        "blurb": "GREC license law, BRRETA, and Georgia procedure.",
        "scored": 52,
        "minutes": 90,
    },
    "comprehensive": {
        "name": "Comprehensive",
        "blurb": "Cross-cutting drill: vocabulary, judgment calls, GREC detail, "
                 "and closing math. Not a section of the real exam.",
        "scored": 0,
        "minutes": 60,
        "practice_only": True,
    },
}

# topic key -> (portion, label, questions on the real exam, study blurb)
TOPICS = {
    "national/ownership": ("national", "Property ownership", 8,
        "Estates, tenancy, condos/co-ops, fixtures, water and air rights."),
    "national/landuse": ("national", "Land use controls", 5,
        "Zoning, deed restrictions, eminent domain, police power, CC&Rs."),
    "national/valuation": ("national", "Valuation & market analysis", 7,
        "The three approaches to value, CMA, appraisal principles."),
    "national/financing": ("national", "Financing", 10,
        "Loan types, points, amortization, TRID/RESPA, qualifying ratios."),
    "national/agency": ("national", "Principles of agency", 8,
        "Fiduciary duties, agency creation and termination, dual agency."),
    "national/disclosures": ("national", "Property condition & disclosures", 6,
        "Material facts, latent defects, lead paint, environmental hazards."),
    "national/contracts": ("national", "Contracts", 13,
        "Formation, contingencies, breach and remedies, assignment."),
    "national/transfer": ("national", "Transfer of title", 8,
        "Deeds, title insurance, recording, closing, adverse possession."),
    "national/practice": ("national", "Practice of real estate", 10,
        "Advertising, fair housing, antitrust, licensing, trust funds."),
    "national/math": ("national", "Real estate math", 5,
        "Commissions, prorations, LTV, points, area, appreciation."),

    "georgia/license-law": ("georgia", "GREC license law & rules", 14,
        "Licensing, renewal, education, GREC authority, sanctions."),
    "georgia/brreta": ("georgia", "Brokerage relationships (BRRETA)", 10,
        "Georgia agency law, engagements, dual and designated agency."),
    "georgia/contracts": ("georgia", "Georgia contracts & forms", 8,
        "Georgia contract requirements, offers, earnest money terms."),
    "georgia/disclosures": ("georgia", "Georgia disclosures", 6,
        "What Georgia requires disclosed, and what it protects."),
    "georgia/trust-accounts": ("georgia", "Trust accounts & earnest money", 4,
        "Designated trust accounts, deadlines, disbursement, records."),
    "georgia/procedures": ("georgia", "Closings, escrow & procedure", 5,
        "Attorney-conducted closings, title, transfer tax, recording."),
    "georgia/fair-housing": ("georgia", "Fair housing in Georgia", 5,
        "Federal and Georgia fair housing as GREC enforces it."),

    # The comprehensive subtest is a study tool, not a section of the exam.
    # Its numbers are drill weights, not exam question counts -- see PRACTICE_ONLY.
    "comp/vocabulary": ("comprehensive", "Vocabulary & terminology", 12,
        "The terms both portions assume you already know."),
    "comp/situational": ("comprehensive", "Situational judgment", 12,
        "You are the licensee -- what do you actually do?"),
    "comp/grec-deep": ("comprehensive", "GREC law deep-dive", 10,
        "The license-law detail the state portion leans on hardest."),
    "comp/closing-math": ("comprehensive", "Closing & settlement math", 8,
        "Debits, credits, prorations, and who pays what at the table."),
}

# Topics that are drills rather than scored sections of the PSI exam. They are
# excluded from the exam blueprint and from the scheduler's exam weighting, and
# the UI never claims they are "worth N on the exam".
PRACTICE_ONLY = set(k for k, v in TOPICS.items() if v[0] == "comprehensive")

DIFFICULTY = {1: "Core", 2: "Hard"}


def counts_on_exam(key):
    return key not in PRACTICE_ONLY


def exam_portions():
    return [p for p in PORTIONS if not PORTIONS[p].get("practice_only")]

ORDER = list(TOPICS.keys())


def portion_topics(portion):
    return [k for k in ORDER if TOPICS[k][0] == portion]


def label(key):
    return TOPICS[key][1] if key in TOPICS else key


def weight(key):
    return TOPICS[key][2] if key in TOPICS else 1


def blueprint(portion, total):
    """Split `total` questions across a portion's topics by exam weight."""
    keys = portion_topics(portion)
    wsum = float(sum(weight(k) for k in keys)) or 1.0
    raw = [(k, total * weight(k) / wsum) for k in keys]
    out = {k: int(v) for k, v in raw}
    # hand out the rounding remainder to the largest fractional parts
    short = total - sum(out.values())
    for k, v in sorted(raw, key=lambda kv: -(kv[1] - int(kv[1]))):
        if short <= 0:
            break
        out[k] += 1
        short -= 1
    return out


def catalog():
    rows = []
    for k in ORDER:
        p, lab, w, blurb = TOPICS[k]
        rows.append({"key": k, "portion": p, "label": lab,
                     "exam_questions": w, "blurb": blurb,
                     "counts_on_exam": counts_on_exam(k)})
    return rows
