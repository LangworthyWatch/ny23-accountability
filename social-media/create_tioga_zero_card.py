#!/usr/bin/env python3
"""Spin-off card — Tioga: $0 from Langworthy, $3.1M from the senators. House style."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib.card import Card, NAVY, RED, GREEN, MUTED, DARK, WHITE, BORDER

c = Card(scale=3)
c.brand_bar()
y = c.badge(70, "MISSING CONTEXT")
y = c.title(y, "Tioga County: $0 From Langworthy", size=33)
y = c.subtitle(y + 6, "Federal earmarks secured for Tioga, 2023 to 2026", size=15)
y = c.divider(y + 18)

py0 = y + 16
ph = 150
lx0, lx1 = 44, c.w / 2 - 10
rx0, rx1 = c.w / 2 + 10, c.w - 44
lc, rc = (lx0 + lx1) / 2, (rx0 + rx1) / 2

c.panel(lx0, py0, lx1, py0 + ph, fill=WHITE, outline=RED)
c.text(lc, py0 + 36, "LANGWORTHY", size=15, bold=True, fill=RED, anchor="mm")
c.text(lc, py0 + 88, "$0", size=48, bold=True, fill=RED, anchor="mm")
c.text(lc, py0 + 126, "enacted earmarks", size=13, fill=MUTED, anchor="mm")

c.panel(rx0, py0, rx1, py0 + ph, fill=WHITE, outline=GREEN)
c.text(rc, py0 + 36, "SCHUMER & GILLIBRAND", size=14, bold=True, fill=GREEN, anchor="mm")
c.text(rc, py0 + 88, "~$3.1M", size=42, bold=True, fill=GREEN, anchor="mm")
c.text(rc, py0 + 126, "for Tioga projects", size=13, fill=MUTED, anchor="mm")

y = py0 + ph + 26
c.panel(44, y, c.w - 44, y + 150)
c.text(74, y + 40, "What the senators delivered for Tioga:", size=16, bold=True, fill=DARK, anchor="lm")
c.bullets(74, y + 80, [
    "Owego-Apalachin schools, workforce training: $811,000",
    "Upper Susquehanna watershed resilience: $1,580,628",
    "Racker nonprofit service hub, Owego: $750,000",
], accent=GREEN, step=34, size=15)

y = y + 150 + 20
c.text(c.w / 2, y, "In fairness: Langworthy has requested a Tioga radio upgrade. It is not yet funded.",
       size=14, fill=MUTED, anchor="mm")

c.kicker(c.h - 175,
         "The senators he campaigns against delivered $3.1M for Tioga.",
         "His enacted total for the county: zero.")
c.footer_bar()
c.save("social-media/tioga_zero_card.png", to_desktop=True)
