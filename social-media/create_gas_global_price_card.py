#!/usr/bin/env python3
"""Social card: the Energy Choice Act pitch ("affordable, reliable, and proven") beside EIA data showing U.S. gas
prices move with exports, world demand and weather, not just domestic output.

Anchored to content/fact-checks/2026-02-25-energy-choice-act.md (verdict: MISLEADING). New figures are from EIA pages
retained under research/sources/gas-global-2026-10/ (STEO Oct 6, 2026; Today in Energy 55119, 64844).

Hero: production +4% vs. price +61% in 2025. Middle: why (exports, 2022 Europe demand, Freeport outage, weather).
Fair reading on the card. 1080x1080, no em dashes (enforced).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GOLD, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()

y = c.badge(58, "MISLEADING")
y = c.title(y, '"Energy That Is Affordable, Reliable, and Proven."', size=27)
y = c.title(y + 4, "U.S. Gas Production Went Up in 2025. So Did the Price.", size=23, fill=DARK)
y = c.subtitle(y + 6, "His pitch for the Energy Choice Act, beside U.S. Energy Information Administration (EIA) data.", size=14)
y = c.divider(y + 12)

# ---- hero ---------------------------------------------------------------------------------
col_w = (c.w - 44 * 2 - 16) // 2
hero_h = 216
lx, rx = 44, 44 + col_w + 16
top = y + 2
for x0, fill, outline, color, label, big, l1, l2 in [
    (lx, "#EDF2F7", "#A3BFD9", NAVY, "U.S. GAS PRODUCTION, 2024 TO 2025", "+4%", "103.1 to 107.6 billion", "cubic feet a day"),
    (rx, "#FFF5F5", "#FEB2B2", RED, "U.S. GAS PRICE (HENRY HUB), 2024 TO 2025", "+61%", "$2.19 to $3.53", "per million Btu"),
]:
    c.panel(x0, top, x0 + col_w, top + hero_h, fill=fill, outline=outline)
    c.text(x0 + col_w / 2, top + 26, label, size=14, bold=True, fill=color, anchor="mm")
    c.text(x0 + col_w / 2, top + 102, big, size=76, impact=True, fill=color, anchor="mm")
    c.text(x0 + col_w / 2, top + 166, l1, size=15, bold=True, fill=DARK, anchor="mm")
    c.text(x0 + col_w / 2, top + 190, l2, size=14, fill=DARK, anchor="mm")
y = top + hero_h + 14

# ---- why ------------------------------------------------------------------------------------
rows = [("More of our gas is sold overseas", "The U.S. is the world's largest LNG exporter. Exports rose from 11.9 to 15.1 billion cubic feet a day in 2025."),
        ("2022: demand from Europe", "EIA cited high European demand for U.S. LNG. Henry Hub averaged $6.45, the highest since 2008."),
        ("One terminal outage cut U.S. prices 40%", "When the Freeport LNG export terminal shut after a fire, prices fell 40% from early June to July 4, 2022."),
        ("Weather still drives spikes", "Winter Storm Fern pushed the January 2026 average to $7.72.")]
row_h = 56
box_h = 40 + row_h * len(rows)
c.panel(44, y, c.w - 44, y + box_h, fill=WHITE, outline=BORDER)
c.text(c.w / 2, y + 22, "WHAT ELSE MOVES THE PRICE: EXPORTS, WORLD DEMAND, WEATHER", size=14, bold=True, fill=NAVY, anchor="mm")
for i, (lab, txt) in enumerate(rows):
    ry = y + 42 + i * row_h
    c.text(66, ry + 14, lab, size=15, bold=True, fill=NAVY, anchor="lm")
    c.text(66, ry + 36, txt, size=13.5, fill=DARK, anchor="lm")
y += box_h + 12

# ---- fair reading ---------------------------------------------------------------------------
fr_h = 108
c.panel(44, y, c.w - 44, y + fr_h, fill="#FFFBEB", outline=GOLD)
c.text(c.w / 2, y + 22, "THE FAIR READING", size=14, bold=True, fill="#744210", anchor="mm")
for i, ln in enumerate(["One year is a short window, and 2025 rose from a low 2024 price. More supply does help: EIA says",
                        "rising production keeps storage full, which limits spikes, and forecasts about $3.16 for 2027.",
                        "But exports are growing faster: about 16% of U.S. gas in 2026 (EIA projection), up from about 12% in 2024."]):
    c.text(c.w / 2, y + 48 + i * 21, ln, size=13, fill=DARK, anchor="mm")
y += fr_h + 12

# ---- kicker ---------------------------------------------------------------------------------
kick_h = 86
c.panel(44, y, c.w - 44, y + kick_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 26, "The Energy Choice Act blocks state and local limits on gas hookups.", size=13.5, fill=LIGHTGRAY, anchor="mm")
c.text(c.w / 2, y + 58, "It does not change what the gas costs.", size=19, bold=True, fill=WHITE, anchor="mm")
y += kick_h + 10

c.text(c.w / 2, y, "Sources: EIA Short-Term Energy Outlook, Oct 6, 2026  ·  EIA Today in Energy, Jan 9, 2023 and Mar 27, 2025  ·  H.R. 3699  ·  his June 2025 release",
       size=10.5, fill=MUTED, anchor="mm")
c.text(c.w / 2, y + 17, "Full entry at langworthywatch.org", size=11, fill=MUTED, anchor="mm")

c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "gas_global_price_card.png"), to_desktop=True)
