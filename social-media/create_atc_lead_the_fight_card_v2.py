#!/usr/bin/env python3
"""Air traffic control v2, Nov 19, 2026. Entry 2026-11-16-air-traffic-control-lead-the-fight (MISSING CONTEXT).
Template B. Pairs his May 7, 2025 vow (Fox News Digital) with his own Nov 17, 2026 standard
("deserves constant attention, not just when tragedy strikes", Flight 5342 families event transcript)
against: no ATC bill of his own (119th sponsored list, govinfo BILLSTATUS); 1 of 455 House press releases
since Jan 3, 2023 about air traffic control (full-text scan of 454 through Oct 15, 2026, plus the Nov 19 gas-ban release).
Fair strip: Aye H.R. 1 (2025 roll 190), Yea FY2026 law (2026 rolls 45, 53), Yea ROTOR (2026 roll 72)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card_v2 import said_vs_record
said_vs_record(
    title="He Vowed to “Lead the Fight” to Fully Fund Air Traffic Control. 18 Months Later: No Bill.",
    said_items=[("I will absolutely lead the fight… we have to frontload this process.", "Fox News Digital, May 7, 2025"),
                ("deserves constant attention, not just when tragedy strikes", "On aviation safety, Capitol event, November 17, 2026")],
    record_points=[("0 BILLS", "of his own to fund or fix air traffic control. He sits on neither committee that writes FAA law or funding."),
                   ("1 OF 455", "of his House press releases since January 2023 is about air traffic control: a 2024 letter to the FAA.")],
    fair_line="He voted for the $12.5 billion in H.R. 1, the $4 billion in the 2026 spending law, and the ROTOR aviation safety bill, which failed by one vote.",
    verdict="MISSING CONTEXT",
    sources="Sources: House Clerk roll calls; govinfo bill status; his press releases; Fox News, May 7, 2025",
    url="langworthywatch.org/fact-checks/2026-11-16-air-traffic-control-lead-the-fight/",
    kicker="WHAT HE SAID / THE RECORD",
    path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "atc_lead_the_fight_card_v2.png"))
