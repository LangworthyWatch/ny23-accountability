#!/usr/bin/env python3
"""Social card: veterans pipeline + the oversight seat — DOCUMENTED PATTERN — July 25, 2026."""

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
y = c.badge(56, "DOCUMENTED PATTERN")
y = c.title(y, "Making Veterans Faster", size=36)
y = c.title(y + 2, "Than We Care For Them", size=36)
y += 8
y = c.subtitle(y, "The war, the count, and the system waiting for them", size=16)
y = c.divider(y + 10, margin=48, pad=14)

# ── Pipeline stages ──
STAGES = [
    ("7", RED, "votes to keep an unauthorized war going",
     "Two passed the House anyway. One failed on a 212 to 212 tie."),
    ("18→14", ORANGE, "the Pentagon's death count went DOWN",
     "Wounded fell 482 to 420. Zero July wounded recorded."),
    ("50%→0%", RED, "sleep apnea rating, for future claims",
     "Tinnitus loses its standalone rating. He voted 7 times to keep it in."),
    ("1,102", ORANGE, "fewer VBA claims examiners",
     "67,849 claims already past 125 days. Vacancies unfilled by policy."),
    ("5.1%", BRONZE, "cut to VA research staffing",
     "Research is how the next PACT Act ever gets proven."),
]

LX, SX, RIGHT = 44, 248, c.w - 60
for i, (stat, accent, head, detail) in enumerate(STAGES, 1):
    dl = wrap(detail, 15, False, RIGHT - SX)
    row_h = 98
    c.rect(LX, y, LX + 5, y + row_h, fill=accent)
    c.rect(LX + 5, y, c.w - 44, y + row_h, fill=WHITE, outline=BORDER, radius=0)
    c.d.ellipse([c._p(LX + 20), c._p(y + 36), c._p(LX + 46), c._p(y + 62)], fill=NAVY)
    c.text(LX + 33, y + 49, str(i), size=14, bold=True, fill=WHITE, anchor="mm")
    c.text(LX + 60, y + 50, stat, size=(42 if len(stat) <= 5 else 33),
           impact=True, fill=accent, anchor="lm")
    c.text(SX, y + 34, head, size=17, bold=True, fill=DARK, anchor="lm")
    yy = y + 58
    for ln in dl:
        c.text(SX, yy, ln, size=15, fill="#4A5568", anchor="lm")
        yy += 19
    y += row_h + 8

# ── Closing panel: the oversight seat ──
y += 8
pan_h = 132
c.panel(44, y, c.w - 44, y + pan_h, fill=NAVY, outline=None, radius=8)
c.text(c.w / 2, y + 30, "He sits on the Oversight Committee.",
       size=25, bold=True, fill=WHITE, anchor="mm")
c.text(c.w / 2, y + 62, "The committee that investigates federal agencies. He is in the majority.",
       size=16, fill="#CBD5E0", anchor="mm")
c.text(c.w / 2, y + 92, "Sixteen senators had to send a letter. He could call a hearing.",
       size=18, bold=True, fill=GOLD, anchor="mm")
c.text(c.w / 2, y + 115, "No hearing request, committee letter, or statement located.",
       size=15, fill="#93A9C4", anchor="mm")
y += pan_h + 16

# ── Fairness line (kept, compressed) ──
c.text(c.w / 2, y + 9, "What cuts the other way: he voted to RAISE toxic exposure funding, and he has",
       size=15, fill=GREEN, anchor="mm")
c.text(c.w / 2, y + 30, "no PACT Act votes at all. That law passed before he took office.",
       size=15, fill=GREEN, anchor="mm")
y += 50

# ── Sources + URL ──
c.text(c.w / 2, y + 6,
       "Sources: clerk.house.gov  ·  DoD Inspector General  ·  VA Workforce Dashboard  ·  VBA  ·  16-senator letter",
       size=13, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 28, "langworthywatch.org", size=17, bold=True, fill=NAVY, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "veterans_pipeline_card.png"),
       to_desktop=True)
