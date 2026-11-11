#!/usr/bin/env python3
"""Comments limited on both Facebook pages (update to 2026-10-16-who-funds-him-and-who-can-reach-him,
DOCUMENTED PATTERN). Pilot, v2 said-vs-record template."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card_v2 import said_vs_record
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
    kicker="WHAT HE SAID / THE RECORD",
    path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "comments_limited_card.png"))
