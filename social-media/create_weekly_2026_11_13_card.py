#!/usr/bin/env python3
"""Weekly roundup, week of Nov 9, 2026 (pilot week 1, v2 template). Votes from House Clerk rolls 315-319;
refresh the votes row on Friday morning if the House votes again Nov 12-13."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card_v2 import weekly_roundup
weekly_roundup(
    week_label="Week of November 9, 2026",
    rows=[("Votes", "5 of 5", "Cast every roll call. Voted to send the Hegseth impeachment resolution to committee (211 to 204) and for two nuclear-energy bills."),
          ("His pages", "Nov. 10", "Commenting closed on both his Facebook pages to everyone except people a post tags."),
          ("What we checked", "1 update", "Who can reach him: the comment limits, his five office phone numbers, and the email form's address check.")],
    held_up=("IN HIS FAVOR", "46 of 47", "Votes cast since July 22. His only miss was September 14."),
    sources="Sources: House Clerk roll calls 315 to 319; his Facebook pages; langworthy.house.gov",
    url="langworthywatch.org/fact-checks/",
    path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "weekly_2026_11_13_card.png"))
