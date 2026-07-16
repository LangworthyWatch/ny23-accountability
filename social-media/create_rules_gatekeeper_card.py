#!/usr/bin/env python3
"""Rules Committee gatekeeper card — same move across four bills. House style."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib.card import Card, NAVY, RED, GREEN, MUTED, DARK, WHITE, BORDER

c = Card(scale=3)
c.brand_bar()
y = c.badge(66, "DOCUMENTED PATTERN")
y = c.title(y, "The Gatekeeper's Seat", size=32)
y = c.subtitle(y + 10, "He holds New York's only seat on the House Rules Committee,", size=15)
y = c.subtitle(y + 4, "the panel that decides what the full House may even vote on.", size=15)
y = c.divider(y + 18)

# --- panel: what he voted to keep off the floor ---
p = y + 16
ph = 300
c.panel(44, p, c.w - 44, p + ph)
c.rect(44, p, c.w - 44, p + 44, fill=RED, radius=8)
c.rect(44, p + 28, c.w - 44, p + 44, fill=RED)
c.text(74, p + 22, "WHAT HE VOTED TO KEEP OFF THE FLOOR", size=17, bold=True, fill=WHITE, anchor="lm")
rows = [
    ("Medicaid", "the vote to strike the cuts"),
    ("Tariffs", "the vote to end the tariffs hitting his district"),
    ("Veterans", "the Star Act without the benefit cuts"),
    ("Epstein", "the vote to force out the files"),
]
ry = p + 84
for subj, fix in rows:
    c.d.ellipse([c._p(74), c._p(ry - 4), c._p(83), c._p(ry + 5)], fill=RED)
    c.text(96, ry, subj + ":", size=17, bold=True, fill=DARK, anchor="lm")
    c.text(96, ry + 26, fix, size=15, fill=MUTED, anchor="lm")
    ry += 58

c.text(c.w / 2, p + ph + 44, "Four unrelated bills. The subjects have nothing in common. The vote does.",
       size=16, bold=True, fill=NAVY, anchor="mm")
c.text(c.w / 2, p + ph + 82, "He is 1 of 9 majority members, and the state's only seat on the committee.",
       size=15, fill=MUTED, anchor="mm")

c.kicker(c.h - 176,
         "Every time: NO on letting the House vote on the popular fix.",
         "YES on the rule that closed the door.")
c.footer_bar()
c.save("social-media/rules_gatekeeper_card.png", to_desktop=True)
