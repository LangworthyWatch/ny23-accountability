#!/usr/bin/env python3
"""Card — Olean police "secured" that Congress hasn't funded. DOCUMENTED PATTERN."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib.card import Card, NAVY, RED, GREEN, MUTED, DARK, WHITE, GOLD

c = Card(scale=3)
c.brand_bar()
y = c.badge(70, "DOCUMENTED PATTERN")
y = c.title(y, "He “Secured” $1M for Olean Police", size=34)
y = c.subtitle(y + 6, "It's a request. Congress has not funded it.", size=17)
y = c.divider(y + 18)

py0 = y + 24
ph = 184
lx0, lx1 = 44, c.w / 2 - 10
rx0, rx1 = c.w / 2 + 10, c.w - 44
lc, rc = (lx0 + lx1) / 2, (rx0 + rx1) / 2

c.panel(lx0, py0, lx1, py0 + ph, outline=RED)
c.text(lc, py0 + 40, "WHAT HE SAID", size=16, bold=True, fill=RED, anchor="mm")
c.text(lc, py0 + 100, "“I secured", size=27, bold=True, fill=DARK, anchor="mm")
c.text(lc, py0 + 143, "$1 million”", size=27, bold=True, fill=DARK, anchor="mm")

c.panel(rx0, py0, rx1, py0 + ph, outline=GREEN)
c.text(rc, py0 + 40, "WHAT IT IS", size=16, bold=True, fill=GREEN, anchor="mm")
c.text(rc, py0 + 100, "An FY2027 request.", size=22, bold=True, fill=DARK, anchor="mm")
c.text(rc, py0 + 143, "“The Senate must act.”", size=17, fill=MUTED, anchor="mm")

y = py0 + ph + 32
list_h = 214
c.panel(44, y, c.w - 44, y + list_h)
c.text(74, y + 46, "The same past-tense claim, three times in 2026:", size=18, bold=True, fill=DARK, anchor="lm")
c.bullets(74, y + 100, [
    "February: FY2026 earmarks announced as done",
    "June: $300K + $500K hospital labs, “delivered”",
    "July: $1M Olean police, “secured”",
], accent=RED, step=38, size=18)

ny = y + list_h + 32
nh = 154
c.panel(44, ny, c.w - 44, ny + nh, outline=GOLD)
c.text(c.w / 2, ny + 56, "His own USDA Rural Development nexus letter shows", size=18, fill=MUTED, anchor="mm")
c.text(c.w / 2, ny + 99, "a single request, with no other funding behind it.", size=21, bold=True, fill=DARK, anchor="mm")

c.kicker(c.h - 178,
         "His last batch of “secured” earmarks, at this same stage:",
         "zeroed out by a stopgap budget before they became law.")
c.footer_bar()
c.save("social-media/olean_secured_card.png", to_desktop=True)
