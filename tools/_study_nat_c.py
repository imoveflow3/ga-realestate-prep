# -*- coding: utf-8 -*-
"""Study notes: contracts, transfer of title, practice of real estate, math."""

STUDY = {
"national/contracts": {
 "summary":
   "Contracts is the biggest block on the national exam (13 questions). Nearly every "
   "question reduces to one of three things: was a contract formed, what happens when "
   "someone does not perform, and can the deal be handed to someone else.",
 "sections": [
  {"h": "The four essentials",
   "l": ["Competent parties - legal age and sound mind.",
         "Mutual assent - a valid offer and an acceptance that mirrors it.",
         "Consideration - something of value each way. A promise for a promise is enough, "
         "so earnest money is NOT what makes a contract valid.",
         "Lawful object - a legal purpose.",
         "For real estate, add the STATUTE OF FRAUDS: it must be in writing and signed by "
         "the party to be charged. Leases of a year or less are commonly exempt."]},
  {"h": "Valid, void, voidable, unenforceable",
   "l": ["VALID - meets all requirements and binds both.",
         "VOID - never a contract at all (illegal purpose).",
         "VOIDABLE - one party may disaffirm: a minor's contract (voidable by the MINOR, "
         "the adult stays bound), or one induced by fraud, duress, menace, undue influence, "
         "or mistake.",
         "UNENFORCEABLE - looks valid but a court will not enforce it, e.g. an oral land "
         "contract barred by the Statute of Frauds."]},
  {"h": "Offer and acceptance",
   "l": ["Acceptance is effective when COMMUNICATED to the offeror. Signing alone is not "
         "acceptance.",
         "MIRROR-IMAGE RULE - any change to terms is a COUNTEROFFER, which REJECTS the "
         "original and makes the former offeree the new offeror.",
         "An offer terminates by: revocation before acceptance, rejection, counteroffer, "
         "lapse of the stated time, death or incapacity, or destruction of the property.",
         "Private intent is irrelevant. Telling a friend you will probably accept changes "
         "nothing."]},
  {"h": "Contract classifications",
   "l": ["Bilateral - a promise for a promise. The typical purchase contract.",
         "Unilateral - a promise for an ACT. An OPTION is the classic example: the seller "
         "must sell if the optionee exercises, but the optionee need not buy.",
         "Executory - signed but not yet fully performed (between contract and closing).",
         "Executed - fully performed by both. Careful: 'executed' also loosely means "
         "'signed' in everyday speech, and the exam exploits that."]},
  {"h": "Contingencies",
   "p": ["A contingency is a condition precedent - the duty to perform does not arise "
         "until it is satisfied or waived. Read them exactly as written: an approval at "
         "6.75% does not satisfy a contingency for financing at no more than 6.5%. The "
         "buyer must still apply in good faith."]},
  {"h": "Breach and remedies",
   "l": ["Specific performance - a court orders the actual transfer. Available because "
         "every parcel of land is legally unique.",
         "Liquidated damages - the parties agree in advance what the loss is, usually the "
         "earnest money. Enforceable only if it is a reasonable pre-estimate; if it is so "
         "large it functions as a penalty, courts void it.",
         "Compensatory damages - actual proven loss.",
         "Rescission - unwind the contract and restore both parties to their prior position.",
         "Reformation - a court REWRITES the document to reflect what the parties actually "
         "agreed, used for scrivener's errors like a wrong parcel number."]},
  {"h": "Assignment and novation",
   "l": ["ASSIGNMENT transfers RIGHTS. Real estate purchase contracts are assignable "
         "unless they say otherwise. The assignor stays SECONDARILY liable.",
         "NOVATION substitutes a new party with everyone's consent and RELEASES the "
         "original. Only novation ends liability."]},
  {"h": "Special contract forms",
   "l": ["Option - the optionee buys the RIGHT to decide, for option consideration that is "
         "usually nonrefundable. Once paid it is binding and not revocable; a recorded "
         "option binds later buyers with notice.",
         "Land contract / contract for deed - the seller keeps LEGAL title while the buyer "
         "takes possession and EQUITABLE title, paying over time.",
         "Lease option - a lease plus a right to buy.",
         "Right of first refusal - the right to match an offer the owner receives; weaker "
         "than an option because it does not set a price or force a sale."]},
  {"h": "Time and risk",
   "l": ["'Time is of the essence' turns stated dates into hard deadlines. Without it, "
         "courts allow performance within a REASONABLE time.",
         "Equitable conversion (older rule) put risk of loss on the BUYER from signing. "
         "The Uniform Vendor and Purchaser Risk Act reverses that, leaving risk with the "
         "SELLER until title or possession passes."]},
 ],
 "vocab": [
  ("Statute of Frauds", "Requires real estate contracts to be in writing and signed."),
  ("Mutual assent", "A valid offer met by a matching acceptance."),
  ("Consideration", "Something of value exchanged by each party."),
  ("Void", "Never a contract at all."),
  ("Voidable", "Valid until the protected party disaffirms."),
  ("Unenforceable", "Apparently valid but a court will not enforce it."),
  ("Mirror-image rule", "Acceptance must match the offer exactly or it is a counteroffer."),
  ("Counteroffer", "A response changing terms; rejects and replaces the original offer."),
  ("Bilateral contract", "A promise exchanged for a promise."),
  ("Unilateral contract", "A promise exchanged for an act."),
  ("Executory", "Signed but not yet fully performed."),
  ("Executed", "Fully performed by both parties."),
  ("Contingency", "A condition that must be met before performance is due."),
  ("Condition precedent", "A condition that must occur before a duty arises."),
  ("Specific performance", "A court order compelling the actual transfer."),
  ("Liquidated damages", "An amount agreed in advance as the measure of loss."),
  ("Rescission", "Unwinding a contract and restoring the parties."),
  ("Reformation", "Court correction of a document to reflect true intent."),
  ("Assignment", "Transfer of contract rights; assignor stays secondarily liable."),
  ("Novation", "Substituting a party and releasing the original."),
  ("Option", "A paid right to buy on set terms within a set time."),
  ("Optionor / optionee", "The one who must sell / the one who may buy."),
  ("Land contract", "Seller keeps legal title; buyer holds equitable title and possession."),
  ("Equitable title", "The buyer's interest after contracting but before closing."),
  ("Right of first refusal", "The right to match an offer the owner receives."),
  ("Earnest money", "A good-faith deposit; evidence of intent, not what makes the contract valid."),
  ("Time is of the essence", "A clause making stated dates strictly binding."),
  ("Equitable conversion", "The doctrine placing risk of loss on the buyer at signing."),
 ],
 "examples": [
  {"t": "Signed in time, delivered too late",
   "s": "The offer says acceptance must be RECEIVED by 5pm Friday. The seller signs at "
        "3pm Friday but the acceptance is not delivered until Saturday morning.",
   "w": ["Acceptance is effective on COMMUNICATION, not on signature.",
         "Nothing was communicated before the deadline, so the offer lapsed.",
         "The late acceptance is legally a new offer."],
   "k": "No contract on the original terms. The buyer may accept the late acceptance as a "
        "fresh offer, or walk away."},
  {"t": "Contingencies are read literally",
   "s": "The contract is contingent on financing at no more than 6.5%. The buyer is "
        "approved at 6.75% and terminates. The seller cries bad faith.",
   "w": ["The parties fixed a number, and 6.75% does not meet it.",
         "Courts enforce the stated term; materiality is not re-argued afterwards.",
         "The buyer only needed to apply in good faith, which one genuine application meets."],
   "k": "The buyer prevails and recovers the earnest money."},
  {"t": "Assignment does not free you",
   "s": "A buyer assigns her purchase contract to a third party. The contract is silent "
        "on assignment; the seller objects.",
   "w": ["Real estate contracts are assignable unless they say otherwise.",
         "The assignment is valid over the seller's objection.",
         "But the original buyer remains SECONDARILY liable."],
   "k": "Only a novation - substituting the party with the seller's consent - would "
        "release the original buyer."},
 ],
 "ga": [
  "Georgia measures deadlines from the BINDING AGREEMENT DATE - the date acceptance is "
  "communicated to the offeror.",
  "Georgia's standard DUE DILIGENCE period lets the buyer terminate for any reason and "
  "recover the earnest money. After it expires the buyer's exits narrow sharply.",
  "A Georgia licensee may fill in blanks on approved preprinted forms. Drafting original "
  "clauses is the unauthorised practice of law.",
  "Handwritten or typed special stipulations PREVAIL over conflicting preprinted text.",
 ],
 "traps": [
  "Earnest money is not consideration and not required for validity.",
  "A minor's contract is voidable BY THE MINOR; the adult remains bound.",
  "'Executed' means fully performed in exam language, not merely signed.",
  "Assignment transfers rights but keeps you liable. Novation is the release.",
 ],
},

"national/transfer": {
 "summary":
   "Title passes on DELIVERY AND ACCEPTANCE of a valid deed. Recording is not required to "
   "make the deed good between the parties - it exists to give notice to everyone else and "
   "to settle priority when two people claim the same land.",
 "sections": [
  {"h": "Requirements for a valid deed",
   "l": ["In writing, with a competent GRANTOR",
         "A named, identifiable GRANTEE",
         "Words of conveyance (the granting clause)",
         "An adequate legal description",
         "The grantor's SIGNATURE",
         "DELIVERY to and ACCEPTANCE by the grantee - this is what actually passes title",
         "Notarisation (acknowledgment) is needed to RECORD, not for validity. The grantee "
         "does not sign. Consideration need only be recited."]},
  {"h": "Types of deed, strongest to weakest",
   "l": ["GENERAL WARRANTY - warrants title against all defects through the ENTIRE chain, "
         "including before the grantor owned it. Strongest.",
         "SPECIAL (limited) WARRANTY - warrants only against defects arising during the "
         "GRANTOR'S ownership.",
         "BARGAIN AND SALE - implies the grantor holds title but gives no warranty.",
         "QUITCLAIM - conveys whatever interest the grantor has, if any, with NO warranty. "
         "The tool for clearing clouds.",
         "Special-purpose deeds: executor's, sheriff's, tax, gift, and trustee's deeds."]},
  {"h": "The covenants of title",
   "l": ["PRESENT covenants - breached at delivery if at all, so the clock starts then: "
         "seisin (the grantor owns and can convey), right to convey, and against encumbrances.",
         "FUTURE covenants - breached only on a later disturbance: quiet enjoyment "
         "(undisturbed possession and defence against lawful claims), warranty forever, and "
         "further assurance (the grantor will sign whatever is later needed)."]},
  {"h": "Recording, notice, and priority",
   "l": ["Recording gives CONSTRUCTIVE notice - everyone is charged with knowledge whether "
         "or not they looked.",
         "ACTUAL notice is what a person genuinely knows. Open POSSESSION by someone can "
         "itself be constructive notice, which defeats a later buyer who ignored it.",
         "Race - first to record wins.",
         "Notice - a later buyer without notice wins.",
         "RACE-NOTICE - a later buyer wins only if they took WITHOUT NOTICE and recorded FIRST.",
         "Generally, first in time, first in right - subject to those statutes. Property "
         "tax liens usually take priority over everything."]},
  {"h": "Title evidence",
   "l": ["Chain of title - the sequence of owners.",
         "Abstract of title - the condensed written history of every recorded document.",
         "Opinion of title - an attorney's interpretation of the abstract.",
         "Title commitment - the insurer's promise to issue a policy, with Schedule B "
         "EXCEPTIONS listing what it will NOT cover.",
         "Title insurance - protects against defects that ALREADY EXISTED when issued: "
         "forgery, undisclosed heirs, recording errors. Paid once. An OWNER'S policy covers "
         "the buyer; a LENDER'S policy covers only the lender.",
         "Marketable title - title a reasonable buyer would accept. An unreleased mortgage "
         "of record must be cleared with a recorded release; insurance does not fix it.",
         "Cloud on title - removed by a QUITCLAIM from the claimant, or a QUIET TITLE suit. "
         "A LIS PENDENS creates a cloud by giving notice of pending litigation."]},
  {"h": "Involuntary and non-sale transfers",
   "l": ["Adverse possession - open, notorious, hostile, actual, and continuous possession "
         "for the statutory period, plus any state-specific element. EVERY element is "
         "required. GEORGIA: 20 years, or 7 years under COLOUR OF TITLE.",
         "Accretion - gradual gain of land by deposit (the new soil is alluvion). Erosion "
         "is gradual loss. AVULSION is sudden change and does NOT move boundaries. "
         "Reliction is land exposed by permanently receding water.",
         "Death: TESTATE (with a will) - real property passes by DEVISE. INTESTATE - state "
         "succession law controls. Escheat if no will and no heirs.",
         "Foreclosure, tax sale, eminent domain, and dedication."]},
  {"h": "Legal descriptions",
   "l": ["METES AND BOUNDS - distances and directions from a POINT OF BEGINNING; must "
         "return to it to close.",
         "LOT AND BLOCK - references a recorded plat. The most common system in Georgia "
         "subdivisions.",
         "RECTANGULAR (government) SURVEY - townships, ranges, and sections. A section is "
         "1 square mile = 640 acres; a township is 36 sections. Georgia does NOT use it."]},
 ],
 "vocab": [
  ("Grantor / grantee", "The one conveying / the one receiving."),
  ("Granting clause", "The words of conveyance in a deed."),
  ("Delivery and acceptance", "What actually transfers title."),
  ("Acknowledgment", "Notarisation; required to record, not for validity."),
  ("General warranty deed", "Warrants title against all defects through the whole chain."),
  ("Special warranty deed", "Warrants only against defects during the grantor's ownership."),
  ("Quitclaim deed", "Conveys whatever interest the grantor has, with no warranty."),
  ("Covenant of seisin", "The grantor's promise that they own and can convey."),
  ("Covenant of quiet enjoyment", "Promise of undisturbed possession and defence of title."),
  ("Constructive notice", "Legal notice given by recording; everyone is charged with it."),
  ("Actual notice", "Knowledge a person genuinely has."),
  ("Race-notice statute", "A later buyer prevails only if without notice AND recording first."),
  ("Chain of title", "The successive record of ownership."),
  ("Abstract of title", "A condensed history of all recorded documents."),
  ("Title commitment", "The insurer's promise to issue a policy, listing exceptions."),
  ("Schedule B exception", "A defect the title policy will not cover."),
  ("Marketable title", "Title free enough of defects that a reasonable buyer would accept it."),
  ("Cloud on title", "A claim or defect casting doubt on ownership."),
  ("Quiet title action", "A suit asking a court to settle ownership."),
  ("Lis pendens", "Recorded notice of pending litigation; creates a cloud."),
  ("Adverse possession", "Acquiring title by long, open, hostile possession."),
  ("Colour of title", "A written instrument that appears to convey title but is defective."),
  ("Accretion / alluvion", "Gradual addition of land by water / the deposited soil."),
  ("Avulsion", "Sudden loss or addition of land; boundaries do not change."),
  ("Testate / intestate", "Dying with a will / without one."),
  ("Devise", "A gift of real property by will."),
  ("Metes and bounds", "Description by distances and directions from a point of beginning."),
  ("Lot and block", "Description by reference to a recorded plat."),
  ("Section", "One square mile; 640 acres."),
 ],
 "examples": [
  {"t": "Race-notice, decided by notice",
   "s": "A buyer records Monday. An earlier buyer of the same parcel, who had paid and "
        "moved in, records Wednesday. Race-notice state.",
   "w": ["Race-notice protects a later buyer only if they took WITHOUT NOTICE and recorded first.",
         "The Monday buyer did record first.",
         "But the earlier buyer's open POSSESSION is constructive notice."],
   "k": "If the Monday buyer had no notice (including no reason to see the possession), "
        "they win. If the possession was open and obvious, they lose. Notice decides it."},
  {"t": "Insurance does not clear a lien",
   "s": "A title commitment lists an unreleased 1978 mortgage as a Schedule B exception.",
   "w": ["An EXCEPTION is exactly what the policy will NOT cover.",
         "So buying insurance does not solve the problem.",
         "Marketable title requires clearing the lien of record."],
   "k": "The seller must obtain and RECORD a release or satisfaction. A buyer cannot be "
        "forced to take title subject to an undischarged mortgage."},
 ],
 "ga": [
  "Georgia records with the CLERK OF SUPERIOR COURT in the county where the land lies.",
  "Georgia adverse possession: 20 years, or 7 years under colour of title.",
  "Georgia real estate transfer tax is $1.00 per $1,000 of consideration, customarily "
  "paid by the SELLER and collected when the deed is recorded.",
  "Georgia closings are supervised by a licensed ATTORNEY, who customarily represents the "
  "LENDER, not the buyer.",
 ],
 "traps": [
  "Recording is not required for a deed to be valid between grantor and grantee.",
  "The grantee never signs the deed.",
  "A title EXCEPTION is uncovered, not covered. The word means the opposite of what it sounds.",
  "Avulsion is sudden and does not move boundaries; accretion is gradual and does.",
 ],
},

"national/practice": {
 "summary":
   "This block covers how you are allowed to run the business: fair housing, antitrust, "
   "advertising, trust funds, listings, and supervision. The recurring theme is that good "
   "intentions are no defence - conduct is judged by its effect.",
 "sections": [
  {"h": "Federal fair housing",
   "l": ["The SEVEN protected classes: race, colour, religion, sex, national origin, "
         "familial status, and handicap.",
         "Familial status covers households with children under 18, pregnant people, and "
         "those securing custody. Exception: qualified housing for older persons (55+/62+).",
         "Handicap includes HIV/AIDS. Landlords must allow reasonable MODIFICATIONS at the "
         "TENANT'S expense, and make reasonable ACCOMMODATIONS to rules at the LANDLORD'S "
         "expense (waiving a no-pets rule for an assistance animal - and no pet fee).",
         "Source of income and marital status are NOT federally protected in housing, "
         "though some states and cities protect them.",
         "The 1866 Civil Rights Act bars ALL racial discrimination with no exceptions."]},
  {"h": "The named violations",
   "l": ["STEERING - channelling people toward or away from areas by protected class. It "
         "does not require saying anything negative; selectively providing information does it.",
         "BLOCKBUSTING (panic peddling) - inducing sales by suggesting a protected group's "
         "entry will harm the neighbourhood. Illegal whether or not the claim is true.",
         "REDLINING - a lender refusing or pricing loans by area demographics.",
         "Discriminatory advertising - describe the PROPERTY, never the desired occupant.",
         "DISPARATE IMPACT - a neutral policy that falls disproportionately on a protected "
         "class can violate the Act with NO intent to discriminate. The defence is a "
         "substantial, legitimate business need with no less discriminatory alternative."]},
  {"h": "Enforcement",
   "p": ["HUD handles federal complaints, generally filed within one year. A licensee's "
         "conduct can also independently cost them their licence through the state "
         "commission, and private suits are available."]},
  {"h": "Antitrust",
   "l": ["PRICE FIXING - competitors agreeing on commission rates. A per se violation: no "
         "defence, no disclosure cure. Commission is always negotiated between a broker "
         "and a client.",
         "GROUP BOYCOTT - competitors conspiring to refuse to deal with someone.",
         "MARKET ALLOCATION - dividing territories or customer types.",
         "TIE-IN - conditioning one sale on the purchase of another product.",
         "A SINGLE FIRM setting its own rate is lawful company policy, not conspiracy. "
         "Antitrust requires an AGREEMENT between competitors; parallel behaviour alone "
         "is not proof."]},
  {"h": "Listings and agreements",
   "l": ["OPEN - many brokers; the seller owes nothing if the seller finds the buyer.",
         "EXCLUSIVE AGENCY - one broker, but the seller may still sell it themselves "
         "commission-free.",
         "EXCLUSIVE RIGHT TO SELL - one broker paid no matter who sells. Most common.",
         "NET LISTING - the broker keeps everything above a price the seller sets. Illegal "
         "in many states; Georgia permits it only under strict disclosure.",
         "Buyer agency agreements mirror these structures."]},
  {"h": "Trust funds",
   "p": ["Client money goes into a separate trust or escrow account, never the operating "
         "account. COMMINGLING is mixing; CONVERSION is spending. When buyer and seller "
         "both demand a disputed deposit, the broker must NOT pick a side - hold the funds "
         "and use interpleader or the state's prescribed procedure."]},
  {"h": "Advertising, licensing, supervision",
   "l": ["Advertising must identify the firm and must never mislead or imply a licensee "
         "operates independently of their broker. Claiming credit for another firm's sale "
         "is a misrepresentation.",
         "Do-not-call rules: an established business relationship or express written "
         "consent is needed. FSBO and expired-listing calls are a common violation source.",
         "Unlicensed assistants may do clerical and ministerial work - scheduling, "
         "preparing materials for approval, basic factual answers. They may NOT negotiate, "
         "solicit, discuss terms, or host an open house unaccompanied.",
         "Independent contractor status: the broker controls RESULTS, not hours and "
         "methods, but must still supervise for licence-law compliance. The IRS safe "
         "harbour needs a licence, pay based on output, and a written IC agreement.",
         "ADA Title III requires removing barriers in public accommodations where READILY "
         "ACHIEVABLE; new construction faces stricter standards."]},
 ],
 "vocab": [
  ("Protected class", "A group the law shields from housing discrimination."),
  ("Familial status", "Households with children under 18, pregnant people, those seeking custody."),
  ("Reasonable modification", "A physical change for a disabled tenant, at the tenant's expense."),
  ("Reasonable accommodation", "A change to rules or policies, at the provider's expense."),
  ("Steering", "Channelling buyers toward or away from areas by protected class."),
  ("Blockbusting", "Inducing panic selling by claims about a protected group moving in."),
  ("Redlining", "Refusing or pricing loans by neighbourhood demographics."),
  ("Disparate impact", "A neutral policy with a discriminatory effect; intent not required."),
  ("Price fixing", "Competitors agreeing on prices; a per se antitrust violation."),
  ("Group boycott", "Competitors agreeing to refuse to deal with someone."),
  ("Market allocation", "Competitors dividing territories or customers."),
  ("Tie-in arrangement", "Conditioning one transaction on another purchase."),
  ("Open listing", "Non-exclusive; seller owes nothing if they sell it themselves."),
  ("Exclusive agency listing", "One broker, but the seller may sell it themselves commission-free."),
  ("Exclusive right to sell", "One broker is paid regardless of who sells."),
  ("Net listing", "Broker keeps everything above the seller's stated net; heavily restricted."),
  ("Commingling", "Mixing trust funds with the broker's own money."),
  ("Conversion", "Using or spending trust funds."),
  ("Interpleader", "A court action letting a stakeholder deposit disputed funds for decision."),
  ("Ministerial acts", "Clerical, non-discretionary tasks an unlicensed assistant may do."),
  ("Independent contractor", "A licensee whose results, not methods, the broker directs."),
  ("Readily achievable", "The ADA standard for barrier removal: easily accomplishable."),
 ],
 "examples": [
  {"t": "Company policy is not conspiracy",
   "s": "A brokerage tells its agents never to quote below 5%. Competitors independently "
        "do the same.",
   "w": ["Antitrust requires an AGREEMENT between competitors.",
         "One firm setting its own rate is competition, not conspiracy.",
         "Parallel behaviour alone is not proof of an agreement."],
   "k": "Lawful company policy. What would make it illegal is evidence the firms "
        "coordinated with each other."},
  {"t": "Neutral rule, discriminatory effect",
   "s": "A manager requires income of three times the rent. It statistically screens out "
        "a protected class at a much higher rate.",
   "w": ["The policy is facially neutral and applied to everyone.",
         "But fair housing reaches EFFECTS, not just intent.",
         "That is a disparate impact claim."],
   "k": "The landlord must show a substantial, legitimate business need that no less "
        "discriminatory rule would serve."},
 ],
 "ga": [
  "Georgia permits net listings only under strict disclosure conditions.",
  "Georgia advertising must identify the firm; a licensee may not appear to operate "
  "independently of their broker.",
  "A Georgia salesperson may be paid ONLY by their affiliated broker.",
 ],
 "traps": [
  "Source of income and marital status are not among the seven federal classes.",
  "Occupancy limits by NUMBER of people can be lawful; limits by AGE of occupant are not.",
  "Modification = physical = tenant pays. Accommodation = rules = landlord absorbs.",
  "Intent is not required for a fair housing violation.",
 ],
},

"national/math": {
 "summary":
   "Real estate math is arithmetic with vocabulary attached. Almost every mistake is "
   "choosing the wrong BASE - a percentage of the loan versus the price, or of the net "
   "versus the sale price. Identify the base first, then compute.",
 "sections": [
  {"h": "Conversions to memorise",
   "l": ["1 acre = 43,560 square feet",
         "1 mile = 5,280 feet",
         "1 section = 640 acres = 1 square mile",
         "1 township = 36 sections",
         "1 square yard = 9 square feet",
         "Area of a rectangle = length x width. Triangle = 1/2 base x height."]},
  {"h": "Commission",
   "p": ["Commission is always a percentage of the SALE price, then split - first between "
         "brokerages, then between each brokerage and its agent. Work outward one step at "
         "a time and do not stop at the total."]},
  {"h": "Percentage of loan vs. percentage of price",
   "l": ["Discount points and origination fees: percentage of the LOAN.",
         "Commission and transfer tax: percentage of the SALE price.",
         "LTV: loan divided by the LESSER of price and appraised value."]},
  {"h": "Net to seller - divide, never add",
   "p": ["To find the price that produces a target net, add the seller's costs to the "
         "target, then DIVIDE by (100% - commission%). Adding the commission percentage "
         "back on always understates the price, because the commission is a percentage of "
         "the larger sale price, not of the net."]},
  {"h": "Prorations",
   "l": ["Work out the daily rate, count the days, assign them to the right party.",
         "A 360-day banker's year (30-day months) is the exam default unless told otherwise.",
         "The SELLER owns through the day BEFORE closing; the buyer owns closing day forward.",
         "UNPAID item (taxes in arrears): the seller owes for their time -> seller DEBIT, "
         "buyer CREDIT.",
         "PREPAID item (rent collected, insurance paid ahead): the seller already has the "
         "benefit -> seller CREDIT... except rent, where the seller HOLDS the buyer's cash, "
         "so seller DEBIT, buyer CREDIT.",
         "Ask 'who has the money, and who will get the benefit?' and the direction follows."]},
  {"h": "Interest",
   "p": ["Interest for one month = principal x annual rate / 12. In an amortized loan the "
         "interest portion shrinks as principal is repaid, so 'interest on the NEXT payment' "
         "uses the CURRENT balance."]},
  {"h": "Appreciation and depreciation",
   "l": ["COMPOUND appreciation applies the rate to the NEW value each year: multiply by "
         "(1 + rate) once per year.",
         "STRAIGHT-LINE depreciation takes the same dollar amount off the original basis "
         "every year: basis / useful life.",
         "Simple (non-compound) growth multiplies the original by (1 + rate x years) - the "
         "classic wrong answer on a compound question."]},
  {"h": "Qualifying ratios",
   "p": ["Front-end ratio = housing expense (PITI) / gross monthly income. Back-end adds "
         "all recurring monthly debt. Convert annual income to monthly FIRST."]},
 ],
 "vocab": [
  ("Acre", "43,560 square feet."),
  ("Section", "One square mile, 640 acres."),
  ("Township", "36 sections, six miles square."),
  ("Front foot", "A measure of frontage along a street or water."),
  ("Basis", "The original cost used to compute depreciation or gain."),
  ("Straight-line depreciation", "Equal annual deductions over a useful life."),
  ("Proration", "Dividing a shared expense between buyer and seller at closing."),
  ("Banker's year", "A 360-day year of twelve 30-day months."),
  ("Debit", "An amount a party owes at closing."),
  ("Credit", "An amount reducing what a party owes."),
  ("Front-end ratio", "Housing expense divided by gross monthly income."),
  ("Back-end ratio", "All recurring debt divided by gross monthly income."),
  ("PITI", "Principal, interest, taxes, and insurance."),
 ],
 "examples": [
  {"t": "Commission all the way down",
   "s": "$511,000 sale, 5.5% total commission. The listing brokerage keeps 40% and pays "
        "the rest to the co-op brokerage. The listing agent's split is 70% to the agent.",
   "w": ["Total = $511,000 x 5.5% = $28,105",
         "Listing brokerage = $28,105 x 40% = $11,242",
         "Listing agent = $11,242 x 70% = $7,869.40"],
   "k": "$7,869.40. The wrong answers are the totals from each earlier step - stopping "
        "early is the trap."},
  {"t": "Net to seller",
   "s": "The seller wants to net $478,000 after $2,000 of costs and a 7% commission.",
   "w": ["The seller must clear $478,000 + $2,000 = $480,000",
         "That $480,000 is the 93% left after commission",
         "Price = $480,000 / 0.93 = $516,129.03"],
   "k": "Adding 7% to $480,000 gives $513,600 - always offered, always wrong."},
  {"t": "Unpaid tax proration",
   "s": "Annual taxes $4,980, unpaid. Closing March 9, 360-day year, seller responsible "
        "through the day before closing.",
   "w": ["Daily = $4,980 / 360 = $13.83",
         "Seller's days = 2 full months x 30 + 8 = 68 days",
         "Seller's share = $13.83 x 68 = $940.67"],
   "k": "$940.67 as a seller DEBIT and buyer CREDIT, because the buyer will pay the whole "
        "bill later."},
 ],
 "ga": [
  "Georgia transfer tax is $1.00 per $1,000 of consideration - divide the price by 1,000.",
  "Georgia property taxes become a lien on JANUARY 1, which is why closings prorate them.",
 ],
 "traps": [
  "Points on the LOAN, commission on the PRICE. Mixing these is the top math error.",
  "Net-to-seller is division, not addition.",
  "Compound appreciation multiplies each year; simple growth does not.",
  "Convert annual income to monthly before applying a qualifying ratio.",
 ],
},
}
