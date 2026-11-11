#!/usr/bin/env python3
"""Baseline for the term tracker: Rep. Langworthy (L000600) in the 119th Congress, H.R. bills only.
Reads govinfo BILLSTATUS bulk XML (research/sources/ec-record-2026-10/bills/bulk/x-hr/, retrieved Oct 2026).
Cosponsors are parsed from <cosponsors><item> (see the BILLSTATUS cosponsor-parsing note); withdrawn
cosponsorships are excluded."""
import glob, os, re, json, sys
SRC = sys.argv[1] if len(sys.argv) > 1 else "research/sources/ec-record-2026-10/bills/bulk/x-hr"
REFRESH = sys.argv[2] if len(sys.argv) > 2 else None   # newer files override same-named older ones
ME = "L000600"
def blk(t, tag):
    i = t.find(f"<{tag}>"); j = t.find(f"</{tag}>", i)
    return t[i:j] if i >= 0 and j > i else ""
sponsored, cosponsored = [], []
paths = {os.path.basename(f): f for f in glob.glob(os.path.join(SRC, "BILLSTATUS-119hr*.xml"))}
if REFRESH:
    for f in glob.glob(os.path.join(REFRESH, "BILLSTATUS-119hr*.xml")):
        if "<billStatus" in open(f, encoding="utf-8", errors="ignore").read(200):
            paths[os.path.basename(f)] = f
for f in paths.values():
    t = open(f, encoding="utf-8", errors="ignore").read()
    b = t[t.find("<bill>"):]
    sp = blk(b, "sponsors")
    sp_id = (re.search(r"<bioguideId>([^<]+)", sp) or [None, ""])[1]
    sp_party = (re.search(r"<party>([^<]+)", sp) or [None, ""])[1]
    num = (re.search(r"<number>(\d+)", b) or [None, "?"])[1]
    title = (re.search(r"<title>([^<]+)</title>\s*<titles>", b) or [None, ""])[1]  # own title precedes <titles>; earlier <title> tags belong to related bills
    cos = []
    for it in re.findall(r"<item>(.*?)</item>", blk(b, "cosponsors"), re.S):
        bid = (re.search(r"<bioguideId>([^<]+)", it) or [None, ""])[1]
        if not bid or re.search(r"<sponsorshipWithdrawnDate>\d", it):
            continue
        cos.append({"id": bid, "party": (re.search(r"<party>([^<]+)", it) or [None, ""])[1],
                    "orig": "True" in (re.search(r"<isOriginalCosponsor>([^<]+)", it) or [None, ""])[1]})
    laws = re.findall(r"<laws>.*?<number>([^<]+)</number>", b, re.S)
    rec = {"bill": f"H.R. {num}", "title": title[:90], "sponsor_party": sp_party, "n_cos": len(cos),
           "dem_cos": sum(c["party"] == "D" for c in cos), "dem_orig": sum(c["party"] == "D" and c["orig"] for c in cos),
           "law": bool(laws)}
    if sp_id == ME:
        sponsored.append(rec)
    elif any(c["id"] == ME for c in cos):
        rec["lw_orig"] = any(c["id"] == ME and c["orig"] for c in cos)
        cosponsored.append(rec)
S = len(sponsored); C = len(cosponsored)
out = {"sponsored": S,
       "sponsored_with_any_dem_cosponsor": sum(r["dem_cos"] > 0 for r in sponsored),
       "sponsored_with_dem_original_cosponsor": sum(r["dem_orig"] > 0 for r in sponsored),
       "sponsored_became_law": sum(r["law"] for r in sponsored),
       "cosponsored_total": C,
       "cosponsored_dem_sponsored": sum(r["sponsor_party"] == "D" for r in cosponsored),
       "cosponsored_rep_sponsored": sum(r["sponsor_party"] == "R" for r in cosponsored)}
print(json.dumps(out, indent=1))
print("-- sponsored with a Democratic cosponsor:")
for r in sorted(sponsored, key=lambda r: -r["dem_cos"]):
    if r["dem_cos"]: print(f'  {r["bill"]:10} D cos {r["dem_cos"]:>2} (orig {r["dem_orig"]}) law={r["law"]}  {r["title"]}')
print("-- Democrat-sponsored bills he cosponsored:")
for r in cosponsored:
    if r["sponsor_party"] == "D": print(f'  {r["bill"]:10} orig={r.get("lw_orig")} law={r["law"]}  {r["title"]}')
json.dump({"summary": out, "sponsored": sponsored, "cosponsored": cosponsored},
          open("research/term-tracker-2026-11/bipartisan_baseline.json", "w"), indent=1)
