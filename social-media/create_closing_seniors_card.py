#!/usr/bin/env python3
"""Closing series 5 of 5 (pre-ledger): the Social Security claim he keeps repeating. Anchored to 2025-12-social-security-tax,
2026-09-09-town-hall-social-security-tax-credit, 2026-10-15-tax-claims-social-security-cola."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()
y = c.badge(58, "THE RECORD, 3 OF 5")
y = c.title(y, '"No Tax on Social Security." Four Times. Still Not What the Law Says.', size=28)
y = c.subtitle(y + 6, "The claim aimed at seniors, checked each time he made it. The law never changed how benefits are taxed.", size=14)
y = c.divider(y + 12)

tl_h = 250
c.panel(44, y + 2, c.w - 44, y + 2 + tl_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(c.w / 2, y + 26, "WHAT HE SAID, AND WHEN", size=14, bold=True, fill=RED, anchor="mm")
steps = [
    ("JULY 11, 2025", '"88% of seniors will no', 'longer pay federal tax on', 'their Social Security benefits."', "Rated MISLEADING, Dec 2025"),
    ("SEPT 1, 2026", "A 76-year-old asked at a", "town hall. He said three times", 'it was a "tax credit."', "It is a deduction. MISLEADING"),
    ("OCT 6, 2026", '"We gave no tax on Social', 'Security for our seniors."', "WETM debate.", "Rated FALSE, Oct 15"),
    ("OCT 14, 2026", 'The law "eliminated taxes on', 'Social Security for middle', 'class seniors." To WGRZ.', "Rated FALSE, Oct 15"),
]
n = len(steps); inner_w = c.w - 44 * 2 - 24; step_w = inner_w / n
for i, (when, *lines) in enumerate(steps):
    cx = 44 + 12 + step_w * i + step_w / 2
    c.text(cx, y + 66, when, size=14, bold=True, fill=NAVY, anchor="mm")
    for j, ln in enumerate(lines):
        c.text(cx, y + 98 + j * 26, ln, size=12, bold=(j == 3), fill=RED if j == 3 else DARK, anchor="mm")
y = y + 2 + tl_h + 12

col_w = (c.w - 44 * 2 - 16) // 2
col_h = 346
lx, rx = 44, 44 + col_w + 16
top = y
c.panel(lx, top, lx + col_w, top + col_h, fill="#EBF8F0", outline="#9AE6B4")
c.text(lx + col_w / 2, top + 30, "WHAT THE LAW ACTUALLY DID", size=15, bold=True, fill=GREEN, anchor="mm")
for i, (t, b) in enumerate([("A $6,000 deduction per person 65 and over,", True), ("tax years 2025 through 2028.", True), ("", False),
                            ("Shrinks by 6 cents per dollar of income", False), ("over $75,000 ($150,000 joint).", False), ("", False),
                            ("Worth $600 to a senior in the 10% bracket.", False), ("$0 to a senior with no taxable income.", False)]):
    c.text(lx + col_w / 2, top + 72 + i * 32, t, size=13, bold=b, fill=DARK, anchor="mm")
c.panel(rx, top, rx + col_w, top + col_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(rx + col_w / 2, top + 30, "WHAT IT DID NOT DO", size=15, bold=True, fill=RED, anchor="mm")
for i, (t, b) in enumerate([("It did not touch the rules for taxing", True), ("Social Security benefits (IRC Sec. 86).", True), ("", False),
                            ("Up to 85% of benefits remain taxable", False), ("above the same thresholds as before.", False), ("", False),
                            ('Also: "doubled the Child Tax Credit" was', False), ("the 2017 law. His moved it $2,000 to $2,200.", False)]):
    c.text(rx + col_w / 2, top + 72 + i * 32, t, size=13, bold=b, fill=DARK, anchor="mm")
y = top + col_h + 14

kick_h = 84
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 26, "A real, temporary deduction for most seniors. Not the elimination of a tax, and not a credit.",
       size=13, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 56, "Corrected in December. Repeated in September and October.", size=18, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 14
c.text(c.w / 2, y, "Sources: P.L. 119-21 Sec. 70103 and 70104 (govinfo)  ·  IRC Sec. 86  ·  his July 11, 2025 release  ·  Sept 1, 2026 town hall audio  ·  WETM Oct 6  ·  WGRZ Oct 14", size=10.5, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "Full entries at langworthywatch.org", size=11, fill=MUTED, anchor="mm")
c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "closing_3_seniors_card.png"), to_desktop=True)
