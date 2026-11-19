#!/usr/bin/env python3
"""Air traffic control, Nov 16, 2026. Entry 2026-11-16-air-traffic-control-lead-the-fight (MISSING CONTEXT).
Template B: his May 7, 2025 vow (Fox News Digital) and Nov 16, 2026 caption beside the record:
no ATC bill of his own (119th sponsored list, govinfo BILLSTATUS), no T&I or Appropriations seat,
two letters (Nov 25, 2024 caucus letter he co-led; May 23, 2025 Gillen letter, CHRG-119hhrg61463).
Fair strip: Aye on H.R. 1 (2025 roll 190, Sec. 40003 = $12.52B), Yea on H.R. 7148 ($4B F&E; 2026 rolls 45, 53),
Yea on ROTOR (S. 2503, 2026 roll 72, failed 264-133)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card_v2 import said_vs_record
said_vs_record(
    title="He Vowed to “Lead the Fight” to Fully Fund Air Traffic Control. He Has Introduced No Bill to Do It.",
    said_items=[("I will absolutely lead the fight… we have to frontload this process.", "Fox News Digital, May 7, 2025"),
                ("I have long called for wholesale upgrades.", "Official Facebook page, November 16, 2026")],
    record_points=[("0 BILLS", "of his own to fund or fix air traffic control. He sits on neither committee that writes FAA law or funding."),
                   ("2 LETTERS", "A 2024 caucus letter on FAA oversight, and a 2025 funding request that another member led.")],
    fair_line="He voted for the $12.5 billion in H.R. 1, the $4 billion in the 2026 spending law, and the ROTOR aviation safety bill, which failed by one vote.",
    verdict="MISSING CONTEXT",
    sources="Sources: House Clerk roll calls; govinfo bill status; P.L. 119-21; Fox News, May 7, 2025",
    url="langworthywatch.org/fact-checks/2026-11-16-air-traffic-control-lead-the-fight/",
    kicker="WHAT HE SAID / THE RECORD",
    path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "atc_lead_the_fight_card.png"))
