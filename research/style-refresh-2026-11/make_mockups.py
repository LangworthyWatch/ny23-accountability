#!/usr/bin/env python3
"""Style-refresh mockups (Nov 11, 2026): the three v2 templates with this week's material."""
import os, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
sys.path.insert(0, os.path.join(ROOT, "social-media"))
from lib.card_v2 import one_number, said_vs_record, weekly_roundup
OUT = os.path.dirname(os.path.abspath(__file__))

one_number(
    number="46 of 47",
    unit_line="House votes he cast from July 22 through November 10, 2026.",
    sentence="His one miss in that stretch was a September 14 roll call.",
    context="Through July 21, his record showed 66 misses in 1,875 votes, more than half of them in one quarter of 2024.",
    tag_label="IN HIS FAVOR", favor=True,
    sources="Source: House Clerk roll calls 273 to 319 (2026); missed-votes page",
    url="langworthywatch.org/missed-votes/",
    kicker="THE RECORD", path=os.path.join(OUT, "mock-A-one-number.png"), dots=(46, 47))

said_vs_record(
    title="Since November 10, No One Can Comment on His Facebook Posts Except People a Post Tags",
    said_items=[("please don't ever hesitate to reach out.", "Casework graphic, official Facebook page, November 9, 2026"),
                ("Send me an email or sign up for my newsletter at Langworthy.house.gov.", "Official Facebook page bio, as of November 11, 2026")],
    record_points=[("Nov. 10", "Commenting limited on both of his pages, followers included. Seven of seven recent posts checked."),
                   ("0", "In-person public town halls found since he took office in January 2023.")],
    fair_line="Phones and an email form still work, through five offices. Pages often limit comments, and the setting applies to everyone alike.",
    verdict="DOCUMENTED PATTERN",
    sources="Sources: his Facebook pages, Nov. 11, 2026; langworthy.house.gov; WSKG, April 2025",
    url="langworthywatch.org/fact-checks/2026-10-16-who-funds-him-and-who-can-reach-him/",
    kicker="WHAT HE SAID / THE RECORD", path=os.path.join(OUT, "mock-B-said-vs-record.png"))

weekly_roundup(
    week_label="Week of November 9, 2026",
    rows=[("Votes", "5 of 5", "Cast every roll call. Voted to send the Hegseth impeachment resolution to committee (211 to 204) and for two nuclear-energy bills."),
          ("His pages", "Nov. 10", "Commenting closed on both his Facebook pages to everyone except people a post tags."),
          ("What we checked", "1 update", "Who can reach him: the comment limits, his five office phone numbers, and the email form's address check.")],
    held_up=("IN HIS FAVOR", "46 of 47", "Votes cast since July 22. His only miss was September 14."),
    sources="Sources: House Clerk roll calls 315 to 319; his Facebook pages; langworthy.house.gov",
    url="langworthywatch.org/fact-checks/",
    path=os.path.join(OUT, "mock-C-weekly-roundup.png"))
