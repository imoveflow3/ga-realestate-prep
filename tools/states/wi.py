"""Wisconsin state content: lessons and practice questions.

Wisconsin writes ONE paper and it is Wisconsin law from end to end. The
Pearson VUE content outline says in terms: "The state portion of the
salesperson examination consists of 140 scored items, and 5-10 pretest
items." The handbook gives the salesperson 4 hours.

The pass mark is NOT a percentage. The handbook says scores are equated
and reported on a converted 0-100 scale, that DSPS set a passing SCALED
SCORE of 75, and that the scaled score "is neither the number of questions
answered correctly nor the percentage of questions answered correctly".
So the pack sets pass_published False and gives 75% only as a study target.

Wisconsin also has a set of changes made by 2025 Wis. Act 69 that take
effect 1 JANUARY 2027 - the firm-to-firm compensation ban, the rule that
seller-paid buyer-agent compensation must sit in the executed offer, and
an AI-altered advertising disclosure. They are flagged as not yet in force
rather than taught as current law.

Every rule below was read from the official text on 2026-11-10:
  - Wis. Stat. ch. 452 (real estate practice), from docs.legis.wisconsin.gov.
  - Wis. Admin. Code REEB 25 (education).
  - Wis. Stat. ch. 709 (condition reports), s. 106.50 (open housing),
    s. 77.22 (real estate transfer fee), s. 766.31 (marital property).
  - The DSPS continuing education page at dsps.wi.gov.
  - The Pearson VUE Wisconsin Real Estate Candidate Handbook (#095000) and
    Content Outlines (#095006).
The section a fact comes from is cited next to it. Do not add a fact here
without reading its source first.
"""

EXAM = {
    # One paper: 140 scored items, 4 hours. Scaled pass of 75 on 0-100,
    # which the handbook says is not a percentage correct.
    "state_scored": 99,
    "state_minutes": 170,
    "national_scored": 41,
    "national_minutes": 70,
    "pass": 0.75,
    "pass_published": False,
    "pass_note": ("Wisconsin equates its forms and reports a SCALED score on a 0-100 "
                  "scale. DSPS set the passing scaled score at 75, but the handbook "
                  "says that score is neither the number nor the percentage of "
                  "questions answered correctly. Numeric scores are reported only to "
                  "candidates who FAIL. Treat 75% here as a study target, not the "
                  "state's requirement."),
}

# Pearson's Wisconsin salesperson outline. The 99 Wisconsin-law items here,
# plus 41 general items (ownership and transfer 14, land use 5, valuing and
# financing and calculations 20, federal antitrust 2), make the 140.
TOPICS = [
    ("wi/agency", "Agency", 32,
     "Duties to parties and clients, multiple representation, the WB agency forms."),
    ("wi/contracts", "Contract law & approved forms", 22,
     "Approved forms, the WB-11 offer, counter-offers, amendments, notices."),
    ("wi/ethics", "Business ethics", 14,
     "Conduct and ethical practice rules for Wisconsin licensees."),
    ("wi/disclosures", "Disclosures", 13,
     "The condition report, environmental items, condominiums, lead paint."),
    ("wi/misc", "Trust accounts & responsibilities", 12,
     "Client funds, fee splitting, firm supervision, leases and rentals."),
    ("wi/fair-housing", "Fair housing", 6,
     "Wisconsin's open housing law, local ordinances and the ADA."),
]

SOURCES = [
    {"by": "Wisconsin Legislature",
     "name": "Wis. Stat. ch. 452, Real Estate Practice",
     "note": "Duties of licensees, multiple representation, disclosure statements, trust accounts, advertising and compensation.",
     "url": "https://docs.legis.wisconsin.gov/statutes/statutes/452"},
    {"by": "Wisconsin Real Estate Examining Board",
     "name": "Wis. Admin. Code ch. REEB 25, Education",
     "note": "The 72-hour salesperson pre-licence programme and the continuing education rules.",
     "url": "https://docs.legis.wisconsin.gov/code/admin_code/reeb/25"},
    {"by": "Wisconsin Legislature",
     "name": "Wis. Stat. ch. 709, s. 106.50, s. 77.22 and s. 766.31",
     "note": "The real estate condition report, open housing, the transfer fee and marital property.",
     "url": "https://docs.legis.wisconsin.gov/statutes/statutes/709"},
    {"by": "Wisconsin DSPS",
     "name": "Real Estate Continuing Education",
     "note": "The Board's own published 18-hour biennial requirement: 12 mandatory hours plus 6 electives.",
     "url": "https://dsps.wi.gov/credentialing/real-estate-continuing-education/"},
    {"by": "Pearson VUE and Wisconsin DSPS",
     "name": "Wisconsin Real Estate Candidate Handbook and Content Outlines",
     "note": "140 scored items, 4 hours, a scaled passing score of 75, and the Wisconsin outline.",
     "url": "https://www.pearsonvue.com/us/en/wi/realestate.html"},
]


# --------------------------------------------------------------- lessons

STUDY = {}

STUDY["wi/agency"] = {
    "summary": "Thirty-two items, by far the biggest block. Wisconsin's duties run from the FIRM, not the individual, and the firm owes a short list of duties to EVERY party and a longer list to its clients.",
    "sections": [
        {"h": "Duties to ALL parties (s. 452.133(1))",
         "p": ["A firm providing brokerage services to a party owes that party, client or not:"],
         "l": ["The duty to provide brokerage services HONESTLY AND FAIRLY.",
               "The duty to provide them with REASONABLE SKILL AND CARE.",
               "The duty to TIMELY DISCLOSE IN WRITING all MATERIAL ADVERSE FACTS the firm knows and the party does not know or cannot discover through reasonably vigilant observation, unless disclosure is prohibited by law.",
               "The duty to KEEP CONFIDENTIAL any information given in confidence, or that the firm knows a reasonable person would want kept confidential - and it CONTINUES AFTER the transaction is complete and after the firm stops providing services.",
               "The duty to provide ACCURATE INFORMATION ABOUT MARKET CONDITIONS within a reasonable time of a request.",
               "The duty to SAFEGUARD TRUST FUNDS and other property held.",
               "When negotiating for a party, the duty to present contract proposals in an OBJECTIVE AND UNBIASED manner and to disclose the ADVANTAGES AND DISADVANTAGES of the proposals."],
         "check": [("Wisconsin's duty of confidentiality to a party:", "Continues after the transaction is complete and after the firm stops providing services", ["Ends at closing", "Applies only to clients"], "s. 452.133(1)(d)."),
                   ("A material adverse fact must be disclosed:", "Timely and in writing, where the firm knows it and the party cannot discover it by reasonably vigilant observation", ["Orally at the showing", "Only if the party asks"], "s. 452.133(1)(c)."),
                   ("When negotiating, a firm must present contract proposals:", "In an objective and unbiased manner, disclosing advantages and disadvantages", ["In the light most favourable to its client", "Without comment"], "s. 452.133(1)(g)."),
                   ("Accurate information about market conditions is owed to:", "Any party who requests it, within a reasonable time", ["Clients only", "Only the seller"], "s. 452.133(1)(e).")]},
        {"h": "Extra duties to CLIENTS (s. 452.133(2))",
         "l": ["LOYAL REPRESENTATION: placing the client's interests ahead of the FIRM'S OWN interests, and ahead of the interests of non-clients in the transaction by not disclosing to them information or advice contrary to the client's interests unless the law requires it.",
               "On request, INFORMATION AND ADVICE on matters material to the client's transaction that are within the knowledge, skills and training required for a licence.",
               "DISCLOSURE of all information known to the firm that is material to the transaction and not known to or discoverable by the client, except confidential information and information whose disclosure is prohibited.",
               "FULFILLING the obligations of the agency agreement and any client order within its scope, so long as not inconsistent with another duty under the chapter.",
               "The duty to NEGOTIATE on behalf of the client.",
               "An AGENCY AGREEMENT is a WRITTEN agreement between a firm and a client authorising the firm to provide brokerage services (s. 452.01(1m))."],
         "check": [("A client's interests must be placed ahead of:", "The firm's own interests and the interests of non-clients", ["Only the other party's interests", "Nobody's"], "s. 452.133(2)(a)."),
                   ("An agency agreement in Wisconsin must be:", "In writing", ["Oral if witnessed", "Implied by conduct"], "s. 452.01(1m)."),
                   ("A firm owes the duty to negotiate:", "To its client", ["To every party", "To the other firm"], "s. 452.133(2)(d)."),
                   ("Which may a firm NOT do for a client?", "Disclose the client's confidential information to advance the client's position", ["Place the client's interests ahead of its own", "Negotiate for the client"], "s. 452.133(2)(b) carves out confidential information.")]},
        {"h": "Who may negotiate, and multiple representation",
         "l": ["A firm may provide BROKERAGE SERVICES to any party whether or not there is an agency agreement, but may NOT NEGOTIATE on behalf of a party unless that party is the firm's CLIENT or a client of a PRINCIPAL FIRM that engaged it as a SUBAGENT (s. 452.134(1)).",
               "A firm may not provide services in a MULTIPLE REPRESENTATION RELATIONSHIP unless ALL of the firm's clients in it have CONSENTED IN WRITING (s. 452.134(2)).",
               "DESIGNATED AGENCY within a multiple representation relationship also needs the WRITTEN CONSENT of all the firm's clients in that relationship, and a client may WITHDRAW consent by written notice AT ANY TIME (s. 452.134(3)(a)).",
               "With designated agency, the licensee negotiating for a client may give that client information, opinions and advice to assist in the negotiation EVEN IF it places one client's interests ahead of another client's (s. 452.134(3)(b)).",
               "WITHOUT designated agency - or if consent is withdrawn - the firm and its licensees may NOT place the interests of any client ahead of any other in the negotiations (s. 452.134(4)).",
               "A SUBAGENT owes all parties the duties in s. 452.133(1) but does NOT owe the principal firm's clients the client duties in sub. (2). A subagent may not put its own interests ahead of the principal firm's clients, nor give advice contrary to their interests unless required by law (s. 452.133(4))."],
         "check": [("A firm may negotiate on behalf of a party only if that party is:", "The firm's client, or a client of a principal firm that engaged the firm as a subagent", ["Anyone it is working with", "Anyone who signs a disclosure"], "s. 452.134(1)(b)."),
                   ("A multiple representation relationship requires:", "The written consent of all of the firm's clients in it", ["Oral consent", "Board approval", "Nothing"], "s. 452.134(2)."),
                   ("A client may withdraw consent to designated agency:", "At any time, by written notice to the firm", ["Only before an offer", "Not at all"], "s. 452.134(3)(a)."),
                   ("Without designated agency, a firm in multiple representation:", "May not place any client's interests ahead of any other's", ["Favours the seller", "Favours whoever signed first"], "s. 452.134(4)."),
                   ("A subagent owes the principal firm's clients:", "Only the duties owed to all parties, not the client duties", ["Full client duties", "No duties at all"], "s. 452.133(4)(a).")]},
        {"h": "The disclosure statements (s. 452.135)",
         "l": ["A firm may NOT NEGOTIATE on behalf of a party who is NOT its client unless it first gives that party a copy of the statutory DISCLOSURE TO CUSTOMERS - which recites the duties owed to a customer under s. 452.133(1) and tells the reader to go to an attorney, tax advisor or home inspector for that advice.",
               "A firm must give a CLIENT a copy of the statutory DISCLOSURE TO CLIENTS NOT LATER THAN the time the firm ENTERS INTO THE AGENCY AGREEMENT with the client.",
               "A SUBAGENT must give the Disclosure to Customers to any person who is not the principal firm's client and who receives brokerage services from the subagent.",
               "The supervising broker's pre-closing review must CONFIRM that the written disclosure statement was provided (s. 452.132(4)(b))."],
         "check": [("The Disclosure to Clients must be given:", "Not later than the time the firm enters into the agency agreement", ["At the first showing", "Before closing", "With the offer"], "s. 452.135(2)(a)."),
                   ("The Disclosure to Customers must be given before:", "The firm negotiates on behalf of a party who is not its client", ["Any conversation at all", "The listing is taken"], "s. 452.135(1)(a)."),
                   ("The Disclosure to Customers is described in the statute as:", "A plain-language summary of the duties to a customer under s. 452.133(1)", ["A contract", "A warranty of condition"], "s. 452.135(1)(a).")]},
        {"h": "Prohibited conduct in providing brokerage services (s. 452.133(3))",
         "l": ["Accepting any FEE OR COMPENSATION related to the transaction from any person OTHER THAN the licensee's client or firm WITHOUT THE PRIOR WRITTEN CONSENT OF ALL PARTIES.",
               "Acting in a transaction ON THE LICENSEE'S OWN BEHALF, for the licensee's IMMEDIATE FAMILY, for the licensee's FIRM, or for any entity in which the licensee has an interest, WITHOUT the prior written consent of all parties - and the consent must be taken IN THE OFFER TO PURCHASE, OPTION, LEASE OR OTHER TRANSACTION CONTRACT.",
               "REFERRING or recommending a service provider from which the licensee may receive compensation, or in which the licensee has an interest, WITHOUT DISCLOSING THAT IN WRITING.",
               "NEGOTIATING the sale, exchange, purchase or rental of PERSONAL PROPERTY unless related to the transaction.",
               "COMMON LAW is superseded: the chapter's duties override inconsistent common law duties (s. 452.139(1)). A CLIENT is NOT LIABLE for a firm's misrepresentation unless the client knew or should have known, or the firm is repeating the client's own misrepresentation (s. 452.139(2)(a))."],
         "check": [("A licensee buying a listed property personally must take the parties' written consent:", "In the offer to purchase, option, lease or other transaction contract", ["In a separate letter", "Orally before writing"], "s. 452.133(3)(b)."),
                   ("Recommending a home inspector who pays the licensee a referral fee requires:", "Written disclosure of the compensation or interest", ["Nothing, if the inspector is licensed", "The client's oral consent"], "s. 452.133(3)(c)."),
                   ("Accepting compensation from someone other than the licensee's client or firm requires:", "The prior written consent of all parties to the transaction", ["Only the payer's consent", "Nothing"], "s. 452.133(3)(a)."),
                   ("A client is liable for a firm's misrepresentation:", "Only if the client knew or should have known, or the firm repeated the client's own misrepresentation", ["Always", "Never"], "s. 452.139(2)(a).")]},
    ],
    "traps": [
        "Duties run from the FIRM; each associated licensee owes the same duties the firm owes.",
        "Confidentiality survives the transaction and the relationship. It does not end at closing.",
        "You may work with anyone, but you may only NEGOTIATE for a client or a principal firm's client.",
        "Designated agency lets one licensee favour one client; without it, nobody is favoured.",
        "Self-dealing consent goes IN the contract, not in a side letter.",
    ],
    "vocab": [
        ["Firm", "The licensed broker business entity or individual broker the duties run from."],
        ["Agency agreement", "The written agreement authorising brokerage services for a client."],
        ["Material adverse fact", "A condition significantly affecting value, structure or health, or showing a party will not perform."],
        ["Multiple representation", "One firm with more than one client in the same transaction."],
        ["Designated agency", "Naming individual licensees to negotiate for each client."],
        ["Subagent", "A firm engaged by a principal firm to help its clients."],
    ],
    "examples": [
        {"t": "Two clients, one firm",
         "s": "Your firm lists a house and also has a buyer client who wants it. Both consent in writing to multiple representation but the seller refuses designated agency.",
         "w": ["Multiple representation is allowed because both clients consented in writing.",
               "Designated agency is NOT available without the consent of all the firm's clients in the relationship.",
               "So the firm and its licensees may not place either client's interests ahead of the other's in the negotiations."],
         "k": "Consent to multiple representation and consent to designated agency are two separate consents."},
    ],
}

STUDY["wi/contracts"] = {
    "summary": "Twenty-two items, most of them on the WB forms. Wisconsin licensees fill in Board-approved forms; they do not draft and they do not advise on legal rights.",
    "sections": [
        {"h": "Approved forms and the line you cannot cross (s. 452.40)",
         "l": ["To USE A FORM means to complete it by FILLING IN BLANKS or MODIFYING PRINTED PROVISIONS at the instruction of a party the licensee is working with or representing in a SPECIFIC TRANSACTION.",
               "A firm and its licensees MAY use a form approved by the Board under s. 452.05(1)(b) in real estate practice.",
               "A licensee MAY NOT provide advice or opinions about the LEGAL RIGHTS OR OBLIGATIONS of the parties, the LEGAL EFFECT of a specific contract or conveyance, or the STATE OF TITLE.",
               "A licensee MAY give a GENERAL EXPLANATION of the provisions of an approved form, at the time of completing it or when delivering it for the seller's or buyer's acceptance.",
               "A supervising broker's review under s. 452.132(4) is NOT the provision of legal advice."],
         "check": [("A Wisconsin licensee may:", "Give a general explanation of an approved form's provisions when completing or delivering it", ["Advise on the legal effect of the contract", "Opine on the state of title"], "s. 452.40(2)."),
                   ("'Use a form' means:", "Filling in blanks or modifying printed provisions at a party's instruction in a specific transaction", ["Writing a form from scratch", "Reading a form aloud"], "s. 452.40(1)(a)."),
                   ("A supervising broker's pre-closing review is:", "Not the provision of legal advice or opinion", ["Unauthorised practice of law", "Optional"], "s. 452.40(2).")]},
        {"h": "The forms the outline names",
         "l": ["WB-1 Residential Listing Contract and WB-4 Residential Condominium Listing Contract.",
               "WB-36 Buyer Agency / Tenant Representation Agreement.",
               "WB-11 Residential Offer to Purchase, WB-13 Vacant Land Offer to Purchase and WB-14 Residential Condominium Offer to Purchase.",
               "WB-40 Amendment to Offer to Purchase, WB-41 Notice Relating to Offer to Purchase, WB-44 Counter-Offer and WB-46 Multiple Counter Proposal.",
               "An AMENDMENT (WB-40) changes terms by agreement of BOTH parties; a NOTICE (WB-41) is a UNILATERAL communication one party is entitled to give under the contract, such as delivering a contingency notice."],
         "check": [("Which form changes the terms of an accepted offer by agreement of both parties?", "WB-40 Amendment to Offer to Purchase", ["WB-41 Notice Relating to Offer to Purchase", "WB-44 Counter-Offer"], "An amendment is bilateral; a notice is unilateral."),
                   ("Which form does a buyer use to respond to a seller's counter with new terms?", "WB-44 Counter-Offer", ["WB-40 Amendment", "WB-46 Multiple Counter Proposal"], "Named on the Wisconsin salesperson outline."),
                   ("The buyer agency and tenant representation agreement is:", "WB-36", ["WB-11", "WB-1", "WB-13"], "Named on the Wisconsin salesperson outline."),
                   ("A vacant land purchase uses:", "WB-13", ["WB-11", "WB-14", "WB-4"], "Named on the Wisconsin salesperson outline.")]},
        {"h": "Supervision, copies and records",
         "l": ["A FIRM must SUPERVISE the brokerage activities of each associated licensee, give each one a WRITTEN STATEMENT of the firm's procedures for handling leases, agency agreements, offers and records, tell them where to get the Board's conduct rules, and confirm each licensee holds a VALID LICENCE before association and at the start of each biennial period (s. 452.132(1), (2)).",
               "A SUPERVISING BROKER must, BEFORE CLOSING, review all agency agreements, offers, leases and other executed documents and records, and all TRUST ACCOUNT RECORDS for the transaction. The review is LIMITED to confirming the written disclosure statement was given, confirming any applicable approved form was used and completed consistently with its structure, and COMMUNICATING any errors apparent on the face of the document (s. 452.132(4)).",
               "The licensee must then DISCUSS any communicated error with the party, and THE PARTY decides whether to request changes (s. 452.132(6)(a)).",
               "A licensee must submit to the firm, IN A TIMELY MANNER, all executed agreements, offers, leases and records (s. 452.132(6)(b)), and the FIRM is responsible for their custody and safety (s. 452.132(3)).",
               "A firm that is a licensed broker business entity MUST delegate supervision to a SUPERVISING BROKER who is a licensed individual broker; the delegation is WRITTEN AND SIGNED by both. A firm may delegate to MORE THAN ONE supervising broker (s. 452.132(5)).",
               "Licensees must RETAIN transaction documents as the Board's rules require, and records MAY be kept in ELECTRONIC form (s. 452.42)."],
         "check": [("A supervising broker's pre-closing review covers:", "Executed documents, records and the transaction's trust account records", ["Only the offer", "Only the commission"], "s. 452.132(4)(a)."),
                   ("If the review turns up an error on the face of a document:", "The licensee discusses it with the party, who decides whether to request changes", ["The broker corrects it", "The closing is cancelled"], "s. 452.132(4)(b), (6)(a)."),
                   ("A licensed broker business entity must delegate supervision to:", "A supervising broker who is a licensed individual broker, in a signed writing", ["Any associated salesperson", "Nobody; the entity supervises itself"], "s. 452.132(5)(a), (c)."),
                   ("Transaction records may be retained:", "In electronic file format", ["On paper only", "Only by the Board"], "s. 452.42(2).")]},
    ],
    "traps": [
        "Fill in blanks, explain generally - never advise on legal rights, legal effect or title.",
        "Amendment = both parties agree. Notice = one party exercising a contract right.",
        "The supervising broker's review is narrow and does not make them the drafter.",
    ],
    "vocab": [
        ["Approved form", "A form the Real Estate Examining Board has approved for use."],
        ["Supervising broker", "The licensed individual broker a firm delegates supervision to."],
        ["WB-11", "The Residential Offer to Purchase."],
        ["WB-41", "The unilateral Notice Relating to Offer to Purchase."],
    ],
    "examples": [],
}

STUDY["wi/ethics"] = {
    "summary": "Fourteen items on conduct. Advertising and compensation carry most of the weight, and Wisconsin has a big change arriving on 1 January 2027 that you should know is COMING but is not law yet.",
    "sections": [
        {"h": "Advertising (s. 452.136)",
         "l": ["A licensee MAY NOT advertise in a manner that is FALSE, DECEPTIVE OR MISLEADING.",
               "Except for advertising the rental of real estate the licensee owns, all advertising must disclose the FIRM'S NAME exactly as printed on the licence, or a TRADE NAME previously filed with the department, and must CLEARLY INDICATE THAT THE FIRM IS A BUSINESS ENTERPRISE AND NOT A PRIVATE PARTY.",
               "An associated licensee advertises UNDER THE SUPERVISION OF AND IN THE NAME OF THE FIRM, and the firm's name must be CLEAR AND CONSPICUOUS.",
               "A licensee may advertise the OCCASIONAL sale of real estate the licensee owns, or occasionally solicit property for their own purchase, without the firm name, PROVIDED the advertisement CLEARLY IDENTIFIES them as a real estate licensee.",
               "A firm may NOT ADVERTISE A PROPERTY unless it is the LISTING FIRM or it has the LISTING FIRM'S CONSENT.",
               "A licensee may not advertise a property at a price OTHER THAN THAT AGREED WITH THE OWNER, though the price may be given as a RANGE or in general terms if it reflects the agreed price."],
         "check": [("All licensee advertising must clearly indicate that:", "The firm is a business enterprise and not a private party", ["The licensee owns the property", "The price is negotiable"], "s. 452.136(2)(a)."),
                   ("A firm may advertise a property it has not listed:", "Only with the listing firm's consent", ["Freely", "Never"], "s. 452.136(3)."),
                   ("A licensee advertising their own home for sale without the firm name must:", "Clearly identify themselves as a real estate licensee", ["Get Board approval", "Use the firm name anyway"], "s. 452.136(2)(c)."),
                   ("Advertising a price different from the one agreed with the owner is:", "Prohibited, though a range reflecting the agreed price is allowed", ["Allowed to attract interest", "Allowed below the agreed price only"], "s. 452.136(4).")]},
        {"h": "Compensation: the rule today, and the rule from 1 January 2027",
         "l": ["TODAY: no licensee may pay a fee, commission, referral fee or finder's fee to a person NOT LICENSED under ch. 452, unless that person is regularly and lawfully in the brokerage business in another state, territory or country, or was licensed here when the commission was earned or the referral arrangement was made (s. 452.19(1m)(a)).",
               "TODAY: if a licensee is associated with a firm, ALL fees, commissions, referral fees and finder's fees SHALL BE PAID TO THE FIRM (s. 452.19(1m)(b)).",
               "FROM 1 JANUARY 2027 (2025 Wis. Act 69): a firm SHALL NOT ACCEPT COMPENSATION OF ANY KIND FROM ANOTHER FIRM in a transaction involving RESIDENTIAL PROPERTY OF ONE TO FOUR DWELLING UNITS - whatever the parties represented, and whether the non-listing firm is a buyer's agent, a subagent or any other cooperative capacity. Referral and finder's fees are not caught. An agreement that violates it is VOID AND UNENFORCEABLE (s. 452.19(3)).",
               "FROM 1 JANUARY 2027: in a one-to-four unit residential transaction, a seller's agreement to pay a firm that is NOT the listing firm must be EXPRESSLY STATED IN THE FULLY EXECUTED OFFER OR OPTION TO PURCHASE and SIGNED BY BOTH BUYER AND SELLER as part of the contract. A listing contract may not require or imply such a payment unless it is contingent on that inclusion, and a listing contract must state whether the seller AUTHORISES THE LISTING FIRM TO DISCLOSE that compensation is being offered (s. 452.19(4)).",
               "FROM 1 JANUARY 2027: advertising ALTERED OR MODIFIED USING TECHNOLOGY, INCLUDING ARTIFICIAL INTELLIGENCE, to add, remove or change elements of the property in a way that creates a false or misleading impression must be DISCLOSED (s. 452.136(1m))."],
         "check": [("Under the law in force now, a licensee associated with a firm must have commissions paid to:", "The firm", ["The licensee personally", "An escrow agent"], "s. 452.19(1m)(b)."),
                   ("Paying a finder's fee to an unlicensed neighbour is:", "Prohibited", ["Allowed under $500", "Allowed with disclosure"], "s. 452.19(1m)(a)."),
                   ("From 1 January 2027, firm-to-firm compensation in a 1-4 unit residential sale is:", "Prohibited, and an agreement to pay it is void and unenforceable", ["Capped at 3%", "Allowed with written consent"], "s. 452.19(3), created by 2025 Wis. Act 69."),
                   ("From 1 January 2027, a seller's agreement to pay the buyer's firm must be:", "Expressly stated in the fully executed offer and signed by buyer and seller", ["In the listing contract only", "In the MLS"], "s. 452.19(4)(a)."),
                   ("From 1 January 2027, an AI-altered listing photo that misleads must be:", "Disclosed in the advertising", ["Removed by the MLS", "Reported to DSPS"], "s. 452.136(1m).")]},
        {"h": "Discipline and penalties",
         "l": ["The Board investigates on the secretary's motion or its own determination where it receives CREDIBLE INFORMATION that a licensee violated ch. 452 or a rule (s. 452.14(1)).",
               "Practising WITHOUT A LICENCE is prosecuted by the district attorney or the attorney general and carries a fine of NOT MORE THAN $5,000 or imprisonment of NOT MORE THAN 6 MONTHS or both. Any other violation of the chapter carries the same maximum (s. 452.17(1), (3)).",
               "For a DISCRIMINATION violation under s. 452.14(3)(jm) the Board SHALL suspend the licence for NOT LESS THAN 90 DAYS on a first offence and SHALL REVOKE it on a second, in addition to any other penalty (s. 452.17(4)).",
               "An INITIAL licence may not be issued to an individual convicted of a FELONY; after the confinement portion is complete or the applicant is released, and 3 YEARS have elapsed, the applicant may ask the Board for a suitability determination (s. 452.25(1)).",
               "The Board's register lists everyone whose licence was REVOKED WITHIN THE PAST 2 YEARS (s. 452.12(4))."],
         "check": [("The maximum fine for practising without a Wisconsin licence is:", "$5,000, or 6 months' imprisonment, or both", ["$1,000", "$10,000", "A civil forfeiture only"], "s. 452.17(1)."),
                   ("A first discrimination violation brings:", "Suspension of not less than 90 days", ["A warning", "Immediate revocation", "A $500 fine"], "s. 452.17(4)(a)(1)."),
                   ("A second discrimination violation brings:", "Revocation", ["A 180-day suspension", "A fine only"], "s. 452.17(4)(a)(2)."),
                   ("A felony conviction bars an initial licence until:", "The applicant has completed or been released from the sentence and 3 years have elapsed, then asks the Board for a determination", ["Five years have passed automatically", "Forever"], "s. 452.25(1)(b).")]},
    ],
    "traps": [
        "2025 Act 69's compensation and AI rules take effect 1 JANUARY 2027. Know which rule the question is asking about.",
        "Commissions are paid to the FIRM, not to the licensee.",
        "Discrimination carries a mandatory 90-day minimum suspension, then revocation.",
    ],
    "vocab": [
        ["Trade name", "A name filed with the department that a firm may advertise under."],
        ["Listing firm", "The only firm that may advertise a property without consent."],
        ["Finder's fee", "A referral payment; unlicensed people may not receive one."],
        ["2025 Wis. Act 69", "The act whose compensation and AI rules begin 1 January 2027."],
    ],
    "examples": [],
}

STUDY["wi/disclosures"] = {
    "summary": "Thirteen items. The real estate condition report drives this topic, and the rescission right attached to it is the number worth memorising.",
    "sections": [
        {"h": "The real estate condition report (ch. 709)",
         "l": ["The OWNER must furnish the prospective buyer a COMPLETED report NOT LATER THAN 10 DAYS AFTER ACCEPTANCE of a contract of sale or option contract.",
               "A buyer who does NOT receive the report within those 10 days may, WITHIN 2 BUSINESS DAYS after the end of the 10-day period, RESCIND by delivering WRITTEN NOTICE of rescission to the owner or the owner's agent, and is entitled to the RETURN OF ANY DEPOSITS OR OPTION FEES paid.",
               "The report is COMPLETE only if the owner answered, or supplied the substitute information allowed by s. 709.035, for EVERY ITEM.",
               "The owner may SUBSTITUTE written information supplied by a licensed engineer, a professional land surveyor, a structural pest control operator, a qualified third party, a contractor within their occupation, or a public agency, as long as it is furnished on time and the entry it relates to is identified.",
               "For a CONDOMINIUM UNIT the owner must add an ADDENDUM at the same time, giving the condominium's name and creation date, the unit number, the seller or agent's contact details, and the association's name and address, whether it is SELF-MANAGED or has hired management, and a contact individual (s. 709.02(2))."],
         "check": [("The owner must furnish a Wisconsin real estate condition report:", "Not later than 10 days after acceptance of the contract", ["Before the offer is written", "At closing"], "s. 709.02(1)."),
                   ("A buyer who never receives the report may rescind within:", "2 business days after the end of the 10-day period", ["10 days after closing", "72 hours of the offer"], "s. 709.02(1)."),
                   ("On rescission the buyer is entitled to:", "The return of any deposits or option fees paid", ["Damages", "Specific performance"], "s. 709.02(1)."),
                   ("A condominium seller must also supply:", "An addendum naming the association and whether it is self-managed", ["A reserve study", "An appraisal"], "s. 709.02(2).")]},
        {"h": "What a licensee need NOT disclose (s. 452.23(2))",
         "l": ["That the property was the SITE OF A SPECIFIC ACT OR OCCURRENCE, if it had NO EFFECT ON THE PHYSICAL CONDITION of the property or its structures.",
               "Information about the PHYSICAL CONDITION or the transaction that is already in a WRITTEN REPORT PREPARED BY A QUALIFIED THIRD PARTY and provided to the person - a governmental agency, or anyone the licensee or a party reasonably believes has the expertise to meet industry standards for that kind of inspection.",
               "The LOCATION of an adult family home, community-based residential facility or nursing home relative to the property.",
               "Sex offender registry information, except as s. 452.24 requires.",
               "BUT a licensee MUST disclose any facts they know that CONTRADICT the third-party report (s. 452.23(3)), and must exercise the care of a reasonably prudent person with the knowledge, skills and training required for licensure (s. 452.23(4)).",
               "No licensee may disclose information whose disclosure would be UNLAWFUL DISCRIMINATION under s. 106.50 or the federal handicap provisions (s. 452.23(1)).",
               "A licensee who in GOOD FAITH passes on information attributable to a state or local governmental or quasi-governmental body may not be held civilly liable if it turns out to be inaccurate, unless they knew it was - and good faith is PRESUMED (s. 452.23(5))."],
         "check": [("A licensee need not disclose an event at the property if it:", "Had no effect on the physical condition of the property", ["Happened over 5 years ago", "Was never reported"], "s. 452.23(2)(a)."),
                   ("A third-party inspection report relieves disclosure, except:", "Where the licensee knows facts that contradict the report", ["Never", "Only for structural items"], "s. 452.23(2)(b), (3)."),
                   ("The location of a nearby community-based residential facility:", "Need not be disclosed", ["Must always be disclosed", "Must be disclosed on request"], "s. 452.23(2)(c)."),
                   ("Passing on inaccurate information from a government agency in good faith:", "Carries no civil liability, and good faith is presumed", ["Is always actionable", "Requires a written waiver"], "s. 452.23(5).")]},
        {"h": "The sex offender registry (s. 452.24)",
         "l": ["If a person the licensee is serving ASKS for information about whether someone must register as a sex offender, or about the registry generally, the licensee HAS A DUTY TO DISCLOSE such information IF THE LICENSEE HAS ACTUAL KNOWLEDGE of it.",
               "The licensee is IMMUNE from liability for any act or omission related to that disclosure if they TIMELY give the person WRITTEN NOTICE that the person may obtain registry information from the DEPARTMENT OF CORRECTIONS - the notice must include the department's TELEPHONE NUMBER AND INTERNET SITE."],
         "check": [("A Wisconsin licensee asked about the sex offender registry:", "Must disclose what they have actual knowledge of", ["Must refuse to answer", "Must run a search"], "s. 452.24(1)."),
                   ("Immunity attaches if the licensee timely provides:", "Written notice that the person may get the information from the Department of Corrections, with its phone number and website", ["An oral referral", "A copy of the registry"], "s. 452.24(2).")]},
        {"h": "Material adverse facts and environment",
         "l": ["An ADVERSE FACT is a condition or occurrence a competent licensee generally recognises as SIGNIFICANTLY AND ADVERSELY AFFECTING THE VALUE of the property, SIGNIFICANTLY REDUCING THE STRUCTURAL INTEGRITY of improvements, or PRESENTING A SIGNIFICANT HEALTH RISK to occupants - or information showing a PARTY CANNOT OR DOES NOT INTEND TO MEET their obligations (s. 452.01(1e)).",
               "The outline's environmental items include ASBESTOS and UNDERGROUND STORAGE TANKS, and the Board's own education rule points licensees at underground storage tanks under ch. ATCP 93, FLOODPLAINS under s. 87.30, WETLANDS under s. 23.32 and FARMLAND PRESERVATION under ss. 91.60 to 91.70 (REEB 25.028(2)(g)).",
               "The FEDERAL LEAD-BASED PAINT disclosure law applies to target housing built before 1978, and condominium disclosure requirements sit alongside the condition report addendum."],
         "check": [("An adverse fact includes information that:", "A party is unable or does not intend to meet their contract obligations", ["The property is overpriced", "The buyer is slow to respond"], "s. 452.01(1e)(b)."),
                   ("A condition presenting a significant health risk to occupants is:", "An adverse fact", ["Immaterial unless structural", "Only relevant to lenders"], "s. 452.01(1e)(a)(3)."),
                   ("Federal lead-based paint disclosure applies to housing built:", "Before 1978", ["Before 1950", "Before 1992"], "Federal law; named on the Wisconsin outline.")]},
    ],
    "traps": [
        "10 days to deliver the report; 2 BUSINESS days after that window to rescind.",
        "A third-party report shields you - unless you know something that contradicts it.",
        "You answer registry questions from actual knowledge, and get immunity by pointing to Corrections in writing.",
    ],
    "vocab": [
        ["Condition report", "The owner's completed ch. 709 disclosure of the property's condition."],
        ["Qualified 3rd party", "An agency or expert whose written report relieves the licensee."],
        ["Adverse fact", "The statutory definition driving material adverse fact disclosure."],
        ["Rescission", "The buyer's written cancellation and return of deposits."],
    ],
    "examples": [
        {"t": "No report arrives",
         "s": "An offer is accepted on 1 March. No condition report has arrived by 11 March.",
         "w": ["The owner's 10 days expired on 11 March.",
               "The buyer then has 2 business days to deliver written notice of rescission.",
               "On rescission the buyer gets back deposits and option fees."],
         "k": "The clock is 10 days, then 2 business days - and the notice must be in writing."},
    ],
}

STUDY["wi/misc"] = {
    "summary": "Twelve items on where the money sits and who is responsible. Wisconsin's trust account is unusual: it is an INTEREST-BEARING COMMON account and the interest belongs to the state.",
    "sections": [
        {"h": "Trust accounts (s. 452.13)",
         "l": ["CLIENT FUNDS are all DOWNPAYMENTS, EARNEST MONEY DEPOSITS or other money related to a conveyance of real estate received by a licensee on behalf of a firm or any other person. PROMISSORY NOTES ARE NOT client funds.",
               "A firm that HOLDS client funds must establish an INTEREST-BEARING COMMON TRUST ACCOUNT in a DEPOSITORY INSTITUTION - a bank, savings bank, savings and loan association or credit union authorised to do business in Wisconsin and federally insured.",
               "The account must earn interest at a rate NOT LESS THAN that for individual accounts of the same type, size and duration from which withdrawals can be made without delay.",
               "The firm must REGISTER the institution's name and address and the account number with the department, NOTIFY it of changes, and furnish a LETTER AUTHORISING the department and the Department of Administration to EXAMINE AND AUDIT the account whenever either considers it necessary.",
               "ALL client funds go into that account, and the DEPARTMENT OF ADMINISTRATION is the BENEFICIAL OWNER of the interest, minus service charges. The institution remits the interest ANNUALLY BEFORE 1 FEBRUARY, and need not remit at all if the total for the period is LESS THAN $10 before charges.",
               "A trust account is OPTIONAL in the sense that the section does not require a firm to hold client funds, nor require anyone to transfer client funds to a firm (s. 452.13(4))."],
         "check": [("Wisconsin client funds go into:", "An interest-bearing common trust account at an insured depository institution", ["A non-interest-bearing account", "The firm's operating account"], "s. 452.13(2)(a), (c)."),
                   ("Who is the beneficial owner of the interest?", "The Department of Administration", ["The firm", "The buyer", "The seller"], "s. 452.13(2)(d)."),
                   ("Which is NOT client funds?", "A promissory note", ["An earnest money deposit", "A downpayment"], "s. 452.13(1)(a)."),
                   ("Interest must be remitted:", "Annually, before 1 February", ["Monthly", "At each closing"], "s. 452.13(2)(e)(1)."),
                   ("The firm must give the department:", "A letter authorising examination and audit of the trust account", ["A surety bond", "Monthly statements"], "s. 452.13(2)(b)(3).")]},
        {"h": "Responsibilities of firms and licensees",
         "l": ["A FIRM is responsible for brokerage services provided on its behalf by an associated licensee ONLY TO THE EXTENT that the firm FAILED TO COMPLY with s. 452.132 and the supervision rules as to that licensee (s. 452.12(3)).",
               "A firm may NOT be held civilly liable for NEGLIGENT HIRING where a licensee commits a crime or other wrongful act, if the firm relied on the department's investigations under s. 440.03(13) or on a Board determination - WHETHER OR NOT the firm did its own investigation (s. 452.139(3)).",
               "A broker's licence may be issued to a BUSINESS ENTITY that has at least one BUSINESS REPRESENTATIVE licensed as a broker. A broker may be a business representative for MORE THAN ONE entity with each entity's EXPRESS WRITTEN CONSENT, and a change of business representative must be REPORTED WITHIN 30 DAYS (s. 452.12(2)).",
               "If a FIRM'S licence is not renewed, the firm and every licensee associated with it may not act under that licence, and the business representative must notify each licensee and, WITHIN 10 DAYS of notifying them, file a NOTICE OF TERMINATION for each (s. 452.12(5)(bm))."],
         "check": [("A Wisconsin firm is liable for an associated licensee's brokerage services:", "Only to the extent the firm failed to comply with its supervision duties", ["Always, without limit", "Never"], "s. 452.12(3)."),
                   ("A change in a business entity's business representatives must be reported within:", "30 days of the effective date", ["10 days", "At renewal"], "s. 452.12(2)(c)."),
                   ("If the firm's licence lapses, the business representative must file notices of termination within:", "10 days after notifying the licensees", ["30 days", "Immediately"], "s. 452.12(5)(bm)(3)."),
                   ("A firm relying on the department's investigation of a licensee:", "Cannot be held liable for negligent hiring, even if it did no investigation of its own", ["Must still investigate independently", "Is strictly liable"], "s. 452.139(3).")]},
        {"h": "Transfer fee and marital property",
         "l": ["The REAL ESTATE TRANSFER FEE is imposed on the GRANTOR at 30 CENTS FOR EACH $100 OF VALUE or fraction of $100, on every conveyance not exempt. On a LAND CONTRACT the value is the TOTAL PRINCIPAL the buyer agrees to pay (s. 77.22(1)).",
               "The REGISTER OF DEEDS collects it when the instrument is submitted for recording, and both a completed TRANSFER RETURN - signed by BOTH grantor and grantee - and payment are PREREQUISITES TO RECORDING. The register has NO DUTY to determine the correct value or the validity of a claimed exemption, and an exemption must be stated on the face of the conveyance by reference to the subsection of s. 77.25.",
               "MARITAL PROPERTY: all property of spouses IS marital property unless classified otherwise, all property of spouses is PRESUMED marital, and each spouse has a PRESENT UNDIVIDED ONE-HALF INTEREST in each item of marital property (s. 766.31(1) to (3))."],
         "check": [("The Wisconsin real estate transfer fee is:", "30 cents per $100 of value or fraction of $100, paid by the grantor", ["$3.75 per $500, paid by the seller", "1% of value, paid by the buyer"], "s. 77.22(1)."),
                   ("The transfer return must be signed by:", "Both the grantor and the grantee", ["The grantor only", "The register of deeds"], "s. 77.22(1)."),
                   ("On a land contract the taxable value is:", "The total principal the buyer agrees to pay", ["The downpayment", "The assessed value"], "s. 77.22(1)."),
                   ("Each spouse's interest in an item of marital property is:", "A present undivided one-half interest", ["A survivorship interest only", "A one-third dower interest"], "s. 766.31(3)."),
                   ("Property of Wisconsin spouses is:", "Presumed to be marital property", ["Presumed individual", "Classified only at divorce"], "s. 766.31(2).")]},
    ],
    "traps": [
        "The trust account is INTEREST-BEARING and the interest goes to the Department of Administration.",
        "Promissory notes are not client funds.",
        "30 cents per $100 - and the GRANTOR pays.",
        "Spouses hold a present undivided one-half interest, not a future one.",
    ],
    "vocab": [
        ["Client funds", "Downpayments and earnest money, but not promissory notes."],
        ["Common trust account", "The single interest-bearing account holding all client funds."],
        ["Business representative", "The licensed broker through whom an entity acts."],
        ["Transfer return", "The form both parties sign before a deed may be recorded."],
        ["Marital property", "The default classification of all property of Wisconsin spouses."],
    ],
    "examples": [
        {"t": "Transfer fee on a $280,000 sale",
         "s": "Work out the Wisconsin real estate transfer fee.",
         "w": ["$280,000 / $100 = 2,800 increments.",
               "2,800 x $0.30 = $840.",
               "The grantor pays it, and the register of deeds collects it at recording."],
         "k": "Divide by 100, multiply by 0.30, and round any fraction of $100 up."},
    ],
}

STUDY["wi/fair-housing"] = {
    "summary": "Six items. Wisconsin's open housing law protects several classes the federal Act does not, and the penalty for breaking it is the harshest in the licence law.",
    "sections": [
        {"h": "Wisconsin's protected classes (s. 106.50(1))",
         "p": ["Wisconsin's declared policy is equal opportunity for housing regardless of:"],
         "l": ["SEX", "RACE", "COLOR", "SEXUAL ORIENTATION", "DISABILITY",
               "RELIGION", "NATIONAL ORIGIN", "MARITAL STATUS", "FAMILY STATUS",
               "STATUS AS A VICTIM OF DOMESTIC ABUSE, SEXUAL ASSAULT OR STALKING",
               "LAWFUL SOURCE OF INCOME", "AGE", "ANCESTRY",
               "'AGE', for a member of a protected class, means AT LEAST 18 YEARS OF AGE (s. 106.50(1m)(am)).",
               "The statute also makes it the duty of POLITICAL SUBDIVISIONS to help prevent and remove housing discrimination, so LOCAL EQUAL OPPORTUNITY ordinances sit on top of the state law."],
         "check": [("Which is protected by Wisconsin's open housing law but not the federal Fair Housing Act?", "Lawful source of income", ["Race", "Religion", "National origin"], "s. 106.50(1)."),
                   ("Wisconsin also protects:", "Status as a victim of domestic abuse, sexual assault or stalking", ["Credit history", "Occupation"], "s. 106.50(1)."),
                   ("'Age' as a Wisconsin protected class means:", "At least 18 years of age", ["Over 40", "Any age"], "s. 106.50(1m)(am)."),
                   ("Marital status and ancestry are:", "Protected classes in Wisconsin housing", ["Federal classes only", "Not protected anywhere"], "s. 106.50(1).")]},
        {"h": "The prohibited acts (s. 106.50(2))",
         "l": ["Refusing to SELL, RENT, FINANCE OR CONTRACT TO CONSTRUCT housing, or refusing to NEGOTIATE OR DISCUSS the terms.",
               "Refusing to permit INSPECTION, or exacting DIFFERENT OR MORE STRINGENT price, terms or conditions.",
               "Refusing to finance or sell an UNIMPROVED RESIDENTIAL LOT or to build a home on one.",
               "ADVERTISING in a manner that indicates discrimination by a preference or limitation.",
               "For an insurer, refusing or varying a HAZARD INSURANCE contract on a dwelling.",
               "Refusing to RENEW A LEASE, causing an EVICTION, or HARASSING a tenant.",
               "Discriminating in the PRIVILEGES, SERVICES OR FACILITIES available with housing.",
               "FALSELY REPRESENTING that housing is unavailable for inspection, rental or sale.",
               "Denying ACCESS TO OR MEMBERSHIP IN a multiple listing service or other real estate service.",
               "COERCING, INTIMIDATING, THREATENING OR INTERFERING with a person exercising a right under the section, or with someone who aided another in doing so."],
         "check": [("Telling a caller a vacant flat is taken when it is not is:", "A false representation of unavailability, and unlawful", ["Lawful puffing", "A listing error only"], "s. 106.50(2)(h)."),
                   ("Denying a licensee membership in an MLS on a protected ground is:", "Unlawful discrimination", ["An internal MLS matter", "Lawful if voted on"], "s. 106.50(2)(i)."),
                   ("Harassing a tenant or causing an eviction on a protected ground is:", "Unlawful", ["Lawful if the lease allows it", "A landlord-tenant matter only"], "s. 106.50(2)(f)."),
                   ("Refusing to finance an unimproved residential lot on a protected ground is:", "Unlawful", ["Outside the open housing law", "A lending matter only"], "s. 106.50(2)(c).")]},
        {"h": "Consequences for a licensee",
         "l": ["A licensee MAY NOT DISCLOSE information whose disclosure would be unlawful discrimination under s. 106.50 or unlawful handicap discrimination under 42 USC 3604, 3605, 3606 or 3617 (s. 452.23(1)).",
               "For a discrimination violation the Board SHALL suspend the licence for NOT LESS THAN 90 DAYS on the FIRST offence and SHALL REVOKE it on the SECOND. That penalty may be imposed IN ADDITION to any other penalty under ch. 452, s. 66.1011 or s. 106.50 (s. 452.17(4)).",
               "The outline also covers providing AUXILIARY SERVICES FOR THE DISABLED under the Americans with Disabilities Act."],
         "check": [("A first discrimination violation by a Wisconsin licensee brings:", "Suspension of not less than 90 days", ["A written warning", "A $500 forfeiture", "Immediate revocation"], "s. 452.17(4)(a)(1)."),
                   ("A second brings:", "Revocation", ["A 180-day suspension", "A fine"], "s. 452.17(4)(a)(2)."),
                   ("A licensee asked a question whose answer would be unlawful discrimination must:", "Not disclose the information", ["Answer honestly", "Refer the question to the seller"], "s. 452.23(1).")]},
    ],
    "traps": [
        "Lawful source of income, victim status, marital status and ancestry are the Wisconsin additions.",
        "'Age' here means 18 or over, not a senior category.",
        "90 days minimum then revocation - the discipline is mandatory, not discretionary.",
    ],
    "vocab": [
        ["Open housing law", "Wisconsin's fair housing statute, s. 106.50."],
        ["Lawful source of income", "A Wisconsin protected class covering vouchers and benefits."],
        ["Family status", "A Wisconsin protected class covering households with children."],
        ["Conciliation", "The informal resolution of a housing discrimination complaint."],
    ],
    "examples": [],
}


# ------------------------------------------------------------- questions

Q = [
 # agency
 ("wi/agency", "Duties to parties", 1, "In Wisconsin, the duty to keep a party's information confidential:",
  "Continues after the transaction is complete and after the firm stops providing services", ["Ends at closing", "Applies only to clients", "Ends when the listing expires"],
  "s. 452.133(1)(d)."),
 ("wi/agency", "Duties to parties", 1, "A material adverse fact known to the firm must be disclosed:",
  "Timely and in writing, unless disclosure is prohibited by law", ["Orally at the showing", "Only if the party asks", "Only to clients"],
  "s. 452.133(1)(c)."),
 ("wi/agency", "Duties to parties", 2, "When negotiating, a Wisconsin firm must present contract proposals:",
  "In an objective and unbiased manner, disclosing the advantages and disadvantages", ["In the light most favourable to its client", "Without any comment"],
  "s. 452.133(1)(g)."),
 ("wi/agency", "Duties to parties", 2, "Accurate information about market conditions is owed to:",
  "Any party who requests it, within a reasonable time", ["Clients only", "The listing firm only"],
  "s. 452.133(1)(e)."),
 ("wi/agency", "Duties to parties", 2, "The duty to provide brokerage services with reasonable skill and care is owed to:",
  "Every party the firm provides brokerage services to", ["Clients only", "Buyers only"],
  "s. 452.133(1)(b)."),
 ("wi/agency", "Duties to clients", 1, "Loyal representation in Wisconsin requires placing the client's interests ahead of:",
  "The firm's own interests and the interests of non-clients in the transaction", ["Only the other party's interests", "Nothing in particular"],
  "s. 452.133(2)(a)."),
 ("wi/agency", "Duties to clients", 1, "A Wisconsin agency agreement must be:",
  "A written agreement between a firm and a client", ["Oral if witnessed", "Implied from conduct", "Filed with the Board"],
  "s. 452.01(1m)."),
 ("wi/agency", "Duties to clients", 2, "The duty to negotiate is owed:",
  "To the firm's client", ["To every party", "To the cooperating firm"],
  "s. 452.133(2)(d)."),
 ("wi/agency", "Duties to clients", 3, "A firm must disclose to its client information material to the transaction, except:",
  "Confidential information and information whose disclosure is prohibited by law", ["Anything unfavourable to the client", "Price information"],
  "s. 452.133(2)(b)."),
 ("wi/agency", "Negotiating", 1, "A Wisconsin firm may negotiate on behalf of a party only where that party is:",
  "The firm's client, or a client of a principal firm that engaged the firm as a subagent", ["Anyone the firm is working with", "Anyone who signed a disclosure"],
  "s. 452.134(1)(b)."),
 ("wi/agency", "Negotiating", 2, "May a firm provide brokerage services to someone with no agency agreement?",
  "Yes, but it may not negotiate on that person's behalf", ["No, never", "Yes, with full client duties"],
  "s. 452.134(1)."),
 ("wi/agency", "Multiple representation", 1, "A multiple representation relationship requires:",
  "The written consent of all of the firm's clients in the relationship", ["Oral consent from one client", "Board approval", "Nothing"],
  "s. 452.134(2)."),
 ("wi/agency", "Designated agency", 1, "Designated agency in Wisconsin requires:",
  "The written consent of all the firm's clients in the multiple representation relationship", ["The broker's decision", "Consent from the seller only"],
  "s. 452.134(3)(a)."),
 ("wi/agency", "Designated agency", 2, "A client may withdraw consent to designated agency:",
  "At any time, by written notice to the firm", ["Only before an offer is written", "Not once an offer is accepted", "Never"],
  "s. 452.134(3)(a)."),
 ("wi/agency", "Designated agency", 2, "With designated agency in place, the negotiating licensee may give their client advice:",
  "Even if it places one of the firm's clients ahead of another", ["Only if it is neutral between the clients", "Only in writing"],
  "s. 452.134(3)(b)."),
 ("wi/agency", "Designated agency", 2, "In a multiple representation relationship WITHOUT designated agency, the firm:",
  "May not place any client's interests ahead of any other client's", ["Favours the seller", "Favours the first client signed"],
  "s. 452.134(4)."),
 ("wi/agency", "Subagency", 2, "A subagent owes the principal firm's clients:",
  "Only the duties owed to all parties, not the client duties", ["Full client duties", "No duties at all"],
  "s. 452.133(4)(a)."),
 ("wi/agency", "Subagency", 3, "A subagent may not:",
  "Give advice contrary to the principal firm's clients' interests, unless required by law", ["Work with a buyer", "Show the property"],
  "s. 452.133(4)(b)(2)."),
 ("wi/agency", "Disclosure", 1, "The Disclosure to Clients must be provided:",
  "Not later than the time the firm enters into the agency agreement", ["At the first showing", "Before closing", "With the offer"],
  "s. 452.135(2)(a)."),
 ("wi/agency", "Disclosure", 1, "The Disclosure to Customers must be provided before the firm:",
  "Negotiates on behalf of a party who is not the firm's client", ["Answers any question", "Takes a listing"],
  "s. 452.135(1)(a)."),
 ("wi/agency", "Disclosure", 3, "The statute describes the Disclosure to Customers as:",
  "A plain-language summary of the duties owed to a customer under s. 452.133(1)", ["A binding contract", "A warranty of condition"],
  "s. 452.135(1)(a)."),
 ("wi/agency", "Prohibited conduct", 1, "A licensee buying a listed property personally must obtain the parties' written consent:",
  "In the offer to purchase, option, lease or other transaction contract", ["In a separate side letter", "Orally before writing"],
  "s. 452.133(3)(b)."),
 ("wi/agency", "Prohibited conduct", 2, "Recommending a service provider who pays the licensee a referral fee requires:",
  "Written disclosure of the compensation or the interest", ["Nothing if the provider is licensed", "Oral consent"],
  "s. 452.133(3)(c)."),
 ("wi/agency", "Prohibited conduct", 2, "Accepting compensation from someone other than the licensee's client or firm requires:",
  "The prior written consent of all parties to the transaction", ["The payer's consent only", "Nothing at all"],
  "s. 452.133(3)(a)."),
 ("wi/agency", "Prohibited conduct", 3, "A licensee acting in a transaction for an entity in which they hold an interest:",
  "Needs the prior written consent of all parties", ["May proceed without disclosure", "Is barred outright"],
  "s. 452.133(3)(b)."),
 ("wi/agency", "Common law", 2, "Under Wisconsin law, ch. 452 duties:",
  "Supersede common law duties to the extent the common law is inconsistent", ["Supplement common law in all cases", "Have no effect on common law"],
  "s. 452.139(1)."),
 ("wi/agency", "Common law", 2, "A client is liable for a firm's misrepresentation:",
  "Only if the client knew or should have known, or the firm repeated the client's own misrepresentation", ["Always", "Never"],
  "s. 452.139(2)(a)."),
 ("wi/agency", "Adverse facts", 2, "Which is an adverse fact under Wisconsin law?",
  "Information showing a party is unable or does not intend to meet their contract obligations", ["A high asking price", "A slow-responding buyer"],
  "s. 452.01(1e)(b)."),
 ("wi/agency", "Adverse facts", 3, "A condition that significantly reduces the structural integrity of improvements is:",
  "An adverse fact", ["Only relevant to the appraiser", "Immaterial unless visible"],
  "s. 452.01(1e)(a)(2)."),
 ("wi/agency", "Licensee duties", 3, "A firm's duties to a party:",
  "Extend to each licensee associated with the firm who provides brokerage services to that party", ["Stop at the firm", "Apply only to the supervising broker"],
  "s. 452.133(4m)(a), (d)."),
 ("wi/agency", "Trust funds", 2, "The duty to safeguard trust funds and other property held is owed to:",
  "Every party the firm provides brokerage services to", ["Clients only", "The Board only"],
  "s. 452.133(1)(f)."),
 ("wi/agency", "Duties to clients", 3, "On request, a firm must give its client information and advice on matters material to the transaction that are:",
  "Within the knowledge, skills and training required for licensure", ["Of any kind, including legal advice", "Limited to the asking price"],
  "s. 452.133(2)(am)."),

 # contracts
 ("wi/contracts", "Forms", 1, "A Wisconsin licensee may:",
  "Give a general explanation of an approved form's provisions when completing or delivering it", ["Advise on the legal effect of a specific contract", "Give an opinion on the state of title"],
  "s. 452.40(2)."),
 ("wi/contracts", "Forms", 1, "A licensee may NOT provide advice or opinions about:",
  "The legal rights or obligations of the parties", ["Current market conditions", "The condition of the roof"],
  "s. 452.40(2)."),
 ("wi/contracts", "Forms", 2, "'Use a form' in Wisconsin means:",
  "Completing it by filling in blanks or modifying printed provisions at a party's instruction in a specific transaction", ["Drafting a new form", "Reading the form aloud"],
  "s. 452.40(1)(a)."),
 ("wi/contracts", "Forms", 3, "A supervising broker's pre-closing review is:",
  "Not the provision of legal advice or opinion", ["Unauthorised practice of law", "Required to be done by an attorney"],
  "s. 452.40(2)."),
 ("wi/contracts", "WB forms", 1, "Which form changes an accepted offer by agreement of both parties?",
  "WB-40 Amendment to Offer to Purchase", ["WB-41 Notice Relating to Offer to Purchase", "WB-44 Counter-Offer", "WB-46 Multiple Counter Proposal"],
  "An amendment is bilateral; a notice is unilateral."),
 ("wi/contracts", "WB forms", 1, "The buyer agency and tenant representation agreement is:",
  "WB-36", ["WB-11", "WB-1", "WB-13"],
  "Named on the Wisconsin salesperson content outline."),
 ("wi/contracts", "WB forms", 2, "A vacant land purchase uses:",
  "WB-13", ["WB-11", "WB-14", "WB-4"],
  "Named on the Wisconsin salesperson content outline."),
 ("wi/contracts", "WB forms", 2, "The residential condominium listing contract is:",
  "WB-4", ["WB-1", "WB-14", "WB-36"],
  "Named on the Wisconsin salesperson content outline."),
 ("wi/contracts", "WB forms", 2, "A party exercising a right the contract already gives them delivers:",
  "A WB-41 Notice Relating to Offer to Purchase", ["A WB-40 Amendment", "A WB-44 Counter-Offer"],
  "A notice is unilateral; an amendment needs both parties."),
 ("wi/contracts", "WB forms", 3, "A seller responding to several offers at once may use:",
  "WB-46 Multiple Counter Proposal", ["WB-44 Counter-Offer only", "WB-40 Amendment"],
  "Named on the Wisconsin salesperson content outline."),
 ("wi/contracts", "Supervision", 1, "A Wisconsin supervising broker must review, before closing:",
  "Executed documents, transaction records, and the trust account records for the transaction", ["Only the offer to purchase", "Only the commission statement"],
  "s. 452.132(4)(a)."),
 ("wi/contracts", "Supervision", 2, "That review is limited to confirming the disclosure statement was given, that approved forms were used and completed consistently, and:",
  "Communicating errors apparent on the face of the document and known to the reviewer", ["Rewriting the contract", "Approving the price"],
  "s. 452.132(4)(b)."),
 ("wi/contracts", "Supervision", 2, "When an error is communicated to the licensee:",
  "The licensee discusses it with the party, who decides whether to request changes", ["The broker amends the document", "The transaction is voided"],
  "s. 452.132(6)(a)."),
 ("wi/contracts", "Supervision", 2, "A licensed broker business entity must delegate supervision to:",
  "A supervising broker who is a licensed individual broker, by a signed written delegation", ["Any associated salesperson", "The Board"],
  "s. 452.132(5)(a), (c)."),
 ("wi/contracts", "Supervision", 3, "A firm may delegate the duty to supervise:",
  "To more than one supervising broker", ["To only one person", "Only to an attorney"],
  "s. 452.132(5)(d)."),
 ("wi/contracts", "Supervision", 3, "A firm that is not a licensed broker business entity and names no supervising broker:",
  "Is itself deemed to be the supervising broker", ["Has no supervision duty", "Must close"],
  "s. 452.132(5)(b)."),
 ("wi/contracts", "Records", 1, "A licensee must submit executed agreements, offers and leases to the firm:",
  "In a timely manner", ["Within 30 days", "Only on request"],
  "s. 452.132(6)(b)."),
 ("wi/contracts", "Records", 2, "Transaction records in Wisconsin:",
  "May be retained in electronic file format", ["Must be kept on paper", "Must be filed with the Board"],
  "s. 452.42(2)."),
 ("wi/contracts", "Records", 2, "Custody and safety of transaction documents submitted to the firm is the responsibility of:",
  "The firm", ["The individual licensee", "The closing agent"],
  "s. 452.132(3)."),
 ("wi/contracts", "Firm procedures", 2, "A firm must give each associated licensee:",
  "A written statement of the firm's procedures for handling leases, agency agreements, offers, documents and records", ["A copy of the Board's register", "A commission schedule"],
  "s. 452.132(2)(a)."),
 ("wi/contracts", "Firm procedures", 3, "Before a licensee becomes associated, and at the start of each biennial licensure period, the firm must:",
  "Ensure the licensee holds a valid licence", ["Re-examine the licensee", "Notify the Board"],
  "s. 452.132(2)(c)."),
 ("wi/contracts", "Firm procedures", 3, "A firm must tell each associated licensee:",
  "Where to obtain the Board's rules on conduct, ethical practices and responsibilities", ["The Board's enforcement statistics", "The firm's tax identification number"],
  "s. 452.132(2)(b)."),

 # ethics
 ("wi/ethics", "Advertising", 1, "All Wisconsin licensee advertising must clearly indicate that:",
  "The firm is a business enterprise and not a private party", ["The licensee owns the property", "The price is negotiable"],
  "s. 452.136(2)(a)."),
 ("wi/ethics", "Advertising", 1, "A firm may advertise a property it did not list:",
  "Only with the listing firm's consent", ["Freely", "Never under any circumstances"],
  "s. 452.136(3)."),
 ("wi/ethics", "Advertising", 2, "A licensee advertising the occasional sale of their own property without the firm name must:",
  "Clearly identify themselves as a real estate licensee", ["Obtain Board approval", "Use the firm name anyway"],
  "s. 452.136(2)(c)."),
 ("wi/ethics", "Advertising", 2, "Advertising a price other than the one agreed with the owner is:",
  "Prohibited, though a range reflecting the agreed price is allowed", ["Allowed to generate interest", "Allowed if below the agreed price"],
  "s. 452.136(4)."),
 ("wi/ethics", "Advertising", 2, "An associated licensee must advertise:",
  "Under the supervision of and in the name of the firm, clearly and conspicuously", ["In the licensee's own name", "In the seller's name"],
  "s. 452.136(2)(b)."),
 ("wi/ethics", "Compensation", 1, "Under Wisconsin law in force now, a licensee associated with a firm must have all commissions paid to:",
  "The firm", ["The licensee personally", "An escrow agent", "The client"],
  "s. 452.19(1m)(b)."),
 ("wi/ethics", "Compensation", 1, "Paying a finder's fee to an unlicensed neighbour is:",
  "Prohibited", ["Allowed under $500", "Allowed with written disclosure"],
  "s. 452.19(1m)(a)."),
 ("wi/ethics", "Compensation", 2, "A referral fee may be paid to an out-of-state broker who:",
  "Is regularly and lawfully engaged in the brokerage business in that state", ["Has any licence of any kind", "Is a friend of the firm"],
  "s. 452.19(1m)(a)."),
 ("wi/ethics", "2027 changes", 2, "From 1 January 2027, firm-to-firm compensation in a one-to-four unit residential sale will be:",
  "Prohibited, and any agreement to pay it void and unenforceable", ["Capped at 3%", "Allowed with the parties' written consent"],
  "s. 452.19(3), created by 2025 Wis. Act 69."),
 ("wi/ethics", "2027 changes", 2, "From 1 January 2027, a seller's agreement to pay a firm that is not the listing firm must be:",
  "Expressly stated in the fully executed offer or option and signed by buyer and seller", ["In the listing contract alone", "Published in the MLS"],
  "s. 452.19(4)(a)."),
 ("wi/ethics", "2027 changes", 3, "From 1 January 2027, a listing contract must state whether the seller:",
  "Authorises the listing firm to disclose that compensation is offered to another firm", ["Will pay the buyer's closing costs", "Will accept a land contract"],
  "s. 452.19(4)(d)."),
 ("wi/ethics", "2027 changes", 3, "From 1 January 2027, advertising altered using artificial intelligence so as to mislead about the property must be:",
  "Disclosed in the advertising", ["Removed from the MLS", "Reported to DSPS"],
  "s. 452.136(1m), created by 2025 Wis. Act 69."),
 ("wi/ethics", "Penalties", 1, "Practising real estate in Wisconsin without a licence carries a maximum of:",
  "A $5,000 fine or 6 months' imprisonment or both", ["A $1,000 fine", "A $10,000 fine", "A civil forfeiture only"],
  "s. 452.17(1)."),
 ("wi/ethics", "Penalties", 3, "An applicant convicted of a felony may ask the Board for a suitability determination once:",
  "The confinement is complete or they are released and 3 years have elapsed", ["One year has elapsed", "Five years have elapsed"],
  "s. 452.25(1)(b)."),

 # disclosures
 ("wi/disclosures", "Condition report", 1, "The owner must furnish a Wisconsin real estate condition report:",
  "Not later than 10 days after acceptance of the contract of sale or option contract", ["Before the offer is written", "At closing", "Within 30 days"],
  "s. 709.02(1)."),
 ("wi/disclosures", "Condition report", 1, "A buyer who does not receive the report in time may rescind within:",
  "2 business days after the end of the 10-day period", ["10 days after closing", "72 hours of the offer", "5 business days"],
  "s. 709.02(1)."),
 ("wi/disclosures", "Condition report", 2, "On a valid rescission the buyer is entitled to:",
  "The return of any deposits or option fees paid", ["Damages", "Specific performance", "A new report"],
  "s. 709.02(1)."),
 ("wi/disclosures", "Condition report", 2, "A condition report is complete only if the owner:",
  "Answered, or supplied substitute information for, every item", ["Signed it", "Had it notarised"],
  "s. 709.02(1)."),
 ("wi/disclosures", "Condition report", 3, "A condominium seller must also supply, at the same time:",
  "An addendum naming the association and saying whether it is self-managed", ["A reserve study", "An appraisal", "A title commitment"],
  "s. 709.02(2)."),
 ("wi/disclosures", "No duty", 1, "A licensee need not disclose an act or occurrence at the property if it:",
  "Had no effect on the physical condition of the property or its structures", ["Happened more than 5 years ago", "Was not reported to police"],
  "s. 452.23(2)(a)."),
 ("wi/disclosures", "No duty", 2, "A qualified third party's written report relieves the licensee of disclosure, except:",
  "Where the licensee knows facts that contradict the report", ["Never", "Only for structural matters"],
  "s. 452.23(2)(b), (3)."),
 ("wi/disclosures", "No duty", 2, "The location of a nearby community-based residential facility:",
  "Need not be disclosed", ["Must always be disclosed", "Must be disclosed on request"],
  "s. 452.23(2)(c)."),
 ("wi/disclosures", "Good faith", 3, "A licensee who in good faith passes on inaccurate information from a state agency:",
  "May not be held civilly liable, and good faith is presumed", ["Is strictly liable", "Must indemnify the buyer"],
  "s. 452.23(5)."),
 ("wi/disclosures", "Registry", 1, "Asked about the sex offender registry, a Wisconsin licensee:",
  "Must disclose information of which they have actual knowledge", ["Must refuse to answer", "Must run a registry search"],
  "s. 452.24(1)."),
 ("wi/disclosures", "Registry", 2, "The licensee gains immunity by timely providing:",
  "Written notice that the person may get registry information from the Department of Corrections, with its phone number and website", ["An oral referral", "A printed copy of the registry"],
  "s. 452.24(2)."),
 ("wi/disclosures", "Care", 2, "In making a disclosure a licensee must exercise:",
  "The care of a reasonably prudent person with the knowledge, skills and training required for licensure", ["The care of an engineer", "No particular standard"],
  "s. 452.23(4)."),
 ("wi/disclosures", "Lead paint", 2, "Federal lead-based paint disclosure applies to target housing built:",
  "Before 1978", ["Before 1950", "Before 1992", "Before 1985"],
  "Federal law; named on the Wisconsin salesperson outline."),

 # misc
 ("wi/misc", "Trust accounts", 1, "Wisconsin client funds must be held in:",
  "An interest-bearing common trust account at an insured depository institution", ["A non-interest-bearing trust account", "The firm's operating account"],
  "s. 452.13(2)(a), (c)."),
 ("wi/misc", "Trust accounts", 1, "The beneficial owner of the interest on a Wisconsin trust account is:",
  "The Department of Administration", ["The firm", "The buyer", "The seller"],
  "s. 452.13(2)(d)."),
 ("wi/misc", "Trust accounts", 2, "Which is NOT client funds in Wisconsin?",
  "A promissory note", ["An earnest money deposit", "A downpayment", "Other money related to a conveyance"],
  "s. 452.13(1)(a)."),
 ("wi/misc", "Trust accounts", 2, "Trust account interest must be remitted:",
  "Annually, before 1 February", ["Monthly", "At each closing", "On demand"],
  "s. 452.13(2)(e)(1)."),
 ("wi/misc", "Trust accounts", 2, "A firm maintaining a trust account must furnish the department:",
  "A letter authorising examination and audit of the account", ["A surety bond", "Quarterly statements"],
  "s. 452.13(2)(b)(3)."),
 ("wi/misc", "Trust accounts", 3, "An institution need not remit trust account interest for a period if the total is:",
  "Less than $10 before service charges", ["Less than $100", "Less than $1"],
  "s. 452.13(2)(e)(1)."),
 ("wi/misc", "Responsibility", 1, "A Wisconsin firm is responsible for an associated licensee's brokerage services:",
  "Only to the extent the firm failed to comply with its supervision obligations", ["Always and without limit", "Never"],
  "s. 452.12(3)."),
 ("wi/misc", "Responsibility", 2, "A change in a business entity's business representatives must be reported within:",
  "30 days after the effective date of the change", ["10 days", "At the next renewal", "Immediately"],
  "s. 452.12(2)(c)."),
 ("wi/misc", "Responsibility", 3, "If a firm's licence is not renewed, notices of termination must be filed within:",
  "10 days after notifying the associated licensees", ["30 days", "The same day"],
  "s. 452.12(5)(bm)(3)."),
 ("wi/misc", "Transfer fee", 1, "The Wisconsin real estate transfer fee is:",
  "30 cents per $100 of value or fraction of $100, imposed on the grantor", ["$3.75 per $500, paid by the seller", "1% of value, paid by the buyer", "30 cents per $500"],
  "s. 77.22(1)."),
 ("wi/misc", "Transfer fee", 2, "The real estate transfer return must be signed by:",
  "Both the grantor and the grantee", ["The grantor alone", "The register of deeds", "The closing agent"],
  "s. 77.22(1)."),
 ("wi/misc", "Marital property", 1, "Under Wisconsin law, property of spouses is:",
  "Presumed to be marital property, with each spouse holding a present undivided one-half interest", ["Presumed individual property", "Held as joint tenants by law"],
  "s. 766.31(2), (3)."),

 # fair housing
 ("wi/fair-housing", "Classes", 1, "Which is protected by Wisconsin's open housing law but not the federal Fair Housing Act?",
  "Lawful source of income", ["Race", "Religion", "National origin"],
  "s. 106.50(1)."),
 ("wi/fair-housing", "Classes", 1, "Wisconsin also protects:",
  "Status as a victim of domestic abuse, sexual assault or stalking", ["Credit history", "Occupation", "Length of residence"],
  "s. 106.50(1)."),
 ("wi/fair-housing", "Classes", 2, "'Age', for a member of a Wisconsin protected class, means:",
  "At least 18 years of age", ["Over 40", "Over 62", "Any age"],
  "s. 106.50(1m)(am)."),
 ("wi/fair-housing", "Practices", 2, "Falsely telling a caller that a vacant unit is unavailable is:",
  "Unlawful discrimination in housing", ["Lawful puffing", "A listing error only"],
  "s. 106.50(2)(h)."),
 ("wi/fair-housing", "Practices", 2, "Denying a licensee access to or membership in a multiple listing service on a protected ground is:",
  "Unlawful", ["An internal MLS matter", "Lawful if members vote"],
  "s. 106.50(2)(i)."),
 ("wi/fair-housing", "Discipline", 1, "A first discrimination violation by a Wisconsin licensee brings:",
  "Suspension of not less than 90 days", ["A written warning", "A $500 forfeiture", "Immediate revocation"],
  "s. 452.17(4)(a)(1); a second offence brings revocation."),
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
            "id": "wi-" + hashlib.sha1(q.encode()).hexdigest()[:8],
            "portion": "georgia", "topic": topic, "subtopic": sub,
            "sub": topic + "|" + sub, "concept": "Wisconsin " + sub.lower(),
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
        "code": "WI", "name": "Wisconsin", "abbr": "WI",
        "regulator": "Wisconsin Real Estate Examining Board",
        "pass": EXAM["pass"], "single": True,
        "pass_published": EXAM["pass_published"],
        "pass_note": EXAM["pass_note"],
        "portions": {
            "national": {"name": "General practice",
                         "scored": EXAM["national_scored"],
                         "minutes": EXAM["national_minutes"],
                         "blurb": "Ownership, transfer, land use, valuation, financing and the maths."},
            "georgia": {"name": "Wisconsin law", "scored": EXAM["state_scored"],
                        "minutes": EXAM["state_minutes"],
                        "blurb": "Chapter 452, the REEB rules, the WB forms, condition reports and open housing."},
        },
        "topics": topics, "bank": bank, "study": study,
        "sources": SOURCES, "diffs": DIFFS,
    }


# Where Wisconsin departs from the national rule.
DIFFS = {
    "national/agency": [
        "Wisconsin's duties run from the FIRM. A firm owes every party honesty, reasonable skill and care, written disclosure of material adverse facts, confidentiality that SURVIVES the transaction, accurate market information, safeguarding of trust funds, and objective presentation of proposals (s. 452.133(1)).",
        "A firm may work with anyone but may only NEGOTIATE for its own client or a principal firm's client (s. 452.134(1)).",
        "MULTIPLE REPRESENTATION and DESIGNATED AGENCY each need separate WRITTEN consent from all of the firm's clients, and consent to designated agency may be withdrawn at any time (s. 452.134(2), (3)).",
        "Self-dealing consent must be taken IN the offer, option or lease itself (s. 452.133(3)(b)).",
    ],
    "national/disclosures": [
        "The owner delivers the REAL ESTATE CONDITION REPORT within 10 DAYS of acceptance; a buyer who does not get it may rescind within 2 BUSINESS DAYS of that deadline (s. 709.02).",
        "A licensee need NOT disclose an occurrence with no effect on physical condition, matters already in a qualified third party's written report, or the location of an adult family home, CBRF or nursing home - but must disclose facts that CONTRADICT the report (s. 452.23).",
        "Registry questions are answered from ACTUAL KNOWLEDGE, with immunity for pointing the asker to the Department of Corrections in writing (s. 452.24).",
    ],
    "national/practice": [
        "Client funds go into an INTEREST-BEARING COMMON TRUST ACCOUNT and the interest belongs to the DEPARTMENT OF ADMINISTRATION (s. 452.13).",
        "Open housing adds LAWFUL SOURCE OF INCOME, marital status, ancestry and victim-of-abuse status, and a first discrimination violation brings a MANDATORY 90-day suspension, a second revocation (s. 106.50; s. 452.17(4)).",
        "Licensees FILL IN board-approved forms and may give a general explanation, but may not advise on legal rights, legal effect or title (s. 452.40).",
        "The transfer fee is 30 CENTS PER $100 of value and the GRANTOR pays it (s. 77.22).",
        "2025 Wis. Act 69 bans firm-to-firm compensation in 1-4 unit residential sales and requires seller-paid buyer-agent compensation to sit in the executed offer - FROM 1 JANUARY 2027, not yet in force (s. 452.19(3), (4)).",
    ],
}


if __name__ == "__main__":
    import io, json, os
    here = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    out = os.path.join(here, "greprep", "packs", "WI.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    pack = build()
    with io.open(out, "w", encoding="utf-8") as f:
        json.dump(pack, f, ensure_ascii=False, indent=1, sort_keys=True)
    print("wrote", out, len(pack["bank"]), "questions,", len(pack["study"]), "lessons")
