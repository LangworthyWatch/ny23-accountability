#!/usr/bin/env python3
"""Workforce Pell claim, entry 2026-11-11-workforce-pell-claim (MOSTLY TRUE). Pilot week 1, template B with
a HELD UP tag. Figures: P.L. 119-21 Sec. 83002; 20 U.S.C. 1088(b)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card_v2 import said_vs_record
said_vs_record(
    title="Pell Grants Now Cover 8-to-14-Week Training Programs. His Post Holds Up.",
    said_items=[("House Republicans expanded Pell Grants to cover approved 8–14 week training programs.", "Official Facebook page, October 27, 2026"),
                ("it used to be only associates", "Same post, spoken, in a conversation on a warehouse floor")],
    record_points=[("8 to 14 weeks", "The July 2025 law opened Pell to programs of 150 to 599 clock hours, approved by the governor and the Education Department, starting July 1, 2026."),
                   ("600+ hours", "Training programs this long were already Pell-eligible, with no degree required. The spoken line overstates what changed.")],
    fair_line="The written claim is precise and the change is real. He voted for it twice. One offhand spoken line overstates it.",
    fair_label="THE ONE CATCH",
    verdict="MOSTLY TRUE", favor_tag="HELD UP",
    sources="Sources: P.L. 119-21, Sec. 83002; 20 U.S.C. 1088(b); House Roll Calls 145 and 190 (2025)",
    url="langworthywatch.org/fact-checks/2026-11-11-workforce-pell-claim/",
    kicker="WHAT HE SAID / THE RECORD",
    path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "workforce_pell_card.png"))
