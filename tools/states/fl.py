"""Florida state content: lessons and practice questions.

Florida does not sit a national portion. It writes one 100-question exam of
its own, covering Florida law, general principles and practice, and real
estate maths together, scored as a single paper at 75%. The pack therefore
sets `single`, and the material is still kept in two groups because that is
how it is studied: Florida law, and the general practice shared with every
other state.

Every rule below was read from the official text on 2026-10-17:
  - Chapter 475, Part I, Florida Statutes, and Chapter 61J2, Florida
    Administrative Code, as published together in the Florida Real Estate
    Commission's own law book (myfloridalicense.com).
  - Florida Statutes ch. 83, 95, 190, 193, 196, 201, 404, 689, 697, 702,
    720, from flsenate.gov.
  - The DBPR Candidate Information Booklet for the Sales Associate
    examination, effective January 2025, for the blueprint and weights.
The section a fact comes from is cited next to it. Do not add a fact here
without reading its source first.
"""

EXAM = {
    # One paper. The booklet: 100 multiple-choice items, three and a half
    # hours, and the Division publishes the pass mark as 75 correct.
    "state_scored": 44,      # the Florida-law share of the outline
    "state_minutes": 92,
    "national_scored": 56,   # general principles, practice and maths
    "national_minutes": 118,
    "pass": 0.75,
}

# key, label, questions out of the 100, blurb.
# Weights are the Candidate Information Booklet's own percentages, with the
# general-practice areas left to the shared national lessons.
TOPICS = [
    ("fl/licensing", "Licensing & qualifications", 7,
     "Who needs a licence, who is exempt, education, renewal, inactive status."),
    ("fl/commission", "FREC & the DBPR", 2,
     "The Commission, the Division, and where their authority comes from."),
    ("fl/relationships", "Authorized relationships & disclosures", 7,
     "Transaction broker, single agent, no brokerage relationship."),
    ("fl/brokerage", "Brokerage activities & procedures", 12,
     "Offices, advertising, escrow deadlines, commissions, business entities."),
    ("fl/violations", "Violations, penalties & the Recovery Fund", 3,
     "The complaint process, what FREC can impose, and who the fund pays."),
    ("fl/fedstate", "Federal & Florida laws", 3,
     "Fair housing, and the Florida Residential Landlord and Tenant Act."),
    ("fl/disclosures", "Florida mandatory disclosures", 3,
     "Radon, property tax, homeowners' association, CDD, and known defects."),
    ("fl/homestead", "Homestead & Florida property rights", 3,
     "Homestead protection, tenancy by the entireties, adverse possession."),
    ("fl/taxes", "Taxes affecting real estate", 3,
     "Documentary stamps, the homestead exemption, Save Our Homes."),
    ("fl/planning", "Planning & zoning", 1,
     "Local planning agencies, the planning process, and code enforcement."),
]

SOURCES = [
    {"by": "Florida Real Estate Commission",
     "name": "Florida Real Estate Law Book (ch. 475 F.S. and ch. 61J2 F.A.C.)",
     "note": "The Commission's own compilation of the licence law and its rules. Every licensing, agency, escrow and discipline rule in these notes was read from it.",
     "url": "https://www2.myfloridalicense.com/servop/testing/documents/FREC_printable_LawBook.pdf"},
    {"by": "Florida Legislature",
     "name": "Chapter 475, Part I, Florida Statutes",
     "note": "The real estate licence law itself, current text.",
     "url": "https://www.flsenate.gov/Laws/Statutes/2026/Chapter475/All"},
    {"by": "Florida Legislature",
     "name": "Florida Statutes: ch. 83, 95, 190, 193, 196, 201, 697, 702, 720",
     "note": "Leases, adverse possession, CDD and HOA disclosure, assessments, homestead exemption, documentary stamps, mortgages and foreclosure.",
     "url": "https://www.flsenate.gov/Laws/Statutes"},
    {"by": "Florida DBPR",
     "name": "Candidate Information Booklet, Sales Associate Examination",
     "note": "The blueprint: 100 items, three and a half hours, and the nineteen content areas with their weights.",
     "url": "https://www2.myfloridalicense.com/servop/testing/documents/RE_sales_cibs.pdf"},
]


# --------------------------------------------------------------- lessons

STUDY = {}

STUDY["fl/commission"] = {
    "summary": "Seven people appointed by the Governor run real estate licensing in Florida. Learn the make-up of the Commission and the difference between FREC, which makes the rules, and the Department, which runs the office.",
    "sections": [
        {"h": "The Florida Real Estate Commission (475.02)",
         "p": ["FREC sits inside the Department of Business and Professional Regulation. It has SEVEN members appointed by the Governor and confirmed by the Senate:"],
         "l": ["FOUR must be licensed brokers who have held an ACTIVE licence for the 5 years before appointment.",
               "ONE must be a licensed broker OR sales associate who has held an active licence for the 2 years before appointment.",
               "TWO must be people who are not, and never have been, brokers or sales associates - the consumer members.",
               "At least one member must be 60 years of age or older.",
               "Terms are FOUR years."],
         "check": [("FREC has how many members?", "Seven", ["Five", "Nine"], "Four brokers, one broker or sales associate, two consumer members."),
                   ("How many FREC members have never been licensed?", "Two", ["One", "Three"], "475.02(1)."),
                   ("A broker member must have held an active licence for the preceding:", "5 years", ["2 years", "10 years"], "The fifth member needs only 2 years.")]},
        {"h": "Who does what",
         "l": ["FREC adopts rules (chapter 61J2, Florida Administrative Code), decides questions of practice, and disciplines licensees (475.05).",
               "The DIVISION OF REAL ESTATE, inside the DBPR, does the administration: applications, records, and investigations (475.021).",
               "The DEPARTMENT issues and renews licences; the Commission sets the standards they are issued against."],
         "check": [("Chapter 61J2 of the Florida Administrative Code holds:", "FREC's rules", ["The statutes passed by the Legislature", "Federal regulations"], "The statute is chapter 475; the rules are 61J2.")]},
    ],
    "traps": [
        "Seven members, not five or nine. 4 + 1 + 2 = 7.",
        "The Legislature writes chapter 475. FREC writes chapter 61J2.",
        "The Governor appoints; the Senate confirms.",
    ],
    "vocab": [
        ["FREC", "Florida Real Estate Commission, the seven-member regulator."],
        ["DBPR", "Department of Business and Professional Regulation."],
        ["DRE", "Division of Real Estate, the administrative arm inside DBPR."],
        ["Chapter 475", "The Florida real estate licence law."],
        ["Chapter 61J2", "FREC's administrative rules."],
    ],
    "examples": [],
}

STUDY["fl/licensing"] = {
    "summary": "Florida licenses sales associates at 18 with a high school diploma and 63 hours of schooling. The numbers to hold are 63 before, 45 after, and 14 every two years - and the list of people who need no licence at all.",
    "sections": [
        {"h": "Qualifications (475.17)",
         "l": ["At least 18 years old.",
               "Hold a high school diploma or its equivalent.",
               "Be honest, truthful, trustworthy and of good character, with a good reputation for fair dealing.",
               "Pass the examination."],
         "check": [("The minimum age for a Florida sales associate licence is:", "18", ["17", "21"], "475.17(1)(a)."),
                   ("Florida requires an applicant to hold:", "A high school diploma or its equivalent", ["A college degree", "No formal schooling"], "475.17(1)(a).")]},
        {"h": "The education numbers",
         "l": ["PRE-LICENCE, sales associate: 63 classroom hours of 50 minutes (Course I), inclusive of the end-of-course exam (475.17(2); rule 61J2-3.008).",
               "PRE-LICENCE, broker: 72 hours (Course II).",
               "POST-LICENCE, sales associate: 45 hours, completed BEFORE the first renewal after initial licensure (475.17(3); rule 61J2-3.020). Miss it and the licence becomes null and void.",
               "POST-LICENCE, broker: 60 hours.",
               "CONTINUING EDUCATION: at least 14 classroom hours of 50 minutes each BIENNIUM (475.182).",
               "Three of those 14 hours may be earned once per cycle by attending a FREC legal agenda session, telling the Division at least 7 days beforehand - but not if you are there as a party to a disciplinary action."],
         "check": [("Florida's pre-licence course for a sales associate is:", "63 hours", ["45 hours", "72 hours"], "72 is the broker course; 45 is post-licence."),
                   ("Post-licence education for a sales associate is:", "45 hours before the first renewal", ["14 hours every two years", "63 hours before the first renewal"], "14 hours is ordinary CE."),
                   ("Continuing education after the first renewal is:", "14 hours per biennium", ["30 hours per year", "45 hours per biennium"], "475.182(1)(a).")]},
        {"h": "Exemptions (475.011)",
         "p": ["Chapter 475 does not apply to, among others:"],
         "l": ["An attorney at law acting within the scope of their duties, or a CPA within theirs.",
               "An attorney IN FACT, for executing contracts or conveyances only.",
               "A personal representative, receiver, trustee or magistrate appointed by will or by a court.",
               "An owner selling, exchanging or leasing their OWN property - unless they employ someone paid a commission strictly per transaction to deal with the public.",
               "An employee of a public utility, railroad, or a government agency acting within their employment for no extra pay.",
               "A SALARIED employee of an owner, or of the owner's registered broker, working in an ON-SITE rental office of an apartment community in a leasing capacity.",
               "A salaried manager of a condominium or cooperative, for rentals of ONE YEAR OR LESS."],
         "check": [("A salaried on-site apartment leasing agent:", "Is exempt from licensure", ["Needs a sales associate licence", "Needs a broker licence"], "475.011(4)."),
                   ("An owner who hires an agent paid per transaction to sell to the public:", "Loses the owner exemption for that agent", ["Keeps the exemption", "Must become a broker"], "475.011(2).")]},
        {"h": "Keeping the licence",
         "l": ["Licences run in two-year BIENNIUMS and expire on 31 March or 30 September depending on the cycle issued.",
               "VOLUNTARILY inactive: the licensee chooses it, and renews under 475.183 with the education FREC prescribes.",
               "INVOLUNTARILY inactive: the licence lapsed for failure to renew or to complete post-licence education.",
               "A licence involuntarily inactive for 12 MONTHS OR LESS can be reactivated with at least 14 hours of a FREC-prescribed course (475.183(2)).",
               "A sales associate works only for one registered employer; operating for anyone else violates 475.42(1)(b)."],
         "check": [("A licence involuntarily inactive for 10 months can be reactivated by completing:", "14 hours of a FREC-prescribed course", ["63 hours of pre-licence education", "Nothing; just pay the fee"], "475.183(2)(a).")]},
    ],
    "traps": [
        "63 before, 45 after, 14 every two years. Those three numbers carry most of the licensing questions.",
        "Miss the 45-hour post-licence course and the licence is null and void - it is not merely inactive.",
        "The owner exemption disappears the moment a commissioned salesperson is used with the public.",
        "The condo manager exemption covers rentals of one year or less only.",
    ],
    "vocab": [
        ["Course I", "The 63-hour pre-licence course for a sales associate."],
        ["Post-licence education", "45 hours a sales associate must finish before the first renewal."],
        ["Biennium", "The two-year licence period; 14 hours of CE are due in each."],
        ["Voluntarily inactive", "A licence the holder chose to make inactive."],
        ["Involuntarily inactive", "A licence that lapsed, usually for missing renewal or post-licence education."],
        ["Attorney in fact", "Someone acting under a power of attorney; exempt for executing documents only."],
    ],
    "examples": [
        {"t": "The first renewal",
         "s": "A sales associate licensed in May takes 14 hours of continuing education and renews.",
         "w": ["The FIRST renewal needs the 45-hour post-licence course, not ordinary CE.",
               "CE of 14 hours applies to every renewal AFTER the first."],
         "k": "The licence becomes null and void. Post-licence education cannot be made up late."},
    ],
}

STUDY["fl/relationships"] = {
    "summary": "Florida bans dual agency and presumes every licensee is a TRANSACTION BROKER unless something in writing says otherwise. The exam leans hard on the three relationships and the exact duty lists: seven duties, nine duties, three duties.",
    "sections": [
        {"h": "The three relationships (475.278)",
         "l": ["A licensee may be a TRANSACTION BROKER or a SINGLE AGENT, or may have NO BROKERAGE RELATIONSHIP.",
               "DUAL AGENCY is prohibited in Florida, disclosed or not. A dual agent means a broker representing both buyer and seller as a fiduciary.",
               "PRESUMPTION: every licensee is presumed to be operating as a transaction broker unless a single agent or no-brokerage relationship is established IN WRITING."],
         "check": [("If nothing is agreed in writing, a Florida licensee is presumed to be:", "A transaction broker", ["A single agent", "A dual agent"], "475.278(1)(b)."),
                   ("Dual agency in Florida is:", "Prohibited", ["Allowed with written consent", "Allowed for commercial deals"], "475.278(1)(a).")]},
        {"h": "Transaction broker: SEVEN duties",
         "l": ["Dealing honestly and fairly.",
               "Accounting for all funds.",
               "Using skill, care and diligence in the transaction.",
               "Disclosing all known facts that materially affect the VALUE of residential real property and are not readily observable to the buyer.",
               "Presenting all offers and counteroffers in a timely manner, unless a party has directed otherwise in writing.",
               "LIMITED CONFIDENTIALITY, unless waived in writing.",
               "Any additional duties mutually agreed."],
         "p": ["Limited confidentiality prevents disclosing that the seller will take less than the asking price, that the buyer will pay more than the written offer, the MOTIVATION of any party, that a party will accept other financing terms, or anything else a party asked to be kept confidential."],
         "check": [("Limited confidentiality stops a transaction broker revealing:", "That the seller will take less than the asking price", ["A known roof leak", "The listed price"], "Value-affecting condition is disclosed, not hidden."),
                   ("A transaction broker owes:", "Limited representation, not fiduciary duties", ["Full fiduciary duties", "No duties at all"], "475.278(2).")]},
        {"h": "Single agent: NINE duties",
         "l": ["Dealing honestly and fairly.", "Loyalty.", "Confidentiality.", "Obedience.",
               "Full disclosure.", "Accounting for all funds.",
               "Skill, care and diligence in the transaction.",
               "Presenting all offers and counteroffers in a timely manner, unless directed otherwise in writing.",
               "Disclosing all known facts that materially affect the value of residential real property and are not readily observable."],
         "p": ["The single agent notice must be given BEFORE, OR AT THE TIME OF, entering into a listing or representation agreement, OR BEFORE SHOWING PROPERTY, whichever happens first. Its first sentence is printed in uppercase and bold."],
         "check": [("Which duty belongs to a single agent but not a transaction broker?", "Loyalty", ["Accounting for all funds", "Dealing honestly and fairly"], "Loyalty, obedience, confidentiality and full disclosure are the single agent's extras."),
                   ("The single agent notice is given:", "Before or at the time of the agreement, or before showing property, whichever is first", ["At closing", "Within three days of the contract"], "475.278(3)(b)1.")]},
        {"h": "No brokerage relationship: THREE duties",
         "l": ["Dealing honestly and fairly.",
               "Disclosing all known facts that materially affect the value of residential real property and are not readily observable to the buyer.",
               "Accounting for all funds entrusted to the licensee."],
         "p": ["The no-brokerage-relationship notice must be given BEFORE THE SHOWING OF PROPERTY."],
         "check": [("A licensee with no brokerage relationship owes how many duties?", "Three", ["Seven", "Nine"], "Honesty and fairness, disclosure of material value facts, accounting."),
                   ("The no-brokerage-relationship notice is due:", "Before showing the property", ["At closing", "Only if asked"], "475.278(4)(b).")]},
        {"h": "Changing relationship, and designated sales associates",
         "l": ["A SINGLE AGENT may transition to a TRANSACTION BROKER at any time, but only with the principal's WRITTEN CONSENT obtained FIRST (475.278(3)(b)2.).",
               "DESIGNATED SALES ASSOCIATES (475.2755) are the narrow exception: in a NON-residential transaction where the buyer and seller each have assets of $1 MILLION or more, at the customers' request the broker may designate two sales associates to act as SINGLE AGENTS for the opposing customers in the same deal. Both customers sign a disclosure stating they meet the asset threshold."],
         "check": [("Designated sales associates may be used when:", "It is non-residential and both parties have assets of $1 million or more", ["Any transaction, with consent", "Only residential sales"], "475.2755(1)."),
                   ("Transitioning from single agent to transaction broker requires:", "The principal's written consent, obtained before the change", ["Verbal notice", "Nothing; it is automatic"], "475.278(3)(b)2.")]},
    ],
    "traps": [
        "7 transaction broker, 9 single agent, 3 no brokerage relationship. Learn the counts, then the lists.",
        "Transaction brokerage is the DEFAULT. Anything else must be in writing.",
        "Limited confidentiality never hides a defect affecting value - condition is always disclosed.",
        "Designated sales associates need BOTH: non-residential AND $1 million in assets each.",
        "Florida has no dual agency at all. If an answer says 'disclosed dual agency', it is wrong.",
    ],
    "vocab": [
        ["Transaction broker", "Limited representation to one or both parties; the presumed relationship."],
        ["Single agent", "A fiduciary for one party, owing nine duties."],
        ["No brokerage relationship", "No representation; three duties remain."],
        ["Limited confidentiality", "The transaction broker's duty not to reveal price, motivation or financing flexibility."],
        ["Designated sales associate", "Two associates acting as single agents in one non-residential deal between million-dollar parties."],
        ["Transition disclosure", "The written consent needed to move from single agent to transaction broker."],
    ],
    "examples": [
        {"t": "No paperwork, one question",
         "s": "A licensee shows a buyer three homes. Nothing was signed about representation.",
         "w": ["No writing establishes a single agent or no-brokerage relationship.",
               "The presumption in 475.278(1)(b) applies."],
         "k": "The licensee is a transaction broker, owing the seven duties including limited confidentiality."},
    ],
}

STUDY["fl/brokerage"] = {
    "summary": "The biggest slice of the exam. Offices and signs, what every advert must say, and above all the escrow clock: next business day for a sales associate, third business day for a broker, 15 and 30 business days when a deposit is in dispute.",
    "sections": [
        {"h": "Offices and signs (475.22)",
         "l": ["Each ACTIVE broker must maintain an office of at least ONE ENCLOSED ROOM in a building of stationary construction.",
               "A sign at the entrance of the principal office and each branch office, readable by anyone about to enter.",
               "The sign carries the broker's name, the trade name if any, and at minimum the words 'licensed real estate broker' or 'lic. real estate broker'.",
               "A sales associate does not register an office; the associate works from the broker's."],
         "check": [("A Florida broker's office must be:", "At least one enclosed room in a building of stationary construction", ["Any commercial space over 200 sq ft", "A home office only"], "475.22(1)."),
                   ("The entrance sign must contain at minimum:", "The broker's name and the words 'licensed real estate broker'", ["The broker's licence number", "The office hours"], "475.22(1).")]},
        {"h": "Advertising (rule 61J2-10.025 and 61J2-10.026)",
         "l": ["Every advertisement must be in a way that a reasonable person would know they are dealing with a licensee, and must include the LICENSED NAME OF THE BROKERAGE FIRM.",
               "No advert may be fraudulent, false, deceptive or misleading.",
               "If the licensee's personal name appears, at least the LAST NAME must be used as registered with the Commission.",
               "On the internet, the brokerage firm name sits ADJACENT TO, or immediately above or below, the point of contact information - any address, email, telephone or fax by which to reach the firm or licensee.",
               "TEAM names may include 'team' or 'group', but NOT agency, associates, brokerage, brokers, company, corporation, Corp., Inc., LLC, LP, LLP, partnership, properties, property, real estate, realty, or anything similar.",
               "Each team files a designated licensee with the broker who is responsible for advert compliance, and the broker keeps a current written record of team members at least monthly."],
         "check": [("Every Florida real estate advertisement must include:", "The licensed name of the brokerage firm", ["The licensee's licence number", "The broker's home address"], "Rule 61J2-10.025(1)."),
                   ("Which may NOT appear in a team name?", "Realty", ["Team", "Group"], "Rule 61J2-10.026(4).")]},
        {"h": "Escrow: the clock",
         "l": ["A SALES ASSOCIATE who receives a deposit must deliver it to the broker by the END OF THE NEXT BUSINESS DAY after receipt (rule 61J2-14.009).",
               "A BROKER must place it in escrow 'immediately', which the rule defines as no later than the END OF THE THIRD BUSINESS DAY after receipt (rule 61J2-14.008(3)).",
               "Saturdays, Sundays and legal holidays are NOT business days.",
               "Receipt by a sales associate counts as receipt by the broker for the broker's three-day clock.",
               "The broker must be a SIGNATORY on all escrow accounts."],
         "check": [("A sales associate must deliver an earnest money deposit to the broker by:", "The end of the next business day", ["The end of the third business day", "Within five calendar days"], "Rule 61J2-14.009."),
                   ("The broker must place it in escrow by:", "The end of the third business day after receipt", ["The same day", "Within ten business days"], "Rule 61J2-14.008(3).")]},
        {"h": "Escrow: personal funds and disputes",
         "l": ["A broker may keep up to $1,000 of personal or brokerage funds in each SALES escrow account, and up to $5,000 in each PROPERTY MANAGEMENT escrow account (rule 61J2-14.010(2)). Anything above that is commingling.",
               "On CONFLICTING DEMANDS, or a GOOD FAITH DOUBT about who is entitled to the money, the broker must notify FREC in writing within 15 BUSINESS DAYS, and institute a settlement procedure within 30 BUSINESS DAYS (rule 61J2-10.032).",
               "The four settlement procedures (475.25(1)(d)1.): request an ESCROW DISBURSEMENT ORDER from FREC; submit to ARBITRATION with the consent of all parties; seek court adjudication by INTERPLEADER; or submit to MEDIATION with the written consent of all parties, which must finish within 90 days.",
               "A broker who disburses in compliance with an EDO and is then sued may be reimbursed from the Recovery Fund - but only if the broker notified the Commission and diligently defended the action (475.482(2))."],
         "check": [("On conflicting demands, the broker must notify FREC within:", "15 business days", ["3 business days", "30 calendar days"], "Rule 61J2-10.032(1)(a)."),
                   ("A settlement procedure must be started within:", "30 business days of the last demand", ["15 business days", "90 days"], "Rule 61J2-10.032(1)(a)."),
                   ("Personal funds allowed in a sales escrow account:", "Up to $1,000", ["Up to $5,000", "None at all"], "Property management accounts allow $5,000.")]},
        {"h": "Commissions and who may be paid",
         "l": ["A SALES ASSOCIATE may collect money only in the NAME OF THE EMPLOYER and with the employer's express consent, and may sue for a commission only against the registered employer (475.42(1)(d)).",
               "A person who is not licensed cannot enforce a contract for a commission (475.41).",
               "Commission rates are set by agreement, never by law or by agreement among competitors - price fixing is an antitrust violation."],
         "check": [("A Florida sales associate may be paid by:", "Only the registered employer", ["The seller directly", "The title company"], "475.42(1)(d).")]},
    ],
    "traps": [
        "Next business day for the associate, third business day for the broker. Weekends and holidays do not count.",
        "15 business days to tell FREC, 30 business days to start a procedure.",
        "$1,000 sales escrow, $5,000 property management escrow.",
        "Every advert carries the BROKERAGE firm's licensed name - not the team's, not just the agent's.",
        "A team name may not contain 'realty', 'properties' or 'company'.",
    ],
    "vocab": [
        ["Commingling", "Mixing escrow money with the broker's own beyond the permitted amount."],
        ["Conversion", "Using escrow money for the broker's own purposes."],
        ["EDO", "Escrow Disbursement Order, FREC's ruling on who gets a disputed deposit."],
        ["Interpleader", "A court action asking a judge to decide who is entitled to held funds."],
        ["Good faith doubt", "The broker's genuine uncertainty about who is entitled to the deposit."],
        ["Point of contact information", "Any way to reach the firm; the brokerage name must sit beside it online."],
    ],
    "examples": [
        {"t": "A Friday deposit",
         "s": "A sales associate takes a cheque on Friday. Monday is a legal holiday.",
         "w": ["The associate must deliver it to the broker by the end of the next business day: Tuesday.",
               "The broker then has until the end of the third business day after receipt."],
         "k": "Associate by Tuesday; the broker's clock runs from receipt, counting only business days."},
    ],
}

STUDY["fl/violations"] = {
    "summary": "Practising without a licence is a felony in Florida. FREC can fine $5,000 a count and suspend for up to ten years, and the Recovery Fund pays wronged consumers $50,000 per transaction and $150,000 per licensee.",
    "sections": [
        {"h": "The complaint process",
         "l": ["A complaint is filed with the DBPR, which reviews it for LEGAL SUFFICIENCY - does it allege a violation of chapter 475, 455 or the rules?",
               "If sufficient, the Division INVESTIGATES and reports.",
               "PROBABLE CAUSE is determined by a panel; if found, a formal complaint is issued.",
               "The licensee may request a FORMAL hearing (disputed facts, heard by an administrative law judge at DOAH) or an INFORMAL hearing (facts not disputed, before FREC).",
               "FREC issues a FINAL ORDER. An appeal goes to the District Court of Appeal."],
         "check": [("A complaint is first reviewed for:", "Legal sufficiency", ["Probable cause", "A final order"], "Does it allege a violation of the law FREC enforces?"),
                   ("A hearing where the facts are disputed is held:", "Before an administrative law judge", ["Before FREC itself", "In circuit court"], "Disputed facts go to DOAH; undisputed facts stay with FREC.")]},
        {"h": "What FREC can impose (475.25)",
         "l": ["Deny an application, or a renewal.", "Issue a reprimand.", "Place on probation.",
               "Suspend a licence for up to 10 YEARS.", "Revoke a licence.",
               "Impose an administrative fine of up to $5,000 FOR EACH COUNT or separate offence.",
               "Any or all of these together."],
         "check": [("The maximum administrative fine is:", "$5,000 per count", ["$1,000 per count", "$5,000 per case"], "475.25(1)."),
                   ("The maximum suspension is:", "10 years", ["5 years", "2 years"], "475.25(1).")]},
        {"h": "Criminal penalties (475.42)",
         "l": ["Operating as a broker or sales associate WITHOUT a valid and current ACTIVE licence is a THIRD-DEGREE FELONY.",
               "A sales associate may not operate for any person not registered as their employer.",
               "A broker may not employ a person as a sales associate who does not hold a valid current licence.",
               "Most other violations of 475.42 are second-degree misdemeanours."],
         "check": [("Practising real estate in Florida without a licence is:", "A third-degree felony", ["A second-degree misdemeanour", "A civil infraction"], "475.42(1)(a).")]},
        {"h": "The Real Estate Recovery Fund (475.482-475.484)",
         "l": ["It reimburses a person who wins a court judgment against a licensee for an act that violated 475.25 or 475.42, committed while acting SOLELY as a licensee, and who cannot collect it.",
               "Up to $50,000 per claim, limited to ACTUAL or COMPENSATORY damages. Treble damages, court costs, attorney's fees and interest are NOT paid.",
               "$50,000 in the aggregate per TRANSACTION, regardless of the number of claimants or parcels.",
               "$150,000 in the aggregate against any ONE licensee.",
               "The licensee's licence is AUTOMATICALLY SUSPENDED on the date the fund pays, and stays suspended until the fund is repaid in full with interest. No further action is needed.",
               "Bankruptcy does not wipe out that obligation."],
         "check": [("The Recovery Fund pays at most, per transaction:", "$50,000", ["$25,000", "$150,000"], "$150,000 is the per-licensee aggregate."),
                   ("When the fund pays on a judgment against a licensee, the licence is:", "Automatically suspended until the fund is repaid with interest", ["Revoked permanently", "Unaffected"], "475.484(7)."),
                   ("The fund will NOT pay:", "Attorney's fees and court costs", ["Compensatory damages", "Actual damages"], "475.484(1)(a).")]},
    ],
    "traps": [
        "Unlicensed practice is a FELONY in Florida - harsher than most states.",
        "$5,000 per COUNT, and up to a TEN-year suspension.",
        "$50,000 per transaction, $150,000 per licensee.",
        "The fund pays actual damages only, and suspension is automatic on payment.",
        "Legal sufficiency comes first, then investigation, then probable cause.",
    ],
    "vocab": [
        ["Legal sufficiency", "Whether a complaint alleges a violation of the law FREC enforces."],
        ["Probable cause panel", "The panel that decides whether a formal complaint should issue."],
        ["DOAH", "Division of Administrative Hearings, where disputed facts are tried."],
        ["Final order", "FREC's decision in a disciplinary case."],
        ["Recovery Fund", "The fund that pays consumers holding uncollectable judgments against licensees."],
        ["Third-degree felony", "The grade of unlicensed real estate practice in Florida."],
    ],
    "examples": [
        {"t": "Two claimants, one deal",
         "s": "A buyer and a seller each win $40,000 against the same licensee in the same transaction and cannot collect.",
         "w": ["The per-transaction aggregate is $50,000 regardless of claimants.",
               "Claims total $80,000, over the cap."],
         "k": "Together they receive no more than $50,000, and the licence is suspended until the fund is repaid."},
    ],
}

STUDY["fl/fedstate"] = {
    "summary": "The federal fair housing rules you already know, plus Florida's own landlord and tenant deadlines: 15 days to return a deposit, 30 days to claim against it, and 15 days for the tenant to object.",
    "sections": [
        {"h": "Fair housing",
         "l": ["The federal Fair Housing Act protects race, colour, religion, sex, national origin, disability and familial status.",
               "Florida's Fair Housing Act mirrors the federal classes.",
               "Steering, blockbusting and redlining are prohibited, and so is refusing a reasonable accommodation or modification for a disability."],
         "check": [("Which is a protected class under the federal Fair Housing Act?", "Familial status", ["Occupation", "Income level"], "Race, colour, religion, sex, national origin, disability and familial status.")]},
        {"h": "Security deposits (83.49)",
         "l": ["A landlord holds the deposit in a separate Florida account - non-interest-bearing, or interest-bearing paying the tenant at least 75% of the average annualised rate or 5% simple interest - or posts a surety bond.",
               "The landlord may not commingle deposits with their own funds.",
               "Written notice of how and where the deposit is held: in the lease, or within 30 DAYS of receiving it. This does not apply to a landlord renting fewer than five units.",
               "NO CLAIM on the deposit: return it within 15 DAYS of the tenancy ending.",
               "CLAIM on the deposit: send written notice by certified mail within 30 DAYS of the tenancy ending, stating the amount and the reason.",
               "The tenant then has 15 DAYS from receiving that notice to OBJECT in writing.",
               "A landlord who misses the 30-day notice FORFEITS the right to claim against the deposit."],
         "check": [("A landlord with no claim must return the deposit within:", "15 days", ["30 days", "60 days"], "83.49(3)(a)."),
                   ("To claim against the deposit, the landlord must give written notice within:", "30 days", ["15 days", "45 days"], "By certified mail."),
                   ("A landlord who misses the 30-day deadline:", "Forfeits the right to impose a claim on the deposit", ["May still claim within 60 days", "Keeps the whole deposit"], "83.49(3)(a).")]},
    ],
    "traps": [
        "15 / 30 / 15: return in 15, claim in 30, tenant objects within 15.",
        "The deposit-notice rule does not bind a landlord with fewer than five units.",
        "Missing the claim deadline does not delay the claim - it destroys it.",
    ],
    "vocab": [
        ["Steering", "Directing people toward or away from areas based on a protected class."],
        ["Blockbusting", "Inducing sales by suggesting people of a protected class are moving in."],
        ["Redlining", "Refusing to lend or insure in an area based on its make-up."],
        ["Advance rent", "Rent paid for a period beyond the next immediate rental period."],
    ],
    "examples": [
        {"t": "The silent landlord",
         "s": "A tenant leaves on 1 June having caused $600 of damage. The landlord sends nothing until 10 July.",
         "w": ["Notice of a claim was due within 30 days, by 1 July.",
               "The landlord missed it."],
         "k": "The landlord forfeits the claim on the deposit and must return it, though they may still sue separately for the damage."},
    ],
}

STUDY["fl/disclosures"] = {
    "summary": "Florida stacks mandatory notices onto residential contracts: radon, property taxes, homeowners' association, community development district. Plus the duty every Florida seller has to disclose known defects that a buyer cannot see.",
    "sections": [
        {"h": "Known defects",
         "p": ["Under Florida Supreme Court case law (Johnson v. Davis, 1985), a seller of residential property must disclose facts KNOWN to the seller that MATERIALLY AFFECT THE VALUE of the property and are NOT READILY OBSERVABLE to the buyer. The same standard appears in the licensee's duties in 475.278 for every brokerage relationship, including no brokerage relationship."],
         "check": [("A seller must disclose a known defect when it:", "Materially affects value and is not readily observable", ["Is visible from the street", "Cost more than $500 to repair"], "Johnson v. Davis; echoed in 475.278."),
                   ("Which licensee owes the duty to disclose known material defects?", "All of them, including one with no brokerage relationship", ["Only a single agent", "Only a transaction broker"], "It is in all three duty lists.")]},
        {"h": "The notices a contract carries",
         "l": ["RADON GAS (404.056(5)): the statutory radon paragraph must appear on at least one document executed at or before the contract for sale, or the rental agreement.",
               "PROPERTY TAX (689.261): a disclosure summary at or before execution of the contract, warning the buyer not to rely on the seller's current taxes because a change of ownership triggers reassessment.",
               "HOMEOWNERS' ASSOCIATION (720.401): a disclosure summary BEFORE the contract is signed. If it is not given, the buyer may VOID the contract within 3 DAYS of receiving it or before closing, whichever comes first. The right cannot be waived and ends at closing.",
               "COMMUNITY DEVELOPMENT DISTRICT (190.048): a boldfaced, conspicuous notice immediately above the buyer's signature, warning that the district may levy taxes and assessments.",
               "Federal LEAD-BASED PAINT disclosure applies to housing built before 1978."],
         "check": [("A buyer who never received the HOA disclosure summary may:", "Void the contract within 3 days of receiving it, or before closing", ["Sue for treble damages", "Do nothing"], "720.401(1)(c)."),
                   ("The radon notice must appear:", "On at least one document at or before the contract", ["Only on rentals", "At closing"], "404.056(5).")]},
    ],
    "traps": [
        "Johnson v. Davis is about RESIDENTIAL property and KNOWN, non-observable defects affecting value.",
        "The HOA right to void is 3 days from receiving the summary, and it dies at closing.",
        "Radon goes on sales AND leases.",
        "The property-tax summary exists because reassessment on sale often raises the bill sharply.",
    ],
    "vocab": [
        ["Johnson v. Davis", "The 1985 case creating Florida's residential seller disclosure duty."],
        ["Readily observable", "Visible or obvious to a buyer; such facts need no disclosure."],
        ["CDD", "Community Development District, which can levy its own assessments."],
        ["Disclosure summary", "The statutory notice given before a contract is signed."],
    ],
    "examples": [],
}

STUDY["fl/homestead"] = {
    "summary": "Florida's homestead is unusually strong: protected from most creditors without limit on value, restricted on how it can be left by will, and carrying tax breaks. Add tenancy by the entireties and the seven-year adverse possession rule.",
    "sections": [
        {"h": "Homestead protection",
         "l": ["Article X, section 4 of the Florida Constitution protects the homestead from forced sale by most creditors.",
               "Protected area: up to HALF AN ACRE inside a municipality, or up to 160 ACRES outside one.",
               "The protection does NOT stop a mortgage the owner signed, property taxes and assessments, or liens for work done on the property - mechanics' liens.",
               "If the owner is married or has a minor child, the homestead cannot be devised freely by will, and a conveyance or mortgage needs BOTH spouses to join."],
         "check": [("Homestead protection inside a city covers up to:", "Half an acre", ["One acre", "160 acres"], "160 acres applies outside a municipality."),
                   ("Which claim can still reach a Florida homestead?", "A mortgage the owner signed", ["A credit card judgment", "A medical bill judgment"], "Mortgages, taxes and construction liens survive.")]},
        {"h": "How Florida owners hold title",
         "l": ["TENANCY BY THE ENTIRETIES is available to married couples and carries right of survivorship; neither spouse can convey alone and it is protected from the separate creditors of one spouse.",
               "JOINT TENANCY with right of survivorship must be stated expressly; otherwise co-owners take as TENANTS IN COMMON.",
               "Florida recognises condominiums (ch. 718), cooperatives (ch. 719) and timeshares (ch. 721)."],
         "check": [("A married couple taking title together in Florida are presumed to hold as:", "Tenants by the entireties", ["Tenants in common", "Joint tenants without survivorship"], "The marital estate, with survivorship.")]},
        {"h": "Adverse possession (95.18)",
         "l": ["WITHOUT colour of title, Florida requires 7 YEARS of actual, continued possession under a claim of title.",
               "The claimant must have PAID ALL TAXES on the property within 1 year of entering possession and for every year after.",
               "They must also file a return with the county PROPERTY APPRAISER within 30 days of paying.",
               "Possession is shown by substantial enclosure, or cultivation, maintenance or improvement in the usual manner."],
         "check": [("Adverse possession without colour of title in Florida takes:", "7 years, with all taxes paid", ["20 years", "7 years, taxes irrelevant"], "95.18 makes paying taxes a condition.")]},
    ],
    "traps": [
        "Half an acre in the city, 160 acres outside it.",
        "Homestead does not defeat a mortgage, property taxes or a construction lien.",
        "Florida adverse possession REQUIRES paying the taxes - that is what catches people out.",
        "Married couples take by the entireties, not as ordinary joint tenants.",
    ],
    "vocab": [
        ["Homestead", "The protected Florida residence: half an acre urban, 160 acres rural."],
        ["Tenancy by the entireties", "Married co-ownership with survivorship, protected from one spouse's creditors."],
        ["Colour of title", "A written instrument that appears to give title but is defective."],
        ["Devise", "To leave real property by will; restricted for a Florida homestead."],
    ],
    "examples": [],
}

STUDY["fl/taxes"] = {
    "summary": "Three numbers carry this topic: 70 cents per $100 on a deed, 35 cents per $100 on a note, and the homestead exemption of $25,000 plus a second $25,000 - with Save Our Homes capping the yearly rise at 3%.",
    "sections": [
        {"h": "Documentary stamp taxes",
         "l": ["On a DEED (201.02): 70 CENTS per $100 of consideration, or any fraction of $100. Consideration includes money paid and any mortgage assumed.",
               "On a PROMISSORY NOTE or recorded mortgage (201.08): 35 CENTS per $100 of the debt, or any fraction.",
               "Round the consideration UP to the next full $100 before applying the rate."],
         "check": [("Documentary stamp tax on a deed is:", "70 cents per $100 of consideration", ["35 cents per $100", "$1.00 per $1,000"], "201.02(1)(a)."),
                   ("Documentary stamp tax on a new promissory note is:", "35 cents per $100", ["70 cents per $100", "Nothing"], "201.08(1)(a).")]},
        {"h": "The homestead exemption (196.031)",
         "l": ["$25,000 off the assessed value of a permanent Florida residence, for a person holding title on 1 JANUARY.",
               "An ADDITIONAL exemption of up to $25,000 on assessed value ABOVE $50,000 - and that second one does NOT apply to SCHOOL DISTRICT levies.",
               "So the band from $25,000 to $50,000 is taxable, and the second exemption covers $50,000 to $75,000 for non-school levies."],
         "check": [("The second $25,000 homestead exemption does not apply to:", "School district levies", ["County levies", "City levies"], "196.031(1)(b)."),
                   ("Homestead exemption eligibility is judged on:", "1 January", ["The closing date", "1 July"], "Title and permanent residence as of 1 January.")]},
        {"h": "Save Our Homes (193.155)",
         "p": ["Once a property has the homestead exemption, its assessed value may rise each year by no more than the LOWER of 3 PERCENT or the change in the Consumer Price Index. The cap is lost on a change of ownership, when the property is reassessed at just value - which is why the property-tax disclosure summary warns buyers not to rely on the seller's bill."],
         "check": [("Save Our Homes caps the annual rise in assessed value at:", "The lower of 3% or CPI", ["A flat 3% always", "10%"], "193.155(1).")]},
    ],
    "traps": [
        "70 cents deed, 35 cents note. Both per $100, rounding UP to the next $100.",
        "The second $25,000 exemption skips school levies.",
        "Save Our Homes resets on sale - that is the whole point of the tax disclosure.",
        "January 1 is the date that decides homestead for the year.",
    ],
    "vocab": [
        ["Documentary stamp tax", "Florida's excise tax on deeds and notes."],
        ["Just value", "Market value as determined by the property appraiser."],
        ["Assessed value", "Just value adjusted by caps such as Save Our Homes."],
        ["Save Our Homes", "The 3%-or-CPI cap on a homestead's annual assessment increase."],
        ["Millage", "The tax rate, in dollars per $1,000 of taxable value."],
    ],
    "examples": [
        {"t": "Stamps on a $285,400 sale",
         "s": "A buyer pays $285,400 cash for a home.",
         "w": ["$285,400 / 100 = 2,854 taxable hundreds, with no fraction left over.",
               "2,854 x $0.70 = $1,997.80."],
         "k": "$1,997.80 in documentary stamps on the deed."},
    ],
}

STUDY["fl/planning"] = {
    "summary": "A single question, usually. Know that each local government plans through a comprehensive plan and a local planning agency, and that zoning is enforced locally through variances, special exceptions and nonconforming uses.",
    "sections": [
        {"h": "How Florida plans",
         "l": ["The Community Planning Act (ch. 163, part II) requires local governments to adopt a COMPREHENSIVE PLAN, and development must be consistent with it.",
               "A LOCAL PLANNING AGENCY prepares and recommends the plan and its amendments.",
               "Zoning implements the plan. Changes come as a rezoning, a VARIANCE (relief from a dimensional requirement because of hardship), or a SPECIAL EXCEPTION (a use the code allows under conditions).",
               "A NONCONFORMING USE is one that was lawful before the rules changed and may continue - 'grandfathered'.",
               "A building permit and certificate of occupancy come from the local building department under the Florida Building Code."],
         "check": [("Relief from a setback requirement because of a hardship is:", "A variance", ["A special exception", "A rezoning"], "A special exception is a use the code already contemplates."),
                   ("A use that was lawful before the zoning changed is:", "A nonconforming use", ["A variance", "An illegal use"], "Commonly called grandfathered.")]},
    ],
    "traps": [
        "Variance = dimensional relief for hardship. Special exception = a conditional use already in the code.",
        "Development must be consistent with the comprehensive plan.",
    ],
    "vocab": [
        ["Comprehensive plan", "The local government's long-range land use plan."],
        ["Variance", "Permission to depart from a dimensional zoning requirement."],
        ["Special exception", "A use allowed in a district subject to conditions."],
        ["Nonconforming use", "A lawful use that predates the current zoning."],
    ],
    "examples": [],
}


# ------------------------------------------------------------- questions
# (topic, subtopic, difficulty, question, right, [wrong x3], explanation)

Q = [
 # commission
 ("fl/commission", "Composition", 1, "The Florida Real Estate Commission consists of:",
  "Seven members appointed by the Governor", ["Five members elected by licensees", "Nine members appointed by the Senate", "Seven members elected statewide"],
  "Appointed by the Governor and confirmed by the Senate (475.02(1))."),
 ("fl/commission", "Composition", 1, "How many FREC members must be licensed brokers with five years of active licensure?",
  "Four", ["Two", "Five", "Seven"],
  "Plus one broker or sales associate with two years, and two consumer members (475.02(1))."),
 ("fl/commission", "Composition", 2, "How many FREC members must never have been licensed as a broker or sales associate?",
  "Two", ["One", "Three", "None"],
  "The consumer members (475.02(1))."),
 ("fl/commission", "Composition", 2, "FREC members serve terms of:",
  "Four years", ["Two years", "Three years", "Six years"],
  "475.02(2)."),
 ("fl/commission", "Authority", 2, "FREC's rules are found in:",
  "Chapter 61J2, Florida Administrative Code", ["Chapter 475, Florida Statutes", "Chapter 455, Florida Statutes", "The Florida Constitution"],
  "Chapter 475 is the statute; 61J2 is the rules FREC adopts under it."),
 ("fl/commission", "Authority", 2, "The administrative work of licensing in Florida is carried out by:",
  "The Division of Real Estate within the DBPR", ["FREC itself", "The Department of Revenue", "The county clerk"],
  "475.021."),

 # licensing
 ("fl/licensing", "Qualifications", 1, "To be licensed as a Florida sales associate an applicant must be at least:",
  "18 years old", ["17 years old", "19 years old", "21 years old"],
  "475.17(1)(a)."),
 ("fl/licensing", "Qualifications", 1, "Florida requires a sales associate applicant to hold:",
  "A high school diploma or its equivalent", ["A bachelor's degree", "An associate degree", "No educational credential"],
  "475.17(1)(a)."),
 ("fl/licensing", "Education", 1, "The Florida pre-licence course for a sales associate is:",
  "63 hours", ["45 hours", "72 hours", "14 hours"],
  "Course I, 63 classroom hours of 50 minutes (475.17(2); rule 61J2-3.008)."),
 ("fl/licensing", "Education", 2, "The Florida pre-licence course for a broker is:",
  "72 hours", ["63 hours", "60 hours", "45 hours"],
  "Course II (475.17(2))."),
 ("fl/licensing", "Education", 1, "Post-licence education for a Florida sales associate is:",
  "45 hours before the first renewal", ["14 hours every two years", "63 hours before the first renewal", "None"],
  "475.17(3); rule 61J2-3.020."),
 ("fl/licensing", "Education", 2, "Post-licence education for a Florida broker is:",
  "60 hours", ["45 hours", "72 hours", "14 hours"],
  "Rule 61J2-3.020(1)(b)."),
 ("fl/licensing", "Education", 1, "Continuing education in Florida, after the first renewal, is:",
  "14 classroom hours each biennium", ["30 hours each year", "45 hours each biennium", "8 hours each year"],
  "475.182(1)(a)."),
 ("fl/licensing", "Education", 3, "A sales associate who fails to complete the 45-hour post-licence course before the first renewal:",
  "Has a licence that becomes null and void", ["Is placed on probation", "May complete it within 12 months", "Is fined $500"],
  "Post-licence education cannot be made up after the fact (475.17(3))."),
 ("fl/licensing", "Education", 3, "A licensee may substitute attendance at a FREC legal agenda session for:",
  "Three classroom hours, once per renewal cycle", ["All 14 hours", "Seven hours each year", "Nothing"],
  "Notify the Division at least 7 days in advance (475.182(1)(b))."),
 ("fl/licensing", "Exemptions", 1, "Which person needs a Florida real estate licence?",
  "A person paid a commission per sale to sell an owner's homes to the public", ["A salaried on-site apartment leasing agent", "An attorney at law acting within their duties", "An owner selling their own house"],
  "The owner exemption is lost when a commissioned salesperson deals with the public (475.011(2))."),
 ("fl/licensing", "Exemptions", 2, "A salaried manager of a cooperative apartment complex is exempt when arranging rentals of:",
  "One year or less", ["Any length", "Five years or less", "Month-to-month only"],
  "475.011(5)."),
 ("fl/licensing", "Exemptions", 2, "An attorney in fact is exempt under chapter 475 for:",
  "Executing contracts or conveyances only", ["Any brokerage act", "Up to three transactions a year", "Leasing only"],
  "475.011(1)."),
 ("fl/licensing", "Exemptions", 3, "A salaried employee of a public utility who buys land for the utility within their employment:",
  "Is exempt, provided no extra compensation is paid", ["Needs a sales associate licence", "Needs a broker licence", "Is exempt only for leases"],
  "475.011(3)."),
 ("fl/licensing", "Inactive status", 2, "A licence involuntarily inactive for 12 months or less may be reactivated by completing:",
  "At least 14 hours of a FREC-prescribed course", ["The 63-hour pre-licence course", "45 hours of post-licence education", "Nothing beyond the fee"],
  "475.183(2)(a)."),
 ("fl/licensing", "Sponsorship", 2, "A Florida sales associate may work for:",
  "Only the broker registered as their employer", ["Any broker who pays them", "Two brokers at once with consent", "Themselves"],
  "475.42(1)(b)."),

 # relationships
 ("fl/relationships", "Presumption", 1, "A Florida licensee with no written agreement about representation is presumed to be:",
  "A transaction broker", ["A single agent", "A dual agent", "In no brokerage relationship"],
  "475.278(1)(b)."),
 ("fl/relationships", "Dual agency", 1, "Dual agency in Florida is:",
  "Prohibited, whether disclosed or not", ["Allowed with written consent", "Allowed only in commercial deals", "Required when one broker has both sides"],
  "475.278(1)(a)."),
 ("fl/relationships", "Transaction broker", 1, "How many duties does a transaction broker owe?",
  "Seven", ["Three", "Nine", "Five"],
  "Honesty and fairness, accounting, skill care and diligence, disclosure of material value facts, presenting offers, limited confidentiality, and any agreed extras."),
 ("fl/relationships", "Single agent", 1, "How many duties does a single agent owe?",
  "Nine", ["Seven", "Three", "Six"],
  "475.278(3)(a)."),
 ("fl/relationships", "No brokerage relationship", 1, "A licensee with no brokerage relationship owes:",
  "Three duties", ["No duties", "Seven duties", "Nine duties"],
  "Honesty and fairness, disclosure of known material value facts, and accounting for funds (475.278(4)(a))."),
 ("fl/relationships", "Single agent", 2, "Which duty is owed by a single agent but NOT by a transaction broker?",
  "Loyalty", ["Accounting for all funds", "Dealing honestly and fairly", "Presenting all offers"],
  "Loyalty, obedience, confidentiality and full disclosure are the single agent's additions."),
 ("fl/relationships", "Confidentiality", 2, "Limited confidentiality prevents a transaction broker from revealing:",
  "That the buyer will pay more than the written offer", ["A known defect that affects value", "The asking price", "The property's square footage"],
  "475.278(2)(f). Condition information is always disclosed."),
 ("fl/relationships", "Confidentiality", 3, "A seller tells a transaction broker they must sell quickly because of a divorce. The broker:",
  "May not reveal the motivation without written waiver", ["Must tell any buyer who asks", "May reveal it after an offer is made", "Must report it to FREC"],
  "Motivation is covered by limited confidentiality (475.278(2)(f))."),
 ("fl/relationships", "Disclosure timing", 2, "The single agent notice must be given:",
  "Before or at the time of the agreement, or before showing property, whichever is first", ["At closing", "Within 3 days of the contract", "Only on request"],
  "475.278(3)(b)1."),
 ("fl/relationships", "Disclosure timing", 2, "The no-brokerage-relationship notice must be given:",
  "Before showing the property", ["At the contract", "At closing", "Within 10 days"],
  "475.278(4)(b)."),
 ("fl/relationships", "Transition", 2, "To move from single agent to transaction broker, a licensee must first obtain:",
  "The principal's written consent", ["The other party's consent", "FREC approval", "Nothing; it happens automatically"],
  "475.278(3)(b)2."),
 ("fl/relationships", "Designated sales associate", 2, "Designated sales associates may be used only when:",
  "The transaction is non-residential and each party has assets of $1 million or more", ["Any transaction where both parties consent", "The sale price exceeds $1 million", "Both parties are represented by the same agent"],
  "475.2755(1)."),
 ("fl/relationships", "Designated sales associate", 3, "Designated sales associates act as:",
  "Single agents for their respective customers", ["Transaction brokers for both", "Dual agents", "Licensees with no brokerage relationship"],
  "475.2755(1)."),
 ("fl/relationships", "Duties", 3, "Which duty appears in ALL THREE Florida brokerage relationships?",
  "Dealing honestly and fairly", ["Loyalty", "Obedience", "Limited confidentiality"],
  "Honesty and fairness, disclosure of known material value facts, and accounting appear in all three."),

 # brokerage
 ("fl/brokerage", "Escrow", 1, "A Florida sales associate who receives an earnest money deposit must deliver it to the broker by:",
  "The end of the next business day", ["The end of the third business day", "Within five calendar days", "Closing"],
  "Rule 61J2-14.009."),
 ("fl/brokerage", "Escrow", 1, "A Florida broker must place a deposit into escrow by:",
  "The end of the third business day after receipt", ["The same day", "The end of the next business day", "Within ten business days"],
  "'Immediately' is defined in rule 61J2-14.008(3)."),
 ("fl/brokerage", "Escrow", 2, "For escrow deadlines, which counts as a business day?",
  "Tuesday", ["Saturday", "Sunday", "A legal holiday"],
  "Saturdays, Sundays and legal holidays are excluded."),
 ("fl/brokerage", "Escrow", 2, "The most personal funds a broker may keep in a sales escrow account is:",
  "$1,000", ["$500", "$5,000", "Nothing"],
  "Property management escrow accounts allow $5,000 (rule 61J2-14.010(2))."),
 ("fl/brokerage", "Escrow", 2, "The most personal funds a broker may keep in a property management escrow account is:",
  "$5,000", ["$1,000", "$10,000", "Nothing"],
  "Rule 61J2-14.010(2)."),
 ("fl/brokerage", "Escrow disputes", 1, "On conflicting demands for escrowed funds, the broker must notify FREC within:",
  "15 business days", ["3 business days", "30 calendar days", "10 business days"],
  "Rule 61J2-10.032(1)(a)."),
 ("fl/brokerage", "Escrow disputes", 2, "After conflicting demands, the broker must institute a settlement procedure within:",
  "30 business days of the last demand", ["15 business days", "60 days", "90 days"],
  "Rule 61J2-10.032(1)(a)."),
 ("fl/brokerage", "Escrow disputes", 2, "Which is NOT one of Florida's four escrow settlement procedures?",
  "Keeping the deposit until the parties agree", ["Requesting an escrow disbursement order", "Interpleader", "Mediation with written consent"],
  "The fourth is arbitration with the consent of all parties (475.25(1)(d)1.)."),
 ("fl/brokerage", "Escrow disputes", 3, "Mediation of an escrow dispute must be completed within:",
  "90 days", ["30 days", "6 months", "One year"],
  "475.25(1)(d)1.d."),
 ("fl/brokerage", "Escrow disputes", 3, "A broker who disburses under an escrow disbursement order and is later sued:",
  "May be reimbursed from the Recovery Fund if they notified FREC and defended the suit", ["Is personally liable with no recourse", "Loses their licence automatically", "Must repay the buyer from escrow"],
  "475.482(2)."),
 ("fl/brokerage", "Office", 1, "An active Florida broker must maintain an office consisting of:",
  "At least one enclosed room in a building of stationary construction", ["Any leased commercial space", "A registered mailing address", "No office is required"],
  "475.22(1)."),
 ("fl/brokerage", "Office", 2, "The broker's entrance sign must contain at minimum:",
  "The broker's name and the words 'licensed real estate broker'", ["The licence number", "The office hours", "The names of all sales associates"],
  "475.22(1)."),
 ("fl/brokerage", "Advertising", 1, "Every Florida real estate advertisement must include:",
  "The licensed name of the brokerage firm", ["The licensee's licence number", "The broker's home address", "The words 'equal housing'"],
  "Rule 61J2-10.025(1)."),
 ("fl/brokerage", "Advertising", 2, "If a licensee's personal name appears in an advertisement, it must include at least:",
  "The last name as registered with the Commission", ["The first name only", "Initials", "A nickname is acceptable"],
  "Rule 61J2-10.025(2)."),
 ("fl/brokerage", "Advertising", 2, "On a website, the brokerage firm's name must appear:",
  "Adjacent to, or immediately above or below, the point of contact information", ["In the page footer only", "On the home page only", "Anywhere on the site"],
  "Rule 61J2-10.025(3)(a)."),
 ("fl/brokerage", "Advertising", 2, "Which word may NOT appear in a Florida team name?",
  "Realty", ["Team", "Group", "The members' surnames"],
  "Rule 61J2-10.026(4) bars realty, properties, company, associates and similar words."),
 ("fl/brokerage", "Advertising", 3, "How often must a broker maintain a current written record of each team's members?",
  "At least monthly", ["Annually", "At each renewal", "Only on FREC request"],
  "Rule 61J2-10.026(3)."),
 ("fl/brokerage", "Commissions", 1, "A Florida sales associate may collect money in a brokerage transaction:",
  "Only in the name of the employer, with the employer's express consent", ["Directly from the seller", "From the title company", "From any party who offers it"],
  "475.42(1)(d)."),
 ("fl/brokerage", "Commissions", 2, "An unlicensed person who negotiates a sale for a fee:",
  "Cannot enforce a contract for the commission", ["May sue for the commission", "May collect half", "May collect if the seller agrees"],
  "475.41."),
 ("fl/brokerage", "Commissions", 2, "Brokers in a city agree to charge the same commission rate. This is:",
  "Illegal price fixing", ["Permitted if disclosed", "Set by FREC", "Required by the local board"],
  "An antitrust violation; rates are always negotiable."),

 # violations
 ("fl/violations", "Criminal", 1, "Operating as a broker or sales associate in Florida without a valid current active licence is:",
  "A third-degree felony", ["A second-degree misdemeanour", "A civil infraction", "A first-degree felony"],
  "475.42(1)(a)."),
 ("fl/violations", "Discipline", 1, "The maximum administrative fine FREC may impose is:",
  "$5,000 for each count", ["$1,000 for each count", "$5,000 per case", "$10,000 for each count"],
  "475.25(1)."),
 ("fl/violations", "Discipline", 2, "The maximum period for which FREC may suspend a licence is:",
  "10 years", ["2 years", "5 years", "Indefinitely"],
  "475.25(1)."),
 ("fl/violations", "Complaint process", 2, "A complaint received by the DBPR is first reviewed for:",
  "Legal sufficiency", ["Probable cause", "A final order", "Mediation"],
  "Does it allege a violation of the law FREC enforces?"),
 ("fl/violations", "Complaint process", 2, "A disciplinary hearing where the facts ARE disputed is heard by:",
  "An administrative law judge at DOAH", ["FREC itself", "A circuit judge", "The probable cause panel"],
  "Undisputed facts go to an informal hearing before FREC."),
 ("fl/violations", "Complaint process", 3, "An appeal from a FREC final order goes to:",
  "The District Court of Appeal", ["The circuit court", "The Florida Supreme Court", "The DBPR secretary"],
  "Final agency action is reviewed by the DCA."),
 ("fl/violations", "Recovery Fund", 1, "The Recovery Fund pays at most, per transaction:",
  "$50,000", ["$25,000", "$100,000", "$150,000"],
  "Regardless of the number of claimants or parcels (475.484(3))."),
 ("fl/violations", "Recovery Fund", 2, "The Recovery Fund pays at most, against any one licensee:",
  "$150,000", ["$50,000", "$100,000", "$250,000"],
  "475.484(4)."),
 ("fl/violations", "Recovery Fund", 2, "Which may NOT be recovered from the Recovery Fund?",
  "Attorney's fees and court costs", ["Actual damages", "Compensatory damages", "The unsatisfied part of a judgment"],
  "475.484(1)(a) limits payment to actual or compensatory damages."),
 ("fl/violations", "Recovery Fund", 2, "When the Recovery Fund pays on a judgment against a licensee, that licence is:",
  "Automatically suspended until the fund is repaid with interest", ["Revoked permanently", "Unaffected", "Placed on probation for one year"],
  "475.484(7); no further administrative action is needed."),
 ("fl/violations", "Recovery Fund", 3, "A licensee discharged in bankruptcy after the fund paid a claim:",
  "Still may not have the licence reinstated until the fund is repaid", ["Is released from the obligation", "Must reapply as a new licensee", "Is fined instead"],
  "475.484(7)."),

 # federal and state laws
 ("fl/fedstate", "Fair housing", 1, "Which is a protected class under the federal Fair Housing Act?",
  "Familial status", ["Occupation", "Income level", "Marital status"],
  "Race, colour, religion, sex, national origin, disability and familial status."),
 ("fl/fedstate", "Fair housing", 2, "Telling an owner that people of a particular race are moving in, to induce a sale, is:",
  "Blockbusting", ["Steering", "Redlining", "Puffing"],
  "Prohibited under the Fair Housing Act."),
 ("fl/fedstate", "Security deposits", 1, "A Florida landlord with no claim on the deposit must return it within:",
  "15 days of the tenancy ending", ["30 days", "45 days", "60 days"],
  "83.49(3)(a)."),
 ("fl/fedstate", "Security deposits", 1, "To impose a claim on a security deposit, a Florida landlord must give written notice within:",
  "30 days of the tenancy ending", ["15 days", "45 days", "60 days"],
  "By certified mail (83.49(3)(a))."),
 ("fl/fedstate", "Security deposits", 2, "After receiving a landlord's notice of claim, the tenant must object in writing within:",
  "15 days", ["7 days", "30 days", "60 days"],
  "83.49(3)(a)."),
 ("fl/fedstate", "Security deposits", 2, "A landlord who fails to give notice of a claim within 30 days:",
  "Forfeits the right to impose a claim on the deposit", ["May still claim within 60 days", "Keeps the deposit", "Is fined by the state"],
  "They may still sue separately for damages (83.49(3)(a))."),
 ("fl/fedstate", "Security deposits", 3, "The written notice of where a deposit is held need not be given by a landlord renting:",
  "Fewer than five individual dwelling units", ["Fewer than ten units", "Only single-family homes", "Only condominiums"],
  "83.49(2)."),

 # disclosures
 ("fl/disclosures", "Known defects", 1, "A Florida seller of a home must disclose facts that:",
  "Are known, materially affect value, and are not readily observable", ["Are visible on inspection", "Cost more than $1,000 to repair", "Any buyer asks about"],
  "Johnson v. Davis (Fla. 1985); echoed in 475.278."),
 ("fl/disclosures", "Known defects", 2, "Which licensee owes the duty to disclose known material defects to a buyer?",
  "Every licensee, including one with no brokerage relationship", ["Only a single agent", "Only a transaction broker", "Only the listing broker"],
  "The duty appears in all three lists in 475.278."),
 ("fl/disclosures", "Radon", 1, "The Florida radon notice must appear:",
  "On at least one document executed at or before the sales contract or rental agreement", ["Only on new construction", "At closing", "Only if the buyer asks"],
  "404.056(5)."),
 ("fl/disclosures", "Property tax", 2, "The property tax disclosure summary warns the buyer that:",
  "A change of ownership triggers reassessment and taxes may rise", ["Property taxes never change", "The seller pays all taxes", "Taxes are capped at 3% forever"],
  "689.261(1)."),
 ("fl/disclosures", "HOA", 2, "A buyer who did not receive the homeowners' association disclosure summary may:",
  "Void the contract within 3 days of receiving it, or before closing, whichever is first", ["Void it any time within a year", "Sue for treble damages", "Do nothing once the contract is signed"],
  "720.401(1)(c); the right cannot be waived and ends at closing."),
 ("fl/disclosures", "CDD", 2, "The community development district disclosure must be:",
  "In boldfaced conspicuous type immediately before the buyer's signature", ["In the appendix of the contract", "Given at closing", "Read aloud to the buyer"],
  "190.048."),
 ("fl/disclosures", "Lead paint", 1, "The federal lead-based paint disclosure applies to housing built:",
  "Before 1978", ["Before 1988", "Before 1968", "Any age"],
  "Residential property built before 1978."),

 # homestead and property rights
 ("fl/homestead", "Homestead", 1, "Florida homestead protection covers up to how much land inside a municipality?",
  "Half an acre", ["One acre", "10 acres", "160 acres"],
  "160 acres applies outside a municipality (Art. X, s. 4, Fla. Const.)."),
 ("fl/homestead", "Homestead", 1, "Florida homestead protection covers up to how much land outside a municipality?",
  "160 acres", ["Half an acre", "100 acres", "200 acres"],
  "Art. X, s. 4, Fla. Const."),
 ("fl/homestead", "Homestead", 2, "Which claim can still be enforced against a Florida homestead?",
  "A mortgage the owner signed", ["A credit card judgment", "A medical bill judgment", "An unsecured personal loan"],
  "Mortgages, property taxes and construction liens survive the protection."),
 ("fl/homestead", "Homestead", 3, "An owner with a spouse and a minor child wishes to leave the homestead to a friend by will. This is:",
  "Restricted; the homestead cannot be freely devised", ["Permitted without limit", "Permitted with the friend's consent", "Permitted if recorded"],
  "Art. X, s. 4(c), Fla. Const."),
 ("fl/homestead", "Co-ownership", 1, "A married Florida couple taking title together are presumed to hold as:",
  "Tenants by the entireties", ["Tenants in common", "Joint tenants without survivorship", "Community property owners"],
  "Carries right of survivorship."),
 ("fl/homestead", "Co-ownership", 2, "Co-owners who are not married and whose deed says nothing about survivorship hold as:",
  "Tenants in common", ["Joint tenants", "Tenants by the entireties", "Partners"],
  "Survivorship must be expressly stated."),
 ("fl/homestead", "Adverse possession", 2, "Adverse possession without colour of title in Florida requires:",
  "7 years of possession with all taxes paid", ["7 years, taxes irrelevant", "20 years of possession", "10 years with a recorded deed"],
  "95.18."),
 ("fl/homestead", "Adverse possession", 3, "A Florida adverse possessor must pay the outstanding taxes within:",
  "1 year after entering into possession", ["30 days", "3 years", "7 years"],
  "95.18(1)(a)."),

 # taxes
 ("fl/taxes", "Documentary stamps", 1, "Florida documentary stamp tax on a deed is:",
  "70 cents per $100 of consideration", ["35 cents per $100", "$1.00 per $1,000", "2 mills"],
  "201.02(1)(a)."),
 ("fl/taxes", "Documentary stamps", 1, "Florida documentary stamp tax on a promissory note is:",
  "35 cents per $100 of the debt", ["70 cents per $100", "55 cents per $100", "Nothing"],
  "201.08(1)(a)."),
 ("fl/taxes", "Documentary stamps", 2, "A home sells for $240,000 cash. The documentary stamp tax on the deed is:",
  "$1,680", ["$840", "$1,200", "$2,400"],
  "$240,000 / 100 = 2,400 hundreds; 2,400 x $0.70 = $1,680."),
 ("fl/taxes", "Documentary stamps", 3, "Consideration of $185,250 is taxed on how many $100 units?",
  "1,853, because any fraction of $100 is rounded up", ["1,852", "1,852.5", "1,850"],
  "201.02 taxes each $100 or fractional part."),
 ("fl/taxes", "Homestead exemption", 1, "The first homestead exemption in Florida is:",
  "$25,000", ["$50,000", "$75,000", "$10,000"],
  "196.031(1)(a)."),
 ("fl/taxes", "Homestead exemption", 2, "The additional $25,000 homestead exemption applies to assessed value above:",
  "$50,000", ["$25,000", "$75,000", "$100,000"],
  "196.031(1)(b)."),
 ("fl/taxes", "Homestead exemption", 2, "The additional $25,000 homestead exemption does NOT apply to:",
  "School district levies", ["County levies", "Municipal levies", "Special district levies"],
  "196.031(1)(b)."),
 ("fl/taxes", "Homestead exemption", 2, "Eligibility for the homestead exemption is judged as of:",
  "1 January", ["The closing date", "1 July", "The date of application"],
  "Legal or beneficial title and permanent residence on 1 January (196.031(1)(a))."),
 ("fl/taxes", "Save Our Homes", 2, "Save Our Homes caps the annual increase in a homestead's assessed value at:",
  "The lower of 3% or the change in the CPI", ["A flat 3%", "A flat 10%", "The change in the CPI only"],
  "193.155(1)."),
 ("fl/taxes", "Save Our Homes", 3, "The Save Our Homes cap is lost when:",
  "Ownership changes, and the property is reassessed at just value", ["The owner refinances", "The owner improves the kitchen", "The CPI exceeds 3%"],
  "Which is why the property tax disclosure warns buyers (193.155)."),

 # planning
 ("fl/planning", "Zoning", 1, "Permission to build closer to a boundary than the setback allows, because of a hardship, is:",
  "A variance", ["A special exception", "A rezoning", "A nonconforming use"],
  "A special exception is a use the code already allows under conditions."),
 ("fl/planning", "Zoning", 2, "A use that was lawful before the zoning changed and may continue is:",
  "A nonconforming use", ["A variance", "A special exception", "An illegal use"],
  "Commonly called grandfathered."),
 ("fl/planning", "Planning", 2, "Florida development must be consistent with:",
  "The local comprehensive plan", ["The state building code only", "The county budget", "The MLS rules"],
  "Chapter 163, part II."),
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
            "id": "fl-" + hashlib.sha1(q.encode()).hexdigest()[:8],
            "portion": "georgia", "topic": topic, "subtopic": sub,
            "sub": topic + "|" + sub, "concept": "Florida " + sub.lower(),
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
        "code": "FL", "name": "Florida", "abbr": "FL",
        "regulator": "FREC",
        "pass": EXAM["pass"],
        "single": True,
        "portions": {
            "national": {"name": "General practice",
                         "scored": EXAM["national_scored"],
                         "minutes": EXAM["national_minutes"],
                         "blurb": "Principles, practice and the maths, as Florida tests them."},
            "georgia": {"name": "Florida law", "scored": EXAM["state_scored"],
                        "minutes": EXAM["state_minutes"],
                        "blurb": "Chapter 475, FREC's rules, and the Florida property law on the outline."},
        },
        "topics": topics, "bank": bank, "study": study,
        "sources": SOURCES, "diffs": DIFFS,
    }


# Where Florida departs from the general rule, shown on the general lessons
# in place of the Georgia notes.
DIFFS = {
    "national/agency": [
        "Florida bans dual agency. Every licensee is PRESUMED to be a transaction broker unless a single agent or no-brokerage relationship is put in writing (475.278).",
        "Transaction broker: 7 duties, including limited confidentiality. Single agent: 9. No brokerage relationship: 3.",
    ],
    "national/financing": [
        "Florida is a LIEN THEORY state: a mortgage is a specific lien, not a conveyance of legal title or the right of possession (s. 697.02).",
        "All Florida mortgages are foreclosed in equity - judicially, through the court, tried without a jury (s. 702.01).",
    ],
    "national/transfer": [
        "Adverse possession without colour of title takes 7 years AND requires the claimant to have paid all taxes within a year of entering possession (s. 95.18).",
        "Documentary stamp tax on the deed is 70 cents per $100 of consideration; on a note or mortgage, 35 cents per $100 (ss. 201.02, 201.08).",
    ],
    "national/disclosures": [
        "A Florida seller of residential property must disclose known facts that materially affect value and are not readily observable (Johnson v. Davis, Fla. 1985).",
        "Florida contracts also carry radon, property tax, homeowners' association and community development district notices (ss. 404.056, 689.261, 720.401, 190.048).",
    ],
    "national/ownership": [
        "Florida homestead is protected from most creditors: up to half an acre inside a municipality, 160 acres outside one (Art. X, s. 4, Fla. Const.).",
        "Married couples take title as TENANTS BY THE ENTIRETIES, with survivorship and protection from one spouse's separate creditors.",
    ],
    "national/practice": [
        "Escrow: a sales associate hands a deposit to the broker by the end of the NEXT business day; the broker deposits it by the end of the THIRD (rules 61J2-14.009, -14.008).",
        "Every advertisement must carry the licensed name of the brokerage firm, and online it must sit beside the point of contact information (rule 61J2-10.025).",
    ],
    "national/contracts": [
        "Florida licensees are not required to use state-promulgated contract forms, but a licensee who drafts terms beyond filling in blanks risks the unauthorised practice of law.",
    ],
}


if __name__ == "__main__":
    import io, json, os
    here = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    out = os.path.join(here, "greprep", "packs", "FL.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    pack = build()
    with io.open(out, "w", encoding="utf-8") as f:
        json.dump(pack, f, ensure_ascii=False, indent=1, sort_keys=True)
    print("wrote", out, len(pack["bank"]), "questions,", len(pack["study"]), "lessons")
