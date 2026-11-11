"""Indiana state content: lessons and practice questions.

Indiana splits the broker examination. The Pearson VUE handbook gives the
real estate broker examination 145 total questions in 240 minutes - 80
scored NATIONAL items and 50 scored STATE items, plus 5 to 10 unscored
pretest items.

The pass mark is NOT a percentage. The handbook says forms are EQUATED,
that on the converted scale the IPLA set a PASSING SCORE OF 75, and that
the scaled score "is neither the number of questions answered correctly
nor the percentage of questions answered correctly". Numeric scores go
only to candidates who FAIL, and results are good for ONE YEAR.

Indiana's own twist: a licensee HAS an agency relationship with, and is
representing, the person they are working with UNLESS there is a written
agreement to the contrary or they are merely assisting a customer without
compensation. Agency is the default here, not the exception.

Every rule below was read on 2026-11-11 from the official text:
  - Indiana Code title 25 article 34.1 (Real Estate Brokers and
    Salespersons), from iga.in.gov.
  - Indiana Code title 32 article 21 chapters 5 and 6 (residential sales
    disclosure and psychologically affected properties), from iga.in.gov.
  - The Pearson VUE Indiana Real Estate Candidate Handbook (#091500), for
    the examination tables and the 50-item state outline.
The section a fact comes from is cited next to it. Do not add a fact here
without reading its source first.
"""

EXAM = {
    # Broker: 145 total questions / 240 minutes; 80 scored national and
    # 50 scored state. Scaled passing score of 75, not a percentage.
    "state_scored": 50,
    "state_minutes": 92,
    "national_scored": 80,
    "national_minutes": 148,
    "pass": 0.75,
    "pass_published": False,
    "pass_note": ("Indiana EQUATES its examination forms and reports a SCALED score. "
                  "The IPLA set the passing scaled score at 75, but the handbook says "
                  "that score is neither the number nor the percentage of questions "
                  "answered correctly. Numeric scores are reported only to candidates "
                  "who FAIL, and a pass is good for ONE YEAR. Treat 75% here as a "
                  "study target, not the state's requirement."),
}

# Pearson's Indiana broker state outline, item counts summing to 50.
TOPICS = [
    ("in/statutes-rules", "Statutes & rules governing licensees", 17,
     "Agency relationships and disclosures, office policy, and licensee conduct."),
    ("in/statutory", "Statutory & regulatory requirements", 12,
     "Advertising, compensation, brokerage agreements, offers, trust money, disclosure."),
    ("in/licensing", "Licensing", 9,
     "Who needs a licence, licence types, education, renewal, transfers and status."),
    ("in/office", "Real estate office procedures", 7,
     "Records, monies, place of business, branches, assistants, closings, supervision."),
    ("in/commission", "The Indiana Real Estate Commission", 5,
     "Powers, records, investigations and sanctions, including the recovery fund."),
]

SOURCES = [
    {"by": "Indiana General Assembly",
     "name": "Indiana Code title 25, article 34.1",
     "note": "The licence law: broker requirements, trust accounts, education and chapter 10 on agency relationships.",
     "url": "https://iga.in.gov/ic/2026/Title_25/Article_34.1.pdf"},
    {"by": "Indiana General Assembly",
     "name": "Indiana Code 32-21-5 and 32-21-6",
     "note": "The residential sales disclosure form, and psychologically affected properties.",
     "url": "https://iga.in.gov/ic/2026/Title_32/Article_21/Chapter_5.pdf"},
    {"by": "Pearson VUE and the Indiana Professional Licensing Agency",
     "name": "Indiana Real Estate Candidate Handbook",
     "note": "145 questions in 240 minutes, 80 national and 50 state scored items, and a scaled passing score of 75.",
     "url": "https://www.pearsonvue.com/us/en/in/realestate.html"},
]


# --------------------------------------------------------------- lessons

STUDY = {}

STUDY["in/statutes-rules"] = {
    "summary": "Seventeen items, the biggest block. Indiana's rule is the opposite of most states: you ARE their agent unless something in writing says you are not.",
    "sections": [
        {"h": "Agency is the default (IC 25-34.1-10-9.5)",
         "l": ["A licensee HAS AN AGENCY RELATIONSHIP WITH, AND IS REPRESENTING, THE INDIVIDUAL WITH WHOM THE LICENSEE IS WORKING unless (1) there is a WRITTEN AGREEMENT TO THE CONTRARY, or (2) the licensee is MERELY ASSISTING THE INDIVIDUAL AS A CUSTOMER WITHOUT COMPENSATION.",
               "Where a WRITTEN AGREEMENT removes the agency relationship, the licensee must STILL PERFORM AT LEAST THREE DUTIES under that agreement: BE AVAILABLE TO RECEIVE AND TIMELY PRESENT offers and counteroffers; ASSIST IN NEGOTIATING, COMPLETING REAL ESTATE FORMS, COMMUNICATING and timely presenting offers, counteroffers, notices and addenda until a purchase agreement or lease is SIGNED and all CONTINGENCIES SATISFIED OR WAIVED; and TIMELY RESPOND to questions on offers, counteroffers, notices, addenda and contingencies.",
               "If that licensee FAILS to perform those duties and ANOTHER LICENSEE performs them for the party, that performance DOES NOT CREATE AN AGENCY RELATIONSHIP for the other licensee.",
               "Nothing stops a licensee from performing DUTIES IN ADDITION to those specified.",
               "The duties begin WHEN THE AGENCY RELATIONSHIP IS ENTERED and continue UNTIL IT TERMINATES. After termination only two duties survive: ACCOUNTING for money and property received, and KEEPING CONFIDENTIAL information made confidential by the client's request or instruction, unless the law requires disclosure or the client consents in writing (IC 25-34.1-10-14)."],
         "check": [("In Indiana, a licensee working with a buyer who has signed nothing is:", "That buyer's agent, by default", ["A transaction broker", "A customer-only licensee", "A subagent of the seller"], "IC 25-34.1-10-9.5(a)."),
                   ("Agency does NOT arise where:", "There is a written agreement to the contrary, or the licensee merely assists a customer without compensation", ["The licensee is not paid by that party", "No offer is written"], "IC 25-34.1-10-9.5(a)."),
                   ("A licensee who has contracted OUT of agency must still:", "Receive and timely present offers, assist with forms and negotiation, and timely answer questions", ["Do nothing at all", "Act as a dual agent"], "IC 25-34.1-10-9.5(b)."),
                   ("Which duties survive the end of an Indiana agency relationship?", "Accounting for money and property, and keeping confidential information confidential", ["Loyalty and obedience", "All of the statutory duties"], "IC 25-34.1-10-14(c).")]},
        {"h": "Duties to a seller or landlord (IC 25-34.1-10-10)",
         "l": ["FULFIL THE TERMS of the agency relationship; DISCLOSE ITS NATURE, and REDEFINE AND DISCLOSE IF IT CHANGES.",
               "PROMOTE THE CLIENT'S INTERESTS by seeking a satisfactory price and terms - though NOT OBLIGED to seek additional offers once one is accepted, unless agreed otherwise - and by PRESENTING ALL OFFERS TO AND FROM the seller IMMEDIATELY ON RECEIPT, REGARDLESS of whether an offer has already been accepted, unless the seller directs otherwise.",
               "DISCLOSE ADVERSE MATERIAL FACTS OR RISKS ACTUALLY KNOWN concerning the transaction; ADVISE the client to get EXPERT ADVICE on matters beyond the licensee's expertise; ACCOUNT TIMELY for money and property; exercise REASONABLE CARE AND SKILL; and COMPLY with the chapter and all applicable law INCLUDING FAIR HOUSING AND CIVIL RIGHTS.",
               "WITHOUT THE CLIENT'S INFORMED WRITTEN CONSENT the licensee may NOT disclose THAT THE SELLER WILL ACCEPT LESS than the listed price or other concessions, WHAT MOTIVATES the seller, or ANY MATERIAL OR CONFIDENTIAL INFORMATION unless the law requires it or silence would be FRAUD OR DISHONEST DEALING.",
               "A seller's agent OWES NO DUTIES TO THE BUYER except to TREAT ALL PROSPECTIVE BUYERS HONESTLY and NOT KNOWINGLY GIVE THEM FALSE INFORMATION.",
               "But a licensee MUST disclose to a prospective buyer ADVERSE MATERIAL FACTS OR RISKS ACTUALLY KNOWN about the PHYSICAL CONDITION of the property, and facts required by statute to be disclosed, THAT COULD NOT BE DISCOVERED BY A REASONABLE AND TIMELY INSPECTION. There is NO duty to conduct an independent inspection or to verify statements by the seller or an independent inspector, and NO CAUSE OF ACTION arises for disclosing in compliance with the section.",
               "A seller's agent may SHOW ALTERNATIVE PROPERTIES and LIST COMPETING PROPERTIES without breaching any duty.",
               "The mirror-image duties are owed to a BUYER OR TENANT by their agent (IC 25-34.1-10-11)."],
         "check": [("An Indiana seller's agent must present offers:", "Immediately on receipt, even after an offer has been accepted, unless the seller directs otherwise", ["Only until the first acceptance", "At the next weekly meeting"], "IC 25-34.1-10-10(a)(3)(B)."),
                   ("Which may NOT be disclosed without the seller's informed written consent?", "That the seller will accept less than the listed price", ["A known foundation crack", "A required statutory disclosure"], "IC 25-34.1-10-10(b)(1)."),
                   ("A seller's agent owes a prospective buyer:", "Honest treatment and no knowingly false information", ["Full fiduciary duties", "Nothing whatever"], "IC 25-34.1-10-10(c)."),
                   ("Adverse material facts about physical condition must be disclosed to a buyer where they:", "Are actually known and could not be found by a reasonable and timely inspection", ["Are suspected", "Appear in the listing"], "IC 25-34.1-10-10(d)."),
                   ("Does an Indiana seller's agent have to inspect the property for the buyer?", "No, and need not verify the seller's or an inspector's statements", ["Yes, a visual inspection", "Yes, a full inspection"], "IC 25-34.1-10-10(d)."),
                   ("Must a seller's agent keep seeking offers after one is accepted?", "No, unless the parties agree otherwise", ["Yes, always", "Yes, for 30 days"], "IC 25-34.1-10-10(a)(3)(A).")]},
        {"h": "Limited agency (IC 25-34.1-10-12)",
         "l": ["A licensee may act as a LIMITED AGENT - Indiana's name for dual agency - ONLY WITH THE WRITTEN CONSENT OF ALL PARTIES.",
               "Consent is PRESUMED GIVEN and all parties CONSIDERED INFORMED where a party signs a writing at the time of entering the agency relationship containing SIX things: a DESCRIPTION of the transactions in which the licensee will serve as limited agent; a statement that the licensee REPRESENTS PARTIES WHOSE INTERESTS ARE DIFFERENT OR EVEN ADVERSE; a statement of what MAY NOT BE DISCLOSED without informed written consent; a statement that there is NO IMPUTATION OF KNOWLEDGE between any party and the limited agent or among licensees; a statement that A PARTY DOES NOT HAVE TO CONSENT to limited agency; and a statement that consent was given VOLUNTARILY and the disclosure READ AND UNDERSTOOD.",
               "The protected items are: any MATERIAL OR CONFIDENTIAL INFORMATION - except adverse material facts actually known about the PHYSICAL CONDITION and statutory disclosures not discoverable by reasonable and timely inspection; THAT A BUYER WILL PAY MORE than offered; THAT A SELLER WILL ACCEPT LESS than listed; WHAT MOTIVATES a party; and OTHER TERMS that would create a CONTRACTUAL ADVANTAGE for one party.",
               "A limited agent MAY disclose and provide BOTH parties PROPERTY INFORMATION, including listed and sold properties from a multiple listing service or other source.",
               "NO CAUSE OF ACTION arises against a licensee for disclosing or failing to disclose in compliance with the section, and making a REQUIRED DISCLOSURE DOES NOT TERMINATE the limited agency."],
         "check": [("Indiana's term for dual agency is:", "Limited agency", ["Transaction brokerage", "Designated agency", "Facilitation"], "IC 25-34.1-10-12."),
                   ("A limited agent may act only with:", "The written consent of all parties", ["Oral consent", "The managing broker's approval"], "IC 25-34.1-10-12(a)."),
                   ("Which may a limited agent disclose to both sides?", "Property information, including listed and sold properties from an MLS", ["What motivates a party", "That the buyer will pay more"], "IC 25-34.1-10-12(b)."),
                   ("The limited agency writing must state that:", "A party does not have to consent to the limited agency", ["The fee is non-negotiable", "The Commission has approved it"], "IC 25-34.1-10-12(a)(5)."),
                   ("In limited agency, knowledge is:", "Not imputed between any party and the limited agent or among licensees", ["Imputed to the whole firm", "Imputed to the managing broker"], "IC 25-34.1-10-12(a)(4)."),
                   ("Making a required disclosure as limited agent:", "Does not terminate the limited agency relationship", ["Ends the relationship", "Requires fresh consent"], "IC 25-34.1-10-12(c).")]},
        {"h": "Written office policy and compensation (IC 25-34.1-10-13)",
         "l": ["A MANAGING BROKER shall DEVELOP AND ENFORCE a BROKER COMPANY WRITTEN OFFICE POLICY identifying and describing the agency relationships a licensee may have, and SPECIFICALLY PERMITTING OR REJECTING the practice of DISCLOSED LIMITED AGENCY.",
               "At the BEGINNING of an agency relationship a licensee shall DISCLOSE THAT WRITTEN OFFICE POLICY IN WRITING, BEFORE the potential client discloses ANY CONFIDENTIAL INFORMATION specific to them.",
               "Parties must be ADVISED WHETHER COMPENSATION WILL BE SHARED with other broker companies that may represent other parties whose interests are different or even adverse.",
               "THE PAYMENT OF COMPENSATION DOES NOT CREATE AN AGENCY RELATIONSHIP between a licensee and a seller, landlord, buyer or tenant."],
         "check": [("An Indiana managing broker must develop and enforce:", "A written office policy describing agency relationships and permitting or rejecting disclosed limited agency", ["A commission schedule", "A marketing plan"], "IC 25-34.1-10-13(a)."),
                   ("The written office policy must be disclosed:", "In writing at the beginning of the relationship, before any confidential information is given", ["At the offer", "At closing"], "IC 25-34.1-10-13(b)."),
                   ("Paying a licensee's compensation:", "Does not create an agency relationship", ["Makes the payer the client", "Creates limited agency"], "IC 25-34.1-10-13(d)."),
                   ("Parties must be told whether:", "Compensation will be shared with other broker companies representing adverse parties", ["The licensee is a Realtor", "The firm is incorporated"], "IC 25-34.1-10-13(c).")]},
        {"h": "Psychologically affected property (IC 32-21-6)",
         "l": ["A PSYCHOLOGICALLY AFFECTED PROPERTY is real estate or a dwelling for sale, rent or lease to which one or more facts - OR A REASONABLE SUSPICION of them - apply: that an INDIVIDUAL DIED on the property; or that it was the site of a FELONY under IC 35, CRIMINAL ORGANIZATION ACTIVITY, the DISCHARGE OF A FIREARM INVOLVING A LAW ENFORCEMENT OFFICER on duty, or the ILLEGAL MANUFACTURE OR DISTRIBUTION OF A CONTROLLED SUBSTANCE.",
               "AN OWNER OR AGENT IS NOT REQUIRED TO DISCLOSE any knowledge of a psychologically affected property to a transferee (IC 32-21-6-5).",
               "An owner or agent IS NOT LIABLE for refusing to disclose that a property is psychologically affected, or details of it (IC 32-21-6-6).",
               "A TRANSFEREE here means a purchaser, tenant, lessee or prospective one."],
         "check": [("In Indiana, disclosure of a psychologically affected property is:", "Not required, and refusing to disclose carries no liability", ["Required on request", "Required in every sale"], "IC 32-21-6-5, 32-21-6-6."),
                   ("Which makes a property psychologically affected in Indiana?", "An individual died on the property", ["A low appraisal", "An expired listing"], "IC 32-21-6-3(1)."),
                   ("The definition also reaches:", "A reasonable suspicion of the listed facts, not only the facts themselves", ["Only proven facts", "Only facts within five years"], "IC 32-21-6-3.")]},
    ],
    "traps": [
        "Agency is the DEFAULT in Indiana - the written agreement is what removes it.",
        "Even without agency, three duties survive under the written agreement.",
        "Limited agency, not dual agency, and consent must be written.",
        "Psychologically affected property NEVER has to be disclosed here.",
    ],
    "vocab": [
        ["Limited agent", "Indiana's dual agent, acting for both sides with written consent."],
        ["Adverse material fact", "A known fact about condition that must be disclosed."],
        ["Broker company", "Indiana's term for the brokerage firm."],
        ["Managing broker", "The broker who runs the company and owns the office policy."],
        ["Psychologically affected property", "A property marked by death or crime; no disclosure required."],
    ],
    "examples": [
        {"t": "The buyer who signed nothing",
         "s": "A buyer has toured three houses with you. Nothing has been signed and you expect to be paid from the listing side.",
         "w": ["Because you are being compensated and there is no written agreement to the contrary, you ARE their agent.",
               "That means the full IC 25-34.1-10-11 duties apply - loyalty, confidentiality, the lot.",
               "If you wanted a customer relationship, it had to be in writing, and three duties would still apply."],
         "k": "In Indiana, silence creates agency; writing removes it."},
    ],
}

STUDY["in/statutory"] = {
    "summary": "Twelve items on the mechanics - adverts, agreements, offers, earnest money, and the two disclosure statutes consumers actually see.",
    "sections": [
        {"h": "The sales disclosure form (IC 32-21-5)",
         "l": ["The chapter applies ONLY to a SALE, EXCHANGE, INSTALLMENT SALES CONTRACT, or LEASE WITH OPTION TO BUY of residential real estate containing NOT MORE THAN FOUR RESIDENTIAL DWELLING UNITS, and NOT to court-ordered transfers, foreclosure sales, transfers by a bankruptcy trustee, eminent domain and similar.",
               "An OWNER MUST COMPLETE AND SIGN a disclosure form and SUBMIT IT TO A PROSPECTIVE BUYER BEFORE AN OFFER FOR THE SALE IS ACCEPTED (IC 32-21-5-10(a)).",
               "The form is NOT A WARRANTY by the owner or the owner's agent and MAY NOT BE USED AS A SUBSTITUTE for inspections or warranties (IC 32-21-5-9).",
               "BEFORE CLOSING, an accepted offer is NOT ENFORCEABLE AGAINST THE BUYER until the OWNER AND THE PROSPECTIVE BUYER HAVE SIGNED the form. AFTER CLOSING, the owner's failure to deliver one DOES NOT BY ITSELF INVALIDATE the transaction, and a buyer may NOT invalidate a transaction because of THEIR OWN failure to sign a form they received.",
               "The owner is NOT LIABLE for an error, inaccuracy or omission that was NOT WITHIN THEIR ACTUAL KNOWLEDGE or was based on information from a PUBLIC AGENCY or a licensed or specially knowledgeable person whose report the owner reasonably believed correct (IC 32-21-5-11).",
               "An owner who later finds the form inaccurate does NOT violate the chapter, but AT OR BEFORE SETTLEMENT must DISCLOSE ANY MATERIAL CHANGE in the physical condition, or CERTIFY that the condition is SUBSTANTIALLY THE SAME (IC 32-21-5-12).",
               "If a buyer receives a disclosure form or AMENDED form AFTER AN OFFER HAS BEEN ACCEPTED and it DISCLOSES A DEFECT, the buyer may NULLIFY THE CONTRACT WITHIN TWO BUSINESS DAYS by DELIVERING A WRITTEN RESCISSION, and is ENTITLED TO A RETURN OF DEPOSITS (IC 32-21-5-13).",
               "HOMEOWNERS ASSOCIATION property: for transfers after 30 June 2015 the seller must give the purchaser, NOT LATER THAN TEN DAYS BEFORE CLOSING, a disclosure that the property is in an HOA community, a COPY OF THE RECORDED GOVERNING DOCUMENTS, a statement of ASSESSMENTS and their amount, and the NAME AND ADDRESS of a board member, HOA agent or management contractor. An HOA may not charge more than $50 for a statement of unpaid assessments (IC 32-21-5-8.5)."],
         "check": [("The Indiana sales disclosure form must be given to the buyer:", "Before an offer for the sale is accepted", ["At closing", "Within 10 days of the offer"], "IC 32-21-5-10(a)."),
                   ("The chapter applies to residential real estate of:", "Not more than four dwelling units", ["Any residential property", "Single-family homes only"], "IC 32-21-5-1(a)."),
                   ("A disclosure form received after acceptance that reveals a defect lets the buyer nullify within:", "Two business days, by written rescission", ["Three days", "Ten days", "Not at all"], "IC 32-21-5-13(a)."),
                   ("Before closing, an accepted offer is not enforceable against the buyer until:", "Both the owner and the prospective buyer have signed the disclosure form", ["The inspection is complete", "The appraisal is in"], "IC 32-21-5-10(c)."),
                   ("At or before settlement, the owner must:", "Disclose any material change in physical condition, or certify the condition is substantially the same", ["Re-sign the original form", "Do nothing further"], "IC 32-21-5-12(a)."),
                   ("HOA documents must reach the purchaser:", "Not later than ten days before closing", ["At closing", "Within 30 days after closing"], "IC 32-21-5-8.5(e)."),
                   ("The disclosure form is:", "Not a warranty, and not a substitute for inspections", ["A seller's warranty of condition", "An inspection report"], "IC 32-21-5-9.")]},
        {"h": "Trust accounts and earnest money (IC 25-34.1-4-5)",
         "l": ["Each BROKER COMPANY shall MAINTAIN ONE OR MORE TRUST ACCOUNTS (INTEREST OR NONINTEREST BEARING); DEPOSIT INTO THEM ALL FUNDS BELONGING TO OTHERS that come into the possession of the company or of any broker whose licence it holds; and CLEARLY IDENTIFY any account that is a trust account.",
               "The trust accounts shall contain ALL EARNEST MONEY DEPOSITS, FUNDS HELD FOR CLOSING ESCROWS, SALE PROCEEDS NOT YET DISBURSED, and all other funds belonging to others.",
               "The company SHALL NOT USE ANY TRUST ACCOUNT for the deposit of ANY PERSONAL FUNDS OR OTHER BUSINESS FUNDS, and shall keep a DETAILED RECORD of the funds and any interest accrued IDENTIFYING THE AMOUNT HELD FOR EACH BENEFICIARY. ANY INTEREST EARNED SHALL BE HELD FOR THE BENEFICIARY.",
               "On the DEATH of a sole proprietor, the TERMINATION of a broker company, or the EXPIRATION, REVOCATION OR SUSPENSION of its licence, THE COMMISSION SHALL TAKE CUSTODY of each trust account and may APPOINT A SUCCESSOR TRUSTEE.",
               "A managing broker's statutory duties include DEPOSITING ALL ESCROW FUNDS, SECURITY DEPOSITS AND OTHER MONEY RECEIVED into the company's trust account."],
         "check": [("An Indiana trust account may be:", "Interest or noninterest bearing, with any interest held for the beneficiary", ["Interest bearing only", "Noninterest bearing only"], "IC 25-34.1-4-5(a)(1), (b)."),
                   ("A broker company may deposit its own operating funds in a trust account:", "No; personal and other business funds are prohibited", ["Yes, up to $1,000", "Yes, to avoid bank charges"], "IC 25-34.1-4-5(b)."),
                   ("Trust account records must identify:", "The amount of funds held for each beneficiary", ["Only the total balance", "Only the firm's share"], "IC 25-34.1-4-5(b)."),
                   ("If a broker company's licence is revoked, its trust accounts are:", "Taken into the Commission's custody, which may appoint a successor trustee", ["Frozen by the bank indefinitely", "Distributed by the broker"], "IC 25-34.1-4-5(c)."),
                   ("Which belongs in the trust account?", "Earnest money, closing escrow funds and undisbursed sale proceeds", ["The firm's commission income", "The broker's rent"], "IC 25-34.1-4-5(a).")]},
        {"h": "Advertising, agreements and offers",
         "l": ["The outline lists ADVERTISING, COMMISSIONS AND OTHER COMPENSATIONS, BROKERAGE AGREEMENTS - LISTING AGREEMENTS, EXCLUSIVE BUYER/TENANT AGENCY AGREEMENTS, LEASING, and PROPERTY MANAGEMENT AGREEMENTS - OFFERS TO PURCHASE, EARNEST MONEY AND TRUST ACCOUNTS, APPRAISALS, the SELLER'S RESIDENTIAL REAL ESTATE SALES DISCLOSURE and PSYCHOLOGICALLY AFFECTED PROPERTIES.",
               "A BROKER LICENSED under the article may APPRAISE REAL ESTATE IN INDIANA FOR COMPENSATION without being a licensed or certified appraiser - the statute says so expressly (IC 25-34.1-3-8(a)).",
               "A BROKERAGE AGREEMENT is where the written agreement under IC 25-34.1-10-9.5 lives, so the agreement itself decides whether there is agency and which duties apply.",
               "COMPENSATION never creates agency (IC 25-34.1-10-13(d)), and the parties must be told whether compensation will be SHARED with firms representing adverse parties."],
         "check": [("An Indiana licensed broker appraising real estate for compensation:", "May do so without appraiser licensure or certification", ["Must hold an appraiser certificate", "May only give a broker price opinion"], "IC 25-34.1-3-8(a)."),
                   ("Where does Indiana's decision about agency actually get made?", "In the written brokerage agreement, or its absence", ["In the purchase agreement", "At the first showing"], "IC 25-34.1-10-9.5(a).")]},
    ],
    "traps": [
        "Sales disclosure BEFORE the offer is accepted; two business days to rescind if a defect surfaces late.",
        "Four units or fewer, and court-ordered and foreclosure transfers are out.",
        "Trust account interest belongs to the BENEFICIARY, not the firm.",
        "A broker may appraise for compensation in Indiana without an appraiser licence.",
    ],
    "vocab": [
        ["Disclosure form", "The owner's residential sales disclosure under IC 32-21-5."],
        ["Defect", "What triggers the two-business-day rescission if revealed late."],
        ["Beneficiary", "The person whose money a trust account holds."],
        ["Broker company", "The licensed firm that must maintain the trust accounts."],
    ],
    "examples": [
        {"t": "The late disclosure",
         "s": "An offer is accepted on Monday. On Thursday the seller hands over an amended disclosure form revealing a cracked sewer line.",
         "w": ["The amended form was received AFTER acceptance and discloses a defect.",
               "The buyer has TWO BUSINESS DAYS from receipt to nullify by delivering a WRITTEN rescission.",
               "On nullifying, the buyer is not liable and gets the deposits back."],
         "k": "Two business days, in writing, deposits returned."},
    ],
}

STUDY["in/licensing"] = {
    "summary": "Nine items. The numbers: 18 years old, 90 hours, 30 hours of post-licensing in the first two years, then 12 hours a year and 36 per three-year cycle.",
    "sections": [
        {"h": "Getting the licence (IC 25-34.1-3-4.1, IC 25-34.1-5-5)",
         "l": ["An applicant must be AT LEAST 18 YEARS OF AGE before applying, and must NOT have a conviction for an act that would ground disciplinary sanction under IC 25-1-11, a CRIME WITH A DIRECT BEARING on the ability to practise competently, or a crime indicating a PROPENSITY TO ENDANGER THE PUBLIC.",
               "The applicant must hold a HIGH SCHOOL DIPLOMA OR GED.",
               "They must complete an APPROVED BROKER COURSE OF STUDY: a total of AT LEAST 90 HOURS covering PRINCIPLES, PRACTICES, INDIANA LICENCE LAW AND PROFESSIONAL STANDARDS, LAW OF AGENCY, CONTRACTS, FINANCING, SETTLEMENT PROCEDURES, ESCROW RESPONSIBILITY, RECORDKEEPING, GOVERNMENT REGULATIONS and APPRAISING (IC 25-34.1-5-5).",
               "They must APPLY, naming the BROKER COMPANY they intend to associate with and its address, PASS THE WRITTEN EXAMINATION, and WITHIN ONE YEAR AFTER PASSING submit the licence fee - otherwise the Commission VOIDS THE APPLICATION and the applicant must apply and sit again.",
               "The licence must be DISPLAYED at the broker's place of business.",
               "FOR AT LEAST TWO YEARS after issue, the individual CANNOT BE A MANAGING BROKER."],
         "check": [("Indiana prelicence education is:", "At least 90 hours", ["60 hours", "75 hours", "120 hours"], "IC 25-34.1-5-5."),
                   ("An Indiana broker applicant must be at least:", "18 years of age", ["21", "19", "There is no minimum"], "IC 25-34.1-3-4.1(a)(1)."),
                   ("After passing the examination, the licence fee must be submitted within:", "One year", ["90 days", "Two years"], "IC 25-34.1-3-4.1(a)(6)."),
                   ("A newly licensed Indiana broker may become a managing broker:", "Not for at least two years after the licence is issued", ["Immediately", "After one year"], "IC 25-34.1-3-4.1(f)."),
                   ("The applicant must also hold:", "A high school diploma or GED", ["An associate degree", "No educational credential"], "IC 25-34.1-3-4.1(a)(2).")]},
        {"h": "Post-licensing and continuing education (IC 25-34.1-9-11)",
         "l": ["An individual who applied for a broker's licence AFTER 30 JUNE 2014 must, DURING THE FIRST TWO YEARS after the licence is issued, TAKE AND PASS AT LEAST 30 HOURS OF POSTLICENSING EDUCATION focused on the PRACTICAL MATTERS of real estate transactions, INSTEAD OF the continuing education requirement.",
               "Otherwise the approved education requirement is AT LEAST 12 HOURS PER YEAR and AT LEAST 36 HOURS PER THREE-YEAR RENEWAL CYCLE, in subjects the Commission determines - including LICENCE AND ESCROW LAW, ANTI-TRUST LAW, CIVIL RIGHTS LAW, AGENCY LAW, LISTING CONTRACTS AND PURCHASE AGREEMENTS, ETHICS AND PROFESSIONAL STANDARDS, SETTLEMENT PROCEDURES, APPRAISING, PROPERTY MANAGEMENT, FINANCING and others.",
               "A MANAGING BROKER must complete at least 12 HOURS A YEAR and 36 PER CYCLE, of which AT LEAST 4 HOURS EACH YEAR must be dedicated to the BUSINESS AND MANAGEMENT SKILLS AND LEGAL KNOWLEDGE a managing broker needs.",
               "An INDIANA ATTORNEY in good standing may satisfy the requirement with CONTINUING LEGAL EDUCATION in the listed subjects.",
               "A broker licensed after 30 June 2014 who goes INACTIVE before finishing the 30 postlicensing hours must COMPLETE THEM BEFORE REACTIVATION.",
               "A broker licence EXPIRES on a date set by the licensing agency and then EVERY THREE YEARS. An expired licence may be REINSTATED within THREE YEARS of expiry on meeting IC 25-1-8-6(c)."],
         "check": [("A new Indiana broker's first two years require:", "At least 30 hours of postlicensing education instead of continuing education", ["12 hours of CE each year", "Nothing"], "IC 25-34.1-9-11(c)."),
                   ("Indiana continuing education is:", "At least 12 hours per year and 36 hours per three-year cycle", ["16 hours per cycle", "24 hours per year"], "IC 25-34.1-9-11(a)(1)."),
                   ("A managing broker must devote, each year, at least:", "4 hours to business and management skills and legal knowledge", ["2 hours to ethics", "8 hours to agency"], "IC 25-34.1-9-11(d)."),
                   ("An Indiana broker licence renews:", "Every three years", ["Annually", "Every two years"], "IC 25-34.1-3-4.1(g)."),
                   ("An expired licence may be reinstated within:", "Three years of expiry", ["One year", "Five years"], "IC 25-34.1-3-4.1(h)."),
                   ("An Indiana attorney may meet the education requirement by:", "Completing continuing legal education in the listed subjects", ["Being exempt entirely", "Taking half the hours"], "IC 25-34.1-9-11(b).")]},
        {"h": "Status and transfers",
         "l": ["The outline covers ACTIVITIES REQUIRING A LICENCE, EXEMPTIONS AND WAIVERS, and TYPES OF LICENCES - INDIVIDUAL, ORGANIZATIONAL, RESIDENT AND NONRESIDENT.",
               "It also covers LICENCE MAINTENANCE: POST-LICENSING EDUCATION, RENEWALS, TRANSFERS AND CHANGES - including AGENTS CHANGING BROKERS and a BROKER TERMINATING AN AGENT - CONTINUING EDUCATION for both managing broker and broker, and ACTIVE, INACTIVE, ASSIGNED, UNASSIGNED and REFERRAL STATUS.",
               "An individual holding an INACTIVE licence is NOT REQUIRED to fulfil the continuing education requirements while inactive (IC 25-34.1-3-10), but the Commission sets requirements for REACTIVATION.",
               "REFERRAL STATUS means the Commission granted a waiver under IC 25-34.1-9-19; such a licensee MAY ONLY MAKE REFERRALS to a licensed broker and may NOT perform any other act requiring a broker's licence unless they complete the required 24 hours of education and meet the other conditions.",
               "A PARTNERSHIP broker licence requires that ALL PARTNERS BE LICENSED BROKERS and that AT LEAST ONE PARTNER QUALIFY AS A MANAGING BROKER."],
         "check": [("An inactive Indiana licensee:", "Is not required to complete continuing education while inactive", ["Must still complete 12 hours a year", "Loses the licence automatically"], "IC 25-34.1-3-10."),
                   ("A licensee in referral status may:", "Only make referrals to a licensed broker", ["Take listings", "Write offers for buyers"], "IC 25-34.1-3-10.5(e)."),
                   ("A partnership broker licence requires:", "All partners to be licensed brokers, with at least one qualifying as managing broker", ["One licensed partner only", "No licensed partners"], "IC 25-34.1-3-4.1(b).")]},
    ],
    "traps": [
        "90 hours to qualify, then 30 POST-licensing hours in the first two years INSTEAD of CE.",
        "12 a year AND 36 a cycle - both numbers are tested.",
        "No managing broker role for the first two years.",
        "Licence fee within ONE YEAR of passing, or the application is void.",
    ],
    "vocab": [
        ["Managing broker", "The broker who runs a broker company; not available for two years."],
        ["Postlicensing education", "The 30 practical hours required in a new broker's first two years."],
        ["Referral status", "A waiver status permitting referrals only."],
        ["IPLA", "The Indiana Professional Licensing Agency."],
    ],
    "examples": [],
}

STUDY["in/office"] = {
    "summary": "Seven items on running the office: records, money, the place of business, assistants and who answers for whom.",
    "sections": [
        {"h": "The managing broker's statutory duties (IC 25-34.1-4)",
         "l": ["A MANAGING BROKER is the individual responsible for a BROKER COMPANY. Statutory duties include DEPOSITING ALL ESCROW FUNDS, SECURITY DEPOSITS AND OTHER MONEY RECEIVED by the company or its brokers into the company's TRUST ACCOUNT.",
               "The managing broker is responsible for SUPERVISION of the brokers whose licences the company holds, and the outline names GENERAL SUPERVISION and EMPLOYMENT AND COMMISSIONS ISSUES as its own topic.",
               "The outline also lists BROKER COMPANY / BROKER COMPANY RELATIONSHIPS - that is, cooperation and compensation between firms, which ties back to the rule that parties must be told whether compensation will be SHARED with firms representing adverse parties (IC 25-34.1-10-13(c)).",
               "On the DEATH of a sole proprietor or the termination of a broker company, business contracted before the death may be carried out for a MAXIMUM PERIOD OF NINETY DAYS, during which a TRUST ACCOUNT must still be maintained (IC 25-34.1-4-6).",
               "The licence must be DISPLAYED AT THE BROKER'S PLACE OF BUSINESS (IC 25-34.1-3-4.1(f))."],
         "check": [("Where must an Indiana broker's licence be displayed?", "At the broker's place of business", ["Filed with the Commission only", "Carried in the car"], "IC 25-34.1-3-4.1(f)."),
                   ("Who must deposit escrow funds, security deposits and other money received?", "The managing broker, into the broker company's trust account", ["Each individual broker, into their own account", "The closing agent"], "IC 25-34.1-4; IC 25-34.1-4-5."),
                   ("After the death of a sole proprietor, business contracted beforehand may be completed for a maximum of:", "Ninety days", ["Thirty days", "One year"], "IC 25-34.1-4-6.")]},
        {"h": "Records, monies and the rest of the outline",
         "l": ["The outline names DOCUMENTS AND RECORDS, HANDLING OF MONIES, PLACE OF BUSINESS, BRANCH OFFICES, UNLICENSED ASSISTANTS, CLOSING PROCEDURES, and the MANAGING BROKER / BROKER RELATIONSHIP.",
               "UNLICENSED ASSISTANTS may do clerical and administrative work but NOT the activities that require a licence - showing property, negotiating, or discussing terms.",
               "HANDLING OF MONIES is the trust account rule: ALL FUNDS BELONGING TO OTHERS go into a trust account, NO personal or other business funds go in, and a DETAILED RECORD identifies the amount held FOR EACH BENEFICIARY (IC 25-34.1-4-5).",
               "CLOSING PROCEDURES tie to the sales disclosure duty to disclose any MATERIAL CHANGE in the physical condition AT OR BEFORE SETTLEMENT, or certify the condition is SUBSTANTIALLY THE SAME (IC 32-21-5-12(a))."],
         "check": [("An unlicensed assistant in Indiana may:", "Perform clerical and administrative work, but not licensed activities", ["Show property to buyers", "Negotiate contract terms"], "Named on the Indiana state outline."),
                   ("At or before settlement an owner must:", "Disclose any material change in the property's physical condition, or certify it is substantially the same", ["Re-sign the listing", "Nothing further"], "IC 32-21-5-12(a)."),
                   ("Trust account records must show:", "The amount of funds held for each beneficiary", ["A single running total", "Only deposits"], "IC 25-34.1-4-5(b).")]},
    ],
    "traps": [
        "Money belonging to others goes to the company trust account - never a broker's own.",
        "Ninety days is the wind-up window after a sole proprietor's death.",
    ],
    "vocab": [
        ["Broker company", "The licensed firm."],
        ["Unlicensed assistant", "Support staff limited to non-licensed tasks."],
        ["Branch office", "An additional place of business of a broker company."],
    ],
    "examples": [],
}

STUDY["in/commission"] = {
    "summary": "Five items on the regulator. Indiana's distinctive piece is the CONSUMER RESTITUTION / RECOVERY FUND.",
    "sections": [
        {"h": "Powers and sanctions",
         "l": ["The outline lists the Commission's GENERAL POWERS AND DUTIES, EXAMINATION OF RECORDS, INVESTIGATIONS, HEARINGS AND APPEALS, and DISCIPLINARY SANCTIONS.",
               "Those sanctions are named as CEASE AND DESIST ORDERS, LICENCE SUSPENSION OR REVOCATION, OTHER SANCTIONS AND CIVIL PENALTIES, and the CONSUMER RESTITUTION / RECOVERY FUND.",
               "The Commission may require CONTINUING EDUCATION as a condition of renewal (IC 25-34.1-3).",
               "Where a broker company's licence EXPIRES, IS REVOKED OR SUSPENDED, or the company terminates, THE COMMISSION TAKES CUSTODY of each trust account and may APPOINT A SUCCESSOR TRUSTEE (IC 25-34.1-4-5(c)) - the clearest example of its power over client money.",
               "A licence applicant is disqualified by a conviction for an act grounding disciplinary sanction under IC 25-1-11, a crime with a DIRECT BEARING on competent practice, or one showing a PROPENSITY TO ENDANGER THE PUBLIC (IC 25-34.1-3-4.1(a)(1))."],
         "check": [("Which sanction does the Indiana outline name alongside suspension and revocation?", "Cease and desist orders, civil penalties, and the consumer restitution or recovery fund", ["Criminal sentencing", "Contract rescission"], "Pearson Indiana state content outline."),
                   ("If a broker company's licence is revoked, its trust accounts are:", "Taken into the Commission's custody, with a possible successor trustee", ["Closed by the bank", "Paid to the managing broker"], "IC 25-34.1-4-5(c)."),
                   ("A conviction bars licensure where it:", "Has a direct bearing on competent practice or shows a propensity to endanger the public", ["Is any conviction at all", "Is more than ten years old"], "IC 25-34.1-3-4.1(a)(1)."),
                   ("The Commission may require continuing education:", "As a condition of licence renewal", ["Only for managing brokers", "Not at all"], "IC 25-34.1-3.")]},
        {"h": "Education infrastructure",
         "l": ["A REAL ESTATE EDUCATION ADVISORY COUNCIL is established, consisting of FIVE MEMBERS, THREE of whom must be RECOMMENDED BY THE INDIANA ASSOCIATION OF REALTORS and appointed by the Commission, each for a TWO YEAR TERM (IC 25-34.1-9-2 to 9-4).",
               "The Commission may remove a council member FOR CAUSE, and appoints replacements for unexpired terms.",
               "The Commission approves COURSE SPONSORS, inspects their RECORDS AND FACILITIES, may DENY, SUSPEND OR REVOKE approval of courses or sponsors, issues CONTINUING EDUCATION INSTRUCTOR PERMITS, and maintains an ELECTRONIC CONTINUING EDUCATION TRACKING SYSTEM (IC 25-34.1-9).",
               "Course approval and school permits EXPIRE ON 31 DECEMBER each year, and renewal requires a letter, an ANNUAL REPORT and a BOND of 20 PERCENT of the previous year's figure to be submitted BY 30 NOVEMBER (IC 25-34.1-5-7)."],
         "check": [("Indiana's real estate education advisory council has:", "Five members, three recommended by the Indiana Association of Realtors", ["Seven members, all appointed by the Governor", "Three members"], "IC 25-34.1-9-3."),
                   ("A council member's term is:", "Two years", ["Four years", "One year"], "IC 25-34.1-9-4."),
                   ("Course approvals and school permits expire:", "On 31 December each year", ["On the anniversary of approval", "Every three years"], "IC 25-34.1-5-7(a).")]},
    ],
    "traps": [
        "The recovery fund is listed as a Commission sanction topic, not just a consumer remedy.",
        "Course approvals lapse every 31 December; renewal paperwork is due by 30 November.",
    ],
    "vocab": [
        ["IPLA", "Indiana Professional Licensing Agency, which sets the passing score."],
        ["Cease and desist order", "A Commission sanction stopping conduct."],
        ["Recovery fund", "The consumer restitution fund named on the outline."],
        ["Successor trustee", "Who the Commission may appoint over a failed firm's trust account."],
    ],
    "examples": [],
}


# ------------------------------------------------------------- questions

Q = [
 # statutes-rules
 ("in/statutes-rules", "Default agency", 1, "In Indiana, a licensee working with a buyer who has signed nothing is:",
  "That buyer's agent, by default", ["A transaction broker", "A customer-only licensee", "A subagent of the seller"],
  "IC 25-34.1-10-9.5(a)."),
 ("in/statutes-rules", "Default agency", 1, "An Indiana agency relationship does NOT arise where:",
  "There is a written agreement to the contrary, or the licensee merely assists a customer without compensation", ["The licensee is paid by the other side", "No offer has been written"],
  "IC 25-34.1-10-9.5(a)."),
 ("in/statutes-rules", "Default agency", 2, "A licensee who has contracted OUT of agency must still:",
  "Receive and timely present offers, assist with forms and negotiation, and timely answer questions", ["Do nothing further", "Act as a limited agent"],
  "IC 25-34.1-10-9.5(b)."),
 ("in/statutes-rules", "Default agency", 3, "If that licensee fails those duties and another licensee performs them:",
  "No agency relationship is created for the other licensee", ["The other licensee becomes the agent", "Both become dual agents"],
  "IC 25-34.1-10-9.5(c)."),
 ("in/statutes-rules", "Termination", 2, "Which duties survive the end of an Indiana agency relationship?",
  "Accounting for money and property, and keeping confidential information confidential", ["Loyalty and obedience", "All the statutory duties"],
  "IC 25-34.1-10-14(c)."),
 ("in/statutes-rules", "Seller duties", 1, "An Indiana seller's agent must present offers:",
  "Immediately on receipt, even after an offer has been accepted, unless the seller directs otherwise", ["Only until the first acceptance", "Weekly"],
  "IC 25-34.1-10-10(a)(3)(B)."),
 ("in/statutes-rules", "Seller duties", 1, "Which may NOT be disclosed without the seller's informed written consent?",
  "That the seller will accept less than the listed price", ["A known foundation crack", "A statutory disclosure"],
  "IC 25-34.1-10-10(b)(1)."),
 ("in/statutes-rules", "Seller duties", 2, "A seller's agent owes a prospective buyer:",
  "Honest treatment and no knowingly false information", ["Full fiduciary duties", "No duty at all"],
  "IC 25-34.1-10-10(c)."),
 ("in/statutes-rules", "Seller duties", 2, "Adverse material facts about physical condition must be disclosed to a buyer where they:",
  "Are actually known and could not be found by a reasonable and timely inspection", ["Are merely suspected", "Appear in the listing"],
  "IC 25-34.1-10-10(d)."),
 ("in/statutes-rules", "Seller duties", 2, "Does an Indiana seller's agent have to inspect the property for the buyer?",
  "No, and need not verify the seller's or an inspector's statements", ["Yes, a visual inspection", "Yes, a full inspection"],
  "IC 25-34.1-10-10(d)."),
 ("in/statutes-rules", "Seller duties", 3, "Must an Indiana seller's agent keep seeking offers after one is accepted?",
  "No, unless the parties agree otherwise", ["Yes, always", "Yes, until closing"],
  "IC 25-34.1-10-10(a)(3)(A)."),
 ("in/statutes-rules", "Limited agency", 1, "Indiana's term for dual agency is:",
  "Limited agency", ["Transaction brokerage", "Designated agency", "Facilitation"],
  "IC 25-34.1-10-12."),
 ("in/statutes-rules", "Limited agency", 1, "A limited agent may act only with:",
  "The written consent of all parties to the transaction", ["Oral consent of both", "The managing broker's approval"],
  "IC 25-34.1-10-12(a)."),
 ("in/statutes-rules", "Limited agency", 2, "Which may a limited agent disclose to both sides?",
  "Property information, including listed and sold properties from a multiple listing service", ["What motivates a party", "That the buyer will pay more"],
  "IC 25-34.1-10-12(b)."),
 ("in/statutes-rules", "Limited agency", 2, "The limited agency writing must state that:",
  "A party does not have to consent to the limited agency", ["The fee is non-negotiable", "The Commission has approved it"],
  "IC 25-34.1-10-12(a)(5)."),
 ("in/statutes-rules", "Limited agency", 3, "In Indiana limited agency, knowledge is:",
  "Not imputed between any party and the limited agent or among licensees", ["Imputed to the whole firm", "Imputed to the managing broker"],
  "IC 25-34.1-10-12(a)(4)."),
 ("in/statutes-rules", "Limited agency", 3, "Making a required disclosure as a limited agent:",
  "Does not terminate the limited agency relationship", ["Ends the relationship", "Requires fresh written consent"],
  "IC 25-34.1-10-12(c)."),
 ("in/statutes-rules", "Office policy", 1, "An Indiana managing broker must develop and enforce:",
  "A written office policy describing agency relationships and permitting or rejecting disclosed limited agency", ["A commission schedule", "An advertising budget"],
  "IC 25-34.1-10-13(a)."),
 ("in/statutes-rules", "Office policy", 2, "That written office policy must be disclosed:",
  "In writing at the beginning of the relationship, before any confidential information is given", ["With the offer", "At closing"],
  "IC 25-34.1-10-13(b)."),
 ("in/statutes-rules", "Compensation", 1, "Paying an Indiana licensee's compensation:",
  "Does not create an agency relationship", ["Makes the payer the client", "Creates limited agency"],
  "IC 25-34.1-10-13(d)."),
 ("in/statutes-rules", "Compensation", 2, "Parties to an Indiana transaction must be told whether:",
  "Compensation will be shared with other broker companies representing adverse parties", ["The licensee belongs to a trade body", "The firm is incorporated"],
  "IC 25-34.1-10-13(c)."),
 ("in/statutes-rules", "Stigma", 1, "In Indiana, disclosure of a psychologically affected property is:",
  "Not required, and refusing to disclose carries no liability", ["Required on request", "Required in every sale"],
  "IC 32-21-6-5; 32-21-6-6."),
 ("in/statutes-rules", "Stigma", 2, "Which makes a property psychologically affected in Indiana?",
  "An individual died on the property", ["A low appraisal", "An expired listing", "A boundary dispute"],
  "IC 32-21-6-3(1)."),
 ("in/statutes-rules", "Stigma", 3, "The Indiana definition also reaches:",
  "A reasonable suspicion of the listed facts, not only the facts themselves", ["Only proven facts", "Only events within five years"],
  "IC 32-21-6-3."),

 # statutory
 ("in/statutory", "Disclosure", 1, "The Indiana sales disclosure form must be given to the buyer:",
  "Before an offer for the sale is accepted", ["At closing", "Within 10 days of the offer"],
  "IC 32-21-5-10(a)."),
 ("in/statutory", "Disclosure", 1, "The sales disclosure chapter applies to residential real estate of:",
  "Not more than four dwelling units", ["Any residential property", "Single-family homes only"],
  "IC 32-21-5-1(a)."),
 ("in/statutory", "Disclosure", 1, "A disclosure form received after acceptance that reveals a defect lets the buyer nullify within:",
  "Two business days, by written rescission", ["Three days", "Ten days", "It does not"],
  "IC 32-21-5-13(a)."),
 ("in/statutory", "Disclosure", 2, "Before closing, an accepted Indiana offer is not enforceable against the buyer until:",
  "Both the owner and the prospective buyer have signed the disclosure form", ["The inspection is complete", "The appraisal is received"],
  "IC 32-21-5-10(c)."),
 ("in/statutory", "Disclosure", 2, "At or before settlement an Indiana owner must:",
  "Disclose any material change in physical condition, or certify it is substantially the same", ["Re-sign the original form", "Do nothing further"],
  "IC 32-21-5-12(a)."),
 ("in/statutory", "Disclosure", 2, "The Indiana disclosure form is:",
  "Not a warranty, and not a substitute for inspections", ["A seller's warranty of condition", "An inspection report"],
  "IC 32-21-5-9."),
 ("in/statutory", "HOA", 3, "HOA governing documents must reach an Indiana purchaser:",
  "Not later than ten days before closing", ["At closing", "Within 30 days after closing"],
  "IC 32-21-5-8.5(e)."),
 ("in/statutory", "Trust money", 1, "An Indiana trust account may be:",
  "Interest or noninterest bearing, with any interest held for the beneficiary", ["Interest bearing only", "Noninterest bearing only"],
  "IC 25-34.1-4-5(a)(1), (b)."),
 ("in/statutory", "Trust money", 1, "May an Indiana broker company put its own operating funds in a trust account?",
  "No; personal and other business funds are prohibited", ["Yes, up to $1,000", "Yes, to cover bank charges"],
  "IC 25-34.1-4-5(b)."),
 ("in/statutory", "Trust money", 2, "Indiana trust account records must identify:",
  "The amount of funds held for each beneficiary", ["Only the total balance", "Only the firm's share"],
  "IC 25-34.1-4-5(b)."),
 ("in/statutory", "Trust money", 2, "Which belongs in an Indiana trust account?",
  "Earnest money, funds held for closing escrows and undisbursed sale proceeds", ["The firm's commission income", "The broker's office rent"],
  "IC 25-34.1-4-5(a)."),
 ("in/statutory", "Appraisal", 3, "An Indiana licensed broker appraising real estate for compensation:",
  "May do so without appraiser licensure or certification", ["Must hold an appraiser certificate", "May give only a broker price opinion"],
  "IC 25-34.1-3-8(a)."),

 # licensing
 ("in/licensing", "Education", 1, "Indiana prelicence education is:",
  "At least 90 hours", ["60 hours", "75 hours", "120 hours"],
  "IC 25-34.1-5-5."),
 ("in/licensing", "Eligibility", 1, "An Indiana broker applicant must be at least:",
  "18 years of age", ["21", "19", "There is no minimum"],
  "IC 25-34.1-3-4.1(a)(1)."),
 ("in/licensing", "Eligibility", 2, "An Indiana broker applicant must also hold:",
  "A high school diploma or GED", ["An associate degree", "No educational credential"],
  "IC 25-34.1-3-4.1(a)(2)."),
 ("in/licensing", "Application", 2, "After passing the Indiana examination, the licence fee must be submitted within:",
  "One year", ["90 days", "Two years", "Six months"],
  "IC 25-34.1-3-4.1(a)(6)."),
 ("in/licensing", "Managing broker", 2, "A newly licensed Indiana broker may become a managing broker:",
  "Not for at least two years after the licence is issued", ["Immediately", "After one year"],
  "IC 25-34.1-3-4.1(f)."),
 ("in/licensing", "Post-licensing", 1, "A new Indiana broker's first two years require:",
  "At least 30 hours of postlicensing education instead of continuing education", ["12 hours of CE each year", "Nothing"],
  "IC 25-34.1-9-11(c)."),
 ("in/licensing", "Continuing education", 1, "Indiana continuing education is:",
  "At least 12 hours per year and 36 hours per three-year cycle", ["16 hours per cycle", "24 hours per year"],
  "IC 25-34.1-9-11(a)(1)."),
 ("in/licensing", "Continuing education", 2, "An Indiana managing broker must devote each year at least:",
  "4 hours to business and management skills and legal knowledge", ["2 hours to ethics", "8 hours to agency"],
  "IC 25-34.1-9-11(d)."),
 ("in/licensing", "Renewal", 2, "An Indiana broker licence renews:",
  "Every three years", ["Annually", "Every two years", "Every four years"],
  "IC 25-34.1-3-4.1(g)."),

 # office
 ("in/office", "Display", 1, "Where must an Indiana broker's licence be displayed?",
  "At the broker's place of business", ["Filed with the Commission only", "Carried on the person"],
  "IC 25-34.1-3-4.1(f)."),
 ("in/office", "Monies", 1, "Who must deposit escrow funds, security deposits and other money received?",
  "The managing broker, into the broker company's trust account", ["Each broker, into a personal account", "The closing agent"],
  "IC 25-34.1-4; IC 25-34.1-4-5."),
 ("in/office", "Assistants", 1, "An unlicensed assistant in Indiana may:",
  "Perform clerical and administrative work, but not activities requiring a licence", ["Show property to buyers", "Negotiate contract terms"],
  "Named on the Indiana state outline."),
 ("in/office", "Wind-up", 3, "After the death of a sole proprietor, business contracted beforehand may be completed for a maximum of:",
  "Ninety days", ["Thirty days", "One year", "Six months"],
  "IC 25-34.1-4-6."),
 ("in/office", "Closing", 2, "Indiana closing procedure requires the owner, at or before settlement, to:",
  "Disclose any material change in the property's physical condition or certify it is substantially the same", ["Re-sign the listing agreement", "Provide a new appraisal"],
  "IC 32-21-5-12(a)."),
 ("in/office", "Records", 2, "Indiana trust account records must show:",
  "The amount of funds held for each beneficiary", ["A single running total", "Deposits only"],
  "IC 25-34.1-4-5(b)."),
 ("in/office", "Supervision", 3, "Supervision of the brokers whose licences a company holds falls to:",
  "The managing broker", ["Each individual broker", "The Commission"],
  "IC 25-34.1-4; Indiana state outline."),

 # commission
 ("in/commission", "Sanctions", 1, "Which sanction does the Indiana outline name alongside suspension and revocation?",
  "Cease and desist orders, civil penalties, and the consumer restitution or recovery fund", ["Criminal sentencing", "Rescission of the contract"],
  "Pearson Indiana state content outline."),
 ("in/commission", "Trust accounts", 2, "If an Indiana broker company's licence is revoked, its trust accounts are:",
  "Taken into the Commission's custody, which may appoint a successor trustee", ["Closed by the bank", "Paid out to the managing broker"],
  "IC 25-34.1-4-5(c)."),
 ("in/commission", "Eligibility", 2, "A conviction bars Indiana licensure where it:",
  "Has a direct bearing on competent practice or shows a propensity to endanger the public", ["Is any conviction at all", "Is more than ten years old"],
  "IC 25-34.1-3-4.1(a)(1)."),
 ("in/commission", "Education council", 3, "Indiana's real estate education advisory council has:",
  "Five members, three recommended by the Indiana Association of Realtors", ["Seven members appointed by the Governor", "Three members"],
  "IC 25-34.1-9-3."),
 ("in/commission", "Course approval", 3, "Indiana course approvals and school permits expire:",
  "On 31 December each year", ["On the anniversary of approval", "Every three years"],
  "IC 25-34.1-5-7(a)."),
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
            "id": "in-" + hashlib.sha1(q.encode()).hexdigest()[:8],
            "portion": "georgia", "topic": topic, "subtopic": sub,
            "sub": topic + "|" + sub, "concept": "Indiana " + sub.lower(),
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
        "code": "IN", "name": "Indiana", "abbr": "IN",
        "regulator": "Indiana Real Estate Commission",
        "pass": EXAM["pass"],
        "pass_published": EXAM["pass_published"],
        "pass_note": EXAM["pass_note"],
        "portions": {
            "national": {"scored": EXAM["national_scored"],
                         "minutes": EXAM["national_minutes"],
                         "blurb": "80 scored general items."},
            "georgia": {"name": "Indiana law", "scored": EXAM["state_scored"],
                        "minutes": EXAM["state_minutes"],
                        "blurb": "50 scored items on IC 25-34.1, agency relationships and the disclosure statutes."},
        },
        "topics": topics, "bank": bank, "study": study,
        "sources": SOURCES, "diffs": DIFFS,
    }


# Where Indiana departs from the national rule.
DIFFS = {
    "national/agency": [
        "Indiana makes AGENCY THE DEFAULT: a licensee represents the person they work with UNLESS a written agreement says otherwise or they merely assist a customer without compensation (IC 25-34.1-10-9.5).",
        "Even without agency, three duties survive under the written agreement - receive and present offers, assist with forms and negotiation, and answer questions timely.",
        "Dual agency is called LIMITED AGENCY and needs the WRITTEN consent of all parties, with six specific statements in the writing (IC 25-34.1-10-12).",
        "The MANAGING BROKER must keep a WRITTEN OFFICE POLICY that permits or rejects disclosed limited agency, disclosed in writing before any confidential information is given (IC 25-34.1-10-13).",
        "PAYING compensation never creates agency, and only accounting and confidentiality survive termination (IC 25-34.1-10-13(d), 10-14).",
    ],
    "national/disclosures": [
        "The owner's SALES DISCLOSURE FORM must be delivered BEFORE AN OFFER IS ACCEPTED, and a defect revealed afterwards gives the buyer TWO BUSINESS DAYS to rescind in writing (IC 32-21-5-10, 32-21-5-13).",
        "An accepted offer is NOT ENFORCEABLE against the buyer before closing until BOTH parties have signed the form (IC 32-21-5-10(c)).",
        "PSYCHOLOGICALLY AFFECTED PROPERTY - death, a felony, criminal organisation activity, a police firearm discharge or drug manufacture - NEVER has to be disclosed, and refusing to disclose carries no liability (IC 32-21-6).",
    ],
    "national/practice": [
        "Education: 90 prelicence hours, then 30 hours of POSTLICENSING education in the first two years INSTEAD of continuing education, then 12 hours a year and 36 per three-year cycle (IC 25-34.1-5-5, 25-34.1-9-11).",
        "A new broker CANNOT be a managing broker for two years (IC 25-34.1-3-4.1(f)).",
        "Trust accounts may be interest or noninterest bearing, and ANY INTEREST IS HELD FOR THE BENEFICIARY; the Commission takes custody if the firm fails (IC 25-34.1-4-5).",
        "A licensed Indiana BROKER MAY APPRAISE for compensation without appraiser licensure (IC 25-34.1-3-8(a)).",
    ],
}


if __name__ == "__main__":
    import io, json, os
    here = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    out = os.path.join(here, "greprep", "packs", "IN.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    pack = build()
    with io.open(out, "w", encoding="utf-8") as f:
        json.dump(pack, f, ensure_ascii=False, indent=1, sort_keys=True)
    print("wrote", out, len(pack["bank"]), "questions,", len(pack["study"]), "lessons")
