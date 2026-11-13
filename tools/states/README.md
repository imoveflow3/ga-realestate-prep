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

## Progress

**Done (23):** GA, TX, FL, CA, NY, NC, OH, PA, IL, AZ, VA, MI, NJ, WI, WA, MA,
CO, TN, IN, MO, MD, MN, LA.

**Remaining (27):** AL, AK, AR, CT, DE, HI, ID, IA, KS, KY, ME, MS, MT, NE, NV,
NH, NM, ND, OK, OR, RI, SC, SD, UT, VT, WV, WY.

Work one state at a time, newest first in whatever order makes sense; population
order has been the habit. Report only "<State> done" and move on.

## Exam shapes already handled

Most states split the exam national + state, which is the shape the app was
built around. Six write ONE exam with no national portion — CA, FL, MI, NJ, NY
and WI — and a pack declares that with `single: True`. Wisconsin is the odd one:
Pearson calls all 140 items the state portion, so the pack splits them by
subject (99 state / 41 national).

Pass marks vary more than the counts do:

- A plain `pass` float where the state publishes one percentage.
- Per-portion `pass` where the marks differ (IL 70% national / 75% state;
  VA 56/80 and 30/40; CO raw counts 60/80 and 53/74; MO 70%/75%).
- `pass_published: False` plus a `pass_note` where the state publishes no
  percentage at all: NY reports only pass/fail; PA, WI, WA, IN and LA report
  SCALED scores their own handbooks say are not percentages correct.

## Watch the outline arithmetic

A handbook's content outline does not always add up to the scored total in its
own examination summary table. Check before trusting it.

- Minnesota's outline totals 40 while the table gives the state portion 50
  items, so the MN pack keeps PSI's proportions and scales them x1.25.
- Louisiana's outline gives a RANGE per section whose midpoints happen to total
  exactly 55, so no scaling was needed.

## The ship pipeline

Run from the repo root, in this order:

```
python3 -I tools/states/<xx>.py          # writes greprep/packs/<XX>.json
python3 -I tools/build_online.py
python3 -I tools/build_paid.py
grep -c -o '<xx>-[0-9a-f]\{8\}' worker/assets/gated.js   # must equal the question count
grep -c -o '<xx>-[0-9a-f]\{8\}' docs/*.js                # must be 0 - state content is paid
node --test worker/test/gate.test.mjs
cd worker && npx wrangler deploy
```

`grep -c` exits 1 when it finds zero matches, so chaining it with `&&` stops the
chain on the docs check even though 0 is the result you want. Run that one on
its own line.

Commit messages end with the `Co-Authored-By: Claude Opus 5` line, and the
project memory note `ga-realestate-prep-site` gets the new state count plus
anything learned about that state's law or its statute source.

## Checks before shipping a state

- `python3 tools/states/<xx>.py` writes the pack without an assertion failing.
- `python3 tools/build_paid.py` and `cd worker && npm test`.
- Load the app with that state chosen and read one lesson end to end.
- Confirm the pack is in `worker/assets/gated.js` and **not** in `docs/`:
  state content is paid material.
