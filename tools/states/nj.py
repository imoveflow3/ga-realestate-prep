"""New Jersey state content: lessons and practice questions.

New Jersey writes ONE paper. The PSI bulletin's examination summary table
gives the salesperson examination as 110 questions, a passing score of 70%
(77 correct) and 4 hours. The New Jersey portion of the content outline
carries 30 of those items; the other 80 are the national areas.

The big thing to know about New Jersey in 2026 is that its agency law was
rewritten by P.L.2024, c.32, the act that created brokerage services
agreements, the transaction broker, the designated agent and the open
house sign. Commercial study guides written before it are wrong.

Every rule below was read from the official statute text on 2026-11-09 and
2026-11-10 at lis.njleg.state.nj.us:
  - R.S.45:15-1 et seq., the real estate licence act (education, offices,
    commissions, grounds for discipline, the guaranty fund).
  - P.L.2024, c.32 (C.45:15-16.86 et al.), the agency statute.
  - The Real Estate Sales Full Disclosure Act (C.45:15-16.27 et seq.) and
    the New Jersey Real Estate Timeshare Act (C.45:15-16.50 et seq.).
  - The Law Against Discrimination, N.J.S.A. 10:5-12.
  - The realty transfer fee, N.J.S.A. 46:15-7; security deposits,
    N.J.S.A. 46:8-19; the Truth in Renting Act, N.J.S.A. 46:8-44 et seq.
  - The Real Estate Commission's own published continuing education
    breakdown at nj.gov/dobi/division_rec.
  - The PSI New Jersey Candidate Information Bulletin, for the examination
    table and the 30-item New Jersey outline.
The section a fact comes from is cited next to it. Do not add a fact here
without reading its source first.
"""

EXAM = {
    # One paper: 110 questions, 70% (77 correct), 4 hours.
    "state_scored": 30,
    "state_minutes": 65,
    "national_scored": 80,
    "national_minutes": 175,
    "pass": 0.70,
}

# PSI's New Jersey outline, salesperson item counts: 22+3+3+2 = 30.
TOPICS = [
    ("nj/activities", "Statutes & rules on licensee activity", 22,
     "Agency, trust money, advertising, listings, commissions, other laws."),
    ("nj/licensing", "Licensing requirements", 3,
     "Who needs a licence, the types, education and offices."),
    ("nj/additional", "Additional requirements", 3,
     "Full Disclosure Act, the Law Against Discrimination, guaranty fund, timeshares."),
    ("nj/commission", "Duties & powers of the Commission", 2,
     "Records, investigations and what the Commission can do to a licence."),
]

SOURCES = [
    {"by": "New Jersey Legislature",
     "name": "R.S.45:15-1 et seq., the real estate licence act",
     "note": "Education, offices, commissions, the grounds for discipline in 45:15-17, and the guaranty fund.",
     "url": "https://lis.njleg.state.nj.us/nxt/gateway.dll/statutes/1"},
    {"by": "New Jersey Legislature",
     "name": "P.L.2024, c.32 (C.45:15-16.86 et al.)",
     "note": "The current agency law: brokerage services agreements, buyer's and seller's agents, disclosed dual agents, designated agents and transaction brokers.",
     "url": "https://lis.njleg.state.nj.us/nxt/gateway.dll/statutes/1"},
    {"by": "New Jersey Legislature",
     "name": "N.J.S.A. 10:5-12, the Law Against Discrimination",
     "note": "New Jersey's protected classes in housing, which run far past the federal list.",
     "url": "https://lis.njleg.state.nj.us/nxt/gateway.dll/statutes/1"},
    {"by": "New Jersey Real Estate Commission",
     "name": "Breakdown of required continuing education hours",
     "note": "The Commission's own published 12-hour breakdown.",
     "url": "https://www.nj.gov/dobi/division_rec/licensing/breakdowncehours.html"},
    {"by": "PSI Services and the New Jersey Real Estate Commission",
     "name": "New Jersey Candidate Information Bulletin",
     "note": "One 110-question paper, 4 hours, 70% (77 correct), and the 30-item New Jersey outline.",
     "url": "https://test-takers.psiexams.com/njre"},
]


# --------------------------------------------------------------- lessons

STUDY = {}

STUDY["nj/activities"] = {
    "summary": "Twenty-two of the thirty state items. Agency was rewritten in 2024, so learn it from the statute, not from an older guide. After that the marks are in 45:15-17, the long list of things that cost you your licence.",
    "sections": [
        {"h": "The 2024 agency act: what a firm IS by default",
         "l": ["A brokerage firm that performs real estate brokerage services FOR A BUYER IS A BUYER'S AGENT unless (1) the firm represents the seller under a brokerage services agreement, (2) it represents both under agreements, making it a DISCLOSED DUAL AGENT, (3) it has agreed to work with the buyer as a TRANSACTION BROKER, or (4) the licensee is the seller (C.45:15-16.88).",
               "The mirror rule applies to sellers: a firm performing services FOR A SELLER IS A SELLER'S AGENT subject to the same four exceptions (C.45:15-16.90).",
               "In a RESIDENTIAL transaction the firm must enter into a BROKERAGE SERVICES AGREEMENT with the buyer BEFORE, OR AS SOON AS REASONABLY PRACTICAL AFTER, it starts rendering services. No such agreement is required with a buyer in a COMMERCIAL transaction (C.45:15-16.88(b)(1)).",
               "A BROKERAGE SERVICES AGREEMENT is a written agreement appointing a firm to represent a principal as agent or to work with a party as a transaction broker. It covers listing agreements, buyer agency agreements, and transaction broker, dual agency and designated agency agreements (C.45:15-16.86).",
               "The agreement must state the TERM, that the firm is appointed as agent, whether the relationship is EXCLUSIVE OR NONEXCLUSIVE, and, by separate initial or signature, whether the party consents to DISCLOSED DUAL AGENCY or DESIGNATED AGENCY - with an acknowledgement that a disclosed dual agent will NOT advocate terms favourable to one principal to the detriment of the other."],
         "check": [("A New Jersey firm that performs brokerage services for a buyer is, by default:", "A buyer's agent", ["A subagent of the seller", "A transaction broker", "A dual agent"], "C.45:15-16.88(a)."),
                   ("A written brokerage services agreement with the buyer is required:", "In a residential transaction, before or as soon as reasonably practical after services begin", ["In every transaction without exception", "Only at the offer", "Never"], "C.45:15-16.88(b)(1)."),
                   ("A buyer in a COMMERCIAL transaction:", "Does not need a brokerage services agreement with the firm", ["Needs one before any showing", "Needs one signed by the Commission"], "C.45:15-16.88(b)(1)."),
                   ("Consent to dual or designated agency must be shown by:", "Separate initialling or signature in the brokerage services agreement or another document", ["A verbal agreement", "The listing alone"], "C.45:15-16.88(b)(2)(d).")]},
        {"h": "Duties that cannot be waived (C.45:15-16.87)",
         "p": ["A brokerage firm acting as a buyer's agent, seller's agent, disclosed dual agent or designated agent owes these to its principal AND to all parties, and they MAY NOT BE WAIVED:"],
         "l": ["Strict compliance with the laws of agency and the principles governing FIDUCIARY relationships.",
               "REASONABLE SKILL AND CARE.",
               "To deal HONESTLY AND IN GOOD FAITH.",
               "To present ALL WRITTEN OFFERS AND COUNTEROFFERS in a timely manner and confirm receipt in writing to the other side - REGARDLESS of whether the property is already under contract or the buyer is already a party to a contract on another property, unless the principal directs otherwise in writing.",
               "Where the principal is a residential seller, to obtain a SIGNED PROPERTY CONDITION DISCLOSURE STATEMENT (C.56:8-19.1); an unrepresented seller must give it to the buyer BEFORE the buyer becomes obligated under a contract.",
               "To disclose all existing MATERIAL INFORMATION known, or that a reasonable effort would have revealed, about the PHYSICAL CONDITION of the property.",
               "To ACCOUNT in a timely manner for all money and property received.",
               "To provide the CONSUMER INFORMATION STATEMENT in the Commission's form and get a signed acknowledgement - to a party the firm serves no later than when they sign the brokerage services agreement, and to an unrepresented party before they sign an offer or as soon as practical after.",
               "To disclose in writing, no later than when the principal signs, the firm's capacity in a paragraph titled 'AGENCY DISCLOSURE', and the terms of any compensation offered to another firm.",
               "To undertake a reasonable effort to obtain material information about the condition of every property it takes on."],
         "check": [("Written offers must be presented:", "In a timely manner even where the property is already under contract, unless the principal directs otherwise in writing", ["Only until a contract is signed", "Only above list price"], "C.45:15-16.87(d)."),
                   ("The consumer information statement must reach a party the firm serves:", "No later than when they sign the brokerage services agreement", ["At closing", "Within 7 days of the offer"], "C.45:15-16.87(h)(1)."),
                   ("An unrepresented party must get the consumer information statement:", "Before signing an offer, or as soon as reasonably practical after", ["Never", "Only on request"], "C.45:15-16.87(h)(2)."),
                   ("The agency capacity must be disclosed in writing in a paragraph titled:", "Agency Disclosure", ["Notice to Consumer", "Material Facts"], "C.45:15-16.87(i)(1)."),
                   ("These statutory duties:", "May not be waived", ["May be waived in writing", "Apply only to sellers"], "C.45:15-16.87.")]},
        {"h": "Buyer's agent, dual agent, transaction broker",
         "l": ["A BUYER'S AGENT owes LOYALTY (no action adverse to the buyer, primary devotion to the buyer's interests), timely disclosure of conflicts, advice to seek expert help beyond the agent's expertise, CONFIDENTIALITY that survives termination of the relationship, and a good-faith continuous effort to find a property - though not while the buyer is under a contract that is past the attorney-review period (C.45:15-16.89).",
               "Showing the same property to OTHER prospective buyers does NOT breach loyalty, and representing more than one buyer in COMPETING transactions on the same property does NOT breach loyalty or create a conflict (C.45:15-16.89(b)).",
               "A DISCLOSED DUAL AGENT acts only with the INFORMED CONSENT OF BOTH PARTIES, set out in the brokerage services agreements each signs. The dual agent takes no action adverse to either, keeps BOTH sides' confidential information, and advises both to seek expert advice (C.45:15-16.92).",
               "A TRANSACTION BROKER is NOT an agent for and does not represent any party, does not promote one party's interest over the other, and IS NOT REQUIRED TO KEEP ANY INFORMATION CONFIDENTIAL. It treats all parties honestly, presents all written offers, keeps everyone informed, and works toward an agreement WITHOUT advising any party how to gain an advantage at the other's expense (C.45:15-16.94)."],
         "check": [("A New Jersey transaction broker:", "Represents no party and is not required to keep information confidential", ["Is a dual agent", "Owes fiduciary duties to the buyer"], "C.45:15-16.94(a)."),
                   ("Showing the same property to other prospective buyers:", "Does not breach a buyer's agent's duty of loyalty", ["Breaches loyalty", "Requires written consent"], "C.45:15-16.89(b)(1)."),
                   ("A buyer's agent's duty of confidentiality:", "Survives termination of the agency relationship", ["Ends at closing", "Ends when the agreement expires"], "C.45:15-16.89(a)(4)."),
                   ("A disclosed dual agent may act only with:", "The informed consent of both parties in their signed brokerage services agreements", ["The broker's approval", "An oral consent"], "C.45:15-16.92(a)."),
                   ("A dual agent must:", "Take no action adverse or detrimental to either party's interest", ["Favour the seller", "Disclose each side's position to the other"], "C.45:15-16.92(b)(1).")]},
        {"h": "The open house sign (C.45:15-16.99)",
         "p": ["At any residential showing GENERALLY OPEN TO THE PUBLIC, a sign must be posted at the ENTRANCE OR AT THE SIGN-IN SHEET telling prospective buyers the hosting firm REPRESENTS THE SELLER ONLY. The statute prints the exact wording, which warns that ANY INFORMATION YOU GIVE THIS AGENT IS NOT CONSIDERED CONFIDENTIAL and could be disclosed to the seller, that the buyer may have their own agent, and that a buyer already exclusively represented MUST disclose that on the sign-in sheet."],
         "check": [("At a public open house the required sign must be posted:", "At the entrance or at the sign-in sheet", ["In the kitchen", "In the listing only"], "C.45:15-16.99(a)."),
                   ("The sign tells buyers that what they say to the open house agent is:", "Not confidential and could be disclosed to the seller", ["Confidential", "Privileged"], "C.45:15-16.99(b)."),
                   ("A buyer already exclusively represented by a buyer's agent must:", "Disclose that representation on the sign-in sheet", ["Leave the open house", "Say nothing"], "C.45:15-16.99(b).")]},
        {"h": "Trust money, commissions and rebates",
         "l": ["COMMINGLING the money or property of principals with the licensee's own, or failing to maintain and deposit in a SPECIAL ACCOUNT SEPARATE AND APART from personal or other business accounts all money received as broker, escrow agent or temporary custodian of others' funds, is a ground for discipline (R.S.45:15-17(o)).",
               "FAILURE TO ACCOUNT FOR OR PAY OVER money belonging to others is likewise a ground (R.S.45:15-17(d)).",
               "A salesperson or broker-salesperson may accept a commission ONLY FROM THEIR EMPLOYING OR CONTRACTING BROKER, who must be a licensed broker (R.S.45:15-16(a); 45:15-17(m)). They may form an LLC or other entity to receive it, registered with the Commission (R.S.45:15-16(b), (c)).",
               "PAYING any rebate, profit, compensation or commission to ANYONE NOT HOLDING A REAL ESTATE LICENCE is a ground for discipline, with two exceptions: the promotional services in subsection g., and a REBATE to a PURCHASER OF RESIDENTIAL REAL PROPERTY - but to no other third party - where the rebate was contracted for IN WRITING AT THE ONSET of the broker relationship, the broker complies with disclosure requirements, and the broker recommends the purchaser speak to a TAX PROFESSIONAL. The rebate is paid AT CLOSING as a credit reducing the commission or a cheque from the closing agent (R.S.45:15-17(k)).",
               "If a broker runs a promotion conferring a benefit WORTH MORE THAN $1,000, the broker must disclose the benefit in writing to the recipient and disclose any compensation received, in RESPA form, NO LATER THAN WHEN THE OFFER IS EXTENDED (R.S.45:15-17(g))."],
         "check": [("A salesperson may accept a commission from:", "Their employing or contracting broker only", ["The seller directly", "Any licensed broker", "The title company"], "R.S.45:15-16(a); 45:15-17(m)."),
                   ("A broker may rebate part of the commission to:", "A purchaser of residential real property, under a written agreement made at the onset of the relationship", ["Any unlicensed referrer", "The seller's attorney", "Nobody"], "R.S.45:15-17(k)(2)."),
                   ("That rebate must be paid:", "At the time of closing, as a credit or a cheque from the closing agent", ["In cash on signing", "Within 30 days of closing"], "R.S.45:15-17(k)(2)."),
                   ("A promotional benefit requiring written disclosure is one worth more than:", "$1,000", ["$100", "$500", "$5,000"], "R.S.45:15-17(g)."),
                   ("Money held for others must be kept:", "In a special account separate and apart from personal or other business accounts", ["In the broker's operating account", "By the salesperson"], "R.S.45:15-17(o).")]},
        {"h": "Listings, contracts and conflicts (R.S.45:15-17)",
         "l": ["FAILURE to give the client a FULLY EXECUTED COPY of any sale or exclusive sales or rental listing contract AT THE TIME OF EXECUTION, or failure to state a DEFINITE TERMINAL DATE not subject to qualifying terms or conditions, is a ground for discipline (subsection f.).",
               "ACTING FOR MORE THAN ONE PARTY in a transaction WITHOUT THE KNOWLEDGE of all parties is a ground (subsection b.).",
               "SELLING property in which the licensee has an interest requires DISCLOSURE IN THE CONTRACT OF SALE of that interest and of the licensee's status; BUYING property requires disclosure of the licensee's status in the contract (subsections p. and q.).",
               "Collecting a commission as broker while at the same time representing either party in a DIFFERENT CAPACITY for consideration is a ground (subsection i.).",
               "Using a TRADE NAME OR INSIGNIA of a real estate organisation the licensee does not belong to is a ground (subsection j.).",
               "Any plan for selling real estate involving a LOTTERY, CONTEST, GAME, PRIZE OR DRAWING, or offering lots for advertising purposes, is a ground (subsection g.).",
               "Charging a fee for information on PURPORTEDLY AVAILABLE RENTAL HOUSING before a lease is executed, or before the tenant takes possession where there is no lease, without complying with the Commission's rules, is a ground (subsection r.).",
               "A licensee must NOTIFY THE COMMISSION WITHIN 30 DAYS of a conviction of any crime, misdemeanour or disorderly persons offence, an indictment, the filing of formal criminal charges, the suspension or revocation of a licence in another state, or formal discipline elsewhere (subsection s.)."],
         "check": [("A listing contract must specify:", "A definite terminal date not subject to qualifying terms or conditions", ["A 90-day minimum", "An automatic renewal"], "R.S.45:15-17(f)."),
                   ("A licensee selling property they own must disclose their interest and licence status:", "In the contract of sale", ["At the closing table", "Only if asked"], "R.S.45:15-17(p)."),
                   ("A licensee convicted of a disorderly persons offence must notify the Commission within:", "30 days", ["90 days", "At renewal", "Never"], "R.S.45:15-17(s)."),
                   ("Promoting a sale of real estate with a prize drawing is:", "A ground for discipline", ["Permitted with disclosure", "Permitted for new construction"], "R.S.45:15-17(g).")]},
        {"h": "Other laws on the outline",
         "l": ["REALTY TRANSFER FEE: the GRANTOR pays it to the COUNTY RECORDING OFFICER at the time the deed is offered for recording. The basic fee is $1.25 per $500 of consideration (state portion) plus $0.50 per $500 (county portion), with an additional fee of $0.75 per $500 on consideration ABOVE $150,000 and a tiered general purpose fee that starts at $0.90 per $500 and does NOT apply at all where the total consideration does not exceed $350,000 (N.J.S.A. 46:15-7). A misstated consideration does NOT impair the title conveyed.",
               "SECURITY DEPOSITS: the money REMAINS THE PROPERTY OF THE TENANT, is HELD IN TRUST, and SHALL NOT BE MINGLED with the landlord's property or become an asset of the landlord. It must be invested in a qualifying money market fund or deposited in an insured New Jersey institution in an interest-bearing account (N.J.S.A. 46:8-19).",
               "TRUTH IN RENTING ACT: 'landlord' EXCLUDES premises of not more than two dwelling units, owner-occupied premises of not more than three, and hotels and motels serving transient or seasonal guests (N.J.S.A. 46:8-44). The Department of Community Affairs prepares an annual STATEMENT OF LEGAL RIGHTS AND RESPONSIBILITIES of tenants and landlords, free, in ENGLISH AND SPANISH, posted on its website (N.J.S.A. 46:8-45).",
               "The outline also names the FARMLAND REASSESSMENT ACT, the PINELANDS PROTECTION ACT of 1979, the FRESHWATER WETLANDS PROTECTION ACT of 1987, MOUNT LAUREL affordable housing requirements, zoning and building codes, and the MUNICIPAL LAND USE LAW."],
         "check": [("Who pays the New Jersey realty transfer fee?", "The grantor, at the time the deed is offered for recording", ["The grantee at closing", "The lender", "The broker"], "N.J.S.A. 46:15-7(a)."),
                   ("A security deposit in New Jersey:", "Remains the tenant's property and is held in trust, not mingled with the landlord's property", ["Becomes the landlord's on receipt", "May be spent on repairs at any time"], "N.J.S.A. 46:8-19."),
                   ("The Truth in Renting Act's definition of landlord excludes:", "Premises of not more than two dwelling units, and owner-occupied premises of not more than three", ["All single-family rentals", "Any property under 10 units"], "N.J.S.A. 46:8-44(a)."),
                   ("The Truth in Renting statement must be printed in:", "English and Spanish", ["English only", "Every language requested"], "N.J.S.A. 46:8-45(a)."),
                   ("The general purpose part of the realty transfer fee does not apply where the consideration:", "Does not exceed $350,000", ["Does not exceed $150,000", "Exceeds $1,000,000"], "N.J.S.A. 46:15-7(a)(3)(a).")]},
    ],
    "traps": [
        "Agency changed in 2024. A firm working with a buyer IS a buyer's agent by default.",
        "A transaction broker keeps NOTHING confidential; a dual agent keeps EVERYTHING confidential.",
        "The rebate exception runs to a residential PURCHASER only - no other third party.",
        "A listing needs a definite terminal date, and the client gets a copy at execution.",
        "The grantor pays the realty transfer fee, at recording, to the county.",
    ],
    "vocab": [
        ["Brokerage services agreement", "The written agreement appointing a firm as agent or transaction broker."],
        ["Consumer information statement", "The Commission's form explaining the relationships available."],
        ["Disclosed dual agent", "One firm representing both sides with informed written consent."],
        ["Designated agent", "An individual licensee named to act for one party."],
        ["Transaction broker", "A firm representing nobody, keeping nothing confidential."],
        ["Attorney-review period", "The window the statute refers to for contracts past review."],
    ],
    "examples": [
        {"t": "Open house walk-in",
         "s": "A buyer with no agent walks into your public open house and starts telling you their top price.",
         "w": ["The sign at the entrance or sign-in sheet already told them you represent the seller only and that nothing they say is confidential.",
               "You must give them the consumer information statement before they sign an offer, or as soon as reasonably practical.",
               "You may become a disclosed dual agent or designated agent only with informed consent in signed agreements."],
        "k": "The sign does the warning; the consumer information statement does the explaining."},
    ],
}

STUDY["nj/licensing"] = {
    "summary": "Only three items, so learn the four numbers: 75 hours, 150 hours, 12 hours of continuing education, and age 18.",
    "sections": [
        {"h": "Education (R.S.45:15-10.1)",
         "l": ["SALESPERSON: 75 HOURS in the aggregate of approved courses at a Commission-licensed school, as a PREREQUISITE TO ADMISSION TO THE EXAMINATION. At least 3 HOURS must be on ETHICS and ethical conduct, and at least 1 HOUR on FAIR HOUSING and housing discrimination.",
               "BROKER or BROKER-SALESPERSON: 150 HOURS in the aggregate, of which 30 HOURS must be on ETHICS and at least 1 HOUR on FAIR HOUSING. The broker course is taken as a 90-hour general course plus two 30-hour courses, all certified on a SINGLE SCHOOL CERTIFICATE though they need not be taken at the same school.",
               "CONTINUING EDUCATION, as the Commission publishes it: at least 12 CREDIT HOURS per cycle - 1 hour FAIR HOUSING AND THE NEW JERSEY LAW AGAINST DISCRIMINATION, 1 hour AGENCY, 2 hours ETHICS, 2 hours ANY CORE TOPIC, and 6 hours of any combination of core and elective topics. Ethics, fair housing and agency hours may substitute for core and elective hours, but core and elective hours may NOT substitute for them."],
         "check": [("Prelicensure education for a New Jersey salesperson is:", "75 hours", ["150 hours", "60 hours", "90 hours"], "R.S.45:15-10.1(a)."),
                   ("Of those hours, the statute requires at least:", "3 hours of ethics and 1 hour of fair housing", ["6 hours of ethics", "4 hours of fair housing"], "R.S.45:15-10.1(a)."),
                   ("A broker candidate must complete:", "150 hours, including 30 hours of ethics", ["75 hours", "120 hours including 10 of ethics"], "R.S.45:15-10.1(b)."),
                   ("Continuing education in New Jersey is:", "12 credit hours per cycle", ["18 hours", "6 hours", "24 hours"], "NJREC published CE breakdown."),
                   ("Of those 12 hours, ethics accounts for:", "2 credit hours", ["1 hour", "3 hours", "4 hours"], "NJREC published CE breakdown."),
                   ("May core and elective hours be used in place of the required fair housing hour?", "No; fair housing may replace core and electives, but not the reverse", ["Yes, freely", "Yes, with Commission approval"], "NJREC published CE breakdown.")]},
        {"h": "Qualifying (R.S.45:15-9)",
         "l": ["Every applicant must be 18 YEARS OF AGE OR OVER and have the EQUIVALENT OF A HIGH SCHOOL EDUCATION.",
               "The applicant must furnish evidence of GOOD MORAL CHARACTER, and must submit NAME, ADDRESS, FINGERPRINTS and written consent for a CRIMINAL HISTORY RECORD BACKGROUND CHECK, at the applicant's own cost. The State Police must notify the commissioner if a licensee or applicant who was checked is later ARRESTED in New Jersey.",
               "A BROKER or BROKER-SALESPERSON applicant must FIRST have held a New Jersey SALESPERSON'S licence and have been actively engaged FULL TIME in the brokerage business in New Jersey as a salesperson for THREE YEARS immediately preceding the application. The Commission may waive that where the applicant held a broker's licence in another state for at least three years, meets the education requirement and passes the examination.",
               "A nonresident's licence is deemed IRREVOCABLE CONSENT to service of process through the Commission's secretary."],
         "check": [("The minimum age for a New Jersey licence is:", "18", ["17", "19", "21"], "R.S.45:15-9(a)."),
                   ("Every applicant must have:", "The equivalent of a high school education", ["A college degree", "No educational minimum"], "R.S.45:15-9(a)."),
                   ("A broker applicant must have been a full-time New Jersey salesperson for:", "Three years immediately preceding the application", ["One year", "Five years", "Six months"], "R.S.45:15-9(a)."),
                   ("Who pays for the criminal history record background check?", "The applicant", ["The employing broker", "The Commission"], "R.S.45:15-9(a).")]},
        {"h": "Offices (R.S.45:15-12)",
         "l": ["Every broker must maintain a DESIGNATED MAIN OFFICE OPEN TO THE PUBLIC, with the licence certificates of the broker and all licensed persons in their employ PROMINENTLY DISPLAYED. That office is the BUSINESS ADDRESS of all those licensees for all purposes under the act.",
               "A BRANCH OFFICE LICENCE is required for each additional place of business, each branch must be under the DIRECT SUPERVISION OF A BROKER-SALESPERSON, and the fee is $50 PER LICENCE.",
               "Every place of business must display CONSPICUOUSLY ON THE EXTERIOR the name the broker is authorised to operate under, for a corporation or partnership the name of its authorised broker, and the words LICENSED REAL ESTATE BROKER.",
               "A broker whose main office is in another state must hold a valid broker's licence in good standing in that state."],
         "check": [("Each New Jersey branch office must be under the direct supervision of:", "A broker-salesperson", ["Any licensed salesperson", "The main office broker remotely"], "R.S.45:15-12."),
                   ("Every place of business must display on the exterior:", "The authorised name and the words Licensed Real Estate Broker", ["The licence number", "The office hours"], "R.S.45:15-12."),
                   ("The broker's main office must:", "Be open to the public and display the licence certificates of the broker and everyone in their employ", ["Be in the broker's home", "Display only the broker's certificate"], "R.S.45:15-12.")]},
    ],
    "traps": [
        "75 for salesperson, 150 for broker. The broker's ethics requirement is 30 hours, not 3.",
        "Continuing education is 12 hours, and the mandated hours cannot be covered by electives.",
        "Three years full time as a New Jersey salesperson before a broker's licence.",
        "A branch is supervised by a BROKER-SALESPERSON, not by any salesperson.",
    ],
    "vocab": [
        ["Broker-salesperson", "A licensee qualified as a broker who works for another broker."],
        ["School certificate", "The single certificate carrying all three broker courses."],
        ["Main office", "The designated public office that is every licensee's business address."],
        ["CHRI check", "The criminal history record background check applicants pay for."],
    ],
    "examples": [],
}

STUDY["nj/additional"] = {
    "summary": "Three items across four named statutes. The Law Against Discrimination is the one worth real study - its list is the longest in the country.",
    "sections": [
        {"h": "The Law Against Discrimination (N.J.S.A. 10:5-12(h))",
         "p": ["It is unlawful for ANY PERSON, including a real estate broker or salesperson or their employee or agent, to refuse to sell, rent, lease, assign or sublease, to refuse to negotiate, to represent that property is unavailable when it is available, to discriminate in the terms, conditions or privileges, or to publish any advertisement or make any record or inquiry indicating a preference, because of:"],
         "l": ["RACE", "CREED", "COLOR", "NATIONAL ORIGIN", "ANCESTRY",
               "MARITAL STATUS", "CIVIL UNION STATUS", "DOMESTIC PARTNERSHIP STATUS",
               "FAMILIAL STATUS", "PREGNANCY OR BREASTFEEDING", "SEX",
               "GENDER IDENTITY OR EXPRESSION", "AFFECTIONAL OR SEXUAL ORIENTATION",
               "DISABILITY", "LIABILITY FOR SERVICE IN THE ARMED FORCES", "NATIONALITY",
               "SOURCE OF LAWFUL INCOME USED FOR RENTAL OR MORTGAGE PAYMENTS",
               "A landlord may not refuse a tenant because of the SOURCE of lawful income or rent payment, including by refusing to accept it, or by applying a MINIMUM INCOME REQUIREMENT that is not based exclusively on THE PORTION OF THE RENT THE TENANT ACTUALLY PAYS (10:5-12(g)(4)).",
               "Refusing to rent because a family includes CHILDREN UNDER 18, or making a lease void on the birth of a child, is unlawful, except for HOUSING FOR OLDER PERSONS (10:5-12(g)(5)).",
               "Producing a discriminatory advertisement or application is PRESUMPTIVE EVIDENCE that the person named authorised it."],
         "check": [("Which is protected in New Jersey housing but not by the federal Fair Housing Act?", "Source of lawful income used for rental or mortgage payments", ["Race", "Color", "National origin"], "N.J.S.A. 10:5-12(h)(1)."),
                   ("New Jersey also protects:", "Civil union status and domestic partnership status", ["Credit score", "Employment history"], "N.J.S.A. 10:5-12(h)(1)."),
                   ("A landlord applying a minimum income test to a voucher holder must base it on:", "Only the portion of the rent the tenant actually pays", ["The full contract rent", "Three times the market rent"], "N.J.S.A. 10:5-12(g)(4)."),
                   ("Refusing to rent to a family with children under 18 is lawful only for:", "Housing for older persons as defined in the act", ["Any owner-occupied building", "Studio apartments"], "N.J.S.A. 10:5-12(g)(5)."),
                   ("A discriminatory advertisement is:", "Presumptive evidence that the person named authorised it", ["Only evidence if admitted", "Not actionable without a refusal"], "N.J.S.A. 10:5-12(g)(3).")]},
        {"h": "The Real Estate Guaranty Fund (C.45:15-34)",
         "l": ["A special TRUST FUND maintained by the STATE TREASURER and administered by the COMMISSION.",
               "It pays a person aggrieved by the EMBEZZLEMENT, CONVERSION OR UNLAWFUL OBTAINING of money or property IN A REAL ESTATE BROKERAGE TRANSACTION by a licensed broker, broker-salesperson or salesperson, or by an UNLICENSED EMPLOYEE OF A BROKER.",
               "The cap is $20,000 IN THE AGGREGATE PER TRANSACTION for causes of action accruing after P.L.1993, c.51 - regardless of the number of claims, aggrieved persons or parcels involved. The original figure was $10,000."],
         "check": [("The Real Estate Guaranty Fund covers losses from:", "Embezzlement, conversion or unlawful obtaining of money in a brokerage transaction", ["A bad home inspection", "A failed mortgage application", "Negligent pricing advice"], "C.45:15-34."),
                   ("The maximum recovery per transaction is:", "$20,000 in the aggregate", ["$10,000", "$50,000", "Unlimited"], "C.45:15-34, as amended by P.L.1993, c.51."),
                   ("The fund is held by:", "The State Treasurer, administered by the Commission", ["The Commission's own bank", "A private insurer"], "C.45:15-34.")]},
        {"h": "The Real Estate Sales Full Disclosure Act",
         "l": ["It governs the DISPOSITION OF SUBDIVIDED LANDS. No one may dispose of an interest unless a CURRENT PUBLIC OFFERING STATEMENT is DELIVERED TO THE PURCHASER and the purchaser has a REASONABLE OPPORTUNITY TO EXAMINE IT BEFORE the disposition (C.45:15-16.30).",
               "It does NOT apply to, among others, a sale by an owner for their own account in a SINGLE OR ISOLATED transaction, purely INDUSTRIAL OR COMMERCIAL dispositions, sales by court order or a governmental agency, CEMETERY lots, subdivisions of FEWER THAN 100 lots, parcels, units or interests, or developments made up WHOLLY OF RENTAL UNITS (C.45:15-16.32).",
               "A subdivider adding land under the same common promotional plan may make a CONSOLIDATED FILING (C.45:15-16.39)."],
         "check": [("The Full Disclosure Act does not apply to a subdivision of:", "Fewer than 100 lots, parcels, units or interests", ["Fewer than 10 lots", "Fewer than 50 lots"], "C.45:15-16.32(a)(6)."),
                   ("Before disposing of an interest in subdivided lands the seller must:", "Deliver a current public offering statement and give a reasonable opportunity to examine it", ["Record a plat", "Post a bond with the county"], "C.45:15-16.30(b)."),
                   ("A development made up wholly of rental units is:", "Exempt, because the relationship created is landlord and tenant", ["Covered in full", "Covered only above 100 units"], "C.45:15-16.32(a)(8).")]},
        {"h": "The New Jersey Real Estate Timeshare Act (2006)",
         "l": ["A developer who sells or offers timeshare interests in New Jersey must REGISTER the timeshare plan with the Commission. The Commission may grant a 90-DAY PRELIMINARY REGISTRATION while a full application is pursued (C.45:15-16.57).",
               "The developer must prepare a PUBLIC OFFERING STATEMENT, give it to each purchaser AT THE TIME OF PURCHASE, and have the purchaser CERTIFY RECEIPT IN WRITING (C.45:15-16.59).",
               "The statement must say that a purchaser may CANCEL the purchase contract WITHIN SEVEN DAYS after RECEIPT OF THE PUBLIC OFFERING STATEMENT or after EXECUTION OF THE PURCHASE CONTRACT, WHICHEVER IS LATER (C.45:15-16.59(b)(10)).",
               "The DEVELOPER is responsible for each registered plan and for the acts of any SALES AGENT, MARKETING ENTITY OR MANAGING ENTITY it uses - a violation by them is a violation by the developer too (C.45:15-16.58)."],
         "check": [("A New Jersey timeshare purchaser may cancel within:", "Seven days of receiving the public offering statement or executing the contract, whichever is later", ["Three days", "Ten business days", "Thirty days"], "C.45:15-16.59(b)(10)."),
                   ("A violation committed by a timeshare developer's sales agent is:", "A violation by the developer as well", ["The agent's alone", "Not actionable"], "C.45:15-16.58."),
                   ("A preliminary timeshare registration lasts:", "90 days, extendable while a complete application is pursued", ["One year", "30 days"], "C.45:15-16.57(b).")]},
    ],
    "traps": [
        "Source of lawful income is the New Jersey class most likely to be tested.",
        "Guaranty fund: $20,000 per TRANSACTION, not per claimant.",
        "Full Disclosure Act kicks in at 100 lots or more.",
        "Timeshare cancellation is seven days from the LATER of the two events.",
    ],
    "vocab": [
        ["NJLAD", "The New Jersey Law Against Discrimination."],
        ["Source of lawful income", "Vouchers, benefits and other lawful rent money."],
        ["Public offering statement", "The disclosure document for subdivisions and timeshares."],
        ["Subdivider", "The person disposing of subdivided lands."],
    ],
    "examples": [],
}

STUDY["nj/commission"] = {
    "summary": "Two items. Know what the Commission can do to a licence and what the fines are.",
    "sections": [
        {"h": "Investigations (R.S.45:15-17)",
         "l": ["The Commission MAY investigate on its OWN MOTION and MUST investigate on the VERIFIED WRITTEN COMPLAINT of any person - including against someone acting as a licensee WITHOUT A LICENCE.",
               "A lapse, suspension or VOLUNTARY SURRENDER of a licence does NOT deprive the Commission of jurisdiction, provided the charges arose while the person was licensed.",
               "EACH TRANSACTION IS A SEPARATE OFFENCE.",
               "The Commission may take depositions, require written statements under oath, SUBPOENA witnesses, compel attendance, take evidence and require production of any relevant material, including all of a licensee's records. Failure to obey a subpoena or to answer questions may be construed as CONDUCT DEMONSTRATING UNWORTHINESS, and the Commission may apply to the SUPERIOR COURT for an order compelling compliance."],
         "check": [("The Commission must investigate when:", "It receives a verified written complaint", ["Only on its own motion", "Only after a court refers a case"], "R.S.45:15-17."),
                   ("Surrendering a licence after the conduct:", "Does not deprive the Commission of jurisdiction", ["Ends the case", "Halves the penalty"], "R.S.45:15-17."),
                   ("For penalty purposes, each transaction is:", "A separate offence", ["Part of one course of conduct", "Counted only once per year"], "R.S.45:15-17."),
                   ("Refusing to answer the Commission's questions may be treated as:", "Conduct demonstrating unworthiness", ["A civil contempt only", "No violation at all"], "R.S.45:15-17.")]},
        {"h": "Sanctions",
         "l": ["The Commission may place a licensee on PROBATION, SUSPEND for a period less than the unexpired portion of the licence period, or REVOKE the licence - or the RIGHT OF LICENSURE where the person no longer holds a licence at the time of hearing.",
               "In addition or as an alternative it may impose a penalty of NOT MORE THAN $5,000 FOR A FIRST VIOLATION and NOT MORE THAN $10,000 FOR ANY SUBSEQUENT VIOLATION, recovered in the Commission's name by summary proceedings under the Penalty Enforcement Law of 1999.",
               "On a THIRD VIOLATION of the section - whether of the same provision or of separate provisions - the Commission may deem the person a REPEAT OFFENDER and direct that NO LICENCE SHALL HENCEFORTH BE ISSUED to them.",
               "The Commission is expressly vested with power to make and enforce rules for the conduct of the real estate brokerage business, and violating those rules is itself a ground for discipline (subsection t.)."],
         "check": [("The maximum penalty for a first violation is:", "$5,000", ["$1,000", "$10,000", "$25,000"], "R.S.45:15-17."),
                   ("For any subsequent violation the maximum is:", "$10,000", ["$5,000", "$20,000"], "R.S.45:15-17."),
                   ("On a third violation the Commission may:", "Deem the person a repeat offender and bar any future licence", ["Only double the fine", "Suspend for 6 months"], "R.S.45:15-17."),
                   ("A suspension imposed by the Commission must be:", "For a period less than the unexpired portion of the licence period", ["At least one year", "Permanent"], "R.S.45:15-17.")]},
    ],
    "traps": [
        "$5,000 first, $10,000 subsequent. Three violations can bar you for good.",
        "Surrendering the licence does not stop the case.",
    ],
    "vocab": [
        ["Verified complaint", "A sworn written complaint that forces an investigation."],
        ["Right of licensure", "What the Commission revokes when the licence has already lapsed."],
        ["Repeat offender", "A third-violation finding barring future licensure."],
    ],
    "examples": [],
}


# ------------------------------------------------------------- questions

Q = [
 # activities - agency
 ("nj/activities", "Agency default", 1, "A New Jersey brokerage firm performing brokerage services for a buyer is, by default:",
  "A buyer's agent", ["A subagent of the seller", "A transaction broker", "A disclosed dual agent"],
  "C.45:15-16.88(a), from P.L.2024, c.32."),
 ("nj/activities", "Agency default", 1, "A firm performing brokerage services for a seller is, by default:",
  "A seller's agent", ["A transaction broker", "A dual agent", "An unrepresented party"],
  "C.45:15-16.90(a)."),
 ("nj/activities", "Brokerage agreement", 1, "A written brokerage services agreement with a buyer is required:",
  "In a residential transaction, before or as soon as reasonably practical after services begin", ["In every transaction without exception", "Only when an offer is written", "Never"],
  "C.45:15-16.88(b)(1)."),
 ("nj/activities", "Brokerage agreement", 2, "A buyer in a commercial real estate transaction:",
  "Does not need a brokerage services agreement with the firm", ["Must sign one before any showing", "Must file one with the Commission"],
  "C.45:15-16.88(b)(1)."),
 ("nj/activities", "Brokerage agreement", 2, "The brokerage services agreement must state whether the agency relationship is:",
  "Exclusive or nonexclusive", ["Full service or limited service", "Written or oral"],
  "C.45:15-16.88(b)(2)(c)."),
 ("nj/activities", "Brokerage agreement", 3, "Consent to disclosed dual agency or designated agency must be shown by:",
  "Separate initialling or signature, with an acknowledgment that a dual agent will not advocate terms favouring one principal", ["A verbal agreement witnessed by the broker", "A clause in the listing only"],
  "C.45:15-16.88(b)(2)(d)."),
 ("nj/activities", "Duties", 1, "Written offers and counteroffers must be presented:",
  "In a timely manner even where the property is already under contract, unless the principal directs otherwise in writing", ["Only until a contract is signed", "Only if above the asking price", "At the agent's discretion"],
  "C.45:15-16.87(d)."),
 ("nj/activities", "Duties", 2, "The statutory duties owed by a New Jersey brokerage firm to its principal:",
  "May not be waived", ["May be waived in writing", "May be waived in commercial deals only"],
  "C.45:15-16.87."),
 ("nj/activities", "Duties", 2, "A party the firm serves must receive the consumer information statement:",
  "No later than when they sign the brokerage services agreement", ["At the first showing only", "At closing", "Within 7 days of an offer"],
  "C.45:15-16.87(h)(1)."),
 ("nj/activities", "Duties", 2, "A party NOT represented by any firm must receive the consumer information statement:",
  "Before signing an offer, or as soon as reasonably practical after", ["Never", "Only on written request"],
  "C.45:15-16.87(h)(2)."),
 ("nj/activities", "Duties", 3, "The firm's capacity must be disclosed in writing in a paragraph titled:",
  "Agency Disclosure", ["Notice to Consumer", "Material Facts", "Statement of Relationship"],
  "C.45:15-16.87(i)(1)."),
 ("nj/activities", "Duties", 2, "Where the principal is a residential seller, the firm must obtain:",
  "A signed property condition disclosure statement", ["A title commitment", "A home warranty", "A survey"],
  "C.45:15-16.87(e), referring to C.56:8-19.1."),
 ("nj/activities", "Transaction broker", 1, "A New Jersey transaction broker:",
  "Represents no party and is not required to keep any information confidential", ["Is a form of dual agent", "Owes fiduciary duties to the buyer", "Represents whoever pays"],
  "C.45:15-16.94(a)."),
 ("nj/activities", "Transaction broker", 2, "A transaction broker must work toward an agreement:",
  "Without advising any party how to gain an advantage at the other's expense", ["By advocating for the seller", "By advocating for whoever signed first"],
  "C.45:15-16.94(b)(7)."),
 ("nj/activities", "Dual agency", 1, "A disclosed dual agent may act only with:",
  "The informed consent of both parties, in their signed brokerage services agreements", ["The broker's written approval", "An oral consent at the showing"],
  "C.45:15-16.92(a)."),
 ("nj/activities", "Dual agency", 2, "A disclosed dual agent's duty of confidentiality:",
  "Covers both parties and survives termination of the relationship", ["Covers the seller only", "Ends at closing"],
  "C.45:15-16.92(b)(4)."),
 ("nj/activities", "Buyer agent", 2, "A buyer's agent who shows the same property to other prospective buyers:",
  "Does not breach the duty of loyalty", ["Breaches loyalty", "Must get written consent first"],
  "C.45:15-16.89(b)(1)."),
 ("nj/activities", "Buyer agent", 3, "A buyer's agent's duty not to disclose confidential information:",
  "Survives termination of the agency relationship", ["Ends when the agreement expires", "Ends at closing"],
  "C.45:15-16.89(a)(4)."),
 ("nj/activities", "Open house", 1, "At a residential showing generally open to the public, the required sign must be posted:",
  "At the entrance or at the sign-in sheet", ["In the kitchen", "On the street", "In the listing"],
  "C.45:15-16.99(a)."),
 ("nj/activities", "Open house", 2, "The open house sign tells prospective buyers that what they say to the agent is:",
  "Not confidential and could be disclosed to the seller", ["Confidential", "Privileged", "Covered by the listing agreement"],
  "C.45:15-16.99(b)."),
 ("nj/activities", "Open house", 3, "A buyer already exclusively represented by a buyer's agent must:",
  "Disclose that representation on the sign-in sheet", ["Leave the open house", "Bring their agent", "Say nothing"],
  "C.45:15-16.99(b)."),
 # activities - money and conduct
 ("nj/activities", "Commissions", 1, "A New Jersey salesperson may accept a commission from:",
  "Their employing or contracting broker only", ["The seller directly", "Any licensed broker", "The closing agent"],
  "R.S.45:15-16(a); 45:15-17(m)."),
 ("nj/activities", "Rebates", 2, "A New Jersey broker may rebate part of the commission to:",
  "A purchaser of residential real property, and no other third party", ["Any unlicensed referrer", "The seller's attorney", "A relocation consultant"],
  "R.S.45:15-17(k)(2)."),
 ("nj/activities", "Rebates", 3, "That rebate is paid:",
  "At the time of closing, as a credit reducing the commission or a cheque from the closing agent", ["In cash at signing", "Within 30 days after closing"],
  "R.S.45:15-17(k)(2)."),
 ("nj/activities", "Rebates", 3, "Before paying a rebate the broker must also:",
  "Recommend the purchaser contact a tax professional", ["Notify the Commission", "Obtain the seller's consent"],
  "R.S.45:15-17(k)(2)."),
 ("nj/activities", "Inducements", 2, "A promotional benefit requiring written disclosure to the recipient is one conferring more than:",
  "$1,000", ["$100", "$500", "$5,000"],
  "R.S.45:15-17(g)."),
 ("nj/activities", "Trust money", 1, "Money a New Jersey broker receives belonging to others must be:",
  "Deposited in a special account separate and apart from personal or other business accounts", ["Held in the broker's operating account", "Kept by the salesperson until closing"],
  "R.S.45:15-17(o)."),
 ("nj/activities", "Trust money", 2, "Failing to account for or pay over money belonging to others is:",
  "A ground for suspension or revocation", ["A civil matter only", "Permitted pending a dispute"],
  "R.S.45:15-17(d)."),
 ("nj/activities", "Listings", 1, "A New Jersey listing contract must:",
  "State a definite terminal date not subject to qualifying terms or conditions", ["Run for at least 90 days", "Renew automatically"],
  "R.S.45:15-17(f)."),
 ("nj/activities", "Listings", 2, "The client must receive a fully executed copy of the listing contract:",
  "At the time of execution", ["Within 5 business days", "At closing"],
  "R.S.45:15-17(f)."),
 ("nj/activities", "Conflicts", 2, "A licensee selling property in which they have an interest must disclose that interest and their licence status:",
  "In the contract of sale", ["At the closing table", "In the MLS only", "Only if asked"],
  "R.S.45:15-17(p)."),
 ("nj/activities", "Conflicts", 2, "Acting for more than one party without the knowledge of all parties is:",
  "A ground for discipline", ["Permitted dual agency", "Allowed in commercial deals"],
  "R.S.45:15-17(b)."),
 ("nj/activities", "Conduct", 2, "A licensee convicted of a disorderly persons offence must notify the Commission within:",
  "30 days", ["90 days", "At the next renewal", "Only if sentenced to jail"],
  "R.S.45:15-17(s)."),
 ("nj/activities", "Conduct", 3, "Promoting the sale of real estate by means of a prize drawing is:",
  "A ground for discipline", ["Permitted with written disclosure", "Permitted for new construction"],
  "R.S.45:15-17(g)."),
 ("nj/activities", "Transfer fee", 1, "Who pays the New Jersey realty transfer fee?",
  "The grantor, when the deed is offered for recording", ["The grantee at closing", "The lender", "The listing broker"],
  "N.J.S.A. 46:15-7(a)."),
 ("nj/activities", "Transfer fee", 3, "The general purpose portion of the realty transfer fee is not imposed where the total consideration:",
  "Does not exceed $350,000", ["Does not exceed $150,000", "Exceeds $1,000,000", "Is paid in cash"],
  "N.J.S.A. 46:15-7(a)(3)(a)."),
 ("nj/activities", "Transfer fee", 3, "If the consideration is misstated on a recorded deed:",
  "The title conveyed is not impaired, but the fee remains owed", ["The deed is void", "The title becomes unmarketable"],
  "N.J.S.A. 46:15-7(b)."),
 ("nj/activities", "Security deposits", 1, "A New Jersey security deposit:",
  "Remains the tenant's property, is held in trust, and may not be mingled with the landlord's property", ["Becomes the landlord's on receipt", "May be used for operating expenses"],
  "N.J.S.A. 46:8-19."),
 ("nj/activities", "Truth in Renting", 2, "The Truth in Renting Act's definition of landlord excludes:",
  "Premises of not more than two dwelling units, and owner-occupied premises of not more than three", ["All single-family rentals", "Any building under ten units"],
  "N.J.S.A. 46:8-44(a)."),
 ("nj/activities", "Truth in Renting", 3, "The statement of legal rights and responsibilities must be printed in:",
  "English and Spanish", ["English only", "Any language the tenant requests"],
  "N.J.S.A. 46:8-45(a)."),
 ("nj/activities", "Other laws", 3, "Which appears on the New Jersey outline as a land use statute?",
  "The Pinelands Protection Act of 1979", ["The Coastal Zone Act of 1965", "The Highlands Act of 1965"],
  "PSI New Jersey state outline, Other Laws and Regulations."),

 # licensing
 ("nj/licensing", "Education", 1, "Prelicensure education for a New Jersey salesperson is:",
  "75 hours", ["150 hours", "60 hours", "90 hours"],
  "R.S.45:15-10.1(a)."),
 ("nj/licensing", "Education", 2, "The salesperson's 75 hours must include at least:",
  "3 hours of ethics and 1 hour of fair housing", ["6 hours of ethics", "4 hours of fair housing", "No specified subjects"],
  "R.S.45:15-10.1(a)."),
 ("nj/licensing", "Education", 2, "A New Jersey broker candidate must complete:",
  "150 hours, including 30 hours of ethics", ["75 hours", "120 hours including 10 of ethics", "90 hours"],
  "R.S.45:15-10.1(b)."),
 ("nj/licensing", "Continuing education", 1, "Continuing education in New Jersey is:",
  "12 credit hours per cycle", ["18 hours", "6 hours", "24 hours"],
  "NJREC published breakdown of required CE hours."),
 ("nj/licensing", "Continuing education", 2, "Of those 12 hours, the required subjects are:",
  "1 fair housing and NJLAD, 1 agency, 2 ethics and 2 any core", ["3 ethics and 3 agency", "2 fair housing and 2 contracts"],
  "NJREC published breakdown of required CE hours."),
 ("nj/licensing", "Continuing education", 3, "May an elective course be used in place of the required fair housing hour?",
  "No; fair housing may substitute for core and electives, but not the reverse", ["Yes, freely", "Yes, with Commission approval"],
  "NJREC published breakdown of required CE hours."),
 ("nj/licensing", "Qualifying", 1, "The minimum age for a New Jersey real estate licence is:",
  "18", ["17", "19", "21"],
  "R.S.45:15-9(a)."),
 ("nj/licensing", "Qualifying", 2, "Every New Jersey applicant must have:",
  "The equivalent of a high school education", ["A college degree", "Two years of sales experience", "No educational minimum"],
  "R.S.45:15-9(a)."),
 ("nj/licensing", "Qualifying", 2, "A broker applicant must have been actively engaged full time as a New Jersey salesperson for:",
  "Three years immediately preceding the application", ["One year", "Five years", "Six months"],
  "R.S.45:15-9(a); the Commission may waive it for an out-of-state broker of three years."),
 ("nj/licensing", "Qualifying", 3, "The cost of the criminal history record background check is borne by:",
  "The applicant", ["The employing broker", "The Commission", "The State Police"],
  "R.S.45:15-9(a)."),
 ("nj/licensing", "Offices", 1, "Each New Jersey branch office must be under the direct supervision of:",
  "A broker-salesperson", ["Any licensed salesperson", "The main office broker by telephone"],
  "R.S.45:15-12."),
 ("nj/licensing", "Offices", 2, "Every place of business must display conspicuously on the exterior:",
  "The authorised name and the words Licensed Real Estate Broker", ["The licence number", "The office hours", "The Commission's seal"],
  "R.S.45:15-12."),
 ("nj/licensing", "Offices", 3, "The broker's designated main office is:",
  "The business address of all licensed persons in the broker's employ", ["Only the broker's own address", "Optional if a branch exists"],
  "R.S.45:15-12."),

 # additional
 ("nj/additional", "NJLAD", 1, "Which is protected in New Jersey housing but not by the federal Fair Housing Act?",
  "Source of lawful income used for rental or mortgage payments", ["Race", "Color", "National origin"],
  "N.J.S.A. 10:5-12(h)(1)."),
 ("nj/additional", "NJLAD", 1, "New Jersey also protects, in housing:",
  "Civil union status and domestic partnership status", ["Credit score", "Employment history", "Length of residence"],
  "N.J.S.A. 10:5-12(h)(1)."),
 ("nj/additional", "NJLAD", 2, "A landlord applying a minimum income test to a voucher holder must base it on:",
  "Only the portion of the rent the tenant actually pays", ["The full contract rent", "Three times the market rent"],
  "N.J.S.A. 10:5-12(g)(4)."),
 ("nj/additional", "NJLAD", 2, "Refusing to rent to a family with children under 18 is lawful only for:",
  "Housing for older persons as defined in the act", ["Owner-occupied buildings", "Studio apartments", "Any two-family house"],
  "N.J.S.A. 10:5-12(g)(5)."),
 ("nj/additional", "NJLAD", 3, "A discriminatory advertisement is treated as:",
  "Presumptive evidence that the person named authorised it", ["Inadmissible unless signed", "Actionable only with a refusal"],
  "N.J.S.A. 10:5-12(g)(3)."),
 ("nj/additional", "Guaranty fund", 1, "The Real Estate Guaranty Fund compensates a person harmed by:",
  "Embezzlement, conversion or unlawful obtaining of money in a brokerage transaction", ["A bad home inspection", "A declined mortgage", "A low appraisal"],
  "C.45:15-34."),
 ("nj/additional", "Guaranty fund", 1, "The maximum recovery from the fund is:",
  "$20,000 in the aggregate per transaction", ["$10,000 per claimant", "$50,000 per transaction", "Unlimited"],
  "C.45:15-34, as amended by P.L.1993, c.51."),
 ("nj/additional", "Guaranty fund", 3, "The fund is maintained by:",
  "The State Treasurer, and administered by the Commission", ["A private insurer", "The Commission's own bank", "The Attorney General"],
  "C.45:15-34."),
 ("nj/additional", "Full Disclosure Act", 1, "The Real Estate Sales Full Disclosure Act does not apply to a subdivision of:",
  "Fewer than 100 lots, parcels, units or interests", ["Fewer than 10 lots", "Fewer than 25 lots", "Fewer than 50 lots"],
  "C.45:15-16.32(a)(6)."),
 ("nj/additional", "Full Disclosure Act", 2, "Before disposing of an interest in subdivided lands the seller must:",
  "Deliver a current public offering statement and allow a reasonable opportunity to examine it", ["Record a plat", "Post a bond", "Obtain a county permit"],
  "C.45:15-16.30(b)."),
 ("nj/additional", "Full Disclosure Act", 3, "A development made up wholly of rental units is exempt because:",
  "The relationship created is one of landlord and tenant", ["Rentals are federally regulated", "No consideration changes hands"],
  "C.45:15-16.32(a)(8)."),
 ("nj/additional", "Timeshares", 1, "A New Jersey timeshare purchaser may cancel within:",
  "Seven days of receiving the public offering statement or executing the contract, whichever is later", ["Three days", "Ten business days", "Thirty days"],
  "C.45:15-16.59(b)(10)."),
 ("nj/additional", "Timeshares", 2, "A violation committed by a timeshare developer's marketing entity is:",
  "A violation by the developer as well", ["The entity's alone", "Not actionable in New Jersey"],
  "C.45:15-16.58."),
 ("nj/additional", "Timeshares", 3, "A preliminary timeshare registration runs for:",
  "90 days, extendable while a complete application is pursued", ["One year", "30 days", "Indefinitely"],
  "C.45:15-16.57(b)."),

 # commission
 ("nj/commission", "Investigations", 1, "The New Jersey Real Estate Commission must investigate when:",
  "It receives a verified written complaint from any person", ["It chooses to", "A court refers a case", "A broker requests it"],
  "R.S.45:15-17."),
 ("nj/commission", "Investigations", 2, "Voluntarily surrendering a licence after the conduct complained of:",
  "Does not deprive the Commission of jurisdiction", ["Ends the proceeding", "Reduces the penalty by half"],
  "R.S.45:15-17."),
 ("nj/commission", "Investigations", 2, "For penalty purposes each transaction is treated as:",
  "A separate offence", ["Part of a single course of conduct", "One offence per licensee per year"],
  "R.S.45:15-17."),
 ("nj/commission", "Investigations", 3, "Refusing to answer the Commission's questions in an investigation may be construed as:",
  "Conduct demonstrating unworthiness", ["Civil contempt only", "No violation"],
  "R.S.45:15-17(e)."),
 ("nj/commission", "Sanctions", 1, "The maximum monetary penalty for a first violation is:",
  "$5,000", ["$1,000", "$10,000", "$25,000"],
  "R.S.45:15-17."),
 ("nj/commission", "Sanctions", 1, "For any subsequent violation the maximum penalty is:",
  "$10,000", ["$5,000", "$20,000", "$50,000"],
  "R.S.45:15-17."),
 ("nj/commission", "Sanctions", 2, "On a third violation the Commission may:",
  "Deem the person a repeat offender and direct that no licence be issued to them again", ["Only double the fine", "Suspend the licence for six months"],
  "R.S.45:15-17."),
 ("nj/commission", "Sanctions", 3, "A suspension imposed by the Commission must be for a period:",
  "Less than the unexpired portion of the licence period", ["Of at least one year", "Fixed at six months"],
  "R.S.45:15-17."),
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
            "id": "nj-" + hashlib.sha1(q.encode()).hexdigest()[:8],
            "portion": "georgia", "topic": topic, "subtopic": sub,
            "sub": topic + "|" + sub, "concept": "New Jersey " + sub.lower(),
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
        "code": "NJ", "name": "New Jersey", "abbr": "NJ",
        "regulator": "New Jersey Real Estate Commission",
        "pass": EXAM["pass"], "single": True,
        "portions": {
            "national": {"name": "General practice",
                         "scored": EXAM["national_scored"],
                         "minutes": EXAM["national_minutes"],
                         "blurb": "Principles, practice and the maths, as New Jersey tests them."},
            "georgia": {"name": "New Jersey law", "scored": EXAM["state_scored"],
                        "minutes": EXAM["state_minutes"],
                        "blurb": "R.S.45:15, the 2024 agency act, the Law Against Discrimination and the other named statutes."},
        },
        "topics": topics, "bank": bank, "study": study,
        "sources": SOURCES, "diffs": DIFFS,
    }


# Where New Jersey departs from the national rule.
DIFFS = {
    "national/agency": [
        "P.L.2024, c.32 rebuilt New Jersey agency. A firm working with a BUYER is a BUYER'S AGENT by default, and a residential buyer needs a written BROKERAGE SERVICES AGREEMENT (C.45:15-16.88).",
        "A TRANSACTION BROKER represents nobody and is NOT required to keep any information confidential - the opposite of the dual agent, who keeps both sides' confidences (C.45:15-16.92, 16.94).",
        "The statutory duties, including presenting written offers even when the property is under contract, MAY NOT BE WAIVED (C.45:15-16.87).",
        "Every public open house needs a posted sign, in statutory wording, warning buyers that nothing they say is confidential (C.45:15-16.99).",
    ],
    "national/practice": [
        "A salesperson may be paid ONLY by their employing or contracting broker, and rebates may go to a residential PURCHASER but to no other unlicensed person (R.S.45:15-16, 45:15-17(k)).",
        "Listings must carry a DEFINITE TERMINAL DATE with no qualifying conditions, and the client gets a fully executed copy at signing (R.S.45:15-17(f)).",
        "Discipline runs to $5,000 for a first violation and $10,000 after; a third violation can bar licensure for good (R.S.45:15-17).",
        "The REAL ESTATE GUARANTY FUND pays up to $20,000 per transaction for a licensee's embezzlement or conversion (C.45:15-34).",
        "Education: 75 hours for a salesperson, 150 for a broker, then 12 hours of continuing education a cycle.",
    ],
    "national/disclosures": [
        "The Law Against Discrimination adds SOURCE OF LAWFUL INCOME, civil union and domestic partnership status, pregnancy or breastfeeding, gender identity or expression and liability for military service to the federal classes (N.J.S.A. 10:5-12).",
        "A residential seller's agent must obtain a SIGNED PROPERTY CONDITION DISCLOSURE STATEMENT (C.45:15-16.87(e)).",
        "Subdivisions of 100 lots or more need a PUBLIC OFFERING STATEMENT delivered before disposition (C.45:15-16.30, 16.32).",
    ],
}


if __name__ == "__main__":
    import io, json, os
    here = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    out = os.path.join(here, "greprep", "packs", "NJ.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    pack = build()
    with io.open(out, "w", encoding="utf-8") as f:
        json.dump(pack, f, ensure_ascii=False, indent=1, sort_keys=True)
    print("wrote", out, len(pack["bank"]), "questions,", len(pack["study"]), "lessons")
