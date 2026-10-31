#!/usr/bin/env python3
"""Pre-election money filings, entry 2026-10-31-pre-election-money-filings (DOCUMENTED PATTERN).
Every figure is parsed from Langworthy for Congress's own FEC filings (pre-general 2035999; 48-hour notices Oct 16-30)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()
y = c.badge(58, "DOCUMENTED PATTERN  ·  OCT 31, 2026")
y = c.title(y, "His Last Money Before the Vote.", size=30)
y = c.title(y - 2, "Where It Came From. Where It Went.", size=30)
y = c.subtitle(y + 6, "Langworthy for Congress, FEC pre-general report (Oct 1-14) and 48-hour notices through Oct 29.", size=14.5)
y = c.divider(y + 12)

col_w = (c.w - 44 * 2 - 16) // 2
col_h = 372
lx, rx = 44, 44 + col_w + 16
top = y + 2
c.panel(lx, top, lx + col_w, top + col_h, fill="#F0FFF4", outline="#9AE6B4")
c.text(lx + col_w / 2, top + 30, "WHAT CAME IN, OCT 1-14", size=16, bold=True, fill=GREEN, anchor="mm")
c.text(lx + col_w / 2, top + 98, "$6,850", size=58, impact=True, fill=GREEN, anchor="mm")
c.text(lx + col_w / 2, top + 144, "from donors with addresses in the district", size=14, bold=True, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 166, "six contributions, 27% of itemized individual money", size=13, fill=MUTED, anchor="mm")
for i, t in enumerate(["$16,600 of the $25,700 itemized arrived earmarked",
                       "through AIPAC's PAC: 18 donors, Westchester and NYC.",
                       "$26,000 from PACs: AICPA, SpaceX, UPS at $5,000 each.",
                       "Oct 15-29: $79,500 more. $42,000 of it from PACs",
                       "and firms. Three district donors. Three lobbyists."]):
    c.text(lx + col_w / 2, top + 208 + i * 31, t, size=13, bold=(i == 4), fill=DARK, anchor="mm")

c.panel(rx, top, rx + col_w, top + col_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(rx + col_w / 2, top + 30, "WHAT WENT OUT, OCT 1-14", size=16, bold=True, fill=RED, anchor="mm")
c.text(rx + col_w / 2, top + 98, "$551,000", size=58, impact=True, fill=RED, anchor="mm")
c.text(rx + col_w / 2, top + 144, "one television buy, October 9", size=14, bold=True, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 166, "92% of the period's spending; first TV money of the cycle", size=13, fill=MUTED, anchor="mm")
for i, t in enumerate(["$25,000 to the Nassau County Republican Committee,",
                       "Long Island. Largest county-party payment of his cycle.",
                       "(Erie County's committee: $11,500 over two years.)",
                       "$22,900 for a poll, two days before early voting.",
                       "Cash on hand Oct 14: $1,994,177."]):
    c.text(rx + col_w / 2, top + 208 + i * 31, t, size=13, bold=(i == 4), fill=DARK, anchor="mm")
y = top + col_h + 14

strip_h = 176
c.panel(44, y, c.w - 44, y + strip_h, fill=WHITE, outline=BORDER)
c.text(c.w / 2, y + 32, "THE WHOLE CYCLE, THROUGH OCT 14", size=14, bold=True, fill=NAVY, anchor="mm")
c.text(c.w / 2, y + 68, "$2.30 million in contributions. 53.8% from PACs. At most 17 cents of each dollar from addresses in the district.", size=13, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 98, "Earmarked through AIPAC's PAC: 36 donors, $42,400, none in the district, 4.3% of his individual money. AIPAC PAC: $10,000.", size=13, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 134, "Sent out: $125,000 to the NRCC and $142,000 to 33 other candidates' committees.", size=13.5, bold=True, fill=RED, anchor="mm")
y += strip_h + 14

kick_h = 118
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 38, "All of it is legal and disclosed. The filing does not say what the Nassau County payment was for, and we draw no inference.",
       size=12.5, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 76, "Six district donors. Eighteen through AIPAC's PAC. One TV buy. One check to Long Island.", size=17, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 16
c.text(c.w / 2, y, "Sources: FEC filings 2035999 (pre-general) and nine 48-hour notices, parsed from the raw files  ·  Census ZIP-to-district file  ·  FingerLakes1 Oct 27", size=10.5, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "langworthywatch.org/fact-checks/2026-10-31-pre-election-money-filings/", size=11, fill=MUTED, anchor="mm")
c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "pre_election_money_card.png"), to_desktop=True)
