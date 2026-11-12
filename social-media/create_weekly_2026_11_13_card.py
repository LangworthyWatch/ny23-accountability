#!/usr/bin/env python3
"""Weekly roundup, week of Nov 9, 2026 (pilot week 1, v2 template). Votes from House Clerk rolls 315-321 (refreshed Nov 11);
refresh the votes row on Friday morning if the House votes again Nov 12-13."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card_v2 import weekly_roundup
weekly_roundup(
    week_label="Week of November 9, 2026",
    rows=[("Votes", "6 of 7", "Missed the Nov. 11 vote to force a floor vote on a veterans' pay bill he cosponsors (passed 245 to 175). Cast the other six."),
          ("His pages", "Nov. 10", "Commenting closed on both his Facebook pages to everyone except people a post tags."),
          ("What we checked", "1 update", "Who can reach him: the comment limits, his five office phone numbers, and the email form's address check.")],
    held_up=("IN HIS FAVOR", "47 of 49", "Votes cast since July 22. His two misses: Sept. 14 and Nov. 11."),
    sources="Sources: House Clerk roll calls 315 to 321, Discharge Petition 22; his Facebook pages; langworthy.house.gov",
    url="langworthywatch.org/fact-checks/",
    path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "weekly_2026_11_13_card.png"))
