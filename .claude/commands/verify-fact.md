---
name: verify-fact
description: Deterministically verify a scriptable primary-source fact — a House roll-call vote, NY-23 county membership, or bill cosponsorship — instead of reasoning about it or trusting an aggregator. Trigger when the user asks "did Langworthy vote yes/no on roll call N", "is X a cosponsor of H.R. N", "is Yates / Wyoming in NY-23", "read roll call N verbatim", or whenever a draft makes a vote / county / cosponsor claim that needs confirming. Prefer this over "by elimination" reasoning and over GovTrack/billsponsor (CLAUDE.md failure mode #5).
---

# /verify-fact

Some load-bearing facts are *scriptable*, and those are exactly the ones that
get botched by shortcuts — "confirmed by elimination" for a roll call, an
aggregator for a cosponsor list, a guess for whether a county is in the
district. Run the script instead. It hits the primary source directly (clerk
evs XML, govinfo BILLSTATUS) with a browser User-Agent so the usual 403s don't
bite, and reports the answer verbatim.

```bash
python .claude/scripts/verify_fact.py <subcommand> ...
```

## Subcommands

**Roll-call vote** — reads the Clerk's recorded-vote table verbatim:
```bash
python .claude/scripts/verify_fact.py rollcall 2025 145 Langworthy
#   measure: H R 1 | question: On Passage | result: Passed | date: 22-May-2025
#   VOTE: Langworthy (R-NY) = Yea
```
Use this anywhere a draft says "voted Yes/No/Aye/Nay on Roll Call N." Never
write "by elimination" — read the member's row.

**NY-23 county membership** — tests against the canonical 8-county set and the
known traps:
```bash
python .claude/scripts/verify_fact.py county Yates Schuyler "Erie County" Wyoming
#   Yates -> NOT IN NY-23 <-- trap   |   Schuyler -> IN NY-23 (PARTIAL)
#   Erie  -> IN NY-23 (PARTIAL)      |   Wyoming  -> NOT IN NY-23 <-- trap
```
Use this for any "serves N NY-23 counties" / catchment / BOCES claim — a service
area that includes an NY-23 county is not the same as "all NY-23 counties."

**Bill cosponsorship** — checks the govinfo BILLSTATUS cosponsor roster:
```bash
python .claude/scripts/verify_fact.py cosponsor 119 hr 2598 Langworthy
#   cosponsors: 167 found | RESULT: Langworthy is NOT a cosponsor <-- don't assert
python .claude/scripts/verify_fact.py cosponsor 119 hr 2598 Lawler
#   MATCH: Rep. Lawler, Michael [R-NY-17] -> IS a cosponsor
```
Use this for any "X cosponsored / did not cosponsor H.R. N" claim. This is the
authoritative roster — not GovTrack, not "fits the pattern."

## Exit codes

`0` = lookup succeeded and the checkable claim holds (member voted / is a
cosponsor / county is in-district); `1` = the claim does NOT hold (not found /
not a cosponsor / county not in NY-23 — a trap); `2` = fetch or parse error.

## Notes

- congress.gov and clerk human pages 403 non-browser fetches; this script uses
  the evs XML and govinfo bulk endpoints, which respond. If clerk XML ever
  blocks, the Wayback `/evs/YYYY/rollNNN.xml` snapshot is a fallback.
- Extend the county lists or add subcommands in `.claude/scripts/verify_fact.py`
  as new scriptable facts come up.

## Related

- `/claim-audit` — calls this script for the scriptable joins in a draft.
- `/fact-check-review` — failure mode #5 (membership from aggregators) is exactly
  what `cosponsor` defends against.
- `.claude/references/ny23-landmines.md` — the county canon and roll-call pairs.
