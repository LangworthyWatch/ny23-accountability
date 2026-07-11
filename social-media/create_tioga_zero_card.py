#!/usr/bin/env python3
"""Spin-off card — Tioga: $0 from Langworthy, $3.1M from the senators. House style."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib.card import Card, NAVY, RED, GREEN, MUTED, DARK, WHITE, BORDER, GOLD

c = Card(scale=3)
c.brand_bar()
y = c.badge(70, "MISSING CONTEXT")
y = c.title(y, "Tioga County: $0 From Langworthy", size=33)
y = c.subtitle(y + 6, "Federal earmarks secured for Tioga, 2023 to 2026", size=16)
y = c.divider(y + 18)

py0 = y + 24
ph = 186
lx0, lx1 = 44, c.w / 2 - 10
rx0, rx1 = c.w / 2 + 10, c.w - 44
lc, rc = (lx0 + lx1) / 2, (rx0 + rx1) / 2

c.panel(lx0, py0, lx1, py0 + ph, fill=WHITE, outline=RED)
c.text(lc, py0 + 42, "LANGWORTHY", size=16, bold=True, fill=RED, anchor="mm")
c.text(lc, py0 + 108, "$0", size=52, bold=True, fill=RED, anchor="mm")
c.text(lc, py0 + 156, "enacted earmarks", size=14, fill=MUTED, anchor="mm")

c.panel(rx0, py0, rx1, py0 + ph, fill=WHITE, outline=GREEN)
c.text(rc, py0 + 42, "SCHUMER & GILLIBRAND", size=15, bold=True, fill=GREEN, anchor="mm")
c.text(rc, py0 + 108, "~$3.1M", size=46, bold=True, fill=GREEN, anchor="mm")
c.text(rc, py0 + 156, "for Tioga projects", size=14, fill=MUTED, anchor="mm")

y = py0 + ph + 30
list_h = 190
c.panel(44, y, c.w - 44, y + list_h)
c.text(74, y + 46, "What the senators delivered for Tioga:", size=17, bold=True, fill=DARK, anchor="lm")
c.bullets(74, y + 96, [
    "Owego-Apalachin schools, workforce training: $811,000",
    "Upper Susquehanna watershed resilience: $1,580,628",
    "Racker nonprofit service hub, Owego: $750,000",
], accent=GREEN, step=40, size=16)

ny = y + list_h + 30
nh = 118
c.panel(44, ny, c.w - 44, ny + nh, outline=GOLD)
c.text(c.w / 2, ny + 44, "In fairness, his one action for Tioga:", size=16, fill=MUTED, anchor="mm")
c.text(c.w / 2, ny + 82, "a requested radio upgrade, still not funded.", size=18, bold=True, fill=DARK, anchor="mm")

c.kicker(c.h - 178,
         "The senators he campaigns against delivered $3.1M for Tioga.",
         "His enacted total for the county: zero.")
c.footer_bar()
c.save("social-media/tioga_zero_card.png", to_desktop=True)
