#!/usr/bin/env python3
"""Social card: no in-person town hall since 2023, and where his campaign dollars come from.

Anchored to content/fact-checks/2026-10-16-who-funds-him-and-who-can-reach-him.md (verdict: DOCUMENTED PATTERN).

Three hero numbers (0 town halls, 55 cents PACs, 9-17 cents NY-23 donors), then one stacked bar splitting a campaign
dollar by source (precedent: shared_earmarks split bar). Parallel facts, not claim vs. reality, so no red/green: PACs
navy, NY-23 donors gold, other sources muted. Fair reading on the card. 1080x1080, no em dashes (enforced).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, GOLD, MUTED, BORDER, WHITE, LIGHTGRAY, LIGHT)

c = Card(scale=2)
c.brand_bar()

y = c.badge(58, "DOCUMENTED PATTERN")
y = c.title(y, "No In-Person Town Hall Since 2023.", size=28)
y = c.title(y + 2, "Where His Campaign Dollars Come From.", size=28)
y = c.subtitle(y + 6, "Langworthy for Congress, FEC filings, Jan 2025 to Sep 2026: $2.2 million in contributions.", size=15)
y = c.divider(y + 12)

# ---- three hero tiles ---------------------------------------------------------------
tiles = [("0", "in-person public town halls", "since he took office, Jan 2023", NAVY),
         ("55¢", "of every campaign dollar", "came from PACs", NAVY),
         ("9-17¢", "from donors in NY-23:", "about 9¢ by address, at most 17¢", "#975A16")]
gap = 14
tw = (c.w - 44 * 2 - gap * 2) / 3
th = 186
top = y + 2
for i, (big, l1, l2, col) in enumerate(tiles):
    x0 = 44 + i * (tw + gap)
    c.panel(x0, top, x0 + tw, top + th, fill="#EDF2F7" if col == NAVY else "#FFFBEB",
            outline="#A3BFD9" if col == NAVY else GOLD)
    c.text(x0 + tw / 2, top + 72, big, size=60, impact=True, fill=col, anchor="mm")
    c.text(x0 + tw / 2, top + 130, l1, size=14.5, bold=True, fill=DARK, anchor="mm")
    c.text(x0 + tw / 2, top + 154, l2, size=14, fill=DARK, anchor="mm")
y = top + th + 14

# ---- stacked dollar bar ----------------------------------------------------------------
segs = [("PACs and political committees", 54.6, NAVY, WHITE),
        ("Donors in ZIPs entirely in NY-23", 8.9, "#975A16", WHITE),
        ("Donors in ZIPs split with NY-23", 5.4, GOLD, DARK),
        ("Donors elsewhere in New York", 16.0, "#718096", WHITE),
        ("Donors outside New York", 11.8, "#A0AEC0", DARK),
        ("Unitemized gifts (no address)", 3.1, "#CBD5E0", DARK)]
box_h = 288
c.panel(44, y, c.w - 44, y + box_h, fill=WHITE, outline=BORDER)
c.text(c.w / 2, y + 24, "ONE CAMPAIGN DOLLAR, BY SOURCE", size=14, bold=True, fill=NAVY, anchor="mm")
bx0, bx1, by0, by1 = 70, c.w - 70, y + 50, y + 108
total = sum(s[1] for s in segs)
x = bx0
for name, pct, col, tcol in segs:
    w = (bx1 - bx0) * pct / total
    c.rect(x, by0, x + w, by1, fill=col)
    if w > 60:
        c.text(x + w / 2, (by0 + by1) / 2, f"{pct:.0f}¢" if pct >= 1 else "", size=16, bold=True, fill=tcol, anchor="mm")
    x += w
# legend, two columns
for i, (name, pct, col, _) in enumerate(segs):
    lx = 80 + (i % 2) * 480
    ly = y + 138 + (i // 2) * 32
    c.rect(lx, ly - 9, lx + 18, ly + 9, fill=col, radius=3)
    c.text(lx + 28, ly, f"{name}: {pct:.1f}%", size=14, fill=DARK, anchor="lm")
c.text(c.w / 2, y + 242, "Party committees 0.3%, unmatched ZIPs 1.0% (shown with elsewhere in NY). At most 17 cents can be from the district.",
       size=12, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 266, "Lobbyists and government-affairs donors gave $70,850; 84% of it came from Virginia and D.C.",
       size=13.5, bold=True, fill=DARK, anchor="mm")
y += box_h + 12

# ---- fair reading ------------------------------------------------------------------------
fr_h = 122
c.panel(44, y, c.w - 44, y + fr_h, fill="#FFFBEB", outline=GOLD)
c.text(c.w / 2, y + 22, "THE FAIR READING", size=14, bold=True, fill="#744210", anchor="mm")
for i, ln in enumerate([
        "His PAC share ranks 7th of 26 New York House members; four Democrats and two Republicans are higher.",
        "Buffalo donors count as outside NY-23. He holds monthly telephone town halls and cites other channels.",
        "These records show who funds his campaign. They do not show who influences his decisions."]):
    c.text(c.w / 2, y + 52 + i * 24, ln, size=13.5, bold=(i == 2), fill=DARK, anchor="mm")
y += fr_h + 12

# ---- kicker --------------------------------------------------------------------------------
kick_h = 88
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 29, 'He says telephone town halls reach "all the constituents of NY-23."', size=13, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 60, "Voters can weigh both: how they can reach him, and who pays for his campaigns.", size=17, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 10

c.text(c.w / 2, y, "Sources: Langworthy for Congress FEC reports, 2025-26  ·  Census ZIP-to-district file (119th Congress)  ·  FEC candidate summary file  ·  WSKG, Apr 18, 2025",
       size=10.5, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "Full entry at langworthywatch.org", size=11, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "funding_access_card.png"), to_desktop=True)
