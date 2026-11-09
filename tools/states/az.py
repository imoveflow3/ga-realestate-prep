"""Arizona state content: lessons and practice questions.

Arizona splits the examination 80 national + 60 state, and needs 75% on
each. The handbook is unusually plain about what that means: the score is
reported as a percent on a 0-100% scale and IS the percentage of questions
answered correctly. No scaled-score caveat here.

The eleven state categories and their item counts below are Pearson VUE's
published Arizona Salesperson outline, effective 1 January 2026.

Every rule below was read from the official text on 2026-11-09:
  - Arizona Revised Statutes title 32 chapter 20 (the real estate licence
    law) and title 33 (homestead, anti-deficiency), from azleg.gov.
  - The Pearson VUE Arizona Candidate Handbook and Content Outlines
    (#090300, #090301), for the blueprint, the pass mark and the
    education requirements.
The section a fact comes from is cited next to it. Do not add a fact here
without reading its source first.
"""

EXAM = {
    # Pearson: 80 scored national (+5 pretest), 60 scored state (+5
    # pretest), 75% on each, reported as percent correct.
    "state_scored": 60,
    "state_minutes": 90,
    "national_scored": 80,
    "national_minutes": 120,
    "pass": 0.75,
}

# Pearson's published Arizona Salesperson state outline, 1 January 2026.
TOPICS = [
    ("az/contracts", "Contracts", 8,
     "Employment agreements, purchase contracts, closing and costs."),
    ("az/agency", "Arizona agency", 6,
     "Types, creation, Arizona case law on clients and customers, termination."),
    ("az/duties", "Licensee duties & obligations", 6,
     "Disclosure, conflicts, compensation, timing, cross-sale disputes."),
    ("az/competency", "Competencies & property types", 6,
     "Professional competency, new homes, property management, timeshare, land."),
    ("az/skill-care", "Reasonable skill & care", 6,
     "The licensee's obligation, property taxes, utilities and environment."),
    ("az/regulatory", "Regulatory framework", 5,
     "The Department, its powers, licensing, and the Recovery Fund."),
    ("az/consumer", "Consumer protection laws", 5,
     "Consumer Fraud Act, statute of frauds, fair housing, homestead."),
    ("az/advertising", "Advertising", 5,
     "Licensee advertising, promotions, development ads, supervision."),
    ("az/services", "Critical business services", 5,
     "Escrow, title insurance and lending in an Arizona transaction."),
    ("az/ownership", "Ownership & encumbrances", 5,
     "Ownership, liens, deeds, HOAs, easements."),
    ("az/foreclosure", "Foreclosure & short sale", 3,
     "The Arizona anti-deficiency statute and the foreclosure process."),
]

SOURCES = [
    {"by": "Arizona Legislature",
     "name": "Arizona Revised Statutes title 32, chapter 20",
     "note": "The real estate licence law: the Department, licensing, broker records, discipline and the Recovery Fund.",
     "url": "https://www.azleg.gov/arsDetail/?title=32"},
    {"by": "Arizona Legislature",
     "name": "Arizona Revised Statutes title 33",
     "note": "The homestead exemption and the anti-deficiency statutes for mortgages and deeds of trust.",
     "url": "https://www.azleg.gov/arsDetail/?title=33"},
    {"by": "Pearson VUE and the Arizona Department of Real Estate",
     "name": "Arizona Candidate Handbook and Content Outlines",
     "note": "The blueprint: 80 national and 60 state scored items, 75% on each as a percentage of items correct, and the eleven state categories.",
     "url": "https://www.pearsonvue.com/us/en/az/realestate.html"},
]


# --------------------------------------------------------------- lessons

STUDY = {}

STUDY["az/regulatory"] = {
    "summary": "Five items on who runs real estate in Arizona and the fund that pays when a licensee wrongs someone. The two numbers to hold are $30,000 and $90,000.",
    "sections": [
        {"h": "The Department and the Commissioner",
         "l": ["The ARIZONA DEPARTMENT OF REAL ESTATE (ADRE) administers title 32, chapter 20, headed by the REAL ESTATE COMMISSIONER.",
               "The Commissioner issues licences, approves schools and courses, adopts the Commissioner's Rules, and disciplines licensees.",
               "Arizona real estate law sits in ARS title 32 chapter 20, the Commissioner's Rules, and - distinctively - ARTICLE XXVI of the ARIZONA CONSTITUTION, which lets licensed brokers and salespersons draft the documents incident to a transaction they handle."],
         "check": [("Arizona's real estate regulator is headed by:", "The Real Estate Commissioner", ["A nine-member commission", "The Attorney General"], "ADRE is headed by the Commissioner."),
                   ("Which part of the Arizona Constitution concerns real estate licensees?", "Article XXVI", ["Article II", "Article IX"], "It is the first heading on the state exam outline.")]},
        {"h": "The Real Estate Recovery Fund (ARS 32-2186)",
         "l": ["The Commissioner maintains the fund for a person aggrieved by an act, representation, transaction or conduct of a licensee.",
               "The fund's liability may not exceed $30,000 FOR EACH TRANSACTION, regardless of the number of persons aggrieved, licensees, or parcels involved.",
               "It may not exceed $90,000 FOR EACH LICENSEE. Once orders authorise that aggregate, the fund's liability for that licensee ends.",
               "A LICENSEE acting as principal or agent has NO CLAIM against the fund - nor do marital communities, corporations, LLCs or partnerships in which the licensee is a principal, member, partner, officer or director, or holds at least a 10 PER CENT direct or indirect interest.",
               "The fund pays only against the licence of a NATURAL PERSON, never a corporation, partnership or other entity."],
         "check": [("The Arizona Recovery Fund pays at most, per transaction:", "$30,000", ["$20,000", "$50,000", "$90,000"], "ARS 32-2186(B)(1)."),
                   ("The aggregate limit for each licensee is:", "$90,000", ["$30,000", "$60,000", "$150,000"], "ARS 32-2186(B)(2)."),
                   ("A licensee who loses money in a transaction may claim against the fund:", "No - licensees have no claim", ["Yes, like any consumer", "Yes, up to half"], "ARS 32-2186(D)."),
                   ("The fund pays against the licence of:", "A natural person only", ["A corporation", "A partnership", "Any licensed entity"], "ARS 32-2186(E).")]},
        {"h": "Broker records (ARS 32-2151.01)",
         "l": ["An employing broker keeps records of ALL transactions handled by or through the broker, and employment records for all current and former employees.",
               "Records include earnest money receipts confirming the money was handled as the transaction required, closing statements showing receipts, disbursements and adjustments, sales contracts, and employment agreements where applicable.",
               "Records are kept at least FIVE YEARS after the transaction or employment ends.",
               "They are kept at the employing broker's principal or licensed branch office in Arizona, or at an off-site Arizona storage location if the broker has given the Department prior WRITTEN notice of the street address.",
               "Records are open at all reasonable times for inspection by the Commissioner."],
         "check": [("Arizona broker records must be kept for at least:", "Five years after the transaction or employment ends", ["Three years", "Seven years"], "ARS 32-2151.01(A)."),
                   ("Off-site record storage requires:", "Prior written notice to the Department of the street address", ["Nothing", "Commissioner approval by order"], "ARS 32-2151.01(A).")]},
    ],
    "traps": [
        "$30,000 per transaction, $90,000 per licensee. Both appear as answer options.",
        "Licensees - and entities they substantially own - cannot claim on the fund.",
        "Five years for broker records, and off-site storage needs prior written notice.",
    ],
    "vocab": [
        ["ADRE", "Arizona Department of Real Estate."],
        ["Commissioner", "The head of ADRE who licenses and disciplines."],
        ["Recovery Fund", "The fund paying people wronged by a licensee."],
        ["Employing broker", "The broker who holds the records and employs the licensees."],
        ["Article XXVI", "The Arizona constitutional provision on licensees drafting documents."],
    ],
    "examples": [
        {"t": "Two victims, one deal",
         "s": "Two buyers are defrauded by the same salesperson in a single transaction.",
         "w": ["The per-transaction cap is $30,000 regardless of how many were wronged.",
               "The per-licensee aggregate is $90,000 across all transactions."],
         "k": "They share $30,000 for that transaction."},
    ],
}

STUDY["az/agency"] = {
    "summary": "Six items. Arizona's rule is short: acting for more than one party without the knowledge or WRITTEN CONSENT of all parties is a ground for discipline.",
    "sections": [
        {"h": "Dual representation (ARS 32-2153(A)(2))",
         "p": ["A licence may be denied, suspended or revoked where a licensee has ACTED FOR MORE THAN ONE PARTY IN A TRANSACTION WITHOUT THE KNOWLEDGE OR WRITTEN CONSENT OF ALL PARTIES. So dual representation is permitted in Arizona, but only with everyone knowing and consenting in writing."],
         "check": [("Acting for both parties in Arizona requires:", "The knowledge and written consent of all parties", ["Verbal consent", "Broker approval only", "Nothing; it is prohibited"], "ARS 32-2153(A)(2)."),
                   ("Dual representation in Arizona is:", "Allowed with written consent of all parties", ["Prohibited outright", "Allowed only in commercial deals"], "ARS 32-2153(A)(2).")]},
        {"h": "Representing the right broker",
         "l": ["A salesperson or associate broker may not REPRESENT OR ATTEMPT TO REPRESENT a broker other than the one they are licensed to (ARS 32-2153(A)(8)).",
               "A broker may not employ an UNLICENSED salesperson or associate broker (32-2153(A)(6)).",
               "A licensee may accept compensation only from a person authorised to pay it under ARS 32-2155 (32-2153(A)(7)).",
               "Paying or receiving a REBATE, profit, compensation or commission in violation of the chapter is a ground for discipline (32-2153(A)(10))."],
         "check": [("An Arizona salesperson may accept compensation from:", "Only a person authorised under ARS 32-2155", ["Any party to the deal", "The buyer directly"], "ARS 32-2153(A)(7)."),
                   ("Representing a broker other than the one you are licensed to is:", "A ground for discipline", ["Allowed with disclosure", "Allowed for one transaction"], "ARS 32-2153(A)(8).")]},
        {"h": "Accounting and documents",
         "p": ["Failing, WITHIN A REASONABLE TIME, to account for or remit money, or to surrender to the rightful owner documents or other valuable property belonging to others that came into the licensee's possession, is a ground for discipline (ARS 32-2153(A)(9)). The same provision covers issuing an appraisal report on property in which the licensee has an interest without fully disclosing the nature and extent of that interest."],
         "check": [("A licensee holding money belonging to another must account for it:", "Within a reasonable time", ["Within 24 hours", "At closing only"], "ARS 32-2153(A)(9)."),
                   ("An appraisal report on property the licensee has an interest in must:", "Fully disclose the nature and extent of that interest", ["Be refused", "Be reviewed by the Commissioner"], "ARS 32-2153(A)(9).")]},
        {"h": "Trust money and withdrawals",
         "p": ["A broker may NOT grant anyone authority to withdraw money from the broker's TRUST FUND ACCOUNT unless the statute permits it (ARS 32-2151.01(B)). Trust money is the client's, and the employing broker answers for it."],
         "check": [("Authority to withdraw from a broker's trust fund account:", "Is restricted by statute", ["May be given to any employee", "Belongs to the salesperson who took the deposit"], "ARS 32-2151.01(B).")]},
    ],
    "traps": [
        "Arizona allows dual representation WITH written consent; it is not banned.",
        "Compensation must come through a person ARS 32-2155 authorises.",
        "'Within a reasonable time' is the accounting standard, not a fixed number of days.",
    ],
    "vocab": [
        ["Associate broker", "A broker working under an employing broker."],
        ["Employing broker", "The broker a licensee is licensed to."],
        ["Designated broker", "The broker responsible for a brokerage's compliance."],
        ["Trust fund account", "The account holding money belonging to others."],
    ],
    "examples": [],
}

STUDY["az/consumer"] = {
    "summary": "Five items. The Arizona-specific numbers here are the homestead exemption at $400,000 and the Consumer Fraud Act of 1967.",
    "sections": [
        {"h": "The homestead exemption (ARS 33-1101)",
         "l": ["Any person at least EIGHTEEN, married or single, residing in Arizona may hold a homestead EXEMPT FROM ATTACHMENT, EXECUTION AND FORCED SALE, not exceeding $400,000 IN VALUE.",
               "It may be the person's interest in real property in one compact body with a dwelling house in which they reside; a CONDOMINIUM or COOPERATIVE in which they reside; or a MOBILE HOME, park model trailer, motor home, travel trailer, fifth wheel, houseboat or manufactured home in which they reside, plus the land it sits on.",
               "The figure is adjusted annually, so treat $400,000 as the statutory base."],
         "check": [("The Arizona homestead exemption is:", "$400,000 in value", ["$150,000", "$250,000", "Unlimited"], "ARS 33-1101(A)."),
                   ("Which qualifies for the Arizona homestead exemption?", "A cooperative in which the person resides", ["A rental property", "A vacant lot", "A commercial building"], "ARS 33-1101(A)(2)."),
                   ("The homestead exemption protects against:", "Attachment, execution and forced sale", ["Property taxes", "A mortgage the owner signed"], "ARS 33-1101(A).")]},
        {"h": "Consumer Fraud and the statute of frauds",
         "l": ["The 1967 ARIZONA CONSUMER FRAUD PROTECTION ACT is named on the exam outline; it reaches deception, false promise and concealment in connection with the sale or advertisement of merchandise, which includes real estate.",
               "The STATUTE OF FRAUDS requires contracts for the sale of land, and leases longer than one year, to be in writing to be enforceable.",
               "ARIZONA FAIR HOUSING and ARIZONA HOMESTEAD LAWS complete this outline category."],
         "check": [("The Arizona Consumer Fraud Protection Act dates from:", "1967", ["1980", "1995", "2001"], "Named on the Arizona state content outline."),
                   ("Under the statute of frauds, which must be written?", "A contract for the sale of land", ["A one-month tenancy", "An oral price quote"], "Land contracts and leases over a year.")]},
    ],
    "traps": [
        "$400,000 homestead, adjusted annually.",
        "A mobile home plus its land can be the homestead.",
        "Homestead does not defeat a mortgage the owner signed or property taxes.",
    ],
    "vocab": [
        ["Homestead exemption", "Arizona's $400,000 protection from forced sale."],
        ["Consumer Fraud Act", "Arizona's 1967 deceptive practices statute."],
        ["Statute of frauds", "The rule that land contracts must be written."],
        ["Attachment", "A creditor's seizure of property to secure a claim."],
    ],
    "examples": [],
}

STUDY["az/foreclosure"] = {
    "summary": "Three items, and they turn on one Arizona rule: on a small home financed with purchase money, the lender takes the house and nothing more.",
    "sections": [
        {"h": "The anti-deficiency statute (ARS 33-729)",
         "p": ["Where a MORTGAGE secures the balance of the purchase price, or a loan to pay all or part of the purchase price, of a parcel of REAL PROPERTY OF TWO AND ONE-HALF ACRES OR LESS, LIMITED TO AND USED FOR A SINGLE ONE-FAMILY OR SINGLE TWO-FAMILY DWELLING, the judgment lien in a foreclosure action does NOT extend to the debtor's other property, no general execution may issue, and if the sale proceeds fall short the judgment may not otherwise be enforced."],
         "l": ["In short: no DEFICIENCY JUDGMENT on a qualifying small home bought with purchase money.",
               "The three tests are PURCHASE MONEY, 2.5 ACRES OR LESS, and a SINGLE ONE- OR TWO-FAMILY DWELLING actually used as such."],
         "check": [("Arizona's anti-deficiency protection covers parcels of:", "Two and one-half acres or less", ["Five acres or less", "Ten acres or less", "Any size"], "ARS 33-729(A)."),
                   ("The dwelling must be:", "A single one-family or single two-family dwelling", ["Any residential building", "A fourplex or smaller"], "ARS 33-729(A)."),
                   ("Where the statute applies, the lender:", "May not obtain a deficiency judgment", ["May pursue the borrower's other property", "May garnish wages"], "ARS 33-729(A).")]},
        {"h": "Deeds of trust (ARS 33-814)",
         "l": ["Arizona lenders normally use a DEED OF TRUST with a trustee's power of sale.",
               "After a trustee's sale, an action for a DEFICIENCY JUDGMENT must be brought within NINETY DAYS of the date of sale.",
               "The deficiency is the total owed the beneficiary as of the date of sale, less the property's value as the court determines.",
               "Subsections F, G and H carry the same anti-deficiency protection for qualifying small homes."],
         "check": [("After an Arizona trustee's sale, a deficiency action must be brought within:", "90 days of the sale", ["30 days", "6 months", "One year"], "ARS 33-814(A)."),
                   ("Arizona lenders normally secure loans with:", "A deed of trust with a power of sale", ["A mortgage foreclosed judicially", "A land contract"], "ARS 33-814.")]},
    ],
    "traps": [
        "2.5 acres, one- or two-family, purchase money. All three must hold.",
        "90 days after a trustee's sale to sue for a deficiency.",
        "Anti-deficiency protects the borrower; it does not cancel the debt before sale.",
    ],
    "vocab": [
        ["Anti-deficiency statute", "Arizona's bar on deficiency judgments for qualifying homes."],
        ["Deficiency judgment", "A judgment for the shortfall after a foreclosure sale."],
        ["Deed of trust", "Arizona's usual security instrument, with a trustee's power of sale."],
        ["Trustee's sale", "The non-judicial sale under a deed of trust."],
    ],
    "examples": [
        {"t": "The shortfall",
         "s": "A purchase-money loan on a 0.2-acre single-family home; the trustee's sale raises $60,000 less than the debt.",
         "w": ["Purchase money, under 2.5 acres, single one-family dwelling.",
               "All three conditions of the anti-deficiency statute are met."],
         "k": "No deficiency judgment. The lender takes the sale proceeds and nothing further."},
    ],
}

STUDY["az/advertising"] = {
    "summary": "Five items. The licence law's advertising ground for discipline is broad: knowingly putting out any materially false or misleading statement about the business or the property.",
    "sections": [
        {"h": "False or misleading advertising (ARS 32-2153(A)(4))",
         "p": ["A licence may be denied, suspended or revoked where a licensee KNOWINGLY authorised, directed, connived at or aided in the publication, advertisement, distribution or circulation of any MATERIALLY FALSE OR MISLEADING statement or representation concerning the licensee's business, or any land, cemetery property, subdivision, membership campground or camping contract offered for sale - IN THIS OR ANY OTHER STATE."],
         "check": [("False advertising is a ground for discipline where the licensee acted:", "Knowingly", ["Negligently only", "Regardless of knowledge"], "ARS 32-2153(A)(4)."),
                   ("The advertising ground reaches statements made:", "In this or any other state", ["Only in Arizona", "Only in print"], "ARS 32-2153(A)(4).")]},
        {"h": "Titles and supervision",
         "l": ["Knowingly using the term REAL ESTATE BROKER, cemetery broker or membership camping broker without the legal right to do so is a ground for discipline (ARS 32-2153(A)(5)).",
               "The state outline divides advertising into ADVERTISING BY A LICENSEE, PROMOTIONAL ACTIVITIES, DEVELOPMENT ADVERTISING and ADVERTISING SUPERVISION - the last putting responsibility on the broker for what the brokerage publishes.",
               "Pursuing a COURSE OF MISREPRESENTATION, or making false promises, directly or through others, is a ground for discipline whether acting as a licensee or as a PRINCIPAL in the transaction (32-2153(A)(1))."],
         "check": [("Misrepresentation is a ground for discipline:", "Whether the licensee acts as a licensee or as a principal", ["Only when acting for a client", "Only in listings"], "ARS 32-2153(A)(1)."),
                   ("Calling yourself a real estate broker without the right to do so is:", "A ground for discipline", ["A civil matter only", "Permitted if unpaid"], "ARS 32-2153(A)(5).")]},
    ],
    "traps": [
        "The advertising ground needs KNOWLEDGE; the misrepresentation ground reaches a course of conduct.",
        "Discipline follows a licensee even when they are the principal in their own deal.",
        "Advertising supervision is the broker's problem, not only the agent's.",
    ],
    "vocab": [
        ["Development advertising", "Advertising for a subdivision or development."],
        ["Connive at", "To knowingly allow or assist; used in the statute."],
        ["Material misstatement", "A false statement that matters to the decision."],
    ],
    "examples": [],
}

STUDY["az/duties"] = {
    "summary": "Six items on what a licensee must say and when. The outline puts disclosure obligations, conflicts, compensation and timing together, and adds the Arizona oddity of a dispute between cross-sale agents.",
    "sections": [
        {"h": "What must be disclosed",
         "l": ["LICENSEE OBLIGATIONS OF DISCLOSURE generally.",
               "LICENSEE OBLIGATIONS ON SELLER DISCLOSURES - helping the seller complete and deliver them.",
               "CONFLICTS OF INTEREST DISCLOSURE - including the licensee's own interest in the property.",
               "COMPENSATION DISCLOSURES - where the licensee's compensation comes from.",
               "EXPERIENCE AND KNOWLEDGE DISCLOSURES - a licensee must not hold out expertise they do not have.",
               "TIMING OF PERFORMANCE for clients and customers.",
               "CONTROVERSY BETWEEN CROSS SALE AGENTS - how a dispute between the two sides' agents is handled."],
         "check": [("A licensee who holds an interest in the property they are selling must:", "Disclose the conflict of interest", ["Say nothing", "Resign the listing"], "Arizona state content outline; ARS 32-2153."),
                   ("A licensee must not claim:", "Expertise they do not have", ["Any market opinion", "Knowledge of the neighbourhood"], "Experience and knowledge disclosures.")]},
        {"h": "Accounting and remitting (ARS 32-2153(A)(9))",
         "p": ["Failing within a reasonable time to account for or remit money, or to surrender documents or other valuable property belonging to others, is a ground for discipline. Money and documents belonging to someone else are never the licensee's to hold onto."],
         "check": [("Documents belonging to another that come into a licensee's possession must be:", "Surrendered to the rightful owner within a reasonable time", ["Kept for five years", "Destroyed at closing"], "ARS 32-2153(A)(9).")]},
        {"h": "Inducing a breach",
         "p": ["The licence law also reaches a licensee who INDUCES a party to break a contract - the statute lists it among the grounds for discipline alongside misrepresentation and unlawful compensation."],
         "check": [("Persuading a seller to break an existing contract so a new one can be written is:", "A ground for discipline", ["Good advocacy", "Permitted with disclosure"], "ARS 32-2153(A).")]},
    ],
    "traps": [
        "Compensation sources are disclosed, not assumed.",
        "Claiming expertise you lack is itself a disclosure failure in Arizona.",
        "Money AND documents both fall under the duty to account and surrender.",
    ],
    "vocab": [
        ["Cross sale", "A transaction where different agents represent each side."],
        ["Conflict of interest", "A personal interest at odds with the client's."],
        ["Material fact", "A fact that would affect a reasonable party's decision."],
    ],
    "examples": [],
}

STUDY["az/competency"] = {
    "summary": "Six items on staying inside what you actually know. Arizona names the niches by name: new homes, property management, timeshare, vacant land, commercial.",
    "sections": [
        {"h": "Professional competency",
         "p": ["The outline opens with PROFESSIONAL COMPETENCY REQUIREMENTS: a licensee takes on work they are competent to do, or gets help. It then lists PROPERTY TYPES and the NICHE AREAS where competence is most often lacking."],
         "l": ["NEW HOME SALES AND DEVELOPMENTS - builder contracts and subdivision rules differ from resale practice.",
               "PROPERTY MANAGEMENT - trust money, leases and the landlord and tenant act.",
               "TIMESHARE - regulated separately under title 32 chapter 20.",
               "VACANT LAND - access, water, utilities and the AFFIDAVIT OF DISCLOSURE for certain unsubdivided parcels.",
               "COMMERCIAL - different contracts, different clients, different liabilities."],
         "check": [("Arizona lists which as a niche needing particular competence?", "Timeshare", ["Residential resale", "Open houses"], "Arizona state content outline."),
                   ("A licensee asked to handle work beyond their competence should:", "Get help or decline", ["Proceed and learn on the job", "Refer it to the Commissioner"], "Professional competency requirements.")]},
        {"h": "Subdivisions and the Affidavit of Disclosure",
         "p": ["The state outline lists SUBDIVISIONS under the licence law, and names the AFFIDAVIT OF DISCLOSURE. Arizona requires a seller of certain unsubdivided land to give the buyer an affidavit covering access, utilities, roads and physical conditions - a document with no national equivalent."],
         "check": [("The Affidavit of Disclosure concerns:", "Certain unsubdivided land, covering access, utilities and roads", ["Condominium budgets", "Commercial leases"], "Named on the Arizona state content outline.")]},
    ],
    "traps": [
        "The Affidavit of Disclosure is for land, not for a house in a subdivision.",
        "Timeshare is separately regulated in Arizona.",
    ],
    "vocab": [
        ["Affidavit of Disclosure", "The Arizona land disclosure for certain unsubdivided parcels."],
        ["Subdivision", "Land divided for sale; separately regulated under title 32."],
        ["Timeshare", "An interest giving periodic use, regulated under chapter 20."],
    ],
    "examples": [],
}

STUDY["az/skill-care"] = {
    "summary": "Six items. The licensee's obligation of reasonable skill and care, plus two Arizona subjects it reaches: property taxes with special assessments, and utility and environmental regulation.",
    "sections": [
        {"h": "The obligation",
         "p": ["A licensee must act with REASONABLE SKILL AND CARE. The outline ties that duty to two concrete areas where Arizona practice differs: PROPERTY TAXES AND SPECIAL ASSESSMENTS, and ARIZONA UTILITY AND ENVIRONMENTAL REGULATION."],
         "check": [("Reasonable skill and care in Arizona is tied by the outline to:", "Property taxes, special assessments, and utility and environmental regulation", ["Commission negotiation", "Office management"], "Arizona state content outline.")]},
        {"h": "Arizona water law",
         "l": ["Arizona water is on the broker outline and matters in practice: the ARIZONA WATER DOCTRINE, and the ARIZONA GROUNDWATER MANAGEMENT ACT 1980.",
               "The 1980 Act created ACTIVE MANAGEMENT AREAS and IRRIGATION NON-EXPANSION AREAS, recognised GRANDFATHERED RIGHTS, and governs the TRANSFER OF WELL RIGHTS.",
               "Surface water in Arizona follows PRIOR APPROPRIATION - first in time, first in right - rather than the riparian rule used in wetter states."],
         "check": [("The Arizona Groundwater Management Act dates from:", "1980", ["1912", "1968", "1995"], "Named on the Arizona content outlines."),
                   ("The 1980 Act created:", "Active Management Areas and Irrigation Non-Expansion Areas", ["Riparian districts", "Water courts"], "Named on the Arizona content outlines."),
                   ("Arizona surface water follows:", "Prior appropriation", ["Riparian rights", "Absolute ownership"], "Prior appropriation governs in Arizona.")]},
    ],
    "traps": [
        "Arizona is prior appropriation, not riparian.",
        "AMAs and INAs both come from the 1980 Groundwater Management Act.",
        "Special assessments are separate from ordinary property taxes.",
    ],
    "vocab": [
        ["Prior appropriation", "First in time, first in right; Arizona's surface water rule."],
        ["Active Management Area", "An area with groundwater withdrawal controls."],
        ["Irrigation Non-Expansion Area", "An area where irrigated acreage may not expand."],
        ["Grandfathered right", "A groundwater right recognised from before the 1980 Act."],
        ["Special assessment", "A charge for a local improvement benefiting the property."],
    ],
    "examples": [],
}

STUDY["az/contracts"] = {
    "summary": "Eight items, the largest category. Arizona lets licensees draft the documents incident to their own transactions, which makes contract competence a licence-law issue rather than a nicety.",
    "sections": [
        {"h": "Employment agreements and purchase contracts",
         "l": ["EMPLOYMENT AGREEMENTS - listing agreements and buyer-broker agreements, which the outline treats as the licensee's own contract with the client.",
               "PURCHASE CONTRACTS, covering VALID CONTRACT REQUIREMENTS, CONSIDERATION, TERMS AND CONDITIONS, the CLOSING PROCESS AND POSSESSION, and COSTS AT CLOSING.",
               "A valid contract needs offer and acceptance, consideration, capable parties, lawful object, and - for land - writing under the statute of frauds."],
         "check": [("Which does the Arizona outline group under contracts?", "Employment agreements and purchase contracts", ["Only purchase contracts", "Only listing agreements"], "Arizona state content outline."),
                   ("A land contract must be in writing because of:", "The statute of frauds", ["The Consumer Fraud Act", "Commissioner's Rules"], "Named under Arizona consumer protection laws.")]},
        {"h": "Drafting, and the six-hour requirement",
         "p": ["An applicant for an original Arizona salesperson's licence must certify completion of SIX HOURS of instruction in REAL ESTATE CONTRACT LAW AND CONTRACT WRITING, and that instruction must include the applicant actually DRAFTING contracts to purchase real property, listing agreements and lease agreements (ARS 32-2124(M)). Arizona expects licensees to write contracts, so it makes them practise first."],
         "check": [("Arizona requires an original salesperson applicant to complete:", "Six hours of contract law and contract writing, including drafting", ["Three hours of contract theory", "No contract instruction"], "ARS 32-2124(M)."),
                   ("That instruction must include drafting:", "Purchase contracts, listing agreements and lease agreements", ["Deeds and mortgages", "Appraisal reports"], "ARS 32-2124(M).")]},
    ],
    "traps": [
        "Six hours of contract writing is an Arizona licensing requirement, separate from the 90-hour course.",
        "Employment agreement here means the listing or buyer-broker agreement.",
    ],
    "vocab": [
        ["Employment agreement", "A listing or buyer-broker agreement in Arizona usage."],
        ["Consideration", "The value each party gives; required for a valid contract."],
        ["Possession", "When the buyer takes occupancy; set by the contract."],
    ],
    "examples": [],
}

STUDY["az/services"] = {
    "summary": "Five items on the three outside businesses every Arizona transaction leans on: escrow, title insurance and lending.",
    "sections": [
        {"h": "Escrow, title and lending",
         "l": ["ESCROW - a neutral third party holds the money and documents and closes on the agreed terms. In Arizona a licensed escrow agent commonly handles closing.",
               "TITLE INSURANCE - the owner's policy protects the buyer's interest; the lender's policy protects the lender up to the loan amount.",
               "LENDING - qualifying the buyer, the loan instruments, and the costs that land on the closing statement.",
               "A licensee who holds earnest money must handle it as the transaction requires and keep the receipt in the broker's records (ARS 32-2151.01(A))."],
         "check": [("A lender's title policy protects:", "The lender, up to the loan amount", ["The buyer's equity", "The seller"], "An owner's policy is separate."),
                   ("Earnest money receipts must:", "Confirm the money was handled as the transaction required, and be kept in the broker's records", ["Be filed with the Department", "Be destroyed at closing"], "ARS 32-2151.01(A).")]},
    ],
    "traps": [
        "Owner's policy and lender's policy are different policies with different beneficiaries.",
        "The escrow agent is neutral; it is not the buyer's or seller's agent.",
    ],
    "vocab": [
        ["Escrow agent", "The neutral party holding funds and documents to closing."],
        ["Owner's title policy", "Title insurance protecting the buyer's interest."],
        ["Lender's title policy", "Title insurance protecting the lender."],
    ],
    "examples": [],
}

STUDY["az/ownership"] = {
    "summary": "Five items. Arizona is a community property state, which changes how married couples take and convey title.",
    "sections": [
        {"h": "How Arizonans hold title",
         "l": ["ARIZONA IS A COMMUNITY PROPERTY STATE: property acquired by either spouse during marriage is generally community property.",
               "SEPARATE PROPERTY is what a spouse owned before marriage or acquired by gift, devise or descent.",
               "Arizona also recognises community property WITH RIGHT OF SURVIVORSHIP, joint tenancy with right of survivorship, and tenancy in common.",
               "The outline also covers LIENS, DEEDS, HOMEOWNER'S ASSOCIATION restrictions, and EASEMENTS AND OTHER ENCUMBRANCES."],
         "check": [("Arizona is:", "A community property state", ["A common law title state only", "A dower and curtesy state"], "Property acquired during marriage is generally community."),
                   ("Property one spouse owned before marriage is:", "Separate property", ["Community property", "Jointly owned by law"], "Separate property keeps its character."),
                   ("Which gives survivorship between spouses in Arizona?", "Community property with right of survivorship", ["Tenancy in common", "Severalty"], "Arizona recognises the survivorship form.")]},
    ],
    "traps": [
        "Community property is the default for what is acquired during marriage.",
        "Plain community property does NOT carry survivorship; the survivorship form must be stated.",
    ],
    "vocab": [
        ["Community property", "Property acquired by either spouse during marriage."],
        ["Separate property", "Owned before marriage, or acquired by gift, devise or descent."],
        ["Severalty", "Sole ownership by one person or entity."],
        ["Encumbrance", "A claim or restriction on the title."],
    ],
    "examples": [],
}


# ------------------------------------------------------------- questions

Q = [
 # regulatory
 ("az/regulatory", "Recovery Fund", 1, "The Arizona Real Estate Recovery Fund pays at most, per transaction:",
  "$30,000", ["$20,000", "$50,000", "$90,000"],
  "ARS 32-2186(B)(1), regardless of claimants, licensees or parcels."),
 ("az/regulatory", "Recovery Fund", 1, "The Recovery Fund's aggregate limit for each licensee is:",
  "$90,000", ["$30,000", "$60,000", "$150,000"],
  "ARS 32-2186(B)(2)."),
 ("az/regulatory", "Recovery Fund", 2, "A licensee who loses money as a party to a transaction may:",
  "Not claim against the fund", ["Claim like any consumer", "Claim up to half", "Claim only for fraud"],
  "ARS 32-2186(D)."),
 ("az/regulatory", "Recovery Fund", 2, "The fund pays only against the licence of:",
  "A natural person", ["A corporation", "A partnership", "Any licensed entity"],
  "ARS 32-2186(E)."),
 ("az/regulatory", "Recovery Fund", 3, "An entity in which the licensee holds a direct or indirect interest of at least how much is barred from claiming?",
  "Ten per cent", ["Five per cent", "Twenty-five per cent", "Fifty per cent"],
  "ARS 32-2186(D)."),
 ("az/regulatory", "Recovery Fund", 3, "Once orders authorise payment of the licensee aggregate, the fund's liability for that licensee:",
  "Is terminated", ["Resets annually", "Doubles", "Continues indefinitely"],
  "ARS 32-2186(C)."),
 ("az/regulatory", "Records", 1, "Arizona broker transaction records must be kept for at least:",
  "Five years after the transaction ends", ["Three years", "Seven years", "One year"],
  "ARS 32-2151.01(A)."),
 ("az/regulatory", "Records", 2, "Storing broker records off-site in Arizona requires:",
  "Prior written notice to the Department of the street address", ["Nothing", "A Commissioner's order", "Annual reporting"],
  "ARS 32-2151.01(A)."),
 ("az/regulatory", "Records", 2, "Which must the employing broker's records include?",
  "Earnest money receipts and closing statements", ["The licensee's tax returns", "Appraisal licences", "Client credit reports"],
  "ARS 32-2151.01(A)."),
 ("az/regulatory", "Framework", 2, "Which part of the Arizona Constitution appears on the state exam outline?",
  "Article XXVI", ["Article II", "Article IX", "Article XIV"],
  "It heads the Real Estate Statutes category."),
 ("az/regulatory", "Framework", 1, "Arizona's real estate regulator is:",
  "The Arizona Department of Real Estate, headed by the Commissioner", ["A nine-member commission", "The Secretary of State", "The Attorney General"],
  "ARS title 32, chapter 20."),

 # agency
 ("az/agency", "Dual representation", 1, "Acting for more than one party in an Arizona transaction requires:",
  "The knowledge or written consent of all parties", ["Verbal consent from one party", "Broker approval only", "Nothing; it is prohibited"],
  "ARS 32-2153(A)(2)."),
 ("az/agency", "Dual representation", 2, "Dual representation in Arizona is:",
  "Permitted with the knowledge and written consent of all parties", ["Prohibited outright", "Allowed only commercially", "Allowed only by brokers"],
  "ARS 32-2153(A)(2)."),
 ("az/agency", "Brokers", 1, "A salesperson who represents a broker other than the one they are licensed to:",
  "Commits a ground for discipline", ["May do so with disclosure", "May do so for one deal", "Must notify the Department only"],
  "ARS 32-2153(A)(8)."),
 ("az/agency", "Brokers", 2, "A broker who employs an unlicensed salesperson:",
  "Commits a ground for discipline", ["Is fine if supervised", "Is fine for clerical work only"],
  "ARS 32-2153(A)(6)."),
 ("az/agency", "Compensation", 1, "An Arizona licensee may accept compensation from:",
  "Only a person authorised under ARS 32-2155", ["Any party to the transaction", "The buyer directly", "The escrow agent"],
  "ARS 32-2153(A)(7)."),
 ("az/agency", "Compensation", 2, "Paying or receiving a rebate in violation of the chapter is:",
  "A ground for discipline", ["Permitted if disclosed", "Permitted under $500", "A criminal felony"],
  "ARS 32-2153(A)(10)."),
 ("az/agency", "Accounting", 1, "A licensee holding money belonging to another must account for it:",
  "Within a reasonable time", ["Within 24 hours", "Within three business days", "At closing only"],
  "ARS 32-2153(A)(9)."),
 ("az/agency", "Accounting", 2, "Documents belonging to another that come into a licensee's possession must be:",
  "Surrendered to the rightful owner within a reasonable time", ["Kept for five years", "Destroyed at closing", "Filed with the Department"],
  "ARS 32-2153(A)(9)."),
 ("az/agency", "Appraisals", 3, "A licensee issuing an appraisal report on property they have an interest in must:",
  "Fully disclose the nature and extent of that interest", ["Decline to issue it", "Have it countersigned", "Report it to the Commissioner"],
  "ARS 32-2153(A)(9)."),
 ("az/agency", "Trust money", 2, "Authority to withdraw from a broker's trust fund account:",
  "Is restricted by statute", ["May be given to any employee", "Belongs to whoever took the deposit", "Is unlimited"],
  "ARS 32-2151.01(B)."),

 # duties
 ("az/duties", "Disclosure", 1, "A licensee holding an interest in the property being sold must:",
  "Disclose the conflict of interest", ["Say nothing", "Resign the listing", "Notify only the broker"],
  "Arizona state content outline; ARS 32-2153."),
 ("az/duties", "Disclosure", 2, "A licensee must not hold out:",
  "Expertise they do not have", ["Any opinion on value", "Knowledge of the neighbourhood", "Membership of a trade body"],
  "Experience and knowledge disclosures on the outline."),
 ("az/duties", "Disclosure", 2, "Where the licensee's compensation comes from must be:",
  "Disclosed", ["Assumed from custom", "Kept confidential", "Set by the Department"],
  "Compensation disclosures on the outline."),
 ("az/duties", "Misrepresentation", 1, "Pursuing a course of misrepresentation is a ground for discipline:",
  "Whether the licensee acts as a licensee or as a principal", ["Only when representing a client", "Only in listings", "Only if money changes hands"],
  "ARS 32-2153(A)(1)."),
 ("az/duties", "Contracts", 2, "Inducing a party to break an existing contract is:",
  "A ground for discipline", ["Skilled advocacy", "Permitted with disclosure", "Permitted if the client benefits"],
  "ARS 32-2153(A)."),
 ("az/duties", "Cross sale", 3, "The Arizona outline includes a category on:",
  "Controversy between cross sale agents", ["Commission arbitration by the Department", "Agent licensing appeals"],
  "Licensee duties and obligations, item G."),
 ("az/duties", "Seller disclosure", 2, "A licensee's obligation on seller disclosures is to:",
  "Help the seller complete and deliver them", ["Complete them for the seller", "Verify every statement personally", "Ignore them if as-is"],
  "Licensee obligations on seller disclosures."),

 # consumer
 ("az/consumer", "Homestead", 1, "The Arizona homestead exemption is:",
  "$400,000 in value", ["$150,000", "$250,000", "Unlimited"],
  "ARS 33-1101(A), adjusted annually."),
 ("az/consumer", "Homestead", 2, "Which may be held as an Arizona homestead?",
  "A cooperative in which the person resides", ["A rental house", "A vacant lot", "A commercial building"],
  "ARS 33-1101(A)(2)."),
 ("az/consumer", "Homestead", 2, "A mobile home may be an Arizona homestead:",
  "Yes, plus the land on which it sits, if the person resides there", ["No", "Only if permanently affixed", "Only in a park"],
  "ARS 33-1101(A)(3)."),
 ("az/consumer", "Homestead", 2, "The homestead exemption protects against:",
  "Attachment, execution and forced sale", ["Property taxes", "A mortgage the owner signed", "HOA assessments"],
  "ARS 33-1101(A)."),
 ("az/consumer", "Homestead", 3, "To hold an Arizona homestead a person must be:",
  "At least eighteen and resident in the state", ["Married", "A property owner for five years", "A US citizen"],
  "ARS 33-1101(A)."),
 ("az/consumer", "Consumer fraud", 2, "The Arizona Consumer Fraud Protection Act dates from:",
  "1967", ["1980", "1995", "2001"],
  "Named on the Arizona state content outline."),
 ("az/consumer", "Statute of frauds", 1, "Under the statute of frauds, which must be in writing?",
  "A contract for the sale of land", ["A month-to-month tenancy", "A verbal price quote", "An open house sign-in"],
  "Land contracts and leases over one year."),

 # advertising
 ("az/advertising", "False advertising", 1, "False or misleading advertising is a ground for discipline where the licensee acted:",
  "Knowingly", ["Negligently only", "Regardless of knowledge", "Only if a sale resulted"],
  "ARS 32-2153(A)(4)."),
 ("az/advertising", "False advertising", 2, "The advertising ground for discipline reaches statements made:",
  "In this or any other state", ["Only in Arizona", "Only in print media", "Only online"],
  "ARS 32-2153(A)(4)."),
 ("az/advertising", "Titles", 2, "Knowingly using the term 'real estate broker' without the right to do so is:",
  "A ground for discipline", ["A civil matter only", "Permitted if unpaid", "Permitted while an application is pending"],
  "ARS 32-2153(A)(5)."),
 ("az/advertising", "Supervision", 2, "Advertising supervision in Arizona places responsibility on:",
  "The broker, for what the brokerage publishes", ["Each agent alone", "The Department", "The seller"],
  "Advertising supervision on the state outline."),
 ("az/advertising", "Development", 3, "Development advertising on the Arizona outline concerns:",
  "Advertising for a subdivision or development", ["Builder warranties", "Construction permits"],
  "Arizona state content outline."),

 # foreclosure
 ("az/foreclosure", "Anti-deficiency", 1, "Arizona's anti-deficiency protection covers parcels of:",
  "Two and one-half acres or less", ["Five acres or less", "Ten acres or less", "Any size"],
  "ARS 33-729(A)."),
 ("az/foreclosure", "Anti-deficiency", 1, "The protected dwelling must be:",
  "A single one-family or single two-family dwelling", ["Any residential building", "A fourplex or smaller", "An owner-occupied home of any size"],
  "ARS 33-729(A)."),
 ("az/foreclosure", "Anti-deficiency", 2, "Where ARS 33-729 applies, the lender:",
  "May not obtain a deficiency judgment", ["May pursue the borrower's other property", "May garnish wages", "May sue for the shortfall within a year"],
  "ARS 33-729(A)."),
 ("az/foreclosure", "Anti-deficiency", 2, "The loan must be:",
  "Purchase money - for the balance of the price or a loan to pay it", ["Any mortgage", "A refinance", "A home equity line"],
  "ARS 33-729(A)."),
 ("az/foreclosure", "Trustee sale", 1, "After an Arizona trustee's sale, a deficiency action must be brought within:",
  "90 days of the sale", ["30 days", "6 months", "One year"],
  "ARS 33-814(A)."),
 ("az/foreclosure", "Trustee sale", 2, "Arizona lenders normally secure loans with:",
  "A deed of trust with a power of sale", ["A mortgage foreclosed judicially", "A land contract", "A security deed"],
  "ARS 33-814."),

 # skill and care
 ("az/skill-care", "Water", 1, "The Arizona Groundwater Management Act dates from:",
  "1980", ["1912", "1968", "1995"],
  "Named on the Arizona content outlines."),
 ("az/skill-care", "Water", 2, "The 1980 Act created:",
  "Active Management Areas and Irrigation Non-Expansion Areas", ["Riparian districts", "Water courts", "Groundwater trusts"],
  "Named on the Arizona content outlines."),
 ("az/skill-care", "Water", 2, "Arizona surface water follows:",
  "Prior appropriation", ["Riparian rights", "Absolute ownership", "Correlative rights"],
  "First in time, first in right."),
 ("az/skill-care", "Water", 3, "A groundwater right recognised from before the 1980 Act is:",
  "A grandfathered right", ["A riparian right", "A littoral right", "An appropriative right"],
  "Named on the Arizona content outlines."),
 ("az/skill-care", "Taxes", 2, "A charge for a local improvement benefiting a particular property is:",
  "A special assessment", ["An ad valorem tax", "A transfer tax", "An excise tax"],
  "Property taxes and special assessments on the outline."),
 ("az/skill-care", "Obligation", 2, "Reasonable skill and care in the Arizona outline is tied to:",
  "Property taxes, special assessments, and utility and environmental regulation", ["Commission negotiation", "Office management", "Advertising budgets"],
  "Arizona state content outline."),

 # competency
 ("az/competency", "Niches", 1, "Which does Arizona name as a niche needing particular competence?",
  "Timeshare", ["Residential resale", "Open houses", "Comparative market analysis"],
  "Arizona state content outline, item VI.C."),
 ("az/competency", "Niches", 2, "Which is listed among the Arizona niche areas?",
  "New home sales and developments", ["Mortgage origination", "Title examination", "Home inspection"],
  "Arizona state content outline."),
 ("az/competency", "Competency", 1, "A licensee asked to handle work beyond their competence should:",
  "Get help or decline the work", ["Proceed and learn on the job", "Refer it to the Commissioner", "Charge a higher fee"],
  "Professional competency requirements."),
 ("az/competency", "Land", 2, "The Affidavit of Disclosure concerns:",
  "Certain unsubdivided land, covering access, utilities and roads", ["Condominium budgets", "Commercial leases", "New home warranties"],
  "Named on the Arizona state content outline."),
 ("az/competency", "Subdivisions", 3, "Subdivisions in Arizona are:",
  "Separately regulated under title 32, chapter 20", ["Unregulated", "Regulated only by counties", "Regulated by the Corporation Commission"],
  "Named on the Arizona state content outline."),

 # contracts
 ("az/contracts", "Education", 1, "An original Arizona salesperson applicant must complete:",
  "Six hours of contract law and contract writing", ["Three hours of contract theory", "Twelve hours of contracts", "No contract instruction"],
  "ARS 32-2124(M)."),
 ("az/contracts", "Education", 2, "That contract instruction must include the applicant drafting:",
  "Purchase contracts, listing agreements and lease agreements", ["Deeds and mortgages", "Appraisal reports", "Escrow instructions"],
  "ARS 32-2124(M)."),
 ("az/contracts", "Employment agreements", 1, "In the Arizona outline, 'employment agreements' means:",
  "Listing and buyer-broker agreements", ["Salesperson employment contracts", "Property management staffing", "Independent contractor agreements"],
  "Arizona state content outline, item VIII.A."),
 ("az/contracts", "Validity", 1, "A valid Arizona purchase contract requires:",
  "Offer and acceptance, consideration, capable parties and a lawful object", ["Notarisation", "Recording", "Commissioner approval"],
  "Valid contract requirements on the outline."),
 ("az/contracts", "Closing", 2, "The Arizona contracts category also covers:",
  "The closing process, possession, and costs at closing", ["Appraisal methodology", "Loan underwriting", "Title plant operations"],
  "Arizona state content outline, item VIII.B."),
 ("az/contracts", "Drafting", 3, "Arizona licensees may draft the documents incident to a transaction they handle because of:",
  "Article XXVI of the Arizona Constitution", ["A Commissioner's rule", "A Supreme Court order", "The Consumer Fraud Act"],
  "Named first on the Real Estate Statutes outline."),

 # services
 ("az/services", "Title", 1, "A lender's title policy protects:",
  "The lender, up to the loan amount", ["The buyer's equity", "The seller", "The escrow agent"],
  "An owner's policy is separate."),
 ("az/services", "Escrow", 1, "An escrow agent in an Arizona transaction is:",
  "A neutral third party holding funds and documents", ["The buyer's agent", "The seller's agent", "The lender's agent"],
  "Critical business services on the outline."),
 ("az/services", "Escrow", 2, "Earnest money receipts in the broker's records must:",
  "Confirm the money was handled as the transaction required", ["Show the commission split", "Be filed with the Department", "Be notarised"],
  "ARS 32-2151.01(A)."),
 ("az/services", "Lending", 2, "Costs that appear on the Arizona closing statement include:",
  "Receipts, disbursements and adjustments", ["Only the purchase price", "Only the loan amount"],
  "ARS 32-2151.01(A) describes the closing statement contents."),
 ("az/services", "Title", 2, "An owner's title policy protects:",
  "The buyer's interest in the title", ["The lender only", "The listing broker", "The escrow company"],
  "The lender's policy is separate."),

 # ownership
 ("az/ownership", "Marital property", 1, "Arizona is:",
  "A community property state", ["A common law title state only", "A dower and curtesy state", "A tenancy by the entireties state"],
  "Property acquired during marriage is generally community property."),
 ("az/ownership", "Marital property", 1, "Property one spouse owned before marriage is:",
  "Separate property", ["Community property", "Jointly owned by law", "Held in trust"],
  "Separate property keeps its character."),
 ("az/ownership", "Marital property", 2, "Property acquired by one spouse during marriage by gift or inheritance is:",
  "Separate property", ["Community property", "Half community", "Community after five years"],
  "Gift, devise or descent is separate."),
 ("az/ownership", "Survivorship", 2, "Which gives survivorship between Arizona spouses?",
  "Community property with right of survivorship", ["Plain community property", "Tenancy in common", "Severalty"],
  "The survivorship form must be stated."),
 ("az/ownership", "Encumbrances", 2, "Which is an encumbrance?",
  "An easement across the property", ["The owner's fee simple interest", "The property's market value"],
  "Encumbrances are claims or restrictions on title."),
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
            "id": "az-" + hashlib.sha1(q.encode()).hexdigest()[:8],
            "portion": "georgia", "topic": topic, "subtopic": sub,
            "sub": topic + "|" + sub, "concept": "Arizona " + sub.lower(),
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
        "code": "AZ", "name": "Arizona", "abbr": "AZ",
        "regulator": "Arizona Department of Real Estate",
        "pass": EXAM["pass"],
        "portions": {
            "national": {"scored": EXAM["national_scored"],
                         "minutes": EXAM["national_minutes"]},
            "georgia": {"name": "Arizona state", "scored": EXAM["state_scored"],
                        "minutes": EXAM["state_minutes"],
                        "blurb": "ARS title 32 chapter 20, the Commissioner's Rules, and the Arizona law the outline names."},
        },
        "topics": topics, "bank": bank, "study": study,
        "sources": SOURCES, "diffs": DIFFS,
    }


# Where Arizona departs from the national rule.
DIFFS = {
    "national/ownership": [
        "Arizona is a COMMUNITY PROPERTY state, and also recognises community property WITH RIGHT OF SURVIVORSHIP.",
        "The homestead exemption protects up to $400,000 in value from attachment, execution and forced sale, and can cover a mobile home plus its land (ARS 33-1101).",
    ],
    "national/financing": [
        "Arizona lenders use a DEED OF TRUST with a trustee's power of sale; a deficiency action after a trustee's sale must be brought within 90 days (ARS 33-814).",
        "The ANTI-DEFICIENCY statute bars a deficiency judgment where purchase money financed a parcel of 2.5 acres or less used as a single one- or two-family dwelling (ARS 33-729).",
    ],
    "national/ownership_water": [],
    "national/practice": [
        "Arizona broker records are kept five years, at the principal or branch office, or at an Arizona off-site location notified to the Department in writing (ARS 32-2151.01).",
        "The Recovery Fund pays $30,000 per transaction and $90,000 per licensee, and licensees themselves cannot claim (ARS 32-2186).",
        "Acting for more than one party needs the knowledge or written consent of all parties (ARS 32-2153(A)(2)).",
    ],
    "national/landuse": [
        "Arizona surface water follows PRIOR APPROPRIATION, and the Groundwater Management Act 1980 created Active Management Areas, Irrigation Non-Expansion Areas and grandfathered rights.",
    ],
    "national/contracts": [
        "Article XXVI of the Arizona Constitution lets licensees draft the documents incident to a transaction they handle - which is why an applicant must complete six hours of contract law and contract WRITING, including drafting practice (ARS 32-2124(M)).",
    ],
}


if __name__ == "__main__":
    import io, json, os
    here = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    out = os.path.join(here, "greprep", "packs", "AZ.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    pack = build()
    with io.open(out, "w", encoding="utf-8") as f:
        json.dump(pack, f, ensure_ascii=False, indent=1, sort_keys=True)
    print("wrote", out, len(pack["bank"]), "questions,", len(pack["study"]), "lessons")
