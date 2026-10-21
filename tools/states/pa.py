"""Pennsylvania state content: lessons and practice questions.

Pennsylvania splits the examination: 80 scored national items and 40 scored
state items. The five state categories and their item counts below are
Pearson VUE's published outline for the State Real Estate Commission,
effective 16 March 2026.

Pennsylvania does NOT publish a percentage pass mark. The candidate
handbook says raw scores are converted to a scaled score from 0 to 100, set
by the Commission with Pearson, and that "the scaled score that is reported
to you is neither the number of questions you answered correctly nor the
percentage of questions you answered correctly". Numeric scores go only to
failing candidates. So this pack sets `pass_published: false` and the app
presents the figure as a study target. The 75% that prep sites quote is not
the Commission's published mark, and by the handbook's own words it cannot
be read as a percentage of items correct.

Every rule below was read from the official text on 2026-10-21:
  - 49 Pa. Code chapter 35, the State Real Estate Commission's regulations,
    from pacodeandbulletin.gov, current through 56 Pa.B. 5370.
  - The Pearson VUE Pennsylvania Candidate Handbook and Content Outlines
    (#093900, #093901), for the blueprint and the licensing requirements.
  - The Pennsylvania Human Relations Commission, for the protected classes.
The section a fact comes from is cited next to it. Do not add a fact here
without reading its source first.
"""

EXAM = {
    # Pearson: 80 scored national (+5 pretest), 40 scored state (+10
    # pretest). The handbook gives no per-portion timing, only "1 to 2.5
    # hours, depending on the exam"; the minutes below split that maximum
    # in proportion to the item counts and are not a published figure.
    "state_scored": 40,
    "state_minutes": 50,
    "national_scored": 80,
    "national_minutes": 100,
    "pass": 0.75,          # a study target, NOT a published pass mark
}

PASS_NOTE = ("Pennsylvania reports a scaled score from 0 to 100, and its own "
             "handbook says that score is neither the number nor the percentage "
             "of questions answered correctly. The Commission does not publish "
             "the passing figure, and only failing candidates are told a number. "
             "The 75% here is this app's study target, not the state's "
             "requirement.")

# Pearson's published state outline for salespersons, effective 16 March 2026.
TOPICS = [
    ("pa/regulations", "Regulations governing licensees", 11,
     "Advertising, broker and salesperson relations, escrow, prohibited conduct."),
    ("pa/agency", "Agency & disclosure", 10,
     "The Consumer Notice and Pennsylvania's five business relationships."),
    ("pa/licensure", "Licensure", 8,
     "Qualifications, what needs a licence, renewal, reactivation, exemptions."),
    ("pa/misc", "Miscellaneous", 6,
     "Seller disclosure, forms, the Human Relations Act, condos and leases."),
    ("pa/commission", "Real Estate Commission", 5,
     "Duties and powers, complaints and hearings, the Recovery Fund."),
]

SOURCES = [
    {"by": "Pennsylvania State Real Estate Commission",
     "name": "49 Pa. Code chapter 35 (Commission regulations)",
     "note": "Escrow, the Consumer Notice, records, standards of conduct and continuing education. Every rule of practice here was read from it.",
     "url": "https://www.pacodeandbulletin.gov/Display/pacode?file=/secure/pacode/data/049/chapter35/chap35toc.html"},
    {"by": "Pennsylvania General Assembly",
     "name": "Real Estate Licensing and Registration Act (63 P.S. 455.101-455.902)",
     "note": "The licence law the Commission's regulations are made under.",
     "url": "https://www.dos.pa.gov/ProfessionalLicensing/BoardsCommissions/RealEstateCommission"},
    {"by": "Pearson VUE and the State Real Estate Commission",
     "name": "Pennsylvania Candidate Handbook and Content Outlines",
     "note": "The blueprint: 80 national and 40 state scored items, the five state categories, and the scaled-score explanation.",
     "url": "https://www.pearsonvue.com/us/en/pa/realestate.html"},
    {"by": "Pennsylvania Human Relations Commission",
     "name": "Protected classes under the Human Relations Act",
     "note": "Pennsylvania's protected classes, which go beyond the federal list.",
     "url": "https://www.pa.gov/agencies/phrc"},
]


# --------------------------------------------------------------- lessons

STUDY = {}

STUDY["pa/agency"] = {
    "summary": "Pennsylvania does not presume any relationship. A licensee hands over the CONSUMER NOTICE at the initial interview, and the consumer then chooses from five business relationships - including a TRANSACTION LICENSEE, who represents nobody at all.",
    "sections": [
        {"h": "The Consumer Notice (49 Pa. Code 35.336)",
         "l": ["A licensee must give the consumer the CONSUMER NOTICE at the INITIAL INTERVIEW.",
               "It is headed 'Consumer Notice' and says plainly 'THIS IS NOT A CONTRACT'.",
               "The licensee keeps the signed or refused ACKNOWLEDGEMENT for SIX MONTHS and gives the consumer a copy of the whole summary.",
               "It warns the consumer: until you select a business relationship by signing a written agreement, the licensee is NOT representing you. A BUSINESS RELATIONSHIP IS NOT PRESUMED."],
         "check": [("The Consumer Notice must be given:", "At the initial interview", ["At the first showing", "When an offer is written"], "49 Pa. Code 35.336(a)."),
                   ("The signed acknowledgement of the Consumer Notice is kept for:", "Six months", ["Three years", "One year"], "35.336(b)."),
                   ("Until a consumer signs a written agreement, the licensee:", "Is not representing them; no relationship is presumed", ["Is their agent by default", "Is a dual agent"], "The Notice says so expressly.")]},
        {"h": "The five business relationships",
         "l": ["SELLER AGENT - works exclusively for the seller or landlord and must act in their best interest, including a continuous and good faith effort to find a buyer or tenant, except while the property is under an existing agreement. Keeps confidential information confidential, EXCEPT that known MATERIAL DEFECTS must be revealed. A SUBAGENT has the same duties.",
               "BUYER AGENT - works exclusively for the buyer or tenant EVEN IF PAID BY THE SELLER, with the same good faith effort and the same confidentiality rule.",
               "DUAL AGENT - works for both. May not take any action ADVERSE OR DETRIMENTAL to either party, must disclose known material defects, and needs the WRITTEN CONSENT of both parties.",
               "DESIGNATED AGENT - the broker designates some licensees to act exclusively for the seller and others exclusively for the buyer. Because the broker supervises everyone, THE BROKER AUTOMATICALLY SERVES AS A DUAL AGENT, and must take reasonable steps to keep confidential information from spreading inside the company.",
               "TRANSACTION LICENSEE - provides real estate services with NO agency relationship. No duty of loyalty or confidentiality - but still prohibited from disclosing that the seller will take less than the asking price, that the buyer will pay more than the written offer, or that either will agree to other financing terms. Must still disclose known material defects."],
         "check": [("A buyer agent paid by the seller works for:", "The buyer, exclusively", ["The seller, because they pay", "Both parties"], "The Consumer Notice says so expressly."),
                   ("In designated agency, the broker:", "Automatically serves as a dual agent", ["Has no role", "Must pick one side"], "Because the broker supervises all the licensees."),
                   ("A transaction licensee may NOT disclose:", "That the seller will accept less than the asking price", ["A known material defect", "The listing price"], "Material defects are always disclosed."),
                   ("Which relationship carries no duty of loyalty?", "Transaction licensee", ["Buyer agent", "Dual agent", "Designated agent"], "They have no agency relationship at all.")]},
        {"h": "Duties every licensee owes, whatever the relationship",
         "l": ["Exercise reasonable professional SKILL AND CARE meeting the practice standards RELRA requires.",
               "Deal HONESTLY AND IN GOOD FAITH.",
               "Present, AS SOON AS PRACTICABLE, all written offers, counteroffers, notices and communications. A seller may WAIVE this IN WRITING once their property is under contract.",
               "Comply with the Real Estate Seller Disclosure Law.",
               "ACCOUNT for escrow and deposit funds.",
               "Disclose, as soon as practicable, all CONFLICTS OF INTEREST and financial interests.",
               "Assist with document preparation and advise on compliance with the laws of the transaction.",
               "Advise the consumer to seek EXPERT ADVICE on matters beyond the licensee's expertise.",
               "Keep the consumer informed about the transaction and the tasks to be completed.",
               "Disclose a financial interest in a service - financial, title, insurance, construction, repair or inspection - when it is recommended, or when the licensee first learns it will be used."],
         "check": [("The duty to present offers as soon as practicable may be waived:", "In writing by the seller, once the property is under contract", ["Orally by either party", "Never"], "The Consumer Notice sets out the one waiver."),
                   ("A licensee recommending their brother-in-law's inspection firm must:", "Disclose the financial interest when the service is recommended", ["Say nothing", "Disclose only at closing"], "The duty applies to all licensees.")]},
        {"h": "What is negotiable",
         "p": ["The Consumer Notice names four terms as NEGOTIABLE between licensee and consumer, which must be addressed in the agreement or disclosure statement: the DURATION of the employment, listing or contract; the licensee's FEES OR COMMISSION; the SCOPE of the licensee's activities; and the broker's COOPERATION with and SHARING OF FEES with other brokers."],
         "check": [("Which is negotiable under the Consumer Notice?", "The broker's cooperation and fee-sharing with other brokers", ["The Consumer Notice itself", "The duty to disclose material defects"], "All four negotiable terms concern the engagement, not the duties.")]},
    ],
    "traps": [
        "No relationship is PRESUMED in Pennsylvania. Nothing is owed as an agent until something is signed.",
        "Five relationships, and the transaction licensee is the one that is not an agency at all.",
        "In designated agency the BROKER is automatically a dual agent.",
        "Confidentiality never covers a known material defect - in any relationship.",
        "Consumer Notice at the INITIAL INTERVIEW; acknowledgement kept six months.",
    ],
    "vocab": [
        ["Consumer Notice", "The disclosure summary given at the initial interview."],
        ["Transaction licensee", "A licensee providing services with no agency relationship."],
        ["Designated agent", "A licensee assigned to one side where the broker has both."],
        ["Initial interview", "The first contact where substantive discussion occurs; the Notice is due."],
        ["Material defect", "A property fault that must be disclosed whatever the relationship."],
    ],
    "examples": [
        {"t": "Nobody's agent",
         "s": "A licensee meets a buyer at an open house, gives the Consumer Notice, and the buyer signs nothing.",
         "w": ["A business relationship is not presumed in Pennsylvania.",
               "The licensee may act as a transaction licensee: no loyalty, no confidentiality.",
               "They still may not reveal that the seller would take less, and must disclose known material defects."],
         "k": "No agency exists, but the price confidences and the defect duty still bind."},
    ],
}

STUDY["pa/regulations"] = {
    "summary": "Eleven items, the largest category. Most of it is escrow: where the money goes, who may touch it, who gets the interest, and what the broker does when the parties fall out.",
    "sections": [
        {"h": "The escrow account (49 Pa. Code 35.325)",
         "l": ["Maintained in a FEDERALLY- OR STATE-INSURED bank or recognised depository.",
               "DESIGNATES THE BROKER AS TRUSTEE.",
               "Provides for WITHDRAWAL WITHOUT PRIOR NOTICE.",
               "Used EXCLUSIVELY for escrow purposes.",
               "A sole proprietor or broker of record may give an employee WRITTEN authority to deposit, and a LICENSED employee written authority to withdraw for payments properly chargeable to the account.",
               "Where money is expected to be held MORE THAN SIX MONTHS, the broker is ENCOURAGED to use an interest-bearing account. Interest is held and disbursed PRO RATA in the same way as the principal, unless the parties agree otherwise.",
               "A broker MAY NOT CLAIM the interest, unless the broker is a lessor under section 511.2 of the Landlord and Tenant Act."],
         "check": [("A Pennsylvania escrow account must designate:", "The broker as trustee", ["The seller as trustee", "The title company as trustee"], "49 Pa. Code 35.325(a)(2)."),
                   ("Interest earned on an escrow account:", "Is disbursed pro rata like the principal, and the broker may not claim it", ["Belongs to the broker", "Goes to the Commission"], "35.325(c), with the lessor exception."),
                   ("Where money will be held more than six months, the broker is:", "Encouraged to use an interest-bearing account", ["Required to use a non-interest account", "Required to return it"], "35.325(c)."),
                   ("Who may be given written authority to WITHDRAW from escrow?", "A licensed employee, for payments properly chargeable", ["Any employee", "Only the broker, never anyone else"], "35.325(b).")]},
        {"h": "Depositing, and what is not escrow (35.321)",
         "l": ["A broker deposits money received belonging to another into the escrow account, HELD PENDING CONSUMMATION of the transaction or a prior termination that does not involve a dispute - then pays the FULL AMOUNT to the party entitled to it.",
               "Where the broker is a partnership, association or corporation, the BROKER OF RECORD is responsible for ensuring the escrow duty is performed.",
               "RENTS received as a PROPERTY MANAGER for a lessor need NOT be held in escrow. They go into a RENTAL MANAGEMENT ACCOUNT, separate from both the escrow and the general business accounts."],
         "check": [("Rents collected as a property manager go into:", "A separate rental management account", ["The escrow account", "The general business account"], "49 Pa. Code 35.321(b)."),
                   ("In a corporate brokerage, responsibility for the escrow duty rests with:", "The broker of record", ["Each salesperson", "The corporation's accountant"], "35.321(a).")]},
        {"h": "Commingling, and disputes",
         "l": ["A broker MAY NOT COMMINGLE escrow money, or the interest on it, with business, personal or other funds (35.326(a)).",
               "The one exception: a broker MAY deposit business or personal funds to cover BANK SERVICE CHARGES or to maintain a MINIMUM BALANCE the bank requires (35.326(b)).",
               "A broker may not MISAPPROPRIATE escrow money or its interest for business, personal or other purposes (35.326(c)).",
               "DISPUTE (35.327): where the parties disagree over entitlement, the broker RETAINS the money in escrow until the dispute is resolved. If resolution looks remote without legal action, the broker may - after 30 DAYS' NOTICE to the parties - petition the county court to INTERPLEAD the rival claimants."],
         "check": [("A broker may put personal money into escrow only to:", "Cover bank service charges or keep a required minimum balance", ["Round up a deposit", "Lend to a client"], "49 Pa. Code 35.326(b)."),
                   ("When the parties dispute the deposit, the broker first:", "Retains the money in escrow until the dispute is resolved", ["Splits it evenly", "Pays the seller"], "35.327."),
                   ("Before petitioning the court to interplead, the broker must give the parties:", "30 days' notice", ["10 days' notice", "No notice"], "35.327.")]},
        {"h": "Records",
         "l": ["Escrow records must show the NAME of the party from whom the money was received, the name of the party TO WHOM IT BELONGS, the name of the party FOR WHOSE ACCOUNT it is deposited, and the dates (35.328).",
               "The broker must give the Commission, on written request or at an office inspection, a letter authorising the bank to RELEASE THE RECORDS of the escrow account (35.325(d)).",
               "RETENTION (35.286): records of a real estate transaction are kept at least THREE YEARS following consummation. The acknowledgement portion of a Consumer Notice where there was NO transaction is kept SIX MONTHS."],
         "check": [("Transaction records in Pennsylvania are kept for:", "At least three years after consummation", ["One year", "Six months", "Seven years"], "49 Pa. Code 35.286(a)."),
                   ("A Consumer Notice acknowledgement where no transaction followed is kept:", "Six months", ["Three years", "Indefinitely"], "35.286(a)(1).")]},
    ],
    "traps": [
        "Broker as TRUSTEE, withdrawal WITHOUT prior notice, used EXCLUSIVELY for escrow.",
        "Rents as a property manager are NOT escrow - separate rental management account.",
        "The broker never keeps escrow interest, unless acting as a lessor under the Landlord and Tenant Act.",
        "Dispute: hold, then 30 days' notice, then interplead.",
        "Three years for transaction records; six months for an unused Consumer Notice acknowledgement.",
    ],
    "vocab": [
        ["Escrow account", "The insured account, with the broker as trustee, used only for escrow."],
        ["Broker of record", "The broker answerable for a corporate brokerage's escrow duty."],
        ["Rental management account", "The separate account for rents collected as property manager."],
        ["Interplead", "Asking a court to decide between rival claimants to held money."],
        ["Commingling", "Mixing escrow money with business or personal funds."],
    ],
    "examples": [
        {"t": "The deal falls apart",
         "s": "A sale collapses; the buyer wants the deposit back and the seller says it is forfeit.",
         "w": ["The broker holds the money in escrow while the dispute runs.",
               "If settlement looks remote, the broker gives 30 days' notice.",
               "Then the broker may petition the county court to interplead."],
         "k": "Hold, notify for 30 days, then interplead. Never pick a side."},
    ],
}

STUDY["pa/licensure"] = {
    "summary": "Eight items. The entry numbers are 18, a high school diploma, and 75 hours - and renewal turns on 14 hours of continuing education by 31 May.",
    "sections": [
        {"h": "Qualifying as a salesperson",
         "l": ["Be at least 18 YEARS OLD.",
               "Be at least a HIGH SCHOOL GRADUATE or the equivalent.",
               "Complete 5 CREDITS OR 75 HOURS of basic real estate courses through an education provider approved by the Commission, by an out-of-state provider approved where it sits, or at an accredited college.",
               "Alternatively, hold a qualifying degree - for example a bachelor's degree with a MAJOR IN REAL ESTATE from an accredited college.",
               "Pre-licensing courses must have been completed within FIVE YEARS before passing the examination.",
               "Examination scores are valid for THREE YEARS; the licence application must be made within that period."],
         "check": [("The minimum age for a Pennsylvania salesperson licence is:", "18", ["17", "19", "21"], "Pearson handbook / RELRA."),
                   ("Pre-licensing education for a salesperson is:", "5 credits or 75 hours", ["30 hours", "60 hours", "120 hours"], "Through a Commission-approved provider or accredited college."),
                   ("Pennsylvania examination scores remain valid for:", "Three years", ["One year", "Five years"], "The licence application must be filed within that time.")]},
        {"h": "Renewal and continuing education",
         "l": ["A broker or salesperson with a STANDARD licence must, as a CONDITION PRECEDENT to renewal, complete 14 HOURS of Commission-approved continuing education during the preceding licence period (49 Pa. Code 35.382(a)).",
               "It must be completed by the MAY 31 RENEWAL DEADLINE.",
               "To REACTIVATE and renew a NONCURRENT standard licence, the same 14 hours must be completed in the 2-YEAR PERIOD before the reactivation application is submitted (35.382(b)).",
               "The same course may not be used twice."],
         "check": [("Continuing education in Pennsylvania is:", "14 hours per licence period", ["30 hours", "22.5 hours", "8 hours"], "49 Pa. Code 35.382(a)."),
                   ("The continuing education deadline is:", "May 31", ["December 31", "June 30", "The licensee's birthday"], "35.382(a)."),
                   ("Completing the continuing education is:", "A condition precedent to renewal", ["Optional for the first renewal", "Required only of brokers"], "35.382(a).")]},
    ],
    "traps": [
        "75 hours in, 14 hours every licence period, deadline 31 MAY.",
        "Courses must be within five years of passing; scores last three years.",
        "A reactivating licensee needs the 14 hours in the two years before applying.",
    ],
    "vocab": [
        ["Standard licence", "An ordinary Pennsylvania broker or salesperson licence."],
        ["Noncurrent licence", "A licence not renewed, requiring reactivation."],
        ["Condition precedent", "Something that must be done before renewal is possible."],
        ["Rental listing referral agent", "A separate Pennsylvania licence category."],
    ],
    "examples": [],
}

STUDY["pa/misc"] = {
    "summary": "Six items gathering the Pennsylvania law that sits outside the Commission's rules: the Seller Disclosure Law, the zoning line every sales agreement must carry, and a fair housing list longer than the federal one.",
    "sections": [
        {"h": "Seller disclosure and the zoning line",
         "l": ["Every licensee owes consumers a duty to COMPLY WITH THE REAL ESTATE SELLER DISCLOSURE LAW.",
               "ALL SALES AGREEMENTS must contain the property's ZONING CLASSIFICATION - except where the property is zoned solely or primarily to permit SINGLE FAMILY DWELLINGS."],
         "check": [("A Pennsylvania sales agreement must state the zoning classification:", "Unless the property is zoned solely or primarily for single family dwellings", ["Always, without exception", "Only for commercial property"], "The Consumer Notice sets out the rule."),
                   ("Complying with the Seller Disclosure Law is:", "A duty every licensee owes, whatever the relationship", ["Only the seller agent's duty", "Optional in an as-is sale"], "It is in the common duty list.")]},
        {"h": "The Pennsylvania Human Relations Act",
         "p": ["The Pennsylvania Human Relations Commission enforces the Act, which prohibits discrimination in housing and commercial property on these grounds:"],
         "l": ["RACE", "COLOR", "RELIGIOUS CREED", "ANCESTRY", "AGE (40 and over)",
               "SEX", "NATIONAL ORIGIN", "FAMILIAL STATUS (in housing)",
               "DISABILITY", "The USE, HANDLING OR TRAINING OF SUPPORT OR GUIDE ANIMALS for a disability",
               "RETALIATION"],
         "check": [("Which is protected under the Pennsylvania Human Relations Act but not the federal Fair Housing Act?", "Ancestry", ["Race", "Colour", "National origin"], "Pennsylvania adds ancestry, religious creed, age and the guide-animal class."),
                   ("Pennsylvania's protected classes include:", "The use or training of a support or guide animal for a disability", ["Occupation", "Credit score"], "Pennsylvania Human Relations Commission."),
                   ("Age is protected under the Act:", "At 40 and over", ["At any age", "Only under 18"], "Pennsylvania Human Relations Commission.")]},
        {"h": "Time-shares, planned communities and leases",
         "l": ["The outline also reaches TIME-SHARES, PLANNED COMMUNITIES and CONDOMINIUMS, and RENTALS, LEASING AND PROPERTY MANAGEMENT.",
               "A separate Consumer Notice exists for the LEASE of property where the licensee acts for the OWNER, stating whether the licensee is the owner or landlord, a direct employee of the owner, or an agent under a property management or exclusive leasing agreement (49 Pa. Code 35.337).",
               "A further Consumer Notice applies to TIME-SHARE ESTATES (35.338)."],
         "check": [("The Consumer Notice for a lease on the owner's behalf asks the licensee to state:", "Whether they are the owner, the owner's employee, or an agent under a management or leasing agreement", ["The rent", "The lease term"], "49 Pa. Code 35.337.")]},
    ],
    "traps": [
        "The zoning line goes in EXCEPT for single-family-zoned property - the exception is the tested part.",
        "Pennsylvania protects ancestry, religious creed, age 40+, and guide or support animals.",
        "There is a different Consumer Notice for leases where the licensee acts for the owner.",
    ],
    "vocab": [
        ["Seller Disclosure Law", "Pennsylvania's residential property disclosure statute."],
        ["PHRA", "The Pennsylvania Human Relations Act."],
        ["Planned community", "A development with common areas governed by an association."],
        ["Time-share estate", "An interest giving periodic use; it has its own Consumer Notice."],
    ],
    "examples": [],
}

STUDY["pa/commission"] = {
    "summary": "Five items on the Commission itself and the fund behind it. The Recovery Fund pays where a licensee's fraud, misrepresentation or deceit leaves a judgment nobody can collect.",
    "sections": [
        {"h": "The Commission",
         "l": ["The STATE REAL ESTATE COMMISSION sits within the Bureau of Professional and Occupational Affairs in the Department of State.",
               "It is established by the REAL ESTATE LICENSING AND REGISTRATION ACT (RELRA), 63 P.S. 455.101-455.902, and makes the regulations in 49 Pa. Code chapter 35.",
               "It licenses, investigates complaints, holds hearings and disciplines licensees, and may inspect a broker's office (49 Pa. Code 35.246).",
               "On request or at an inspection, a broker must give the Commission a letter authorising the bank to release the escrow account records."],
         "check": [("The Commission's regulations are found in:", "49 Pa. Code chapter 35", ["63 P.S. 455", "Title 68 of the Consolidated Statutes"], "RELRA is the statute; chapter 35 is the regulations."),
                   ("At an office inspection the broker must provide:", "A letter authorising the bank to release escrow records", ["The broker's personal bank statements", "A list of clients"], "49 Pa. Code 35.325(d).")]},
        {"h": "The Real Estate Recovery Fund",
         "p": ["The Fund reimburses a person who has obtained a FINAL CIVIL JUDGMENT against a Pennsylvania licensee owing to FRAUD, MISREPRESENTATION OR DECEIT in a real estate transaction, and who has been unable to collect it AFTER EXHAUSTING ALL LEGAL AND EQUITABLE REMEDIES."],
         "check": [("A Recovery Fund claim must rest on a judgment for:", "Fraud, misrepresentation or deceit in a real estate transaction", ["Any unpaid debt", "A disputed commission", "Negligent advice"], "As the Consumer Notice states."),
                   ("Before the Fund will pay, the claimant must have:", "Exhausted all legal and equitable remedies to collect", ["Filed a complaint with the Commission", "Waited one year"], "The Consumer Notice sets the condition.")]},
    ],
    "traps": [
        "RELRA is the Act; chapter 35 is the regulations. Questions often swap them.",
        "The Fund covers fraud, misrepresentation or deceit - not every loss.",
        "Collection must be attempted and exhausted first.",
    ],
    "vocab": [
        ["RELRA", "The Real Estate Licensing and Registration Act."],
        ["Recovery Fund", "The fund paying uncollectable judgments for licensee fraud."],
        ["BPOA", "Bureau of Professional and Occupational Affairs, which houses the Commission."],
        ["Office inspection", "The Commission's right to examine a broker's office and records."],
    ],
    "examples": [],
}


# ------------------------------------------------------------- questions

Q = [
 # agency
 ("pa/agency", "Consumer Notice", 1, "The Consumer Notice must be given to a consumer:",
  "At the initial interview", ["At the first showing", "When an offer is prepared", "At settlement"],
  "49 Pa. Code 35.336(a)."),
 ("pa/agency", "Consumer Notice", 2, "The signed or refused acknowledgement of the Consumer Notice is retained for:",
  "Six months", ["Three years", "One year", "Thirty days"],
  "49 Pa. Code 35.336(b)."),
 ("pa/agency", "Consumer Notice", 1, "The Consumer Notice states that it is:",
  "Not a contract", ["A binding listing agreement", "An offer to purchase", "A disclosure of defects"],
  "It is headed 'THIS IS NOT A CONTRACT'."),
 ("pa/agency", "Consumer Notice", 2, "Until a consumer signs a written agreement selecting a relationship, the licensee:",
  "Is not representing them; no relationship is presumed", ["Is their agent by default", "Is automatically a dual agent", "Is a subagent of the seller"],
  "The Consumer Notice says a business relationship is NOT presumed."),
 ("pa/agency", "Relationships", 1, "A buyer agent paid by the seller works exclusively for:",
  "The buyer or tenant", ["The seller, because they pay", "Both parties equally", "The listing broker"],
  "The Consumer Notice states this expressly."),
 ("pa/agency", "Relationships", 1, "A dual agent in Pennsylvania needs:",
  "The written consent of both parties", ["Verbal consent from one", "The broker's approval alone", "Commission approval"],
  "The Consumer Notice."),
 ("pa/agency", "Relationships", 2, "A dual agent may not:",
  "Take any action adverse or detrimental to either party", ["Disclose a known material defect", "Present offers", "Collect a commission"],
  "Material defects must still be disclosed."),
 ("pa/agency", "Relationships", 2, "In designated agency, the broker:",
  "Automatically serves as a dual agent", ["Has no role in the transaction", "Must represent only the seller", "Becomes a transaction licensee"],
  "Because the broker supervises all the licensees."),
 ("pa/agency", "Relationships", 2, "A designated agency broker must additionally:",
  "Take reasonable steps to keep confidential information from being disclosed within the company", ["Pay both sides' fees", "Withdraw from the deal", "Notify the Commission"],
  "The Consumer Notice."),
 ("pa/agency", "Transaction licensee", 1, "A transaction licensee:",
  "Provides services with no agency relationship", ["Represents both parties", "Represents the seller only", "Is prohibited in Pennsylvania"],
  "No duty of loyalty or confidentiality."),
 ("pa/agency", "Transaction licensee", 2, "A transaction licensee is prohibited from disclosing:",
  "That the buyer will pay more than the price in the written offer", ["A known material defect", "The asking price", "The property's square footage"],
  "The three price confidences bind even without agency."),
 ("pa/agency", "Transaction licensee", 2, "A transaction licensee must still:",
  "Disclose known material defects about the property", ["Keep all information confidential", "Act in the buyer's best interest", "Advocate on price"],
  "The Consumer Notice."),
 ("pa/agency", "Subagency", 2, "A subagent in Pennsylvania has:",
  "The same duties and obligations as the seller agent", ["No duties at all", "The duties of a transaction licensee", "Duties to the buyer"],
  "The Consumer Notice."),
 ("pa/agency", "Common duties", 1, "Which duty is owed by EVERY licensee, whatever the relationship?",
  "Dealing honestly and in good faith", ["Loyalty", "Confidentiality", "Advocacy on price"],
  "The Consumer Notice lists the common duties."),
 ("pa/agency", "Common duties", 2, "The duty to present offers as soon as practicable may be waived:",
  "In writing by the seller, once the property is under contract", ["Orally by the buyer", "By the broker", "Never"],
  "The Consumer Notice sets out the one waiver."),
 ("pa/agency", "Common duties", 2, "A licensee recommending a title or inspection service in which they hold a financial interest must disclose it:",
  "When the service is recommended, or when they first learn it will be used", ["At settlement", "Only if asked", "Within 30 days"],
  "The Consumer Notice."),
 ("pa/agency", "Common duties", 3, "Where a matter is beyond the licensee's expertise, the duty is to:",
  "Advise the consumer to seek expert advice", ["Give a best guess", "Decline the engagement", "Refer to the Commission"],
  "The Consumer Notice."),
 ("pa/agency", "Negotiable terms", 2, "Which is expressly negotiable under the Consumer Notice?",
  "The licensee's fees or commission", ["The duty to disclose material defects", "The Consumer Notice itself", "The Seller Disclosure Law"],
  "Duration, fees, scope, and cooperation with other brokers."),
 ("pa/agency", "Negotiable terms", 3, "The broker's cooperation with and sharing of fees with other brokers is:",
  "A negotiable term that must be addressed in the agreement", ["Fixed by the Commission", "Set by the local board", "Prohibited"],
  "The Consumer Notice."),

 # regulations
 ("pa/regulations", "Escrow", 1, "A Pennsylvania escrow account must designate:",
  "The broker as trustee", ["The seller as trustee", "The title company as trustee", "The Commission as trustee"],
  "49 Pa. Code 35.325(a)(2)."),
 ("pa/regulations", "Escrow", 1, "An escrow account must be used:",
  "Exclusively for escrow purposes", ["For escrow and payroll", "For any brokerage purpose", "For the broker's reserves"],
  "49 Pa. Code 35.325(a)(4)."),
 ("pa/regulations", "Escrow", 2, "An escrow account must provide for:",
  "Withdrawal of funds without prior notice", ["A 30-day notice period", "Joint signatures of both parties", "Quarterly withdrawals only"],
  "49 Pa. Code 35.325(a)(3)."),
 ("pa/regulations", "Escrow", 2, "Interest earned on a Pennsylvania escrow account:",
  "Is disbursed pro rata like the principal, and the broker may not claim it", ["Belongs to the broker", "Goes to the Commission", "Is always paid to the buyer"],
  "49 Pa. Code 35.325(c), with the lessor exception."),
 ("pa/regulations", "Escrow", 2, "Where escrow money will be held more than six months, the broker is:",
  "Encouraged to deposit it in an interest-bearing account", ["Required to use a non-interest account", "Required to return it", "Required to notify the Commission"],
  "49 Pa. Code 35.325(c)."),
 ("pa/regulations", "Escrow", 3, "Who may be given written authority to withdraw from the escrow account?",
  "A licensed employee, for payments properly chargeable to the account", ["Any employee", "The seller", "Nobody but the broker"],
  "49 Pa. Code 35.325(b)."),
 ("pa/regulations", "Escrow", 1, "Rents a broker receives as a property manager:",
  "Go into a separate rental management account", ["Must be held in escrow", "Go into the general business account", "May be kept by the broker"],
  "49 Pa. Code 35.321(b)."),
 ("pa/regulations", "Escrow", 2, "In a corporate brokerage, responsibility for performing the escrow duty rests with:",
  "The broker of record", ["Each salesperson", "The corporation's accountant", "The Commission"],
  "49 Pa. Code 35.321(a)."),
 ("pa/regulations", "Commingling", 1, "A broker may deposit personal funds into escrow only to:",
  "Cover bank service charges or maintain a required minimum balance", ["Round a deposit up", "Lend to a client", "Cover a shortfall"],
  "49 Pa. Code 35.326(b)."),
 ("pa/regulations", "Commingling", 2, "Using escrow money for the broker's own purposes is:",
  "Misappropriation, and prohibited", ["Permitted if repaid", "Permitted up to $200", "Permitted with the client's consent"],
  "49 Pa. Code 35.326(c)."),
 ("pa/regulations", "Disputes", 1, "When the parties dispute entitlement to escrowed money, the broker must first:",
  "Retain the money in escrow until the dispute is resolved", ["Split it evenly", "Pay the seller", "Return it to the buyer"],
  "49 Pa. Code 35.327."),
 ("pa/regulations", "Disputes", 2, "Before petitioning the county court to interplead rival claimants, the broker must give the parties:",
  "30 days' notice", ["10 days' notice", "60 days' notice", "No notice"],
  "49 Pa. Code 35.327."),
 ("pa/regulations", "Records", 1, "Pennsylvania transaction records must be kept for:",
  "At least three years following consummation", ["Six months", "One year", "Seven years"],
  "49 Pa. Code 35.286(a)."),
 ("pa/regulations", "Records", 2, "A Consumer Notice acknowledgement where no transaction followed is kept for:",
  "Six months", ["Three years", "One year", "Indefinitely"],
  "49 Pa. Code 35.286(a)(1)."),
 ("pa/regulations", "Records", 3, "Escrow records must identify:",
  "The party the money came from, the party it belongs to, and the account it is held for", ["Only the amount and date", "Only the buyer", "The broker's commission"],
  "49 Pa. Code 35.328."),

 # licensure
 ("pa/licensure", "Qualifying", 1, "The minimum age for a Pennsylvania salesperson licence is:",
  "18", ["17", "19", "21"],
  "Pearson handbook; RELRA."),
 ("pa/licensure", "Qualifying", 1, "A Pennsylvania salesperson applicant must be at least:",
  "A high school graduate or the equivalent", ["A college graduate", "A trade school graduate", "Able to show five years' work history"],
  "Pearson handbook."),
 ("pa/licensure", "Education", 1, "Pre-licensing education for a Pennsylvania salesperson is:",
  "5 credits or 75 hours of basic real estate courses", ["30 hours", "60 hours", "120 hours"],
  "Through a Commission-approved provider or an accredited college."),
 ("pa/licensure", "Education", 2, "Pre-licensing courses must have been completed within:",
  "Five years before passing the examination", ["One year", "Three years", "Ten years"],
  "Pearson handbook."),
 ("pa/licensure", "Examination", 2, "Pennsylvania examination scores are valid for:",
  "Three years", ["One year", "Five years", "Indefinitely"],
  "The licence application must be filed within that period."),
 ("pa/licensure", "Continuing education", 1, "Continuing education in Pennsylvania is:",
  "14 hours per licence period", ["30 hours", "22.5 hours", "8 hours"],
  "49 Pa. Code 35.382(a)."),
 ("pa/licensure", "Continuing education", 1, "The Pennsylvania continuing education deadline is:",
  "May 31", ["December 31", "June 30", "The licensee's birthday"],
  "49 Pa. Code 35.382(a)."),
 ("pa/licensure", "Continuing education", 2, "Completing the continuing education is:",
  "A condition precedent to renewal", ["Optional for a first renewal", "Required only of brokers", "Waived for inactive licensees"],
  "49 Pa. Code 35.382(a)."),
 ("pa/licensure", "Reactivation", 3, "To reactivate and renew a noncurrent standard licence, the 14 hours must be completed:",
  "In the two-year period before the reactivation application", ["At any time in the past", "After reactivation", "Within 30 days of applying"],
  "49 Pa. Code 35.382(b)."),
 ("pa/licensure", "Reactivation", 3, "A licensee reactivating a licence:",
  "May not use the same continuing education course twice", ["May reuse previous courses", "Is exempt from education", "Must retake the examination"],
  "49 Pa. Code 35.382(b)."),

 # miscellaneous
 ("pa/misc", "Zoning", 2, "A Pennsylvania sales agreement must state the property's zoning classification:",
  "Unless the property is zoned solely or primarily for single family dwellings", ["Always, without exception", "Only for commercial property", "Only if the buyer asks"],
  "The Consumer Notice sets out the rule."),
 ("pa/misc", "Seller disclosure", 1, "Complying with the Real Estate Seller Disclosure Law is:",
  "A duty every licensee owes, whatever the relationship", ["Only the seller agent's duty", "Optional in an as-is sale", "The buyer's responsibility"],
  "It is in the Consumer Notice's common duty list."),
 ("pa/misc", "Fair housing", 1, "Which is protected under the Pennsylvania Human Relations Act but not the federal Fair Housing Act?",
  "Ancestry", ["Race", "Colour", "National origin"],
  "Pennsylvania also adds religious creed, age and the guide-animal class."),
 ("pa/misc", "Fair housing", 2, "Age is protected under the Pennsylvania Human Relations Act:",
  "At 40 and over", ["At any age", "Only for those under 18", "Only in employment"],
  "Pennsylvania Human Relations Commission."),
 ("pa/misc", "Fair housing", 2, "Pennsylvania's protected classes include:",
  "The use, handling or training of a support or guide animal for a disability", ["Occupation", "Credit score", "Length of residence"],
  "Pennsylvania Human Relations Commission."),
 ("pa/misc", "Leases", 2, "The Consumer Notice for a lease where the licensee acts for the owner asks the licensee to state:",
  "Whether they are the owner, the owner's direct employee, or an agent under a management or leasing agreement", ["The rent and term", "The tenant's credit score", "The commission"],
  "49 Pa. Code 35.337."),

 # commission
 ("pa/commission", "Structure", 1, "The Pennsylvania Commission's regulations are found in:",
  "49 Pa. Code chapter 35", ["63 P.S. 455", "Title 68 of the Consolidated Statutes", "The Pennsylvania Bulletin only"],
  "RELRA is the statute; chapter 35 holds the regulations."),
 ("pa/commission", "Structure", 2, "The Real Estate Licensing and Registration Act is cited as:",
  "63 P.S. 455.101-455.902", ["49 Pa. Code 35", "68 Pa.C.S. 3101", "43 P.S. 955"],
  "The Commission's regulations are made under it."),
 ("pa/commission", "Powers", 2, "At an office inspection, a broker must provide the Commission with:",
  "A letter authorising the bank to release the escrow account records", ["The broker's personal bank statements", "A list of all clients", "Copies of every listing"],
  "49 Pa. Code 35.325(d)."),
 ("pa/commission", "Recovery Fund", 1, "A Recovery Fund claim must rest on a final civil judgment for:",
  "Fraud, misrepresentation or deceit in a real estate transaction", ["Any unpaid debt", "A disputed commission", "Negligent advice"],
  "As stated in the Consumer Notice."),
 ("pa/commission", "Recovery Fund", 2, "Before the Recovery Fund will pay, the claimant must have:",
  "Exhausted all legal and equitable remedies to collect the judgment", ["Filed a Commission complaint", "Waited twelve months", "Obtained the licensee's consent"],
  "As stated in the Consumer Notice."),

 # --- commission, further
 ("pa/commission", "Structure", 2, "The State Real Estate Commission sits within:",
  "The Bureau of Professional and Occupational Affairs, Department of State", ["The Attorney General's office", "The Department of Revenue", "The Treasury"],
  "RELRA establishes it there."),
 ("pa/commission", "Powers", 2, "The Commission may inspect:",
  "A broker's office and its records", ["Only records sent voluntarily", "Nothing without a court order", "Only escrow statements"],
  "49 Pa. Code 35.246."),
 ("pa/commission", "Powers", 3, "Escrow records must be produced to the Commission:",
  "On written request or at an office inspection", ["Only at renewal", "Only under subpoena", "Annually"],
  "49 Pa. Code 35.328."),
 ("pa/commission", "Recovery Fund", 3, "The Recovery Fund reimburses a person who:",
  "Could not collect a final civil judgment against a licensee", ["Lost money on a property's value", "Disagrees with a commission", "Was refused a listing"],
  "The Consumer Notice."),

 # --- miscellaneous, further
 ("pa/misc", "Fair housing", 2, "Religious creed is:",
  "A protected class under the Pennsylvania Human Relations Act", ["Not protected in Pennsylvania", "Protected only in employment", "Protected only in public accommodation"],
  "Pennsylvania Human Relations Commission."),
 ("pa/misc", "Fair housing", 2, "Familial status is protected under the Pennsylvania Act:",
  "In housing", ["In employment only", "Nowhere", "In public accommodation only"],
  "Pennsylvania Human Relations Commission."),
 ("pa/misc", "Fair housing", 3, "Retaliation against someone who asserts their rights is:",
  "Itself prohibited under the Act", ["Permitted if the claim failed", "Only a federal matter", "Outside the Commission's reach"],
  "Pennsylvania Human Relations Commission."),
 ("pa/misc", "Time-shares", 2, "Time-share estates in Pennsylvania:",
  "Have their own Consumer Notice", ["Need no disclosure", "Use the sales Consumer Notice", "Are not regulated"],
  "49 Pa. Code 35.338."),
 ("pa/misc", "Documents", 3, "The acknowledgement portion of a time-share Consumer Notice is retained for:",
  "Six months", ["Three years", "One year", "Indefinitely"],
  "49 Pa. Code 35.286(a)(2)."),

 # --- licensure, further
 ("pa/licensure", "Qualifying", 2, "An alternative to the 75 hours is:",
  "A bachelor's degree with a major in real estate from an accredited college", ["Five years in construction", "A mortgage licence", "A paralegal certificate"],
  "Pearson handbook."),
 ("pa/licensure", "Qualifying", 3, "Pennsylvania also licenses:",
  "Rental listing referral agents", ["Property inspectors", "Mortgage brokers", "Appraisal trainees under this Act"],
  "A separate category under RELRA; 49 Pa. Code 35.227."),
 ("pa/licensure", "Examination", 3, "A candidate who passes one portion of the Pennsylvania examination:",
  "May not retake a previously passed portion", ["Must retake both", "Must wait a year", "Loses the result after 30 days"],
  "Pearson handbook."),
 ("pa/licensure", "Scores", 3, "Pennsylvania reports a numeric examination score:",
  "Only to failing candidates", ["To every candidate", "Only on request", "Never"],
  "Pearson handbook; passing candidates are told only that they passed."),
 ("pa/licensure", "Scores", 2, "Pennsylvania converts raw scores into:",
  "A scaled score ranging from 0 to 100", ["A percentage of items correct", "A letter grade", "A percentile rank"],
  "And the handbook says the scaled score is NOT the percentage correct."),

 # --- regulations, further
 ("pa/regulations", "Escrow", 2, "An escrow account must be held in:",
  "A federally- or state-insured bank or recognised depository", ["Any account the broker chooses", "A brokerage investment account", "An out-of-state trust"],
  "49 Pa. Code 35.325(a)(1)."),
 ("pa/regulations", "Escrow", 3, "A broker acting as a lessor may claim escrow interest:",
  "Only as provided by section 511.2 of the Landlord and Tenant Act", ["Always", "Never", "With the tenant's consent"],
  "49 Pa. Code 35.325(c)."),
 ("pa/regulations", "Escrow", 2, "Money belonging to another is held in escrow:",
  "Pending consummation, or a prior termination not involving a dispute", ["Until the listing expires", "For a fixed 90 days", "Until the broker is paid"],
  "49 Pa. Code 35.321(a)."),
 ("pa/regulations", "Escrow", 3, "On consummation or an undisputed termination, the broker pays:",
  "The full amount to the party entitled to receive it", ["The amount less the commission", "Half to each party", "The amount the seller directs"],
  "49 Pa. Code 35.321(a)."),
 ("pa/regulations", "Commingling", 2, "Commingling under the Commission's rules covers:",
  "Escrow money and the interest earned on it", ["Escrow principal only", "Only amounts over $1,000", "Only personal funds"],
  "49 Pa. Code 35.326(a)."),
 ("pa/regulations", "Records", 3, "Escrow records must be produced:",
  "For examination by the Commission on written request or at an office inspection", ["Only to the parties", "Only under court order", "Only at renewal"],
  "49 Pa. Code 35.328."),
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
            "id": "pa-" + hashlib.sha1(q.encode()).hexdigest()[:8],
            "portion": "georgia", "topic": topic, "subtopic": sub,
            "sub": topic + "|" + sub, "concept": "Pennsylvania " + sub.lower(),
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
        "code": "PA", "name": "Pennsylvania", "abbr": "PA",
        "regulator": "PA State Real Estate Commission",
        "pass": EXAM["pass"],
        "pass_published": False,
        "pass_note": PASS_NOTE,
        "portions": {
            "national": {"scored": EXAM["national_scored"],
                         "minutes": EXAM["national_minutes"]},
            "georgia": {"name": "Pennsylvania state", "scored": EXAM["state_scored"],
                        "minutes": EXAM["state_minutes"],
                        "blurb": "RELRA, the Commission's regulations, the Consumer Notice and escrow."},
        },
        "topics": topics, "bank": bank, "study": study,
        "sources": SOURCES, "diffs": DIFFS,
    }


# Where Pennsylvania departs from the national rule.
DIFFS = {
    "national/agency": [
        "Pennsylvania presumes NO relationship. The Consumer Notice at the initial interview tells the consumer that until they sign a written agreement, the licensee does not represent them (49 Pa. Code 35.336).",
        "Five business relationships: seller agent (and subagent), buyer agent, dual agent, designated agent, and TRANSACTION LICENSEE - who is not an agent at all but still may not reveal price confidences.",
        "In designated agency the supervising BROKER automatically becomes a dual agent.",
    ],
    "national/practice": [
        "The escrow account names the broker as TRUSTEE, allows withdrawal without prior notice, and is used exclusively for escrow (49 Pa. Code 35.325).",
        "Rents taken as a property manager are NOT escrow: they go to a separate rental management account (35.321(b)).",
        "On a dispute the broker holds the money, gives 30 days' notice, then may petition the county court to interplead (35.327).",
        "Pennsylvania fair housing adds ancestry, religious creed, age 40 and over, and the use or training of a support or guide animal (Human Relations Act).",
    ],
    "national/contracts": [
        "All sales agreements must state the property's zoning classification, except where it is zoned solely or primarily for single family dwellings.",
    ],
}


if __name__ == "__main__":
    import io, json, os
    here = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    out = os.path.join(here, "greprep", "packs", "PA.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    pack = build()
    with io.open(out, "w", encoding="utf-8") as f:
        json.dump(pack, f, ensure_ascii=False, indent=1, sort_keys=True)
    print("wrote", out, len(pack["bank"]), "questions,", len(pack["study"]), "lessons")
