#!/usr/bin/env python3
"""Social card: response to the Oct 19, 2026 "Our Working Families Tax Cuts created a $50 billion Rural Health
Transformation Program" post.

Anchored to content/fact-checks/2026-09-15-rural-health-fund-vs-cuts-and-oversight.md (verdict: MISSING CONTEXT;
Oct 19 update) and content/fact-checks/2026-06-02-rural-health-transformation-212m.md (KFF figures).

Hero: three numbers (37% offset, 64% after the fund ends, 8 at-risk NY-23 hospitals). Then what's true vs. what's left
out, as navy/red. Fair reading on the card. 1080x1080, no em dashes (enforced).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, GOLD, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(58, "MISSING CONTEXT")
y = c.title(y, '"Our Working Families Tax Cuts Created a $50 Billion', size=25)
y = c.title(y + 2, 'Rural Health Transformation Program."', size=25)
y = c.title(y + 4, "The Same Law Cut Rural Medicaid by About $137 Billion.", size=21, fill=DARK)
y = c.subtitle(y + 6, "Oct 19, 2026 post on his official page. Figures from KFF and the Fiscal Policy Institute.", size=14)
y = c.divider(y + 12)

# ---- three numbers -------------------------------------------------------------------
tiles = [("37%", "of the rural Medicaid cut", "the fund offsets", "$50B fund vs. ~$137B cut (KFF)"),
         ("64%", "of the law's Medicaid cuts", "land after fiscal 2030", "when the fund ends (KFF)"),
         ("8", "NY-23 hospitals on an", "at-risk list", "most of any NY district (FPI)")]
gap = 14
tw = (c.w - 44 * 2 - gap * 2) / 3
th = 204
top = y + 2
for i, (big, l1, l2, l3) in enumerate(tiles):
    x0 = 44 + i * (tw + gap)
    c.panel(x0, top, x0 + tw, top + th, fill="#FFF5F5", outline="#FEB2B2")
    c.text(x0 + tw / 2, top + 68, big, size=62, impact=True, fill=RED, anchor="mm")
    c.text(x0 + tw / 2, top + 126, l1, size=14.5, bold=True, fill=DARK, anchor="mm")
    c.text(x0 + tw / 2, top + 150, l2, size=14.5, bold=True, fill=DARK, anchor="mm")
    c.text(x0 + tw / 2, top + 178, l3, size=12.5, fill=MUTED, anchor="mm")
y = top + th + 14

# ---- true vs. left out -------------------------------------------------------------------
col_w = (c.w - 44 * 2 - 16) // 2
col_h = 280
lx, rx = 44, 44 + col_w + 16
c.panel(lx, y, lx + col_w, y + col_h, fill="#EDF2F7", outline="#A3BFD9")
c.text(lx + col_w / 2, y + 26, "WHAT HOLDS UP", size=15, bold=True, fill=NAVY, anchor="mm")
for i, ln in enumerate(["The fund is real: $50 billion", "over five years, through fiscal 2030.", "",
                        "New York's rules give priority", "to maternity care projects.", "",
                        "Nine Sept 4 awards serve NY-23,", "including St. James, Jones Memorial", "and Westfield Memorial hospitals."]):
    c.text(lx + col_w / 2, y + 60 + i * 24, ln, size=14, bold=(i in (0, 3, 6)), fill=DARK, anchor="mm")
c.panel(rx, y, rx + col_w, y + col_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(rx + col_w / 2, y + 26, "WHAT THE POST LEAVES OUT", size=15, bold=True, fill=RED, anchor="mm")
for i, ln in enumerate(["The Senate added the fund \"just prior", "to passage,\" per KFF. He voted for", "the final law.", "",
                        "The same law cut federal Medicaid", "by $911 billion, about $137 billion", "of it in rural areas.", "",
                        "The fund ends in fiscal 2030. Most of", "the Medicaid cuts come after."]):
    c.text(rx + col_w / 2, y + 60 + i * 21.5, ln, size=14, bold=(i in (0, 4, 8)), fill=DARK, anchor="mm")
y += col_h + 12

# ---- fair reading -------------------------------------------------------------------------
fr_h = 92
c.panel(44, y, c.w - 44, y + fr_h, fill="#FFFBEB", outline=GOLD)
c.text(c.w / 2, y + 22, "THE FAIR READING", size=14, bold=True, fill="#744210", anchor="mm")
c.text(c.w / 2, y + 52, "The fund helps rural hospitals, and the money is reaching the district.", size=13.5, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 74, "It replaces about a third of what the same law takes out of rural Medicaid.", size=13.5, fill=DARK, anchor="mm")
y += fr_h + 12

# ---- kicker ---------------------------------------------------------------------------------
kick_h = 88
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 29, "His sixth announcement of this fund since December 2025.", size=13.5, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 60, "A $50 billion fund inside a $911 billion Medicaid cut.", size=19, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 10

c.text(c.w / 2, y, "Sources: KFF (CBO estimates; rural health fund analysis)  ·  Fiscal Policy Institute, June 2025  ·  NYS DOH Rural Community Health Integration guidance and awards",
       size=10.5, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "Full entry at langworthywatch.org", size=11, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "rhtp_50b_response_card.png"), to_desktop=True)
