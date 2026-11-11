"""Maryland state content: lessons and practice questions.

Maryland splits the salesperson examination and publishes ONE uniform pass
mark. The PSI Maryland Real Estate Candidate Information Bulletin and the
Maryland Real Estate Commission's own examination page: National 80 items /
90 minutes / 56 correct to pass; State 30 items / 30 minutes / 21 correct to
pass - 110 items and 120 minutes in all, "at least 70%" on each portion.

Maryland's agency law is the thing to learn first. Dual agency is PERMITTED
but only with the written informed consent of all parties, and a dual agency
only works through INTRA-COMPANY AGENTS: the broker assigns one licensee to
the seller and a different licensee to the buyer, and those intra-company
agents give FULL service, including advice on price and negotiation strategy.
A dual agent may not also be an intra-company agent in the same transaction.

Every rule below was read on 2026-11-11 from the official text:
  - Maryland Code, Business Occupations and Professions, Title 17, from
    mgaleg.maryland.gov - in particular 17-202, 17-209, 17-310, 17-313,
    17-315, 17-320, 17-322, 17-404, 17-502, 17-505, 17-518, 17-524,
    17-527.2, 17-530, 17-530.1, 17-530.2, 17-532, 17-604, 17-605, 17-607.
  - Maryland Code, Real Property, 10-702 (residential property disclosure
    and disclaimer statement), from mgaleg.maryland.gov.
  - The Maryland Real Estate Commission's published continuing education
    requirements at labor.maryland.gov/license/mrec/mreceducreq.shtml.
  - The PSI Maryland Real Estate Candidate Information Bulletin and MREC's
    examination page at labor.maryland.gov/license/mrec/mrecexam.shtml, for
    the examination table, the education requirements and the 30-item
    salesperson state outline.
The section a fact comes from is cited next to it. Do not add a fact here
without reading its source first.
"""

EXAM = {
    # Salesperson: National 80 items / 90 minutes / 56 to pass (70%);
    # State 30 items / 30 minutes / 21 to pass (70%).
    "state_scored": 30,
    "state_minutes": 30,
    "national_scored": 80,
    "national_minutes": 90,
    "pass": 0.70,
}

# PSI's Maryland salesperson state outline, item counts summing to 30.
TOPICS = [
    ("md/relationships", "Brokerage relationships", 7,
     "Listing agreements, agency disclosure, dual agency and intra-company agents, conflicts."),
    ("md/conduct", "Business conduct", 6,
     "Offers, commissions and rebates, advertising and signs, fair housing, summary suspension."),
    ("md/supervision", "Supervision", 5,
     "Trust money, records, broker and branch manager supervision, other Maryland laws."),
    ("md/commission", "Duties and powers of the Commission", 4,
     "The Commission, investigations and hearings, penalties, the Guaranty Fund."),
    ("md/licensing", "Licensing requirements", 4,
     "What needs a licence, status changes, renewal, continuing education, entities, offices."),
    ("md/ethics", "Ethics", 4,
     "Unfair inducements, dealings with other licensees, the Maryland Code of Ethics."),
]

SOURCES = [
    {"by": "Maryland General Assembly",
     "name": "Business Occupations and Professions Article, Title 17",
     "note": "Licensing, the Commission, grounds for discipline, the Guaranty Fund, trust money and the brokerage relationship sections 17-528 to 17-535.",
     "url": "https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gbo&section=17-530.1&enactments=false"},
    {"by": "Maryland General Assembly",
     "name": "Real Property Article, 10-702",
     "note": "The residential property condition disclosure statement and the disclaimer statement, and the purchaser's 5-day right to rescind.",
     "url": "https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=grp&section=10-702&enactments=false"},
    {"by": "Maryland Real Estate Commission",
     "name": "Continuing Education Requirements",
     "note": "15 clock hours every 2-year term, and the mandatory Maryland topics that may not be substituted.",
     "url": "https://labor.maryland.gov/license/mrec/mreceducreq.shtml"},
    {"by": "PSI Services and the Maryland Real Estate Commission",
     "name": "Maryland Real Estate Candidate Information Bulletin",
     "note": "National 80 items at 70% and State 30 items at 70%, the 60-hour salesperson course, and the state outline.",
     "url": "https://labor.maryland.gov/license/mrec/mrecexam.shtml"},
]


# --------------------------------------------------------------- lessons

STUDY = {}

STUDY["md/relationships"] = {
    "summary": "The biggest block on the state paper, seven items. Maryland PERMITS dual agency, but only with written informed consent and only through INTRA-COMPANY AGENTS who give full service to their own side. Learn who may say what, and when the disclosure is due.",
    "sections": [
        {"h": "Dual agency and the intra-company agent (17-530.1)",
         "l": ["A broker, an associate broker or a salesperson may NOT make a contract with any party that would make the licensee a DUAL AGENT without the WRITTEN INFORMED CONSENT OF ALL PARTIES.",
               "When a broker is a dual agent, the broker MUST ASSIGN ONE licensee affiliated with the broker as an INTRA-COMPANY AGENT FOR THE SELLER, and ANOTHER licensee as an intra-company agent FOR THE BUYER.",
               "A DUAL AGENT MAY NOT ALSO BE AN INTRA-COMPANY AGENT in the same transaction, and an intra-company agent may not also be the dual agent.",
               "An intra-company agent PROVIDES THE SAME SERVICES as any other agent for that party, INCLUDING ADVISING ON PRICE AND NEGOTIATION STRATEGY. That is what makes Maryland's version different from a transaction brokerage.",
               "An intra-company agent may NOT disclose confidential information about the party they represent TO ANYONE EXCEPT THE DUAL AGENT.",
               "THE DUAL AGENT may NOT disclose confidential information about either party to the other party or to that party's intra-company agent.",
               "NEITHER the dual agent NOR an intra-company agent may tell the buyer that the seller will take less than the asking price, or tell the seller that the buyer will pay more than the offered price, UNLESS AUTHORISED IN WRITING by the party concerned.",
               "Any FINANCIAL BONUS offered to an affiliated licensee for selling the broker's own listings must be DISCLOSED TO EACH PARTY to the transaction.",
               "The consent form must state that the broker DOES NOT OWE UNDIVIDED LOYALTY to either party in a dual agency."],
         "check": [("Maryland dual agency requires:", "The written informed consent of all parties", ["Oral consent of the seller", "Nothing, it is the default", "Commission approval"], "BOP 17-530.1(a)."),
                   ("In a Maryland dual agency, the broker must:", "Assign one intra-company agent for the seller and a different one for the buyer", ["Act alone for both sides", "Refer the buyer out of the firm"], "BOP 17-530.1(b)."),
                   ("May a dual agent also serve as an intra-company agent in the same deal?", "No, the roles are mutually exclusive", ["Yes, with written consent", "Yes, if the parties never meet"], "BOP 17-530.1."),
                   ("What does a Maryland intra-company agent provide?", "The same services as any agent, including advice on price and negotiation strategy", ["Ministerial acts only", "No advice of any kind"], "BOP 17-530.1."),
                   ("An intra-company agent may share confidential information about their party with:", "The dual agent only", ["The other intra-company agent", "Anyone in the firm", "No one at all"], "BOP 17-530.1."),
                   ("May a dual agent tell a buyer the seller will accept less than the asking price?", "Only if the seller authorised it in writing", ["Yes, dual agents owe both sides full candour", "Never, under any circumstances"], "BOP 17-530.1."),
                   ("A bonus offered to affiliated licensees for selling in-house listings must be:", "Disclosed to each party to the transaction", ["Kept confidential", "Reported to the Commission"], "BOP 17-530.1.")]},
        {"h": "The agency disclosure, and when it is due (17-530)",
         "l": ["A licensee acting as a SELLER'S AGENT, a BUYER'S AGENT or a SUBAGENT must give a WRITTEN AGENCY DISCLOSURE on the Commission's form.",
               "The requirement DOES NOT APPLY where a WRITTEN BROKERAGE AGREEMENT already exists with that person - the agreement does the job.",
               "If the FIRST CONTACT is NOT FACE TO FACE, the licensee must make the disclosure THROUGH THAT SAME MEDIUM. Otherwise the disclosure is due NOT LATER THAN THE FIRST SCHEDULED FACE-TO-FACE CONTACT.",
               "AT AN OPEN HOUSE, a CONSPICUOUSLY DISPLAYED notice in the form the Commission provides satisfies the requirement.",
               "The written disclosure must explain, among other things, whom the licensee represents, that the licensee may represent the other party, and the duties owed.",
               "The COMMISSION ITSELF prepares and provides both the standard agency disclosure form and the standard dual agency consent form. Both must be in PLAIN LANGUAGE, CAPTIONED, and printed in AT LEAST 10 POINT TYPE (17-530.2).",
               "Failing to make the disclosure or to provide the consent form required by 17-530.2 is an independent ground for discipline (17-322(b)(30))."],
         "check": [("When is the Maryland agency disclosure due if first contact is face to face?", "Not later than the first scheduled face-to-face contact", ["Within 3 days", "At the contract signing", "At settlement"], "BOP 17-530."),
                   ("If first contact with a prospect is by telephone, the licensee must disclose:", "Through that same medium", ["At closing", "Only in writing by mail"], "BOP 17-530."),
                   ("The agency disclosure requirement does not apply where:", "A written brokerage agreement already exists with that person", ["The property is commercial", "The licensee is a subagent"], "BOP 17-530."),
                   ("At an open house, the disclosure may be satisfied by:", "A conspicuously displayed notice on the Commission's form", ["A verbal announcement", "A sign-in sheet"], "BOP 17-530."),
                   ("Who prepares Maryland's standard agency disclosure and dual agency consent forms?", "The Maryland Real Estate Commission", ["The Maryland Association of Realtors", "Each broker"], "BOP 17-530.2."),
                   ("Maryland's standard disclosure forms must be printed in:", "At least 10 point type, plain language, captioned", ["Any legible type", "Bold 12 point only"], "BOP 17-530.2.")]},
        {"h": "What a Maryland licensee owes (17-532)",
         "l": ["Perform the terms of the BROKERAGE AGREEMENT.",
               "PROMOTE THE INTERESTS OF THE CLIENT: seek a sale at the price and terms stated in the agreement or at a price and terms acceptable to the client, and PRESENT ALL WRITTEN OFFERS AND COUNTEROFFERS IN A TIMELY MANNER EVEN IF THE REAL ESTATE IS ALREADY SUBJECT TO A CONTRACT OF SALE OR LEASE.",
               "DISCLOSE ALL MATERIAL FACTS about the property that the licensee knows or should know, under 17-322(b)(4).",
               "TREAT ALL PARTIES TO THE TRANSACTION HONESTLY AND FAIRLY AND ANSWER ALL QUESTIONS TRUTHFULLY. This is owed to EVERYONE, not only the client.",
               "ACCOUNT IN A TIMELY MANNER for all money and property received.",
               "Exercise REASONABLE CARE AND DILIGENCE.",
               "COMPLY WITH ALL FAIR HOUSING LAW, federal and State.",
               "CONFIDENTIALITY is STRICT and WIDE: a licensee may not disclose confidential information about the licensee's OWN past or present clients, OR about the BROKER'S past or present clients, without that client's written consent."],
         "check": [("A Maryland licensee must present written offers:", "In a timely manner even if the property is already under contract", ["Only until a contract is ratified", "Only above the list price"], "BOP 17-532(c)(1)(ii)."),
                   ("Whom must a Maryland licensee treat honestly and fairly and answer truthfully?", "All parties to the transaction", ["The client only", "The client and the broker"], "BOP 17-532(c)(1)(iv)."),
                   ("Maryland's confidentiality duty covers:", "The licensee's and the broker's past and present clients", ["Current clients only", "The client named in the listing only"], "BOP 17-532."),
                   ("Confidential client information may be disclosed:", "With the client's written consent", ["To any licensee in the firm", "Once the deal closes"], "BOP 17-532."),
                   ("Which is NOT one of the 17-532 duties?", "Guaranteeing the property's future resale value", ["Timely accounting for money", "Reasonable care and diligence", "Compliance with fair housing law"], "Guaranteeing future profits is itself a ground for discipline under 17-322(b)(8).")]},
        {"h": "Listings and conflicts of interest",
         "l": ["A listing contract to sell real property must have a DEFINITE TERMINATION DATE THAT IS EFFECTIVE AUTOMATICALLY WITHOUT NOTICE from either side. Accepting one without it is a ground for discipline (17-322(b)(10)).",
               "NET LISTINGS are prohibited: a licensee may not accept a listing that provides for a NET RETURN to the seller and leaves the licensee free to sell at any higher price (17-322(b)(11)).",
               "A licensee may not KNOWINGLY SOLICIT a party to another licensee's EXCLUSIVE listing to terminate it and sign with the soliciting licensee (17-322(b)(12)).",
               "A licensee may not solicit a party to a contract, lease or agreement negotiated by another to BREACH it in order to substitute a new one on which the soliciting licensee earns (17-322(b)(13)).",
               "A licensee must FURNISH PROMPTLY to each party a copy of the listing contract, the contract of sale or the lease, and must KEEP A COPY of each executed one (17-322(b)(14) and (15)).",
               "GUARANTEEING or allowing another to guarantee FUTURE PROFITS from a resale is a ground for discipline (17-322(b)(8))."],
         "check": [("A Maryland listing contract must contain:", "A definite termination date effective automatically without notice", ["A 90-day minimum term", "An automatic renewal clause"], "BOP 17-322(b)(10)."),
                   ("A net listing in Maryland is:", "A ground for discipline", ["Permitted with written consent", "Permitted on commercial property"], "BOP 17-322(b)(11)."),
                   ("Soliciting a party to another licensee's exclusive listing to break it is:", "A ground for discipline", ["Fair competition", "Allowed after 30 days"], "BOP 17-322(b)(12)."),
                   ("After a contract of sale is signed, the licensee must:", "Promptly furnish each party a copy and keep a copy", ["Keep the only copy at the brokerage", "Deliver copies at settlement"], "BOP 17-322(b)(14), (15)."),
                   ("Guaranteeing a buyer future profits on resale is:", "A ground for discipline", ["Permitted if written", "Permitted for new construction"], "BOP 17-322(b)(8).")]},
    ],
    "traps": [
        "Maryland PERMITS dual agency. Do not carry over Colorado's or Florida's ban.",
        "An intra-company agent gives FULL service, including price and negotiation advice - not the stripped-down role of a transaction broker in other states.",
        "A dual agent and an intra-company agent are DIFFERENT PEOPLE in the same deal. The same licensee may not hold both roles.",
        "The disclosure deadline is the FIRST SCHEDULED FACE-TO-FACE CONTACT, not a number of days and not contract signing.",
        "Offers must be presented EVEN IF the property is already under contract.",
        "The honesty-and-fairness duty runs to ALL PARTIES, not only the client.",
    ],
    "vocab": [
        ["Dual agent", "The broker (and the broker's company) representing both the seller and the buyer in the same transaction with the written informed consent of all parties (BOP 17-530.1)."],
        ["Intra-company agent", "The licensee the dual-agent broker assigns to one party, who provides that party full service including advice on price and negotiation strategy (BOP 17-530.1)."],
        ["Written informed consent", "The consent, on the Commission's form, that makes dual agency lawful; the form states the broker does not owe undivided loyalty (BOP 17-530.1, 17-530.2)."],
        ["Subagent", "A licensee of another broker who works for the seller through the listing broker and who owes the same written agency disclosure (BOP 17-530)."],
        ["Net listing", "A listing that promises the seller a net return and lets the licensee keep anything above it - prohibited in Maryland (BOP 17-322(b)(11))."],
    ],
    "examples": [
        ["A broker lists a house. A buyer working with another licensee in the same firm wants to make an offer. What must happen?",
         "The broker becomes a dual agent only on the written informed consent of both the seller and the buyer. The broker then assigns one licensee as intra-company agent for the seller and a different licensee as intra-company agent for the buyer. The broker, as dual agent, may not also be one of those intra-company agents (BOP 17-530.1)."],
        ["An intra-company agent for the buyer learns from the buyer that the buyer would pay $20,000 more. May the agent tell the seller's side?",
         "No. That is confidential, and it may be shared only with the dual agent - never with the seller or the seller's intra-company agent. Neither the dual agent nor an intra-company agent may tell the seller the buyer will pay more unless the buyer authorises it in writing (BOP 17-530.1)."],
        ["A licensee meets a prospect for the first time at a scheduled showing. When is the agency disclosure due?",
         "Not later than that first scheduled face-to-face contact. If the first contact had been by telephone or email, the disclosure would have had to go through that medium (BOP 17-530)."],
    ],
}

STUDY["md/conduct"] = {
    "summary": "Six items on how business is actually done: advertising, offers, commissions and rebates, fair housing and blockbusting, and what gets a licence suspended on the spot.",
    "sections": [
        {"h": "Advertising (17-527.2 and 17-322)",
         "l": ["A licensee may NOT advertise unless the advertisement MEANINGFULLY AND CONSPICUOUSLY includes BOTH the licensee's name or DESIGNATED NAME as it appears on the licence certificate and pocket card, AND the name of the BUSINESS the licensee is affiliated with.",
               "The business name must be the FULL NAME OF THE BUSINESS, NOT A LOGO used by the business.",
               "\"Advertisement\" is broad: correspondence, mailings, newsletters, brochures, BUSINESS CARDS, FOR SALE and FOR LEASE SIGNS AND SIGN RIDERS, promotional items, AUTOMOBILE SIGNAGE, telephone directory listings, television and radio announcements, telephone solicitation, and WEB AND INTERNET VOICE-OVERS.",
               "A \"DESIGNATED NAME\" is a name other than the full legal name - a first name, a nickname or a last name - and it must match the licence certificate and pocket card.",
               "Advertising in any MISLEADING OR UNTRUTHFUL manner, or violating 17-527.2, is a ground for discipline (17-322(b)(19)).",
               "An advertisement must disclose the ADVERTISER'S NAME AND THE FACT THAT THE ADVERTISER IS A LICENSEE (17-322(b)(18)); a salesperson or associate broker advertising in their own name must also DISCLOSE THE BROKER'S NAME (17-322(b)(20)).",
               "A licensee may not use a listing form, a contract form or ANY ADVERTISING MATTER bearing the name of an ORGANISATION OR ASSOCIATION THE LICENSEE IS NOT A MEMBER OF (17-322(b)(17)).",
               "Advertising \"FREE APPRAISALS\" is prohibited UNLESS the advertiser is prepared to appraise free of charge for ANY person, REGARDLESS of the purpose of the request (17-322(b)(9)(iii))."],
         "check": [("A Maryland advertisement must conspicuously include:", "The licensee's name or designated name and the full name of the affiliated business", ["The licence number only", "The brokerage logo only"], "BOP 17-527.2(b)."),
                   ("May a brokerage's logo stand in for its name in an advertisement?", "No, the full business name is required", ["Yes, if the logo is well known", "Yes, on signs only"], "BOP 17-527.2(b)(2)(ii)."),
                   ("Which of these is an \"advertisement\" under 17-527.2?", "A sign rider on a for-sale sign", ["A private email to the broker", "An internal office memo"], "BOP 17-527.2(a)(3)(ii)."),
                   ("A salesperson advertising in their own name must also disclose:", "The name of the broker on whose behalf they act", ["Their licence expiry date", "The seller's name"], "BOP 17-322(b)(20)."),
                   ("Advertising \"free appraisals\" is allowed only if:", "The advertiser will appraise free for anyone, for any purpose", ["The property is listed with the advertiser", "The appraisal is for a mortgage"], "BOP 17-322(b)(9)(iii)."),
                   ("Using a contract form bearing an association's name when not a member is:", "A ground for discipline", ["Permitted with attribution", "Permitted if the form is public"], "BOP 17-322(b)(17).")]},
        {"h": "Commissions, rebates and referrals (17-604, 17-605)",
         "l": ["A licensee may NOT pay compensation IN ANY FORM for real estate brokerage services to ANY PERSON WHO IS NOT LICENSED under Title 17.",
               "Exceptions: an individual LICENSED IN ANOTHER STATE who meets 17-513; a professional service corporation, LLC or business entity formed under 17-512; and a licensed TITLE INSURANCE PRODUCER acting under 17-604(c).",
               "During settlement, a licensed title insurance producer MAY, on the broker's behalf and under the broker's WRITTEN DISBURSEMENT AUTHORISATION, pay compensation to an associate broker, a salesperson or a 17-512 business entity.",
               "An associate broker or salesperson may NOT accept a commission or other valuable consideration from ANY PERSON OTHER THAN THE BROKER they are affiliated with, except as 17-604 allows (17-322(b)(21)).",
               "Retaining an UNLICENSED individual as an associate broker or salesperson to EVADE the ban on paying unlicensed people a commission is a ground for discipline (17-322(b)(7)).",
               "A licensee may NOT pay or offer to pay a commission TO A LAWYER SIMPLY FOR REFERRING a person as a possible party to a RESIDENTIAL transaction, and may not MASS SOLICIT referral business from lawyers by offering fees or commissions (17-605).",
               "That ban does not apply to lawyers who hold a Maryland real estate broker licence or are otherwise entitled to a commission, and it does not bar paying a lawyer for an actual SERVICE related to the transaction (17-605(b), (c)).",
               "Paying or receiving a rebate, profit, compensation or commission IN VIOLATION of Title 17 is a ground for discipline (17-322(b)(23))."],
         "check": [("A Maryland licensee may pay a brokerage commission to:", "A licensee, a 17-512 entity, a qualifying out-of-state licensee, or a title insurance producer under 17-604(c)", ["Any unlicensed referrer", "A friend who found the buyer"], "BOP 17-604."),
                   ("A salesperson's commission must come from:", "The broker with whom the salesperson is affiliated", ["The seller directly", "The title company, always"], "BOP 17-322(b)(21)."),
                   ("May a licensee pay a lawyer for simply referring a residential client?", "No", ["Yes, if the fee is under $500", "Yes, with the client's consent"], "BOP 17-605(a)(1)."),
                   ("A title insurance producer may pay a salesperson at settlement:", "On the broker's behalf under the broker's written disbursement authorisation", ["Only in cash", "Never"], "BOP 17-604(c)."),
                   ("Hiring an unlicensed person as a \"salesperson\" to get around the commission ban is:", "A ground for discipline", ["Permitted for assistants", "Permitted for leads only"], "BOP 17-322(b)(7).")]},
        {"h": "Offers, settlement providers and prizes",
         "l": ["Each real estate contract submitted for the SALE OF A SINGLE-FAMILY DWELLING must contain, IN BOLD-FACED TYPE, a statement that the BUYER HAS THE RIGHT TO SELECT the buyer's own TITLE INSURANCE COMPANY, SETTLEMENT COMPANY, ESCROW COMPANY, MORTGAGE LENDER OR FINANCIAL INSTITUTION, or TITLE LAWYER (17-524(a)).",
               "The same bold-faced statement must say that a SELLER MAY NOT BE PROHIBITED from offering OWNER FINANCING as a condition of settlement (17-524(b)).",
               "OMITTING that statement DOES NOT INVALIDATE THE CONTRACT (17-524(c)) - but providing a contract without the notice is a ground for discipline (17-322(b)(28)).",
               "In a single-family dwelling transaction, a licensee may NOT REQUIRE a buyer, as a CONDITION OF SETTLEMENT, to use a particular title insurance company, settlement company, escrow company, mortgage lender or financial institution, or title lawyer (17-607). Doing so is a ground for discipline (17-322(b)(29)).",
               "A licensee may not influence a prospective party by OFFERING A PRIZE OR A FREE LOT, or by CONDUCTING A LOTTERY OR CONTEST (17-322(b)(9))."],
         "check": [("Maryland single-family sales contracts must contain, in bold type:", "Notice of the buyer's right to select their own title, settlement, escrow, lender or title lawyer", ["A notice of the commission rate", "A home warranty disclosure"], "BOP 17-524(a)."),
                   ("If the buyer's-right-of-selection notice is omitted, the contract is:", "Still valid, but the licensee may be disciplined", ["Void", "Voidable by the buyer"], "BOP 17-524(c), 17-322(b)(28)."),
                   ("May a licensee require a buyer to use a named settlement company?", "No, not in a single-family dwelling transaction", ["Yes, if the seller agrees", "Yes, if disclosed"], "BOP 17-607(a)."),
                   ("The 17-524 notice must also state that:", "A seller may not be prohibited from offering owner financing", ["The buyer must use a licensed inspector", "The deposit is non-refundable"], "BOP 17-524(b)."),
                   ("Running a prize drawing to attract buyers is:", "A ground for discipline", ["Permitted with Commission approval", "Permitted for new subdivisions"], "BOP 17-322(b)(9).")]},
        {"h": "Fair housing and blockbusting (17-322(b)(16))",
         "l": ["Whether or not acting for monetary gain, a licensee may NOT knowingly induce or attempt to induce a person to TRANSFER real estate, or discourage a person from BUYING real estate, by making representations about the EXISTING OR POTENTIAL PROXIMITY of property owned or used by individuals of a particular RACE, COLOR, RELIGION, SEX, HANDICAP, FAMILIAL STATUS OR NATIONAL ORIGIN.",
               "It is equally prohibited to represent that such proximity WILL OR MAY result in: LOWERED PROPERTY VALUES; A CHANGE IN THE RACIAL, RELIGIOUS OR ETHNIC CHARACTER of the block, neighbourhood or area; AN INCREASE IN CRIMINAL OR ANTISOCIAL BEHAVIOUR; or A DECLINE IN THE QUALITY OF THE SCHOOLS serving the area.",
               "\"Handicap\" and \"familial status\" carry their FEDERAL FAIR HOUSING ACT meanings (17-322(a)).",
               "Compliance with ALL fair housing law is also an affirmative duty under 17-532(c)(1)(vii), and the Commission's continuing education requires a 2 clock hour FAIR HOUSING course every renewal."],
         "check": [("Maryland's blockbusting ban applies:", "Whether or not the licensee acts for monetary gain", ["Only where a commission is earned", "Only to brokers"], "BOP 17-322(b)(16)."),
                   ("Which statement is prohibited blockbusting?", "Saying the schools will decline because of who is moving in", ["Quoting published test scores on request", "Giving the county's own crime statistics link"], "BOP 17-322(b)(16)(ii)4."),
                   ("\"Familial status\" in 17-322 takes its meaning from:", "The federal Fair Housing Act", ["Maryland's own definition in Title 20", "Each county's code"], "BOP 17-322(a)."),
                   ("Fair housing compliance is:", "Both an affirmative 17-532 duty and a ground for discipline if breached", ["A federal matter only", "A continuing education topic only"], "BOP 17-532(c)(1)(vii), 17-322(b)(16).")]},
        {"h": "Discipline, penalties and convictions (17-322)",
         "l": ["Subject to the hearing provisions of 17-324, the Commission may DENY a licence, REPRIMAND a licensee, or SUSPEND OR REVOKE a licence on any of the 35 grounds in 17-322(b).",
               "INSTEAD OF OR IN ADDITION TO a reprimand, suspension or revocation, the Commission may impose a PENALTY NOT EXCEEDING $5,000 FOR EACH VIOLATION.",
               "In setting the amount the Commission must consider the SERIOUSNESS of the violation, the HARM CAUSED, the licensee's GOOD FAITH, and any HISTORY OF PREVIOUS VIOLATIONS. Penalties go into the GENERAL FUND OF THE STATE.",
               "The Commission MAY NOT impose a fine BASED SOLELY on discipline in another jurisdiction (17-322(c)(4)) - though that discipline is itself a ground for action (17-322(b)(35)).",
               "Convictions that support action: a FELONY; a MISDEMEANOUR DIRECTLY RELATED to fitness and qualification to provide brokerage services; or a crime that violates Title 17 (17-322(b)(24)).",
               "On a conviction the Commission must consider the NATURE OF THE CRIME, its RELATIONSHIP to licensed activity, (for a felony) its RELEVANCE to fitness, the TIME SINCE the conviction, and the applicant's BEHAVIOUR BEFORE AND AFTER (17-322(d)).",
               "Conduct showing BAD FAITH, INCOMPETENCY OR UNTRUSTWORTHINESS, or constituting DISHONEST, FRAUDULENT OR IMPROPER DEALINGS, is its own ground (17-322(b)(25)).",
               "ASSOCIATING with a licensee in a violating transaction WITH ACTUAL KNOWLEDGE of the violation is a ground (17-322(b)(26)); so is violating any REGULATION or any provision of the CODE OF ETHICS (17-322(b)(33))."],
         "check": [("The maximum Maryland penalty per violation is:", "$5,000", ["$1,000", "$2,500", "$25,000"], "BOP 17-322(c)(1)."),
                   ("Penalties collected under 17-322 are paid into:", "The General Fund of the State", ["The Guaranty Fund", "The Commission's operating budget"], "BOP 17-322(c)(3)."),
                   ("May the Commission fine a licensee solely because another state disciplined them?", "No", ["Yes, up to $5,000", "Yes, if the conduct was fraud"], "BOP 17-322(c)(4)."),
                   ("Which conviction supports Commission action?", "A misdemeanour directly related to fitness to provide brokerage services", ["Any traffic infraction", "Any misdemeanour whatsoever"], "BOP 17-322(b)(24)(ii)."),
                   ("In setting a penalty amount the Commission must consider:", "Seriousness, harm, the licensee's good faith, and prior violations", ["The licensee's income", "The brokerage's size"], "BOP 17-322(c)(2).")]},
    ],
    "traps": [
        "The maximum penalty is $5,000 PER VIOLATION, not per case, and it goes to the General Fund, not the Guaranty Fund.",
        "A logo is NOT a business name. The full business name must appear.",
        "Omitting the buyer's-right-of-selection notice does not void the contract - it is a discipline matter.",
        "Blockbusting is prohibited even with NO commission involved.",
        "A referral fee to a lawyer is banned for RESIDENTIAL referrals, but paying for a real service is fine.",
    ],
    "vocab": [
        ["Designated name", "A name other than a licensee's full legal name - a first name, nickname or last name - which must match the licence certificate and pocket card to be used in advertising (BOP 17-527.2(a)(4))."],
        ["Blockbusting", "Inducing a transfer, or discouraging a purchase, by representations about the proximity of people of a protected class, or its supposed effect on values, character, crime or schools (BOP 17-322(b)(16))."],
        ["Buyer's right of selection", "The bold-faced contract notice that the buyer chooses their own title, settlement, escrow, lender and title lawyer (BOP 17-524)."],
        ["Reprimand", "The lightest formal discipline the Commission may impose, available alone or alongside a penalty of up to $5,000 per violation (BOP 17-322)."],
    ],
    "examples": [
        ["A salesperson posts an Instagram ad with their nickname and the brokerage's logo mark, nothing else. Compliant?",
         "No. The nickname is fine if it is the designated name on the licence certificate and pocket card, but the FULL NAME OF THE BUSINESS must appear - a logo does not satisfy 17-527.2(b)(2)(ii)."],
        ["A lawyer sends a licensee three homebuyer referrals and asks for 10% of each commission. May the licensee pay?",
         "Not for the referrals themselves, in a residential transaction, unless the lawyer holds a Maryland broker licence or is otherwise entitled to a commission. Paying the lawyer for an actual service related to the transaction is allowed (BOP 17-605)."],
        ["The Commission finds four separate advertising violations by one licensee. What is the maximum fine?",
         "$5,000 for each violation, so up to $20,000, and the Commission must weigh seriousness, harm, good faith and prior history in setting each amount (BOP 17-322(c))."],
    ],
}

STUDY["md/supervision"] = {
    "summary": "Five items on the money and the chain of command: trust money, records, who supervises whom, and the other Maryland laws the outline expects you to recognise.",
    "sections": [
        {"h": "Trust money: getting it in (17-502)",
         "l": ["An associate broker or salesperson who obtains TRUST MONEY must PROMPTLY SUBMIT IT TO THE BROKER on whose behalf the services were provided.",
               "The broker must deposit trust money PROMPTLY, BUT NOT MORE THAN 7 BUSINESS DAYS AFTER THE ACCEPTANCE OF A CONTRACT OF SALE BY BOTH PARTIES, in an account maintained SEPARATELY from the broker's own accounts and SOLELY for trust money.",
               "A broker may NOT use trust money for ANY PURPOSE OTHER THAN that for which it was entrusted.",
               "The 7-business-day rule does not apply where the broker receives WRITTEN DIRECTIONS TO THE CONTRARY as 17-505 authorises.",
               "Violating any trust-money provision of Subtitle 5 is a ground for discipline (17-322(b)(31)); failing to ACCOUNT FOR OR REMIT PROMPTLY money belonging to another is another (17-322(b)(22))."],
         "check": [("A Maryland broker must deposit trust money within:", "7 business days after both parties accept the contract of sale", ["3 banking days of receipt", "24 hours", "The next business day"], "BOP 17-502(b)(1)."),
                   ("A salesperson who receives a deposit must:", "Promptly submit it to the broker", ["Deposit it personally", "Hold it until settlement"], "BOP 17-502(a)."),
                   ("A trust account must be:", "Separate from the broker's own accounts and used solely for trust money", ["A sub-account of the operating account", "An interest-bearing personal account"], "BOP 17-502(b)(1)."),
                   ("Using trust money to cover office rent is:", "Prohibited and a ground for discipline", ["Allowed up to $1,000", "Allowed if repaid before settlement"], "BOP 17-502(b)(2), 17-322(b)(31).")]},
        {"h": "Trust money: letting it out (17-505)",
         "l": ["A broker must HOLD trust money until: the transaction is CONSUMMATED OR TERMINATED; the broker receives PROPER WRITTEN INSTRUCTIONS from the owner and beneficial owner; a COURT ORDERS otherwise on an INTERPLEADER filed by the broker; or a party FAILS TO COMPLETE the transaction and the broker, IN THE BROKER'S SOLE DISCRETION, decides to distribute under subsection (b).",
               "Before distributing under that last route, the broker must NOTIFY BOTH the owner and the beneficial owner IN WRITING, STATE WHO WILL BE PAID, and DISCLOSE that either party may PREVENT the distribution by submitting a PROTEST WITHIN 30 DAYS of delivery or mailing, and that absent a protest the money will go as the notice says.",
               "The notice must be HAND DELIVERED to both, or sent by CERTIFIED MAIL, RETURN RECEIPT REQUESTED, AND REGULAR MAIL to both.",
               "A PROTEST must be in WRITING and either hand delivered or sent certified (return receipt) and regular mail, WITHIN 30 DAYS.",
               "IF A PROTEST ARRIVES, the broker must fall back on the other three routes - consummation or termination, written instructions, or a court order on interpleader.",
               "When the duty to hold ends, the broker PROMPTLY ACCOUNTS for all trust money. A broker may INVEST trust money only as the owner and beneficial owner direct in writing, or as broker, owner and beneficial owner agree in writing.",
               "The broker is NOT LIABLE for a GOOD FAITH decision to distribute under (a)(4), nor for deciding NOT to distribute.",
               "The agreement entrusting the money must CONTAIN A STATEMENT that the broker may distribute under subsection (b) if a party fails to complete the transaction."],
         "check": [("How long does a party have to protest a Maryland broker's proposed distribution?", "30 days from delivery or mailing of the notice", ["10 days", "15 days", "60 days"], "BOP 17-505(b)(2)(iii)1."),
                   ("If a written protest is received, the broker must:", "Wait for consummation or termination, written instructions, or a court order on interpleader", ["Pay the protesting party", "Split the deposit"], "BOP 17-505(b)(5)(i)."),
                   ("The 17-505 notice must be:", "Hand delivered, or sent certified mail return receipt requested and regular mail, to both owners", ["Emailed", "Sent by regular mail only"], "BOP 17-505(b)(3)."),
                   ("A broker may invest trust money:", "Only as the owner and beneficial owner direct in writing, or as all three agree in writing", ["At the broker's discretion", "Never, under any circumstances"], "BOP 17-505(e)."),
                   ("A broker who distributes in good faith under 17-505(a)(4) is:", "Not liable to the owner or beneficial owner", ["Strictly liable", "Liable for double the deposit"], "BOP 17-505(f).")]},
        {"h": "Who supervises whom (17-320, 17-518)",
         "l": ["A broker may use as an INDEPENDENT CONTRACTOR, employ, or otherwise contract with a licensed salesperson or associate broker to provide brokerage services on the broker's behalf - and may NOT provide brokerage services through any OTHER individual.",
               "ANY individual, INCLUDING A LICENSED ASSOCIATE BROKER, who provides brokerage services on behalf of a broker is CONSIDERED A SALESPERSON with respect to those services.",
               "A broker must exercise REASONABLE AND ADEQUATE SUPERVISION over the provision of brokerage services by any other individual, INCLUDING AN INDEPENDENT CONTRACTOR - REGARDLESS OF THE MANNER OF AFFILIATION. Failing to is a ground for discipline (17-322(b)(27)).",
               "A BRANCH OFFICE MANAGER must exercise reasonable and adequate supervision over the salespersons and associate brokers REGISTERED WITH THAT OFFICE, and that duty is IN ADDITION TO, NOT IN LIEU OF, the broker's (17-320(d)). Failing to is its own ground (17-322(b)(34)).",
               "When an affiliation TERMINATES, the broker IMMEDIATELY must: MAIL NOTICE to the licensee at the last known HOME AND OFFICE address; SUBMIT WRITTEN NOTICE to the Commission with copies of those notices; and RETURN THE LICENCE CERTIFICATE to the Commission (17-320(e)).",
               "A broker must obtain a BRANCH OFFICE CERTIFICATE before maintaining a branch office, with a $5 application fee, and must DESIGNATE A MANAGER for each branch - who may be the broker (17-518).",
               "A designated branch office manager must be an associate broker; OR a salesperson with AT LEAST 3 YEARS' experience providing brokerage services; OR a salesperson who has completed a Commission-approved BROKER course AND PASSED THE BROKER'S EXAMINATION (17-518(d)(2)).",
               "A branch office certificate expires on the first APRIL 30 in an EVEN-NUMBERED YEAR after its effective date, and renews for 2-YEAR TERMS for a $5 fee, filed with the MANAGER'S OWN licence renewal application (17-518(e))."],
         "check": [("A Maryland broker's supervision duty covers:", "Anyone providing brokerage services on the broker's behalf, including independent contractors", ["Employees only", "Salespersons but not associate brokers"], "BOP 17-320(c)."),
                   ("An associate broker providing services for a broker is treated as:", "A salesperson with respect to those services", ["A co-broker", "An unsupervised principal"], "BOP 17-320(b)."),
                   ("A branch office manager's supervision duty is:", "In addition to, not in lieu of, the broker's duty", ["A substitute for the broker's duty", "Optional if the broker visits weekly"], "BOP 17-320(d)(2)."),
                   ("When an affiliation ends, the broker must immediately:", "Notify the licensee, notify the Commission, and return the licence certificate", ["Only notify the Commission", "Wait for the licensee to transfer"], "BOP 17-320(e)."),
                   ("A salesperson may manage a branch office with:", "At least 3 years' experience, or an approved broker course plus a passed broker's examination", ["Any length of experience", "Two years and a letter from the broker"], "BOP 17-518(d)(2)."),
                   ("A Maryland branch office certificate expires on:", "The first April 30 in an even-numbered year after its effective date", ["December 31 each year", "The broker's licence expiry date"], "BOP 17-518(e)(1).")]},
        {"h": "Records, and the other Maryland laws",
         "l": ["For any transaction in which the licensee served as or on behalf of a broker, the licensee must KEEP A COPY of every EXECUTED listing contract, contract of sale and lease agreement (17-322(b)(15)) and FURNISH A COPY PROMPTLY to each party (17-322(b)(14)).",
               "A licensee must ACCOUNT FOR OR REMIT PROMPTLY any money that comes into the licensee's possession but belongs to another person (17-322(b)(22)).",
               "RESIDENTIAL PROPERTY DISCLOSURE (Real Property 10-702): a vendor of single-family residential property improved by FOUR OR FEWER single family units must complete and deliver EITHER a DISCLOSURE statement (what the vendor actually knows about the property's condition) OR a DISCLAIMER statement (\"as is\", with all defects) - on the COMMISSION'S FORM.",
               "A DISCLAIMER still has to DISCLOSE LATENT DEFECTS the vendor ACTUALLY KNOWS OF. \"Latent defects\" are material defects a purchaser would not reasonably be expected to see on a careful visual inspection AND that pose a DIRECT THREAT TO HEALTH OR SAFETY (10-702(a), (d)).",
               "Delivery is due ON OR BEFORE entering into the contract of sale. If the purchaser does NOT get it by then, the purchaser has an UNCONDITIONAL RIGHT, on WRITTEN NOTICE, to RESCIND at any time before receipt or WITHIN 5 DAYS AFTER receipt, and to the IMMEDIATE RETURN OF DEPOSITS (10-702(f), (h)).",
               "A purchaser who DOES receive it on time has NO right to rescind based on its contents (10-702(g)). The rights MAY NOT BE WAIVED in the contract, and any attempted waiver is VOID (10-702(k)).",
               "The LISTING BROKER'S licensee has a DUTY TO INFORM THE VENDOR of these rights and obligations; the buyer's licensee (or, if the buyer is unrepresented, the licensee dealing with the buyer) must inform the PURCHASER. Having done so, the licensee has NO FURTHER DUTIES and is NOT LIABLE for a violation of the section (10-702(m)).",
               "The outline also expects recognition of Maryland's SHORT SALE, HOME IMPROVEMENT and PROTECTION OF HOMEOWNERS IN FORECLOSURE law, and of the fact that deposits returned under the new-home or other statutory termination rights follow the 17-505 procedure (17-505(c))."],
         "check": [("Real Property 10-702 applies to:", "Single family residential property improved by four or fewer single family units", ["Any property including unimproved land", "Only new construction"], "RP 10-702(b)(1)."),
                   ("A Maryland vendor using the DISCLAIMER statement must still:", "Disclose latent defects the vendor actually knows of", ["Complete the full condition disclosure", "Provide a home inspection"], "RP 10-702(d)(1)."),
                   ("A \"latent defect\" under 10-702 is one that:", "A careful visual inspection would not reveal and that threatens health or safety", ["Any defect the buyer missed", "Any defect over $1,000 to repair"], "RP 10-702(a)."),
                   ("A purchaser who never received the 10-702 statement may rescind:", "Any time before receipt, or within 5 days after receipt, on written notice", ["Within 3 days of closing", "Only before the deposit is paid"], "RP 10-702(h)(1)."),
                   ("A purchaser who receives the statement on time may:", "Not rescind based on the information in it", ["Rescind within 5 days anyway", "Demand repairs"], "RP 10-702(g)."),
                   ("A waiver of the purchaser's 10-702 rights in the contract is:", "Void", ["Enforceable if initialled", "Enforceable in commercial deals"], "RP 10-702(k)(1)."),
                   ("Once a licensee informs their party of the 10-702 rights, the licensee:", "Has no further duties under the section and is not liable for a violation", ["Must verify the statement's accuracy", "Must obtain an inspection"], "RP 10-702(m)(3).")]},
    ],
    "traps": [
        "Deposit deadline is 7 BUSINESS DAYS AFTER BOTH PARTIES ACCEPT - not days from receipt, and not 3 banking days as in some states.",
        "The protest window in 17-505 is 30 DAYS, and a protest forces the broker back to consummation, written instructions or interpleader.",
        "A DISCLAIMER does NOT excuse latent defects the seller knows about.",
        "The 10-702 rescission window is 5 DAYS AFTER RECEIPT when the statement came late - there is no rescission right at all when it came on time.",
        "A branch manager's duty is ON TOP OF the broker's, never instead of it.",
        "An associate broker working under a broker is treated as a SALESPERSON for those services.",
    ],
    "vocab": [
        ["Trust money", "Money a licensee holds for another in a real estate transaction, which must reach the broker promptly and a dedicated trust account within 7 business days of acceptance (BOP 17-502)."],
        ["Interpleader", "The court action a broker files to have a court decide who gets disputed trust money (BOP 17-505(a)(3))."],
        ["Beneficial owner", "The party entitled to the benefit of the trust money - the other person, with the owner, who must be notified and may protest a distribution (BOP 17-505)."],
        ["Latent defect", "A material defect a careful visual inspection would not reveal that poses a direct threat to health or safety - disclosable even on a disclaimer (RP 10-702(a))."],
        ["Disclaimer statement", "The 10-702 alternative in which the vendor sells \"as is\" with all defects, except latent defects actually known."],
        ["Branch office certificate", "The $5 certificate a broker must hold for each branch office, expiring on the first April 30 of an even-numbered year and renewing for 2-year terms (BOP 17-518)."],
    ],
    "examples": [
        ["Both parties ratify a contract on a Friday and the buyer's $10,000 deposit is already with the salesperson. What must happen?",
         "The salesperson promptly submits it to the broker, and the broker deposits it in a dedicated trust account within 7 BUSINESS DAYS of that acceptance, unless written directions authorised under 17-505 say otherwise (BOP 17-502)."],
        ["The buyer walks away. The broker thinks the seller is entitled to the deposit. Can the broker just pay the seller?",
         "Only by the 17-505(b) route: written notice to both the owner and beneficial owner, hand delivered or sent certified return-receipt plus regular mail, stating who will be paid and that either may protest within 30 days. A written protest sends the broker back to consummation, written instructions or interpleader (BOP 17-505)."],
        ["A seller gives the purchaser the 10-702 disclosure two weeks after the contract was signed. What are the purchaser's rights?",
         "The purchaser had an unconditional right to rescind on written notice at any time before receipt, and still has 5 days after receipt, plus immediate return of deposits - unless the right already terminated under the lender-application rules in 10-702(h)(2)."],
    ],
}

STUDY["md/commission"] = {
    "summary": "Four items. Know who the Commission is, what it can compel, what it can impose, and the Guaranty Fund's limit and deadline.",
    "sections": [
        {"h": "Who the Commission is (17-202, 17-203)",
         "l": ["The Commission consists of 9 MEMBERS: 5 LICENSEES (brokers, associate brokers or salespersons) and 4 CONSUMER MEMBERS.",
               "The 5 professional members are distributed GEOGRAPHICALLY - one each from the Eastern Shore counties; from Baltimore, Carroll, Harford and Howard; from BALTIMORE CITY; from Anne Arundel, Calvert, Charles, Prince George's and St. Mary's; and from Allegany, Frederick, Garrett, Montgomery and Washington.",
               "The GOVERNOR appoints members with the advice of the SECRETARY and the advice and consent of the SENATE. Every member must be a CITIZEN OF THE STATE.",
               "A professional member must have lived in their area AT LEAST 5 YEARS before appointment and have been licensed AT LEAST 10 YEARS before appointment.",
               "A CONSUMER MEMBER must be a member of the general public, may not be a licensee or otherwise regulated by the Commission, may not have had a financial interest in or compensation from a regulated person WITHIN 1 YEAR before appointment, and MAY NOT GRADE ANY EXAMINATION given by or for the Commission.",
               "A member's TERM IS 4 YEARS, beginning JUNE 1; terms are staggered; a member serves until a successor qualifies.",
               "The Governor may REMOVE a member for INCOMPETENCE OR MISCONDUCT, and a member is treated as having RESIGNED if they miss more than a third of meetings in any consecutive 12-month period, unless the Governor waives it publicly.",
               "The Commission ELECTS A CHAIRMAN ANNUALLY from its members for a 1-YEAR term, who may be reelected and who must be covered by a SURETY BOND or insurance policy set by the STATE TREASURER (17-203)."],
         "check": [("The Maryland Real Estate Commission has:", "9 members - 5 licensees and 4 consumer members", ["7 members", "5 members, all licensees", "12 members"], "BOP 17-202(a)."),
                   ("A professional Commission member must have been licensed for at least:", "10 years before appointment", ["3 years", "5 years", "15 years"], "BOP 17-202(c)(2)."),
                   ("A Commission member's term is:", "4 years, beginning June 1", ["2 years", "6 years", "At the Governor's pleasure"], "BOP 17-202(f)(1)."),
                   ("A consumer member may not:", "Grade any examination given by or for the Commission", ["Vote on discipline", "Attend hearings"], "BOP 17-202(d)(2)(ii)."),
                   ("The Commission's chairman:", "Is elected annually from among the members for a 1-year term", ["Is appointed by the Governor", "Serves the full 4-year term"], "BOP 17-203(a), (b).")]},
        {"h": "Investigations, hearings and enforcement (17-209)",
         "l": ["The Commission ADMINISTERS AND ENFORCES Title 17.",
               "In a disciplinary action, investigation or proceeding, the COMMISSION, A HEARING BOARD, THE EXECUTIVE DIRECTOR or THE ASSISTANT DIRECTOR may HOLD HEARINGS, ADMINISTER OATHS, ISSUE SUBPOENAS for witnesses or evidence, and TAKE DEPOSITIONS as in civil cases.",
               "If a person ignores a subpoena, a CIRCUIT COURT may COMPEL compliance on the petition of the Commission or another party.",
               "If the Commission concludes that alleged conduct MAY RESULT IN IRREPARABLE HARM, it may SUE FOR AN EX PARTE, INTERLOCUTORY OR FINAL INJUNCTION - and need NOT POST BOND against an unlicensed person, nor ALLEGE OR PROVE that no adequate remedy at law exists.",
               "The Commission MUST investigate any complaint alleging that an UNAUTHORISED PERSON provided brokerage services. A complaint must be IN WRITING, STATE THE FACTS SPECIFICALLY, and be FILED with the Commission - and if it comes from anyone other than a COMMISSION MEMBER it must be made UNDER OATH.",
               "Discipline under 17-322 is SUBJECT TO THE HEARING PROVISIONS OF 17-324."],
         "check": [("Who may issue a subpoena in a Maryland real estate investigation?", "The Commission, a hearing board, the executive director or the assistant director", ["Only a circuit court judge", "Only the full Commission"], "BOP 17-209(a)(2)."),
                   ("A complaint against an unlicensed practitioner must be:", "In writing, specific as to facts, filed with the Commission, and under oath unless made by a Commission member", ["Oral and anonymous", "Filed with the Attorney General"], "BOP 17-209(c)."),
                   ("To get an injunction against an unlicensed person, the Commission:", "Need not post bond or prove the absence of an adequate remedy at law", ["Must post a bond", "Must first complete a hearing"], "BOP 17-209(b)(2)."),
                   ("If a witness ignores a Commission subpoena:", "A circuit court may compel compliance", ["The Commission may jail the witness", "Nothing can be done"], "BOP 17-209(a)(3).")]},
        {"h": "The Real Estate Guaranty Fund (17-404)",
         "l": ["The Fund pays a claimant's ACTUAL LOSS from THEFT, EMBEZZLEMENT, FALSE PRETENSES, FORGERY, FRAUD OR MISREPRESENTATION by a LICENSEE - or by an UNLICENSED EMPLOYEE OF A BROKER.",
               "The REAL ESTATE MUST BE LOCATED IN MARYLAND.",
               "The MAXIMUM IS $50,000 PER CLAIM.",
               "EXCLUDED: a claim arising from a LIMITED PARTNERSHIP INTEREST, a PROMOTED JOINT VENTURE, or COMMERCIAL PAPER SECURED BY REAL ESTATE.",
               "A LICENSEE'S SPOUSE, or that spouse's personal representative, MAY NOT RECOVER from the Fund.",
               "A claim must be submitted WITHIN 3 YEARS of when the claimant DISCOVERED, or BY THE EXERCISE OF ORDINARY DILIGENCE SHOULD HAVE DISCOVERED, the loss."],
         "check": [("The maximum Guaranty Fund recovery per claim is:", "$50,000", ["$25,000", "$100,000", "$150,000"], "BOP 17-404."),
                   ("A Guaranty Fund claim must be filed within:", "3 years of discovery, or when it should have been discovered by ordinary diligence", ["1 year of the transaction", "6 months of discovery", "5 years of closing"], "BOP 17-404."),
                   ("Whose misconduct can support a Guaranty Fund claim?", "A licensee, or an unlicensed employee of a broker", ["Any party to the transaction", "A licensed appraiser"], "BOP 17-404."),
                   ("Which claim is excluded from the Fund?", "A loss on a promoted joint venture", ["A forged deed by a salesperson", "An embezzled deposit"], "BOP 17-404."),
                   ("May the spouse of the offending licensee recover from the Fund?", "No", ["Yes, up to $50,000", "Yes, if separated"], "BOP 17-404."),
                   ("The property involved in a Guaranty Fund claim must be:", "Located in Maryland", ["Owned by the claimant for a year", "Residential only"], "BOP 17-404.")]},
    ],
    "traps": [
        "9 members: 5 licensees, 4 consumers. Not a licensee-only board.",
        "Guaranty Fund cap is $50,000 PER CLAIM, and the deadline runs from DISCOVERY, not from the transaction.",
        "Penalties under 17-322 go to the GENERAL FUND; the Guaranty Fund is a separate pot that pays victims.",
        "A complaint from a non-member must be UNDER OATH.",
    ],
    "vocab": [
        ["Guaranty Fund", "The State fund paying a claimant's actual loss, up to $50,000 per claim, from a licensee's or a broker's unlicensed employee's theft, fraud or misrepresentation on Maryland property (BOP 17-404)."],
        ["Hearing board", "A panel that may hold hearings, administer oaths, subpoena and take depositions in a Commission matter (BOP 17-209(a)(2))."],
        ["Consumer member", "One of the four Commission members from the general public, barred from grading examinations and from any financial interest in a regulated person (BOP 17-202(d))."],
        ["Reprimand, suspension, revocation", "The three licence sanctions in 17-322(b), available alone or with a penalty of up to $5,000 per violation."],
    ],
    "examples": [
        ["A salesperson pockets a $30,000 deposit on a Baltimore house and disappears. The buyer sues, wins, and cannot collect. Now what?",
         "The buyer may claim against the Guaranty Fund for the actual loss, up to $50,000 per claim, as long as the claim is submitted within 3 years of discovery and the property is in Maryland (BOP 17-404)."],
        ["A complaint arrives by anonymous email saying an unlicensed person is listing homes. Must the Commission investigate?",
         "Not on that document. The Commission must investigate complaints of unauthorised practice, but the complaint has to be in writing, specific as to facts, filed with the Commission, and sworn unless a Commission member made it (BOP 17-209(c))."],
    ],
}

STUDY["md/licensing"] = {
    "summary": "Four items. The 60-hour course and the 1-year window, what the licence lets you do, how status changes work, and the 15 hours of continuing education with Maryland's mandatory topics.",
    "sections": [
        {"h": "Getting licensed",
         "l": ["A salesperson applicant must be AT LEAST 18, of GOOD CHARACTER AND REPUTATION, complete a COMMISSION-APPROVED 60-HOUR SALESPERSON PRE-LICENSING COURSE, and PASS BOTH PORTIONS of the examination.",
               "A BROKER applicant's pre-licensing course is 135 HOURS.",
               "BOTH PORTIONS must be passed WITHIN 1 YEAR OF COMPLETING THE COURSE; otherwise the course must be retaken (PSI Maryland bulletin).",
               "The examination is NATIONAL 80 SCORED ITEMS IN 90 MINUTES, 56 CORRECT TO PASS, and STATE 30 SCORED ITEMS IN 30 MINUTES, 21 CORRECT TO PASS - at least 70% on each portion, graded SEPARATELY.",
               "FRAUDULENTLY OR DECEPTIVELY obtaining or attempting to obtain a licence - for yourself or another - and fraudulently or deceptively USING a licence are both grounds for denial or discipline (17-322(b)(1), (2))."],
         "check": [("Maryland's salesperson pre-licensing course is:", "60 hours", ["45 hours", "75 hours", "90 hours"], "PSI Maryland Real Estate Candidate Information Bulletin."),
                   ("The Maryland salesperson examination is:", "80 national items in 90 minutes and 30 state items in 30 minutes", ["One 110-item exam", "100 national and 40 state"], "PSI Maryland bulletin; MREC examination page."),
                   ("To pass, a Maryland candidate needs:", "56 of 80 national and 21 of 30 state - 70% on each portion separately", ["70% of all 110 combined", "75% on the state portion"], "MREC examination page."),
                   ("A candidate must pass both portions within:", "1 year of completing the pre-licensing course", ["6 months", "2 years", "No limit"], "PSI Maryland bulletin."),
                   ("A Maryland broker applicant's pre-licensing course is:", "135 hours", ["90 hours", "60 hours", "180 hours"], "PSI Maryland bulletin.")]},
        {"h": "What the licence authorises, and status changes",
         "l": ["A BROKER LICENCE, while in effect, authorises the licensee to provide real estate brokerage services (17-310(a)).",
               "An ASSOCIATE BROKER or SALESPERSON licence authorises brokerage services ONLY on behalf of the broker NAMED IN THE LICENCE CERTIFICATE and with whom the licensee is AFFILIATED - NOT on the licensee's own behalf, and not for anyone else (17-310(b)).",
               "An associate broker or salesperson may NOT provide brokerage services on behalf of a broker WITHOUT INFORMING IN WRITING any OTHER broker with whom they are affiliated (17-322(b)(5)).",
               "A licensee may hold ADDITIONAL LICENCES and affiliate with ADDITIONAL BROKERS, and may move between salesperson, associate broker and broker status, but must in each case give WRITTEN NOTICE to every broker they are currently affiliated with, obtain a COMMITMENT from the new broker where one is required, and follow the 17-313(j) application procedure.",
               "A broker must obtain a SEPARATE BROKER LICENCE FOR EACH REAL ESTATE BROKERAGE the broker operates (17-313(i)).",
               "The Commission issues a LICENCE CERTIFICATE AND POCKET CARD to each individual granted a licence (17-313(l)).",
               "PARTNERSHIPS, CORPORATIONS AND LLCs: a professional service corporation, LLC or other business entity formed under 17-512 may be paid brokerage compensation; an unlicensed person may not (17-604)."],
         "check": [("A Maryland salesperson licence authorises services:", "Only on behalf of the broker named in the licence certificate", ["On the salesperson's own behalf too", "For any licensed broker"], "BOP 17-310(b)."),
                   ("To affiliate with a second broker, a salesperson must:", "Give written notice to each current broker and obtain a commitment from the new one", ["Simply notify the Commission after the fact", "Resign from the first broker"], "BOP 17-313(a)."),
                   ("A broker operating two brokerages needs:", "A separate broker licence for each brokerage", ["One licence and two branch certificates", "One licence only"], "BOP 17-313(i)(1)."),
                   ("Working for a broker without telling another broker you are affiliated with is:", "A ground for discipline", ["Permitted if disclosed to clients", "Permitted after 30 days"], "BOP 17-322(b)(5)."),
                   ("Brokerage compensation may be paid to a business entity if:", "The entity was formed under 17-512", ["The entity is any LLC", "The entity is owned by a licensee"], "BOP 17-604(b).")]},
        {"h": "Renewal and continuing education (17-315, MREC)",
         "l": ["To renew, a licensee must complete AT LEAST 15 CLOCK HOURS of continuing education during the preceding 2-YEAR TERM.",
               "For a licensee renewing an established licence, the 15 hours must include, EVERY 2 YEARS: a 3-HOUR LEGAL AND LEGISLATIVE UPDATE course on changes in federal, State or local law, regulations, court cases and industry trends; a 2-HOUR FAIR HOUSING course, INCLUDING FAIR HOUSING ADVERTISING; a 3-HOUR ETHICS course; and a 3-HOUR course on the PRINCIPLES OF BROKERAGE RELATIONSHIPS AND DISCLOSURES. The remaining 4 hours are ELECTIVES.",
               "The ETHICS course must cover the MARYLAND CODE OF ETHICS, FRAUDULENT REAL ESTATE PRACTICES, and PROFESSIONALISM including conflict resolution and the duty to respect the public, peers and property. The Commission states that NAR ETHICS IS NOT A SUBSTITUTE for the Maryland ethics course.",
               "A BROKER, a DESIGNATED BRANCH OFFICE MANAGER or a TEAM LEADER must also take a 1.5-HOUR BROKER SUPERVISION course every 2 years, and has 90 DAYS after assuming a supervisory role to complete it if it was not done in the previous renewal.",
               "FIRST RENEWAL for a salesperson initially licensed on or after 1 OCTOBER 2023, effective 1 OCTOBER 2025: 15 hours of MANDATORY topics - 3 hours CONTRACTS, 3 hours BROKERAGE RELATIONSHIPS AND DISCLOSURE, 3 hours PRINCIPLES OF REAL ESTATE PRACTICE (advertising, escrow handling, common ownership communities), 3 hours PROPERTY MANAGEMENT AND LANDLORD AND TENANT LAW, 1.5 hours PROFESSIONALISM, and 1.5 hours REAL ESTATE FINANCING. These may NOT be substituted with other education or with another state's continuing education.",
               "A licensee who works SOLELY IN NONRESIDENTIAL real estate takes a 2-HOUR AMERICANS WITH DISABILITIES ACT course INSTEAD OF the fair housing course (17-315(a)(2), (b)(4)).",
               "The LEGAL UPDATE, ETHICS and BROKERAGE RELATIONSHIPS AND DISCLOSURE courses are REQUIRED MARYLAND COURSES FOR ALL LICENSEES AND MAY NOT BE SUBSTITUTED.",
               "Out-of-state hours may count toward MARYLAND ELECTIVES only if the other state approves them as real estate continuing education, they meet the distribution requirements, AND that state permits the reverse substitution for its own licensees (17-315(a)(3), (4)).",
               "Continuing education must be completed DURING THE LICENCE TERM AND AT LEAST 30 DAYS BEFORE submitting a renewal application. MARYLAND DOES NOT RECOGNISE POST-LICENSING EDUCATION.",
               "Course identity must be verified: PHOTO IDENTIFICATION for an in-person course, a SIGNED AFFIDAVIT for a virtual or remote one (17-315(c)(4)). The provider may submit completions electronically WITHIN 14 DAYS (17-315(e)).",
               "The Commission MAY WAIVE the continuing education requirement FOR GOOD CAUSE (17-315(f))."],
         "check": [("Maryland continuing education is:", "At least 15 clock hours each 2-year term", ["7.5 hours a year, any topic", "12 hours each 2-year term"], "BOP 17-315(a)(1)."),
                   ("Which three Maryland courses may NOT be substituted?", "Legal and legislative update, ethics, and brokerage relationships and disclosure", ["Any three electives", "Fair housing, financing and contracts"], "MREC Continuing Education Requirements."),
                   ("Maryland's required fair housing course is:", "2 clock hours, including fair housing advertising", ["3 hours, advertising excluded", "1 hour"], "BOP 17-315(b)(2)(iii)."),
                   ("Does NAR's ethics course satisfy Maryland's ethics requirement?", "No", ["Yes, it is equivalent", "Yes, for Realtor members"], "MREC Continuing Education Requirements."),
                   ("A broker or branch office manager must additionally take:", "A 1.5-hour broker supervision course every 2 years", ["A 3-hour management course", "Nothing additional"], "BOP 17-315(b)(2)(vi)."),
                   ("A licensee working solely in nonresidential real estate takes, instead of fair housing:", "A 2-hour Americans with Disabilities Act course", ["Nothing", "A 2-hour commercial agency course"], "BOP 17-315(a)(2), (b)(4)."),
                   ("Continuing education must be completed:", "During the licence term and at least 30 days before submitting the renewal application", ["Any time before the expiry date", "Within 30 days after renewal"], "MREC Continuing Education Requirements."),
                   ("Maryland recognises post-licensing education:", "No, it does not", ["Yes, up to 15 hours", "Yes, for new licensees only"], "MREC Continuing Education Requirements.")]},
    ],
    "traps": [
        "15 hours every TWO YEARS, not per year, and most of it is pinned to named Maryland topics.",
        "NAR ethics does NOT satisfy Maryland ethics.",
        "The first-renewal track for salespersons first licensed on or after 1 Oct 2023 is a DIFFERENT, all-mandatory 15 hours - no electives.",
        "Maryland does NOT recognise post-licensing education.",
        "Both exam portions must be passed within 1 YEAR of course completion.",
        "A salesperson licence never authorises working on your own behalf.",
    ],
    "vocab": [
        ["Pocket card", "The card the Commission issues with the licence certificate; the name on it is the name that must appear in advertising (BOP 17-313(l), 17-527.2)."],
        ["Associate real estate broker", "A licensee who holds broker qualifications but provides services on behalf of another broker, and who is treated as a salesperson for those services (BOP 17-310, 17-320(b))."],
        ["Team leader", "A supervisory role that, like a broker and a branch office manager, must take the 1.5-hour broker supervision course (BOP 17-315(b)(2)(vi))."],
        ["Elective hours", "The 4 of the 15 renewal hours not tied to a mandatory Maryland topic - the only place out-of-state hours can land (MREC CE requirements)."],
    ],
    "examples": [
        ["A candidate finishes the 60-hour course in March, passes the national portion in May, and fails the state portion repeatedly.",
         "They must pass the state portion within 1 year of completing the course - by the following March - or retake the 60-hour course (PSI Maryland bulletin)."],
        ["A salesperson first licensed in January 2024 is up for a first renewal. What continuing education applies?",
         "The first-renewal track: 15 hours of mandatory topics - 3 contracts, 3 brokerage relationships and disclosure, 3 principles of real estate practice, 3 property management and landlord-tenant, 1.5 professionalism, 1.5 real estate financing - with no electives and no substitution (MREC CE requirements, effective 1 Oct 2025)."],
        ["A licensee also holds a Virginia licence and took 12 hours there. Can those hours count in Maryland?",
         "Only toward Maryland ELECTIVES, and only if Virginia approved them as real estate continuing education, they meet the distribution requirements, and Virginia allows the reverse substitution. The Maryland legal update, ethics and brokerage relationships courses can never be substituted (BOP 17-315(a)(3), (4))."],
    ],
}

STUDY["md/ethics"] = {
    "summary": "Four items on conduct the statute calls out by name: unfair inducements, how licensees treat each other, and the Maryland Code of Ethics the Commission enforces by regulation.",
    "sections": [
        {"h": "Unfair inducements",
         "l": ["A licensee may not solicit, sell or offer to sell so as to INFLUENCE a prospective party by OFFERING A PRIZE OR A FREE LOT, by CONDUCTING A LOTTERY OR CONTEST, or by ADVERTISING FREE APPRAISALS unless free appraisals are genuinely available to anyone for any purpose (17-322(b)(9)).",
               "GUARANTEEING, or authorising or allowing another to guarantee, FUTURE PROFITS from the resale of real property is prohibited (17-322(b)(8)).",
               "Directly or through another person, WILFULLY MAKING A MISREPRESENTATION or KNOWINGLY MAKING A FALSE PROMISE is a ground for discipline (17-322(b)(3)).",
               "INTENTIONALLY OR NEGLIGENTLY failing to disclose to ANY PERSON the licensee deals with a MATERIAL FACT the licensee KNOWS OR SHOULD KNOW relating to the property is a ground for discipline (17-322(b)(4)) - the negligence standard matters.",
               "Conduct demonstrating BAD FAITH, INCOMPETENCY OR UNTRUSTWORTHINESS, or constituting DISHONEST, FRAUDULENT OR IMPROPER DEALINGS, is a ground in its own right (17-322(b)(25))."],
         "check": [("The standard for failing to disclose a material fact is:", "Intentionally or negligently, as to facts the licensee knows or should know", ["Wilfully only", "Actual knowledge only"], "BOP 17-322(b)(4)."),
                   ("Offering a free lot to attract buyers is:", "A prohibited inducement", ["A permitted promotion", "Permitted if disclosed"], "BOP 17-322(b)(9)(i)."),
                   ("Telling a buyer the property will be worth 20% more in two years, as a guarantee, is:", "A ground for discipline", ["Permitted opinion", "Permitted with a disclaimer"], "BOP 17-322(b)(8)."),
                   ("\"Bad faith, incompetency or untrustworthiness\" is:", "An independent ground for discipline", ["Only relevant to penalty amount", "Not actionable without loss"], "BOP 17-322(b)(25).")]},
        {"h": "Dealings with other licensees",
         "l": ["A licensee may not KNOWINGLY SOLICIT a party to another licensee's EXCLUSIVE LISTING CONTRACT to terminate it and sign with the soliciting licensee (17-322(b)(12)).",
               "A licensee may not solicit a party to a SALES CONTRACT, LEASE OR AGREEMENT negotiated by another to BREACH it so the soliciting licensee can substitute a new one (17-322(b)(13)).",
               "An associate broker or salesperson may not provide brokerage services for a broker WITHOUT INFORMING IN WRITING any other broker they are affiliated with (17-322(b)(5)).",
               "A licensee may not, WITH ACTUAL KNOWLEDGE of the violation, ASSOCIATE with a licensee in a transaction or practice that violates Title 17 (17-322(b)(26)).",
               "A licensee may not use a LISTING FORM, a CONTRACT FORM or ANY ADVERTISING MATTER bearing the name of an ORGANISATION OR ASSOCIATION THE LICENSEE IS NOT A MEMBER OF (17-322(b)(17)).",
               "A licensee may not RETAIN OR ATTEMPT TO RETAIN an unlicensed individual as an associate broker or salesperson to evade the ban on paying commissions to unlicensed people (17-322(b)(7))."],
         "check": [("Knowingly going after another licensee's exclusive listing client to switch the listing is:", "A ground for discipline", ["Normal competition", "Permitted once the listing is within 30 days of expiry"], "BOP 17-322(b)(12)."),
                   ("Participating in a transaction knowing another licensee is violating Title 17 is:", "A ground for discipline", ["Only the other licensee's problem", "Actionable only if a client is harmed"], "BOP 17-322(b)(26)."),
                   ("Using a Realtor-branded contract form without being a member is:", "A ground for discipline", ["Permitted if the form is standard", "Permitted on commercial deals"], "BOP 17-322(b)(17)."),
                   ("Inducing a party to breach a lease negotiated by another licensee so you can write a new one is:", "A ground for discipline", ["Permitted if better for the client", "Permitted after the lease term starts"], "BOP 17-322(b)(13).")]},
        {"h": "The Maryland Code of Ethics",
         "l": ["Violating ANY REGULATION adopted under Title 17 OR ANY PROVISION OF THE CODE OF ETHICS is itself a ground for denial, reprimand, suspension or revocation (17-322(b)(33)).",
               "Because of that, the Code of Ethics is ENFORCEABLE LAW in Maryland, not a trade-association standard - and the Commission's mandatory 3-hour ethics course is built on THE MARYLAND CODE OF ETHICS, not NAR's.",
               "That ethics course must also cover FRAUDULENT REAL ESTATE PRACTICES and PROFESSIONALISM, including CONFLICT RESOLUTION and a licensee's DUTY TO RESPECT THE PUBLIC, PEERS AND PROPERTY (17-315(b)(2)(iv)).",
               "The affirmative conduct standards sit in 17-532: honesty and fairness to ALL PARTIES, truthful answers to ALL QUESTIONS, disclosure of material facts, timely accounting, reasonable care and diligence, fair housing compliance, and strict confidentiality.",
               "CONFLICT OF INTEREST: a dual-agent broker must disclose any FINANCIAL BONUS offered to affiliated licensees for selling in-house listings to EACH PARTY, and the consent form must say the broker DOES NOT OWE UNDIVIDED LOYALTY (17-530.1)."],
         "check": [("A violation of the Maryland Code of Ethics is:", "A ground for Commission discipline", ["A private association matter", "Only grounds for a fine"], "BOP 17-322(b)(33)."),
                   ("The required Maryland ethics course must discuss:", "The Maryland Code of Ethics, fraudulent practices, and professionalism", ["NAR's Code of Ethics", "Antitrust law only"], "BOP 17-315(b)(2)(iv)."),
                   ("A licensee must answer questions:", "Truthfully, for all parties to the transaction", ["Truthfully for the client only", "Only in writing"], "BOP 17-532(c)(1)(iv)."),
                   ("An in-house bonus for selling the broker's own listings must be:", "Disclosed to each party", ["Kept internal", "Reported annually to the Commission"], "BOP 17-530.1.")]},
    ],
    "traps": [
        "The Code of Ethics here is STATE LAW, enforced by the Commission - not NAR's.",
        "The failure-to-disclose ground reaches NEGLIGENT omissions and facts the licensee SHOULD know.",
        "The honesty duty runs to all parties, including the other side's customer.",
        "Associating in someone else's violation, with actual knowledge, is its own ground.",
    ],
    "vocab": [
        ["Maryland Code of Ethics", "The Commission's own code, whose violation is a statutory ground for discipline under BOP 17-322(b)(33) and whose content anchors the mandatory 3-hour ethics course."],
        ["Material fact", "A fact relating to the property that the licensee knows or should know and must disclose to any person they deal with (BOP 17-322(b)(4))."],
        ["Unfair inducement", "A prize, free lot, lottery, contest, false \"free appraisal\" offer or profit guarantee used to influence a prospective party (BOP 17-322(b)(8), (9))."],
    ],
    "examples": [
        ["A licensee learns at a listing appointment that the roof leaks, and simply never mentions it to the buyer's side.",
         "That is a ground for discipline under 17-322(b)(4) - intentionally or negligently failing to disclose a material fact the licensee knows or should know - and it breaches the 17-532 duty of honesty and fairness to all parties."],
        ["A licensee takes NAR's ethics course and submits it for the Maryland ethics requirement.",
         "It will not count. The Commission requires a Maryland ethics course covering the Maryland Code of Ethics, fraudulent practices and professionalism, and states NAR ethics is not a substitute."],
    ],
}


# ------------------------------------------------------------- questions

Q = [
    # relationships
    ("md/relationships", "Dual agency", 2, "In Maryland, a broker may act as a dual agent only with:", "The written informed consent of all parties", ["The seller's oral consent", "The Commission's prior approval", "A signed listing agreement alone"], "BOP 17-530.1(a)"),
    ("md/relationships", "Dual agency", 2, "When a Maryland broker is a dual agent, the broker must assign:", "One intra-company agent for the seller and a different one for the buyer", ["A single licensee to both parties", "An outside broker to the buyer", "No one; the broker handles both sides"], "BOP 17-530.1(b)"),
    ("md/relationships", "Dual agency", 3, "May the same licensee be both the dual agent and an intra-company agent in one transaction?", "No, the statute forbids holding both roles", ["Yes, with written consent of both parties", "Yes, if the parties are related", "Yes, in commercial transactions"], "BOP 17-530.1"),
    ("md/relationships", "Dual agency", 2, "A Maryland intra-company agent provides their party:", "The same services as any agent, including advice on price and negotiation strategy", ["Ministerial acts only", "Document preparation only", "No advice of any kind"], "BOP 17-530.1"),
    ("md/relationships", "Dual agency", 3, "An intra-company agent may disclose confidential information about their party to:", "The dual agent only", ["The other intra-company agent", "Any licensee in the firm", "The settlement company"], "BOP 17-530.1"),
    ("md/relationships", "Dual agency", 3, "May a Maryland dual agent tell the seller that the buyer would pay more than the offer?", "Only if the buyer authorised it in writing", ["Yes, the dual agent owes both sides candour", "Yes, after the offer is rejected", "Never, even with written authority"], "BOP 17-530.1"),
    ("md/relationships", "Conflicts", 2, "A financial bonus offered to affiliated licensees for selling in-house listings must be:", "Disclosed to each party to the transaction", ["Kept confidential as firm business", "Reported to the Commission annually", "Split with the cooperating broker"], "BOP 17-530.1"),
    ("md/relationships", "Dual agency", 2, "Maryland's dual agency consent form must state that the broker:", "Does not owe undivided loyalty to either party", ["Owes full fiduciary duties to both", "Will reduce the commission", "May withdraw at will"], "BOP 17-530.1"),
    ("md/relationships", "Disclosure", 2, "If first contact with a prospect is face to face, the Maryland agency disclosure is due:", "Not later than that first scheduled face-to-face contact", ["Within 3 business days", "At the contract signing", "At settlement"], "BOP 17-530"),
    ("md/relationships", "Disclosure", 2, "If the first contact is by email, the licensee must make the agency disclosure:", "Through that same medium", ["At the first showing", "By certified mail", "At closing"], "BOP 17-530"),
    ("md/relationships", "Disclosure", 2, "The Maryland agency disclosure requirement does not apply where:", "A written brokerage agreement already exists with that person", ["The property is over $1 million", "The licensee is a subagent", "The prospect is unrepresented"], "BOP 17-530"),
    ("md/relationships", "Disclosure", 2, "At a Maryland open house, the agency disclosure may be satisfied by:", "A conspicuously displayed notice on the Commission's form", ["A verbal announcement at the door", "A sign-in sheet", "Nothing; no disclosure is needed"], "BOP 17-530"),
    ("md/relationships", "Disclosure", 1, "Who prepares Maryland's standard agency disclosure and dual agency consent forms?", "The Maryland Real Estate Commission", ["The Maryland Association of Realtors", "Each individual broker", "The Attorney General"], "BOP 17-530.2"),
    ("md/relationships", "Disclosure", 2, "Maryland's standard disclosure forms must be printed in:", "At least 10 point type, in plain language, and captioned", ["At least 12 point bold", "Any legible typeface", "The broker's house style"], "BOP 17-530.2"),
    ("md/relationships", "Duties", 2, "A Maryland licensee must present written offers and counteroffers:", "In a timely manner even if the property is already subject to a contract", ["Only until a contract is ratified", "Only if above the list price", "Only with the client's prior approval of each"], "BOP 17-532(c)(1)(ii)"),
    ("md/relationships", "Duties", 2, "A Maryland licensee must treat honestly and fairly, and answer truthfully:", "All parties to the transaction", ["The client only", "The client and the broker", "Licensees only"], "BOP 17-532(c)(1)(iv)"),
    ("md/relationships", "Duties", 3, "Maryland's confidentiality duty extends to:", "The licensee's and the broker's past and present clients", ["Current clients only", "Clients named in the listing only", "Buyers only"], "BOP 17-532"),
    ("md/relationships", "Duties", 2, "Confidential client information may be disclosed:", "With the client's written consent", ["To any licensee in the firm", "Once the transaction closes", "To the cooperating broker"], "BOP 17-532"),
    ("md/relationships", "Listings", 2, "A Maryland listing contract to sell real property must contain:", "A definite termination date effective automatically without notice", ["A 90-day minimum term", "An automatic renewal clause", "A protection period"], "BOP 17-322(b)(10)"),
    ("md/relationships", "Listings", 2, "A net listing in Maryland is:", "A ground for discipline", ["Permitted with written consent", "Permitted on commercial property", "Permitted if the seller proposes it"], "BOP 17-322(b)(11)"),
    ("md/relationships", "Listings", 2, "Knowingly soliciting a party to another licensee's exclusive listing to terminate it is:", "A ground for discipline", ["Fair competition", "Permitted after 30 days", "Permitted if the listing is expiring"], "BOP 17-322(b)(12)"),
    ("md/relationships", "Listings", 2, "After a contract of sale is executed, the licensee must:", "Promptly furnish each party a copy and keep a copy", ["Keep the only original at the brokerage", "Deliver copies at settlement", "Send copies to the Commission"], "BOP 17-322(b)(14), (15)"),
    ("md/relationships", "Conflicts", 2, "Guaranteeing a buyer future profits on resale is:", "A ground for discipline", ["Permitted if put in writing", "Permitted for new construction", "Permitted with a disclaimer"], "BOP 17-322(b)(8)"),

    # conduct
    ("md/conduct", "Advertising", 2, "A Maryland advertisement must conspicuously include:", "The licensee's name or designated name and the full name of the affiliated business", ["The licence number only", "The brokerage logo only", "The broker's address"], "BOP 17-527.2(b)"),
    ("md/conduct", "Advertising", 2, "May a brokerage's logo substitute for its name in an advertisement?", "No, the full business name is required", ["Yes, if the logo is well known", "Yes, on signs only", "Yes, online only"], "BOP 17-527.2(b)(2)(ii)"),
    ("md/conduct", "Advertising", 2, "Which is an \"advertisement\" under 17-527.2?", "A sign rider on a for-sale sign", ["An internal office memo", "A private email to the broker", "A listing agreement"], "BOP 17-527.2(a)(3)(ii)"),
    ("md/conduct", "Advertising", 2, "A \"designated name\" must:", "Match the name on the licence certificate and pocket card", ["Be the full legal name only", "Be registered as a trade name", "Include the broker's name"], "BOP 17-527.2(a)(4)"),
    ("md/conduct", "Advertising", 2, "A salesperson advertising in their own name must also disclose:", "The name of the broker on whose behalf they act", ["Their licence expiry date", "The seller's name", "The listing price"], "BOP 17-322(b)(20)"),
    ("md/conduct", "Advertising", 3, "Advertising \"free appraisals\" is permitted only if:", "The advertiser will appraise free for anyone, for any purpose", ["The property is listed with the advertiser", "The appraisal is for a mortgage", "The advertiser is a licensed appraiser"], "BOP 17-322(b)(9)(iii)"),
    ("md/conduct", "Advertising", 2, "Using a contract form bearing an association's name when not a member is:", "A ground for discipline", ["Permitted with attribution", "Permitted if the form is public", "Permitted for leases only"], "BOP 17-322(b)(17)"),
    ("md/conduct", "Commissions", 2, "A Maryland licensee may not pay brokerage compensation to:", "A person not licensed under Title 17, except as 17-604 allows", ["A cooperating broker", "A 17-512 business entity", "An out-of-state licensee meeting 17-513"], "BOP 17-604(a)"),
    ("md/conduct", "Commissions", 2, "A Maryland salesperson's commission must come from:", "The broker with whom the salesperson is affiliated", ["The seller directly", "The title company in every case", "The cooperating broker"], "BOP 17-322(b)(21)"),
    ("md/conduct", "Commissions", 3, "May a licensee pay a lawyer purely for referring a residential client?", "No", ["Yes, if the fee is under $500", "Yes, with the client's written consent", "Yes, if the lawyer is a member of the bar"], "BOP 17-605(a)(1)"),
    ("md/conduct", "Commissions", 3, "At settlement, a licensed title insurance producer may pay a salesperson:", "On the broker's behalf under the broker's written disbursement authorisation", ["Only in cash", "Only with Commission approval", "Never"], "BOP 17-604(c)"),
    ("md/conduct", "Commissions", 2, "Retaining an unlicensed person as a \"salesperson\" to evade the commission ban is:", "A ground for discipline", ["Permitted for unlicensed assistants", "Permitted for lead generation", "Permitted if the person is paid hourly"], "BOP 17-322(b)(7)"),
    ("md/conduct", "Offers", 2, "A Maryland single-family sales contract must contain, in bold-faced type:", "Notice of the buyer's right to select their own title, settlement, escrow, lender or title lawyer", ["The commission rate", "A home warranty disclosure", "The seller's net sheet"], "BOP 17-524(a)"),
    ("md/conduct", "Offers", 3, "If the buyer's-right-of-selection notice is omitted, the contract is:", "Still valid, though the licensee may be disciplined", ["Void", "Voidable by the buyer", "Unenforceable against the seller"], "BOP 17-524(c), 17-322(b)(28)"),
    ("md/conduct", "Offers", 2, "May a licensee require a buyer to use a named settlement company?", "No, not in a single-family dwelling transaction", ["Yes, if the seller agrees", "Yes, if it is disclosed in writing", "Yes, if the lender requires it"], "BOP 17-607(a)"),
    ("md/conduct", "Offers", 2, "The 17-524 notice must also state that:", "A seller may not be prohibited from offering owner financing", ["The buyer must use a licensed inspector", "The deposit is non-refundable", "Settlement must occur in Maryland"], "BOP 17-524(b)"),
    ("md/conduct", "Inducements", 2, "Running a prize drawing to attract prospective buyers is:", "A ground for discipline", ["Permitted with Commission approval", "Permitted for new subdivisions", "Permitted if the prize is under $100"], "BOP 17-322(b)(9)"),
    ("md/conduct", "Fair housing", 2, "Maryland's blockbusting prohibition applies:", "Whether or not the licensee acts for monetary gain", ["Only where a commission is earned", "Only to brokers", "Only to residential property"], "BOP 17-322(b)(16)"),
    ("md/conduct", "Fair housing", 3, "Which is prohibited blockbusting in Maryland?", "Saying the schools will decline because of who is moving into the area", ["Providing the county's published test scores on request", "Giving a buyer the police department's crime map link", "Stating the property's assessed value"], "BOP 17-322(b)(16)(ii)4"),
    ("md/conduct", "Fair housing", 2, "\"Handicap\" and \"familial status\" in 17-322 take their meanings from:", "The federal Fair Housing Act", ["Maryland Title 20", "Each county's code", "Commission regulation"], "BOP 17-322(a)"),
    ("md/conduct", "Discipline", 1, "Maryland's maximum penalty per violation is:", "$5,000", ["$1,000", "$2,500", "$25,000"], "BOP 17-322(c)(1)"),
    ("md/conduct", "Discipline", 2, "Penalties collected under 17-322 are paid into:", "The General Fund of the State", ["The Guaranty Fund", "The Commission's operating budget", "A consumer restitution account"], "BOP 17-322(c)(3)"),
    ("md/conduct", "Discipline", 3, "May the Commission fine a licensee solely because another state disciplined them?", "No", ["Yes, up to $5,000", "Yes, if the conduct was fraud", "Yes, if the other state imposed a fine"], "BOP 17-322(c)(4)"),
    ("md/conduct", "Discipline", 2, "In setting a penalty amount the Commission must consider:", "Seriousness, harm caused, the licensee's good faith, and prior violations", ["The licensee's income", "The brokerage's size", "The client's wishes"], "BOP 17-322(c)(2)"),
    ("md/conduct", "Discipline", 2, "Which conviction supports Commission action?", "A misdemeanour directly related to fitness to provide brokerage services", ["Any traffic infraction", "Any misdemeanour whatsoever", "Only a felony"], "BOP 17-322(b)(24)(ii)"),

    # supervision
    ("md/supervision", "Trust money", 1, "A Maryland broker must deposit trust money within:", "7 business days after both parties accept the contract of sale", ["3 banking days of receipt", "24 hours of receipt", "The next business day"], "BOP 17-502(b)(1)"),
    ("md/supervision", "Trust money", 2, "A salesperson who receives a deposit must:", "Promptly submit it to the broker", ["Deposit it in the trust account personally", "Hold it until settlement", "Give it to the seller"], "BOP 17-502(a)"),
    ("md/supervision", "Trust money", 2, "A Maryland trust account must be:", "Separate from the broker's own accounts and used solely for trust money", ["A sub-account of the operating account", "An interest-bearing personal account", "Held at a Commission-designated bank"], "BOP 17-502(b)(1)"),
    ("md/supervision", "Trust money", 2, "Using trust money to pay office expenses is:", "Prohibited, and a ground for discipline", ["Allowed up to $1,000", "Allowed if repaid before settlement", "Allowed with the client's oral consent"], "BOP 17-502(b)(2), 17-322(b)(31)"),
    ("md/supervision", "Trust money", 2, "How long does a party have to protest a Maryland broker's proposed distribution of trust money?", "30 days from delivery or mailing of the notice", ["10 days", "15 days", "60 days"], "BOP 17-505(b)(2)(iii)1"),
    ("md/supervision", "Trust money", 3, "If a written protest is received, the broker must:", "Await consummation or termination, written instructions, or a court order on interpleader", ["Pay the protesting party", "Split the deposit equally", "Send the money to the Commission"], "BOP 17-505(b)(5)(i)"),
    ("md/supervision", "Trust money", 3, "The 17-505 distribution notice must be:", "Hand delivered, or sent certified mail return receipt requested plus regular mail, to both owners", ["Emailed to both owners", "Sent by regular mail only", "Published in a newspaper"], "BOP 17-505(b)(3)"),
    ("md/supervision", "Trust money", 3, "A Maryland broker may invest trust money:", "Only as the owner and beneficial owner direct in writing, or as all three agree in writing", ["At the broker's own discretion", "In insured certificates only", "Never, under any circumstances"], "BOP 17-505(e)"),
    ("md/supervision", "Trust money", 3, "A broker who distributes trust money in good faith under 17-505(a)(4) is:", "Not liable to the owner or beneficial owner", ["Strictly liable for the amount", "Liable for double the deposit", "Subject to automatic suspension"], "BOP 17-505(f)"),
    ("md/supervision", "Supervision", 2, "A Maryland broker's supervision duty covers:", "Anyone providing brokerage services on the broker's behalf, including independent contractors", ["Employees only", "Salespersons but not associate brokers", "Only licensees in the main office"], "BOP 17-320(c)"),
    ("md/supervision", "Supervision", 3, "An associate broker providing services on a broker's behalf is treated as:", "A salesperson with respect to those services", ["A co-broker", "An independent principal", "A branch manager"], "BOP 17-320(b)"),
    ("md/supervision", "Supervision", 2, "A Maryland branch office manager's supervision duty is:", "In addition to, not in lieu of, the broker's duty", ["A substitute for the broker's duty", "Optional if the broker visits weekly", "Limited to new licensees"], "BOP 17-320(d)(2)"),
    ("md/supervision", "Supervision", 2, "When an affiliation terminates, the broker must immediately:", "Notify the licensee, notify the Commission, and return the licence certificate", ["Only notify the Commission", "Wait for the licensee to transfer", "Hold the certificate for 30 days"], "BOP 17-320(e)"),
    ("md/supervision", "Offices", 3, "A Maryland salesperson may be designated a branch office manager with:", "At least 3 years' experience, or an approved broker course plus a passed broker's examination", ["Any length of experience", "Two years and the broker's letter", "A completed 60-hour course"], "BOP 17-518(d)(2)"),
    ("md/supervision", "Offices", 3, "A Maryland branch office certificate expires on:", "The first April 30 in an even-numbered year after its effective date", ["December 31 each year", "The broker's licence expiry date", "Two years from issue, to the day"], "BOP 17-518(e)(1)"),
    ("md/supervision", "Records", 2, "A licensee must keep a copy of every executed:", "Listing contract, contract of sale and lease agreement", ["Contract of sale only", "Closing statement only", "Advertisement"], "BOP 17-322(b)(15)"),
    ("md/supervision", "Disclosure", 2, "Real Property 10-702 applies to:", "Single family residential property improved by four or fewer single family units", ["Any property including unimproved land", "New construction only", "Property over $500,000"], "RP 10-702(b)(1)"),
    ("md/supervision", "Disclosure", 3, "A Maryland vendor who uses the DISCLAIMER statement must still:", "Disclose latent defects of which the vendor has actual knowledge", ["Complete the full condition disclosure too", "Provide a home inspection report", "Warrant the roof and systems"], "RP 10-702(d)(1)"),
    ("md/supervision", "Disclosure", 3, "A \"latent defect\" under 10-702 is a material defect that:", "A careful visual inspection would not reveal and that poses a direct threat to health or safety", ["Any defect the buyer failed to notice", "Any defect costing over $1,000", "Any defect the seller repaired"], "RP 10-702(a)"),
    ("md/supervision", "Disclosure", 2, "A purchaser who never received the 10-702 statement may rescind:", "At any time before receipt, or within 5 days after receipt, on written notice", ["Within 3 days of closing", "Only before paying the deposit", "Not at all"], "RP 10-702(h)(1)"),
    ("md/supervision", "Disclosure", 3, "A purchaser who receives the 10-702 statement on time may:", "Not rescind based on the information in it", ["Rescind within 5 days anyway", "Demand repairs of every item listed", "Rescind within 3 days"], "RP 10-702(g)"),
    ("md/supervision", "Disclosure", 2, "A contractual waiver of the purchaser's 10-702 rights is:", "Void", ["Enforceable if initialled", "Enforceable in commercial transactions", "Enforceable with consideration"], "RP 10-702(k)(1)"),
    ("md/supervision", "Disclosure", 3, "Once a licensee informs their party of the 10-702 rights and obligations, the licensee:", "Has no further duties under the section and is not liable for a violation of it", ["Must verify the statement's accuracy", "Must order an inspection", "Must deliver the statement personally"], "RP 10-702(m)(3)"),
    ("md/supervision", "Disclosure", 2, "Under 10-702, the listing broker's licensee has a duty to inform:", "The vendor of the vendor's rights and obligations", ["The purchaser only", "The lender", "The settlement agent"], "RP 10-702(m)(1)"),

    # commission
    ("md/commission", "Composition", 1, "The Maryland Real Estate Commission consists of:", "9 members - 5 licensees and 4 consumer members", ["7 members, all licensees", "5 members", "12 members, 6 and 6"], "BOP 17-202(a)"),
    ("md/commission", "Composition", 2, "A professional Commission member must have been licensed for at least:", "10 years before appointment", ["3 years", "5 years", "15 years"], "BOP 17-202(c)(2)"),
    ("md/commission", "Composition", 2, "A Commission member's term is:", "4 years, beginning June 1", ["2 years", "6 years", "Indefinite"], "BOP 17-202(f)(1)"),
    ("md/commission", "Composition", 3, "A consumer member of the Commission may not:", "Grade any examination given by or for the Commission", ["Vote on disciplinary matters", "Attend hearings", "Serve as chairman"], "BOP 17-202(d)(2)(ii)"),
    ("md/commission", "Composition", 2, "Commission members are appointed by:", "The Governor, with the advice of the Secretary and the advice and consent of the Senate", ["The Secretary alone", "The Commission itself", "The Maryland Association of Realtors"], "BOP 17-202(a)(4)"),
    ("md/commission", "Composition", 3, "The Commission's chairman:", "Is elected annually from among the members for a 1-year term", ["Is appointed by the Governor", "Serves a full 4-year term", "Is the executive director"], "BOP 17-203(a), (b)"),
    ("md/commission", "Powers", 2, "Who may issue a subpoena in a Maryland real estate disciplinary investigation?", "The Commission, a hearing board, the executive director or the assistant director", ["Only a circuit court judge", "Only the full Commission", "Only the Attorney General"], "BOP 17-209(a)(2)"),
    ("md/commission", "Powers", 3, "A complaint alleging unauthorised practice must be:", "In writing, specific as to facts, filed with the Commission, and sworn unless made by a Commission member", ["Oral and may be anonymous", "Filed with the circuit court", "Notarised in every case"], "BOP 17-209(c)"),
    ("md/commission", "Powers", 3, "Seeking an injunction against an unlicensed person, the Commission:", "Need not post bond or prove the absence of an adequate remedy at law", ["Must post a bond", "Must first hold a hearing", "Must join the Attorney General"], "BOP 17-209(b)(2)"),
    ("md/commission", "Powers", 2, "If a witness ignores a Commission subpoena:", "A circuit court may compel compliance", ["The Commission may jail the witness", "The Commission may revoke a non-licensee's rights", "Nothing can be done"], "BOP 17-209(a)(3)"),
    ("md/commission", "Guaranty Fund", 1, "The maximum Maryland Guaranty Fund recovery per claim is:", "$50,000", ["$25,000", "$100,000", "$150,000"], "BOP 17-404"),
    ("md/commission", "Guaranty Fund", 2, "A Guaranty Fund claim must be submitted within:", "3 years of discovery, or when it should have been discovered by ordinary diligence", ["1 year of the transaction", "6 months of discovery", "5 years of closing"], "BOP 17-404"),
    ("md/commission", "Guaranty Fund", 2, "Whose misconduct can support a Maryland Guaranty Fund claim?", "A licensee, or an unlicensed employee of a broker", ["Any party to the transaction", "A licensed appraiser", "A settlement attorney"], "BOP 17-404"),
    ("md/commission", "Guaranty Fund", 3, "Which claim is excluded from the Maryland Guaranty Fund?", "A loss on a promoted joint venture", ["A forged deed by a salesperson", "An embezzled deposit", "A misrepresented lot size"], "BOP 17-404"),
    ("md/commission", "Guaranty Fund", 3, "May the spouse of the offending licensee recover from the Guaranty Fund?", "No", ["Yes, up to $50,000", "Yes, if legally separated", "Yes, with Commission approval"], "BOP 17-404"),
    ("md/commission", "Guaranty Fund", 2, "Property involved in a Guaranty Fund claim must be:", "Located in Maryland", ["Owned by the claimant for a year", "Residential only", "Under $500,000 in value"], "BOP 17-404"),

    # licensing
    ("md/licensing", "Education", 1, "Maryland's salesperson pre-licensing course is:", "60 hours", ["45 hours", "75 hours", "90 hours"], "PSI Maryland Real Estate Candidate Information Bulletin"),
    ("md/licensing", "Education", 2, "Maryland's broker pre-licensing course is:", "135 hours", ["90 hours", "60 hours", "180 hours"], "PSI Maryland bulletin"),
    ("md/licensing", "Exam", 1, "The Maryland salesperson examination is:", "80 national items in 90 minutes and 30 state items in 30 minutes", ["One 110-item exam in 180 minutes", "100 national and 40 state", "80 national and 40 state"], "MREC examination page; PSI Maryland bulletin"),
    ("md/licensing", "Exam", 2, "To pass in Maryland a candidate needs:", "56 of 80 national and 21 of 30 state, each portion graded separately", ["70% of all 110 items combined", "75% on the state portion", "A scaled score of 75"], "MREC examination page"),
    ("md/licensing", "Exam", 2, "Both portions must be passed within:", "1 year of completing the pre-licensing course", ["6 months", "2 years", "There is no limit"], "PSI Maryland bulletin"),
    ("md/licensing", "Licences", 2, "A Maryland salesperson licence authorises brokerage services:", "Only on behalf of the broker named in the licence certificate", ["On the salesperson's own behalf as well", "For any licensed broker", "For any seller who signs a listing"], "BOP 17-310(b)"),
    ("md/licensing", "Licences", 2, "To affiliate with an additional broker, a Maryland salesperson must:", "Give written notice to each current broker and obtain a commitment from the new one", ["Notify the Commission after the fact", "Resign from the first broker", "Wait for the renewal date"], "BOP 17-313(a)"),
    ("md/licensing", "Licences", 3, "A broker operating two separate brokerages needs:", "A separate broker licence for each brokerage", ["One licence and two branch certificates", "One licence only", "A corporate licence"], "BOP 17-313(i)(1)"),
    ("md/licensing", "Licences", 2, "Providing services for a broker without informing another broker you are affiliated with is:", "A ground for discipline", ["Permitted if disclosed to clients", "Permitted after 30 days", "Permitted for referrals only"], "BOP 17-322(b)(5)"),
    ("md/licensing", "Entities", 2, "Brokerage compensation may be paid to a business entity if:", "The entity was formed under 17-512", ["The entity is any Maryland LLC", "A licensee owns the entity", "The entity registers with the Commission"], "BOP 17-604(b)"),
    ("md/licensing", "CE", 1, "Maryland continuing education is:", "At least 15 clock hours each 2-year term", ["7.5 hours per year, any topic", "12 hours each 2-year term", "30 hours each 2-year term"], "BOP 17-315(a)(1)"),
    ("md/licensing", "CE", 2, "Which three Maryland courses may not be substituted?", "Legal and legislative update, ethics, and brokerage relationships and disclosure", ["Any three electives", "Fair housing, financing and contracts", "Supervision, ethics and property management"], "MREC Continuing Education Requirements"),
    ("md/licensing", "CE", 2, "Maryland's required fair housing continuing education course is:", "2 clock hours, including fair housing advertising", ["3 hours, advertising excluded", "1 hour", "4 hours"], "BOP 17-315(b)(2)(iii)"),
    ("md/licensing", "CE", 2, "Does NAR's ethics course satisfy Maryland's ethics requirement?", "No", ["Yes, it is treated as equivalent", "Yes, for Realtor members", "Yes, with a Commission waiver"], "MREC Continuing Education Requirements"),
    ("md/licensing", "CE", 2, "A Maryland broker, branch office manager or team leader must additionally take:", "A 1.5-hour broker supervision course every 2 years", ["A 3-hour management course", "A 6-hour broker refresher", "Nothing additional"], "BOP 17-315(b)(2)(vi)"),
    ("md/licensing", "CE", 3, "A licensee working solely in nonresidential real estate takes, instead of fair housing:", "A 2-hour Americans with Disabilities Act course", ["Nothing in its place", "A 2-hour commercial agency course", "A 3-hour contracts course"], "BOP 17-315(a)(2), (b)(4)"),
    ("md/licensing", "CE", 2, "Maryland continuing education must be completed:", "During the licence term and at least 30 days before submitting the renewal application", ["Any time before the expiry date", "Within 30 days after renewal", "In the final 6 months of the term"], "MREC Continuing Education Requirements"),
    ("md/licensing", "CE", 3, "Does Maryland recognise post-licensing education?", "No", ["Yes, up to 15 hours", "Yes, for new licensees only", "Yes, if taken in Maryland"], "MREC Continuing Education Requirements"),
    ("md/licensing", "CE", 3, "For a salesperson first licensed on or after 1 October 2023, the first renewal requires:", "15 hours of mandatory topics with no electives and no substitution", ["The standard 15 hours with 4 electives", "30 hours", "No continuing education"], "MREC Continuing Education Requirements, effective 1 October 2025"),
    ("md/licensing", "CE", 3, "Out-of-state continuing education hours may count in Maryland:", "Toward electives only, if that state approves them and permits reverse substitution", ["Toward any requirement", "Never", "Toward the ethics requirement"], "BOP 17-315(a)(3), (4)"),

    # ethics
    ("md/ethics", "Code of Ethics", 2, "A violation of the Maryland Code of Ethics is:", "A ground for Commission discipline", ["A private association matter", "Grounds for a fine only", "Not actionable"], "BOP 17-322(b)(33)"),
    ("md/ethics", "Code of Ethics", 2, "Maryland's required ethics course must discuss:", "The Maryland Code of Ethics, fraudulent real estate practices, and professionalism", ["NAR's Code of Ethics", "Antitrust law only", "Agency law only"], "BOP 17-315(b)(2)(iv)"),
    ("md/ethics", "Disclosure", 2, "The standard for failing to disclose a material fact in Maryland is:", "Intentionally or negligently, as to facts the licensee knows or should know", ["Wilfully only", "Actual knowledge only", "Only where loss results"], "BOP 17-322(b)(4)"),
    ("md/ethics", "Inducements", 2, "Offering a free lot to influence a prospective buyer is:", "A prohibited inducement", ["A permitted promotion", "Permitted if disclosed", "Permitted for subdivisions"], "BOP 17-322(b)(9)(i)"),
    ("md/ethics", "Inducements", 2, "Guaranteeing future resale profits is:", "A ground for discipline", ["Permitted opinion of value", "Permitted with a disclaimer", "Permitted in writing"], "BOP 17-322(b)(8)"),
    ("md/ethics", "Misrepresentation", 2, "Wilfully making a misrepresentation or knowingly making a false promise is:", "A ground for discipline, whether done directly or through another person", ["Actionable only in court", "A ground only if a client suffers loss", "Permitted puffing"], "BOP 17-322(b)(3)"),
    ("md/ethics", "Conduct", 2, "\"Bad faith, incompetency or untrustworthiness\" is:", "An independent ground for discipline", ["Only relevant to the penalty amount", "Not actionable without a loss", "A matter for the courts"], "BOP 17-322(b)(25)"),
    ("md/ethics", "Other licensees", 2, "Participating in a transaction with actual knowledge that another licensee is violating Title 17 is:", "A ground for discipline", ["Only the other licensee's problem", "Actionable only if a client is harmed", "Permitted if reported later"], "BOP 17-322(b)(26)"),
    ("md/ethics", "Other licensees", 3, "Inducing a party to breach a lease negotiated by another licensee to substitute a new one is:", "A ground for discipline", ["Permitted if better for the client", "Permitted after the term starts", "Permitted with written consent"], "BOP 17-322(b)(13)"),
    ("md/ethics", "Other licensees", 2, "Using an association-branded form without being a member is:", "A ground for discipline", ["Permitted if the form is standard", "Permitted on commercial deals", "Permitted with attribution"], "BOP 17-322(b)(17)"),
    ("md/ethics", "Duties", 2, "A Maryland licensee must answer questions:", "Truthfully, for all parties to the transaction", ["Truthfully for the client only", "Only in writing", "Only about the property's condition"], "BOP 17-532(c)(1)(iv)"),
    ("md/ethics", "Conflicts", 2, "An in-house bonus for selling the broker's own listings must be:", "Disclosed to each party", ["Kept internal to the firm", "Reported annually to the Commission", "Split with the buyer"], "BOP 17-530.1"),
]


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
        topics.append({"key": key, "label": label, "portion": "georgia",
                       "weight": n, "blurb": blurb})

    bank = []
    ids = []
    for key, sub, diff, q, right, wrongs, cite in Q:
        choices, ans = _place(key + q, right, wrongs)
        qid = "md-" + hashlib.sha1(q.encode()).hexdigest()[:8]
        ids.append(qid)
        bank.append({"id": qid, "topic": key, "sub": sub, "portion": "georgia",
                     "difficulty": diff, "q": q, "choices": choices,
                     "answer": ans, "why": cite})
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
        "code": "MD", "name": "Maryland", "abbr": "MD",
        "regulator": "Maryland Real Estate Commission",
        "pass": EXAM["pass"],
        "portions": {
            "national": {"scored": EXAM["national_scored"],
                         "minutes": EXAM["national_minutes"],
                         "blurb": "80 items in 90 minutes, 56 correct to pass."},
            "georgia": {"name": "Maryland law", "scored": EXAM["state_scored"],
                        "minutes": EXAM["state_minutes"],
                        "blurb": "30 items in 30 minutes, 21 correct to pass: Title 17, the brokerage relationship sections and the Commission's rules."},
        },
        "topics": topics, "bank": bank, "study": study,
        "sources": SOURCES, "diffs": DIFFS,
    }


# Where Maryland departs from the national rule.
DIFFS = {
    "national/agency": [
        "Dual agency is PERMITTED with the written informed consent of all parties, and the broker must assign TWO INTRA-COMPANY AGENTS, one per side (BOP 17-530.1).",
        "A Maryland INTRA-COMPANY AGENT gives FULL service to their party, including ADVICE ON PRICE AND NEGOTIATION STRATEGY - unlike a transaction broker elsewhere (BOP 17-530.1).",
        "The dual agent and an intra-company agent MAY NOT BE THE SAME PERSON in one transaction (BOP 17-530.1).",
        "The agency disclosure is due NOT LATER THAN THE FIRST SCHEDULED FACE-TO-FACE CONTACT, or through the medium of a non-face-to-face first contact (BOP 17-530).",
        "Confidentiality extends to the BROKER'S past and present clients as well as the licensee's own (BOP 17-532).",
    ],
    "national/practice": [
        "Trust money goes into the trust account within 7 BUSINESS DAYS AFTER BOTH PARTIES ACCEPT the contract of sale (BOP 17-502).",
        "A broker may distribute a disputed deposit only after written notice and a 30-DAY PROTEST WINDOW; a protest forces consummation, written instructions or INTERPLEADER (BOP 17-505).",
        "The GUARANTY FUND pays up to $50,000 PER CLAIM, within 3 YEARS of discovery, for Maryland property (BOP 17-404).",
        "Advertising must carry the licensee's name or designated name AND THE FULL BUSINESS NAME - a LOGO IS NOT ENOUGH (BOP 17-527.2).",
        "Education: a 60-hour salesperson course (broker 135), both exam portions passed WITHIN 1 YEAR of the course, then 15 hours of continuing education each 2-year term with named Maryland topics; NAR ETHICS IS NOT A SUBSTITUTE.",
        "The maximum penalty is $5,000 PER VIOLATION, paid into the GENERAL FUND (BOP 17-322(c)).",
    ],
    "national/disclosures": [
        "A vendor of 1-4 unit residential property delivers EITHER a DISCLOSURE statement OR a DISCLAIMER statement on the Commission's form - and the disclaimer still has to disclose KNOWN LATENT DEFECTS (RP 10-702).",
        "Late delivery gives the purchaser an unconditional right to rescind before receipt or WITHIN 5 DAYS AFTER receipt, with immediate return of deposits; on-time delivery gives NO rescission right (RP 10-702(g), (h)).",
        "The purchaser's 10-702 rights MAY NOT BE WAIVED in the contract; any attempted waiver is VOID (RP 10-702(k)).",
        "A licensee who informs their own party of the 10-702 rights has NO FURTHER DUTIES and is NOT LIABLE under the section (RP 10-702(m)).",
        "A licensee may not REQUIRE a buyer to use a particular title, settlement, escrow, lender or title lawyer in a single-family deal, and the contract must carry the BOLD-FACED right-of-selection notice (BOP 17-607, 17-524).",
    ],
}


if __name__ == "__main__":
    import io, json, os
    here = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    out = os.path.join(here, "greprep", "packs", "MD.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    pack = build()
    with io.open(out, "w", encoding="utf-8") as f:
        json.dump(pack, f, ensure_ascii=False, indent=1, sort_keys=True)
    print("wrote", out, len(pack["bank"]), "questions,", len(pack["study"]), "lessons")
