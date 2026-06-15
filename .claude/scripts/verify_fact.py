#!/usr/bin/env python3
"""
verify_fact.py — deterministic primary-source verifier for LangworthyWatch.

Removes the model from the loop for the *scriptable* load-bearing facts — the
ones most prone to the "by elimination" shortcut or aggregator-trust error
(CLAUDE.md failure mode #5). Used by /claim-audit and /verify-fact.

Subcommands:
  rollcall <year> <num> <surname>           Read a House roll-call vote verbatim
  county <name> [name ...]                   Test NY-23 county membership
  cosponsor <congress> <type> <num> <name>   Check bill cosponsor membership

Examples:
  python verify_fact.py rollcall 2025 145 Langworthy
  python verify_fact.py county Yates Schuyler "Erie County" Wyoming
  python verify_fact.py cosponsor 119 hr 2598 Langworthy

No third-party deps (urllib + xml.etree). A browser User-Agent is sent because
clerk.house.gov and congress.gov 403 non-browser fetches; clerk evs XML and
govinfo BULKDATA respond fine to it. Exit code 0 = lookup succeeded, 1 = a
checkable claim failed (vote/member/county not as asserted), 2 = fetch/parse error.
"""
import sys
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36")


def fetch(url, timeout=45):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


# ---------------------------------------------------------------- rollcall ----
def cmd_rollcall(args):
    if len(args) < 3:
        print("usage: rollcall <year> <num> <surname>", file=sys.stderr)
        return 2
    year, num, surname = args[0], int(args[1]), args[2]
    url = f"https://clerk.house.gov/evs/{year}/roll{num:03d}.xml"
    try:
        root = ET.fromstring(fetch(url))
    except (urllib.error.URLError, ET.ParseError, OSError) as e:
        print(f"ERROR fetching/parsing {url}: {e}", file=sys.stderr)
        return 2

    meta = root.find("vote-metadata")
    def m(tag):
        el = meta.find(tag) if meta is not None else None
        return el.text.strip() if el is not None and el.text else "?"

    print(f"  source:        {url}")
    print(f"  measure:       {m('legis-num')}")
    print(f"  question:      {m('vote-question')}")
    print(f"  description:   {m('vote-desc')}")
    print(f"  result:        {m('vote-result')}")
    print(f"  date:          {m('action-date')}")

    hits = []
    for rv in root.iter("recorded-vote"):
        leg = rv.find("legislator")
        vote = rv.find("vote")
        if leg is None or vote is None:
            continue
        name = (leg.get("unaccented-name") or leg.get("sort-field")
                or (leg.text or "")).strip()
        if surname.lower() in name.lower():
            hits.append((name, leg.get("state", "?"), leg.get("party", "?"),
                         (vote.text or "?").strip()))
    if not hits:
        print(f"  VOTE:          {surname} NOT FOUND in roll {num}")
        return 1
    for name, st, party, v in hits:
        print(f"  VOTE:          {name} ({party}-{st}) = {v}")
    return 0


# ------------------------------------------------------------------ county ----
# Canonical NY-23 (119th Congress) county tagging set. See
# .claude/references/ny23-landmines.md for the partial/edge nuance.
NY23_WHOLE = {"chemung", "allegany", "cattaraugus", "chautauqua", "tioga"}
NY23_PARTIAL = {"erie", "schuyler", "steuben"}        # partial — count, but note
NY23_EDGE = {"niagara"}                                # small sliver — VERIFY
NOT_NY23 = {"yates", "wyoming", "seneca", "ontario", "tompkins", "cortland",
            "broome", "monroe", "livingston", "genesee", "orleans", "wayne"}


def _norm_county(name):
    n = name.strip().lower()
    for suffix in (" county", " co.", " co"):
        if n.endswith(suffix):
            n = n[: -len(suffix)]
    return n.strip()


def cmd_county(args):
    if not args:
        print("usage: county <name> [name ...]", file=sys.stderr)
        return 2
    bad = False
    for raw in args:
        c = _norm_county(raw)
        if c in NY23_WHOLE:
            verdict = "IN NY-23 (whole county)"
        elif c in NY23_PARTIAL:
            verdict = "IN NY-23 (PARTIAL — only part of the county is NY-23)"
        elif c in NY23_EDGE:
            verdict = "EDGE — small NY-23 sliver; VERIFY before asserting"
        elif c in NOT_NY23:
            verdict = "NOT IN NY-23  <-- trap"
            bad = True
        else:
            verdict = "UNKNOWN — not in canonical lists; verify manually"
            bad = True
        print(f"  {raw:<18} -> {verdict}")
    return 1 if bad else 0


# --------------------------------------------------------------- cosponsor ----
def cmd_cosponsor(args):
    if len(args) < 4:
        print("usage: cosponsor <congress> <billtype> <num> <surname>", file=sys.stderr)
        return 2
    congress, btype, num, surname = args[0], args[1].lower(), args[2], args[3]
    url = (f"https://www.govinfo.gov/bulkdata/BILLSTATUS/"
           f"{congress}/{btype}/BILLSTATUS-{congress}{btype}{num}.xml")
    try:
        root = ET.fromstring(fetch(url))
    except (urllib.error.URLError, ET.ParseError, OSError) as e:
        print(f"ERROR fetching/parsing {url}: {e}", file=sys.stderr)
        return 2

    print(f"  source:        {url}")
    sponsor = root.find(".//sponsors/item/fullName")
    if sponsor is not None and sponsor.text:
        print(f"  sponsor:       {sponsor.text.strip()}")

    names = []
    for item in root.iter("item"):
        full = item.find("fullName")
        last = item.find("lastName")
        # cosponsor items carry a sponsorshipDate; that disambiguates from sponsors
        if item.find("sponsorshipDate") is not None and full is not None and full.text:
            names.append((full.text.strip(), (last.text or "").strip() if last is not None else ""))

    print(f"  cosponsors:    {len(names)} found")
    matched = [f for f, l in names
               if surname.lower() in f.lower() or surname.lower() == l.lower()]
    if matched:
        for f in matched:
            print(f"  MATCH:         {f}  -> IS a cosponsor")
        return 0
    spon_txt = sponsor.text if (sponsor is not None and sponsor.text) else ""
    if surname.lower() in spon_txt.lower():
        print(f"  NOTE:          {surname} is the SPONSOR (not in cosponsor list)")
        return 0
    print(f"  RESULT:        {surname} is NOT a cosponsor of {btype.upper()} {num} "
          f"({congress}th)  <-- do not assert cosponsorship")
    return 1


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    cmd, rest = sys.argv[1], sys.argv[2:]
    dispatch = {"rollcall": cmd_rollcall, "county": cmd_county, "cosponsor": cmd_cosponsor}
    if cmd not in dispatch:
        print(f"unknown subcommand: {cmd}\n", file=sys.stderr)
        print(__doc__, file=sys.stderr)
        return 2
    return dispatch[cmd](rest)


if __name__ == "__main__":
    sys.exit(main())
