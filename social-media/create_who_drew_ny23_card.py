#!/usr/bin/env python3
"""Who drew NY-23, entry 2026-11-13-who-drew-ny23-redistricting (MOSTLY TRUE). Template B with HELD UP.
Figures: Downballot 2020 presidential vote by 2022 and 2024 lines; House Clerk 2024 statistics; McAllister order May 20, 2022."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card_v2 import said_vs_record
said_vs_record(
    title="No Court Has Found NY-23 to Be a Gerrymander. His “Fair Maps” Claim Holds Up.",
    said_items=[("when the courts put fair maps on the table, that we ran on", "Interview, Erie News Now via WZMQ, June 15, 2026"),
                ("a gerrymander that’s led to them taking two seats", "Same interview, on the Legislature’s 2024 map")],
    record_points=[("Trump +17", "NY-23 on the 2022 court map, drawn without regard to incumbents’ homes (2020 vote). Today’s lines are a point redder."),
                   ("1 of 3", "Seats Democrats gained in 2024 that the new map moved meaningfully. There the shift was 3.9 points; the Democrat won by 9.1.")],
    fair_line="The 2024 map did move two districts, NY-3 and NY-22, toward Democrats, and Democrats won both.",
    verdict="MOSTLY TRUE", favor_tag="HELD UP",
    sources="Sources: Harkenrider v. Hochul (2022); Census district files; The Downballot; House Clerk 2024 results",
    url="langworthywatch.org/fact-checks/2026-11-13-who-drew-ny23-redistricting/",
    kicker="WHAT HE SAID / THE RECORD",
    path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "who_drew_ny23_card.png"))
