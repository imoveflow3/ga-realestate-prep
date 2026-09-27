"""Copy and icons for the public pages.

Shared by tools/build_paid.py (the Cloudflare build) and
tools/build_online.py (the GitHub Pages build) so the two front doors
cannot drift apart.
"""

ICONS = {
    "quiz":  '<rect x="3.5" y="3.5" width="17" height="17" rx="4"/>'
             '<path d="M8.6 12.2l2.3 2.4 4.5-5"/>',
    "book":  '<path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5Z"/>'
             '<path d="M4 20.5A2.5 2.5 0 0 1 6.5 18H20v3H6.5"/>',
    "math":  '<rect x="4" y="3" width="16" height="18" rx="3"/>'
             '<path d="M8 8h8M8 12h3M8 16h3M15 12v4M13 14h4"/>',
    "cards": '<rect x="3" y="7" width="13" height="13" rx="2.5"/>'
             '<path d="M7.5 4h11A2.5 2.5 0 0 1 21 6.5v11"/>',
    "target": '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="3.4"/>'
              '<path d="M12 1.6v2.6M12 19.8v2.6M22.4 12h-2.6M4.2 12H1.6"/>',
    "note":  '<path d="M5 3.5h14v17l-3.2-2.2-3.4 2.2-3.4-2.2L5.8 20.5Z"/>'
             '<path d="M9 8.5h6M9 12.5h6"/>',
}

FEATURES = [
    ("quiz", "Practice quizzes",
     "Timed sets, scored National and Georgia separately"),
    ("book", "Study notes",
     "%(terms)d terms defined, with a quiz after every section"),
    ("math", "Real estate math",
     "Every calculation broken into steps you can follow"),
    ("cards", "Vocabulary drill",
     "Definitions, flashcards and spaced repetition"),
    ("target", "Weak-spot targeting",
     "Drills for the sub-topics dragging your score down"),
    ("note", "Your notebook",
     "Every miss kept with the reason, on your account"),
]


AUDIENCE = [
    ["You have finished the 75-hour course",
     "The course teaches you the material. It does not sit you down in front "
     "of a hundred and thirty-two questions written the way the exam writes "
     "them, and that is a different skill."],
    ["You are sitting it for the first time",
     "Most people who fail do not fail both halves. They clear National and "
     "miss Georgia, or the other way round. This tracks the two portions "
     "apart, because that is how you are scored."],
    ["You failed one half and have to retake",
     "You only resit the portion you missed. The weak-spot drill finds which "
     "narrow topics actually sank it, rather than making you reread the lot."],
]

WHY = {
    "title": "Built by someone sitting the same exam.",
    "paras": [
        "This started as one person's study tool for the Georgia salesperson "
        "exam, built because the free material was thin and the paid material "
        "was ninety dollars. It got them through, and it is still here.",
        "The Georgia half was not copied out of a cram guide. It was read out "
        "of the Georgia Real Estate Commission's own InfoBase and the Georgia "
        "Code, chapter by chapter. That matters in the places where the guides "
        "are simply wrong \u2014 continuing education in Georgia is 24 hours "
        "per four-year renewal, not the 36 that national study guides quote.",
        "The national half follows the standard content outline the licensing "
        "exams use: agency, contracts, financing, valuation, property "
        "ownership, transfer of title, practice and disclosures, and the maths.",
    ],
}

STEPS = [
    ["01", "Read it once",
     "Notes for every topic on the blueprint, in plain sentences, with a short "
     "quiz after each section so it sticks the first time."],
    ["02", "Quiz until it holds",
     "Timed sets at the real difficulty. Every answer tells you why it is "
     "right and names the concept being tested."],
    ["03", "Attack the gaps",
     "Anything you miss lands in your notebook and on the flashcard deck, and "
     "comes back until it stops being a gap."],
]

HONEST = [
    "Not affiliated with, endorsed by, or connected to the Georgia Real Estate "
    "Commission, PSI, or any school or exam vendor.",
    "Not legal advice and not an official statement of Georgia law. Rules "
    "change; grec.state.ga.us is the authority, not this site.",
    "Not a substitute for the 75-hour pre-licence course Georgia requires "
    "before you may sit the exam. You still have to do that.",
    "Not a guarantee. It is practice, and practice is only worth what you put "
    "into it.",
]
