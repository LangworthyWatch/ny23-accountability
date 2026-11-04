#!/usr/bin/env python3
"""'Massive mandate' vs. the returns, entry 2026-11-04-mandate-claim-election-returns (MISSING CONTEXT).
v2: hero = his three margins (same direction, large); peers demoted to a slim strip in the same direction.
Figures: certified 2022/2024 (Ballotpedia) and Times/AP unofficial 2026 counts, retained under
research/sources/election-results-2026-11-04/."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()
y = c.badge(58, "MISSING CONTEXT  ·  NOV 4, 2026")
y = c.title(y, "\"A Massive Mandate.\"", size=34)
y = c.title(y - 2, "It Was His Smallest Margin in Three Races for This Seat.", size=30)
y = c.subtitle(y + 4, "Campaign page, Nov 4: \"a 20-point victory, a mandate\" and \"a massive mandate and resounding victory.\"", size=13.5)
y = c.divider(y + 10)

# HERO: his margin, three races
h_h = 316
c.panel(44, y, c.w - 44, y + h_h, fill=WHITE, outline=BORDER)
c.text(66, y + 26, "HIS MARGIN OF VICTORY", size=15, bold=True, fill=NAVY, anchor="lm")
rows = [("2022", "midterm", 29.8, NAVY), ("2024", "presidential year", 31.6, NAVY), ("2026", "midterm, unofficial", 20.6, RED)]
x0 = 250; xmax = c.w - 190; unit = (xmax - x0) / 32.0
ry = y + 80
for yr, lab, v, col in rows:
    c.text(66, ry - 10, yr, size=22, bold=True, fill=col, anchor="lm")
    c.text(66, ry + 14, lab, size=12, fill=MUTED, anchor="lm")
    c.rect(x0, ry - 24, x0 + v * unit, ry + 24, fill=col, outline=None, radius=4)
    c.text(x0 + v * unit + 14, ry, f"+{v:.1f}", size=30, impact=True, fill=col, anchor="lm")
    ry += 72
c.rect(66, y + h_h - 56, c.w - 66, y + h_h - 55, fill=BORDER, outline=None)
c.text(66, y + h_h - 36, "Same number of voters as 2022, about 300,000. He got roughly 10,900 fewer votes;", size=13, bold=True, fill=DARK, anchor="lm")
c.text(66, y + h_h - 16, "the Democratic candidate got 15,600 more.", size=13, bold=True, fill=DARK, anchor="lm")
y += h_h + 12

# STRIP: every NY Republican incumbent, drop in share, same direction (bars grow right = bigger drop)
s_h = 254
c.panel(44, y, c.w - 44, y + s_h, fill="#EDF2F7", outline=BORDER)
c.text(66, y + 24, "THE SAME NIGHT, EVERY REPUBLICAN INCUMBENT FROM NEW YORK LOST VOTE SHARE", size=13.5, bold=True, fill=NAVY, anchor="lm")
c.text(66, y + 44, "Points lost, 2024 to 2026. His drop is in the middle. This is the environment, not something about him.", size=12, fill=MUTED, anchor="lm")
peers = [("Garbarino", 8.1), ("Malliotakis", 7.7), ("Langworthy", 5.5), ("Tenney", 5.2), ("Lawler", 4.3), ("LaLota", 4.1)]
px0 = 250; punit = (c.w - 190 - px0) / 9.0
ry = y + 76
for lab, v in peers:
    him = lab == "Langworthy"
    col = RED if him else "#4A5568"
    c.text(66, ry, lab, size=13.5, bold=him, fill=col if him else DARK, anchor="lm")
    c.rect(px0, ry - 11, px0 + v * punit, ry + 11, fill=col, outline=None, radius=3)
    c.text(px0 + v * punit + 10, ry, f"-{v:.1f}", size=14, bold=True, fill=col, anchor="lm")
    ry += 30
y += s_h + 12

# Fair-case strip
f_h = 78
c.panel(44, y, c.w - 44, y + f_h, fill="#F0FFF4", outline="#9AE6B4")
c.text(c.w / 2, y + 22, "WHAT CUTS HIS WAY", size=13, bold=True, fill=GREEN, anchor="mm")
c.text(c.w / 2, y + 44, "Twenty points is a decisive win and he carried all nine counties. Midterms run against the president's party.", size=12.5, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 62, "His 2024 opponent raised $32,743 for the whole cycle; this year's Democratic candidate raised $678,484 through Oct. 14.", size=12.5, fill=DARK, anchor="mm")
y += f_h + 12

k_h = 84
c.panel(44, y, c.w - 44, y + k_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 28, "\"A 20-point victory\": TRUE.   \"A massive mandate and resounding victory\": MISSING CONTEXT.", size=14, bold=True, fill=WHITE, anchor="mm")
c.text(c.w / 2, y + 58, "2026 counts are the AP's as of Nov. 4 afternoon, unofficial until certified in December. Every figure is sourced on the entry.", size=11.5, fill=LIGHTGRAY, anchor="mm")
y += k_h + 12
c.text(c.w / 2, y, "langworthywatch.org/fact-checks/2026-11-04-mandate-claim-election-returns/", size=11.5, bold=True, fill=NAVY, anchor="mm")
assert y < 1080 - 50 - 6, y
c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "mandate_card.png"), to_desktop=True)
