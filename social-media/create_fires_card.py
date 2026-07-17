#!/usr/bin/env python3
"""Social card for the Canada wildfire 'policy choice' fact-check (verdict: MISLEADING).
House style via lib/card.py. Angle: our smoke does the same thing to Canada."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from lib.card import Card, NAVY, RED, GREEN, GOLD, DARK, MUTED, WHITE

GREEN_TINT = "#E7F1EB"
RED_TINT = "#FBEAEA"

c = Card(scale=3)
c.brand_bar()

y = c.badge(70, "MISLEADING")
y = c.title(y + 6, "Our Smoke Goes North, Too", size=35)
y = c.subtitle(y + 12, 'He blames Canada\'s "policy choice." The smoke crosses both ways.', size=17)
y = c.divider(y + 22)

# HIS CLAIM (green)
gh = 132
c.panel(44, y, c.w - 44, y + gh, fill=GREEN_TINT, outline=None, radius=10)
c.text(74, y + 34, "HIS CLAIM", size=15, bold=True, fill=GREEN, anchor="lm")
c.text(74, y + 72, 'Canada\'s forest "policy choice" is poisoning our', size=18, fill=DARK, anchor="lm")
c.text(74, y + 102, "air, and there should be consequences.", size=18, fill=DARK, anchor="lm")
y = y + gh + 28

# THE RECORD (red)
rh = 296
c.panel(44, y, c.w - 44, y + rh, fill=RED_TINT, outline=None, radius=10)
c.text(74, y + 36, "THE RECORD", size=15, bold=True, fill=RED, anchor="lm")
c.bullets(80, y + 92, [
    "Climate made the record 2023 fires 2x likelier (peer-reviewed)",
    "US smoke hit 5+ Canadian provinces in 2020, shut Vancouver's mail",
    "Canadian officials blame the warming climate too",
    "The US is running its own severe 2026 fire season now",
    "He voted NO on clean energy, YES on the law repealing it",
], accent=RED, step=42, size=16)
y = y + rh + 40

c.kicker(y, "Smoke crosses both ways.", "He only points one direction.")
c.footer_bar()
c.save("social-media/fires_policy_choice_card.png", to_desktop=True)
