#!/usr/bin/env python3
"""Social card: his Aug 12 2026 "proud to have delivered" list, all ten items checked.

Supersedes the 4-of-10 version. Every verdict matches a published entry:
  Jasper-Troupsburg   MOSTLY TRUE        2026-06-10-jasper-troupsburg-fema-award
  $7.7M / $5.7M / $3.2M / $3.1M / $1.4M  DOCUMENTED PATTERN  2026-05-20-federal-grants (inst. 1-3, 5-6)
  Newstead / Chautauqua  MISSING CONTEXT  own entries
  Allegany            DOCUMENTED PATTERN  2026-07-16-allegany-water-third-announcement
  Elmira College      ACCURATE (claim-level)  2026-02-11-fy2026-appropriations-credit
Light house style, 1080x1080, no em dashes (enforced by Card.save).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, BRONZE, MUTED, BORDER, WHITE, LIGHTGRAY)

ROWS = [
    ("$60.5M", "Jasper-Troupsburg School Campus", "MOSTLY TRUE", GREEN),
    ("$7.7M",  "Early Childhood + Behavioral Health (HHS award)", "DOCUMENTED PATTERN", RED),
    ("$5.7M",  "Jamestown Airport (FAA formula grant)", "DOCUMENTED PATTERN", RED),
    ("$5M",    "Newstead Community Center (senators too, same day)", "MISSING CONTEXT", BRONZE),
    ("$3.2M",  "Pomfret water (agency grant)", "DOCUMENTED PATTERN", RED),
    ("$3.1M",  "Southern Tier airports (FAA formula grant)", "DOCUMENTED PATTERN", RED),
    ("$1.4M",  "Schuyler Head Start (HHS award to the grantee)", "DOCUMENTED PATTERN", RED),
    ("$1.25M", "Allegany water (joint request, 3rd announcement)", "DOCUMENTED PATTERN", RED),
    ("$1M",    "Chautauqua Mental Hygiene (county won by applying)", "MISSING CONTEXT", BRONZE),
    ("$480K",  "Elmira College (his own solo earmark)", "ACCURATE", GREEN),
]

c = Card(scale=2)
c.brand_bar()

y = c.badge(56, "10 OF 10 CHECKED")
y = c.title(y, 'He Listed 10 Things He "Delivered." We Checked All 10.', size=28)
y = c.divider(y + 8)

# ---- hero ---------------------------------------------------------------
hero_h = 92
c.panel(44, y + 2, c.w - 44, y + 2 + hero_h, fill="#EDF2F7", outline=BORDER)
c.text(134, y + 2 + hero_h / 2, "6 of 10", size=42, impact=True, fill=NAVY, anchor="mm")
c.text(240, y + 30, "are agency grants that no member of Congress directs.", size=17, bold=True, fill=DARK, anchor="lm")
c.text(240, y + 56, "Two held up clean, and we say so. Every verdict below is as published.", size=14, fill=MUTED, anchor="lm")
y = y + 2 + hero_h + 10

# ---- ten rows -----------------------------------------------------------
row_h, gap = 53, 4
for i, (amt, item, verdict, col) in enumerate(ROWS):
    ry = y + i * (row_h + gap)
    fill = WHITE if i % 2 == 0 else "#F7FAFC"
    c.panel(44, ry, c.w - 44, ry + row_h, fill=fill, outline=BORDER, width=1, radius=6)
    c.text(66, ry + row_h / 2, amt, size=19, impact=True, fill=NAVY, anchor="lm")
    c.text(158, ry + row_h / 2, item, size=15, fill=DARK, anchor="lm")
    c.text(c.w - 66, ry + row_h / 2, verdict, size=15, bold=True, fill=col, anchor="rm")
y = y + len(ROWS) * (row_h + gap) + 8

# ---- kicker -------------------------------------------------------------
kick_h = 88
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 28, 'His framing is fair: "once the pie is set in stone," bring money home. Not disputed.',
       size=15, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 60, "The question is who awarded it, who applied, and who else secured it.", size=17, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 14

c.text(c.w / 2, y, "Source: his Aug. 12, 2026 post  ·  six published fact-checks, langworthywatch.org", size=13, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "delivered_list_card.png"), to_desktop=True)
