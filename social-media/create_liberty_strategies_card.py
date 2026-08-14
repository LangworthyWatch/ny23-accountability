#!/usr/bin/env python3
"""Social card: what the disclosure rules make checkable, and what they do not.

Anchored to content/fact-checks/2026-06-24-liberty-strategies-disclosure.md
(published verdict: MISSING CONTEXT).

DESIGN NOTE ON COLOR: the right-hand panel is deliberately NOT red. The entry
makes no allegation of wrongdoing, and red in this house style signals an
adversarial contrast. The gap here is in the disclosure regime, not in his
conduct, so the panel is neutral amber. Green on the left is used because that
side genuinely verifies in his favor.
Light house style, 1080x1080, no em dashes (enforced by Card.save).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, GREEN, BRONZE, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(60, "MISSING CONTEXT")
y = c.title(y, "Where the Rules Let You Check, He Checks Out", size=29)
y = c.subtitle(y + 6, "And where they do not, no one can. Both halves are his own filings.", size=16)
y = c.divider(y + 12)

# ---- hero ---------------------------------------------------------------
hero_h = 116
c.panel(44, y + 2, c.w - 44, y + 2 + hero_h, fill="#FFFAF0", outline="#F6C177")
c.text(140, y + 2 + hero_h / 2, "N/A", size=58, impact=True, fill=BRONZE, anchor="mm")
c.text(250, y + 38, "is the amount of spouse consulting income his", size=18, bold=True, fill=DARK, anchor="lm")
c.text(250, y + 66, "filings report. Every year. That is the rule,", size=18, bold=True, fill=DARK, anchor="lm")
c.text(250, y + 94, "not an omission: the House form asks for the source, never the amount.", size=13, fill=MUTED, anchor="lm")
y = y + 2 + hero_h + 12

# ---- two columns --------------------------------------------------------
col_w = (c.w - 44 * 2 - 16) // 2
col_h = 352
lx, rx = 44, 44 + col_w + 16
top = y

c.panel(lx, top, lx + col_w, top + col_h, fill="#EBF8F0", outline="#9AE6B4")
c.text(lx + col_w / 2, top + 32, "CHECKABLE BY DESIGN", size=16, bold=True, fill=GREEN, anchor="mm")
c.text(lx + col_w / 2, top + 56, "his stock trading", size=14, fill=MUTED, anchor="mm")
c.text(lx + col_w / 2, top + 122, "0", size=64, impact=True, fill=GREEN, anchor="mm")
c.text(lx + col_w / 2, top + 184, "transaction reports filed,", size=17, bold=True, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 210, "in four years.", size=17, bold=True, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 248, "Named assets. Dated filings.", size=15, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 274, "Index funds and TSP.", size=15, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 312, "His claim is true. We say so.", size=15, bold=True, fill=GREEN, anchor="mm")

c.panel(rx, top, rx + col_w, top + col_h, fill="#FFFAF0", outline="#F6C177")
c.text(rx + col_w / 2, top + 32, "NOT CHECKABLE BY DESIGN", size=16, bold=True, fill=BRONZE, anchor="mm")
c.text(rx + col_w / 2, top + 56, "spouse consulting income", size=14, fill=MUTED, anchor="mm")
c.text(rx + col_w / 2, top + 122, "1 line", size=54, impact=True, fill=BRONZE, anchor="mm")
c.text(rx + col_w / 2, top + 184, "on 4 of his 5 filings.", size=17, bold=True, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 210, "No amount. No clients.", size=17, bold=True, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 248, "Last documented client", size=15, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 274, "payments were in 2022.", size=15, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 312, "Nothing here is assessable.", size=15, bold=True, fill=BRONZE, anchor="mm")
y = top + col_h + 14

# ---- fairness strip -----------------------------------------------------
strip_h = 112
c.panel(44, y, c.w - 44, y + strip_h, fill="#EDF2F7", outline=BORDER)
c.text(c.w / 2, y + 26, "WHAT THIS IS NOT", size=15, bold=True, fill=NAVY, anchor="mm")
third = (c.w - 88) // 3
for i, (val, lab) in enumerate([("No wrongdoing", "none alleged, and none found"),
                                ("Not concealment", "the rules ask source, not amount"),
                                ("A career is normal", "a spouse working is lawful and ordinary")]):
    cx = 44 + i * third + third / 2
    c.text(cx, y + 62, val, size=18, bold=True, fill=NAVY, anchor="mm")
    c.text(cx, y + 90, lab, size=12, fill=DARK, anchor="mm")
y += strip_h + 14

# ---- kicker -------------------------------------------------------------
kick_h = 98
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 32, "Congress wrote rules that make stock trading checkable. It did not write them here.",
       size=16, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 66, "The gap is in the disclosure regime, not in his answer.", size=18, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 20

c.text(c.w / 2, y, "Sources: five House financial disclosures, 2022 to 2026  ·  FEC operating expenditures  ·  NYS Board of Elections", size=13, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 20, "No payments to the firm were located in either database for 2023 to 2025", size=13, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "liberty_strategies_card.png"), to_desktop=True)
