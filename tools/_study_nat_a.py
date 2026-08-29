# -*- coding: utf-8 -*-
"""Study notes: property ownership, land use controls, valuation.

Original notes written to cover the same ground as the exam outline. Georgia
specifics are drawn from the GREC Real Estate InfoBase (public state material).
"""

STUDY = {
"national/ownership": {
 "summary":
   "Ownership is a bundle of separate rights, and almost every question here asks "
   "which sticks in the bundle a party actually holds. Work out three things for any "
   "scenario: how long the interest lasts, whether anything can cut it short, and who "
   "else has a claim on the same land.",
 "sections": [
  {"h": "The bundle of rights",
   "p": ["Ownership is not one right but several that can be separated and sold "
         "independently. Remember them as DUPES."],
   "l": ["Dispose - sell, gift, will, or encumber it",
         "Use - occupy and use it for any lawful purpose",
         "Possess - occupy it and exclude others",
         "Exclude - keep others off",
         "Sell/transfer - convey title to someone else"]},
  {"h": "Freehold estates: ownership without a fixed end",
   "p": ["A freehold lasts for an indefinite time. The three you must know:"],
   "l": ["Fee simple absolute - the whole bundle, no conditions, no time limit. The "
         "most complete ownership the law recognises.",
         "Fee simple defeasible - ownership that can be LOST if a condition happens. "
         "A DETERMINABLE fee ends automatically the instant the condition occurs "
         "(the grantor holds a possibility of reverter). A fee on CONDITION SUBSEQUENT "
         "does not end automatically - the grantor must act on a right of re-entry.",
         "Life estate - lasts for someone's lifetime. Measured by the holder's life, "
         "or by a third party's life (pur autre vie). When it ends, the property goes "
         "to the REMAINDERMAN, or back to the grantor as a REVERSION."]},
  {"h": "Leasehold estates: possession with an end date",
   "p": ["A leasehold gives possession, not ownership. The landlord keeps the LEASED "
         "FEE; the tenant holds the leasehold."],
   "l": ["Estate for years - fixed start and end. Ends automatically; no notice needed. "
         "'Years' is misleading: a 30-day lease with fixed dates is an estate for years.",
         "Periodic estate - renews itself (month to month) until someone gives notice.",
         "Estate at will - continues at the pleasure of both parties, endable any time.",
         "Estate at sufferance - a holdover who stays without permission. Lowest estate: "
         "possession with no right, but entry was originally lawful so it is not trespass."]},
  {"h": "Co-ownership",
   "p": ["Ask two questions: is there a right of survivorship, and can one owner convey "
         "their share alone?"],
   "l": ["Tenancy in common - shares may be unequal, NO survivorship, each share passes "
         "by will or inheritance. The default when a deed says nothing.",
         "Joint tenancy - equal shares with RIGHT OF SURVIVORSHIP. Requires the four "
         "unities: Possession, Interest, Time, Title (PITT). Selling a share severs the "
         "joint tenancy as to that share; the buyer becomes a tenant in common.",
         "Tenancy by the entirety - joint tenancy between spouses that neither can sever "
         "alone. GEORGIA DOES NOT RECOGNISE IT.",
         "Community property - a marital form used in nine states; Georgia is not one."]},
  {"h": "Condominiums, cooperatives, and timeshares",
   "l": ["Condominium - you own your unit in fee simple, PLUS an undivided tenancy-in-"
         "common share of the common elements. That percentage, set in the declaration, "
         "drives your assessments and usually your voting weight, and cannot be sold "
         "separately from the unit.",
         "Cooperative - a corporation owns the whole building. You own SHARES of stock "
         "plus a proprietary lease on your unit. You own personal property, not real property.",
         "Timeshare estate - a deeded fractional real property interest. A right-to-use "
         "timeshare is only a contract right to occupy, which expires with the contract."]},
  {"h": "Fixtures",
   "p": ["A fixture is personal property that has become part of the real estate, so it "
         "conveys with the property unless the contract excludes it. Courts weigh three "
         "things, remembered as MAI:"],
   "l": ["Method of annexation - how firmly is it attached?",
         "Adaptation - is it specially fitted to this property?",
         "Intent - what did the person attaching it intend? Intent carries the most weight.",
         "TRADE FIXTURES are the exception: items a COMMERCIAL TENANT installs to run "
         "their business stay the tenant's personal property and may be removed before "
         "the lease ends, with damage repaired. Left past lease end, they can be forfeited."]},
  {"h": "Encumbrances: other people's claims on your land",
   "l": ["Easement appurtenant - runs with the land and benefits an adjoining parcel. The "
         "benefited parcel is the DOMINANT tenement; the burdened one is the SERVIENT "
         "tenement. It passes automatically to later owners.",
         "Easement in gross - benefits a person or company, not a parcel. No dominant "
         "tenement. Commercial ones (utilities) are assignable and survive a sale.",
         "Easement by necessity - implied when a parcel is landlocked by the seller's own "
         "severance of the land.",
         "Easement by prescription - acquired by long, open, hostile use.",
         "Licence - mere permission to use land. Personal and revocable at any time.",
         "Encroachment - an unauthorised physical intrusion, usually found by SURVEY.",
         "Lien - a money claim against the property.",
         "Deed restriction / CC&R - a private restriction enforceable by benefited owners."]},
  {"h": "Water and air rights",
   "l": ["Riparian rights - attach to FLOWING water (rivers, streams).",
         "Littoral rights - attach to STILL water (lakes, seas, ponds).",
         "Prior appropriation - the western doctrine where use is granted by permit "
         "regardless of whether you touch the water.",
         "Air rights can be sold separately - that is how air-rights development works."]},
 ],
 "vocab": [
  ("Fee simple absolute", "Ownership with no conditions and no time limit; the complete bundle of rights."),
  ("Defeasible fee", "A fee that can be lost if a stated condition occurs."),
  ("Possibility of reverter", "The grantor's future interest after a determinable fee; takes effect automatically."),
  ("Right of re-entry", "The grantor's future interest after a fee on condition subsequent; must be exercised."),
  ("Life estate", "An interest lasting for a person's lifetime."),
  ("Pur autre vie", "A life estate measured by the life of someone other than the holder."),
  ("Remainderman", "The person who takes the property when a life estate ends."),
  ("Reversion", "The interest returning to the grantor when a lesser estate ends."),
  ("Waste", "A life tenant's failure to maintain, pay taxes, or preserve the property; the remainderman may sue now."),
  ("Leased fee", "The landlord's ownership interest, subject to the lease."),
  ("Leasehold", "The tenant's right of possession for a term."),
  ("Estate at sufferance", "Possession by a holdover tenant with no right to be there."),
  ("Tenancy in common", "Co-ownership with no survivorship; shares pass to heirs."),
  ("Joint tenancy", "Co-ownership with right of survivorship, requiring the four unities."),
  ("Four unities (PITT)", "Possession, Interest, Time, Title - all required for joint tenancy."),
  ("Severance", "Breaking a joint tenancy, usually by one owner conveying their share."),
  ("Tenancy by the entirety", "Marital joint tenancy neither spouse can sever alone. Not recognised in Georgia."),
  ("Common elements", "The parts of a condominium owned by all unit owners as tenants in common."),
  ("Proprietary lease", "The occupancy right a cooperative shareholder holds."),
  ("Fixture", "Personal property that has become part of the realty and conveys with it."),
  ("Trade fixture", "A commercial tenant's business equipment; remains personal property and is removable."),
  ("Emblements", "Annual crops, treated as the tenant-farmer's personal property."),
  ("Chattel", "Personal property."),
  ("Encumbrance", "Any claim, lien, easement, or restriction limiting the fee."),
  ("Dominant tenement", "The parcel benefited by an easement appurtenant."),
  ("Servient tenement", "The parcel burdened by an easement."),
  ("Easement in gross", "An easement benefiting a person or company rather than a parcel."),
  ("Encroachment", "A physical intrusion onto a neighbouring parcel."),
  ("Licence", "Revocable permission to use land; not an interest in land."),
  ("Riparian rights", "Water rights along flowing water."),
  ("Littoral rights", "Water rights along still water."),
 ],
 "examples": [
  {"t": "Determinable fee vs. condition subsequent",
   "s": "Ann conveys land 'to the city so long as it is used as a park.' The city later "
        "builds offices on it.",
   "w": ["'So long as' is durational language, so this is a fee simple DETERMINABLE.",
         "A determinable fee ends AUTOMATICALLY the moment the condition is broken.",
         "Title reverts to Ann (or her heirs) with no lawsuit required."],
   "k": "Durational words (so long as, while, during, until) = determinable = automatic. "
        "Conditional words (but if, provided that, on condition that) = condition "
        "subsequent = the grantor must act."},
  {"t": "Survivorship beats a will",
   "s": "Two sisters own a lake house as joint tenants. One dies leaving a will giving "
        "'all my real property' to her son.",
   "w": ["Survivorship operates at the instant of death.",
         "At that instant the deceased sister's interest disappears into the survivor's.",
         "There is nothing left for the will to pass."],
   "k": "The son receives nothing in this property. A will only passes what the person "
        "still owned at death."},
  {"t": "Is it a fixture?",
   "s": "A commercial tenant bolts refrigeration units to the floor of a leased space. "
        "The lease is silent. The lease ends.",
   "w": ["Bolting looks like annexation, which would normally make it a fixture.",
         "But the tenant is COMMERCIAL and installed it to run the business.",
         "That makes it a TRADE FIXTURE, which stays the tenant's personal property."],
   "k": "The tenant may remove it before the lease ends and must repair the damage. If "
        "they leave it past lease end, it can become the landlord's."},
 ],
 "ga": [
  "Georgia does NOT recognise tenancy by the entirety. Married Georgians who want "
  "survivorship hold as joint tenants with right of survivorship, stated expressly in "
  "the deed.",
  "A Georgia licensee who buys, sells, or leases property for their own account must "
  "disclose their licensed status in writing in the contract or lease, and must place "
  "any trust funds in an account approved by their broker.",
 ],
 "traps": [
  "'Estate for years' does not mean years. A 60-day lease with fixed dates is one.",
  "The landlord holds the LEASED FEE; the tenant holds the leasehold. Questions try to "
  "flip these.",
  "A condominium owner owns real property; a co-op shareholder owns personal property "
  "(stock plus a lease).",
  "Every encroachment is an encumbrance, but not every encumbrance is physical.",
 ],
},

"national/landuse": {
 "summary":
   "Two systems restrict what an owner may do: PUBLIC controls imposed by government, "
   "and PRIVATE controls created by contract or deed. The most common exam error is "
   "mixing them up - zoning is public and enforced by the municipality, CC&Rs are "
   "private and enforced by owners or an HOA.",
 "sections": [
  {"h": "The four public powers (PETE)",
   "l": ["Police power - regulate for health, safety, morals, and general welfare. "
         "Zoning, building codes, and environmental rules. NO compensation is paid.",
         "Eminent domain - TAKE private property for public use. Just compensation IS "
         "required. The lawsuit that exercises it is CONDEMNATION.",
         "Taxation - levy against property to fund government.",
         "Escheat - property passes to the state when an owner dies with no will and no "
         "locatable heirs."]},
  {"h": "Zoning and relief from it",
   "l": ["Comprehensive (master) plan - the long-range policy document. Zoning is the "
         "ordinance that IMPLEMENTS the plan parcel by parcel.",
         "Nonconforming use - a lawful use that predates the new zoning may continue "
         "('grandfathered'). It is usually LOST on destruction beyond a set percentage, "
         "on abandonment for a stated period, or on change to a different nonconforming use.",
         "Variance - permission to deviate from a DIMENSIONAL requirement (setback, height) "
         "because strict compliance creates a unique hardship the owner did not cause.",
         "Special use / conditional use permit - allows a listed USE that needs review, "
         "such as a church or a school in a residential zone.",
         "Spot zoning - rezoning one parcel inconsistently with the plan for one owner's "
         "benefit. Generally invalid.",
         "Downzoning - reducing permitted intensity across an area.",
         "Buffer zone - a strip separating incompatible districts.",
         "Setback - the required distance from a lot line to a structure."]},
  {"h": "When regulation becomes a taking",
   "p": ["A regulation is a valid exercise of police power even if it reduces value. It "
         "becomes a TAKING requiring compensation only when it denies ALL economically "
         "viable use. An owner claiming a regulation went that far sues in INVERSE "
         "CONDEMNATION."]},
  {"h": "Private controls",
   "l": ["CC&Rs / restrictive covenants - recorded private restrictions that RUN WITH THE "
         "LAND and bind later buyers. Any benefited owner (or the HOA) may enforce them, "
         "usually by injunction. Government does not enforce them.",
         "Defences to enforcement: abandonment through widespread non-enforcement, and "
         "laches where delay has prejudiced the defendant.",
         "Where a covenant and zoning conflict, the MORE RESTRICTIVE one controls."]},
  {"h": "Codes, permits, and environmental review",
   "l": ["Building permit and inspections exist for public safety, not revenue. The "
         "CERTIFICATE OF OCCUPANCY at the end confirms lawful occupancy.",
         "NEPA requires an Environmental Impact Statement for major FEDERAL actions "
         "significantly affecting the environment."]},
 ],
 "vocab": [
  ("Police power", "Government's power to regulate land use for public welfare without paying."),
  ("Eminent domain", "The power to take private property for public use with just compensation."),
  ("Condemnation", "The legal proceeding that exercises eminent domain."),
  ("Inverse condemnation", "An owner's suit claiming regulation has effectively taken the property."),
  ("Escheat", "Transfer to the state when an owner dies with no will and no heirs."),
  ("Comprehensive plan", "The long-range policy guide that zoning implements."),
  ("Nonconforming use", "A lawful pre-existing use that does not meet current zoning."),
  ("Variance", "Permission to deviate from a dimensional zoning requirement on hardship grounds."),
  ("Special use permit", "Approval for a listed conditional use in a district."),
  ("Spot zoning", "Rezoning one parcel inconsistently with the plan; generally invalid."),
  ("Downzoning", "Reducing the permitted intensity of use across an area."),
  ("Buffer zone", "A transitional strip between incompatible zoning districts."),
  ("Setback", "The required distance between a lot line and a structure."),
  ("CC&Rs", "Covenants, conditions and restrictions - recorded private land use controls."),
  ("Run with the land", "A restriction or benefit that binds and passes to later owners."),
  ("Certificate of occupancy", "The document confirming a structure may lawfully be occupied."),
  ("Environmental Impact Statement", "The NEPA study required for major federal actions."),
  ("Plat", "A recorded subdivision map showing lots, blocks, and easements."),
 ],
 "examples": [
  {"t": "Value loss is not a taking",
   "s": "A city downzones an area. An owner's lot stays usable but is worth 40% less. "
        "The owner sues claiming a taking.",
   "w": ["Ask the only question that matters: does ANY economically viable use remain?",
         "It does - the lot is still usable, just less profitably.",
         "Diminution in value alone, even substantial, is a cost of regulation."],
   "k": "The owner loses. A taking requires denial of ALL economically viable use, not "
        "a large loss of value."},
  {"t": "Losing nonconforming status",
   "s": "A legal nonconforming gas station burns down. The owner wants to rebuild it "
        "exactly as it was.",
   "w": ["Nonconforming rights exist to phase a use out, not preserve it forever.",
         "Most ordinances end the status on destruction beyond a stated percentage.",
         "Rebuilding therefore requires conforming to current zoning, or a variance."],
   "k": "Destruction, abandonment, and changing to a different nonconforming use are the "
        "three classic ways the protection is lost."},
 ],
 "ga": [
  "Georgia subdivisions are typically described by LOT AND BLOCK from a plat recorded "
  "with the clerk of superior court in the county where the land lies.",
 ],
 "traps": [
  "Eminent domain is the POWER; condemnation is the PROCEEDING.",
  "A variance is for dimensional hardship; a special use permit is for a different type "
  "of use. Questions swap them constantly.",
  "Zoning is public and enforced by government. CC&Rs are private and enforced by owners.",
 ],
},

"national/valuation": {
 "summary":
   "Value is an OPINION of the most probable price, not a fact. Three approaches exist, "
   "and the whole skill is picking the right one for the property type and then weighting "
   "them honestly. Appraisers never average the three.",
 "sections": [
  {"h": "Value, price, and cost are three different things",
   "l": ["Market value - the most probable price in an arm's-length sale, with an informed "
         "buyer and seller, adequate exposure, and no duress. An OPINION.",
         "Market price - what a property actually sold for. A historical FACT, which may "
         "reflect a distress sale.",
         "Cost - what it took to build. Cost does not equal value.",
         "Assessed value - the tax base, often a percentage of market value.",
         "Insurable value - the improvements only, since land does not burn."]},
  {"h": "The four characteristics of value (DUST)",
   "l": ["Demand - buyers who want it and can pay",
         "Utility - it can satisfy a need",
         "Scarcity - supply is limited",
         "Transferability - title can be conveyed"]},
  {"h": "Appraisal principles",
   "l": ["Substitution - value is capped by the cost of an equally desirable substitute. "
         "This underlies the whole sales comparison approach.",
         "Highest and best use - the use that is legally permitted, physically possible, "
         "financially feasible, and maximally productive. Legality comes first; an illegal "
         "use is never highest and best.",
         "Conformity - maximum value where properties are reasonably similar.",
         "Progression - a modest property is pulled UP by superior neighbours.",
         "Regression - a superior property is dragged DOWN by lesser neighbours.",
         "Contribution - a component is worth what it ADDS to the whole, not what it cost.",
         "Anticipation - value reflects expected future benefits.",
         "Assemblage - combining parcels. PLOTTAGE is the extra value that results.",
         "Supply and demand, and change - values move with the market and never sit still."]},
  {"h": "The three approaches",
   "l": ["SALES COMPARISON - compare recent similar sales. Best for houses and land. "
         "Always adjust the COMPARABLE, never the subject. Comp superior: SUBTRACT. Comp "
         "inferior: ADD. Memory hook CIA - Comp Inferior, Add.",
         "COST - reproduction or replacement cost, LESS depreciation, PLUS land value. "
         "Best for new construction and special-purpose property (churches, schools, "
         "libraries) that rarely sells and produces no rent.",
         "INCOME - convert income into value. Best for rentals and commercial. Use IRV: "
         "Income = Rate x Value, so Value = NOI / Rate."]},
  {"h": "Building NOI correctly",
   "p": ["Nearly every income-approach mistake is a bad NOI. Work down the statement in "
         "order:"],
   "l": ["Potential gross income (all units, fully rented)",
         "minus vacancy and collection loss = EFFECTIVE GROSS INCOME",
         "minus operating expenses = NET OPERATING INCOME",
         "minus debt service = CASH FLOW",
         "DEBT SERVICE IS NEVER AN OPERATING EXPENSE. Neither is depreciation or capital "
         "improvement. This is the single most common trap."]},
  {"h": "Depreciation: three kinds",
   "l": ["Physical deterioration - wear, tear, and deferred maintenance. Often curable.",
         "Functional obsolescence - a defect in the design or utility of the structure "
         "itself: one bathroom, a bedroom you walk through, an outdated layout.",
         "External (economic) obsolescence - caused by something OUTSIDE the property "
         "line: a new highway, a failing neighbourhood. ALWAYS INCURABLE, because the "
         "owner cannot fix it. It is charged against the LAND.",
         "Curable vs. incurable is an ECONOMIC test, not a physical one: an item is "
         "curable when the cost to fix it is recovered in added value."]},
  {"h": "CMA vs. appraisal vs. BPO",
   "p": ["A competitive market analysis is a broker's pricing opinion built from "
         "comparables to help set a list price. It is NOT an appraisal, must never be "
         "presented as one, and needs no appraiser licence. An appraisal is an "
         "independent opinion by a licensed or certified appraiser."]},
  {"h": "The appraisal process ends in reconciliation",
   "p": ["Reconciliation weighs each approach by how RELIABLE it is for that property, "
         "and states a single value conclusion. Averaging the three is always wrong."]},
 ],
 "vocab": [
  ("Market value", "The most probable price under normal, arm's-length conditions."),
  ("Market price", "The actual price a property sold for."),
  ("Assessed value", "The value used as the property tax base."),
  ("Insurable value", "The value of the improvements only."),
  ("DUST", "Demand, Utility, Scarcity, Transferability - the four elements of value."),
  ("Substitution", "Value is limited by the cost of an equally desirable alternative."),
  ("Highest and best use", "Legally permitted, physically possible, financially feasible, maximally productive."),
  ("Conformity", "Value is maximised where properties are similar."),
  ("Progression", "A lesser property gains value from superior neighbours."),
  ("Regression", "A superior property loses value among lesser neighbours."),
  ("Contribution", "A component is worth what it adds to the whole."),
  ("Anticipation", "Value based on expected future benefits."),
  ("Assemblage", "Combining adjacent parcels under one owner."),
  ("Plottage", "The added value created by assemblage."),
  ("Comparable", "A recently sold similar property used in the sales comparison approach."),
  ("Reproduction cost", "Cost to build an exact replica."),
  ("Replacement cost", "Cost to build equivalent utility with current materials."),
  ("Potential gross income", "Income if fully rented with no losses."),
  ("Effective gross income", "Potential gross income less vacancy and collection loss."),
  ("Net operating income", "Effective gross income less operating expenses, before debt service."),
  ("Capitalization rate", "The rate converting income to value; Value = NOI / Rate."),
  ("Gross rent multiplier", "Sale price divided by gross rent; a quick screening tool."),
  ("Physical deterioration", "Loss in value from wear and tear."),
  ("Functional obsolescence", "Loss in value from a defect in the structure's own design or utility."),
  ("External obsolescence", "Loss in value caused from outside the property; always incurable."),
  ("Reconciliation", "Weighting the approaches into one value conclusion."),
  ("CMA", "A broker's comparative pricing opinion; not an appraisal."),
 ],
 "examples": [
  {"t": "Adjusting comparables in the right direction",
   "s": "A comparable sold for $420,000. It has an extra half-bath worth $12,000, and "
        "its lot is inferior to the subject's by $8,000.",
   "w": ["Adjust the COMP toward the subject, never the subject toward the comp.",
         "Comp is SUPERIOR on the bath: subtract $12,000 -> $408,000.",
         "Comp is INFERIOR on the lot: add $8,000 -> $416,000."],
   "k": "$416,000. CIA: Comp Inferior, Add. Superior features come off."},
  {"t": "Cap rate value with a proper NOI",
   "s": "A four-unit building rents for $1,400 per unit per month, vacancy is 5%, and "
        "operating expenses are $19,000 a year. Cap rate 8%.",
   "w": ["Potential gross = 4 x $1,400 x 12 = $67,200",
         "Less 5% vacancy ($3,360) = $63,840 effective gross",
         "Less $19,000 expenses = $44,840 NOI",
         "Value = NOI / rate = $44,840 / 0.08 = $560,500"],
   "k": "About $560,000. Skipping vacancy or expenses inflates the answer - which is "
        "exactly what the wrong choices will look like."},
  {"t": "Which depreciation is it?",
   "s": "A house on a busy corner sells for less than identical houses mid-block.",
   "w": ["The cause is outside the property line, so it is EXTERNAL obsolescence.",
         "External obsolescence is always incurable - the owner cannot move the road.",
         "Because a location penalty attaches to the site, it is charged against the LAND."],
   "k": "External obsolescence, incurable, deducted from the land - not the improvements."},
 ],
 "ga": [
  "A Georgia licensee preparing a CMA is giving a broker's pricing opinion. Presenting "
  "it as an appraisal, or implying appraiser credentials, is a licence-law problem.",
 ],
 "traps": [
  "Debt service is NEVER an operating expense when building NOI.",
  "Cap rate and value move INVERSELY: a higher cap rate means a lower value.",
  "Curability is about economics, not physics. If the fix costs more than it returns, "
  "it is incurable even though it is physically repairable.",
  "Cost approach for a church or school; sales comparison for a house; income for a rental.",
 ],
},
}
