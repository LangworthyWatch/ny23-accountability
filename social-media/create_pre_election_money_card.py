#!/usr/bin/env python3
"""Pre-election money filings, entry 2026-10-31-pre-election-money-filings (DOCUMENTED PATTERN). v2: composition frame.
Every figure is parsed from Langworthy for Congress's own FEC filings (pre-general 2035999; 48-hour notices Oct 16-30).
Composition of $53,220.25 raised Oct 1-14: PACs 26,000 (48.9%); AIPAC-earmarked individuals 16,600 (31.2%);
district-ZIP individuals 6,850 (12.9%); everyone else 3,770.25 (7.1%: other NY individuals 1,500, RJC/WinRed-earmarked 750,
unitemized 520.25, party 1,000)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()
y = c.badge(58, "DOCUMENTED PATTERN  ·  OCT 31, 2026")
y = c.title(y, "In the Two Weeks Before Early Voting,", size=29)
y = c.title(y - 2, "13 Cents of Every Dollar Came From the District.", size=29)
y = c.subtitle(y + 6, "Langworthy for Congress, FEC pre-general report, October 1-14, 2026. Parsed from the raw filing.", size=14.5)
y = c.divider(y + 12)

col_w = (c.w - 44 * 2 - 16) // 2
col_h = 400
lx, rx = 44, 44 + col_w + 16
top = y + 2

# LEFT: composition
c.panel(lx, top, lx + col_w, top + col_h, fill="#F0FFF4", outline="#9AE6B4")
c.text(lx + col_w / 2, top + 30, "WHO PAID FOR THE LAST TWO WEEKS", size=16, bold=True, fill=GREEN, anchor="mm")
c.text(lx + col_w / 2, top + 96, "13¢", size=60, impact=True, fill=GREEN, anchor="mm")
c.text(lx + col_w / 2, top + 142, "of every dollar came from the district", size=14, bold=True, fill=DARK, anchor="mm")
c.text(lx + col_w / 2, top + 164, "$6,850 of the $53,220 raised, from six contributions", size=13, fill=MUTED, anchor="mm")
# stacked bar
segs = [("PACs", 0.489, NAVY), ("Through AIPAC's PAC", 0.312, "#B7791F"), ("District", 0.129, GREEN), ("Other", 0.070, "#A0AEC0")]
bx0, bx1, by0, by1 = lx + 28, lx + col_w - 28, top + 192, top + 226
x = bx0
for name, frac, col in segs:
    w = (bx1 - bx0) * frac
    c.rect(x, by0, x + w, by1, fill=col, outline=None)
    x += w
c.rect(bx0, by0, bx1, by1, fill=None, outline=WHITE, width=1)
legend = [("PACs: $26,000, 49%", NAVY, "SpaceX, UPS, the CPAs' association, BASF, AbbVie, NRA Victory Fund"),
          ("Earmarked through AIPAC's PAC: $16,600, 31%", "#B7791F", "18 donors, Westchester and New York City"),
          ("District addresses: $6,850, 13%", GREEN, "Williamsville, Ellicottville, Silver Creek, Waverly"),
          ("Everyone else: $3,770, 7%", "#718096", "other New York donors, small gifts, party")]
ly = top + 252
for i, (lab, col, sub) in enumerate(legend):
    c.rect(lx + 28, ly - 6, lx + 40, ly + 6, fill=col, outline=None)
    c.text(lx + 50, ly, lab, size=12.5, bold=True, fill=DARK, anchor="lm")
    c.text(lx + 50, ly + 16, sub, size=11, fill=MUTED, anchor="lm")
    ly += 36

# RIGHT: where it went
c.panel(rx, top, rx + col_w, top + col_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(rx + col_w / 2, top + 30, "WHERE IT WENT", size=16, bold=True, fill=RED, anchor="mm")
c.text(rx + col_w / 2, top + 96, "$25,000", size=60, impact=True, fill=RED, anchor="mm")
c.text(rx + col_w / 2, top + 142, "to the Nassau County Republican Committee", size=14, bold=True, fill=DARK, anchor="mm")
c.text(rx + col_w / 2, top + 164, "Long Island, October 9. Largest county-party payment of his cycle.", size=12.5, fill=MUTED, anchor="mm")
for i, t in enumerate(["His home county's committee, Erie, got $11,500 in two years.",
                       "The filing says only \"political contribution.\"",
                       "",
                       "Also: a $551,000 TV buy, his first of the cycle,",
                       "and a $22,900 poll two days before early voting.",
                       "Spent $597,785. Cash on hand: $1,994,177."]):
    if t: c.text(rx + col_w / 2, top + 204 + i * 30, t, size=13, bold=(i == 5), fill=DARK, anchor="mm")
y = top + col_h + 14

strip_h = 170
c.panel(44, y, c.w - 44, y + strip_h, fill=WHITE, outline=BORDER)
c.text(c.w / 2, y + 32, "THE REST OF THE RECORD", size=14, bold=True, fill=NAVY, anchor="mm")
c.text(c.w / 2, y + 66, "Oct 15-29, 48-hour notices: $79,500 more. $42,000 from PACs and firms, $5,500 from three lobbyists, $6,000 from three district donors.", size=12.5, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 96, "Whole cycle: $2.30 million, 53.8% from PACs, at most 17 cents per dollar from the district. $267,000 sent to the NRCC and 33 other campaigns.", size=12.5, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 130, "Through AIPAC's PAC this cycle: 36 donors, $42,400, none in the district, 4.3% of his individual money. The PAC itself: $10,000, the maximum.", size=12.5, bold=True, fill=DARK, anchor="mm")
y += strip_h + 14

kick_h = 112
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 36, "All of it is legal and disclosed. The filing does not say what the Nassau County payment was for, and we draw no inference.",
       size=12.5, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 72, "Half from PACs. A third through one conduit. An eighth from the people he represents.", size=17, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 16
c.text(c.w / 2, y, "Sources: FEC filing 2035999 (pre-general) and nine 48-hour notices, parsed from the raw files  ·  Census ZIP-to-district file  ·  FingerLakes1 Oct 27", size=10.5, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "langworthywatch.org/fact-checks/2026-10-31-pre-election-money-filings/", size=11, fill=MUTED, anchor="mm")
c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "pre_election_money_card.png"), to_desktop=True)
