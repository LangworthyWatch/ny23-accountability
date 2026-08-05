#!/usr/bin/env python3
"""Social card: the recurring gap between a bill's popular framing and its actual text.

Five published entries, five verdicts, all cross-checked against their frontmatter:
  SAVE Act (H.R. 22, promoted)              2026-02-10  MISLEADING
  Stop Insider Trading Act (H.R. 7008, cosponsor) 2026-07-21  MISLEADING
  KIDS Act (H.R. 7757, voted for)           2026-06-30  MISSING CONTEXT
  SECURE Data Act (H.R. 8413, cosponsor)    2026-06-06  DOCUMENTED PATTERN
  Infrastructure Expansion Act (H.R. 3548, his bill) 2026-06-24 MISSING CONTEXT

Documents what the framing says vs. what the text does. Makes no claim about intent.
Light house style, 1080x1080, no em dashes (enforced by Card.save).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

ROWS = [
    ("SAVE ACT  ·  H.R. 22  ·  promoted on Facebook",
     "\"83% of Americans support showing identification to vote\"",
     "Requires proof of citizenship, delivered in person. A standard REAL ID does not count."),
    ("STOP INSIDER TRADING ACT  ·  H.R. 7008  ·  cosponsor",
     "Members \"shouldn't run from a briefing to a broker\"",
     "Does not ban selling stock. The bill's own sponsor calls that framing \"accurate but misleading.\""),
    ("KIDS ACT  ·  H.R. 7757  ·  voted for it",
     "\"Holds Big Tech accountable\"",
     "The House version dropped the duty of care, the bill's core accountability tool."),
    ("SECURE DATA ACT  ·  H.R. 8413  ·  cosponsor",
     "Named for securing your data",
     "No private right of action. Its preemption clause would override stronger state privacy laws."),
    ("INFRASTRUCTURE EXPANSION ACT  ·  H.R. 3548  ·  his own bill",
     "Named for expanding infrastructure",
     "Repeals New York's Scaffold Law, the fall-injury protection, on federally funded projects."),
]

c = Card(scale=2)
c.brand_bar()

y = c.badge(62, "DOCUMENTED PATTERN")
y = c.title(y, "The Popular Headline, and What Is In the Bill", size=29)
y = c.divider(y + 10)

# hero stat band
hero_h = 76
c.panel(44, y + 2, c.w - 44, y + 2 + hero_h, fill="#EDF2F7", outline=BORDER)
c.text(112, y + 2 + hero_h / 2, "5", size=60, impact=True, fill=NAVY, anchor="mm")
c.text(170, y + 30, "bills where the popular framing and the bill text diverge.",
       size=18, bold=True, fill=DARK, anchor="lm")
c.text(170, y + 58, "Five separate published fact-checks. Five different policy areas.",
       size=15, fill=MUTED, anchor="lm")
y = y + 2 + hero_h + 10

row_h, gap = 105, 6
top = y
for i, (bill, said, text) in enumerate(ROWS):
    ry = top + i * (row_h + gap)
    c.panel(44, ry, c.w - 44, ry + row_h, fill=WHITE, outline=BORDER)
    c.text(62, ry + 17, bill, size=13, bold=True, fill=NAVY, anchor="lm")
    # green marker + framing
    c.rect(62, ry + 33, 68, ry + 55, fill="#9AE6B4")
    c.text(80, ry + 44, said, size=16, fill=DARK, anchor="lm")
    # red marker + what the text does
    c.rect(62, ry + 63, 68, ry + 92, fill="#FEB2B2")
    c.text(80, ry + 77, text, size=15, bold=True, fill=DARK, anchor="lm")
y = top + len(ROWS) * (row_h + gap) + 9

kick_h = 100
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 32, "Each policy is genuinely popular. Each bill is real, and some of them do real things.",
       size=16, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 66, "The gap is between how the bill is described and what its text does.",
       size=18, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 22

c.text(c.w / 2, y, "Verdicts as published: Misleading, Misleading, Missing Context, Documented Pattern, Missing Context.",
       size=14, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 21, "Bill text from congress.gov and govinfo. This documents wording, not intent.",
       size=14, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "headline_vs_text_pattern_card.png"),
       to_desktop=True)
