"""Colorado state content: lessons and practice questions.

Colorado splits the broker examination and sets the pass mark as a RAW
COUNT on each portion. The PSI bulletin's table: National 80 questions,
60 CORRECT to pass, 120 minutes; State 74 questions, 53 CORRECT to pass,
110 minutes. That is 75% on the national portion and 53/74, about 71.6%,
on the state portion - so the pack puts a different `pass` on each.

Colorado is the state that does NOT allow dual agency at all, and whose
DEFAULT relationship is TRANSACTION-BROKER unless a written agreement
makes the broker a single agent. Its state portion is also unusually
practical: 23 of the 74 items are Commission-approved FORMS AND CONTRACTS
and another 10 are CLOSING AND SETTLEMENT.

Every rule below was read from the official text on 2026-11-10:
  - The Colorado Real Estate Manual, 2026 edition, Chapter 1 (Real Estate
    Broker License Law, C.R.S. title 12 article 10) and Chapter 2 (the
    Commission's Rules), published by the Division of Real Estate.
  - The Colorado Civil Rights Division's own fair housing page, for the
    classes Colorado adds to the federal list.
  - The PSI Colorado Candidate Information Bulletin, for the examination
    table and the 74-item state outline.
The section a fact comes from is cited next to it. Do not add a fact here
without reading its source first.
"""

EXAM = {
    # National 80 items / 60 correct / 120 minutes.
    # State 74 items / 53 correct / 110 minutes.
    "state_scored": 74,
    "state_minutes": 110,
    "state_pass": 53 / 74.0,
    "national_scored": 80,
    "national_minutes": 120,
    "national_pass": 0.75,
    "pass": 0.75,
}

# PSI's Colorado state outline, broker item counts, summing to 74.
TOPICS = [
    ("co/forms", "Colorado forms and contracts", 23,
     "Commission-approved forms, the contract to buy and sell, counterproposals."),
    ("co/requirements", "Requirements governing licensees", 11,
     "Advertising, brokerage administration, commissions, disclosure, listings."),
    ("co/relationships", "Brokerage relationships", 11,
     "Transaction-broker, single agent, designated brokers, disclosure."),
    ("co/closing", "Closing and settlement", 10,
     "Prorations, accuracy of closing statements, who does what at closing."),
    ("co/additional", "Additional topics", 7,
     "Property management, water rights, taxes, fair housing, foreclosure."),
    ("co/licensing", "Licensing requirements", 5,
     "Licence types, education, renewal, continuing education, E&O insurance."),
    ("co/records", "Record keeping & trust accounts", 5,
     "Trust account requirements, delivery of funds and transaction records."),
    ("co/commission", "Duties & powers of the Commission", 2,
     "General powers, investigations and audits, hearings and violations."),
]

SOURCES = [
    {"by": "Colorado Division of Real Estate",
     "name": "Colorado Real Estate Manual, Chapter 1 - Real Estate Broker License Law",
     "note": "C.R.S. title 12 article 10: licensing, renewal, discipline, and the brokerage relationship statutes in part 4.",
     "url": "https://dre.colorado.gov/real-estate-manual-and-position-statements"},
    {"by": "Colorado Real Estate Commission",
     "name": "Colorado Real Estate Manual, Chapter 2 - Rules and Regulations",
     "note": "Advertising, supervision, brokerage relationships, trust accounts and record keeping.",
     "url": "https://dre.colorado.gov/real-estate-manual-and-position-statements"},
    {"by": "Colorado Civil Rights Division",
     "name": "Housing Discrimination, C.R.S. 24-34-501 et seq.",
     "note": "The Colorado Anti-Discrimination Act's housing provisions and the classes Colorado adds.",
     "url": "https://ccrd.colorado.gov/housing-discrimination"},
    {"by": "PSI Services and the Division of Real Estate",
     "name": "Colorado Candidate Information Bulletin",
     "note": "National 80 with 60 correct to pass, State 74 with 53 correct, and the state outline.",
     "url": "https://test-takers.psiexams.com/core"},
]


# --------------------------------------------------------------- lessons

STUDY = {}

STUDY["co/relationships"] = {
    "summary": "Eleven items, and the whole thing turns on two sentences: a broker is a TRANSACTION-BROKER unless a written agreement makes them a single agent, and DUAL AGENCY IS PROHIBITED.",
    "sections": [
        {"h": "The two relationships Colorado allows",
         "l": ["A broker may act in any transaction as a SINGLE AGENT or a TRANSACTION-BROKER (C.R.S. 12-10-403(1)).",
               "A broker SHALL BE CONSIDERED A TRANSACTION-BROKER unless a single agency relationship is established through a WRITTEN AGREEMENT between the broker and the party to be represented (12-10-403(2)).",
               "A BROKER SHALL NOT ESTABLISH DUAL AGENCY with any seller, landlord, buyer or tenant (C.R.S. 12-10-406). That is the whole section.",
               "A broker may work with the SAME party in SEPARATE transactions under DIFFERENT relationships - selling one property as their seller's agent and helping them buy another as a transaction-broker - provided the relationship is properly established for each (12-10-403(3)).",
               "A transaction-broker MAY COOPERATE with other brokers but SHALL NOT ENGAGE OR CREATE ANY SUBAGENTS (12-10-407(8))."],
         "check": [("In Colorado, a broker who has signed nothing with a consumer is:", "A transaction-broker", ["A single agent", "A dual agent", "A subagent"], "C.R.S. 12-10-403(2)."),
                   ("Dual agency in Colorado is:", "Prohibited", ["Allowed with written consent", "Allowed for commercial property", "The default"], "C.R.S. 12-10-406."),
                   ("A Colorado transaction-broker may:", "Cooperate with other brokers, but may not create subagents", ["Appoint subagents freely", "Not work with other brokers"], "C.R.S. 12-10-407(8)."),
                   ("Single agency in Colorado is established by:", "A written agreement with the party to be represented", ["An oral agreement", "Showing the property"], "C.R.S. 12-10-403(2).")]},
        {"h": "The transaction-broker's duties (C.R.S. 12-10-407)",
         "l": ["A transaction-broker IS NOT AN AGENT FOR EITHER PARTY.",
               "They must perform the terms of any WRITTEN OR ORAL agreement, and exercise reasonable skill and care - which includes PRESENTING ALL OFFERS AND COUNTEROFFERS in a timely manner REGARDLESS of whether the property is already under contract; ADVISING the parties and suggesting EXPERT ADVICE on material matters beyond the broker's expertise; ACCOUNTING in a timely manner for money and property; KEEPING THE PARTIES FULLY INFORMED; and ASSISTING them to comply with the contract and close.",
               "They must disclose to prospective BUYERS or TENANTS all ADVERSE MATERIAL FACTS ACTUALLY KNOWN, including facts about TITLE, the PHYSICAL CONDITION, DEFECTS and ENVIRONMENTAL HAZARDS required by law to be disclosed.",
               "They must disclose to a prospective SELLER or LANDLORD all adverse material facts actually known, including about the BUYER'S OR TENANT'S FINANCIAL ABILITY to perform and the BUYER'S INTENT TO OCCUPY the property as a principal residence.",
               "They must INFORM THE PARTIES that they are NOT VICARIOUSLY LIABLE for the transaction-broker's acts.",
               "SIX THINGS MAY NOT BE DISCLOSED without the INFORMED CONSENT OF ALL PARTIES: that a buyer will pay MORE than offered; that a seller will take LESS than asking; any party's MOTIVATING FACTORS; that a party would accept OTHER FINANCING TERMS; any facts or suspicions that may PSYCHOLOGICALLY IMPACT OR STIGMATIZE the property under C.R.S. 38-35.5-101; and any MATERIAL INFORMATION about the other party unless the law requires it or silence would be fraud or dishonest dealing.",
               "A transaction-broker has NO DUTY to inspect the property independently, to verify the seller's or an inspector's statements, or to investigate the buyer's finances (12-10-407(4), (5)).",
               "Without breaching anything, a transaction-broker may SHOW ALTERNATIVE PROPERTIES, LIST COMPETING PROPERTIES, show the buyer's property to OTHER buyers, and serve as a single agent or transaction-broker in OTHER transactions.",
               "There is NO IMPUTATION of knowledge between a party and the transaction-broker, or among people within an entity acting as transaction-broker (12-10-407(7))."],
         "check": [("A Colorado transaction-broker must present offers:", "Timely, even where the property is already under contract", ["Only until a contract is signed", "At the seller's request"], "C.R.S. 12-10-407(2)(b)(I)."),
                   ("Which may a transaction-broker NOT disclose without all parties' informed consent?", "That the seller would accept less than the asking price", ["A known roof defect", "An environmental hazard"], "C.R.S. 12-10-407(3)(b)."),
                   ("A transaction-broker must tell a seller:", "Adverse material facts actually known about the buyer's financial ability to perform", ["The buyer's credit score", "Nothing about the buyer"], "C.R.S. 12-10-407(2)(b)(VII)."),
                   ("A transaction-broker's duty to inspect the property is:", "None, unless otherwise agreed", ["A full physical inspection", "A visual walkthrough"], "C.R.S. 12-10-407(4)."),
                   ("The parties to a transaction-broker's deal are:", "Not vicariously liable for the broker's acts, and must be told so", ["Fully liable for the broker's acts", "Liable only on closing"], "C.R.S. 12-10-407(2)(b)(VIII).")]},
        {"h": "The single agent's duties (C.R.S. 12-10-404, 12-10-405)",
         "l": ["A broker engaged by a seller or landlord as a SELLER'S AGENT is a LIMITED AGENT who must PERFORM THE WRITTEN AGREEMENT, exercise REASONABLE SKILL AND CARE, and PROMOTE THE SELLER'S INTERESTS WITH UTMOST GOOD FAITH, LOYALTY AND FIDELITY.",
               "That includes SEEKING A PRICE AND TERMS acceptable to the seller - though the broker is NOT obliged to seek additional offers while the property is under contract - PRESENTING ALL OFFERS TO AND FROM the seller in a timely manner REGARDLESS of whether the property is under contract, DISCLOSING ADVERSE MATERIAL FACTS ACTUALLY KNOWN, and COUNSELLING the seller as to material benefits and risks.",
               "A broker engaged by a buyer or tenant as a BUYER'S AGENT owes the mirror-image duties (12-10-405).",
               "The same six categories of confidential information protected for a transaction-broker apply, and a single agent's duty of confidentiality is correspondingly stronger toward their own client."],
         "check": [("A Colorado single agent is described by the statute as:", "A limited agent", ["A universal agent", "A general agent", "A fiduciary without limits"], "C.R.S. 12-10-404(1)."),
                   ("A seller's agent must present offers:", "To and from the seller in a timely manner, even while the property is under contract", ["Only before a contract is signed", "Only above the listing price"], "C.R.S. 12-10-404(1)(c)(II)."),
                   ("Must a Colorado seller's agent keep seeking offers after a contract is signed?", "No, that duty is expressly excluded", ["Yes, always", "Yes, unless the seller objects"], "C.R.S. 12-10-404(1)(c)(I).")]},
        {"h": "Disclosure and who the relationship is with (C.R.S. 12-10-408; Rules 6.5 to 6.9)",
         "l": ["Every broker must adopt a WRITTEN OFFICE POLICY identifying and describing the relationships the broker offers to the public. A broker need NOT offer all of them, and if a consumer asks about one the broker does not offer, the broker must give the consumer the COMMISSION'S WRITTEN DEFINITION of that relationship.",
               "BEFORE engaging in brokerage activity, a TRANSACTION-BROKER must disclose IN WRITING that they are NOT acting as agent for the party, with a SIGNATURE BLOCK for the consumer to acknowledge receipt. The disclosure and acknowledgment BY ITSELF IS NOT A CONTRACT. If the consumer will not sign, the broker NOTES THAT ON A COPY AND RETAINS IT.",
               "BEFORE engaging in brokerage activity, a broker intending SINGLE AGENCY must enter a WRITTEN AGENCY AGREEMENT disclosing the statutory duties, and NOTICE of the single agency must be given to any prospective other party in a timely manner.",
               "A broker working with a buyer AS THE SELLER'S AGENT must give the buyer a written disclosure saying the broker is the SELLER'S agent and NOT the buyer's, listing the TASKS the agent intends to perform, and stating the buyer is NOT VICARIOUSLY LIABLE for the agent's acts unless they approve, direct or ratify them.",
               "A broker who already has a relationship with one party must ADVISE OTHER POTENTIAL PARTIES OR THEIR AGENTS of it AT THE EARLIEST REASONABLE OPPORTUNITY.",
               "Every written agreement must advise the consumer that the relationship exists ONLY WITH THE DESIGNATED BROKER - NOT with the employing broker, not with other brokers of the firm who are not designated, and NOT with the brokerage company. That does NOT limit the employing broker's duty to supervise or shield the firm from vicarious liability (12-10-408(2)(e)).",
               "Rule 6.7: neither a broker nor a TEAM may be a single agent for one consumer and a single agent OR transaction-broker for the other in the SAME transaction. With proper written disclosure they may instead act as (A) TRANSACTION-BROKER FOR BOTH, (B) transaction-broker for one and treat the other as a CUSTOMER, or (C) SINGLE AGENT for one and treat the other as a CUSTOMER.",
               "Rule 6.8: when working with a customer, a broker may perform MINISTERIAL TASKS after proper disclosure - SHOWING A PROPERTY, acting as SCRIVENER, CONVEYING written offers and counteroffers, explaining FINANCING ALTERNATIVES, and giving information on professional, governmental and community services. Ministerial tasks DO NOT create an agency or transaction-broker relationship with the customer."],
         "check": [("Every Colorado broker must adopt:", "A written office policy identifying the relationships offered to the public", ["A commission schedule", "A marketing plan"], "C.R.S. 12-10-408(1)(a)."),
                   ("If a consumer refuses to sign the transaction-broker disclosure, the broker:", "Notes that on a copy and retains it", ["Cannot work with them", "Must get a witness"], "C.R.S. 12-10-408(2)(a)(II)."),
                   ("A Colorado brokerage relationship exists:", "Only with the designated broker, not the employing broker or the firm", ["With the whole brokerage", "With every licensee in the office"], "C.R.S. 12-10-408(2)(e)(I)."),
                   ("A broker or team working both sides of one transaction may:", "Act as transaction-broker for both, or serve one and treat the other as a customer", ["Be a single agent for both", "Be a dual agent"], "Commission Rule 6.7."),
                   ("Performing ministerial tasks for a customer:", "Does not create an agency or transaction-broker relationship with them", ["Makes them a client", "Creates dual agency"], "Commission Rule 6.8."),
                   ("A broker who already represents one party must tell other potential parties:", "At the earliest reasonable opportunity", ["At the offer", "Only if asked"], "C.R.S. 12-10-408(2)(d).")]},
        {"h": "Broker engagement contracts (C.R.S. 12-10-403.5)",
         "p": ["Since 7 August 2023, a BROKER ENGAGEMENT CONTRACT for a RESIDENTIAL PREMISES must NOT purport to be a COVENANT RUNNING WITH THE LAND or bind future owners; must NOT allow ASSIGNMENT of the right to provide service without the owner's notice and agreement; and must NOT purport to create a RECORDABLE LIEN, ENCUMBRANCE OR OTHER SECURITY INTEREST - any such interest is VOID AND UNENFORCEABLE. Offering such a contract is an UNFAIR OR DECEPTIVE TRADE PRACTICE."],
         "check": [("A Colorado residential broker engagement contract may not:", "Purport to create a recordable lien or run with the land", ["Last more than 90 days", "Be exclusive"], "C.R.S. 12-10-403.5(2)."),
                   ("A lien purportedly created by such a contract is:", "Void and unenforceable", ["Enforceable if recorded", "Valid for one year"], "C.R.S. 12-10-403.5(2)(c)."),
                   ("Offering a contract with a prohibited term is:", "An unfair or deceptive trade practice", ["A licence violation only", "Permitted with disclosure"], "C.R.S. 12-10-403.5(3).")]},
    ],
    "traps": [
        "Transaction-broker is the DEFAULT. Single agency takes a written agreement.",
        "Dual agency is flatly prohibited - there is no consent that cures it.",
        "No subagents. A transaction-broker may cooperate but not create them.",
        "The relationship is with the DESIGNATED BROKER, not the firm.",
        "Ministerial tasks do not create a relationship with a customer.",
    ],
    "vocab": [
        ["Transaction-broker", "A broker who assists without being anyone's agent."],
        ["Single agent", "A limited agent for one party, created in writing."],
        ["Designated broker", "The individual broker the relationship actually runs with."],
        ["Customer", "A party the broker assists without a brokerage relationship."],
        ["Ministerial task", "Help that creates no relationship, such as showing or conveying offers."],
        ["Adverse material fact", "A known fact a Colorado broker must disclose."],
    ],
    "examples": [
        {"t": "Both sides of one deal",
         "s": "You have a signed listing as the seller's single agent. Your own buyer wants the house.",
         "w": ["Colorado forbids dual agency, so you cannot be a single agent for both.",
               "Rule 6.7 leaves you three options: transaction-broker for both; transaction-broker for one with the other as a customer; or stay the seller's single agent and treat the buyer as a CUSTOMER.",
               "Whichever you pick must be disclosed in writing, and you may still do ministerial tasks for the customer."],
         "k": "No dual agency - change the relationship or treat one side as a customer."},
    ],
}

STUDY["co/forms"] = {
    "summary": "Twenty-three items, almost a third of the state portion. Colorado brokers do not draft - they complete COMMISSION-APPROVED FORMS, and the exam tests which form does what.",
    "sections": [
        {"h": "Which forms a broker may use (C.R.S. 12-10-403(4))",
         "l": ["A licensed broker, whether a single agent or transaction-broker, MAY COMPLETE STANDARD FORMS for use in a real estate transaction - including standard forms intended to convey PERSONAL PROPERTY as part of the transaction - when performing licensed activities in that transaction.",
               "A STANDARD FORM means either a form PROMULGATED BY THE REAL ESTATE COMMISSION for current use (a 'COMMISSION-APPROVED FORM'), or a form DRAFTED BY A LICENSED COLORADO ATTORNEY representing the broker, the employing broker or the brokerage firm - with the attorney's or firm's name on it.",
               "Completing the blanks on an approved form is NOT the unauthorised practice of law. DRAFTING new contract language, or giving legal advice about the effect of a contract, IS - the outline lists 'PRACTICE OF LAW' as its own topic.",
               "An attorney-drafted form retained for a brokerage must be kept FOR FOUR YEARS from the date it was used (Commission rules)."],
         "check": [("A Colorado broker may complete:", "Commission-approved forms, or forms drafted by a Colorado attorney for the brokerage", ["Any form the broker writes", "Only forms from the MLS"], "C.R.S. 12-10-403(4)."),
                   ("An attorney-drafted form used by a brokerage must bear:", "The name of the attorney or law firm that drafted it", ["The Commission's seal", "The MLS number"], "C.R.S. 12-10-403(4)(b)(II)."),
                   ("Filling in the blanks of a Commission-approved form is:", "Permitted, and not the unauthorised practice of law", ["The practice of law", "Allowed only for brokers with 3 years' experience"], "C.R.S. 12-10-403(4).")]},
        {"h": "The forms the outline names",
         "l": ["LISTING CONTRACTS and BUYER REPRESENTATION AGREEMENTS - the Exclusive Right-to-Sell and Exclusive Right-to-Buy listing contracts.",
               "CONTRACTS TO BUY AND SELL REAL ESTATE, including the new disclosures the Commission adds each year.",
               "DEEDS OF TRUST and PROMISSORY NOTES - Colorado secures loans with a DEED OF TRUST and a PUBLIC TRUSTEE, not a mortgage.",
               "DISCLOSURE DOCUMENTS, including the Seller's Property Disclosure and the Source of Water addendum.",
               "ADDENDA, including the FORECLOSURE PROPERTY ADDENDUM and SHORT SALE addendum.",
               "The COUNTERPROPOSAL form - Colorado's name for a counter-offer, which replaces the stated terms of the original contract rather than being a separate agreement.",
               "CLOSING INSTRUCTIONS - the form by which buyer, seller and the closing company set out what the closing entity is to do.",
               "SELLER FINANCING documents, which the outline pairs with the practice-of-law topic because the broker must not draft the note or security instrument terms."],
         "check": [("Colorado's counter-offer form is called:", "The Counterproposal", ["The Counter-Offer", "The Amendment", "The Addendum"], "Named on the Colorado state outline."),
                   ("Colorado secures real estate loans with:", "A deed of trust, foreclosed through the public trustee", ["A mortgage foreclosed judicially", "A land contract"], "Named on the Colorado state outline."),
                   ("The form by which the parties instruct the closing entity is:", "Closing Instructions", ["The Settlement Statement", "The Counterproposal"], "Named on the Colorado state outline."),
                   ("A Foreclosure Property Addendum is used:", "When the property being bought is in foreclosure", ["On every contract", "Only for new construction"], "Named on the Colorado state outline.")]},
        {"h": "Listings and the contract to buy and sell",
         "l": ["The outline lists LISTINGS as its own heading under requirements governing licensees. A listing contract is a written employment agreement and, for a residential premises, is a BROKER ENGAGEMENT CONTRACT subject to C.R.S. 12-10-403.5's prohibited terms.",
               "A broker must GIVE COPIES of signed documents to the parties and keep the transaction file - the outline's 'HANDLING OF DOCUMENTS' topic.",
               "The CONTRACT TO BUY AND SELL REAL ESTATE is the Commission's central form and carries DEADLINES, OBJECTION AND RESOLUTION dates, and the buyer's right to TERMINATE on specified grounds. Every change to its stated terms goes on a COUNTERPROPOSAL (before acceptance) or an AMEND/EXTEND (after acceptance).",
               "Commission Position statements the Division publishes cover, among others, BROKER COMMISSIONS, RESPA AND REFERRAL FEES, REBATING part of a commission, RELEASE OF EARNEST MONEY DEPOSITS, WORKING WITH A FOR SALE BY OWNER, OFFICE POLICY MANUALS, BROKER BUYING PROPERTY, SHORT TERM RENTALS and SINGLE AGENT VERSUS TRANSACTION-BROKER."],
         "check": [("A change to terms made BEFORE acceptance goes on:", "A Counterproposal", ["An Amend/Extend", "A Notice to Terminate"], "Named on the Colorado state outline."),
                   ("A residential listing contract is subject to:", "The prohibited-terms rules for broker engagement contracts", ["No special restrictions", "The subdivision laws"], "C.R.S. 12-10-403.5."),
                   ("Commission Position statements address, among other things:", "Release of earnest money deposits and working with a for sale by owner", ["MLS rules", "Appraisal methodology"], "Division of Real Estate Commission Positions.")]},
    ],
    "traps": [
        "Fill in blanks - never draft. Attorney-drafted forms must carry the attorney's name.",
        "Counterproposal before acceptance; Amend/Extend after.",
        "Deed of trust and public trustee, not mortgage and judicial foreclosure.",
    ],
    "vocab": [
        ["Commission-approved form", "A form promulgated by the Real Estate Commission."],
        ["Counterproposal", "Colorado's counter-offer form."],
        ["Closing Instructions", "The parties' written instructions to the closing entity."],
        ["Public trustee", "The Colorado officer who conducts deed of trust foreclosures."],
        ["Amend/Extend", "The form changing terms after a contract is accepted."],
    ],
    "examples": [],
}

STUDY["co/requirements"] = {
    "summary": "Eleven items on how a brokerage is run: who may advertise in whose name, how commissions may move, and what must be disclosed.",
    "sections": [
        {"h": "Advertising and names (Rule 6.10)",
         "l": ["No broker may be licensed to conduct brokerage services under MORE THAN ONE BROKERAGE FIRM, and no broker or firm may conduct or promote brokerage services EXCEPT IN THE NAME UNDER WHICH THEY APPEAR IN THE COMMISSION'S RECORDS.",
               "Brokers must not advertise so as to MISLEAD THE PUBLIC about the identity of the broker or the firm, and ALL ADVERTISING must be done CLEARLY AND CONSPICUOUSLY IN THE NAME OF THE BROKER'S BROKERAGE FIRM.",
               "EXCEPTION: a broker advertising REAL PROPERTY THEY OWN that is NOT LISTED with their firm is exempt from advertising it in the firm's name.",
               "A firm may use a TRADE NAME in addition to or instead of its legal name, and the trade name must be FILED WITH THE COMMISSION. A firm may use ONLY ONE TRADE NAME.",
               "A firm using a third party's TRADE NAME OR TRADEMARK must display, clearly and conspicuously, 'Each (trade name) brokerage business is independently owned and operated' or 'Each office independently owned and operated'.",
               "A broker may not use a PROFESSIONAL DESIGNATION in advertising unless they are in good standing and it is EASILY VERIFIABLE, and must be able to VERIFY any advertised award, membership or achievement on request from the public or the Commission.",
               "TEAMS must not advertise so as to mislead the public about the identity of the team's brokerage firm, and the rules forbid certain words in a team's name."],
         "check": [("All Colorado advertising must appear:", "Clearly and conspicuously in the name of the broker's brokerage firm", ["In the individual broker's name", "In the seller's name"], "Commission Rule 6.10.A.4."),
                   ("A broker advertising property they personally own that is not listed with their firm:", "Is exempt from using the firm's name", ["Must still use the firm's name", "May not advertise at all"], "Commission Rule 6.10.A.4."),
                   ("How many trade names may a Colorado brokerage firm use?", "One", ["Two", "Any number", "None"], "Commission Rule 6.10.A.7."),
                   ("A firm using a franchisor's trade name must display:", "A statement that each office is independently owned and operated", ["The franchisor's licence number", "A disclaimer of liability"], "Commission Rule 6.10.A.6."),
                   ("A broker may advertise a professional designation only if:", "They are in good standing and it is easily verifiable", ["They once held it", "The MLS recognises it"], "Commission Rule 6.10.A.8.")]},
        {"h": "Brokerage administration and supervision",
         "l": ["The outline covers EMPLOYER/EMPLOYEE RELATIONSHIPS, PLACE OF BUSINESS requirements and OFFICE POLICY requirements.",
               "Rule 6.3 sets the EMPLOYING BROKER'S RESPONSIBILITIES AND SUPERVISION, and Rule 6.4 requires BROKERAGE FIRM POLICIES. The Commission publishes a position statement on OFFICE POLICY MANUALS.",
               "Rule 6.2 requires COMPETENCY: a broker must be competent in the services they offer.",
               "C.R.S. 12-10-222 makes a broker responsible for the ACTS OF THIRD PARTIES in defined circumstances, and the employing broker's duty to supervise is NOT limited by the fact that the brokerage relationship runs only with the designated broker (12-10-408(2)(e)(II)).",
               "UNLICENSED PERSONAL ASSISTANTS are their own outline heading: they may do clerical work but not the activities that require a licence.",
               "SIGN CROSSING - placing a sign on property listed by another firm, or soliciting such a listing - is a named topic."],
         "check": [("An employing broker's duty to supervise licensees:", "Is not limited by the rule that the relationship runs with the designated broker", ["Ends once a designated broker is named", "Applies only to new licensees"], "C.R.S. 12-10-408(2)(e)(II)."),
                   ("An unlicensed personal assistant may:", "Perform clerical tasks, but not activities requiring a licence", ["Show property to buyers", "Negotiate offers"], "Named on the Colorado state outline."),
                   ("Colorado requires each brokerage firm to maintain:", "Written office policies", ["A bond", "A franchise agreement"], "Commission Rule 6.4.")]},
        {"h": "Commissions, referrals and inducements",
         "l": ["BROKER REMUNERATION: C.R.S. 12-10-221 governs how a broker is paid, and a broker may not receive compensation from more than one party without full disclosure and consent.",
               "REFERRAL FEES must CONFORM WITH FEDERAL LAW - C.R.S. 12-10-304 ties Colorado's rule to RESPA, and the Commission publishes positions on RESPA AND REFERRAL FEES and on a BROKER'S PAYMENT OR REBATING of part of a commission.",
               "AFFILIATED BUSINESS ARRANGEMENTS are regulated by C.R.S. 12-10-218, which requires disclosure where the broker has an interest in a settlement service provider.",
               "The outline names INDUCEMENTS FROM SETTLEMENT SERVICE PROVIDERS as its own topic - the Colorado-specific restriction on accepting things of value from title companies and the like.",
               "DISCLOSURE OF CONFLICT OF INTEREST OR LICENSED STATUS is a separate heading: a licensee buying or selling for their own account must disclose their licensed status, and the Commission publishes a position on BROKER BUYING PROPERTY."],
         "check": [("Colorado referral fees must:", "Conform with federal law, meaning RESPA", ["Be capped at 25%", "Be paid only to Colorado brokers"], "C.R.S. 12-10-304."),
                   ("Where a broker has an interest in a settlement service provider, Colorado requires:", "Disclosure of the affiliated business arrangement", ["Nothing", "Commission approval"], "C.R.S. 12-10-218."),
                   ("A licensee buying property for their own account must:", "Disclose their licensed status", ["Use a nominee", "Resign the listing"], "Named on the Colorado state outline.")]},
    ],
    "traps": [
        "One firm, one trade name, and every advertisement in the firm's name - unless it is the broker's own unlisted property.",
        "Referral fees are tested through RESPA, not a Colorado cap.",
        "Supervision survives the designated broker rule.",
    ],
    "vocab": [
        ["Employing broker", "The broker responsible for supervising a firm's licensees."],
        ["Trade name", "A filed business name a firm may advertise under."],
        ["Sign crossing", "Interfering with another firm's listing sign or listing."],
        ["Affiliated business arrangement", "An ownership link to a settlement service provider."],
    ],
    "examples": [],
}

STUDY["co/closing"] = {
    "summary": "Ten items - unusual for a state portion. Colorado brokers are at the closing table and are answerable for the numbers on the statement.",
    "sections": [
        {"h": "What the outline tests",
         "l": ["COMPUTATION OF PRORATION - taxes, interest, rents and association dues divided between buyer and seller as of the closing date.",
               "RESPONSIBILITY FOR ACCURACY OF CLOSING STATEMENTS - in Colorado the BROKER is responsible for the accuracy of the closing statement for their party, even where a title company prepares it.",
               "ENSURING THAT CLOSING STATEMENTS MATCH CONTRACT INSTRUCTIONS - the figures must reflect the Contract to Buy and Sell and the Closing Instructions, not whatever the closing entity assumed.",
               "RESPONSIBILITIES OF PARTIES AT CLOSING and the CLOSING DOCUMENTS themselves.",
               "A broker must keep a COPY OF THE CLOSING STATEMENT in the transaction file; transaction records are kept FOUR YEARS from the CONSUMMATION DATE of the transaction (Commission rules)."],
         "check": [("Who is responsible for the accuracy of a Colorado closing statement?", "The broker, for their own party", ["The title company alone", "The lender", "Nobody"], "Named on the Colorado state outline."),
                   ("Closing figures must match:", "The contract and the closing instructions", ["The MLS listing", "The appraisal"], "Named on the Colorado state outline."),
                   ("Colorado transaction records, including closing statements, must be kept for:", "Four years from the consummation date", ["One year", "Three years", "Seven years"], "Commission Rules; the manual gives four years."),
                   ("Prorations divide items such as:", "Taxes, interest, rents and association dues as of the closing date", ["The sale price", "The commission"], "Named on the Colorado state outline.")]},
        {"h": "Working the prorations",
         "p": ["The exam's closing maths is ordinary proration, but Colorado tests it as state content because the broker signs off on it. Work in three steps: find the ANNUAL OR MONTHLY amount; divide by the number of days in the period the question tells you to use; multiply by the number of days each party owns. Then decide who gets the DEBIT and who the CREDIT - the party who has had the benefit pays."],
         "check": [("In a proration, the party who received the benefit of the period:", "Is debited for it", ["Is credited for it", "Pays nothing"], "Standard proration practice tested on the Colorado outline."),
                   ("A prepaid item the seller has already paid beyond closing produces:", "A credit to the seller and a debit to the buyer", ["A debit to the seller", "No entry"], "Standard proration practice tested on the Colorado outline.")]},
    ],
    "traps": [
        "The broker - not the title company - answers for the statement's accuracy.",
        "Four years from consummation for the transaction file.",
    ],
    "vocab": [
        ["Proration", "Dividing a shared cost between buyer and seller at closing."],
        ["Debit", "An amount a party owes on the closing statement."],
        ["Credit", "An amount shown in a party's favour."],
        ["Consummation date", "The date the four-year retention clock starts."],
    ],
    "examples": [
        {"t": "Rent proration",
         "s": "Rent of $1,500 for a 30-day month was collected by the seller. Closing is on the 10th.",
         "w": ["The seller has the whole month's rent but owns only 10 days of it.",
               "The buyer owns 20 days: 20/30 x $1,500 = $1,000.",
               "So $1,000 is a DEBIT to the seller and a CREDIT to the buyer."],
         "k": "Collected rent runs with the days of ownership, so the seller hands over the buyer's share."},
    ],
}

STUDY["co/additional"] = {
    "summary": "Seven items across five unrelated Colorado subjects. Water rights and fair housing carry most of the weight.",
    "sections": [
        {"h": "Colorado fair housing",
         "l": ["Colorado's fair housing rules are in the COLORADO ANTI-DISCRIMINATION ACT, C.R.S. 24-34-501 et seq. The state passed statewide fair housing in 1959 - NINE YEARS BEFORE the federal Fair Housing Act.",
               "The Colorado Civil Rights Division states that Colorado's law is MORE EXPANSIVE than federal law because it adds ANCESTRY, CREED, MARITAL STATUS, SEXUAL ORIENTATION and SOURCE OF INCOME as protected classes.",
               "It also applies to MORE PROPERTIES: federal law does NOT apply to OWNER-OCCUPIED BUILDINGS WITH FOUR OR FEWER UNITS, but Colorado's law does.",
               "ALL HOUSING offered for sale, lease, rent or transfer in Colorado is covered, and the Act reaches REAL ESTATE TRANSACTIONS generally - making and purchasing residential loans, constructing, improving or maintaining a dwelling, and the SELLING, BROKERING OR APPRAISING of residential real property.",
               "The familial status protection does not apply in limited circumstances, such as HOUSING FOR OLDER PEOPLE and the sale of a single-family home WITHOUT a broker, advertising or other housing professional.",
               "Discrimination is also a ground for licence discipline under C.R.S. 12-10-217, and the CCRD is a HUD-certified FAIR HOUSING ASSISTANCE PROGRAM agency, so most Colorado housing cases are DUAL-FILED with HUD."],
         "check": [("Which is protected under Colorado fair housing law but not the federal Fair Housing Act?", "Source of income", ["Race", "Color", "National origin"], "Colorado Civil Rights Division, C.R.S. 24-34-501 et seq."),
                   ("Colorado also protects:", "Ancestry, creed, marital status and sexual orientation", ["Credit score", "Occupation"], "Colorado Civil Rights Division."),
                   ("An owner-occupied four-unit building is:", "Covered by Colorado fair housing law, though exempt federally", ["Exempt under both", "Covered only if a broker is used"], "Colorado Civil Rights Division."),
                   ("Colorado passed statewide fair housing legislation in:", "1959, nine years before the federal Act", ["1968", "1974", "1988"], "Colorado Civil Rights Division.")]},
        {"h": "Water and the rest",
         "l": ["WATER RIGHTS AND DISCLOSURES are a named topic: Colorado water rights are a separate property interest that may or may not pass with the land, and the Contract to Buy and Sell carries a SOURCE OF WATER disclosure. A WELL CHANGE OF OWNERSHIP must be filed with the Division of Water Resources on transfer.",
               "PROPERTY MANAGEMENT and the LANDLORD TENANT ACT are a named topic. Money received for property management goes into the firm's trust account NO LATER THAN FIVE BUSINESS DAYS after receipt or mutual execution of the lease, whichever is later (Commission Rule 5.7.A).",
               "A firm receipting for SECURITY DEPOSITS may NOT deliver them to the owner without the TENANT'S WRITTEN AUTHORISATION in a lease, or unless WRITTEN NOTICE has been given to the tenant telling them who holds the deposit and how to request its return (Rule 5.8.A).",
               "Where a firm takes over management from another firm, it must disclose the status of any security deposit held by the previous firm, in writing, to the owner and tenant WITHIN 30 DAYS, and the previous firm must TRANSFER the deposit WITHIN 60 DAYS of the new management agreement (Rule 5.8.B).",
               "COLORADO TAXES and the FORECLOSURE PROTECTION ACT AND PROCESSES complete the heading - Colorado forecloses deeds of trust through the PUBLIC TRUSTEE, and the Commission's Foreclosure Property Addendum attaches to contracts for properties in foreclosure."],
         "check": [("Property management money must reach the trust account within:", "Five business days of receipt or mutual execution of the lease, whichever is later", ["Three business days", "One business day"], "Commission Rule 5.7.A."),
                   ("A firm may hand a tenant's security deposit to the owner:", "Only with the tenant's written authorisation in a lease, or after written notice to the tenant", ["On the owner's demand", "At any time"], "Commission Rule 5.8.A."),
                   ("When management transfers between firms, the deposit must be transferred within:", "60 days of the new management agreement", ["30 days", "90 days"], "Commission Rule 5.8.B."),
                   ("Colorado foreclosures of deeds of trust run through:", "The public trustee", ["The sheriff only", "The district court in every case"], "Named on the Colorado state outline.")]},
    ],
    "traps": [
        "Source of income is the Colorado addition most often tested.",
        "Colorado fair housing reaches owner-occupied 1-4 unit buildings that federal law exempts.",
        "Property management money: 5 business days. Everything else: 3.",
    ],
    "vocab": [
        ["CADA", "The Colorado Anti-Discrimination Act."],
        ["Source of income", "A Colorado protected class covering vouchers and benefits."],
        ["Public trustee", "The county officer who conducts deed of trust foreclosures."],
        ["Source of Water addendum", "The Commission form disclosing the water supply."],
    ],
    "examples": [],
}

STUDY["co/licensing"] = {
    "summary": "Five items. The numbers: 168 hours to qualify, a three-year licence, 24 hours of continuing education with 12 of them the Commission's own update, and errors and omissions insurance for everyone active.",
    "sections": [
        {"h": "Qualifying education (C.R.S. 12-10-203(4))",
         "l": ["An applicant must complete approved courses as follows: 48 HOURS in REAL ESTATE LAW AND REAL ESTATE PRACTICE; 48 HOURS in UNDERSTANDING AND PREPARATION OF COLORADO REAL ESTATE CONTRACTS; and a total of 72 HOURS drawn from TRUST ACCOUNTS AND RECORD KEEPING, REAL ESTATE CLOSINGS, CURRENT LEGAL ISSUES and PRACTICAL APPLICATIONS. That is 168 HOURS in all.",
               "An applicant already licensed as a BROKER IN ANOTHER JURISDICTION need complete only the CONTRACTS course and REAL ESTATE CLOSINGS.",
               "A broker who will hold MONEY BELONGING TO OTHERS must have completed 12 HOURS of instruction in TRUST ACCOUNTS.",
               "Colorado licenses everyone as a BROKER - there is no separate salesperson licence. The outline's 'types of licenses' refers to ASSOCIATE BROKER, INDEPENDENT BROKER and EMPLOYING BROKER."],
         "check": [("Colorado prelicence education totals:", "168 hours", ["90 hours", "120 hours", "60 hours"], "C.R.S. 12-10-203(4)(a): 48 + 48 + 72."),
                   ("Of those hours, how many cover Colorado contracts?", "48", ["24", "72", "12"], "C.R.S. 12-10-203(4)(a)(II)."),
                   ("A broker licensed in another state applying in Colorado must complete:", "The Colorado contracts course and real estate closings", ["All 168 hours", "Nothing"], "C.R.S. 12-10-203(4)(b)."),
                   ("Colorado's entry-level licence is:", "A broker's licence; there is no salesperson licence", ["A salesperson licence", "An apprentice licence"], "C.R.S. title 12 article 10 part 2.")]},
        {"h": "Renewal and continuing education (C.R.S. 12-10-213)",
         "l": ["For a THREE-YEAR licence, the licensee must either PASS THE COLORADO PORTION OF THE REAL ESTATE EXAM within the previous three years, or complete at least 24 HOURS OF CREDIT - 12 OF WHICH must be the credits the COMMISSION DEVELOPS under subsection (2).",
               "For a licence expiring LESS THAN THREE YEARS after issue, the same 24 hours applies but AT LEAST 8 must be the Commission-developed credits.",
               "The Commission develops 12 HOURS of credit designed to keep licensees current, INCLUDING AN UPDATE OF THE CURRENT STATUTES AND COMMISSION RULES - the Annual Commission Update.",
               "Successful completion requires PASSING A WRITTEN EXAMINATION on the material, and the Commission AUDITS those examinations.",
               "Other credits come from approved courses contributing directly to professional competence, in subjects the statute lists - real estate law, contracts, finance, appraisal, closing, ETHICS, condominiums and co-operatives, time-sharing, property management, AGENCY, and others.",
               "A licensee renewing a licence that expires on 31 DECEMBER OF THE YEAR IT WAS ISSUED is NOT subject to the education requirement."],
         "check": [("Colorado continuing education is:", "24 hours per three-year licence, 12 of them the Commission-developed credits", ["12 hours a year", "30 hours per cycle", "No requirement"], "C.R.S. 12-10-213(1)(a)."),
                   ("The Commission-developed credits must include:", "An update of the current statutes and Commission rules", ["A sales skills module", "An appraisal course"], "C.R.S. 12-10-213(2)."),
                   ("A licensee may satisfy the education requirement instead by:", "Passing the Colorado portion of the real estate examination within the licence period", ["Paying a higher fee", "Attending a Commission meeting"], "C.R.S. 12-10-213(1)."),
                   ("Continuing education credits require:", "Satisfactory passage of a written examination on the material", ["Attendance only", "A certificate of completion only"], "C.R.S. 12-10-213(2).")]},
        {"h": "Errors and omissions insurance (C.R.S. 12-10-204)",
         "l": ["EVERY LICENSEE must maintain ERRORS AND OMISSIONS INSURANCE covering all licensed activities - EXCEPT an INACTIVE broker, and except an ATTORNEY LICENSEE who carries professional malpractice insurance covering their licensed activities.",
               "The DIVISION makes a GROUP POLICY available to all licensees through competitive bid, and the insurer has NO RIGHT TO CANCEL A LICENSEE. A licensee may instead obtain their own coverage if it meets the Division's minimum requirements.",
               "Each licensee must FILE A CERTIFICATE OF COVERAGE with the Commission by the ANNUAL PREMIUM RENEWAL DATE, and the Commission must notify licensees of the required terms AT LEAST THIRTY DAYS BEFORE that date.",
               "The outline also covers LICENCE MAINTENANCE: renewal, changes, expiration, suspension and INACTIVE STATUS (C.R.S. 12-10-211)."],
         "check": [("Errors and omissions insurance in Colorado is:", "Required of every licensee except an inactive broker or an insured attorney licensee", ["Optional", "Required only of employing brokers"], "C.R.S. 12-10-204(1)."),
                   ("A licensee must file with the Commission:", "A certificate of coverage by the annual premium renewal date", ["A copy of the policy each month", "Nothing"], "C.R.S. 12-10-204(3)."),
                   ("The Division's group errors and omissions policy:", "Must be available to all licensees, with no right for the insurer to cancel a licensee", ["May exclude high-risk licensees", "Is only for new licensees"], "C.R.S. 12-10-204(1).")]},
    ],
    "traps": [
        "168 hours, made of 48 + 48 + 72.",
        "24 continuing education hours per three-year licence, 12 of them the Commission update.",
        "E&O insurance is mandatory for every active licensee.",
        "Colorado has no salesperson licence - everyone is a broker.",
    ],
    "vocab": [
        ["Associate broker", "A licensed broker working under an employing broker."],
        ["Employing broker", "The broker who supervises a firm's associates."],
        ["Annual Commission Update", "The Commission-developed continuing education credits."],
        ["Inactive status", "A licence not in use, and the one E&O exception."],
    ],
    "examples": [],
}

STUDY["co/records"] = {
    "summary": "Five items on money and paper. The deposit deadlines and the four-year retention rule are the reliable marks.",
    "sections": [
        {"h": "Trust accounts (Commission Rule 5)",
         "l": ["MONEY BELONGING TO OTHERS accepted by a broker or firm must be kept SEPARATE from the broker's or firm's own funds, in a TRUST OR ESCROW ACCOUNT that contains ONLY money belonging to others.",
               "If a firm is NOT in possession of money belonging to others, there is NO OBLIGATION to maintain a separate trust or escrow account.",
               "DEPOSIT DEADLINES: money received for PROPERTY MANAGEMENT goes in NO LATER THAN FIVE BUSINESS DAYS after receipt of funds or mutual execution of the lease, whichever is later. ALL OTHER money belonging to others goes in NO LATER THAN THREE BUSINESS DAYS after receipt or mutual execution of the contract, whichever is later (Rule 5.7).",
               "DIVERSION AND CONVERSION PROHIBITED: money belonging to one beneficiary must not be used for another beneficiary, and never for the benefit of the firm or broker (Rule 5.9).",
               "COMMINGLING PROHIBITED: a broker's or firm's personal or business operating funds must not be mixed with money belonging to others. Money in the account that becomes DUE AND PAYABLE TO THE FIRM must be WITHDRAWN MONTHLY (Rule 5.10).",
               "Unless the parties agree otherwise in writing, money belonging to others must NOT be invested in anything with a FIXED MATURITY or an EARLY-WITHDRAWAL PENALTY.",
               "A firm receiving money belonging to others must establish WRITTEN policies for it."],
         "check": [("Earnest money must reach a Colorado trust account within:", "Three business days of receipt or mutual execution of the contract, whichever is later", ["One business day", "Five business days", "At closing"], "Commission Rule 5.7.B."),
                   ("Property management money must be deposited within:", "Five business days of receipt or mutual execution of the lease, whichever is later", ["Three business days", "Ten days"], "Commission Rule 5.7.A."),
                   ("Money in the trust account that has become due to the firm must be:", "Withdrawn monthly", ["Left until year end", "Withdrawn at each closing"], "Commission Rule 5.10.A."),
                   ("A firm holding no money belonging to others:", "Need not maintain a separate trust or escrow account", ["Must still open one", "Must post a bond"], "Commission Rule 5."),
                   ("Trust money may not be placed in:", "An account with a fixed maturity or early-withdrawal penalty, unless the parties agree in writing", ["Any interest-bearing account", "A credit union"], "Commission Rule 5.6.")]},
        {"h": "Transaction records",
         "l": ["A broker must RETAIN ALL RECORDS relating to a transaction for FOUR YEARS from the CONSUMMATION DATE of the transaction, or from the date the transaction otherwise ends.",
               "An ATTORNEY-DRAFTED FORM used by the brokerage must be retained for FOUR YEARS from the date it was used.",
               "A course provider must keep ATTENDANCE RECORDS for FOUR YEARS from the date of the course.",
               "On the Commission's request, a broker must produce a COPY OF ANY ADVERTISING OR PROMOTIONAL MATERIAL used.",
               "RECORDS - EVIDENCE - INSPECTION: C.R.S. 12-10-216 makes the broker's records available to the Commission, and the Commission may conduct INVESTIGATIONS OR AUDITS (C.R.S. 12-10-217)."],
         "check": [("Colorado transaction records must be retained for:", "Four years from the consummation date", ["One year", "Three years", "Seven years"], "Commission Rules; Colorado Real Estate Manual."),
                   ("An attorney-drafted form used by a brokerage must be kept:", "Four years from the date it was used", ["Until the deal closes", "Indefinitely"], "Commission Rules."),
                   ("On request, a broker must give the Commission:", "A copy of any advertising or promotional material used", ["Only the listing agreement", "Nothing without a subpoena"], "Commission Rules.")]},
    ],
    "traps": [
        "Three business days for earnest money, five for property management.",
        "Four years is the Colorado retention period for everything.",
        "Earned money comes OUT monthly - leaving it in is commingling.",
    ],
    "vocab": [
        ["Money Belonging to Others", "Colorado's term for trust funds."],
        ["Diversion", "Using one beneficiary's money for another's benefit."],
        ["Conversion", "Using trust money for the broker's own benefit."],
        ["Consummation date", "When the four-year record clock starts."],
    ],
    "examples": [],
}

STUDY["co/commission"] = {
    "summary": "Two items. Know what the Commission can do and how a case moves.",
    "sections": [
        {"h": "Powers and process",
         "l": ["The outline lists the GENERAL POWERS OF THE REAL ESTATE COMMISSION, and INVESTIGATIONS OR AUDITS, HEARINGS AND APPEALS, CRIMINAL VIOLATIONS and LICENCE LAW VIOLATIONS.",
               "C.R.S. 12-10-217 is the discipline section: investigation, revocation and actions against a licensee. C.R.S. 12-10-219 provides for a HEARING BEFORE AN ADMINISTRATIVE LAW JUDGE with review.",
               "The Commission may SUBPOENA witnesses and compel production of documents (12-10-224), and FAILURE TO OBEY A SUBPOENA carries a penalty (12-10-225).",
               "The Commission has power to seek INJUNCTIONS (12-10-226), and C.R.S. 12-10-223 covers VIOLATIONS - acting without a licence and the like.",
               "C.R.S. 12-10-216 makes the broker's RECORDS available as evidence and open to INSPECTION.",
               "C.R.S. 12-10-220 gives the Commission general RULEMAKING power, and 12-10-220.5 requires a RADON DISCLOSURE by rule."],
         "check": [("A Colorado disciplinary hearing is held before:", "An administrative law judge", ["The full Commission only", "A district court jury"], "C.R.S. 12-10-219."),
                   ("Failing to obey a Commission subpoena:", "Carries a statutory penalty", ["Has no consequence", "Ends the investigation"], "C.R.S. 12-10-225."),
                   ("The Commission may also:", "Seek an injunction", ["Order criminal sentences", "Void contracts"], "C.R.S. 12-10-226."),
                   ("Colorado requires a disclosure by Commission rule about:", "Radon", ["Asbestos", "Mold"], "C.R.S. 12-10-220.5.")]},
    ],
    "traps": [
        "Administrative law judge, not the Commission sitting as a court.",
        "Radon has its own statutory disclosure mandate in Colorado.",
    ],
    "vocab": [
        ["Division of Real Estate", "The agency; the Commission sits within it."],
        ["Administrative law judge", "Who hears a contested disciplinary case."],
        ["Audit", "The Commission's examination of a broker's records and accounts."],
    ],
    "examples": [],
}


# ------------------------------------------------------------- questions

Q = [
 # relationships
 ("co/relationships", "Default", 1, "In Colorado, a broker who has signed no written agreement with a consumer is:",
  "A transaction-broker", ["A single agent", "A dual agent", "A subagent of the seller"],
  "C.R.S. 12-10-403(2)."),
 ("co/relationships", "Dual agency", 1, "Dual agency in Colorado is:",
  "Prohibited", ["Allowed with written consent", "Allowed in commercial transactions", "The default relationship"],
  "C.R.S. 12-10-406."),
 ("co/relationships", "Single agency", 1, "Single agency in Colorado is established by:",
  "A written agreement with the party to be represented", ["An oral agreement", "Showing the property", "Accepting a commission"],
  "C.R.S. 12-10-403(2)."),
 ("co/relationships", "Subagency", 2, "A Colorado transaction-broker:",
  "May cooperate with other brokers but may not create subagents", ["May appoint subagents freely", "May not work with other brokers"],
  "C.R.S. 12-10-407(8)."),
 ("co/relationships", "Transaction-broker", 1, "A Colorado transaction-broker must present offers:",
  "In a timely manner, even where the property is already under contract", ["Only until a contract is signed", "Only at the seller's request"],
  "C.R.S. 12-10-407(2)(b)(I)."),
 ("co/relationships", "Transaction-broker", 1, "Which may a Colorado transaction-broker NOT disclose without all parties' informed consent?",
  "That the seller would accept less than the asking price", ["A known roof defect", "A known environmental hazard", "A title problem"],
  "C.R.S. 12-10-407(3)(b)."),
 ("co/relationships", "Transaction-broker", 2, "A transaction-broker must disclose to a prospective seller:",
  "Adverse material facts actually known about the buyer's financial ability to perform", ["The buyer's full credit report", "Nothing about the buyer"],
  "C.R.S. 12-10-407(2)(b)(VII)."),
 ("co/relationships", "Transaction-broker", 2, "A Colorado transaction-broker's duty to inspect the property is:",
  "None, unless otherwise agreed", ["A full physical inspection", "A visual walkthrough of every room"],
  "C.R.S. 12-10-407(4)."),
 ("co/relationships", "Transaction-broker", 2, "A transaction-broker must inform the parties that they are:",
  "Not vicariously liable for the broker's acts", ["Jointly liable with the broker", "Liable only after closing"],
  "C.R.S. 12-10-407(2)(b)(VIII)."),
 ("co/relationships", "Transaction-broker", 3, "Facts or suspicions that may psychologically impact or stigmatize a property:",
  "May not be disclosed without the informed consent of all parties", ["Must always be disclosed", "Must be disclosed to buyers only"],
  "C.R.S. 12-10-407(3)(e); 38-35.5-101."),
 ("co/relationships", "Transaction-broker", 3, "Knowledge within an entity acting as a transaction-broker is:",
  "Not imputed between the parties or among persons within the entity", ["Imputed to all licensees", "Imputed to the employing broker only"],
  "C.R.S. 12-10-407(7)."),
 ("co/relationships", "Single agent", 1, "The Colorado statute describes a single agent as:",
  "A limited agent", ["A universal agent", "A general agent", "An unlimited fiduciary"],
  "C.R.S. 12-10-404(1)."),
 ("co/relationships", "Single agent", 2, "Must a Colorado seller's agent keep seeking offers once the property is under contract?",
  "No; that obligation is expressly excluded", ["Yes, always", "Yes, unless the seller objects"],
  "C.R.S. 12-10-404(1)(c)(I)."),
 ("co/relationships", "Disclosure", 1, "Every Colorado broker must adopt:",
  "A written office policy identifying the relationships offered to the public", ["A published commission schedule", "A marketing plan"],
  "C.R.S. 12-10-408(1)(a)."),
 ("co/relationships", "Disclosure", 2, "If a consumer refuses to sign the transaction-broker disclosure, the broker:",
  "Notes that fact on a copy of the disclosure and retains it", ["May not work with them", "Must obtain a witness signature"],
  "C.R.S. 12-10-408(2)(a)(II)."),
 ("co/relationships", "Disclosure", 2, "A Colorado brokerage relationship exists:",
  "Only with the designated broker, not the employing broker or the brokerage company", ["With the whole firm", "With every licensee in the office"],
  "C.R.S. 12-10-408(2)(e)(I)."),
 ("co/relationships", "Disclosure", 3, "The rule that the relationship runs only with the designated broker:",
  "Does not limit the employing broker's duty to supervise or the firm's vicarious liability", ["Ends the employing broker's duties", "Shields the firm entirely"],
  "C.R.S. 12-10-408(2)(e)(II)."),
 ("co/relationships", "Both sides", 1, "A Colorado broker or team working with both consumers in one transaction may:",
  "Act as transaction-broker for both, or serve one and treat the other as a customer", ["Be a single agent for both", "Be a disclosed dual agent"],
  "Commission Rule 6.7."),
 ("co/relationships", "Customers", 2, "Performing ministerial tasks for a customer:",
  "Does not create an agency or transaction-broker relationship with them", ["Makes the customer a client", "Creates dual agency"],
  "Commission Rule 6.8."),
 ("co/relationships", "Customers", 3, "Which is a ministerial task in Colorado?",
  "Showing a property and conveying written offers and counteroffers", ["Advising on price strategy", "Negotiating terms for the customer"],
  "Commission Rule 6.8."),
 ("co/relationships", "Engagement contracts", 2, "A Colorado residential broker engagement contract may not:",
  "Purport to create a recordable lien or to run with the land", ["Exceed 90 days", "Be exclusive"],
  "C.R.S. 12-10-403.5(2)."),
 ("co/relationships", "Engagement contracts", 3, "Offering a broker engagement contract with a prohibited term is:",
  "An unfair or deceptive trade practice", ["A licence violation only", "Permitted with disclosure"],
  "C.R.S. 12-10-403.5(3)."),
 ("co/relationships", "Disclosure", 2, "A broker already representing one party must advise other potential parties:",
  "At the earliest reasonable opportunity", ["When an offer is written", "Only if asked"],
  "C.R.S. 12-10-408(2)(d)."),

 # forms
 ("co/forms", "Forms", 1, "A Colorado broker may complete:",
  "Commission-approved forms, or forms drafted by a Colorado attorney for the brokerage", ["Any form the broker writes", "Only MLS forms"],
  "C.R.S. 12-10-403(4)."),
 ("co/forms", "Forms", 2, "A form drafted for a brokerage by a Colorado attorney must show:",
  "The name of the attorney or law firm that drafted it", ["The Commission's seal", "The broker's licence number"],
  "C.R.S. 12-10-403(4)(b)(II)."),
 ("co/forms", "Forms", 1, "Filling in the blanks on a Commission-approved form is:",
  "Permitted, and not the unauthorised practice of law", ["The unauthorised practice of law", "Allowed only for employing brokers"],
  "C.R.S. 12-10-403(4)."),
 ("co/forms", "Counterproposal", 1, "Colorado's counter-offer form is called:",
  "The Counterproposal", ["The Counter-Offer", "The Amendment", "The Rider"],
  "Named on the Colorado state outline."),
 ("co/forms", "Counterproposal", 2, "A change to contract terms made BEFORE acceptance goes on:",
  "A Counterproposal", ["An Amend/Extend", "A Notice to Terminate", "A Closing Instruction"],
  "Named on the Colorado state outline."),
 ("co/forms", "Security", 1, "Colorado secures real estate loans with:",
  "A deed of trust, foreclosed through the public trustee", ["A mortgage foreclosed judicially", "An installment land contract"],
  "Named on the Colorado state outline."),
 ("co/forms", "Closing", 2, "The form by which the parties instruct the closing entity is:",
  "Closing Instructions", ["The Settlement Statement", "The Counterproposal", "The Listing Contract"],
  "Named on the Colorado state outline."),
 ("co/forms", "Addenda", 2, "A Foreclosure Property Addendum is used when:",
  "The property being purchased is in foreclosure", ["Every residential contract is written", "The buyer is paying cash"],
  "Named on the Colorado state outline."),
 ("co/forms", "Forms", 3, "May a Colorado broker complete a standard form conveying personal property as part of the transaction?",
  "Yes, where the form is a standard form and the broker is performing licensed activities", ["No, never", "Only with an attorney present"],
  "C.R.S. 12-10-403(4)(a)."),
 ("co/forms", "Listings", 2, "A Colorado residential listing contract is:",
  "A broker engagement contract subject to the prohibited-terms rules", ["Exempt from statutory restrictions", "Governed by the subdivision laws"],
  "C.R.S. 12-10-403.5."),
 ("co/forms", "Practice of law", 2, "Drafting new contract language for a client is:",
  "The unauthorised practice of law for a Colorado broker", ["Allowed with the client's consent", "Allowed for cash transactions"],
  "C.R.S. 12-10-403(4); the outline lists Practice of Law separately."),
 ("co/forms", "Retention", 3, "An attorney-drafted form used by a Colorado brokerage must be retained for:",
  "Four years from the date it was used", ["One year", "Until the transaction closes"],
  "Commission Rules; Colorado Real Estate Manual."),

 # requirements
 ("co/requirements", "Advertising", 1, "All Colorado advertising must appear:",
  "Clearly and conspicuously in the name of the broker's brokerage firm", ["In the individual broker's name", "In the owner's name"],
  "Commission Rule 6.10.A.4."),
 ("co/requirements", "Advertising", 2, "A Colorado broker advertising property they own that is not listed with their firm:",
  "Is exempt from advertising it in the firm's name", ["Must still use the firm's name", "May not advertise it at all"],
  "Commission Rule 6.10.A.4."),
 ("co/requirements", "Advertising", 2, "How many trade names may a Colorado brokerage firm use?",
  "One", ["Two", "Any number", "None"],
  "Commission Rule 6.10.A.7."),
 ("co/requirements", "Advertising", 2, "A firm advertising under a franchisor's trade name must display:",
  "A statement that each office is independently owned and operated", ["The franchisor's licence number", "A liability disclaimer"],
  "Commission Rule 6.10.A.6."),
 ("co/requirements", "Advertising", 3, "A Colorado broker may advertise a professional designation only if:",
  "They are in good standing and the designation is easily verifiable", ["They held it at any time", "The MLS recognises it"],
  "Commission Rule 6.10.A.8."),
 ("co/requirements", "Advertising", 3, "A Colorado broker may be licensed under:",
  "One brokerage firm only", ["Two firms with consent", "Any number of firms"],
  "C.R.S. 12-10-203(9); Commission Rule 6.10.A.1."),
 ("co/requirements", "Supervision", 2, "An employing broker's duty to supervise:",
  "Survives the rule that the relationship runs only with the designated broker", ["Ends when a designated broker is named", "Applies only to new licensees"],
  "C.R.S. 12-10-408(2)(e)(II)."),
 ("co/requirements", "Assistants", 1, "An unlicensed personal assistant in Colorado may:",
  "Perform clerical tasks, but not activities requiring a licence", ["Show property to buyers", "Negotiate contract terms"],
  "Named on the Colorado state outline."),
 ("co/requirements", "Policies", 2, "Colorado requires each brokerage firm to maintain:",
  "Written office policies", ["A surety bond", "A franchise agreement"],
  "Commission Rule 6.4."),
 ("co/requirements", "Referrals", 2, "Colorado referral fees must:",
  "Conform with federal law, meaning RESPA", ["Be capped at 25%", "Go only to Colorado brokers"],
  "C.R.S. 12-10-304."),
 ("co/requirements", "Conflicts", 2, "A Colorado licensee buying property for their own account must:",
  "Disclose their licensed status", ["Buy through a nominee", "Resign the listing first"],
  "Named on the Colorado state outline; Commission Position 14."),

 # closing
 ("co/closing", "Accuracy", 1, "Who is responsible for the accuracy of a Colorado closing statement?",
  "The broker, for their own party", ["The title company alone", "The lender", "The buyer"],
  "Named on the Colorado state outline."),
 ("co/closing", "Accuracy", 2, "Closing statement figures must match:",
  "The contract and the closing instructions", ["The MLS listing", "The appraisal", "The lender's estimate"],
  "Named on the Colorado state outline."),
 ("co/closing", "Records", 1, "Colorado transaction records, including closing statements, must be kept for:",
  "Four years from the consummation date", ["One year", "Three years", "Seven years"],
  "Commission Rules; Colorado Real Estate Manual."),
 ("co/closing", "Prorations", 1, "In a proration, the party who had the benefit of the period:",
  "Is debited for it", ["Is credited for it", "Pays nothing"],
  "Standard proration practice tested on the Colorado outline."),
 ("co/closing", "Prorations", 2, "A seller who has prepaid an item beyond closing receives:",
  "A credit, with the buyer debited the same amount", ["A debit", "No entry at all"],
  "Standard proration practice tested on the Colorado outline."),
 ("co/closing", "Prorations", 2, "Rent of $1,500 for a 30-day month was collected by the seller and closing is on the 10th. The buyer's share is:",
  "$1,000, credited to the buyer and debited to the seller", ["$500, credited to the buyer", "$1,000, credited to the seller"],
  "20 of 30 days belong to the buyer: 20/30 x $1,500 = $1,000."),
 ("co/closing", "Documents", 3, "Prorations typically divide:",
  "Taxes, interest, rents and association dues as of the closing date", ["The purchase price", "The brokerage commission"],
  "Named on the Colorado state outline."),

 # additional
 ("co/additional", "Fair housing", 1, "Which is protected under Colorado fair housing law but not the federal Fair Housing Act?",
  "Source of income", ["Race", "Color", "National origin"],
  "Colorado Civil Rights Division; C.R.S. 24-34-501 et seq."),
 ("co/additional", "Fair housing", 1, "Colorado also protects:",
  "Ancestry, creed, marital status and sexual orientation", ["Credit score", "Occupation", "Length of residence"],
  "Colorado Civil Rights Division."),
 ("co/additional", "Fair housing", 2, "An owner-occupied building with four or fewer units is:",
  "Covered by Colorado fair housing law, although exempt under federal law", ["Exempt under both laws", "Covered only if a broker is used"],
  "Colorado Civil Rights Division."),
 ("co/additional", "Fair housing", 3, "Colorado passed statewide fair housing legislation in:",
  "1959, nine years before the federal Fair Housing Act", ["1968", "1974", "1988"],
  "Colorado Civil Rights Division."),
 ("co/additional", "Property management", 1, "Property management money must reach the trust account within:",
  "Five business days of receipt or mutual execution of the lease, whichever is later", ["Three business days", "One business day"],
  "Commission Rule 5.7.A."),
 ("co/additional", "Security deposits", 2, "A Colorado firm may deliver a tenant's security deposit to the owner:",
  "Only with the tenant's written authorisation in a lease, or after written notice to the tenant", ["On the owner's demand", "At any time"],
  "Commission Rule 5.8.A."),
 ("co/additional", "Foreclosure", 2, "Colorado forecloses deeds of trust through:",
  "The public trustee", ["The sheriff alone", "A district court action in every case"],
  "Named on the Colorado state outline."),

 # licensing
 ("co/licensing", "Education", 1, "Colorado prelicence education totals:",
  "168 hours", ["90 hours", "120 hours", "60 hours"],
  "C.R.S. 12-10-203(4)(a): 48 + 48 + 72."),
 ("co/licensing", "Education", 2, "How many of those hours cover understanding and preparing Colorado contracts?",
  "48", ["24", "72", "12"],
  "C.R.S. 12-10-203(4)(a)(II)."),
 ("co/licensing", "Licence types", 1, "Colorado's entry-level real estate licence is:",
  "A broker's licence; there is no salesperson licence", ["A salesperson licence", "An apprentice permit"],
  "C.R.S. title 12 article 10 part 2."),
 ("co/licensing", "Continuing education", 1, "Colorado continuing education for a three-year licence is:",
  "24 hours, 12 of them the Commission-developed credits", ["12 hours a year", "30 hours per cycle", "None"],
  "C.R.S. 12-10-213(1)(a)."),
 ("co/licensing", "E&O", 1, "Errors and omissions insurance in Colorado is:",
  "Required of every licensee except an inactive broker or an insured attorney licensee", ["Optional", "Required only of employing brokers"],
  "C.R.S. 12-10-204(1)."),

 # records
 ("co/records", "Deposits", 1, "Earnest money must reach a Colorado trust account within:",
  "Three business days of receipt or mutual execution of the contract, whichever is later", ["One business day", "Five business days", "At closing"],
  "Commission Rule 5.7.B."),
 ("co/records", "Commingling", 1, "Money in a Colorado trust account that has become due to the firm must be:",
  "Withdrawn monthly", ["Left until the year ends", "Withdrawn at each closing"],
  "Commission Rule 5.10.A."),
 ("co/records", "Trust accounts", 2, "A Colorado firm that holds no money belonging to others:",
  "Need not maintain a separate trust or escrow account", ["Must still open one", "Must post a bond"],
  "Commission Rule 5."),
 ("co/records", "Trust accounts", 3, "Unless the parties agree otherwise in writing, trust money may not be placed in:",
  "An account with a fixed maturity or an early-withdrawal penalty", ["Any interest-bearing account", "A credit union account"],
  "Commission Rule 5.6."),
 ("co/records", "Diversion", 2, "Using one beneficiary's trust money for another beneficiary is:",
  "Prohibited diversion", ["Allowed if repaid", "Allowed with the firm's consent"],
  "Commission Rule 5.9."),

 # commission
 ("co/commission", "Hearings", 1, "A Colorado real estate disciplinary hearing is held before:",
  "An administrative law judge", ["The full Commission sitting as a court", "A district court jury"],
  "C.R.S. 12-10-219."),
 ("co/commission", "Powers", 2, "The Colorado Real Estate Commission may also:",
  "Seek an injunction", ["Impose criminal sentences", "Void a contract between the parties"],
  "C.R.S. 12-10-226."),
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
            "id": "co-" + hashlib.sha1(q.encode()).hexdigest()[:8],
            "portion": "georgia", "topic": topic, "subtopic": sub,
            "sub": topic + "|" + sub, "concept": "Colorado " + sub.lower(),
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
        "code": "CO", "name": "Colorado", "abbr": "CO",
        "regulator": "Colorado Real Estate Commission",
        "pass": EXAM["pass"],
        "portions": {
            "national": {"scored": EXAM["national_scored"],
                         "minutes": EXAM["national_minutes"],
                         "pass": EXAM["national_pass"],
                         "blurb": "80 questions, 60 correct to pass."},
            "georgia": {"name": "Colorado law", "scored": EXAM["state_scored"],
                        "minutes": EXAM["state_minutes"],
                        "pass": EXAM["state_pass"],
                        "blurb": "74 questions, 53 correct to pass: statute, Commission rules and the approved forms."},
        },
        "topics": topics, "bank": bank, "study": study,
        "sources": SOURCES, "diffs": DIFFS,
    }


# Where Colorado departs from the national rule.
DIFFS = {
    "national/agency": [
        "Colorado FORBIDS DUAL AGENCY outright - there is no consent that cures it (C.R.S. 12-10-406).",
        "The DEFAULT relationship is TRANSACTION-BROKER; single agency requires a WRITTEN agreement (12-10-403(2)).",
        "A transaction-broker is NOT an agent, owes no loyalty, and may not create SUBAGENTS (12-10-407).",
        "Six categories of information may not be disclosed without all parties' informed consent, including a party's MOTIVATING FACTORS and anything that would STIGMATIZE the property (12-10-407(3)).",
        "The brokerage relationship runs only with the DESIGNATED BROKER - not the employing broker and not the firm (12-10-408(2)(e)).",
    ],
    "national/practice": [
        "Colorado licenses everyone as a BROKER: 168 hours of prelicence education, then 24 hours of continuing education per three-year licence, 12 of which are the Commission's own update (12-10-203, 12-10-213).",
        "ERRORS AND OMISSIONS INSURANCE is mandatory for every active licensee (12-10-204).",
        "Brokers complete COMMISSION-APPROVED FORMS and do not draft; the counter-offer is a COUNTERPROPOSAL (12-10-403(4)).",
        "Trust deposits: THREE business days for earnest money, FIVE for property management; records are kept FOUR YEARS (Commission Rules 5.7, and the manual's retention rule).",
        "All advertising goes in the FIRM'S name, one trade name per firm, except a broker's own unlisted property (Rule 6.10).",
    ],
    "national/disclosures": [
        "Colorado fair housing adds SOURCE OF INCOME, ancestry, creed, marital status and sexual orientation, and covers OWNER-OCCUPIED 1-4 UNIT buildings that federal law exempts.",
        "Colorado requires a RADON disclosure by Commission rule (C.R.S. 12-10-220.5).",
        "The BROKER is answerable for the accuracy of the closing statement, which must match the contract and the closing instructions.",
    ],
}


if __name__ == "__main__":
    import io, json, os
    here = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    out = os.path.join(here, "greprep", "packs", "CO.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    pack = build()
    with io.open(out, "w", encoding="utf-8") as f:
        json.dump(pack, f, ensure_ascii=False, indent=1, sort_keys=True)
    print("wrote", out, len(pack["bank"]), "questions,", len(pack["study"]), "lessons")
