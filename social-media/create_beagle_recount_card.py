#!/usr/bin/env python3
"""Beagle posts recount (v2 template A), Nov 15, 2026. Counts from research/sources/beagle-posts-recount-2026-11-15/ledger.csv:
39 posts May 3 to about Nov 10; 28 from May 3 to June 29. Silence finding from the July 2 automated text sweep in the entry.
Replaces the count of 30 used in the July 2 post (beagle_count_contrast_post.md), which mixed in press releases and a survey."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card_v2 import one_number
one_number(
    number="39",
    unit_line="beagle and animal-testing posts on Rep. Langworthy's official Facebook page since May 3.",
    sentence="28 came in the first eight weeks. In that time, a sweep of his page's post text found none mentioning the Essential Plan or Medicaid.",
    context="About 450,000 New Yorkers lost Essential Plan coverage on July 1; the state attributes it to H.R. 1, which he voted for. Recounted Nov. 15, 2026 from captures of each post, replacing our earlier count of 30.",
    tag_label="DOCUMENTED PATTERN",
    sources="Sources: his official Facebook page, captured Nov. 15, 2026; NY Department of Health; House Clerk",
    url="langworthywatch.org/fact-checks/2026-05-22-beagle-posts-credit-claiming-distraction/",
    kicker="RECOUNT",
    path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "beagle_recount_card.png"))
