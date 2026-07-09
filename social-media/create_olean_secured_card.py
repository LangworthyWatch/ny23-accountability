#!/usr/bin/env python3
"""Card — Olean police "secured" that Congress hasn't funded. DOCUMENTED PATTERN."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib.card import Card, NAVY, RED, GREEN, MUTED, DARK, WHITE

c = Card(scale=3)
c.brand_bar()
y = c.badge(70, "DOCUMENTED PATTERN")
y = c.title(y, "He “Secured” $1M for Olean Police", size=31)
y = c.subtitle(y + 6, "It's a request. Congress has not funded it.", size=15)
y = c.divider(y + 18)

py0 = y + 16
ph = 150
lx0, lx1 = 44, c.w / 2 - 10
rx0, rx1 = c.w / 2 + 10, c.w - 44
lc, rc = (lx0 + lx1) / 2, (rx0 + rx1) / 2

c.panel(lx0, py0, lx1, py0 + ph, outline=RED)
c.text(lc, py0 + 34, "WHAT HE SAID", size=14, bold=True, fill=RED, anchor="mm")
c.text(lc, py0 + 82, "“I secured", size=22, bold=True, fill=DARK, anchor="mm")
c.text(lc, py0 + 116, "$1 million”", size=22, bold=True, fill=DARK, anchor="mm")

c.panel(rx0, py0, rx1, py0 + ph, outline=GREEN)
c.text(rc, py0 + 34, "WHAT IT IS", size=14, bold=True, fill=GREEN, anchor="mm")
c.text(rc, py0 + 82, "An FY2027 request.", size=18, bold=True, fill=DARK, anchor="mm")
c.text(rc, py0 + 116, "“The Senate must act.”", size=15, fill=MUTED, anchor="mm")

y = py0 + ph + 26
c.panel(44, y, c.w - 44, y + 138)
c.text(74, y + 38, "The same past-tense claim, three times in 2026:", size=16, bold=True, fill=DARK, anchor="lm")
c.bullets(74, y + 78, [
    "February: FY2026 earmarks announced as done",
    "June: $300K + $500K hospital labs, “delivered”",
    "July: $1M Olean police, “secured”",
], accent=RED, step=32, size=15)

c.kicker(c.h - 175,
         "His last batch of “secured” earmarks, at this same stage:",
         "zeroed out by a stopgap budget before they became law.")
c.footer_bar()
c.save("social-media/olean_secured_card.png", to_desktop=True)
