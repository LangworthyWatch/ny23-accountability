#!/usr/bin/env python3
"""Social card for the Nick Shirley amplification fact-check (verdict: MISSING CONTEXT).
House style via lib/card.py."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from lib.card import Card, NAVY, RED, GREEN, GOLD, DARK, MUTED, WHITE

GREEN_TINT = "#E7F1EB"
RED_TINT = "#FBEAEA"

c = Card(scale=3)
c.brand_bar()

y = c.badge(70, "MISSING CONTEXT")
y = c.title(y + 6, "$190M the Video Never Says", size=35)
y = c.subtitle(y + 12, "He amplified the number. The video never states it.", size=17)
y = c.divider(y + 22)

# WHAT HE DID (green)
gh = 128
c.panel(44, y, c.w - 44, y + gh, fill=GREEN_TINT, outline=None, radius=10)
c.text(74, y + 34, "WHAT HE POSTED", size=15, bold=True, fill=GREEN, anchor="lm")
c.text(74, y + 72, '"New York should take him up on his offer to', size=18, fill=DARK, anchor="lm")
c.text(74, y + 102, 'help uncover fraud, waste, and abuse."', size=18, fill=DARK, anchor="lm")
y = y + gh + 28

# WHAT THE VIDEO ACTUALLY IS (red)
rh = 300
c.panel(44, y, c.w - 44, y + rh, fill=RED_TINT, outline=None, radius=10)
c.text(74, y + 36, "WHAT THE VIDEO ACTUALLY IS", size=15, bold=True, fill=RED, anchor="lm")
c.bullets(80, y + 92, [
    '"$190M" is never spoken in the video, only in the caption',
    "The confirmed DOJ case is $120M, not $190M",
    'Opens with "mafias," later: "nothing to do with Koreans"',
    "Dr. Oz adds his own ethnic claims on camera",
    "Same creator's last fraud video was largely debunked",
], accent=RED, step=42, size=16)
y = y + rh + 40

c.kicker(y, "He put it on his official page.", "None of that context came with it.")
c.footer_bar()
c.save("social-media/shirley_amplification_card.png", to_desktop=True)
