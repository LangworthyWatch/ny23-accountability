#!/usr/bin/env python3
"""Social card: veterans pipeline, war to claims — DOCUMENTED PATTERN — July 25, 2026."""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lib.card import (Card, NAVY, NAVY_DK, DARK, GOLD, RED, RED_DK, GREEN,
                      ORANGE, BRONZE, MUTED, LIGHTGRAY, BORDER, WHITE)

c = Card(scale=3)


def wrap(text, size, bold, max_w):
    f = c.font(size, bold)
    lines, cur = [], ""
    for w in text.split():
        t = f"{cur} {w}".strip()
        if c.d.textlength(t, font=f) / c.s <= max_w:
            cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines


# ── Header ──
c.brand_bar()
y = c.badge(58, "DOCUMENTED PATTERN")
y = c.title(y, "Making Veterans Faster", size=37)
y = c.title(y + 2, "Than We Care For Them", size=37)
y += 10
y = c.subtitle(y, "The war, the count, and the system waiting for them", size=17)
y = c.divider(y + 12, margin=48, pad=16)

# ── Pipeline stages ──
STAGES = [
    ("7", RED, "votes to keep an unauthorized war going",
     "Two passed the House anyway. One failed on a 212 to 212 tie."),
    ("18→14", ORANGE, "the Pentagon's death count went DOWN",
     "Wounded fell 482 to 420. Zero July wounded recorded. 16 senators objected."),
    ("50%→0%", RED, "sleep apnea rating, for future claims",
     "Tinnitus loses its standalone rating. He voted 7 times to keep it in."),
    ("1,102", ORANGE, "fewer VBA claims examiners",
     "67,849 claims already past 125 days. Vacancies unfilled by policy."),
    ("5.1%", BRONZE, "cut to VA research staffing",
     "Research is how the next PACT Act ever gets proven."),
]

LX, SX, RIGHT = 44, 250, c.w - 60
for i, (stat, accent, head, detail) in enumerate(STAGES, 1):
    dl = wrap(detail, 15, False, RIGHT - SX)
    row_h = 108
    c.rect(LX, y, LX + 5, y + row_h, fill=accent)
    c.rect(LX + 5, y, c.w - 44, y + row_h, fill=WHITE, outline=BORDER, radius=0)
    # step number
    c.d.ellipse([c._p(LX + 20), c._p(y + 44), c._p(LX + 48), c._p(y + 72)], fill=NAVY)
    c.text(LX + 34, y + 58, str(i), size=15, bold=True, fill=WHITE, anchor="mm")
    # stat
    size = 44 if len(stat) <= 5 else 34
    c.text(LX + 62, y + 58, stat, size=size, impact=True, fill=accent, anchor="lm")
    # headline + detail
    c.text(SX, y + 40, head, size=18, bold=True, fill=DARK, anchor="lm")
    yy = y + 66
    for ln in dl:
        c.text(SX, yy, ln, size=15, fill="#4A5568", anchor="lm")
        yy += 19
    y += row_h + 10

# ── Fairness panel ──
y += 6
pan_h = 104
c.panel(44, y, c.w - 44, y + pan_h, fill="#EDF7F0", outline="#9AE6B4", radius=8)
c.text(c.w / 2, y + 30, "What cuts the other way, and we say so:",
       size=16, bold=True, fill=GREEN, anchor="mm")
c.text(c.w / 2, y + 56, "He voted to RAISE toxic exposure funding, and for the bill that put VA research",
       size=15, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 79, "above last year. He has no PACT Act votes: it passed before he took office.",
       size=15, fill=DARK, anchor="mm")
y += pan_h + 14

# ── Sources + URL ──
c.text(c.w / 2, y + 8,
       "Sources: clerk.house.gov  ·  DoD Inspector General  ·  VA Workforce Dashboard  ·  VBA  ·  16-senator letter",
       size=14, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 31, "langworthywatch.org", size=17, bold=True, fill=NAVY, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "veterans_pipeline_card.png"),
       to_desktop=True)
