"""Missouri state content: lessons and practice questions.

Missouri splits the salesperson examination and sets a DIFFERENT pass mark
on each portion. The PSI handbook published by the Missouri Division of
Professional Registration: National 100 items, 70%, 150 minutes; State 40
items, 75%, 120 minutes. So the pack puts 0.70 on the national portion and
0.75 on the state portion.

Missouri's agency law is its own animal. Everything runs through the
DESIGNATED BROKER, the statutes call a seller's or buyer's agent a LIMITED
AGENT, a licensee may be a TRANSACTION BROKER with no agency at all, and a
broker may appoint DESIGNATED AGENTS without becoming a dual agent.

Every rule below was read on 2026-11-11 from the official text:
  - RSMo chapter 339 (Real Estate Brokers and Salespersons), from
    revisor.mo.gov - in particular 339.040, 339.105 and the brokerage
    relationship sections 339.710 to 339.860.
  - The Missouri Real Estate Commission's published continuing education
    requirement at pr.mo.gov and 20 CSR 2250-10.100.
  - The PSI Missouri Real Estate Candidate Handbook, published on
    pr.mo.gov, for the examination table, licence requirements and the
    40-item salesperson state outline.
The section a fact comes from is cited next to it. Do not add a fact here
without reading its source first.
"""

EXAM = {
    # Salesperson: National 100 items / 70% / 150 minutes;
    # State 40 items / 75% / 120 minutes.
    "state_scored": 40,
    "state_minutes": 120,
    "state_pass": 0.75,
    "national_scored": 100,
    "national_minutes": 150,
    "national_pass": 0.70,
    "pass": 0.75,
}

# PSI's Missouri salesperson state outline, item counts summing to 40.
TOPICS = [
    ("mo/conduct", "Business conduct and practices", 17,
     "Advertising, listings, offers, earnest money, closings, commissions."),
    ("mo/licenses", "Licenses", 7,
     "Applications, qualification, renewal, broker-salesperson, transfers, denial."),
    ("mo/discipline", "Disciplinary proceedings", 6,
     "Complaints, investigation, violations, the Commission and the AHC."),
    ("mo/relationships", "Brokerage relationships", 6,
     "Agency disclosure, the relationships Missouri permits, duties, dual agency."),
    ("mo/general", "General rules", 2,
     "Definitions, and what counts as a dispute."),
    ("mo/education", "Educational requirements", 2,
     "The salesperson course and continuing education."),
]

SOURCES = [
    {"by": "Missouri Revisor of Statutes",
     "name": "RSMo chapter 339",
     "note": "Licensing, escrow accounts, grounds for discipline and the brokerage relationship sections 339.710 to 339.860.",
     "url": "https://revisor.mo.gov/main/OneChapter.aspx?chapter=339"},
    {"by": "Missouri Real Estate Commission",
     "name": "20 CSR 2250 and the Commission's published requirements",
     "note": "The 12-hour continuing education requirement with a 3-hour core course.",
     "url": "https://pr.mo.gov/realestate.asp"},
    {"by": "PSI Services and the Missouri Division of Professional Registration",
     "name": "Missouri Real Estate Candidate Handbook",
     "note": "National 100 items at 70% and State 40 items at 75%, the licence requirements and the state outline.",
     "url": "https://pr.mo.gov/boards/realestate/MOREP-handbook.pdf"},
]


# --------------------------------------------------------------- lessons

STUDY = {}

STUDY["mo/relationships"] = {
    "summary": "Six items, and they decide how the rest of the paper reads. Missouri has FIVE relationships, calls its agents LIMITED AGENTS, and lets a broker appoint designated agents without becoming a dual agent.",
    "sections": [
        {"h": "Everything is the designated broker's (RSMo 339.780)",
         "l": ["ALL WRITTEN AGREEMENTS for brokerage services on behalf of a seller, landlord, buyer or tenant must be ENTERED INTO BY THE DESIGNATED BROKER on behalf of that broker and the affiliated licensees - unless the designated broker AUTHORISES AFFILIATED LICENSEES IN WRITING to enter them on the broker's behalf.",
               "BEFORE engaging in licensed activity, a designated broker intending LIMITED AGENCY with a SELLER OR LANDLORD must enter a WRITTEN AGENCY AGREEMENT including the duties in 339.730, the TERMS OF COMPENSATION, and WHETHER AN OFFER OF SUBAGENCY may be made to another designated broker.",
               "BEFORE engaging in licensed activity, except MINISTERIAL ACTS, a designated broker acting as a SINGLE AGENT FOR A BUYER OR TENANT must enter a written agency agreement including the 339.740 duties and the terms of compensation.",
               "A designated broker intending to act as a DUAL AGENT must enter a written agreement WITH BOTH SIDES permitting it, including the 339.750 duties and the compensation terms.",
               "A designated broker intending to act as a SUBAGENT must enter a written agreement with the client's designated broker - though where a UNILATERAL OFFER OF SUBAGENCY has been made, another broker may enter the relationship simply BY DISCLOSING TO THE CUSTOMER that they are a subagent of the client.",
               "A designated broker intending to act as a TRANSACTION BROKER who expects compensation from the party assisted must enter a WRITTEN TRANSACTION BROKERAGE AGREEMENT including the 339.755 duties and the compensation terms.",
               "EVERY EXCLUSIVE brokerage agreement must specify at least three minimum services: ACCEPTING DELIVERY OF AND PRESENTING offers and counteroffers; ASSISTING in developing, communicating, negotiating and presenting offers, counteroffers and notices UNTIL a lease or purchase agreement is signed and ALL CONTINGENCIES SATISFIED OR WAIVED; and ANSWERING QUESTIONS about offers, counteroffers, notices and contingencies."],
         "check": [("In Missouri, written brokerage agreements are entered into by:", "The designated broker, unless affiliated licensees are authorised in writing", ["Any affiliated licensee", "The managing salesperson"], "RSMo 339.780.1."),
                   ("A seller's limited agency agreement must specify:", "The duties, the terms of compensation, and whether subagency may be offered", ["Only the commission", "Only the listing period"], "RSMo 339.780.2."),
                   ("A broker expecting compensation as a transaction broker must:", "Enter a written transaction brokerage agreement with the party", ["Rely on an oral understanding", "Use the agency agreement"], "RSMo 339.780.6."),
                   ("Every exclusive brokerage agreement must guarantee at least:", "Presenting offers, assisting with negotiation to signing, and answering questions about them", ["A minimum advertising spend", "An open house a week"], "RSMo 339.780.7."),
                   ("Where a unilateral offer of subagency has been made, another broker becomes a subagent by:", "Disclosing to the customer that they are a subagent of the client", ["Signing the listing", "Notifying the Commission"], "RSMo 339.780.5.")]},
        {"h": "The limited agent for a seller (RSMo 339.730)",
         "l": ["A licensee representing a seller or landlord is a LIMITED AGENT who must PERFORM THE WRITTEN AGREEMENT; EXERCISE REASONABLE SKILL AND CARE; and PROMOTE THE CLIENT'S INTERESTS WITH THE UTMOST GOOD FAITH, LOYALTY AND FIDELITY.",
               "That includes SEEKING an acceptable price and terms - but NOT being obliged to seek additional offers while the property is under a CONTRACT FOR SALE or a LEASE OR LETTER OF INTENT; PRESENTING ALL WRITTEN OFFERS to and from the client TIMELY, REGARDLESS of an existing contract; DISCLOSING to the client all ADVERSE MATERIAL FACTS ACTUALLY KNOWN OR THAT SHOULD HAVE BEEN KNOWN; and ADVISING the client to get EXPERT ADVICE beyond the licensee's expertise.",
               "The licensee must ACCOUNT TIMELY for money and property, COMPLY with the brokerage relationship statutes and 339.100.2, and comply with all law INCLUDING FAIR HOUSING AND CIVIL RIGHTS.",
               "CONFIDENTIAL INFORMATION about the client may NOT be disclosed unless disclosure is REQUIRED BY STATUTE OR RULE, failure to disclose would be a MISREPRESENTATION, or disclosure is NECESSARY TO DEFEND the licensee against an action for wrongful conduct. NO CAUSE OF ACTION arises for a required or permitted disclosure.",
               "A seller's agent OWES NO DUTY TO A CUSTOMER except to DISCLOSE ALL ADVERSE MATERIAL FACTS ACTUALLY KNOWN OR THAT SHOULD HAVE BEEN KNOWN. There is NO duty to conduct an independent inspection for the customer and NO duty to verify statements by the client or an independent inspector.",
               "A seller's agent may SHOW ALTERNATIVE PROPERTIES without breaching any duty. The mirror duties apply to a BUYER'S OR TENANT'S agent (RSMo 339.740)."],
         "check": [("Missouri calls a seller's agent a:", "Limited agent", ["General agent", "Universal agent", "Transaction broker"], "RSMo 339.730.1."),
                   ("A Missouri seller's agent must present written offers:", "Timely, regardless of whether the property is already under contract", ["Only until a contract is signed", "Only above the listed price"], "RSMo 339.730.1(3)(b)."),
                   ("Adverse material facts owed to the CLIENT are those:", "Actually known or that should have been known by the licensee", ["Actually known only", "Discoverable by inspection only"], "RSMo 339.730.1(3)(c)."),
                   ("What does a Missouri seller's agent owe a CUSTOMER?", "Disclosure of adverse material facts actually known or that should have been known", ["Nothing at all", "Full fiduciary duties"], "RSMo 339.730.3."),
                   ("A seller's agent's duty to inspect for the customer is:", "None, and there is no duty to verify the client's or an inspector's statements", ["A visual inspection", "A full inspection"], "RSMo 339.730.3."),
                   ("Confidential client information may be disclosed where:", "A statute or rule requires it, silence would be a misrepresentation, or it is needed to defend the licensee", ["The deal has closed", "The other agent asks"], "RSMo 339.730.2.")]},
        {"h": "Dual agency (RSMo 339.750)",
         "l": ["A licensee may act as a DUAL AGENT ONLY WITH THE CONSENT OF ALL PARTIES, and CONSENT IS PRESUMED by a written agreement under 339.780.",
               "A dual agent is a LIMITED AGENT FOR BOTH SIDES with the 339.730 and 339.740 duties, except as the section provides.",
               "A dual agent MAY disclose to one client information gained from the other IF IT IS MATERIAL TO THE TRANSACTION, UNLESS it is CONFIDENTIAL INFORMATION as defined in 339.710.",
               "FIVE things may NOT be disclosed without the consent of the client they concern: that a BUYER WILL PAY MORE than offered; that a SELLER WILL ACCEPT LESS than asking; WHAT MOTIVATES a client; that a client WILL AGREE TO OTHER FINANCING TERMS; and THE TERMS OF ANY PRIOR OFFERS OR COUNTEROFFERS made by any party.",
               "A dual agent must NOT disclose confidential information about one client to the other except where required by statute or rule, where silence would be a MISREPRESENTATION, or where disclosure is NECESSARY TO DEFEND the licensee. Making a required or permitted disclosure DOES NOT TERMINATE the dual agency.",
               "In dual agency there is NO IMPUTATION of knowledge between the client and the dual agent or among persons within the entity."],
         "check": [("Missouri dual agency requires:", "The consent of all parties, presumed by the written agreement under 339.780", ["Oral consent", "No consent at all"], "RSMo 339.750.1."),
                   ("Which may a Missouri dual agent NOT disclose without consent?", "The terms of any prior offers or counteroffers", ["A known structural defect", "A statutory disclosure"], "RSMo 339.750.4(5)."),
                   ("A Missouri dual agent is:", "A limited agent for both sides", ["A fiduciary for both sides", "Not an agent at all"], "RSMo 339.750.2."),
                   ("Making a required disclosure as a dual agent:", "Does not terminate the dual agency relationship", ["Ends the relationship", "Converts it to transaction brokerage"], "RSMo 339.750.5."),
                   ("In Missouri dual agency, knowledge is:", "Not imputed between the client and the dual agent or within the entity", ["Imputed to the firm", "Imputed to the designated broker"], "RSMo 339.750.6.")]},
        {"h": "Transaction broker (RSMo 339.755)",
         "l": ["A licensee may provide service to any party WITHOUT AN AGENCY OR FIDUCIARY RELATIONSHIP to anyone. Such a licensee is a TRANSACTION BROKER.",
               "A transaction broker must PERFORM any written or oral agreement, and exercise REASONABLE SKILL, CARE AND DILIGENCE - including PRESENTING ALL WRITTEN OFFERS AND COUNTEROFFERS TIMELY regardless of an existing contract or letter of intent, INFORMING the parties and SUGGESTING EXPERT ADVICE on material matters beyond the broker's expertise, ACCOUNTING TIMELY, DISCLOSING TO EACH PARTY ANY ADVERSE MATERIAL FACTS OF WHICH THE LICENSEE HAS ACTUAL NOTICE OR KNOWLEDGE, and ASSISTING the parties to comply with the contract.",
               "THE PARTIES ARE NOT LIABLE FOR ANY ACTS OF THE TRANSACTION BROKER.",
               "FIVE items may not be disclosed without informed consent: that a buyer WILL PAY MORE; that a seller WILL ACCEPT LESS; a party's MOTIVATING FACTORS; that a party will agree to OTHER FINANCING TERMS; and ANY CONFIDENTIAL INFORMATION about the other party, unless the law requires disclosure or silence would be fraud or dishonest dealing.",
               "A transaction broker has NO DUTY to conduct an independent inspection or investigation for adverse material facts, and NO DUTY to investigate the buyer's financial condition.",
               "A transaction broker may SHOW ALTERNATIVE PROPERTIES, LIST COMPETING PROPERTIES, show the buyer's property to OTHER buyers, and SERVE AS A SINGLE AGENT, SUBAGENT, DESIGNATED AGENT, LIMITED AGENT OR DISCLOSED DUAL AGENT in OTHER transactions.",
               "Each party and the transaction broker possess ONLY ACTUAL KNOWLEDGE; there is NO IMPUTATION of knowledge by operation of law."],
         "check": [("A Missouri transaction broker:", "Provides service with no agency or fiduciary relationship to any party", ["Is a limited agent for both", "Represents the seller"], "RSMo 339.755.1."),
                   ("Adverse material facts a transaction broker must disclose are those of which the licensee has:", "Actual notice or knowledge", ["Any suspicion", "Constructive notice"], "RSMo 339.755.2(2)(d)."),
                   ("In a Missouri transaction brokerage, the parties:", "Are not liable for any acts of the transaction broker", ["Are vicariously liable", "Are liable only after closing"], "RSMo 339.755.2(2)(f)."),
                   ("A transaction broker's duty to inspect is:", "None, and there is no duty to investigate the buyer's finances", ["A visual inspection", "A financial check"], "RSMo 339.755.4, .5."),
                   ("A transaction broker may, in OTHER transactions:", "Serve as a single agent, subagent, designated agent, limited agent or disclosed dual agent", ["Only be a transaction broker", "Not work at all"], "RSMo 339.755.6(4).")]},
        {"h": "Designated agents and the disclosure form (RSMo 339.820, 339.770)",
         "l": ["A designated broker entering a LIMITED AGENCY agreement may APPOINT IN WRITING affiliated licensees as DESIGNATED AGENTS TO THE EXCLUSION OF ALL OTHER affiliated licensees. The same works for a TRANSACTION BROKERAGE agreement and DESIGNATED TRANSACTION BROKERS.",
               "Where such an appointment has been made, an affiliated licensee assisting a party WITHOUT a written agreement is PRESUMED TO BE A TRANSACTION BROKER to the exclusion of all other affiliated licensees, unless a different status has been disclosed or established.",
               "A designated broker is NOT a dual agent or transaction broker SOLELY BECAUSE of making such an appointment - BUT any licensee who PERSONALLY REPRESENTS BOTH SIDES in a particular transaction IS a dual agent or transaction broker and must comply with those rules.",
               "DISCLOSURE: in a RESIDENTIAL transaction, AT THE EARLIEST PRACTICABLE OPPORTUNITY during or following the FIRST SUBSTANTIAL CONTACT with a seller, landlord, buyer or tenant WHO HAS NOT ENTERED INTO A WRITTEN AGREEMENT for services, the licensee must give that person a written copy of the CURRENT BROKER DISCLOSURE FORM PRESCRIBED BY THE COMMISSION.",
               "Where the person HAS ALREADY entered a written agreement with a designated broker, NO OTHER LICENSEE is required to make the disclosure.",
               "Disclosures made under sections 339.710 to 339.860 are SUFFICIENT AS A MATTER OF LAW to disclose brokerage relationships to the public."],
         "check": [("Appointing designated agents makes the Missouri designated broker:", "Neither a dual agent nor a transaction broker, by that fact alone", ["Automatically a dual agent", "A transaction broker"], "RSMo 339.820.2."),
                   ("Where designated agents have been appointed, an affiliated licensee helping a party with no written agreement is:", "Presumed to be a transaction broker", ["Presumed a subagent", "Presumed a dual agent"], "RSMo 339.820.1."),
                   ("The Missouri broker disclosure form is given:", "At the earliest practicable opportunity during or after first substantial contact, to someone with no written agreement", ["At the offer", "At closing"], "RSMo 339.770.1."),
                   ("Where the consumer already has a written agreement with a designated broker:", "No other licensee need make the disclosure", ["Every licensee must repeat it", "The Commission must be notified"], "RSMo 339.770.2."),
                   ("A licensee who personally represents both sides of one transaction:", "Is a dual agent or transaction broker and must comply with those rules", ["Is still only a designated agent", "Must withdraw"], "RSMo 339.820.2.")]},
    ],
    "traps": [
        "The DESIGNATED BROKER signs the agreements, not the individual licensee, unless authorised in writing.",
        "Missouri's agents are LIMITED AGENTS; the no-agency option is TRANSACTION BROKER.",
        "Appointing designated agents does NOT make the broker a dual agent.",
        "Prior offers and counteroffers are on the dual agent's do-not-disclose list.",
        "The disclosure form goes to someone with NO written agreement, at first substantial contact.",
    ],
    "vocab": [
        ["Designated broker", "The broker who holds the firm's agreements and responsibility."],
        ["Limited agent", "Missouri's statutory name for a seller's or buyer's agent."],
        ["Transaction broker", "A licensee with no agency relationship to anyone."],
        ["Designated agent", "An affiliated licensee appointed for one client, excluding the others."],
        ["Ministerial acts", "Acts a buyer's agent may do before the written agreement."],
    ],
    "examples": [
        {"t": "Both sides, one office",
         "s": "Your designated broker appointed you for the seller and another agent for the buyer, both in writing.",
         "w": ["Each of you is a DESIGNATED AGENT for your own client, to the exclusion of the rest of the office.",
               "The designated broker is NOT a dual agent just for making the appointments.",
               "If you personally ended up representing both sides, THEN you would be a dual agent and the dual agency rules apply."],
         "k": "The appointment splits the agents; only personally serving both sides creates dual agency."},
    ],
}

STUDY["mo/conduct"] = {
    "summary": "Seventeen items - the biggest block by far. Escrow money, offers, advertising, and the commission rules that catch licensees out.",
    "sections": [
        {"h": "Escrow and trust accounts (RSMo 339.105)",
         "l": ["Each broker holding funds belonging to another must maintain them in a SEPARATE BANK ACCOUNT designated an ESCROW OR TRUST ACCOUNT - including funds in which the broker may have a FUTURE INTEREST OR CLAIM.",
               "Such funds must be DEPOSITED PROMPTLY unless ALL PARTIES having an interest have AGREED OTHERWISE IN WRITING.",
               "NO COMMINGLING of personal or other funds, EXCEPT that a broker may deposit and keep A SUM NOT TO EXCEED ONE THOUSAND DOLLARS of personal funds, SPECIFICALLY IDENTIFIED, to cover SERVICE CHARGES related to the account.",
               "The broker must NOTIFY THE COMMISSION of an intent NOT to maintain an escrow account, or of the financial institution, the name and number of each account, and must file WRITTEN AUTHORISATION letting the Commission examine each account. Any change must be notified WITHIN TEN BUSINESS DAYS.",
               "The broker must maintain BOOKS, RECORDS, CONTRACTS AND OTHER DOCUMENTS so the adequacy of the account may be determined AT ANY TIME, available for inspection DURING REGULAR BUSINESS HOURS at the broker's usual place of business.",
               "Where OWNERSHIP OF ESCROW MONEY IS IN DISPUTE, the broker must REPORT AND DELIVER THE MONEY TO THE STATE TREASURER WITHIN 365 DAYS of the INITIAL PROJECTED CLOSING DATE, under the unclaimed property law. The parties may agree IN WRITING that the funds are not in dispute and notify the broker.",
               "A BROKER IS NOT ENTITLED to any money paid in connection with a transaction as part of a commission or fee UNTIL THE TRANSACTION HAS BEEN CONSUMMATED OR TERMINATED, unless all parties agree otherwise in writing."],
         "check": [("How much of a broker's own money may sit in a Missouri escrow account?", "Not more than $1,000, specifically identified, to cover service charges", ["Nothing at all", "Up to $2,000", "Any amount"], "RSMo 339.105.1."),
                   ("Disputed escrow money must be delivered to the state treasurer within:", "365 days of the initial projected closing date", ["90 days", "One year from the dispute", "Never"], "RSMo 339.105.4."),
                   ("A Missouri broker may take their commission from escrow:", "Only once the transaction is consummated or terminated, unless all parties agree in writing", ["At any time after acceptance", "On the closing date regardless"], "RSMo 339.105.5."),
                   ("A change of escrow account or status must be reported to the Commission within:", "Ten business days", ["Thirty days", "At renewal"], "RSMo 339.105.2."),
                   ("Escrow funds must be deposited:", "Promptly, unless all parties with an interest agree otherwise in writing", ["Within 10 banking days", "At closing"], "RSMo 339.105.1."),
                   ("The Commission's access to a broker's escrow records is:", "At all times during regular business hours at the broker's usual place of business", ["By subpoena only", "Once a year"], "RSMo 339.105.3.")]},
        {"h": "Offers, listings and standard forms",
         "l": ["The outline lists IMPROPER USE OF LICENSE AND OFFICE, BRANCH OFFICES, CLERICAL PERSONNEL AND PERSONAL OR PROFESSIONAL ASSISTANTS, ADVERTISING, LISTINGS, OFFERS, the LICENSEE'S INTEREST IN TRANSACTIONS AND RELATIONSHIP WITH PARTIES, EARNEST MONEY AND DISPUTES, STANDARD FORMS, CLOSINGS AND CLOSING STATEMENTS, GENERAL matters, and COMMISSIONS.",
               "The three MINIMUM SERVICES in every exclusive brokerage agreement are the practical heart of the 'offers' topic: accepting delivery of and PRESENTING offers and counteroffers; ASSISTING with developing, communicating, negotiating and presenting them until a contract is signed and contingencies are satisfied or waived; and ANSWERING the client's or customer's questions about them (RSMo 339.780.7).",
               "A limited agent must PRESENT ALL WRITTEN OFFERS to and from the client TIMELY REGARDLESS of an existing contract, and need NOT seek additional offers while the property is under contract (RSMo 339.730.1(3)).",
               "A transaction broker must PRESENT ALL WRITTEN OFFERS AND COUNTEROFFERS TIMELY regardless of an existing contract or letter of intent, unless the agreement with the party provides otherwise (RSMo 339.755.2(2)(a)).",
               "Nothing stops the public from contracting for DUTIES, OBLIGATIONS OR RESPONSIBILITIES IN ADDITION to the statutory ones (RSMo 339.780.8)."],
         "check": [("A Missouri limited agent must present written offers:", "Timely, to and from the client, regardless of an existing contract", ["Only before a contract exists", "Weekly"], "RSMo 339.730.1(3)(b)."),
                   ("May a Missouri brokerage agreement add duties beyond the statutory ones?", "Yes; nothing prohibits the public from contracting for additional duties", ["No, the statute is exhaustive", "Only with Commission approval"], "RSMo 339.780.8."),
                   ("The minimum services in an exclusive agreement include:", "Answering the client's questions about offers, counteroffers, notices and contingencies", ["Holding a weekly open house", "Paying for staging"], "RSMo 339.780.7(3).")]},
        {"h": "Compensation and interests",
         "l": ["The outline's 'COMMISSIONS (must be licensee)' heading points at the rule that compensation for licensed activity goes to LICENSEES. A salesperson is paid through their broker, and paying an unlicensed person for licensed activity is improper.",
               "The 'LICENSEE'S INTEREST IN TRANSACTIONS; RELATIONSHIP WITH PARTIES' heading covers a licensee dealing for their own account, which engages the duty to disclose ADVERSE MATERIAL FACTS and the ban on misrepresentation under RSMo 339.100.2.",
               "A broker's compensation is NOT EARNED OUT OF ESCROW until the transaction is CONSUMMATED OR TERMINATED (RSMo 339.105.5).",
               "A limited agency agreement must state the TERMS OF COMPENSATION and whether SUBAGENCY may be offered; a transaction brokerage agreement must state the terms of compensation (RSMo 339.780.2, .6)."],
         "check": [("A Missouri broker's commission may be taken from escrow:", "Only after the transaction is consummated or terminated, absent written agreement otherwise", ["On acceptance of the offer", "At the broker's discretion"], "RSMo 339.105.5."),
                   ("A limited agency agreement must state:", "The terms of compensation and whether an offer of subagency may be made", ["The MLS number", "The closing date"], "RSMo 339.780.2.")]},
    ],
    "traps": [
        "$1,000 of the broker's own money, and only for service charges.",
        "Disputed escrow goes to the STATE TREASURER after 365 days from the initial projected closing date.",
        "No commission out of escrow until consummated or terminated.",
        "Ten BUSINESS days to report an escrow account change.",
    ],
    "vocab": [
        ["Escrow or trust account", "The separate account holding others' funds."],
        ["Initial projected closing date", "When the 365-day clock on disputed money starts."],
        ["Commingling", "Mixing the broker's own funds with clients', beyond the $1,000."],
        ["Minimum services", "The three services every exclusive agreement must guarantee."],
    ],
    "examples": [
        {"t": "Earnest money stand-off",
         "s": "A deal collapses. Buyer and seller each demand the $5,000 earnest money. The initial projected closing date was 1 March.",
         "w": ["The broker cannot pick a side; the money stays in escrow.",
               "If the parties never agree in writing that the funds are not in dispute, the broker must report and deliver the money to the STATE TREASURER within 365 DAYS of 1 March.",
               "The broker's own commission cannot come out of that money either."],
         "k": "Unresolved escrow goes to the state, not to whoever shouts loudest."},
    ],
}

STUDY["mo/licenses"] = {
    "summary": "Seven items. Missouri's own quirks: 18 years old, a 48-hour pre-exam course, and a six-month clock that catches people out.",
    "sections": [
        {"h": "Qualifying (RSMo 339.040; MREC handbook)",
         "l": ["Licences are granted only to persons who present SATISFACTORY PROOF THAT THEY ARE COMPETENT to transact business in a manner that SAFEGUARDS THE INTEREST OF THE PUBLIC.",
               "Each applicant for a broker or salesperson licence must be AT LEAST 18 YEARS OF AGE and pay the examination fee.",
               "A SALESPERSON applicant must earn a CERTIFICATE OF SATISFACTORY COMPLETION from a 48-HOUR PRE-EXAM SALESPERSON COURSE at an accredited Missouri school ON OR BEFORE THE EXAM DATE, PASS BOTH PORTIONS, and complete the 24-HOUR MISSOURI REAL ESTATE PRACTICE COURSE (MREP) BEFORE SUBMITTING the licence application. MREP may be taken BEFORE OR AFTER the exam.",
               "The complete application must be submitted WITHIN SIX MONTHS of the COMPLETION DATE OF THE 48-HOUR PRE-EXAM COURSE.",
               "A LICENSED ATTORNEY may have the education requirements WAIVED, passing both portions and applying within six months, with a copy of a current Bar card.",
               "Someone holding a CURRENT ACTIVE LICENCE IN ANOTHER JURISDICTION passes the STATE PORTION only and completes MREP, applying within six months of passing, with a licence history certification issued within three months.",
               "A BROKER applicant must have been ACTIVELY ENGAGED as a licensed salesperson for AT LEAST TWO YEARS immediately preceding the application, and must have completed the prescribed broker curriculum WITHIN SIX MONTHS prior to application. The Commission may waive parts of that for other acceptable education or experience.",
               "A broker applicant must also have SATISFACTORILY COMPLETED THE SALESPERSON LICENCE EXAMINATION, and the Commission may let someone not associated with a broker sit it."],
         "check": [("The minimum age for a Missouri real estate licence is:", "18", ["21", "19", "There is none"], "RSMo 339.040.3."),
                   ("A Missouri salesperson applicant's pre-exam course is:", "48 hours, completed on or before the exam date", ["72 hours", "90 hours", "24 hours"], "MREC candidate handbook."),
                   ("The 24-hour MREP course must be completed:", "Before the licence application is submitted; it may be taken before or after the exam", ["Before the exam only", "Within a year of licensure"], "MREC candidate handbook."),
                   ("The licence application must be submitted within:", "Six months of completing the 48-hour pre-exam course", ["One year of passing", "Three months of the exam"], "MREC candidate handbook."),
                   ("A Missouri broker applicant must have been an active salesperson for:", "At least two years immediately preceding the application", ["One year", "Three years"], "RSMo 339.040.5."),
                   ("A licensed Missouri attorney applying as a salesperson:", "Has the education requirements waived but must pass both portions", ["Is licensed without examination", "Has no exemption"], "MREC candidate handbook.")]},
        {"h": "What the outline covers",
         "l": ["APPLICATIONS FOR LICENSE; QUALIFICATION FOR, EXPIRATION, AND RENEWAL; INDIVIDUAL LICENSE AND BUSINESS NAME; the BROKER-SALESPERSON RELATIONSHIP; SALESPERSON LICENSE AND TRANSFERS; DENIAL OF LICENSE; and APPLICATION AND LICENSE FEES.",
               "A BROKER-SALESPERSON holds a broker licence but works under another broker - the application must include EVIDENCE OF THE CURRENT BROKER LICENCE held by the applicant (RSMo 339.040.5).",
               "A licence may be granted to a CORPORATION, ASSOCIATION, PARTNERSHIP, LIMITED PARTNERSHIP, LIMITED LIABILITY COMPANY OR PROFESSIONAL CORPORATION whose officers, managers, associates, general partners or members ACTIVELY PARTICIPATING in the brokerage business present satisfactory proof of competence (RSMo 339.040.1).",
               "All written brokerage agreements belong to the DESIGNATED BROKER, which is the statutory expression of the broker-salesperson relationship (RSMo 339.780.1)."],
         "check": [("A Missouri broker-salesperson:", "Holds a broker licence but works under another broker", ["Is an unlicensed assistant", "Is a salesperson awaiting a broker licence"], "RSMo 339.040.5."),
                   ("An entity licence requires satisfactory proof of competence from:", "The officers, managers, associates, general partners or members who actively participate in the brokerage business", ["Every shareholder", "Only the registered agent"], "RSMo 339.040.1.")]},
    ],
    "traps": [
        "48 hours pre-exam, 24 hours MREP, six months to apply.",
        "Broker needs TWO years as an active salesperson.",
        "Attorneys get the education waived, not the examination.",
    ],
    "vocab": [
        ["MREP", "The 24-hour Missouri Real Estate Practice course."],
        ["Broker-salesperson", "A broker licensee working under another broker."],
        ["Designated broker", "The broker responsible for a firm's agreements."],
    ],
    "examples": [],
}

STUDY["mo/discipline"] = {
    "summary": "Six items. Missouri splits the job: the COMMISSION brings the case, the ADMINISTRATIVE HEARING COMMISSION decides whether there are grounds.",
    "sections": [
        {"h": "How a case moves",
         "l": ["The outline lists COMPLAINTS, INVESTIGATION, VIOLATIONS, ACTION BY THE COMMISSION, ACTION BY THE ADMINISTRATIVE HEARING COMMISSION, and the PENALTY FOR VIOLATING OR PRACTISING WITHOUT A LICENCE.",
               "RSMo 339.100 sets out the Commission's investigative powers and the grounds for discipline. The MISSOURI REAL ESTATE COMMISSION investigates and FILES A COMPLAINT WITH THE ADMINISTRATIVE HEARING COMMISSION; the AHC decides whether cause for discipline exists; the Commission then imposes the DISCIPLINE.",
               "Where the Commission has REASONABLE CAUSE to believe a licensee has acted, is acting or is about to act in violation of the escrow section, it may proceed THROUGH THE ATTORNEY GENERAL (RSMo 339.105.6).",
               "A limited agent must COMPLY with the brokerage relationship sections and with SUBSECTION 2 OF SECTION 339.100 - the grounds for discipline - as part of their statutory duties (RSMo 339.730.1(5)).",
               "NO CAUSE OF ACTION arises against a licensee for making a REQUIRED OR PERMITTED DISCLOSURE under the agency sections (RSMo 339.730.2, 339.750.5)."],
         "check": [("In Missouri, who decides whether grounds for discipline exist?", "The Administrative Hearing Commission, on a complaint filed by the Real Estate Commission", ["The Real Estate Commission alone", "A circuit court jury"], "RSMo 339.100; the state outline lists both."),
                   ("On an escrow violation the Commission may act:", "Through the attorney general", ["By seizing the account itself", "Only after a conviction"], "RSMo 339.105.6."),
                   ("A licensee who makes a disclosure the agency sections require:", "Faces no cause of action for it", ["May be sued by the client", "Must notify the Commission"], "RSMo 339.730.2; 339.750.5."),
                   ("Compliance with RSMo 339.100.2 is:", "Part of a limited agent's statutory duties", ["Optional guidance", "Only relevant to brokers"], "RSMo 339.730.1(5).")]},
    ],
    "traps": [
        "The Commission prosecutes; the Administrative Hearing Commission adjudicates.",
        "Required disclosures are protected - no cause of action.",
    ],
    "vocab": [
        ["AHC", "The Administrative Hearing Commission."],
        ["MREC", "The Missouri Real Estate Commission."],
        ["Cause for discipline", "What the AHC finds before the Commission sanctions."],
    ],
    "examples": [],
}

STUDY["mo/general"] = {
    "summary": "Two items on definitions and disputes - small, but the definitions decide every other answer.",
    "sections": [
        {"h": "Who is who",
         "l": ["RSMo 339.010 defines what acts require a licence; RSMo 339.710 defines the brokerage relationship terms, including CONFIDENTIAL INFORMATION, MINISTERIAL ACTS, CLIENT and CUSTOMER.",
               "A CLIENT is the party the licensee represents; a CUSTOMER is a party the licensee works with but does not represent. A seller's agent owes a customer ONLY the disclosure of ADVERSE MATERIAL FACTS actually known or that should have been known (RSMo 339.730.3).",
               "MINISTERIAL ACTS are the acts a designated broker may perform for a buyer or tenant BEFORE entering the written agency agreement (RSMo 339.780.3).",
               "The DESIGNATED BROKER is the broker responsible for the firm's written agreements and for the acts of affiliated licensees (RSMo 339.780.1).",
               "DISPUTES: where ownership of escrow money is in dispute the broker reports and delivers it to the STATE TREASURER within 365 days of the initial projected closing date, unless the parties agree IN WRITING that the funds are not in dispute (RSMo 339.105.4)."],
         "check": [("A Missouri CUSTOMER is owed:", "Disclosure of adverse material facts actually known or that should have been known", ["Nothing at all", "Full fiduciary duties"], "RSMo 339.730.3."),
                   ("Ministerial acts may be performed for a buyer:", "Before the written agency agreement is entered", ["Only after the agreement", "Never"], "RSMo 339.780.3."),
                   ("An escrow dispute ends with the money going to:", "The state treasurer, within 365 days of the initial projected closing date", ["The buyer", "The seller", "The broker"], "RSMo 339.105.4.")]},
    ],
    "traps": [
        "Client versus customer decides which duties apply.",
        "Ministerial acts are the exception that lets a buyer's broker work before signing.",
    ],
    "vocab": [
        ["Client", "The party a licensee represents."],
        ["Customer", "A party the licensee works with but does not represent."],
        ["Ministerial act", "Work allowed before a buyer agency agreement is signed."],
        ["Confidential information", "Defined in RSMo 339.710 and protected by the agency sections."],
    ],
    "examples": [],
}

STUDY["mo/education"] = {
    "summary": "Two items. Two numbers: the 48-hour salesperson course and 12 hours of continuing education with a 3-hour core.",
    "sections": [
        {"h": "The courses",
         "l": ["SALESPERSON COURSE: a 48-HOUR PRE-EXAM SALESPERSON COURSE from an ACCREDITED MISSOURI REAL ESTATE SCHOOL, completed ON OR BEFORE THE EXAM DATE, plus the 24-HOUR MISSOURI REAL ESTATE PRACTICE COURSE (MREP) before the licence application.",
               "CONTINUING EDUCATION: 20 CSR 2250-10.100 requires 12 HOURS of approved instruction per renewal, of which AT LEAST 3 HOURS must be taken in a CORE COURSE identified by the Commission and noticed on its official website NO LATER THAN 31 MARCH OF EACH EVEN-NUMBERED YEAR.",
               "The Commission publishes which core topic applies: for the 2026-2028 licence period the required CORE course is on FAIR HOUSING.",
               "FAILURE to provide the Commission with evidence of course completion is GROUNDS FOR NOT RENEWING A LICENCE.",
               "An ACTIVE LICENCE, for continuing education purposes, is any licence except one placed on INACTIVE STATUS.",
               "A BROKER applicant must have completed the prescribed BROKER CURRICULUM within SIX MONTHS prior to application (RSMo 339.040.5)."],
         "check": [("Missouri continuing education is:", "12 hours per renewal, at least 3 of them a core course", ["16 hours", "24 hours", "6 hours"], "20 CSR 2250-10.100; MREC."),
                   ("The Commission identifies the core course topic:", "No later than 31 March of each even-numbered year, on its official website", ["At each renewal", "Annually in December"], "20 CSR 2250-10.100(3)."),
                   ("The required core topic for the 2026-2028 Missouri licence period is:", "Fair housing", ["Agency", "Escrow", "Contracts"], "Missouri Real Estate Commission, published CE requirements."),
                   ("Failing to give the Commission evidence of completed courses:", "Is grounds for not renewing the licence", ["Carries a fine only", "Has no consequence"], "20 CSR 2250-10."),
                   ("A Missouri broker applicant's curriculum must be completed within:", "Six months prior to the application", ["Two years", "One year"], "RSMo 339.040.5.")]},
    ],
    "traps": [
        "12 hours with a 3-hour CORE - and the core topic changes by biennium.",
        "48 pre-exam hours, 24 MREP hours. Two different courses.",
    ],
    "vocab": [
        ["Core course", "The Commission-designated 3-hour continuing education topic."],
        ["MREP", "The 24-hour Missouri Real Estate Practice course."],
        ["Inactive status", "A licence excluded from the 'active licence' definition."],
    ],
    "examples": [],
}


# ------------------------------------------------------------- questions

Q = [
 # relationships
 ("mo/relationships", "Agreements", 1, "In Missouri, written brokerage agreements are entered into by:",
  "The designated broker, unless affiliated licensees are authorised in writing", ["Any affiliated licensee", "The managing salesperson"],
  "RSMo 339.780.1."),
 ("mo/relationships", "Agreements", 2, "A Missouri seller's limited agency agreement must specify:",
  "The duties, the terms of compensation, and whether an offer of subagency may be made", ["Only the commission rate", "Only the listing period"],
  "RSMo 339.780.2."),
 ("mo/relationships", "Agreements", 2, "A broker expecting compensation as a transaction broker must:",
  "Enter a written transaction brokerage agreement with the party", ["Rely on an oral understanding", "Use the standard agency agreement"],
  "RSMo 339.780.6."),
 ("mo/relationships", "Agreements", 2, "Every Missouri exclusive brokerage agreement must guarantee at least:",
  "Presenting offers, assisting with negotiation until signing, and answering questions about them", ["A minimum advertising spend", "A weekly open house"],
  "RSMo 339.780.7."),
 ("mo/relationships", "Subagency", 3, "Where a unilateral offer of subagency has been made, another broker becomes a subagent by:",
  "Disclosing to the customer that they are a subagent of the client", ["Signing the listing agreement", "Notifying the Commission"],
  "RSMo 339.780.5."),
 ("mo/relationships", "Limited agent", 1, "Missouri calls a seller's agent a:",
  "Limited agent", ["General agent", "Universal agent", "Transaction broker"],
  "RSMo 339.730.1."),
 ("mo/relationships", "Limited agent", 1, "A Missouri seller's agent must present written offers:",
  "Timely, regardless of whether the property is already under contract", ["Only until a contract is signed", "Only above the listed price"],
  "RSMo 339.730.1(3)(b)."),
 ("mo/relationships", "Limited agent", 2, "Adverse material facts owed to the CLIENT are those:",
  "Actually known or that should have been known by the licensee", ["Actually known only", "Discoverable by inspection only"],
  "RSMo 339.730.1(3)(c)."),
 ("mo/relationships", "Customers", 1, "What does a Missouri seller's agent owe a CUSTOMER?",
  "Disclosure of adverse material facts actually known or that should have been known", ["Nothing at all", "Full fiduciary duties"],
  "RSMo 339.730.3."),
 ("mo/relationships", "Customers", 2, "A Missouri seller's agent's duty to inspect for the customer is:",
  "None, and there is no duty to verify the client's or an inspector's statements", ["A visual inspection", "A full inspection"],
  "RSMo 339.730.3."),
 ("mo/relationships", "Confidentiality", 2, "Confidential client information may be disclosed where:",
  "A statute or rule requires it, silence would be a misrepresentation, or it is needed to defend the licensee", ["The deal has closed", "The cooperating agent asks"],
  "RSMo 339.730.2."),
 ("mo/relationships", "Dual agency", 1, "Missouri dual agency requires:",
  "The consent of all parties, presumed by the written agreement under 339.780", ["Oral consent", "No consent at all"],
  "RSMo 339.750.1."),
 ("mo/relationships", "Dual agency", 2, "Which may a Missouri dual agent NOT disclose without consent?",
  "The terms of any prior offers or counteroffers", ["A known structural defect", "A statutory disclosure"],
  "RSMo 339.750.4(5)."),
 ("mo/relationships", "Dual agency", 2, "A Missouri dual agent is:",
  "A limited agent for both sides", ["A full fiduciary for both", "Not an agent at all"],
  "RSMo 339.750.2."),
 ("mo/relationships", "Dual agency", 3, "Making a required disclosure as a Missouri dual agent:",
  "Does not terminate the dual agency relationship", ["Ends the relationship", "Converts it to transaction brokerage"],
  "RSMo 339.750.5."),
 ("mo/relationships", "Transaction broker", 1, "A Missouri transaction broker:",
  "Provides service with no agency or fiduciary relationship to any party", ["Is a limited agent for both sides", "Represents the seller"],
  "RSMo 339.755.1."),
 ("mo/relationships", "Transaction broker", 2, "Adverse material facts a transaction broker must disclose are those of which the licensee has:",
  "Actual notice or knowledge", ["Any suspicion", "Constructive notice"],
  "RSMo 339.755.2(2)(d)."),
 ("mo/relationships", "Transaction broker", 2, "In a Missouri transaction brokerage, the parties:",
  "Are not liable for any acts of the transaction broker", ["Are vicariously liable", "Are liable only after closing"],
  "RSMo 339.755.2(2)(f)."),
 ("mo/relationships", "Transaction broker", 3, "A Missouri transaction broker, in OTHER transactions, may:",
  "Serve as a single agent, subagent, designated agent, limited agent or disclosed dual agent", ["Only ever be a transaction broker", "Not represent anyone"],
  "RSMo 339.755.6(4)."),
 ("mo/relationships", "Designated agents", 1, "Appointing designated agents makes the Missouri designated broker:",
  "Neither a dual agent nor a transaction broker, by that fact alone", ["Automatically a dual agent", "A transaction broker"],
  "RSMo 339.820.2."),
 ("mo/relationships", "Designated agents", 2, "Where designated agents have been appointed, an affiliated licensee helping a party with no written agreement is:",
  "Presumed to be a transaction broker", ["Presumed a subagent", "Presumed a dual agent"],
  "RSMo 339.820.1."),
 ("mo/relationships", "Designated agents", 2, "A Missouri licensee who personally represents both sides of one transaction:",
  "Is a dual agent or transaction broker and must comply with those rules", ["Remains only a designated agent", "Must withdraw from the deal"],
  "RSMo 339.820.2."),
 ("mo/relationships", "Disclosure", 1, "The Missouri broker disclosure form is given:",
  "At the earliest practicable opportunity during or after first substantial contact, to someone with no written agreement", ["At the offer", "At closing"],
  "RSMo 339.770.1."),
 ("mo/relationships", "Disclosure", 2, "Where the consumer already has a written agreement with a designated broker:",
  "No other licensee need make the disclosure", ["Every licensee must repeat it", "The Commission must be told"],
  "RSMo 339.770.2."),

 # conduct
 ("mo/conduct", "Escrow", 1, "How much of a broker's own money may sit in a Missouri escrow account?",
  "Not more than $1,000, specifically identified, to cover service charges", ["Nothing at all", "Up to $2,000", "Any amount"],
  "RSMo 339.105.1."),
 ("mo/conduct", "Escrow", 1, "Disputed Missouri escrow money must be delivered to the state treasurer within:",
  "365 days of the initial projected closing date", ["90 days of the dispute", "One year of the dispute", "It never is"],
  "RSMo 339.105.4."),
 ("mo/conduct", "Escrow", 1, "A Missouri broker may take their commission from escrow:",
  "Only once the transaction is consummated or terminated, unless all parties agree in writing", ["On acceptance of the offer", "At any time"],
  "RSMo 339.105.5."),
 ("mo/conduct", "Escrow", 2, "A change of escrow account or account status must be reported to the Commission within:",
  "Ten business days", ["Thirty days", "At the next renewal"],
  "RSMo 339.105.2."),
 ("mo/conduct", "Escrow", 2, "Missouri escrow funds must be deposited:",
  "Promptly, unless all parties with an interest agree otherwise in writing", ["Within 10 banking days", "At closing"],
  "RSMo 339.105.1."),
 ("mo/conduct", "Escrow", 2, "The Commission's access to escrow records is:",
  "At all times during regular business hours at the broker's usual place of business", ["By subpoena only", "Once a year by appointment"],
  "RSMo 339.105.3."),
 ("mo/conduct", "Escrow", 3, "Funds in which the broker may have a future interest or claim:",
  "Must still be held in the escrow or trust account", ["May be kept in the operating account", "Belong to the broker"],
  "RSMo 339.105.1."),
 ("mo/conduct", "Escrow", 3, "Parties may take escrow money out of 'dispute' status by:",
  "Agreeing in writing that the funds are not in dispute and notifying the broker", ["Telephoning the broker", "Letting 365 days pass"],
  "RSMo 339.105.4."),
 ("mo/conduct", "Offers", 1, "A Missouri transaction broker must present all written offers and counteroffers:",
  "Timely, regardless of an existing contract or letter of intent, unless the agreement provides otherwise", ["Only before a contract exists", "At the party's request"],
  "RSMo 339.755.2(2)(a)."),
 ("mo/conduct", "Offers", 2, "A Missouri limited agent's duty to seek further offers once one is accepted is:",
  "None, while the property is under a contract for sale", ["Continuing", "Continuing for 30 days"],
  "RSMo 339.730.1(3)(a)."),
 ("mo/conduct", "Agreements", 2, "May a Missouri brokerage agreement add duties beyond the statutory ones?",
  "Yes; nothing prohibits the public from contracting for additional duties", ["No, the statute is exhaustive", "Only with Commission approval"],
  "RSMo 339.780.8."),
 ("mo/conduct", "Minimum services", 2, "The minimum services in a Missouri exclusive agreement include:",
  "Answering the client's or customer's questions about offers, counteroffers, notices and contingencies", ["Providing professional photography", "Paying for staging"],
  "RSMo 339.780.7(3)."),
 ("mo/conduct", "Compensation", 2, "A Missouri limited agency agreement must state:",
  "The terms of compensation and whether an offer of subagency may be made", ["The MLS number", "The projected closing date"],
  "RSMo 339.780.2."),
 ("mo/conduct", "Fair housing", 2, "A Missouri limited agent's statutory duties expressly include complying with:",
  "Fair housing and civil rights statutes and regulations", ["The MLS rules", "The local board's code"],
  "RSMo 339.730.1(6)."),
 ("mo/conduct", "Discipline", 3, "A Missouri limited agent must also comply with:",
  "Subsection 2 of section 339.100, the grounds for discipline", ["Only the agency sections", "Only the escrow section"],
  "RSMo 339.730.1(5)."),

 # licenses
 ("mo/licenses", "Age", 1, "The minimum age for a Missouri real estate licence is:",
  "18", ["21", "19", "There is no minimum"],
  "RSMo 339.040.3."),
 ("mo/licenses", "Education", 1, "A Missouri salesperson applicant's pre-exam course is:",
  "48 hours, completed on or before the exam date", ["72 hours", "90 hours", "24 hours"],
  "MREC candidate handbook."),
 ("mo/licenses", "Education", 1, "The 24-hour MREP course must be completed:",
  "Before the licence application is submitted; it may be taken before or after the exam", ["Before the exam only", "Within a year of licensure"],
  "MREC candidate handbook."),
 ("mo/licenses", "Application", 2, "The Missouri licence application must be submitted within:",
  "Six months of completing the 48-hour pre-exam course", ["One year of passing", "Three months of the exam"],
  "MREC candidate handbook."),
 ("mo/licenses", "Broker", 2, "A Missouri broker applicant must have been an active salesperson for:",
  "At least two years immediately preceding the application", ["One year", "Three years"],
  "RSMo 339.040.5."),
 ("mo/licenses", "Attorneys", 3, "A licensed Missouri attorney applying as a salesperson:",
  "Has the education requirements waived but must still pass both portions", ["Is licensed without examination", "Has no exemption"],
  "MREC candidate handbook."),
 ("mo/licenses", "Types", 2, "A Missouri broker-salesperson:",
  "Holds a broker licence but works under another broker", ["Is an unlicensed assistant", "Is a salesperson awaiting a broker licence"],
  "RSMo 339.040.5."),

 # discipline
 ("mo/discipline", "Process", 1, "In Missouri, who decides whether grounds for discipline exist?",
  "The Administrative Hearing Commission, on a complaint filed by the Real Estate Commission", ["The Real Estate Commission alone", "A circuit court jury"],
  "RSMo 339.100; the state outline names both bodies."),
 ("mo/discipline", "Escrow", 2, "On an escrow violation the Missouri Commission may act:",
  "Through the attorney general", ["By seizing the account itself", "Only after a criminal conviction"],
  "RSMo 339.105.6."),
 ("mo/discipline", "Protection", 2, "A licensee who makes a disclosure the agency sections require:",
  "Faces no cause of action for it", ["May be sued by the client", "Must report it to the Commission"],
  "RSMo 339.730.2; 339.750.5."),
 ("mo/discipline", "Competence", 2, "Missouri grants licences only to those who show:",
  "They are competent to transact business in a manner that safeguards the public interest", ["Two years of residency", "A clean credit record"],
  "RSMo 339.040.1."),
 ("mo/discipline", "Records", 3, "A Missouri broker's escrow books and records must be kept so that:",
  "The adequacy of the account may be determined at any time", ["They can be audited annually", "They survive seven years"],
  "RSMo 339.105.3."),
 ("mo/discipline", "Authorisation", 3, "A Missouri broker must file with the Commission:",
  "Written authorisation allowing it to examine each escrow account", ["A surety bond", "Monthly bank statements"],
  "RSMo 339.105.2."),

 # general
 ("mo/general", "Customer", 1, "A Missouri CUSTOMER is owed:",
  "Disclosure of adverse material facts actually known or that should have been known", ["Nothing at all", "Full fiduciary duties"],
  "RSMo 339.730.3."),
 ("mo/general", "Ministerial acts", 2, "Ministerial acts may be performed for a Missouri buyer:",
  "Before the written agency agreement is entered", ["Only after the agreement is signed", "Never"],
  "RSMo 339.780.3."),

 # education
 ("mo/education", "Continuing education", 1, "Missouri continuing education is:",
  "12 hours per renewal, at least 3 of them a core course", ["16 hours", "24 hours", "6 hours"],
  "20 CSR 2250-10.100; Missouri Real Estate Commission."),
 ("mo/education", "Core course", 2, "The Commission identifies the Missouri core course topic:",
  "No later than 31 March of each even-numbered year, on its official website", ["At each renewal", "Every December"],
  "20 CSR 2250-10.100(3)."),
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
            "id": "mo-" + hashlib.sha1(q.encode()).hexdigest()[:8],
            "portion": "georgia", "topic": topic, "subtopic": sub,
            "sub": topic + "|" + sub, "concept": "Missouri " + sub.lower(),
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
        "code": "MO", "name": "Missouri", "abbr": "MO",
        "regulator": "Missouri Real Estate Commission",
        "pass": EXAM["pass"],
        "portions": {
            "national": {"scored": EXAM["national_scored"],
                         "minutes": EXAM["national_minutes"],
                         "pass": EXAM["national_pass"],
                         "blurb": "100 items, 70% to pass."},
            "georgia": {"name": "Missouri law", "scored": EXAM["state_scored"],
                        "minutes": EXAM["state_minutes"],
                        "pass": EXAM["state_pass"],
                        "blurb": "40 items at 75%: chapter 339, the brokerage relationship sections and the Commission's rules."},
        },
        "topics": topics, "bank": bank, "study": study,
        "sources": SOURCES, "diffs": DIFFS,
    }


# Where Missouri departs from the national rule.
DIFFS = {
    "national/agency": [
        "Missouri routes everything through the DESIGNATED BROKER: all written brokerage agreements are the broker's unless affiliated licensees are authorised in writing (RSMo 339.780.1).",
        "A seller's or buyer's agent is a LIMITED AGENT; the no-agency option is the TRANSACTION BROKER, whose parties are NOT LIABLE for the broker's acts (RSMo 339.730, 339.755).",
        "A broker may appoint DESIGNATED AGENTS without becoming a dual agent, and an affiliated licensee helping a party with no written agreement is then PRESUMED A TRANSACTION BROKER (RSMo 339.820).",
        "A dual agent's do-not-disclose list includes THE TERMS OF ANY PRIOR OFFERS OR COUNTEROFFERS (RSMo 339.750.4(5)).",
        "Every EXCLUSIVE agreement must guarantee three MINIMUM SERVICES (RSMo 339.780.7).",
    ],
    "national/practice": [
        "A broker may keep up to $1,000 OF PERSONAL FUNDS in the escrow account, for service charges only (RSMo 339.105.1).",
        "DISPUTED escrow money goes to the STATE TREASURER within 365 DAYS of the initial projected closing date (RSMo 339.105.4).",
        "No commission may be taken from escrow until the transaction is CONSUMMATED OR TERMINATED (RSMo 339.105.5).",
        "Education: a 48-hour pre-exam course plus the 24-hour MREP course, with the application due within SIX MONTHS of the pre-exam course; then 12 hours of continuing education with a 3-hour CORE.",
        "A broker applicant needs TWO YEARS as an active salesperson (RSMo 339.040.5).",
    ],
    "national/disclosures": [
        "The COMMISSION'S BROKER DISCLOSURE FORM goes to anyone with no written agreement, at the earliest practicable opportunity during or after FIRST SUBSTANTIAL CONTACT in a residential transaction (RSMo 339.770).",
        "ADVERSE MATERIAL FACTS owed to a CLIENT are those actually known OR THAT SHOULD HAVE BEEN KNOWN; a TRANSACTION BROKER owes only those of which they have ACTUAL notice or knowledge (RSMo 339.730.1(3)(c), 339.755.2(2)(d)).",
        "No licensee owes a duty to inspect for a customer or to verify the client's or an inspector's statements (RSMo 339.730.3).",
    ],
}


if __name__ == "__main__":
    import io, json, os
    here = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    out = os.path.join(here, "greprep", "packs", "MO.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    pack = build()
    with io.open(out, "w", encoding="utf-8") as f:
        json.dump(pack, f, ensure_ascii=False, indent=1, sort_keys=True)
    print("wrote", out, len(pack["bank"]), "questions,", len(pack["study"]), "lessons")
