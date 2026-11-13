#!/usr/bin/env python3
"""Weekly roundup, week of Nov 9, 2026 (pilot week 1, v2 template). Votes from House Clerk rolls 315-323 (refreshed Nov 13, after the Nov 12 Star Act rule and passage votes)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card_v2 import weekly_roundup
weekly_roundup(
    week_label="Week of November 9, 2026",
    rows=[("Votes", "8 of 9", "Missed one: the Nov. 11 motion to force a floor vote on the Major Richard Star Act, a veterans' pay bill he cosponsors."),
          ("Star Act, Nov. 12", "No / Yes", "No on the rule bringing it to the floor (passed 271 to 135). Yes on the bill itself (passed 392 to 18)."),
          ("His pages", "Nov. 10", "Commenting closed on both his Facebook pages to everyone except people a post tags.")],
    held_up=("HELD UP", "2 claims", "Pell now covers approved 8-to-14-week training, and his Olean and Ellicottville fire-grant credit. Both MOSTLY TRUE."),
    sources="Sources: House Clerk roll calls 315 to 323, Discharge Petition 22; his Facebook pages; P.L. 119-21",
    url="langworthywatch.org/fact-checks/",
    path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "weekly_2026_11_13_card.png"))
