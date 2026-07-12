#!/usr/bin/env python3
"""Card — "I secured": about half his earmark dollars are co-requested with the
Democratic senators he campaigns against. Uses the vetted split from the
out-of-district fact-check (~$17.7M shared / ~$14.9M solo of ~$32M). House style."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib.card import Card, NAVY, RED, GREEN, MUTED, DARK, WHITE, GOLD

c = Card(scale=3)
c.brand_bar()
y = c.badge(70, "MISSING CONTEXT")
y = c.title(y, "He Says “I Secured.”", size=34)
y = c.subtitle(y + 6, "About half his earmark dollars are shared with two senators.", size=16)
y = c.divider(y + 18)

# ---- split bar: shared vs solo (of ~$32M enacted CPF, FY24-FY26) ----
py0 = y + 22
bx0, bx1 = 44, c.w - 44
barw = bx1 - bx0
split = bx0 + barw * 0.54
bh = 72
c.rect(bx0, py0, split, py0 + bh, fill=RED, radius=8)
c.rect(split, py0, bx1, py0 + bh, fill=GREEN, radius=8)
c.text(bx0 + (split - bx0) / 2, py0 + bh / 2, "54% CO-REQUESTED", size=17, bold=True, fill=WHITE, anchor="mm")
c.text(split + (bx1 - split) / 2, py0 + bh / 2, "46% SOLO", size=16, bold=True, fill=WHITE, anchor="mm")

# ---- two labeled panels ----
y = py0 + bh + 28
ph = 184
lx0, lx1 = 44, c.w / 2 - 10
rx0, rx1 = c.w / 2 + 10, c.w - 44
lc, rc = (lx0 + lx1) / 2, (rx0 + rx1) / 2

c.panel(lx0, y, lx1, y + ph, outline=RED)
c.text(lc, y + 62, "≈ $17.7M", size=32, bold=True, fill=RED, anchor="mm")
c.text(lc, y + 116, "co-requested with Sens.", size=15, fill=DARK, anchor="mm")
c.text(lc, y + 144, "Schumer & Gillibrand", size=17, bold=True, fill=DARK, anchor="mm")

c.panel(rx0, y, rx1, y + ph, outline=GREEN)
c.text(rc, y + 62, "≈ $14.9M", size=32, bold=True, fill=GREEN, anchor="mm")
c.text(rc, y + 116, "genuinely his own", size=15, fill=DARK, anchor="mm")
c.text(rc, y + 144, "(led by $4.2M sheriff air unit)", size=14, fill=MUTED, anchor="mm")

# ---- shared examples ----
y = y + ph + 30
eh = 208
c.panel(44, y, c.w - 44, y + eh, outline=GOLD)
c.text(74, y + 46, "Projects he shares with the two senators:", size=17, bold=True, fill=DARK, anchor="lm")
c.bullets(74, y + 98, [
    "West Seneca water, Portville water, Hornell water",
    "North Chautauqua Lake sewer, Town of Friendship water",
    "The senators requested several of them first, back in 2022.",
], accent=GOLD, step=40, size=15)

c.kicker(c.h - 182,
         "The two Democratic senators he campaigns against",
         "co-request about half the earmarks he calls his own.")
c.footer_bar()
c.save("social-media/shared_earmarks_card.png", to_desktop=True)
