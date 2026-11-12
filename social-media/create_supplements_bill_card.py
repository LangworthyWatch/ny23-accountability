#!/usr/bin/env python3
"""Supplements reel, Nov 12, 2026 update to entry 2026-02-state-preemption-pattern. Template B.
Verdict pill = the entry's rating of "safe, effective" (NOT SUPPORTED); the framework line is MISSING CONTEXT
in the entry and is named as such in the caption. Figures: H.R. 7366 IH text; FDA 101; Tucker et al. 2018
(CDPH, JAMA Netw Open, 776 products); LDA 2026 Q1-Q3 (12 clients); FEC (NPA PAC $5,000, Mar 26, 2026)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card_v2 import said_vs_record
said_vs_record(
    title="His Supplements Bill Overrides State Rules. It Adds No Federal Safety Check.",
    said_items=[("My bill creates a national regulatory framework versus a patchwork of bad laws.", "Official Facebook page, November 12, 2026"),
                ("ensure vitamins and supplements are safe, effective, accessible and affordable.", "Same post")],
    record_points=[("0", "Safety or effectiveness provisions in the bill. FDA still cannot approve supplements before sale."),
                   ("776", "Products marketed as supplements that FDA found had hidden drugs, 2007 to 2016. Most were sold for weight loss, muscle or sexual enhancement."),
                   ("12", "Groups that lobbied on the bill in 2026, including all four of its endorsers.")],
    fair_line="One national rule is a real policy goal, and the bill lets a state ask HHS to keep a stricter rule.",
    verdict="NOT SUPPORTED",
    sources="Sources: H.R. 7366 text; FDA; Congress.gov; Calif. Dept. of Public Health (JAMA Netw Open 2018); lobbying disclosures, 2026",
    url="langworthywatch.org/fact-checks/2026-02-state-preemption-pattern/",
    kicker="WHAT HE SAID / THE RECORD",
    path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "supplements_bill_card.png"))
