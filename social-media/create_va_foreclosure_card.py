#!/usr/bin/env python3
"""Social card: the VA home loan backstop gap. July 25, 2026."""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lib.card import (Card, NAVY, NAVY_DK, DARK, GOLD, RED, RED_DK, GREEN,
                      ORANGE, BRONZE, MUTED, LIGHTGRAY, BORDER, WHITE)

c = Card(scale=3)

# ── Header ──
c.brand_bar()
y = c.badge(56, "DOCUMENTED PATTERN")
y = c.title(y, "The Backstop Was Gone", size=38)
y = c.title(y + 2, "For 13 Months", size=38)
y += 8
y = c.subtitle(y, "VA ended its foreclosure rescue before the replacement existed", size=16)
y = c.divider(y + 10, margin=48, pad=16)

# ── The headline stat ──
c.text(c.w / 2, y + 46, "10,000+", size=92, impact=True, fill=RED, anchor="mm")
y += 92
c.text(c.w / 2, y + 6, "veterans lost their homes to foreclosure in the gap",
       size=19, bold=True, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 32, "The highest pace of VA loan foreclosures in a decade.",
       size=15, fill="#4A5568", anchor="mm")
c.text(c.w / 2, y + 54, "90,000 more are behind on payments or already in foreclosure.",
       size=15, fill="#4A5568", anchor="mm")
y += 82

# ── Timeline ──
STEPS = [
    ("Mar. 2025", "The mortgage industry tells a House committee exactly\nwhat will happen if VA scraps it: \"Foreclosure. Period.\"", ORANGE),
    ("May 1, 2025", "VA ends VASP anyway. No replacement exists.", RED),
    ("Jul. 30, 2025", "Congress authorizes a replacement. It becomes law.", BRONZE),
    ("Jun. 15, 2026", "VA finally opens it, 10 months after the law passed.", GREEN),
    ("Nov. 28, 2026", "Deadline for mortgage servicers to finish adopting it.", NAVY),
]
LX = 52
for i, (when, what, accent) in enumerate(STEPS):
    lines = what.split("\n")
    row_h = 50 if len(lines) == 1 else 68
    c.rect(LX, y, LX + 5, y + row_h, fill=accent)
    c.rect(LX + 5, y, c.w - 52, y + row_h, fill=WHITE, outline=BORDER, radius=0)
    c.text(LX + 20, y + (25 if len(lines) == 1 else 26), when,
           size=15, bold=True, fill=accent, anchor="lm")
    yy = y + (25 if len(lines) == 1 else 24)
    for ln in lines:
        c.text(LX + 168, yy, ln, size=15, fill=DARK, anchor="lm")
        yy += 20
    y += row_h + 10

y += 14

# ── The gap ──
pan_h = 120
c.panel(52, y, c.w - 52, y + pan_h, fill=NAVY, outline=None, radius=8)
c.text(c.w / 2, y + 30, "13 months with no backstop at all.",
       size=25, bold=True, fill=WHITE, anchor="mm")
c.text(c.w / 2, y + 62, "And servicers have until Nov. 28, 2026 to finish implementing it,",
       size=15, fill="#CBD5E0", anchor="mm")
c.text(c.w / 2, y + 80, "so for some veterans the gap has not closed yet.",
       size=15, fill="#CBD5E0", anchor="mm")
y += pan_h + 18

# ── Fairness ──
c.text(c.w / 2, y + 8, "In fairness: this began under the previous administration, and there is no",
       size=14, fill=GREEN, anchor="mm")
c.text(c.w / 2, y + 27, "Langworthy vote to point to. The replacement passed by voice vote.",
       size=14, fill=GREEN, anchor="mm")
y += 64

# ── Sources + URL ──
c.text(c.w / 2, y + 4,
       "Sources: VA Circular 26-25-2  ·  ICE Mortgage Technology via NPR  ·  Mortgage Bankers Association  ·  VA servicer FAQs",
       size=12, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 34, "langworthywatch.org", size=17, bold=True, fill=NAVY, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "va_foreclosure_card.png"),
       to_desktop=True)
