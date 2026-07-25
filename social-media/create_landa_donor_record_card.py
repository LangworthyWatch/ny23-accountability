#!/usr/bin/env python3
"""Social card: Benjamin Landa donor public record — DOCUMENTED PATTERN — July 25, 2026."""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lib.card import (Card, NAVY, NAVY_DK, DARK, GOLD, RED, RED_DK, GREEN,
                      ORANGE, MUTED, LIGHT, LIGHTGRAY, BORDER, WHITE, BG)

c = Card(scale=3)


def wrap(text, size, bold, max_w):
    """Greedy wrap in logical 1080-space units."""
    f = c.font(size, bold)
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if c.d.textlength(trial, font=f) / c.s <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


# ── Header ──
c.brand_bar()
y = c.badge(62, "DOCUMENTED PATTERN")
y = c.title(y, "The Donor's Public Record", size=36)
y += 6
y = c.subtitle(y, "Benjamin Landa, nursing home operator, Lawrence NY", size=18)
y = c.divider(y + 10, margin=48, pad=18)

# ── Money strip ──
strip_h = 106
c.panel(44, y, c.w - 44, y + strip_h, fill="#EDF7F0", outline="#9AE6B4", radius=8)
c.text(232, y + strip_h / 2 + 4, "$55,000", size=58, impact=True, fill=GREEN, anchor="mm")
c.text(430, y + 34, "to Langworthy's committees, 2022 to 2025",
       size=19, bold=True, fill=DARK, anchor="lm")
c.text(430, y + 64, "Every dollar before the vote blocking the federal",
       size=17, fill=MUTED, anchor="lm")
c.text(430, y + 86, "nursing home staffing rule until 2034", size=17, fill=MUTED, anchor="lm")
y += strip_h + 22

# ── Document rows ──
ROWS = [
    ("PROPUBLICA  ·  2015", ORANGE,
     "State regulators left at least 20 federal fines off 15 of his ownership applications.",
     "He is a former member of the state health council that reviews them."),
    ("BUFFALO NEWS  ·  2018", ORANGE,
     "At four Erie County homes: nursing assistants cut from 80 to 38, care time 89 min/day against a 133 state average.",
     "Those four are owned by his wife. His spokesman says he does not run them."),
    ("NY ATTORNEY GENERAL  ·  2022", RED,
     "Two fraud lawsuits name him: $18.6M and $22.6M alleged diverted from Medicare and Medicaid.",
     "Civil allegations. No court has found him liable on them."),
    ("HHS INSPECTOR GENERAL  ·  2025", RED,
     "99 of 100 sampled Medicare claims at a facility he co-owns failed payment requirements.",
     "Estimated total overpayment: at least $31.2 million."),
    ("FEDERAL COURT  ·  2023", NAVY,
     "He sued a magazine over these descriptions. A judge dismissed his case.",
     "Statements on fraud and understaffing held substantially true or privileged."),
]

LX, TX, RIGHT = 62, 62, c.w - 62
for label, accent, main, note in ROWS:
    main_lines = wrap(main, 17, True, RIGHT - TX)
    row_h = 36 + len(main_lines) * 24 + 28
    c.rect(44, y, 48, y + row_h, fill=accent)          # accent spine
    c.rect(48, y, c.w - 44, y + row_h, fill=WHITE, outline=BORDER, radius=0)
    c.text(LX, y + 19, label, size=14, bold=True, fill=accent, anchor="lm")
    yy = y + 42
    for ln in main_lines:
        c.text(TX, yy, ln, size=17, bold=True, fill=DARK, anchor="lm")
        yy += 24
    c.text(TX, yy + 4, note, size=15, fill=MUTED, anchor="lm")
    y += row_h + 11

# ── Restraint panel ──
y += 6
pan_h = 106
c.panel(44, y, c.w - 44, y + pan_h, fill="#EDF2F7", outline=BORDER, radius=8)
c.text(c.w / 2, y + 30, "We are not claiming a deal, and there is no evidence of one.",
       size=17, bold=True, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 58, "No Landa facility is in NY-23. A 2019 trafficking liability ruling was vacated in 2022.",
       size=15, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 82, "This is the public record of the donor. Langworthy has not been asked about it.",
       size=15, fill=MUTED, anchor="mm")
y += pan_h + 18

# ── Sources + URL ──
c.text(c.w / 2, y + 10, "Sources: ProPublica  ·  Buffalo News  ·  ag.ny.gov  ·  oig.hhs.gov  ·  E.D.N.Y.  ·  FEC",
       size=15, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 38, "langworthywatch.org/fact-checks/2026-07-25-landa-donor-public-record/",
       size=16, bold=True, fill=NAVY, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "landa_donor_record_card.png"),
       to_desktop=True)
