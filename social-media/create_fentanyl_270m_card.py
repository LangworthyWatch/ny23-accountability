#!/usr/bin/env python3
"""Social card: the 270 million fentanyl claim vs. CBP's own seizure data. September 18, 2026."""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lib.card import (Card, NAVY, DARK, GOLD, RED, RED_DK, GREEN,
                      MUTED, BORDER, WHITE)

c = Card(scale=3)
RED_BG, RED_BD = "#FFF5F5", "#FEB2B2"
GREEN_BG, GREEN_BD = "#F0FFF4", "#9AE6B4"

c.brand_bar()
y = c.badge(58, "NOT SUPPORTED")
y = c.title(y, "His Number vs. the Government's Number", size=31)
y += 4
y = c.subtitle(y, "Northern border fentanyl seizures in 2024, from his official page and from CBP's own data", size=14.5)
y = c.divider(y + 10, margin=48, pad=14)

# ── Two panels: claim vs. data ──
PT, PB = y, y + 372
MID = c.w / 2
c.panel(44, PT, MID - 8, PB, fill=RED_BG, outline=RED_BD, radius=8)
c.panel(MID + 8, PT, c.w - 44, PB, fill=GREEN_BG, outline=GREEN_BD, radius=8)
lcx = (44 + MID - 8) / 2
rcx = (MID + 8 + c.w - 44) / 2

c.text(lcx, PT + 26, "WHAT HE POSTED", size=14, bold=True, fill=RED_DK, anchor="mm")
c.text(lcx, PT + 46, "official Facebook page, Sept. 17, 2026", size=12, fill=MUTED, anchor="mm")
c.text(lcx, PT + 128, "270", size=100, impact=True, fill=RED, anchor="mm")
c.text(lcx, PT + 194, "MILLION", size=22, bold=True, fill=RED_DK, anchor="mm")
for i, s in enumerate(['"the amount of fentanyl seized there', 'was enough to potentially kill',
                       '270 million Americans"', '', 'No source given in the post or video']):
    c.text(lcx, PT + 236 + i * 24, s, size=13.5 if i < 3 else 12.5,
           fill=(DARK if i < 3 else MUTED), anchor="mm")

c.text(rcx, PT + 26, "WHAT CBP'S OWN DATA SUPPORTS", size=14, bold=True, fill=GREEN, anchor="mm")
c.text(rcx, PT + 46, "fiscal 2024, northern border", size=12, fill=MUTED, anchor="mm")
c.text(rcx, PT + 128, "9.75", size=100, impact=True, fill=GREEN, anchor="mm")
c.text(rcx, PT + 194, "MILLION", size=22, bold=True, fill=GREEN, anchor="mm")
for i, s in enumerate(['43.0 lbs of fentanyl seized (CBP)', 'x DEA: "one kilogram of fentanyl has',
                       'the potential to kill 500,000 people"', '', 'Still a serious number. Not 270 million.']):
    c.text(rcx, PT + 236 + i * 24, s, size=13.5 if i < 3 else 12.5,
           fill=(DARK if i < 3 else MUTED), bold=(i == 4), anchor="mm")
y = PB + 16

# ── The math strip ──
SH = 140
c.panel(44, y, c.w - 44, y + SH, fill="#EDF2F7", outline=None, radius=8)
c.text(c.w / 2, y + 22, "WHAT 270 MILLION WOULD ACTUALLY TAKE", size=13, bold=True, fill=NAVY, anchor="mm")
for cx, big, lab, col in [(c.w * 0.22, "1,190 lbs", "of fentanyl, by DEA's ratio", NAVY),
                          (c.w * 0.50, "~28x", "what CBP seized there", RED),
                          (c.w * 0.78, "0.2%", "of all CBP fentanyl seizures", NAVY)]:
    c.text(cx, y + 70, big, size=38, impact=True, fill=col, anchor="mm")
    c.text(cx, y + 110, lab, size=13.5, fill=DARK, anchor="mm")
y += SH + 14

# ── Fairness callout ──
CH = 80
c.panel(44, y, c.w - 44, y + CH, fill="#FFFBEB", outline=GOLD, radius=8)
c.text(c.w / 2, y + 26, "EVEN THE HIGHER YEAR DOESN'T GET CLOSE", size=13, bold=True, fill="#975A16", anchor="mm")
c.text(c.w / 2, y + 54, "Fiscal 2025 northern border seizures rose to 77.1 lbs: about 17.5 million by the same ratio.",
       size=14, fill=DARK, anchor="mm")
y += CH + 12

y = c.kicker(y,
             "We could not find a source for the 270 million figure.",
             "If his office has one, we'll publish it.",
             h=100)

c.text(c.w / 2, y + 28, "Sources: CBP Nationwide Drug Seizures, FY2024 and FY2025, Northern Border region  ·  DEA, \"Facts About Fentanyl\"",
       size=11.5, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 50, "langworthywatch.org/fact-checks/2026-07-06-northern-border-security-review-act/",
       size=12.5, bold=True, fill=NAVY, anchor="mm")

c.footer_bar()
c.save("social-media/fentanyl_270m_card.png", to_desktop=True)
print("saved")
