"""Tennessee state content: lessons and practice questions.

Tennessee splits the affiliate broker examination. The PSI bulletin's
tables: National 80 questions in 160 minutes, State 40 questions in 80
minutes, and the minimum passing score is 56 of 80 (70%) on the national
portion and 28 of 40 (70%) on the state portion. A pass on one section is
good for two retakes of the failed section or one year, whichever comes
first.

Tennessee's own vocabulary matters. Its licensees are AFFILIATE BROKERS
under a PRINCIPAL BROKER, its agents are LIMITED AGENTS whose statutory
duties SUPERSEDE common law fiduciary duty, and a licensee who represents
nobody is a FACILITATOR. Seven of the forty state items are advertising
alone.

Every rule below was read on 2026-11-11 from:
  - Tenn. Comp. R. & Regs. 1260-02, Rules of Conduct, as published by the
    Tennessee Secretary of State (revised September 2025).
  - The Tennessee Real Estate Broker License Act of 1973, T.C.A. title 62
    chapter 13, as published in the Tennessee Code. The state itself
    publishes the Code through LexisNexis, so section text was read from
    the published Code and the figures were cross-checked against TREC's
    own rules, bulletin and training materials.
  - The PSI Tennessee Candidate Information Bulletin for TREC, for the
    examination tables, the 40-item state outline and the licensing
    requirements.
  - The TREC Instructor Training Manual on tn.gov, for the continuing
    education requirement.
The section a fact comes from is cited next to it. Do not add a fact here
without reading its source first.
"""

EXAM = {
    # Affiliate broker: National 80 / 160 minutes / 56 correct (70%);
    # State 40 / 80 minutes / 28 correct (70%).
    "state_scored": 40,
    "state_minutes": 80,
    "national_scored": 80,
    "national_minutes": 160,
    "pass": 0.70,
}

# PSI's Tennessee state outline, affiliate broker item counts, summing to 40.
TOPICS = [
    ("tn/advertising", "Advertising and marketing", 7,
     "Firm name and number, signs, teams, internet and social media, gifts."),
    ("tn/agency", "Agency and disclosure issues", 6,
     "Duties to all parties and to clients, disclosure, designated agents, facilitators."),
    ("tn/broker-affiliate", "Broker / affiliate relationships", 5,
     "How compensation is paid, supervision, affiliation changes, listings."),
    ("tn/commission", "Duties and powers of the Commission", 4,
     "What TREC does, what it cannot touch, complaints and discipline."),
    ("tn/licensing", "Licensing requirements", 4,
     "Education, qualifications, change of status, firm licences, renewal, E&O."),
    ("tn/records", "Documents and record keeping", 4,
     "Who keeps what, for how long, handling offers and leaving copies."),
    ("tn/escrow", "Trust and escrow funds", 4,
     "Deposit timing, permitted disbursements, commingling, interest."),
    ("tn/improper", "Other improper activities", 3,
     "Net listings, discrimination and other misconduct."),
    ("tn/special", "Special areas of practice", 3,
     "Timeshare, property management and commercial practice."),
]

SOURCES = [
    {"by": "Tennessee Secretary of State",
     "name": "Tenn. Comp. R. & Regs. 1260-02, Rules of Conduct",
     "note": "Supervision, offices, escrow, advertising, personal interest, gifts, teams and record retention.",
     "url": "https://publications.tnsosfiles.com/rules/1260/1260-02.20250923.pdf"},
    {"by": "Tennessee General Assembly",
     "name": "Tennessee Real Estate Broker License Act of 1973, T.C.A. title 62 chapter 13",
     "note": "Part 4 is the agency law: limited agency, duties to all parties and to clients, written disclosure and designated agents.",
     "url": "https://www.tn.gov/commerce/regboards/trec/rules-and-laws/laws.html"},
    {"by": "Tennessee Real Estate Commission",
     "name": "TREC rules, bulletins and instructor materials",
     "note": "The 90-hour education split, the 16-hour continuing education requirement and the TREC Core course.",
     "url": "https://www.tn.gov/commerce/regboards/trec.html"},
    {"by": "PSI Services and TREC",
     "name": "Tennessee Candidate Information Bulletin",
     "note": "National 80 in 160 minutes with 56 correct, State 40 in 80 with 28 correct, and the 40-item state outline.",
     "url": "https://test-takers.psiexams.com/tnre"},
]


# --------------------------------------------------------------- lessons

STUDY = {}

STUDY["tn/advertising"] = {
    "summary": "Seven items - the largest single block on the Tennessee state paper, and almost all of it is Rule 1260-02-.12. Learn what must appear, and in what size.",
    "sections": [
        {"h": "What counts as advertising (1260-02-.12(1), (2))",
         "l": ["ADVERTISING means anything promoting EITHER A LICENSEE OR THE SALE OR LEASE OF REAL PROPERTY, in any medium - print, radio, television, SIGNS, FLYERS, LETTERHEADS, E-MAIL SIGNATURES, WEBSITES, SOCIAL MEDIA, and VIDEO OR AUDIO transmitted by internet or broadcast streaming.",
               "It does NOT include promotional items that merely advertise a licensee - HATS, PENS, NOTEPADS, T-SHIRTS, NAME TAGS, BUSINESS CARDS, and the SPONSORSHIP OF CHARITABLE AND COMMUNITY EVENTS.",
               "FIRM NAME means either the entire name of the firm AS LICENSED with the Commission, or the firm's D/B/A NAME as licensed."],
         "check": [("Which is NOT advertising under the Tennessee rule?", "A branded notepad or t-shirt", ["A website", "An e-mail signature", "A yard sign"], "Rule 1260-02-.12(1)."),
                   ("'Firm name' means:", "The firm's entire name as licensed, or its licensed d/b/a name", ["The franchise name", "The principal broker's name"], "Rule 1260-02-.12(2)."),
                   ("A video posted to a streaming platform promoting a listing is:", "Advertising, subject to the rule", ["Exempt as content", "Exempt if unpaid"], "Rule 1260-02-.12(1).")]},
        {"h": "The general principles (1260-02-.12(3))",
         "l": ["No licensee may advertise in a manner indicating the licensee is NOT ENGAGED IN THE REAL ESTATE BUSINESS.",
               "ALL advertising is UNDER THE DIRECT SUPERVISION OF THE PRINCIPAL BROKER and must list the FIRM NAME and the FIRM TELEPHONE NUMBER as on file with the Commission. The FIRM NAME must appear in letters THE SAME SIZE OR LARGER than the name of a licensee or of any team or group.",
               "Advertising that refers to an individual licensee must list that licensee's NAME AS LICENSED with the Commission.",
               "No licensee may post a SIGN advertising property without WRITTEN AUTHORISATION FROM THE OWNER or the owner's agent.",
               "No licensee may advertise property LISTED BY ANOTHER LICENSEE without WRITTEN AUTHORISATION from the listing agent or listing broker.",
               "No false, misleading or deceptive advertising - which expressly INCLUDES advertising that shows ONLY THE FRANCHISE NAME without the firm name; a TEAM using words like 'Real Estate', 'Realty', 'Company', 'LLC', 'Inc.' or 'Associates' that suggest it operates independently of the firm; and any WEBPAGE LINKING to an unlicensed entity's site where that entity appears to be doing work requiring a licence."],
         "check": [("In Tennessee advertising, the firm name must appear:", "In letters the same size or larger than the licensee's or team's name", ["Anywhere on the advertisement", "In smaller type than the agent's name"], "Rule 1260-02-.12(3)(b)."),
                   ("Posting a 'For Sale' sign requires:", "Written authorisation from the owner or the owner's agent", ["A verbal go-ahead", "Nothing, if the property is listed"], "Rule 1260-02-.12(3)(d)."),
                   ("Advertising using only the franchise name is:", "False, misleading or deceptive advertising", ["Permitted for franchisees", "Permitted online only"], "Rule 1260-02-.12(3)(f)(1)."),
                   ("A team may NOT use, in its name, words such as:", "Realty, Company, LLC, Inc. or Associates", ["The team leader's surname", "The word 'Team'"], "Rule 1260-02-.12(3)(f)(2)."),
                   ("Advertising another licensee's listing requires:", "Written authorisation from the listing agent or listing broker", ["MLS membership alone", "Nothing"], "Rule 1260-02-.12(3)(e).")]},
        {"h": "Franchise, internet and social media (1260-02-.12(4) to (6))",
         "l": ["A licensee using a FRANCHISE TRADE NAME or advertising as part of a COOPERATIVE GROUP must clearly and unmistakably show their NAME, FIRM NAME and FIRM TELEPHONE NUMBER (all as registered with TREC) ADJACENT TO any specific properties advertised.",
               "The same three items must appear on BUSINESS CARDS, CONTRACTS and other transaction documents that use a franchise trade name.",
               "INTERNET: the firm name and firm telephone number must CONSPICUOUSLY APPEAR ON EACH PAGE of the website. Any page displaying listings from an OUTSIDE DATABASE must state that SOME OR ALL OF THE LISTINGS MAY NOT BELONG to the firm whose site is being visited. Listing information must be KEPT CURRENT AND ACCURATE - a duty that applies to FIRST GENERATION advertising the licensee places, not to syndicated or aggregated copies outside the licensee's control.",
               "SOCIAL MEDIA means internet-based applications or platforms letting the public create and share content - the rule names Facebook, Twitter, Instagram and LinkedIn - and the advertising rule applies to it."],
         "check": [("On a licensee's website, the firm name and telephone number must appear:", "Conspicuously on each page", ["On the home page only", "In the contact page footer"], "Rule 1260-02-.12(5)(a)."),
                   ("A page showing listings pulled from an outside database must state:", "That some or all of the listings may not belong to the firm whose website is being visited", ["The database's name", "The number of listings"], "Rule 1260-02-.12(5)(b)."),
                   ("A franchise-name advertisement for a specific property must show, adjacent to it:", "The licensee's name, the firm name and the firm telephone number as registered with TREC", ["Only the franchise logo", "Only the firm name"], "Rule 1260-02-.12(4)(a)."),
                   ("The duty to keep listing information current applies to:", "First generation advertising the licensee places, not syndicated copies beyond their control", ["Every copy anywhere on the internet", "Nothing online"], "Rule 1260-02-.12(5)(c).")]},
        {"h": "Gifts and prizes (1260-02-.33)",
         "l": ["A licensee may offer a GIFT, PRIZE OR OTHER VALUABLE CONSIDERATION as an inducement to purchase, list or lease real estate ONLY IF the offer is made UNDER THE SPONSORSHIP AND WITH THE APPROVAL OF THE FIRM, and IN WRITING, SIGNED BY THE LICENSEE, disclosing the pertinent details: ACCURATE SPECIFICATIONS of the gift, its FAIR MARKET VALUE, the TIME AND PLACE OF DELIVERY, and ANY REQUIREMENTS the prospect must satisfy.",
               "A licensee SHALL NOT give or pay CASH REBATES, CASH GIFTS, GIFT CARDS, CASH PRIZES or any similar cash-based incentive in a real estate transaction, with three exceptions: a GIFT CARD AT AN OPEN HOUSE FOR OTHER LICENSEES; a GIFT CARD AS A CLOSING GIFT; and those closing-gift cards may NOT be used in any ADVERTISEMENT to induce business."],
         "check": [("A gift offered as an inducement in Tennessee must be:", "Sponsored and approved by the firm, and offered in writing signed by the licensee", ["Approved by TREC", "Worth less than $100"], "Rule 1260-02-.33(1)."),
                   ("Cash rebates and gift cards as transaction incentives are:", "Prohibited, except a gift card at a licensee open house or as a closing gift", ["Always allowed", "Allowed up to $500"], "Rule 1260-02-.33(2)."),
                   ("A closing-gift gift card:", "May not be used in advertising to induce business", ["May be advertised freely", "Must be reported to TREC"], "Rule 1260-02-.33(2)(c)."),
                   ("The written gift offer must disclose:", "Specifications, fair market value, time and place of delivery, and any requirements", ["Only the value", "Only the delivery date"], "Rule 1260-02-.33(1)(b).")]},
    ],
    "traps": [
        "Firm name SAME SIZE OR LARGER than the agent's or team's name.",
        "Firm name AND firm phone number on EVERY page of a website.",
        "Franchise name alone is deceptive advertising.",
        "Cash and gift cards are out, except a licensee open house card or a closing gift.",
    ],
    "vocab": [
        ["Firm name", "The firm's licensed name or licensed d/b/a."],
        ["First generation advertising", "What the licensee places, as opposed to syndicated copies."],
        ["Cooperative group", "An advertising group a licensee may belong to."],
        ["Team", "Licensees within one firm who hold themselves out together."],
    ],
    "examples": [
        {"t": "The team sign",
         "s": "A team wants a yard sign reading 'The Smith Group Realty' with the firm name in small print underneath.",
         "w": ["'Realty' is one of the words a team may not use - it suggests independence from the firm.",
               "The FIRM NAME must be in letters the same size or larger than the team's name.",
               "And the sign needs written authorisation from the owner before it goes up."],
         "k": "Teams never outshine the firm, in words or in type size."},
    ],
}

STUDY["tn/agency"] = {
    "summary": "Six items. Tennessee replaced common law fiduciary duty with a STATUTORY list, and the default is that you represent nobody unless you have a written agreement.",
    "sections": [
        {"h": "Limited agency (T.C.A. 62-13-402)",
         "l": ["A licensee engaged as an agent serves as a LIMITED AGENT retained to provide real estate services to a client, and FUNCTIONS AS AN INTERMEDIARY in negotiations unless the parties negotiate directly.",
               "A licensee owes ALL PARTIES the duties in 62-13-403, and owes the CLIENT the additional duties in 62-13-404.",
               "The statutory duties SUPERSEDE ANY FIDUCIARY OR COMMON LAW DUTIES owed by a licensee to a client. That is the sentence that makes Tennessee different from the national material.",
               "A licensee who is NOT an agent for either party is a FACILITATOR, owing only the 62-13-403 duties owed to all parties.",
               "A client or other party is NOT LIABLE for damages for a licensee's acts or omissions where services are provided as agent, subagent or facilitator, except in defined circumstances (62-13-407)."],
         "check": [("A Tennessee licensee acting as an agent is:", "A limited agent who functions as an intermediary in negotiations", ["A universal agent", "A general agent with full fiduciary duty"], "T.C.A. 62-13-402(a)."),
                   ("The statutory duties in 62-13-403 and 62-13-404:", "Supersede any fiduciary or common law duties owed to the client", ["Supplement common law duty", "Apply only to buyers"], "T.C.A. 62-13-402(c)."),
                   ("A Tennessee licensee who represents neither party is:", "A facilitator", ["A dual agent", "A subagent", "A transaction broker"], "T.C.A. 62-13-405; Part 4 generally.")]},
        {"h": "Duties owed to ALL parties (T.C.A. 62-13-403)",
         "p": ["Every licensee providing services in a transaction owes these to EVERY party:"],
         "l": ["DILIGENTLY EXERCISE REASONABLE SKILL AND CARE.",
               "DISCLOSE TO EACH PARTY any ADVERSE FACTS of which the licensee has ACTUAL NOTICE OR KNOWLEDGE.",
               "MAINTAIN CONFIDENTIALITY of information obtained BEFORE disclosure to all parties of a written agency or subagency agreement. It extends to anything the party would REASONABLY EXPECT to be held in confidence, and it SURVIVES both the later establishment of an agency relationship AND THE CLOSING OF THE TRANSACTION.",
               "Provide services with HONESTY AND GOOD FAITH.",
               "Disclose TIMELY AND ACCURATE MARKET CONDITION INFORMATION - but ONLY where it is available through PUBLIC RECORDS and only WHEN REQUESTED by a party.",
               "TIMELY ACCOUNT for trust fund deposits and all other property received.",
               "NOT ENGAGE IN SELF-DEALING, nor act for the licensee's IMMEDIATE FAMILY or an entity in which the licensee has a personal interest, without PRIOR DISCLOSURE and the TIMELY WRITTEN CONSENT OF ALL PARTIES.",
               "NOT RECOMMEND a service provider in which the licensee has an interest or from whom a REFERRAL FEE may be received - other than referrals to other real estate licensees - WITHOUT TIMELY DISCLOSING that interest or the possible fee to the party receiving the referral."],
         "check": [("Tennessee's duty of confidentiality to a party:", "Survives both a later agency relationship and the closing of the transaction", ["Ends at closing", "Ends when an agency agreement is signed"], "T.C.A. 62-13-403(3)."),
                   ("Adverse facts must be disclosed where the licensee has:", "Actual notice or knowledge", ["Any suspicion", "Constructive notice"], "T.C.A. 62-13-403(2)."),
                   ("Market condition information must be given:", "Only where available through public records and only when a party requests it", ["Proactively to every party", "Never"], "T.C.A. 62-13-403(5)."),
                   ("Acting for a member of the licensee's immediate family requires:", "Prior disclosure and the timely written consent of all parties", ["Oral disclosure", "Nothing"], "T.C.A. 62-13-403(7)(A)."),
                   ("Recommending a home warranty company that pays the licensee a referral fee requires:", "Timely disclosure of the interest or the possible fee", ["Nothing, if the company is licensed", "Written consent of all parties"], "T.C.A. 62-13-403(7)(B).")]},
        {"h": "Extra duties owed to a CLIENT (T.C.A. 62-13-404)",
         "l": ["OBEY ALL LAWFUL INSTRUCTIONS of the client within the scope of the agency agreement.",
               "BE LOYAL to the client's interests, placing them before all others - EXCEPT where loyalty would violate the licensee's duties to a CUSTOMER under 62-13-402 or to another client in a DUAL AGENCY.",
               "Unless SPECIFICALLY AND INDIVIDUALLY WAIVED IN WRITING by the client, assist the client by: SCHEDULING ALL PROPERTY SHOWINGS; RECEIVING ALL OFFERS AND COUNTEROFFERS and forwarding them PROMPTLY; ANSWERING QUESTIONS in negotiating a successful purchase agreement within the licensee's expertise; and ADVISING on the forms, procedures and steps needed AFTER EXECUTION for a successful closing.",
               "On waiver of any of those four, the consumer must be ADVISED IN WRITING that they MAY NOT EXPECT OR SEEK ASSISTANCE FROM ANY OTHER LICENSEE in the transaction for the waived duties."],
         "check": [("Which four client services may be waived in Tennessee?", "Scheduling showings, receiving and forwarding offers, answering negotiation questions, and advising on post-execution steps", ["Loyalty and obedience", "Confidentiality and accounting"], "T.C.A. 62-13-404(3)(A)."),
                   ("A waiver must be:", "Specific, individual and in writing by the client", ["Oral with a witness", "Implied by the listing"], "T.C.A. 62-13-404(3)(A)."),
                   ("On waiving a duty, the consumer must be told in writing that:", "They may not expect or seek that assistance from any other licensee in the transaction", ["The fee will be reduced", "TREC must approve"], "T.C.A. 62-13-404(3)(B)."),
                   ("A client's lawful instruction must be obeyed:", "When it is within the scope of the agency agreement", ["Always, without limit", "Only if in writing"], "T.C.A. 62-13-404(1).")]},
        {"h": "Written disclosure (T.C.A. 62-13-405)",
         "l": ["If a licensee PERSONALLY ASSISTS a prospective buyer or seller who is NOT REPRESENTED by any licensee, the licensee must VERBALLY DISCLOSE their FACILITATOR, AGENT, SUBAGENT OR DESIGNATED AGENT STATUS BEFORE ANY REAL ESTATE SERVICES ARE PROVIDED.",
               "That disclosure must be CONFIRMED IN WRITING: with an unrepresented BUYER, BEFORE THE PREPARATION OF AN OFFER TO PURCHASE; with an unrepresented SELLER, BEFORE EXECUTION OF A LISTING AGREEMENT OR PRESENTATION OF AN OFFER, WHICHEVER COMES FIRST.",
               "The licensee must obtain a SIGNED RECEIPT, which must state that complaints alleging a violation of 62-13-312 must be filed within the statute of limitations in 62-13-313(e), and must give the COMMISSION'S ADDRESS AND TELEPHONE NUMBER.",
               "The disclosure of status is NOT a substitute for a WRITTEN AGREEMENT establishing an agency relationship under 62-13-406.",
               "On INITIAL CONTACT with any other licensee in the same prospective transaction, a licensee must IMMEDIATELY DISCLOSE their role, and must IMMEDIATELY NOTIFY other licensees and the parties if that role LATER CHANGES.",
               "Known ADVERSE FACTS must also be disclosed under the residential property disclosure law in title 66 chapter 5 part 2, but licensees are NOT obliged to DISCOVER OR DISCLOSE LATENT DEFECTS or to advise on matters outside the scope of their licence.",
               "The disclosure duties in 62-13-403, 62-13-404 and 62-13-405 do NOT apply to COMMERCIAL property, transfers by PUBLIC AUCTION, residential property of MORE THAN FOUR UNITS, or the LEASE OR RENTAL of residential property."],
         "check": [("Agency status must be confirmed in writing with an unrepresented buyer:", "Before the preparation of an offer to purchase", ["At closing", "Within 3 days of the offer"], "T.C.A. 62-13-405(b)."),
                   ("With an unrepresented seller, the written confirmation comes:", "Before execution of a listing agreement or presentation of an offer, whichever comes first", ["Only at listing", "Only at the offer"], "T.C.A. 62-13-405(b)."),
                   ("The signed receipt must include:", "The complaint time limit and the Commission's address and telephone number", ["The commission rate", "The licensee's licence number only"], "T.C.A. 62-13-405(b)."),
                   ("Are licensees obliged to discover latent defects?", "No; the duty is to disclose known adverse facts", ["Yes, by inspection", "Yes, by hiring an inspector"], "T.C.A. 62-13-405(a)."),
                   ("The 403 to 405 disclosure duties do NOT apply to:", "Commercial property, public auctions, residential property of more than four units, and residential leases", ["Vacant land", "New construction"], "T.C.A. 62-13-405(e)."),
                   ("On first contact with another licensee in the deal, a licensee must:", "Immediately disclose their role, including any agency relationship", ["Wait until an offer is made", "Say nothing"], "T.C.A. 62-13-405(d).")]},
        {"h": "Designated agency (T.C.A. 62-13-406)",
         "l": ["A licensee with a WRITTEN AGREEMENT to represent a party may be APPOINTED AS THE DESIGNATED AND INDIVIDUAL AGENT of that party by the MANAGING BROKER, to the EXCLUSION of all other licensees of that broker.",
               "A managing broker IS NOT A DUAL AGENT where the appointed designated agent - by specific appointment OR BY WRITTEN COMPANY POLICY - does not represent any other party to the same transaction.",
               "Designated agency does NOT abolish or diminish the managing broker's CONTRACTUAL RIGHTS to a listing or advertising agreement, nor LESSEN the broker's responsibility to ensure all affiliated licensees follow the law.",
               "There is NO IMPUTATION OF KNOWLEDGE OR INFORMATION among or between clients, the managing broker and any designated agent in a designated agency situation.",
               "Licensees who hold themselves out as a TEAM may NOT designate members as DESIGNATED FIRM AGENTS - that remains the PRINCIPAL BROKER'S responsibility (Rule 1260-02-.41(5))."],
         "check": [("In Tennessee designated agency, the managing broker:", "Is not a dual agent where the designated agent represents only one party", ["Automatically becomes a dual agent", "Must withdraw"], "T.C.A. 62-13-406(a)."),
                   ("Knowledge in a designated agency situation is:", "Not imputed among clients, the managing broker and the designated agents", ["Imputed to the whole firm", "Imputed to the managing broker only"], "T.C.A. 62-13-406(c)."),
                   ("A designated agent may be appointed:", "By specific appointment or by written company policy", ["Only by specific appointment", "Only by TREC"], "T.C.A. 62-13-406(a)."),
                   ("A team may designate its own members as designated firm agents:", "No; that is the principal broker's responsibility", ["Yes, with the firm's consent", "Yes, in writing"], "Rule 1260-02-.41(5).")]},
        {"h": "Exclusive buyer representation (Rule 1260-02-.36)",
         "p": ["When entering an EXCLUSIVE BUYER REPRESENTATION AGREEMENT a licensee must ADVISE AND CONFIRM IN WRITING that the buyer should arrange ALL VIEWINGS AND INSPECTIONS THROUGH THE LICENSEE and NOT CONTACT OTHER LICENSEES DIRECTLY; that the buyer should IMMEDIATELY TELL ANY OTHER LICENSEE they meet - for example at an open house - that they are represented; and WHETHER THE BUYER WILL OWE A COMMISSION if they buy without the licensee's assistance, through another licensee or directly from an owner."],
         "check": [("An exclusive buyer representation agreement must confirm in writing that the buyer:", "Should arrange all viewings through the licensee and tell other licensees they are represented", ["May use any agent they wish", "Owes nothing in any event"], "Rule 1260-02-.36."),
                   ("It must also state:", "Whether the buyer will owe a commission if they buy without the licensee's assistance", ["The listing commission", "The lender's fee"], "Rule 1260-02-.36(3).")]},
    ],
    "traps": [
        "Statutory duties SUPERSEDE common law fiduciary duty in Tennessee.",
        "Confidentiality survives closing - and starts before any agency agreement.",
        "Market condition information only from PUBLIC RECORDS and only ON REQUEST.",
        "Four client services are waivable in writing; loyalty and obedience are not.",
        "Designated agency does not make the managing broker a dual agent.",
    ],
    "vocab": [
        ["Limited agent", "What a Tennessee agent is called by statute."],
        ["Facilitator", "A licensee representing neither party."],
        ["Adverse fact", "A known fact that must be disclosed to every party."],
        ["Designated agent", "An individual appointed by the managing broker for one party."],
        ["Affiliate broker", "Tennessee's name for a salesperson-level licensee."],
    ],
    "examples": [
        {"t": "The unrepresented seller",
         "s": "You represent a buyer. A for-sale-by-owner lets you bring your buyer through.",
         "w": ["Before providing any services you must VERBALLY disclose that you are the buyer's agent.",
               "Because the seller is unrepresented, that must be CONFIRMED IN WRITING before you present an offer.",
               "You take a SIGNED RECEIPT carrying the complaint time limit and TREC's address and telephone number."],
         "k": "Verbal first, written before the offer, and get the signed receipt."},
    ],
}

STUDY["tn/broker-affiliate"] = {
    "summary": "Five items on who pays whom and who answers for what. One rule carries most of it: an affiliate broker is paid by, and supervised by, the principal broker.",
    "sections": [
        {"h": "Supervision and offices (Rules 1260-02-.01, .03, .05)",
         "l": ["NO LICENSEE may engage in real estate activity in any office unless there is a PRINCIPAL BROKER DEVOTED TO THE FULL TIME MANAGEMENT of that office.",
               "A licensee may be engaged only by a principal broker who is ENGAGED PRIMARILY IN THE REAL ESTATE BUSINESS and ACCESSIBLE DURING NORMAL DAYTIME WORKING HOURS.",
               "USE OF A POST OFFICE BOX AS A BUSINESS LOCATION IS PROHIBITED (Rule 1260-02-.05).",
               "The PRINCIPAL BROKER REMAINS ULTIMATELY RESPONSIBLE for oversight of all licensees in the firm and may NOT DELEGATE supervisory responsibilities to a team (Rule 1260-02-.41(3)).",
               "The Commission must be NOTIFIED WITHIN TEN DAYS of the DEATH, RESIGNATION, TERMINATION OR INCAPACITY of a principal broker (Rule 1260-02-.38)."],
         "check": [("A Tennessee office must have:", "A principal broker devoted to its full time management", ["A broker on call", "Any licensed affiliate in charge"], "Rule 1260-02-.01(1)."),
                   ("Using a post office box as a business location is:", "Prohibited", ["Allowed for rural offices", "Allowed with TREC approval"], "Rule 1260-02-.05."),
                   ("A principal broker may delegate supervisory responsibility to a team:", "No; the principal broker remains ultimately responsible", ["Yes, in writing", "Yes, for team members only"], "Rule 1260-02-.41(3)."),
                   ("The Commission must be told of a principal broker's death or incapacity within:", "Ten days", ["Thirty days", "Immediately, by telephone only"], "Rule 1260-02-.38(1).")]},
        {"h": "Compensation",
         "l": ["Licensees who hold themselves out as a TEAM, GROUP OR SIMILAR ENTITY within a firm SHALL NOT RECEIVE COMPENSATION FROM ANYONE OTHER THAN THEIR PRINCIPAL BROKER for acts requiring a licence (Rule 1260-02-.41(2)).",
               "Such licensees must be AFFILIATED WITH THE SAME LICENSED FIRM and may NOT ESTABLISH A SEPARATE PHYSICAL LOCATION from the firm's location of record, and may NOT represent themselves as a SEPARATE ENTITY from the firm (Rule 1260-02-.41(1), (4)).",
               "A Tennessee broker may pay a commission to a BROKER LICENSED IN ANOTHER STATE provided that non-resident broker DOES NOT CONDUCT ANY NEGOTIATION IN TENNESSEE - an out-of-state licensee cannot 'partner' with a Tennessee licensee to do work that requires a Tennessee licence.",
               "An AFFILIATED BROKER must PAY OVER TO THE PRINCIPAL BROKER all trust money IMMEDIATELY UPON RECEIPT (Rule 1260-02-.09(3)).",
               "Rule 1260-02-.39 governs COMMISSIONS EARNED BY AFFILIATED LICENSEES."],
         "check": [("A Tennessee team member may be paid by:", "Their principal broker only", ["The seller directly", "The team leader", "Any licensed broker"], "Rule 1260-02-.41(2)."),
                   ("A team may maintain a separate office from the firm's location of record:", "No", ["Yes, within the same county", "Yes, with TREC approval"], "Rule 1260-02-.41(1)."),
                   ("A Tennessee broker may pay a commission to an out-of-state broker:", "Provided that broker conducts no negotiation in Tennessee", ["Never", "Only through an escrow agent"], "TREC guidance on T.C.A. title 62 chapter 13."),
                   ("An affiliate broker who receives earnest money must:", "Pay it over to the principal broker immediately upon receipt", ["Deposit it personally within 3 days", "Hold it until closing"], "Rule 1260-02-.09(3).")]},
        {"h": "Change of affiliation (Rule 1260-02-.02)",
         "l": ["To terminate affiliation, the licensee or principal broker submits a completed TRANSFER, RELEASE AND CHANGE OF STATUS FORM (TREC FORM 1) or the required information ONLINE.",
               "The principal broker's supervisory responsibility for the licensee's FUTURE ACTS TERMINATES UPON THE COMMISSION'S RECEIPT of the release form or online submission - not when the licensee walks out.",
               "The principal broker must RETAIN A COPY of the executed form or confirmation of online submission.",
               "WITHIN TEN DAYS after the date of release the licensee must complete the administrative steps for either CHANGE OF AFFILIATION OR RETIREMENT, and the licensee SHALL NOT ENGAGE IN ANY LICENSED ACTIVITY until the change of affiliation is RECEIVED AND PROCESSED by the Commission.",
               "Failure to comply MAY RESULT IN DISCIPLINARY ACTION."],
         "check": [("A Tennessee principal broker's responsibility for a departing licensee's future acts ends:", "When the Commission receives the release form or online submission", ["When the licensee resigns", "At the end of the month"], "Rule 1260-02-.02(1)."),
                   ("After release, the licensee must complete the change of affiliation or retirement within:", "Ten days", ["Thirty days", "Sixty days"], "Rule 1260-02-.02(2)."),
                   ("Between release and processing, the licensee may:", "Not engage in any activity requiring a licence", ["Continue working for the old firm", "Work under the new firm immediately"], "Rule 1260-02-.02(2).")]},
    ],
    "traps": [
        "Paid only by the principal broker - teams included.",
        "Supervision ends on the COMMISSION'S RECEIPT of the release, not on resignation.",
        "No post office box as a business location.",
    ],
    "vocab": [
        ["Principal broker", "The broker who manages an office full time and supervises its licensees."],
        ["Affiliate broker", "A licensee engaged by a principal broker."],
        ["TREC Form 1", "The Transfer, Release and Change of Status form."],
        ["Team", "Licensees of one firm holding themselves out together."],
    ],
    "examples": [],
}

STUDY["tn/commission"] = {
    "summary": "Four items on the regulator. Know what TREC covers, and the things it expressly does not.",
    "sections": [
        {"h": "Purpose and jurisdiction",
         "l": ["The TENNESSEE REAL ESTATE COMMISSION administers the TENNESSEE REAL ESTATE BROKER LICENSE ACT OF 1973 and its RULES, together with the TENNESSEE TIMESHARE ACT OF 1987. Its purpose is PUBLIC PROTECTION, not resolving private disputes.",
               "The outline flags PERSONS AND DISPUTES NOT WITHIN COMMISSION JURISDICTION: TREC does NOT decide COMMISSION DISPUTES BETWEEN LICENSEES, does NOT award DAMAGES to consumers, and has NO AUTHORITY over people who are NOT LICENSEES except for UNLICENSED ACTIVITY.",
               "The Commission issues rules under T.C.A. 62-13-203, investigates COMPLAINTS, holds HEARINGS, and imposes DISCIPLINARY ACTION including CIVIL PENALTIES (Rule 1260-02-.32).",
               "Successful completion of the examination DOES NOT GUARANTEE the issuance of a licence - TREC reviews the applicant's qualifications."],
         "check": [("Which is OUTSIDE TREC's jurisdiction?", "A commission dispute between two licensees", ["Unlicensed activity", "A licensee's advertising", "Escrow handling"], "PSI Tennessee state outline; TREC's statutory purpose."),
                   ("Passing the examination:", "Does not guarantee a licence will be issued", ["Entitles the candidate to a licence", "Replaces the application"], "PSI Tennessee bulletin."),
                   ("TREC's sanctions include:", "Civil penalties, as well as suspension and revocation", ["Awarding damages to consumers", "Ordering a sale to complete"], "Rule 1260-02-.32.")]},
        {"h": "Complaints and discipline",
         "l": ["A complaint alleging a violation of T.C.A. 62-13-312 - the grounds for discipline - must be FILED WITHIN THE APPLICABLE STATUTE OF LIMITATIONS set out in 62-13-313(e). That is why the agency disclosure receipt must tell consumers about it.",
               "The signed receipt for the agency disclosure must also carry the COMMISSION'S ADDRESS AND TELEPHONE NUMBER, so a consumer knows where to complain (62-13-405(b)).",
               "Rule 1260-01-.01(4) bars examination or licensure until TWO YEARS have passed from the expiry of probation or parole, from conviction, or from release from incarceration, WHICHEVER IS LATER - applying to ALL FELONIES and to MISDEMEANOURS INVOLVING THEFT of money, services or property.",
               "Records of a licensee are OPEN TO THE COMMISSION, and the outline names COMMISSION ACCESS TO RECORDS as its own topic."],
         "check": [("The agency disclosure receipt must tell the consumer:", "The complaint time limit and TREC's address and telephone number", ["The commission split", "The firm's licence number"], "T.C.A. 62-13-405(b)."),
                   ("After a conviction for a theft misdemeanour, a person may not be licensed until:", "Two years have passed from conviction, release or the end of probation or parole, whichever is later", ["One year has passed", "The conviction is expunged"], "Rule 1260-01-.01(4)."),
                   ("The two-year bar applies to:", "All felonies and misdemeanours involving theft of money, services or property", ["Any criminal offence", "Felonies only"], "Rule 1260-01-.01(4).")]},
    ],
    "traps": [
        "TREC protects the public; it does not referee commission splits or award damages.",
        "Two years from the LATER of conviction, release, or the end of probation or parole.",
    ],
    "vocab": [
        ["TREC", "The Tennessee Real Estate Commission."],
        ["Civil penalty", "A monetary sanction TREC may impose."],
        ["62-13-312", "The statutory grounds for discipline."],
    ],
    "examples": [],
}

STUDY["tn/licensing"] = {
    "summary": "Four items. The numbers: 18 years old, 90 hours in two parts, 16 hours of continuing education with a 6-hour TREC Core, and errors and omissions insurance.",
    "sections": [
        {"h": "Becoming an affiliate broker",
         "l": ["An applicant must be AT LEAST 18 YEARS OF AGE.",
               "An affiliate broker must complete A TOTAL OF 90 HOURS of real estate education. SIXTY HOURS must cover REAL ESTATE PRINCIPLES / FUNDAMENTALS and must be done to QUALIFY TO TAKE THE EXAMINATION. The remaining 30-HOUR 'COURSE FOR NEW AFFILIATES' must be completed BEFORE A LICENCE WILL BE ISSUED (T.C.A. 62-13-303(b)(2); Rule 1260-05-.03).",
               "After passing ALL portions, the candidate must APPLY FOR THE LICENCE WITHIN ONE YEAR of passing.",
               "A pass on ONE SECTION is valid for TWO RETAKES of the failed section OR ONE YEAR, whichever comes first.",
               "BROKER candidates need experience: licensed as an affiliate broker AFTER 12 May 1988, an ACTIVE licence for at least 36 MONTHS, or a BACCALAUREATE DEGREE WITH A MAJOR IN REAL ESTATE for at least 24 MONTHS."],
         "check": [("Tennessee affiliate broker education totals:", "90 hours - 60 before the examination and a 30-hour Course for New Affiliates before licensure", ["60 hours in total", "90 hours all before the exam"], "T.C.A. 62-13-303(b)(2); Rule 1260-05-.03."),
                   ("Which 60 hours must be done before sitting the examination?", "Real estate principles and fundamentals", ["The Course for New Affiliates", "Contracts and closings"], "PSI Tennessee bulletin."),
                   ("After passing both portions, a candidate must apply within:", "One year", ["Six months", "Two years"], "PSI Tennessee bulletin."),
                   ("A pass on one section stays valid for:", "Two retakes of the failed section or one year, whichever comes first", ["Indefinitely", "Three attempts"], "TREC PSI exam information."),
                   ("A broker candidate licensed after 12 May 1988 needs:", "An active licence for at least 36 months, or a real estate degree plus 24 months", ["12 months of licensure", "No experience"], "PSI Tennessee bulletin.")]},
        {"h": "Keeping the licence",
         "l": ["CONTINUING EDUCATION: a licensee must complete 16 HOURS, of which SIX HOURS is the mandatory TREC CORE COURSE and TEN HOURS is approved ELECTIVE education (TREC Instructor Training Manual; Rule 1260-05). OUT-OF-STATE licensees must also complete the 16 hours for renewal.",
               "The TREC CORE course covers, among other topics, LICENSING AND PENALTY FEES, AGENCY, ADVERTISING (Rule 1260-02-.12; T.C.A. 62-13-310; Rule 1260-02-.33), CONTRACTS, PROPERTY MANAGEMENT, the DISCLOSURE FORM (T.C.A. 66-5-210) and PRINCIPAL BROKER SUPERVISION.",
               "ERRORS AND OMISSIONS INSURANCE is required of licensees, and PRINCIPAL BROKERS must AT ALL TIMES ENSURE THEIR AFFILIATED LICENSEES HOLD E&O INSURANCE as required by law - the outline lists it under licensing requirements.",
               "The outline also covers CHANGE OF STATUS, NAME OR ADDRESS, FIRM LICENCES AND LICENCE DISPLAY, and RENEWAL OF LICENCE."],
         "check": [("Tennessee continuing education is:", "16 hours, including the 6-hour mandatory TREC Core course", ["12 hours", "24 hours", "8 hours"], "TREC Instructor Training Manual; Rule 1260-05."),
                   ("How many of the 16 hours are elective?", "Ten", ["Six", "Sixteen", "None"], "TREC Instructor Training Manual."),
                   ("Out-of-state Tennessee licensees:", "Must also complete 16 hours of continuing education for renewal", ["Are exempt", "Need only the Core course"], "TREC Core course topics page."),
                   ("Errors and omissions insurance in Tennessee is:", "Required, and the principal broker must ensure affiliates carry it at all times", ["Optional", "Required only of principal brokers"], "PSI Tennessee state outline; TREC newsletter.")]},
    ],
    "traps": [
        "90 hours split 60 before the exam and 30 before the licence.",
        "16 CE hours = 6 TREC Core + 10 elective.",
        "Apply within ONE YEAR of passing, and a single-section pass lapses after two retakes or a year.",
    ],
    "vocab": [
        ["Course for New Affiliates", "The 30-hour course required before a licence issues."],
        ["TREC Core", "The mandatory 6-hour continuing education course."],
        ["E&O insurance", "Errors and omissions cover required of licensees."],
        ["CORE system", "Tennessee's online licensing portal at core.tn.gov."],
    ],
    "examples": [],
}

STUDY["tn/records"] = {
    "summary": "Four items. Three years is the number, and the principal broker is the keeper.",
    "sections": [
        {"h": "Retention (Rule 1260-02-.40)",
         "l": ["Under T.C.A. 62-13-312(b)(6), licensees must PRESERVE RECORDS relating to any real estate transaction FOR THREE YEARS FOLLOWING THE CONSUMMATION of the transaction.",
               "Records may be kept ELECTRONICALLY, but all documents required to be retained must be READILY ACCESSIBLE IN AN ORGANISED manner, on a backup schedule that SAFEGUARDS THE SECURITY, AUTHENTICITY AND ACCURACY of the records, with hardware that keeps them accessible IN A READABLE FORMAT.",
               "The outline also names RESPONSIBILITY FOR KEEPING RECORDS, WHAT INFORMATION AND DOCUMENTS MUST BE KEPT, and COMMISSION ACCESS TO RECORDS.",
               "A principal broker must also RETAIN A COPY of each executed Transfer, Release and Change of Status form or online confirmation (Rule 1260-02-.02(1))."],
         "check": [("Tennessee transaction records must be kept for:", "Three years following consummation of the transaction", ["One year", "Five years", "Seven years"], "T.C.A. 62-13-312(b)(6); Rule 1260-02-.40(1)."),
                   ("Electronic records are:", "Permitted, if readily accessible, organised, backed up and readable", ["Prohibited", "Permitted only with TREC approval"], "Rule 1260-02-.40."),
                   ("Who must retain the executed release form when a licensee transfers?", "The principal broker", ["The licensee", "TREC"], "Rule 1260-02-.02(1).")]},
        {"h": "Handling offers and copies (Rules 1260-02-.08, .10)",
         "l": ["A broker or affiliate broker shall PROMPTLY TENDER EVERY WRITTEN OFFER to purchase or sell obtained on a property UNTIL A CONTRACT IS SIGNED BY ALL PARTIES.",
               "On a proper acceptance of an offer or any counteroffer, the licensee shall PROMPTLY DELIVER TRUE EXECUTED COPIES, SIGNED BY THE SELLER, TO BOTH THE PURCHASER AND THE SELLER.",
               "Licensees must MAKE CERTAIN THAT ALL TERMS AND CONDITIONS of the transaction are INCLUDED IN THE CONTRACT to purchase.",
               "If an offer is REJECTED, the licensee shall REQUEST THE SELLER TO NOTE THE REJECTION ON THE OFFER and return it to the offeror or the offeror's agent.",
               "CLOSING STATEMENTS: if a broker acts as CLOSING AGENT, the broker shall PROVIDE COPIES of the closing statement to the parties (Rule 1260-02-.10).",
               "A licensee preparing an OFFER TO BUY must provide in the offer, and make the buyer aware, that a SEPTIC SYSTEM INSPECTION LETTER is available for a fee from the Tennessee Department of Environment and Conservation, Division of Ground Water Protection (Rule 1260-02-.37)."],
         "check": [("Written offers must be tendered:", "Promptly, until a contract is signed by all parties", ["Only until the first offer is accepted", "At the seller's convenience"], "Rule 1260-02-.08."),
                   ("On acceptance, copies signed by the seller go to:", "Both the purchaser and the seller, promptly", ["The purchaser only", "The closing agent only"], "Rule 1260-02-.08."),
                   ("When an offer is rejected, the licensee must:", "Ask the seller to note the rejection on the offer and return it to the offeror or their agent", ["Destroy the offer", "File it without comment"], "Rule 1260-02-.08."),
                   ("A licensee preparing an offer to buy must tell the buyer about:", "The septic system inspection letter available from TDEC for a fee", ["A free radon test", "A state home warranty"], "Rule 1260-02-.37.")]},
    ],
    "traps": [
        "Three years from CONSUMMATION, not from the listing.",
        "Offers keep being tendered until all parties sign - not until the first acceptance.",
        "The septic inspection letter notice goes in the offer itself.",
    ],
    "vocab": [
        ["Consummation", "The event that starts the three-year retention clock."],
        ["Tender", "To present an offer to the party entitled to see it."],
        ["TDEC", "Tennessee Department of Environment and Conservation."],
    ],
    "examples": [],
}

STUDY["tn/escrow"] = {
    "summary": "Four items. Tennessee ties the deposit to ACCEPTANCE, gives seven lawful ways out of the account, and puts a 21-day clock on a disbursement request.",
    "sections": [
        {"h": "The account (Rule 1260-02-.09(1) to (6))",
         "l": ["COMMINGLING is defined as a licensee MAINTAINING FUNDS BELONGING TO OTHERS IN THE SAME BANK ACCOUNT that contains the licensee's personal or business funds. It is EXPRESSLY PROHIBITED (subsection (13)).",
               "TRUST MONEY is money belonging to others received by a licensee acting as AGENT OR FACILITATOR, or any money held by a licensee acting as TEMPORARY CUSTODIAN of others' funds.",
               "Each PRINCIPAL BROKER shall maintain a SEPARATE ESCROW OR TRUSTEE ACCOUNT for trust money received in a fiduciary capacity.",
               "An AFFILIATED BROKER shall PAY OVER TO THE PRINCIPAL BROKER all trust money IMMEDIATELY UPON RECEIPT.",
               "Principal brokers are RESPONSIBLE AT ALL TIMES for trust money accepted by them or their affiliated brokers, in accordance with the terms of the contract.",
               "Where a contract authorises the principal broker to hold trust money, the broker must SPECIFY IN THE CONTRACT the TERMS AND CONDITIONS FOR DISBURSEMENT and the NAME AND ADDRESS OF THE PERSON OR FIRM who will actually hold it.",
               "Where the contract authorises SOMEONE ELSE to hold the money, the principal broker is RELIEVED OF RESPONSIBILITY once that escrow agent RECEIVES the funds.",
               "All trust money relating to the LEASE of property must be held in ONE OR MORE SEPARATE escrow or trustee accounts (subsection (12))."],
         "check": [("Commingling in Tennessee means:", "Keeping funds belonging to others in the same account as the licensee's own personal or business funds", ["Mixing two clients' deposits", "Holding funds too long"], "Rule 1260-02-.09(1)(a)."),
                   ("An affiliate broker who receives trust money must:", "Pay it over to the principal broker immediately upon receipt", ["Deposit it within 3 banking days", "Hold it until acceptance"], "Rule 1260-02-.09(3)."),
                   ("Where the contract names another escrow agent, the principal broker:", "Is relieved of responsibility once that agent receives the funds", ["Remains liable regardless", "Must still open an account"], "Rule 1260-02-.09(6)."),
                   ("Trust money relating to leases must be held:", "In one or more separate escrow or trustee accounts", ["In the sales escrow account", "By the property owner"], "Rule 1260-02-.09(12).")]},
        {"h": "Deposit and disbursement (Rule 1260-02-.09(7) to (11))",
         "l": ["TRUST MONEY SHALL BE DEPOSITED PROMPTLY UPON ACCEPTANCE OF THE OFFER, unless the offer contains a statement such as 'Trust money to be deposited by:'.",
               "NO POSTDATED CHECK may be accepted for payment of trust money UNLESS OTHERWISE PROVIDED IN THE OFFER.",
               "A principal broker may PROPERLY DISBURSE trust money in SEVEN ways: on a REASONABLE INTERPRETATION OF THE CONTRACT; on a SEPARATE WRITTEN AGREEMENT SIGNED BY ALL PARTIES having an interest; AT THE CLOSING; on the REJECTION of an offer; on the WITHDRAWAL of an offer not yet accepted; on FILING AN INTERPLEADER ACTION; or on the ORDER OF A COURT.",
               "Trust money shall be disbursed IN A PROPER MANNER WITHOUT UNREASONABLE DELAY.",
               "Absent a COMPELLING REASON, earnest money shall be DISBURSED, INTERPLEADED, OR TURNED OVER TO AN ATTORNEY with instructions to interplead WITHIN 21 CALENDAR DAYS from the date of receipt of a WRITTEN REQUEST FOR DISBURSEMENT.",
               "INTEREST-BEARING escrow accounts are NEITHER REQUIRED NOR PROHIBITED by the Commission; if used, the licensee must DISCLOSE TO THE PAYOR AT THE TIME OF CONTRACT EXECUTION, among the other conditions the rule sets."],
         "check": [("Tennessee trust money must be deposited:", "Promptly upon acceptance of the offer, unless the offer says who will deposit it and when", ["Within 3 banking days of receipt", "At closing"], "Rule 1260-02-.09(11)."),
                   ("On a written request for disbursement, earnest money must be disbursed, interpleaded or turned over to an attorney within:", "21 calendar days, absent a compelling reason", ["10 business days", "30 days", "60 days"], "Rule 1260-02-.09(9)."),
                   ("Which is NOT a permitted disbursement?", "On the oral agreement of the buyer and seller", ["At closing", "On filing an interpleader action", "On a court order"], "Rule 1260-02-.09(7) requires a signed separate written agreement."),
                   ("A postdated cheque for trust money:", "May not be accepted unless the offer provides otherwise", ["Is always acceptable", "Is acceptable up to 30 days"], "Rule 1260-02-.09(10)."),
                   ("Interest-bearing escrow accounts in Tennessee are:", "Neither required nor prohibited, but conditions apply if used", ["Required", "Prohibited"], "Rule 1260-02-.09(14).")]},
    ],
    "traps": [
        "Deposit on ACCEPTANCE, not on receipt - unless the offer says otherwise.",
        "21 CALENDAR days from a written request for disbursement.",
        "Separate accounts for lease money.",
    ],
    "vocab": [
        ["Trust money", "Money belonging to others held by a licensee."],
        ["Commingling", "Mixing trust money with the licensee's own funds."],
        ["Interpleader", "A court action to let a judge decide who gets the deposit."],
        ["Temporary custodian", "A licensee holding others' funds without agency."],
    ],
    "examples": [
        {"t": "The deal falls apart",
         "s": "A buyer sends a written request for the earnest money back after a failed inspection, and the seller objects.",
         "w": ["You cannot simply pay it over on one party's word - a disbursement on agreement needs a SEPARATE WRITING SIGNED BY ALL PARTIES.",
               "Absent a compelling reason you have 21 CALENDAR DAYS from the written request to disburse, interplead, or hand the funds to an attorney to interplead.",
               "A court order is the other clean route out."],
         "k": "Signed by everyone, a court order, or interplead - within 21 days."},
    ],
}

STUDY["tn/improper"] = {
    "summary": "Three items. Net listings, discrimination, and the self-dealing rule that catches brokers buying for themselves.",
    "sections": [
        {"h": "Net listings and personal interest",
         "l": ["NO broker or affiliate broker shall ACCEPT OR ENTER A LISTING BASED ON A 'NET PRICE' - that is, a price EXCLUDING the customary commission and expenses associated with the sale (Rule 1260-02-.07). Net listings are simply prohibited.",
               "PERSONAL INTEREST: no licensee may, directly or through a third party, PURCHASE FOR HIMSELF or acquire any interest in or OPTION TO PURCHASE property listed with him or his company, or property the owner has approached him to broker, WITHOUT FIRST MAKING A FULL DISCLOSURE OF HIS TRUE POSITION to the owner or to any prospective purchaser he has acted for.",
               "After acquiring such an interest, the licensee must MAKE A FULL DISCLOSURE OF HIS TRUE POSITION to prospective purchasers who tender offers.",
               "ALL LICENSEES SHALL IDENTIFY THEMSELVES AS A LICENSEE when buying or selling property FOR THEMSELVES (Rule 1260-02-.11(2)).",
               "The statutory duty to all parties forbids SELF-DEALING, or acting for IMMEDIATE FAMILY or an entity in which the licensee has an interest, without prior disclosure and the TIMELY WRITTEN CONSENT OF ALL PARTIES (T.C.A. 62-13-403(7)(A))."],
         "check": [("A net listing in Tennessee is:", "Prohibited", ["Allowed with written consent", "Allowed for commercial property"], "Rule 1260-02-.07."),
                   ("A licensee buying or selling property for themselves must:", "Identify themselves as a licensee", ["Use a corporate nominee", "Notify TREC in advance"], "Rule 1260-02-.11(2)."),
                   ("Taking an option on a property the owner approached you to broker requires:", "Full prior disclosure of your true position", ["Nothing, as the listing was never signed", "TREC approval"], "Rule 1260-02-.11(1)."),
                   ("Acting for a company in which the licensee has an interest requires:", "Prior disclosure and the timely written consent of all parties", ["Oral notice", "Nothing"], "T.C.A. 62-13-403(7)(A).")]},
        {"h": "Discrimination and other misconduct",
         "l": ["The outline lists DISCRIMINATION under 'Other Improper Activities and Consumer Protection'. Federal fair housing applies, and the TREC CORE course covers fair housing within its law and ethics content.",
               "Known ADVERSE FACTS must be disclosed under the residential property disclosure law in T.C.A. title 66 chapter 5 part 2, and the TREC Core topics name the DISCLOSURE FORM at T.C.A. 66-5-210.",
               "IMPROPER LISTING AGREEMENTS are a named topic, of which the NET LISTING is the headline example.",
               "The advertising rule's ban on FALSE, MISLEADING OR DECEPTIVE advertising and the gifts rule's ban on CASH INCENTIVES both sit under consumer protection."],
         "check": [("Tennessee's residential property disclosure law sits in:", "T.C.A. title 66, chapter 5, part 2", ["T.C.A. title 62, chapter 13", "The TREC rules"], "T.C.A. 62-13-405(a); TREC Core topics."),
                   ("The clearest example of an improper listing agreement is:", "A net listing", ["An exclusive right to sell", "An open listing"], "Rule 1260-02-.07.")]},
    ],
    "traps": [
        "Net listings are banned outright, not merely discouraged.",
        "You must say you are a licensee whenever you buy or sell for yourself.",
    ],
    "vocab": [
        ["Net listing", "A listing priced net of commission and expenses. Prohibited."],
        ["Personal interest", "The rule requiring disclosure of a licensee's own stake."],
        ["Self-dealing", "Acting for one's own benefit without disclosure and consent."],
    ],
    "examples": [],
}

STUDY["tn/special"] = {
    "summary": "Three items on where the ordinary rules bend: timeshares, property management and commercial deals.",
    "sections": [
        {"h": "What changes",
         "l": ["COMMERCIAL property, transfers by PUBLIC AUCTION, residential property of MORE THAN FOUR UNITS, and the LEASE OR RENTAL of residential property are NOT subject to the disclosure duties of T.C.A. 62-13-403, 62-13-404 and 62-13-405.",
               "TIMESHARE is governed by the TENNESSEE TIMESHARE ACT OF 1987, which TREC also administers. It carries its own licence categories - TIMESHARE SALESPERSON and ACQUISITION AGENT - each with a 35-item state examination requiring 25 correct (70%).",
               "The timeshare state outline names PUBLIC OFFERING STATEMENTS, ESCROW OF DEPOSITS, MUTUAL RIGHTS OF CANCELLATION, the ban on MISLEADING ADVERTISEMENTS, specific ADVERTISING PROHIBITIONS, and PRIZE OR GIFT PROMOTIONAL OFFERS.",
               "PROPERTY MANAGEMENT: money relating to leases goes in SEPARATE escrow or trustee accounts (Rule 1260-02-.09(12)), and the TREC Core course covers property management as a listed topic.",
               "Rule 1260-02-.15 and others concerning specialised practice have been REPEALED, so the modern rules are the general ones applied to these contexts."],
         "check": [("Which transactions escape the 403 to 405 disclosure duties?", "Commercial property, public auctions, residential property of more than four units, and residential leases", ["New construction", "Vacant land", "Cash sales"], "T.C.A. 62-13-405(e)."),
                   ("The Tennessee Timeshare Act dates from:", "1987", ["1973", "1995", "2006"], "PSI Tennessee bulletin."),
                   ("A timeshare salesperson's state examination is:", "35 items, with 25 correct to pass", ["40 items, 28 correct", "80 items, 56 correct"], "PSI Tennessee bulletin score table."),
                   ("Lease-related trust money must be held:", "In one or more separate escrow or trustee accounts", ["In the firm's sales escrow account", "By the landlord"], "Rule 1260-02-.09(12).")]},
    ],
    "traps": [
        "Residential of MORE than four units is outside the disclosure duties; one to four is inside.",
        "Timeshare has its own act, its own licences and its own 35-item examination.",
    ],
    "vocab": [
        ["Timeshare Act", "The Tennessee Timeshare Act of 1987."],
        ["Acquisition agent", "A timeshare licence category with its own state exam."],
        ["Public offering statement", "The timeshare disclosure document."],
    ],
    "examples": [],
}


# ------------------------------------------------------------- questions

Q = [
 # advertising
 ("tn/advertising", "Scope", 1, "Which is NOT advertising under the Tennessee rule?",
  "A branded notepad or t-shirt", ["A website", "An e-mail signature", "A yard sign"],
  "Rule 1260-02-.12(1) excludes promotional items and event sponsorship."),
 ("tn/advertising", "Scope", 2, "'Firm name' in the Tennessee advertising rule means:",
  "The firm's entire name as licensed, or its licensed d/b/a name", ["The franchise name", "The principal broker's name"],
  "Rule 1260-02-.12(2)."),
 ("tn/advertising", "Principles", 1, "In Tennessee advertising, the firm name must appear:",
  "In letters the same size or larger than the licensee's or team's name", ["Anywhere on the advertisement", "In smaller type than the agent's name"],
  "Rule 1260-02-.12(3)(b)."),
 ("tn/advertising", "Principles", 1, "All Tennessee advertising must list:",
  "The firm name and the firm telephone number as on file with the Commission", ["The licensee's mobile number", "The MLS number"],
  "Rule 1260-02-.12(3)(b)."),
 ("tn/advertising", "Signs", 1, "Posting a 'For Sale' sign in Tennessee requires:",
  "Written authorisation from the owner or the owner's agent", ["A verbal go-ahead", "Nothing, if the property is listed"],
  "Rule 1260-02-.12(3)(d)."),
 ("tn/advertising", "Franchise", 2, "Advertising that shows only the franchise name is:",
  "False, misleading or deceptive advertising", ["Permitted for franchisees", "Permitted online only"],
  "Rule 1260-02-.12(3)(f)(1)."),
 ("tn/advertising", "Teams", 2, "A Tennessee team name may NOT include:",
  "Words such as Realty, Company, LLC, Inc. or Associates", ["The team leader's surname", "The word Team"],
  "Rule 1260-02-.12(3)(f)(2)."),
 ("tn/advertising", "Cooperation", 2, "Advertising a property listed by another licensee requires:",
  "Written authorisation from the listing agent or listing broker", ["MLS membership alone", "Nothing at all"],
  "Rule 1260-02-.12(3)(e)."),
 ("tn/advertising", "Internet", 1, "On a Tennessee licensee's website, the firm name and telephone number must appear:",
  "Conspicuously on each page", ["On the home page only", "In the footer of the contact page"],
  "Rule 1260-02-.12(5)(a)."),
 ("tn/advertising", "Internet", 2, "A page showing listings from an outside database must state:",
  "That some or all of the listings may not belong to the firm whose website is being visited", ["The database's name", "The total number of listings"],
  "Rule 1260-02-.12(5)(b)."),
 ("tn/advertising", "Internet", 3, "The duty to keep listing information current applies to:",
  "First generation advertising the licensee places, not syndicated copies beyond their control", ["Every copy anywhere on the internet", "Nothing online"],
  "Rule 1260-02-.12(5)(c)."),
 ("tn/advertising", "Franchise", 3, "A franchise-name advertisement for a specific property must show, adjacent to it:",
  "The licensee's name, the firm name and the firm telephone number as registered with TREC", ["Only the franchise logo", "Only the firm name"],
  "Rule 1260-02-.12(4)(a)."),
 ("tn/advertising", "Gifts", 1, "A gift offered as an inducement in Tennessee must be:",
  "Sponsored and approved by the firm, and offered in writing signed by the licensee", ["Approved by TREC", "Worth less than $100"],
  "Rule 1260-02-.33(1)."),
 ("tn/advertising", "Gifts", 1, "Cash rebates and gift cards as transaction incentives are:",
  "Prohibited, except a gift card at a licensee open house or as a closing gift", ["Always permitted", "Permitted up to $500"],
  "Rule 1260-02-.33(2)."),
 ("tn/advertising", "Gifts", 3, "A closing-gift gift card:",
  "May not be used in advertising to induce business", ["May be advertised freely", "Must be reported to TREC"],
  "Rule 1260-02-.33(2)(c)."),
 ("tn/advertising", "Gifts", 2, "The written gift offer must disclose:",
  "Accurate specifications, fair market value, time and place of delivery, and any requirements", ["Only the value", "Only the delivery date"],
  "Rule 1260-02-.33(1)(b)."),
 ("tn/advertising", "Supervision", 2, "Tennessee advertising is under the direct supervision of:",
  "The principal broker", ["The team leader", "The franchise"],
  "Rule 1260-02-.12(3)(b)."),

 # agency
 ("tn/agency", "Limited agency", 1, "A Tennessee licensee acting as an agent is:",
  "A limited agent who functions as an intermediary in negotiations", ["A universal agent", "A general agent with full fiduciary duty"],
  "T.C.A. 62-13-402(a)."),
 ("tn/agency", "Limited agency", 1, "The statutory duties in 62-13-403 and 62-13-404:",
  "Supersede any fiduciary or common law duties owed to the client", ["Supplement common law fiduciary duty", "Apply only to buyers"],
  "T.C.A. 62-13-402(c)."),
 ("tn/agency", "Facilitator", 1, "A Tennessee licensee who represents neither party is:",
  "A facilitator", ["A dual agent", "A subagent", "A designated agent"],
  "T.C.A. 62-13-405; title 62 chapter 13 part 4."),
 ("tn/agency", "Duties to all", 1, "Tennessee's duty of confidentiality to a party:",
  "Survives both a later agency relationship and the closing of the transaction", ["Ends at closing", "Ends when an agency agreement is signed"],
  "T.C.A. 62-13-403(3)."),
 ("tn/agency", "Duties to all", 1, "Adverse facts must be disclosed where the licensee has:",
  "Actual notice or knowledge", ["Any suspicion", "Constructive notice", "A rumour"],
  "T.C.A. 62-13-403(2)."),
 ("tn/agency", "Duties to all", 2, "Market condition information must be given:",
  "Only where available through public records and only when a party requests it", ["Proactively to every party", "Never"],
  "T.C.A. 62-13-403(5)."),
 ("tn/agency", "Duties to all", 2, "Acting for a member of the licensee's immediate family requires:",
  "Prior disclosure and the timely written consent of all parties", ["Oral disclosure", "Nothing at all"],
  "T.C.A. 62-13-403(7)(A)."),
 ("tn/agency", "Duties to all", 2, "Recommending a service provider who may pay the licensee a referral fee requires:",
  "Timely disclosure of the interest or the possible fee", ["Nothing if the provider is licensed", "Written consent of all parties"],
  "T.C.A. 62-13-403(7)(B)."),
 ("tn/agency", "Client duties", 1, "Which four client services may be waived in Tennessee?",
  "Scheduling showings, receiving and forwarding offers, answering negotiation questions, and advising on post-execution steps", ["Loyalty and obedience", "Confidentiality and accounting"],
  "T.C.A. 62-13-404(3)(A)."),
 ("tn/agency", "Client duties", 2, "A waiver of those duties must be:",
  "Specific, individual and in writing by the client", ["Oral with a witness", "Implied by the listing agreement"],
  "T.C.A. 62-13-404(3)(A)."),
 ("tn/agency", "Client duties", 2, "On waiving a duty, the consumer must be told in writing that:",
  "They may not expect or seek that assistance from any other licensee in the transaction", ["The commission will be reduced", "TREC must approve the waiver"],
  "T.C.A. 62-13-404(3)(B)."),
 ("tn/agency", "Disclosure", 1, "Agency status must be confirmed in writing with an unrepresented buyer:",
  "Before the preparation of an offer to purchase", ["At closing", "Within three days of the offer"],
  "T.C.A. 62-13-405(b)."),
 ("tn/agency", "Disclosure", 1, "With an unrepresented seller, the written confirmation comes:",
  "Before execution of a listing agreement or presentation of an offer, whichever comes first", ["Only at listing", "Only at the offer"],
  "T.C.A. 62-13-405(b)."),
 ("tn/agency", "Disclosure", 2, "The signed receipt for the agency disclosure must include:",
  "The complaint time limit and the Commission's address and telephone number", ["The commission rate", "The firm's licence number"],
  "T.C.A. 62-13-405(b)."),
 ("tn/agency", "Disclosure", 2, "Are Tennessee licensees obliged to discover latent defects?",
  "No; the duty is to disclose known adverse facts", ["Yes, by personal inspection", "Yes, by hiring an inspector"],
  "T.C.A. 62-13-405(a)."),
 ("tn/agency", "Disclosure", 2, "On first contact with another licensee in the same transaction, a licensee must:",
  "Immediately disclose their role, including any agency relationship", ["Wait until an offer is made", "Say nothing"],
  "T.C.A. 62-13-405(d)."),
 ("tn/agency", "Designated agency", 1, "In Tennessee designated agency, the managing broker:",
  "Is not a dual agent where the designated agent represents only one party to the transaction", ["Automatically becomes a dual agent", "Must withdraw from the deal"],
  "T.C.A. 62-13-406(a)."),
 ("tn/agency", "Designated agency", 2, "Knowledge in a designated agency situation is:",
  "Not imputed among clients, the managing broker and the designated agents", ["Imputed to the whole firm", "Imputed to the managing broker only"],
  "T.C.A. 62-13-406(c)."),
 ("tn/agency", "Designated agency", 3, "A designated agent may be appointed:",
  "By specific appointment or by written company policy", ["Only by specific appointment", "Only by TREC"],
  "T.C.A. 62-13-406(a)."),
 ("tn/agency", "Buyer agreements", 2, "An exclusive buyer representation agreement must confirm in writing that the buyer:",
  "Should arrange all viewings through the licensee and tell other licensees they are represented", ["May work with any agent", "Owes nothing in any event"],
  "Rule 1260-02-.36."),

 # broker/affiliate
 ("tn/broker-affiliate", "Supervision", 1, "A Tennessee real estate office must have:",
  "A principal broker devoted to its full time management", ["A broker on call", "Any licensed affiliate in charge"],
  "Rule 1260-02-.01(1)."),
 ("tn/broker-affiliate", "Offices", 1, "Using a post office box as a business location is:",
  "Prohibited", ["Allowed for rural offices", "Allowed with TREC approval"],
  "Rule 1260-02-.05."),
 ("tn/broker-affiliate", "Compensation", 1, "A Tennessee team member may be paid by:",
  "Their principal broker only", ["The seller directly", "The team leader", "Any licensed broker"],
  "Rule 1260-02-.41(2)."),
 ("tn/broker-affiliate", "Teams", 2, "A Tennessee team may maintain an office separate from the firm's location of record:",
  "No", ["Yes, within the same county", "Yes, with TREC approval"],
  "Rule 1260-02-.41(1)."),
 ("tn/broker-affiliate", "Teams", 2, "A principal broker may delegate supervisory responsibility to a team:",
  "No; the principal broker remains ultimately responsible", ["Yes, in writing", "Yes, for team members only"],
  "Rule 1260-02-.41(3)."),
 ("tn/broker-affiliate", "Affiliation", 1, "A principal broker's responsibility for a departing licensee's future acts ends:",
  "When the Commission receives the release form or online submission", ["When the licensee resigns", "At the end of the month"],
  "Rule 1260-02-.02(1)."),
 ("tn/broker-affiliate", "Affiliation", 2, "After release, the licensee must complete the change of affiliation or retirement within:",
  "Ten days", ["Thirty days", "Sixty days"],
  "Rule 1260-02-.02(2)."),
 ("tn/broker-affiliate", "Affiliation", 2, "Between release and processing, the licensee may:",
  "Not engage in any activity requiring a licence", ["Keep working for the old firm", "Work for the new firm immediately"],
  "Rule 1260-02-.02(2)."),
 ("tn/broker-affiliate", "Out of state", 3, "A Tennessee broker may pay a commission to a broker licensed in another state:",
  "Provided that broker conducts no negotiation in Tennessee", ["Never", "Only through an escrow agent"],
  "TREC guidance on the Broker License Act."),
 ("tn/broker-affiliate", "Principal broker", 3, "TREC must be notified of a principal broker's death or incapacity within:",
  "Ten days", ["Thirty days", "Five business days"],
  "Rule 1260-02-.38(1)."),

 # commission
 ("tn/commission", "Jurisdiction", 1, "Which is OUTSIDE TREC's jurisdiction?",
  "A commission dispute between two licensees", ["Unlicensed activity", "A licensee's advertising", "Escrow handling"],
  "PSI Tennessee state outline; TREC's statutory purpose is public protection."),
 ("tn/commission", "Licensure", 2, "Passing the Tennessee examination:",
  "Does not guarantee that a licence will be issued", ["Entitles the candidate to a licence", "Replaces the application"],
  "PSI Tennessee bulletin."),
 ("tn/commission", "Discipline", 2, "After a conviction for a theft misdemeanour, a person may not be licensed until:",
  "Two years have passed from conviction, release, or the end of probation or parole, whichever is later", ["One year has passed", "The conviction is expunged"],
  "Rule 1260-01-.01(4)."),
 ("tn/commission", "Discipline", 3, "The two-year bar applies to:",
  "All felonies and to misdemeanours involving theft of money, services or property", ["Any criminal offence", "Felonies only"],
  "Rule 1260-01-.01(4)."),

 # licensing
 ("tn/licensing", "Education", 1, "Tennessee affiliate broker education totals:",
  "90 hours - 60 before the examination and a 30-hour Course for New Affiliates before licensure", ["60 hours in total", "90 hours all before the examination"],
  "T.C.A. 62-13-303(b)(2); Rule 1260-05-.03."),
 ("tn/licensing", "Education", 2, "Which 60 hours must be completed before sitting the examination?",
  "Real estate principles and fundamentals", ["The Course for New Affiliates", "Contracts and closings"],
  "PSI Tennessee bulletin."),
 ("tn/licensing", "Continuing education", 1, "Tennessee continuing education is:",
  "16 hours, including the 6-hour mandatory TREC Core course", ["12 hours", "24 hours", "8 hours"],
  "TREC Instructor Training Manual; Rule 1260-05."),
 ("tn/licensing", "E&O", 1, "Errors and omissions insurance in Tennessee is:",
  "Required, and the principal broker must ensure affiliated licensees carry it at all times", ["Optional", "Required only of principal brokers"],
  "PSI Tennessee state outline; TREC newsletter."),

 # records
 ("tn/records", "Retention", 1, "Tennessee transaction records must be kept for:",
  "Three years following consummation of the transaction", ["One year", "Five years", "Seven years"],
  "T.C.A. 62-13-312(b)(6); Rule 1260-02-.40(1)."),
 ("tn/records", "Offers", 1, "Written offers must be tendered:",
  "Promptly, until a contract is signed by all parties", ["Only until the first offer is accepted", "At the seller's convenience"],
  "Rule 1260-02-.08."),
 ("tn/records", "Offers", 2, "On acceptance, true executed copies signed by the seller go to:",
  "Both the purchaser and the seller, promptly", ["The purchaser only", "The closing agent only"],
  "Rule 1260-02-.08."),
 ("tn/records", "Offers", 2, "When an offer is rejected, the Tennessee licensee must:",
  "Ask the seller to note the rejection on the offer and return it to the offeror or their agent", ["Destroy the offer", "File it without comment"],
  "Rule 1260-02-.08."),

 # escrow
 ("tn/escrow", "Deposit", 1, "Tennessee trust money must be deposited:",
  "Promptly upon acceptance of the offer, unless the offer states who will deposit it", ["Within three banking days of receipt", "At closing"],
  "Rule 1260-02-.09(11)."),
 ("tn/escrow", "Disbursement", 1, "On a written request for disbursement, earnest money must be disbursed, interpleaded or given to an attorney within:",
  "21 calendar days, absent a compelling reason", ["10 business days", "30 days", "60 days"],
  "Rule 1260-02-.09(9)."),
 ("tn/escrow", "Commingling", 1, "Commingling in Tennessee means:",
  "Keeping funds belonging to others in the same account as the licensee's own personal or business funds", ["Mixing two clients' deposits", "Holding funds too long"],
  "Rule 1260-02-.09(1)(a)."),
 ("tn/escrow", "Disbursement", 2, "Which is NOT a permitted disbursement of Tennessee trust money?",
  "On the oral agreement of the buyer and seller", ["At the closing", "On filing an interpleader action", "On the order of a court"],
  "Rule 1260-02-.09(7) requires a separate written agreement signed by all parties."),

 # improper
 ("tn/improper", "Net listing", 1, "A net listing in Tennessee is:",
  "Prohibited", ["Allowed with written consent", "Allowed for commercial property"],
  "Rule 1260-02-.07."),
 ("tn/improper", "Personal interest", 1, "A Tennessee licensee buying or selling property for themselves must:",
  "Identify themselves as a licensee", ["Use a corporate nominee", "Notify TREC in advance"],
  "Rule 1260-02-.11(2)."),
 ("tn/improper", "Personal interest", 2, "Taking an option on a property the owner approached you to broker requires:",
  "Full prior disclosure of your true position to the owner", ["Nothing, as no listing was signed", "TREC approval"],
  "Rule 1260-02-.11(1)."),

 # special
 ("tn/special", "Exemptions", 1, "Which transactions escape the 62-13-403 to 405 disclosure duties?",
  "Commercial property, public auctions, residential property of more than four units, and residential leases", ["New construction", "Vacant land", "All cash sales"],
  "T.C.A. 62-13-405(e)."),
 ("tn/special", "Timeshare", 2, "The Tennessee Timeshare Act dates from:",
  "1987", ["1973", "1995", "2006"],
  "PSI Tennessee bulletin."),
 ("tn/special", "Property management", 2, "Trust money relating to leases must be held:",
  "In one or more separate escrow or trustee accounts", ["In the firm's sales escrow account", "By the property owner"],
  "Rule 1260-02-.09(12)."),
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
            "id": "tn-" + hashlib.sha1(q.encode()).hexdigest()[:8],
            "portion": "georgia", "topic": topic, "subtopic": sub,
            "sub": topic + "|" + sub, "concept": "Tennessee " + sub.lower(),
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
        "code": "TN", "name": "Tennessee", "abbr": "TN",
        "regulator": "Tennessee Real Estate Commission",
        "pass": EXAM["pass"],
        "portions": {
            "national": {"scored": EXAM["national_scored"],
                         "minutes": EXAM["national_minutes"],
                         "blurb": "80 questions, 56 correct to pass."},
            "georgia": {"name": "Tennessee law", "scored": EXAM["state_scored"],
                        "minutes": EXAM["state_minutes"],
                        "blurb": "The Broker License Act of 1973, TREC's Rules of Conduct and the 40-item state outline."},
        },
        "topics": topics, "bank": bank, "study": study,
        "sources": SOURCES, "diffs": DIFFS,
    }


# Where Tennessee departs from the national rule.
DIFFS = {
    "national/agency": [
        "Tennessee's STATUTORY duties SUPERSEDE common law fiduciary duty, and an agent is a LIMITED AGENT acting as an intermediary (T.C.A. 62-13-402).",
        "Confidentiality attaches BEFORE any agency agreement and SURVIVES CLOSING (62-13-403(3)).",
        "Market condition information is owed only from PUBLIC RECORDS and only ON REQUEST (62-13-403(5)).",
        "Four client services - scheduling showings, receiving and forwarding offers, answering negotiation questions, and post-execution advice - may be WAIVED IN WRITING, with a warning that no other licensee will supply them (62-13-404(3)).",
        "A licensee representing neither party is a FACILITATOR, and under DESIGNATED AGENCY the managing broker is NOT a dual agent (62-13-406).",
    ],
    "national/practice": [
        "Trust money is deposited PROMPTLY UPON ACCEPTANCE of the offer, and a written disbursement request starts a 21 CALENDAR DAY clock (Rule 1260-02-.09).",
        "NET LISTINGS are prohibited outright (Rule 1260-02-.07), and a licensee must identify themselves as a licensee when buying or selling for themselves (1260-02-.11).",
        "Advertising must carry the FIRM NAME and FIRM TELEPHONE NUMBER, with the firm name in type the SAME SIZE OR LARGER than the agent's or team's; the firm name must be on EVERY page of a website (Rule 1260-02-.12).",
        "CASH rebates and gift cards are banned as incentives, except a gift card at a licensee open house or as a closing gift (Rule 1260-02-.33).",
        "Education: 90 hours split 60 plus a 30-hour Course for New Affiliates, then 16 hours of continuing education including the 6-hour TREC Core; records are kept THREE YEARS.",
    ],
    "national/disclosures": [
        "Agency status is disclosed VERBALLY before any services to an unrepresented party, then CONFIRMED IN WRITING before the offer is prepared (buyer) or before listing or presentation of an offer (seller), with a SIGNED RECEIPT carrying TREC's contact details (62-13-405).",
        "Licensees need not DISCOVER latent defects; the duty is to disclose KNOWN adverse facts (62-13-405(a)).",
        "Commercial property, public auctions, residential property of MORE THAN FOUR UNITS and residential leases are OUTSIDE the disclosure duties (62-13-405(e)).",
    ],
}


if __name__ == "__main__":
    import io, json, os
    here = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    out = os.path.join(here, "greprep", "packs", "TN.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    pack = build()
    with io.open(out, "w", encoding="utf-8") as f:
        json.dump(pack, f, ensure_ascii=False, indent=1, sort_keys=True)
    print("wrote", out, len(pack["bank"]), "questions,", len(pack["study"]), "lessons")
