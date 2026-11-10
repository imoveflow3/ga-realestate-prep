"""Washington state content: lessons and practice questions.

Washington splits the broker examination: the PSI bulletin's table gives
National 100 items in 150 minutes and State 30 items in 90 minutes, and a
candidate who passes only one portion must pass the other WITHIN SIX
MONTHS.

The pass mark is NOT a percentage. The bulletin says a scaled score of 70
is required on each portion of the Broker examination, and that "the
scaled score is not the same as a percentage" - the raw passing score may
vary slightly between forms. So the pack sets pass_published False and
gives 70% only as a study target.

Washington rewrote its agency law in 2023 c 318, effective in 2024: a
broker working with a buyer is a BUYER'S AGENT by default, every principal
needs a written SERVICES AGREEMENT, and a buyer's agreement carries a
DEFAULT TERM OF 60 DAYS. Guides written before that are wrong.

Every rule below was read from the official text on 2026-11-10:
  - RCW 18.86 (brokerage relationships) and RCW 18.85 (real estate
    brokers), from app.leg.wa.gov.
  - RCW 64.06 (seller disclosure), RCW 49.60.222 (unfair practices in real
    estate), RCW 82.45 (real estate excise tax).
  - WAC 308-124A (continuing education and core curriculum).
  - The PSI Washington Real Estate Commission Candidate Information
    Bulletin, for the examination table and the 30-item state outline.
The section a fact comes from is cited next to it. Do not add a fact here
without reading its source first.
"""

EXAM = {
    # Broker: National 100 items / 150 minutes, State 30 items / 90 minutes.
    # Scaled score of 70 on each portion, which is not a percentage.
    "state_scored": 30,
    "state_minutes": 90,
    "national_scored": 100,
    "national_minutes": 150,
    "pass": 0.70,
    "pass_published": False,
    "pass_note": ("Washington reports a SCALED score. The PSI bulletin requires a "
                  "scaled score of 70 on EACH portion of the Broker examination and "
                  "says the scaled score is not the same as a percentage - the raw "
                  "passing score varies slightly between forms. Candidates who pass "
                  "are told only PASS. Treat 70% here as a study target, not the "
                  "state's requirement. Pass one portion and you have SIX MONTHS to "
                  "pass the other, or you retake both."),
}

# PSI's Washington state outline, broker item counts: 4-5 + 8 + 13 + 4-5 = 30.
TOPICS = [
    ("wa/statutes", "Statutes & rules on licensee activity", 13,
     "Firm and affiliate relationships, trust money, records, offices, advertising."),
    ("wa/licensing", "Licensing requirements", 8,
     "Who needs a licence, eligibility, types, renewal, status, education."),
    ("wa/agency", "Brokerage relationships (agency)", 5,
     "Services agreements, buyer's and seller's agents, limited dual agency."),
    ("wa/general", "General rules", 4,
     "Definitions, the Commission and Director, investigations and sanctions."),
]

SOURCES = [
    {"by": "Washington State Legislature",
     "name": "RCW 18.86, Real Estate Brokerage Relationships",
     "note": "The agency law as rewritten by 2023 c 318: services agreements, duties, limited dual agency, compensation.",
     "url": "https://app.leg.wa.gov/RCW/default.aspx?cite=18.86"},
    {"by": "Washington State Legislature",
     "name": "RCW 18.85, Real Estate Brokers and Managing Brokers",
     "note": "Licence requirements, renewal, trust accounts, records and the grounds for discipline.",
     "url": "https://app.leg.wa.gov/RCW/default.aspx?cite=18.85"},
    {"by": "Washington State Legislature",
     "name": "RCW 64.06, RCW 49.60.222 and RCW 82.45",
     "note": "The seller disclosure statement, unfair practices in real estate, and the real estate excise tax.",
     "url": "https://app.leg.wa.gov/RCW/default.aspx?cite=64.06"},
    {"by": "Washington Department of Licensing",
     "name": "WAC 308-124A",
     "note": "The 30 clock hours of continuing education, including core and Washington fair housing curricula.",
     "url": "https://app.leg.wa.gov/WAC/default.aspx?cite=308-124A"},
    {"by": "PSI Services and the Washington Real Estate Commission",
     "name": "Washington Candidate Information Bulletin",
     "note": "National 100 items in 150 minutes, State 30 in 90, a scaled score of 70 on each portion, and the state outline.",
     "url": "https://test-takers.psiexams.com/ware"},
]


# --------------------------------------------------------------- lessons

STUDY = {}

STUDY["wa/statutes"] = {
    "summary": "Thirteen items, the biggest block. Trust money, records, advertising and supervision - and the long list in RCW 18.85.361 of things that cost you your licence.",
    "sections": [
        {"h": "Trust funds (RCW 18.85.285)",
         "l": ["If ANY LICENSEE EXERCISES CONTROL over real estate transaction funds, those funds ARE TRUST FUNDS.",
               "All licensees must keep clients' funds, INCLUDING ADVANCE FEES, SEPARATE AND APART AND PHYSICALLY SEGREGATED from the licensee's own funds.",
               "A brokers must DEPOSIT ALL FUNDS INTO THE FIRM'S TRUST BANK ACCOUNT THE NEXT BANKING DAY following receipt, unless the purchase and sale agreement provides for DEFERRED DEPOSIT OR DELIVERY - in which case the broker deposits or delivers promptly in accordance with the agreement.",
               "A firm need NOT maintain a trust account for a transaction where the purchase and sale agreement INSTRUCTS the broker to deliver the earnest money cheque DIRECTLY TO A NAMED CLOSING AGENT OR TO THE SELLER.",
               "Trust fund accounts must be in a RECOGNISED WASHINGTON STATE DEPOSITORY, and the firm must keep enough of its own funds there to open the account or prevent its closure.",
               "If a firm receives or maintains earnest money or client funds, it must keep a POOLED INTEREST-BEARING TRUST ACCOUNT - property management trust accounts excepted. The INTEREST, net of reasonable service charges, GOES TO THE STATE TREASURER for the WASHINGTON HOUSING TRUST FUND and the REAL ESTATE EDUCATION PROGRAM ACCOUNT. The firm NEED NOT notify the client of that use.",
               "Where trust funds are CLAIMED BY MORE THAN ONE PARTY, the designated broker must promptly give WRITTEN NOTICE to all contracting parties of the intent to disburse - naming the parties, the amount, to whom it goes, and a disbursement date NO LATER THAN 30 CONSECUTIVE DAYS after the notification date."],
         "check": [("A Washington broker must deposit client funds into the firm's trust account:", "The next banking day after receipt, unless the agreement provides for deferred deposit", ["Within 3 business days", "Within 5 days", "At closing"], "RCW 18.85.285(7)."),
                   ("Interest on a Washington pooled trust account goes to:", "The state treasurer, for the housing trust fund and the real estate education program account", ["The firm", "The buyer", "The seller"], "RCW 18.85.285(8)(b)."),
                   ("No trust account is needed where the purchase and sale agreement:", "Instructs the broker to deliver the earnest money directly to a named closing agent or the seller", ["Is for new construction", "Is a cash sale"], "RCW 18.85.285(6)."),
                   ("Where two parties claim the trust funds, disbursement must occur:", "No later than 30 consecutive days after the written notification date", ["Immediately", "Only by court order", "Within 10 days"], "RCW 18.85.285(9)."),
                   ("Funds a licensee exercises control over are:", "Trust funds", ["The firm's income", "The client's problem"], "RCW 18.85.285(2).")]},
        {"h": "Records and documents",
         "l": ["Brokers and managing brokers must submit COMPLETE COPIES of their transactions to their FIRM, and the DESIGNATED BROKER keeps adequate records of all transactions handled by or through the firm - including the PURCHASE AND SALE AGREEMENT, the EARNEST MONEY RECEIPT and an ITEMISATION OF RECEIPTS AND DISBURSEMENTS for each transaction. They are OPEN TO INSPECTION by the director (RCW 18.85.285(1)).",
               "Every licensee must DELIVER, WITHIN A REASONABLE TIME AFTER SIGNING, purchase and sale agreements, listing agreements and like instruments TO ALL PARTIES SIGNING THEM (RCW 18.85.285(3)); failing to furnish a copy is also a ground for discipline (RCW 18.85.361(18)).",
               "ESCROW OR TRUSTEE ACCOUNT RECORDS must be kept for THREE YEARS, showing to whom paid and other required information, available on demand (RCW 18.85.361(16)).",
               "A FIRM AND ITS DESIGNATED BROKER must preserve transaction records for THREE YEARS after they are submitted to the firm (RCW 18.85.361(17))."],
         "check": [("Washington transaction and trust records must be kept for:", "Three years", ["One year", "Five years", "Seven years"], "RCW 18.85.361(16), (17)."),
                   ("Signed purchase and sale agreements must be delivered to all signing parties:", "Within a reasonable time after signing", ["At closing", "Within 30 days"], "RCW 18.85.285(3)."),
                   ("Who keeps the firm's transaction records?", "The designated broker", ["Each individual broker", "The closing agent"], "RCW 18.85.285(1).")]},
        {"h": "Advertising and names",
         "l": ["Advertising WITHOUT INCLUDING THE FIRM'S NAME OR LICENSED ASSUMED NAME in a CLEAR AND CONSPICUOUS MANNER is a ground for discipline. The exception: a broker, managing broker or firm advertising their PERSONALLY OWNED real property need only disclose that THEY HOLD A REAL ESTATE LICENCE (RCW 18.85.361(8)).",
               "ALL real estate brokerage services must be conducted IN THE NAME OF THE FIRM or its licensed assumed name. A firm may use one or more ASSUMED NAMES but must obtain a SEPARATE LICENCE FOR EACH ONE before using it (RCW 18.85.221).",
               "A licence authorises only the person named on it, operating under the name on the licence (RCW 18.85.221)."],
         "check": [("A broker advertising their own home for sale must:", "Disclose that they hold a real estate licence", ["Include the firm name anyway", "Obtain the firm's written consent"], "RCW 18.85.361(8)."),
                   ("A firm wishing to trade under an additional assumed name must:", "Obtain a separate licence for each assumed name before using it", ["File a notice within 30 days", "Simply register it with the county"], "RCW 18.85.221."),
                   ("Real estate brokerage services must be conducted:", "In the name of the firm or its licensed assumed name", ["In the individual broker's name", "In the client's name"], "RCW 18.85.221.")]},
        {"h": "Grounds for discipline (RCW 18.85.361)",
         "l": ["CONVERSION of money, a contract, deed, note, mortgage or other evidence of title delivered in trust. Failing to return it WITHIN 30 DAYS after the owner is entitled and makes demand is PRIMA FACIE EVIDENCE of conversion.",
               "Accepting EARNEST MONEY OTHER THAN CASH OR ITS EQUIVALENT unless that fact is COMMUNICATED TO THE OWNER BEFORE acceptance of the offer AND shown in the purchase and sale agreement.",
               "Charging or accepting COMPENSATION FROM MORE THAN ONE PARTY in a transaction WITHOUT FIRST MAKING FULL WRITTEN DISCLOSURE to all interested parties.",
               "Accepting any UNDISCLOSED commission, rebate or direct profit on expenditures made for the principal.",
               "Directing a principal's transaction to a LENDER OR ESCROW COMPANY in expectation of a KICKBACK without first disclosing that expectation to the principal.",
               "BUYING, SELLING OR LEASING any interest in real property, directly or through a third party, WITHOUT DISCLOSING IN WRITING that the person is a real estate licensee.",
               "A broker or managing broker ACCEPTING A COMMISSION from anyone EXCEPT THE LICENSED FIRM they are licensed with.",
               "A firm, managing broker or designated broker FAILING TO EXERCISE ADEQUATE SUPERVISION over their brokers.",
               "Accepting employment for an APPRAISAL CONTINGENT ON A PREDETERMINED VALUE, or issuing a report on property the licensee has an interest in without stating that interest.",
               "DISCRIMINATION in hiring or in brokerage service activity under any local, county, state or federal antidiscrimination law.",
               "Any conduct in a transaction demonstrating BAD FAITH, DISHONESTY, UNTRUSTWORTHINESS OR INCOMPETENCE."],
         "check": [("Taking a promissory note as earnest money is permissible only if:", "The owner is told before accepting the offer and the fact is shown in the purchase and sale agreement", ["The broker approves", "It is converted to cash before closing"], "RCW 18.85.361(9)."),
                   ("Accepting compensation from both parties requires:", "Full written disclosure to all interested parties first", ["Oral consent", "Nothing, if the amounts are equal"], "RCW 18.85.361(10)."),
                   ("A licensee buying property for themselves must disclose:", "In writing, that they are a real estate licensee", ["Only their firm name", "Nothing, if buying as a private party"], "RCW 18.85.361(21)."),
                   ("Failing to return trust property within 30 days of demand is:", "Prima facie evidence of conversion", ["A technical violation only", "A civil matter only"], "RCW 18.85.361(5)."),
                   ("A broker may accept a commission from:", "The licensed real estate firm they are licensed with", ["Any party to the transaction", "The lender"], "RCW 18.85.361(19).")]},
        {"h": "Affiliation and termination (RCW 18.85.291)",
         "l": ["Licences are KEPT AT ALL TIMES BY THE FIRM, and when a broker or managing broker ceases to represent the firm their licence CEASES TO BE IN FORCE.",
               "The broker must give WRITTEN NOTIFICATION to the firm's DESIGNATED BROKER on terminating affiliation; the firm, through the designated broker, then notifies the director and SURRENDERS the licence.",
               "A designated broker who fails to promptly notify the director after the affected broker's demand is subject to DISCIPLINARY ACTION, against both the firm and the designated broker.",
               "Where the firm terminates a broker FOR A VIOLATION of ch. 18.85, 18.86 or 18.235, the firm must IMMEDIATELY FILE A WRITTEN STATEMENT OF THE FACTS with the director."],
         "check": [("When a Washington broker leaves a firm, their licence:", "Ceases to be in force", ["Transfers automatically", "Stays active for 30 days"], "RCW 18.85.291."),
                   ("A firm that terminates a broker for a violation must:", "Immediately file a written statement of the facts with the director", ["Wait for the Commission to ask", "Do nothing"], "RCW 18.85.291."),
                   ("A designated broker who will not notify the director of a termination:", "Is subject to disciplinary action, as is the firm", ["Faces no consequence", "Is fined by the MLS"], "RCW 18.85.291.")]},
    ],
    "traps": [
        "Next banking day, not three days, for the trust deposit.",
        "Trust interest goes to the state housing trust fund - and you need not tell the client.",
        "Three years for records; 30 days before return of trust property becomes prima facie conversion.",
        "Advertising your own property: disclose that you hold a licence.",
    ],
    "vocab": [
        ["Designated broker", "The broker who runs and is responsible for a firm."],
        ["Managing broker", "A broker qualified to supervise other brokers in a firm."],
        ["Pooled interest-bearing trust account", "The account whose interest funds state housing and education."],
        ["Conversion", "Using trust money or property for one's own purposes."],
        ["Assumed name", "A separately licensed trading name of a firm."],
    ],
    "examples": [
        {"t": "Earnest money arrives Friday",
         "s": "A broker receives a $10,000 earnest money cheque on Friday afternoon. The purchase and sale agreement says nothing about deferred deposit.",
         "w": ["There is no deferred-deposit instruction, so the ordinary rule applies.",
               "The funds go into the firm's trust bank account the NEXT BANKING DAY - Monday.",
               "They sit in a pooled interest-bearing account, and the interest is remitted to the state."],
         "k": "Next banking day, unless the agreement itself defers the deposit."},
    ],
}

STUDY["wa/licensing"] = {
    "summary": "Eight items. The numbers: 18 years old, 90 hours before the examination, a two-year licence, 90 more hours for the first renewal, then 30 hours of continuing education.",
    "sections": [
        {"h": "Broker's licence (RCW 18.85.101)",
         "l": ["The applicant must be 18 YEARS OF AGE OR OLDER and hold a HIGH SCHOOL DIPLOMA OR ITS EQUIVALENT.",
               "They must complete 90 HOURS of instruction in real estate - FUNDAMENTALS, which must include 3 HOURS ON FAIR HOUSING AND CONSUMER PROTECTION ISSUES, and PRACTICES. Each course must be completed WITHIN TWO YEARS before applying for the examination, be approved by the director, and be passed with a course examination.",
               "They must pass the BROKER'S LICENCE EXAMINATION.",
               "A broker is LICENSED TO ONE FIRM AT A TIME and is SUPERVISED by a designated or managing broker.",
               "FIRST RENEWAL: the education requirement is a further 90 HOURS, including REAL ESTATE LAW - which must itself include 3 HOURS ON FAIR HOUSING AND CONSUMER PROTECTION - plus ADVANCED PRACTICES and continuing education."],
         "check": [("Prelicence education for a Washington broker is:", "90 hours, including 3 hours of fair housing and consumer protection within fundamentals", ["60 hours", "120 hours", "30 hours"], "RCW 18.85.101(1)(c)."),
                   ("Each prelicence course must be completed within:", "Two years before applying for the examination", ["Five years", "One year"], "RCW 18.85.101(1)(c)."),
                   ("The FIRST renewal of a Washington broker's licence requires:", "A further 90 hours, including real estate law with 3 hours of fair housing and consumer protection, and advanced practices", ["30 hours of continuing education only", "Nothing extra"], "RCW 18.85.101(2)."),
                   ("A Washington broker may be licensed to:", "One firm at a time", ["Two firms", "Any number of firms"], "RCW 18.85.101(3).")]},
        {"h": "Managing broker's licence (RCW 18.85.111)",
         "l": ["18 OR OLDER, a HIGH SCHOOL DIPLOMA or equivalent, and a MINIMUM OF THREE YEARS of licensed experience as a FULL-TIME REAL ESTATE BROKER in Washington or a comparable jurisdiction WITHIN THE PREVIOUS FIVE YEARS - or other qualifying practical experience by rule.",
               "90 HOURS of instruction including REAL ESTATE BROKERAGE MANAGEMENT, BUSINESS MANAGEMENT and ADVANCED REAL ESTATE LAW. Each course must be AT LEAST 30 CLOCK HOURS, carry a comprehensive examination, and be completed WITHIN THREE YEARS before applying.",
               "A managing broker may be LICENSED TO ONE FIRM ONLY at any one time."],
         "check": [("A Washington managing broker applicant needs:", "Three years as a full-time broker within the previous five years", ["One year of licensure", "Five years with no time limit"], "RCW 18.85.111(1)(c)."),
                   ("Each managing broker course must be:", "At least 30 clock hours, with a comprehensive examination", ["At least 15 hours", "Any length"], "RCW 18.85.111(1)(d)."),
                   ("Those courses must be completed within:", "Three years before applying for the examination", ["Two years", "Five years"], "RCW 18.85.111(1)(d).")]},
        {"h": "Renewal, expiry and cancellation (RCW 18.85.191)",
         "l": ["A licence EXPIRES TWO YEARS from its issuance date, and must be RENEWED EVERY TWO YEARS with the biennial fee.",
               "Firm licences for partnerships, LLPs, LLCs, corporations and other business entities expire WHEN THE REGISTRATION OR CERTIFICATE OF AUTHORITY filed with the SECRETARY OF STATE expires.",
               "A late application brings a PENALTY FEE, and the director's acceptance of a late application is NOT A WAIVER of the delinquency.",
               "A licence whose renewal fee is not received WITHIN ONE YEAR of expiry is CANCELLED; a new licence then requires satisfying the procedures and requirements prescribed by rule.",
               "The director must set by rule a procedure and schedule so that all active licensees, and those applying for active status, renewal or reinstatement, have FINGERPRINT AND BACKGROUND CHECKS done REGULARLY."],
         "check": [("A Washington real estate licence expires:", "Two years from the issuance date", ["Annually", "Every four years"], "RCW 18.85.191."),
                   ("A licence is cancelled if the renewal fee is not received within:", "One year of expiry", ["30 days", "Three years"], "RCW 18.85.191."),
                   ("A firm licence issued to a corporation expires:", "When its registration or certificate of authority with the secretary of state expires", ["Two years after issue", "Never"], "RCW 18.85.191.")]},
        {"h": "Continuing education (WAC 308-124A)",
         "l": ["30 CLOCK HOURS of approved courses per renewal.",
               "Of those 30, THREE CLOCK HOURS must be the prescribed CORE CURRICULUM and THREE CLOCK HOURS the prescribed WASHINGTON REAL ESTATE FAIR HOUSING curriculum. Failing to complete them RESULTS IN DENIAL OF LICENCE RENEWAL.",
               "The CORE CURRICULUM may be a separate three-hour course or three hours inside an approved course of thirty hours or less, and must be COMPLETED WITHIN 24 MONTHS of the renewal date. Core taken more than 24 but within 36 months counts as ordinary continuing education, NOT as core.",
               "Continuing education clock hours must be STARTED AFTER the first licence is issued.",
               "A licensee MUST NOT place a licence on INACTIVE STATUS to avoid continuing education or post-licensing requirements. A licensee inactive LESS THAN ONE YEAR must attest to completing the hours to reactivate, and attestations are SUBJECT TO AUDIT."],
         "check": [("Washington continuing education is:", "30 clock hours per renewal", ["18 hours", "12 hours", "45 hours"], "WAC 308-124A."),
                   ("Of those hours, the prescribed requirements are:", "3 hours of core curriculum and 3 hours of Washington real estate fair housing curriculum", ["6 hours of ethics", "3 hours of agency only"], "WAC 308-124A."),
                   ("Core curriculum must be completed within:", "24 months of the renewal date", ["36 months", "12 months"], "WAC 308-124A-800."),
                   ("Going inactive to avoid continuing education is:", "Prohibited", ["A recognised option", "Allowed once"], "WAC 308-124A."),
                   ("Failing to complete the prescribed core and fair housing hours results in:", "Denial of licence renewal", ["A fine", "A 30-day grace period"], "WAC 308-124A.")]},
    ],
    "traps": [
        "90 hours before the exam AND another 90 at the first renewal. Both carry 3 fair housing hours.",
        "30 hours of continuing education, of which 3 core and 3 Washington fair housing.",
        "Two-year licence; cancelled after one year unrenewed.",
        "Managing broker needs 3 years full time within the last 5.",
    ],
    "vocab": [
        ["Designated broker", "The managing broker responsible for a firm's licence."],
        ["Core curriculum", "The prescribed 3-hour course required each renewal."],
        ["Inactive status", "A licence not in use, which does not excuse education."],
        ["Clock hour", "The unit Washington counts education in."],
    ],
    "examples": [],
}

STUDY["wa/agency"] = {
    "summary": "Four or five items, and they hang on one 2023 rewrite: work with a buyer and you ARE their agent unless a services agreement says otherwise.",
    "sections": [
        {"h": "What you are by default (RCW 18.86.020)",
         "l": ["A broker who performs real estate brokerage services FOR A BUYER IS A BUYER'S AGENT unless (a) the firm appointed the broker to represent the SELLER under a services agreement, (b) the firm appointed the broker to represent BOTH under services agreements, making the broker a LIMITED DUAL AGENT, or (c) the broker IS the seller.",
               "A firm MUST ENTER INTO A SERVICES AGREEMENT with the principal BEFORE, OR AS SOON AS REASONABLY PRACTICAL AFTER, its appointed broker starts rendering brokerage services.",
               "The services agreement must state: the TERM - and for a BUYER a DEFAULT TERM OF 60 DAYS with the option of a longer one; the BROKER APPOINTED as agent; whether the relationship is EXCLUSIVE OR NONEXCLUSIVE, with CHECKBOX OPTIONS for a buyer; whether the principal consents to LIMITED DUAL AGENCY, SEPARATELY INITIALLED, with an acknowledgment that a limited dual agent MAY NOT ADVOCATE TERMS FAVOURABLE TO ONE PRINCIPAL TO THE DETRIMENT OF THE OTHER; and whether the principal consents to the DESIGNATED BROKER and any supervising MANAGING BROKER acting as limited dual agents where different brokers in the firm represent different parties.",
               "NO services agreement is required where a broker acts as a buyer's agent SOLELY FOR COMMERCIAL REAL ESTATE.",
               "A broker may work with the same party in SEPARATE TRANSACTIONS under DIFFERENT relationships - representing them in one and not in another - as long as the chapter is complied with for each."],
         "check": [("A Washington broker working with a buyer is, by default:", "The buyer's agent", ["A subagent of the seller", "A dual agent", "Unrepresented"], "RCW 18.86.020(1)."),
                   ("The default term of a buyer's services agreement is:", "60 days, with the option of a longer term", ["30 days", "6 months", "Indefinite"], "RCW 18.86.020(2)(b)(i)."),
                   ("Consent to limited dual agency must be:", "Separately initialled by the principal in the services agreement", ["Oral", "Implied by signing the listing"], "RCW 18.86.020(2)(b)(iv)."),
                   ("A services agreement is NOT required where the broker acts as a buyer's agent:", "Solely for commercial real estate", ["In any new construction sale", "For a cash buyer"], "RCW 18.86.020(3)."),
                   ("The buyer's services agreement must offer:", "Checkbox options for an exclusive or nonexclusive relationship", ["A choice of commission rates", "A list of lenders"], "RCW 18.86.020(2)(b)(iii).")]},
        {"h": "Duties owed to EVERYONE (RCW 18.86.030)",
         "p": ["A broker owes these to their principal AND to all parties, and they MAY NOT BE WAIVED:"],
         "l": ["To exercise REASONABLE SKILL AND CARE.",
               "To deal HONESTLY AND IN GOOD FAITH.",
               "To present ALL WRITTEN OFFERS, WRITTEN NOTICES AND OTHER WRITTEN COMMUNICATIONS to and from either party in a TIMELY MANNER - REGARDLESS of whether the property is already under contract or the buyer is already a party to a contract to purchase.",
               "To DISCLOSE ALL EXISTING MATERIAL FACTS known to the broker and not apparent or readily ascertainable to a party. This does NOT imply a duty to investigate matters the broker has not agreed to investigate.",
               "To ACCOUNT IN A TIMELY MANNER for all money and property received.",
               "To PROVIDE THE AGENCY PAMPHLET prescribed by RCW 18.86.120 and obtain an ACKNOWLEDGMENT OF RECEIPT - to a party the broker renders services to BEFORE THAT PARTY SIGNS A SERVICES AGREEMENT, and to an unrepresented party BEFORE THEY SIGN AN OFFER or as soon as reasonably practical.",
               "To DISCLOSE IN WRITING, before the principal signs an offer and before mutual agreement, whether the broker represents the buyer, the seller or both as a LIMITED DUAL AGENT - in a separate paragraph titled 'AGENCY DISCLOSURE' - and any TERMS OF COMPENSATION offered by a party or firm to a firm representing another party.",
               "Unless otherwise agreed, a broker owes NO DUTY to inspect the property independently, to investigate either party's finances, or to verify statements made by either party or by a source reasonably believed reliable."],
         "check": [("Written offers must be presented:", "Timely, even where the property is already under contract", ["Only until mutual acceptance", "Only above list price"], "RCW 18.86.030(1)(c)."),
                   ("The agency pamphlet must reach a party the broker serves:", "Before that party signs a services agreement", ["At closing", "Within 5 days of the offer"], "RCW 18.86.030(1)(f)(i)."),
                   ("An unrepresented party must get the pamphlet:", "Before they sign an offer, or as soon as reasonably practical", ["Never", "Only on request"], "RCW 18.86.030(1)(f)(ii)."),
                   ("The capacity disclosure must appear in a separate paragraph titled:", "Agency Disclosure", ["Material Facts", "Notice to Consumer"], "RCW 18.86.030(1)(g)(i)."),
                   ("Unless otherwise agreed, a Washington broker owes no duty to:", "Independently inspect the property or verify a party's statements", ["Disclose known material facts", "Account for money received"], "RCW 18.86.030(2).")]},
        {"h": "Seller's agent, buyer's agent, limited dual agent",
         "l": ["A SELLER'S AGENT or BUYER'S AGENT additionally owes LOYALTY - taking no action adverse or detrimental to the principal's interest; TIMELY DISCLOSURE OF CONFLICTS; advice to SEEK EXPERT HELP beyond the agent's expertise; CONFIDENTIALITY, with no disclosure of confidential information EXCEPT UNDER SUBPOENA OR COURT ORDER, EVEN AFTER TERMINATION of the relationship; and a GOOD FAITH AND CONTINUOUS EFFORT to find a buyer or a property - though not obliged to seek more while the property or the buyer is under an existing contract (RCW 18.86.040, 18.86.050).",
               "Showing the same property to OTHER prospective buyers, or representing MORE THAN ONE BUYER through different brokers of the same firm in COMPETING transactions on the same property, does NOT in itself breach loyalty or create a conflict (RCW 18.86.050(2)).",
               "A broker may act as a LIMITED DUAL AGENT ONLY WITH THE WRITTEN CONSENT OF BOTH PARTIES, SET FORTH IN THE SERVICES AGREEMENT (RCW 18.86.060(1)). The limited dual agent takes no action adverse to either, discloses conflicts to both, advises both to seek expert advice, and discloses NO confidential information from or about EITHER party except under subpoena or court order, even after termination.",
               "Where DIFFERENT BROKERS AFFILIATED WITH THE SAME FIRM represent DIFFERENT PARTIES, the firm's DESIGNATED BROKER and any MANAGING BROKER supervising both IS A LIMITED DUAL AGENT - and each appointed broker SOLELY REPRESENTS their own party (RCW 18.86.060(5))."],
         "check": [("A Washington limited dual agent may act only with:", "The written consent of both parties, set out in the services agreement", ["Oral consent", "The designated broker's approval"], "RCW 18.86.060(1)."),
                   ("Confidential information may be disclosed:", "Only under subpoena or court order, even after the relationship ends", ["Once the deal closes", "With the other agent's consent"], "RCW 18.86.050(1)(d)."),
                   ("When two brokers of one firm represent opposite parties:", "The designated broker and any supervising managing broker are limited dual agents, while each appointed broker solely represents their own party", ["Both brokers are dual agents", "The arrangement is prohibited"], "RCW 18.86.060(5)."),
                   ("Showing the same property to other buyers:", "Does not in itself breach the duty of loyalty", ["Breaches loyalty", "Requires written consent"], "RCW 18.86.050(2)(a).")]},
        {"h": "Compensation (RCW 18.86.080)",
         "l": ["Compensation may be paid by the SELLER, the BUYER, a THIRD PARTY, or SHARED BETWEEN FIRMS, and a firm may be compensated BY MORE THAN ONE PARTY.",
               "An agreement to pay, or payment of, compensation DOES NOT ESTABLISH AN AGENCY RELATIONSHIP between the payer and the broker.",
               "A firm may receive compensation BASED ON THE PURCHASE PRICE without breaching any duty.",
               "To receive compensation, a firm MUST HAVE A SERVICES AGREEMENT stating the AMOUNT the principal agrees to pay, the principal's CONSENT (if any) to compensation sharing between firms and parties, the principal's CONSENT (if any) to being compensated by MORE THAN ONE PARTY, and - in a BUYER'S agreement - WHETHER THE BROKER WILL SHOW THE BUYER PROPERTIES IF NO PARTY OR FIRM OFFERS TO PAY the firm.",
               "For COMMERCIAL real estate, a broker serving a buyer may, instead of a services agreement, disclose in writing before the buyer signs an offer the SOURCES AND AMOUNTS of compensation expected, in a separate paragraph titled 'COMPENSATION DISCLOSURE'.",
               "No services agreement is needed to be paid for a BROKER'S PRICE OPINION or for a REFERRAL by one firm to another where the referring firm provided no brokerage services."],
         "check": [("Paying a broker's compensation:", "Does not establish an agency relationship with the payer", ["Makes the payer the client", "Creates dual agency"], "RCW 18.86.080(2)."),
                   ("A buyer's services agreement must state:", "Whether the broker will show properties where no party or firm offers to pay the firm", ["The buyer's maximum price", "The lender's name"], "RCW 18.86.080(7)(b)."),
                   ("A firm may be compensated:", "By more than one party in a transaction", ["Only by its own client", "Only by the seller"], "RCW 18.86.080(5)."),
                   ("A referral fee between firms where the referring firm did no brokerage work:", "Needs no services agreement", ["Is prohibited", "Needs the client's consent"], "RCW 18.86.080(9)."),
                   ("Compensation based on the purchase price:", "Does not breach any duty to the buyer or seller", ["Is prohibited", "Requires separate consent"], "RCW 18.86.080(6).")]},
    ],
    "traps": [
        "60-day default buyer term - a Washington-specific number.",
        "A payment does not make the payer your client.",
        "Confidentiality breaks only for a subpoena or court order, and it survives termination.",
        "The designated broker becomes the limited dual agent when two firm brokers split a deal.",
    ],
    "vocab": [
        ["Services agreement", "The written agreement appointing a broker as agent."],
        ["Limited dual agent", "A broker representing both parties with written consent."],
        ["Agency pamphlet", "The RCW 18.86.120 pamphlet that must be given and acknowledged."],
        ["Appointed broker", "The individual broker the firm appoints for a principal."],
    ],
    "examples": [
        {"t": "No one is offering to pay",
         "s": "A buyer asks you to show a for-sale-by-owner where the seller offers nothing to your firm.",
         "w": ["Your firm needs a services agreement with the buyer to be paid at all.",
               "That agreement must already say whether you will show properties when no party or firm offers compensation.",
               "The buyer may agree to pay your firm directly; paying you does not change who you represent."],
         "k": "The question is answered in the services agreement before it ever arises."},
    ],
}

STUDY["wa/general"] = {
    "summary": "Four items on who regulates and what else Washington requires: the seller disclosure statement, the discrimination law, and the excise tax.",
    "sections": [
        {"h": "The seller disclosure statement (RCW 64.06)",
         "l": ["Unless the buyer has EXPRESSLY WAIVED the right to receive it, the seller must deliver a COMPLETED, SIGNED AND DATED real property transfer disclosure statement NOT LATER THAN FIVE BUSINESS DAYS - or as otherwise agreed - after MUTUAL ACCEPTANCE.",
               "Within THREE BUSINESS DAYS of receiving it - or as otherwise agreed - the buyer may either APPROVE AND ACCEPT it or RESCIND the agreement, in the BUYER'S SOLE DISCRETION, by delivering WRITTEN NOTICE of rescission within that period. On rescission the buyer gets back ALL DEPOSITS AND OTHER CONSIDERATION, less any agreed disbursements, and the agreement is VOID.",
               "If the buyer delivers NO written rescission notice within the three business days, the statement is DEEMED APPROVED AND ACCEPTED.",
               "If the seller later learns of additional information or an ADVERSE CHANGE making a disclosure inaccurate, the seller must AMEND and deliver the amendment - unless the seller CORRECTS the problem at least THREE BUSINESS DAYS BEFORE CLOSING. Otherwise the buyer may accept the amendment or RESCIND WITHIN THREE BUSINESS DAYS of receiving it.",
               "If closing is scheduled inside that three-business-day rescission period, the CLOSING DATE IS EXTENDED until the period expires."],
         "check": [("The Washington seller disclosure statement is due:", "Not later than five business days after mutual acceptance, unless otherwise agreed", ["Before the offer", "At closing", "Within 10 days"], "RCW 64.06.030."),
                   ("The buyer's right to rescind after receiving it runs for:", "Three business days", ["72 hours", "Five business days", "Ten days"], "RCW 64.06.030."),
                   ("If the buyer sends no rescission notice in that window, the statement is:", "Deemed approved and accepted", ["Void", "Resent by the seller"], "RCW 64.06.030."),
                   ("A seller who corrects an adverse change at least three business days before closing:", "Need not amend, and the buyer has no right of rescission", ["Must still amend", "Must extend closing"], "RCW 64.06.040(1)."),
                   ("If closing falls inside the three-business-day rescission period:", "The closing date is extended until the period expires", ["The buyer loses the right", "The sale is void"], "RCW 64.06.040(1).")]},
        {"h": "Unfair practices in real estate (RCW 49.60.222)",
         "p": ["It is an UNFAIR PRACTICE for any person, acting for themselves or another, to refuse a real estate transaction, discriminate in its terms, refuse to transmit a bona fide offer, refuse to negotiate, misrepresent availability, make a dwelling unavailable, publish a discriminatory advertisement or application, take a discriminatory listing, expel a person from occupancy, or discriminate in financing, because of:"],
         "l": ["SEX", "MARITAL STATUS", "SEXUAL ORIENTATION", "RACE", "CREED",
               "COLOR", "NATIONAL ORIGIN", "CITIZENSHIP OR IMMIGRATION STATUS",
               "FAMILIES WITH CHILDREN STATUS",
               "HONORABLY DISCHARGED VETERAN OR MILITARY STATUS",
               "THE PRESENCE OF ANY SENSORY, MENTAL OR PHYSICAL DISABILITY",
               "THE USE OF A TRAINED DOG GUIDE OR SERVICE ANIMAL BY A PERSON WITH A DISABILITY",
               "The protection reaches not only the buyer or renter but a person who will RESIDE IN the dwelling afterwards and ANY PERSON ASSOCIATED with the buyer or renter.",
               "Discrimination in hiring or in brokerage service activity under ANY local, county, state or federal antidiscrimination law is separately a ground for DISCIPLINE (RCW 18.85.361(15))."],
         "check": [("Which is protected in Washington real estate but not by the federal Fair Housing Act?", "Citizenship or immigration status", ["Race", "Color", "National origin"], "RCW 49.60.222(1)."),
                   ("Washington also protects:", "Honorably discharged veteran or military status", ["Credit score", "Occupation"], "RCW 49.60.222(1)."),
                   ("The use of a trained dog guide or service animal is:", "A protected basis in its own right", ["Covered only by the ADA", "Not protected in housing"], "RCW 49.60.222(1)."),
                   ("The protection extends to:", "People who will reside in the dwelling afterwards and people associated with the buyer or renter", ["The named buyer only", "Only tenants"], "RCW 49.60.222(1)(f).")]},
        {"h": "The real estate excise tax (RCW 82.45)",
         "l": ["An excise tax is imposed on EACH SALE of real property. Since 1 January 2020 the state rate is GRADUATED on portions of the selling price: 1.1%, then 1.28%, then 2.75%, then 3% on the highest portion. TIMBERLAND AND AGRICULTURAL LAND are taxed at a flat 1.28%.",
               "The statutory thresholds between the brackets are ADJUSTED BY THE DEPARTMENT OF REVENUE EVERY FOURTH YEAR, by the lesser of the growth in the consumer price index for shelter or 5%, and the department PUBLISHES the updated thresholds - so always check the current figures rather than memorising dollar amounts.",
               "The tax is THE OBLIGATION OF THE SELLER, and the department may enforce it by an ACTION OF DEBT against the seller or by proceeding as for the FORECLOSURE OF A MORTGAGE (RCW 82.45.080)."],
         "check": [("The Washington real estate excise tax is the obligation of:", "The seller", ["The buyer", "The lender", "The closing agent"], "RCW 82.45.080(1)."),
                   ("Since 2020 the state excise tax is:", "Graduated by portions of the selling price, from 1.1% up to 3%", ["A flat 1.28%", "A flat 1.78%"], "RCW 82.45.060(1)(b)."),
                   ("Timberland and agricultural land are taxed at:", "A flat 1.28% of the selling price", ["The graduated rates", "1.1% flat"], "RCW 82.45.060(1)(c)."),
                   ("The bracket thresholds are adjusted:", "Every fourth year, by the lesser of CPI-shelter growth or 5%", ["Annually by inflation", "Never"], "RCW 82.45.060(2).")]},
        {"h": "Discipline and the Commission",
         "l": ["The director may take disciplinary action and impose the sanctions and fines in RCW 18.235.110 against a broker, managing broker, designated broker or firm - WHETHER OR NOT the transaction was for the person's own account - for violating ch. 18.85, ch. 18.86's RCW 18.86.030 duties, ch. 18.235, ch. 64.36 or ch. 19.105, or the rules under them (RCW 18.85.361(1)).",
               "The outline also covers DEFINITIONS, the POWERS AND DUTIES OF THE REAL ESTATE COMMISSION AND DIRECTOR, INVESTIGATIONS AND SANCTIONS (violations, hearings and appeals, penalties), and the REAL ESTATE RESEARCH CENTER.",
               "A licensee who FAILS, ON DEMAND, to disclose information within their knowledge or to produce a document, book or record for inspection by the director is subject to discipline (RCW 18.85.361(6))."],
         "check": [("Discipline can follow conduct in a transaction:", "Whether or not it was for the licensee's own account", ["Only in client transactions", "Only where a client complains"], "RCW 18.85.361."),
                   ("Refusing to produce records for the director on demand is:", "A ground for discipline", ["Permitted without a subpoena", "A civil matter"], "RCW 18.85.361(6)."),
                   ("Breaching the RCW 18.86.030 duties is:", "A ground for discipline under the licence law too", ["Only a civil claim", "Outside the director's power"], "RCW 18.85.361(1).")]},
    ],
    "traps": [
        "Five business days to deliver the disclosure, three business days to rescind.",
        "Citizenship or immigration status, veteran or military status, and service animal use are Washington additions.",
        "The excise tax is graduated and the SELLER owes it; the thresholds move every four years.",
    ],
    "vocab": [
        ["Form 17", "The common name for the real property transfer disclosure statement."],
        ["Mutual acceptance", "The point the five-business-day clock starts from."],
        ["REET", "The real estate excise tax."],
        ["Unfair practice", "The term RCW 49.60 uses for discrimination."],
    ],
    "examples": [],
}


# ------------------------------------------------------------- questions

Q = [
 # statutes
 ("wa/statutes", "Trust funds", 1, "A Washington broker must deposit client funds into the firm's trust bank account:",
  "The next banking day after receipt, unless the agreement provides for deferred deposit", ["Within 3 business days", "Within 5 banking days", "At closing"],
  "RCW 18.85.285(7)."),
 ("wa/statutes", "Trust funds", 1, "Interest on a Washington pooled trust account is paid to:",
  "The state treasurer, for the housing trust fund and the real estate education program account", ["The firm", "The buyer", "The seller"],
  "RCW 18.85.285(8)(b)."),
 ("wa/statutes", "Trust funds", 2, "No trust account is required where the purchase and sale agreement:",
  "Instructs the broker to deliver the earnest money directly to a named closing agent or to the seller", ["Is an all-cash sale", "Is for new construction"],
  "RCW 18.85.285(6)."),
 ("wa/statutes", "Trust funds", 2, "Where trust funds are claimed by more than one party, disbursement must occur:",
  "No later than 30 consecutive days after the written notification date", ["Immediately", "Only on a court order", "Within 10 days"],
  "RCW 18.85.285(9)."),
 ("wa/statutes", "Trust funds", 2, "Funds over which a licensee exercises control in a transaction are:",
  "Trust funds", ["The firm's income", "The client's own problem", "Escrow company property"],
  "RCW 18.85.285(2)."),
 ("wa/statutes", "Trust funds", 3, "Must a Washington firm tell the client that trust account interest funds state housing programmes?",
  "No; the firm or designated broker is not required to notify the client", ["Yes, in writing", "Yes, at closing"],
  "RCW 18.85.285(8)(b)."),
 ("wa/statutes", "Records", 1, "Washington transaction and escrow records must be kept for:",
  "Three years", ["One year", "Five years", "Seven years"],
  "RCW 18.85.361(16), (17)."),
 ("wa/statutes", "Records", 2, "Signed purchase and sale agreements must be delivered to all signing parties:",
  "Within a reasonable time after signing", ["At closing", "Within 30 days", "Only on request"],
  "RCW 18.85.285(3)."),
 ("wa/statutes", "Records", 2, "Who must keep the firm's transaction records?",
  "The designated broker", ["Each individual broker", "The closing agent", "The managing broker only"],
  "RCW 18.85.285(1)."),
 ("wa/statutes", "Advertising", 1, "A Washington broker advertising their own home for sale must:",
  "Disclose that they hold a real estate licence", ["Include the firm's name anyway", "Get the firm's written consent", "Use the MLS"],
  "RCW 18.85.361(8)."),
 ("wa/statutes", "Advertising", 2, "A firm wanting to trade under an extra assumed name must:",
  "Obtain a separate licence for each assumed name before using it", ["File a notice within 30 days", "Register it with the county"],
  "RCW 18.85.221."),
 ("wa/statutes", "Advertising", 2, "All real estate brokerage services in Washington must be conducted:",
  "In the name of the firm or its licensed assumed name", ["In the individual broker's name", "In the designated broker's name"],
  "RCW 18.85.221."),
 ("wa/statutes", "Discipline", 1, "Taking a promissory note as earnest money is permitted only if:",
  "The owner is told before accepting the offer and the fact is shown in the purchase and sale agreement", ["The broker approves it", "It is cashed before closing"],
  "RCW 18.85.361(9)."),
 ("wa/statutes", "Discipline", 1, "Accepting compensation from more than one party requires:",
  "Full written disclosure to all interested parties first", ["Oral consent from both", "Nothing if the amounts are equal"],
  "RCW 18.85.361(10)."),
 ("wa/statutes", "Discipline", 2, "A licensee buying property for their own account must disclose:",
  "In writing, that they are a real estate licensee", ["Only the firm's name", "Nothing, as a private party"],
  "RCW 18.85.361(21)."),
 ("wa/statutes", "Discipline", 2, "Failing to return trust property within 30 days after demand is:",
  "Prima facie evidence of conversion", ["A technical violation only", "A civil matter only"],
  "RCW 18.85.361(5)."),
 ("wa/statutes", "Discipline", 2, "A Washington broker may accept a commission from:",
  "The licensed real estate firm they are licensed with", ["Any party to the transaction", "The lender", "The escrow company"],
  "RCW 18.85.361(19)."),
 ("wa/statutes", "Discipline", 3, "Referring a principal to a lender expecting a kickback is permitted only if:",
  "The expectation is disclosed to the principal first", ["The kickback is under $500", "The lender is licensed"],
  "RCW 18.85.361(20)."),
 ("wa/statutes", "Discipline", 3, "Accepting an appraisal engagement contingent on reporting a predetermined value is:",
  "A ground for discipline", ["Allowed with disclosure", "Allowed for lender work"],
  "RCW 18.85.361(12)."),
 ("wa/statutes", "Supervision", 2, "A firm, managing broker or designated broker who fails to supervise brokers adequately:",
  "Is subject to discipline", ["Is liable only in contract", "Faces no sanction"],
  "RCW 18.85.361(22)."),
 ("wa/statutes", "Affiliation", 1, "When a Washington broker leaves a firm, their licence:",
  "Ceases to be in force", ["Transfers automatically to the new firm", "Stays active for 30 days"],
  "RCW 18.85.291."),
 ("wa/statutes", "Affiliation", 2, "A firm that terminates a broker for a violation of the licence law must:",
  "Immediately file a written statement of the facts with the director", ["Wait to be asked", "Notify the MLS only"],
  "RCW 18.85.291."),
 ("wa/statutes", "Affiliation", 3, "A designated broker who will not notify the director of a termination after demand:",
  "Exposes both the firm and themselves to disciplinary action", ["Faces no consequence", "Is fined by the MLS"],
  "RCW 18.85.291."),

 # licensing
 ("wa/licensing", "Education", 1, "Prelicence education for a Washington broker is:",
  "90 hours, including 3 hours of fair housing and consumer protection", ["60 hours", "120 hours", "30 hours"],
  "RCW 18.85.101(1)(c)."),
 ("wa/licensing", "Education", 2, "Each prelicence course must be completed within:",
  "Two years before applying for the broker's examination", ["Five years", "One year", "No limit"],
  "RCW 18.85.101(1)(c)."),
 ("wa/licensing", "Education", 1, "The FIRST renewal of a Washington broker's licence requires:",
  "A further 90 hours, including real estate law with 3 hours of fair housing, plus advanced practices", ["30 hours of continuing education only", "No additional education"],
  "RCW 18.85.101(2)."),
 ("wa/licensing", "Eligibility", 1, "The minimum age and education for a Washington broker's licence are:",
  "18 years old and a high school diploma or equivalent", ["21 years old and a diploma", "18 years old with no education requirement"],
  "RCW 18.85.101(1)(a), (b)."),
 ("wa/licensing", "Eligibility", 2, "A Washington broker may be licensed to:",
  "One firm at a time", ["Two firms", "Any number of firms"],
  "RCW 18.85.101(3)."),
 ("wa/licensing", "Managing broker", 2, "A managing broker applicant must have:",
  "Three years as a full-time broker within the previous five years", ["One year of licensure", "Five years with no time limit"],
  "RCW 18.85.111(1)(c)."),
 ("wa/licensing", "Managing broker", 3, "Each managing broker course must be:",
  "At least 30 clock hours with a comprehensive examination, completed within three years before applying", ["At least 15 hours", "Of any length"],
  "RCW 18.85.111(1)(d)."),
 ("wa/licensing", "Renewal", 1, "A Washington real estate licence expires:",
  "Two years from the issuance date", ["Annually", "Every four years", "On 31 December"],
  "RCW 18.85.191."),
 ("wa/licensing", "Renewal", 2, "A licence is cancelled if the renewal fee is not received within:",
  "One year of expiry", ["30 days", "Three years", "Six months"],
  "RCW 18.85.191."),
 ("wa/licensing", "Renewal", 3, "A firm licence issued to a corporation expires:",
  "When its registration or certificate of authority with the secretary of state expires", ["Two years after issue", "On the designated broker's renewal date"],
  "RCW 18.85.191."),
 ("wa/licensing", "Continuing education", 1, "Washington continuing education is:",
  "30 clock hours per renewal", ["18 hours", "12 hours", "45 hours"],
  "WAC 308-124A."),
 ("wa/licensing", "Continuing education", 1, "Of those hours, the prescribed curricula are:",
  "3 hours of core curriculum and 3 hours of Washington real estate fair housing", ["6 hours of ethics", "3 hours of agency only"],
  "WAC 308-124A."),
 ("wa/licensing", "Continuing education", 2, "Core curriculum must be completed within:",
  "24 months of the renewal date", ["36 months", "12 months", "The whole biennium"],
  "WAC 308-124A-800."),
 ("wa/licensing", "Continuing education", 2, "Placing a licence on inactive status to avoid continuing education is:",
  "Prohibited", ["A recognised option", "Allowed once per career"],
  "WAC 308-124A."),
 ("wa/licensing", "Continuing education", 2, "Failing to complete the prescribed core and fair housing hours results in:",
  "Denial of licence renewal", ["A fine", "A 30-day grace period"],
  "WAC 308-124A."),

 # agency
 ("wa/agency", "Default", 1, "A Washington broker performing brokerage services for a buyer is, by default:",
  "The buyer's agent", ["A subagent of the seller", "A limited dual agent", "Unrepresented"],
  "RCW 18.86.020(1)."),
 ("wa/agency", "Services agreement", 1, "The default term of a buyer's services agreement in Washington is:",
  "60 days, with the option of a longer term", ["30 days", "90 days", "Six months"],
  "RCW 18.86.020(2)(b)(i)."),
 ("wa/agency", "Services agreement", 2, "Consent to limited dual agency must be:",
  "Separately initialled by the principal in the services agreement", ["Given orally", "Implied by signing the listing"],
  "RCW 18.86.020(2)(b)(iv)."),
 ("wa/agency", "Services agreement", 2, "A services agreement is NOT required where a broker acts as a buyer's agent:",
  "Solely for commercial real estate", ["In any new construction sale", "For an all-cash buyer"],
  "RCW 18.86.020(3)."),
 ("wa/agency", "Services agreement", 3, "A buyer's services agreement must offer:",
  "Checkbox options for an exclusive or nonexclusive relationship", ["A choice of commission rates", "A list of approved lenders"],
  "RCW 18.86.020(2)(b)(iii)."),
 ("wa/agency", "Duties", 1, "Written offers must be presented:",
  "Timely, even where the property is already subject to a contract for sale", ["Only until mutual acceptance", "Only if above list price"],
  "RCW 18.86.030(1)(c)."),
 ("wa/agency", "Duties", 1, "The agency pamphlet must be given to a party the broker serves:",
  "Before that party signs a services agreement", ["At closing", "Within five days of the offer"],
  "RCW 18.86.030(1)(f)(i)."),
 ("wa/agency", "Duties", 2, "An unrepresented party must receive the agency pamphlet:",
  "Before signing an offer, or as soon as reasonably practical", ["Never", "Only on written request"],
  "RCW 18.86.030(1)(f)(ii)."),
 ("wa/agency", "Duties", 2, "The capacity disclosure must appear in a separate paragraph titled:",
  "Agency Disclosure", ["Material Facts", "Notice to Consumer", "Statement of Relationship"],
  "RCW 18.86.030(1)(g)(i)."),
 ("wa/agency", "Duties", 2, "Unless otherwise agreed, a Washington broker owes no duty to:",
  "Independently inspect the property or verify a party's statements", ["Disclose known material facts", "Account for money received"],
  "RCW 18.86.030(2)."),
 ("wa/agency", "Duties", 3, "The duty to disclose material facts:",
  "Does not imply a duty to investigate matters the broker has not agreed to investigate", ["Requires an independent inspection", "Extends to the parties' finances"],
  "RCW 18.86.030(1)(d)."),
 ("wa/agency", "Dual agency", 1, "A Washington limited dual agent may act only with:",
  "The written consent of both parties, set out in the services agreement", ["Oral consent of both", "The designated broker's approval"],
  "RCW 18.86.060(1)."),
 ("wa/agency", "Confidentiality", 1, "A Washington agent may disclose a client's confidential information:",
  "Only under subpoena or court order, even after the relationship ends", ["Once the transaction closes", "With the other broker's consent"],
  "RCW 18.86.050(1)(d)."),
 ("wa/agency", "Dual agency", 2, "Where two brokers of one firm represent opposite parties:",
  "The designated broker and any supervising managing broker are limited dual agents, and each appointed broker solely represents their own party", ["Both brokers become dual agents", "The arrangement is prohibited"],
  "RCW 18.86.060(5)."),
 ("wa/agency", "Loyalty", 2, "Showing the same property to other prospective buyers:",
  "Does not in itself breach the duty of loyalty", ["Breaches loyalty", "Requires the buyer's written consent"],
  "RCW 18.86.050(2)(a)."),
 ("wa/agency", "Compensation", 1, "Paying a Washington broker's compensation:",
  "Does not establish an agency relationship with the payer", ["Makes the payer the client", "Creates limited dual agency"],
  "RCW 18.86.080(2)."),
 ("wa/agency", "Compensation", 2, "A buyer's services agreement must state:",
  "Whether the broker will show properties if no party or firm offers to pay the firm", ["The buyer's maximum price", "The lender's name"],
  "RCW 18.86.080(7)(b)."),
 ("wa/agency", "Compensation", 2, "A Washington firm may be compensated:",
  "By more than one party in a transaction", ["Only by its own client", "Only by the seller"],
  "RCW 18.86.080(5)."),
 ("wa/agency", "Compensation", 3, "A referral between firms where the referring firm did no brokerage work:",
  "Needs no services agreement", ["Is prohibited", "Needs the client's written consent"],
  "RCW 18.86.080(9)."),
 ("wa/agency", "Compensation", 3, "Compensation calculated on the purchase price:",
  "Does not breach any duty to the buyer or seller", ["Is prohibited", "Requires separate written consent"],
  "RCW 18.86.080(6)."),

 # general
 ("wa/general", "Disclosure", 1, "The Washington seller disclosure statement is due:",
  "Not later than five business days after mutual acceptance, unless otherwise agreed", ["Before the offer is written", "At closing", "Within 10 days"],
  "RCW 64.06.030."),
 ("wa/general", "Disclosure", 1, "After receiving it, the buyer may rescind within:",
  "Three business days", ["72 hours", "Five business days", "Ten days"],
  "RCW 64.06.030."),
 ("wa/general", "Disclosure", 2, "If the buyer sends no written rescission notice in that window, the statement is:",
  "Deemed approved and accepted", ["Void", "Automatically re-sent"],
  "RCW 64.06.030."),
 ("wa/general", "Disclosure", 2, "A seller who corrects an adverse change at least three business days before closing:",
  "Need not amend, and the buyer gets no right of rescission", ["Must still amend and wait", "Must extend closing"],
  "RCW 64.06.040(1)."),
 ("wa/general", "Disclosure", 3, "If closing falls inside the three-business-day rescission period:",
  "The closing date is extended until the period expires", ["The buyer loses the right", "The agreement is void"],
  "RCW 64.06.040(1)."),
 ("wa/general", "Fair housing", 1, "Which is protected in Washington real estate but not by the federal Fair Housing Act?",
  "Citizenship or immigration status", ["Race", "Color", "National origin"],
  "RCW 49.60.222(1)."),
 ("wa/general", "Fair housing", 1, "Washington also protects:",
  "Honorably discharged veteran or military status", ["Credit score", "Occupation", "Length of residence"],
  "RCW 49.60.222(1)."),
 ("wa/general", "Fair housing", 2, "The use of a trained dog guide or service animal by a person with a disability is:",
  "A protected basis in its own right", ["Covered only by the ADA", "Not protected in housing"],
  "RCW 49.60.222(1)."),
 ("wa/general", "Excise tax", 1, "The Washington real estate excise tax is the obligation of:",
  "The seller", ["The buyer", "The lender", "The closing agent"],
  "RCW 82.45.080(1)."),
 ("wa/general", "Excise tax", 2, "Since 2020 the state real estate excise tax is:",
  "Graduated on portions of the selling price, from 1.1% up to 3%", ["A flat 1.28%", "A flat 1.78%", "A flat 1.1%"],
  "RCW 82.45.060(1)(b)."),
 ("wa/general", "Excise tax", 2, "Timberland and agricultural land are taxed at:",
  "A flat 1.28% of the selling price", ["The graduated rates", "A flat 1.1%"],
  "RCW 82.45.060(1)(c)."),
 ("wa/general", "Excise tax", 3, "The excise tax bracket thresholds are adjusted:",
  "Every fourth year, by the lesser of the growth in the CPI for shelter or 5%", ["Annually with inflation", "Never"],
  "RCW 82.45.060(2)."),
 ("wa/general", "Discipline", 2, "Refusing to produce records for the director on demand is:",
  "A ground for discipline", ["Permitted without a subpoena", "A civil matter only"],
  "RCW 18.85.361(6)."),
 ("wa/general", "Discipline", 3, "Discipline can follow conduct in a transaction:",
  "Whether or not it was for the licensee's own account", ["Only in client transactions", "Only when a client complains"],
  "RCW 18.85.361."),
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
            "id": "wa-" + hashlib.sha1(q.encode()).hexdigest()[:8],
            "portion": "georgia", "topic": topic, "subtopic": sub,
            "sub": topic + "|" + sub, "concept": "Washington " + sub.lower(),
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
        "code": "WA", "name": "Washington", "abbr": "WA",
        "regulator": "Washington Department of Licensing",
        "pass": EXAM["pass"],
        "pass_published": EXAM["pass_published"],
        "pass_note": EXAM["pass_note"],
        "portions": {
            "national": {"scored": EXAM["national_scored"],
                         "minutes": EXAM["national_minutes"]},
            "georgia": {"name": "Washington law", "scored": EXAM["state_scored"],
                        "minutes": EXAM["state_minutes"],
                        "blurb": "RCW 18.85 and 18.86, the seller disclosure statement, fair housing and the excise tax."},
        },
        "topics": topics, "bank": bank, "study": study,
        "sources": SOURCES, "diffs": DIFFS,
    }


# Where Washington departs from the national rule.
DIFFS = {
    "national/agency": [
        "Since 2023 c 318 a broker working with a BUYER is the BUYER'S AGENT by default, and every principal needs a written SERVICES AGREEMENT - with a DEFAULT 60-DAY TERM for a buyer (RCW 18.86.020).",
        "The RCW 18.86.030 duties MAY NOT BE WAIVED, including presenting written offers even where the property is already under contract, and giving the AGENCY PAMPHLET with an acknowledgment of receipt.",
        "Confidentiality is broken only by SUBPOENA OR COURT ORDER, and it survives termination of the relationship (RCW 18.86.040, .050, .060).",
        "Where two brokers of one firm take opposite sides, the DESIGNATED BROKER and supervising managing broker become LIMITED DUAL AGENTS while each appointed broker solely represents their own party (RCW 18.86.060(5)).",
        "Paying compensation does NOT create an agency relationship, and a firm may be paid by more than one party (RCW 18.86.080).",
    ],
    "national/practice": [
        "Client funds go into the firm's trust account the NEXT BANKING DAY, into a POOLED INTEREST-BEARING account whose interest goes to the STATE HOUSING TRUST FUND and the real estate education account (RCW 18.85.285).",
        "Records are kept THREE YEARS, and failing to return trust property within 30 days of demand is PRIMA FACIE CONVERSION (RCW 18.85.361).",
        "Education: 90 hours before the examination, another 90 at the FIRST renewal, then 30 clock hours each renewal including 3 core and 3 Washington fair housing hours.",
        "A licence runs TWO YEARS and is CANCELLED if unrenewed for a year (RCW 18.85.191).",
    ],
    "national/disclosures": [
        "The seller's disclosure statement is due within FIVE BUSINESS DAYS of mutual acceptance and the buyer may rescind within THREE BUSINESS DAYS, in their sole discretion (RCW 64.06.030).",
        "A late amendment restarts a three-business-day rescission right, and closing is EXTENDED if it falls inside that window (RCW 64.06.040).",
        "RCW 49.60.222 adds CITIZENSHIP OR IMMIGRATION STATUS, honorably discharged veteran or military status, and use of a trained dog guide or service animal to the federal classes.",
        "The real estate excise tax is GRADUATED from 1.1% to 3% and is the SELLER'S obligation (RCW 82.45.060, .080).",
    ],
}


if __name__ == "__main__":
    import io, json, os
    here = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    out = os.path.join(here, "greprep", "packs", "WA.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    pack = build()
    with io.open(out, "w", encoding="utf-8") as f:
        json.dump(pack, f, ensure_ascii=False, indent=1, sort_keys=True)
    print("wrote", out, len(pack["bank"]), "questions,", len(pack["study"]), "lessons")
