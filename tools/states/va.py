"""Virginia state content: lessons and practice questions.

Virginia splits the examination 80 national + 40 state, with a different
mark on each portion: the PSI bulletin gives the salesperson passing scores
as 56 of 80 national (70%) and 30 of 40 state (75%). The pack puts `pass`
on each portion.

The six state categories and their item counts below are PSI's published
Virginia state outline for salespersons.

Every rule below was read from the official text on 2026-11-09:
  - Code of Virginia title 54.1 chapter 21 (real estate), title 36
    (fair housing) and title 55.1 (residential property disclosure), from
    law.lis.virginia.gov.
  - Virginia Administrative Code 18VAC135-20, the Real Estate Board's
    regulations.
  - The PSI Virginia Candidate Information Bulletin for DPOR, for the
    blueprint, the passing scores and the timings.
The section a fact comes from is cited next to it. Do not add a fact here
without reading its source first.
"""

EXAM = {
    # PSI: Salesperson National 80 questions / 105 minutes, pass 56;
    # State 40 questions / 45 minutes, pass 30.
    "state_scored": 40,
    "state_minutes": 45,
    "state_pass": 0.75,
    "national_scored": 80,
    "national_minutes": 105,
    "national_pass": 0.70,
    "pass": 0.75,
}

# PSI's published Virginia state outline, salesperson item counts.
TOPICS = [
    ("va/agency", "Agency definitions & relationships", 12,
     "Standard and limited service agents, dual and designated agency, duties."),
    ("va/disclosures", "Disclosure requirements", 10,
     "Buyer beware, Chesapeake Bay, aircraft noise, septic, HOA, advertising."),
    ("va/licensing", "Licensing", 8,
     "Qualifications, supervision, discipline, records, education, transfers."),
    ("va/fair-housing", "Virginia Fair Housing Law", 4,
     "Virginia's protected classes, which go well past the federal list."),
    ("va/acts", "Specific Virginia acts", 4,
     "Condominium Act, VRLTA, POA Act, Underground Utility Damage Prevention."),
    ("va/escrow", "Escrow accounts", 2,
     "Holding and protecting money that belongs to others."),
]

SOURCES = [
    {"by": "Virginia General Assembly",
     "name": "Code of Virginia title 54.1, chapter 21 (Real Estate)",
     "note": "The licence law: brokerage relationships, standard agent duties, limited service agents, escrow protection.",
     "url": "https://law.lis.virginia.gov/vacode/title54.1/chapter21/"},
    {"by": "Virginia Real Estate Board",
     "name": "18VAC135-20 (Real Estate Board regulations)",
     "note": "Continuing education, records, escrow and standards of practice.",
     "url": "https://law.lis.virginia.gov/admincode/title18/agency135/chapter20/"},
    {"by": "Virginia General Assembly",
     "name": "Code of Virginia title 36 and title 55.1",
     "note": "The Virginia Fair Housing Law and the Residential Property Disclosure Act.",
     "url": "https://law.lis.virginia.gov/vacode/title36/chapter5.1/"},
    {"by": "PSI Services and Virginia DPOR",
     "name": "Virginia Real Estate Candidate Information Bulletin",
     "note": "The blueprint: 80 national and 40 state questions, passing scores 56 and 30, and the six state categories.",
     "url": "https://test-takers.psiexams.com/vare"},
]


# --------------------------------------------------------------- lessons

STUDY = {}

STUDY["va/agency"] = {
    "summary": "Twelve items, the biggest category. Virginia's own invention is the LIMITED SERVICE AGENT, who must list in writing not only what they will do but which standard agent duties they will NOT do.",
    "sections": [
        {"h": "The standard agent's duties to a seller (54.1-2131)",
         "l": ["Perform in accordance with the terms of the brokerage agreement.",
               "PROMOTE THE SELLER'S INTERESTS: market the property per the agreement, seeking a sale at the agreed price and terms or terms acceptable to the seller; assist in drafting and negotiating offers, counteroffers, amendments and addenda; receive and present WRITTEN offers and counteroffers in a timely manner EVEN WHEN THE PROPERTY IS ALREADY UNDER CONTRACT; and give reasonable assistance to satisfy the seller's contract obligations and reach settlement.",
               "A licensee is NOT obliged to seek additional offers while the property is under a contract of sale, unless the brokerage agreement or the contract says so.",
               "MAINTAIN CONFIDENTIALITY of all personal and financial information received during the relationship, and anything else the client asks be kept confidential, unless the law provides otherwise or the seller consents in writing.",
               "EXERCISE ORDINARY CARE.",
               "ACCOUNT in a timely manner for money and property in which the seller has or may have an interest.",
               "Disclose to the seller MATERIAL FACTS related to the property or the transaction of which the licensee has ACTUAL KNOWLEDGE.",
               "Comply with the article, fair housing law and other applicable law."],
         "check": [("A Virginia seller's agent must present written offers:", "In a timely manner, even when the property is already under contract", ["Only until a contract is signed", "Only above the asking price"], "Va. Code 54.1-2131(A)(2)(c)."),
                   ("The standard of care a Virginia licensee owes a client is:", "Ordinary care", ["Extraordinary care", "Strict liability", "Best efforts without limit"], "Va. Code 54.1-2131(A)(4)."),
                   ("Material facts must be disclosed to the client where the licensee has:", "Actual knowledge", ["Any suspicion", "Constructive notice"], "Va. Code 54.1-2131(A)(6)."),
                   ("Confidentiality may be released by:", "The seller's written consent, or where the law provides otherwise", ["The broker's decision", "The passage of time"], "Va. Code 54.1-2131(A)(3).")]},
        {"h": "Duties to the other side",
         "p": ["Licensees must treat ALL PROSPECTIVE BUYERS HONESTLY and must not KNOWINGLY give them false information. That duty runs to customers as well as clients, and sits alongside the agent's loyalty to the client."],
         "check": [("A seller's agent owes a prospective buyer:", "Honest treatment and no knowingly false information", ["Full fiduciary duties", "No duty whatever"], "Va. Code 54.1-2131(B).")]},
        {"h": "The limited service agent (54.1-2138.1)",
         "l": ["A licensee may act as a LIMITED SERVICE AGENT in a residential transaction ONLY under a WRITTEN brokerage agreement that: (i) discloses the licensee is acting as a limited service agent; (ii) lists the SPECIFIC SERVICES the licensee WILL provide; and (iii) lists the SPECIFIC STANDARD AGENT DUTIES the licensee WILL NOT provide.",
               "That disclosure must be CONSPICUOUS and printed in BOLD LETTERING or ALL CAPITALS, and either UNDERLINED or IN A SEPARATE BOX.",
               "The Act prints acknowledgement language that, used substantially, satisfies the requirement - including that NEITHER the other party NOR the other party's licensee is under any legal obligation to help with the duties the limited service agent is not performing.",
               "A limited service agent must still disclose DUAL AGENCY under 54.1-2139."],
         "check": [("A limited service agreement must list:", "Both the services provided and the standard agent duties not provided", ["Only the services provided", "Only the fee"], "Va. Code 54.1-2138.1(A)."),
                   ("The limited service disclosure must be:", "Conspicuous, in bold or capitals, and underlined or boxed", ["In the same type as the rest", "Initialled only"], "Va. Code 54.1-2138.1(A)."),
                   ("The statutory acknowledgement warns the client that:", "Neither the other party nor their licensee must help with the duties not performed", ["The fee is non-refundable", "The agreement cannot be cancelled"], "Va. Code 54.1-2138.1(A)."),
                   ("Limited service agency is available:", "In residential real estate transactions, under a written agreement", ["In any transaction, orally", "Only in commercial deals"], "Va. Code 54.1-2138.1(A).")]},
        {"h": "Dual and designated agency",
         "p": ["Virginia recognises DUAL AGENCY, where one licensee represents both parties, and DESIGNATED AGENCY, where the broker assigns different licensees to each client. Both require disclosure under 54.1-2139. The outline also covers BROKER-SALESPERSON relationships and compensation, document handling (delivery and leaving copies), duties to client versus customer, misrepresentation and omissions, brokerage agreements, and UNREPRESENTED PARTIES."],
         "check": [("Where a broker assigns one licensee to the seller and another to the buyer, that is:", "Designated agency", ["Limited service agency", "Subagency"], "Virginia recognises both dual and designated agency."),
                   ("Dual agency in Virginia must be:", "Disclosed under 54.1-2139", ["Prohibited", "Approved by the Board"], "Va. Code 54.1-2139.")]},
    ],
    "traps": [
        "Offers are presented even when the property is already under contract - that is explicit in the statute.",
        "Ordinary care, not extraordinary care.",
        "A limited service agreement lists the duties NOT provided. That omission list is the point.",
        "Confidentiality survives unless the law or the client's written consent releases it.",
    ],
    "vocab": [
        ["Standard agent", "A licensee owing the full statutory duties."],
        ["Limited service agent", "A licensee who contracts out of named standard duties, in writing."],
        ["Designated agency", "Different licensees of one broker assigned to each client."],
        ["Brokerage agreement", "The written agreement engaging the licensee."],
        ["Ordinary care", "The statutory standard of care in Virginia."],
    ],
    "examples": [
        {"t": "Under contract, new offer",
         "s": "A listed house is under contract; a second buyer submits a written offer.",
         "w": ["The licensee must receive and present written offers in a timely manner even when the property is already under contract.",
               "But the licensee is not obliged to go looking for further offers unless the agreement says so."],
         "k": "Present it. Seeking more offers is optional; presenting one that arrives is not."},
    ],
}

STUDY["va/disclosures"] = {
    "summary": "Ten items. Virginia's disclosure law runs on BUYER BEWARE: the seller discloses that the buyer must investigate, and the statute lists the specific things nobody is required to tell you.",
    "sections": [
        {"h": "Buyer beware and due diligence",
         "p": ["Virginia's Residential Property Disclosure Act (title 55.1, chapter 7) does not make the seller warrant the condition of the house. The seller gives a disclosure statement telling the buyer to EXERCISE WHATEVER DUE DILIGENCE THE BUYER THINKS NECESSARY, and the Act then lists matters on which the owner makes NO REPRESENTATIONS."],
         "check": [("The Virginia Residential Property Disclosure Act works on the principle of:", "Buyer beware, with the buyer exercising due diligence", ["Seller warranty of condition", "Strict seller liability"], "Va. Code 55.1-703.")]},
        {"h": "What the outline names",
         "l": ["PROPERTY DISCLOSURE, including the CHESAPEAKE BAY PRESERVATION ACT - whether the property sits in a designated preservation area.",
               "AIRCRAFT NOISE AND CRASH disclosure - whether the property is in a military air installation noise or accident potential zone.",
               "SEPTIC disclosure - including whether a septic system has been inspected or has operating requirements.",
               "MEGAN'S LAW - the sex offender registry notice; the buyer is directed to the registry rather than the licensee searching it.",
               "STIGMATIZED PROPERTIES - facts about events at the property as opposed to its physical condition.",
               "HOA AND POA DISCLOSURES, with TIMING FOR REVIEW AND CANCELLATION and what constitutes DELIVERY.",
               "ADVERTISING RULES."],
         "check": [("The Chesapeake Bay disclosure tells a buyer:", "Whether the property is in a designated preservation area", ["The water quality", "The flood insurance premium"], "Named on the Virginia state outline."),
                   ("On Megan's Law, a Virginia licensee:", "Directs the buyer to the registry rather than searching it for them", ["Must search and report offenders", "May not mention it"], "The notice points the buyer to the registry."),
                   ("Aircraft noise disclosure concerns:", "Military air installation noise or accident potential zones", ["Commercial flight paths only", "Airport construction plans"], "Named on the Virginia state outline.")]},
        {"h": "Methamphetamine (55.1-708)",
         "p": ["Virginia also requires disclosure where the property was PREVIOUSLY USED TO MANUFACTURE METHAMPHETAMINE and has not been cleaned up in accordance with the applicable guidelines."],
         "check": [("Virginia requires specific disclosure where a property was previously used to:", "Manufacture methamphetamine", ["Store fuel", "House livestock"], "Va. Code 55.1-708.")]},
        {"h": "Association disclosure timing",
         "p": ["For HOA and POA disclosure packets the exam cares about TIMING - how long the buyer has to review and cancel - and what counts as DELIVERY of the packet. Those two points decide whether a cancellation is effective."],
         "check": [("For an association disclosure packet, the two tested points are:", "The timing for review and cancellation, and what constitutes delivery", ["The packet fee and page count", "The association's budget"], "Named on the Virginia state outline.")]},
    ],
    "traps": [
        "Virginia is buyer beware; the seller is not warranting condition.",
        "Megan's Law directs the buyer to the registry - the licensee does not run searches.",
        "Chesapeake Bay, aircraft noise and septic are all Virginia-specific disclosure headings.",
        "Methamphetamine manufacture has its own statutory disclosure.",
    ],
    "vocab": [
        ["Residential Property Disclosure Act", "Virginia's buyer-beware disclosure statute."],
        ["Chesapeake Bay Preservation Area", "A designated area with land use restrictions."],
        ["Accident potential zone", "A military airfield zone affecting nearby land."],
        ["Stigmatized property", "Property affected by events rather than physical defects."],
        ["Disclosure packet", "The HOA or POA documents given to a buyer."],
    ],
    "examples": [],
}

STUDY["va/licensing"] = {
    "summary": "Eight items. Virginia's education numbers: 60 hours to qualify, 30 hours of post-licence inside the first year, then 16 hours each renewal for a salesperson.",
    "sections": [
        {"h": "Qualifying",
         "l": ["An applicant for the Virginia examinations must be at least 18 YEARS OLD.",
               "They must complete the required PRE-LICENCE EDUCATION before taking the examination, or be licensed in another state - in which case they take ONLY THE STATE PORTION.",
               "Fingerprinting is required; the licence application must reach the Board within 90 CALENDAR DAYS of the Board receiving the fingerprint results, or the applicant pays to be fingerprinted again."],
         "check": [("The minimum age for a Virginia salesperson applicant is:", "18", ["17", "19", "21"], "PSI Virginia bulletin."),
                   ("A licensee from another state applying in Virginia takes:", "Only the state portion", ["Both portions", "Neither portion"], "PSI Virginia bulletin."),
                   ("After fingerprint results reach the Board, the licence application must follow within:", "90 calendar days", ["30 days", "6 months"], "PSI Virginia bulletin.")]},
        {"h": "Post-licence education (54.1-2105.01)",
         "p": ["The Board sets a POST-LICENCE curriculum of AT LEAST 30 HOURS, required of all salespersons WITHIN THE INITIAL YEAR OF LICENSURE. A new licensee who fails to complete it within one year from the LAST DAY OF THE MONTH in which the licence was issued has the licence placed on INACTIVE STATUS until it is done."],
         "check": [("Virginia post-licence education is:", "At least 30 hours within the initial year of licensure", ["16 hours", "45 hours within two years"], "Va. Code 54.1-2105.01(A)."),
                   ("A new salesperson who misses the post-licence deadline:", "Has the licence placed on inactive status until it is completed", ["Loses the licence permanently", "Is fined"], "Va. Code 54.1-2105.01(A)."),
                   ("The one-year post-licence clock runs from:", "The last day of the month in which the licence was issued", ["The exam date", "1 January"], "Va. Code 54.1-2105.01(A).")]},
        {"h": "Continuing education (54.1-2105.03; 18VAC135-20-101)",
         "l": ["SALESPERSONS: at least 16 HOURS each licensing term. 11 of those are mandated - 2 hours FAIR HOUSING, 3 hours ETHICS AND STANDARDS OF CONDUCT, 2 hours REAL ESTATE AGENCY, 2 hours REAL ESTATE CONTRACTS including contract principles, forms and ESCROW DEPOSITS AND ACCOUNTS, and 2 hours LEGAL UPDATES AND EMERGING TRENDS including FLOOD ZONE AREAS AND THE NATIONAL FLOOD INSURANCE PROGRAM. The remaining hours are electives.",
               "BROKERS: at least 24 HOURS, with the same 11 mandated hours plus at least 8 hours relating to broker subjects."],
         "check": [("Continuing education for a Virginia salesperson is:", "16 hours per licensing term", ["24 hours", "12 hours", "30 hours"], "18VAC135-20-101."),
                   ("How many of those hours are mandated subjects?", "11", ["8", "16", "4"], "2 fair housing, 3 ethics, 2 agency, 2 contracts, 2 legal updates."),
                   ("The legal updates hours must include:", "Flood zone areas and the National Flood Insurance Program", ["Appraisal standards", "Tax law"], "18VAC135-20-101."),
                   ("Continuing education for a Virginia broker is:", "24 hours per licensing term", ["16 hours", "30 hours"], "Va. Code 54.1-2105.03(A)(1).")]},
        {"h": "Supervision, records and discipline",
         "l": ["The outline covers the BROKER'S SUPERVISORY REQUIREMENTS, DISCIPLINARY PROCEDURES AND SANCTIONS, and in particular IMPROPER DEALINGS and IMPROPER BROKERAGE including commission arrangements.",
               "It also covers INSPECTION OF RECORDS AND AUDITS and the RECORD KEEPING REQUIREMENTS behind them.",
               "LICENCE MAINTENANCE: post-licence education, continuing education, LICENCE TRANSFER, and INFORMING THE BOARD OF CHANGES."],
         "check": [("A Virginia licensee who changes firm must:", "Inform the Board", ["Wait until renewal", "Re-sit the examination"], "Licence maintenance on the state outline."),
                   ("Improper brokerage on the outline includes:", "Improper commission arrangements", ["Slow email replies", "Late open houses"], "PSI Virginia state outline.")]},
    ],
    "traps": [
        "30 hours of post-licence inside the FIRST YEAR, and the clock starts at month end.",
        "16 hours salesperson CE, 24 broker; 11 mandated either way.",
        "The flood insurance hours sit inside the legal updates requirement.",
        "Out-of-state licensees sit the state portion only.",
    ],
    "vocab": [
        ["DPOR", "Department of Professional and Occupational Regulation."],
        ["Real Estate Board", "The Virginia board regulating licensees."],
        ["Post-licence education", "The 30 hours due in the first year."],
        ["Inactive status", "A licence that may not be used until a deficiency is cured."],
    ],
    "examples": [],
}

STUDY["va/fair-housing"] = {
    "summary": "Four items, and the whole category rests on one list. Virginia protects several classes the federal Act does not, including ELDERLINESS and SOURCE OF FUNDS.",
    "sections": [
        {"h": "Virginia's protected classes (54.1 / 36-96.3)",
         "p": ["It is an unlawful discriminatory housing practice to refuse to sell or rent after a bona fide offer, refuse to negotiate, or otherwise make unavailable or deny a dwelling to any person because of:"],
         "l": ["RACE", "COLOR", "RELIGION", "NATIONAL ORIGIN", "SEX",
               "ELDERLINESS", "SOURCE OF FUNDS", "FAMILIAL STATUS",
               "SEXUAL ORIENTATION", "GENDER IDENTITY", "MILITARY STATUS"],
         "check": [("Which is protected under Virginia fair housing law but not the federal Fair Housing Act?", "Elderliness", ["Race", "Religion", "National origin"], "Va. Code 36-96.3(A)(1)."),
                   ("Virginia also protects:", "Source of funds", ["Credit score", "Occupation", "Length of residence"], "Va. Code 36-96.3(A)(1)."),
                   ("Virginia's list includes:", "Gender identity and military status", ["Political affiliation", "Union membership"], "Va. Code 36-96.3(A)(1).")]},
        {"h": "What else the section reaches",
         "l": ["DISCRIMINATING IN THE TERMS, CONDITIONS OR PRIVILEGES of a sale or rental, or in the services and facilities that go with it.",
               "MAKING, PRINTING OR PUBLISHING any notice, statement or advertisement about a sale or rental indicating a preference or limitation.",
               "Fair housing is also a mandated two hours in every licensee's continuing education."],
         "check": [("An advertisement indicating a preference based on a protected class is:", "Unlawful, even without a refusal", ["Lawful if the owner asked for it", "Lawful in private sales"], "Va. Code 36-96.3(A)(3)."),
                   ("Fair housing in Virginia continuing education is:", "Two mandated hours each term", ["Optional", "Four hours"], "18VAC135-20-101.")]},
    ],
    "traps": [
        "Elderliness and source of funds are the two most-tested Virginia additions.",
        "Virginia also covers sexual orientation, gender identity and military status.",
        "The advertisement itself is unlawful; no refusal is needed.",
    ],
    "vocab": [
        ["Elderliness", "A Virginia protected class based on age."],
        ["Source of funds", "A Virginia protected class covering vouchers and benefits."],
        ["Bona fide offer", "A genuine offer; refusing after one triggers the section."],
        ["Dwelling", "The residential property the fair housing law protects."],
    ],
    "examples": [],
}

STUDY["va/acts"] = {
    "summary": "Four items covering four named Virginia statutes. Worth knowing what each one is for rather than its detail.",
    "sections": [
        {"h": "The four acts",
         "l": ["The VIRGINIA CONDOMINIUM ACT and its regulations - CC&Rs, definitions and unit-owner restrictions.",
               "The VIRGINIA RESIDENTIAL LANDLORD AND TENANT ACT (VRLTA) - the statute governing most residential tenancies.",
               "The VIRGINIA PROPERTY OWNERS' ASSOCIATION ACT - governing POAs outside the condominium regime, and the disclosure packet a buyer receives.",
               "The VIRGINIA UNDERGROUND UTILITY DAMAGE PREVENTION ACT - the 'call before you dig' law requiring notice before excavation so utilities can be marked.",
               "The VIRGINIA COMMON INTEREST COMMUNITIES ACT appears on the BROKER outline only."],
         "check": [("The Virginia Underground Utility Damage Prevention Act requires:", "Notice before excavation so utilities can be marked", ["A survey before listing", "Utility easements to be recorded"], "Named on the Virginia state outline."),
                   ("Tenancies in Virginia are mainly governed by:", "The Virginia Residential Landlord and Tenant Act", ["The Condominium Act", "The POA Act"], "Named on the Virginia state outline."),
                   ("Which appears on the BROKER outline but not the salesperson outline?", "The Virginia Common Interest Communities Act", ["The VRLTA", "The Condominium Act"], "PSI marks it broker only."),
                   ("Unit-owner restrictions and CC&Rs fall under:", "The Virginia Condominium Act", ["The VRLTA", "The Underground Utility Damage Prevention Act"], "Named on the Virginia state outline.")]},
    ],
    "traps": [
        "VRLTA governs tenancies; the POA Act governs owners' associations. Different statutes.",
        "Common Interest Communities Act is broker-only on the outline.",
    ],
    "vocab": [
        ["VRLTA", "Virginia Residential Landlord and Tenant Act."],
        ["POA", "Property Owners' Association."],
        ["CC&Rs", "Covenants, conditions and restrictions."],
        ["Miss Utility", "The notification system behind the underground utility law."],
    ],
    "examples": [],
}

STUDY["va/escrow"] = {
    "summary": "Only two items, but they are easy marks. Escrow money belongs to someone else, and Virginia protects it by statute.",
    "sections": [
        {"h": "Protecting escrow funds (54.1-2108)",
         "l": ["The Code has a dedicated section on the PROTECTION OF ESCROW FUNDS held by a broker.",
               "Escrow money is held for the parties, kept separate from the broker's own funds, and accounted for in a timely manner.",
               "Record keeping and the Board's INSPECTION OF RECORDS AND AUDITS reach the escrow account as well as the transaction file.",
               "Continuing education reinforces it: two mandated hours on real estate contracts must cover ESCROW DEPOSITS AND ACCOUNTS."],
         "check": [("Escrow money held by a Virginia broker is:", "Kept separate from the broker's own funds and accounted for in a timely manner", ["The broker's once a contract is signed", "Held by the listing agent personally"], "Va. Code 54.1-2108; 54.1-2131(A)(5)."),
                   ("Escrow deposits and accounts are a required subject in:", "The two mandated contract hours of continuing education", ["The elective hours only", "Post-licence education only"], "18VAC135-20-101."),
                   ("The Board may examine a broker's escrow records:", "Through inspection of records and audits", ["Only with a court order", "Only after a complaint"], "Named on the Virginia state outline.")]},
    ],
    "traps": [
        "Escrow is only 2 of 40 items - do not over-study it, but do not drop the easy marks.",
        "Timely accounting is a statutory agent duty, not just good practice.",
    ],
    "vocab": [
        ["Escrow account", "The account holding money belonging to the parties."],
        ["Audit", "The Board's examination of a broker's records."],
        ["Timely accounting", "The statutory duty to account for others' money promptly."],
    ],
    "examples": [],
}


# ------------------------------------------------------------- questions

Q = [
 # agency
 ("va/agency", "Seller duties", 1, "A Virginia seller's agent must present written offers:",
  "In a timely manner, even when the property is already under contract", ["Only until a contract is signed", "Only if above the asking price", "At the seller's request"],
  "Va. Code 54.1-2131(A)(2)(c)."),
 ("va/agency", "Seller duties", 1, "The standard of care a Virginia licensee owes a client is:",
  "Ordinary care", ["Extraordinary care", "Strict liability", "Utmost care"],
  "Va. Code 54.1-2131(A)(4)."),
 ("va/agency", "Seller duties", 2, "Material facts must be disclosed to the client where the licensee has:",
  "Actual knowledge", ["Any suspicion", "Constructive notice", "A rumour"],
  "Va. Code 54.1-2131(A)(6)."),
 ("va/agency", "Seller duties", 2, "Confidential client information may be released:",
  "Where the law provides otherwise or the client consents in writing", ["At the broker's discretion", "Once the deal closes", "After one year"],
  "Va. Code 54.1-2131(A)(3)."),
 ("va/agency", "Seller duties", 2, "While a property is under a contract of sale, the licensee:",
  "Need not seek additional offers unless the agreement says so", ["Must keep marketing in all cases", "Must withdraw the listing"],
  "Va. Code 54.1-2131(A)(2)(a)."),
 ("va/agency", "Seller duties", 3, "A Virginia licensee must account for the client's money:",
  "In a timely manner", ["At closing only", "Annually", "On written demand only"],
  "Va. Code 54.1-2131(A)(5)."),
 ("va/agency", "Customers", 1, "A Virginia seller's agent owes a prospective buyer:",
  "Honest treatment and no knowingly false information", ["Full fiduciary duties", "No duty at all", "Confidentiality"],
  "Va. Code 54.1-2131(B)."),
 ("va/agency", "Limited service", 1, "A limited service agreement must list:",
  "Both the services provided and the standard agent duties not provided", ["Only the services provided", "Only the fee", "Only the term"],
  "Va. Code 54.1-2138.1(A)."),
 ("va/agency", "Limited service", 2, "The limited service disclosure must be:",
  "Conspicuous, in bold or all capitals, and underlined or in a separate box", ["In the same type as the rest of the agreement", "Initialled only", "Read aloud"],
  "Va. Code 54.1-2138.1(A)."),
 ("va/agency", "Limited service", 2, "Limited service agency is available:",
  "In residential transactions, under a written brokerage agreement", ["In any transaction, orally", "In commercial deals only", "Without any agreement"],
  "Va. Code 54.1-2138.1(A)."),
 ("va/agency", "Limited service", 3, "The statutory acknowledgement warns the client that:",
  "Neither the other party nor their licensee must help with the duties not performed", ["The fee is non-refundable", "The agreement cannot be cancelled", "The Board approves the arrangement"],
  "Va. Code 54.1-2138.1(A)."),
 ("va/agency", "Limited service", 3, "A limited service agent must still:",
  "Disclose dual agency under 54.1-2139", ["Perform all standard duties", "Refuse dual agency", "Notify the Board"],
  "Va. Code 54.1-2138.1(A)."),
 ("va/agency", "Designated agency", 2, "Where a broker assigns one licensee to the seller and another to the buyer, that is:",
  "Designated agency", ["Limited service agency", "Subagency", "Transaction brokerage"],
  "Virginia recognises dual and designated agency."),
 ("va/agency", "Dual agency", 2, "Dual agency in Virginia must be:",
  "Disclosed under 54.1-2139", ["Prohibited", "Approved by the Board", "Limited to commercial deals"],
  "Va. Code 54.1-2139."),

 # disclosures
 ("va/disclosures", "Buyer beware", 1, "The Virginia Residential Property Disclosure Act works on the principle of:",
  "Buyer beware, with the buyer exercising due diligence", ["Seller warranty of condition", "Strict seller liability", "Agent certification"],
  "Va. Code 55.1-703."),
 ("va/disclosures", "Chesapeake Bay", 2, "The Chesapeake Bay disclosure tells a buyer:",
  "Whether the property is in a designated preservation area", ["The water quality", "The flood insurance premium", "The shoreline length"],
  "Named on the Virginia state outline."),
 ("va/disclosures", "Aircraft", 2, "Aircraft noise disclosure in Virginia concerns:",
  "Military air installation noise or accident potential zones", ["Commercial flight paths", "Airport expansion plans", "Helicopter routes"],
  "Named on the Virginia state outline."),
 ("va/disclosures", "Megan's Law", 1, "On Megan's Law, a Virginia licensee:",
  "Directs the buyer to the registry rather than searching it for them", ["Must search and report offenders", "May not mention it", "Must warn neighbours"],
  "The notice points the buyer to the registry."),
 ("va/disclosures", "Septic", 2, "Virginia septic disclosure concerns:",
  "Whether a septic system has been inspected or carries operating requirements", ["The well depth", "The water bill", "The sewer connection fee"],
  "Named on the Virginia state outline."),
 ("va/disclosures", "Stigmatized", 2, "A stigmatized property is one affected by:",
  "Events at the property rather than its physical condition", ["A structural defect", "An unpaid lien", "A boundary dispute"],
  "Named on the Virginia state outline."),
 ("va/disclosures", "Associations", 2, "For an association disclosure packet, the two tested points are:",
  "The timing for review and cancellation, and what constitutes delivery", ["The packet fee and page count", "The association's budget", "The number of units"],
  "Named on the Virginia state outline."),
 ("va/disclosures", "Methamphetamine", 2, "Virginia requires specific disclosure where a property was previously used to:",
  "Manufacture methamphetamine", ["Store fuel", "House livestock", "Operate a business"],
  "Va. Code 55.1-708."),
 ("va/disclosures", "Advertising", 2, "Advertising rules appear in the Virginia outline under:",
  "Disclosure requirements", ["Escrow accounts", "Licensing", "Fair housing"],
  "PSI Virginia state outline, item 7."),
 ("va/disclosures", "Due diligence", 3, "Under the Act the owner makes:",
  "No representations on the matters the statute lists", ["A full warranty of condition", "A warranty of title", "A guarantee of value"],
  "Va. Code 55.1-703."),

 # licensing
 ("va/licensing", "Qualifying", 1, "The minimum age for a Virginia salesperson applicant is:",
  "18", ["17", "19", "21"],
  "PSI Virginia bulletin."),
 ("va/licensing", "Qualifying", 2, "A licensee from another state applying in Virginia takes:",
  "Only the state portion of the examination", ["Both portions", "Neither portion", "A reciprocity interview"],
  "PSI Virginia bulletin."),
 ("va/licensing", "Qualifying", 3, "After fingerprint results reach the Board, the licence application must follow within:",
  "90 calendar days", ["30 days", "6 months", "One year"],
  "Otherwise the applicant pays to be fingerprinted again."),
 ("va/licensing", "Post-licence", 1, "Virginia post-licence education is:",
  "At least 30 hours within the initial year of licensure", ["16 hours", "45 hours within two years", "None"],
  "Va. Code 54.1-2105.01(A)."),
 ("va/licensing", "Post-licence", 2, "A new salesperson who misses the post-licence deadline:",
  "Has the licence placed on inactive status until it is completed", ["Loses the licence permanently", "Is fined $500", "Must retake the exam"],
  "Va. Code 54.1-2105.01(A)."),
 ("va/licensing", "Post-licence", 3, "The one-year post-licence clock runs from:",
  "The last day of the month in which the licence was issued", ["The examination date", "1 January", "The date of application"],
  "Va. Code 54.1-2105.01(A)."),
 ("va/licensing", "Continuing education", 1, "Continuing education for a Virginia salesperson is:",
  "16 hours per licensing term", ["24 hours", "12 hours", "30 hours"],
  "18VAC135-20-101."),
 ("va/licensing", "Continuing education", 1, "Continuing education for a Virginia broker is:",
  "24 hours per licensing term", ["16 hours", "30 hours", "12 hours"],
  "Va. Code 54.1-2105.03(A)(1)."),
 ("va/licensing", "Continuing education", 2, "How many of a salesperson's 16 hours are mandated subjects?",
  "11", ["8", "16", "4"],
  "2 fair housing, 3 ethics, 2 agency, 2 contracts, 2 legal updates."),
 ("va/licensing", "Continuing education", 2, "The mandated ethics and standards of conduct hours total:",
  "Three", ["Two", "Four", "One"],
  "18VAC135-20-101."),
 ("va/licensing", "Continuing education", 2, "The legal updates hours must include:",
  "Flood zone areas and the National Flood Insurance Program", ["Appraisal standards", "Federal tax law", "Antitrust"],
  "18VAC135-20-101."),
 ("va/licensing", "Continuing education", 3, "The mandated contracts hours must cover:",
  "Contract principles, forms, and escrow deposits and accounts", ["Only contract forms", "Only escrow", "Only negotiation"],
  "18VAC135-20-101."),
 ("va/licensing", "Maintenance", 2, "A Virginia licensee who changes firm must:",
  "Inform the Board", ["Wait until renewal", "Retake the state portion", "Do nothing"],
  "Licence maintenance on the state outline."),
 ("va/licensing", "Discipline", 2, "Improper brokerage on the Virginia outline includes:",
  "Improper commission arrangements", ["Slow email replies", "Weekend open houses", "Advertising online"],
  "PSI Virginia state outline."),

 # fair housing
 ("va/fair-housing", "Classes", 1, "Which is protected under Virginia fair housing law but not the federal Fair Housing Act?",
  "Elderliness", ["Race", "Religion", "National origin"],
  "Va. Code 36-96.3(A)(1)."),
 ("va/fair-housing", "Classes", 1, "Virginia also protects:",
  "Source of funds", ["Credit score", "Occupation", "Length of residence"],
  "Va. Code 36-96.3(A)(1)."),
 ("va/fair-housing", "Classes", 2, "Virginia's protected classes include:",
  "Gender identity and military status", ["Political affiliation", "Union membership", "Education level"],
  "Va. Code 36-96.3(A)(1)."),
 ("va/fair-housing", "Practices", 2, "An advertisement indicating a preference based on a protected class is:",
  "Unlawful, even without any refusal", ["Lawful if the owner requested it", "Lawful in private sales", "Lawful if not published"],
  "Va. Code 36-96.3(A)(3)."),
 ("va/fair-housing", "Education", 2, "Fair housing in Virginia continuing education is:",
  "Two mandated hours each term", ["Optional", "Four hours", "One hour"],
  "18VAC135-20-101."),

 # acts
 ("va/acts", "Utilities", 1, "The Virginia Underground Utility Damage Prevention Act requires:",
  "Notice before excavation so utilities can be marked", ["A survey before listing", "Easements to be recorded", "Utility deposits"],
  "Named on the Virginia state outline."),
 ("va/acts", "Tenancies", 1, "Residential tenancies in Virginia are mainly governed by:",
  "The Virginia Residential Landlord and Tenant Act", ["The Condominium Act", "The POA Act", "The Common Interest Communities Act"],
  "Named on the Virginia state outline."),
 ("va/acts", "Associations", 2, "Unit-owner restrictions and CC&Rs fall under:",
  "The Virginia Condominium Act", ["The VRLTA", "The Underground Utility Damage Prevention Act"],
  "Named on the Virginia state outline."),
 ("va/acts", "Associations", 3, "Which appears on the Virginia BROKER outline but not the salesperson outline?",
  "The Virginia Common Interest Communities Act", ["The VRLTA", "The Condominium Act", "The POA Act"],
  "PSI marks it broker only."),

 # escrow
 ("va/escrow", "Protection", 1, "Escrow money held by a Virginia broker is:",
  "Kept separate from the broker's own funds and accounted for in a timely manner", ["The broker's once a contract is signed", "Held personally by the listing agent", "Paid to the seller at once"],
  "Va. Code 54.1-2108; 54.1-2131(A)(5)."),
 ("va/escrow", "Education", 2, "Escrow deposits and accounts are a required subject in:",
  "The two mandated contract hours of continuing education", ["The elective hours only", "Post-licence education only", "Broker education only"],
  "18VAC135-20-101."),
 ("va/escrow", "Audits", 2, "The Board may examine a broker's escrow records:",
  "Through inspection of records and audits", ["Only with a court order", "Only after a complaint", "Only at renewal"],
  "Named on the Virginia state outline."),
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
            "id": "va-" + hashlib.sha1(q.encode()).hexdigest()[:8],
            "portion": "georgia", "topic": topic, "subtopic": sub,
            "sub": topic + "|" + sub, "concept": "Virginia " + sub.lower(),
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
        "code": "VA", "name": "Virginia", "abbr": "VA",
        "regulator": "Virginia Real Estate Board",
        "pass": EXAM["pass"],
        "portions": {
            "national": {"scored": EXAM["national_scored"],
                         "minutes": EXAM["national_minutes"],
                         "pass": EXAM["national_pass"]},
            "georgia": {"name": "Virginia state", "scored": EXAM["state_scored"],
                        "minutes": EXAM["state_minutes"],
                        "pass": EXAM["state_pass"],
                        "blurb": "Title 54.1 chapter 21, the Board's regulations, disclosure and Virginia fair housing."},
        },
        "topics": topics, "bank": bank, "study": study,
        "sources": SOURCES, "diffs": DIFFS,
    }


# Where Virginia departs from the national rule.
DIFFS = {
    "national/agency": [
        "Virginia's LIMITED SERVICE AGENT must set out in writing not only the services provided but the standard agent duties NOT provided, conspicuously in bold or capitals (Va. Code 54.1-2138.1).",
        "A seller's agent must present written offers in a timely manner EVEN WHEN the property is already under contract, though they need not seek further offers (54.1-2131).",
        "The standard of care is ORDINARY care, and material facts are disclosed where the licensee has ACTUAL knowledge.",
    ],
    "national/disclosures": [
        "Virginia is a BUYER BEWARE state: the Residential Property Disclosure Act has the seller point the buyer to their own due diligence rather than warranting condition (Va. Code 55.1-703).",
        "Virginia-specific disclosures include the Chesapeake Bay Preservation Act, military aircraft noise and accident potential zones, septic systems, and prior methamphetamine manufacture (55.1-708).",
    ],
    "national/practice": [
        "Virginia fair housing adds ELDERLINESS, SOURCE OF FUNDS, sexual orientation, gender identity and military status to the federal classes (Va. Code 36-96.3).",
        "Salespersons take 30 hours of post-licence education in the first year, then 16 hours each term; brokers take 24 (54.1-2105.01, 54.1-2105.03).",
    ],
}


if __name__ == "__main__":
    import io, json, os
    here = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    out = os.path.join(here, "greprep", "packs", "VA.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    pack = build()
    with io.open(out, "w", encoding="utf-8") as f:
        json.dump(pack, f, ensure_ascii=False, indent=1, sort_keys=True)
    print("wrote", out, len(pack["bank"]), "questions,", len(pack["study"]), "lessons")
