#!/usr/bin/env python3
"""Election Day card, Nov 3, 2026: all 182 published fact-checks as a 14 x 13 dot grid, by finding.
Counts from the verdict: frontmatter of every non-draft entry in content/fact-checks/ (tallied Nov 3, 2026),
normalized to the seven buckets used by closing_5_ledger_post.md. Supporting lines from entries
2026-09-15 (rural health fund), 2026-10-16 (who funds him), 2026-10-15 (tax claims), 2026-07-16 (Rules Committee)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()
y = c.badge(58, "ELECTION DAY  ·  NOV 3, 2026")
y = c.title(y, "182 of His Statements, Checked Against the Record.", size=30)
y = c.title(y - 2, "Eight Held Up.", size=30)
y = c.subtitle(y + 4, "Every post, press release, debate answer and constituent letter this site has checked since July 2025.", size=14)
y = c.divider(y + 10)

buckets = [
    ("Held up as accurate", 8, "#2F855A"),
    ("Left out context that changed the meaning", 64, "#2C5282"),
    ("Misleading", 40, "#C05621"),
    ("Part of a documented pattern", 35, "#975A16"),
    ("Contradicted his own votes", 13, "#9B2C2C"),
    ("False, or blamed the wrong cause", 13, "#E53E3E"),
    ("Dodged the question, or mixed", 9, "#718096"),
]
assert sum(n for _, n, _ in buckets) == 182

# dot grid, 14 columns x 13 rows = 182
cols, rows = 14, 13
pitch, dot = 34, 26
gx, gy = 48, y + 30
seq = []
for _, n, col in buckets:
    seq += [col] * n
for i, col in enumerate(seq):
    r, q = divmod(i, cols)
    x0 = gx + q * pitch
    y0 = gy + r * pitch
    c.d.ellipse([c._p(x0), c._p(y0), c._p(x0 + dot), c._p(y0 + dot)], fill=col)
grid_bottom = gy + rows * pitch
# bracket under the eight green dots
c.rect(gx, gy - 6, gx + 8 * pitch - (pitch - dot), gy - 4, fill="#2F855A", outline=None)
c.text(gx + 8 * pitch - (pitch - dot) + 10, gy - 7, "these eight", size=12, bold=True, fill="#2F855A", anchor="lm")

# legend
lx = gx + cols * pitch + 40
ly = gy - 14
c.text(lx, ly, "182 FACT-CHECKS", size=15, bold=True, fill=NAVY, anchor="lm")
ly += 40
for label, n, col in buckets:
    c.rect(lx, ly - 11, lx + 22, ly + 11, fill=col, outline=None, radius=4)
    c.text(lx + 34, ly, label, size=14, bold=(n == 8), fill=DARK, anchor="lm")
    c.text(c.w - 48, ly, str(n), size=17, bold=True, fill=col, anchor="rm")
    ly += 46
c.text(lx, grid_bottom - 28, "One dot per published entry.", size=12, fill=MUTED, anchor="lm")
c.text(lx, grid_bottom - 10, "Each entry links and archives its sources.", size=12, fill=MUTED, anchor="lm")
y = grid_bottom + 6

# what the record shows
strip_h = 186
c.panel(44, y, c.w - 44, y + strip_h, fill=WHITE, outline=BORDER)
c.text(c.w / 2, y + 24, "FOUR THINGS THE RECORD SHOWS", size=14, bold=True, fill=NAVY, anchor="mm")
lines = [
    "He voted for the law that cut Medicaid by $911 billion, then promoted the $76 million it sent back to New York.",
    "No in-person town hall since he took office in January 2023. 55 cents of every campaign dollar came from PACs.",
    "\"No tax on Social Security,\" told to seniors five times. The law he voted for did not change how Social Security is taxed.",
    "On the Rules Committee, he voted to keep the House from voting on the Epstein files, on tariffs, and on a veterans bill.",
]
yy = y + 54
for ln in lines:
    c.d.ellipse([c._p(66), c._p(yy - 4), c._p(75), c._p(yy + 5)], fill=RED)
    c.text(88, yy, ln, size=12.5, fill=DARK, anchor="lm")
    yy += 34
y += strip_h + 12

kick_h = 86
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 28, "Every entry includes the strongest case for his side. When we were wrong, we said so on the page.", size=13.5, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 58, "Don't take our word for it. Pick one entry and check it yourself.", size=18, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 14
c.text(c.w / 2, y, "langworthywatch.org/fact-checks/", size=13, bold=True, fill=NAVY, anchor="mm")
assert y < 1080 - 50 - 8, y
c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "election_day_card.png"), to_desktop=True)
