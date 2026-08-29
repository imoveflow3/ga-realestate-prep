# -*- coding: utf-8 -*-
"""Subtopic taxonomy: the "little topics" the weak-spot table drills.

Each question already carries a one-line `concept`. These rules group those
concepts into a handful of named subtopics per topic, so a weak-spot row has
several questions behind it instead of one. Matching is first-rule-wins on a
lowercase substring of the concept; a topic's LAST rule is its catch-all and
must have an empty keyword list.
"""

RULES = {
 "national/ownership": [
   ("Fixtures & trade fixtures", ["fixture"]),
   ("Easements & encroachments", ["easement", "encroach"]),
   ("Co-ownership & survivorship", ["severance", "survivorship", "co-ownership"]),
   ("Condos, co-ops & timeshares", ["condominium", "common-element", "timeshare"]),
   ("Water & private controls", ["water rights", "private land use"]),
   ("Estates & the bundle of rights", []),
 ],
 "national/landuse": [
   ("Zoning, variances & nonconforming use", ["zoning", "nonconforming", "variance"]),
   ("Private restrictions & access", ["covenant", "deed restriction", "necessity"]),
   ("Codes, permits & environmental review", ["building code", "nepa", "environmental"]),
   ("Government powers over land", []),
 ],
 "national/valuation": [
   ("Sales comparison & adjustments", ["comparable", "sales comparison", "adjustment"]),
   ("Income approach & cap rates", ["noi", "irv", "cap rate", "income approach"]),
   ("Depreciation & obsolescence", ["depreciation", "obsolescence"]),
   ("Appraisal process & approaches", ["appraisal process", "approach to value",
                                       "reconciliation", "cma", "weighting"]),
   ("Value principles", []),
 ],
 "national/financing": [
   ("Points, yield & TRID disclosure", ["point", "trid", "cd re-disclosure",
                                        "consumer credit", "respa"]),
   ("Assumption, novation & 'subject to'", ["subject to", "assumption", "va entitlement"]),
   ("Mortgage clauses & instruments", ["mortgage clause", "deed of trust", "usury"]),
   ("Loan types & structures", ["arm", "amortization", "specialty loan", "blanket",
                                "mortgage insurance"]),
   ("Lending law & the secondary market", ["ecoa", "secondary mortgage", "appraisal gap"]),
   ("Financing fundamentals", []),
 ],
 "national/agency": [
   ("Fiduciary duties", ["fiduciary", "six fiduciary", "obedience", "duties survive"]),
   ("Confidentiality & disclosure", ["confidential", "disclose material", "personal interest",
                                     "puffing"]),
   ("Creating & ending agency", ["how agency is created", "termination of agency",
                                 "scope of agency", "subagency"]),
   ("Dual agency & conflicts", ["dual agency", "presenting all offers"]),
   ("Client vs. customer", ["client vs. customer", "advocacy"]),
   ("Trust funds & supervision", ["client money", "supervision"]),
   ("Commission & representation", []),
 ],
 "national/disclosures": [
   ("Environmental hazards", ["asbestos", "cercla", "environmental", "ust", "radon"]),
   ("Lead-based paint", ["lead"]),
   ("Material facts & latent defects", ["latent", "material fact", "past defects",
                                        "no duty to discover", "falsehood"]),
   ("Stigma & fair housing limits", ["stigmatiz", "fair housing"]),
   ("Disclosure timing & duties", []),
 ],
 "national/contracts": [
   ("Offer, acceptance & counteroffers", ["acceptance", "mirror-image", "termination of an offer"]),
   ("Contingencies & conditions", ["contingenc"]),
   ("Breach, remedies & damages", ["remedies", "liquidated", "discharge", "reformation"]),
   ("Assignment & novation", ["assign", "novation"]),
   ("Validity, capacity & the Statute of Frauds", ["capacity", "statute of frauds",
                                                   "genuine assent", "void"]),
   ("Options & installment contracts", ["option", "installment"]),
   ("Contract terms & performance", ["bilateral", "executory", "time-is-of-the-essence",
                                     "earnest money", "risk act"]),
   ("Contract fundamentals", []),
 ],
 "national/transfer": [
   ("Deeds & covenants of title", ["deed", "covenant"]),
   ("Recording, notice & priority", ["recording", "notice"]),
   ("Title evidence & clearing defects", ["title", "abstract", "chain of title"]),
   ("Adverse possession & involuntary transfer", ["adverse possession", "involuntary",
                                                  "natural changes", "transfer at death"]),
   ("Closing & prorations", ["proration", "escrow delivery"]),
   ("Legal descriptions", []),
 ],
 "national/practice": [
   ("Antitrust", ["antitrust", "conspiracy"]),
   ("Fair housing & advertising", ["fair housing", "advertis", "protected classes",
                                   "disparate", "ada"]),
   ("Trust funds & commingling", ["commingling", "trust fund"]),
   ("Listings & agreements", ["listing", "net listing"]),
   ("Licensing & supervision", ["unlicensed", "independent contractor",
                                "telephone consumer"]),
   ("Practice standards", []),
 ],
 # Generated math questions take their generator's label as the subtopic, so the
 # six written ones sit together rather than as five singletons.
 "national/math": [
   ("Math fundamentals", []),
 ],

 "georgia/license-law": [
   ("Education requirements", ["prelicense", "postlicense", "continuing education",
                               "ce is per renewal"]),
   ("Licensure & experience", ["age requirement", "experience", "which licenses",
                               "activities requiring", "inactive"]),
   ("Investigations & hearings", ["alj", "investigation", "who hears", "30-day"]),
   ("GREC discipline & sanctions", ["grec", "disciplinary", "restitution", "convictions"]),
   ("Broker supervision & the firm", ["supervis", "qualifying broker", "advertising"]),
   ("Licensee as principal", ["principal", "exceptions to licensure"]),
   ("Licence administration", []),
 ],
 "georgia/brreta": [
   ("Dual agency", ["dual agenc", "dual agent"]),
   ("Designated agency", ["designated agent", "designated agency"]),
   ("Creating the engagement", ["how agency is created", "written engagement",
                                "compensation", "timing of the agency"]),
   ("Required disclosures", ["pre-engagement disclosures"]),
   ("Scope of duties under BRRETA", ["scope of duties", "narrowed broker liability",
                                     "duties owed", "purpose of brreta"]),
   ("Engagement duration & termination", ["duration", "termination dates"]),
   ("Client vs. customer", []),
 ],
 "georgia/contracts": [
   ("Binding agreement date", ["binding agreement", "formation"]),
   ("Due diligence period", ["due diligence"]),
   ("Offers & counteroffers", ["counteroffer", "revocation"]),
   ("Listing agreement rules", ["listing agreement", "termination dates",
                                "automatic renewal"]),
   ("Drafting limits & special stipulations", ["unauthorized practice", "form-filling",
                                               "specific terms", "conflicting contract"]),
   ("Georgia contract terms", []),
 ],
 "georgia/disclosures": [
   ("Stigmatized property", ["stigmatiz", "nondisclosure is protected"]),
   ("Adverse material facts", ["adverse material", "material physical",
                               "no duty to discover", "false information"]),
   ("Who discloses what", ["who makes the disclosure", "licensee-as-principal"]),
   ("Specific required disclosures", []),
 ],
 "georgia/trust-accounts": [
   ("Opening & registering the account", ["requirements", "ein", "seizure",
                                          "multiple trust", "recordkeeping"]),
   ("Deposit timing", ["timing of trust", "prompt deposit", "commingling"]),
   ("FDIC coverage", ["fdic"]),
   ("Audits & reconciliation", ["audit", "cpa", "affiliate-held"]),
   ("What counts as trust money", []),
 ],
 "georgia/procedures": [
   ("Attorney closings", ["attorney"]),
   ("Security deeds & foreclosure", ["security instrument", "foreclosure"]),
   ("Transfer tax & recording", ["transfer tax", "recorded", "trid"]),
   ("Georgia title & ownership rules", ["entirety", "co-ownership", "adverse possession"]),
   ("Taxes & prorations", []),
 ],
 "georgia/fair-housing": [
   ("Steering & blockbusting", ["steering", "blockbusting"]),
   ("Accommodations & modifications", ["accommodation", "modification", "animal"]),
   ("Protected classes", ["protected classes", "familial", "source of income"]),
   ("Unlawful instructions & enforcement", []),
 ],

 "comp/vocabulary": [
   ("Estates & tenancy terms", ["leasehold estates", "holdover", "community vs. separate"]),
   ("Liens & encumbrances", ["lien", "encumbrance", "sub-' words", "'sub-'"]),
   ("Financing terms", ["mortgage clauses", "loan documents", "redemption",
                        "seller-financing"]),
   ("Title & deed terms", ["deed vocabulary", "title-evidence"]),
   ("Valuation terms", ["appraisal principles", "kinds of value", "income statement"]),
   ("Property & water terms", ["real vs. personal", "water changes", "pete"]),
   ("Practice terms", []),
 ],
 "comp/situational": [
   ("Fair housing judgment calls", ["discriminatory request", "modification vs. accommodation"]),
   ("Disclosure & concealment", ["concealment", "waiver does not", "speak up",
                                 "silent second"]),
   ("Confidentiality & dual agency", ["confidentiality", "dual agent"]),
   ("Trust funds & accounting", ["prompt deposit", "accounting survives"]),
   ("Conflicts & compensation", ["referral fee", "firm-level conflicts"]),
   ("Client vs. customer conduct", ["customers get honesty", "advice grounded",
                                    "presenting offers"]),
   ("Supervision & licensure", []),
 ],
 "comp/grec-deep": [
   ("Education & licensure detail", ["education stages", "nonresident", "inactive"]),
   ("Trust account rules", ["trust account", "why the trust"]),
   ("GREC process & powers", ["grec", "consent settlement"]),
   ("Firm operations", []),
 ],
 "comp/closing-math": [
   ("Debits vs. credits", ["debits and credits", "largest line", "buyer money",
                           "payoff", "loan charges", "bottom line"]),
   ("Prorations at closing", ["taxes", "rent runs", "prepaid items", "accrued interest"]),
   ("Georgia closing items", ["georgia transfer tax", "security deposits"]),
   ("Reading the statement", []),
 ],
}


def subtopic_for(topic, concept):
    rules = RULES.get(topic)
    if not rules:
        return "General"
    text = (concept or "").lower()
    for label, keys in rules:
        if not keys:
            return label                      # catch-all
        for k in keys:
            if k in text:
                return label
    return rules[-1][0]
