#!/usr/bin/env python3
"""Social card: "eliminated taxes on Social Security for middle class seniors" vs. the record, plus six tax claims.

Anchored to content/fact-checks/2026-10-15-tax-claims-social-security-cola.md (verdict: MISLEADING; Claim 1 FALSE,
Claim 2 MISLEADING, Claim 3 TRUE, Claim 4 MISLEADING, Claim 6 MISLEADING, Claim 7 TRUE).

Hero is his word ("ELIMINATED") vs. the Tax Policy Center's estimate ("ABOUT HALF" of Social Security recipients
still pay some income tax on benefits). Red = the claim, navy = the record. The ledger below carries six claims with
per-claim verdicts so the TRUE findings are on the card too. Light house style, 1080x1080, no em dashes (enforced).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, ORANGE, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(58, "MISLEADING")
y = c.title(y, '"Eliminated Taxes on Social Security for Middle Class Seniors."', size=26)
y = c.title(y + 2, "The Law Never Changed the Rules for Taxing Benefits.", size=26)
y = c.subtitle(y + 6, "His Oct 6 debate and Oct 13-15 official-page posts. Seven tax claims checked against the law.", size=15)
y = c.divider(y + 12)

# ---- hero: word vs. estimate ----------------------------------------------------
col_w = (c.w - 44 * 2 - 16) // 2
hero_h = 214
lx, rx = 44, 44 + col_w + 16
top = y + 2

c.panel(lx, top, lx + col_w, top + hero_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(lx + col_w / 2, top + 26, "HIS STATEMENT, OCT 14", size=14, bold=True, fill=RED, anchor="mm")
c.text(lx + col_w / 2, top + 86, "ELIMINATED", size=54, impact=True, fill=RED, anchor="mm")
for i, ln in enumerate(['"the Working Families Tax Cuts we passed',
                        'last year eliminated taxes on Social',
                        'Security for middle class seniors."']):
    c.text(lx + col_w / 2, top + 140 + i * 23, ln, size=14.5, bold=(i >= 1), fill=DARK, anchor="mm")

c.panel(rx, top, rx + col_w, top + hero_h, fill="#EDF2F7", outline="#A3BFD9")
c.text(rx + col_w / 2, top + 26, "TAX POLICY CENTER ESTIMATE", size=14, bold=True, fill=NAVY, anchor="mm")
c.text(rx + col_w / 2, top + 86, "ABOUT HALF", size=54, impact=True, fill=NAVY, anchor="mm")
for i, ln in enumerate(["of Social Security recipients will still",
                        "pay some income tax on their benefits.",
                        "The tax rule for benefits was \"not changed\" (CRS)."]):
    c.text(rx + col_w / 2, top + 140 + i * 23, ln, size=14.5, bold=(i <= 1), fill=DARK, anchor="mm")
y = top + hero_h + 14

# ---- ledger --------------------------------------------------------------------
rows = [
    ("FALSE", RED, '"Eliminated taxes on Social Security for middle class seniors."',
     "The law added a $6,000 deduction for most taxpayers 65+, 2025 to 2028. Benefits stay taxable."),
    ("MISLEADING", ORANGE, '"Our Working Families Tax Cuts deliver $6,000 more relief."',
     "It is a deduction: worth $600 to $1,320 a year to a single senior in the 10-22% brackets."),
    ("TRUE", GREEN, '"A 3.6% COLA means $75 more a month for retirees."',
     "Matches SSA's Oct 14 announcement. The adjustment is automatic, tied to inflation."),
    ("MISLEADING", ORANGE, '"We doubled the child tax credit." (debate)',
     "The 2017 law doubled it. The law he voted for raised it from $2,000 to $2,200."),
    ("MISLEADING", ORANGE, '"No tax on tips, no tax on overtime."',
     "Capped deductions through 2028. Overtime base pay is still taxed."),
    ("TRUE", GREEN, '"Tax refund checks went up 11% year over year." (debate)',
     "IRS: the average refund was up 11.5% through May 8, 2026."),
]
row_h = 62
box_h = 34 + row_h * len(rows)
c.panel(44, y, c.w - 44, y + box_h, fill=WHITE, outline=BORDER)
c.text(c.w / 2, y + 20, "SIX OF THE SEVEN CLAIMS", size=14, bold=True, fill=NAVY, anchor="mm")
for i, (label, color, line1, line2) in enumerate(rows):
    ry = y + 36 + i * row_h
    c.rect(62, ry + 6, 196, ry + 36, fill=color, radius=6)
    c.text(129, ry + 21, label, size=13, bold=True, fill=WHITE, anchor="mm")
    c.text(214, ry + 12, line1, size=14.5, bold=True, fill=DARK, anchor="lm")
    c.text(214, ry + 34, line2, size=13.5, fill=DARK, anchor="lm")
y += box_h + 12

# ---- kicker --------------------------------------------------------------------
kick_h = 84
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 27, "The COLA and refund numbers are right. The law did cut taxes for many seniors.",
       size=13, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 57, "It did not make Social Security tax-free. The rules for taxing benefits did not change.",
       size=17, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 12

c.text(c.w / 2, y, "Sources: P.L. 119-21 Secs. 70102-70104, 70201-70202  ·  CRS R48613  ·  Tax Policy Center, July 2025  ·  SSA, Oct 14 2026  ·  IRS filing statistics  ·  WETM debate",
       size=10.5, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "Full entry at langworthywatch.org", size=11, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "tax_claims_ss_cola_card.png"), to_desktop=True)
