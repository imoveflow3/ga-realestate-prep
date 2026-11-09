"""Illinois state content: lessons and practice questions.

Illinois splits the examination 100 national + 40 state, and is the first
state in this app to set a DIFFERENT pass mark on each portion: 70% on the
national paper and 75% on the Illinois paper. The pack puts `pass` on each
portion and the app scores them apart.

Illinois also issues only a BROKER licence at entry level, like North
Carolina. "Salesperson" is the wrong word here; a managing broker is the
supervising grade above.

Every rule below was read from the official text on 2026-11-09:
  - Real Estate License Act of 2000, 225 ILCS 454, current text from
    ilga.gov.
  - The PSI Illinois Candidate Information Booklet for IDFPR's Division of
    Real Estate, for the blueprint, the pass marks and the timings.
  - The Illinois Department of Human Rights, for the protected
    characteristics in housing.
The section a fact comes from is cited next to it. Do not add a fact here
without reading its source first.
"""

EXAM = {
    # PSI booklet: Broker National 100 items / 70% / 150 minutes;
    # State 40 items / 75% / 90 minutes.
    "state_scored": 40,
    "state_minutes": 90,
    "state_pass": 0.75,
    "national_scored": 100,
    "national_minutes": 150,
    "national_pass": 0.70,
    "pass": 0.75,          # the stricter of the two, used where one is shown
}

# PSI's published state outline, with the Broker item counts.
TOPICS = [
    ("il/license-act", "Illinois Real Estate License Act", 16,
     "Agency, advertising, brokerage agreements, money, discipline."),
    ("il/other-laws", "Other Illinois laws", 10,
     "Ownership, transfer taxes, the Human Rights Act, landlord and tenant."),
    ("il/disclosures", "Disclosures", 10,
     "Designated agency, dual agency, property condition, environmental."),
    ("il/licensing", "Licensing requirements", 4,
     "Who needs a licence, the grades, education, renewal."),
]

SOURCES = [
    {"by": "Illinois General Assembly",
     "name": "Real Estate License Act of 2000 (225 ILCS 454)",
     "note": "The licence law itself. Every agency, licensing, money and discipline rule here was read from it.",
     "url": "https://www.ilga.gov/Legislation/ILCS/Articles?ActID=1364&ChapterID=24"},
    {"by": "PSI Services and IDFPR Division of Real Estate",
     "name": "Illinois Candidate Information Booklet",
     "note": "The blueprint: 100 national items at 70% and 40 state items at 75%, with the four state categories.",
     "url": "https://test-takers.psiexams.com/ilrep"},
    {"by": "Illinois Department of Human Rights",
     "name": "Housing rights and protected characteristics",
     "note": "Illinois protects far more characteristics in housing than federal law does.",
     "url": "https://dhr.illinois.gov/rights/housing-rights.html"},
]


# --------------------------------------------------------------- lessons

STUDY = {}

STUDY["il/license-act"] = {
    "summary": "Sixteen of the forty state items. The thing to fix first: Illinois PRESUMES you are a designated agent for whoever you work with. Representation is the default here, not something the consumer has to choose.",
    "sections": [
        {"h": "Agency is presumed (225 ILCS 454/15-10)",
         "p": ["Licensees are considered to be representing the consumer they are working with AS A DESIGNATED AGENT for that consumer, UNLESS there is a WRITTEN AGREEMENT between the sponsoring broker and the consumer providing a different relationship."],
         "l": ["So doing nothing creates agency in Illinois. Contrast that with states where no relationship is presumed.",
               "DESIGNATED AGENCY means the individual licensee is the agent, named by the sponsoring broker.",
               "Where the relationship is designated agency, whether a DUAL AGENCY exists is decided by the relationships of the DESIGNATED AGENTS of the parties, not by the sponsoring broker's (225 ILCS 454/1-10)."],
         "check": [("An Illinois licensee working with a consumer, with nothing in writing, is:", "That consumer's designated agent", ["A transaction broker", "Representing nobody", "The seller's subagent"], "225 ILCS 454/15-10."),
                   ("To create something other than designated agency, Illinois requires:", "A written agreement between the sponsoring broker and the consumer", ["An oral understanding", "A note in the file"], "225 ILCS 454/15-10."),
                   ("In a designated agency, dual agency is judged by:", "The relationships of the designated agents, not the sponsoring broker", ["The sponsoring broker's relationships", "Who pays the commission"], "225 ILCS 454/1-10.")]},
        {"h": "Duties to a client (15-15)",
         "l": ["Perform the terms of the brokerage agreement.",
               "Promote the client's best interest by seeking a transaction at the price and terms in the agreement, or otherwise acceptable to the client.",
               "TIMELY PRESENT all offers to and from the client, unless the client has WAIVED that duty.",
               "Disclose MATERIAL FACTS concerning the transaction of which the licensee has ACTUAL KNOWLEDGE, unless the information is confidential.",
               "Timely ACCOUNT for all money and property in which the client has or may have an interest.",
               "Obey the client's specific directions.",
               "Material facts do NOT include, for real estate that is not the subject of the transaction: physical conditions without a substantial adverse effect on value, fact situations, or occurrences and acts at the property."],
         "check": [("A licensee must disclose material facts of which they have:", "Actual knowledge, unless the information is confidential", ["Any suspicion", "Only what the seller wrote down"], "225 ILCS 454/15-15(a)(2)(C)."),
                   ("The duty to present all offers:", "May be waived by the client", ["Can never be waived", "Is waived automatically under contract"], "225 ILCS 454/15-15(a)(2)(B).")]},
        {"h": "Duties to a customer (15-25)",
         "p": ["Licensees must treat all CUSTOMERS honestly and must not negligently or knowingly give them false information. A licensee engaged by a SELLER CLIENT must timely disclose to customers who are prospective buyers all LATENT MATERIAL ADVERSE FACTS about the PHYSICAL CONDITION of the property that are ACTUALLY KNOWN to the licensee and that could NOT be discovered by a reasonably diligent inspection by the customer."],
         "l": ["A licensee is NOT liable to a customer for false information that the licensee's own CLIENT supplied, where the licensee did not actually know it was false.",
               "No cause of action arises against a licensee for revealing information in compliance with this section."],
         "check": [("A seller's licensee must disclose to a prospective buyer:", "Latent material adverse facts about physical condition, actually known and not reasonably discoverable", ["Every fact about the property", "Nothing at all"], "225 ILCS 454/15-25."),
                   ("A licensee repeats false information their client gave them, not knowing it was false. The licensee is:", "Not liable to the customer", ["Strictly liable", "Liable only for half"], "225 ILCS 454/15-25.")]},
        {"h": "After the agreement ends (15-30)",
         "p": ["Unless a written agreement says otherwise, neither the sponsoring broker nor any affiliated licensee owes further duties after termination, expiry or completion of the brokerage agreement, EXCEPT to account for all money and property relating to the transaction, and to KEEP CONFIDENTIAL all confidential information."],
         "check": [("After a brokerage agreement ends, the licensee still must:", "Account for money and keep confidential information confidential", ["Continue seeking a buyer", "Do nothing further"], "225 ILCS 454/15-30.")]},
        {"h": "Exclusive brokerage agreements and minimum services (15-75)",
         "l": ["ALL exclusive brokerage agreements must be IN WRITING.",
               "They must specify that the sponsoring broker, through one or more sponsored licensees, provides at a minimum: accepting delivery of and presenting offers and counteroffers; assisting the client in developing, communicating, negotiating and presenting offers, counteroffers and related notices until a lease or purchase agreement is signed and all contingencies are satisfied or waived; and answering the client's questions about those offers, counteroffers, notices and contingencies."],
         "check": [("Exclusive brokerage agreements in Illinois must be:", "In writing, and must specify the minimum services", ["Oral until an offer", "Filed with the Department"], "225 ILCS 454/15-75."),
                   ("Minimum services continue until:", "A lease or purchase agreement is signed and all contingencies are satisfied or waived", ["The offer is accepted", "The listing expires"], "225 ILCS 454/15-75(2).")]},
        {"h": "Money, records and the managing broker",
         "l": ["ESCROW MONEYS means all money, promissory notes or other legal tender or financial consideration deposited with any person for the benefit of the parties. A transaction exists once an agreement is reached and an accepted contract signed or lease agreed (225 ILCS 454/1-10).",
               "The DESIGNATED MANAGING BROKER is responsible for, and supervises, ALL SPECIAL ACCOUNTS of the company.",
               "The designated managing broker must DIRECTLY HANDLE all earnest money, escrows and contract negotiations for any transaction where the designated agent has NOT completed their 45 hours of post-license education - and must approve that licensee's advertisements.",
               "Records relating to a special account transaction are kept a minimum of FIVE YEARS; electronic records are backed up at least monthly.",
               "The office may not sit inside a retail or financial business unless clearly separated and in a distinct area."],
         "check": [("Who supervises all special accounts of an Illinois brokerage?", "The designated managing broker", ["Each sponsored licensee", "The Department"], "225 ILCS 454/5-50."),
                   ("Where a designated agent has not finished their 45 post-license hours, earnest money and contract negotiations are:", "Handled directly by the designated managing broker", ["Handled as normal", "Referred to the Department"], "225 ILCS 454/5-50."),
                   ("Special account transaction records are kept for a minimum of:", "Five years", ["Three years", "Seven years"], "225 ILCS 454/5-50.")]},
        {"h": "Discipline (20-20)",
         "p": ["The Department may refuse to issue or renew, place on probation, suspend or revoke a licence, reprimand, take other disciplinary or non-disciplinary action, and impose a FINE NOT TO EXCEEDING $25,000 FOR EACH VIOLATION - against a licensee or applicant, or against a licensee handling their own property."],
         "check": [("The maximum Illinois fine is:", "$25,000 for each violation", ["$5,000 per violation", "$10,000 per case"], "225 ILCS 454/20-20(a)."),
                   ("Discipline may be imposed against a licensee:", "Even when handling their own property", ["Only in client transactions", "Only for escrow errors"], "225 ILCS 454/20-20(a).")]},
    ],
    "traps": [
        "Illinois PRESUMES designated agency. Nothing signed still means you represent them.",
        "Latent, material, adverse, physical, actually known, not reasonably discoverable - all six words matter in 15-25.",
        "Exclusive agreements: written, with the three minimum services.",
        "$25,000 per violation, and it reaches a licensee's own property deals.",
        "Five years for special account records.",
    ],
    "vocab": [
        ["Designated agent", "The individual licensee named as the consumer's agent; Illinois' default."],
        ["Sponsoring broker", "The brokerage a licensee works under."],
        ["Designated managing broker", "The supervising broker responsible for special accounts and training."],
        ["Latent material adverse fact", "A hidden physical defect a seller's licensee must disclose to a buyer."],
        ["Escrow moneys", "Money or consideration deposited for the benefit of the parties."],
        ["Minimum services", "The three services an exclusive brokerage agreement must promise."],
    ],
    "examples": [
        {"t": "No paperwork, still an agent",
         "s": "A licensee shows homes to a buyer who has signed nothing.",
         "w": ["225 ILCS 454/15-10 presumes designated agency.",
               "Only a written agreement with the sponsoring broker changes that."],
         "k": "The licensee is the buyer's designated agent, with the full 15-15 duties."},
    ],
}

STUDY["il/disclosures"] = {
    "summary": "Ten items. Dual agency in Illinois needs informed written consent, and the Act prints the words that consent must contain. Illinois also forbids the transactional-broker role that other states rely on.",
    "sections": [
        {"h": "Dual agency (15-45)",
         "l": ["A licensee may act as a dual agent, or a sponsoring broker may permit sponsored licensees to do so, ONLY with the INFORMED WRITTEN CONSENT of ALL CLIENTS.",
               "Informed written consent is PRESUMED where the client signs a document containing the statutory language the Act sets out.",
               "That language tells the client dual representation is a CONFLICT OF INTEREST, that both clients may rely on the licensee's advice while their interests may be adverse, that any agreement on price and terms results from negotiation between the clients acting in their own interests, and that the client has been ADVISED TO SEEK INDEPENDENT ADVICE from their own advisors or attorneys before signing.",
               "The Act then lists what a licensee CAN do as a dual agent, beginning with treating all clients honestly."],
         "check": [("Dual agency in Illinois requires:", "Informed written consent of all clients", ["Verbal consent", "The sponsoring broker's approval alone"], "225 ILCS 454/15-45(a)."),
                   ("Informed written consent is presumed where:", "The client signs a document containing the statutory language", ["The licensee explains it orally", "The Department is notified"], "225 ILCS 454/15-45(a)."),
                   ("The statutory dual agency language advises the client to:", "Seek independent advice from their own advisors or attorneys", ["Waive all claims", "Accept the licensee's valuation"], "225 ILCS 454/15-45(a).")]},
        {"h": "What Illinois does not allow",
         "p": ["The state outline lists a PROHIBITION AGAINST TRANSACTIONAL BROKER AND FACILITATOR. Illinois has no non-agency middle role: a licensee is a designated agent, a dual agent with consent, or in a disclosed no-agency relationship. Answers offering 'transaction broker' or 'facilitator' as an Illinois option are wrong."],
         "check": [("Acting as a transactional broker or facilitator in Illinois is:", "Prohibited", ["The default relationship", "Allowed with disclosure"], "The Act provides no such role."),
                   ("Which is an Illinois relationship?", "Designated agency", ["Transaction brokerage", "Facilitation"], "225 ILCS 454/15-10.")]},
        {"h": "Other disclosures on the outline",
         "l": ["NOTICE OF NO AGENCY RELATIONSHIP, where the licensee is not representing the consumer.",
               "CONTEMPORANEOUS OFFERS - where more than one offer is in play at once.",
               "LICENSEE STATUS and any DIRECT OR INDIRECT INTEREST the licensee holds.",
               "COMPENSATION SOURCES.",
               "The RESIDENTIAL REAL PROPERTY DISCLOSURE ACT, and MATERIAL DEFECTS.",
               "Environmental and other disclosures: RADON, LEAD-BASED PAINT, MINE SUBSIDENCE, UNDERGROUND STORAGE TANKS, and FLOODING for landlords."],
         "check": [("Which environmental disclosure is distinctively Illinois?", "Mine subsidence", ["Lead-based paint", "Radon"], "Lead and radon are national; mine subsidence is an Illinois concern."),
                   ("Flooding disclosure on the Illinois outline applies to:", "Landlords", ["Sellers only", "Lenders"], "The state content outline lists it under landlords.")]},
        {"h": "Compensation does not decide agency",
         "p": ["Who pays does not determine who is represented. The Act keeps compensation and agency apart, which is why a buyer's designated agent paid from the seller's proceeds still represents the buyer."],
         "check": [("A buyer's agent paid out of the seller's commission represents:", "The buyer", ["The seller, because they pay", "Both parties"], "Compensation does not determine agency.")]},
    ],
    "traps": [
        "Illinois has NO transaction broker and NO facilitator. That alone kills several answer options.",
        "Dual agency: informed WRITTEN consent of ALL clients, with the statutory wording.",
        "Mine subsidence and underground storage tanks are on the Illinois list.",
        "Payment never decides representation.",
    ],
    "vocab": [
        ["Informed written consent", "Consent given on a document carrying the statutory dual agency language."],
        ["Contemporaneous offers", "More than one offer pending at the same time."],
        ["Mine subsidence", "Ground movement from old mine workings; an Illinois disclosure."],
        ["No agency relationship", "A disclosed relationship where the licensee represents neither party."],
    ],
    "examples": [
        {"t": "Both sides, one agent",
         "s": "A designated agent's buyer client wants the house their seller client listed.",
         "w": ["That licensee would be a dual agent.",
               "It is allowed only with the informed written consent of both clients.",
               "Consent is presumed if both signed the statutory dual agency language."],
         "k": "Get both consents in writing before proceeding, or hand one side to another designated agent."},
    ],
}

STUDY["il/other-laws"] = {
    "summary": "Ten items of Illinois law outside the Act. The standout is fair housing: Illinois protects about twenty characteristics, including source of income and immigration status.",
    "sections": [
        {"h": "The Illinois Human Rights Act",
         "p": ["Illinois protects far more than federal law. The Department of Human Rights lists these protected characteristics:"],
         "l": ["Race, Color, Ancestry, National Origin", "Religion",
               "Sex, Sexual Orientation (including gender identity), Sexual Harassment",
               "Disability, physical and mental", "Age (40 and over)",
               "Marital Status, Familial Status",
               "Pregnancy (including childbirth and related conditions), Reproductive Health Decisions",
               "Military Status, Unfavorable Military Discharge",
               "Order of Protection Status", "Arrest Record",
               "Immigration Status", "SOURCE OF INCOME"],
         "check": [("Which is protected in Illinois housing but not by the federal Fair Housing Act?", "Source of income", ["Race", "Religion", "National origin"], "Illinois Department of Human Rights."),
                   ("Refusing to accept a housing voucher in Illinois is:", "Unlawful source-of-income discrimination", ["A landlord's free choice", "Permitted for small landlords"], "IDHR lists refusal to accept vouchers as discrimination."),
                   ("Age is protected in Illinois:", "At 40 and over", ["At any age", "Only under 18"], "Illinois Department of Human Rights."),
                   ("Which of these is an Illinois protected characteristic?", "Order of protection status", ["Credit score", "Occupation", "Education level"], "Illinois Department of Human Rights.")]},
        {"h": "Ownership and transfer",
         "l": ["The outline reaches TRUSTS - the Illinois land trust is a familiar device - HOMESTEAD, government powers, CO-OWNERSHIP, CONDOMINIUMS and COOPERATIVES.",
               "TRANSFER TAXES are charged on conveyance, and the outline tests them under Illinois law rather than the national material.",
               "TRANSFER OF TITLE covers voluntary and involuntary transfer.",
               "LEGAL DESCRIPTION and the PLAT ACT.",
               "REAL ESTATE TAXES AND EXEMPTIONS."],
         "check": [("Which Illinois device appears under ownership interests on the outline?", "Trusts", ["Life tenancies only", "Community property"], "The Illinois land trust is a long-standing device."),
                   ("Illinois is a community property state:", "No - it is not", ["Yes", "Only for homesteads"], "Community property is not Illinois law.")]},
        {"h": "Staying inside the licence",
         "l": ["The outline warns against PERFORMING ACTIVITIES EXCEEDING THE SCOPE of a real estate licence: practising LAW, dealing in SECURITIES, and the ILLINOIS BUSINESS BROKER ACT.",
               "The leading case is CHICAGO BAR ASSOCIATION v. QUINLAN AND TYSON, INC., which marks the line between a licensee filling in a contract and a licensee practising law.",
               "A COMPARATIVE MARKET ANALYSIS is not an appraisal within the Real Estate Appraiser Licensing Act of 2002 (225 ILCS 454/1-10), but acting beyond a CMA can be unauthorised appraisal practice."],
         "check": [("Chicago Bar Association v. Quinlan and Tyson concerns:", "The line between completing a contract and practising law", ["Commission splits", "Fair housing", "Escrow deadlines"], "It is named in the state outline."),
                   ("A comparative market analysis in Illinois is:", "Not an appraisal under the Appraiser Licensing Act", ["An appraisal requiring a licence", "Prohibited"], "225 ILCS 454/1-10.")]},
        {"h": "Other Illinois statutes on the outline",
         "l": ["The ILLINOIS ASSISTANCE ANIMAL INTEGRITY ACT.",
               "The ILLINOIS LANDLORD TENANT ACT.",
               "The COMMERCIAL BROKER LIEN ACT, which lets a broker claim a lien for commission on commercial property.",
               "The RADON RESISTANT CONSTRUCTION ACT."],
         "check": [("The Commercial Broker Lien Act lets a broker:", "Claim a lien for commission on commercial property", ["Lien a residence", "Seize earnest money"], "It is on the state content outline."),
                   ("The Radon Resistant Construction Act concerns:", "Building techniques that limit radon entry", ["Radon testing fees", "Radon in commercial leases"], "It is on the state content outline.")]},
    ],
    "traps": [
        "Illinois fair housing goes far past the federal seven - source of income and immigration status included.",
        "Refusing a housing voucher is discrimination in Illinois.",
        "Illinois is NOT a community property state.",
        "Quinlan and Tyson is the practice-of-law case the outline names.",
    ],
    "vocab": [
        ["Source of income", "An Illinois protected characteristic; covers housing vouchers."],
        ["Land trust", "An Illinois device holding title with the beneficiary's interest kept private."],
        ["Commercial Broker Lien Act", "Illinois statute allowing a commission lien on commercial property."],
        ["Mine subsidence", "Ground settlement over old mine workings."],
        ["Plat Act", "The Illinois statute governing subdivision plats."],
    ],
    "examples": [],
}

STUDY["il/licensing"] = {
    "summary": "Four items. Illinois issues a BROKER licence at entry, not a salesperson licence: 75 hours in, 45 hours of post-licence education, then 12 hours of continuing education each term.",
    "sections": [
        {"h": "The grades of licence",
         "l": ["BROKER - the entry-level licence.",
               "MANAGING BROKER - the supervising grade.",
               "RESIDENTIAL LEASING AGENT.",
               "INSTRUCTOR, for pre-licence and continuing education.",
               "There is no Illinois 'salesperson' licence."],
         "check": [("Illinois' entry-level real estate licence is:", "Broker", ["Salesperson", "Agent", "Associate"], "Managing broker is the supervising grade."),
                   ("Which is an Illinois licence category?", "Residential leasing agent", ["Transaction broker", "Facilitator"], "225 ILCS 454/5-27 and the state outline.")]},
        {"h": "Qualifying as a broker (5-27)",
         "l": ["Be at least 18 YEARS OLD.",
               "Be of GOOD MORAL CHARACTER.",
               "Complete a four-year high school course of study, or hold a State of Illinois High School Diploma, verified under oath.",
               "Complete 75 HOURS of Department-approved real estate instruction, of which 15 HOURS must be SITUATIONAL AND CASE STUDIES, presented in a classroom, by live interactive webinar, or by online distance education.",
               "Personally take and pass the written examination.",
               "Be SPONSORED - a licensee acts under a sponsoring broker."],
         "check": [("Illinois pre-licence education for a broker is:", "75 hours, 15 of them situational and case studies", ["90 hours", "60 hours", "120 hours"], "225 ILCS 454/5-27(a)(5)."),
                   ("The minimum age for an Illinois broker licence is:", "18", ["17", "19", "21"], "225 ILCS 454/5-27(a)(1).")]},
        {"h": "Exemptions (5-20)",
         "l": ["An OWNER or LESSOR performing broker acts only for their own property, and their REGULAR EMPLOYEE doing so incidentally to managing that property. The exemption does NOT extend to acts for property the person does not own or lease.",
               "An ATTORNEY IN FACT under a duly executed and recorded power of attorney to convey real estate, and an ATTORNEY AT LAW performing their duties as such.",
               "A RECEIVER, TRUSTEE IN BANKRUPTCY, ADMINISTRATOR, EXECUTOR or GUARDIAN, or a person acting under court order."],
         "check": [("An owner's regular employee leasing the owner's own building is:", "Exempt from licensing", ["Required to be a broker", "Required to be a leasing agent"], "225 ILCS 454/5-20(1)(B)."),
                   ("The owner exemption covers:", "Only the owned or leased property", ["Any property the owner markets", "All property in the portfolio"], "225 ILCS 454/5-20(1).")]},
        {"h": "After licensure",
         "l": ["POST-LICENCE: a first-time broker licensed on or after 9 August 2019 must complete 45 HOURS of post-licence education - three 15-hour courses covering applied brokerage principles, risk management and discipline, and transactional issues. Each course carries its own 50-question final examination.",
               "CONTINUING EDUCATION: 12 HOURS of approved courses during the current term of the licence (225 ILCS 454/5-70(b)).",
               "A managing broker adds a 12-HOUR BROKER MANAGEMENT course.",
               "The CORE CURRICULUM is 6 hours of the total, and must include at least 2 CREDIT HOURS OF FAIR HOUSING training.",
               "No more than 12 hours of continuing education credit may be taken in one calendar day, and a given course counts only once per licence term."],
         "check": [("Illinois post-licence education is:", "45 hours in three 15-hour courses", ["30 hours", "90 hours", "12 hours"], "225 ILCS 454/5-45."),
                   ("Illinois continuing education for a broker is:", "12 hours per licence term", ["30 hours", "14 hours", "22.5 hours"], "225 ILCS 454/5-70(b)."),
                   ("The core curriculum must include at least:", "2 credit hours of fair housing training", ["4 hours of ethics", "1 hour of maths"], "225 ILCS 454/5-70."),
                   ("A managing broker must additionally complete:", "A 12-hour broker management course", ["A 6-hour ethics course", "Nothing extra"], "225 ILCS 454/5-70(b).")]},
    ],
    "traps": [
        "Entry grade is BROKER. 'Salesperson' is not an Illinois licence.",
        "75 hours in (15 situational), 45 hours post-licence, 12 hours CE a term.",
        "The owner exemption stops at property the owner does not own or lease.",
        "Fair housing is a named 2-hour slice of the core curriculum.",
    ],
    "vocab": [
        ["Broker", "Illinois' entry-level licence."],
        ["Managing broker", "The supervising grade, with extra education."],
        ["Residential leasing agent", "A separate Illinois licence for leasing work."],
        ["Sponsoring broker", "The brokerage that sponsors a licensee."],
        ["Core curriculum", "The 6 required hours inside the 12-hour CE requirement."],
    ],
    "examples": [],
}


# ------------------------------------------------------------- questions

Q = [
 # license act
 ("il/license-act", "Agency presumed", 1, "An Illinois licensee working with a consumer, with nothing in writing, is:",
  "That consumer's designated agent", ["A transaction broker", "Representing nobody", "The seller's subagent"],
  "225 ILCS 454/15-10."),
 ("il/license-act", "Agency presumed", 2, "To establish a relationship other than designated agency, Illinois requires:",
  "A written agreement between the sponsoring broker and the consumer", ["An oral understanding", "A note in the transaction file", "Department approval"],
  "225 ILCS 454/15-10."),
 ("il/license-act", "Agency presumed", 3, "Where the relationship is designated agency, whether dual agency exists is decided by:",
  "The relationships of the designated agents of the parties", ["The sponsoring broker's relationships", "Who pays the commission", "The size of the brokerage"],
  "225 ILCS 454/1-10."),
 ("il/license-act", "Client duties", 1, "A licensee must disclose to a client material facts of which they have:",
  "Actual knowledge, unless the information is confidential", ["Any suspicion", "Only what is written down", "Nothing beyond the listing"],
  "225 ILCS 454/15-15(a)(2)(C)."),
 ("il/license-act", "Client duties", 2, "The duty to timely present all offers to a client:",
  "May be waived by the client", ["Can never be waived", "Is waived once under contract", "Applies only to written offers above list price"],
  "225 ILCS 454/15-15(a)(2)(B)."),
 ("il/license-act", "Client duties", 2, "A licensee representing a client must account for money in which the client has an interest:",
  "Timely", ["At closing only", "Annually", "On request only"],
  "225 ILCS 454/15-15(a)(2)(D)."),
 ("il/license-act", "Client duties", 3, "Material facts under 15-15 do NOT include, for property not the subject of the transaction:",
  "Physical conditions without a substantial adverse effect on value", ["Known structural defects in the subject property", "The condition of the roof being sold"],
  "225 ILCS 454/15-15(a)(2)(C)."),
 ("il/license-act", "Customer duties", 1, "A seller's licensee must disclose to a prospective buyer:",
  "Latent material adverse facts about physical condition, actually known and not reasonably discoverable", ["Every fact about the property", "Nothing, as the buyer is a customer", "Only what the seller permits"],
  "225 ILCS 454/15-25."),
 ("il/license-act", "Customer duties", 2, "A licensee passes on false information given by their client, not knowing it was false. The licensee is:",
  "Not liable to the customer", ["Strictly liable", "Liable for half the loss", "Liable only if a contract results"],
  "225 ILCS 454/15-25."),
 ("il/license-act", "Customer duties", 2, "Licensees must treat all customers:",
  "Honestly, without negligently or knowingly giving false information", ["As clients", "With full fiduciary duties", "With no duty at all"],
  "225 ILCS 454/15-25."),
 ("il/license-act", "After termination", 2, "After a brokerage agreement ends, the licensee still owes a duty to:",
  "Account for money and keep confidential information confidential", ["Keep seeking a buyer", "Present further offers", "Nothing at all"],
  "225 ILCS 454/15-30."),
 ("il/license-act", "Brokerage agreements", 1, "Exclusive brokerage agreements in Illinois must be:",
  "In writing, specifying the minimum services", ["Oral until an offer is made", "Filed with the Department", "Witnessed by two people"],
  "225 ILCS 454/15-75."),
 ("il/license-act", "Brokerage agreements", 2, "Minimum services under an exclusive agreement continue until:",
  "A lease or purchase agreement is signed and all contingencies are satisfied or waived", ["The offer is accepted", "The listing expires", "Closing"],
  "225 ILCS 454/15-75(2)."),
 ("il/license-act", "Brokerage agreements", 3, "Which is one of the statutory minimum services?",
  "Answering the client's questions about offers, counteroffers, notices and contingencies", ["Holding an open house weekly", "Paying for photography", "Guaranteeing a sale"],
  "225 ILCS 454/15-75(3)."),
 ("il/license-act", "Money", 1, "Who supervises all special accounts of an Illinois brokerage?",
  "The designated managing broker", ["Each sponsored licensee", "The Department", "The closing attorney"],
  "225 ILCS 454/5-50."),
 ("il/license-act", "Money", 2, "Where a designated agent has not completed their 45 hours of post-licence education, earnest money and contract negotiations must be:",
  "Handled directly by the designated managing broker", ["Handled by the licensee as normal", "Referred to the Department", "Held by the buyer's attorney"],
  "225 ILCS 454/5-50."),
 ("il/license-act", "Money", 2, "Records of a special account transaction are kept for a minimum of:",
  "Five years", ["Three years", "Seven years", "One year"],
  "225 ILCS 454/5-50."),
 ("il/license-act", "Money", 3, "Escrow moneys under the Act include:",
  "Money, promissory notes or other legal tender deposited for the benefit of the parties", ["Only cash", "Only certified funds", "Only the broker's commission"],
  "225 ILCS 454/1-10."),
 ("il/license-act", "Discipline", 1, "The maximum Illinois fine for a violation is:",
  "$25,000 for each violation", ["$5,000", "$10,000", "$1,000"],
  "225 ILCS 454/20-20(a)."),
 ("il/license-act", "Discipline", 2, "Discipline under 20-20 may be imposed against a licensee:",
  "Even when handling their own property", ["Only in client transactions", "Only for escrow violations", "Only after a criminal conviction"],
  "225 ILCS 454/20-20(a)."),
 ("il/license-act", "Offices", 3, "A brokerage office inside a retail establishment must be:",
  "Clearly separated and situated in a distinct area", ["Prohibited entirely", "Approved by the Department", "Open to the public at all hours"],
  "225 ILCS 454/5-50."),

 # disclosures
 ("il/disclosures", "Dual agency", 1, "Dual agency in Illinois requires:",
  "The informed written consent of all clients", ["Verbal consent", "The sponsoring broker's approval alone", "Department approval"],
  "225 ILCS 454/15-45(a)."),
 ("il/disclosures", "Dual agency", 2, "Informed written consent is presumed where:",
  "The client signs a document containing the statutory language", ["The licensee explains it orally", "The client does not object", "The Department is notified"],
  "225 ILCS 454/15-45(a)."),
 ("il/disclosures", "Dual agency", 2, "The statutory dual agency language advises the client to:",
  "Seek independent advice from their own advisors or attorneys", ["Waive all claims against the licensee", "Accept the licensee's valuation", "Pay a higher commission"],
  "225 ILCS 454/15-45(a)."),
 ("il/disclosures", "Dual agency", 3, "The statutory language describes dual representation as:",
  "A conflict of interest, since both clients may rely on the licensee's advice", ["A routine arrangement", "A benefit to the buyer", "Required by law"],
  "225 ILCS 454/15-45(a)."),
 ("il/disclosures", "Prohibited roles", 1, "Acting as a transactional broker or facilitator in Illinois is:",
  "Prohibited", ["The default relationship", "Allowed with written disclosure", "Allowed in commercial deals"],
  "The Act provides no such role; the state outline lists the prohibition."),
 ("il/disclosures", "Prohibited roles", 2, "Which is a recognised Illinois relationship?",
  "Designated agency", ["Transaction brokerage", "Facilitation", "Non-agency brokerage"],
  "225 ILCS 454/15-10."),
 ("il/disclosures", "Compensation", 1, "A buyer's designated agent paid out of the seller's proceeds represents:",
  "The buyer", ["The seller, because they pay", "Both parties", "Neither party"],
  "Compensation does not determine agency."),
 ("il/disclosures", "Property condition", 1, "Residential property condition disclosure in Illinois is governed by:",
  "The Residential Real Property Disclosure Act", ["The Plat Act", "The Commercial Broker Lien Act", "The Human Rights Act"],
  "Named on the state content outline."),
 ("il/disclosures", "Environmental", 2, "Which environmental disclosure is distinctively Illinois?",
  "Mine subsidence", ["Lead-based paint", "Radon", "Asbestos"],
  "Lead and radon are national concerns; mine subsidence is Illinois-specific."),
 ("il/disclosures", "Environmental", 2, "Flooding disclosure on the Illinois outline applies to:",
  "Landlords", ["Sellers only", "Lenders", "Appraisers"],
  "The state content outline lists flooding under landlords."),
 ("il/disclosures", "Environmental", 2, "Which is on the Illinois environmental disclosure list?",
  "Underground storage tanks", ["Wetlands delineation", "Seismic zones", "Coastal erosion"],
  "State content outline."),
 ("il/disclosures", "Agency notice", 2, "Where a licensee represents neither party, Illinois uses:",
  "A notice of no agency relationship", ["A transaction broker agreement", "A facilitator disclosure", "No notice at all"],
  "State content outline."),
 ("il/disclosures", "Interests", 2, "A licensee with a direct or indirect interest in the property must:",
  "Disclose that interest", ["Say nothing", "Withdraw from the deal", "Notify only the broker"],
  "State content outline; licensee status disclosure."),

 # other laws
 ("il/other-laws", "Fair housing", 1, "Which is protected in Illinois housing but not by the federal Fair Housing Act?",
  "Source of income", ["Race", "Religion", "National origin"],
  "Illinois Department of Human Rights."),
 ("il/other-laws", "Fair housing", 1, "Refusing to accept a housing voucher in Illinois is:",
  "Unlawful source-of-income discrimination", ["A landlord's free choice", "Permitted for small landlords", "Permitted if disclosed"],
  "IDHR lists refusal to accept vouchers as discrimination."),
 ("il/other-laws", "Fair housing", 2, "Age is protected in Illinois housing:",
  "At 40 and over", ["At any age", "Only under 18", "Only over 65"],
  "Illinois Department of Human Rights."),
 ("il/other-laws", "Fair housing", 2, "Which is an Illinois protected characteristic?",
  "Order of protection status", ["Credit score", "Occupation", "Education level"],
  "Illinois Department of Human Rights."),
 ("il/other-laws", "Fair housing", 2, "Illinois also protects:",
  "Immigration status", ["Length of employment", "Vehicle ownership", "Club membership"],
  "Illinois Department of Human Rights."),
 ("il/other-laws", "Fair housing", 3, "Illinois protects reproductive health decisions:",
  "Yes, as a listed characteristic", ["No", "Only in employment", "Only in lending"],
  "Illinois Department of Human Rights."),
 ("il/other-laws", "Ownership", 2, "Illinois is a community property state:",
  "No", ["Yes", "Only for homesteads", "Only for spouses who elect it"],
  "Community property is not Illinois law."),
 ("il/other-laws", "Ownership", 2, "Which device appears under Illinois ownership interests on the outline?",
  "Trusts", ["Community property", "Dower and curtesy", "Tenancy by sufferance only"],
  "The Illinois land trust is a long-standing device."),
 ("il/other-laws", "Practice of law", 2, "Chicago Bar Association v. Quinlan and Tyson, Inc. concerns:",
  "The line between completing a contract and practising law", ["Commission splits", "Fair housing", "Escrow deadlines"],
  "Named on the Illinois state content outline."),
 ("il/other-laws", "Appraisal", 2, "A comparative market analysis in Illinois is:",
  "Not an appraisal under the Real Estate Appraiser Licensing Act of 2002", ["An appraisal requiring an appraiser licence", "Prohibited for brokers", "Allowed only for commercial property"],
  "225 ILCS 454/1-10."),
 ("il/other-laws", "Liens", 2, "The Commercial Broker Lien Act lets a broker:",
  "Claim a lien for commission on commercial property", ["Lien a private residence", "Seize earnest money", "Foreclose on a client"],
  "Named on the state content outline."),
 ("il/other-laws", "Other statutes", 3, "The Radon Resistant Construction Act concerns:",
  "Construction techniques that limit radon entry", ["Radon testing fees", "Radon disclosure in leases", "Radon insurance"],
  "Named on the state content outline."),
 ("il/other-laws", "Other statutes", 3, "The Illinois Assistance Animal Integrity Act addresses:",
  "Assistance animals and claims about them", ["Pet deposits generally", "Kennel licensing", "Veterinary fees"],
  "Named on the state content outline."),

 # licensing
 ("il/licensing", "Licence grades", 1, "Illinois' entry-level real estate licence is:",
  "Broker", ["Salesperson", "Agent", "Associate broker"],
  "Managing broker is the supervising grade."),
 ("il/licensing", "Licence grades", 2, "Which is an Illinois licence category?",
  "Residential leasing agent", ["Transaction broker", "Facilitator", "Sales associate"],
  "225 ILCS 454/5-27 and the state outline."),
 ("il/licensing", "Education", 1, "Illinois pre-licence education for a broker is:",
  "75 hours, 15 of them situational and case studies", ["90 hours", "60 hours", "120 hours"],
  "225 ILCS 454/5-27(a)(5)."),
 ("il/licensing", "Education", 1, "Illinois post-licence education is:",
  "45 hours, in three 15-hour courses", ["30 hours", "90 hours", "12 hours"],
  "Applied brokerage principles, risk management and discipline, transactional issues."),
 ("il/licensing", "Education", 1, "Continuing education for an Illinois broker is:",
  "12 hours per licence term", ["30 hours", "14 hours", "22.5 hours"],
  "225 ILCS 454/5-70(b)."),
 ("il/licensing", "Education", 2, "The core curriculum must include at least:",
  "2 credit hours of fair housing training", ["4 hours of ethics", "1 hour of maths", "3 hours of agency"],
  "225 ILCS 454/5-70."),
 ("il/licensing", "Education", 2, "A managing broker must additionally complete:",
  "A 12-hour broker management course", ["A 6-hour ethics course", "A 15-hour appraisal course", "Nothing extra"],
  "225 ILCS 454/5-70(b)."),
 ("il/licensing", "Education", 3, "No more than how many hours of continuing education may be taken in one calendar day?",
  "12", ["6", "8", "There is no limit"],
  "225 ILCS 454/5-70(j)."),
 ("il/licensing", "Education", 3, "Each 15-hour post-licence course requires:",
  "Its own 50-question final examination", ["No examination", "A state-administered exam", "A written essay"],
  "225 ILCS 454/5-45."),
 ("il/licensing", "Qualifying", 1, "The minimum age for an Illinois broker licence is:",
  "18", ["17", "19", "21"],
  "225 ILCS 454/5-27(a)(1)."),
 ("il/licensing", "Qualifying", 2, "An Illinois broker applicant must also:",
  "Be of good moral character and hold a high school diploma or equivalent", ["Hold a college degree", "Have two years' sales experience", "Own property in Illinois"],
  "225 ILCS 454/5-27(a)(2)-(3)."),
 ("il/licensing", "Exemptions", 2, "An owner's regular employee leasing the owner's own building is:",
  "Exempt from licensing", ["Required to hold a broker licence", "Required to hold a leasing agent licence", "Exempt only for residential"],
  "225 ILCS 454/5-20(1)(B)."),
 ("il/licensing", "Exemptions", 2, "The Illinois owner exemption covers:",
  "Only the property the person owns or leases", ["Any property the owner markets", "The owner's whole portfolio including managed property"],
  "225 ILCS 454/5-20(1)."),
 ("il/licensing", "Exemptions", 3, "Which person is exempt from the Illinois licence requirement?",
  "A trustee in bankruptcy acting as such", ["A property manager paid a commission", "A leasing agent for a third party", "A buyer's representative paid a fee"],
  "225 ILCS 454/5-20(3)."),
 ("il/licensing", "Exemptions", 3, "An attorney in fact is exempt where acting under:",
  "A duly executed and recorded power of attorney to convey real estate", ["Any written authority", "An oral appointment", "A listing agreement"],
  "225 ILCS 454/5-20(2)."),
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
            "id": "il-" + hashlib.sha1(q.encode()).hexdigest()[:8],
            "portion": "georgia", "topic": topic, "subtopic": sub,
            "sub": topic + "|" + sub, "concept": "Illinois " + sub.lower(),
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
        "code": "IL", "name": "Illinois", "abbr": "IL",
        "regulator": "IDFPR Division of Real Estate",
        "pass": EXAM["pass"],
        "portions": {
            "national": {"scored": EXAM["national_scored"],
                         "minutes": EXAM["national_minutes"],
                         "pass": EXAM["national_pass"]},
            "georgia": {"name": "Illinois state", "scored": EXAM["state_scored"],
                        "minutes": EXAM["state_minutes"],
                        "pass": EXAM["state_pass"],
                        "blurb": "The Real Estate License Act of 2000, agency, disclosures and Illinois law."},
        },
        "topics": topics, "bank": bank, "study": study,
        "sources": SOURCES, "diffs": DIFFS,
    }


# Where Illinois departs from the national rule.
DIFFS = {
    "national/agency": [
        "Illinois PRESUMES designated agency: a licensee represents the consumer they work with unless a written agreement with the sponsoring broker says otherwise (225 ILCS 454/15-10).",
        "There is no transaction broker and no facilitator in Illinois. Dual agency needs the informed WRITTEN consent of all clients, using the statutory wording (15-45).",
        "A seller's licensee owes a buyer-customer disclosure of latent material adverse facts about physical condition that are actually known and not reasonably discoverable (15-25).",
    ],
    "national/practice": [
        "The entry-level Illinois licence is a BROKER licence; a managing broker supervises. There is no salesperson licence.",
        "The designated managing broker supervises all special accounts, and must personally handle earnest money and contract negotiations for any licensee who has not finished 45 hours of post-licence education.",
        "Illinois fair housing protects about twenty characteristics, including SOURCE OF INCOME, immigration status, order of protection status and arrest record.",
        "The Department may fine up to $25,000 per violation (225 ILCS 454/20-20).",
    ],
    "national/contracts": [
        "All exclusive brokerage agreements must be in writing and must promise the three statutory minimum services (225 ILCS 454/15-75).",
        "Chicago Bar Association v. Quinlan and Tyson marks where filling in a contract ends and practising law begins.",
    ],
    "national/disclosures": [
        "Illinois adds mine subsidence and underground storage tanks to the usual radon and lead-based paint disclosures, and a flooding disclosure for landlords.",
    ],
}


if __name__ == "__main__":
    import io, json, os
    here = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    out = os.path.join(here, "greprep", "packs", "IL.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    pack = build()
    with io.open(out, "w", encoding="utf-8") as f:
        json.dump(pack, f, ensure_ascii=False, indent=1, sort_keys=True)
    print("wrote", out, len(pack["bank"]), "questions,", len(pack["study"]), "lessons")
