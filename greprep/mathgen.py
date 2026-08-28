"""Procedural real estate math problems, each with a worked solution.

Every generator returns the same shape as a bank question, plus `steps`:
an ordered list of "do this -> get that" lines. Distractors are built from
the mistakes people actually make (annual instead of monthly, wrong side of
the closing, list price instead of sale price), not from random noise.
"""
import random

SQFT_PER_ACRE = 43560

# generator key -> (label, concept sentence)
TOPICS = {
    "commission": ("Commission & splits",
        "Commission is always a percentage of the SALE price, then divided between "
        "brokerages and again between each brokerage and its agent."),
    "proration-tax": ("Property tax proration",
        "Prorations divide a shared expense on the calendar. The seller owes through "
        "the day before closing; the buyer owns closing day forward."),
    "proration-rent": ("Rent proration",
        "Rent is collected in advance, so the seller holds money that belongs to the "
        "buyer and is DEBITED for the buyer's share."),
    "ltv": ("Loan-to-value & down payment",
        "LTV = loan / value, where value is the LESSER of appraised value and sale price."),
    "points": ("Discount points",
        "One point is 1% of the LOAN amount -- never of the sale price."),
    "area": ("Square footage & price per sq ft",
        "Break an irregular shape into rectangles, total the areas, then divide."),
    "acreage": ("Acreage conversion",
        "One acre is 43,560 square feet. A section is 640 acres; a mile is 5,280 feet."),
    "appreciation": ("Appreciation & depreciation",
        "Appreciation compounds on the new value each year; straight-line depreciation "
        "takes the same dollar amount off the original basis every year."),
    "interest": ("Interest & amortization",
        "Interest for one month = principal x annual rate / 12. In an amortized loan "
        "the interest portion shrinks as principal is repaid."),
    "seller-net": ("Seller's net & required sale price",
        "To hit a target net, DIVIDE by (100% - commission%). Never just add the "
        "commission percentage back on."),
    "transfer-tax": ("Georgia transfer tax",
        "Georgia's real estate transfer tax is $1.00 per $1,000 of consideration "
        "(0.10%), rounded up to the next full $500 increment above the first $500."),
    "cash-to-close": ("Buyer's cash to close",
        "Cash to close = price + buyer costs - loan - earnest money already paid."),
    "seller-proceeds": ("Seller's net proceeds",
        "Seller proceeds = price - payoff - commission - seller costs, adjusted for prorations."),
    "proration-direction": ("Proration direction (debit or credit)",
        "Unpaid items debit the seller; PREPAID items credit the seller. Ask who has "
        "the money and who will enjoy the benefit."),
    "qualifying": ("Lender qualifying ratios",
        "The front-end ratio is housing expense / gross monthly income; the back-end "
        "ratio adds all recurring monthly debt."),
}

ORDER = list(TOPICS.keys())


def _money(x):
    return "$%s" % format(round(x, 2), ",.2f").replace(".00", "")


def _ord(n):
    """1 -> 1st, 2 -> 2nd, 11 -> 11th, 21 -> 21st."""
    if 10 <= n % 100 <= 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return "%d%s" % (n, suffix)


def _pct(x):
    s = ("%.4f" % x).rstrip("0").rstrip(".")
    return s + "%"


def _pack(key, q, correct, wrongs, steps, fmt=_money):
    """Assemble choices from the right answer plus mistake-based distractors."""
    seen, opts = set(), []
    for v in [correct] + list(wrongs):
        r = round(v, 2)
        if r in seen:
            continue
        seen.add(r)
        opts.append(v)
    while len(opts) < 4:                       # pad if a distractor collided
        bump = correct * random.choice([0.85, 1.15, 1.25, 0.75])
        if round(bump, 2) not in seen:
            seen.add(round(bump, 2))
            opts.append(bump)
    opts = opts[:4]
    random.shuffle(opts)
    label, concept = TOPICS[key]
    closing = key in ("cash-to-close", "seller-proceeds", "proration-direction")
    return {
        "id": "math:%s:%d" % (key, random.randrange(10 ** 9)),
        "portion": "comprehensive" if closing else "national",
        "topic": "comp/closing-math" if closing else "national/math",
        "generator": key,
        "q": q,
        "choices": [fmt(o) for o in opts],
        "answer": opts.index(correct),
        "concept": concept,
        "explain": "Correct answer: %s. %s" % (fmt(correct), concept),
        "steps": steps,
    }


# ------------------------------------------------------------------ generators
def commission():
    price = random.randrange(180, 720) * 1000
    rate = random.choice([5, 5.5, 6, 7])
    co_op = random.choice([50, 50, 60, 40])
    agent = random.choice([50, 60, 70])
    total = price * rate / 100.0
    listing_side = total * co_op / 100.0
    agent_cut = listing_side * agent / 100.0
    q = ("A home sells for %s with a %s total commission. The listing brokerage keeps "
         "%d%% of the commission and pays the rest to the cooperating brokerage. The "
         "listing agent's split with their own broker is %d%% to the agent. How much "
         "does the LISTING AGENT receive?" % (_money(price), _pct(rate), co_op, agent))
    steps = [
        "Total commission = sale price x rate = %s x %s = %s"
        % (_money(price), _pct(rate), _money(total)),
        "Listing brokerage's share = %s x %d%% = %s"
        % (_money(total), co_op, _money(listing_side)),
        "Listing agent's share = %s x %d%% = %s"
        % (_money(listing_side), agent, _money(agent_cut)),
    ]
    return _pack("commission", q, agent_cut,
                 [total, listing_side, total * agent / 100.0], steps)


def proration_tax():
    annual = random.randrange(1800, 7200, 60)
    month = random.randrange(2, 12)
    day = random.randrange(2, 28)
    names = ["January", "February", "March", "April", "May", "June", "July",
             "August", "September", "October", "November", "December"]
    days_through = (month - 1) * 30 + (day - 1)      # 360-day year, seller through day before
    daily = annual / 360.0
    seller = daily * days_through
    buyer = annual - seller
    q = ("Annual property taxes are %s and have NOT yet been paid. Closing is %s %d. "
         "Using a 360-day banker's year with the seller responsible through the day "
         "before closing, what is the SELLER's share (debited to the seller)?"
         % (_money(annual), names[month - 1], day))
    steps = [
        "Daily tax = %s / 360 = %s per day" % (_money(annual), _money(daily)),
        "Seller's days = %d full months x 30 + %d days = %d days"
        % (month - 1, day - 1, days_through),
        "Seller's share = %s x %d = %s" % (_money(daily), days_through, _money(seller)),
        "Check: buyer picks up the rest, %s - %s = %s"
        % (_money(annual), _money(seller), _money(buyer)),
    ]
    return _pack("proration-tax", q, seller,
                 [buyer, daily * (days_through + 1), annual / 2.0], steps)


def proration_rent():
    rent = random.randrange(900, 3200, 25)
    day = random.randrange(5, 27)
    days_in = 30
    daily = rent / float(days_in)
    buyer_days = days_in - day + 1        # buyer owns closing day forward
    buyer_share = daily * buyer_days
    q = ("A rental property collects %s in rent on the first of a 30-day month. The sale "
         "closes on the %s, and the buyer owns the property beginning on the day of "
         "closing. How much rent is credited to the BUYER at closing?"
         % (_money(rent), _ord(day)))
    steps = [
        "Daily rent = %s / 30 = %s per day" % (_money(rent), _money(daily)),
        "Buyer owns the %s through the 30th = %d days" % (_ord(day), buyer_days),
        "Buyer's credit = %s x %d = %s" % (_money(daily), buyer_days, _money(buyer_share)),
        "The seller already has this cash, so it is a seller DEBIT / buyer CREDIT.",
    ]
    return _pack("proration-rent", q, buyer_share,
                 [rent - buyer_share, daily * (buyer_days - 1), rent / 2.0], steps)


def ltv():
    price = random.randrange(150, 600) * 1000
    appraised = price - random.choice([0, 0, 5000, 10000, 15000])
    ltv_pct = random.choice([80, 85, 90, 95])
    basis = min(price, appraised)
    loan = basis * ltv_pct / 100.0
    down = price - loan
    q = ("A buyer agrees to pay %s for a home that appraises at %s. The lender will make "
         "a %d%% LTV loan. How much cash must the buyer put down?"
         % (_money(price), _money(appraised), ltv_pct))
    steps = [
        "Lenders lend on the LESSER of sale price or appraised value = %s" % _money(basis),
        "Loan = %s x %d%% = %s" % (_money(basis), ltv_pct, _money(loan)),
        "Down payment = sale price - loan = %s - %s = %s"
        % (_money(price), _money(loan), _money(down)),
    ]
    return _pack("ltv", q, down,
                 [price * (100 - ltv_pct) / 100.0, loan,
                  appraised * (100 - ltv_pct) / 100.0], steps)


def points():
    price = random.randrange(160, 560) * 1000
    ltv_pct = random.choice([80, 90, 95])
    pts = random.choice([1, 1.5, 2, 2.5, 3])
    loan = price * ltv_pct / 100.0
    cost = loan * pts / 100.0
    q = ("A buyer purchases a %s home with a %d%% LTV loan and pays %s discount points. "
         "What do the points cost at closing?" % (_money(price), ltv_pct, pts))
    steps = [
        "Loan amount = %s x %d%% = %s" % (_money(price), ltv_pct, _money(loan)),
        "One point = 1%% of the LOAN = %s" % _money(loan * 0.01),
        "%s points = %s x %s%% = %s" % (pts, _money(loan), pts, _money(cost)),
    ]
    return _pack("points", q, cost,
                 [price * pts / 100.0, loan * 0.01, cost * 2], steps)


def area():
    a_w, a_l = random.randrange(20, 45), random.randrange(30, 60)
    b_w, b_l = random.randrange(10, 25), random.randrange(12, 30)
    total = a_w * a_l + b_w * b_l
    price = total * random.randrange(95, 240)
    ppsf = price / float(total)
    q = ("A house is an L shape: the main section is %d ft x %d ft and the wing is "
         "%d ft x %d ft. The house is listed at %s. What is the price per square foot?"
         % (a_w, a_l, b_w, b_l, _money(price)))
    steps = [
        "Main section = %d x %d = %s sq ft" % (a_w, a_l, format(a_w * a_l, ",")),
        "Wing = %d x %d = %s sq ft" % (b_w, b_l, format(b_w * b_l, ",")),
        "Total = %s sq ft" % format(total, ","),
        "Price per sq ft = %s / %s = %s" % (_money(price), format(total, ","), _money(ppsf)),
    ]
    return _pack("area", q, ppsf, [price / (a_w * a_l), ppsf * 2, ppsf / 2.0], steps)


def acreage():
    acres = random.choice([0.25, 0.5, 0.75, 1.5, 2.0, 2.5, 5.0])
    per_acre = random.randrange(12, 60) * 1000
    sq = acres * SQFT_PER_ACRE
    value = acres * per_acre
    q = ("A parcel contains %s square feet and comparable land sells for %s per acre. "
         "What is the parcel worth?" % (format(int(sq), ","), _money(per_acre)))
    steps = [
        "Acres = %s sq ft / 43,560 = %s acres" % (format(int(sq), ","), acres),
        "Value = %s acres x %s = %s" % (acres, _money(per_acre), _money(value)),
    ]
    return _pack("acreage", q, value,
                 [per_acre, value * 2, sq * 0.1], steps)


def appreciation():
    start = random.randrange(150, 500) * 1000
    rate = random.choice([3, 4, 5, 6])
    years = random.choice([2, 3, 4])
    val = start * (1 + rate / 100.0) ** years
    simple = start * (1 + rate * years / 100.0)
    q = ("A property bought for %s appreciates %d%% per year, COMPOUNDED, for %d years. "
         "What is it worth at the end?" % (_money(start), rate, years))
    steps = ["Year 0 value = %s" % _money(start)]
    running = start
    for y in range(1, years + 1):
        running *= (1 + rate / 100.0)
        steps.append("Year %d = previous x 1.%02d = %s" % (y, rate, _money(running)))
    steps.append("Compounding is applied to the NEW value each year, not the original.")
    return _pack("appreciation", q, val, [simple, start * rate / 100.0, val * 0.9], steps)


def interest():
    loan = random.randrange(120, 480) * 1000
    rate = random.choice([5.5, 6, 6.5, 7, 7.5])
    monthly = loan * (rate / 100.0) / 12
    q = ("A borrower owes %s on a loan at %s annual interest. How much of the NEXT "
         "monthly payment is interest?" % (_money(loan), _pct(rate)))
    steps = [
        "Annual interest = %s x %s = %s" % (_money(loan), _pct(rate), _money(loan * rate / 100.0)),
        "Monthly interest = %s / 12 = %s" % (_money(loan * rate / 100.0), _money(monthly)),
        "Only the interest portion is asked for -- principal is whatever the payment "
        "exceeds this.",
    ]
    return _pack("interest", q, monthly,
                 [loan * rate / 100.0, monthly / 2.0, monthly * 2], steps)


def seller_net():
    net = random.randrange(180, 520) * 1000
    costs = random.randrange(2, 9) * 1000
    rate = random.choice([5, 6, 7])
    price = (net + costs) / (1 - rate / 100.0)
    wrong = (net + costs) * (1 + rate / 100.0)
    q = ("A seller wants to net %s after paying %s in closing costs and a %s commission. "
         "What must the property sell for?" % (_money(net), _money(costs), _pct(rate)))
    steps = [
        "Seller must clear net + costs = %s + %s = %s"
        % (_money(net), _money(costs), _money(net + costs)),
        "That amount is the %d%% of the price left after commission" % (100 - rate),
        "Price = %s / 0.%02d = %s" % (_money(net + costs), 100 - rate, _money(price)),
        "Adding %s back on instead gives %s -- that is the classic wrong answer."
        % (_pct(rate), _money(wrong)),
    ]
    return _pack("seller-net", q, price, [wrong, net + costs, net / (1 - rate / 100.0)], steps)


def transfer_tax():
    price = random.randrange(120, 640) * 1000
    tax = price / 1000.0 * 1.00
    q = ("A Georgia property sells for %s. At $1.00 per $1,000 of consideration, what is "
         "the Georgia real estate transfer tax?" % _money(price))
    steps = [
        "Georgia transfer tax = $1.00 per $1,000 of consideration (0.10%).",
        "%s / 1,000 = %s thousands" % (_money(price), format(price / 1000.0, ",.1f")),
        "Tax = %s x $1.00 = %s" % (format(price / 1000.0, ",.1f"), _money(tax)),
        "The tax is paid by the SELLER and collected by the clerk of superior court.",
    ]
    return _pack("transfer-tax", q, tax, [tax * 10, tax / 10.0, price * 0.01], steps)


def qualifying():
    income = random.randrange(48, 145) * 1000
    front = random.choice([28, 31])
    gross_mo = income / 12.0
    allowed = gross_mo * front / 100.0
    q = ("A buyer earns %s per year. Using a %d%% front-end (housing) ratio, what is the "
         "maximum monthly PITI payment the lender will allow?" % (_money(income), front))
    steps = [
        "Gross monthly income = %s / 12 = %s" % (_money(income), _money(gross_mo)),
        "Maximum housing payment = %s x %d%% = %s" % (_money(gross_mo), front, _money(allowed)),
        "The front-end ratio counts PITI only; the back-end ratio adds car loans, "
        "student loans, and credit cards.",
    ]
    return _pack("qualifying", q, allowed,
                 [income * front / 100.0, gross_mo, allowed * 1.3], steps)


def cash_to_close():
    price = random.randrange(180, 620) * 1000
    ltv_pct = random.choice([80, 90, 95])
    earnest = random.choice([2, 3, 5, 10]) * 1000
    costs = random.randrange(4, 12) * 1000
    loan = price * ltv_pct / 100.0
    cash = price + costs - loan - earnest
    q = ("A buyer purchases for %s with a %d%% LTV loan. Closing costs charged to the "
         "buyer total %s, and %s of earnest money is already on deposit. How much must "
         "the buyer bring to closing?"
         % (_money(price), ltv_pct, _money(costs), _money(earnest)))
    steps = [
        "Loan = %s x %d%% = %s" % (_money(price), ltv_pct, _money(loan)),
        "Buyer debits = price + costs = %s + %s = %s"
        % (_money(price), _money(costs), _money(price + costs)),
        "Buyer credits = loan + earnest money = %s + %s = %s"
        % (_money(loan), _money(earnest), _money(loan + earnest)),
        "Cash to close = debits - credits = %s - %s = %s"
        % (_money(price + costs), _money(loan + earnest), _money(cash)),
    ]
    return _pack("cash-to-close", q, cash,
                 [price - loan, cash + earnest, price + costs - loan], steps)


def seller_proceeds():
    price = random.randrange(200, 700) * 1000
    payoff = int(price * random.uniform(0.35, 0.72) / 1000) * 1000
    rate = random.choice([5, 6, 7])
    costs = random.randrange(2, 9) * 1000
    comm = price * rate / 100.0
    net = price - payoff - comm - costs
    q = ("A home sells for %s. The seller's loan payoff is %s, the commission is %s, and "
         "the seller owes %s in other closing costs. What are the seller's net proceeds?"
         % (_money(price), _money(payoff), _pct(rate), _money(costs)))
    steps = [
        "Commission = %s x %s = %s" % (_money(price), _pct(rate), _money(comm)),
        "Seller debits = payoff + commission + costs = %s + %s + %s = %s"
        % (_money(payoff), _money(comm), _money(costs), _money(payoff + comm + costs)),
        "Net = price - debits = %s - %s = %s"
        % (_money(price), _money(payoff + comm + costs), _money(net)),
    ]
    return _pack("seller-proceeds", q, net,
                 [price - payoff, price - comm - costs, net - costs], steps)


def proration_direction():
    """A direction question -- the answer is a phrase, not a dollar amount."""
    annual = random.randrange(1800, 7200, 120)
    month = random.randrange(3, 11)
    prepaid = random.choice([True, False])
    names = ["January", "February", "March", "April", "May", "June", "July",
             "August", "September", "October", "November", "December"]
    daily = annual / 360.0
    seller_days = (month - 1) * 30
    amount = daily * seller_days
    if prepaid:
        correct = "Seller credit / buyer debit of %s" % _money(annual - amount)
        wrongs = ["Seller debit / buyer credit of %s" % _money(annual - amount),
                  "Seller credit / buyer debit of %s" % _money(amount),
                  "Seller debit / buyer credit of %s" % _money(amount)]
        steps = [
            "Taxes are PREPAID, so the seller has already paid for time the buyer will own.",
            "Daily = %s / 360 = %s" % (_money(annual), _money(daily)),
            "Seller owned %d days; the buyer's remaining share is %s - %s = %s"
            % (seller_days, _money(annual), _money(amount), _money(annual - amount)),
            "The seller is reimbursed: seller CREDIT, buyer DEBIT.",
        ]
    else:
        correct = "Seller debit / buyer credit of %s" % _money(amount)
        wrongs = ["Seller credit / buyer debit of %s" % _money(amount),
                  "Seller debit / buyer credit of %s" % _money(annual - amount),
                  "Seller credit / buyer debit of %s" % _money(annual - amount)]
        steps = [
            "Taxes are UNPAID, so the seller owes for the time they owned.",
            "Daily = %s / 360 = %s" % (_money(annual), _money(daily)),
            "Seller's share = %s x %d days = %s" % (_money(daily), seller_days, _money(amount)),
            "The buyer will pay the whole bill later: seller DEBIT, buyer CREDIT.",
        ]
    q = ("Annual property taxes are %s and are %s. Closing is %s 1 in a 360-day year, "
         "with the seller responsible through the day before closing. How does this "
         "appear on the settlement statement?"
         % (_money(annual), "already PAID in full" if prepaid else "UNPAID", names[month - 1]))
    opts = [correct] + wrongs
    random.shuffle(opts)
    label, concept = TOPICS["proration-direction"]
    return {
        "id": "math:proration-direction:%d" % random.randrange(10 ** 9),
        "portion": "comprehensive", "topic": "comp/closing-math",
        "generator": "proration-direction", "q": q, "choices": opts,
        "answer": opts.index(correct), "concept": concept,
        "explain": "Correct answer: %s. %s" % (correct, concept),
        "steps": steps,
    }


GENERATORS = {
    "commission": commission, "proration-tax": proration_tax,
    "proration-rent": proration_rent, "ltv": ltv, "points": points,
    "area": area, "acreage": acreage, "appreciation": appreciation,
    "interest": interest, "seller-net": seller_net,
    "transfer-tax": transfer_tax, "qualifying": qualifying,
    "cash-to-close": cash_to_close, "seller-proceeds": seller_proceeds,
    "proration-direction": proration_direction,
}

# generators whose output belongs to the comprehensive subtest's closing topic
CLOSING = ("cash-to-close", "seller-proceeds", "proration-direction")


def make(kind=None):
    if kind not in GENERATORS:
        kind = random.choice(ORDER)
    return GENERATORS[kind]()


def batch(n, kinds=None):
    pool = [k for k in (kinds or ORDER) if k in GENERATORS] or ORDER
    out, spin = [], list(pool)
    random.shuffle(spin)
    for i in range(n):
        if not spin:
            spin = list(pool)
            random.shuffle(spin)
        out.append(make(spin.pop()))
    return out
