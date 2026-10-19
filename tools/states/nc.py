"""North Carolina state content: lessons and practice questions.

North Carolina splits the examination the way most states do: 80 scored
national items and 60 scored state items, each section scored separately
and each needing a score of 75. The state section's eight categories and
their item counts below are the Commission's own published outline.

North Carolina has one quirk worth holding on to: there is only ONE kind
of licence, a BROKER licence, and a newcomer holds it on "provisional"
status. There is no salesperson licence.

Every rule below was read from the official text on 2026-10-18:
  - N.C. General Statutes chapter 93A (the Real Estate License Law), from
    ncleg.gov, together with chapters 42 (tenant security deposits), 47E
    (residential property disclosure) and 105 (the excise tax).
  - "North Carolina Real Estate License Law and Commission Rules", the
    Commission's own commentary on the rules in 21 NCAC 58A.
  - "Real Estate Licensing in North Carolina" (April 2026), the Commission
    and Pearson VUE handbook, for the blueprint, the pass mark and the
    education requirements.
The section a fact comes from is cited next to it. Do not add a fact here
without reading its source first.
"""

EXAM = {
    # Handbook: 80 scored national + 5 pretest; 60 scored state + 5 pretest.
    # "The passing score for each of the two sections is 75 and is computed
    # separately for each exam section."
    "state_scored": 60,
    "state_minutes": 120,
    "national_scored": 80,
    "national_minutes": 150,
    "pass": 0.75,
}

# The Commission's published state-section outline, category by category.
TOPICS = [
    ("nc/agency", "Agency", 16,
     "Working With Real Estate Agents, written agreements, dual and designated agency."),
    ("nc/practice", "Brokerage practice", 12,
     "Trust money, the three-banking-day rule, advertising and records."),
    ("nc/other", "Other NC laws", 11,
     "Residential property disclosure, mineral rights, fair housing, the Recovery Fund."),
    ("nc/contracts", "Contracts & closing", 7,
     "Agency agreements, offers, and what the closing statement must show."),
    ("nc/supervision", "Supervision & compensation", 4,
     "The broker-in-charge, provisional brokers, and who may be paid."),
    ("nc/taxes", "Taxes & insurance", 4,
     "The excise tax, property tax, and insurance in a transaction."),
    ("nc/licensure", "Licensure", 3,
     "One licence, provisional status, and the education that lifts it."),
    ("nc/landlord", "Landlord & tenant", 3,
     "The Tenant Security Deposit Act and its deadlines."),
]

SOURCES = [
    {"by": "North Carolina General Assembly",
     "name": "N.C. General Statutes chapter 93A (Real Estate License Law)",
     "note": "The licence law itself, including the Real Estate Education and Recovery Fund.",
     "url": "https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/ByChapter/Chapter_93A.html"},
    {"by": "North Carolina Real Estate Commission",
     "name": "License Law and Commission Rules (with the Commission's comments)",
     "note": "The Commission's own commentary on the rules in 21 NCAC 58A. Agency, trust money and brokerage practice here were read from it.",
     "url": "https://www.ncrec.gov/Resources/LicenseLaw"},
    {"by": "NCREC and Pearson VUE",
     "name": "Real Estate Licensing in North Carolina (April 2026)",
     "note": "The blueprint: 80 national and 60 state scored items, a score of 75 on each, and the education requirements.",
     "url": "https://www.ncrec.gov/Pdfs/Licensing/RELINC.pdf"},
    {"by": "North Carolina General Assembly",
     "name": "N.C.G.S. chapters 42, 47E and 105",
     "note": "Tenant security deposits, the residential property and mineral rights disclosures, and the excise tax.",
     "url": "https://www.ncleg.gov/Laws/GeneralStatutesTOC"},
]


# --------------------------------------------------------------- lessons

STUDY = {}

STUDY["nc/agency"] = {
    "summary": "Sixteen of the sixty state items, more than any other category. North Carolina runs on one form handed over at first substantial contact, written agreements with every seller, and dual agency that needs express written authority.",
    "sections": [
        {"h": "Working With Real Estate Agents, at first substantial contact",
         "p": ["At FIRST SUBSTANTIAL CONTACT with a prospective buyer or seller, a broker must provide the WORKING WITH REAL ESTATE AGENTS disclosure, REVIEW ITS CONTENTS with them, and reach agreement about the relationship. Handing over the form to read is NOT enough. The broker puts their own name and licence number on the form (Rule A.0104)."],
         "l": ["A seller's agent or subagent must also disclose their agency status IN WRITING to a prospective buyer at first substantial contact (Rule A.0104(e)).",
               "With a prospective SELLER the broker may act as the seller's agent - which needs a written agreement from the outset - or may work with them as a buyer's agent if they already represent a buyer.",
               "With a prospective BUYER the broker may act as the buyer's agent under an oral or written agreement, or may work with them as the seller's agent, which must be disclosed in writing from the outset."],
         "check": [("The Working With Real Estate Agents disclosure is given:", "At first substantial contact", ["At the closing table", "When an offer is written"], "Rule A.0104."),
                   ("Providing the form satisfies the rule only if the broker also:", "Reviews its contents and reaches agreement on the relationship", ["Files a copy with the Commission", "Has it notarised"], "Handing it over is not enough."),
                   ("A seller's agent meeting an unrepresented buyer must disclose agency status:", "In writing, at first substantial contact", ["Orally, at the first showing", "Only if the buyer asks"], "Rule A.0104(e).")]},
        {"h": "Agency agreements must be in writing - with one exception",
         "l": ["Every agency agreement for brokerage services, in sales AND leases, must be IN WRITING and SIGNED by the parties (G.S. 93A-13; Rule A.0104(a)).",
               "With a PROPERTY OWNER - seller or landlord, any property type - the agreement must be in writing BEFORE the broker provides any services.",
               "With a BUYER or TENANT an EXPRESS ORAL agreement is allowed at the outset, but it must be reduced to writing NO LATER THAN the time any party makes an OFFER.",
               "That oral buyer agreement must be NON-EXCLUSIVE, for an INDEFINITE period, and terminable by the client at any time. If it limits the client's right to work with other agents, or binds them for a definite period, it must be written from the outset.",
               "Every written agency agreement must state a DEFINITE PERIOD and end without notice at its expiry. The one exception is an agreement with a landlord to procure tenants, which may renew automatically if the landlord can terminate."],
         "check": [("An agency agreement with a seller must be in writing:", "Before the broker provides any services", ["Within ten days", "Before closing"], "Rule A.0104(a)."),
                   ("An oral buyer agency agreement must be reduced to writing:", "No later than the time any party makes an offer", ["Within 30 days", "At closing"], "Rule A.0104(a)."),
                   ("An oral buyer agency agreement must be:", "Non-exclusive, indefinite and terminable at any time", ["Exclusive for 90 days", "Witnessed by the broker-in-charge"], "Otherwise it must be written from the outset."),
                   ("A written agency agreement must:", "State a definite period and end without notice at its expiry", ["Renew automatically", "Run for at least six months"], "Landlord tenant-procurement agreements are the exception.")]},
        {"h": "Dual agency and designated agency",
         "l": ["G.S. 93A-6(a)(4) forbids acting for more than one party in a transaction WITHOUT THE KNOWLEDGE of all parties for whom the broker acts.",
               "Rule A.0104(d) and (i) go further: a broker or firm representing one party may not undertake to represent another party in the same transaction without the EXPRESS WRITTEN AUTHORITY of each party.",
               "A dual agent must stay COMPLETELY NEUTRAL AND IMPARTIAL; advocacy for either client is lost.",
               "DESIGNATED AGENCY (Rule A.0104(j)-(m)) lets a firm appoint one agent to represent only the seller and another to represent only the buyer in an in-house dual agency. Each client then gets an advocate again.",
               "Authority to practise designated agency must be IN WRITING no later than the time a written dual agency agreement is required."],
         "check": [("A firm may represent both buyer and seller only with:", "The express written authority of each party", ["Verbal consent from one party", "The broker-in-charge's approval"], "Rule A.0104(d)."),
                   ("A standard dual agent must:", "Remain completely neutral and impartial", ["Advocate for the seller", "Advocate for whoever pays"], "Advocacy is the thing dual agency gives up."),
                   ("Designated agency differs from standard dual agency because:", "Each client keeps an advocate in their designated agent", ["It needs no written authority", "It is used only in leases"], "Rule A.0104(j)-(m).")]},
    ],
    "traps": [
        "First substantial contact, and the broker must REVIEW the form, not just hand it over.",
        "Sellers: written before any services. Buyers: oral allowed, written by the time of an offer.",
        "An oral buyer agreement must be non-exclusive and indefinite - otherwise it must be written at once.",
        "Dual agency needs EXPRESS WRITTEN authority from each party, not mere knowledge.",
    ],
    "vocab": [
        ["First substantial contact", "When the Working With Real Estate Agents disclosure is due."],
        ["WWREA", "The Working With Real Estate Agents disclosure form."],
        ["Dual agency", "Representing both parties; neutral, and needing express written authority."],
        ["Designated agency", "In-house dual agency with a separate agent appointed to each client."],
        ["Subagent", "An agent of the seller through the listing firm."],
    ],
    "examples": [
        {"t": "The oral buyer agreement",
         "s": "A broker agrees orally to help a buyer, shows four homes, and the buyer wants to make an offer.",
         "w": ["An oral buyer agency agreement is permitted at the outset.",
               "It must be reduced to writing no later than the time any party makes an offer."],
         "k": "The agreement must be put in writing before that offer goes in."},
    ],
}

STUDY["nc/practice"] = {
    "summary": "Twelve items, and most of them are about other people's money. Three banking days is the rule, but when the clock starts depends on whether the money is earnest money, a security deposit, or cash.",
    "sections": [
        {"h": "What trust money is",
         "p": ["TRUST MONEY is money belonging to others received by a broker acting as an agent, and any money a licensee holds as temporary custodian for someone else - even where that is only collateral to the brokerage role."],
         "l": ["Earnest money deposits", "Down payments", "Tenant security deposits",
               "Rents", "Homeowner association dues and assessments",
               "Money received from final settlements",
               "For short-term and resort rentals: advance reservation deposits, and the sales taxes on gross receipts"],
         "check": [("Which is trust money?", "A tenant's security deposit", ["The broker's earned commission after disbursement", "The firm's advertising budget"], "Money belonging to others."),
                   ("A listing agent receives money from an out-of-town seller for yard maintenance. That money is:", "Trust money", ["The broker's own money", "Exempt because it is not a sale"], "It is held for another, even if collateral to the brokerage.")]},
        {"h": "The three-banking-day rule",
         "l": ["The general rule: trust money must be deposited within THREE BANKING DAYS OF RECEIPT.",
               "EXCEPTION - earnest money received with an offer to purchase, and tenant security deposits with a lease, go in not later than three banking days following ACCEPTANCE of the offer or lease.",
               "EXCEPTION TO THE EXCEPTION - if the deposit is tendered in CASH, it must be deposited within three banking days of RECEIPT, even if nothing has been accepted. Cash is immediately available and can be refunded at once; cheques may need days to clear.",
               "A broker MAY choose to deposit a cheque at once and need not wait for acceptance, unless the buyer or tenant has instructed otherwise.",
               "A PROVISIONAL BROKER who receives trust money must deliver it IMMEDIATELY to their broker-in-charge; they may not hold it any longer than it takes to hand it over (Rule A.0116(b); A.1808)."],
         "check": [("Earnest money paid by cheque with an offer must be deposited within three banking days of:", "Acceptance of the offer", ["Receipt of the cheque", "Closing"], "Unless the buyer instructs otherwise."),
                   ("Earnest money tendered in CASH must be deposited within three banking days of:", "Receipt, even if the offer has not been accepted", ["Acceptance", "The end of the month"], "Cash is immediately available."),
                   ("A provisional broker who receives a deposit must:", "Deliver it immediately to the broker-in-charge", ["Hold it until closing", "Deposit it in their own account"], "Rule A.0116(b)."),
                   ("The date of acceptance matters because:", "It starts the three-banking-day clock for a cheque", ["It sets the closing date", "It fixes the commission"], "Which is why it should be shown in the agreement.")]},
    ],
    "traps": [
        "Three BANKING days - not business days, not calendar days.",
        "Cheque: clock starts at acceptance. Cash: clock starts at receipt.",
        "A provisional broker never holds trust money; it goes straight to the broker-in-charge.",
        "Commission is the broker's money only after it is properly earned and disbursed.",
    ],
    "vocab": [
        ["Trust money", "Money belonging to others held by a licensee."],
        ["Banking day", "A day the broker's bank is open for business."],
        ["Commingling", "Mixing trust money with the broker's own."],
        ["Conversion", "Using trust money for the broker's own purposes."],
        ["Broker-in-charge", "The broker who supervises an office and its provisional brokers."],
    ],
    "examples": [
        {"t": "Cash across the desk",
         "s": "A buyer hands a provisional broker $2,000 in cash with an offer the seller has not yet seen.",
         "w": ["The provisional broker must pass it to the broker-in-charge immediately.",
               "Because it is cash, the three-banking-day clock runs from receipt, not acceptance."],
         "k": "Into the trust account within three banking days of receipt, accepted or not."},
    ],
}

STUDY["nc/other"] = {
    "summary": "Eleven items of North Carolina law that sits outside the licence law: the disclosure form with its famous third option, the mineral rights notice, and the fund that pays consumers when a broker converts their money.",
    "sections": [
        {"h": "Residential Property and Owners' Association Disclosure",
         "p": ["Chapter 47E requires most residential property owners to complete a disclosure statement for prospective purchasers. The form asks about the condition of the property, and the owner may answer YES, NO, or - uniquely - NO REPRESENTATION."],
         "l": ["Answering 'no representation' means the owner makes no statement either way, and is not a misrepresentation.",
               "FAILURE to provide the buyer with the form may allow the buyer to CANCEL the contract by notifying the seller in writing within THREE CALENDAR DAYS of contract acceptance.",
               "Licensees have a duty under G.S. 47E-8 to inform their clients of the client's rights and obligations under the statute.",
               "Licensees are expected to ASSIST the seller in completing the form, but must NOT complete it for them."],
         "check": [("The three answers on the North Carolina disclosure form are:", "Yes, no, or no representation", ["Yes, no, or unknown", "True, false, or not applicable"], "'No representation' is the North Carolina option."),
                   ("If the form is never given to the buyer, the buyer may:", "Cancel in writing within three calendar days of contract acceptance", ["Sue for treble damages", "Do nothing"], "Chapter 47E."),
                   ("A licensee should:", "Assist the seller with the form but not complete it for them", ["Complete it on the seller's behalf", "Verify every answer personally"], "G.S. 47E-8 and the Commission's guidance.")]},
        {"h": "Mineral, oil and gas rights (G.S. 47E-4.1)",
         "p": ["Separately from the condition disclosure, the owner must give the purchaser a MINERAL AND OIL AND GAS RIGHTS disclosure statement, conspicuous and in BOLDFACE type. It explains that those rights can be severed from the title by conveyance or reservation, and that whoever owns them may have a perpetual right to drill, mine, explore and remove resources, from the surface or from nearby."],
         "check": [("The mineral and oil and gas rights disclosure must be:", "Conspicuous and in boldface type", ["In the appendix", "Given only on request"], "G.S. 47E-4.1(a)."),
                   ("Mineral rights may be severed from the title by:", "Conveyance or reservation by the owner", ["Zoning change", "The buyer's election"], "G.S. 47E-4.1(a).")]},
        {"h": "The Real Estate Education and Recovery Fund",
         "l": ["The Commission maintains the fund to pay unsatisfied judgments where an aggrieved person suffered a DIRECT MONETARY LOSS from the CONVERSION OF TRUST FUNDS by a licensed broker (G.S. 93A-16, 93A-17).",
               "The claimant must have sued the broker and given the Commission written notice of the suit within 60 DAYS of its start - or, where the claim is under $3,000 excluding attorney's fees, within 60 days of the end of all proceedings.",
               "A final judgment on grounds of conversion of trust funds is required.",
               "Limits (G.S. 93A-21): $50,000 PER TRANSACTION regardless of the number of claimants or parcels; $25,000 in the aggregate for ONE LICENSEE in a single calendar year; and $75,000 in the aggregate for one licensee ever.",
               "Application must be made within ONE YEAR after all proceedings end.",
               "The fund does NOT pay consequential, multiple, punitive, incidental or special damages, civil penalties, interest or court costs."],
         "check": [("The fund pays at most, per transaction:", "$50,000", ["$25,000", "$75,000"], "G.S. 93A-21(a)(2)."),
                   ("The aggregate limit for one licensee, ever, is:", "$75,000", ["$25,000", "$50,000"], "$25,000 is the cap within a single calendar year."),
                   ("A claim on the fund must rest on:", "A judgment for conversion of trust funds", ["Any breach of contract", "A negligent appraisal"], "G.S. 93A-17(a)."),
                   ("The fund will NOT pay:", "Court costs and punitive damages", ["Direct monetary loss", "Converted trust funds"], "G.S. 93A-21(a)(4).")]},
        {"h": "The Commission itself (G.S. 93A-3)",
         "l": ["NINE members: SEVEN appointed by the Governor, ONE by the General Assembly on the recommendation of the President Pro Tempore of the Senate, and ONE on the recommendation of the Speaker of the House.",
               "At least THREE must be licensed real estate brokers.",
               "At least TWO must be people not involved directly or indirectly in the real estate or appraisal business.",
               "Members serve THREE-YEAR staggered terms, and elect a chairman annually."],
         "check": [("The North Carolina Real Estate Commission has:", "Nine members", ["Seven members", "Five members"], "Seven appointed by the Governor and two by the General Assembly."),
                   ("At least how many members must be licensed brokers?", "Three", ["Five", "Seven"], "G.S. 93A-3(a)."),
                   ("Commission members serve terms of:", "Three years, staggered", ["Four years", "Two years"], "G.S. 93A-3(a).")]},
    ],
    "traps": [
        "'No representation' is a valid answer and is not a misrepresentation.",
        "Three CALENDAR days to cancel when the disclosure was never given.",
        "$50,000 per transaction, $25,000 per licensee per year, $75,000 per licensee ever.",
        "Nine Commission members, at least three brokers and at least two outsiders.",
    ],
    "vocab": [
        ["RPOADS", "Residential Property and Owners' Association Disclosure Statement."],
        ["No representation", "The North Carolina answer meaning the owner states nothing either way."],
        ["Conversion", "Taking trust money for one's own use; the ground for a fund claim."],
        ["Recovery Fund", "The Real Estate Education and Recovery Fund."],
        ["Severed mineral rights", "Subsurface rights separated from surface ownership."],
    ],
    "examples": [
        {"t": "Two claims, one closing",
         "s": "A broker converts $60,000 of trust money in one transaction; two clients sue and win.",
         "w": ["The per-transaction cap is $50,000 regardless of how many were wronged.",
               "The yearly cap for one licensee is $25,000."],
         "k": "The transaction cap is $50,000, and no more than $25,000 may be paid for that licensee in a calendar year."},
    ],
}

STUDY["nc/contracts"] = {
    "summary": "Seven items. The agency agreement rules do much of the work here, joined by the closing statement and the broker's duty to flag errors in it.",
    "sections": [
        {"h": "What must be in writing",
         "l": ["Every agency agreement for brokerage services, in sales and leases, must be in writing and signed (G.S. 93A-13).",
               "A listing or other agreement with an owner must be written BEFORE any services are provided.",
               "Each written agreement must carry a DEFINITE termination date and end without notice at it.",
               "A contract for the sale of land must be in writing to be enforceable, under the statute of frauds.",
               "A broker completing a preprinted offer form in the ordinary course is not practising law, but drafting provisions is."],
         "check": [("A listing agreement in North Carolina must be:", "In writing before any services are provided", ["Oral until an offer arrives", "Written within ten days"], "Rule A.0104(a)."),
                   ("Every written agency agreement must have:", "A definite termination date", ["An automatic renewal", "A minimum term of 90 days"], "Rule A.0104(a).")]},
        {"h": "Closing",
         "l": ["The broker should review the settlement statement and NOTIFY THE SETTLEMENT AGENT of any errors or omissions they believe exist.",
               "North Carolina closings are commonly handled by an attorney, who certifies title and records the deed.",
               "Trust money held by the broker is disbursed only at the proper time and to the party entitled to it."],
         "check": [("A broker who spots an error on the settlement statement should:", "Notify the settlement agent", ["Correct it themselves", "Ignore it if small"], "The Commission's guidance.")]},
    ],
    "traps": [
        "Owner agreements: written first. Buyer agreements: oral allowed, written by the offer.",
        "A definite termination date is mandatory in every written agency agreement.",
    ],
    "vocab": [
        ["Statute of frauds", "The rule that land contracts must be written to be enforceable."],
        ["Settlement statement", "The accounting of debits and credits at closing."],
        ["Due diligence fee", "A fee a North Carolina buyer may pay the seller for the due diligence period."],
        ["Definite termination date", "The required end date in a written agency agreement."],
    ],
    "examples": [],
}

STUDY["nc/supervision"] = {
    "summary": "Four items on who answers for whom. The broker-in-charge is the pivot: a provisional broker cannot act without one, and cannot be paid by anyone else.",
    "sections": [
        {"h": "The broker-in-charge",
         "l": ["An office must have a designated BROKER-IN-CHARGE, who supervises the brokers in it.",
               "To be designated, a broker must first obtain BIC ELIGIBLE status, which requires the experience the Commission prescribes - the Commission may require evidence of it.",
               "After obtaining BIC Eligible status, the broker must complete the Commission's 12-HOUR BROKER-IN-CHARGE COURSE within 120 DAYS of designation, unless taken in the previous year. Missing that deadline costs the BIC Eligible status, and the course must be taken again before it can be regained.",
               "A PROVISIONAL BROKER may do the same acts as a full broker only while supervised by a designated broker-in-charge, and may NEVER operate independently in any way."],
         "check": [("A broker must complete the 12-hour Broker-in-Charge course within:", "120 days of designation", ["30 days", "one year"], "Unless taken within the previous year."),
                   ("A provisional broker may:", "Act only under the supervision of a designated broker-in-charge", ["Operate independently after one year", "Supervise other provisional brokers"], "G.S. 93A-2(a2)."),
                   ("Missing the 12-hour course deadline means:", "Losing BIC Eligible status until the course is taken", ["A $500 fine", "Automatic licence revocation"], "The Commission's rules.")]},
        {"h": "Who may be paid",
         "l": ["A provisional broker's compensation for brokerage comes through the broker they are affiliated with, not directly from a party.",
               "Acting for more than one party without the knowledge of all parties is a ground for discipline (G.S. 93A-6(a)(4)).",
               "Paying an unlicensed person for acts requiring a licence is prohibited."],
         "check": [("A provisional broker is paid by:", "The affiliated broker", ["The seller directly", "The closing attorney"], "Brokerage compensation flows through the broker.")]},
    ],
    "traps": [
        "12 hours, within 120 days of designation.",
        "A provisional broker is never independent - supervision is the whole point of the status.",
    ],
    "vocab": [
        ["Broker-in-charge", "The designated broker supervising an office."],
        ["BIC Eligible", "The status a broker must hold before being designated."],
        ["Provisional broker", "The entry-level status; supervised, never independent."],
        ["Affiliated broker", "The broker through whom a provisional broker works."],
    ],
    "examples": [],
}

STUDY["nc/taxes"] = {
    "summary": "Four items. The number to carry is the excise tax: a dollar for every five hundred, paid by the seller at the register of deeds.",
    "sections": [
        {"h": "The excise tax (G.S. 105-228.30)",
         "l": ["An EXCISE TAX is levied on each instrument conveying an interest in real property.",
               "The rate is $1.00 ON EACH $500 of the consideration or value conveyed, OR FRACTIONAL PART of $500.",
               "The TRANSFEROR - the seller - pays it to the REGISTER OF DEEDS of the county where the property lies, BEFORE the instrument is recorded.",
               "Where a parcel lies in two or more counties, it is paid to the register of deeds of the county holding the greater part by value.",
               "It also applies to timber deeds and contracts for the sale of standing timber."],
         "check": [("The North Carolina excise tax rate is:", "$1.00 per $500 of consideration or fraction of it", ["$1.00 per $1,000", "70 cents per $100"], "G.S. 105-228.30(a)."),
                   ("The excise tax is paid by:", "The transferor, to the register of deeds", ["The buyer, at closing", "The lender"], "G.S. 105-228.30(a)."),
                   ("A $200,400 sale is taxed on how many $500 units?", "401, because a fractional part counts as a whole unit", ["400", "400.8"], "$200,400 / 500 = 400.8, rounded up.")]},
        {"h": "Property tax and insurance in a transaction",
         "l": ["County and municipal ad valorem property taxes are assessed on the property and are commonly PRORATED between seller and buyer at closing.",
               "A lender normally requires HAZARD INSURANCE at least equal to the loan, and may escrow for taxes and insurance.",
               "TITLE INSURANCE protects against defects in title; the lender's policy protects the lender, an owner's policy the owner."],
         "check": [("Property taxes at closing are usually:", "Prorated between seller and buyer", ["Paid entirely by the buyer", "Waived"], "Standard practice."),
                   ("A lender's title policy protects:", "The lender, up to the loan amount", ["The buyer's equity", "The seller"], "An owner's policy is separate.")]},
    ],
    "traps": [
        "$1 per $500, and any fraction of $500 counts as a whole $500.",
        "The SELLER pays the excise tax, before recording.",
    ],
    "vocab": [
        ["Excise tax", "North Carolina's transfer tax on a recorded conveyance."],
        ["Register of deeds", "The county office where instruments are recorded."],
        ["Ad valorem tax", "A tax according to value; the property tax."],
        ["Proration", "Dividing a shared cost between seller and buyer at closing."],
    ],
    "examples": [
        {"t": "Excise on $286,300",
         "s": "A home sells for $286,300.",
         "w": ["$286,300 / 500 = 572.6 units.",
               "A fractional part counts as a whole unit, so 573.",
               "573 x $1.00 = $573."],
         "k": "$573 in excise tax, paid by the seller."},
    ],
}

STUDY["nc/licensure"] = {
    "summary": "Three items, and the first thing to know is structural: North Carolina issues only a BROKER licence. Newcomers hold it on provisional status until 90 hours of postlicensing education lift that status.",
    "sections": [
        {"h": "One licence, several statuses",
         "l": ["There is only ONE type of licence in North Carolina: a BROKER licence. There is no salesperson licence.",
               "A person who meets the requirements - including the 75-HOUR prelicensing course and the Commission's examination - is first issued a broker licence on PROVISIONAL status.",
               "A provisional broker may do what a full broker does, but only under the supervision of a designated broker-in-charge, and may not operate independently.",
               "An initial licence is issued INACTIVE; it must be activated by affiliating with a broker-in-charge.",
               "A licensee may only engage in brokerage as an AGENT for a party. A licensee is not automatically a REALTOR - that means membership of a private trade association."],
         "check": [("North Carolina issues:", "Only a broker licence, initially on provisional status", ["A salesperson licence and a broker licence", "Three separate licences"], "There is no salesperson licence."),
                   ("The prelicensing course is:", "75 instructional hours", ["60 hours", "90 hours", "120 hours"], "90 hours is the POSTlicensing programme."),
                   ("An initial North Carolina licence is issued:", "Inactive, until the broker affiliates", ["Active immediately", "Provisional but active"], "Activation needs affiliation with a broker-in-charge.")]},
        {"h": "Postlicensing, renewal and continuing education",
         "l": ["POSTLICENSING: 90 instructional hours within 18 MONTHS of initial licensure, in three 30-hour courses - Post 301 Broker Relationships and Responsibilities, Post 302 Contracts and Closing, and Post 303 NC Law, Rules, and Legal Concepts.",
               "Completing all three removes provisional status automatically; the education provider reports it, not the licensee.",
               "Fail to finish in time and the licence goes INACTIVE until the deficiency is cured.",
               "RENEWAL: every licence expires on JUNE 30 each year. Renew online between MAY 15 and JUNE 30; the annual fee is $50.",
               "CONTINUING EDUCATION: 8 hours each annual licence period (July 1 - June 30), to be completed by JUNE 10 to renew on active status.",
               "A broker newly licensed by examination has NO CE requirement in the initial licence year, but must meet the 8 hours before the SECOND renewal."],
         "check": [("Postlicensing education is:", "90 hours within 18 months of initial licensure", ["75 hours within a year", "45 hours within two years"], "Three 30-hour courses."),
                   ("North Carolina licences expire:", "On June 30 each year", ["Two years after issue", "On the licensee's birthday"], "Renewal runs May 15 to June 30."),
                   ("Annual continuing education is:", "8 hours, due by June 10", ["22.5 hours every two years", "45 hours every four years"], "For renewal on active status."),
                   ("A broker newly licensed by examination:", "Has no CE requirement in the initial licence year", ["Must take 8 hours immediately", "Is exempt for two years"], "But must meet it before the second renewal.")]},
    ],
    "traps": [
        "75 hours in, 90 hours of postlicensing within 18 months, 8 hours of CE a year.",
        "Everyone is a BROKER. 'Salesperson' is the wrong word in North Carolina.",
        "Licences expire June 30 annually - not on a two-year cycle.",
        "CE is due by June 10, not June 30.",
    ],
    "vocab": [
        ["Provisional broker", "The entry-level broker licence status."],
        ["Postlicensing education", "The 90 hours that remove provisional status."],
        ["Active / inactive status", "Whether the licensee may currently practise."],
        ["Pocket card", "The annual card evidencing renewal."],
        ["REALTOR", "A member of a private trade association, not a licence status."],
    ],
    "examples": [],
}

STUDY["nc/landlord"] = {
    "summary": "Three items from the Tenant Security Deposit Act. Thirty days is the headline, with a sixty-day backstop when the damage cannot be totted up in time.",
    "sections": [
        {"h": "Holding the deposit (G.S. 42-50)",
         "l": ["Security deposits on residential dwellings go into a TRUST ACCOUNT with a licensed, federally insured depository institution or an authorised trust institution - or the landlord may instead furnish a BOND from an insurance company licensed in North Carolina.",
               "A deposit may be held in a trust account OUTSIDE North Carolina only if the landlord gives the tenant an adequate bond in the amount of the deposits.",
               "The landlord or agent must tell the tenant the NAME AND ADDRESS of the bank or institution holding the deposit - or the bonding insurer - within 30 DAYS after the lease term begins."],
         "check": [("A North Carolina residential security deposit must be:", "Held in a trust account at an insured institution, or covered by a bond", ["Kept in the landlord's own account", "Sent to the Commission"], "G.S. 42-50."),
                   ("The tenant must be told where the deposit is held within:", "30 days after the lease term begins", ["10 days", "60 days"], "G.S. 42-50.")]},
        {"h": "Returning it (G.S. 42-52)",
         "l": ["On termination, the landlord applies the deposit to permitted claims or refunds it.",
               "Either way the landlord must ITEMIZE any damage IN WRITING and mail or deliver it with the balance NO LATER THAN 30 DAYS after the tenancy ends and possession is delivered.",
               "If the extent of the claim cannot be determined in 30 days, the landlord gives an INTERIM accounting within 30 days and a FINAL accounting within 60 DAYS.",
               "If the tenant's address is unknown, the landlord may apply the deposit after 30 days and hold the balance for the tenant.",
               "Permitted deductions (G.S. 42-51) include unpaid rent, damage to the premises, unpaid bills that become a lien, the cost of re-renting after a breach - including a reasonable broker's fee - and damages from non-fulfilment of the rental period."],
         "check": [("The landlord must account for the deposit within:", "30 days of termination and delivery of possession", ["15 days", "60 days always"], "G.S. 42-52."),
                   ("Where the claim cannot be determined in 30 days, the final accounting is due within:", "60 days", ["45 days", "90 days"], "With an interim accounting at 30 days."),
                   ("Which is a permitted deduction?", "The cost of re-renting after the tenant's breach", ["Normal wear and tear", "The landlord's lost opportunity"], "G.S. 42-51(a)(5).")]},
    ],
    "traps": [
        "30 days to account, 60 days for the final figure when it cannot be worked out in time.",
        "Out-of-state trust account only with a bond covering the deposits.",
        "A broker's re-renting fee after a tenant's breach IS deductible.",
    ],
    "vocab": [
        ["Tenant Security Deposit Act", "Article 6 of chapter 42."],
        ["Interim accounting", "The 30-day statement where the final figure is not yet known."],
        ["Demised premises", "The property let to the tenant."],
    ],
    "examples": [],
}


# ------------------------------------------------------------- questions

Q = [
 # agency
 ("nc/agency", "Disclosure", 1, "The Working With Real Estate Agents disclosure must be provided:",
  "At first substantial contact", ["At closing", "When an offer is written", "Within three days of a showing"],
  "Rule A.0104."),
 ("nc/agency", "Disclosure", 2, "Simply handing the disclosure form to a prospective buyer:",
  "Does not satisfy the rule; the broker must review it and reach agreement", ["Satisfies the rule", "Satisfies it if the buyer signs", "Is required only for sellers"],
  "Rule A.0104."),
 ("nc/agency", "Disclosure", 2, "The broker providing the disclosure must include on the form:",
  "Their name and licence number", ["Their broker-in-charge's signature", "The firm's tax number", "The property address"],
  "Rule A.0104."),
 ("nc/agency", "Disclosure", 2, "A seller's agent meeting an unrepresented buyer must disclose agency status:",
  "In writing, at first substantial contact", ["Orally at the first showing", "Only when an offer is made", "Only if asked"],
  "Rule A.0104(e)."),
 ("nc/agency", "Written agreements", 1, "An agency agreement with a seller must be in writing:",
  "Before the broker provides any services", ["Within ten days", "Before closing", "Only if exclusive"],
  "Rule A.0104(a)."),
 ("nc/agency", "Written agreements", 1, "An oral buyer agency agreement must be reduced to writing:",
  "No later than the time any party makes an offer", ["Within 30 days", "At closing", "Never; oral is sufficient"],
  "Rule A.0104(a)."),
 ("nc/agency", "Written agreements", 2, "An oral buyer agency agreement must be:",
  "Non-exclusive, for an indefinite period, terminable at any time", ["Exclusive for 90 days", "Exclusive but terminable", "For a definite six-month term"],
  "Otherwise it must be written from the outset."),
 ("nc/agency", "Written agreements", 2, "Every written agency agreement must:",
  "State a definite period and end without notice at its expiry", ["Renew automatically", "Run at least six months", "Be notarised"],
  "Rule A.0104(a)."),
 ("nc/agency", "Written agreements", 3, "Which agency agreement may provide for automatic renewal?",
  "A landlord's agreement to procure tenants, if the landlord may terminate", ["A residential listing", "A buyer agency agreement", "None may"],
  "The one exception in Rule A.0104(a)."),
 ("nc/agency", "Dual agency", 1, "A firm may represent both buyer and seller in the same transaction only with:",
  "The express written authority of each party", ["Verbal consent from both", "The broker-in-charge's approval", "Commission approval"],
  "Rule A.0104(d) and (i)."),
 ("nc/agency", "Dual agency", 2, "A standard dual agent must:",
  "Remain completely neutral and impartial", ["Advocate for the seller", "Advocate for the buyer", "Advocate for whoever pays"],
  "Advocacy is what dual agency gives up."),
 ("nc/agency", "Dual agency", 2, "G.S. 93A-6(a)(4) prohibits acting for more than one party:",
  "Without the knowledge of all parties for whom the broker acts", ["In any circumstances", "Without Commission approval", "In commercial transactions"],
  "The rule then adds a written-authority requirement."),
 ("nc/agency", "Designated agency", 2, "Designated agency means:",
  "Appointing one agent to the seller and another to the buyer within the firm", ["Using two firms", "Appointing an outside mediator", "Letting the client pick any agent"],
  "Rule A.0104(j)-(m)."),
 ("nc/agency", "Designated agency", 3, "The advantage of designated agency over standard dual agency is:",
  "Each client keeps an advocate", ["It requires no written authority", "It pays a higher commission", "It avoids disclosure"],
  "A standard dual agent must stay neutral."),
 ("nc/agency", "Designated agency", 3, "Authority to practise designated agency must be in writing:",
  "No later than when a written dual agency agreement is required", ["Within 30 days of closing", "Only if the client asks", "At first substantial contact"],
  "Rule A.0104(j)-(m)."),
 ("nc/agency", "Violations", 3, "An agent of the listing firm tells an unrepresented buyer the seller is desperate and will take far less. This:",
  "Violates the duty of loyalty to the seller", ["Is good service to the buyer", "Is permitted puffing", "Is required honesty to the buyer"],
  "Acting to benefit another party without the principal's consent."),

 # practice
 ("nc/practice", "Trust money", 1, "Which is trust money?",
  "A tenant's security deposit", ["The firm's advertising budget", "Commission already properly disbursed", "The broker's salary"],
  "Money belonging to others held by the licensee."),
 ("nc/practice", "Trust money", 1, "The general rule is that trust money must be deposited within:",
  "Three banking days of receipt", ["The next banking day", "Five business days", "Ten calendar days"],
  "Commission rules, Rule A.0116."),
 ("nc/practice", "Trust money", 2, "Earnest money paid by cheque with an offer must be deposited within three banking days of:",
  "Acceptance of the offer", ["Receipt of the cheque", "The closing date", "The end of the month"],
  "Unless the buyer instructs otherwise."),
 ("nc/practice", "Trust money", 2, "Earnest money tendered in CASH must be deposited within three banking days of:",
  "Receipt, even if the offer has not been accepted", ["Acceptance", "Closing", "The buyer's request"],
  "Cash is immediately available and refundable."),
 ("nc/practice", "Trust money", 2, "A tenant security deposit taken with a lease must be deposited within three banking days of:",
  "Acceptance of the lease agreement", ["Receipt", "The tenant moving in", "The end of the lease"],
  "Unless tendered in cash."),
 ("nc/practice", "Trust money", 1, "A provisional broker who receives trust money must:",
  "Deliver it immediately to the broker-in-charge", ["Deposit it in the firm's account", "Hold it until closing", "Return it to the payer"],
  "Rule A.0116(b); A.1808."),
 ("nc/practice", "Trust money", 3, "May a broker deposit an earnest money cheque before the offer is accepted?",
  "Yes, unless the buyer instructed otherwise", ["No, never", "Only with the seller's consent", "Only if it exceeds $5,000"],
  "Early deposit may cause practical problems if the offer fails."),
 ("nc/practice", "Trust money", 3, "Why should the date of acceptance appear in the purchase agreement?",
  "It starts the three-banking-day deposit clock", ["It sets the commission", "It fixes the closing date", "It determines the excise tax"],
  "The Commission's guidance."),
 ("nc/practice", "Trust money", 2, "Money a listing agent receives from an out-of-town seller for yard maintenance is:",
  "Trust money", ["The broker's own money", "Exempt because it is not a sale", "A gift"],
  "Held for another, even if collateral to the brokerage role."),
 ("nc/practice", "Trust money", 2, "Which is NOT trust money in a brokerage?",
  "Commission the broker has properly earned and disbursed", ["Rents collected for an owner", "HOA dues collected", "Advance reservation deposits"],
  "Everything else belongs to someone else."),
 ("nc/practice", "Trust money", 3, "For short-term resort rentals, trust money also includes:",
  "Sales taxes collected on the gross receipts", ["The broker's management fee", "The owner's mortgage payment", "Utility bills"],
  "The Commission's comments."),
 ("nc/practice", "Terminology", 2, "A licensed North Carolina agent is a REALTOR only if:",
  "They belong to the National Association of REALTORS", ["They hold an active licence", "They are a broker-in-charge", "They have passed postlicensing"],
  "It is trade association membership, not a licence status."),

 # other NC laws
 ("nc/other", "Disclosure", 1, "On the North Carolina residential property disclosure form, an owner may answer:",
  "Yes, no, or no representation", ["Yes, no, or unknown", "True or false", "Yes or no only"],
  "Chapter 47E."),
 ("nc/other", "Disclosure", 2, "Answering 'no representation' means:",
  "The owner makes no statement either way, and it is not a misrepresentation", ["The owner is hiding a defect", "The buyer must inspect", "The form is incomplete"],
  "It is a permitted answer."),
 ("nc/other", "Disclosure", 2, "A buyer never given the disclosure statement may cancel the contract:",
  "In writing, within three calendar days of contract acceptance", ["Within ten days", "At any time before closing", "Only with the seller's consent"],
  "Chapter 47E."),
 ("nc/other", "Disclosure", 2, "A licensee's role with the disclosure form is to:",
  "Assist the seller, but not complete the form for them", ["Complete it on the seller's behalf", "Verify every answer", "File it with the Commission"],
  "G.S. 47E-8 and the Commission's guidance."),
 ("nc/other", "Mineral rights", 2, "The mineral and oil and gas rights disclosure must be:",
  "Conspicuous and in boldface type", ["In the appendix of the contract", "Given at closing", "Oral"],
  "G.S. 47E-4.1(a)."),
 ("nc/other", "Mineral rights", 3, "Mineral rights may be severed from a property's title by:",
  "Conveyance or reservation by the owner", ["A zoning change", "The buyer's election", "A survey"],
  "G.S. 47E-4.1(a)."),
 ("nc/other", "Recovery Fund", 1, "The Real Estate Education and Recovery Fund pays at most, per transaction:",
  "$50,000", ["$25,000", "$75,000", "$100,000"],
  "G.S. 93A-21(a)(2), regardless of claimants or parcels."),
 ("nc/other", "Recovery Fund", 2, "The aggregate the fund will pay for one licensee, ever, is:",
  "$75,000", ["$25,000", "$50,000", "$150,000"],
  "G.S. 93A-21(a)(3)."),
 ("nc/other", "Recovery Fund", 2, "The aggregate the fund will pay for one licensee in a single calendar year is:",
  "$25,000", ["$50,000", "$75,000", "No annual limit"],
  "G.S. 93A-21(a)(3)."),
 ("nc/other", "Recovery Fund", 2, "A claim on the fund must rest on a judgment for:",
  "Conversion of trust funds by a licensed broker", ["Any breach of contract", "A negligent valuation", "A disputed commission"],
  "G.S. 93A-17(a)."),
 ("nc/other", "Recovery Fund", 3, "The fund will NOT pay:",
  "Punitive damages, interest and court costs", ["Converted trust funds", "Direct monetary loss", "The unsatisfied judgment amount"],
  "G.S. 93A-21(a)(4)."),
 ("nc/other", "Recovery Fund", 3, "Application to the fund must be made within:",
  "One year after all proceedings end", ["60 days of the judgment", "Three years", "Six months of the conversion"],
  "G.S. 93A-21(a)(1)."),
 ("nc/other", "Commission", 1, "The North Carolina Real Estate Commission has:",
  "Nine members", ["Five members", "Seven members", "Eleven members"],
  "Seven appointed by the Governor and two by the General Assembly (G.S. 93A-3)."),
 ("nc/other", "Commission", 2, "At least how many Commission members must be licensed brokers?",
  "Three", ["Two", "Five", "Seven"],
  "G.S. 93A-3(a)."),
 ("nc/other", "Commission", 2, "Commission members serve terms of:",
  "Three years, staggered", ["Two years", "Four years", "Six years"],
  "G.S. 93A-3(a)."),

 # contracts
 ("nc/contracts", "Writing", 1, "A North Carolina listing agreement must be:",
  "In writing before the broker provides any services", ["Oral until an offer arrives", "Written within ten days", "Written only if exclusive"],
  "G.S. 93A-13; Rule A.0104(a)."),
 ("nc/contracts", "Writing", 2, "A contract for the sale of land must be in writing because of:",
  "The statute of frauds", ["The licence law alone", "Commission rule A.0104", "The excise tax statute"],
  "Writing is required for enforceability."),
 ("nc/contracts", "Writing", 2, "Every written agency agreement must contain:",
  "A definite termination date", ["An automatic renewal clause", "A minimum commission", "A mediation clause"],
  "Rule A.0104(a)."),
 ("nc/contracts", "Closing", 2, "A broker who believes the settlement statement contains an error should:",
  "Notify the settlement agent", ["Correct it personally", "Ignore it if minor", "Refuse to attend closing"],
  "The Commission's guidance."),
 ("nc/contracts", "Closing", 2, "North Carolina closings are commonly conducted by:",
  "An attorney", ["The listing broker", "The lender's loan officer", "The register of deeds"],
  "Attorney-conducted closings are the norm."),
 ("nc/contracts", "Practice of law", 3, "A broker filling in the blanks of a preprinted offer form is:",
  "Not practising law", ["Practising law", "Practising law unless an attorney reviews it", "Required to be an attorney"],
  "Drafting provisions is a different matter."),
 ("nc/contracts", "Due diligence", 2, "A due diligence fee in a North Carolina purchase contract is:",
  "Paid by the buyer to the seller for the due diligence period", ["Held in the broker's trust account as earnest money", "Refundable in all cases", "Paid by the seller"],
  "It is distinct from earnest money."),

 # supervision
 ("nc/supervision", "Broker-in-charge", 1, "A broker must complete the 12-hour Broker-in-Charge course within:",
  "120 days of designation", ["30 days", "60 days", "One year"],
  "Unless taken within the previous year."),
 ("nc/supervision", "Broker-in-charge", 2, "Failing to complete that course on time means:",
  "Losing BIC Eligible status until the course is taken", ["A $1,000 fine", "Automatic revocation", "Nothing, if the office has another BIC"],
  "The status must then be regained."),
 ("nc/supervision", "Provisional brokers", 1, "A provisional broker may:",
  "Act only under the supervision of a designated broker-in-charge", ["Operate independently", "Supervise other provisional brokers", "Hold their own trust account"],
  "G.S. 93A-2(a2)."),
 ("nc/supervision", "Compensation", 2, "A provisional broker's brokerage compensation comes from:",
  "The broker they are affiliated with", ["The seller directly", "The closing attorney", "The buyer"],
  "Compensation flows through the affiliated broker."),

 # taxes
 ("nc/taxes", "Excise tax", 1, "The North Carolina excise tax rate on a conveyance is:",
  "$1.00 per $500 of consideration, or fraction of it", ["$1.00 per $1,000", "70 cents per $100", "$2.00 per $500"],
  "G.S. 105-228.30(a)."),
 ("nc/taxes", "Excise tax", 1, "The excise tax is paid by:",
  "The transferor, to the register of deeds, before recording", ["The buyer, at closing", "The lender", "The listing broker"],
  "G.S. 105-228.30(a)."),
 ("nc/taxes", "Excise tax", 2, "A property sells for $240,250. The excise tax is:",
  "$481", ["$480", "$480.50", "$482"],
  "$240,250 / 500 = 480.5, and a fraction counts as a whole unit, so 481 x $1.00."),
 ("nc/taxes", "Property tax", 2, "Property taxes at a North Carolina closing are usually:",
  "Prorated between seller and buyer", ["Paid entirely by the buyer", "Paid entirely by the seller", "Waived on a sale"],
  "Standard closing practice."),

 # licensure
 ("nc/licensure", "License type", 1, "North Carolina issues:",
  "Only a broker licence, held initially on provisional status", ["A salesperson licence and a broker licence", "Three grades of licence", "A salesperson licence only"],
  "There is no salesperson licence in North Carolina."),
 ("nc/licensure", "Education", 1, "The North Carolina prelicensing course is:",
  "75 instructional hours", ["60 hours", "90 hours", "120 hours"],
  "90 hours is the postlicensing programme."),
 ("nc/licensure", "Education", 1, "Postlicensing education is:",
  "90 hours within 18 months of initial licensure", ["75 hours within a year", "45 hours within two years", "30 hours within six months"],
  "Three 30-hour courses: Post 301, 302 and 303."),

 # landlord tenant
 ("nc/landlord", "Deposits", 1, "A North Carolina residential security deposit must be:",
  "Held in a trust account at an insured institution, or covered by a bond", ["Kept in the landlord's personal account", "Sent to the Commission", "Returned within ten days"],
  "G.S. 42-50."),
 ("nc/landlord", "Deposits", 2, "The landlord must account for the deposit within:",
  "30 days of termination and delivery of possession", ["15 days", "45 days", "60 days in all cases"],
  "G.S. 42-52."),
 ("nc/landlord", "Deposits", 2, "Where the claim cannot be determined within 30 days, the final accounting is due within:",
  "60 days", ["45 days", "90 days", "120 days"],
  "With an interim accounting at 30 days (G.S. 42-52)."),

 # --- licensure, further
 ("nc/licensure", "License type", 2, "A newly licensed North Carolina broker holds the licence:",
  "On provisional status, and initially inactive", ["On active status immediately", "As a salesperson licence", "On probation for a year"],
  "Activation requires affiliation with a broker-in-charge."),
 ("nc/licensure", "Education", 2, "Which is one of the three postlicensing courses?",
  "Post 302: Contracts and Closing", ["Post 302: Trust Account Basics", "Post 302: Appraisal Principles", "Post 302: Property Management"],
  "Post 301, 302 and 303."),
 ("nc/licensure", "Education", 2, "Post 303 covers:",
  "NC Law, Rules, and Legal Concepts", ["Broker Relationships and Responsibilities", "Contracts and Closing", "Fair Housing"],
  "Post 301 is relationships; Post 302 contracts and closing."),
 ("nc/licensure", "Education", 2, "Provisional status is removed:",
  "Automatically, once all three postlicensing courses are reported complete", ["On the licensee's written request", "After two years of practice", "By Commission hearing"],
  "The education provider reports completion."),
 ("nc/licensure", "Education", 3, "A provisional broker who misses the 18-month postlicensing deadline:",
  "Has the licence placed on inactive status until the deficiency is cured", ["Loses the licence permanently", "Is fined $250", "Continues on active status"],
  "Reactivation requires the activation form."),
 ("nc/licensure", "Renewal", 1, "North Carolina real estate licences expire:",
  "On June 30 each year", ["Two years after issue", "On the licensee's birthday", "On December 31"],
  "Renewal runs 15 May to 30 June."),
 ("nc/licensure", "Renewal", 2, "The annual renewal window is:",
  "May 15 to June 30", ["January 1 to March 31", "July 1 to August 31", "Any time in the year"],
  "The annual fee is $50."),
 ("nc/licensure", "Renewal", 1, "Continuing education in North Carolina is:",
  "8 hours each year, due by June 10", ["22.5 hours every two years", "45 hours every four years", "16 hours every two years"],
  "For renewal on active status."),
 ("nc/licensure", "Renewal", 2, "A broker newly licensed by examination:",
  "Has no CE requirement in the initial licence year", ["Must take 8 hours immediately", "Is exempt from CE for two years", "Must take 16 hours in year one"],
  "But must satisfy it before the second renewal."),
 ("nc/licensure", "Renewal", 3, "A licensee who fails to renew by June 30:",
  "Has an expired licence and must apply for reinstatement", ["Has a 90-day grace period", "May renew late for double the fee", "Keeps the licence on inactive status"],
  "It is unlawful to practise without an active licence."),
 ("nc/licensure", "Scope", 2, "A North Carolina licensee may engage in brokerage:",
  "Only as an agent for a party to the transaction", ["As a neutral facilitator", "As a transaction broker", "As an undisclosed principal"],
  "The Commission's comments on G.S. 93A-1 and 93A-2."),
 ("nc/licensure", "Scope", 2, "A business entity engaging in brokerage for compensation in North Carolina:",
  "Must hold a North Carolina broker licence", ["Is exempt if the owner is licensed", "Needs only to register", "Is exempt if out of state"],
  "G.S. 93A-1."),

 # --- supervision, further
 ("nc/supervision", "Broker-in-charge", 2, "Before being designated a broker-in-charge, a broker must first:",
  "Obtain BIC Eligible status", ["Complete postlicensing twice", "Serve five years as a broker", "Open an office"],
  "The Commission may require evidence of the required experience."),
 ("nc/supervision", "Broker-in-charge", 3, "A broker who has lost BIC Eligible status may regain it by:",
  "Taking the Broker-in-Charge course again", ["Waiting one year", "Paying a reinstatement fee", "Applying to the Governor"],
  "The course must be retaken before eligibility returns."),
 ("nc/supervision", "Provisional brokers", 2, "A provisional broker generally may perform:",
  "The same acts as a full broker, while supervised", ["Only clerical work", "Only leasing", "Only acts the broker-in-charge witnesses"],
  "G.S. 93A-2(a2)."),
 ("nc/supervision", "Compensation", 2, "Paying an unlicensed person for acts requiring a licence is:",
  "Prohibited", ["Allowed if disclosed", "Allowed up to $500", "Allowed for referrals only"],
  "G.S. 93A-6."),
 ("nc/supervision", "Discipline", 2, "Acting for more than one party without the knowledge of all is:",
  "A ground for disciplinary action", ["Permitted practice", "A criminal felony", "Allowed with the broker-in-charge's consent"],
  "G.S. 93A-6(a)(4)."),

 # --- landlord tenant, further
 ("nc/landlord", "Deposits", 2, "A landlord may hold a deposit in a trust account outside North Carolina only if:",
  "The tenant is given an adequate bond in the amount of the deposits", ["The tenant agrees orally", "The lease says so", "It is a commercial lease"],
  "G.S. 42-50."),
 ("nc/landlord", "Deposits", 2, "The tenant must be told where the deposit is held within:",
  "30 days after the lease term begins", ["10 days", "60 days", "At the end of the lease"],
  "G.S. 42-50."),
 ("nc/landlord", "Deposits", 2, "Which is a permitted deduction from a North Carolina security deposit?",
  "The cost of re-renting after the tenant's breach", ["Normal wear and tear", "The landlord's lost profit", "Routine repainting"],
  "G.S. 42-51(a)(5), including a reasonable broker's fee."),
 ("nc/landlord", "Deposits", 3, "Unpaid bills that become a lien on the property because of the tenant's occupancy:",
  "May be deducted from the deposit", ["May not be deducted", "Are the landlord's responsibility alone", "Require a court order"],
  "G.S. 42-51(a)(4)."),
 ("nc/landlord", "Deposits", 3, "If the tenant's address is unknown, the landlord may:",
  "Apply the deposit after 30 days and hold the balance for the tenant", ["Keep the whole deposit", "Pay it to the State immediately", "Destroy the record"],
  "G.S. 42-52."),

 # --- taxes, further
 ("nc/taxes", "Excise tax", 2, "Where a parcel lies in two counties, the excise tax is paid to:",
  "The register of deeds of the county holding the greater part by value", ["Both counties equally", "The county of the buyer's residence", "The State"],
  "G.S. 105-228.30(a)."),
 ("nc/taxes", "Excise tax", 3, "The excise tax also applies to:",
  "Timber deeds and contracts for the sale of standing timber", ["Leases of one year", "Mortgage assignments", "Easement releases only"],
  "G.S. 105-228.30(a)."),
 ("nc/taxes", "Excise tax", 2, "A property sells for $310,000. The excise tax is:",
  "$620", ["$310", "$624", "$600"],
  "$310,000 / 500 = 620 units at $1.00."),
 ("nc/taxes", "Insurance", 2, "A lender's title insurance policy protects:",
  "The lender, up to the loan amount", ["The buyer's equity", "The seller", "The broker"],
  "An owner's policy is separate."),
 ("nc/taxes", "Insurance", 2, "Hazard insurance required by a lender normally covers:",
  "At least the amount of the loan", ["The land value", "The buyer's personal belongings only", "Nothing until closing"],
  "Standard lending practice."),

 # --- contracts, further
 ("nc/contracts", "Writing", 2, "An agency agreement for a LEASE transaction in North Carolina:",
  "Must also be in writing and signed", ["May stay oral", "Is exempt from the rule", "Needs only the landlord's signature"],
  "Rule A.0104(a) covers sales and leases."),
 ("nc/contracts", "Earnest money", 2, "Earnest money held by a broker is:",
  "Trust money until properly disbursed", ["The seller's money on acceptance", "The broker's on acceptance", "The buyer's to withdraw at will"],
  "Trust money rules apply throughout."),
 ("nc/contracts", "Closing", 3, "Trust money is disbursed:",
  "At the proper time, to the party entitled to it", ["Whenever the broker chooses", "Always to the seller at closing", "To the listing firm first"],
  "The Commission's comments."),

 # --- practice, further
 ("nc/practice", "Advertising", 2, "A broker's advertising must:",
  "Not be false or misleading", ["Name every salesperson", "Be approved by the Commission", "Include the licence number of the buyer"],
  "G.S. 93A-6."),
 ("nc/practice", "Records", 2, "Records of a brokerage transaction must be:",
  "Retained and made available to the Commission on request", ["Destroyed after closing", "Kept only by the attorney", "Filed with the register of deeds"],
  "The Commission may inspect and audit."),
 ("nc/practice", "Trust money", 3, "Commingling means:",
  "Mixing trust money with the broker's own money", ["Holding two clients' funds in one trust account", "Paying a cooperating broker", "Depositing early"],
  "A properly run pooled trust account is not commingling."),
 ("nc/practice", "Trust money", 3, "Conversion means:",
  "Using trust money for the broker's own purposes", ["Depositing late", "Transferring between trust accounts", "Refunding a buyer"],
  "It is the ground for a Recovery Fund claim."),

 # --- other, further
 ("nc/other", "Recovery Fund", 3, "A claimant must notify the Commission of the lawsuit within:",
  "60 days after it is commenced", ["30 days", "six months", "one year"],
  "Or, for claims under $3,000 excluding fees, within 60 days of the end of all proceedings (G.S. 93A-17)."),
 ("nc/other", "Recovery Fund", 3, "The Commission may not spend fund money on education if it would reduce the balance below:",
  "$200,000", ["$50,000", "$100,000", "$500,000"],
  "G.S. 93A-16(a)."),
 ("nc/other", "Commission", 3, "The Commission chairman is:",
  "Elected by the members for a one-year term", ["Appointed by the Governor", "The longest-serving member", "The Secretary of State"],
  "G.S. 93A-3(a)."),
 ("nc/other", "Commission", 3, "The Governor may remove a Commission member for:",
  "Misconduct, incompetency, or wilful neglect of duty", ["Any reason at all", "Voting against the Governor", "Only a criminal conviction"],
  "G.S. 93A-3(a)."),
 ("nc/other", "Fair housing", 1, "Which is a federally protected class that North Carolina also enforces?",
  "Familial status", ["Occupation", "Income level", "Education"],
  "The State Fair Housing Act mirrors the federal classes."),
 ("nc/other", "Fair housing", 2, "A broker who violates fair housing law:",
  "May face Commission discipline as well as fair housing enforcement", ["Faces only federal action", "Is liable only if the owner instructed it", "Faces no licensing consequence"],
  "The Commission treats it as a licence law matter."),
 ("nc/other", "Disclosure", 3, "The residential property disclosure statement is required of:",
  "Most residential property owners selling under a purchase contract", ["All sellers including commercial", "Only new construction", "Only owners using a broker"],
  "Chapter 47E, with statutory exemptions."),
]


# ------------------------------------------------------------------ build

import hashlib


def _rot(key, n):
    return int(hashlib.sha1(key.encode()).hexdigest(), 16) % n


def _place(key, right, wrongs):
    pos = _rot(key, len(wrongs) + 1)
    choices = list(wrongs)
    choices.insert(pos, right)
    return choices, pos


def build():
    topics = []
    for key, label, n, blurb in TOPICS:
        topics.append({"key": key, "portion": "georgia", "label": label,
                       "exam_questions": n, "blurb": blurb,
                       "counts_on_exam": True})

    bank = []
    for topic, sub, diff, q, right, wrongs, why in Q:
        choices, ans = _place(q, right, wrongs)
        bank.append({
            "id": "nc-" + hashlib.sha1(q.encode()).hexdigest()[:8],
            "portion": "georgia", "topic": topic, "subtopic": sub,
            "sub": topic + "|" + sub, "concept": "North Carolina " + sub.lower(),
            "difficulty": diff, "q": q, "choices": choices, "answer": ans,
            "explain": why,
        })
    ids = [r["id"] for r in bank]
    assert len(ids) == len(set(ids)), "duplicate question"
    assert sum(n for _, _, n, _ in TOPICS) == EXAM["state_scored"], "weights do not sum"

    study = {}
    for key, label, n, blurb in TOPICS:
        s = STUDY[key]
        secs = []
        for sec in s["sections"]:
            out = {"h": sec["h"]}
            if "p" in sec: out["p"] = sec["p"]
            if "l" in sec: out["l"] = sec["l"]
            out["check"] = []
            for q, right, wrongs, why in sec.get("check", []):
                choices, ans = _place(key + q, right, wrongs)
                out["check"].append({"q": q, "choices": choices, "answer": ans, "why": why})
            secs.append(out)
        study[key] = {"topic": key, "label": label, "portion": "georgia",
                      "blurb": blurb, "exam_questions": n, "counts_on_exam": True,
                      "summary": s["summary"], "sections": secs,
                      "traps": s["traps"], "vocab": s["vocab"],
                      "examples": s["examples"], "ga": []}

    return {
        "code": "NC", "name": "North Carolina", "abbr": "NC",
        "regulator": "NCREC",
        "pass": EXAM["pass"],
        "portions": {
            "national": {"scored": EXAM["national_scored"],
                         "minutes": EXAM["national_minutes"]},
            "georgia": {"name": "North Carolina state", "scored": EXAM["state_scored"],
                        "minutes": EXAM["state_minutes"],
                        "blurb": "Chapter 93A, the Commission's rules, and the North Carolina law the outline names."},
        },
        "topics": topics, "bank": bank, "study": study,
        "sources": SOURCES, "diffs": DIFFS,
    }


# Where North Carolina departs from the national rule.
DIFFS = {
    "national/agency": [
        "North Carolina issues only a BROKER licence; newcomers hold it on PROVISIONAL status and may never operate independently.",
        "The Working With Real Estate Agents disclosure goes to buyers and sellers at FIRST SUBSTANTIAL CONTACT, and the broker must review it with them, not merely hand it over.",
        "Dual agency needs the EXPRESS WRITTEN AUTHORITY of each party; designated agency then restores an advocate to each client (Rule A.0104).",
    ],
    "national/practice": [
        "Trust money is deposited within THREE BANKING DAYS - of acceptance for a cheque, of receipt for cash - and a provisional broker must hand it to the broker-in-charge immediately.",
        "The Real Estate Education and Recovery Fund pays $50,000 per transaction, $25,000 per licensee per calendar year and $75,000 per licensee in all (G.S. 93A-21).",
    ],
    "national/disclosures": [
        "The residential property disclosure form offers a third answer found almost nowhere else: NO REPRESENTATION, which is not a misrepresentation (ch. 47E).",
        "A separate MINERAL AND OIL AND GAS RIGHTS disclosure must be given, conspicuous and in boldface (G.S. 47E-4.1).",
        "A buyer never given the disclosure may cancel in writing within three calendar days of contract acceptance.",
    ],
    "national/transfer": [
        "The excise tax is $1.00 per $500 of consideration or fractional part, paid by the SELLER to the register of deeds before recording (G.S. 105-228.30).",
    ],
    "national/contracts": [
        "An agreement with an owner must be written before any services; an oral buyer agency agreement is allowed but must be written by the time any party makes an offer.",
        "Every written agency agreement must carry a definite termination date.",
    ],
}


if __name__ == "__main__":
    import io, json, os
    here = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    out = os.path.join(here, "greprep", "packs", "NC.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    pack = build()
    with io.open(out, "w", encoding="utf-8") as f:
        json.dump(pack, f, ensure_ascii=False, indent=1, sort_keys=True)
    print("wrote", out, len(pack["bank"]), "questions,", len(pack["study"]), "lessons")
