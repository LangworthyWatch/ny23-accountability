#!/usr/bin/env python3
"""Spin-off card — earmarks Langworthy claims that are in NY-26. House style."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib.card import Card, NAVY, RED, GREEN, MUTED, DARK, WHITE, BORDER

c = Card(scale=3)
c.brand_bar()
y = c.badge(70, "MISSING CONTEXT")
y = c.title(y, "He Claims Credit Beyond His District", size=31)
y = c.subtitle(y + 6, "Earmarks Langworthy announced that sit in NY-26, not NY-23", size=15)
y = c.divider(y + 18)

items = [
    ("Town of West Seneca water", "$1,229,360", "A local water district in NY-26 (Rep. Tim Kennedy)"),
    ("Buffalo Niagara Airport", "$1,482,000", "The facility is in Cheektowaga, NY-26"),
]
py = y + 16
ph = 150
for title, amt, note in items:
    c.panel(44, py, c.w - 44, py + ph)
    c.text(74, py + 42, title, size=19, bold=True, fill=DARK, anchor="lm")
    c.text(74, py + 88, amt, size=30, bold=True, fill=RED, anchor="lm")
    c.text(74, py + 124, note, size=15, fill=MUTED, anchor="lm")
    c.text(c.w - 74, py + 88, "NY-26", size=24, bold=True, fill=RED, anchor="rm")
    py += ph + 22

c.text(c.w / 2, py + 6, "About $2.7 million he announces as his own, outside the district he represents.",
       size=16, fill=MUTED, anchor="mm")

c.kicker(c.h - 205,
         "West Seneca and the Buffalo airport have their own congressman.",
         "Tim Kennedy (NY-26). Langworthy announced their projects as his.")
c.footer_bar()
c.save("social-media/out_of_district_card.png", to_desktop=True)
