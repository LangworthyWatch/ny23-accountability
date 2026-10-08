#!/usr/bin/env python3
"""Social card: "My Dairy Farm Resiliency Act strengthened the Dairy Margin Coverage program" vs. the record.

Anchored to content/fact-checks/2026-10-08-dairy-farm-resiliency-act-dmc.md (verdict: MISLEADING).

Hero is the bill's own history in one number. Middle is a four-step timeline. Columns are the fair reading
and the record. Light house style, 1080x1080, no em dashes (enforced).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(58, "MISLEADING")
y = c.title(y, '"My Dairy Farm Resiliency Act Strengthened" the Dairy Safety Net.', size=27)
y = c.title(y + 2, 'His Bill Never Got a Hearing.', size=27)
y = c.subtitle(y + 6, 'Oct 7, 2026 post on his official page. What the bill texts and status files show.', size=15)
y = c.divider(y + 12)

# ---- hero ---------------------------------------------------------------
hero_h = 124
c.panel(44, y + 2, c.w - 44, y + 2 + hero_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(160, y + 44, "0", size=54, impact=True, fill=RED, anchor="mm")
c.text(160, y + 84, "hearings, markups or votes", size=13, bold=True, fill=MUTED, anchor="mm")
c.text(160, y + 102, "on H.R. 294 in 21 months", size=13, bold=True, fill=MUTED, anchor="mm")
c.text(300, y + 30, 'His post: "My Dairy Farm Resiliency Act strengthened the Dairy', size=15, bold=True, fill=DARK, anchor="lm")
c.text(300, y + 52, 'Margin Coverage program. It protects up to 6 million pounds of milk."', size=15, bold=True, fill=DARK, anchor="lm")
c.text(300, y + 80, "The 6-million-pound change is real. It became law in the One Big Beautiful", size=14, fill=DARK, anchor="lm")
c.text(300, y + 102, "Bill Act, Sec. 10313. His bill was referred to subcommittee Feb 14, 2025. Then nothing.", size=14, fill=DARK, anchor="lm")
y = y + 2 + hero_h + 12

# ---- timeline -----------------------------------------------------------
tl_h = 150
c.panel(44, y, c.w - 44, y + tl_h, fill="#EDF2F7", outline=BORDER)
c.text(c.w / 2, y + 24, "WHERE THE 6-MILLION-POUND PROVISION CAME FROM", size=14, bold=True, fill=NAVY, anchor="mm")
steps = [
    ("JUNE 2023", "Rep. Marc Molinaro files", "the Dairy Farm Resiliency Act.", "Same name, same text.", "Langworthy: not a cosponsor."),
    ("MAY 2024", "House Ag Committee puts", "5M to 6M in its own farm bill,", "H.R. 8467. Ordered reported", "33 to 21."),
    ("JAN 2025", "Molinaro has lost his seat.", "Langworthy refiles the bill", "as H.R. 294. Referred to", "subcommittee. No action since."),
    ("JULY 2025", "OBBBA Sec. 10313 enacts the", "committee's text: 6M pounds,", "2021-23 history, 2031.", "H.R. 294 not a related bill."),
]
n = len(steps)
inner_w = c.w - 44 * 2 - 24
step_w = inner_w / n
for i, (when, *lines) in enumerate(steps):
    cx = 44 + 12 + step_w * i + step_w / 2
    c.text(cx, y + 50, when, size=14, bold=True, fill=RED if i in (1, 3) else NAVY, anchor="mm")
    for j, ln in enumerate(lines):
        c.text(cx, y + 72 + j * 17, ln, size=11.5, fill=DARK, anchor="mm")
    if i < n - 1:
        c.text(44 + 12 + step_w * (i + 1), y + 50, ">", size=16, bold=True, fill=MUTED, anchor="mm")
y += tl_h + 14

# ---- two columns --------------------------------------------------------
col_w = (c.w - 44 * 2 - 16) // 2
col_h = 300
lx, rx = 44, 44 + col_w + 16
top = y

c.panel(lx, top, lx + col_w, top + col_h, fill="#EBF8F0", outline="#9AE6B4")
c.text(lx + col_w / 2, top + 30, "WHAT IS TRUE, AND FAIR", size=16, bold=True, fill=GREEN, anchor="mm")
for i, (txt, bold) in enumerate([
        ("Tier I coverage did rise from 5 to", True),
        ("6 million pounds, per USDA.", True),
        ("", False),
        ("His bill contains that line.", False),
        ("He sat on the Ag Committee", False),
        ("when it adopted the text in 2024.", False),
        ("", False),
        ("He voted for the law twice", False),
        ("(Rolls 145 and 190, 2025).", False)]):
    c.text(lx + col_w / 2, top + 66 + i * 26, txt, size=14, bold=bold, fill=DARK, anchor="mm")

c.panel(rx, top, rx + col_w, top + col_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(rx + col_w / 2, top + 30, "WHAT THE RECORD SHOWS", size=16, bold=True, fill=RED, anchor="mm")
for i, (txt, bold) in enumerate([
        ("His bill's one original idea, a", True),
        ("five-year history reset, was", True),
        ("not enacted.", True),
        ("", False),
        ("The enacted section tracks the", False),
        ("committee's 2024 bill line by line.", False),
        ("", False),
        ("The dairy lobby credits Chairman", False),
        ("Thompson. Neither names him.", False)]):
    c.text(rx + col_w / 2, top + 66 + i * 26, txt, size=14, bold=bold, fill=DARK, anchor="mm")
y = top + col_h + 14

# ---- kicker -------------------------------------------------------------
kick_h = 96
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 30, "He supported the change and voted for it. His bill did not do it.",
       size=13, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 62, "A colleague's bill, the committee's text, the chairman's law.",
       size=18, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 16

c.text(c.w / 2, y, "Sources: H.R. 294, H.R. 4125, H.R. 8467 and P.L. 119-21 texts and status (govinfo)  ·  House Clerk rolls 145, 190  ·  USDA FSA Sept 30 2026  ·  NMPF May 2025", size=10.5, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "Full entry at langworthywatch.org", size=11, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "dairy_dmc_card.png"), to_desktop=True)
