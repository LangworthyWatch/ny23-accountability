#!/usr/bin/env python3
"""Social card: the war powers votes + the rebranding + the legal read. July 25, 2026."""

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
y = c.title(y, "Congress Voted Twice", size=37)
y = c.title(y + 2, "To End It. He Voted No.", size=37)
y += 8
y = c.subtitle(y, "Seven war powers votes, and a war that was declared over while it continued", size=15)
y = c.divider(y + 10, margin=48, pad=14)

# ── The vote ledger ──
c.text(60, y + 10, "THE IRAN RESOLUTIONS", size=14, bold=True, fill=NAVY, anchor="lm")
y += 26

ROWS = [
    ("Mar. 5", "H.Con.Res. 38", "Failed 212-219", False),
    ("Apr. 16", "H.Con.Res. 40", "Failed 213-214", False),
    ("May 14", "H.Con.Res. 75", "Failed on a 212-212 TIE", True),
    ("Jun. 3", "H.Con.Res. 86", "PASSED 215-208", True),
    ("Jul. 23", "H.Con.Res. 89", "PASSED 214-208", True),
]
LX = 48
for date, meas, result, hilite in ROWS:
    row_h = 44
    c.rect(LX, y, LX + 4, y + row_h, fill=(RED if hilite else LIGHTGRAY))
    c.rect(LX + 4, y, c.w - 48, y + row_h, fill=WHITE, outline=BORDER, radius=0)
    c.text(LX + 20, y + 23, date, size=15, bold=True, fill=DARK, anchor="lm")
    c.text(LX + 108, y + 23, meas, size=15, fill="#4A5568", anchor="lm")
    c.text(LX + 300, y + 23, result, size=15,
           bold=hilite, fill=(RED_DK if hilite else "#4A5568"), anchor="lm")
    c.text(c.w - 68, y + 23, "NAY", size=16, bold=True, fill=RED, anchor="rm")
    y += row_h + 7

c.text(60, y + 14, "Plus two on Lebanon, also Nay. Seven votes, seven times No.",
       size=14, fill=MUTED, anchor="lm")
y += 42

# ── The rebranding ──
pan_h = 118
c.panel(48, y, c.w - 48, y + pan_h, fill="#FFF8E7", outline=GOLD, radius=6)
c.text(68, y + 26, "Then the war was declared over, and the strikes went on.",
       size=17, bold=True, fill=DARK, anchor="lm")
c.text(68, y + 52, "May 1: the President tells Congress the operation is \"terminated.\"",
       size=14, fill="#4A5568", anchor="lm")
c.text(68, y + 74, "July 6: near-daily strikes resume. They are now called \"overseas operations.\"",
       size=14, fill="#4A5568", anchor="lm")
y += pan_h + 16

# ── The legal read ──
pan_h = 126
c.panel(48, y, c.w - 48, y + pan_h, fill=WHITE, outline=BORDER, radius=6)
c.text(68, y + 24, "What the lawyers say about that theory:", size=15, bold=True, fill=NAVY, anchor="lm")
c.text(68, y + 52, "\"I find this interpretation of the WPR implausible.\"",
       size=17, bold=True, fill=DARK, anchor="lm")
c.text(68, y + 78, "Jack Goldsmith, who ran the Office of Legal Counsel under George W. Bush.",
       size=14, fill="#4A5568", anchor="lm")
c.text(68, y + 97, "Critics at Just Security reached the same word, independently.",
       size=14, fill="#4A5568", anchor="lm")
y += pan_h + 16

# ── Bipartisan objection ──
c.text(c.w / 2, y + 10, "A Republican calls the relabeling an \"absurd ruse\":",
       size=15, bold=True, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 34, "\"The Pentagon is pretending there have been two Iran wars",
       size=15, fill=RED_DK, anchor="mm")
c.text(c.w / 2, y + 55, "separated by a brief cease-fire.\"  Rep. Thomas Massie, R-KY",
       size=15, fill=RED_DK, anchor="mm")
y += 88

# ── Fairness ──
c.text(c.w / 2, y + 8, "In fairness: presidents of both parties have stretched this statute for 50 years,",
       size=13, fill=GREEN, anchor="mm")
c.text(c.w / 2, y + 26, "and no court has struck down a concurrent resolution in the war powers context.",
       size=13, fill=GREEN, anchor="mm")
y += 50

# ── Sources + URL ──
c.text(c.w / 2, y + 8,
       "Sources: clerk.house.gov roll calls  ·  Dept. of War  ·  Cong. Record  ·  Goldsmith, Executive Functions  ·  Just Security",
       size=12, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 28, "langworthywatch.org", size=17, bold=True, fill=NAVY, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "war_powers_card.png"),
       to_desktop=True)
