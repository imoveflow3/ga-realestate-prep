"""Michigan state content: lessons and practice questions.

Michigan writes ONE paper. The PSI bulletin's examination summary table
gives the salesperson examination as 115 questions, 180 minutes, a passing
percentage of 70 and a passing raw score of 80. The Michigan-specific
portion of the content outline carries 35 of those items, which is what
the state topics below add up to; the other 80 are the national areas.

Passing numeric scores are not reported to candidates - the bulletin says
a candidate who passes receives only an indication of PASS - but the mark
itself is published, so the pack states it.

Every rule below was read from the official text on 2026-11-09:
  - Occupational Code, 1980 PA 299, article 25 (MCL 339.2501 to 339.2518),
    the real estate licence law, from legislature.mi.gov.
  - Elliott-Larsen Civil Rights Act, 1976 PA 453 (MCL 37.2102, 37.2502).
  - Seller Disclosure Act, 1993 PA 92 (MCL 565.952 to 565.957).
  - Land Division Act, 1967 PA 288 (MCL 560.109, 560.261).
  - State Real Estate Transfer Tax Act, 1993 PA 330 (MCL 207.523, 207.525).
  - Security deposit act, 1972 PA 348; Truth in Renting Act, 1978 PA 454;
    Condominium Act, 1978 PA 59; Michigan Antitrust Reform Act, 1984 PA 274.
  - The PSI Michigan Candidate Information Bulletin for LARA, for the
    examination table and the Michigan content outline.
The section a fact comes from is cited next to it. Do not add a fact here
without reading its source first.
"""

EXAM = {
    # One paper: 115 questions, 180 minutes, 70% (raw 80).
    "state_scored": 35,
    "state_minutes": 55,
    "national_scored": 80,
    "national_minutes": 125,
    "pass": 0.70,
}

# PSI's Michigan-specific outline, salesperson item counts: 3+5+10+5+12 = 35.
TOPICS = [
    ("mi/activities", "Statutory requirements on licensees", 10,
     "Advertising, trust money, records, inducements, stigmatized property."),
    ("mi/additional", "Additional Michigan topics", 12,
     "Fair housing, land division, transfer tax, condos, landlord-tenant."),
    ("mi/licensing", "Licensing requirements", 5,
     "Who needs a licence, education, renewal, transfer, offices."),
    ("mi/agency", "Contractual relationships", 5,
     "Agency disclosure, designated agency, transaction coordinator, waivers."),
    ("mi/department", "Department and Board", 3,
     "Who regulates, how they investigate, and what the penalties are."),
]

SOURCES = [
    {"by": "Michigan Legislature",
     "name": "Occupational Code article 25 (MCL 339.2501 to 339.2518)",
     "note": "The licence law: definitions, education, trust money, advertising, agency disclosure, prohibited conduct.",
     "url": "https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-299-1980-25"},
    {"by": "Michigan Legislature",
     "name": "Elliott-Larsen Civil Rights Act (MCL 37.2102, 37.2502)",
     "note": "Michigan's own protected classes, which include several the federal Act leaves out.",
     "url": "https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-37-2502"},
    {"by": "Michigan Legislature",
     "name": "Seller Disclosure Act (1993 PA 92) and Land Division Act (1967 PA 288)",
     "note": "The seller's disclosure statement and its timing, and the private road notice.",
     "url": "https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-565-954"},
    {"by": "PSI Services and Michigan LARA",
     "name": "Michigan Real Estate Candidate Information Bulletin",
     "note": "One 115-question paper, 180 minutes, 70% to pass, and the 35-item Michigan outline.",
     "url": "https://test-takers.psiexams.com/mire"},
]


# --------------------------------------------------------------- lessons

STUDY = {}

STUDY["mi/activities"] = {
    "summary": "Ten items, the biggest state category. The money rules and the advertising rules carry most of the marks, and Michigan has a statute saying what you DON'T have to disclose.",
    "sections": [
        {"h": "Trust money (MCL 339.2512(k))",
         "l": ["A salesperson who receives a deposit must pay or deliver it to the EMPLOYING BROKER ON RECEIPT.",
               "The broker deposits money belonging to others into a separate CUSTODIAL TRUST OR ESCROW ACCOUNT not later than 2 BANKING DAYS after the broker receives notice that an offer to purchase is ACCEPTED BY ALL PARTIES, and holds it until the transaction is consummated or terminated, then accounts for the full amount.",
               "If the purchase agreement names an escrowee other than the broker, a licensee holding the deposit delivers it to that escrowee within the same 2 BANKING DAYS.",
               "NO COMMINGLING: the broker may not put advance payments belonging to others into a business or personal account.",
               "A broker may keep more than one trust account, and may deposit NOT MORE THAN $2,000.00 of its own money in each one to cover bank service charges and minimum balances - and must account for that money in the records.",
               "The account designates the broker as TRUSTEE and must allow withdrawal without previous notice. Records show the date, from whom, the date deposited, the date of withdrawal, for whose account, and to whom the money belongs. They are open to department inspection."],
         "check": [("A Michigan broker deposits accepted-offer money into the trust account within:", "2 banking days after notice that all parties accepted", ["5 business days", "24 hours", "At closing"], "MCL 339.2512(k)(v)."),
                   ("A salesperson who takes a deposit must:", "Pay or deliver it to the employing broker on receipt", ["Deposit it personally", "Hold it until closing", "Give it to the seller"], "MCL 339.2512(k)(ii)."),
                   ("How much of its own money may a broker keep in each trust account?", "Not more than $2,000.00", ["Nothing at all", "$100", "Any amount"], "MCL 339.2512(k)(iv)."),
                   ("The trust account must allow:", "Withdrawal of funds without previous notice", ["90 days' notice", "Only the seller to withdraw"], "MCL 339.2512(k)(vi).")]},
        {"h": "Advertising (MCL 339.2512e)",
         "l": ["A BROKER'S advertisement must include the broker's name or business name, the broker's telephone number OR street address, and must STATE THAT THE ADVERTISER IS A REAL ESTATE BROKER.",
               "A SALESPERSON or associate broker advertises only under the supervision of, and IN THE BUSINESS NAME OF, the employing broker. Advertising naming the salesperson must carry the employing broker's telephone number or street address and the broker's BUSINESS NAME IN EQUAL OR GREATER TYPE SIZE than the salesperson's name.",
               "A salesperson may not advertise property for sale under their own name UNLESS it is their PRINCIPAL RESIDENCE, and may not advertise property for rent under their own name unless they OWN it.",
               "A broker may not advertise under any name other than the one the licence was issued in, or a lawfully authorised assumed name, and must notify the department of an assumed name with the application or WITHIN 30 DAYS of adopting it."],
         "check": [("In advertising that names a salesperson, the employing broker's business name must be:", "In equal or greater type size than the salesperson's name", ["Anywhere on the advertisement", "In smaller type", "Optional"], "MCL 339.2512e(3)(b)."),
                   ("A salesperson may advertise a property for sale in their own name only if:", "It is the salesperson's principal residence", ["The broker agrees", "It is a rental", "It is listed with another firm"], "MCL 339.2512e(4)."),
                   ("A broker adopting an assumed name must notify the department:", "With the licence application, or within 30 days of adopting it", ["At renewal", "Within one year", "Never"], "MCL 339.2512e(5)."),
                   ("A broker's advertisement must state:", "That the advertiser is a real estate broker", ["The commission rate", "The seller's name"], "MCL 339.2512e(1).")]},
        {"h": "No duty to disclose: stigma (MCL 339.2518)",
         "p": ["Michigan bars an ACTION against a licensee for failing to disclose three things:"],
         "l": ["That a FORMER OCCUPANT has or is suspected of having a DISABILITY - because disclosing it would be unlawful discrimination under the federal Fair Housing Act.",
               "That the property was or was suspected to have been the site of a HOMICIDE, SUICIDE OR OTHER OCCURRENCE PROHIBITED BY LAW which had NO MATERIAL EFFECT on the condition of the property.",
               "Any information from the SEX OFFENDERS REGISTRATION ACT compilation that is made available to the public."],
         "check": [("A Michigan licensee may be sued for failing to disclose:", "None of these: a former occupant's disability, a homicide with no effect on condition, or registry information", ["All three", "Only the homicide", "Only the registry"], "MCL 339.2518."),
                   ("Why does the statute bar a claim over a former occupant's disability?", "Disclosing it would be unlawful discrimination under the federal Fair Housing Act", ["It is confidential medical data", "The seller owns the information"], "MCL 339.2518(a)."),
                   ("The homicide exemption applies where the event had:", "No material effect on the condition of the property", ["Any effect at all", "Occurred over ten years ago"], "MCL 339.2518(b).")]},
        {"h": "Inducements, fee sharing and the rest",
         "l": ["A licensee may not SHARE OR PAY a fee, commission or other valuable consideration to a person NOT LICENSED under article 25 - including paying anyone for the name of a potential seller or buyer. Buying a COMMERCIALLY PREPARED LIST of names is excluded, and a broker may pay a commission to an out-of-state broker who did no negotiating in Michigan.",
               "Acting for MORE THAN ONE PARTY in a transaction without the knowledge of the parties is prohibited (property management aside).",
               "A licensee who does not ACCOUNT FOR or REMIT money belonging to others is subject to penalty, as is one who changes business location WITHOUT NOTIFYING THE DEPARTMENT.",
               "A broker must DELIVER OR MAIL a discharged salesperson's licence to the department WITHIN 5 DAYS, and tell the salesperson in writing that it did so (MCL 339.2507).",
               "An unlicensed person cannot MAINTAIN AN ACTION IN COURT for a commission: they must allege and prove they were licensed at the time (MCL 339.2512a).",
               "PROPERTY MANAGEMENT money goes in accounts kept SEPARATE from all other accounts, under a written property management employment contract (MCL 339.2512c).",
               "A complaint seeking a penalty must be filed NOT LATER THAN 18 MONTHS after the violation or, for a transaction, after it was completed."],
         "check": [("Paying an unlicensed person for the name of a potential buyer is:", "Prohibited", ["Allowed if under $100", "Allowed with a written receipt"], "MCL 339.2512(h)."),
                   ("A broker must return a discharged salesperson's licence to the department within:", "5 days", ["30 days", "10 business days"], "MCL 339.2507(1); 339.2512(f)."),
                   ("An unlicensed person suing for a commission:", "Cannot maintain the action; they must allege and prove they were licensed", ["May sue in small claims", "May recover half"], "MCL 339.2512a."),
                   ("A complaint seeking a penalty must be filed within:", "18 months", ["6 months", "3 years", "No limit"], "MCL 339.2512(2)."),
                   ("Property management money must be:", "Kept in accounts separate from all other accounts", ["Mixed with the trust account", "Held by the owner"], "MCL 339.2512c(2).")]},
    ],
    "traps": [
        "2 banking days, counted from notice that ALL PARTIES accepted - not from the offer.",
        "$2,000 of the broker's own money per trust account is allowed, not zero.",
        "Michigan's stigma statute is a shield, not a duty: no action lies for not disclosing.",
        "A salesperson's own-name advertising is limited to their principal residence (sale) or property they own (rent).",
    ],
    "vocab": [
        ["Custodial trust account", "The separate account holding others' money, broker as trustee."],
        ["Commingling", "Mixing clients' money with the broker's own. Prohibited."],
        ["Inducement", "Paying for a referral or a name. Unlicensed payees are barred."],
        ["Banking day", "A day the bank is open; the deposit clock is counted in these."],
        ["Assumed name", "A business name other than the licensed one; 30-day notice."],
    ],
    "examples": [
        {"t": "Deposit timing",
         "s": "A salesperson takes a $5,000 deposit Friday. All parties sign Monday, and the broker hears Monday afternoon.",
         "w": ["The salesperson delivers the cheque to the broker ON RECEIPT, Friday.",
               "The broker's 2-banking-day clock starts Monday, when it learns all parties accepted.",
               "So the deposit must be in the trust account by Wednesday."],
         "k": "Delivery is immediate; the deposit clock runs from acceptance by all parties."},
    ],
}

STUDY["mi/additional"] = {
    "summary": "Twelve items spread over eight Michigan statutes. The fair housing list and the transfer tax number are the reliable marks.",
    "sections": [
        {"h": "Elliott-Larsen Civil Rights Act (MCL 37.2502)",
         "p": ["In a real estate transaction, a person, broker or salesperson may not refuse to deal, discriminate in terms or conditions, refuse to transmit a bona fide offer, refuse to negotiate, misrepresent availability, advertise a preference, take a discriminatory listing, or discriminate in brokering or appraising, on the basis of:"],
         "l": ["RELIGION", "RACE", "COLOR", "NATIONAL ORIGIN", "AGE", "SEX",
               "SEXUAL ORIENTATION", "GENDER IDENTITY OR EXPRESSION",
               "FAMILIAL STATUS", "MARITAL STATUS",
               "- of the individual OR OF ANYONE RESIDING WITH THEM.",
               "The Act's declaration of civil right in MCL 37.2102 also names HEIGHT and WEIGHT.",
               "DISABILITY is covered by a separate statute, the PERSONS WITH DISABILITIES CIVIL RIGHTS ACT, 1976 PA 220.",
               "SOURCE OF INCOME: a landlord may not deny a tenancy, discriminate on price or terms, or exclude a rent voucher or subsidy when applying an income threshold. This subsection does NOT apply to a landlord of FEWER THAN 5 rental units in Michigan."],
         "check": [("Which is protected in a Michigan real estate transaction but not by the federal Fair Housing Act?", "Marital status", ["Race", "Religion", "Color"], "MCL 37.2502(1)."),
                   ("Elliott-Larsen also protects:", "Age and gender identity or expression", ["Credit score", "Occupation"], "MCL 37.2502(1)."),
                   ("Disability in Michigan housing is covered by:", "The Persons with Disabilities Civil Rights Act, 1976 PA 220", ["Elliott-Larsen alone", "The Occupational Code"], "Elliott-Larsen's housing list does not name disability."),
                   ("The source-of-income rule does not apply to a landlord of:", "Fewer than 5 rental units in Michigan", ["Fewer than 20 units", "Any single-family home"], "MCL 37.2502(4)."),
                   ("Elliott-Larsen protects a person against discrimination based on the characteristics of:", "The individual or anyone residing with them", ["Only the applicant", "Only the owner"], "MCL 37.2502(1).")]},
        {"h": "The seller's disclosure statement (1993 PA 92)",
         "l": ["It applies to a transfer of any interest in real estate of NOT LESS THAN 1 AND NOT MORE THAN 4 RESIDENTIAL DWELLING UNITS, by sale, exchange, installment land contract, lease with an option to purchase, other option, or a residential co-operative interest (MCL 565.952).",
               "The seller delivers it BEFORE THE SELLER EXECUTES A BINDING PURCHASE AGREEMENT. If it goes to the seller's agent, that agent gives a copy to the buyer or the buyer's agent; delivery to the buyer's agent counts as delivery to the buyer (MCL 565.954).",
               "If the statement or an amendment arrives AFTER the seller signed a binding purchase agreement, the buyer may TERMINATE by written notice within 72 HOURS of in-person delivery, or 120 HOURS if delivered by registered mail. That right EXPIRES on transfer by deed or installment sales contract.",
               "The form is NOT A WARRANTY and the seller answers from KNOWLEDGE, using UNKNOWN or NOT AVAILABLE where they do not know. Failure to give a signed statement lets the purchaser terminate an otherwise binding agreement.",
               "The form's 'Other Items' include a FARM OR FARM OPERATION IN THE VICINITY, shared features such as roads and driveways, encroachments and easements, work done without permits, and pending litigation. It also tells buyers the SEX OFFENDER REGISTRY compilation is public and to contact local law enforcement."],
         "check": [("The Michigan seller's disclosure statement covers property of:", "Not less than 1 and not more than 4 residential dwelling units", ["Any property", "Commercial property only"], "MCL 565.952."),
                   ("A disclosure statement delivered in person after the agreement was signed gives the buyer:", "72 hours to terminate in writing", ["24 hours", "10 days", "No right"], "MCL 565.954(3)(a)."),
                   ("Delivered by registered mail instead, the period is:", "120 hours", ["72 hours", "5 days"], "MCL 565.954(3)(b)."),
                   ("The buyer's right to terminate expires:", "On transfer of the property by deed or installment sales contract", ["At closing of escrow", "After 30 days"], "MCL 565.954(4)."),
                   ("The disclosure statement is:", "A disclosure from the seller's knowledge, not a warranty", ["A warranty of condition", "An inspection report"], "MCL 565.957.")]},
        {"h": "Land Division Act (1967 PA 288)",
         "l": ["PRIVATE ROAD NOTICE: no one may sell a lot in a recorded plat, or a parcel of unplatted land in an UNINCORPORATED AREA, that abuts a street or road NOT ACCEPTED AS PUBLIC, unless the seller first tells the buyer IN WRITING ON A SEPARATE INSTRUMENT ATTACHED TO THE CONVEYANCE that the road is private and IS NOT REQUIRED TO BE MAINTAINED BY THE BOARD OF COUNTY ROAD COMMISSIONERS. A contract made in violation is VOIDABLE AT THE PURCHASER'S OPTION (MCL 560.261).",
               "1996 PA 591 added MCL 560.109: a municipality approves or disapproves a proposed division within 45 DAYS of a complete application, and each resulting parcel must be ACCESSIBLE and meet the depth-to-width and area rules.",
               "A deed for unplatted land must state how many divisions the grantor conveys ('zero', a number, or 'all'); with no conforming statement, the division rights STAY WITH THE REMAINDER retained by the grantor (MCL 560.109(3)).",
               "Every deed for unplatted land executed after MARCH 31, 1997 must carry the RIGHT TO FARM statement: the property may be near farm land, and generally accepted agricultural practices generating noise, dust and odours are protected by the Michigan Right to Farm Act (MCL 560.109(4))."],
         "check": [("A sale of a parcel abutting a road not accepted as public requires:", "A separate written instrument attached to the conveyance saying the road is private", ["A note in the listing", "An oral warning", "Nothing"], "MCL 560.261."),
                   ("A sale made without that private road notice is:", "Voidable at the purchaser's option", ["Void from the start", "Fully valid", "A felony"], "MCL 560.261."),
                   ("Deeds for unplatted land after 31 March 1997 must carry:", "The Michigan Right to Farm Act statement", ["A flood notice", "A mineral rights waiver"], "MCL 560.109(4)."),
                   ("If a deed for unplatted land says nothing about division rights:", "They stay with the remainder the grantor retained", ["They pass to the grantee", "They are lost"], "MCL 560.109(3)."),
                   ("A municipality must act on a complete division application within:", "45 days", ["30 days", "90 days"], "MCL 560.109(1).")]},
        {"h": "State real estate transfer tax (1993 PA 330)",
         "l": ["The state tax is $3.75 FOR EACH $500.00 or fraction of $500.00 of the total value of the property transferred (MCL 207.525).",
               "The SELLER OR GRANTOR is liable for it (MCL 207.523(2)).",
               "It is paid to the COUNTY TREASURER where the property is located NOT LATER THAN 15 DAYS after delivery of the instrument.",
               "The instrument must state the total value on its face, or carry an affidavit declaring it. Where real and personal property are sold together, the tax falls only on the real property if the values are stated separately."],
         "check": [("The Michigan state transfer tax rate is:", "$3.75 per $500 or fraction of $500 of value", ["$1.10 per $1,000", "0.75% of value"], "MCL 207.525(1)."),
                   ("Who is liable for the state transfer tax?", "The seller or grantor", ["The buyer", "The lender", "The broker"], "MCL 207.523(2)."),
                   ("It is paid to the county treasurer within:", "15 days after delivery of the instrument", ["30 days", "At recording only"], "MCL 207.523(3)."),
                   ("On a sale of real and personal property together, the tax applies to:", "Only the real property, if the values are stated separately", ["The whole price always", "Only the personal property"], "MCL 207.525(2).")]},
        {"h": "Condominium Act (1978 PA 59)",
         "l": ["A signed purchase agreement for a residential condominium unit DOES NOT BIND the purchaser, who may WITHDRAW without cause and without penalty before conveyance and WITHIN 9 BUSINESS DAYS after receiving the section 84a documents - counting the day of receipt if it is a business day (MCL 559.184(2)).",
               "The developer must hold all funds in ESCROW and return them within 3 BUSINESS DAYS after a withdrawal.",
               "The section 84a documents are the RECORDED MASTER DEED, a signable purchase agreement with the escrow agreement, a CONDOMINIUM BUYER'S HANDBOOK, and a DISCLOSURE STATEMENT with the first-year projected budget and the developers' experience.",
               "The purchase agreement must offer BINDING ARBITRATION, at the purchaser's exclusive option, for a claim under $2,500.00.",
               "The right of withdrawal may be waived only in exceptional cases, by a purchaser given all the documents who waives it KNOWINGLY AND VOLUNTARILY IN WRITING."],
         "check": [("A Michigan condominium purchaser may withdraw within:", "9 business days after receiving the required documents", ["3 days", "15 days", "72 hours"], "MCL 559.184(2)."),
                   ("Withdrawn funds must be returned within:", "3 business days", ["30 days", "At closing"], "MCL 559.184(4)(a)."),
                   ("The purchase agreement must offer binding arbitration for claims under:", "$2,500.00", ["$10,000", "$500"], "MCL 559.184(4)(d)."),
                   ("The withdrawal right may be waived:", "Only in exceptional cases, knowingly and voluntarily in writing", ["By initialling the agreement", "Never"], "MCL 559.184(5).")]},
        {"h": "Landlord and tenant",
         "l": ["SECURITY DEPOSIT: it may not exceed 1 1/2 MONTHS' RENT (MCL 554.602).",
               "Within 14 DAYS of the tenant taking possession the landlord must give written notice of its name and address, the financial institution or surety, and the tenant's duty to give a forwarding address WITHIN 4 DAYS of moving out - in 12 POINT BOLDFACE at least 4 points larger than the body (MCL 554.603).",
               "The landlord must mail an ITEMISED NOTICE OF DAMAGES WITHIN 30 DAYS after the tenancy ends, with the balance of the deposit. The tenant then has 7 DAYS to respond or forfeits the amount claimed (MCL 554.609).",
               "TRUTH IN RENTING ACT: a rental agreement may not waive habitability remedies or security-deposit rights, discriminate under Elliott-Larsen or the Persons with Disabilities Civil Rights Act, provide a confession of judgment, exculpate the lessor, waive a jury trial, or let the lessor alter the agreement without the tenant's written consent. Such a provision is VOID (MCL 554.633)."],
         "check": [("A Michigan security deposit may not exceed:", "1 1/2 months' rent", ["2 months' rent", "One month's rent"], "MCL 554.602."),
                   ("The landlord must mail an itemised notice of damages within:", "30 days after the tenancy ends", ["14 days", "45 days"], "MCL 554.609(1)."),
                   ("The tenant must give a forwarding address within:", "4 days after moving out", ["14 days", "30 days"], "MCL 554.603."),
                   ("A lease provision that waives the tenant's security deposit rights is:", "Void", ["Enforceable if initialled", "Valid for one year"], "MCL 554.633(1)(b), (3).")]},
        {"h": "Antitrust and MSHDA",
         "l": ["MICHIGAN ANTITRUST REFORM ACT: a contract, combination or conspiracy between 2 OR MORE PERSONS in restraint of, or to monopolise, trade or commerce in a relevant market is UNLAWFUL (MCL 445.772). Commission fixing between competing brokers is the classic example.",
               "The MICHIGAN STATE HOUSING DEVELOPMENT AUTHORITY (MSHDA) is a PUBLIC BODY CORPORATE AND POLITIC created by 1966 PA 346, governed by 3 heads of state departments plus gubernatorial appointees, and it administers state and federal housing programmes (MCL 125.1421).",
               "LAND CONTRACTS: changes in federal law, the Dodd-Frank Act, now reach seller financing, which the outline flags under land contract law."],
         "check": [("A conspiracy in restraint of trade under Michigan law requires:", "Two or more persons", ["One broker acting alone", "A written contract only"], "MCL 445.772."),
                   ("MSHDA is:", "A public body corporate and politic created by 1966 PA 346", ["A private lender", "A trade association"], "MCL 125.1421(1)."),
                   ("The federal statute the outline ties to land contract changes is:", "The Dodd-Frank Act", ["RESPA", "The Sherman Act"], "PSI Michigan outline, Additional State Topics.")]},
    ],
    "traps": [
        "Elliott-Larsen's housing list does NOT name disability; that is the Persons with Disabilities Civil Rights Act.",
        "Marital status and age ARE protected in Michigan; they are not federal classes.",
        "$3.75 per $500 is the STATE tax, and the SELLER pays it.",
        "Condominium withdrawal is 9 BUSINESS days, counting the day of receipt.",
        "72 hours in person, 120 hours by registered mail. Do not swap them.",
    ],
    "vocab": [
        ["Elliott-Larsen", "Michigan's civil rights act, 1976 PA 453."],
        ["Unplatted land", "Land not in a recorded plat; special deed statements apply."],
        ["Grantor", "The seller who conveys, and who owes the transfer tax."],
        ["Section 84a documents", "The condominium package that starts the 9-day clock."],
        ["Truth in Renting Act", "The statute voiding unlawful lease clauses."],
    ],
    "examples": [
        {"t": "Transfer tax on a $240,000 sale",
         "s": "Work out the state real estate transfer tax.",
         "w": ["$240,000 / $500 = 480 increments.",
               "480 x $3.75 = $1,800.",
               "The seller pays it to the county treasurer within 15 days of delivery."],
         "k": "Divide by 500, multiply by 3.75, and round any fraction of $500 UP to a full increment."},
    ],
}

STUDY["mi/licensing"] = {
    "summary": "Five items. The numbers to hold: 40 hours to sit the salesperson exam, 90 for a broker, 18 hours of continuing education a cycle, and 18 years old.",
    "sections": [
        {"h": "Prelicensure education (MCL 339.2504)",
         "l": ["A SALESPERSON applicant must show, before being permitted to take the examination, at least 40 CLOCK HOURS of approved prelicensure classroom courses in principles of real estate, INCLUDING AT LEAST 4 CLOCK HOURS on civil rights law and equal opportunity in housing, completed within the 36 MONTHS preceding the application.",
               "A BROKER applicant must complete at least 90 CLOCK HOURS, including AT LEAST 9 HOURS on civil rights and fair housing, in addition to the salesperson hours, within the same 36-month window unless they held an active salesperson licence throughout.",
               "A CLOCK HOUR is 50 to 60 minutes of actual classroom instruction, not counting outside assignments and reading.",
               "A course provider must be approved by the department and MAY NOT represent that its students are assured of passing."],
         "check": [("Prelicensure education for a Michigan salesperson is:", "40 clock hours", ["90 clock hours", "60 clock hours", "24 clock hours"], "MCL 339.2504(2)."),
                   ("Of those hours, how many must be civil rights and equal opportunity in housing?", "At least 4", ["At least 9", "At least 2", "None"], "MCL 339.2504(2)."),
                   ("A broker applicant's prelicensure requirement is:", "90 clock hours, including at least 9 on civil rights and fair housing", ["40 hours", "120 hours"], "MCL 339.2504(1)(b)."),
                   ("The hours must be completed within:", "The 36 months preceding the application", ["5 years", "12 months"], "MCL 339.2504(2).")]},
        {"h": "Continuing education (MCL 339.2504a)",
         "l": ["18 CLOCK HOURS of eligible continuing education each licence cycle - the department sets the figure by rule as 6 HOURS FOR EACH YEAR of the cycle.",
               "In EACH YEAR of the cycle: not less than 2 HOURS on laws, rules and court cases regarding real estate, and not less than 1 HOUR on local, state or federal FAIR HOUSING compliance. The rest are the licensee's choice.",
               "At the course the licensee must present the POCKET CARD or licence number AND a government photo identification.",
               "Repeating a course earns no additional hours. Records must be kept for NOT LESS THAN 4 YEARS and produced on request; renewals are subject to audit.",
               "Broker prelicensure hours and continuing education hours DO NOT COUNT for each other."],
         "check": [("Continuing education in Michigan is:", "18 clock hours per licence cycle", ["24 hours", "12 hours", "30 hours"], "MCL 339.2504a(1)(b)."),
                   ("How much of each YEAR's continuing education must be law, rules and court cases?", "Not less than 2 hours", ["Not less than 6 hours", "None"], "MCL 339.2504a(2)(a)(i)."),
                   ("And fair housing, each year?", "Not less than 1 hour", ["2 hours", "4 hours"], "MCL 339.2504a(2)(a)(ii)."),
                   ("Continuing education records must be kept for:", "Not less than 4 years", ["1 year", "7 years"], "MCL 339.2504a(3)."),
                   ("Repeating the same eligible course in a cycle earns:", "No additional hours", ["Half credit", "Full credit again"], "MCL 339.2504a(2)(e).")]},
        {"h": "Eligibility, renewal and lapse (MCL 339.2502a, 339.2505)",
         "l": ["The department SHALL NOT ISSUE A LICENCE to an individual UNDER 18 YEARS OF AGE.",
               "A salesperson's application must be SIGNED BY THE BROKER THAT WILL EMPLOY the applicant, and a salesperson licence is issued only to an INDIVIDUAL.",
               "The department SHALL NOT ISSUE A BROKER'S LICENCE to an individual convicted of EMBEZZLEMENT OR MISAPPROPRIATION OF FUNDS.",
               "A passing score on the examination, or on a portion of it, is VALID FOR 1 YEAR.",
               "A licensee who misses renewal may be relicensed WITHOUT EXAMINATION if they apply within 3 YEARS of expiry, pay the fees, and complete 6 CLOCK HOURS of continuing education FOR EACH YEAR AND PARTIAL YEAR elapsed. After 3 years they must instead redo the prelicensure hours in the preceding 12 months or pass the examination again.",
               "A licensee whose licence is REVOKED may not apply for a new one for AT LEAST 3 YEARS, and gets NO CREDIT for education, experience or examinations from before the revocation.",
               "A BROKER must maintain a PLACE OF BUSINESS in Michigan and a BRANCH OFFICE LICENCE for each additional place. A branch more than 25 MILES from the nearest boundary of the main office's municipality must be under the DIRECT SUPERVISION of an associate broker, physically present on a regular basis.",
               "A broker applicant needs the equivalent of 3 YEARS of full-time real estate experience; a salesperson earns 1 year of credit for each 12-month period in which they closed 5 OR MORE transactions."],
         "check": [("The minimum age for a Michigan licence is:", "18", ["17", "19", "21"], "MCL 339.2502a(1)."),
                   ("A salesperson's licence application must be signed by:", "The broker who will employ the applicant", ["Two references", "A notary only"], "MCL 339.2505(4)."),
                   ("A passing examination score is valid for:", "1 year", ["6 months", "3 years", "Indefinitely"], "MCL 339.2505(6)(b)."),
                   ("A branch office more than 25 miles from the main office's municipality must be:", "Under the direct supervision of an associate broker physically present on a regular basis", ["Visited monthly", "Closed"], "MCL 339.2505(3)."),
                   ("Someone relicensing 2 years after expiry must complete:", "6 clock hours of continuing education for each year and partial year elapsed", ["The full 40 prelicensure hours", "Nothing"], "MCL 339.2502a(4)(c)."),
                   ("After revocation, a licensee may not apply again for:", "At least 3 years", ["1 year", "5 years", "Ever"], "MCL 339.2502a(7)."),
                   ("A broker applicant's experience requirement is:", "The equivalent of 3 years full-time in the business of real estate", ["1 year", "5 years"], "MCL 339.2505(7)."),
                   ("A broker's licence is barred outright for a conviction of:", "Embezzlement or misappropriation of funds", ["Any misdemeanour", "A traffic offence"], "MCL 339.2505(2).")]},
        {"h": "Who needs a licence",
         "p": ["A REAL ESTATE BROKER is a person who, intending to collect a fee, sells, buys, provides market analyses of, lists or negotiates real estate; negotiates its mortgage; negotiates construction on it; leases or rents it for others; engages in PROPERTY MANAGEMENT; sells businesses or goodwill for others; or as owner engages in the sale of real estate as a PRINCIPAL VOCATION. A REAL ESTATE SALESPERSON does those things FOR COMPENSATION, EMPLOYED DIRECTLY OR INDIRECTLY BY A LICENSED BROKER (MCL 339.2501(u), (v)).",
               "A salesperson's employment may be an INDEPENDENT CONTRACTOR RELATIONSHIP - a written agreement treating them as not an employee for tax purposes, with at least 75% of annual compensation from real estate sales commissions. That does NOT relieve the broker of the duty to SUPERVISE (MCL 339.2501(g), (h))."],
         "check": [("Property management for a fee in Michigan:", "Requires a real estate licence", ["Is exempt", "Needs only registration"], "MCL 339.2501(r), (u)."),
                   ("An independent contractor agreement requires at least what share of annual compensation from sales commissions?", "75%", ["50%", "90%", "None"], "MCL 339.2501(h)(ii)."),
                   ("An independent contractor relationship means the broker:", "Still must supervise the licensee's regulated acts", ["Has no supervisory duty", "Is not liable at all"], "MCL 339.2501(g).")]},
    ],
    "traps": [
        "40 hours salesperson, 90 broker. The 4 and 9 civil rights hours sit inside those totals.",
        "18 hours of continuing education a cycle, but the 2-hour law and 1-hour fair housing minimums are PER YEAR.",
        "The 3-year relicensure window needs 6 hours for each year AND PARTIAL YEAR.",
        "The 25-mile branch rule is measured from the nearest boundary of the main office's municipality.",
    ],
    "vocab": [
        ["Clock hour", "50 to 60 minutes of actual instruction."],
        ["Associate broker", "Someone who qualifies as a broker but works for one."],
        ["Principal", "The designated control person of a licensed business entity."],
        ["Pocket card", "The card the department issues with the licence."],
        ["Branch office licence", "Required for each additional place of business."],
    ],
    "examples": [],
}

STUDY["mi/agency"] = {
    "summary": "Five items. Michigan's quirks: the agency disclosure comes BEFORE any confidential information, services can be WAIVED by a limited service agreement, and a TRANSACTION COORDINATOR represents nobody.",
    "sections": [
        {"h": "When the disclosure is made (MCL 339.2517(1))",
         "p": ["A licensee must disclose to a potential buyer or seller ALL TYPES OF AGENCY RELATIONSHIPS AVAILABLE and the duties each creates BEFORE that person discloses to the licensee ANY CONFIDENTIAL INFORMATION specific to them. The disclosure is IN WRITING, given to the client, and substantially in the statutory form. Failing to give it is prohibited conduct under MCL 339.2512(b)."],
         "check": [("The Michigan agency disclosure must be given:", "Before the buyer or seller discloses any confidential information to the licensee", ["At the first showing", "Before closing", "With the purchase agreement"], "MCL 339.2517(1)."),
                   ("The disclosure must be:", "In writing and substantially in the statutory form", ["Oral is enough", "Any format the broker prefers"], "MCL 339.2517(3)."),
                   ("A real estate transaction, for the disclosure statute, means:", "Not less than 1 and not more than 4 residential dwelling units, or a residential building site", ["Any property at all", "Commercial property"], "MCL 339.2517(11)(g).")]},
        {"h": "Minimum duties and services (MCL 339.2512d, reproduced in 2517)",
         "l": ["DUTIES owed to the client: reasonable CARE AND SKILL; PERFORMANCE of the terms of the agreement; LOYALTY to the client's interest; COMPLIANCE with law; REFERRAL to other licensed professionals for expert advice outside the licensee's expertise; timely ACCOUNTING for money and property; and CONFIDENTIALITY of information obtained in the relationship unless released by the client or by law, including not disclosing it to a licensee who is not the client's agent.",
               "SERVICES owed: marketing as agreed; ACCEPTANCE OF DELIVERY AND PRESENTATION of offers and counteroffers; assistance in developing, communicating, negotiating and presenting offers and related documents until an agreement is executed and contingencies satisfied or waived; assistance after execution to complete the transaction; and, for a broker at closing, a COMPLETE AND DETAILED SIGNED CLOSING STATEMENT showing each party its receipts and disbursements.",
               "ONLY THREE SERVICES may be waived by a LIMITED SERVICE AGREEMENT - presentation of offers, negotiation assistance, and post-execution assistance. The DUTIES cannot be waived.",
               "The waiver is on a SEPARATE FORM, initialled service by service, and tells the client that NO OTHER LICENSEE must provide the waived services and that they may need to retain an attorney."],
         "check": [("Which may a client waive by a limited service agreement?", "Presentation of offers, negotiation assistance, and post-execution assistance", ["Loyalty and confidentiality", "The duty to account", "Compliance with law"], "MCL 339.2517(2), (4)."),
                   ("The limited service waiver must be:", "On a separate form, with each waived service initialled", ["A clause in the listing", "Oral with a witness"], "MCL 339.2517(4)."),
                   ("A licensee who does not provide the minimum services without a written waiver:", "Commits prohibited conduct", ["Is merely negligent", "Owes a refund only"], "MCL 339.2512(j)."),
                   ("The waiver form warns the client that:", "No other licensee is required to provide the waived services", ["The fee is reduced by law", "The listing cannot be cancelled"], "MCL 339.2517(4).")]},
        {"h": "Dual agency, designated agency, transaction coordinator",
         "l": ["DUAL AGENCY is permitted, but only with the KNOWLEDGE AND INFORMED CONSENT, IN WRITING, of both seller and buyer. The dual agent then cannot disclose all known information to either side.",
               "A TRANSACTION COORDINATOR is a licensee who is NOT THE AGENT OF EITHER party. Acting as one is allowed UPON PROPER NOTICE to all parties (MCL 339.2517(5), (11)(k)).",
               "DESIGNATED AGENCY: a broker and client may agree in writing that one named salesperson or associate broker is the client's agent. WITHOUT a written designated agency agreement, the client is considered to have an agency relationship with the BROKER AND ALL AFFILIATED LICENSEES (MCL 339.2517(6)).",
               "With a designated agency agreement, two designated agents in the same firm may represent OPPOSITE PARTIES in the same transaction and are NOT dual agents, and the designated agent's knowledge of confidential information is NOT IMPUTED to other affiliated licensees. But the BROKER AND ALL SUPERVISORY BROKERS are then DISCLOSED CONSENSUAL DUAL AGENTS, and the designated agents must tell their clients that BEFORE AN OFFER IS MADE OR PRESENTED (MCL 339.2517(7), (8)).",
               "A designated agency agreement must NAME every associate broker authorised to act as a SUPERVISORY BROKER. A designated agent may share confidential information with a supervisory broker to seek advice for the client's benefit, but with no other licensee (MCL 339.2517(9)).",
               "A listing or buyer agency agreement may be amended at any time by WRITTEN ADDENDUM SIGNED BY THE PARTIES to create designated agency or change the agent or supervisory broker."],
         "check": [("A licensee who is the agent of neither party is a:", "Transaction coordinator", ["Dual agent", "Subagent", "Designated agent"], "MCL 339.2517(11)(k)."),
                   ("With no written designated agency agreement, the client's agency relationship runs with:", "The broker and all affiliated licensees", ["Only the individual salesperson", "No one"], "MCL 339.2517(6)."),
                   ("Two designated agents in one firm on opposite sides of a deal are:", "Not dual agents, but their broker and supervisory brokers are disclosed consensual dual agents", ["Both dual agents", "In breach of the Act"], "MCL 339.2517(7), (8)."),
                   ("They must tell their clients about the broker's position:", "Before an offer to purchase is made or presented", ["At closing", "In the disclosure booklet only"], "MCL 339.2517(7)."),
                   ("Dual agency in Michigan requires:", "The knowledge and informed written consent of both buyer and seller", ["Only an oral agreement", "Board approval"], "MCL 339.2517(3), Dual Agents."),
                   ("A designated agent may share a client's confidential information with:", "A supervisory broker, to seek advice for the client's benefit", ["Any affiliated licensee", "The other party's agent"], "MCL 339.2517(9).")]},
    ],
    "traps": [
        "Designated agency defeats dual agency for the AGENTS but not for the BROKER.",
        "Only three services are waivable. No duty is waivable.",
        "The disclosure precedes confidential information, not the offer.",
        "A transaction coordinator is not a dual agent; they represent nobody.",
    ],
    "vocab": [
        ["Transaction coordinator", "A licensee acting for neither party."],
        ["Designated agent", "The individual named as the client's agent."],
        ["Supervisory broker", "An associate broker named to supervise the relationship."],
        ["Affiliated licensees", "Salespersons and associate brokers of the same broker."],
        ["Limited service agreement", "The written waiver of named services."],
    ],
    "examples": [
        {"t": "Two agents, one firm",
         "s": "Both buyer and seller have signed designated agency agreements with different salespersons at the same brokerage.",
         "w": ["The two designated agents are NOT dual agents, and neither one's confidential knowledge is imputed to the other.",
               "The broker and every named supervisory broker ARE disclosed consensual dual agents.",
               "Both agents must tell their clients that before an offer is made or presented."],
         "k": "Designated agency splits the agents but not the broker."},
    ],
}

STUDY["mi/department"] = {
    "summary": "Only three items. Know who 'Department' and 'Board' mean on the paper, and that the penalties live in articles 5 and 6 of the Occupational Code.",
    "sections": [
        {"h": "Who is who",
         "l": ["On examination questions about Michigan law, 'DEPARTMENT' means the DEPARTMENT OF LICENSING AND REGULATORY AFFAIRS (LARA) and 'BOARD' means the BOARD OF REAL ESTATE BROKERS AND SALESPERSONS - the bulletin says so in terms.",
               "The Board of real estate brokers and salespersons is created by MCL 339.2502.",
               "The department issues and renews licences, approves prelicensure courses and providers, sets the licence cycle and the continuing education hours BY RULE, and may suspend or revoke a course provider's approval.",
               "The department may audit a licensee's continuing education on renewal, and records of trust accounts, property management accounts and courses are SUBJECT TO ITS INSPECTION."],
         "check": [("On the Michigan examination, 'Department' means:", "The Department of Licensing and Regulatory Affairs", ["The Board of Realtors", "The county clerk"], "PSI Michigan bulletin, state outline note."),
                   ("'Board' on the examination means:", "The Board of Real Estate Brokers and Salespersons", ["The county road commission", "The Real Estate Commission"], "MCL 339.2502; PSI bulletin."),
                   ("Trust account records are:", "Subject to inspection by the department", ["Private to the broker", "Open only by subpoena"], "MCL 339.2512(k)(vi).")]},
        {"h": "Penalties and complaints",
         "l": ["A licensee who commits the prohibited conduct in MCL 339.2512 is subject to the PENALTIES SET FORTH IN ARTICLE 6 of the Occupational Code.",
               "A complaint seeking a penalty under ARTICLE 5 must be filed NOT LATER THAN 18 MONTHS after the violation or, where it arose in a transaction, after the transaction was completed.",
               "A person operating an unapproved prelicensure school in violation of MCL 339.2504(4) is also subject to the article 6 penalties.",
               "Where an audit shows a licensee short of continuing education, the penalty MUST INCLUDE a requirement to complete enough additional hours to cure the deficient period."],
         "check": [("The time limit for filing a complaint seeking a penalty is:", "18 months after the violation or completion of the transaction", ["6 months", "No limit", "5 years"], "MCL 339.2512(2)."),
                   ("Penalties for prohibited conduct are set out in:", "Article 6 of the Occupational Code", ["Article 25 itself", "The Elliott-Larsen Act"], "MCL 339.2512(1)."),
                   ("A continuing education shortfall found on audit means the penalty must include:", "Completing enough additional hours to cure the deficient period", ["Only a fine", "Automatic revocation"], "MCL 339.2504a(5).")]},
    ],
    "traps": [
        "LARA is the Department; the Board is a separate body named in the statute.",
        "18 months, from the later of the violation and the completed transaction.",
    ],
    "vocab": [
        ["LARA", "Department of Licensing and Regulatory Affairs."],
        ["Article 6", "The Occupational Code's penalty provisions."],
        ["Audit", "The department's check of continuing education or records."],
    ],
    "examples": [],
}


# ------------------------------------------------------------- questions

Q = [
 # activities
 ("mi/activities", "Trust money", 1, "A Michigan broker must deposit money belonging to others into the trust account within:",
  "2 banking days after notice that all parties accepted the offer", ["5 business days after the offer", "24 hours of receipt", "10 days of closing"],
  "MCL 339.2512(k)(v)."),
 ("mi/activities", "Trust money", 1, "A salesperson who receives a deposit must:",
  "Pay or deliver it to the employing broker on receipt", ["Deposit it in their own account", "Hold it until closing", "Give it to the seller"],
  "MCL 339.2512(k)(ii)."),
 ("mi/activities", "Trust money", 2, "How much of its own money may a broker keep in each trust account?",
  "Not more than $2,000.00", ["Nothing at all", "$100", "Up to one month's expenses"],
  "MCL 339.2512(k)(iv), for bank charges and minimum balances."),
 ("mi/activities", "Trust money", 2, "A Michigan broker's custodial trust account must:",
  "Designate the broker as trustee and allow withdrawal without previous notice", ["Be interest bearing", "Be held at a national bank only", "Require the seller's signature"],
  "MCL 339.2512(k)(vi)."),
 ("mi/activities", "Trust money", 2, "Putting advance payments belonging to others into the broker's business account is:",
  "Commingling, and prohibited", ["Allowed for up to 30 days", "Allowed with written consent"],
  "MCL 339.2512(k)(iii)."),
 ("mi/activities", "Trust money", 3, "Where the purchase agreement names an escrowee other than the broker, a licensee holding the deposit must deliver it to that escrowee within:",
  "2 banking days after notice that all parties accepted", ["5 days", "Immediately on signing"],
  "MCL 339.2512(k)(vii)."),
 ("mi/activities", "Advertising", 1, "In advertising that names a salesperson, the employing broker's business name must appear:",
  "In equal or greater type size than the salesperson's name", ["Anywhere on the advertisement", "In the smallest legible type", "Only on request"],
  "MCL 339.2512e(3)(b)."),
 ("mi/activities", "Advertising", 2, "A salesperson may advertise a property for sale under their own name only if:",
  "The property is the salesperson's principal residence", ["The broker consents in writing", "It is a rental property", "The listing has expired"],
  "MCL 339.2512e(4)."),
 ("mi/activities", "Advertising", 2, "A broker's advertisement must include the broker's name and:",
  "The broker's telephone number or street address, and a statement that the advertiser is a real estate broker", ["The licence number and expiry date", "The seller's name"],
  "MCL 339.2512e(1)."),
 ("mi/activities", "Advertising", 3, "A broker that adopts an assumed name must notify the department:",
  "With the licence application or within 30 days of adopting it, whichever is earlier", ["At the next renewal", "Within 90 days", "Only if asked"],
  "MCL 339.2512e(5)."),
 ("mi/activities", "Stigma", 1, "A Michigan licensee may be sued for failing to disclose that a prior occupant had a disability:",
  "No; an action may not be brought on that ground", ["Yes, always", "Yes, if the buyer asks"],
  "MCL 339.2518(a); disclosing it would be unlawful discrimination."),
 ("mi/activities", "Stigma", 2, "The statute bars an action for not disclosing a homicide at the property where the event:",
  "Had no material effect on the condition of the property", ["Happened more than 5 years ago", "Was never reported"],
  "MCL 339.2518(b)."),
 ("mi/activities", "Stigma", 2, "On sex offender registry information, a Michigan licensee:",
  "Cannot be sued for failing to disclose it; the compilation is public", ["Must search and report it", "Must warn every buyer"],
  "MCL 339.2518(c)."),
 ("mi/activities", "Inducements", 1, "Paying an unlicensed person for the name of a potential buyer is:",
  "Prohibited", ["Allowed under $100", "Allowed with the broker's consent", "Allowed once per transaction"],
  "MCL 339.2512(h)."),
 ("mi/activities", "Inducements", 3, "Which payment is NOT caught by the fee-sharing prohibition?",
  "Payment for a commercially prepared list of names", ["A finder's fee to a neighbour", "A gift card for a referral"],
  "MCL 339.2512(h) excludes it expressly."),
 ("mi/activities", "Records", 2, "A broker must deliver or mail a discharged salesperson's licence to the department within:",
  "5 days", ["30 days", "10 business days", "At the next renewal"],
  "MCL 339.2507(1); failing to do so violates MCL 339.2512(f)."),
 ("mi/activities", "Records", 2, "An unlicensed person suing for a commission in a Michigan court:",
  "Cannot maintain the action; they must allege and prove they were licensed", ["May recover in quantum meruit", "May sue in small claims only"],
  "MCL 339.2512a."),
 ("mi/activities", "Records", 2, "Money a broker holds as a property manager must be:",
  "Kept in property management accounts separate from all other accounts", ["Held in the sales trust account", "Paid to the owner weekly"],
  "MCL 339.2512c(2)."),
 ("mi/activities", "Discipline", 2, "A licensee acting for more than one party in a transaction without the parties' knowledge:",
  "Commits prohibited conduct", ["Is acting as a transaction coordinator", "Needs only an oral disclosure"],
  "MCL 339.2512(a)."),

 # additional
 ("mi/additional", "Fair housing", 1, "Which is protected in a Michigan real estate transaction but not by the federal Fair Housing Act?",
  "Marital status", ["Race", "Religion", "National origin"],
  "MCL 37.2502(1), the Elliott-Larsen Civil Rights Act."),
 ("mi/additional", "Fair housing", 1, "Elliott-Larsen's real estate list also includes:",
  "Age and gender identity or expression", ["Credit score", "Occupation", "Length of employment"],
  "MCL 37.2502(1)."),
 ("mi/additional", "Fair housing", 2, "Disability discrimination in Michigan housing is governed by:",
  "The Persons with Disabilities Civil Rights Act, 1976 PA 220", ["Elliott-Larsen alone", "The Occupational Code", "The Truth in Renting Act"],
  "Elliott-Larsen's housing list does not name disability."),
 ("mi/additional", "Fair housing", 2, "Michigan's source-of-income protection does not apply to a landlord of:",
  "Fewer than 5 rental units in the state", ["Fewer than 20 units", "Any owner-occupied duplex"],
  "MCL 37.2502(4)."),
 ("mi/additional", "Fair housing", 3, "Elliott-Larsen protects a person against discrimination based on the characteristics of:",
  "That individual or anyone residing with that individual", ["Only the applicant", "Only the named tenant"],
  "MCL 37.2502(1)."),
 ("mi/additional", "Disclosure", 1, "The Michigan seller's disclosure statement applies to real estate of:",
  "Not less than 1 and not more than 4 residential dwelling units", ["Any real estate", "Commercial property only", "New construction only"],
  "MCL 565.952."),
 ("mi/additional", "Disclosure", 1, "The seller must deliver the disclosure statement:",
  "Before the seller executes a binding purchase agreement", ["At closing", "Within 10 days of the offer", "On request"],
  "MCL 565.954(1)(a)."),
 ("mi/additional", "Disclosure", 2, "A disclosure statement handed over in person after the agreement was signed lets the buyer terminate within:",
  "72 hours", ["24 hours", "120 hours", "10 days"],
  "MCL 565.954(3)(a)."),
 ("mi/additional", "Disclosure", 2, "Delivered instead by registered mail, the termination window is:",
  "120 hours", ["72 hours", "48 hours", "5 business days"],
  "MCL 565.954(3)(b)."),
 ("mi/additional", "Disclosure", 3, "The buyer's right to terminate for a late disclosure expires:",
  "On transfer of the property by deed or installment sales contract", ["After 30 days", "At the inspection deadline"],
  "MCL 565.954(4)."),
 ("mi/additional", "Disclosure", 2, "The seller's disclosure statement is:",
  "A disclosure of what the seller knows, and not a warranty", ["A warranty of condition", "An inspection report", "A representation of the seller's agent"],
  "MCL 565.957(1)."),
 ("mi/additional", "Land division", 1, "Selling a parcel of unplatted land in an unincorporated area abutting a road not accepted as public requires:",
  "A separate written instrument attached to the conveyance stating the road is private and need not be maintained by the county road commissioners", ["A note in the listing", "An oral warning at closing", "Nothing special"],
  "MCL 560.261."),
 ("mi/additional", "Land division", 2, "A sale made without the required private road notice is:",
  "Voidable at the purchaser's option", ["Void from the start", "Valid in all respects", "A felony"],
  "MCL 560.261."),
 ("mi/additional", "Land division", 2, "A deed for unplatted land executed after 31 March 1997 must contain:",
  "The Michigan Right to Farm Act statement", ["A flood zone notice", "A lead paint warning", "A mineral rights waiver"],
  "MCL 560.109(4), added by 1996 PA 591."),
 ("mi/additional", "Land division", 3, "If a deed for unplatted land says nothing about division rights:",
  "They stay with the remainder of the parent tract retained by the grantor", ["They pass to the grantee", "They are extinguished"],
  "MCL 560.109(3)."),
 ("mi/additional", "Transfer tax", 1, "Michigan's state real estate transfer tax rate is:",
  "$3.75 for each $500 or fraction of $500 of value", ["$1.10 per $1,000", "0.75% of the sale price", "$7.50 per $1,000"],
  "MCL 207.525(1)."),
 ("mi/additional", "Transfer tax", 1, "Who is liable for the state real estate transfer tax?",
  "The seller or grantor", ["The buyer", "The lender", "The listing broker"],
  "MCL 207.523(2)."),
 ("mi/additional", "Transfer tax", 2, "The state transfer tax is paid to the county treasurer not later than:",
  "15 days after delivery of the instrument", ["30 days after closing", "The end of the month"],
  "MCL 207.523(3)."),
 ("mi/additional", "Transfer tax", 3, "The state transfer tax on a $240,000 sale is:",
  "$1,800", ["$900", "$2,400", "$480"],
  "$240,000 / $500 = 480; 480 x $3.75 = $1,800 (MCL 207.525)."),
 ("mi/additional", "Condominiums", 1, "A purchaser of a residential condominium unit may withdraw from a signed purchase agreement within:",
  "9 business days after receiving the required documents", ["3 business days", "15 days", "72 hours"],
  "MCL 559.184(2); the day of receipt counts if it is a business day."),
 ("mi/additional", "Condominiums", 2, "Funds must be returned to a withdrawing condominium purchaser within:",
  "3 business days", ["30 days", "10 days", "At the developer's convenience"],
  "MCL 559.184(4)(a)."),
 ("mi/additional", "Condominiums", 3, "A Michigan condominium purchase agreement must offer binding arbitration, at the purchaser's option, for claims under:",
  "$2,500.00", ["$10,000", "$500", "$25,000"],
  "MCL 559.184(4)(d)."),
 ("mi/additional", "Landlord tenant", 1, "A Michigan security deposit may not exceed:",
  "1 1/2 months' rent", ["One month's rent", "2 months' rent", "Whatever the lease says"],
  "MCL 554.602."),
 ("mi/additional", "Landlord tenant", 2, "After a tenancy ends the landlord must mail an itemised notice of damages within:",
  "30 days", ["14 days", "45 days", "7 days"],
  "MCL 554.609(1)."),
 ("mi/additional", "Landlord tenant", 2, "The tenant must give the landlord a forwarding address within:",
  "4 days after moving out", ["14 days", "30 days", "Before moving out"],
  "MCL 554.603."),
 ("mi/additional", "Landlord tenant", 2, "A lease clause waiving the tenant's security deposit rights is:",
  "Void", ["Enforceable if initialled", "Valid for the first year", "Enforceable against a commercial tenant"],
  "MCL 554.633(1)(b) and (3), the Truth in Renting Act."),
 ("mi/additional", "Antitrust", 1, "Under the Michigan Antitrust Reform Act a restraint of trade requires:",
  "A contract, combination or conspiracy between 2 or more persons", ["One broker setting a high fee", "A written agreement only", "A government finding"],
  "MCL 445.772."),
 ("mi/additional", "MSHDA", 2, "MSHDA is:",
  "A public body corporate and politic created by 1966 PA 346", ["A private mortgage insurer", "A trade association of brokers", "A federal agency"],
  "MCL 125.1421(1)."),

 # licensing
 ("mi/licensing", "Education", 1, "Prelicensure education for a Michigan salesperson is:",
  "40 clock hours", ["90 clock hours", "60 clock hours", "24 clock hours"],
  "MCL 339.2504(2)."),
 ("mi/licensing", "Education", 1, "How many of those hours must cover civil rights law and equal opportunity in housing?",
  "At least 4", ["At least 9", "At least 2", "None"],
  "MCL 339.2504(2)."),
 ("mi/licensing", "Education", 2, "A Michigan broker applicant must complete:",
  "90 clock hours, including at least 9 on civil rights and fair housing", ["40 clock hours", "120 clock hours", "60 clock hours"],
  "MCL 339.2504(1)(b)."),
 ("mi/licensing", "Education", 2, "The prelicensure hours must be completed within:",
  "The 36 months preceding the application", ["5 years", "12 months", "No time limit"],
  "MCL 339.2504(2)."),
 ("mi/licensing", "Education", 3, "A clock hour means:",
  "50 to 60 minutes of actual classroom instruction, not counting outside assignments", ["A full 60 minutes always", "Any session of any length"],
  "MCL 339.2501(d)."),
 ("mi/licensing", "Continuing education", 1, "Continuing education in Michigan is:",
  "18 clock hours per licence cycle", ["24 hours", "12 hours", "6 hours"],
  "MCL 339.2504a(1)(b), being 6 hours for each year of the cycle."),
 ("mi/licensing", "Continuing education", 2, "In each year of the cycle a licensee must take at least:",
  "2 hours on law, rules and court cases and 1 hour on fair housing", ["6 hours of fair housing", "2 hours of ethics only", "Nothing specific"],
  "MCL 339.2504a(2)(a)."),
 ("mi/licensing", "Continuing education", 2, "Continuing education records must be retained for:",
  "Not less than 4 years", ["1 year", "7 years", "Until renewal"],
  "MCL 339.2504a(3)."),
 ("mi/licensing", "Continuing education", 3, "Repeating an eligible continuing education course within a cycle earns:",
  "No additional hours", ["Half credit", "Full credit again"],
  "MCL 339.2504a(2)(e)."),
 ("mi/licensing", "Eligibility", 1, "The minimum age for a Michigan real estate licence is:",
  "18", ["17", "19", "21"],
  "MCL 339.2502a(1)."),
 ("mi/licensing", "Eligibility", 2, "A salesperson's licence application must be signed by:",
  "The real estate broker who will employ the applicant", ["Two licensed references", "A notary public only", "The applicant alone"],
  "MCL 339.2505(4)."),
 ("mi/licensing", "Eligibility", 2, "A broker's licence must be refused to an applicant convicted of:",
  "Embezzlement or misappropriation of funds", ["Any misdemeanour", "A traffic offence", "Any felony whatever"],
  "MCL 339.2505(2)."),
 ("mi/licensing", "Eligibility", 2, "A passing score on the Michigan examination is valid for:",
  "1 year", ["6 months", "3 years", "Indefinitely"],
  "MCL 339.2505(6)(b)."),
 ("mi/licensing", "Offices", 2, "A branch office more than 25 miles from the nearest boundary of the main office's municipality must be:",
  "Under the direct supervision of an associate broker physically present on a regular basis", ["Visited monthly by the broker", "Licensed as a separate brokerage", "Closed"],
  "MCL 339.2505(3)."),
 ("mi/licensing", "Renewal", 2, "A licensee relicensing 2 years after expiry must complete:",
  "6 clock hours of continuing education for each year and partial year elapsed", ["The full prelicensure course", "Nothing but the fees", "A new examination"],
  "MCL 339.2502a(4)(c)."),
 ("mi/licensing", "Renewal", 3, "After a licence is revoked, the licensee may not apply for a new one for:",
  "At least 3 years", ["1 year", "5 years", "Ever"],
  "MCL 339.2502a(7); no credit for prior education or examinations."),
 ("mi/licensing", "Scope", 1, "Property management for a fee in Michigan:",
  "Requires a real estate licence", ["Is exempt from licensing", "Needs only registration with LARA"],
  "MCL 339.2501(r), (u)."),
 ("mi/licensing", "Scope", 3, "An independent contractor relationship requires that at least what share of annual compensation comes from real estate sales commissions?",
  "75%", ["50%", "90%", "100%"],
  "MCL 339.2501(h)(ii)."),
 ("mi/licensing", "Scope", 2, "An independent contractor agreement means the broker:",
  "Still must supervise the licensee's regulated acts", ["Has no supervisory responsibility", "Is not liable for anything"],
  "MCL 339.2501(g)."),
 ("mi/licensing", "Experience", 3, "A Michigan broker applicant must show:",
  "The equivalent of 3 years of full-time experience in the business of real estate", ["1 year of licensure", "5 years of licensure", "No experience"],
  "MCL 339.2505(7)."),

 # agency
 ("mi/agency", "Disclosure", 1, "The Michigan agency disclosure must be given:",
  "Before the buyer or seller discloses any confidential information to the licensee", ["At the first showing", "With the purchase agreement", "Before closing"],
  "MCL 339.2517(1)."),
 ("mi/agency", "Disclosure", 2, "The agency disclosure must be:",
  "In writing, given to the client, and substantially in the statutory form", ["Oral if witnessed", "In any format the broker chooses"],
  "MCL 339.2517(3)."),
 ("mi/agency", "Disclosure", 3, "A 'real estate transaction' under the agency disclosure statute means:",
  "A sale or lease of 1 to 4 residential dwelling units, or a residential building site", ["Any transfer of real estate", "Commercial property only"],
  "MCL 339.2517(11)(g)."),
 ("mi/agency", "Limited service", 1, "Which may a client waive under a Michigan limited service agreement?",
  "Presentation of offers, negotiation assistance, and post-execution assistance", ["Loyalty and confidentiality", "The duty to account", "Compliance with the law"],
  "MCL 339.2517(2), (4); only section 2512d(3)(b), (c), (d) services."),
 ("mi/agency", "Limited service", 2, "The limited service waiver must appear:",
  "On a separate form, with each waived service initialled", ["As a clause in the listing agreement", "In the agency disclosure"],
  "MCL 339.2517(4)."),
 ("mi/agency", "Limited service", 2, "A licensee who fails to provide the minimum services without a written waiver:",
  "Commits prohibited conduct", ["Owes only a refund", "Is merely negligent"],
  "MCL 339.2512(j)."),
 ("mi/agency", "Coordinator", 1, "A licensee who is the agent of neither buyer nor seller is a:",
  "Transaction coordinator", ["Dual agent", "Subagent", "Designated agent"],
  "MCL 339.2517(5), (11)(k); allowed on proper notice to all parties."),
 ("mi/agency", "Designated agency", 2, "With no written designated agency agreement, a client has an agency relationship with:",
  "The broker and all affiliated licensees", ["Only the individual salesperson", "No one until closing"],
  "MCL 339.2517(6)."),
 ("mi/agency", "Designated agency", 2, "Two designated agents of the same broker representing opposite parties are:",
  "Not dual agents, though their broker and supervisory brokers are disclosed consensual dual agents", ["Both dual agents", "In violation of the Act"],
  "MCL 339.2517(7), (8)."),
 ("mi/agency", "Designated agency", 3, "Those designated agents must disclose the broker's dual position:",
  "Before an offer to purchase is made or presented", ["At closing", "Only if asked"],
  "MCL 339.2517(7)."),
 ("mi/agency", "Designated agency", 3, "A designated agent may share a client's confidential information with:",
  "A supervisory broker, to seek advice or assistance for the client's benefit", ["Any affiliated licensee", "The cooperating agent"],
  "MCL 339.2517(9)."),
 ("mi/agency", "Dual agency", 1, "Dual agency in Michigan is:",
  "Permitted with the knowledge and informed written consent of both buyer and seller", ["Prohibited outright", "Permitted on oral consent", "Permitted only in commercial deals"],
  "MCL 339.2517(3), Dual Agents."),
 ("mi/agency", "Duties", 2, "Which is a minimum DUTY a Michigan client cannot waive?",
  "Confidentiality of information obtained in the relationship", ["Presentation of offers", "Negotiation assistance", "Post-execution assistance"],
  "MCL 339.2517(3)(1)(g); only the three services are waivable."),
 ("mi/agency", "Duties", 3, "At closing, a broker or associate broker involved must furnish:",
  "A complete and detailed signed closing statement showing each party its receipts and disbursements", ["A commission invoice only", "A copy of the deed"],
  "MCL 339.2517(3)(2)(e)."),

 # department
 ("mi/department", "Who is who", 1, "On the Michigan examination, 'Department' means:",
  "The Department of Licensing and Regulatory Affairs", ["The Board of Realtors", "The county register of deeds", "The Attorney General"],
  "PSI Michigan bulletin, state outline note."),
 ("mi/department", "Who is who", 1, "'Board' on the Michigan examination means:",
  "The Board of Real Estate Brokers and Salespersons", ["The county road commission", "The Michigan Real Estate Commission"],
  "MCL 339.2502; PSI bulletin note."),
 ("mi/department", "Penalties", 2, "A complaint seeking a penalty for prohibited conduct must be filed within:",
  "18 months of the violation or of completion of the transaction, whichever is later", ["6 months", "3 years", "No time limit"],
  "MCL 339.2512(2)."),
 ("mi/department", "Penalties", 2, "Penalties for prohibited conduct under article 25 are set out in:",
  "Article 6 of the Occupational Code", ["Article 25 itself", "The Elliott-Larsen Act", "The Truth in Renting Act"],
  "MCL 339.2512(1)."),
 ("mi/department", "Penalties", 3, "Where an audit shows a continuing education shortfall, the penalty must include:",
  "Completing enough additional hours to cure the deficient period", ["A fine only", "Automatic revocation", "A public reprimand only"],
  "MCL 339.2504a(5)."),
 ("mi/department", "Inspection", 2, "A broker's trust account records are:",
  "Subject to inspection by the department", ["Private to the broker", "Open only under subpoena"],
  "MCL 339.2512(k)(vi)."),
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
            "id": "mi-" + hashlib.sha1(q.encode()).hexdigest()[:8],
            "portion": "georgia", "topic": topic, "subtopic": sub,
            "sub": topic + "|" + sub, "concept": "Michigan " + sub.lower(),
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
        "code": "MI", "name": "Michigan", "abbr": "MI",
        "regulator": "Michigan Department of Licensing and Regulatory Affairs",
        "pass": EXAM["pass"], "single": True,
        "portions": {
            "national": {"name": "General practice",
                         "scored": EXAM["national_scored"],
                         "minutes": EXAM["national_minutes"],
                         "blurb": "Principles, practice and the maths, as Michigan tests them."},
            "georgia": {"name": "Michigan law", "scored": EXAM["state_scored"],
                        "minutes": EXAM["state_minutes"],
                        "blurb": "Occupational Code article 25, Elliott-Larsen, disclosure, land division and the transfer tax."},
        },
        "topics": topics, "bank": bank, "study": study,
        "sources": SOURCES, "diffs": DIFFS,
    }


# Where Michigan departs from the national rule.
DIFFS = {
    "national/agency": [
        "Michigan allows a LIMITED SERVICE AGREEMENT waiving three named services - presentation of offers, negotiation assistance and post-execution assistance - but no statutory DUTY may be waived (MCL 339.2517(2), (4)).",
        "A TRANSACTION COORDINATOR is a licensee who represents neither party, allowed on proper notice (MCL 339.2517(5)).",
        "Under DESIGNATED AGENCY two agents of one broker may take opposite sides and are not dual agents, but the broker and supervisory brokers become disclosed consensual dual agents (MCL 339.2517(7), (8)).",
        "The agency disclosure comes BEFORE the client gives any confidential information, not at the offer (MCL 339.2517(1)).",
    ],
    "national/disclosures": [
        "Michigan bars an ACTION against a licensee for not disclosing a former occupant's disability, a homicide or suicide with no material effect on condition, or sex offender registry information (MCL 339.2518).",
        "A late seller's disclosure statement lets the buyer terminate within 72 hours (in person) or 120 hours (registered mail), and that right dies on transfer (MCL 565.954).",
        "Selling land abutting a road not accepted as public needs a separate written private road notice attached to the conveyance, or the contract is voidable by the purchaser (MCL 560.261).",
    ],
    "national/practice": [
        "Deposits go into the broker's trust account within 2 BANKING DAYS of notice that all parties accepted, and the broker may keep up to $2,000 of its own money in each trust account (MCL 339.2512(k)).",
        "Elliott-Larsen adds AGE, MARITAL STATUS, sexual orientation and gender identity or expression to the federal classes, and disability is covered by a separate act (MCL 37.2502).",
        "The state transfer tax is $3.75 per $500 of value and the SELLER pays it (MCL 207.523, 207.525).",
        "Education: 40 prelicence hours for a salesperson and 90 for a broker, then 18 hours of continuing education a cycle (MCL 339.2504, 339.2504a).",
    ],
}


if __name__ == "__main__":
    import io, json, os
    here = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    out = os.path.join(here, "greprep", "packs", "MI.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    pack = build()
    with io.open(out, "w", encoding="utf-8") as f:
        json.dump(pack, f, ensure_ascii=False, indent=1, sort_keys=True)
    print("wrote", out, len(pack["bank"]), "questions,", len(pack["study"]), "lessons")
