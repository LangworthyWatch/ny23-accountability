#!/usr/bin/env python3
"""'Massive mandate' vs. the returns, entry 2026-11-04-mandate-claim-election-returns (MISSING CONTEXT).
Figures: certified 2022/2024 (Ballotpedia) and Times/AP unofficial 2026 counts, retained under
research/sources/election-results-2026-11-04/."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()
y = c.badge(58, "MISSING CONTEXT  ·  NOV 4, 2026")
y = c.title(y, "He Called It 'a Massive Mandate.' It Was His Smallest", size=28)
y = c.title(y - 2, "Margin in Three Races, and Every N.Y. Republican Fell With Him.", size=28)
y = c.subtitle(y + 4, "Campaign page, Nov 4: \"a 20-point victory, a mandate\" and \"a massive mandate and resounding victory.\"", size=13.5)
y = c.divider(y + 10)

# Panel 1: his margin, three races
p1_h = 190
c.panel(44, y, c.w - 44, y + p1_h, fill=WHITE, outline=BORDER)
c.text(66, y + 24, "HIS MARGIN OF VICTORY, THREE RACES FOR THIS SEAT", size=14, bold=True, fill=NAVY, anchor="lm")
rows = [("2022 midterm", 29.8, NAVY), ("2024 presidential year", 31.6, NAVY), ("2026 midterm (unofficial)", 20.6, RED)]
x0 = 300; xmax = c.w - 150; unit = (xmax - x0) / 32.0
ry = y + 60
for lab, v, col in rows:
    c.text(66, ry, lab, size=13.5, bold=(col == RED), fill=DARK, anchor="lm")
    c.rect(x0, ry - 13, x0 + v * unit, ry + 13, fill=col, outline=None, radius=3)
    c.text(x0 + v * unit + 12, ry, f"+{v:.1f} pts", size=16, bold=True, fill=col, anchor="lm")
    ry += 44
c.text(66, y + p1_h - 20, "Same-size electorate as 2022: about 10,900 fewer votes for him, 15,600 more for the Democratic candidate.", size=11.5, fill=MUTED, anchor="lm")
y += p1_h + 14

# Panel 2: every NY Republican incumbent, change in share 2024 -> 2026
p2_h = 356
c.panel(44, y, c.w - 44, y + p2_h, fill=WHITE, outline=BORDER)
c.text(66, y + 24, "CHANGE IN VOTE SHARE, 2024 TO 2026, EVERY REPUBLICAN INCUMBENT FROM NEW YORK", size=14, bold=True, fill=NAVY, anchor="lm")
peers = [("Garbarino, NY-2", -8.1), ("Malliotakis, NY-11", -7.7), ("Langworthy, NY-23", -5.5), ("Tenney, NY-24", -5.2),
         ("Lawler, NY-17", -4.3), ("LaLota, NY-1", -4.1)]
zero = c.w - 150; unit2 = (zero - 300) / 9.0
ry = y + 62
for lab, v in peers:
    him = "Langworthy" in lab
    col = RED if him else NAVY
    c.text(66, ry, lab, size=13.5, bold=him, fill=col if him else DARK, anchor="lm")
    c.rect(zero + v * unit2, ry - 13, zero, ry + 13, fill=col, outline=None, radius=3)
    c.text(zero + v * unit2 - 12, ry, f"{v:.1f} pts", size=15, bold=True, fill=col, anchor="rm")
    ry += 42
c.rect(zero, y + 46, zero + 2, ry - 24, fill=BORDER, outline=None)
c.text(zero + 10, y + 46, "2024 share", size=10.5, fill=MUTED, anchor="lt")
c.text(66, y + p2_h - 20, "All six lost 4 to 8 points. His drop is in the middle. The district itself moved 0.6 pts toward Democrats vs. its 2024 presidential vote.", size=11.5, fill=MUTED, anchor="lm")
y += p2_h + 14

# Fair-case strip
s_h = 78
c.panel(44, y, c.w - 44, y + s_h, fill="#F0FFF4", outline="#9AE6B4")
c.text(c.w / 2, y + 22, "WHAT CUTS HIS WAY", size=13, bold=True, fill=GREEN, anchor="mm")
c.text(c.w / 2, y + 44, "Twenty points is a decisive win and he carried all nine counties. Midterms run against the president's party.", size=12.5, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 62, "His 2024 opponent raised $32,743 for the whole cycle; this year's Democratic candidate raised $678,484 through Oct. 14.", size=12.5, fill=DARK, anchor="mm")
y += s_h + 12

k_h = 84
c.panel(44, y, c.w - 44, y + k_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 28, "\"A 20-point victory\": TRUE.   \"A massive mandate and resounding victory\": MISSING CONTEXT.", size=14, bold=True, fill=WHITE, anchor="mm")
c.text(c.w / 2, y + 58, "2026 counts are the AP's as of Nov. 4 afternoon and are unofficial until certified in December. Every figure is sourced on the entry.", size=11.5, fill=LIGHTGRAY, anchor="mm")
y += k_h + 12
c.text(c.w / 2, y, "langworthywatch.org/fact-checks/2026-11-04-mandate-claim-election-returns/", size=11.5, bold=True, fill=NAVY, anchor="mm")
assert y < 1080 - 50 - 6, y
c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "mandate_card.png"), to_desktop=True)
