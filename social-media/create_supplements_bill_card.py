#!/usr/bin/env python3
"""Supplements reel, Nov 12, 2026 update to entry 2026-02-state-preemption-pattern. Template B, rebuilt Nov 12:
his "safe, effective" against FDA's own sentence (fda.gov "FDA 101: Dietary Supplements", archived 20261104022126),
plus the New York minors law (S5823C) the bill would preempt absent an HHS exemption (H.R. 7366 IH, new 343-1(c)(2)).
Verdict pill = the entry's rating of "safe, effective" (NOT SUPPORTED)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card_v2 import said_vs_record
said_vs_record(
    title="He Says His Bill Makes Supplements “Safe, Effective.” It Has No Safety or Effectiveness Provision.",
    said_items=[("common sense legislation to ensure vitamins and supplements are safe, effective, accessible and affordable.", "Official Facebook page, November 12, 2026, on H.R. 7366")],
    record_points=[("FDA", "“does NOT have the authority to approve dietary supplements for safety and effectiveness” before they are sold. The bill leaves that unchanged."),
                   ("NY LAW", "New York bans selling weight-loss and muscle-building supplements to minors. His bill would override it unless HHS grants New York an exemption.")],
    fair_line="One national rule is a real policy goal, and the bill lets a state ask HHS to keep a stricter rule.",
    verdict="NOT SUPPORTED",
    sources="Sources: H.R. 7366 text (GPO); FDA, “FDA 101: Dietary Supplements”; NY S5823C",
    url="langworthywatch.org/fact-checks/2026-02-state-preemption-pattern/",
    kicker="WHAT HE SAID / THE RECORD",
    path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "supplements_bill_card.png"))
