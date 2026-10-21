#!/usr/bin/env python3
"""Social card: seven 2026 credit claims, each with its own entry's verdict, beside what the record shows.

Anchored to content/fact-checks/2026-10-20-credit-claims-2026-roundup.md (verdict: DOCUMENTED PATTERN). Each row's
verdict must match its own entry. Scorecard layout: his words (red) | the record (navy) | verdict chip (gold).
Fair reading on the card. 1080x1080, no em dashes (enforced).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GOLD, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(58, "DOCUMENTED PATTERN")
y = c.title(y, '"I Secured." "Proud to Deliver."', size=30)
y = c.title(y + 4, "Seven Credit Claims He Made in 2026, and What the Record Shows.", size=20, fill=DARK)
y = c.divider(y + 12)

rows = [
    ('"he has secured $5,000,000"', "Newstead center, Feb", "Two senators secured the same $5M. Not mentioned.", "MISSING CONTEXT"),
    ('"proud to deliver $300,000"', "Hospital X-ray labs, June", "FY2027 requests. Not in any bill that is law.", "MISLEADING"),
    ('"I secured $1 million"', "Olean police, July", "Passed the House. Senate hasn't acted.", "DOCUMENTED PATTERN"),
    ('"SECURED $1,250,000"', "Allegany water, July", "Announced at least 3 times. Senators left out.", "DOCUMENTED PATTERN"),
    ('"My Dairy Farm Resiliency Act strengthened"', "Dairy safety net, Oct", "His bill got no vote. The change came from another bill.", "MISLEADING"),
    ('"proud to secure $1.4 million"', "Chemung sewers, Oct", "An ARC grant. The county applied; ARC decided.", "MISSING CONTEXT"),
    ('"we took swift and decisive action"', "Medicaid fraud, Oct", "CMS, HHS's inspector general and states acted.", "MISLEADING"),
]
row_h = 74
box_top = y + 2
box_h = 34 + row_h * len(rows)
c.panel(44, box_top, c.w - 44, box_top + box_h, fill=WHITE, outline=BORDER)
c.text(66, box_top + 18, "WHAT HE SAID", size=12.5, bold=True, fill=RED, anchor="lm")
c.text(540, box_top + 18, "WHAT THE RECORD SHOWS", size=12.5, bold=True, fill=NAVY, anchor="lm")
c.text(c.w - 66, box_top + 18, "VERDICT", size=12.5, bold=True, fill="#744210", anchor="rm")
for i, (quote, what, record, verdict) in enumerate(rows):
    ry = box_top + 34 + i * row_h
    if i:
        c.rect(60, ry, c.w - 60, ry + 1, fill=BORDER)
    c.text(66, ry + 25, quote, size=14.5, bold=True, fill=RED, anchor="lm")
    c.text(66, ry + 49, what, size=12.5, fill=MUTED, anchor="lm")
    c.text(540, ry + 37, record, size=13, fill=DARK, anchor="lm")
    tw = 150 if verdict != "DOCUMENTED PATTERN" else 168
    c.rect(c.w - 66 - tw, ry + 25, c.w - 66, ry + 49, fill="#FFFBEB", outline=GOLD, radius=4, width=1)
    c.text(c.w - 66 - tw / 2, ry + 37, verdict, size=10.5, bold=True, fill="#744210", anchor="mm")
y = box_top + box_h + 12

# ---- fair reading ---------------------------------------------------------------------------
fr_h = 96
c.panel(44, y, c.w - 44, y + fr_h, fill="#FFFBEB", outline=GOLD)
c.text(c.w / 2, y + 22, "THE FAIR READING", size=14, bold=True, fill="#744210", anchor="mm")
for i, ln in enumerate(["Most of the money and actions are real, and four claims came from earmark requests his office made.",
                        "Requesting earmarks is real work. Senators sometimes leave him out, too. Each claim has its own entry."]):
    c.text(c.w / 2, y + 50 + i * 22, ln, size=13.5, fill=DARK, anchor="mm")
y += fr_h + 12

# ---- kicker ---------------------------------------------------------------------------------
kick_h = 84
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 27, "Not yet law. Also secured by others. Decided by an agency. Someone else's bill.", size=13.5, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 57, "The news is real. The credit is the part to check.", size=19, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 10

c.text(c.w / 2, y, "Verdicts are from each claim's own LangworthyWatch entry: 3 Misleading, 2 Missing Context, 2 Documented Pattern",
       size=10.5, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "Full roundup at langworthywatch.org", size=11, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "credit_claims_roundup_card.png"), to_desktop=True)
