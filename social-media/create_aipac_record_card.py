#!/usr/bin/env python3
"""Social card: AIPAC money and Langworthy's record — DOCUMENTED PATTERN — July 25, 2026."""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lib.card import (Card, NAVY, NAVY_DK, DARK, GOLD, RED, RED_DK, GREEN,
                      ORANGE, MUTED, LIGHT, LIGHTGRAY, BORDER, WHITE)

c = Card(scale=3)


def wrap(text, size, bold, max_w):
    f = c.font(size, bold)
    lines, cur = [], ""
    for w in text.split():
        trial = f"{cur} {w}".strip()
        if c.d.textlength(trial, font=f) / c.s <= max_w:
            cur = trial
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines


def pill(x, y, label, fg, bg):
    """Small verdict pill, left-anchored at x. Returns its width."""
    f = c.font(14, bold=True)
    w = c.d.textlength(label, font=f) / c.s + 22
    c.rect(x, y - 12, x + w, y + 12, fill=bg, outline=fg, width=2, radius=12)
    c.text(x + w / 2, y, label, size=14, bold=True, fill=fg, anchor="mm")
    return w


# ── Header ──
c.brand_bar()
y = c.badge(60, "DOCUMENTED PATTERN")
y = c.title(y, "AIPAC and Langworthy", size=38)
y += 8
y = c.subtitle(y, "Four claims people make, checked against the primary records", size=17)
y = c.divider(y + 12, margin=48, pad=18)

# ── Hero: the Rules finding ──
hero_h = 108
c.panel(44, y, c.w - 44, y + hero_h, fill=NAVY, outline=None, radius=8)
c.text(72, y + 32, "He did not just vote for the Israel arms bill.", size=21, bold=True,
       fill=WHITE, anchor="lm")
c.text(72, y + 62, "He wrote the rule that put it on the floor, and it barred amendments.",
       size=18, fill="#CBD5E0", anchor="lm")
c.text(72, y + 86, "H.Res. 1227, May 15 2024: he sponsored it, reported it, floor-managed it.",
       size=15, fill="#93A9C4", anchor="lm")
y += hero_h + 18

# ── Money strip ──
strip_h = 104
c.panel(44, y, c.w - 44, y + strip_h, fill="#EDF7F0", outline="#9AE6B4", radius=8)
cols = [("$25,000", "direct from AIPAC's PAC", "ordinary size"),
        ("$76,016", "bundled through AIPAC", "75 contributions"),
        ("$101,016", "total routed", "2022 to 2026")]
for i, (big, lab, sub) in enumerate(cols):
    cx = 44 + (c.w - 88) * (i + 0.5) / 3
    c.text(cx, y + 34, big, size=40, impact=True, fill=GREEN, anchor="mm")
    c.text(cx, y + 64, lab, size=16, bold=True, fill=DARK, anchor="mm")
    c.text(cx, y + 85, sub, size=14, fill=MUTED, anchor="mm")
for i in (1, 2):
    xx = 44 + (c.w - 88) * i / 3
    c.d.line([(c._p(xx), c._p(y + 20)), (c._p(xx), c._p(y + strip_h - 20))],
             fill="#9AE6B4", width=c._p(1))
y += strip_h + 18

# ── Claim rows ──
ROWS = [
    ("AIPAC's super PAC spent money to elect him.", "FALSE", GREEN, "#EDF7F0",
     "Zero independent expenditures for or against him. From any committee. Ever."),
    ("AIPAC is one of his biggest donors.", "MISSING CONTEXT", ORANGE, "#FFF7ED",
     "The $25,000 check is ordinary. The $76,016 AIPAC bundled is the real number."),
    ("He took an AIPAC-funded trip to Israel.", "TRUE", RED, "#FEF2F2",
     "$15,900.02, April 2024, paid by AIPAC's charitable affiliate. Fully disclosed."),
    ("He votes on Israel like any Republican.", "MISSING CONTEXT", ORANGE, "#FFF7ED",
     "Yes on Israel aid, No on Ukraine aid, same day. No on all six Iran war powers votes."),
]

TX, RIGHT = 66, c.w - 62
for claim, verdict, accent, tint, reality in ROWS:
    rl = wrap(reality, 16, False, RIGHT - TX)
    row_h = 34 + 26 + len(rl) * 21 + 16
    c.rect(44, y, 49, y + row_h, fill=accent)
    c.rect(49, y, c.w - 44, y + row_h, fill=tint, outline=BORDER, radius=0)
    c.text(TX, y + 24, claim, size=17, bold=True, fill=DARK, anchor="lm")
    pill(TX, y + 52, verdict, accent, WHITE)
    yy = y + 76
    for ln in rl:
        c.text(TX, yy, ln, size=16, fill="#2D3748", anchor="lm")
        yy += 21
    y += row_h + 10

# ── Restraint ──
y += 6
pan_h = 76
c.panel(44, y, c.w - 44, y + pan_h, fill="#EDF2F7", outline=BORDER, radius=8)
c.text(c.w / 2, y + 26, "Bundling, advocacy money, and Ethics-approved travel are all legal.",
       size=16, bold=True, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 52, "We are documenting the record, not alleging a deal.",
       size=15, fill=MUTED, anchor="mm")
y += pan_h + 18

# ── Sources + URL ──
c.text(c.w / 2, y + 8, "Sources: FEC OpenFEC API  ·  clerk.house.gov roll calls  ·  GPO BILLSTATUS  ·  House Clerk gift travel",
       size=14, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 32, "langworthywatch.org/fact-checks/aipac-record/",
       size=16, bold=True, fill=NAVY, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "aipac_record_card.png"),
       to_desktop=True)
