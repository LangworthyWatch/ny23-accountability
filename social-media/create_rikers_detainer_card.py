#!/usr/bin/env python3
"""Rikers detainer, Nov 20, 2026. Entry 2026-11-19-rikers-detainer-hochul (FALSE ATTRIBUTION).
Template B. His Nov 17 official-page post against: the NY Post's own line that the NYC Department of
Correction declined the detainer; NYC Admin Code 9-131 (Local Law 58 of 2014) as summarized in
U.S. v. City of New York (E.D.N.Y. Oct 15, 2026): judicial warrant AND conviction for a violent or
serious crime; DHS release lists arrests and charges only; the 2026 state law's municipal detainer rules
exclude local correctional facilities (S.9005-C, GML art. 19-D, sec. 996(5)).
Fair strip: Wells v. DeMarco (2d Dept 2018); 287(g) ban (S.9005-C Part LL Subpart A). The man is not named."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card_v2 import said_vs_record
said_vs_record(
    title="He Blamed Gov. Hochul for a Rikers Release. Rikers Is a City Jail, Bound by a 2014 City Law.",
    said_items=[("an attempted murderer with multiple violent felonies", "Official Facebook page, November 17, 2026"),
                ("freely roaming the streets because Hochul won’t allow law enforcement to cooperate with ICE detainers", "Same post")],
    record_points=[("CITY LAW", "The city’s jail system declined the detainer. City law requires a judge’s warrant and a violent or serious conviction."),
                   ("JAILS LEFT OUT", "The 2026 state law Hochul signed leaves local jails out of its detainer rules."),
                   ("CHARGED", "DHS lists arrests and charges for the man, not convictions.")],
    fair_line="New York does limit cooperation with ICE: a 2018 state court ruling bars holds on civil detainers alone, and Hochul’s 2026 law bans 287(g) agreements.",
    verdict="FALSE ATTRIBUTION",
    sources="Sources: NYC Admin. Code §9-131; U.S. v. City of New York (E.D.N.Y. 2026); DHS; S.9005-C",
    url="langworthywatch.org/fact-checks/2026-11-19-rikers-detainer-hochul/",
    kicker="WHAT HE SAID / THE RECORD",
    path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "rikers_detainer_card.png"))
