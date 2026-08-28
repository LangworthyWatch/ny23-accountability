#!/usr/bin/env python3
"""Social card: the donor / bill map.

A roundup chart. Every row is either already published on the site with its own
sourced entry, or comes from the FEC bulk-file pull documented in
research/sources/ (itpas2 + cm, 2022/2024/2026 cycles, memo entries and refunds
excluded).

Deliberate design choice: no causal claim, and the fair reading is on the card
itself, not buried. Members sponsor bills for industries in their district and
those industries give to members who already agree with them. The card shows the
money and the dates and lets the reader judge.

Figures match the published entries exactly (Seneca $10,100 per the 2026-03-14
entry; ACC $95,900 per the 2026-08-26 entry).
Light house style, 1080x1080, no em dashes (enforced by Card.save).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY, GOLD)

c = Card(scale=2)
c.brand_bar()

y = c.badge(56, "DOCUMENTED PATTERN")
y = c.title(y, 'Four Bills He Sponsored. Four Industries That Fund Him.', size=30)
y = c.subtitle(y + 6, 'The money and the dates, from FEC filings. No claim that one caused the other.', size=15)
y = c.divider(y + 10)

ROWS = [
    ("Energy Choice Act",
     "H.R. 3699, introduced June 2025",
     "$107,263",
     "from gas, propane, fuels and utility PACs across three cycles. The fuels institute",
     "that says it helped draft it gave $9,263, all of it after the bill was introduced."),
    ("Recycled Materials Attribution Act",
     "H.R. 7502, introduced Feb 2026",
     "$95,900",
     "spent by the American Chemistry Council on ads supporting him, Aug 2026.",
     "Its lobbying filings named the bill by title while it was still unintroduced."),
    ("Safer Skies Act",
     "H.R. 2353, introduced March 2025",
     "$113,500",
     "from pilots' unions, air traffic controllers and aviation labor PACs,",
     "his largest single source of union money."),
    ("Seneca Nation Law Enforcement Act",
     "H.R. 7065, introduced Jan 2026",
     "$10,100",
     "from the Seneca Nation of Indians in the two years before introduction.",
     "The bill removes state civil as well as criminal jurisdiction."),
]

row_h = 122
for i, (bill, sub, amt, l1, l2) in enumerate(ROWS):
    top = y + i * (row_h + 10)
    c.panel(44, top, c.w - 44, top + row_h, fill="#FFFFFF" if i % 2 == 0 else "#F7FAFC", outline=BORDER)
    c.text(64, top + 30, bill, size=17, bold=True, fill=NAVY, anchor="lm")
    c.text(64, top + 54, sub, size=12, fill=MUTED, anchor="lm")
    c.text(64, top + 86, l1, size=12, fill=DARK, anchor="lm")
    c.text(64, top + 105, l2, size=12, fill=DARK, anchor="lm")
    c.text(c.w - 70, top + 52, amt, size=34, impact=True, fill=RED, anchor="rm")
y = y + len(ROWS) * (row_h + 10) + 8

# ---- the fair reading, on the card ---------------------------------------
fr_h = 104
c.panel(44, y, c.w - 44, y + fr_h, fill="#EBF8F0", outline="#9AE6B4")
c.text(c.w / 2, y + 24, "THE FAIR READING, BECAUSE IT BELONGS HERE", size=14, bold=True, fill=GREEN, anchor="mm")
c.text(c.w / 2, y + 48, "This pattern is normal. Members sponsor bills for industries in their districts, and those", size=13, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 68, "industries give to members who already agree with them. Nothing here shows a payment for a", size=13, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 88, "vote, and none is alleged. Two of the four rows are union money.", size=13, fill=DARK, anchor="mm")
y += fr_h + 12

# ---- kicker -------------------------------------------------------------
kick_h = 86
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 26, "Disclosure is the point. His press releases announcing these bills name the policy.",
       size=14, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 58, "They do not name the donors.", size=18, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 14

c.text(c.w / 2, y, "Sources: FEC bulk files itpas2 and cm, 2022 to 2026, memo entries and refunds excluded  ·  FEC Form 5 filing 2009256", size=11, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "govinfo BILLSTATUS, 119th Congress  ·  Senate LDA filings  ·  Full sourcing on each entry at langworthywatch.org", size=11, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "donor_bill_map_card.png"), to_desktop=True)
