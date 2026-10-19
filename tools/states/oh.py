"""Ohio state content: lessons and practice questions.

Ohio splits the examination: 80 scored national items and 40 scored state
items, each section needing 70% for a salesperson. The four state-section
categories and their item counts below are PSI's published outline for the
Division of Real Estate & Professional Licensing.

Every rule below was read from the official text on 2026-10-18:
  - Ohio Revised Code chapter 4735 (Real Estate Brokers), from
    codes.ohio.gov, current text including House Bill 96 of the 136th
    General Assembly (effective 30 September 2025) and Senate Bill 155
    (effective 2 March 2026).
  - The PSI Ohio Real Estate Salesperson and Broker Candidate Information
    Bulletin, for the blueprint, the pass mark and the timings.
The section a fact comes from is cited next to it. Do not add a fact here
without reading its source first.

A warning for anyone extending this: Ohio's prelicensing hours were cut in
the current statute. Section 4735.09(F)(6) now requires 40 + 40 + 10 + 10 =
100 hours, not the 120 that commercial guides still teach. Read the live
section before writing a number.
"""

EXAM = {
    # PSI bulletin: Salesperson National 80 items / 70% / 120 minutes;
    # State 40 items / 70% / 60 minutes. (Broker needs 75%.)
    "state_scored": 40,
    "state_minutes": 60,
    "national_scored": 80,
    "national_minutes": 120,
    "pass": 0.70,
}

# PSI's published state-specific outline, category by category.
TOPICS = [
    ("oh/license-law", "License law & Commission rules", 16,
     "Advertising, commissions, records, trust accounts, listings, fair housing."),
    ("oh/agency", "Brokerage relationships", 14,
     "Agency agreements, the disclosure statement, dual agency, confidentiality."),
    ("oh/licensing", "Licensing requirements", 6,
     "Who needs a licence, the education, renewal and status changes."),
    ("oh/governance", "State governance", 4,
     "The Commission, the Division, discipline and the Recovery Fund."),
]

SOURCES = [
    {"by": "Ohio General Assembly",
     "name": "Ohio Revised Code chapter 4735 (Real Estate Brokers)",
     "note": "The licence law itself, current text. Every licensing, agency, trust account and discipline rule here was read from it.",
     "url": "https://codes.ohio.gov/ohio-revised-code/chapter-4735"},
    {"by": "Ohio Real Estate Commission",
     "name": "Ohio Administrative Code 1301:5",
     "note": "The Commission's rules, adopted under ORC 4735.10.",
     "url": "https://codes.ohio.gov/oac/1301:5"},
    {"by": "PSI Services and the Ohio Division of Real Estate",
     "name": "Ohio Real Estate Candidate Information Bulletin",
     "note": "The blueprint: 80 national and 40 state items, 70% for a salesperson, and the four state categories with their counts.",
     "url": "https://test-takers.psiexams.com/ohre"},
]


# --------------------------------------------------------------- lessons

STUDY = {}

STUDY["oh/license-law"] = {
    "summary": "Sixteen of the forty state items, the biggest block. Most of it is what a broker must keep separate, keep on file, and keep out of an advertisement - plus Ohio's fair housing list, which is longer than the federal one.",
    "sections": [
        {"h": "Trust and special accounts",
         "l": ["A broker must maintain at all times a SPECIAL OR TRUST bank account at a state or federally chartered institution LOCATED IN OHIO.",
               "That account must be NONINTEREST-BEARING, and separate and distinct from any personal or other account of the broker.",
               "It holds all escrow funds, security deposits and other money received by the broker in a FIDUCIARY CAPACITY.",
               "The name, account number and location of the depository must be submitted IN WRITING to the superintendent.",
               "A broker managing property for others keeps a SEPARATE property management account, used exclusively for rents, security deposits and escrow funds from that work. That account MAY earn interest, which is paid to the property owners PRO RATA.",
               "Failing to maintain either account is a ground for discipline (ORC 4735.18(A)(26) and (27))."],
         "check": [("A broker's sales trust account in Ohio must be:", "Noninterest-bearing and separate from the broker's own accounts", ["Interest-bearing for the broker's benefit", "Held at any bank in the country"], "ORC 4735.18(A)(26)."),
                   ("Interest earned on a property management trust account is paid to:", "The property owners, pro rata", ["The broker", "The Division", "The tenants"], "ORC 4735.10(A)(2)(e)(ii)."),
                   ("Details of the trust account depository must be:", "Submitted in writing to the superintendent", ["Posted in the office", "Filed with the county"], "ORC 4735.18(A)(26).")]},
        {"h": "Earnest money (ORC 4735.24)",
         "p": ["Once earnest money from a purchase agreement is in the broker's trust account, the broker holds it IN ACCORDANCE WITH THE TERMS OF THE PURCHASE AGREEMENT until one of these happens:"],
         "l": ["The transaction CLOSES and the broker disburses to the closing or escrow agent, or as the agreement directs.",
               "BOTH PARTIES give the broker separate WRITTEN instructions they have both signed, specifying disbursement, and the broker follows them.",
               "The broker receives a copy of a FINAL COURT ORDER saying who gets it, and follows it.",
               "The transaction is cancelled by the record owner of residential property under ORC 5301.95(C)(1).",
               "It becomes UNCLAIMED FUNDS, and after the required notice the broker reports and remits it to the director of commerce."],
         "check": [("A broker may release disputed earnest money on:", "Written instructions signed by both parties", ["The buyer's demand alone", "The listing agent's say-so"], "ORC 4735.24(A)(2)."),
                   ("Absent agreement, a broker may also disburse on:", "A final court order", ["A verbal agreement", "The seller's written demand alone"], "ORC 4735.24(A)(3).")]},
        {"h": "Records, copies and commissions",
         "l": ["A broker must keep the records of their transactions, and failing to produce them is a ground for discipline (ORC 4735.18(A)(24)).",
               "A licensee must furnish ALL PARTIES true copies of all listings and other agreements to which they are a party, AT THE TIME EACH PARTY SIGNS them (ORC 4735.18(A)(25)).",
               "A salesperson's compensation for brokerage comes through the broker with whom they are associated, not directly from a party.",
               "Records relating to an out-of-state commercial broker's Ohio transaction are kept by the Ohio broker for THREE YEARS."],
         "check": [("Copies of a listing agreement must be given to the parties:", "At the time each party signs", ["Within three days", "At closing"], "ORC 4735.18(A)(25)."),
                   ("A salesperson is paid for brokerage by:", "The associated broker", ["The seller directly", "The title agency"], "The salesperson acts for the broker.")]},
        {"h": "Ohio fair housing",
         "p": ["Ohio's fair housing law, ORC 4112.02(H), makes it illegal to refuse to sell, transfer, assign, rent, lease, sublease or finance housing, to refuse to negotiate, or otherwise to deny or make housing unavailable because of:"],
         "l": ["RACE", "COLOR", "RELIGION", "SEX", "FAMILIAL STATUS", "ANCESTRY",
               "MILITARY STATUS", "DISABILITY", "NATIONAL ORIGIN"],
         "check": [("Which is protected under Ohio's fair housing law but not the federal Fair Housing Act?", "Military status", ["Race", "Religion", "National origin"], "Ohio adds ancestry and military status."),
                   ("Every written agency agreement must contain:", "A fair housing statement, a blockbusting definition and the HUD equal housing logotype", ["The commission rate", "The broker's licence number only"], "ORC 4735.55(C).")]},
    ],
    "traps": [
        "The SALES trust account is noninterest-bearing. The PROPERTY MANAGEMENT account may earn interest, paid to owners.",
        "Copies go to the parties AT SIGNING, not later.",
        "Ohio fair housing adds ANCESTRY and MILITARY STATUS to the federal list.",
        "Disputed earnest money needs both parties' signed written instructions, or a court order.",
    ],
    "vocab": [
        ["Special or trust account", "The noninterest-bearing account holding others' money."],
        ["Fiduciary capacity", "Holding money or property for another's benefit."],
        ["Blockbusting", "Inducing sales by suggesting a protected group is moving in."],
        ["Superintendent", "The head of the Division of Real Estate & Professional Licensing."],
        ["Unclaimed funds", "Money reported and remitted to the director of commerce."],
    ],
    "examples": [
        {"t": "The stand-off",
         "s": "A deal collapses and buyer and seller each demand the $5,000 earnest money.",
         "w": ["The broker may not simply pick a side.",
               "Release needs written instructions signed by BOTH, or a final court order."],
         "k": "Hold the money until both sign, or a court decides."},
    ],
}

STUDY["oh/agency"] = {
    "summary": "Fourteen items. Ohio puts agency in writing early: a written agreement before you show a house for a seller or write an offer for a buyer, and an agency disclosure statement signed before the offer goes in.",
    "sections": [
        {"h": "A written agency agreement comes first (ORC 4735.55)",
         "p": ["A licensee must enter into a WRITTEN agency agreement BEFORE doing any of these:"],
         "l": ["ADVERTISING OR SHOWING residential real property on behalf of a SELLER;",
               "Making an OFFER TO PURCHASE residential real property on behalf of a PURCHASER;",
               "Making an offer to LEASE residential premises on behalf of a TENANT for a term EXCEEDING EIGHTEEN MONTHS."],
         "check": [("Before showing a house for a seller, an Ohio licensee must have:", "A written agency agreement", ["An oral understanding", "A signed disclosure statement only"], "ORC 4735.55(B)(1)."),
                   ("A written agency agreement is needed for a tenant's lease of:", "More than eighteen months", ["Any length", "More than one year", "More than three years"], "ORC 4735.55(B)(3)."),
                   ("Before writing an offer for a buyer, the licensee must have:", "A written agency agreement", ["Only the buyer's verbal consent", "The seller's permission"], "ORC 4735.55(B)(2).")]},
        {"h": "What the agreement must contain",
         "l": ["An EXPIRATION DATE.",
               "A statement that refusing housing on the protected grounds is illegal under Ohio and federal fair housing law.",
               "A statement DEFINING BLOCKBUSTING and saying it is illegal.",
               "A copy of the HUD EQUAL HOUSING OPPORTUNITY LOGOTYPE."],
         "check": [("Every Ohio written agency agreement must state:", "An expiration date", ["A minimum commission", "A guaranteed sale price"], "ORC 4735.55(C)(1)."),
                   ("The agreement must include a definition of:", "Blockbusting", ["Steering", "Puffing"], "ORC 4735.55(C)(3).")]},
        {"h": "The agency disclosure statement (ORC 4735.58)",
         "l": ["A PURCHASER'S agent, or a seller's subagent working with a purchaser, presents the statement to the PURCHASER and asks them to sign and date it NO LATER THAN THE PREPARATION OF AN OFFER to purchase or lease.",
               "That signed statement is then delivered to the seller's agent, or to the seller if unrepresented.",
               "BEFORE presenting the seller with a written offer, the seller's agent - or the purchaser's agent if the seller has none - presents the statement to the SELLER to sign and date.",
               "The licensee must indicate the ACCURATE agency relationship on the statement.",
               "AT AUCTION: the licensee must VERBALLY disclose to the audience, before the auction, that they represent the seller, and give the statement to the successful bidder before they sign a purchase contract.",
               "Evidence of failing to comply is PRIMA-FACIE EVIDENCE OF MISCONDUCT under ORC 4735.18(A)(6)."],
         "check": [("The purchaser signs the agency disclosure statement:", "No later than the preparation of an offer", ["At closing", "Within three days of the first showing"], "ORC 4735.58(A)(1)."),
                   ("At an auction, the licensee must disclose representation of the seller:", "Verbally to the audience before the auction", ["Only to the winning bidder", "In the sale catalogue only"], "ORC 4735.58(B)."),
                   ("Failing to comply with the disclosure section is:", "Prima-facie evidence of misconduct", ["A minor paperwork issue", "A criminal offence"], "ORC 4735.58(C).")]},
        {"h": "Dual agency (ORC 4735.70, 4735.71)",
         "l": ["A DUAL AGENT is: a licensee representing both purchaser and seller as clients in the same transaction; a BROKERAGE representing both; or a MANAGEMENT LEVEL licensee representing a client in an in-company transaction.",
               "A management level licensee is NOT a dual agent where another management level licensee is affiliated AND either that licensee personally represents one side only, or is themselves the buyer or seller representing only their own interest.",
               "Dual agency is permitted ONLY where BOTH seller and purchaser have FULL KNOWLEDGE of the dual representation and CONSENT IN WRITING on the agency disclosure statement.",
               "Before taking consent, the licensee must disclose to both parties all relevant information needed for an informed decision."],
         "check": [("Dual agency in Ohio requires:", "Full knowledge and written consent from both parties on the disclosure statement", ["Verbal consent", "Only the broker's approval"], "ORC 4735.71(A)."),
                   ("A brokerage representing both buyer and seller is:", "A dual agent", ["Two separate agencies", "Not an agency at all"], "ORC 4735.70(B).")]},
        {"h": "Fiduciary duties (ORC 4735.62)",
         "p": ["Representing a client, a licensee is a FIDUCIARY and must use best efforts to further the client's interest, including:"],
         "l": ["Exercising reasonable skill and care;",
               "Performing the terms of any written agency agreement;",
               "Following the client's lawful instructions;",
               "Acting LOYALLY to the client's interest;",
               "Complying with Ohio and federal fair housing law;",
               "Disclosing MATERIAL FACTS of the transaction the licensee knows or should know, that are not confidential under a current or prior agency;",
               "Advising the client to get EXPERT ADVICE on material matters where appropriate;",
               "Accounting in a timely manner for money and property;",
               "Keeping CONFIDENTIAL INFORMATION confidential, unless disclosure is permitted."],
         "check": [("A licensee must disclose to the client:", "Material facts they know or should know, that are not confidential", ["Only what the client asks about", "Nothing beyond the listing data"], "ORC 4735.62(F)."),
                   ("Where a material matter needs expertise the licensee lacks, the duty is to:", "Advise the client to obtain expert advice", ["Give an opinion anyway", "Say nothing"], "ORC 4735.62(G).")]},
    ],
    "traps": [
        "Written agreement BEFORE showing for a seller or offering for a buyer - not after.",
        "Eighteen months is the lease threshold, not twelve.",
        "The purchaser signs the disclosure statement by the time the OFFER is prepared.",
        "Dual agency needs written consent ON THE AGENCY DISCLOSURE STATEMENT.",
        "Confidential information survives the end of the agency.",
    ],
    "vocab": [
        ["Agency disclosure statement", "The ORC 4735.57 form naming the relationships."],
        ["Dual agent", "A licensee, brokerage or management level licensee on both sides."],
        ["Management level licensee", "A licensee with supervisory authority in the brokerage."],
        ["In-company transaction", "Both sides represented within one brokerage."],
        ["Subagent", "An agent working for the seller through the listing broker."],
    ],
    "examples": [
        {"t": "The offer that came too soon",
         "s": "A licensee shows a buyer six houses on a handshake, then writes an offer.",
         "w": ["ORC 4735.55(B)(2) requires a written agency agreement before making an offer for a purchaser.",
               "The agency disclosure statement must also be signed by then."],
         "k": "Both the written agreement and the signed disclosure must be in place before that offer."},
    ],
}

STUDY["oh/licensing"] = {
    "summary": "Six items. The hours changed recently: Ohio's prelicensing requirement is now 40 + 40 + 10 + 10, then 20 hours of post-licensure inside a year, then 30 hours every three years.",
    "sections": [
        {"h": "Qualifying",
         "l": ["Be at least EIGHTEEN.",
               "If born after 1950, hold a HIGH SCHOOL DIPLOMA or a certificate of high school equivalence.",
               "Be HONEST AND TRUTHFUL, with no disqualifying offence and no unresolved civil rights adjudication.",
               "Be recommended by the broker with whom the applicant is or will be associated, certifying honesty and truthfulness.",
               "Pass the examination. There is NO LIMIT on the number of retakes (ORC 4735.09(C))."],
         "check": [("The minimum age for an Ohio salesperson licence is:", "18", ["17", "19", "21"], "ORC 4735.09."),
                   ("An Ohio application must be accompanied by:", "The recommendation of the broker the applicant will associate with", ["Two character references", "A credit report"], "ORC 4735.09(A)."),
                   ("How many times may an Ohio applicant retake the examination?", "There is no limit", ["Three times", "Five times"], "ORC 4735.09(C).")]},
        {"h": "The education, as the statute now reads",
         "l": ["40 HOURS of instruction in REAL ESTATE PRACTICE;",
               "40 HOURS covering OHIO REAL ESTATE LAW together with municipal, state and federal CIVIL RIGHTS law, new case law on housing discrimination, desegregation issues and methods of eliminating the effects of prior discrimination;",
               "10 HOURS in REAL ESTATE APPRAISAL;",
               "10 HOURS in REAL ESTATE FINANCE.",
               "That is 100 hours in all, at an institution of higher education, by classroom or distance learning (ORC 4735.09(F)(6)).",
               "The Ohio real estate law instruction should, if feasible, be taught by a law school faculty member, and the civil rights instruction by a knowledgeable Ohio Civil Rights Commission staff member.",
               "The appraisal course does not apply to an applicant already holding an Ohio appraiser licence or certificate."],
         "check": [("Instruction in real estate practice required of an Ohio salesperson applicant is:", "40 hours", ["30 hours", "20 hours", "10 hours"], "ORC 4735.09(F)(6)(a)."),
                   ("Instruction in real estate finance required is:", "10 hours", ["20 hours", "30 hours", "40 hours"], "ORC 4735.09(F)(6)(d)."),
                   ("The 40-hour law course must also cover:", "Municipal, state and federal civil rights law", ["Appraisal theory", "Property management"], "ORC 4735.09(F)(6)(b).")]},
        {"h": "After licensure",
         "l": ["POST-LICENSURE: 20 HOURS of instruction, completed NOT LATER THAN TWELVE MONTHS after the date the salesperson licence is issued, in schools and institutions approved by the Commission (ORC 4735.09(J)).",
               "It covers current practice in commercial real estate, property management, short sales and land contracts; contract law; federal and state programmes; economic conditions; and fiduciary responsibility.",
               "CONTINUING EDUCATION: 30 HOURS, on or before the licensee's birthday THREE YEARS after initial licensure, and every three years after that (ORC 4735.141).",
               "A broker, broker on deposit or management level licensee must include a THREE-HOUR course on the duties of a principal broker and operating a brokerage.",
               "Ohio runs a THREE-YEAR licence and renewal system (ORC 4735.10(A)(2)(b)).",
               "A licence stays valid until placed inactive or resigned, revoked, suspended, or expired by law (ORC 4735.14(A))."],
         "check": [("Post-licensure education in Ohio is:", "20 hours within twelve months of licence issue", ["30 hours within three years", "10 hours within six months"], "ORC 4735.09(J)."),
                   ("Continuing education in Ohio is:", "30 hours every three years", ["30 hours every year", "14 hours every two years"], "ORC 4735.141(A)."),
                   ("A broker's continuing education must include:", "A three-hour course on the duties of a principal broker", ["A six-hour appraisal course", "A one-hour maths course"], "ORC 4735.141(A).")]},
    ],
    "traps": [
        "40 + 40 + 10 + 10 = 100 hours. Older guides say 120 - the appraisal and finance courses were cut to 10 each.",
        "20 hours of post-licensure within TWELVE MONTHS, then 30 hours every THREE YEARS.",
        "The CE clock runs to the licensee's BIRTHDAY three years after initial licensure.",
        "No limit on exam retakes.",
    ],
    "vocab": [
        ["Post-licensure education", "The 20 hours due within a year of licensure."],
        ["Broker on deposit", "A broker whose licence is held on deposit with the Division."],
        ["Management level licensee", "A licensee with supervisory authority in a brokerage."],
        ["Resigned status", "A licence voluntarily given up under ORC 4735.142."],
    ],
    "examples": [],
}

STUDY["oh/governance"] = {
    "summary": "Four items. Five people on the Commission, a Division that does the work, and a fund that pays a wronged consumer up to forty thousand dollars for any one licensee.",
    "sections": [
        {"h": "The Ohio Real Estate Commission (ORC 4735.03)",
         "l": ["FIVE members, appointed by the GOVERNOR with the advice and consent of the SENATE.",
               "FOUR must have been engaged in the real estate business as LICENSED REAL ESTATE BROKERS in Ohio for TEN YEARS immediately preceding appointment.",
               "ONE represents the PUBLIC.",
               "Terms are FIVE YEARS, running 1 July to 30 June.",
               "No more than THREE members may belong to any one political party.",
               "No member may concurrently sit on the real estate appraiser board."],
         "check": [("The Ohio Real Estate Commission has:", "Five members", ["Seven members", "Nine members", "Three members"], "ORC 4735.03."),
                   ("Four Commission members must have been licensed Ohio brokers for:", "Ten years immediately preceding appointment", ["Five years", "Two years"], "ORC 4735.03."),
                   ("Commission terms run for:", "Five years", ["Three years", "Four years"], "ORC 4735.03.")]},
        {"h": "The Division and the superintendent",
         "l": ["The DIVISION OF REAL ESTATE & PROFESSIONAL LICENSING, inside the Ohio Department of Commerce, administers the licence law.",
               "The SUPERINTENDENT OF REAL ESTATE issues licences, investigates complaints and may enter agreements with a national testing service to deliver the examinations.",
               "The Commission adopts the rules in Ohio Administrative Code 1301:5 under ORC 4735.10."],
         "check": [("Ohio's examinations are delivered by:", "A national testing service under agreement with the superintendent", ["The Commission's own staff", "Each real estate school"], "ORC 4735.07(A), 4735.09(D).")]},
        {"h": "The Real Estate Recovery Fund (ORC 4735.12)",
         "l": ["A person who obtains a FINAL JUDGMENT against a licensee, on grounds of conduct violating chapter 4735 or its rules and tied to an act only a licensee may perform, may apply to the COURT OF COMMON PLEAS OF FRANKLIN COUNTY for payment from the fund.",
               "The fund pays the ACTUAL AND DIRECT LOSS that remains unpaid.",
               "PUNITIVE DAMAGES, ATTORNEY'S FEES and INTEREST are NOT recoverable. COURT COSTS may be, at the superintendent's discretion.",
               "The liability of the fund may not exceed $40,000 FOR ANY ONE LICENSEE. Where valid claims exceed that, the $40,000 is distributed in proportion to the claims.",
               "A special assessment of up to $10 a year may be charged at renewal if the fund holds less than $250,000 on the preceding 1 July."],
         "check": [("The Ohio Real Estate Recovery Fund pays at most, for any one licensee:", "$40,000", ["$20,000", "$50,000", "$100,000"], "ORC 4735.12(D)."),
                   ("Which is NOT recoverable from the fund?", "Punitive damages and attorney's fees", ["Actual loss", "Direct loss"], "ORC 4735.12(B)(2)."),
                   ("An application for payment is filed in:", "The court of common pleas of Franklin county", ["Any county court", "The Ohio Supreme Court"], "ORC 4735.12(B)(1)."),
                   ("Where claims exceed the cap for one licensee, the money is:", "Distributed in proportion to the claims", ["Paid first come, first served", "Returned to the state"], "ORC 4735.12(D).")]},
    ],
    "traps": [
        "FIVE Commission members: four brokers of ten years, one public member.",
        "$40,000 per LICENSEE - not per transaction.",
        "No punitive damages, attorney's fees or interest from the fund; court costs only at discretion.",
        "Claims go to Franklin county, wherever the deal happened.",
    ],
    "vocab": [
        ["Superintendent of Real Estate", "The head of the Division administering chapter 4735."],
        ["Recovery Fund", "The state fund paying unsatisfied judgments against licensees."],
        ["Court of common pleas", "The Ohio trial court; Franklin county hears fund claims."],
        ["Special assessment", "The renewal surcharge that tops the fund up."],
    ],
    "examples": [
        {"t": "Three victims, one agent",
         "s": "Three clients hold judgments totalling $70,000 against the same licensee.",
         "w": ["The fund's liability is capped at $40,000 for any one licensee.",
               "Valid claims above that are paid pro rata."],
         "k": "$40,000 is shared in proportion to their claims."},
    ],
}


# ------------------------------------------------------------- questions

Q = [
 # license law and rules
 ("oh/license-law", "Trust accounts", 1, "An Ohio broker's sales trust account must be:",
  "Noninterest-bearing and separate from the broker's own accounts", ["Interest-bearing for the broker", "Combined with the operating account", "Held at any bank in the country"],
  "ORC 4735.18(A)(26)."),
 ("oh/license-law", "Trust accounts", 2, "The trust account must be held at an institution:",
  "Located in Ohio and state or federally chartered", ["Anywhere in the United States", "Outside Ohio for safety", "Chosen by the buyer"],
  "ORC 4735.18(A)(26)."),
 ("oh/license-law", "Trust accounts", 2, "Interest earned on a property management trust account is paid to:",
  "The property owners, pro rata", ["The broker", "The Division of Real Estate", "The tenants"],
  "ORC 4735.10(A)(2)(e)(ii)."),
 ("oh/license-law", "Trust accounts", 2, "A broker who manages property for others must keep:",
  "A separate property management account, distinct from the sales trust account", ["One account for everything", "No account if the owner consents", "The owner's personal account"],
  "ORC 4735.18(A)(27)."),
 ("oh/license-law", "Trust accounts", 2, "Details of the trust account depository must be:",
  "Submitted in writing to the superintendent", ["Posted in the office window", "Filed with the county recorder", "Kept private"],
  "ORC 4735.18(A)(26)."),
 ("oh/license-law", "Earnest money", 1, "A broker holding disputed earnest money may disburse it on:",
  "Written instructions signed by both parties", ["The buyer's written demand alone", "The seller's verbal demand", "The listing agent's decision"],
  "ORC 4735.24(A)(2)."),
 ("oh/license-law", "Earnest money", 2, "Absent agreement between the parties, a broker may also disburse earnest money on:",
  "A final court order specifying who receives it", ["The broker's own judgment", "A mediator's recommendation", "The lender's instruction"],
  "ORC 4735.24(A)(3)."),
 ("oh/license-law", "Earnest money", 3, "Earnest money that is never claimed must eventually be:",
  "Reported and remitted to the director of commerce as unclaimed funds", ["Kept by the broker", "Paid to the seller", "Donated to the Recovery Fund"],
  "ORC 4735.24(A)(5)."),
 ("oh/license-law", "Records", 1, "True copies of a listing agreement must be given to the parties:",
  "At the time each party signs", ["Within three business days", "At closing", "Only on request"],
  "ORC 4735.18(A)(25)."),
 ("oh/license-law", "Records", 2, "Failing to produce transaction records for the Division is:",
  "A ground for disciplinary action", ["Permitted if the file is closed", "A criminal offence only", "Allowed after one year"],
  "ORC 4735.18(A)(24)."),
 ("oh/license-law", "Records", 3, "An Ohio broker holding documents for an out-of-state commercial broker must retain them for:",
  "Three years", ["One year", "Five years", "Seven years"],
  "ORC 4735.022."),
 ("oh/license-law", "Commissions", 1, "An Ohio salesperson is paid for brokerage by:",
  "The broker with whom they are associated", ["The seller directly", "The title agency", "The buyer"],
  "The salesperson acts for and through the broker."),
 ("oh/license-law", "Fair housing", 1, "Which is protected under Ohio fair housing law but not the federal Fair Housing Act?",
  "Military status", ["Race", "Religion", "National origin"],
  "Ohio adds ancestry and military status (ORC 4112.02(H))."),
 ("oh/license-law", "Fair housing", 2, "Ohio's protected classes include:",
  "Ancestry", ["Occupation", "Income level", "Education"],
  "ORC 4112.02(H), as recited in ORC 4735.55(C)(2)."),
 ("oh/license-law", "Fair housing", 2, "Every written agency agreement must include:",
  "A fair housing statement, a blockbusting definition and the HUD equal housing logotype", ["The commission rate", "The broker's licence number only", "A mediation clause"],
  "ORC 4735.55(C)."),
 ("oh/license-law", "Fair housing", 2, "Blockbusting means:",
  "Inducing sales by suggesting people of a protected class are moving in", ["Refusing to show homes in an area", "Charging different commissions", "Advertising without a licence"],
  "The agency agreement must define it and say it is illegal."),

 # agency
 ("oh/agency", "Written agreements", 1, "Before showing residential property on behalf of a seller, an Ohio licensee must have:",
  "A written agency agreement", ["An oral understanding", "A signed disclosure statement only", "Nothing in particular"],
  "ORC 4735.55(B)(1)."),
 ("oh/agency", "Written agreements", 1, "Before making an offer to purchase for a buyer, the licensee must have:",
  "A written agency agreement", ["The buyer's verbal consent", "The seller's permission", "A signed offer only"],
  "ORC 4735.55(B)(2)."),
 ("oh/agency", "Written agreements", 2, "A written agency agreement is required for a tenant's lease exceeding:",
  "Eighteen months", ["Six months", "Twelve months", "Three years"],
  "ORC 4735.55(B)(3)."),
 ("oh/agency", "Written agreements", 2, "Every Ohio written agency agreement must contain:",
  "An expiration date", ["An automatic renewal", "A minimum commission", "A dispute clause"],
  "ORC 4735.55(C)(1)."),
 ("oh/agency", "Disclosure statement", 1, "The purchaser must sign the agency disclosure statement:",
  "No later than the preparation of an offer to purchase or lease", ["At closing", "Within three days of the first showing", "Only if asked"],
  "ORC 4735.58(A)(1)."),
 ("oh/agency", "Disclosure statement", 2, "The seller must be presented with the agency disclosure statement:",
  "Before being presented with a written offer", ["After accepting the offer", "At closing", "When the listing expires"],
  "ORC 4735.58(A)(1)."),
 ("oh/agency", "Disclosure statement", 2, "A purchaser's agent must deliver the purchaser's signed statement to:",
  "The seller's agent, or the seller if unrepresented", ["The Division of Real Estate", "The lender", "The county recorder"],
  "ORC 4735.58(A)(1)."),
 ("oh/agency", "Disclosure statement", 2, "At an auction, the licensee must disclose representing the seller:",
  "Verbally to the audience before the auction", ["Only to the winning bidder", "In the catalogue alone", "After the hammer falls"],
  "ORC 4735.58(B)."),
 ("oh/agency", "Disclosure statement", 3, "Evidence that a licensee failed to comply with the disclosure section is:",
  "Prima-facie evidence of misconduct", ["A minor paperwork matter", "A criminal offence", "Grounds for a civil suit only"],
  "ORC 4735.58(C)."),
 ("oh/agency", "Dual agency", 1, "Dual agency in Ohio is permitted only where:",
  "Both parties have full knowledge and consent in writing on the disclosure statement", ["The broker approves", "One party consents", "It is a commercial deal"],
  "ORC 4735.71(A)."),
 ("oh/agency", "Dual agency", 2, "Which is a dual agent under Ohio law?",
  "A brokerage representing both purchaser and seller as clients", ["A subagent of the seller", "A buyer's agent from another firm", "An appraiser"],
  "ORC 4735.70(B)."),
 ("oh/agency", "Dual agency", 3, "A management level licensee representing a client in an in-company transaction is:",
  "A dual agent, unless the statutory exception applies", ["Never a dual agent", "A subagent", "Outside the agency rules"],
  "ORC 4735.70(C)."),
 ("oh/agency", "Fiduciary duties", 1, "A licensee representing a client must disclose:",
  "Material facts they know or should know that are not confidential", ["Only what the client asks", "Nothing beyond the listing data", "Confidential information too"],
  "ORC 4735.62(F)."),
 ("oh/agency", "Fiduciary duties", 2, "Where a material matter needs expertise the licensee lacks, the duty is to:",
  "Advise the client to obtain expert advice", ["Give an opinion anyway", "Stay silent", "Withdraw from the agency"],
  "ORC 4735.62(G)."),
 ("oh/agency", "Confidentiality", 3, "Confidential information from a prior agency relationship:",
  "Must still be kept confidential", ["May be disclosed once the agency ends", "Belongs to the brokerage", "May be used for the new client"],
  "ORC 4735.62(F) and (I)."),

 # licensing
 ("oh/licensing", "Qualifying", 1, "The minimum age for an Ohio real estate salesperson licence is:",
  "18", ["17", "19", "21"],
  "ORC 4735.09."),
 ("oh/licensing", "Qualifying", 2, "An applicant born after 1950 must hold:",
  "A high school diploma or certificate of high school equivalence", ["A college degree", "No educational credential", "A trade certificate"],
  "ORC 4735.09(F)(5)."),
 ("oh/licensing", "Qualifying", 2, "An Ohio salesperson application must be accompanied by:",
  "The recommendation of the broker the applicant will associate with", ["Two personal references", "A credit report", "A surety bond"],
  "ORC 4735.09(A)."),
 ("oh/licensing", "Qualifying", 3, "How many times may an Ohio applicant retake the licensing examination?",
  "There is no limit", ["Three times", "Five times", "Twice in a year"],
  "ORC 4735.09(C)."),
 ("oh/licensing", "Education", 1, "Instruction in real estate practice required of an Ohio salesperson applicant is:",
  "40 hours", ["30 hours", "20 hours", "10 hours"],
  "ORC 4735.09(F)(6)(a)."),
 ("oh/licensing", "Education", 2, "Instruction in real estate finance required is:",
  "10 hours", ["20 hours", "30 hours", "40 hours"],
  "ORC 4735.09(F)(6)(d). The statute was reduced from 20."),
 ("oh/licensing", "Education", 2, "Instruction in real estate appraisal required is:",
  "10 hours", ["20 hours", "30 hours", "40 hours"],
  "ORC 4735.09(F)(6)(c)."),
 ("oh/licensing", "Education", 2, "The 40-hour Ohio real estate law course must also cover:",
  "Municipal, state and federal civil rights law", ["Appraisal theory", "Property management", "Business economics"],
  "ORC 4735.09(F)(6)(b)."),
 ("oh/licensing", "Education", 3, "The appraisal instruction requirement does not apply to:",
  "An applicant already holding an Ohio appraiser licence or certificate", ["Anyone over 40", "Applicants with a degree", "Military veterans"],
  "ORC 4735.09(G)(2)."),
 ("oh/licensing", "Post-licensure", 1, "Ohio post-licensure education is:",
  "20 hours within twelve months of licence issue", ["30 hours within three years", "10 hours within six months", "45 hours within 18 months"],
  "ORC 4735.09(J)."),
 ("oh/licensing", "Continuing education", 1, "Ohio continuing education is:",
  "30 hours every three years", ["30 hours every year", "14 hours every two years", "8 hours every year"],
  "ORC 4735.141(A)."),
 ("oh/licensing", "Continuing education", 2, "The continuing education deadline falls on:",
  "The licensee's birthday three years after initial licensure, and every three years after", ["31 December each year", "The anniversary of licensure each year", "30 June each year"],
  "ORC 4735.141(A)."),
 ("oh/licensing", "Continuing education", 2, "A broker's continuing education must include:",
  "A three-hour course on the duties of a principal broker", ["A six-hour appraisal course", "A one-hour maths course", "A fair housing roleplay"],
  "ORC 4735.141(A)."),
 ("oh/licensing", "Renewal", 2, "Ohio operates:",
  "A three-year licence and renewal system", ["An annual renewal", "A two-year renewal", "A five-year renewal"],
  "ORC 4735.10(A)(2)(b)."),
 ("oh/licensing", "Renewal", 3, "An Ohio licence remains valid until:",
  "It is placed inactive or resigned, revoked, suspended, or expires by law", ["Exactly two years from issue", "The licensee moves", "The broker closes"],
  "ORC 4735.14(A)."),

 # governance
 ("oh/governance", "Commission", 1, "The Ohio Real Estate Commission consists of:",
  "Five members appointed by the Governor", ["Seven members", "Nine members", "Three members elected by licensees"],
  "ORC 4735.03, with the advice and consent of the Senate."),
 ("oh/governance", "Commission", 2, "How many Commission members must be licensed Ohio brokers?",
  "Four", ["Two", "Three", "Five"],
  "With ten years in the business immediately preceding appointment."),
 ("oh/governance", "Commission", 2, "A broker member must have been licensed in Ohio for:",
  "Ten years immediately preceding appointment", ["Two years", "Five years", "Fifteen years"],
  "ORC 4735.03."),
 ("oh/governance", "Commission", 2, "Commission terms run for:",
  "Five years", ["Three years", "Four years", "Six years"],
  "Commencing 1 July (ORC 4735.03)."),
 ("oh/governance", "Commission", 3, "No more than how many Commission members may belong to one political party?",
  "Three", ["Two", "Four", "There is no limit"],
  "ORC 4735.03."),
 ("oh/governance", "Division", 2, "Ohio's licence law is administered by:",
  "The Division of Real Estate & Professional Licensing", ["The Secretary of State", "The Attorney General", "The Department of Taxation"],
  "Within the Ohio Department of Commerce."),
 ("oh/governance", "Recovery Fund", 1, "The Ohio Real Estate Recovery Fund pays at most, for any one licensee:",
  "$40,000", ["$20,000", "$50,000", "$100,000"],
  "ORC 4735.12(D)."),
 ("oh/governance", "Recovery Fund", 2, "Which is NOT recoverable from the Recovery Fund?",
  "Punitive damages, attorney's fees and interest", ["Actual loss", "Direct loss", "The unpaid part of the judgment"],
  "ORC 4735.12(B)(2)."),
 ("oh/governance", "Recovery Fund", 2, "An application for payment from the fund is filed in:",
  "The court of common pleas of Franklin county", ["Any county court", "The Ohio Supreme Court", "The Division's own tribunal"],
  "ORC 4735.12(B)(1)."),
 ("oh/governance", "Recovery Fund", 3, "Where valid claims against one licensee exceed the cap, the money is:",
  "Distributed in proportion to the claims", ["Paid first come, first served", "Returned to the state", "Split equally"],
  "ORC 4735.12(D)."),
 ("oh/governance", "Recovery Fund", 3, "A special assessment at renewal may be imposed when the fund holds less than:",
  "$250,000 on the preceding 1 July", ["$50,000", "$100,000", "$1,000,000"],
  "Up to $10 a year per licensee (ORC 4735.12(A))."),

 # --- license law, further
 ("oh/license-law", "Trust accounts", 3, "Cheques drawn on a broker's special or trust account are:",
  "Deemed to meet the conditions imposed by ORC 1349.21", ["Subject to a three-day hold", "Void if over $10,000", "Required to be certified"],
  "ORC 4735.18(A)(26)."),
 ("oh/license-law", "Trust accounts", 3, "A brokerage managing property may exercise signatory authority over an owner's account:",
  "Under a written contract with the property owner", ["Never", "Only with Division approval", "Only if the owner is absent"],
  "ORC 4735.10(A)(2)(e)(i)."),
 ("oh/license-law", "Earnest money", 2, "While a purchase agreement is on foot, earnest money in the trust account is held:",
  "In accordance with the terms of the purchase agreement", ["At the broker's discretion", "Until the listing expires", "Until the lender approves"],
  "ORC 4735.24(A)."),
 ("oh/license-law", "Earnest money", 3, "On closing, the broker disburses earnest money to:",
  "The closing or escrow agent, or as the purchase agreement directs", ["The seller always", "The buyer always", "The listing brokerage"],
  "ORC 4735.24(A)(1)."),
 ("oh/license-law", "Advertising", 2, "An out-of-state commercial broker's Ohio advertising must include:",
  "The name of the cooperating Ohio broker", ["Only the out-of-state firm name", "The Division's address", "The licence number of each agent"],
  "ORC 4735.022, referring to ORC 4735.16."),
 ("oh/license-law", "Fair housing", 2, "Refusing to negotiate for the rental of housing because of familial status is:",
  "Illegal under both Ohio and federal fair housing law", ["Legal if the owner occupies the building", "Legal for single-family homes", "A civil matter only"],
  "ORC 4112.02(H); 42 U.S.C. 3601."),
 ("oh/license-law", "Fair housing", 3, "The equal housing opportunity logotype required in an agency agreement comes from:",
  "24 C.F.R. 109.30", ["Ohio Administrative Code 1301:5", "The Ohio Civil Rights Commission", "The National Association of REALTORS"],
  "ORC 4735.55(C)(4)."),
 ("oh/license-law", "Misconduct", 2, "Failing to furnish a party a true copy of an agreement they signed is:",
  "A ground for disciplinary action", ["Acceptable if emailed later", "Only a civil matter", "Permitted for oral agreements"],
  "ORC 4735.18(A)(25)."),

 # --- agency, further
 ("oh/agency", "Written agreements", 3, "'Residential real property' in the written agency agreement section takes its meaning from:",
  "ORC 5302.30", ["ORC 4112.01", "ORC 1349.21", "The Commission's rules alone"],
  "ORC 4735.55(A)(1)."),
 ("oh/agency", "Written agreements", 2, "A licensee who shows a seller's home without a written agency agreement:",
  "Has violated ORC 4735.55", ["Is fine if the seller agrees later", "Is fine for one showing", "Needs only a disclosure statement"],
  "The agreement must precede the showing."),
 ("oh/agency", "Disclosure statement", 2, "The licensee must record on the agency disclosure statement:",
  "The accurate agency relationship", ["The commission split", "The listing price", "The closing date"],
  "ORC 4735.58(A)(2)."),
 ("oh/agency", "Disclosure statement", 3, "At auction, the successful bidder must receive the agency disclosure statement:",
  "Before signing a purchase contract", ["After closing", "Within three days", "Only on request"],
  "ORC 4735.58(B)."),
 ("oh/agency", "Dual agency", 2, "Before taking consent to dual agency, the licensee must:",
  "Disclose all relevant information needed for an informed decision", ["Obtain the broker's signature only", "File a notice with the Division", "Reduce the commission"],
  "ORC 4735.71(A)."),
 ("oh/agency", "Dual agency", 3, "A management level licensee is NOT a dual agent where:",
  "They personally represent only one side, and another management level licensee is affiliated", ["They have never met the parties", "The deal is commercial", "The brokerage is small"],
  "ORC 4735.70(C)(1)."),
 ("oh/agency", "Dual agency", 3, "A management level licensee who is themselves the buyer in an in-company deal:",
  "Represents only their own interest and is not a dual agent", ["Is always a dual agent", "May not buy at all", "Must resign the licence"],
  "ORC 4735.70(C)(2)."),
 ("oh/agency", "Fiduciary duties", 2, "A licensee representing a client must:",
  "Follow the client's lawful instructions", ["Follow all instructions without exception", "Act on the broker's instructions only", "Decide what is best regardless"],
  "ORC 4735.62(C)."),
 ("oh/agency", "Fiduciary duties", 2, "Accounting for money in which the client has an interest must be:",
  "Timely", ["Annual", "Only at closing", "On request alone"],
  "ORC 4735.62(H)."),
 ("oh/agency", "Fiduciary duties", 3, "Performing the terms of a written agency agreement is:",
  "A statutory fiduciary duty", ["A courtesy only", "Required only of brokers", "Optional if the client agrees"],
  "ORC 4735.62(B)."),
 ("oh/agency", "Fiduciary duties", 2, "Complying with fair housing law is:",
  "Part of the licensee's fiduciary duty to the client", ["Separate from agency duties", "The broker's duty alone", "Only a federal matter"],
  "ORC 4735.62(E)."),

 # --- licensing, further
 ("oh/licensing", "Qualifying", 2, "An applicant adjudged to have violated civil rights laws relevant to real estate:",
  "May still qualify if at least two years have passed and the superintendent is satisfied", ["Is barred for life", "Is unaffected", "Must wait ten years"],
  "ORC 4735.09(F)(2)(b)."),
 ("oh/licensing", "Qualifying", 3, "The salesperson application fee under the statute is:",
  "$81", ["$50", "$100", "$150"],
  "ORC 4735.09(B); it includes the initial year of the licensing period."),
 ("oh/licensing", "Qualifying", 3, "The initial year of an Ohio licensing period ends on:",
  "The applicant's first birthday after the licence is issued", ["31 December", "The anniversary of issue", "30 June"],
  "ORC 4735.09(B)."),
 ("oh/licensing", "Education", 3, "The Ohio real estate law instruction should, if feasible, be taught by:",
  "A member of the faculty of an accredited law school", ["Any licensed broker", "A Division employee", "A sitting judge"],
  "ORC 4735.09(F)(6)(b)."),
 ("oh/licensing", "Education", 3, "The civil rights instruction should, if feasible, be taught by:",
  "A knowledgeable staff member of the Ohio Civil Rights Commission", ["A fair housing lawyer", "A real estate broker", "A university professor"],
  "ORC 4735.09(F)(6)(b)."),
 ("oh/licensing", "Education", 3, "An applicant admitted to practise before the supreme court:",
  "Is excused from the 40-hour law and civil rights course", ["Is excused from all education", "Has no exemption", "Must take double the hours"],
  "ORC 4735.09(F)(6)(b)."),
 ("oh/licensing", "Post-licensure", 2, "Ohio post-licensure instruction must cover, among other things:",
  "Contract law and fiduciary responsibility", ["Appraisal theory only", "Construction methods", "Mortgage underwriting only"],
  "ORC 4735.09(J)."),
 ("oh/licensing", "Renewal", 3, "A licensee may not file a notice of renewal earlier than:",
  "Two months before the filing deadline", ["Six months before", "One year before", "There is no limit"],
  "ORC 4735.14(B)."),
 ("oh/licensing", "Renewal", 3, "The renewal notice is sent by the superintendent:",
  "Two months before the filing deadline, by email", ["By post one year ahead", "Only on request", "At the start of each year"],
  "ORC 4735.14(B)."),
 ("oh/licensing", "Status", 2, "A licensee who places the licence in resigned status:",
  "Is excused from the continuing education requirement while resigned", ["Must still complete 30 hours", "Loses the licence permanently", "Must retake the examination"],
  "ORC 4735.141(A), referring to ORC 4735.142."),

 # --- governance, further
 ("oh/governance", "Commission", 3, "A Commission member may not concurrently serve on:",
  "The real estate appraiser board", ["Any state board", "A local zoning board", "A school board"],
  "ORC 4735.03."),
 ("oh/governance", "Commission", 3, "Before taking office, each Commission member must:",
  "Subscribe to and file the constitutional oath of office with the secretary of state", ["Post a bond", "Resign any brokerage", "Pass the licensing exam again"],
  "ORC 4735.03."),
 ("oh/governance", "Commission", 2, "Commission terms commence on:",
  "The first day of July", ["1 January", "The date of appointment", "The first Monday of the year"],
  "ORC 4735.03."),
 ("oh/governance", "Recovery Fund", 2, "A claim on the Recovery Fund must rest on:",
  "A final judgment for conduct violating chapter 4735 in a licensed act", ["Any unpaid debt", "A Division complaint alone", "An arbitration award only"],
  "ORC 4735.12(B)(1)."),
 ("oh/governance", "Recovery Fund", 3, "Court costs may be recovered from the fund:",
  "At the superintendent's discretion", ["Always", "Never", "Only if under $1,000"],
  "ORC 4735.12(B)(2)."),
 ("oh/governance", "Recovery Fund", 3, "If a licensee's licence is reactivated after a fund payment, the fund's liability:",
  "Is again $40,000, but only for later transactions", ["Is exhausted permanently", "Doubles", "Is reduced to $20,000"],
  "ORC 4735.12(D)."),
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
            "id": "oh-" + hashlib.sha1(q.encode()).hexdigest()[:8],
            "portion": "georgia", "topic": topic, "subtopic": sub,
            "sub": topic + "|" + sub, "concept": "Ohio " + sub.lower(),
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
        "code": "OH", "name": "Ohio", "abbr": "OH",
        "regulator": "Ohio Division of Real Estate",
        "pass": EXAM["pass"],
        "portions": {
            "national": {"scored": EXAM["national_scored"],
                         "minutes": EXAM["national_minutes"]},
            "georgia": {"name": "Ohio state", "scored": EXAM["state_scored"],
                        "minutes": EXAM["state_minutes"],
                        "blurb": "Chapter 4735, the Commission's rules, agency, and Ohio fair housing."},
        },
        "topics": topics, "bank": bank, "study": study,
        "sources": SOURCES, "diffs": DIFFS,
    }


# Where Ohio departs from the national rule.
DIFFS = {
    "national/agency": [
        "Ohio requires a WRITTEN agency agreement before advertising or showing for a seller, before offering to purchase for a buyer, and before offering to lease for a tenant for more than eighteen months (ORC 4735.55).",
        "The agency disclosure statement is signed by the purchaser no later than the preparation of an offer, and by the seller before a written offer is presented (ORC 4735.58).",
        "Dual agency is allowed only with both parties' full knowledge and WRITTEN consent on that statement (ORC 4735.71).",
    ],
    "national/practice": [
        "An Ohio broker's sales trust account must be NONINTEREST-BEARING and at an institution located in Ohio; the property management account is separate and may earn interest for the owners (ORC 4735.18(A)(26)-(27)).",
        "Ohio fair housing adds ANCESTRY and MILITARY STATUS to the federal classes (ORC 4112.02(H)).",
        "The Real Estate Recovery Fund pays at most $40,000 for any one licensee, and never punitive damages, attorney's fees or interest (ORC 4735.12).",
    ],
    "national/contracts": [
        "Copies of every listing and agreement go to all parties AT THE TIME EACH SIGNS (ORC 4735.18(A)(25)).",
        "Disputed earnest money may be released only on written instructions signed by both parties, or a final court order (ORC 4735.24).",
    ],
}


if __name__ == "__main__":
    import io, json, os
    here = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    out = os.path.join(here, "greprep", "packs", "OH.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    pack = build()
    with io.open(out, "w", encoding="utf-8") as f:
        json.dump(pack, f, ensure_ascii=False, indent=1, sort_keys=True)
    print("wrote", out, len(pack["bank"]), "questions,", len(pack["study"]), "lessons")
