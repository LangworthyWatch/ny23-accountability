#!/usr/bin/env python3
"""Social card: the rural health fund vs. the cuts in the same law, and the Oversight record.

Anchored to content/fact-checks/2026-09-15-rural-health-fund-vs-cuts-and-oversight.md
(verdict: MISSING CONTEXT).

Hero is the ratio: $50B fund vs. $911B Medicaid cut (KFF from CBO). Left column is the fair
reading. Right column is where the law's money went (CRFB from CBO) and the committee record.
Light house style, 1080x1080, no em dashes (enforced).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(58, "MISSING CONTEXT")
y = c.title(y, '"Historic Investment" in Rural Health: $50 Billion In, $911 Billion Out.', size=27)
y = c.subtitle(y + 6, 'Three posts in one week on the same $76 million. The rest of the One Big Beautiful Bill Act he voted for, per CBO.', size=15)
y = c.divider(y + 12)

# ---- hero ---------------------------------------------------------------
hero_h = 132
c.panel(44, y + 2, c.w - 44, y + 2 + hero_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(170, y + 46, "$2.70", size=46, impact=True, fill=RED, anchor="mm")
c.text(170, y + 88, "cut from rural Medicaid", size=13, bold=True, fill=MUTED, anchor="mm")
c.text(170, y + 106, "per $1 the fund puts in", size=13, bold=True, fill=MUTED, anchor="mm")
c.text(318, y + 30, "Rural Health Transformation Program: $50 billion over five years.", size=15, bold=True, fill=DARK, anchor="lm")
c.text(318, y + 52, "Same law: $911 billion out of federal Medicaid, $137 billion of it rural.", size=15, bold=True, fill=DARK, anchor="lm")
c.text(318, y + 82, "KFF: the fund offsets 37% of the rural Medicaid loss. It ends in 2030;", size=14, fill=DARK, anchor="lm")
c.text(318, y + 104, "most of the cuts land after that. Nine state awards touch NY-23; none of his posts names one.", size=14, fill=DARK, anchor="lm")
y = y + 2 + hero_h + 12

# ---- two columns --------------------------------------------------------
col_w = (c.w - 44 * 2 - 16) // 2
col_h = 372
lx, rx = 44, 44 + col_w + 16
top = y

c.panel(lx, top, lx + col_w, top + col_h, fill="#EBF8F0", outline="#9AE6B4")
c.text(lx + col_w / 2, top + 30, "WHAT IS TRUE, AND FAIR", size=16, bold=True, fill=GREEN, anchor="mm")
for i, (txt, bold) in enumerate([
        ("The fund is real. New York's first", True),
        ("year is $212 million, and he voted", True),
        ("for the law that created it.", True),
        ("", False),
        ("Fraud hearings are oversight. The", False),
        ("committee held two on Minnesota.", False),
        ("", False),
        ("Medicaid oversight also sits with", False),
        ("Energy and Commerce Health, where", False),
        ("he serves. Tariffs offset part of the", False),
        ("cost until the Supreme Court ruling.", False)]):
    c.text(lx + col_w / 2, top + 62 + i * 23, txt, size=14, bold=bold, fill=DARK, anchor="mm")

c.panel(rx, top, rx + col_w, top + col_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(rx + col_w / 2, top + 30, "WHERE THE LAW'S MONEY WENT", size=16, bold=True, fill=RED, anchor="mm")
for i, (txt, bold) in enumerate([
        ("Tax cuts: $5.4 trillion (CBO net: $4.5T).", True),
        ("Defense: $173B. Immigration and", True),
        ("border enforcement: $176B.", True),
        ("", False),
        ("Offsets (Medicaid, SNAP, energy", False),
        ("credits, student loans): $2.5T, less", False),
        ("than half the cost. Rest is borrowed.", False),
        ("", False),
        ("CBO: resources fall for the lowest-", False),
        ("income households, rise for the top.", False),
        ("No refund checks exist.", False)]):
    c.text(rx + col_w / 2, top + 62 + i * 23, txt, size=14, bold=bold, fill=DARK, anchor="mm")
y = top + col_h + 14

# ---- strip --------------------------------------------------------------
strip_h = 112
c.panel(44, y, c.w - 44, y + strip_h, fill="#EDF2F7", outline=BORDER)
c.text(c.w / 2, y + 24, "HIS OVERSIGHT COMMITTEE SINCE THE OBBBA PASSED", size=14, bold=True, fill=NAVY, anchor="mm")
c.text(c.w / 2, y + 52, "Two full-committee hearings on federal funds, both about Minnesota. None on the OBBBA's Medicaid, SNAP or enforcement money.", size=13, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 72, "$176B of it went to DHS and Border Patrol. His votes on subpoenas to Secretary Noem and Border Patrol's Bovino: No and No.", size=13, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 96, "CBO's own table: the law adds $487 billion to the fiscal 2026 deficit ($501 billion with interest), about one dollar in four.", size=12, fill=MUTED, anchor="mm")
y += strip_h + 14

# ---- kicker -------------------------------------------------------------
kick_h = 92
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 28, 'Sept 4: "we created" it. Sept 10: "this historic investment." Sept 11: "now they\'ll have the resources."',
       size=13, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 60, "Five announcements of one award. Zero hearings on the law that made it necessary.",
       size=17, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 16

c.text(c.w / 2, y, "Sources: CBO cost estimates, Jul 21 and Aug 4 2025; CBO distributional analysis, Aug 11 2025; KFF allocation of CBO Medicaid estimates", size=11, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "CRFB, \"What's in the OBBBA\"  ·  House Oversight hearing transcripts and vote sheets  ·  Full entry at langworthywatch.org", size=11, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "rural_fund_vs_cuts_card.png"), to_desktop=True)
