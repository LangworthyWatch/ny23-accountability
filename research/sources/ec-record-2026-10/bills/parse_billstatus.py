#!/usr/bin/env python3
"""Parse govinfo BILLSTATUS bulk XML (119th Congress, House measures) for
Rep. Nick Langworthy (bioguide L000600): sponsored measures, E&C-referred
cosponsorships, and an E&C-wide comparison.

Usage: python3 -I parse_billstatus.py <bulk_dir> <out_dir>
Reads <bulk_dir>/x-{hr,hres,hjres,hconres}/*.xml. Writes CSV/JSON to <out_dir>.

Stage ladder (furthest reached), derived ONLY from BILLSTATUS fields:
  introduced < subcommittee hearing < subcommittee markup < full committee hearing
  < full committee markup < reported < passed House < passed Senate < enacted
(Hearing/markup come from <committees>/<activities>; floor stages from LoC
action codes 8000 / 17000 / 36000 plus action-text fallbacks.)
"""
import csv, glob, json, os, re, sys
import xml.etree.ElementTree as ET

BIO = "L000600"
EC = "hsif00"
STAGES = ["introduced", "subcommittee hearing", "subcommittee markup",
          "full committee hearing", "full committee markup", "reported",
          "passed House", "passed Senate", "enacted"]


def txt(e, p):
    v = e.findtext(p)
    return v.strip() if v else ""


def parse(path):
    b = ET.parse(path).getroot().find("bill")
    typ = txt(b, "type") or txt(b, "billType")
    num = txt(b, "number") or txt(b, "billNumber")
    rec = {
        "bill": f"{typ} {num}", "type": typ, "number": int(num),
        "title": txt(b, "title"), "introduced": txt(b, "introducedDate"),
        "updateDate": txt(b, "updateDate"),
        "sponsor": txt(b, "sponsors/item/bioguideId"),
        "sponsorName": txt(b, "sponsors/item/fullName"),
        "latestActionDate": txt(b, "latestAction/actionDate"),
        "latestAction": txt(b, "latestAction/text"),
        "policyArea": txt(b, "policyArea/name"),
    }
    # committees
    comms, ec_sub_acts, ec_full_acts, all_sub, all_full = [], [], [], [], []
    for c in b.findall("committees/item"):
        code = txt(c, "systemCode"); name = txt(c, "name")
        comms.append(f"{name} ({code})")
        fa = [(txt(a, "name").lower(), txt(a, "date")[:10]) for a in c.findall("activities/item")]
        all_full += [(code, *x) for x in fa]
        if code == EC:
            ec_full_acts += fa
        for s in c.findall("subcommittees/item"):
            sa = [(txt(a, "name").lower(), txt(a, "date")[:10], txt(s, "name")) for a in s.findall("activities/item")]
            all_sub += [(code, *x) for x in sa]
            if code == EC:
                ec_sub_acts += sa
    rec["committees"] = "; ".join(comms)
    rec["EC_referred"] = any(EC in x for x in comms)
    rec["EC_subcommittees"] = "; ".join(sorted({s for _, _, s in ec_sub_acts}))

    acts = []
    for a in b.findall("actions/item"):
        acts.append((txt(a, "actionDate"), txt(a, "actionCode"), txt(a, "text")))
    codes = {c for _, c, _ in acts}
    texts = " || ".join(t for _, _, t in acts)

    def stage_from(full, sub, use_floor=True):
        st = 0
        if any(n.startswith("hearings") for n, *_ in sub): st = max(st, 1)
        if any(n.startswith("markup") for n, *_ in sub): st = max(st, 2)
        if any(n.startswith("hearings") for n, _ in full): st = max(st, 3)
        if any(n.startswith("markup") for n, _ in full): st = max(st, 4)
        if any(n.startswith("reported") or n.startswith("discharged") for n, _ in full): st = max(st, 5)
        if use_floor:
            if "8000" in codes or re.search(r"Passed/agreed to in House|On passage Passed|On motion to suspend the rules and (pass|agree)[^|]*Agreed to", texts):
                st = max(st, 6)
            if "17000" in codes or re.search(r"Passed/agreed to in Senate|Passed Senate", texts):
                st = max(st, 7)
            if "36000" in codes or b.find("laws/item") is not None or re.search(r"Became Public Law", texts):
                st = max(st, 8)
        return st

    st = stage_from([(n, d) for _, n, d in all_full], [(n, d, s) for _, n, d, s in all_sub])
    rec["stage"] = STAGES[st]
    rec["stage_rank"] = st
    ec_st = stage_from(ec_full_acts, ec_sub_acts, use_floor=False)
    rec["EC_committee_stage"] = STAGES[ec_st] if rec["EC_referred"] else ""
    rec["EC_activities"] = "; ".join(f"{s or 'full'}:{n}:{d}" for n, d, s in
                                     [(n, d, None) for n, d in ec_full_acts] + list(ec_sub_acts))
    ecf = lambda acts, pre: any(n.startswith(pre) for n, *_ in acts)
    rec["f_EC_sub_hearing"] = ecf(ec_sub_acts, "hearings")
    rec["f_EC_sub_markup"] = ecf(ec_sub_acts, "markup")
    rec["f_EC_full_hearing"] = ecf(ec_full_acts, "hearings")
    rec["f_EC_full_markup"] = ecf(ec_full_acts, "markup")
    rec["f_EC_reported"] = ecf(ec_full_acts, "reported")
    rec["f_EC_discharged"] = ecf(ec_full_acts, "discharged")
    rec["f_passed_House"] = "8000" in codes
    rec["f_failed_House"] = "9000" in codes
    rec["f_passed_Senate"] = "17000" in codes
    rec["f_enacted"] = "36000" in codes or b.find("laws/item") is not None
    rec["reports"] = "; ".join(txt(r, "citation") for r in b.findall("committeeReports/committeeReport"))
    rec["laws"] = "; ".join(f"{txt(l,'type')} {txt(l,'number')}" for l in b.findall("laws/item"))
    rb = []
    for r in b.findall("relatedBills/item"):
        rels = "/".join(f"{txt(x,'type')} [{txt(x,'identifiedBy')}]" for x in r.findall("relationshipDetails/item"))
        rb.append(f"{txt(r,'type')} {txt(r,'number')} ({rels}) latest={txt(r,'latestAction/actionDate')} {txt(r,'latestAction/text')[:80]}")
    rec["relatedBills"] = " | ".join(rb)
    rec["incorporation_notes"] = " | ".join(f"{d}: {t}" for d, _, t in acts
                                            if re.search(r"incorporat|see also|similar provisions|text of (this|the) (bill|measure)", t, re.I))
    # cosponsors
    cos = None
    items = b.findall("cosponsors/item")
    rec["n_cosponsors"] = len(items)
    for it in items:
        if txt(it, "bioguideId") == BIO:
            cos = {"sponsorshipDate": txt(it, "sponsorshipDate"),
                   "isOriginalCosponsor": txt(it, "isOriginalCosponsor"),
                   "withdrawn": txt(it, "sponsorshipWithdrawnDate")}
    return rec, cos, acts


def main(bulk, out):
    recs = []
    for t in ["hr", "hres", "hjres", "hconres"]:
        for f in glob.glob(os.path.join(bulk, f"x-{t}", "*.xml")):
            rec, cos, acts = parse(f)
            rec["file"] = os.path.relpath(f, out)
            rec["_cos"] = cos
            rec["_acts"] = acts
            recs.append(rec)
    recs.sort(key=lambda r: (r["type"], r["number"]))
    fields = ["bill", "title", "introduced", "committees", "EC_referred", "EC_subcommittees",
              "EC_committee_stage", "stage", "latestActionDate", "latestAction", "f_EC_sub_hearing", "f_EC_sub_markup", "f_EC_full_markup", "f_EC_reported", "f_passed_House", "f_failed_House", "f_passed_Senate", "f_enacted", "reports", "laws",
              "relatedBills", "incorporation_notes", "n_cosponsors", "EC_activities", "updateDate", "file"]

    spons = [r for r in recs if r["sponsor"] == BIO]
    with open(os.path.join(out, "langworthy-sponsored-119.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore"); w.writeheader(); w.writerows(spons)
    with open(os.path.join(out, "langworthy-sponsored-119-actions.txt"), "w") as fh:
        for r in spons:
            fh.write(f"=== {r['bill']}: {r['title']}\n")
            for d, c, t in r["_acts"]:
                fh.write(f"  {d} [{c}] {t}\n")
            if r["relatedBills"]:
                fh.write(f"  RELATED: {r['relatedBills']}\n")
            fh.write("\n")

    cos_all = [r for r in recs if r["_cos"]]
    cfields = ["bill", "title", "sponsorName", "cosponsorDate", "original", "withdrawn"] + fields[2:]
    for r in cos_all:
        r["cosponsorDate"] = r["_cos"]["sponsorshipDate"]; r["original"] = r["_cos"]["isOriginalCosponsor"]
        r["withdrawn"] = r["_cos"]["withdrawn"]
    with open(os.path.join(out, "langworthy-cosponsored-119-all.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cfields, extrasaction="ignore"); w.writeheader(); w.writerows(cos_all)
    cos_ec = [r for r in cos_all if r["EC_referred"]]
    with open(os.path.join(out, "langworthy-cosponsored-119-EC.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cfields, extrasaction="ignore"); w.writeheader(); w.writerows(cos_ec)

    # E&C-wide comparison (H.R. bills only, and all House measure types)
    FL = ["f_EC_sub_hearing", "f_EC_sub_markup", "f_EC_full_hearing", "f_EC_full_markup",
          "f_EC_reported", "f_EC_discharged", "f_passed_House", "f_failed_House", "f_passed_Senate", "f_enacted"]

    def tally(rs):
        n = len(rs); out_ = {"n": n}
        for f in FL:
            out_[f] = sum(1 for r in rs if r[f])
        out_["EC_full_markup_or_reported_or_floor"] = sum(1 for r in rs if r["f_EC_full_markup"] or r["f_EC_reported"] or r["f_passed_House"] or r["f_failed_House"])
        return out_

    def tally_old(rs):
        n = len(rs); out_ = {"n": n}
        for i, s in enumerate(STAGES):
            out_[f">= {s}"] = sum(1 for r in rs if r["stage_rank"] >= i)
        out_[">= EC full committee markup"] = sum(1 for r in rs if STAGES.index(r["EC_committee_stage"] or "introduced") >= 4)
        out_[">= EC reported"] = sum(1 for r in rs if STAGES.index(r["EC_committee_stage"] or "introduced") >= 5)
        return out_
    ec_hr = [r for r in recs if r["EC_referred"] and r["type"] == "HR"]
    ec_all = [r for r in recs if r["EC_referred"]]
    summary = {
        "snapshot_note": "govinfo BILLSTATUS bulk zips, listing lastModified 16-Oct-2026 (hr 13:37, hres 13:39, hjres 13:34, hconres 08:42; govinfo listing time zone not stated); downloaded 2026-10-16 16:14 UTC",
        "max_updateDate_in_data": max(r["updateDate"] for r in recs),
        "n_measures_parsed": len(recs),
        "langworthy_sponsored": tally(spons),
        "langworthy_sponsored_EC": tally([r for r in spons if r["EC_referred"]]),
        "langworthy_cosponsored_all": tally(cos_all),
        "langworthy_cosponsored_EC": tally(cos_ec),
        "langworthy_cosponsored_EC_withdrawn": sum(1 for r in cos_ec if r["withdrawn"]),
        "langworthy_cosponsored_EC_original": sum(1 for r in cos_ec if r["original"] == "True"),
        "all_EC_referred_HR": tally(ec_hr),
        "all_EC_referred_House_measures": tally(ec_all),
        "all_HR": tally([r for r in recs if r["type"] == "HR"]),
    }
    with open(os.path.join(out, "summary-counts.json"), "w") as fh:
        json.dump(summary, fh, indent=2)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
