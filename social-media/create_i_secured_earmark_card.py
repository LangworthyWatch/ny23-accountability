#!/usr/bin/env python3
"""Card B — 'What I Secured Leaves Out'. House style, 1080x1080."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib.card import Card, NAVY, RED, GREEN, MUTED, DARK, WHITE, BORDER

c = Card(scale=3)
c.brand_bar()
y = c.badge(70, "MISSING CONTEXT")
y = c.title(y, "What “I Secured” Leaves Out", size=34)
y = c.subtitle(y + 6, "His roughly $32M in earmarks, by who really delivered", size=15)
y = c.divider(y + 18)

py0 = y + 10
ph = 158
lx0, lx1 = 44, c.w / 2 - 10
rx0, rx1 = c.w / 2 + 10, c.w - 44
lc = (lx0 + lx1) / 2
rc = (rx0 + rx1) / 2

c.panel(lx0, py0, lx1, py0 + ph, fill=WHITE, outline=GREEN)
c.text(lc, py0 + 34, "GENUINELY HIS OWN", size=15, bold=True, fill=GREEN, anchor="mm")
c.text(lc, py0 + 82, "~$14.9M", size=38, bold=True, fill=GREEN, anchor="mm")
c.text(lc, py0 + 124, "incl. $4.2M sheriff helicopters", size=13, fill=MUTED, anchor="mm")

c.panel(rx0, py0, rx1, py0 + ph, fill=WHITE, outline=RED)
c.text(rc, py0 + 34, "SHARED WITH THE SENATORS", size=14, bold=True, fill=RED, anchor="mm")
c.text(rc, py0 + 82, "~$17.7M", size=38, bold=True, fill=RED, anchor="mm")
c.text(rc, py0 + 124, "Schumer & Gillibrand claim the same $", size=12, fill=MUTED, anchor="mm")

y = py0 + ph + 28
c.panel(44, y, c.w - 44, y + 104, fill="#FFF7ED", outline=BORDER)
c.text(70, y + 36, "West Seneca water, before he even took office:", size=16, bold=True, fill=DARK, anchor="lm")
c.text(70, y + 72, "Senators requested $7.4M in 2022.  His share, 2024: $1.2M.", size=16, fill=DARK, anchor="lm")

y = y + 104 + 26
c.panel(44, y, c.w - 44, y + 104, fill="#FFF7ED", outline=BORDER)
c.text(70, y + 36, "And outside NY-23 entirely:", size=16, bold=True, fill=DARK, anchor="lm")
c.text(70, y + 72, "West Seneca + the Buffalo airport ($2.7M) sit in a neighboring district.", size=16, fill=DARK, anchor="lm")

c.kicker(c.h - 205,
         "On the biggest projects, the senators he opposes asked first.",
         "And some of what he claims is not even in his district.")
c.footer_bar()
c.save("social-media/i_secured_earmark_card.png", to_desktop=True)
