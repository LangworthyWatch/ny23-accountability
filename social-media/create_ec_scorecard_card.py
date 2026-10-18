#!/usr/bin/env python3
"""Social card: his Energy and Commerce record vs. the Oct 15 "deliver for NY23 taxpayers" post.

Anchored to content/fact-checks/2026-10-17-energy-commerce-scorecard.md (verdict: MISSING CONTEXT).

Top: the three bills from his post with where each actually stands. Middle: four record tiles, two that favor him
(30% markup rate; ordinary attendance) and two that don't (1 passed House; 0 laws), so the card reads as a scorecard,
not a hit. Parallel facts, so navy/gray, no red/green. 1080x1080, no em dashes (enforced).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, GOLD, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(58, "MISSING CONTEXT")
y = c.title(y, '"Serving on the Energy and Commerce Committee', size=25)
y = c.title(y + 2, 'Means I Can Deliver for NY23 Taxpayers."', size=25)
y = c.title(y + 4, "His Committee Record, by the Numbers.", size=21, fill=DARK)
y = c.subtitle(y + 6, "Oct 15, 2026 post on his official page, checked against govinfo, House Clerk and committee roll calls.", size=14)
y = c.divider(y + 12)

# ---- the three bills ---------------------------------------------------------------
rows = [("POWER Act", '"speeds up pipeline and power plant construction"', "NOT INTRODUCED",
         "A committee chairman's discussion draft. No bill number."),
        ("GRID Power Act", '"prioritizes reliable power plants"', "STALLED IN SENATE",
         "His cosponsorship. Passed the House 216-206 in Sept 2025."),
        ("State Energy Accountability Act", '"exposes the cost of green mandates"', "NO FLOOR VOTE",
         "His bill. Reported by the committee 27-20 in June 2025.")]
row_h = 74
box_h = 38 + row_h * len(rows) + 4
c.panel(44, y, c.w - 44, y + box_h, fill=WHITE, outline=BORDER)
c.text(c.w / 2, y + 21, "THE THREE BILLS IN HIS POST: NONE IS LAW", size=14, bold=True, fill=NAVY, anchor="mm")
for i, (name, desc, status, note) in enumerate(rows):
    ry = y + 40 + i * row_h
    c.text(66, ry + 14, name, size=16, bold=True, fill=DARK, anchor="lm")
    c.text(66, ry + 38, desc + "  " + note, size=13, fill=DARK, anchor="lm")
    c.rect(c.w - 266, ry + 3, c.w - 62, ry + 27, fill="#4A5568", radius=5)
    c.text(c.w - 164, ry + 15, status, size=12.5, bold=True, fill=WHITE, anchor="mm")
y += box_h + 14

# ---- record tiles -----------------------------------------------------------------
c.text(c.w / 2, y + 8, "HIS FULL COMMITTEE RECORD SINCE JANUARY 2025", size=14, bold=True, fill=NAVY, anchor="mm")
y += 22
tiles = [("30%", "of his 20 committee bills", "reached a full markup", "vs 9.9% for GOP bills"),
         ("1", "of his committee bills", "has passed the House", "H.R. 4690, Apr 2026"),
         ("0", "of his 50 bills and", "resolutions became law", "none passed the Senate"),
         ("10%", "of committee votes", "missed (22 of 221)", "GOP median: 11%")]
gap = 12
tw = (c.w - 44 * 2 - gap * 3) / 4
th = 184
for i, (big, l1, l2, l3) in enumerate(tiles):
    x0 = 44 + i * (tw + gap)
    c.panel(x0, y, x0 + tw, y + th, fill="#EDF2F7", outline="#A3BFD9")
    c.text(x0 + tw / 2, y + 56, big, size=54, impact=True, fill=NAVY, anchor="mm")
    c.text(x0 + tw / 2, y + 106, l1, size=13.5, bold=True, fill=DARK, anchor="mm")
    c.text(x0 + tw / 2, y + 126, l2, size=13.5, bold=True, fill=DARK, anchor="mm")
    c.text(x0 + tw / 2, y + 152, l3, size=12.5, fill=MUTED, anchor="mm")
y += th + 14

# ---- fair reading -------------------------------------------------------------------
fr_h = 124
c.panel(44, y, c.w - 44, y + fr_h, fill="#FFFBEB", outline=GOLD)
c.text(c.w / 2, y + 22, "THE FAIR READING", size=14, bold=True, fill="#744210", anchor="mm")
for i, ln in enumerate([
        "He moves bills through committee about three times as often as the typical Republican bill.",
        "His quantum bill passed committee 36-0; two of his bills are co-led with Democrats.",
        "His infrastructure bill and the GRID Power Act passed the House; neither has passed the Senate."]):
    c.text(c.w / 2, y + 52 + i * 25, ln, size=13.5, fill=DARK, anchor="mm")
y += fr_h + 12

# ---- kicker ---------------------------------------------------------------------------
kick_h = 84
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 27, "Productive in committee. Twenty-one months in, nothing he wrote is law.", size=13.5, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 57, "None of the three bills he cited has become law.", size=19, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 12

c.text(c.w / 2, y, "Sources: govinfo BILLSTATUS (Oct 16, 2026)  ·  House Clerk  ·  Energy and Commerce roll-call sheets and vote summaries  ·  E&C POWER Act release, Jul 22, 2026",
       size=10.5, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "Full entry at langworthywatch.org", size=11, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "ec_scorecard_card.png"), to_desktop=True)
