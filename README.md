# Georgia Real Estate Exam Prep

A study app for the Georgia real estate **salesperson** licensing exam (PSI):
80 national questions + 52 Georgia state questions, 75% to pass.

Runs at a public web address, as a private page on claude.ai, or on your own
machine with nothing but the Python 3 that ships with macOS. No third-party
packages any way you run it.

## Three ways to use it

**Public web address (open it anywhere, no sign-in):**
<https://imoveflow3.github.io/ga-realestate-prep/>

Served by GitHub Pages from `docs/index.html`. Works in any browser on any
device -- bookmark it, or add it to your phone's home screen and it opens like
an app. This is the one to use day to day.

**Private page on claude.ai:**
<https://claude.ai/code/artifact/c0451a46-499d-4471-9b9a-d2b3ce5cb9ad>

The same app, private to your account. Only opens on a device where you are
signed in to claude.ai -- elsewhere it shows "Page not found" rather than a
login prompt.

Both are one self-contained page holding all 1,402 questions. Progress is
stored in that browser, so each device keeps its own history -- use
**Setup -> Export / Import** to move it between them.

To publish changes to the public site:

```bash
cd ~/ga-realestate-prep && python3 tools/build_online.py && git add -A && git commit -m "update questions" && git push
```

GitHub Pages redeploys in about a minute. To update the claude.ai page as well,
republish `online/ga-real-estate.html` to the same artifact URL.

**Locally:**

```bash
cd ~/ga-realestate-prep && python3 server.py
```

Then open <http://localhost:8778>. Press `Ctrl-C` in the terminal to stop.
Leave that window open while you study -- closing it stops the server.

You can also double-click **`GA Real Estate Prep.command`** in Finder, which
starts the server and opens your browser for you.

To use a different port: `GAPREP_PORT=9000 python3 server.py`

The two are independent: the local app saves to `data/progress.json`, the
online one saves to browser storage. Whichever you use, the questions and the
scheduling rules are identical.

## What's in it

**352 written questions** (147 of them hard tier) plus an unlimited supply of
generated math problems.

| Section | Questions | Hard | Topics |
|---|---|---|---|
| National | 170 | 50 | ownership, land use, valuation, financing, agency, disclosures, contracts, transfer of title, practice, math |
| Georgia | 121 | 36 | GREC license law, BRRETA, Georgia contracts, disclosures, trust accounts, closings/escrow, fair housing |
| Comprehensive | 61 | 61 | vocabulary & terminology, situational judgment, GREC law deep-dive, closing & settlement math |

The **Comprehensive subtest** is a cross-cutting drill, not a section of the
real exam. It is excluded from mock exams and from the study plan's exam
weighting, and its topics show "drill" rather than an exam question count.

### Difficulty

Every written question is tagged **core** or **hard**. Hard questions are
scenarios rather than definitions, with distractors that are true statements
which do not answer the question asked.

| Mode | What you get |
|---|---|
| Harder mix *(default)* | About two thirds hard tier |
| Hard only | Hard tier only |
| Full bank | Everything, unweighted |
| Core only | Fundamentals, for a first pass |

Georgia facts were checked against the GREC Real Estate InfoBase (chapters 3,
4, 6, and 9) rather than generic national study material, so the state
answers reflect Georgia law — 24 hours of CE per four-year renewal, not the
36 that national guides quote; designated agency permitted; no tenancy by the
entirety; attorney-conducted closings; $1.00/$1,000 transfer tax.

### Modes

- **Practice quiz** — pick National, Georgia, or exam-weighted Mixed; pick a
  single topic or let it weight topics the way the real exam does.
- **Weak-spot quiz** — draws more heavily from topics *and* individual
  questions you have missed before, instead of random selection.
- **Full mock exam** — 132 questions built to the real blueprint, timed.
- **Math practice** — 15 problem generators (commission splits, tax and rent
  proration, LTV, points, area, acreage, appreciation, interest, seller's net,
  Georgia transfer tax, qualifying ratios, buyer's cash to close, seller's net
  proceeds, and proration direction). Every problem shows a numbered worked
  solution, and the wrong answers are built from the mistakes people actually
  make. The three closing generators feed the Comprehensive subtest.

Every question shows, immediately after you answer: right or wrong, the
correct choice, why it's correct, and the **concept being tested** so you
learn the rule instead of the question.

Timed mode allows 75 seconds per question. Unanswered questions score as
wrong, same as the real exam.

### Weak spots

A dedicated section ranking your topics weakest-first, with exam weight
breaking ties, so a bad score in a 13-question topic outranks a bad score in a
4-question one. Every row has a drill button. Below it: math problem types you
are under 80% on, and topics you have answered fewer than 3 questions in --
because untested is not the same as weak, but it is worth finding out.

### Dashboard

Score per topic over time, drawn as a sparkline per topic with the 75% pass
line marked. Weakest topics sort to the top. Separate accuracy and trend for
the National and Georgia portions, plus a per-problem-type breakdown of your
math.

### Study plan

Enter your exam date and how many hours a week you can study. The plan splits
the runway into phases — build coverage, weak-area drill, then mock exams and
review — and allocates each week's questions 80/52 the way the exam is
weighted. Focus topics are chosen from your actual miss data, falling back to
the weak areas you checked off until there's enough history.

## Keyboard shortcuts

`A` `B` `C` `D` answer, `Enter` or `Space` advance to the next question.

## Your data

Progress lives in `data/progress.json` — plain JSON, easy to inspect or back
up. Writes are atomic, so an interrupted save cannot corrupt your history.
Deleting the file resets everything.

## Layout

```
server.py             HTTP server + JSON API (stdlib only)
online/               single-file build sources + the Artifact fragment
docs/index.html       the standalone build GitHub Pages serves
greprep/
  topics.py           exam structure and per-topic weights
  questions.py        bank loading, weak-spot selection, mock exam blueprint
  mathgen.py          12 math generators with worked solutions
  store.py            progress persistence and reporting
  scheduler.py        study plan generator
  banks/*.json        the question banks (built, not hand-edited)
web/                  index.html, style.css, app.js
tools/
  build_banks.py      rebuilds banks/*.json from the _*.py sources
  build_online.py     bundles everything into online/ga-real-estate.html
                      (Artifact fragment) and docs/index.html (standalone)
  _national_*.py      national questions, readable and diffable
  _national_hard_*.py the national hard tier
  _georgia_*.py       Georgia questions
  _georgia_hard.py    the Georgia hard tier
  _comp_*.py          the comprehensive subtest
data/progress.json    your history
```

### Adding questions

Edit the relevant `tools/_national_*.py` or `tools/_georgia_*.py`, then:

```bash
cd ~/ga-realestate-prep && python3 tools/build_banks.py
```

The builder rejects duplicate questions (within a bank and across banks),
duplicate answer choices, missing explanations, unknown topics, and bad
difficulty values, and it shuffles each question's choices so the answer key
isn't clustered in one position. Mark a hard question by adding
`"difficulty": 2`; anything unmarked is core. Restart the server to pick up the
new bank.

## A caveat worth reading

These questions were written to match the style and difficulty of the PSI
exam, and the Georgia material is grounded in the GREC InfoBase — but the
InfoBase itself carries some dated references, and license law changes. This
app is practice, not an authoritative statement of current Georgia law. For
anything you plan to rely on, check the current GREC rules at
<https://grec.state.ga.us>.
