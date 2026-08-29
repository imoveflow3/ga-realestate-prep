# -*- coding: utf-8 -*-
"""Study notes: financing, agency, property disclosures."""

STUDY = {
"national/financing": {
 "summary":
   "Two documents do two jobs: the NOTE is the promise to repay, the SECURITY INSTRUMENT "
   "pledges the property. Everything else - clauses, loan types, disclosure rules - hangs "
   "off that split. Georgia uses a security deed rather than a mortgage.",
 "sections": [
  {"h": "The two documents",
   "l": ["Promissory note - the borrower's personal promise to repay. This is the debt.",
         "Security instrument - pledges the property as collateral. A MORTGAGE creates a "
         "lien in most states. A DEED OF TRUST adds a third party, the TRUSTEE, who holds "
         "title for the lender and can sell without a lawsuit. GEORGIA uses a SECURITY "
         "DEED (deed to secure debt), which passes legal title to the lender until payoff.",
         "Mortgagor = borrower. Mortgagee = lender. The '-or' gives, the '-ee' receives."]},
  {"h": "Clauses you must recognise",
   "l": ["Acceleration - on DEFAULT the whole balance becomes due. A prerequisite to "
         "foreclosure.",
         "Alienation (due-on-sale) - on TRANSFER the whole balance becomes due. Triggered "
         "by sale, not default.",
         "Defeasance - requires the lender to release the lien when the debt is paid.",
         "Subordination - voluntarily moves a lien to lower priority, so a construction "
         "lender can take first position.",
         "Prepayment penalty - a charge for paying early.",
         "Release (partial release) - in a blanket mortgage, frees individual lots as "
         "portions of the debt are paid."]},
  {"h": "Taking over an existing loan",
   "l": ["ASSUMPTION - the buyer becomes PRIMARILY liable; the seller stays SECONDARILY "
         "liable until the lender grants a release.",
         "NOVATION - the lender substitutes the new borrower and RELEASES the original. "
         "Only a novation frees the seller.",
         "'SUBJECT TO' - the buyer takes title but accepts NO personal liability. On "
         "default the buyer loses the property; the ORIGINAL borrower still owes any "
         "deficiency."]},
  {"h": "Amortization",
   "l": ["Fully amortized - level payments retire principal and interest by maturity.",
         "Partially amortized - level payments leave a BALLOON at the end.",
         "Term (straight) loan - interest only, principal due at the end.",
         "In an amortized loan the INTEREST portion shrinks and the principal portion "
         "grows with each payment. Interest for one month = balance x annual rate / 12."]},
  {"h": "Points, yield, and LTV",
   "l": ["One discount point = 1% of the LOAN AMOUNT, never the sale price.",
         "Points are prepaid interest that raise the lender's YIELD, letting the borrower "
         "take a lower note rate. Roughly 8 points move the yield about 1%.",
         "Origination fee compensates the lender for making the loan; also a % of the loan.",
         "LTV = loan / value, where value is the LESSER of sale price and appraised value.",
         "Conventional loans above 80% LTV require PMI, which protects the LENDER. FHA "
         "carries MIP instead; VA carries a funding fee and no monthly mortgage insurance."]},
  {"h": "Loan programmes",
   "l": ["Conventional - not government backed. Conforming loans meet Fannie/Freddie limits.",
         "FHA - insured by FHA, low down payment, MIP required.",
         "VA - guaranteed for eligible veterans, no down payment, funding fee. Entitlement "
         "stays committed until the loan is paid or another veteran substitutes theirs.",
         "ARM - rate = INDEX + MARGIN, adjusted periodically with periodic and lifetime caps. "
         "The margin is the lender's constant markup; the index moves with the market.",
         "Purchase-money mortgage - seller financing taken back at the sale.",
         "Blanket - covers multiple parcels, with a release clause.",
         "Package - includes personal property.",
         "Open-end - lets the borrower re-borrow up to a limit.",
         "Wraparound - a new loan wrapped around an existing one the seller keeps paying.",
         "Construction loan - short term, paid out in draws."]},
  {"h": "The markets",
   "p": ["The PRIMARY market originates loans to consumers. The SECONDARY market - Fannie "
         "Mae, Freddie Mac, Ginnie Mae - BUYS existing loans, returning cash to lenders so "
         "they can lend again. Consumers never deal with the secondary market directly."]},
  {"h": "Consumer protection law",
   "l": ["TILA / Regulation Z - discloses the cost of credit, including the APR, and "
         "governs trigger terms in advertising.",
         "RESPA - governs settlement services. Section 8 bans paying or receiving anything "
         "of value for the mere REFERRAL of settlement business. Fees for services actually "
         "performed are fine.",
         "TRID timing - Loan Estimate within 3 business days of APPLICATION; Closing "
         "Disclosure received at least 3 business days before CONSUMMATION.",
         "Only three changes restart the 3-day CD clock: the APR becomes inaccurate beyond "
         "tolerance, the LOAN PRODUCT changes, or a PREPAYMENT PENALTY is added.",
         "ECOA - bars discrimination in lending on race, colour, religion, national origin, "
         "sex, marital status, age, or receipt of public assistance. A denied applicant is "
         "entitled to SPECIFIC reasons, or notice of the right to request them within 60 days.",
         "Usury laws cap the maximum lawful interest rate."]},
 ],
 "vocab": [
  ("Promissory note", "The borrower's written promise to repay the debt."),
  ("Security deed", "Georgia's instrument conveying title to the lender as security."),
  ("Deed of trust", "A three-party security instrument using a trustee."),
  ("Mortgagor / mortgagee", "Borrower / lender."),
  ("Acceleration clause", "Makes the entire balance due on default."),
  ("Alienation clause", "Due-on-sale; makes the balance due on transfer."),
  ("Defeasance clause", "Requires release of the lien when the debt is paid."),
  ("Subordination", "Voluntarily lowering a lien's priority."),
  ("Assumption", "Buyer takes over the loan and becomes primarily liable."),
  ("Novation", "Substituting a new party and releasing the original."),
  ("Subject to", "Taking title without personal liability on the loan."),
  ("Deficiency judgment", "A judgment for the shortfall after a foreclosure sale."),
  ("Fully amortized loan", "Level payments that retire the debt by maturity."),
  ("Balloon payment", "A large final payment on a partially amortized loan."),
  ("Discount point", "1% of the loan amount, paid to raise the lender's yield."),
  ("Origination fee", "A lender's charge for making the loan, as a % of the loan."),
  ("Loan-to-value (LTV)", "Loan divided by the lesser of price or appraised value."),
  ("PMI", "Private mortgage insurance on conventional loans above 80% LTV; protects the lender."),
  ("MIP", "FHA's mortgage insurance premium."),
  ("Funding fee", "The VA's one-time charge in place of mortgage insurance."),
  ("Index and margin", "An ARM's moving benchmark plus the lender's fixed markup."),
  ("Purchase-money mortgage", "Seller financing taken back at closing."),
  ("Blanket mortgage", "One loan covering several parcels, with a release clause."),
  ("Wraparound mortgage", "A new loan encompassing an existing one that stays in place."),
  ("Primary market", "Where loans are originated to consumers."),
  ("Secondary market", "Where existing loans are bought and sold, providing liquidity."),
  ("Regulation Z", "TILA's implementing rule; governs APR and credit advertising."),
  ("RESPA", "Governs settlement services and bans kickbacks for referrals."),
  ("Loan Estimate", "TRID disclosure due within 3 business days of application."),
  ("Closing Disclosure", "TRID form the borrower must receive 3 business days before closing."),
  ("ECOA", "Equal Credit Opportunity Act; bars discrimination in lending."),
  ("Usury", "Charging interest above the legal maximum."),
 ],
 "examples": [
  {"t": "Who owes the deficiency?",
   "s": "A buyer takes title 'subject to' the seller's existing loan, then defaults. "
        "Foreclosure leaves a $40,000 shortfall.",
   "w": ["'Subject to' means the buyer never promised to pay the note.",
         "The buyer's only exposure was losing the property, which has happened.",
         "The ORIGINAL borrower's promise is still outstanding."],
   "k": "The seller-borrower owes the deficiency. Had the buyer ASSUMED, both would be "
        "liable - buyer primarily, seller secondarily - unless a novation released the seller."},
  {"t": "Do the points pay for themselves?",
   "s": "6.5% with no points, or 6.0% with 2 points on a $300,000 loan.",
   "w": ["Points cost 2% x $300,000 = $6,000.",
         "Rate saving is 0.5% x $300,000 = $1,500 in the first year.",
         "$6,000 / $1,500 = 4 years to break even."],
   "k": "Buy the points only if you will hold the loan longer than about four years."},
  {"t": "The appraisal gap",
   "s": "Contract price $310,000; appraisal comes in at $300,000; the loan is 80% LTV. "
        "There is no appraisal contingency.",
   "w": ["The lender lends on the LESSER figure: 80% x $300,000 = $240,000.",
         "The buyer still owes the contract price of $310,000.",
         "$310,000 - $240,000 = $70,000 due in cash."],
   "k": "The buyer must cover the $10,000 gap on top of the normal down payment, and "
        "without a contingency has no automatic right to walk."},
 ],
 "ga": [
  "Georgia uses a SECURITY DEED, which conveys legal title to the lender until the debt "
  "is paid. That is why Georgia foreclosures are NONJUDICIAL under a power of sale.",
  "Georgia foreclosure: notice to the borrower plus advertisement in the county legal "
  "organ, customarily four weeks, then a public sale on the courthouse steps on the "
  "FIRST TUESDAY of the month.",
 ],
 "traps": [
  "Points are a percentage of the LOAN, not the sale price. This is the single most "
  "common math error on the exam.",
  "PMI protects the LENDER, never the borrower.",
  "Assumption leaves the seller secondarily liable. Only NOVATION releases them.",
  "Loan Estimate = 3 days after application. Closing Disclosure = 3 days before closing. "
  "Don't merge them.",
 ],
},

"national/agency": {
 "summary":
   "Agency is about whose interests you are legally bound to advance. A CLIENT gets "
   "fiduciary-level duties; a CUSTOMER gets honesty and disclosure of known material "
   "defects. Most agency questions are really asking which one the person is.",
 "sections": [
  {"h": "The six duties (OLD CAR)",
   "l": ["Obedience - follow LAWFUL instructions. You must refuse unlawful ones.",
         "Loyalty - put the client's interests ahead of your own.",
         "Disclosure - tell the client everything material you know.",
         "Confidentiality - protect the client's private information. SURVIVES the end "
         "of the relationship, indefinitely.",
         "Accounting - account for all money and documents. Also survives closing.",
         "Reasonable care and diligence - competence and skill.",
         "Which survive termination? CONFIDENTIALITY and ACCOUNTING. The rest end."]},
  {"h": "How agency is created and ended",
   "l": ["Express - written or spoken agreement. Written is required in Georgia.",
         "Implied - created by CONDUCT that leads someone to reasonably believe they are "
         "represented. This is the accidental-agency trap.",
         "Ratification - approving an unauthorised act after the fact.",
         "Estoppel - a party is barred from denying an agency their conduct created.",
         "Termination: expiration, completion, mutual agreement, revocation, renunciation, "
         "death or incapacity of either party, destruction of the property, or bankruptcy. "
         "A client simply refusing an offer does NOT end the agency."]},
  {"h": "Scope of authority",
   "l": ["Special agent - narrow authority for one transaction. The typical listing broker.",
         "General agent - ongoing authority in a range of matters. A property manager.",
         "Universal agent - may act in all matters, usually under power of attorney."]},
  {"h": "Who is who",
   "l": ["Client / principal - the represented party, owed full duties.",
         "Customer - unrepresented; owed honesty, fair dealing, and disclosure of known "
         "material defects. NOT owed advice, advocacy, or confidentiality.",
         "Subagent - works through the listing broker and owes duties to the SELLER, even "
         "while driving the buyer around all day.",
         "Dual agent - represents both sides in the same transaction. Duties shrink to "
         "neutrality; requires informed written consent from both. Illegal in some states.",
         "Designated agent - one licensee assigned to each side within the same firm."]},
  {"h": "Where licensees get into trouble",
   "l": ["Puffing vs. misrepresentation - exaggerated opinion ('best view in town') is "
         "puffing. A false statement of MATERIAL FACT is misrepresentation.",
         "Confidentiality never covers a known material DEFECT. You may decline to state "
         "a seller's motivation; you may not lie about the roof.",
         "Commingling - mixing client funds with the broker's own. CONVERSION is spending "
         "them - far worse.",
         "Failure to present all offers. Every offer goes to the seller, including ones "
         "you dislike or that pay you less.",
         "Undisclosed personal interest - a family or financial stake in a party must be "
         "disclosed in writing before the offer is considered.",
         "Letting an unlicensed assistant discuss terms, negotiate, or hold an open house "
         "unaccompanied."]},
  {"h": "When commission is earned",
   "p": ["Classically, when the broker produces a buyer who is READY, WILLING, AND ABLE on "
         "the seller's stated terms. Under most modern listing agreements it is earned at "
         "that moment even if the seller then refuses to close. PROCURING CAUSE - the "
         "uninterrupted chain of events that produced the buyer - decides disputes between "
         "brokers, and is settled by arbitration or the courts, not the licensing commission."]},
 ],
 "vocab": [
  ("Agency", "A relationship where one person acts for another with authority."),
  ("Principal / client", "The represented party, owed full duties."),
  ("Customer", "An unrepresented party owed honesty and material-defect disclosure."),
  ("Fiduciary", "One who holds a position of trust and must act in another's interest."),
  ("OLD CAR", "Obedience, Loyalty, Disclosure, Confidentiality, Accounting, Reasonable care."),
  ("Express agency", "Agency created by explicit written or spoken agreement."),
  ("Implied agency", "Agency created accidentally by conduct."),
  ("Ratification", "Approving an unauthorised act after it occurred."),
  ("Estoppel", "Being barred from denying an agency your conduct created."),
  ("Special agent", "Limited authority for a single transaction."),
  ("General agent", "Ongoing authority across a range of matters."),
  ("Universal agent", "Authority to act in all matters, typically by power of attorney."),
  ("Subagent", "An agent working through the listing broker, owing duties to the seller."),
  ("Dual agent", "A broker representing both parties in one transaction."),
  ("Designated agent", "A licensee assigned to represent one client exclusively within a firm."),
  ("Puffing", "Exaggerated opinion that is not a statement of fact."),
  ("Misrepresentation", "A false statement of material fact."),
  ("Commingling", "Mixing client trust funds with the broker's own funds."),
  ("Conversion", "Spending or using client trust funds."),
  ("Procuring cause", "The uninterrupted effort that produced a ready, willing and able buyer."),
  ("Ready, willing and able", "A buyer prepared to purchase on the seller's terms."),
 ],
 "examples": [
  {"t": "Confidential, but you still cannot lie",
   "s": "A seller privately tells the listing agent they must move in 30 days. A buyer's "
        "agent asks why the seller is selling.",
   "w": ["Motivation is confidential, not a material defect, so it stays private.",
         "But honesty is owed to customers too, so an invented answer is misrepresentation.",
         "The correct move is to DECLINE to answer, not to make something up."],
   "k": "Declining to answer is not deceit. Saying 'no particular reason' is."},
  {"t": "An unlawful instruction",
   "s": "A seller instructs the listing agent not to show the home to families with children.",
   "w": ["Obedience covers LAWFUL instructions only.",
         "Familial status is a protected class under the Fair Housing Act.",
         "Complying would make the agent personally liable alongside the seller."],
   "k": "Refuse. If the seller persists, withdraw from the engagement. Passing the seller "
        "to a colleague just relocates the violation."},
 ],
 "ga": [
  "In Georgia, agency requires WRITTEN authority - a brokerage engagement. BRRETA also "
  "provides that a broker is NOT deemed a fiduciary; the broker owes reasonable care in "
  "the duties the statute and the engagement specify.",
  "Paying a broker's commission does not by itself create agency in Georgia.",
 ],
 "traps": [
  "Confidentiality and accounting survive termination. Loyalty, obedience, disclosure and "
  "care do not.",
  "A subagent works with the buyer but owes duties to the SELLER.",
  "Refusing an offer does not terminate the agency.",
  "Commingling is mixing; conversion is spending. Know which the question describes.",
 ],
},

"national/disclosures": {
 "summary":
   "The rule is simple and the exceptions are what get tested: disclose known material "
   "facts about the PROPERTY; never disclose facts about the PEOPLE. Agents are not "
   "inspectors and have no duty to hunt for defects, but they cannot ignore what they see "
   "or repeat what they know to be false.",
 "sections": [
  {"h": "Material facts and defects",
   "l": ["Material fact - anything affecting value, desirability, or the decision to buy.",
         "LATENT defect - hidden, not discoverable by ordinary inspection. Known latent "
         "defects MUST be disclosed, because the buyer cannot find them.",
         "PATENT defect - obvious on reasonable inspection.",
         "A past problem that was repaired is still material - a history of flooding bears "
         "on recurrence and insurability. Disclose the problem AND the repair.",
         "No duty to DISCOVER, but no licence to IGNORE. A visible red flag you actually "
         "observe must be passed on."]},
  {"h": "What must NOT be disclosed",
   "p": ["Facts about occupants that touch a protected class are off limits, because "
         "disclosing them facilitates discrimination:"],
   "l": ["A former occupant's HIV/AIDS status or other disability - handicap is protected.",
         "The racial, religious, or ethnic makeup of a neighbourhood - answering steers.",
         "Refer buyers to public data sources they can research themselves."]},
  {"h": "Stigmatized property",
   "p": ["Stigma comes from events - a death, a crime, a rumour - not physical condition. "
         "Most states, including Georgia, do NOT require disclosure and expressly protect "
         "licensees from liability for staying silent. But protection covers NONDISCLOSURE, "
         "not an affirmative lie. If asked directly, decline rather than deny."]},
  {"h": "Lead-based paint (federal, applies everywhere)",
   "l": ["Applies to target housing built BEFORE 1978.",
         "Seller must disclose known lead hazards and provide any records.",
         "Buyer gets the EPA pamphlet and a 10-DAY opportunity to test.",
         "The seller is never required to TEST. 'No knowledge' is a valid answer on the form."]},
  {"h": "Environmental hazards",
   "l": ["Radon - naturally occurring radioactive gas entering through foundation cracks; "
         "second leading cause of lung cancer. Fixed with sub-slab depressurisation.",
         "Asbestos - dangerous when FRIABLE (crumbles and releases fibres). Often best "
         "ENCAPSULATED rather than removed, since bad removal increases exposure.",
         "Lead - paint in pre-1978 housing, and older service pipes.",
         "Underground storage tanks - leak into soil and groundwater.",
         "Mould, formaldehyde, groundwater contamination, brownfields.",
         "CERCLA / Superfund - liability is STRICT, JOINT AND SEVERAL, and RETROACTIVE. A "
         "current owner can be liable without fault. The INNOCENT LANDOWNER defence requires "
         "appropriate due diligence, such as a Phase I, BEFORE buying.",
         "Phase I ESA - records, interviews, site visit, non-invasive. Phase II involves "
         "sampling and testing, and only follows if Phase I finds a concern."]},
  {"h": "Timing",
   "p": ["Disclosure must reach the buyer early enough to weigh it before committing - "
         "normally before or at the time of the offer. Delivery after a binding contract "
         "typically gives the buyer a right to rescind."]},
 ],
 "vocab": [
  ("Material fact", "Anything affecting value, desirability, or the decision to buy."),
  ("Latent defect", "A hidden defect not discoverable by ordinary inspection."),
  ("Patent defect", "An obvious defect visible on reasonable inspection."),
  ("Stigmatized property", "Property made undesirable by events rather than condition."),
  ("Caveat emptor", "'Let the buyer beware' - largely displaced by disclosure duties."),
  ("Target housing", "Residential property built before 1978, covered by the lead rule."),
  ("Friable", "Able to be crumbled by hand, releasing fibres into the air."),
  ("Encapsulation", "Sealing a hazard in place instead of removing it."),
  ("Radon", "A naturally occurring radioactive gas that enters through the foundation."),
  ("CERCLA", "Superfund; imposes strict, joint and several, retroactive cleanup liability."),
  ("Innocent landowner defence", "A CERCLA defence requiring pre-purchase due diligence."),
  ("Phase I ESA", "A non-invasive environmental review of records and site conditions."),
  ("Phase II ESA", "Sampling and testing that follows a concerning Phase I."),
  ("Brownfield", "A property whose redevelopment is complicated by contamination."),
  ("Fraudulent concealment", "Actively hiding a known material defect."),
 ],
 "examples": [
  {"t": "Repaired, but still disclose",
   "s": "A seller fixed a chronic basement leak two years ago and it has not recurred. "
        "They ask whether it goes on the disclosure.",
   "w": ["Water intrusion history affects value, insurability, and recurrence risk.",
         "That makes it material even though it is currently fixed.",
         "Disclosing the problem AND the repair protects the seller."],
   "k": "Disclose it. Silence here is the classic post-closing lawsuit."},
  {"t": "A question you should not answer",
   "s": "A buyer asks whether a nearby group home houses people with disabilities.",
   "w": ["Handicap is a protected class.",
         "Answering, even truthfully and helpfully, facilitates steering.",
         "Decline, and point the buyer to public sources they can research."],
   "k": "Property facts are disclosable. Protected characteristics of people are not."},
 ],
 "ga": [
  "Georgia expressly protects licensees from liability for NOT disclosing that a property "
  "was the site of a death, homicide, suicide, or felony.",
  "Under BRRETA the duty runs to adverse material facts ACTUALLY KNOWN - there is no duty "
  "to inspect or investigate. But the duty runs to customers as well as clients.",
  "The seller completes Georgia's property disclosure statement from personal knowledge. "
  "A licensee should never fill it in for them.",
 ],
 "traps": [
  "External and stigma facts feel similar but are opposite: physical condition must be "
  "disclosed, stigma generally need not.",
  "Nondisclosure protection never licenses an affirmative lie.",
  "CERCLA liability can attach to an innocent current owner - fault is not required.",
 ],
},
}
