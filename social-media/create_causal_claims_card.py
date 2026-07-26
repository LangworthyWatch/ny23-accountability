#!/usr/bin/env python3
"""Social card: two causal claims, and the one he rejected. July 25, 2026."""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lib.card import (Card, NAVY, NAVY_DK, DARK, GOLD, RED, RED_DK, GREEN,
                      ORANGE, BRONZE, MUTED, LIGHTGRAY, BORDER, WHITE)

c = Card(scale=3)

# ── Header ──
c.brand_bar()
y = c.badge(56, "NOT SUPPORTED")
y = c.title(y, "Two Causal Claims.", size=38)
y = c.title(y + 2, "Neither One Supported.", size=38)
y += 8
y = c.subtitle(y, "Three weeks apart, he said one thing caused another. Both times, as fact.", size=15)
y = c.divider(y + 10, margin=48, pad=14)

# ── The two claims ──
CLAIMS = [
    ("JULY 2  ·  ON BUFFALO'S FIREWORKS",
     "\"...has everything to with THAT and nothing to",
     "do with logistics.  #facts\"",
     "The city had already given a written reason: no site could",
     "clear a safe fireworks fallout zone downtown."),
    ("JULY 25  ·  ON THE MAYOR OF NEW YORK",
     "\"...has made every Jewish New Yorker",
     "less safe.\"",
     "No law enforcement official and no charging document has",
     "connected the July 23 attack to anything Mamdani said."),
]
for label, q1, q2, r1, r2 in CLAIMS:
    pan_h = 186
    c.rect(48, y, 53, y + pan_h, fill=RED)
    c.panel(53, y, c.w - 48, y + pan_h, fill=WHITE, outline=BORDER, radius=0)
    c.text(74, y + 26, label, size=13, bold=True, fill=RED_DK, anchor="lm")
    c.text(74, y + 60, q1, size=18, bold=True, fill=DARK, anchor="lm")
    c.text(74, y + 86, q2, size=18, bold=True, fill=DARK, anchor="lm")
    c.text(74, y + 118, r1, size=14, fill="#4A5568", anchor="lm")
    c.text(74, y + 138, r2, size=14, fill="#4A5568", anchor="lm")
    c.text(74, y + 166, "EVIDENCE OFFERED:  NONE", size=14, bold=True, fill=RED, anchor="lm")
    y += pan_h + 16

y += 10

# ── The turn ──
pan_h = 168
c.panel(48, y, c.w - 48, y + pan_h, fill=NAVY, outline=None, radius=8)
c.text(c.w / 2, y + 32, "Three weeks earlier, the same claim was made about him.",
       size=18, bold=True, fill=WHITE, anchor="mm")
c.text(c.w / 2, y + 62, "Buffalo's mayor said his remarks helped fuel threats against City Hall.",
       size=15, fill="#CBD5E0", anchor="mm")
c.text(c.w / 2, y + 97, "\"Sean Ryan can call me whatever he wants. I'm not backing down.\"",
       size=18, bold=True, fill=GOLD, anchor="mm")
c.text(c.w / 2, y + 128, "He was right to reject it. That claim is not established either,",
       size=15, fill="#93A9C4", anchor="mm")
c.text(c.w / 2, y + 147, "and this page does not make it.",
       size=15, fill="#93A9C4", anchor="mm")
y += pan_h + 20

# ── Fairness ──
c.text(c.w / 2, y + 8, "The July 23 attack was real: a man is charged with hate crimes. Criticism of the",
       size=13, fill=GREEN, anchor="mm")
c.text(c.w / 2, y + 26, "mayor came from Democrats and nonpartisan Jewish leaders too, not only Republicans.",
       size=13, fill=GREEN, anchor="mm")
y += 58

# ── Sources + URL ──
c.text(c.w / 2, y + 4,
       "Sources: the posts themselves  ·  City of Buffalo statement  ·  NYPD  ·  amNY  ·  WKBW",
       size=12, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 30, "langworthywatch.org", size=17, bold=True, fill=NAVY, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "causal_claims_card.png"),
       to_desktop=True)
