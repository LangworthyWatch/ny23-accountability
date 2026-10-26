#!/usr/bin/env python3
"""Social card: the Post-Journal endorsement graphic vs. the paragraphs it cut, and the shared-credit earmarks.
Anchored to content/fact-checks/2026-10-26-post-journal-endorsement-graphic.md (MISSING CONTEXT)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()
y = c.badge(58, "MISSING CONTEXT")
y = c.title(y, "The Paper Endorsed Him. The Graphic Cut the Part", size=28)
y = c.title(y + 2, "Where the Paper Praised His Opponent's Town Halls.", size=28)
y = c.subtitle(y + 6, "Post-Journal and Dunkirk OBSERVER, Oct 24, 2026. Same editorial, same editor, both papers.", size=15)
y = c.divider(y + 12)

col_w = (c.w - 44 * 2 - 16) // 2
col_h = 400
lx, rx = 44, 44 + col_w + 16
top = y + 2
c.panel(lx, top, lx + col_w, top + col_h, fill="#EBF8F0", outline="#9AE6B4")
c.text(lx + col_w / 2, top + 30, "WHAT THE GRAPHIC QUOTES", size=16, bold=True, fill=GREEN, anchor="mm")
for i, (t, b) in enumerate([
        ('"Langworthy has been a supporter of', False), ("the region's treasured natural", False), ('resources. He secured federal funding', False),
        ("for a comprehensive study by the U.S.", False), ('Army Corps of Engineers on Chautauqua', False), ('Lake ... With Lake Erie, his work has', False),
        ("improved the Barcelona Harbor with", False), ('dredging projects ... He gets our', False), ('endorsement."', False)]):
    c.text(lx + col_w / 2, top + 70 + i * 34, t, size=14, bold=b, fill=DARK, anchor="mm")

c.panel(rx, top, rx + col_w, top + col_h, fill="#FFF5F5", outline="#FEB2B2")
c.text(rx + col_w / 2, top + 30, "WHAT THE GRAPHIC CUT", size=16, bold=True, fill=RED, anchor="mm")
for i, (t, b) in enumerate([
        ('"Challenger Aaron Gies is to be', True), ('commended ... He has held numerous', True), ('town hall meetings from Erie to', True),
        ('Tioga County ... the gatherings were', False), ('informative and well attended ...', False), ('greatly appreciated by those seeking', False),
        ('an alternative to the incumbent.', False), ('For his part, U.S. Rep. Nick Langworthy', True), ('has not been as amenable to that process."', True)]):
    c.text(rx + col_w / 2, top + 70 + i * 34, t, size=14, bold=b, fill=DARK, anchor="mm")
y = top + col_h + 14

strip_h = 164
c.panel(44, y, c.w - 44, y + strip_h, fill="#EDF2F7", outline=BORDER)
c.text(c.w / 2, y + 26, "THE MONEY THE QUOTE CREDITS HIM WITH, PER THE APPROPRIATIONS DISCLOSURE TABLES", size=13, bold=True, fill=NAVY, anchor="mm")
rows = [("Chautauqua Lake study, FY2024", "$500,000", "House: Langworthy. Senate: Gillibrand, Schumer. Originated: Senate."),
        ("Barcelona Harbor, FY2024", "$7,500,000", "House: Langworthy. Senate: Gillibrand, Schumer. Originated: Senate."),
        ("Barcelona Harbor, FY2022 (the 2023 dredging)", "$1,150,000", "House: none. Senate: Gillibrand, Schumer. Before he took office.")]
for i, (a, b, d) in enumerate(rows):
    yy = y + 62 + i * 34
    c.text(64, yy, a, size=13, bold=True, fill=DARK, anchor="lm")
    c.text(440, yy, b, size=13, bold=True, fill=RED if i == 2 else NAVY, anchor="lm")
    c.text(560, yy, d, size=12.5, fill=DARK, anchor="lm")
y += strip_h + 14

kick_h = 104
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 34, 'The same editor, May 2025: "Since being elected, he said he was not going to hold town hall events."',
       size=13, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 70, "The endorsement is real. So is the paragraph the graphic left out.", size=18, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 16
c.text(c.w / 2, y, "Sources: Post-Journal and OBSERVER editorials Oct 24, 2026  ·  FY2022 and FY2024 Energy and Water explanatory statements  ·  Corps Buffalo District  ·  Post-Journal May 30, 2025", size=10.5, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "Full entry at langworthywatch.org", size=11, fill=MUTED, anchor="mm")
c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "post_journal_card.png"), to_desktop=True)
