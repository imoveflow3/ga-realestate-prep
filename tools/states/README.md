# Adding a state

One file per state, `tools/states/<xx>.py`, built the way `tx.py` is. Run it
to write `greprep/packs/<XX>.json`; `tools/build_paid.py` picks the pack up
automatically and the app swaps it in for anyone who chose that state.

## The rule that matters

**Every fact comes from the state's own law, read directly.** Not from a prep
school's website, not from a competitor's flashcards, not from memory. Several
commercial guides were found wrong on Georgia (they quote 36 CE hours; Georgia
requires 24 per four-year renewal), and a wrong rule here means a paying
customer fails an exam. Cite the section next to each fact, as `tx.py` does, so
any claim can be re-checked later.

If an official source cannot be found for something, leave it out. A thinner
lesson is fine. A confident wrong one is not.

## What to read, in order

1. **The exam handbook** (Pearson VUE or PSI, whichever `greprep/states.json`
   names as `vendor`, at the `src` URL). This gives the blueprint: how many
   scored items, how long, the pass mark, and the state's content outline with
   the number of items per topic. Build the topic list from that outline, not
   from what other states happen to have.
2. **The licence act** — the state's real estate statute. Licensing,
   the commission's powers, agency, prohibited conduct, penalties, the
   recovery fund.
3. **The commission's rules** — the administrative code chapter. Trust money
   deadlines, advertising, continuing education, unlicensed assistants.
4. **The property/civil law the outline asks for** — whatever the outline's
   "special topics" section lists: disclosure duties, homestead, landlord and
   tenant, foreclosure, recording, liens, marital property, wills.

`statutes.capitol.texas.gov`-style official sites are preferred; a state
legislature's own site always beats a third-party mirror.

## The shape of a pack

- `EXAM` — scored counts, minutes, pass mark, as the handbook states them.
- `TOPICS` — one per outline section, with the item count scaled to the
  scored total (handbook outlines usually count pretest items too).
- `STUDY` — a lesson per topic: `summary`, `sections` (each with prose `p`,
  bullets `l`, and `check` questions), `traps`, `vocab`, `examples`.
- `Q` — practice questions, right answer first; `build()` rotates the
  position so the answer is not always in the same slot.
- `DIFFS` — where this state departs from the national rule, shown on the
  national lessons in place of the Georgia notes.
- `SOURCES` — every official text used, with a link.

Aim for the question count to be at least twice the scored state items, spread
across topics in proportion to the outline.

## States that do not fit yet

44 states split the exam into a national portion and a state portion, which is
the shape the app is built around. Six do not — CA, FL, MI, NJ, NY and WI write
a single exam of their own with no national portion. Those need the app to
handle a one-portion exam before a pack is worth writing.

## Checks before shipping a state

- `python3 tools/states/<xx>.py` writes the pack without an assertion failing.
- `python3 tools/build_paid.py` and `cd worker && npm test`.
- Load the app with that state chosen and read one lesson end to end.
- Confirm the pack is in `worker/assets/gated.js` and **not** in `docs/`:
  state content is paid material.
