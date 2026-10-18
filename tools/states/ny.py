"""New York state content: lessons and practice questions.

New York is the awkward one. The Department of State sets its own single
examination, but publishes NEITHER the number of questions NOR a numerical
pass mark: "Exam results are reported as either passed or failed; you will
not receive a numerical score." So this pack sets `pass_published: false`,
and the app presents the figure as a study target rather than the state's
requirement. Do not replace it with a number from a prep school: the DOS
does not publish one.

What the state DOES publish is the 77-hour salesperson syllabus, subject by
subject with its hours. That is the blueprint used here, one practice
question per syllabus hour, so the weighting is the state's own.

Every rule below was read from the official text on 2026-10-18:
  - Real Estate License Law (March 2026), the Department of State's own
    guide, carrying Real Property Law article 12-A, Property Condition
    Disclosure (article 14), Executive Law article 15, and the rules at
    19 NYCRR parts 175-179.
  - The Real Estate Salesperson Syllabus (2022), for the 77 hours.
  - dos.ny.gov for the licensing requirements, the two-year term, and the
    pass/fail score reporting.
The section a fact comes from is cited next to it. Do not add a fact here
without reading its source first.

A warning for anyone extending this: the $500 credit that commercial guides
still teach for the Property Condition Disclosure Act is GONE from the
current statute. Section 465 now speaks only of liability for a willful
failure. Check the live text before writing a number.
"""

EXAM = {
    # The DOS publishes no question count and no pass mark. The practice
    # paper is one question per syllabus hour, split by subject.
    "state_scored": 30,
    "state_minutes": 36,
    "national_scored": 47,
    "national_minutes": 56,
    "pass": 0.75,          # a study target, NOT the state's requirement
}

PASS_NOTE = ("New York reports its examination only as passed or failed and "
             "publishes no numerical pass mark and no question count. The 75% "
             "here is this app's study target, and the blueprint below is the "
             "Department of State's own 77-hour syllabus, one question per hour.")

# key, label, questions (= syllabus hours), blurb
TOPICS = [
    ("ny/agency", "Law of agency", 11,
     "The disclosure form, and the six relationships New York recognises."),
    ("ny/fair-housing", "Human rights & fair housing", 6,
     "New York's protected classes, which go well beyond the federal list."),
    ("ny/practice", "Brokerage practice & escrow", 5,
     "Commingling, exclusive listings, advertising and business signs."),
    ("ny/license-law", "Licence law & regulations", 4,
     "Licensing, education, renewal, discipline, and licensee safety."),
    ("ny/disclosures", "Property condition disclosure", 4,
     "Article 14, its exemptions, and what the 2024 amendment removed."),
]

SOURCES = [
    {"by": "New York Department of State",
     "name": "Real Estate License Law (March 2026)",
     "note": "The Division of Licensing Services' own guide: Real Property Law article 12-A, the Property Condition Disclosure Act, the Human Rights Law, and 19 NYCRR parts 175-179.",
     "url": "https://dos.ny.gov/real-estate-license-law"},
    {"by": "New York Department of State",
     "name": "Real Estate Salesperson Syllabus (2022)",
     "note": "The 77-hour qualifying curriculum, subject by subject with its hours. The weighting in this app comes from it.",
     "url": "https://dos.ny.gov/real-estate-salesperson-77-hour-curriculum-eff-12212022"},
    {"by": "New York Department of State",
     "name": "Become a Real Estate Salesperson",
     "note": "The licensing requirements, the two-year term, and the statement that results are reported only as passed or failed.",
     "url": "https://dos.ny.gov/real-estate-agent"},
]


# --------------------------------------------------------------- lessons

STUDY = {}

STUDY["ny/agency"] = {
    "summary": "Eleven of the syllabus's seventy-seven hours go here, more than any other single subject. New York names six relationships, hands out a disclosure form at precise moments, and keeps the signed receipt for three years.",
    "sections": [
        {"h": "The relationships New York names (RPL 443(1))",
         "l": ["SELLER'S AGENT - a listing agent acting alone, or one cooperating with the listing agent, acting as the seller's subagent or as a broker's agent to find a buyer.",
               "BUYER'S AGENT - contracts to locate property for a buyer, or finds a buyer, presents the offer and negotiates for the buyer.",
               "LISTING AGENT - has entered into a listing agreement to act for the owner for compensation.",
               "DUAL AGENT - acts as buyer's agent and seller's agent, or tenant's agent and landlord's agent, in the SAME transaction.",
               "DESIGNATED SALES AGENT - a salesperson or associate broker, under the broker's supervision, assigned to represent one client where the same broker also represents the other client in that transaction.",
               "BROKER'S AGENT - engaged by a listing, buyer's or tenant's agent to assist, but NOT from the same firm. The broker's agent has no direct relationship with the seller, buyer, landlord or tenant, who therefore carry no vicarious liability for the broker's agent's acts."],
         "check": [("An agent assisting a listing agent but working at a different firm is:", "A broker's agent", ["A subagent of the seller", "A dual agent", "A designated sales agent"], "RPL 443(1)(k)."),
                   ("A designated sales agent works:", "Under the supervision of a broker who represents both clients", ["For a different brokerage", "Without any supervision", "Only in commercial deals"], "RPL 443(1)(j)."),
                   ("Because the broker's agent has no direct relationship with the parties:", "The parties carry no vicarious liability for the broker's agent's acts", ["The broker's agent owes no duties", "The broker's agent cannot be paid", "No disclosure is needed"], "RPL 443(1)(k).")]},
        {"h": "What counts as residential real property",
         "p": ["For the disclosure rules, RESIDENTIAL REAL PROPERTY means property used or intended to be used, wholly or partly, as a home for one or more people, improved by a ONE-TO-FOUR FAMILY DWELLING, or a CONDOMINIUM or COOPERATIVE APARTMENT. Unimproved land on which such dwellings are to be built is NOT included (RPL 443(1)(f))."],
         "check": [("Which is residential real property for the agency disclosure rules?", "A cooperative apartment", ["A vacant lot zoned for houses", "A 12-unit apartment block", "A warehouse"], "RPL 443(1)(f) covers 1-4 family dwellings and condo or co-op apartments.")]},
        {"h": "When the disclosure form is given (RPL 443(3))",
         "l": ["A SELLER'S or LANDLORD'S agent gives it to the seller or landlord BEFORE entering into the listing agreement, and obtains a signed acknowledgment.",
               "That same agent gives it to the BUYER or TENANT (or their agent) at the time of the FIRST SUBSTANTIVE CONTACT, and obtains a signed acknowledgment.",
               "A BUYER'S or TENANT'S agent gives it to the buyer or tenant BEFORE entering into the agreement to act for them, and to the seller or seller's agent at the FIRST SUBSTANTIVE CONTACT.",
               "The agent gives the party a copy of the signed acknowledgment and keeps a copy for NOT LESS THAN THREE YEARS.",
               "If a party REFUSES to sign, the agent sets out the facts in a written declaration under oath or affirmation."],
         "check": [("A listing agent must give the disclosure form to the seller:", "Before entering into the listing agreement", ["At the first open house", "When an offer arrives"], "RPL 443(3)(a)."),
                   ("A buyer's agent meeting the listing agent for the first time must provide the form:", "At the time of first substantive contact", ["Within three days", "Only if asked"], "RPL 443(3)(c)."),
                   ("The signed acknowledgment must be kept for:", "Not less than three years", ["One year", "Six months"], "RPL 443(3)(d)."),
                   ("If the seller refuses to sign the acknowledgment, the agent:", "Sets out the facts in a written declaration under oath", ["Cannot take the listing", "Signs on the seller's behalf"], "RPL 443(3)(e).")]},
        {"h": "Getting paid",
         "l": ["A broker may split a fee only with a salesperson regularly associated with that broker, another licensed broker, or a person regularly engaged in real estate brokerage in a state OUTSIDE New York (RPL 442).",
               "A SALESPERSON may not take compensation of any kind from anyone except the licensed broker with whom they are associated (RPL 442-a).",
               "Nobody may sue for a commission without alleging AND PROVING they were duly licensed when the cause of action arose (RPL 442-d).",
               "When a salesperson's association ends, the broker must notify the Department of State at once (RPL 442-b)."],
         "check": [("A New York salesperson may be paid by:", "Only the broker they are associated with", ["The seller directly", "Any cooperating broker"], "RPL 442-a."),
                   ("To sue for a commission in New York you must prove:", "You were duly licensed when the cause of action arose", ["You had a written agreement only", "You were a board member"], "RPL 442-d.")]},
    ],
    "traps": [
        "Six relationships, and the broker's agent is the one from a DIFFERENT firm.",
        "Before the listing agreement for your own client; first substantive contact for the other side.",
        "Three years for the signed acknowledgment.",
        "A refusal to sign does not stop the deal - it triggers a sworn declaration.",
        "Residential means 1-4 family, condo or co-op; not vacant land.",
    ],
    "vocab": [
        ["Broker's agent", "An agent from another firm assisting a listing or buyer's agent."],
        ["Designated sales agent", "An agent assigned to one client where the broker has both."],
        ["Dual agent", "An agent acting for both sides of the same transaction."],
        ["First substantive contact", "When the disclosure form is due to the other side."],
        ["Vicarious liability", "Liability for another's acts; the parties have none for a broker's agent."],
    ],
    "examples": [
        {"t": "Two clients, one firm",
         "s": "A broker lists a house and another salesperson at the same firm brings a buyer.",
         "w": ["The broker now has both clients, which is dual agency.",
               "New York allows the broker to assign a DESIGNATED SALES AGENT to each client.",
               "The disclosure form must set out the arrangement and be acknowledged."],
         "k": "Dual agency with designated sales agents, disclosed and acknowledged in writing."},
    ],
}

STUDY["ny/fair-housing"] = {
    "summary": "Six syllabus hours, and the single most common way New York differs from the national material: the state's protected classes go a long way past the federal seven.",
    "sections": [
        {"h": "New York's protected classes (Executive Law 296(5))",
         "p": ["It is an unlawful discriminatory practice for an owner, lessee, sub-lessee, assignee or managing agent - or any agent or employee of theirs - to refuse to sell, rent or lease a housing accommodation, or to represent it is unavailable when it is available, because of:"],
         "l": ["RACE", "CREED", "COLOR", "NATIONAL ORIGIN", "SEXUAL ORIENTATION",
               "MILITARY STATUS", "SEX", "AGE", "DISABILITY", "MARITAL STATUS", "FAMILIAL STATUS"],
         "check": [("Which is a protected class under New York's Human Rights Law but not the federal Fair Housing Act?", "Marital status", ["Race", "Colour", "National origin"], "Creed, sexual orientation, military status, age and marital status go beyond the federal list."),
                   ("Telling a caller a flat is taken when it is available is:", "An unlawful discriminatory practice", ["Permissible puffing", "Allowed if the owner instructed it", "A civil matter only"], "Executive Law 296(5)(a)(1).")]},
        {"h": "What else the section reaches",
         "l": ["Discriminating in the TERMS, CONDITIONS OR PRIVILEGES of a sale, rental or lease, or in the facilities or services that go with it (296(5)(a)(2)).",
               "Printing or circulating any statement, advertisement, publication or APPLICATION FORM, or making any record or INQUIRY, that expresses directly or indirectly any limitation or discrimination (296(5)(a)(3)).",
               "An instruction from an owner is no defence: the agent and employee are covered in their own right.",
               "A licensee who breaks article 15 of the Executive Law in their capacity as a broker or salesperson can have the licence revoked or suspended, or be fined (RPL 441-c(1)(a))."],
         "check": [("A discriminatory question on a rental application is:", "Unlawful, even if no one is refused", ["Lawful if the applicant answers willingly", "Lawful for co-ops", "Only a problem if acted on"], "296(5)(a)(3) reaches the inquiry itself."),
                   ("An owner instructs an agent to refuse a family with children. The agent:", "Commits the violation if they comply", ["Is protected by the owner's instruction", "Must comply with the client", "Should get it in writing first"], "The agent is liable in their own right.")]},
        {"h": "Enforcement",
         "p": ["The Department of State may revoke or suspend a licence, or impose a FINE NOT EXCEEDING $2,000, for a violation of article 15 of the Executive Law committed as a broker or salesperson. FIFTY PERCENT of such fines goes to the anti-discrimination in housing fund (RPL 441-c(1)(a)). Continuing education reflects this too: every two-year renewal includes at least three hours on fair housing and discrimination, two hours of cultural competency and two hours of implicit bias."],
         "check": [("The maximum Department of State fine is:", "$2,000", ["$1,000", "$5,000"], "RPL 441-c(1)(a)."),
                   ("Half of such fines is paid to:", "The anti-discrimination in housing fund", ["The general fund", "The complainant"], "RPL 441-c(1)(a).")]},
    ],
    "traps": [
        "Creed, sexual orientation, military status, age and marital status are New York additions. The federal list alone is not enough.",
        "The inquiry or application question is itself unlawful - no refusal is needed.",
        "The fine is $2,000, and half of it funds anti-discrimination work.",
        "An owner's instruction never shields the agent.",
    ],
    "vocab": [
        ["Human Rights Law", "Executive Law article 15, New York's anti-discrimination statute."],
        ["Housing accommodation", "The dwelling covered by section 296(5)."],
        ["Creed", "Religious belief; a New York protected class."],
        ["Military status", "A New York protected class with no federal counterpart."],
        ["Cultural competency", "Understanding cultural norms and challenges; a required CE subject."],
    ],
    "examples": [],
}

STUDY["ny/practice"] = {
    "summary": "The regulations in 19 NYCRR part 175 are short and very testable: three business days for the principal's money, a specific explanation on every exclusive residential listing, and a sign the sidewalk can read.",
    "sections": [
        {"h": "The principal's money (19 NYCRR 175.1)",
         "l": ["A broker shall NOT COMMINGLE the money or property of a principal with their own.",
               "The broker maintains a SEPARATE, SPECIAL bank account used EXCLUSIVELY for those monies.",
               "The deposit shall be made WITHIN THREE BUSINESS DAYS.",
               "Until deposited, the money must be SAFEGUARDED IN A SECURE LOCATION against loss or misappropriation.",
               "It goes only into a FEDERALLY INSURED bank account - no other depository, fund or investment.",
               "Any accrued INTEREST may not be kept by or for the broker, except where applied to and deducted from earned commission with the consent of ALL parties."],
         "check": [("A New York broker must deposit a principal's money within:", "Three business days", ["The next business day", "Five calendar days"], "19 NYCRR 175.1."),
                   ("Interest accrued on escrowed money:", "May not be retained by the broker, save against earned commission with all parties' consent", ["Belongs to the broker", "Always goes to the buyer"], "19 NYCRR 175.1."),
                   ("Before deposit, the money must be:", "Safeguarded in a secure location", ["Held by the salesperson", "Deposited in the operating account"], "19 NYCRR 175.1.")]},
        {"h": "Exclusive listings on homes (19 NYCRR 175.24)",
         "l": ["Every exclusive listing of RESIDENTIAL property (1-4 family, condo or co-op) must carry, attached or printed on it and signed or initialled by the owner, an EXPLANATION in type no smaller than SIX POINT.",
               "The explanation sets out the difference: under an EXCLUSIVE RIGHT TO SELL the owner owes the commission even if the owner finds the buyer; under an EXCLUSIVE AGENCY the owner owes nothing if the owner finds the buyer.",
               "Where the broker belongs to a multiple listing service, the agreement must give the homeowner the OPTION of having offers submitted through the listing broker or through the selling broker."],
         "check": [("Under an exclusive RIGHT TO SELL, an owner who finds their own buyer:", "Still owes the agreed commission", ["Owes nothing", "Owes half"], "That is the difference from an exclusive agency."),
                   ("The explanation on an exclusive residential listing must be in type of at least:", "Six point", ["Ten point", "Twelve point"], "19 NYCRR 175.24(b).")]},
        {"h": "Offices, signs and advertising",
         "l": ["Each licensed broker must have and maintain a DEFINITE PLACE OF BUSINESS in New York, with a sign outside READABLE FROM THE SIDEWALK giving the name and the business. In an office, apartment or hotel building, the name and the words 'licensed real estate broker' go in the space provided for occupants' names - not the mail box (RPL 441-a(3)).",
               "A broker with more than one place of business applies for a SUPPLEMENTAL LICENCE for each branch office, each under the direct supervision of the broker or an appointed office manager.",
               "A salesperson's principal residence is not a place of business merely because the residence telephone number appears on a business card.",
               "ADVERTISING under 19 NYCRR 175.25 covers mail, telephone, websites, email, bulletin boards, business cards, signs, billboards and flyers - anything promoting licensed activity.",
               "A TEAM is two or more people, at least one an associate broker or salesperson, in the same brokerage who hold themselves out as a team."],
         "check": [("A broker's office sign must be:", "Readable from the sidewalk", ["At least one square metre", "Illuminated"], "RPL 441-a(3)."),
                   ("A broker with three offices needs:", "A supplemental licence for each branch", ["One licence covering all", "A separate corporation per office"], "RPL 441-a(3)."),
                   ("Under 19 NYCRR 175.25, advertising includes:", "Websites, email and business cards", ["Only newspaper advertisements", "Only signs on the property"], "The definition is deliberately broad.")]},
    ],
    "traps": [
        "Three BUSINESS days, into a separate special federally insured account.",
        "Six point type for the exclusive-listing explanation.",
        "Exclusive right to sell: owner pays either way. Exclusive agency: owner finding the buyer pays nothing.",
        "Each branch office needs its own supplemental licence.",
    ],
    "vocab": [
        ["Commingling", "Mixing the principal's money with the broker's own."],
        ["Special bank account", "The separate escrow account a New York broker must keep."],
        ["Exclusive right to sell", "The owner owes the commission whoever finds the buyer."],
        ["Exclusive agency", "The owner owes nothing if the owner finds the buyer."],
        ["Supplemental licence", "The licence required for each branch office."],
        ["Team", "Two or more licensees in one brokerage holding out as a team."],
    ],
    "examples": [
        {"t": "The owner's own buyer",
         "s": "A homeowner signs an exclusive right to sell, then sells to a colleague they found themselves.",
         "w": ["Under an exclusive right to sell the commission is owed whoever finds the buyer.",
               "That is precisely what the six-point explanation must have told them."],
         "k": "The commission is owed to the listing broker."},
    ],
}

STUDY["ny/license-law"] = {
    "summary": "Three syllabus hours of licence law plus the hour on licensee safety. The numbers: 18 to sell, 20 to broker, 77 hours in, 22.5 hours every two years to stay.",
    "sections": [
        {"h": "Getting licensed",
         "l": ["A SALESPERSON must be OVER 18. A BROKER must be 20 OR OVER (RPL 440-a).",
               "A salesperson completes 77 HOURS of approved qualifying education, six of which are on fair housing and discrimination, and passes the state examination.",
               "A salesperson must be SPONSORED by a licensed New York broker and cannot operate independently.",
               "A broker needs 152 HOURS in total: the 77-hour salesperson course may be credited if completed within eight years, plus the broker course, together with the required experience.",
               "A conviction is not an automatic bar; the Secretary decides under article 23-A of the Correction Law."],
         "check": [("The minimum age for a New York salesperson licence is:", "Over 18", ["16", "20", "21"], "Brokers must be 20 or over (RPL 440-a)."),
                   ("The minimum age for a New York broker licence is:", "20", ["18", "21", "25"], "RPL 440-a."),
                   ("Qualifying education for a salesperson is:", "77 hours", ["45 hours", "152 hours", "22.5 hours"], "152 hours is the broker total.")]},
        {"h": "Keeping the licence",
         "l": ["A licence runs TWO YEARS.",
               "Continuing education: at least 22.5 HOURS in the two years before renewal, which must include at least 3 hours on FAIR HOUSING and discrimination, 2 hours of CULTURAL COMPETENCY, 2 hours of IMPLICIT BIAS, 2.5 hours of ETHICAL BUSINESS PRACTICES, 1 hour on RECENT LEGAL MATTERS, and 1 hour on the LAW OF AGENCY - 2 hours of agency for a salesperson's initial two-year term (RPL 441(3)(a)).",
               "The broker holds the salesperson's licence; the salesperson carries a POCKET CARD.",
               "When an association ends, the broker notifies the Department of State at once (RPL 442-b)."],
         "check": [("Continuing education in New York is:", "22.5 hours every two years", ["45 hours every four years", "14 hours every two years"], "RPL 441(3)(a)."),
                   ("How much of the CE must be agency instruction in a salesperson's FIRST two-year term?", "2 hours", ["1 hour", "3 hours"], "One hour thereafter (RPL 441(3)(a))."),
                   ("A New York licence term is:", "Two years", ["One year", "Four years"], "Department of State.")]},
        {"h": "Discipline",
         "l": ["The Department of State may REVOKE or SUSPEND a licence, impose a FINE NOT EXCEEDING $2,000, or issue a REPRIMAND (RPL 441-c(1)(a)).",
               "Grounds include a conviction of a violation of article 12-A, a material misstatement in the application, fraud or fraudulent practices, DISHONEST OR MISLEADING ADVERTISING, demonstrated UNTRUSTWORTHINESS OR INCOMPETENCY, and violating the Human Rights Law as a licensee.",
               "A salesperson's licence is suspended by the revocation or suspension of the employing broker's licence (RPL 441-d).",
               "Unlicensed practice and other violations of article 12-A are misdemeanours (RPL 442-e)."],
         "check": [("The maximum Department of State fine is:", "$2,000", ["$1,000", "$5,000", "$10,000"], "RPL 441-c(1)(a)."),
                   ("If a broker's licence is revoked, the salespersons' licences are:", "Suspended", ["Unaffected", "Automatically transferred"], "RPL 441-d.")]},
    ],
    "traps": [
        "18 to sell, 20 to broker. New York is unusual in setting them apart.",
        "77 hours in, 22.5 hours every two years after.",
        "The fine ceiling is $2,000, not $1,000.",
        "The broker holds the licence; the salesperson holds a pocket card.",
    ],
    "vocab": [
        ["Article 12-A", "The Real Property Law article governing brokers and salespersons."],
        ["Pocket card", "The card a licensee carries as evidence of licensure."],
        ["Associate broker", "Someone qualified as a broker but working under another broker."],
        ["Supplemental licence", "The licence for each branch office."],
        ["Blind ad", "An advertisement that conceals that a licensee placed it."],
    ],
    "examples": [],
}

STUDY["ny/disclosures"] = {
    "summary": "Article 14 makes a residential seller hand over a condition statement before the contract is signed. What changed recently matters: the old option of giving the buyer a $500 credit instead is no longer in the statute.",
    "sections": [
        {"h": "The statement (RPL 462)",
         "p": ["Every seller of residential real property under a purchase contract must COMPLETE AND SIGN a property condition disclosure statement and deliver it, or a copy, to the buyer or the buyer's agent BEFORE THE BUYER SIGNS A BINDING CONTRACT OF SALE. A copy signed by BOTH seller and buyer is then ATTACHED to the purchase contract. Nothing in the article stops the parties agreeing to sell 'as is'."],
         "check": [("The property condition disclosure statement must be delivered:", "Before the buyer signs a binding contract of sale", ["At closing", "Within three days after the contract"], "RPL 462(1)."),
                   ("The signed statement must then be:", "Attached to the real estate purchase contract", ["Filed with the county", "Kept by the broker only"], "RPL 462(1).")]},
        {"h": "What the 2024 amendment removed",
         "p": ["Older study guides teach that a seller could simply give the buyer a $500 CREDIT at closing instead of delivering the statement. That option is NOT in the current statute. Section 465 now deals only with LIABILITY: a seller who provides, or fails to provide, a statement or a revised statement is liable only for a WILFUL FAILURE to meet the article's requirements, and for a wilful failure is liable for the buyer's ACTUAL DAMAGES, on top of any other remedy."],
         "check": [("Under the current statute, a seller who does not deliver the statement:", "May be liable for actual damages on a wilful failure", ["Simply credits the buyer $500 at closing", "Voids the contract"], "RPL 465; the $500 credit is gone."),
                   ("Liability under article 14 attaches for:", "A wilful failure to perform the article's requirements", ["Any innocent mistake", "Strict liability regardless of fault"], "RPL 465(2).")]},
        {"h": "Exemptions (RPL 463)",
         "l": ["A transfer under a COURT ORDER - including a probate court transfer, a writ of execution, a bankruptcy trustee or debtor-in-possession, eminent domain, or a decree of specific performance.",
               "A transfer to a mortgagee by DEED IN LIEU of foreclosure, or in satisfaction of the mortgage debt.",
               "A transfer to a beneficiary of a DEED OF TRUST.",
               "A transfer pursuant to a FORECLOSURE SALE following a default."],
         "check": [("Which sale needs no property condition disclosure statement?", "A foreclosure sale after default", ["An owner-occupant selling their house", "An investor selling a renovated house"], "RPL 463(4).")]},
        {"h": "The agent's own duty (RPL 466)",
         "p": ["A LISTING agent must timely inform each seller they represent of the seller's obligations under article 14. An agent representing a BUYER - or, where the buyer is unrepresented, the seller's agent dealing with that buyer - must inform the buyer of the buyer's rights and obligations under the article, and in any event BEFORE THE BUYER SIGNS A BINDING CONTRACT. An agent who does this has no further duty under the article and is not liable for a violation of it."],
         "check": [("A listing agent's duty under article 14 is to:", "Timely inform the seller of the seller's obligations", ["Complete the statement for the seller", "Verify every answer"], "RPL 466."),
                   ("An agent who performs the section 466 duties:", "Has no further duty and is not liable under the article", ["Remains liable for the seller's errors", "Must indemnify the buyer"], "RPL 466.")]},
    ],
    "traps": [
        "The $500 credit is NOT in the current law. Any answer offering it is out of date.",
        "Delivery is before the buyer signs a binding contract, not at closing.",
        "Liability is for a WILFUL failure, and then for actual damages.",
        "An agent who gives the required information is off the hook under the article.",
    ],
    "vocab": [
        ["Property Condition Disclosure Act", "Real Property Law article 14."],
        ["Wilful failure", "The fault standard for seller liability under section 465."],
        ["Deed in lieu of foreclosure", "A transfer to the lender instead of foreclosure; exempt."],
        ["As is", "A sale where the buyer accepts the condition; still permitted by article 14."],
    ],
    "examples": [
        {"t": "The outdated answer",
         "s": "A revision guide says the seller can skip the statement by crediting the buyer $500.",
         "w": ["That option was in an earlier version of the article.",
               "The current section 465 speaks only of liability for a wilful failure."],
         "k": "Check the live statute. The $500 credit no longer exists."},
    ],
}


# ------------------------------------------------------------- questions
# (topic, subtopic, difficulty, question, right, [wrong x3], explanation)

Q = [
 # agency
 ("ny/agency", "Relationships", 1, "An agent engaged by a listing agent to help, but working at a different firm, is:",
  "A broker's agent", ["A subagent of the seller", "A dual agent", "A designated sales agent"],
  "RPL 443(1)(k)."),
 ("ny/agency", "Relationships", 2, "A salesperson assigned to represent one client where the same broker also represents the other client is:",
  "A designated sales agent", ["A broker's agent", "A dual agent", "A subagent"],
  "RPL 443(1)(j)."),
 ("ny/agency", "Relationships", 1, "An agent acting for both buyer and seller in one transaction is:",
  "A dual agent", ["A broker's agent", "A listing agent", "A designated sales agent"],
  "RPL 443(1)(i)."),
 ("ny/agency", "Relationships", 3, "Because a broker's agent has no direct relationship with the parties:",
  "The parties have no vicarious liability for the broker's agent's acts", ["The broker's agent owes no duty of honesty", "No disclosure form is needed", "The broker's agent cannot be paid"],
  "RPL 443(1)(k)."),
 ("ny/agency", "Relationships", 2, "Who gives direction to a broker's agent?",
  "The listing, buyer's or tenant's agent who engaged them", ["The seller directly", "The Department of State", "The buyer directly"],
  "RPL 443(1)(k)."),
 ("ny/agency", "Residential property", 2, "For the agency disclosure rules, residential real property includes:",
  "A cooperative apartment", ["A vacant lot zoned for housing", "A 20-unit apartment building", "A retail unit"],
  "One-to-four family dwellings and condo or co-op apartments (RPL 443(1)(f))."),
 ("ny/agency", "Residential property", 3, "Unimproved land on which homes will be built is:",
  "Not residential real property for these rules", ["Residential real property", "Residential only if subdivided", "Covered once plans are filed"],
  "RPL 443(1)(f)."),
 ("ny/agency", "Disclosure timing", 1, "A listing agent must give the agency disclosure form to the seller:",
  "Before entering into the listing agreement", ["At the first open house", "When the first offer arrives", "At closing"],
  "RPL 443(3)(a)."),
 ("ny/agency", "Disclosure timing", 2, "A seller's agent must give the form to a prospective buyer:",
  "At the time of first substantive contact", ["Only once an offer is made", "At the closing table", "Within five days of the showing"],
  "RPL 443(3)(b)."),
 ("ny/agency", "Disclosure timing", 2, "A buyer's agent must give the form to the buyer:",
  "Before entering into the agreement to act as the buyer's agent", ["After the first showing", "When the offer is accepted", "At closing"],
  "RPL 443(3)(c)."),
 ("ny/agency", "Disclosure timing", 2, "The signed acknowledgment of the disclosure form must be kept for:",
  "Not less than three years", ["One year", "Six months", "Seven years"],
  "RPL 443(3)(d)."),
 ("ny/agency", "Disclosure timing", 3, "A seller refuses to sign the acknowledgment. The agent must:",
  "Set out the facts in a written declaration under oath or affirmation", ["Decline the listing", "Sign it on the seller's behalf", "Report the seller to the Department"],
  "RPL 443(3)(e)."),
 ("ny/agency", "Compensation", 1, "A New York salesperson may accept compensation from:",
  "Only the broker with whom they are associated", ["The seller directly", "Any cooperating broker", "The title company"],
  "RPL 442-a."),
 ("ny/agency", "Compensation", 2, "A broker may split a commission with:",
  "A person regularly engaged in real estate brokerage in another state", ["An unlicensed friend who found the buyer", "The buyer's attorney as a referral fee", "An unlicensed assistant"],
  "RPL 442."),
 ("ny/agency", "Compensation", 2, "To sue for a commission in New York, a person must allege and prove:",
  "They were duly licensed when the cause of action arose", ["They had a written agreement", "They belonged to a board of realtors", "They were a resident of New York"],
  "RPL 442-d."),
 ("ny/agency", "Compensation", 3, "When a salesperson's association with a broker ends, the broker must:",
  "Notify the Department of State at once", ["Wait until the next renewal", "Notify the local board", "Do nothing"],
  "RPL 442-b."),

 # fair housing
 ("ny/fair-housing", "Protected classes", 1, "Which is protected under New York's Human Rights Law but not the federal Fair Housing Act?",
  "Marital status", ["Race", "Colour", "National origin"],
  "New York adds creed, sexual orientation, military status, age and marital status."),
 ("ny/fair-housing", "Protected classes", 2, "Which of these is a New York protected class?",
  "Military status", ["Credit score", "Occupation", "Length of residency"],
  "Executive Law 296(5)(a)(1)."),
 ("ny/fair-housing", "Protected classes", 2, "New York's list of protected classes includes:",
  "Creed", ["Political party", "Education level", "Employer"],
  "Executive Law 296(5)(a)(1)."),
 ("ny/fair-housing", "Unlawful practices", 1, "Telling a caller a flat is unavailable when it is available, because of their race, is:",
  "An unlawful discriminatory practice", ["Lawful if the owner instructed it", "Lawful puffing", "A matter for the courts only"],
  "Executive Law 296(5)(a)(1)."),
 ("ny/fair-housing", "Unlawful practices", 2, "A discriminatory question on a rental application is:",
  "Unlawful in itself, even if nobody is refused", ["Lawful if answered voluntarily", "Lawful for cooperatives", "Only unlawful if acted upon"],
  "Executive Law 296(5)(a)(3) reaches the record or inquiry."),
 ("ny/fair-housing", "Unlawful practices", 3, "An owner instructs the agent to exclude families with children. The agent who complies:",
  "Commits the violation personally", ["Is protected by the owner's instruction", "Must follow the client's lawful instruction", "Is liable only if sued by the owner"],
  "Agents and employees are covered in their own right."),
 ("ny/fair-housing", "Enforcement", 2, "A licensee who breaks the Human Rights Law while acting as a broker or salesperson may:",
  "Have the licence revoked or suspended, or be fined", ["Only be sued privately", "Face no licensing consequence", "Be fined but never suspended"],
  "RPL 441-c(1)(a)."),
 ("ny/fair-housing", "Enforcement", 3, "Fifty percent of such fines is paid into:",
  "The anti-discrimination in housing fund", ["The state general fund", "A fund for complainants", "The licensee education fund"],
  "RPL 441-c(1)(a)."),
 ("ny/fair-housing", "Education", 2, "Every two-year renewal must include at least how many hours on fair housing and discrimination?",
  "Three", ["One", "Two", "Six"],
  "RPL 441(3)(a)."),

 # practice
 ("ny/practice", "Escrow", 1, "A New York broker must deposit a principal's money within:",
  "Three business days", ["The next business day", "Five calendar days", "Ten business days"],
  "19 NYCRR 175.1."),
 ("ny/practice", "Escrow", 1, "The account holding a principal's money must be:",
  "A separate, special, federally insured bank account used exclusively for it", ["The broker's operating account", "Any investment account", "A money market fund"],
  "19 NYCRR 175.1."),
 ("ny/practice", "Escrow", 2, "Interest accruing on escrowed money:",
  "May not be kept by the broker, except applied to earned commission with all parties' consent", ["Belongs to the broker", "Always belongs to the seller", "Must be paid to the Department"],
  "19 NYCRR 175.1."),
 ("ny/practice", "Escrow", 2, "Before it is deposited, a principal's money must be:",
  "Safeguarded in a secure location against loss or misappropriation", ["Held by the salesperson who received it", "Deposited in the operating account temporarily", "Returned to the payer"],
  "19 NYCRR 175.1."),
 ("ny/practice", "Escrow", 1, "Mixing a principal's money with the broker's own is:",
  "Commingling, which is prohibited", ["Permitted up to $200", "Permitted if recorded", "Required for reconciliation"],
  "19 NYCRR 175.1."),
 ("ny/practice", "Exclusive listings", 1, "Under an exclusive RIGHT TO SELL, an owner who finds their own buyer:",
  "Still owes the agreed commission", ["Owes nothing", "Owes half the commission", "Owes only expenses"],
  "19 NYCRR 175.24(b)."),
 ("ny/practice", "Exclusive listings", 2, "Under an exclusive AGENCY listing, an owner who finds their own buyer:",
  "Owes no commission to the broker", ["Owes the full commission", "Owes a commission to both brokers", "Owes a cancellation fee"],
  "19 NYCRR 175.24(b)."),
 ("ny/practice", "Exclusive listings", 2, "The explanation on an exclusive residential listing must be in type of at least:",
  "Six point", ["Eight point", "Ten point", "Twelve point"],
  "19 NYCRR 175.24(b)."),
 ("ny/practice", "Exclusive listings", 3, "Where the listing broker belongs to a multiple listing service, the agreement must give the owner:",
  "The option of having offers submitted through the listing broker or the selling broker", ["A guaranteed sale", "A reduced commission", "The right to cancel at will"],
  "19 NYCRR 175.24(c)."),
 ("ny/practice", "Offices", 1, "A New York broker's office sign must be:",
  "Readable from the sidewalk", ["At least two feet wide", "Illuminated at night", "Approved by the Department"],
  "RPL 441-a(3)."),
 ("ny/practice", "Offices", 2, "In an apartment or hotel building, the broker's name and the words 'licensed real estate broker' go:",
  "In the space provided for occupants' names, not the mail box", ["On the mail box", "On the apartment door only", "Nowhere; the rule does not apply"],
  "RPL 441-a(3)."),
 ("ny/practice", "Offices", 2, "A broker with three places of business needs:",
  "A supplemental licence for each branch office", ["One licence for all offices", "A separate corporation for each", "No additional licence"],
  "RPL 441-a(3)."),
 ("ny/practice", "Offices", 3, "A salesperson's home is a place of business:",
  "Not merely because the home telephone number is on a business card", ["Whenever clients are met there", "Always", "Only if a sign is posted"],
  "RPL 441-a(3)."),
 ("ny/practice", "Advertising", 2, "Under 19 NYCRR 175.25, advertising includes:",
  "Websites, email, business cards, signs and flyers", ["Only newspaper advertisements", "Only signs on the property", "Only paid promotions"],
  "The definition covers promotion of licensed activity in any medium."),
 ("ny/practice", "Advertising", 3, "A 'team' under the advertising rule means:",
  "Two or more licensees in the same brokerage holding out as a team", ["Any two cooperating brokers", "A broker and an attorney", "A brokerage with more than ten agents"],
  "19 NYCRR 175.25(a)(2); one member must be an associate broker or salesperson."),

 # license law
 ("ny/license-law", "Eligibility", 1, "The minimum age for a New York real estate salesperson licence is:",
  "Over 18", ["16", "20", "21"],
  "RPL 440-a."),
 ("ny/license-law", "Eligibility", 2, "The minimum age for a New York real estate broker licence is:",
  "20", ["18", "19", "21"],
  "RPL 440-a. New York sets the two ages apart."),
 ("ny/license-law", "Education", 1, "Qualifying education for a New York salesperson is:",
  "77 hours", ["45 hours", "63 hours", "152 hours"],
  "152 hours is the broker total."),
 ("ny/license-law", "Education", 2, "Total qualifying education for a New York broker is:",
  "152 hours", ["77 hours", "120 hours", "180 hours"],
  "The 77-hour salesperson course may be credited if taken within eight years."),
 ("ny/license-law", "Education", 3, "Of the 77 hours, how many must address fair housing and discrimination?",
  "Six", ["Three", "Two", "Eleven"],
  "RPL 441."),
 ("ny/license-law", "Renewal", 1, "A New York real estate licence runs for:",
  "Two years", ["One year", "Three years", "Four years"],
  "Department of State."),
 ("ny/license-law", "Renewal", 1, "Continuing education in New York is:",
  "22.5 hours every two years", ["14 hours every two years", "45 hours every four years", "30 hours every two years"],
  "RPL 441(3)(a)."),
 ("ny/license-law", "Renewal", 2, "The continuing education must include how many hours of implicit bias instruction?",
  "Two", ["One", "Three", "None"],
  "RPL 441(3)(a)."),
 ("ny/license-law", "Renewal", 3, "In a salesperson's FIRST two-year term, agency instruction must total:",
  "Two hours", ["One hour", "Three hours", "Four hours"],
  "One hour thereafter (RPL 441(3)(a))."),
 ("ny/license-law", "Renewal", 2, "Cultural competency instruction required at each renewal is:",
  "Two hours", ["One hour", "Three hours", "None"],
  "RPL 441(3)(a)."),
 ("ny/license-law", "Discipline", 1, "The Department of State may fine a licensee up to:",
  "$2,000", ["$500", "$1,000", "$5,000"],
  "RPL 441-c(1)(a)."),
 ("ny/license-law", "Discipline", 2, "If a broker's licence is revoked, the associated salespersons' licences are:",
  "Suspended", ["Unaffected", "Automatically transferred to another broker", "Revoked permanently"],
  "RPL 441-d."),
 ("ny/license-law", "Discipline", 2, "Which is a ground for discipline under RPL 441-c?",
  "Dishonest or misleading advertising", ["Charging a negotiated commission", "Refusing a listing", "Working weekends"],
  "RPL 441-c(1)(a)."),
 ("ny/license-law", "Discipline", 3, "A criminal conviction in a licence application:",
  "Is considered under article 23-A of the Correction Law, not an automatic bar", ["Always bars licensure", "Is ignored entirely", "Bars licensure for ten years"],
  "RPL 440-a."),
 ("ny/license-law", "Sponsorship", 1, "A New York salesperson:",
  "Must be sponsored by a licensed broker and cannot operate independently", ["May operate independently after two years", "May sponsor other salespersons", "May hold their own escrow account"],
  "Department of State."),

 # disclosures
 ("ny/disclosures", "Timing", 1, "The property condition disclosure statement must be delivered:",
  "Before the buyer signs a binding contract of sale", ["At closing", "Within three days after the contract", "Only on request"],
  "RPL 462(1)."),
 ("ny/disclosures", "Timing", 2, "Once signed by both parties, the statement must be:",
  "Attached to the real estate purchase contract", ["Filed with the county clerk", "Held by the broker only", "Sent to the Department of State"],
  "RPL 462(1)."),
 ("ny/disclosures", "The 2024 change", 2, "Under the current statute, a seller who fails to deliver the statement:",
  "May be liable for actual damages on a wilful failure", ["Gives the buyer a $500 credit at closing", "Voids the contract automatically", "Faces no consequence"],
  "RPL 465. The $500 credit option is no longer in the law."),
 ("ny/disclosures", "The 2024 change", 3, "Liability under article 14 attaches for:",
  "A wilful failure to perform the article's requirements", ["Any innocent error on the form", "Strict liability regardless of fault", "Negligence only"],
  "RPL 465(2)."),
 ("ny/disclosures", "Exemptions", 1, "Which transfer needs no property condition disclosure statement?",
  "A foreclosure sale following a default", ["An owner-occupant selling their home", "An investor selling a renovated house", "A builder selling a completed house"],
  "RPL 463(4)."),
 ("ny/disclosures", "Exemptions", 2, "A transfer by deed in lieu of foreclosure is:",
  "Exempt from the disclosure statement", ["Subject to the statement", "Exempt only if the lender agrees", "Subject to double disclosure"],
  "RPL 463(2)."),
 ("ny/disclosures", "Exemptions", 2, "A transfer ordered by a probate court during estate administration is:",
  "Exempt", ["Subject to the statement", "Exempt only for small estates", "Subject to the statement if a broker is involved"],
  "RPL 463(1)."),
 ("ny/disclosures", "Agent's duty", 2, "A listing agent's duty under article 14 is to:",
  "Timely inform the seller of the seller's obligations", ["Complete the statement for the seller", "Verify each answer on the statement", "Deliver it to the county"],
  "RPL 466."),
 ("ny/disclosures", "Agent's duty", 3, "An agent who performs the duties in section 466:",
  "Has no further duty and is not liable under the article", ["Remains liable for the seller's mistakes", "Must indemnify the buyer", "Must file a report with the Department"],
  "RPL 466."),
 ("ny/disclosures", "As is", 3, "An 'as is' sale in New York:",
  "Is still permitted; article 14 does not prevent it", ["Is prohibited for residential property", "Removes the need for the statement", "Requires Department approval"],
  "RPL 462(1)."),
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
            "id": "ny-" + hashlib.sha1(q.encode()).hexdigest()[:8],
            "portion": "georgia", "topic": topic, "subtopic": sub,
            "sub": topic + "|" + sub, "concept": "New York " + sub.lower(),
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
        "code": "NY", "name": "New York", "abbr": "NY",
        "regulator": "NYS Department of State",
        "pass": EXAM["pass"],
        "pass_published": False,
        "pass_note": PASS_NOTE,
        "single": True,
        "portions": {
            "national": {"name": "General practice",
                         "scored": EXAM["national_scored"],
                         "minutes": EXAM["national_minutes"],
                         "blurb": "Estates, deeds, finance, land use, valuation and the maths, as the syllabus sets them."},
            "georgia": {"name": "New York law", "scored": EXAM["state_scored"],
                        "minutes": EXAM["state_minutes"],
                        "blurb": "Article 12-A, the agency disclosure, fair housing, and the Department's rules."},
        },
        "topics": topics, "bank": bank, "study": study,
        "sources": SOURCES, "diffs": DIFFS,
    }


# Where New York departs from the general rule.
DIFFS = {
    "national/agency": [
        "New York names six relationships, including the DESIGNATED SALES AGENT and the BROKER'S AGENT - the latter from a different firm, with no direct relationship to the parties (RPL 443(1)).",
        "The disclosure form goes to your own client before the agreement, and to the other side at FIRST SUBSTANTIVE CONTACT; the signed acknowledgment is kept three years.",
    ],
    "national/practice": [
        "A broker deposits a principal's money in a separate, special, federally insured account WITHIN THREE BUSINESS DAYS, and may not keep the interest (19 NYCRR 175.1).",
        "Every exclusive listing of a home carries a six-point-type explanation of the difference between an exclusive right to sell and an exclusive agency (19 NYCRR 175.24).",
        "Fair housing in New York adds creed, sexual orientation, military status, age, marital status and familial status to the federal classes (Executive Law 296(5)).",
    ],
    "national/disclosures": [
        "The seller's property condition disclosure statement is delivered BEFORE the buyer signs a binding contract, and the signed copy is attached to it (RPL 462).",
        "The $500 credit that older guides describe has been REMOVED; section 465 now imposes liability for a wilful failure, measured by the buyer's actual damages.",
    ],
    "national/contracts": [
        "An attorney commonly drafts or reviews the contract in New York, and in much of the state closings are attorney-conducted.",
    ],
    "national/ownership": [
        "Cooperative apartments are shares in a corporation with a proprietary lease, not real property - and they count as residential real property for the disclosure rules (RPL 443(1)(f)).",
    ],
}


if __name__ == "__main__":
    import io, json, os
    here = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    out = os.path.join(here, "greprep", "packs", "NY.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    pack = build()
    with io.open(out, "w", encoding="utf-8") as f:
        json.dump(pack, f, ensure_ascii=False, indent=1, sort_keys=True)
    print("wrote", out, len(pack["bank"]), "questions,", len(pack["study"]), "lessons")
