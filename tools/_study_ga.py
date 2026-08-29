# -*- coding: utf-8 -*-
"""Study notes: the Georgia state portion.

Facts drawn from the GREC Real Estate InfoBase (chapters 2-9, 13-22, 27, 39-48)
and O.C.G.A. Title 43 Chapter 40 / Title 10 Chapter 6A as quoted there.
"""

STUDY = {
"georgia/license-law": {
 "summary":
   "The biggest single block on the state portion (14 questions). Three clusters carry "
   "most of it: what you must do to GET and KEEP a licence, what GREC can and cannot do "
   "to you, and the fact that being a licensee never lets you act as an ordinary owner.",
 "sections": [
  {"h": "Getting licensed",
   "l": ["AGE - 18 for salesperson or community association manager; 21 for broker or "
         "associate broker. You may TAKE the salesperson exam at 17 but cannot activate "
         "until 18 (and the broker exam at 20, activating at 21).",
         "EDUCATION - a 75-HOUR GREC-approved salesperson prelicense course. Brokers take "
         "a 60-hour broker prelicense course.",
         "EXAMINATION - pass the Georgia licensing exam (national + state portions).",
         "EXPERIENCE - NONE for a salesperson. For broker or associate broker, an ACTIVE "
         "licence for THREE of the FIVE years immediately preceding application. Active "
         "licensure in ANOTHER state counts, with a certified licence history from every "
         "state where you have held one.",
         "Background check and application fee."]},
  {"h": "Keeping it: the education ladder",
   "l": ["POSTLICENSE - a 25-hour Sales Post-license Course within ONE YEAR of original "
         "licensure. Applies whether you are active or inactive, resident or nonresident. "
         "Miss it and the licence lapses. CE does not substitute for it.",
         "CONTINUING EDUCATION - at least 24 HOURS of GREC-approved CE during each "
         "FOUR-YEAR renewal period. Not annual. Many national guides say 36 hours; that is "
         "a different state.",
         "The sequence to remember: 75 in, 25 in year one, then 24 every four years."]},
  {"h": "Status and administration",
   "l": ["INACTIVE status - you may hold a licence without affiliating, but you still pay "
         "fees and still owe the postlicense requirement. You may not perform licensed acts.",
         "Change of address, broker affiliation, or status is made by filing a CHANGE "
         "APPLICATION with the Commission.",
         "A salesperson acts only through and under the supervision of their affiliated "
         "broker, and may be COMPENSATED ONLY BY THAT BROKER.",
         "NONRESIDENTS who hold no licence at home must meet the same requirements as "
         "Georgia residents and affiliate with a GREC-licensed broker, who may themselves "
         "be resident or nonresident.",
         "Criminal CONVICTIONS must be reported to GREC. Concealment is usually punished "
         "more severely than the underlying offence."]},
  {"h": "The qualifying broker and the firm",
   "l": ["The qualifying broker answers to GREC for the firm's compliance: supervision, "
         "trust accounts, records, and advertising.",
         "FAILURE TO SUPERVISE is an independent violation - the broker can be disciplined "
         "for an affiliate's conduct.",
         "If a qualifying broker is suspended, a corporation or LLC may keep operating if "
         "it IMMEDIATELY designates a replacement; otherwise the firm's licence and all "
         "affiliated licences are suspended for the same period.",
         "Advertising must identify the FIRM and must never suggest a licensee operates "
         "independently of their broker."]},
  {"h": "What GREC can do - and what it cannot",
   "l": ["Members are appointed by the GOVERNOR. GREC administers the licence law, makes "
         "rules, investigates, and disciplines.",
         "SANCTIONS: reprimand, suspension, revocation, fines, required education, and "
         "required reports from an independent accountant on the trust account.",
         "GREC CANNOT order a licensee to repay a consumer's financial loss. There is no "
         "restitution power. A wronged consumer must sue civilly and should not wait for "
         "the investigation to conclude.",
         "GREC also does NOT resolve commission disputes between brokers - those go to "
         "arbitration or the courts."]},
  {"h": "The disciplinary process",
   "l": ["ANYONE may file a sworn written request for investigation, and the Commission may "
         "act ON ITS OWN MOTION. The licensee is notified they are under investigation.",
         "Where a violation caused no significant public harm, GREC may offer a CONSENT "
         "ORDER stating the violation and a proposed sanction. The licensee may sign, "
         "propose an alternative, present evidence, or demand a hearing.",
         "A CONSENT SETTLEMENT fixes agreed findings of fact, conclusions of law, and a "
         "sanction, with no hearing held.",
         "A formal hearing is conducted by an ADMINISTRATIVE LAW JUDGE from the Office of "
         "State Administrative Hearings.",
         "The respondent has THIRTY DAYS to ask the Commission to review the ALJ's "
         "decision; otherwise it becomes final. The Commission has the same 30 days to "
         "request review. From the Commission's final decision, appeal goes to the courts.",
         "Commission staff may not interpret the law for you - that is legal advice."]},
  {"h": "A licensee is never an ordinary owner",
   "p": ["O.C.G.A. 43-40-29(c) provides that NONE of the exceptions to licensure applies "
         "to a person who holds a licence. Selling or leasing your own property means "
         "disclosing your licensed status IN WRITING in the contract or lease, and placing "
         "any trust funds in an account approved by your broker. Georgia also permits NET "
         "LISTINGS only under strict disclosure conditions."]},
 ],
 "vocab": [
  ("GREC", "The Georgia Real Estate Commission; members appointed by the Governor."),
  ("Qualifying broker", "The broker responsible to GREC for a firm's compliance."),
  ("Associate broker", "A broker-licensed individual working under a qualifying broker."),
  ("Prelicense course", "75 hours for salesperson; 60 for broker."),
  ("Postlicense course", "25 hours due within one year of original licensure."),
  ("Continuing education", "24 hours per four-year renewal period."),
  ("Inactive status", "Holding a licence without affiliating; no licensed activity permitted."),
  ("Change application", "The GREC form used to report affiliation or status changes."),
  ("Consent order", "A negotiated resolution stating the violation and sanction, no hearing."),
  ("Consent settlement", "Agreed findings, conclusions and sanction without a hearing."),
  ("Administrative Law Judge", "The OSAH officer who conducts formal GREC hearings."),
  ("Reprimand", "The mildest GREC sanction."),
  ("Revocation", "Permanent loss of licence."),
  ("Net listing", "Broker keeps everything above the seller's stated net; strictly limited in Georgia."),
  ("O.C.G.A.", "Official Code of Georgia Annotated."),
 ],
 "examples": [
  {"t": "Missing the postlicense deadline",
   "s": "A salesperson licensed 14 months ago never took the 25-hour postlicense course, "
        "but did complete some CE.",
   "w": ["The postlicense course is due within ONE year of original licensure.",
         "It applies regardless of active or inactive status.",
         "CE hours do not substitute for it."],
   "k": "The licence lapses. This is a hard deadline with no CE workaround."},
  {"t": "The limit of GREC's power",
   "s": "A consumer loses $18,000 through a licensee's mishandling of funds and files a "
        "complaint with GREC.",
   "w": ["GREC may reprimand, suspend, revoke, fine, and require education or CPA reports.",
         "It has no authority to order repayment of a financial loss.",
         "The consumer must pursue a civil action for the money."],
   "k": "Discipline and compensation are separate tracks. Do not wait for the investigation "
        "before consulting an attorney."},
 ],
 "ga": [],
 "traps": [
  "75 prelicense / 25 postlicense - candidates transpose these constantly.",
  "CE is 24 hours per FOUR YEARS, not per year and not 36.",
  "GREC cannot order restitution, and does not settle commission disputes.",
  "Being a licensee removes, not grants, the ordinary-owner exemptions.",
 ],
},

"georgia/brreta": {
 "summary":
   "BRRETA (the Brokerage Relationships in Real Estate Transactions Act, O.C.G.A. Title 10 "
   "Chapter 6A) is the single biggest difference between Georgia and general agency law. It "
   "was passed because licensees kept creating ACCIDENTAL agency by treating customers like "
   "clients. Its answer: agency requires WRITING, and duties are limited to what the statute "
   "and the engagement specify.",
 "sections": [
  {"h": "The core definitions",
   "l": ["AGENCY - every relationship in which a broker acts for or represents another as a "
         "CLIENT by that person's WRITTEN authority.",
         "BROKERAGE ENGAGEMENT - the written contract by which a seller, buyer, landlord or "
         "tenant becomes the broker's client.",
         "CLIENT - a person represented under a brokerage engagement.",
         "CUSTOMER - a person NOT represented, for whom the broker may perform MINISTERIAL "
         "ACTS under either a verbal or written agreement.",
         "MINISTERIAL ACTS - acts that do not require discretion or the exercise of the "
         "broker's own judgement."]},
  {"h": "The point that changes everything",
   "p": ["O.C.G.A. 10-6A-4(a): a broker owes a client or customer ONLY the duties set out in "
         "the chapter, unless the parties expressly agree otherwise in a signed writing. A "
         "broker SHALL NOT BE DEEMED to have a fiduciary relationship with any party, and is "
         "responsible only for exercising REASONABLE CARE in discharging the specified "
         "duties. Georgia deliberately narrowed common-law fiduciary exposure."]},
  {"h": "Compensation does not create agency",
   "p": ["Paying the commission does not make you the payer's client. A seller paying the "
         "buyer's broker out of closing proceeds does not make that broker the seller's "
         "agent. Only an express written agreement creates the engagement. This is heavily "
         "tested because intuition runs the other way."]},
  {"h": "Disclosures before or within the engagement",
   "p": ["Before entering into a brokerage engagement, the broker must advise the "
         "prospective client of FOUR things:"],
   "l": ["The types of agency relationships available through the broker",
         "Any brokerage relationships the broker holds with other parties that would "
         "CONFLICT with the prospective client's interests and are actually known - but "
         "EXPRESSLY EXCLUDING the fact that the broker may represent other sellers or "
         "landlords, or other buyers or tenants, generally",
         "The broker's compensation and whether it will be shared with other brokers",
         "The broker's obligations to keep information confidential",
         "BRRETA does not require the agency conversation before the engagement, but the "
         "InfoBase urges having it as early as possible so a customer never presumes they "
         "are represented."]},
  {"h": "Duration and termination",
   "p": ["The engagement begins when the client engages the broker and runs until the "
         "agreed expiration date or another statutory ending event. GREC requires a "
         "DEFINITE expiration date, and automatic renewal clauses are prohibited."]},
  {"h": "Dual agency",
   "p": ["A DUAL AGENT is a broker who simultaneously has a client relationship with both "
         "sides of the same transaction. Georgia ALLOWS it with WRITTEN consent. Consent is "
         "presumed where the writing contains:"],
   "l": ["A description of the transactions or types of transactions involved",
         "A statement that the broker represents two clients whose interests are, or at "
         "times could be, different or even adverse",
         "A statement that the dual agent will disclose all ADVERSE MATERIAL FACTS actually "
         "known - EXCEPT information made confidential by a client's request or instruction",
         "A statement that the client does NOT have to consent to the dual agency",
         "A statement that the consent has been given voluntarily and the writing has been read "
         "and understood",
         "The practical rule: a dual agent discloses adverse material FACTS, never a "
         "client's negotiating POSITION."]},
  {"h": "Designated agency - a genuine Georgia distinction",
   "p": ["A broker may assign different affiliated licensees as DESIGNATED AGENTS to "
         "represent opposing clients in the same transaction, directly or through company "
         "policy. Each designated agent owes their own client the full statutory duties."],
   "l": ["10-6A-13(b): where designated agents are appointed, NEITHER the broker, NOR the "
         "broker's licensees, NOR the firm is deemed a dual agent. Many other states treat "
         "this as firm-wide dual agency; Georgia does not.",
         "10-6A-13(c): there is NO IMPUTATION of knowledge between broker, designated "
         "agents, and clients - each is treated as having only their own actual knowledge.",
         "A designated agent may not disclose confidential client information except to "
         "their BROKER, and the broker in turn may not reveal it.",
         "Confidential information means anything whose disclosure the client has not "
         "consented to that could harm the client's negotiating position."]},
 ],
 "vocab": [
  ("BRRETA", "Brokerage Relationships in Real Estate Transactions Act, O.C.G.A. Title 10 Ch. 6A."),
  ("Brokerage engagement", "The written contract making someone a broker's client."),
  ("Client", "A represented party under a brokerage engagement."),
  ("Customer", "An unrepresented party for whom ministerial acts may be performed."),
  ("Ministerial acts", "Acts requiring no discretion or judgement by the broker."),
  ("Dual agent", "A broker with client relationships on both sides of one transaction."),
  ("Designated agent", "A licensee assigned to represent one client exclusively in a transaction."),
  ("Adverse material fact", "A known fact that would materially affect the transaction."),
  ("Confidential information", "Information a client has not consented to disclose that could harm their position."),
  ("Imputation of knowledge", "Attributing one person's knowledge to another; removed for designated agency."),
 ],
 "examples": [
  {"t": "Weeks of help, no agency",
   "s": "A buyer works with a licensee for weeks. The licensee advises on price and "
        "negotiation. Nothing is ever signed.",
   "w": ["BRRETA defines agency as representation by WRITTEN authority.",
         "With no brokerage engagement there is no agency relationship.",
         "But the licensee has behaved far outside the customer role."],
   "k": "Legally no agency - which is exactly why the statute exists. Practically, this is "
        "the situation that invites a lawsuit, so clarify status early."},
  {"t": "Designated agency is not dual agency",
   "s": "A broker assigns one licensee to the buyer and another to the seller in the same "
        "deal.",
   "w": ["Each designated agent owes their own client the full statutory duties.",
         "10-6A-13(b) says neither the broker, the licensees, nor the firm is a dual agent.",
         "10-6A-13(c) removes imputed knowledge between them."],
   "k": "This is a real Georgia difference. In many states the same facts would create "
        "firm-wide dual agency."},
  {"t": "The dual agent's bind",
   "s": "A seller privately tells her broker she will take $20,000 less. The broker is a "
        "dual agent and the buyer asks about flexibility.",
   "w": ["A dual agent must disclose adverse material FACTS actually known.",
         "A negotiating position is not a material fact; it is confidential.",
         "The client asked that it be kept confidential."],
   "k": "Keep it confidential. Hinting is the same disclosure by another route."},
 ],
 "ga": [],
 "traps": [
  "Compensation never creates agency in Georgia.",
  "A broker is expressly NOT a fiduciary under BRRETA - only reasonable care in specified duties.",
  "Designated agency does NOT make the broker a dual agent.",
  "The four pre-engagement disclosures exclude having to reveal other buyer/seller clients.",
 ],
},

"georgia/trust-accounts": {
 "summary":
   "Trust account rules exist to keep the public's money separate from the broker's, and "
   "they survive the broker's death, bankruptcy, divorce, and judgments. Nearly every "
   "question here is about separation, prompt deposit, or paperwork.",
 "sections": [
  {"h": "Why the account exists",
   "p": ["A properly maintained trust account protects client money regardless of the "
         "broker's own finances. Per the InfoBase, funds in it:"],
   "l": ["Do NOT become part of the broker's estate on death",
         "Are NOT subject to attachment or garnishment from a judgment against the broker",
         "Do NOT go to creditors in the broker's bankruptcy",
         "Are not available to accidentally cover shortfalls in the firm's operating account"]},
  {"h": "Setting it up",
   "l": ["A SEPARATE, FEDERALLY INSURED bank CHECKING account that the BANK designates as "
         "a trust or escrow account.",
         "Registered with the Commission at the time of broker application, and the broker "
         "must have SIGNATORY POWER.",
         "It may be interest-bearing or non-interest-bearing, but funds are deposited into "
         "a NON-interest-bearing account unless all parties authorise otherwise in writing.",
         "Open it under an EMPLOYER IDENTIFICATION NUMBER, not the broker's Social Security "
         "Number. The InfoBase records accounts seized by the IRS for a broker's personal "
         "tax debt, awarded in a divorce, and attached by a bank - the common thread was an "
         "account opened under the broker's SSN.",
         "A broker must have AT LEAST ONE and may have several - commonly separate accounts "
         "for earnest money, rents, and security deposits. Each must be bank-designated and "
         "registered."]},
  {"h": "Prompt deposit",
   "p": ["The law requires trust funds to be deposited PROMPTLY. To do anything else - hold "
         "a check until the offer is accepted, take a postdated check, accept personal "
         "property instead of money, or use an interest-bearing account - the broker needs "
         "CLEAR WRITTEN AUTHORITY agreed to by ALL parties, not just the one who asked. "
         "Once deposited, funds stay there until the transaction is consummated or terminated."]},
  {"h": "What counts as trust money",
   "l": ["Earnest money and other deposits",
         "RENTS collected for an owner",
         "SECURITY, damage, cleaning, key deposits, and last month's rent",
         "Payments collected on land contracts or wraparound mortgages on licensee-owned property",
         "Any funds advanced by a party for expenses - appraisals, credit reports, repairs",
         "Closing funds the broker collects and disburses",
         "NOT trust money: commission properly earned and disbursed after closing."]},
  {"h": "FDIC coverage",
   "p": ["The FDIC insures $250,000 per account owner per bank. Trust accounts get "
         "PASS-THROUGH coverage - each buyer, seller, or tenant is treated as a separate "
         "owner - but only if the broker meets the recordkeeping requirements. The catch: "
         "the FDIC ADDS that person's other deposits at the SAME bank. A client already at "
         "$250,000 in that bank has no coverage for their deposit, and the InfoBase warns "
         "the broker may be liable for the uninsured excess if the client was not told which "
         "bank holds the funds."]},
  {"h": "Records, audits, and affiliates",
   "l": ["Written notice to GREC, on Commission forms, whenever the bank, account name, or "
         "account number changes, the bank changes names, or the account closes.",
         "GREC may EXAMINE trust accounts on reasonable request and does so routinely. It "
         "MAY, at its discretion, accept a CPA's certification of compliance instead.",
         "A nonresident broker may keep the account in their home state if they authorise "
         "GREC to examine it.",
         "If a broker lets an affiliate maintain an account for the affiliate's own rentals, "
         "the broker must REGISTER it with GREC, remains RESPONSIBLE for it, and the "
         "affiliate must supply at least QUARTERLY written reconciliation statements "
         "comparing total trust liability with the reconciled bank balance."]},
  {"h": "Disputes",
   "p": ["When buyer and seller both demand the deposit, the broker must not choose a side. "
         "Hold the funds and use interpleader or the prescribed procedure. Releasing, "
         "splitting, or keeping it all invite a conversion claim."]},
 ],
 "vocab": [
  ("Trust account", "A separate, federally insured, bank-designated account for client funds."),
  ("Escrow", "Money or documents held by a neutral party pending closing."),
  ("Commingling", "Mixing trust funds with the broker's own money."),
  ("Conversion", "Using or spending trust funds."),
  ("Signatory power", "The broker's authority to sign on the account; required."),
  ("EIN", "Employer Identification Number; trust accounts should be opened under one."),
  ("Pass-through coverage", "FDIC treatment of each client as a separate insured owner."),
  ("Reconciliation", "Comparing total trust liability against the bank balance."),
  ("Interpleader", "A court action to resolve competing claims to held funds."),
 ],
 "examples": [
  {"t": "Holding a check needs everyone's signature",
   "s": "A buyer asks the broker to hold the earnest money check uncashed until the seller "
        "accepts.",
   "w": ["The default rule is prompt deposit into a non-interest-bearing account.",
         "Any deviation requires clear WRITTEN authority.",
         "It must be agreed by ALL parties - the seller has an interest in the deposit too."],
   "k": "The buyer's verbal request is not enough. Get it in writing from everyone, "
        "normally as a stipulation in the offer."},
  {"t": "The FDIC gap",
   "s": "A client already has $250,000 at XYZ Bank and gives the broker a $10,000 deposit. "
        "The broker's trust account is also at XYZ. The bank fails.",
   "w": ["Pass-through treats the client as a separate owner - but the FDIC AGGREGATES "
         "their deposits at that bank.",
         "The client is at $260,000 total, so $10,000 is uninsured.",
         "The InfoBase warns the broker may be liable for it if the bank was not disclosed."],
   "k": "Tell clients which bank holds trust funds and mention the $250,000 limit."},
 ],
 "ga": [],
 "traps": [
  "'Promptly' is the standard; written authority from ALL parties is the only way around it.",
  "EIN, not SSN. This is the difference between a protected account and a seizable one.",
  "Commission is only the broker's money AFTER it is properly earned and disbursed.",
  "GREC MAY accept a CPA report - the broker can request it, not demand it.",
 ],
},

"georgia/contracts": {
 "summary":
   "Georgia contract questions turn on three things: WHEN the contract became binding, "
   "what the DUE DILIGENCE period lets the buyer do, and where a licensee's authority to "
   "fill in a form ends and the practice of law begins.",
 "sections": [
  {"h": "The binding agreement date",
   "p": ["A Georgia contract becomes binding when ACCEPTANCE IS COMMUNICATED to the offeror "
         "- not when the seller signs. Every subsequent deadline (due diligence, financing, "
         "closing) is measured from that BINDING AGREEMENT DATE, so getting it wrong shifts "
         "the whole timeline. An offer may be revoked any time before acceptance is "
         "communicated."]},
  {"h": "Due diligence",
   "p": ["Georgia's standard due diligence provision gives the buyer a set number of days to "
         "inspect and, under the common forms, to TERMINATE FOR ANY REASON OR NO REASON and "
         "recover the earnest money. That latitude is why the length is negotiated hard. "
         "Once it expires the buyer's exit rights narrow sharply and the earnest money is "
         "genuinely at risk."]},
  {"h": "Form filling vs. practising law",
   "l": ["A licensee MAY complete the blanks on approved preprinted forms incident to a "
         "transaction they are handling.",
         "A licensee MAY NOT draft original clauses or give legal advice about them - that "
         "is the unauthorised practice of law.",
         "Handwritten or typed SPECIAL STIPULATIONS PREVAIL over conflicting preprinted "
         "text, because they show the parties' specific intent. That is exactly why a badly "
         "drafted stipulation is dangerous: it controls the deal.",
         "Complex terms - owner financing, unusual contingencies - belong with an attorney."]},
  {"h": "Description and definiteness",
   "p": ["Georgia courts require a description that identifies the property with reasonable "
         "certainty, or provides a 'key' leading to identification. A vague description can "
         "make the contract unenforceable for indefiniteness."]},
  {"h": "Listing agreements",
   "l": ["Must be IN WRITING with a DEFINITE EXPIRATION DATE.",
         "AUTOMATIC RENEWAL clauses are prohibited - a broker cannot roll a listing forward "
         "by default.",
         "An engagement with no ending date is a licence-law violation for the broker, "
         "separate from whether the client minds."]},
  {"h": "Earnest money and default",
   "p": ["Where the contract provides liquidated damages, the seller normally retains the "
         "earnest money as the agreed measure of loss. To be enforceable rather than a "
         "penalty it must be a reasonable pre-estimate of damages, damages must be hard to "
         "determine, and the parties must have intended it as liquidated damages."]},
  {"h": "Contingencies you will see",
   "l": ["Financing - buyer may terminate if the stated loan cannot be obtained.",
         "Appraisal - protects against the property valuing below the price.",
         "Sale of buyer's property - usually paired with a KICK-OUT clause letting the "
         "seller keep marketing and requiring the buyer to remove the contingency or "
         "terminate within a short window.",
         "Inspection / due diligence.",
         "'Time is of the essence' makes each stated date strict."]},
 ],
 "vocab": [
  ("Binding agreement date", "The date acceptance is communicated; all deadlines run from it."),
  ("Due diligence period", "The buyer's window to inspect and, typically, terminate for any reason."),
  ("Special stipulation", "A typed or handwritten term that prevails over preprinted text."),
  ("Unauthorised practice of law", "Drafting legal instruments or advising on them without a licence."),
  ("Kick-out clause", "Lets a seller continue marketing while a buyer's sale contingency is pending."),
  ("Liquidated damages", "An agreed sum, usually the earnest money, as the measure of loss."),
  ("Definiteness", "The requirement that a contract identify the property with reasonable certainty."),
 ],
 "examples": [
  {"t": "When the clock actually starts",
   "s": "The seller signs the buyer's offer Tuesday. The agent does not notify the buyer "
        "until Thursday.",
   "w": ["Signing is not acceptance in the legal sense.",
         "Acceptance is effective when COMMUNICATED to the offeror.",
         "That happened Thursday."],
   "k": "Thursday is the binding agreement date, and every deadline in the contract counts "
        "from there - not Tuesday."},
  {"t": "A stipulation beats the form",
   "s": "A licensee types a special stipulation that conflicts with the preprinted contract "
        "language. A dispute follows.",
   "w": ["Preprinted text is generic; typed terms show what these parties actually agreed.",
         "Courts give effect to the specific over the general.",
         "So the stipulation controls."],
   "k": "Which is why drafting them casually is risky - and why original clauses belong "
        "with an attorney."},
 ],
 "ga": [],
 "traps": [
  "Binding agreement date = communication of acceptance, not signature.",
  "During due diligence the buyer generally does NOT need a reason to terminate.",
  "Listings need a definite end date; automatic renewals are prohibited.",
 ],
},

"georgia/disclosures": {
 "summary":
   "Georgia's disclosure rules are narrower than most states'. The duty is to adverse "
   "material facts ACTUALLY KNOWN - there is no duty to investigate - and Georgia expressly "
   "protects licensees who stay silent about stigma. What is never protected is an "
   "affirmative lie.",
 "sections": [
  {"h": "The scope of the duty",
   "p": ["Under BRRETA a broker must disclose ADVERSE MATERIAL FACTS actually known, and "
         "this duty runs to CUSTOMERS as well as clients. There is NO DUTY TO DISCOVER: "
         "brokers are not inspectors and need not investigate. But a licensee may not ignore "
         "what is plainly visible, and may not pass along information they know to be false."]},
  {"h": "Stigmatized property",
   "p": ["Georgia expressly shields licensees from liability for NOT disclosing that a "
         "property was the site of a death, homicide, suicide, or felony. The protection "
         "covers NONDISCLOSURE. It does not license a denial. If a buyer asks directly and "
         "you know, decline to answer and point them to public sources - denying it would "
         "be misrepresentation."]},
  {"h": "Who fills in the form",
   "p": ["The SELLER completes Georgia's property disclosure statement from personal "
         "knowledge. A licensee should never complete it for the seller or guess at answers "
         "- doing so transfers the seller's liability onto the licensee. If the licensee "
         "knows an answer is false, they cannot market the property on that basis; if the "
         "seller will not correct it, withdraw."]},
  {"h": "What must be disclosed",
   "l": ["Known physical defects affecting value, safety, or use - roof, foundation, "
         "septic, systems, water intrusion (including repaired history)",
         "Flood plain location, which affects value, insurability, and lender requirements",
         "Federal lead-based paint disclosure for housing built before 1978, with records, "
         "the EPA pamphlet, and a 10-day testing opportunity",
         "A licensee's own LICENSED STATUS, in writing, whenever acting as a principal"]},
  {"h": "What must not be disclosed",
   "p": ["Anything touching a protected class. A former occupant's HIV/AIDS status is "
         "protected as handicap; the demographic makeup of a neighbourhood is off limits "
         "because answering steers."]},
 ],
 "vocab": [
  ("Adverse material fact", "A known fact materially affecting the property or transaction."),
  ("No duty to discover", "Georgia's rule that brokers need not investigate for defects."),
  ("Property disclosure statement", "The seller's written statement of known conditions."),
  ("Stigmatized property", "Property affected by events rather than physical condition."),
  ("Licensee-as-principal disclosure", "Written disclosure of licensed status when buying or selling for yourself."),
 ],
 "examples": [
  {"t": "Silence is protected; lying is not",
   "s": "A buyer asks the listing agent directly whether anyone died in the house. The "
        "agent knows someone did.",
   "w": ["Georgia protects NONDISCLOSURE of a death on the property.",
         "It does not protect an affirmative false statement.",
         "Denying it would be misrepresentation."],
   "k": "Decline to answer and refer the buyer to sources they can research. That keeps "
        "you inside the protection."},
 ],
 "ga": [],
 "traps": [
  "Physical condition must be disclosed; stigma generally need not.",
  "The duty covers what you ACTUALLY KNOW - but it runs to customers too.",
  "Never complete the seller's disclosure form for them.",
 ],
},

"georgia/procedures": {
 "summary":
   "Closing and conveyancing in Georgia differ from the national norm in several specific "
   "ways, and the exam tests exactly those differences: attorney closings, security deeds, "
   "nonjudicial foreclosure, transfer tax, January 1 tax liens, and no tenancy by the entirety.",
 "sections": [
  {"h": "Attorney closings",
   "p": ["Georgia requires a licensed ATTORNEY to supervise the closing, because examining "
         "title and preparing conveyance documents is the practice of law. That attorney "
         "customarily represents the LENDER. A buyer who wants their own advocate must "
         "retain separate counsel - and a licensee should say so plainly rather than letting "
         "the buyer assume otherwise."]},
  {"h": "The security deed",
   "p": ["Georgia's security instrument is a SECURITY DEED (deed to secure debt). Unlike a "
         "mortgage, which creates only a lien, it conveys LEGAL TITLE to the lender until "
         "the debt is paid. This is what makes Georgia a title-theory state and enables fast "
         "nonjudicial foreclosure."]},
  {"h": "Foreclosure",
   "l": ["Georgia foreclosure is NONJUDICIAL, under the power of sale in the security deed.",
         "Notice to the borrower, plus ADVERTISEMENT in the county LEGAL ORGAN, customarily "
         "for four weeks.",
         "Public sale on the courthouse steps on the FIRST TUESDAY of the month.",
         "A deficiency requires court confirmation of the sale."]},
  {"h": "Transfer tax and recording",
   "l": ["Georgia real estate TRANSFER TAX is $1.00 per $1,000 of consideration (0.10%). "
         "Customarily paid by the SELLER.",
         "Collected by the CLERK OF SUPERIOR COURT when the deed is recorded.",
         "Deeds, security deeds, and plats are recorded with the clerk of superior court in "
         "the county where the land lies, giving constructive notice.",
         "There is also an intangible recording tax on long-term notes."]},
  {"h": "Taxes and prorations",
   "p": ["Georgia property taxes become a LIEN ON JANUARY 1 of the tax year and follow the "
         "property regardless of who owned it when they accrued. That is why closings "
         "prorate them. Unpaid taxes produce a SELLER DEBIT and BUYER CREDIT."]},
  {"h": "Ownership rules that differ",
   "l": ["Georgia does NOT recognise tenancy by the entirety. Spouses wanting survivorship "
         "hold as JOINT TENANTS WITH RIGHT OF SURVIVORSHIP, stated expressly.",
         "Adverse possession: 20 YEARS, or 7 YEARS under COLOUR OF TITLE.",
         "Georgia subdivisions are usually described by LOT AND BLOCK from a recorded plat; "
         "Georgia does not use the rectangular survey system."]},
  {"h": "At the table",
   "p": ["TRID applies: the Closing Disclosure must be received at least three business days "
         "before consummation. The closing attorney disburses, records, and issues title "
         "insurance."]},
 ],
 "vocab": [
  ("Security deed", "Georgia's instrument conveying title to the lender as security."),
  ("Title theory", "The doctrine that the lender holds legal title until the debt is paid."),
  ("Power of sale", "The clause permitting nonjudicial foreclosure."),
  ("Legal organ", "The county newspaper designated for official legal advertisements."),
  ("Confirmation of sale", "Court approval required before pursuing a deficiency in Georgia."),
  ("Transfer tax", "$1.00 per $1,000 of consideration, customarily paid by the seller."),
  ("Intangible recording tax", "A Georgia tax on long-term notes secured by real estate."),
  ("Clerk of superior court", "The county officer with whom Georgia land records are filed."),
  ("Colour of title", "A defective written instrument that appears to convey title."),
 ],
 "examples": [
  {"t": "Who does the closing attorney work for?",
   "s": "At closing the buyer asks the attorney whether the repair clause protects them.",
   "w": ["Georgia requires attorney supervision of the closing.",
         "That attorney customarily represents the LENDER, not the buyer.",
         "The licensee must not supply a legal opinion either."],
   "k": "Say plainly that the attorney represents the lender and the buyer may retain their "
        "own counsel. Letting the buyer assume otherwise is a costly misunderstanding."},
  {"t": "Seven years, not twenty",
   "s": "A neighbour has openly occupied a strip of land for 12 years under a deed they "
        "believed valid but which was defective.",
   "w": ["A defective instrument that appears to convey title is COLOUR OF TITLE.",
         "With colour of title Georgia's period is 7 years, not 20.",
         "Twelve years exceeds it."],
   "k": "The claim is complete. Without colour of title they would have needed 20 years."},
 ],
 "ga": [],
 "traps": [
  "Georgia is an attorney-closing state, not an escrow state.",
  "Security deed, not mortgage; nonjudicial foreclosure, first Tuesday.",
  "$1.00 per $1,000 - divide the price by 1,000. Not 1% and not $0.10.",
  "Tax lien attaches January 1, regardless of when the bill arrives.",
 ],
},

"georgia/fair-housing": {
 "summary":
   "Georgia enforces the federal Fair Housing Act, and GREC can independently discipline a "
   "licensee for discriminatory conduct. The exam focuses on recognising steering and "
   "blockbusting in realistic wording, and on the accommodation/modification split.",
 "sections": [
  {"h": "The seven federal classes",
   "p": ["Race, colour, religion, sex, national origin, familial status, handicap. Source of "
         "income and marital status are not among them federally, though some Georgia local "
         "ordinances protect source of income and a blanket policy can still create "
         "disparate-impact exposure."]},
  {"h": "Steering and blockbusting in practice",
   "l": ["STEERING does not require saying anything negative. Providing school ratings and "
         "crime statistics only to certain buyers, or 'you'd be more comfortable over here', "
         "both steer. Use a consistent policy for every buyer and point everyone to the same "
         "public sources.",
         "BLOCKBUSTING is inducing sales by suggesting a protected group's arrival will harm "
         "the neighbourhood. Illegal whether or not the statement is true.",
         "Advertising must describe the PROPERTY, not the desired occupant. 'Mature Christian "
         "couple' signals age/familial status and religion; 'no children under 12' is a "
         "direct familial status violation."]},
  {"h": "Disability: two different duties",
   "l": ["REASONABLE MODIFICATION - a PHYSICAL change (grab bar, ramp, doorbell light). "
         "Permitted at the TENANT'S expense, with possible restoration on move-out.",
         "REASONABLE ACCOMMODATION - a change to RULES or policies (waiving a no-pets rule "
         "for an assistance animal). At the HOUSING PROVIDER'S expense.",
         "An assistance animal is not a pet: no pet fee or pet deposit may be charged, "
         "though the tenant remains liable for actual damage."]},
  {"h": "Unlawful client instructions",
   "p": ["The duty of obedience covers LAWFUL instructions only. A seller who directs you to "
         "exclude a protected class must be refused, and if they persist you WITHDRAW. "
         "Quietly ignoring the instruction leaves you working for someone who will "
         "discriminate; handing the seller to a colleague simply relocates the violation."]},
  {"h": "Enforcement",
   "p": ["HUD handles federal complaints, generally within one year. Private suits are "
         "available. Separately, GREC can discipline the licence - so one act of "
         "discrimination can produce a HUD case, a lawsuit, and a licence sanction."]},
 ],
 "vocab": [
  ("Fair Housing Act", "The federal law barring housing discrimination on seven grounds."),
  ("Familial status", "Households with children under 18, pregnant people, those securing custody."),
  ("Handicap", "Disability, including HIV/AIDS; a protected class."),
  ("Steering", "Channelling people toward or away from areas by protected class."),
  ("Blockbusting", "Inducing sales with claims about a protected group moving in."),
  ("Redlining", "Refusing or pricing loans by area demographics."),
  ("Reasonable modification", "A physical change at the tenant's expense."),
  ("Reasonable accommodation", "A rules change at the provider's expense."),
  ("Assistance animal", "Not a pet; no pet fee may be charged."),
  ("Disparate impact", "A neutral policy with discriminatory effect."),
  ("Housing for older persons", "The narrow exemption from familial status protection."),
 ],
 "examples": [
  {"t": "Helpful, and still steering",
   "s": "A licensee provides school ratings and crime statistics only when buyers of a "
        "certain background ask for them.",
   "w": ["Nothing negative was said about any area.",
         "But information was delivered selectively by who was asking.",
         "Selective information channels buyers just as effectively as a recommendation."],
   "k": "Steering. Adopt one policy for everyone - typically pointing all buyers to the "
        "same public sources."},
  {"t": "No pet fee for an assistance animal",
   "s": "A manager charges a $300 non-refundable fee to every tenant with an assistance "
        "animal, applied uniformly.",
   "w": ["Uniform application does not save it.",
         "Waiving the pet policy is a reasonable ACCOMMODATION at the provider's expense.",
         "Charging a fee defeats the accommodation."],
   "k": "Unlawful. The tenant is still liable for actual damage the animal causes."},
 ],
 "ga": [],
 "traps": [
  "Steering can happen through selective helpfulness, with no negative statement at all.",
  "Modification = physical = tenant pays. Accommodation = rules = provider absorbs.",
  "Refusing an unlawful instruction is not enough if you keep the listing - withdraw.",
 ],
},
}
