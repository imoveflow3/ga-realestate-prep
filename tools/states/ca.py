"""California state content: lessons and practice questions.

Like Florida, California writes its own single examination: 150 questions,
three hours, 70% to pass for a salesperson. There is no separate national
portion, so the pack sets `single`. The material is still kept in two
groups because that is how it is studied: California law, and the general
principles and practice the state examines alongside it.

Every rule below was read from the official text on 2026-10-17:
  - Business and Professions Code, Division 4 (the Real Estate Law), as
    published by the Department of Real Estate in its own law book,
    "as amended and in effect January 1, 2026".
  - Regulations of the Real Estate Commissioner, title 10 of the California
    Code of Regulations, chapter 6, from the DRE's companion volume.
  - Civil Code ss. 1102 et seq. (transfer disclosure), 1710.2, 2079 et seq.
    (agency), from leginfo.legislature.ca.gov.
  - DRE form RE 425 (Rev. 6/25) for the seven examination areas and their
    weights, and the DRE's own "Taking the Exam" page for the length and
    the pass mark.
The section a fact comes from is cited next to it. Do not add a fact here
without reading its source first.

Note for anyone extending this: California, unlike Florida and Texas,
PERMITS dual agency with disclosure and consent. Do not carry a rule across
from another state's pack.
"""

EXAM = {
    # DRE: salesperson, 3 hours, 150 multiple-choice, 70% to pass.
    "state_scored": 63,      # the California-law share of the seven areas
    "state_minutes": 76,
    "national_scored": 87,   # general principles, practice, valuation, maths
    "national_minutes": 104,
    "pass": 0.70,
}

# key, label, questions out of the 150, blurb.
# RE 425 gives seven areas by percentage. Area 2 (agency, 17%) and Area 6
# (practice and disclosures, 25%) are the California-specific ones; the rest
# are carried by the shared general lessons with California notes attached.
TOPICS = [
    ("ca/agency", "Agency & fiduciary duties", 26,
     "Seller's agent, buyer's agent, dual agency, and the disclosure forms."),
    ("ca/practice", "Trust funds & brokerage practice", 14,
     "Trust fund handling, advertising, supervision, records, advance fees."),
    ("ca/licensing", "Licensing, discipline & the Recovery Account", 12,
     "Getting licensed, renewing, what the Commissioner can do, who the fund pays."),
    ("ca/disclosures", "California disclosures", 11,
     "The Transfer Disclosure Statement, natural hazards, and the inspection duty."),
]

SOURCES = [
    {"by": "California Department of Real Estate",
     "name": "Real Estate Law (Business and Professions Code, Division 4)",
     "note": "The DRE's own law book, in effect 1 January 2026. Every licensing, trust fund, discipline and Recovery Account rule here was read from it.",
     "url": "https://www.dre.ca.gov/files/pdf/relaw/relaw.pdf"},
    {"by": "California Department of Real Estate",
     "name": "Regulations of the Real Estate Commissioner (10 CCR ch. 6)",
     "note": "Trust fund handling, commingling, records, advertising and supervision.",
     "url": "https://www.dre.ca.gov/files/pdf/relaw/regs.pdf"},
    {"by": "California Legislature",
     "name": "Civil Code: ss. 1102 et seq., 1710.2, 2079 et seq.",
     "note": "The Transfer Disclosure Statement, death and HIV disclosure, the agency disclosure form and the agent's inspection duty.",
     "url": "https://leginfo.legislature.ca.gov/faces/codes_displayexpandedbranch.xhtml?tocCode=CIV"},
    {"by": "California Department of Real Estate",
     "name": "Examination Description (RE 425) and Taking the Exam",
     "note": "The seven examination areas with their weights, the three-hour length, and the 70% pass mark for salespersons.",
     "url": "https://www.dre.ca.gov/Examinees/TakingExam.html"},
]


# --------------------------------------------------------------- lessons

STUDY = {}

STUDY["ca/agency"] = {
    "summary": "The biggest single slice of the California exam. Unlike most states California PERMITS dual agency, with disclosure and consent - so the questions turn on which form goes to whom, when, and what a dual agent may never say.",
    "sections": [
        {"h": "The three relationships",
         "l": ["SELLER'S AGENT - owes fiduciary duties to the seller.",
               "BUYER'S AGENT - owes fiduciary duties to the buyer.",
               "DUAL AGENT - represents both. This is LAWFUL in California. What the law forbids is 'acting for more than one party in a transaction without the knowledge or consent of all parties' (B&P 10176(d)).",
               "Every licensee also owes honesty and fair dealing to the other side, and the statutory disclosure duties below."],
         "check": [("Dual agency in California is:", "Lawful, with the knowledge and consent of all parties", ["Prohibited entirely", "Lawful only in commercial deals"], "B&P 10176(d) punishes acting for more than one party WITHOUT consent."),
                   ("A salesperson's fiduciary duties run to:", "The broker's principal", ["Whoever pays the commission", "Both parties equally"], "The salesperson acts for the broker, who is the agent of the principal.")]},
        {"h": "The Agency Disclosure form (Civil Code 2079.14)",
         "l": ["The SELLER'S AGENT gives the disclosure form to the seller BEFORE entering into the listing agreement.",
               "The BUYER'S AGENT gives it to the buyer as soon as practicable BEFORE executing a buyer-broker representation agreement and before the buyer's offer to purchase.",
               "If the buyer's agent did not prepare the offer, the form must be presented not later than the NEXT BUSINESS DAY after receiving the offer from the buyer.",
               "The agent must obtain a SIGNED ACKNOWLEDGEMENT of receipt.",
               "The form itself (Civil Code 2079.16) sets out the duties of a seller's agent, a buyer's agent, and an agent representing both."],
         "check": [("The seller's agent must give the agency disclosure form to the seller:", "Before entering into the listing agreement", ["At the close of escrow", "When an offer arrives"], "Civil Code 2079.14(a)(1)."),
                   ("If a buyer writes their own offer, the buyer's agent must present the disclosure form:", "Not later than the next business day after receiving the offer", ["Within five days", "At closing"], "Civil Code 2079.14(a)(2).")]},
        {"h": "Confirming the relationship (Civil Code 2079.17)",
         "p": ["As soon as practicable, each agent must disclose whether they act as the seller's agent, the buyer's agent, or a DUAL AGENT. That relationship is then CONFIRMED in the purchase contract itself, or in a separate writing signed or acknowledged by the parties, prior to or coincident with the execution of the contract. The statute prints the exact confirmation wording, naming the brokerage firm and its licence number."],
         "check": [("The agency relationship must be confirmed:", "In the purchase contract or a separate writing, at or before execution", ["Only in the listing", "After closing"], "Civil Code 2079.17(a)-(b)."),
                   ("Agency confirmation names:", "The brokerage firm and its licence number", ["Only the salesperson", "Only the buyer"], "Civil Code 2079.17(c).")]},
        {"h": "What a dual agent may never say (Civil Code 2079.21)",
         "l": ["A dual agent may NOT, without the seller's express permission, tell the buyer any confidential information obtained from the seller - and vice versa.",
               "CONFIDENTIAL INFORMATION means facts about the client's financial position, motivations, bargaining position, or other personal information that may affect price - for example that the seller will take less than the listing price, or the buyer will pay more than offered.",
               "This protects PRICE confidences only. It does not cut down any other duty the dual agent owes."],
         "check": [("A dual agent may not reveal, without permission:", "That the seller will accept less than the listing price", ["A known defect in the roof", "The listing price"], "Civil Code 2079.21(c)."),
                   ("Confidential information under 2079.21 covers:", "Financial position, motivation and bargaining position", ["The physical condition of the property", "The square footage"], "Condition is disclosed, never concealed.")]},
        {"h": "The duty owed to a buyer (Civil Code 2079)",
         "p": ["A listing broker or salesperson - and a cooperating broker - owes a prospective buyer of RESIDENTIAL property of ONE TO FOUR dwelling units a duty to conduct a REASONABLY COMPETENT AND DILIGENT VISUAL INSPECTION of the property, and to disclose to the buyer all facts materially affecting the VALUE OR DESIRABILITY of the property that an investigation would reveal. An action for breach must be brought within TWO YEARS of the date of possession - recordation, close of escrow, or occupancy, whichever comes first (2079.4)."],
         "check": [("The agent's visual inspection duty applies to:", "Residential property of one to four dwelling units", ["All property including commercial", "Only new construction"], "Civil Code 2079(a)."),
                   ("An action for breach of the inspection duty must be brought within:", "Two years of the date of possession", ["Four years", "Six months"], "Civil Code 2079.4.")]},
        {"h": "Compensation and listings",
         "l": ["An EXCLUSIVE agreement must contain a DEFINITE, SPECIFIED DATE of final and complete termination. Claiming a fee under one that does not is grounds for discipline (B&P 10176(f)).",
               "Taking any SECRET or undisclosed compensation, commission or profit is grounds for discipline; the full amount must be revealed to the principal before or at the signing of the agreement (B&P 10176(g)).",
               "A licensee who takes an option to purchase under a listing must reveal the full amount of their profit in writing and obtain the principal's written consent (B&P 10176(h)).",
               "Commission rates are negotiable and are never set by law or by agreement among competitors."],
         "check": [("An exclusive listing in California must contain:", "A definite, specified termination date", ["A minimum 90-day term", "A guaranteed sale clause"], "B&P 10176(f)."),
                   ("A licensee who takes an undisclosed profit on a principal's transaction:", "May have the licence suspended or revoked", ["May keep it if the deal closes", "Must simply report it at closing"], "B&P 10176(g).")]},
    ],
    "traps": [
        "California ALLOWS dual agency. Answers that say it is prohibited are describing another state.",
        "Seller's agent: before the listing. Buyer's agent: before the buyer-broker agreement and the offer.",
        "2079.21 protects PRICE confidences, never property condition.",
        "The inspection duty is 1-4 residential units, and the clock is two years.",
        "No definite termination date on an exclusive = discipline.",
    ],
    "vocab": [
        ["Dual agent", "A broker representing both buyer and seller, lawful with consent."],
        ["Agency Disclosure form", "The Civil Code 2079.16 form setting out each agent's duties."],
        ["Agency confirmation", "The written statement of who represents whom, in the contract."],
        ["Confidential information", "Financial position, motivation and bargaining position - price confidences."],
        ["Visual inspection duty", "The 2079 duty owed to a buyer of 1-4 residential units."],
        ["Secret profit", "Undisclosed compensation taken from a principal's transaction."],
    ],
    "examples": [
        {"t": "One broker, both sides",
         "s": "A broker lists a house and then writes the offer for a buyer who walked into the open house.",
         "w": ["The broker now represents both parties, which California permits.",
               "The dual agency must be disclosed and confirmed in the contract.",
               "Price confidences from each side are sealed unless that party permits otherwise."],
         "k": "Lawful dual agency, provided both parties know and consent in the confirmation."},
    ],
}

STUDY["ca/practice"] = {
    "summary": "Trust fund handling is where careers end. Three business days to deposit, $200 of your own money allowed in the account, three years of records - and a broker is answerable for everything a salesperson does.",
    "sections": [
        {"h": "Trust funds: the three-day rule",
         "l": ["Funds accepted on behalf of another must be placed into the OWNER'S HANDS, a NEUTRAL ESCROW DEPOSITORY, or the broker's TRUST ACCOUNT not later than THREE BUSINESS DAYS following receipt by the broker OR by the broker's salesperson (Reg 2832(a)).",
               "A salesperson who receives trust funds must deliver them to the broker; the clock runs from the salesperson's receipt either way.",
               "Withdrawals need the signature of the broker, or of an authorised salesperson, another broker, or an unlicensed employee covered by a fidelity bond at least equal to the funds they can reach (B&P 10145(a)(2))."],
         "check": [("Trust funds must be deposited not later than:", "Three business days after receipt", ["The next business day", "Five calendar days"], "Reg 2832(a)."),
                   ("An unlicensed employee may sign on a trust account only if:", "A fidelity bond covers at least the funds they can access", ["The broker is present", "They have five years' experience"], "B&P 10145(a)(2)(C).")]},
        {"h": "Commingling and uncashed cheques",
         "l": ["COMMINGLING the broker's money with the principal's is grounds for discipline (B&P 10176(e)).",
               "Two things are NOT commingling: up to $200 of the broker's own funds in the trust account to cover bank service charges, and funds belonging partly to the broker when separating them is not reasonably practicable (Reg 2835).",
               "A buyer's cheque may be HELD UNCASHED until the offer is accepted if either the cheque is by its terms not negotiable by the broker or the offeror has given WRITTEN instructions not to deposit it - AND the seller is told it is being held before or at the time the offer is presented (Reg 2832(c))."],
         "check": [("The broker may keep how much personal money in the trust account for bank charges?", "Up to $200", ["Up to $500", "None at all"], "Reg 2835(a)."),
                   ("To hold a buyer's cheque uncashed until acceptance, the broker must:", "Have written instructions or a non-negotiable cheque, and tell the seller", ["Simply decide to hold it", "Get the escrow officer's approval"], "Reg 2832(c).")]},
        {"h": "Records",
         "l": ["A columnar record of all trust funds received, in chronological order, showing date received, from whom, amount, date deposited, cheque number and date of disbursement, and the daily balance (Reg 2831).",
               "A separate record for each beneficiary or transaction (Reg 2831.1).",
               "A monthly RECONCILIATION of the separate beneficiary records against the bank account (Reg 2831.2).",
               "A broker retains copies of all listings, deposit receipts, cancelled cheques, trust records and other transaction documents for THREE YEARS, running from the close of the transaction - or from the LISTING DATE if the deal never closed (B&P 10148)."],
         "check": [("Broker records must be kept for:", "Three years", ["Two years", "Five years"], "B&P 10148(a)."),
                   ("For a listing that never sold, the three years run from:", "The date of the listing", ["The date the listing expired", "The date of the last showing"], "B&P 10148(a).")]},
        {"h": "Advance fees",
         "p": ["An ADVANCE FEE collected before services are rendered is TRUST MONEY, not the broker's, and goes into a trust account. It may be drawn out for the broker only when actually expended for the principal's benefit, or five days after a verified account has been mailed to the principal (B&P 10146). Advance fee agreements and materials must be submitted to the Commissioner in advance (B&P 10085)."],
         "check": [("An advance fee collected by a broker is:", "Trust money belonging to the principal until earned", ["The broker's income immediately", "Exempt from trust rules"], "B&P 10146.")]},
        {"h": "Supervision and unlicensed assistants",
         "l": ["A broker is responsible for supervising the licensed activities of salespersons, with written policies, rules and systems covering transactions, documents, advertising, trust funds, fair housing training and regular reports (Reg 2725).",
               "Unlicensed assistants may do clerical and administrative work. They may not perform acts requiring a licence - soliciting, negotiating, showing property for compensation, or discussing terms.",
               "Advertising must not be false or misleading, and a licensee must disclose that they are a licensee when buying or selling for their own account in a way that could mislead."],
         "check": [("A broker's supervision duty is set out in:", "Commissioner's Regulation 2725", ["Civil Code 2079", "B&P 10474"], "It requires written policies and systems.")]},
    ],
    "traps": [
        "THREE business days, counted from receipt by the broker OR the salesperson.",
        "$200 is the commingling allowance - not $500, not $1,000.",
        "Records run three years from closing, or from the LISTING date if it never closed.",
        "An advance fee is trust money until it is actually earned.",
    ],
    "vocab": [
        ["Trust fund account", "The broker's account holding money belonging to others."],
        ["Neutral escrow depository", "An independent escrow holder; one of the three lawful destinations."],
        ["Commingling", "Mixing the broker's own money with trust funds."],
        ["Conversion", "Using trust funds for the broker's own purposes."],
        ["Advance fee", "A fee collected before services are performed; trust money until earned."],
        ["Reconciliation", "Monthly comparison of beneficiary records against the bank balance."],
    ],
    "examples": [
        {"t": "Counting the three days",
         "s": "A salesperson takes a deposit cheque on Thursday. Saturday and Sunday intervene.",
         "w": ["Business days only: Friday is one, Monday two, Tuesday three.",
               "The clock began on the salesperson's receipt, not the broker's."],
         "k": "Into escrow or the trust account by the end of Tuesday."},
    ],
}

STUDY["ca/licensing"] = {
    "summary": "Three courses before the exam, 150 questions at 70%, four-year licences and 45 hours of continuing education. Then the Commissioner's discipline powers and the Consumer Recovery Account: $50,000 a transaction, $250,000 a licensee.",
    "sections": [
        {"h": "The Department",
         "l": ["The DEPARTMENT OF REAL ESTATE sits in the Business, Consumer Services, and Housing Agency (B&P 10004).",
               "It is headed by the REAL ESTATE COMMISSIONER (B&P 10003), who is appointed by the Governor and enforces the Real Estate Law.",
               "The Commissioner adopts the Regulations of the Real Estate Commissioner, found in title 10 of the California Code of Regulations."],
         "check": [("California's real estate regulator is headed by:", "The Real Estate Commissioner", ["A seven-member commission", "The Attorney General"], "B&P 10003; California has a Commissioner, not a commission board.")]},
        {"h": "Becoming a salesperson",
         "l": ["Be at least 18.",
               "Complete THREE college-level courses before the examination: REAL ESTATE PRINCIPLES, REAL ESTATE PRACTICE, and ONE approved elective other than principles, practice, advanced legal aspects, advanced finance or advanced appraisal (B&P 10151(c)(2)).",
               "Pass the salesperson examination: 150 multiple-choice questions, THREE HOURS, 70% to pass. (The broker examination is 200 questions, four hours, 75%.)",
               "Be honest and truthful; submit fingerprints for a background check.",
               "A salesperson may only act under a broker."],
         "check": [("How many courses must a California salesperson applicant complete before the exam?", "Three", ["One", "Two"], "Principles, Practice, and one elective."),
                   ("The California salesperson exam is:", "150 questions in three hours, 70% to pass", ["100 questions in two hours, 75% to pass", "200 questions in four hours, 75% to pass"], "200/4 hours/75% is the broker exam.")]},
        {"h": "Renewing",
         "l": ["A licence runs FOUR YEARS.",
               "Renewal requires 45 CLOCK HOURS of continuing education in the four years before renewal (B&P 10170.4, 10170.5), including three-hour courses in ETHICS, AGENCY, TRUST FUND handling, FAIR HOUSING (with an interactive roleplay component) and RISK MANAGEMENT, plus a two-hour IMPLICIT BIAS course.",
               "At least 18 of the 45 hours must be consumer-protection courses.",
               "A broker adds a three-hour course in management and supervision."],
         "check": [("A California licence term is:", "Four years", ["Two years", "One year"], "Renewal needs 45 hours of CE."),
                   ("Continuing education for renewal is:", "45 clock hours in the preceding four years", ["14 hours every two years", "30 hours every two years"], "B&P 10170.4(a).")]},
        {"h": "Discipline",
         "l": ["The Commissioner may temporarily suspend or permanently revoke a licence for the conduct listed in B&P 10176 - substantial misrepresentation, false promises, acting for more than one party without consent, commingling, an exclusive without a termination date, secret profit, and the rest.",
               "B&P 10177 adds further grounds, including obtaining a licence by fraud, conviction of a crime substantially related to the licensee's duties, negligence or incompetence, and failure to supervise.",
               "The Commissioner may also issue citations and fines, and may bar a person from the industry."],
         "check": [("Acting for both buyer and seller without the consent of both is:", "Grounds for suspension or revocation", ["Always lawful", "A criminal felony"], "B&P 10176(d).")]},
        {"h": "The Consumer Recovery Account",
         "l": ["It pays an aggrieved person who holds a FINAL JUDGMENT (or a confirmed arbitration award) against a licensee based on FRAUD, MISREPRESENTATION, DECEIT with intent to defraud, or CONVERSION OF TRUST FUNDS, arising from a transaction requiring a licence (B&P 10471).",
               "It pays the ACTUAL AND DIRECT LOSS, up to $50,000 for any ONE TRANSACTION and $250,000 for any ONE LICENSEE, regardless of how many people were wronged or parcels involved (B&P 10474(b)).",
               "On payment the licensee's licence is AUTOMATICALLY SUSPENDED, and is not reinstated until the account is repaid in full with interest (B&P 10475).",
               "A discharge in bankruptcy does not relieve that obligation."],
         "check": [("The Consumer Recovery Account pays at most, per transaction:", "$50,000", ["$20,000", "$250,000"], "$250,000 is the per-licensee cap (B&P 10474(b))."),
                   ("When the account pays, the licensee's licence is:", "Automatically suspended until repaid with interest", ["Revoked permanently", "Unaffected"], "B&P 10475.")]},
    ],
    "traps": [
        "California has a COMMISSIONER, not a commission board. That alone rules out several answers.",
        "Three courses BEFORE the exam, not after.",
        "150 / 3 hours / 70% for salespersons; 200 / 4 hours / 75% for brokers.",
        "Four-year licence, 45 hours of CE - not the two-year cycle most states use.",
        "$50,000 per transaction, $250,000 per licensee.",
    ],
    "vocab": [
        ["DRE", "Department of Real Estate."],
        ["Real Estate Commissioner", "The chief officer enforcing the Real Estate Law."],
        ["Consumer Recovery Account", "The fund paying victims of licensee fraud or conversion."],
        ["Restricted licence", "A conditional licence the Commissioner may issue after discipline."],
        ["Citation", "An order with a fine, short of suspension or revocation."],
    ],
    "examples": [
        {"t": "Two victims, one deal",
         "s": "A buyer and a seller each hold a $40,000 judgment against the same licensee for conversion of trust funds in one transaction.",
         "w": ["The per-transaction cap is $50,000 regardless of the number of claimants.",
               "Their claims total $80,000."],
         "k": "Together they recover no more than $50,000, and the licence is suspended until the account is repaid."},
    ],
}

STUDY["ca/disclosures"] = {
    "summary": "The Transfer Disclosure Statement cannot be waived, and delivering it late hands the buyer a way out: three days if handed over, five if posted. Add the natural hazard disclosure and the rule that some facts need not be told at all.",
    "sections": [
        {"h": "The Transfer Disclosure Statement",
         "l": ["Required on the sale of residential property of ONE TO FOUR dwelling units (Civil Code 1102 et seq.).",
               "Delivered to the buyer AS SOON AS PRACTICABLE BEFORE TRANSFER OF TITLE (Civil Code 1102.3).",
               "If it, or a material amendment to it, is delivered AFTER the buyer's offer has been executed, the buyer may TERMINATE the offer: within THREE DAYS of delivery in person, or FIVE DAYS of delivery by mail or by electronic record.",
               "The termination must be a WRITTEN notice to the seller or the seller's agent.",
               "The TDS may not be waived, and a transfer is not invalidated by a failure to deliver it - but the seller remains liable for the damage caused."],
         "check": [("The TDS is required for:", "Residential property of one to four dwelling units", ["Any property including vacant land", "Commercial buildings only"], "Civil Code 1102."),
                   ("A TDS delivered by mail after the offer was signed gives the buyer:", "Five days to terminate", ["Three days", "Ten days"], "Three days if delivered in person (Civil Code 1102.3)."),
                   ("The buyer's termination must be:", "A written notice to the seller or the seller's agent", ["A phone call", "Noted at closing"], "Civil Code 1102.3.")]},
        {"h": "Natural hazards and other reports",
         "l": ["The NATURAL HAZARD DISCLOSURE STATEMENT (Civil Code 1103) tells the buyer whether the property sits in a special flood hazard area, an area of potential flooding, a very high fire hazard severity zone, a wildland fire area, an earthquake fault zone or a seismic hazard zone.",
               "A MEGAN'S LAW notice about the sex offender database appears in the contract; the agent is not required to search it for the buyer.",
               "A structural pest control report, where one is obtained, must be given to the buyer.",
               "Smoke alarm and water heater bracing compliance are the seller's to certify."],
         "check": [("The Natural Hazard Disclosure Statement covers:", "Flood, fire, earthquake fault and seismic hazard zones", ["Crime statistics", "School rankings"], "Civil Code 1103.")]},
        {"h": "What need not be disclosed (Civil Code 1710.2)",
         "l": ["The death of an occupant on the property, or its manner, where the death occurred MORE THAN THREE YEARS before the buyer's offer.",
               "That an occupant had HIV or died of AIDS-related complications - at any time.",
               "No cause of action arises for withholding those facts.",
               "But a licensee may NOT lie. Answering a direct question falsely is misrepresentation, and a death within three years is not covered by the exemption."],
         "check": [("A death on the property four years ago:", "Need not be disclosed", ["Must always be disclosed", "Must be disclosed only to the agent"], "Civil Code 1710.2(a)(1)(A)."),
                   ("That a former occupant died of AIDS-related complications:", "Need not be disclosed at any time", ["Must be disclosed within three years", "Must always be disclosed"], "Civil Code 1710.2(a)(1)(B).")]},
        {"h": "The agent's own duty",
         "p": ["Separately from the seller's TDS, the agent owes the buyer of one to four residential units a REASONABLY COMPETENT AND DILIGENT VISUAL INSPECTION and must disclose everything materially affecting the VALUE OR DESIRABILITY that an investigation would reveal (Civil Code 2079). The agent's duty is not discharged by handing over the seller's form."],
         "check": [("Delivering the seller's TDS:", "Does not discharge the agent's own inspection duty", ["Ends the agent's obligations", "Transfers liability to the seller"], "Civil Code 2079 stands on its own.")]},
    ],
    "traps": [
        "3 days in person, 5 days by mail or electronically. The pair is the question.",
        "The TDS cannot be waived - 'the buyer agreed to waive it' is always wrong.",
        "Three years for a death; HIV/AIDS is never required.",
        "The agent's visual inspection duty is separate from the seller's TDS.",
    ],
    "vocab": [
        ["TDS", "Transfer Disclosure Statement, required for 1-4 residential units."],
        ["NHD", "Natural Hazard Disclosure Statement."],
        ["Material fact", "A fact affecting the value or desirability of the property."],
        ["Stigmatized property", "One affected by events such as a death; disclosure limited by 1710.2."],
        ["Red flag", "A visible sign that should prompt further investigation."],
    ],
    "examples": [
        {"t": "A late disclosure",
         "s": "The offer is signed on 4 March. The TDS is posted to the buyer and arrives on 9 March.",
         "w": ["Delivery after execution starts the clock.",
               "Delivery by mail gives five days, not three."],
         "k": "The buyer may terminate by written notice within five days of delivery."},
    ],
}


# ------------------------------------------------------------- questions
# (topic, subtopic, difficulty, question, right, [wrong x3], explanation)

Q = [
 # agency
 ("ca/agency", "Dual agency", 1, "Dual agency in California is:",
  "Lawful if all parties know and consent", ["Prohibited in all transactions", "Lawful only in commercial transactions", "Lawful only with the Commissioner's approval"],
  "B&P 10176(d) punishes acting for more than one party WITHOUT the knowledge or consent of all."),
 ("ca/agency", "Dual agency", 2, "Without express permission, a dual agent may NOT disclose:",
  "That the seller will accept less than the listing price", ["A known defect in the foundation", "The listed price", "The property's square footage"],
  "Civil Code 2079.21(c) protects price confidences, never condition."),
 ("ca/agency", "Dual agency", 2, "Under Civil Code 2079.21, confidential information includes:",
  "The client's motivation and bargaining position", ["The property's age", "The neighbourhood's schools", "The listing broker's commission"],
  "Facts that may affect price."),
 ("ca/agency", "Dual agency", 3, "A dual agent learns from the buyer that they would pay $20,000 more. The agent:",
  "May not tell the seller without the buyer's express permission", ["Must tell the seller", "May tell the seller after the offer is accepted", "Must report it to the DRE"],
  "Civil Code 2079.21(b)."),
 ("ca/agency", "Disclosure form", 1, "The seller's agent must deliver the agency disclosure form to the seller:",
  "Before entering into the listing agreement", ["When the first offer arrives", "At close of escrow", "Within five days of the listing"],
  "Civil Code 2079.14(a)(1)."),
 ("ca/agency", "Disclosure form", 2, "The buyer's agent must deliver the agency disclosure form:",
  "As soon as practicable before the buyer-broker agreement and the offer", ["At close of escrow", "Only if the buyer asks", "Within 10 days of showing property"],
  "Civil Code 2079.14(a)(2)."),
 ("ca/agency", "Disclosure form", 3, "A buyer prepares their own offer and hands it to their agent. The agent must present the disclosure form:",
  "Not later than the next business day after receiving the offer", ["Within three business days", "At the time of acceptance", "Before the offer is written"],
  "Civil Code 2079.14(a)(2)."),
 ("ca/agency", "Disclosure form", 2, "After delivering the agency disclosure form the agent must obtain:",
  "A signed acknowledgement of receipt", ["A notarised statement", "The other agent's initials", "Nothing further"],
  "Civil Code 2079.14(b)."),
 ("ca/agency", "Confirmation", 2, "The agency relationship must be confirmed:",
  "In the purchase contract or a separate writing, at or before its execution", ["Only in the listing agreement", "After close of escrow", "Orally at the first meeting"],
  "Civil Code 2079.17(a)-(b)."),
 ("ca/agency", "Confirmation", 3, "The statutory agency confirmation identifies the agent by:",
  "Brokerage firm name and licence number", ["Home address", "Years of experience", "Board membership"],
  "Civil Code 2079.17(c)."),
 ("ca/agency", "Duty to buyer", 1, "A listing agent owes a prospective buyer of a three-unit residential building:",
  "A reasonably competent and diligent visual inspection", ["No duty at all", "A full structural engineering report", "A duty only if the buyer is unrepresented"],
  "Civil Code 2079 covers one to four dwelling units."),
 ("ca/agency", "Duty to buyer", 2, "The agent's inspection duty requires disclosure of facts materially affecting:",
  "The value or desirability of the property", ["Only structural safety", "Only matters the seller mentions", "Only recorded documents"],
  "Civil Code 2079(a)."),
 ("ca/agency", "Duty to buyer", 2, "An action for breach of the agent's inspection duty must be brought within:",
  "Two years of the date of possession", ["One year", "Four years", "Three years"],
  "Recordation, close of escrow or occupancy, whichever is first (Civil Code 2079.4)."),
 ("ca/agency", "Duty to buyer", 3, "Civil Code 2079's inspection duty does NOT extend to:",
  "A 20-unit apartment building", ["A single-family home", "A duplex", "A fourplex"],
  "One to four dwelling units only."),
 ("ca/agency", "Listings", 1, "An exclusive listing in California must contain:",
  "A definite, specified date of final and complete termination", ["An automatic renewal clause", "A minimum price", "A 90-day minimum term"],
  "B&P 10176(f)."),
 ("ca/agency", "Listings", 2, "A broker claims a commission under an exclusive listing with no termination date. This is:",
  "Grounds for suspension or revocation", ["Permitted if the seller agreed", "Permitted for commercial property", "A criminal offence"],
  "B&P 10176(f)."),
 ("ca/agency", "Compensation", 2, "A licensee who takes an undisclosed profit on a principal's transaction:",
  "May have the licence suspended or revoked", ["May keep it once escrow closes", "Must simply disclose it at closing", "Is fined $200"],
  "B&P 10176(g)."),
 ("ca/agency", "Compensation", 3, "A licensee who holds an option to purchase under a listing must:",
  "Disclose the full profit in writing and get the principal's written consent", ["Say nothing until exercising it", "Report it to the DRE only", "Split the profit with the principal"],
  "B&P 10176(h)."),
 ("ca/agency", "Compensation", 2, "Commission rates in California are:",
  "Negotiable between the parties", ["Set by the DRE", "Set by the local association", "Fixed at 6%"],
  "Setting rates among competitors is an antitrust violation."),
 ("ca/agency", "Agency basics", 1, "A salesperson's fiduciary duties run to:",
  "The broker's principal", ["Whoever pays the commission", "Both parties equally", "The escrow holder"],
  "The salesperson acts for the broker, who is the principal's agent."),
 ("ca/agency", "Agency basics", 2, "A seller's agent owes the buyer, at minimum:",
  "Honesty, fair dealing and disclosure of material facts", ["Full fiduciary duties", "No duty whatsoever", "Loyalty and obedience"],
  "Fiduciary duties belong to the principal; the other side still gets honesty and disclosure."),
 ("ca/agency", "Agency basics", 3, "An agency in California may be created by:",
  "Express agreement, ratification, or estoppel", ["Only a written listing agreement", "Only an oral agreement", "Only by court order"],
  "Conduct can create agency even without a signed contract."),

 # practice
 ("ca/practice", "Trust funds", 1, "Trust funds must be deposited not later than:",
  "Three business days following receipt", ["The next business day", "Five calendar days", "Immediately on the same day"],
  "Reg 2832(a)."),
 ("ca/practice", "Trust funds", 2, "The three-business-day clock for trust funds starts on receipt by:",
  "The broker or the broker's salesperson", ["The broker only", "The escrow holder", "The title company"],
  "Reg 2832(a)."),
 ("ca/practice", "Trust funds", 1, "Which is NOT a lawful destination for trust funds?",
  "The broker's general business account", ["The hands of the owner of the funds", "A neutral escrow depository", "The broker's trust fund account"],
  "Reg 2832(a) lists the three lawful destinations."),
 ("ca/practice", "Commingling", 1, "The most of a broker's own money that may sit in the trust account for bank charges is:",
  "$200", ["$100", "$500", "$1,000"],
  "Reg 2835(a)."),
 ("ca/practice", "Commingling", 2, "Mixing a principal's funds with the broker's own money is:",
  "Commingling, and grounds for discipline", ["Permitted if recorded", "Required for reconciliation", "Permitted up to $5,000"],
  "B&P 10176(e)."),
 ("ca/practice", "Trust funds", 2, "A buyer's cheque may be held uncashed until acceptance if:",
  "The offeror gave written instructions and the seller is told before the offer is presented", ["The broker simply decides to hold it", "The cheque is over $10,000", "Escrow has not opened"],
  "Reg 2832(c)."),
 ("ca/practice", "Trust funds", 3, "An unlicensed employee may be a signatory on the trust account only if:",
  "A fidelity bond covers at least the funds they can access", ["They have worked there five years", "The broker co-signs each cheque", "The DRE approves in writing"],
  "B&P 10145(a)(2)(C)."),
 ("ca/practice", "Records", 1, "A California broker must retain transaction records for:",
  "Three years", ["Two years", "Four years", "Seven years"],
  "B&P 10148(a)."),
 ("ca/practice", "Records", 2, "For a listing that never sold, the retention period runs from:",
  "The date of the listing", ["The date the listing expired", "The date of the last offer", "The date the file was closed"],
  "B&P 10148(a)."),
 ("ca/practice", "Records", 2, "How often must a broker reconcile the separate beneficiary records with the bank account?",
  "Monthly", ["Weekly", "Quarterly", "Annually"],
  "Reg 2831.2."),
 ("ca/practice", "Records", 3, "The columnar trust fund record must show, among other things:",
  "The daily balance of the account", ["The broker's net profit", "Each client's credit score", "The listing price"],
  "Reg 2831(a)(7)."),
 ("ca/practice", "Advance fees", 2, "An advance fee collected by a broker is:",
  "Trust money until actually earned", ["The broker's income on receipt", "Exempt from trust fund rules", "Payable to the salesperson"],
  "B&P 10146."),
 ("ca/practice", "Advance fees", 3, "A broker may withdraw an advance fee for their own benefit:",
  "When actually expended for the principal, or five days after a verified account is mailed", ["At any time", "Only at close of escrow", "Only with DRE consent"],
  "B&P 10146."),
 ("ca/practice", "Supervision", 2, "A broker's duty to supervise licensed activity is set out in:",
  "Commissioner's Regulation 2725", ["Civil Code 2079", "B&P 10474", "Civil Code 1102"],
  "It requires written policies, rules, procedures and systems."),
 ("ca/practice", "Unlicensed assistants", 1, "An unlicensed assistant may:",
  "Perform clerical and administrative work", ["Negotiate terms with a buyer", "Show a listing for compensation", "Discuss price with a prospect"],
  "Acts requiring a licence may not be delegated to an unlicensed person."),
 ("ca/practice", "Advertising", 2, "A licensee buying property for their own account must:",
  "Disclose that they are a licensee", ["Say nothing", "Use a different broker", "Obtain DRE approval"],
  "Concealing licensee status in a way that misleads is grounds for discipline."),

 # licensing
 ("ca/licensing", "The Department", 1, "California's real estate regulator is headed by:",
  "The Real Estate Commissioner", ["A seven-member commission", "The Attorney General", "A nine-member board"],
  "B&P 10003. Unlike Florida and Texas, California has a Commissioner, not a commission board."),
 ("ca/licensing", "The Department", 2, "The Department of Real Estate sits within:",
  "The Business, Consumer Services, and Housing Agency", ["The Department of Justice", "The Franchise Tax Board", "The Department of Consumer Affairs"],
  "B&P 10004(a)."),
 ("ca/licensing", "Education", 1, "A California salesperson applicant must complete, before the examination:",
  "Three college-level courses", ["One course", "Two courses", "Five courses"],
  "Real Estate Principles, Real Estate Practice, and one elective (B&P 10151(c)(2))."),
 ("ca/licensing", "Education", 2, "Which course is required of every salesperson applicant?",
  "Real Estate Principles", ["Advanced Real Estate Finance", "Advanced Legal Aspects of Real Estate", "Property Management"],
  "Principles and Practice are both required; the third is an elective."),
 ("ca/licensing", "Examination", 1, "The California salesperson examination is:",
  "150 questions in three hours", ["100 questions in two hours", "200 questions in four hours", "120 questions in three hours"],
  "200 questions in four hours is the broker exam (DRE)."),
 ("ca/licensing", "Examination", 1, "To pass the California salesperson examination you must score at least:",
  "70%", ["60%", "75%", "80%"],
  "Brokers need 75% (DRE)."),
 ("ca/licensing", "Renewal", 1, "A California real estate licence runs for:",
  "Four years", ["One year", "Two years", "Three years"],
  "B&P 10170.4(a)."),
 ("ca/licensing", "Renewal", 1, "Continuing education for renewal is:",
  "45 clock hours in the preceding four years", ["14 hours every two years", "30 hours every two years", "45 hours every two years"],
  "B&P 10170.4(a)."),
 ("ca/licensing", "Renewal", 2, "Which is a required continuing education course?",
  "A three-hour course in trust fund accounting and handling", ["A three-hour course in appraisal", "A six-hour course in property management", "A three-hour course in tax law"],
  "Ethics, agency, trust funds, fair housing and risk management are required (B&P 10170.5(a))."),
 ("ca/licensing", "Renewal", 3, "The implicit bias course required for renewal is:",
  "Two hours", ["Three hours", "One hour", "Six hours"],
  "B&P 10170.5(a)(6)."),
 ("ca/licensing", "Discipline", 2, "Acting for both buyer and seller without the consent of both is:",
  "Grounds for suspension or revocation", ["Always permitted", "A felony", "Permitted if disclosed afterwards"],
  "B&P 10176(d)."),
 ("ca/licensing", "Discipline", 2, "Which is grounds for discipline under B&P 10176?",
  "Making a substantial misrepresentation", ["Charging a negotiated commission", "Advertising on the internet", "Holding an open house"],
  "10176(a)."),
 ("ca/licensing", "Recovery Account", 1, "The Consumer Recovery Account pays at most, per transaction:",
  "$50,000", ["$20,000", "$100,000", "$250,000"],
  "B&P 10474(b); $250,000 is the per-licensee cap."),
 ("ca/licensing", "Recovery Account", 2, "The Consumer Recovery Account pays at most, against any one licensee:",
  "$250,000", ["$50,000", "$100,000", "$500,000"],
  "B&P 10474(b)."),
 ("ca/licensing", "Recovery Account", 2, "A claim on the Consumer Recovery Account must be based on a judgment for:",
  "Fraud, misrepresentation, deceit, or conversion of trust funds", ["Any breach of contract", "Negligence of any kind", "A disputed commission"],
  "B&P 10471(a)."),
 ("ca/licensing", "Recovery Account", 2, "When the Consumer Recovery Account pays, the licensee's licence is:",
  "Automatically suspended until the account is repaid with interest", ["Revoked permanently", "Unaffected", "Placed on probation for a year"],
  "B&P 10475."),
 ("ca/licensing", "Recovery Account", 3, "A licensee discharged in bankruptcy after the account paid a claim:",
  "Still may not be reinstated until the account is repaid", ["Is released from the obligation", "May reapply immediately", "Owes only the principal, not interest"],
  "B&P 10475."),

 # disclosures
 ("ca/disclosures", "TDS", 1, "The Transfer Disclosure Statement is required on the sale of:",
  "Residential property of one to four dwelling units", ["Any real property", "Commercial property only", "Vacant land"],
  "Civil Code 1102."),
 ("ca/disclosures", "TDS", 1, "The TDS must be delivered:",
  "As soon as practicable before transfer of title", ["At close of escrow", "Within 30 days after the contract", "Only on request"],
  "Civil Code 1102.3."),
 ("ca/disclosures", "TDS", 1, "A TDS handed to the buyer in person after the offer was signed gives the buyer:",
  "Three days to terminate", ["Five days", "Seven days", "No right to terminate"],
  "Five days applies to delivery by mail (Civil Code 1102.3)."),
 ("ca/disclosures", "TDS", 2, "A TDS delivered by mail after the offer was signed gives the buyer:",
  "Five days to terminate", ["Three days", "Ten days", "No right to terminate"],
  "Civil Code 1102.3."),
 ("ca/disclosures", "TDS", 2, "The buyer's termination after a late TDS must be:",
  "A written notice to the seller or the seller's agent", ["A phone call to the agent", "Noted in escrow instructions", "Announced at closing"],
  "Civil Code 1102.3."),
 ("ca/disclosures", "TDS", 2, "A buyer's waiver of the TDS is:",
  "Ineffective; the statement cannot be waived", ["Valid if in writing", "Valid if the buyer is an investor", "Valid if the property is sold as-is"],
  "Civil Code 1102.1."),
 ("ca/disclosures", "NHD", 1, "The Natural Hazard Disclosure Statement covers:",
  "Flood, fire, earthquake fault and seismic hazard zones", ["Crime rates", "School performance", "Property tax history"],
  "Civil Code 1103."),
 ("ca/disclosures", "Stigmatized property", 1, "A death on the property five years ago:",
  "Need not be disclosed", ["Must always be disclosed", "Must be disclosed if the buyer asks nothing", "Must be disclosed only in writing"],
  "Civil Code 1710.2(a)(1)(A) sets the line at three years."),
 ("ca/disclosures", "Stigmatized property", 2, "A death on the property two years ago:",
  "Falls outside the three-year exemption", ["Need not be disclosed", "Is never material", "Is disclosed only to the agent"],
  "The exemption covers deaths more than three years before the offer."),
 ("ca/disclosures", "Stigmatized property", 2, "That a former occupant died of AIDS-related complications:",
  "Need not be disclosed at any time", ["Must be disclosed within three years", "Must always be disclosed", "Must be disclosed if asked"],
  "Civil Code 1710.2(a)(1)(B)."),
 ("ca/disclosures", "Agent's duty", 2, "Handing the buyer the seller's TDS:",
  "Does not discharge the agent's own inspection duty", ["Ends all of the agent's obligations", "Shifts liability to the seller", "Satisfies Civil Code 2079"],
  "Civil Code 2079 stands separately."),
 ("ca/disclosures", "Megan's Law", 2, "On the sex offender database, a California agent:",
  "Provides the statutory notice but need not search the database", ["Must search it for every buyer", "Must disclose any offender nearby", "May not mention it"],
  "The notice appears in the contract."),
 ("ca/disclosures", "Material facts", 3, "A visible crack in the foundation that the seller did not mention:",
  "Must be disclosed, because a visual inspection would reveal it", ["Need not be disclosed if the seller is silent", "Is the buyer's inspector's problem alone", "Need not be disclosed in an as-is sale"],
  "Civil Code 2079 requires disclosure of what an investigation would reveal."),

 # --- agency, further
 ("ca/agency", "Disclosure form", 2, "The agency disclosure form set out in Civil Code 2079.16 describes the duties of:",
  "A seller's agent, a buyer's agent, and an agent representing both", ["Only the listing agent", "Only the buyer's agent", "The escrow holder"],
  "The form sets out all three relationships."),
 ("ca/agency", "Dual agency", 3, "Civil Code 2079.21's limit on a dual agent:",
  "Restricts price confidences without altering the agent's other duties", ["Ends all duties to both parties", "Applies only to the seller", "Allows any disclosure once an offer is made"],
  "2079.21(d)."),
 ("ca/agency", "Agency basics", 2, "An agency relationship created by the principal's later approval of an unauthorised act is created by:",
  "Ratification", ["Estoppel", "Express agreement", "Operation of law"],
  "Ratification is after-the-fact approval."),
 ("ca/agency", "Agency basics", 3, "A principal who allows a third party to reasonably believe someone is their agent may be bound by:",
  "Estoppel", ["Ratification", "Novation", "Subrogation"],
  "The principal is stopped from denying the agency."),
 ("ca/agency", "Agency basics", 2, "An agency terminates by all of the following EXCEPT:",
  "The property being placed on the market", ["Expiration of its term", "Mutual agreement", "Destruction of the property"],
  "Listing the property is the performance of the agency, not its end."),
 ("ca/agency", "Duty to buyer", 2, "The Civil Code 2079 inspection duty is owed by:",
  "The listing broker and a cooperating broker", ["The seller alone", "The escrow holder", "The appraiser"],
  "Civil Code 2079(a)."),
 ("ca/agency", "Duty to buyer", 3, "Under Civil Code 2079.4, the two-year period runs from the date of possession, meaning:",
  "Recordation, close of escrow, or occupancy, whichever is first", ["The date the contract was signed", "The date the TDS was delivered", "The date the defect was found"],
  "Civil Code 2079.4."),
 ("ca/agency", "Compensation", 3, "A licensee buying a listed property for themselves must:",
  "Disclose their licensee status and their interest to the principal", ["Use a different brokerage", "Pay full list price", "Obtain DRE approval"],
  "Undisclosed principal dealing is grounds for discipline."),

 # --- practice, further
 ("ca/practice", "Trust funds", 2, "A trust account may not be:",
  "An account requiring prior written notice before withdrawal", ["A non-interest-bearing account", "An account at a California bank", "An account in the broker's name as trustee"],
  "Reg 2832(b)."),
 ("ca/practice", "Trust funds", 3, "A cheque lawfully held uncashed until acceptance must then be placed in escrow or the trust account:",
  "Not later than three business days after acceptance", ["The same day as acceptance", "Within five calendar days", "At close of escrow"],
  "Reg 2832(d)."),
 ("ca/practice", "Trust funds", 2, "Funds in the trust account are held until:",
  "Disbursed in accordance with instructions from the person entitled to them", ["The broker decides to release them", "Escrow closes, whatever the instructions", "The salesperson requests them"],
  "B&P 10145(a)(1)."),
 ("ca/practice", "Trust funds", 3, "A broker receives a deposit and immediately hands it to the escrow holder. The broker:",
  "Has complied, because a neutral escrow depository is a lawful destination", ["Has violated the trust fund rules", "Must still open a trust account", "Must first deposit it for three days"],
  "Reg 2832(a)."),
 ("ca/practice", "Records", 2, "A separate record must be kept for:",
  "Each beneficiary or transaction", ["Each calendar year only", "Each salesperson", "Each bank branch"],
  "Reg 2831.1."),
 ("ca/practice", "Records", 3, "Which need NOT appear in the columnar trust fund record?",
  "The client's credit score", ["The date funds were received", "From whom funds were received", "The daily balance"],
  "Reg 2831(a)."),
 ("ca/practice", "Supervision", 2, "A broker's written supervision policies must cover:",
  "Transactions, documents, advertising, trust funds and reports", ["Only trust funds", "Only advertising", "Only office hours"],
  "Reg 2725."),
 ("ca/practice", "Supervision", 3, "A broker who fails to supervise licensed activity:",
  "May be disciplined even without personally committing the act", ["Is liable only if present", "Is liable only for trust fund errors", "Bears no responsibility"],
  "B&P 10177 and Reg 2725."),
 ("ca/practice", "Advertising", 2, "A real estate advertisement in California must not:",
  "Be false or misleading", ["Mention the sale price", "Include a photograph", "Name the salesperson"],
  "Misleading advertising is grounds for discipline."),

 # --- licensing, further
 ("ca/licensing", "Eligibility", 1, "The minimum age for a California real estate licence is:",
  "18", ["17", "19", "21"],
  "Applicants must also be honest and truthful and submit fingerprints."),
 ("ca/licensing", "Eligibility", 2, "A California salesperson may act:",
  "Only under a licensed broker", ["Independently once licensed", "Under any licensee", "Under a licensed escrow officer"],
  "The salesperson's authority flows from the employing broker."),
 ("ca/licensing", "Examination", 2, "The California broker examination is:",
  "200 questions in four hours, 75% to pass", ["150 questions in three hours, 70% to pass", "150 questions in four hours, 75% to pass", "100 questions in three hours, 70% to pass"],
  "The salesperson exam is 150/3 hours/70% (DRE)."),
 ("ca/licensing", "Examination", 3, "Examinees who pass the California exam are:",
  "Not told their final score", ["Given a percentage score", "Ranked against other candidates", "Sent a certificate with their score"],
  "The exam is qualifying in nature; only those who fail receive the score (DRE)."),
 ("ca/licensing", "Renewal", 2, "Of the 45 continuing education hours, how many must be consumer-protection courses?",
  "At least 18", ["At least 8", "At least 30", "None are specified"],
  "B&P 10170.5(a)(8)."),
 ("ca/licensing", "Renewal", 3, "Which continuing education course is required of brokers but not salespersons?",
  "A three-hour course in management and supervision", ["A three-hour ethics course", "A three-hour agency course", "A two-hour implicit bias course"],
  "B&P 10170.5(a)(7)."),
 ("ca/licensing", "Renewal", 2, "The required fair housing continuing education course must include:",
  "An interactive participatory roleplay component", ["A written examination", "A site visit", "A four-hour minimum"],
  "B&P 10170.5(a)(4)."),
 ("ca/licensing", "Discipline", 2, "Commingling a principal's money with the broker's own is:",
  "Grounds for suspension or revocation", ["Permitted up to $5,000", "Required for reconciliation", "A criminal felony"],
  "B&P 10176(e)."),
 ("ca/licensing", "Discipline", 3, "A continued and flagrant course of misrepresentation through licensees is:",
  "Grounds for suspension or revocation", ["Permitted if unintentional", "Only a civil matter", "Grounds for a fine only"],
  "B&P 10176(c)."),
 ("ca/licensing", "Recovery Account", 3, "A claim on the Consumer Recovery Account may rest on:",
  "A final judgment or a confirmed arbitration award", ["An unpaid invoice", "A complaint filed with the DRE", "An escrow dispute"],
  "B&P 10471(a)."),
 ("ca/licensing", "Recovery Account", 2, "The Consumer Recovery Account pays:",
  "The actual and direct loss in the transaction", ["Punitive damages", "Attorney's fees in all cases", "Lost profits"],
  "B&P 10471(a)."),

 # --- disclosures, further
 ("ca/disclosures", "TDS", 2, "Who completes the Transfer Disclosure Statement?",
  "The seller, with the agents completing their own portions", ["The buyer's agent alone", "The escrow holder", "The appraiser"],
  "The agents add their visual inspection sections."),
 ("ca/disclosures", "TDS", 3, "A material amendment to a delivered TDS:",
  "Restarts the buyer's right to terminate", ["Has no effect once the TDS was delivered", "Must be approved by escrow", "Requires a new contract"],
  "Civil Code 1102.3 covers any material amendment."),
 ("ca/disclosures", "TDS", 3, "Failure to deliver the TDS:",
  "Does not invalidate the transfer, but the seller remains liable for the damage", ["Voids the sale automatically", "Transfers title to the buyer free of liens", "Has no consequence"],
  "Civil Code 1102.13 and the damages provisions."),
 ("ca/disclosures", "Stigmatized property", 3, "A buyer asks directly whether anyone died in the house two years ago. The agent:",
  "Must answer truthfully", ["May decline to answer", "Must say no", "May refer the buyer to the seller only"],
  "The three-year exemption does not cover it, and a false answer is misrepresentation."),
 ("ca/disclosures", "Stigmatized property", 3, "Civil Code 1710.2 provides that for the protected facts:",
  "No cause of action arises against the owner or agent for not disclosing", ["Disclosure is required on request", "The agent must disclose but the seller need not", "The buyer may rescind within three days"],
  "Civil Code 1710.2(a)(3)."),
 ("ca/disclosures", "Reports", 2, "A structural pest control report obtained in the transaction:",
  "Must be given to the buyer", ["May be withheld by the seller", "Goes only to the lender", "Is optional to share"],
  "Delivery to the buyer is required where a report is obtained."),
 ("ca/disclosures", "Material facts", 2, "A material fact in California is one affecting:",
  "The value or desirability of the property", ["Only the structural safety", "Only the recorded title", "Only the price"],
  "Civil Code 2079(a)."),
 ("ca/disclosures", "Material facts", 3, "An agent notices water staining on a ceiling during a showing. The agent should:",
  "Treat it as a red flag and disclose it, investigating further", ["Ignore it unless the seller mentions it", "Tell only the buyer's lender", "Wait for the buyer's inspector to find it"],
  "A visible sign triggers the 2079 duty."),
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
            "id": "ca-" + hashlib.sha1(q.encode()).hexdigest()[:8],
            "portion": "georgia", "topic": topic, "subtopic": sub,
            "sub": topic + "|" + sub, "concept": "California " + sub.lower(),
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
        "code": "CA", "name": "California", "abbr": "CA",
        "regulator": "DRE",
        "pass": EXAM["pass"],
        "single": True,
        "portions": {
            "national": {"name": "General practice",
                         "scored": EXAM["national_scored"],
                         "minutes": EXAM["national_minutes"],
                         "blurb": "Ownership, valuation, financing, transfer and contracts, as California tests them."},
            "georgia": {"name": "California law", "scored": EXAM["state_scored"],
                        "minutes": EXAM["state_minutes"],
                        "blurb": "Agency, trust funds, licensing and the disclosures the Civil Code requires."},
        },
        "topics": topics, "bank": bank, "study": study,
        "sources": SOURCES, "diffs": DIFFS,
    }


# Where California departs from the general rule, shown on the general
# lessons in place of the Georgia notes.
DIFFS = {
    "national/agency": [
        "California PERMITS dual agency. What B&P 10176(d) punishes is acting for more than one party without the knowledge and consent of all of them.",
        "A dual agent may not reveal price confidences - that the seller will take less, or the buyer will pay more - without that party's express permission (Civil Code 2079.21).",
    ],
    "national/ownership": [
        "California is a COMMUNITY PROPERTY state: property acquired during marriage is generally community property, and spouses may also hold as community property with right of survivorship.",
        "Ownership questions lean on vesting: joint tenancy, tenancy in common, community property, and partnership interests.",
    ],
    "national/financing": [
        "California lenders normally use a DEED OF TRUST with a trustee and a power of sale, foreclosed non-judicially, rather than a mortgage foreclosed in court.",
        "An exclusive authorisation to negotiate a loan secured by real property is limited by statute in its term - check the current limit before relying on a number.",
    ],
    "national/transfer": [
        "Title normally passes through ESCROW, with an independent escrow holder acting for both parties as a neutral agent.",
        "A documentary transfer tax is charged by the county on recording; rates are set locally, so confirm the rate for the county in question.",
    ],
    "national/disclosures": [
        "The Transfer Disclosure Statement is required for 1-4 residential units and CANNOT be waived; a late one gives the buyer 3 days (in person) or 5 days (by mail) to terminate (Civil Code 1102.3).",
        "A death on the property more than three years before the offer, and any occupant's HIV or AIDS status, need not be disclosed (Civil Code 1710.2).",
        "The agent separately owes a buyer of 1-4 residential units a reasonably competent and diligent visual inspection (Civil Code 2079).",
    ],
    "national/practice": [
        "Trust funds go to the owner, a neutral escrow depository, or the broker's trust account within THREE BUSINESS DAYS of receipt by the broker or the salesperson (Reg 2832).",
        "Up to $200 of the broker's own money may sit in the trust account for bank charges; records are kept three years (Reg 2835; B&P 10148).",
    ],
    "national/contracts": [
        "An exclusive listing must state a definite, specified termination date, or the broker may not claim the fee (B&P 10176(f)).",
    ],
}


if __name__ == "__main__":
    import io, json, os
    here = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    out = os.path.join(here, "greprep", "packs", "CA.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    pack = build()
    with io.open(out, "w", encoding="utf-8") as f:
        json.dump(pack, f, ensure_ascii=False, indent=1, sort_keys=True)
    print("wrote", out, len(pack["bank"]), "questions,", len(pack["study"]), "lessons")
