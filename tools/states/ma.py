"""Massachusetts state content: lessons and practice questions.

Massachusetts splits the salesperson examination. The PSI bulletin's table
gives General 80 questions in 150 minutes and State 40 questions in 90
minutes, 120 and 240 in total, and the bulletin says in terms: "You need
to score a minimum of 70% to pass." A candidate who passes one portion
keeps that pass while the Education Certificate is valid.

The state portion is Massachusetts law and Board rules only, and the
agency rules in 254 CMR 3.00(13) - seller agency, buyer agency, consensual
dual agency, designated agency, sub-agency and the NON-AGENT FACILITATOR -
carry the most marks of anything on it.

Every rule below was read from the official text on 2026-11-10:
  - M.G.L. c. 112, ss. 87RR to 87DDD (brokers and salespersons), from
    malegislature.gov.
  - 254 CMR 3.00, the Board's Professional Standards of Practice, from
    mass.gov.
  - M.G.L. c. 151B s. 4 (unlawful practices), c. 186 s. 15B (security
    deposits), c. 111 s. 197A (lead notification), c. 148 s. 26F (smoke
    detectors on sale).
  - The PSI Massachusetts Candidate Information Bulletin, for the
    examination table and the 40-item state outline.
The section a fact comes from is cited next to it. Do not add a fact here
without reading its source first.
"""

EXAM = {
    # Salesperson: General 80 / 150 minutes, State 40 / 90 minutes, 70% to pass.
    "state_scored": 40,
    "state_minutes": 90,
    "national_scored": 80,
    "national_minutes": 150,
    "pass": 0.70,
}

# PSI's Massachusetts state outline, salesperson item counts, summing to 40.
TOPICS = [
    ("ma/requirements", "Requirements governing licensees", 12,
     "Advertising, affiliation, fees, disclosures, agency relationships, funds."),
    ("ma/fair-housing", "Massachusetts fair housing law", 6,
     "The state's protected classes, the MCAD, accommodations and sanctions."),
    ("ma/consumer", "Consumer protection laws", 5,
     "Property disclosures, misrepresentation, privacy and enforcement."),
    ("ma/landlord", "Landlord and tenant law", 4,
     "What may be collected at move-in, deposits, and the sanitary code."),
    ("ma/licensing", "Requirements for licensing", 3,
     "Who needs a licence, licence types, renewal and Board notifications."),
    ("ma/contracts", "Contracts", 3,
     "Offer to purchase, purchase and sale, leases and representation agreements."),
    ("ma/environment", "Environment & hazardous materials", 3,
     "Lead, Title 5 septic, smoke and carbon monoxide, wetlands."),
    ("ma/board", "Duties & powers of the Board", 2,
     "Examination of records and the sanctions the Board can impose."),
    ("ma/additional", "Additional topics", 2,
     "Condominiums and co-operatives, and legal descriptions."),
]

SOURCES = [
    {"by": "Massachusetts General Court",
     "name": "M.G.L. c. 112, ss. 87RR to 87DDD",
     "note": "The licence law: who must be licensed, education, renewal and the grounds for discipline in 87AAA.",
     "url": "https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXVI/Chapter112"},
    {"by": "Board of Registration of Real Estate Brokers and Salespersons",
     "name": "254 CMR 3.00, Professional Standards of Practice",
     "note": "Advertising, client funds, conflicts of interest and the whole agency-relationship scheme.",
     "url": "https://www.mass.gov/regulations/254-CMR-300-professional-standards-of-practice"},
    {"by": "Massachusetts General Court",
     "name": "M.G.L. c. 151B s. 4, c. 186 s. 15B, c. 111 s. 197A, c. 148 s. 26F",
     "note": "Unlawful practices, security deposits, lead notification and smoke detectors on transfer.",
     "url": "https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXXI/Chapter151B/Section4"},
    {"by": "PSI Services and the Division of Occupational Licensure",
     "name": "Massachusetts Candidate Information Bulletin",
     "note": "General 80 in 150 minutes, State 40 in 90, 70% to pass, and the 40-item state outline.",
     "url": "https://test-takers.psiexams.com/mare"},
]


# --------------------------------------------------------------- lessons

STUDY = {}

STUDY["ma/requirements"] = {
    "summary": "Twelve items, the biggest block, and most of them are 254 CMR 3.00. Massachusetts has five named relationships, and the FACILITATOR - who represents nobody and keeps nothing confidential - is the one people get wrong.",
    "sections": [
        {"h": "The agency disclosure notice (254 CMR 3.00(13)(a))",
         "l": ["A broker or salesperson must give a prospective PURCHASER OR SELLER the Board's notice disclosing the licensee's relationship with them, AT THE TIME OF THE FIRST PERSONAL MEETING FOR THE PURPOSE OF DISCUSSING A SPECIFIC PROPERTY.",
               "The licensee must ASK the consumer to sign and date it, give the ORIGINAL to the consumer, and keep a copy FOR THREE YEARS. The licensee must also sign, state whether they are a BROKER OR SALESPERSON, give their LICENCE NUMBER, and date it.",
               "If the consumer DECLINES TO SIGN, the licensee notes the date it was given and that they declined, and keeps that notice for THREE YEARS.",
               "No written notice is required for each person who comes to an OPEN HOUSE, provided the licensee CONSPICUOUSLY DISCLOSES any pre-existing agency relationship by SIGN, POSTER, LISTING LITERATURE OR PROPERTY DESCRIPTION FORM - and where literature is distributed at an open house the agency disclosure in it must be MORE CONSPICUOUS than any other written material.",
               "All such records and notices are SUBJECT TO INSPECTION by the Board."],
         "check": [("The Massachusetts agency disclosure notice must be given:", "At the first personal meeting to discuss a specific property", ["At the first telephone call", "With the offer", "At closing"], "254 CMR 3.00(13)(a)."),
                   ("If the consumer refuses to sign the notice, the licensee:", "Notes the date given and the refusal, and keeps it for three years", ["Cannot proceed", "Discards it"], "254 CMR 3.00(13)(a)2."),
                   ("At an open house, no individual written notice is needed if:", "A sign, poster or listing literature conspicuously discloses any pre-existing agency relationship", ["Visitors sign in", "The seller is present"], "254 CMR 3.00(13)(a)3."),
                   ("Agency notices must be retained for:", "Three years from the date on the notice", ["One year", "Six years"], "254 CMR 3.00(13)(a)1.")]},
        {"h": "Consensual dual agency (254 CMR 3.00(13)(b))",
         "l": ["It applies to the purchase or sale of land with a building intended for ONE TO FOUR RESIDENTIAL UNITS, or land on which a ONE OR TWO UNIT dwelling is to be built.",
               "A licensee may act for BOTH seller and buyer only with INFORMED WRITTEN CONSENT FROM BOTH, on a written consent form.",
               "The form must say the dual agent ASSISTS both but SHALL BE NEUTRAL as to any conflicting interest - so the dual agent CANNOT FULLY SATISFY the duties of LOYALTY, FULL DISCLOSURE, REASONABLE CARE AND OBEDIENCE TO LAWFUL INSTRUCTIONS, but STILL OWES CONFIDENTIALITY OF MATERIAL INFORMATION AND THE DUTY TO ACCOUNT FOR FUNDS.",
               "Confidential material information may NOT be disclosed except where (1) disclosure is EXPRESSLY AUTHORISED, (2) it is REQUIRED BY LAW, (3) it is intended to PREVENT ILLEGAL CONDUCT, or (4) it is necessary to PROSECUTE OR DEFEND A CLAIM. Confidentiality CONTINUES AFTER the relationship ends.",
               "There is a CONCLUSIVE PRESUMPTION of consent where the consumer has signed a form containing the regulation's description. Consent can come in the LISTING AGREEMENT, a BUYER REPRESENTATION AGREEMENT, or a separate document before or after a transaction is identified - but where it was given IN ADVANCE, the licensee must also give WRITTEN NOTICE of dual agency once a transaction is identified, BEFORE the parties enter a written purchase and sale agreement."],
         "check": [("A Massachusetts dual agent still owes:", "Confidentiality of material information and the duty to account for funds", ["Full loyalty to the seller", "Undivided loyalty to both"], "254 CMR 3.00(13)(b)."),
                   ("Dual agency requires:", "Informed written consent from both seller and buyer", ["Oral consent", "The broker's decision"], "254 CMR 3.00(13)(b)."),
                   ("Confidential information may be disclosed where:", "Disclosure is expressly authorised, required by law, intended to prevent illegal conduct, or needed to prosecute or defend a claim", ["The deal has closed", "The other agent asks"], "254 CMR 3.00(13)(b)."),
                   ("Where consent was given in advance, written notice of dual agency must be given:", "Before the parties enter a written purchase and sale agreement", ["At closing", "Within 30 days"], "254 CMR 3.00(13)(b)2."),
                   ("The duty of confidentiality:", "Continues after the brokerage relationship ends", ["Ends at closing", "Ends when the listing expires"], "254 CMR 3.00(13)(b).")]},
        {"h": "Designated agency (254 CMR 3.00(13)(c))",
         "l": ["A broker may APPOINT one or more affiliated licensees to represent the seller, or the buyer, with that party's WRITTEN CONSENT after being advised of three things.",
               "(a) The designated agent WILL represent them and owes LOYALTY, FULL DISCLOSURE, CONFIDENTIALITY, THE DUTY TO ACCOUNT FOR FUNDS, REASONABLE CARE AND OBEDIENCE TO LAWFUL INSTRUCTIONS.",
               "(b) ALL OTHER licensees affiliated with the appointing broker will NOT represent them, do NOT owe those duties, and MAY REPRESENT THE OTHER SIDE.",
               "(c) If designated agents of the SAME broker represent both sides, THE APPOINTING BROKER IS A DUAL AGENT and neutral as to conflicting interests, but still owes BOTH confidentiality of material information and the duty to account for funds.",
               "Where both parties consent to designated agency, a SEPARATE CONSENT TO DUAL AGENCY OF THE APPOINTING BROKER IS NOT REQUIRED.",
               "A designated agent EXCLUSIVELY represents their party and may NOT share known or acquired information with any other agent or person where it would HARM that party - EXCEPT KNOWN MATERIAL DEFECTS, which they have an AFFIRMATIVE OBLIGATION to disclose.",
               "Appointing a designated agent does NOT LIMIT the appointing broker's liability for the designated agent's breach of duty."],
         "check": [("Where two designated agents of one Massachusetts broker take opposite sides:", "The appointing broker is a dual agent, neutral but still owing confidentiality and accounting", ["Both agents become dual agents", "The arrangement is prohibited"], "254 CMR 3.00(13)(c)."),
                   ("Where both parties have consented to designated agency:", "A separate consent to the appointing broker's dual agency is not required", ["Separate dual agency consent is still required", "The deal cannot proceed"], "254 CMR 3.00(13)(c)."),
                   ("A designated agent must still disclose:", "Known material defects in the real property", ["Their client's lowest price", "Their client's motivation"], "254 CMR 3.00(13)(c)1."),
                   ("Appointing a designated agent:", "Does not limit the appointing broker's liability for that agent's breach of duty", ["Shifts all liability to the designated agent", "Ends the broker's duties"], "254 CMR 3.00(13)(c)2.")]},
        {"h": "Facilitator and sub-agency",
         "l": ["A NON-AGENT FACILITATOR works with a seller or buyer WITHOUT representing them as a sole, designated or dual agent, on WRITTEN NOTICE stating that NO AGENCY RELATIONSHIP EXISTS. The notice is given AT THE FIRST PERSONAL MEETING TO DISCUSS A SPECIFIC PROPERTY.",
               "A facilitator owes a duty to PRESENT ALL REAL PROPERTY HONESTLY AND ACCURATELY, to DISCLOSE KNOWN MATERIAL DEFECTS and to ACCOUNT FOR FUNDS - but has NO DUTY OF CONFIDENTIALITY as to anything received from the seller or buyer.",
               "A facilitator may also be called a TRANSACTION BROKER, and the relationship MAY BE CHANGED to an agency relationship by WRITTEN AGREEMENT of the person represented (254 CMR 3.00(13)(e)).",
               "SUB-AGENCY: no licensee may agree with another to represent a seller or buyer as a SECONDARY OR SUB-AGENT without first INFORMING THAT PARTY IN WRITING that the sub-agent's actions may subject them to VICARIOUS LIABILITY, and obtaining their CONSENT on that notice. The notice is given at the execution of the listing, or when the agent and buyer agree the agent will represent them (254 CMR 3.00(13)(d))."],
         "check": [("A Massachusetts facilitator:", "Represents neither party and owes no duty of confidentiality", ["Is a kind of dual agent", "Owes loyalty to the seller"], "254 CMR 3.00(13)(e)."),
                   ("A facilitator still owes the duty to:", "Present property honestly, disclose known material defects and account for funds", ["Keep the buyer's top price secret", "Negotiate for the seller"], "254 CMR 3.00(13)(e)."),
                   ("A facilitator relationship may become an agency relationship:", "By written agreement of the person represented", ["Automatically at the offer", "Never"], "254 CMR 3.00(13)(e)."),
                   ("Before offering sub-agency, a licensee must disclose in writing:", "That the sub-agent's acts may subject the client to vicarious liability", ["The sub-agent's commission", "The sub-agent's licence number"], "254 CMR 3.00(13)(d).")]},
        {"h": "Client funds (254 CMR 3.00(10))",
         "l": ["Unless the parties AGREE OTHERWISE IN WRITING, all money of whatever kind paid to a broker to hold during the pendency of a transaction must be IMMEDIATELY DEPOSITED IN A BANK ESCROW ACCOUNT, and the broker is responsible for it until the transaction is CONSUMMATED OR TERMINATED, when a proper account and distribution is made.",
               "An escrow account holds OTHER PARTIES' money in which THE BROKER HAS NO CLAIM. It may be interest or non-interest bearing; if interest bearing the broker must ACCOUNT FOR THE INTEREST at consummation or termination.",
               "Records must show the DATE and FROM WHOM the money came, the DATE DEPOSITED with the SOURCE and CHECK NUMBER, the DATE OF WITHDRAWAL with the NAME of the person receiving it, FOR WHOSE ACCOUNT it is deposited and TO WHOM IT BELONGS. A COPY OF EACH CHECK in and out must be kept for THREE YEARS.",
               "A SALESPERSON SHALL NEVER HOLD CLIENT FUNDS: a salesperson or a broker engaged by another broker must IMMEDIATELY TURN OVER all deposit money to the employing broker.",
               "COMMINGLING the money or property of a principal with the licensee's own is a statutory ground for discipline (M.G.L. c. 112 s. 87AAA(h)), as is failing within a reasonable time to ACCOUNT FOR OR REMIT money belonging to others (s. 87AAA(d))."],
         "check": [("Deposit money paid to a Massachusetts broker must be:", "Immediately deposited in a bank escrow account, unless the parties agree otherwise in writing", ["Deposited within 3 business days", "Held by the salesperson"], "254 CMR 3.00(10)(a)."),
                   ("May a Massachusetts salesperson hold client funds?", "No; they must immediately turn them over to the employing broker", ["Yes, for up to 48 hours", "Yes, with the broker's consent"], "254 CMR 3.00(10)(c)."),
                   ("Copies of escrow account cheques must be kept for:", "Three years from the date of issuance", ["One year", "Six years"], "254 CMR 3.00(10)(b)."),
                   ("An escrow account is one in which the broker:", "Has no claim to the money", ["May keep the interest", "May borrow short term"], "254 CMR 3.00(10)(a).")]},
        {"h": "Advertising, fees and conflicts",
         "l": ["A broker may NOT advertise in any way that is FALSE OR MISLEADING. Every advertisement must AFFIRMATIVELY DISCLOSE that the advertiser is a REAL ESTATE BROKER and must INCLUDE THE BROKER'S NAME - an advertisement showing only a post office box, telephone, fax, email or street address is prohibited (254 CMR 3.00(9)(a)).",
               "SALESPEOPLE ARE PROHIBITED from advertising the purchase, sale, rental or exchange of any real property UNDER THEIR OWN NAME (254 CMR 3.00(9)(b)).",
               "DISCRIMINATORY advertising, direct or indirect, is prohibited (254 CMR 3.00(9)(c)).",
               "A licensee may not buy, sell, rent or represent a client in a property in which the licensee OR THEIR KIN has a PERSONAL FINANCIAL INTEREST unless they FULLY DISCLOSE IT IN WRITING to all parties and get WRITTEN ACKNOWLEDGMENT (254 CMR 3.00(11)(a)).",
               "A broker may not take an OPTION on property they were approached to broker without FIRST DISCLOSING that they are now a prospective purchaser and NO LONGER ACTING AS BROKER (254 CMR 3.00(11)(b)).",
               "A NET LISTING - where the commission is unspecified and the broker keeps any excess over a stated price - may NOT be accepted (254 CMR 3.00(11)(c); M.G.L. c. 112 s. 87AAA(l)).",
               "ALL OFFERS must be CONVEYED FORTHWITH to the owner (254 CMR 3.00(11)(d)), and no licensee may ADVISE AGAINST THE USE OF AN ATTORNEY in any real property transaction (254 CMR 3.00(12)).",
               "A salesperson may be affiliated with ONLY ONE BROKER at a time, may not run their own real estate business, and may accept a fee or commission FROM NO ONE BUT THEIR LICENSED BROKER (M.G.L. c. 112 s. 87RR). Paying or dividing fees with an UNLICENSED person is a ground for discipline (s. 87AAA(e))."],
         "check": [("A Massachusetts salesperson advertising a listing:", "May not advertise under their own name", ["May use their own name with the broker's consent", "Must use only their own name"], "254 CMR 3.00(9)(b)."),
                   ("Every broker advertisement must:", "Include the broker's name and affirmatively disclose that the advertiser is a real estate broker", ["Show a telephone number only", "Show the licence number"], "254 CMR 3.00(9)(a)."),
                   ("A net listing in Massachusetts is:", "Prohibited", ["Allowed with written consent", "Allowed on commercial property"], "254 CMR 3.00(11)(c); c. 112 s. 87AAA(l)."),
                   ("A salesperson may accept a commission from:", "Their own licensed broker only", ["The seller directly", "Any licensed broker"], "M.G.L. c. 112 s. 87RR."),
                   ("Advising a buyer against hiring an attorney is:", "Prohibited", ["Allowed if the deal is simple", "Required for cash sales"], "254 CMR 3.00(12)."),
                   ("Offers received must be:", "Conveyed forthwith to the owner", ["Held until the weekend", "Screened by the broker"], "254 CMR 3.00(11)(d).")]},
    ],
    "traps": [
        "The disclosure comes at the FIRST PERSONAL MEETING to discuss a SPECIFIC PROPERTY - not the first phone call.",
        "A facilitator owes NO confidentiality. A dual agent owes confidentiality but not full loyalty.",
        "Designated agency makes the APPOINTING BROKER the dual agent, and no extra dual agency consent is needed.",
        "Salespeople never hold client funds and never advertise in their own name.",
        "Three years is the Massachusetts retention period for agency notices and escrow cheques.",
    ],
    "vocab": [
        ["Facilitator", "A licensee who represents neither party; also called a transaction broker."],
        ["Designated agent", "An affiliated licensee appointed to represent one party exclusively."],
        ["Appointing broker", "The broker who designates agents and becomes the dual agent."],
        ["Vicarious liability", "The client's exposure for a sub-agent's acts, which must be disclosed."],
        ["Net listing", "A listing with an unspecified commission. Prohibited."],
    ],
    "examples": [
        {"t": "One firm, both sides",
         "s": "Your brokerage lists a three-family and another agent in your office brings the buyer. Both parties signed designated agency consents.",
         "w": ["Each designated agent exclusively represents their own party and owes that party the full duties.",
               "The APPOINTING BROKER is the dual agent - neutral, but still owing both sides confidentiality and accounting.",
               "No separate consent to the broker's dual agency is needed, because both parties consented to designated agency."],
         "k": "Designated agency splits the agents and parks the dual agency with the broker."},
    ],
}

STUDY["ma/fair-housing"] = {
    "summary": "Six items on one statute. Massachusetts protects classes the federal Act does not, and public assistance recipiency is the one most often tested.",
    "sections": [
        {"h": "The protected classes (M.G.L. c. 151B s. 4(6))",
         "p": ["It is an unlawful practice for the owner, lessee, sublessee, LICENSED REAL ESTATE BROKER, assignee or managing agent of publicly assisted, multiple dwelling or contiguously located housing - or any organisation of unit owners in a CONDOMINIUM OR HOUSING CO-OPERATIVE - to refuse to rent, lease, sell or negotiate, or otherwise to deny or withhold such accommodations, because of:"],
         "l": ["RACE", "RELIGIOUS CREED", "COLOR", "NATIONAL ORIGIN", "SEX",
               "GENDER IDENTITY", "SEXUAL ORIENTATION", "AGE",
               "GENETIC INFORMATION", "ANCESTRY", "MARITAL STATUS",
               "BEING A VETERAN OR MEMBER OF THE ARMED FORCES",
               "BEING BLIND, HEARING IMPAIRED, OR HAVING ANY OTHER HANDICAP",
               "Advertising is separately covered: no notice, statement or advertisement about the sale or rental of covered housing may indicate a preference, limitation or discrimination based on race, color, religion, sex, gender identity, sexual orientation, national origin, genetic information, ancestry, CHILDREN, marital status, PUBLIC ASSISTANCE RECIPIENCY or handicap (s. 4(7B)).",
               "It is also unlawful for any person to COERCE, INTIMIDATE, THREATEN OR INTERFERE with another's exercise of a right under the chapter, or to AID, ABET, INCITE, COMPEL OR COERCE any prohibited act (s. 4(4A), 4(5))."],
         "check": [("Which is protected in Massachusetts housing but not by the federal Fair Housing Act?", "Marital status", ["Race", "Color", "National origin"], "M.G.L. c. 151B s. 4(6)."),
                   ("Massachusetts also protects:", "Veterans and members of the armed forces", ["Credit score", "Occupation"], "M.G.L. c. 151B s. 4(6)."),
                   ("Discriminatory advertising in Massachusetts may not indicate a preference based on, among others:", "Children and public assistance recipiency", ["Length of employment", "Pet ownership"], "M.G.L. c. 151B s. 4(7B)."),
                   ("Helping someone else commit a discriminatory act is:", "Itself an unlawful practice", ["Not actionable", "A civil matter only"], "M.G.L. c. 151B s. 4(5)."),
                   ("Age is:", "A Massachusetts protected class in housing", ["Protected only in employment", "Not protected"], "M.G.L. c. 151B s. 4(6).")]},
        {"h": "Consequences for a licensee",
         "l": ["The outline covers the MASSACHUSETTS COMMISSION AGAINST DISCRIMINATION (MCAD), which investigates and decides discrimination complaints.",
               "Where MCAD has made a FINAL FINDING that a licensee committed an unlawful practice under c. 151B arising out of their occupation, the BOARD SHALL suspend that licence for a period of NINETY DAYS (M.G.L. c. 112 s. 87AAA).",
               "BLOCKBUSTING: affirmatively soliciting the sale, lease or listing of residential property on the grounds of an alleged CHANGE OF VALUE due to the presence or prospective entry of persons of another RACE, ECONOMIC LEVEL, RELIGION OR ETHNIC ORIGIN - or distributing material designed to induce an owner to sell for that reason - is a ground for discipline AND a crime punishable by a fine of NOT LESS THAN $1,000 AND NOT MORE THAN $2,500, or imprisonment for NOT MORE THAN SIX MONTHS, or both (s. 87AAA(k)).",
               "The outline also covers the ADA and other accommodations, including ACCESSIBILITY, SERVICE ANIMALS and EMOTIONAL SUPPORT ANIMALS."],
         "check": [("After a final MCAD finding of discrimination against a licensee, the Board:", "Shall suspend the licence for ninety days", ["May issue a warning", "Must revoke the licence"], "M.G.L. c. 112 s. 87AAA."),
                   ("Blockbusting in Massachusetts carries a fine of:", "Not less than $1,000 and not more than $2,500, or up to six months' imprisonment, or both", ["Up to $500", "Up to $10,000"], "M.G.L. c. 112 s. 87AAA(k)."),
                   ("The agency that investigates housing discrimination complaints is:", "The Massachusetts Commission Against Discrimination", ["The Board of Registration", "The Attorney General's office"], "Named on the Massachusetts state outline.")]},
    ],
    "traps": [
        "Marital status, age, veteran status and public assistance recipiency are the Massachusetts additions.",
        "The ninety-day suspension after an MCAD finding is MANDATORY - the statute says shall.",
        "Blockbusting is both a licence violation and a criminal offence here.",
    ],
    "vocab": [
        ["MCAD", "The Massachusetts Commission Against Discrimination."],
        ["Publicly assisted housing", "Housing covered by c. 151B's housing provisions."],
        ["Blockbusting", "Soliciting sales on the grounds of a neighbourhood's changing composition."],
        ["Public assistance recipiency", "A protected basis in Massachusetts housing advertising."],
    ],
    "examples": [],
}

STUDY["ma/consumer"] = {
    "summary": "Five items. Massachusetts is a CAVEAT EMPTOR state for the seller, but the licensee's own duty to disclose known material defects is real and is the line candidates must hold.",
    "sections": [
        {"h": "Disclosure and misrepresentation",
         "l": ["Massachusetts has NO general seller's disclosure form by statute - the state exam tests the licensee's duties instead. A licensee must act HONESTLY AND ETHICALLY and in the client's best interests at all times (254 CMR 3.00(11)).",
               "A DESIGNATED AGENT and a FACILITATOR both have an AFFIRMATIVE OBLIGATION to disclose KNOWN MATERIAL DEFECTS in the property (254 CMR 3.00(13)(c)1., (e)).",
               "KNOWINGLY MAKING ANY SUBSTANTIAL MISREPRESENTATION is a ground for suspension or revocation (M.G.L. c. 112 s. 87AAA(a)), as is obtaining a licence by FALSE OR FRAUDULENT REPRESENTATION.",
               "The outline names STIGMATIZED PROPERTIES, RADON and MOLD among the property disclosure topics, along with material defects.",
               "A licensee must give BOTH the buyer and the seller a COPY OF THE PURCHASE AND SALE AGREEMENT; failing to do so is a ground for discipline (s. 87AAA(i))."],
         "check": [("Failing to give both buyer and seller a copy of the purchase and sale agreement is:", "A ground for suspension or revocation", ["Good practice only", "A civil matter"], "M.G.L. c. 112 s. 87AAA(i)."),
                   ("A Massachusetts facilitator who knows the roof leaks must:", "Disclose that known material defect", ["Stay silent, having no agency duties", "Tell only the seller"], "254 CMR 3.00(13)(e)."),
                   ("Knowingly making a substantial misrepresentation is:", "A ground for the Board to suspend or revoke the licence", ["Actionable only in court", "A warning offence"], "M.G.L. c. 112 s. 87AAA(a).")]},
        {"h": "Conflicts, options and dealings",
         "l": ["ACTING IN THE DUAL CAPACITY OF BROKER AND UNDISCLOSED PRINCIPAL in the same transaction is a ground for discipline (s. 87AAA(b)), as is ACTING FOR MORE THAN ONE PARTY WITHOUT THE KNOWLEDGE AND CONSENT of all parties for whom the licensee acts (s. 87AAA(c)).",
               "Accepting, giving or charging any UNDISCLOSED COMMISSION, REBATE OR PROFIT on expenditures for a principal is a ground (s. 87AAA(f)).",
               "INDUCING a party to BREAK a contract or lease for the licensee's PERSONAL GAIN is a ground (s. 87AAA(g)).",
               "Conviction of a CRIMINAL OFFENCE showing a lack of good moral character is a ground for suspension, revocation or refusal to renew.",
               "The outline also names PRIVACY, specifically the WRITTEN INFORMATION SECURITY POLICY (WISP) Massachusetts requires of those holding personal information."],
         "check": [("A broker buying a listed property without disclosing they are the principal is:", "Acting as broker and undisclosed principal, a ground for discipline", ["Permitted if the price is fair", "A private matter"], "M.G.L. c. 112 s. 87AAA(b)."),
                   ("Taking an undisclosed rebate on expenditures made for a principal is:", "A ground for discipline", ["Allowed if under $100", "Standard practice"], "M.G.L. c. 112 s. 87AAA(f)."),
                   ("Persuading a tenant to break a lease so the licensee can earn a fee is:", "A ground for discipline", ["Legitimate business", "Allowed with notice"], "M.G.L. c. 112 s. 87AAA(g)."),
                   ("A WISP is:", "A Written Information Security Policy for personal information", ["A Water Infiltration Site Plan", "A wetlands permit"], "Named on the Massachusetts state outline.")]},
    ],
    "traps": [
        "There is no statutory seller's disclosure form here; the duty falls on the LICENSEE to disclose known material defects.",
        "Both copies of the purchase and sale agreement must go out, or it is a discipline ground.",
        "Undisclosed principal and undisclosed rebate are two separate grounds.",
    ],
    "vocab": [
        ["Material defect", "A known physical problem a licensee must disclose."],
        ["Stigmatized property", "Property affected by events rather than condition."],
        ["Undisclosed principal", "A licensee secretly dealing for their own account."],
        ["WISP", "The written information security policy protecting personal data."],
    ],
    "examples": [],
}

STUDY["ma/landlord"] = {
    "summary": "Four items, and the exam loves the move-in list: Massachusetts limits exactly what a landlord may collect before a tenancy starts.",
    "sections": [
        {"h": "What may be collected at move-in (M.G.L. c. 186 s. 15B(1)(b))",
         "p": ["At or prior to the commencement of a tenancy, no lessor or agent may require a tenant to pay anything in excess of:"],
         "l": ["RENT FOR THE FIRST FULL MONTH of occupancy;",
               "RENT FOR THE LAST FULL MONTH, calculated at the same rate as the first;",
               "A SECURITY DEPOSIT EQUAL TO THE FIRST MONTH'S RENT, provided it is deposited as the section requires and the tenant is given the STATEMENT OF CONDITION; and",
               "THE PURCHASE AND INSTALLATION COST FOR A KEY AND LOCK.",
               "Nothing else - no 'broker fee' charged by the landlord beyond this list, no pet deposit, no last-plus-extra.",
               "No lease may impose interest or a penalty for unpaid rent UNTIL THIRTY DAYS AFTER the rent was due (s. 15B(1)(c)), and no lessor may later demand rent in advance in excess of the CURRENT MONTH'S RENT (s. 15B(1)(d))."],
         "check": [("At move-in a Massachusetts landlord may collect:", "First month, last month, a security deposit of one month, and the cost of a key and lock", ["Any amount the lease states", "First, last and two months' deposit"], "M.G.L. c. 186 s. 15B(1)(b)."),
                   ("The security deposit may not exceed:", "The first month's rent", ["Two months' rent", "1.5 months' rent"], "M.G.L. c. 186 s. 15B(1)(b)(iii)."),
                   ("A lease may impose a late penalty only:", "After thirty days from the date the rent was due", ["After five days", "Immediately"], "M.G.L. c. 186 s. 15B(1)(c).")]},
        {"h": "Holding the deposit (s. 15B(2), (3))",
         "l": ["A security deposit CONTINUES TO BE THE PROPERTY OF THE TENANT.",
               "It must be held in a SEPARATE, INTEREST-BEARING ACCOUNT IN A BANK LOCATED WITHIN THE COMMONWEALTH, on terms placing it BEYOND THE CLAIM OF THE LESSOR'S CREDITORS - including a foreclosing mortgagee or trustee in bankruptcy - and providing for TRANSFER TO A SUBSEQUENT OWNER.",
               "A RECEIPT must be given WITHIN THIRTY DAYS of the deposit, naming the BANK AND ITS LOCATION, the AMOUNT and the ACCOUNT NUMBER. Failure entitles the tenant to IMMEDIATE RETURN of the deposit.",
               "A receipt must also be given AT THE TIME the deposit is received, showing the AMOUNT, the NAME of the person receiving it and, for an agent, the LESSOR'S NAME.",
               "LAST MONTH'S RENT held in advance earns interest at FIVE PER CENT PER YEAR, or the lesser rate actually received from the bank, from the FIRST DAY OF TENANCY.",
               "If the lessor fails to pay interest due WITHIN THIRTY DAYS AFTER THE TENANCY ENDS, the tenant is awarded THREE TIMES that interest plus costs and reasonable attorney's fees.",
               "Deposit records must be kept for TWO YEARS from the termination of the tenancy.",
               "The outline also covers the STATE SANITARY CODE, the standard of habitability for Massachusetts rentals."],
         "check": [("A Massachusetts security deposit must be held:", "In a separate interest-bearing account in a bank located within the Commonwealth", ["In the landlord's operating account", "By the broker"], "M.G.L. c. 186 s. 15B(3)(a)."),
                   ("A receipt naming the bank and account number must be given within:", "Thirty days of the deposit being received", ["Ten days", "At the end of the tenancy"], "M.G.L. c. 186 s. 15B(3)(a)."),
                   ("Last month's rent paid in advance earns interest at:", "Five per cent per year, or the lesser rate the bank actually paid", ["No interest", "Ten per cent"], "M.G.L. c. 186 s. 15B(2)(b)."),
                   ("A lessor who fails to pay interest within thirty days of the tenancy ending owes:", "Three times the interest, plus costs and reasonable attorney's fees", ["The interest only", "Nothing"], "M.G.L. c. 186 s. 15B(2)(b)."),
                   ("Security deposit records must be kept for:", "Two years from the termination of the tenancy", ["Three years", "Six years"], "M.G.L. c. 186 s. 15B(2).")]},
    ],
    "traps": [
        "Four things at move-in, and the fourth is the KEY AND LOCK cost - not a pet fee.",
        "The deposit is the TENANT'S property and must sit in a Massachusetts bank.",
        "Triple damages for unpaid interest after the tenancy ends.",
    ],
    "vocab": [
        ["Statement of condition", "The move-in condition record the tenant must receive."],
        ["Tenancy at will", "A tenancy with no fixed term, named on the outline."],
        ["State Sanitary Code", "Massachusetts' habitability standard for rental housing."],
        ["Last month's rent", "Rent collected in advance, which earns 5% interest."],
    ],
    "examples": [],
}

STUDY["ma/licensing"] = {
    "summary": "Three items. The numbers: 40 classroom hours, a two-year licence, and 12 hours of continuing education.",
    "sections": [
        {"h": "Getting licensed (M.G.L. c. 112 ss. 87SS, 87TT)",
         "l": ["A SALESPERSON applicant must pass a written examination and, as a PREREQUISITE TO TAKING IT, submit proof of Board-approved courses totalling 40 CLASSROOM HOURS. Someone who completed a REAL PROPERTY course at an accredited Massachusetts law school may also sit.",
               "A BROKER applicant must show they have been ACTIVELY ASSOCIATED WITH A REAL ESTATE BROKER AS A SALESPERSON FOR THREE YEARS and completed an ADDITIONAL 40 CLASSROOM HOURS.",
               "A resident applying for a BROKER'S licence must have had their PRINCIPAL PLACE OF ABODE IN MASSACHUSETTS FOR ONE YEAR before issuance. An ATTORNEY AT LAW of the Commonwealth is exempt from BOTH the examination and that residency requirement.",
               "Every applicant must furnish evidence of GOOD MORAL CHARACTER - for a corporation or partnership, for all officers, directors or partners.",
               "No application may be acted on until it has been ON FILE WITH THE BOARD AT LEAST TEN DAYS, and NO BROKER'S LICENCE may be issued to anyone UNDER EIGHTEEN.",
               "The bulletin adds that a candidate must APPLY FOR AND PASS the examination WITHIN TWO YEARS of completing the required education."],
         "check": [("Prelicence education for a Massachusetts salesperson is:", "40 classroom hours", ["24 hours", "75 hours", "60 hours"], "M.G.L. c. 112 s. 87SS."),
                   ("A Massachusetts broker applicant must have been a salesperson for:", "Three years, plus an additional 40 classroom hours", ["One year", "Two years with no extra hours"], "M.G.L. c. 112 s. 87SS."),
                   ("Who is exempt from the Massachusetts licensing examination?", "An attorney at law of the Commonwealth", ["Any out-of-state broker", "A licensed appraiser"], "M.G.L. c. 112 s. 87SS."),
                   ("The minimum age for a Massachusetts broker's licence is:", "18", ["21", "17", "There is none"], "M.G.L. c. 112 s. 87TT."),
                   ("An application must be on file with the Board for at least:", "Ten days", ["Thirty days", "Five business days"], "M.G.L. c. 112 s. 87TT.")]},
        {"h": "Keeping the licence (ss. 87XX, 87XX 1/2; 254 CMR 3.00)",
         "l": ["A licence is VALID FOR TWO YEARS from the date of issue unless sooner suspended or revoked, and is RENEWED BIENNIALLY WITHOUT EXAMINATION on payment of the fee. The bulletin notes the ISSUE DATE is the date the candidate passed, and the EXPIRATION DATE is the licensee's DATE OF BIRTH.",
               "A corporation's or partnership's licence is renewed ONLY IF at least one of its designated officers or partners renews their individual licence.",
               "CONTINUING EDUCATION: within the TWENTY-FOUR MONTHS before each renewal a licensee must complete Board-approved courses totalling NO LESS THAN SIX AND NO MORE THAN TWELVE HOURS, as the Board determines. At least SIX of those hours must concern COMPLIANCE WITH LAWS AND REGULATIONS, drawn from fair housing, equal employment opportunity, ACCESSIBILITY FOR THE DISABLED, AGENCY LAW, environmental issues, zoning and building codes, appraisal and financing, property tax assessment and valuation, and REAL ESTATE BOARD REGULATIONS.",
               "A SALESPERSON may be affiliated with only ONE broker at a time and may NOT operate their own real estate business (M.G.L. c. 112 s. 87RR; 254 CMR 3.00(5), (6)).",
               "Every broker and salesperson must give the Board WRITTEN NOTICE of their CURRENT BUSINESS AND RESIDENTIAL ADDRESS AT ALL TIMES (254 CMR 3.00(1)), and must NOTIFY THE BOARD OF AFFILIATION (254 CMR 3.00(7)). The licence must be DISPLAYED (254 CMR 3.00(4)).",
               "The outline also lists ACTIVE, INACTIVE AND EXPIRED licence status and Board notifications of DISCIPLINARY ACTION and CRIMINAL CONVICTIONS."],
         "check": [("A Massachusetts real estate licence is valid for:", "Two years from the date of issue", ["One year", "Three years", "Five years"], "M.G.L. c. 112 s. 87XX."),
                   ("Continuing education must be completed:", "Within the twenty-four months before each renewal", ["In the renewal month", "At any time in the licensee's career"], "M.G.L. c. 112 s. 87XX 1/2."),
                   ("Of the continuing education hours, at least six must cover:", "Compliance with laws and regulations, such as fair housing, agency law and Board regulations", ["Sales technique", "Marketing"], "M.G.L. c. 112 s. 87XX 1/2."),
                   ("A Massachusetts salesperson may be affiliated with:", "One broker at a time", ["Two brokers", "Any number of brokers"], "M.G.L. c. 112 s. 87RR."),
                   ("Licensees must keep the Board informed of:", "Their current business and residential address at all times", ["Their commission rates", "Their listing inventory"], "254 CMR 3.00(1).")]},
    ],
    "traps": [
        "40 hours for a salesperson, another 40 plus three years for a broker.",
        "The licence expires on the licensee's BIRTHDAY, two years after passing.",
        "The statute sets a RANGE of 6 to 12 continuing education hours, with at least 6 on compliance subjects.",
        "Attorneys of the Commonwealth skip the exam and the residency requirement.",
    ],
    "vocab": [
        ["Classroom hours", "The unit Massachusetts counts prelicence education in."],
        ["Good moral character", "A statutory condition of licensure here."],
        ["Affiliation", "A salesperson's link to one broker, notifiable to the Board."],
        ["Inactive status", "A licence not currently in use."],
    ],
    "examples": [],
}

STUDY["ma/contracts"] = {
    "summary": "Three items. Massachusetts runs on a two-document sale - the Offer to Purchase, then the Purchase and Sale Agreement - and the licensee must get copies to everyone.",
    "sections": [
        {"h": "The two-document sale",
         "l": ["The OFFER TO PURCHASE comes first and, once accepted, is itself a binding contract. The PURCHASE AND SALE AGREEMENT follows and supersedes it, usually after inspections and attorney review.",
               "ALL OFFERS submitted to a licensee for property they have a right to sell or rent must be CONVEYED FORTHWITH to the owner (254 CMR 3.00(11)(d)).",
               "The licensee must give BOTH the buyer and the seller a COPY OF THE PURCHASE AND SALE AGREEMENT; failing to do so is a statutory ground for discipline (M.G.L. c. 112 s. 87AAA(i)).",
               "No licensee may ADVISE AGAINST THE USE OF AN ATTORNEY in any real property transaction (254 CMR 3.00(12)) - which matters because Massachusetts is an attorney-closing state.",
               "The outline also covers LEASES, naming FIXED TERM and TENANCY AT WILL, plus LANDLORD AND TENANT REPRESENTATION AGREEMENTS, SELLER AND BUYER REPRESENTATION AGREEMENTS, and FACILITATION AGREEMENTS."],
         "check": [("In Massachusetts the document that comes first in a sale is:", "The offer to purchase", ["The purchase and sale agreement", "The deed"], "Named on the Massachusetts state outline."),
                   ("A licensee must give a copy of the purchase and sale agreement to:", "Both the buyer and the seller", ["The buyer only", "Whoever asks"], "M.G.L. c. 112 s. 87AAA(i)."),
                   ("Advising a client not to hire an attorney is:", "Prohibited", ["Allowed for simple sales", "Required to save time"], "254 CMR 3.00(12)."),
                   ("A tenancy with no fixed end date is:", "A tenancy at will", ["A fixed term lease", "A licence"], "Named on the Massachusetts state outline.")]},
        {"h": "Representation agreements",
         "l": ["Consent to DUAL AGENCY may be given by a seller in a LISTING AGREEMENT, by a buyer in a BUYER REPRESENTATION AGREEMENT, or in a separate document signed before or after a transaction is identified (254 CMR 3.00(13)(b)2.).",
               "Consent to DESIGNATED AGENCY may be given the same three ways, and the form may be signed before a potential transaction is identified or when it is - but IN ANY EVENT NO LATER THAN BEFORE the execution of a written agreement for the purchase or sale of residential property (254 CMR 3.00(13)(c)).",
               "A FACILITATION relationship requires its own written notice stating that NO AGENCY RELATIONSHIP EXISTS, given at the FIRST PERSONAL MEETING to discuss a specific property, and it may later be converted to an agency relationship by WRITTEN AGREEMENT (254 CMR 3.00(13)(e))."],
         "check": [("Consent to designated agency must be signed:", "No later than before the written purchase and sale agreement is executed", ["Only at the first meeting", "After closing"], "254 CMR 3.00(13)(c)."),
                   ("Consent to dual agency may be given in:", "A listing agreement, a buyer representation agreement, or a separate consent form", ["A verbal agreement", "The purchase and sale agreement only"], "254 CMR 3.00(13)(b)2."),
                   ("Converting a facilitation to an agency relationship requires:", "The written agreement of the person represented", ["An oral request", "Board approval"], "254 CMR 3.00(13)(e).")]},
    ],
    "traps": [
        "Offer to Purchase first, Purchase and Sale Agreement second.",
        "Both parties get a copy of the P&S, by statute.",
        "Never steer a client away from an attorney.",
    ],
    "vocab": [
        ["Offer to Purchase", "The first binding document in a Massachusetts sale."],
        ["Purchase and Sale Agreement", "The fuller contract that follows and supersedes it."],
        ["Tenancy at will", "An open-ended tenancy terminable on notice."],
        ["Facilitation agreement", "The written agreement for a non-agency relationship."],
    ],
    "examples": [],
}

STUDY["ma/environment"] = {
    "summary": "Three items on four Massachusetts hazards. The lead law is the one with a precise timing rule a licensee can get wrong.",
    "sections": [
        {"h": "Lead (M.G.L. c. 111 s. 197A)",
         "l": ["ALL PERSONS SELLING PREMISES must, PRIOR TO THE SIGNING OF A PURCHASE AND SALE AGREEMENT, give the prospective purchaser a copy of the DIRECTOR'S STANDARD NOTIFICATION FORM and materials about the hazards of lead, the symptoms and treatment of lead poisoning, the requirements of the lead law, LIABILITY for failure to abate or contain, and the PROHIBITIONS AGAINST UNLAWFUL DISCRIMINATION.",
               "A SEPARATE notification form exists for prospective purchasers of RESIDENTIAL PROPERTIES CONTAINING RENTAL UNITS, covering liability insurance and discrimination.",
               "A LEASE WITH AN OPTION TO PURCHASE triggers the same notification before the lease is signed.",
               "At the same time the seller must provide any LETTER OF INTERIM CONTROL or LETTER OF FULL COMPLIANCE for the premises, and BOTH THE SELLER AND ANY REAL ESTATE AGENT involved must DISCLOSE ANY INFORMATION KNOWN to them about lead in paint, plaster or other accessible structural materials.",
               "The outline distinguishes SALES FROM RENTALS and covers lead in PAINT, PIPES, WATER AND SOIL."],
         "check": [("The Massachusetts lead notification must be given:", "Prior to the signing of a purchase and sale agreement", ["At closing", "Within 10 days of the offer"], "M.G.L. c. 111 s. 197A(b)."),
                   ("Who must disclose known information about lead?", "Both the seller and any real estate agent involved in the sale", ["The seller only", "The buyer's inspector"], "M.G.L. c. 111 s. 197A(b)."),
                   ("A lease with an option to purchase:", "Triggers the lead notification before the lease is signed", ["Is exempt", "Triggers it at the option exercise"], "M.G.L. c. 111 s. 197A(b)."),
                   ("Along with the notification, the seller must provide:", "Any letter of interim control or letter of full compliance", ["A home warranty", "A radon test"], "M.G.L. c. 111 s. 197A(b).")]},
        {"h": "Septic, detectors and wetlands",
         "l": ["TITLE 5 is the state environmental code governing PRIVATE SEWAGE DISPOSAL - septic systems and cesspools. The outline names it expressly.",
               "SMOKE DETECTORS: all residential buildings not already regulated by ss. 26A, 26B or 26C must, UPON THE SALE OR TRANSFER of the building, BE EQUIPPED BY THE SELLER with approved smoke detectors, and the HEAD OF THE FIRE DEPARTMENT ENFORCES it (M.G.L. c. 148 s. 26F). In practice the fire department issues a certificate at transfer, and CARBON MONOXIDE detection is tested alongside it.",
               "WETLANDS AND RIVERS PROTECTION are the fourth environmental heading on the outline."],
         "check": [("Under M.G.L. c. 148 s. 26F, who must equip the building with approved smoke detectors on a sale?", "The seller", ["The buyer", "The lender", "The listing broker"], "M.G.L. c. 148 s. 26F."),
                   ("Who enforces the smoke detector requirement on transfer?", "The head of the fire department", ["The Board of Registration", "The building inspector"], "M.G.L. c. 148 s. 26F."),
                   ("Private sewage disposal in Massachusetts is governed by:", "Title 5", ["Title 9", "Chapter 91"], "Named on the Massachusetts state outline.")]},
    ],
    "traps": [
        "The lead notification goes out BEFORE the purchase and sale agreement is signed, not at closing.",
        "The AGENT, not just the seller, must disclose known lead information.",
        "The SELLER equips the property with smoke detectors on transfer.",
    ],
    "vocab": [
        ["Letter of Full Compliance", "Certification that a property meets the lead law."],
        ["Letter of Interim Control", "A temporary lead compliance status."],
        ["Title 5", "The Massachusetts septic system code."],
        ["26F certificate", "The fire department sign-off required at transfer."],
    ],
    "examples": [],
}

STUDY["ma/board"] = {
    "summary": "Two items. Know who investigates, when it must, and what it can do.",
    "sections": [
        {"h": "Investigation and sanctions (M.G.L. c. 112 s. 87AAA)",
         "l": ["The Board MAY investigate on its own, and MUST investigate ON THE VERIFIED WRITTEN COMPLAINT OF AN AGGRIEVED PERSON - including against a person who merely ATTEMPTS TO ACT as a broker or salesperson.",
               "It may SUSPEND, REVOKE OR REFUSE TO RENEW a licence obtained by FALSE OR FRAUDULENT REPRESENTATION, and for the enumerated grounds in s. 87AAA.",
               "It may also act where the licensee has been CONVICTED OF A CRIMINAL OFFENCE demonstrating a lack of GOOD MORAL CHARACTER.",
               "The Board MAY RECONSIDER any decision, REINSTATE a suspended licence and REISSUE a revoked one. A person whose licence is suspended or revoked REMAINS LIABLE to any other punishment provided by law.",
               "The outline lists the Board's sanctions as FINES, action for a CONTINUING EDUCATION VIOLATION, PROBATION, and LICENCE SUSPENSION AND REVOCATION.",
               "EXAMINATION OF RECORDS: broker and brokerage records, including escrow fund records, are SUBJECT TO INSPECTION BY THE BOARD OR ITS AGENTS (254 CMR 3.00(10)(b), (13)(a)4.). A licensee who FAILS, ON DEMAND, to disclose information within their knowledge or produce records is in breach of the licence law."],
         "check": [("The Massachusetts Board must investigate when:", "An aggrieved person files a verified written complaint", ["Only on its own motion", "Only after a court refers a case"], "M.G.L. c. 112 s. 87AAA."),
                   ("Brokerage and escrow records are:", "Subject to inspection by the Board or its agents", ["Private to the broker", "Open only by subpoena"], "254 CMR 3.00(10)(b)."),
                   ("After a revocation, the Board:", "May reconsider its decision and reissue the licence", ["Has no further power", "Must wait five years"], "M.G.L. c. 112 s. 87AAA."),
                   ("A licensee whose licence is revoked:", "Remains liable to any other punishment provided by law", ["Faces no other consequence", "Is immune from suit"], "M.G.L. c. 112 s. 87AAA.")]},
    ],
    "traps": [
        "'May on its own motion, SHALL on a verified written complaint.'",
        "Revocation is not necessarily permanent - the Board may reissue.",
    ],
    "vocab": [
        ["Verified complaint", "A sworn written complaint that compels an investigation."],
        ["Probation", "A Board sanction short of suspension."],
        ["Division of Occupational Licensure", "The agency the Board sits within."],
    ],
    "examples": [],
}

STUDY["ma/additional"] = {
    "summary": "Two items: condominiums and co-operatives, and legal descriptions. Know the difference between owning a unit and owning shares.",
    "sections": [
        {"h": "Condominiums and co-operatives",
         "l": ["In a CONDOMINIUM the buyer owns the UNIT IN FEE together with an UNDIVIDED INTEREST IN THE COMMON AREAS, governed by the Massachusetts Condominium Act, c. 183A. An ORGANISATION OF UNIT OWNERS runs it, and that organisation is expressly covered by the fair housing prohibitions in M.G.L. c. 151B s. 4(6).",
               "In a CO-OPERATIVE the buyer owns SHARES IN A CORPORATION that owns the building, together with a PROPRIETARY LEASE of a unit - personal property, not real property. HOUSING CO-OPERATIVES are likewise covered by c. 151B s. 4(6)."],
         "check": [("A Massachusetts condominium buyer owns:", "The unit in fee plus an undivided interest in the common areas", ["Shares in a corporation", "A leasehold only"], "M.G.L. c. 183A; named on the state outline."),
                   ("A co-operative owner holds:", "Shares in the corporation and a proprietary lease", ["Fee title to the unit", "A life estate"], "Named on the Massachusetts state outline."),
                   ("A condominium unit owners' organisation:", "Is expressly subject to the c. 151B housing discrimination prohibitions", ["Is exempt as a private association", "Is governed only by its bylaws"], "M.G.L. c. 151B s. 4(6).")]},
        {"h": "Legal descriptions",
         "l": ["Massachusetts uses METES AND BOUNDS and RECORDED PLAT (lot and block) descriptions; it is NOT a government survey state.",
               "Massachusetts also has a REGISTERED LAND (Land Court) system alongside recorded land, which is why the outline pairs legal descriptions with the condominium topic."],
         "check": [("Massachusetts legal descriptions commonly use:", "Metes and bounds and recorded plat", ["The government rectangular survey", "Township and range"], "Named on the Massachusetts state outline.")]},
    ],
    "traps": [
        "Condo = real property. Co-op = shares plus a proprietary lease, which is personal property.",
        "No government survey system in Massachusetts.",
    ],
    "vocab": [
        ["Chapter 183A", "The Massachusetts Condominium Act."],
        ["Proprietary lease", "The co-op shareholder's right to occupy a unit."],
        ["Registered land", "Land Court title, distinct from recorded land."],
    ],
    "examples": [],
}


# ------------------------------------------------------------- questions

Q = [
 # requirements
 ("ma/requirements", "Agency disclosure", 1, "The Massachusetts agency disclosure notice must be given:",
  "At the first personal meeting to discuss a specific property", ["At the first telephone contact", "With the offer to purchase", "At closing"],
  "254 CMR 3.00(13)(a)."),
 ("ma/requirements", "Agency disclosure", 2, "If a consumer declines to sign the agency disclosure notice, the licensee:",
  "Notes the date it was given and that they declined, and keeps it three years", ["May not work with them", "Discards the notice"],
  "254 CMR 3.00(13)(a)2."),
 ("ma/requirements", "Agency disclosure", 2, "At an open house, individual written agency notices are not required if:",
  "A sign, poster or listing literature conspicuously discloses any pre-existing agency relationship", ["Visitors sign a register", "The seller is present"],
  "254 CMR 3.00(13)(a)3."),
 ("ma/requirements", "Agency disclosure", 3, "Agency disclosure notices must be retained for:",
  "Three years from the date on the notice", ["One year", "Six years", "Until closing"],
  "254 CMR 3.00(13)(a)1."),
 ("ma/requirements", "Dual agency", 1, "A Massachusetts dual agent still owes both parties:",
  "Confidentiality of material information and the duty to account for funds", ["Full loyalty", "Obedience to lawful instructions"],
  "254 CMR 3.00(13)(b)."),
 ("ma/requirements", "Dual agency", 1, "Consensual dual agency requires:",
  "Informed written consent from both the seller and the buyer", ["Oral consent", "The appointing broker's approval"],
  "254 CMR 3.00(13)(b)."),
 ("ma/requirements", "Dual agency", 2, "A dual agent may disclose confidential material information where:",
  "Disclosure is expressly authorised, required by law, intended to prevent illegal conduct, or needed to prosecute or defend a claim", ["The transaction has closed", "The other broker requests it"],
  "254 CMR 3.00(13)(b)."),
 ("ma/requirements", "Dual agency", 2, "Where dual agency consent was given in advance, written notice of dual agency must be given:",
  "Before the parties enter a written purchase and sale agreement", ["At closing", "Within 30 days of the offer"],
  "254 CMR 3.00(13)(b)2."),
 ("ma/requirements", "Dual agency", 3, "A dual agent's duty of confidentiality:",
  "Continues after the brokerage relationship terminates", ["Ends at closing", "Ends with the listing"],
  "254 CMR 3.00(13)(b)."),
 ("ma/requirements", "Designated agency", 1, "Where two designated agents of the same Massachusetts broker represent opposite parties:",
  "The appointing broker is the dual agent, neutral but still owing confidentiality and accounting", ["Both designated agents become dual agents", "The arrangement is prohibited"],
  "254 CMR 3.00(13)(c)."),
 ("ma/requirements", "Designated agency", 2, "Where both parties have consented to designated agency:",
  "No separate consent to the appointing broker's dual agency is required", ["Separate dual agency consent is still required", "The transaction cannot proceed"],
  "254 CMR 3.00(13)(c)."),
 ("ma/requirements", "Designated agency", 2, "A designated agent must share with others:",
  "Known material defects in the real property", ["Their client's lowest acceptable price", "Their client's motivation to sell"],
  "254 CMR 3.00(13)(c)1."),
 ("ma/requirements", "Designated agency", 3, "Appointing a designated agent:",
  "Does not limit the appointing broker's liability for that agent's breach of duty", ["Transfers all liability to the designated agent", "Ends the broker's duties"],
  "254 CMR 3.00(13)(c)2."),
 ("ma/requirements", "Facilitator", 1, "A Massachusetts facilitator:",
  "Represents neither party and owes no duty of confidentiality", ["Is a form of dual agent", "Owes loyalty to the seller"],
  "254 CMR 3.00(13)(e)."),
 ("ma/requirements", "Facilitator", 2, "A facilitator still owes the duty to:",
  "Present property honestly and accurately, disclose known material defects and account for funds", ["Keep the buyer's price confidential", "Negotiate for the seller"],
  "254 CMR 3.00(13)(e)."),
 ("ma/requirements", "Facilitator", 2, "A facilitator relationship may become an agency relationship:",
  "By written agreement of the person represented", ["Automatically when an offer is made", "Never"],
  "254 CMR 3.00(13)(e)."),
 ("ma/requirements", "Sub-agency", 3, "Before offering sub-agency a licensee must disclose in writing:",
  "That the sub-agent's acts may subject the client to vicarious liability", ["The sub-agent's commission split", "The sub-agent's licence number"],
  "254 CMR 3.00(13)(d)."),
 ("ma/requirements", "Client funds", 1, "Deposit money paid to a Massachusetts broker must be:",
  "Immediately deposited in a bank escrow account, unless the parties agree otherwise in writing", ["Deposited within three business days", "Held by the listing salesperson"],
  "254 CMR 3.00(10)(a)."),
 ("ma/requirements", "Client funds", 1, "May a Massachusetts salesperson hold client funds?",
  "No; they must immediately turn them over to the employing broker", ["Yes, for up to 48 hours", "Yes, with written consent"],
  "254 CMR 3.00(10)(c)."),
 ("ma/requirements", "Client funds", 2, "Copies of escrow account cheques must be kept for:",
  "Three years from the date of issuance", ["One year", "Six years", "Until the transaction closes"],
  "254 CMR 3.00(10)(b)."),
 ("ma/requirements", "Client funds", 3, "An escrow account is defined as one in which the broker:",
  "Has no claim to the money held", ["May keep the interest earned", "May hold personal reserves"],
  "254 CMR 3.00(10)(a)."),
 ("ma/requirements", "Advertising", 1, "A Massachusetts salesperson:",
  "May not advertise real property under their own name", ["May advertise under their own name with the broker's consent", "Must advertise under their own name"],
  "254 CMR 3.00(9)(b)."),
 ("ma/requirements", "Advertising", 1, "Every broker advertisement must:",
  "Include the broker's name and affirmatively disclose that the advertiser is a real estate broker", ["Show a telephone number alone", "Show the Board's seal"],
  "254 CMR 3.00(9)(a)."),
 ("ma/requirements", "Advertising", 3, "An advertisement showing only a post office box and a telephone number is:",
  "Prohibited", ["Acceptable if the broker is licensed", "Acceptable for rentals"],
  "254 CMR 3.00(9)(a)."),
 ("ma/requirements", "Conflicts", 1, "A net listing in Massachusetts is:",
  "Prohibited", ["Allowed with written consent", "Allowed on commercial property", "Allowed if disclosed"],
  "254 CMR 3.00(11)(c); M.G.L. c. 112 s. 87AAA(l)."),
 ("ma/requirements", "Conflicts", 2, "A licensee whose kin has a financial interest in a property must:",
  "Fully disclose it in writing to all parties and obtain written acknowledgment", ["Disclose it orally", "Withdraw from the transaction"],
  "254 CMR 3.00(11)(a)."),
 ("ma/requirements", "Conflicts", 2, "A broker who takes an option on property they were approached to broker must first:",
  "Disclose that they are now a prospective purchaser and no longer acting as broker", ["Obtain Board approval", "Resign the listing"],
  "254 CMR 3.00(11)(b)."),
 ("ma/requirements", "Conflicts", 1, "Offers received by a licensee must be:",
  "Conveyed forthwith to the owner", ["Presented at the broker's convenience", "Screened for suitability first"],
  "254 CMR 3.00(11)(d)."),
 ("ma/requirements", "Attorneys", 2, "Advising a client against using an attorney is:",
  "Prohibited", ["Permitted for simple transactions", "Required in cash sales"],
  "254 CMR 3.00(12)."),
 ("ma/requirements", "Compensation", 1, "A Massachusetts salesperson may accept a commission from:",
  "Their own licensed broker only", ["The seller directly", "Any licensed broker", "The closing attorney"],
  "M.G.L. c. 112 s. 87RR."),
 ("ma/requirements", "Compensation", 2, "Dividing fees with a person required to be licensed who is not is:",
  "A ground for suspension or revocation", ["Permitted between states", "Permitted under $500"],
  "M.G.L. c. 112 s. 87AAA(e)."),
 ("ma/requirements", "Discipline", 2, "Commingling a principal's money with the licensee's own is:",
  "A ground for suspension or revocation", ["Permitted short term", "A bookkeeping matter"],
  "M.G.L. c. 112 s. 87AAA(h)."),

 # fair housing
 ("ma/fair-housing", "Classes", 1, "Which is protected in Massachusetts housing but not by the federal Fair Housing Act?",
  "Marital status", ["Race", "Color", "National origin"],
  "M.G.L. c. 151B s. 4(6)."),
 ("ma/fair-housing", "Classes", 1, "Massachusetts also protects:",
  "Veterans and members of the armed forces", ["Credit score", "Occupation", "Length of residence"],
  "M.G.L. c. 151B s. 4(6)."),
 ("ma/fair-housing", "Classes", 2, "Massachusetts housing advertising may not indicate a preference based on, among others:",
  "Children and public assistance recipiency", ["Pet ownership", "Length of employment"],
  "M.G.L. c. 151B s. 4(7B)."),
 ("ma/fair-housing", "Classes", 2, "Age in Massachusetts housing is:",
  "A protected class", ["Protected only in employment", "Not protected at all"],
  "M.G.L. c. 151B s. 4(6)."),
 ("ma/fair-housing", "Discipline", 1, "After a final MCAD finding of discrimination against a licensee, the Board:",
  "Shall suspend the licence for ninety days", ["May issue a warning", "Must revoke the licence permanently"],
  "M.G.L. c. 112 s. 87AAA."),
 ("ma/fair-housing", "Blockbusting", 2, "Blockbusting in Massachusetts carries:",
  "A fine of not less than $1,000 and not more than $2,500, or up to six months' imprisonment, or both", ["A $500 fine", "A civil penalty only"],
  "M.G.L. c. 112 s. 87AAA(k)."),

 # consumer
 ("ma/consumer", "Disclosure", 1, "Failing to give both the buyer and the seller a copy of the purchase and sale agreement is:",
  "A ground for suspension or revocation", ["Good practice only", "A civil matter between the parties"],
  "M.G.L. c. 112 s. 87AAA(i)."),
 ("ma/consumer", "Disclosure", 1, "A Massachusetts facilitator who knows of a serious roof leak must:",
  "Disclose that known material defect", ["Stay silent, owing no agency duties", "Tell the seller only"],
  "254 CMR 3.00(13)(e)."),
 ("ma/consumer", "Misrepresentation", 2, "Knowingly making a substantial misrepresentation is:",
  "A ground for the Board to suspend or revoke the licence", ["Actionable only in court", "A warning offence"],
  "M.G.L. c. 112 s. 87AAA(a)."),
 ("ma/consumer", "Conflicts", 2, "A broker buying a listed property without disclosing they are the principal is:",
  "Acting as broker and undisclosed principal, a ground for discipline", ["Permitted if the price is fair", "A purely private matter"],
  "M.G.L. c. 112 s. 87AAA(b)."),
 ("ma/consumer", "Privacy", 3, "A WISP in Massachusetts is:",
  "A Written Information Security Policy covering personal information", ["A wetlands site plan", "A waiver of inspection"],
  "Named on the Massachusetts state outline."),

 # landlord
 ("ma/landlord", "Move-in", 1, "At move-in a Massachusetts landlord may collect:",
  "First month, last month, a security deposit of one month, and the cost of a key and lock", ["Whatever the lease provides", "First, last and two months' deposit"],
  "M.G.L. c. 186 s. 15B(1)(b)."),
 ("ma/landlord", "Deposit", 1, "A Massachusetts security deposit may not exceed:",
  "The first month's rent", ["Two months' rent", "1.5 months' rent", "Three months' rent"],
  "M.G.L. c. 186 s. 15B(1)(b)(iii)."),
 ("ma/landlord", "Deposit", 2, "A Massachusetts security deposit must be held:",
  "In a separate interest-bearing account in a bank located within the Commonwealth", ["In the landlord's business account", "By the managing broker"],
  "M.G.L. c. 186 s. 15B(3)(a)."),
 ("ma/landlord", "Interest", 3, "Last month's rent collected in advance earns interest at:",
  "Five per cent per year, or the lesser rate actually received from the bank", ["No interest", "Ten per cent per year"],
  "M.G.L. c. 186 s. 15B(2)(b)."),

 # licensing
 ("ma/licensing", "Education", 1, "Prelicence education for a Massachusetts salesperson is:",
  "40 classroom hours", ["24 hours", "60 hours", "75 hours"],
  "M.G.L. c. 112 s. 87SS."),
 ("ma/licensing", "Broker", 2, "A Massachusetts broker applicant must show:",
  "Three years actively associated with a broker as a salesperson, plus an additional 40 classroom hours", ["One year and no extra education", "Two years and 90 hours"],
  "M.G.L. c. 112 s. 87SS."),
 ("ma/licensing", "Renewal", 1, "A Massachusetts real estate licence is valid for:",
  "Two years from the date of issue", ["One year", "Three years", "Five years"],
  "M.G.L. c. 112 s. 87XX; the expiration date is the licensee's birthday."),

 # contracts
 ("ma/contracts", "Sequence", 1, "In a Massachusetts sale the first binding document is usually:",
  "The offer to purchase", ["The purchase and sale agreement", "The deed", "The listing agreement"],
  "Named on the Massachusetts state outline."),
 ("ma/contracts", "Leases", 2, "A Massachusetts tenancy with no fixed end date is:",
  "A tenancy at will", ["A fixed term lease", "A periodic estate for years"],
  "Named on the Massachusetts state outline."),
 ("ma/contracts", "Consent", 3, "Consent to designated agency must be signed:",
  "No later than before the written purchase and sale agreement is executed", ["Only at the first meeting", "After closing"],
  "254 CMR 3.00(13)(c)."),

 # environment
 ("ma/environment", "Lead", 1, "The Massachusetts lead notification must be given to a buyer:",
  "Prior to the signing of a purchase and sale agreement", ["At closing", "Within 10 days of the offer", "On request"],
  "M.G.L. c. 111 s. 197A(b)."),
 ("ma/environment", "Lead", 2, "Who must disclose known information about lead in the premises?",
  "Both the seller and any real estate agent involved in the sale", ["The seller alone", "The buyer's inspector"],
  "M.G.L. c. 111 s. 197A(b)."),
 ("ma/environment", "Detectors", 1, "On the sale of a residential building, approved smoke detectors must be installed by:",
  "The seller", ["The buyer", "The lender", "The listing broker"],
  "M.G.L. c. 148 s. 26F; the fire department enforces it."),

 # board
 ("ma/board", "Investigations", 1, "The Massachusetts Board must investigate when:",
  "An aggrieved person files a verified written complaint", ["It chooses to", "A court refers a matter"],
  "M.G.L. c. 112 s. 87AAA."),
 ("ma/board", "Records", 2, "Brokerage and escrow records are:",
  "Subject to inspection by the Board or its agents", ["Private to the broker", "Open only under subpoena"],
  "254 CMR 3.00(10)(b)."),

 # additional
 ("ma/additional", "Condominiums", 1, "A Massachusetts condominium buyer owns:",
  "The unit in fee plus an undivided interest in the common areas", ["Shares in a corporation", "A proprietary lease only"],
  "M.G.L. c. 183A; named on the state outline."),
 ("ma/additional", "Co-operatives", 2, "A co-operative owner holds:",
  "Shares in the corporation and a proprietary lease of the unit", ["Fee title to the unit", "A life estate in the unit"],
  "Named on the Massachusetts state outline."),
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
            "id": "ma-" + hashlib.sha1(q.encode()).hexdigest()[:8],
            "portion": "georgia", "topic": topic, "subtopic": sub,
            "sub": topic + "|" + sub, "concept": "Massachusetts " + sub.lower(),
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
        "code": "MA", "name": "Massachusetts", "abbr": "MA",
        "regulator": "Board of Registration of Real Estate Brokers and Salespersons",
        "pass": EXAM["pass"],
        "portions": {
            "national": {"name": "General", "scored": EXAM["national_scored"],
                         "minutes": EXAM["national_minutes"]},
            "georgia": {"name": "Massachusetts law", "scored": EXAM["state_scored"],
                        "minutes": EXAM["state_minutes"],
                        "blurb": "Chapter 112, 254 CMR 3.00, c. 151B fair housing, deposits, lead and the rest."},
        },
        "topics": topics, "bank": bank, "study": study,
        "sources": SOURCES, "diffs": DIFFS,
    }


# Where Massachusetts departs from the national rule.
DIFFS = {
    "national/agency": [
        "Massachusetts recognises FIVE relationships: seller agent, buyer agent, consensual DUAL agent, DESIGNATED agent, and the NON-AGENT FACILITATOR who represents nobody and owes NO confidentiality (254 CMR 3.00(13)).",
        "The agency disclosure notice is given at the FIRST PERSONAL MEETING TO DISCUSS A SPECIFIC PROPERTY, signed if the consumer will, and kept THREE YEARS.",
        "A dual agent cannot fully satisfy loyalty, full disclosure, reasonable care or obedience, but STILL owes confidentiality and accounting - and that confidentiality survives the relationship.",
        "Under designated agency the APPOINTING BROKER is the dual agent, and no separate dual agency consent is needed.",
        "Sub-agency requires written disclosure of VICARIOUS LIABILITY and the client's consent.",
    ],
    "national/practice": [
        "Deposits go into a bank escrow account IMMEDIATELY, and a SALESPERSON MAY NEVER HOLD CLIENT FUNDS (254 CMR 3.00(10)).",
        "Salespeople may not advertise in their own name, and every broker advertisement must name the broker and say they are a real estate broker (254 CMR 3.00(9)).",
        "NET LISTINGS are prohibited, and no licensee may advise against using an attorney (254 CMR 3.00(11), (12)).",
        "Education: 40 classroom hours for a salesperson, three years plus 40 more for a broker; the licence runs two years and expires on the licensee's birthday.",
    ],
    "national/disclosures": [
        "Massachusetts has no statutory seller's disclosure form; the duty to disclose KNOWN MATERIAL DEFECTS falls on the licensee, including a facilitator.",
        "The LEAD notification and any letter of interim control or full compliance go to the buyer BEFORE the purchase and sale agreement is signed, and the AGENT must disclose what they know (M.G.L. c. 111 s. 197A).",
        "The SELLER must equip the building with approved smoke detectors on transfer, enforced by the fire department (c. 148 s. 26F).",
        "c. 151B adds MARITAL STATUS, AGE, veteran status, ancestry, genetic information and public assistance recipiency, and an MCAD finding brings a MANDATORY 90-day suspension.",
        "At move-in a landlord may take only first month, last month, a one-month deposit and the key-and-lock cost (c. 186 s. 15B).",
    ],
}


if __name__ == "__main__":
    import io, json, os
    here = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    out = os.path.join(here, "greprep", "packs", "MA.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    pack = build()
    with io.open(out, "w", encoding="utf-8") as f:
        json.dump(pack, f, ensure_ascii=False, indent=1, sort_keys=True)
    print("wrote", out, len(pack["bank"]), "questions,", len(pack["study"]), "lessons")
