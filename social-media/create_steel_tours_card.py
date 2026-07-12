#!/usr/bin/env python3
"""Card — he tours steel makers to praise "American made" while voting to keep the
Section 232 tariffs. Winners (fabricators like Cimolai) vs losers (steel buyers).
Pairs with the Jamestown/Cimolai tariffs fact-check. MISSING CONTEXT. House style."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib.card import Card, NAVY, RED, GREEN, MUTED, DARK, WHITE, GOLD

c = Card(scale=3)
c.brand_bar()
y = c.badge(70, "MISSING CONTEXT")
y = c.title(y, "He Tours the Steel. Not the Tariff.", size=32)
y = c.subtitle(y + 6, "Two “American-made” steel tours. He voted to keep the tariffs on both.", size=15)
y = c.divider(y + 18)

py0 = y + 24
ph = 232
lx0, lx1 = 44, c.w / 2 - 10
rx0, rx1 = c.w / 2 + 10, c.w - 44
lc, rc = (lx0 + lx1) / 2, (rx0 + rx1) / 2

c.panel(lx0, py0, lx1, py0 + ph, outline=GREEN)
c.text(lc, py0 + 46, "WHO THE TARIFF HELPS", size=14, bold=True, fill=GREEN, anchor="mm")
c.text(lc, py0 + 106, "Cimolai-HY, Olean", size=20, bold=True, fill=DARK, anchor="mm")
c.text(lc, py0 + 150, "the steel fabricator he", size=15, fill=MUTED, anchor="mm")
c.text(lc, py0 + 178, "toured July 9. Its own", size=15, fill=MUTED, anchor="mm")
c.text(lc, py0 + 206, "industry backs the tariffs.", size=15, fill=MUTED, anchor="mm")

c.panel(rx0, py0, rx1, py0 + ph, outline=RED)
c.text(rc, py0 + 46, "WHO IT HURTS", size=14, bold=True, fill=RED, anchor="mm")
c.text(rc, py0 + 106, "Steel buyers", size=20, bold=True, fill=DARK, anchor="mm")
c.text(rc, py0 + 150, "Jamestown Advanced;", size=15, fill=MUTED, anchor="mm")
c.text(rc, py0 + 178, "dairy barns, +$21K each;", size=15, fill=MUTED, anchor="mm")
c.text(rc, py0 + 206, "eSolutions: closed, 230 jobs.", size=15, fill=MUTED, anchor="mm")

ny = py0 + ph + 32
nh = 132
c.panel(44, ny, c.w - 44, ny + nh, outline=GOLD)
c.text(c.w / 2, ny + 50, "His record on the policy that splits them:", size=15, fill=MUTED, anchor="mm")
c.text(c.w / 2, ny + 90, "voted to keep the 50% steel tariffs (Feb 2026).", size=18, bold=True, fill=DARK, anchor="mm")

c.text(c.w / 2, ny + nh + 40, "Steel mill prices since the tariffs: up about 21%.", size=15, fill=MUTED, anchor="mm")

c.kicker(c.h - 272,
         "He toured both sides of the tariff.",
         "He mentioned it at neither.")
c.footer_bar()
c.save("social-media/steel_tours_card.png", to_desktop=True)
