#!/usr/bin/env python3
"""Rikers detainer v2, Nov 20, 2026: timeline version. Entry 2026-11-19-rikers-detainer-hochul (FALSE ATTRIBUTION).
2014 = Local Law 58 (Admin Code 9-131); 2018 = Wells v. DeMarco (2d Dept, Nov 14, 2018); Hochul took office Aug 2021;
2026 law = S.9005-C, GML art. 19-D sec. 996(5) excludes local correctional facilities. NY Post (Fox News) says NYC DOC
declined the detainer. The man is not named; the charges-vs-convictions point is in the caption, not the card."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card_v2 import said_vs_record
said_vs_record(
    title="He Blamed Gov. Hochul for a Rikers Release. The Rules Rikers Followed Predate Her.",
    said_items=[("the infuriating consequence of NYS\u2019s sanctuary policies", "Official Facebook page, November 17, 2026"),
                ("because Hochul won\u2019t allow law enforcement to cooperate with ICE detainers", "Same post")],
    record_points=[("2014", "New York City law: its jails may hold someone for ICE only with a judge\u2019s warrant and a violent or serious conviction."),
                   ("2018", "A state appeals court barred holds on civil immigration detainers alone."),
                   ("2021", "Hochul took office. The 2026 law she signed leaves local jails out of its detainer rules.")],
    fair_line="Her 2026 law does limit local cooperation with ICE: it bans 287(g) agreements.",
    verdict="FALSE ATTRIBUTION",
    sources="Sources: NYC Admin. Code \u00a79-131; Wells v. DeMarco (2018); S.9005-C (2026); NY Post/Fox News",
    url="langworthywatch.org/fact-checks/2026-11-19-rikers-detainer-hochul/",
    kicker="WHAT HE SAID / THE RECORD",
    path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "rikers_detainer_card_v2.png"))
