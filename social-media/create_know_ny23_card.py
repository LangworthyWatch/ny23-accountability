#!/usr/bin/env python3
"""Know NY-23 profile card (v2 template A). District-wide figures on current (119th Congress) lines, ACS 2025 1-year:
B19055 (households with Social Security: 39.7% NY-23, 33.0% NY, 32.9% US), B19065/B19025 (Social Security share of
aggregate household income: 10.5%, 6.3%, 7.2%), B09020/B01003 (65+: 23.8%; NY-3 statistically tied), C27006 (Medicare 25.1%).
Reproduced by research/sources/know-ny23-2026-11-14/acs_profile.py and acs_income_sources.py.
Rebuilt Nov 14, 2026 after audit: the first version led with a BEA figure (30%) that covers only the five whole counties,
about half the district, and counts Medicare and Medicaid payments for care as income."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card_v2 import one_number
one_number(
    number="2 in 5",
    unit_line="households in NY-23 receive Social Security. In New York State and the nation, it is 1 in 3.",
    sentence="Social Security supplies 10.5% of all household income in the district, against 6.3% statewide and 7.2% nationally.",
    context="One resident in four is 65 or older, the highest estimate among New York's 26 districts (NY-3 is statistically tied). One in four has Medicare. Figures are for 2025, on the district's current lines.",
    tag_label="DISTRICT PROFILE",
    sources="Sources: Census Bureau, 2025 American Community Survey 1-year estimates, 119th Congress districts",
    url="langworthywatch.org/know-ny23/",
    kicker="KNOW NY-23",
    path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "know_ny23_card.png"))
