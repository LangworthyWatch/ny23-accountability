---
name: fec-donor-scan
description: Query the local FEC DuckDB index to resolve a donor name or committee into (recipient committee × cycle × amount) rollups, enumerate committees by treasurer/connected-org, or PROFILE a donor's partisan split + temporal (back-the-winner) hedge. For LangworthyWatch, this is the canonical way to answer "what PACs gave to Langworthy?" or "is donor X giving to a sector that overlaps with bill Y's endorser coalition?" Use when the user says "FEC scan [name]", "who did [name] donate to?", "check FEC for [name]", "donor rollup [name]", "what committees does [treasurer] run?", or any time you need cycle-level personal/entity giving rather than issuing a 3-8 min grep across indiv{20..26}.txt. Uses ~/data/public-ledger/federal/fec/fec_index.duckdb (209M rows, indiv20/22/24/26 + committee + candidate masters); falls back to grep with a warning if missing.
---

# FEC Donor Scan

Fast donor + committee lookup against the pre-built FEC **DuckDB** index at
`~/data/public-ledger/federal/fec/fec_index.duckdb` (15.8 GB, ~209M individual
contributions across cycles 2020/2022/2024/2026, plus committee and candidate
masters). Sub-second columnar scans replace the ad-hoc 3–8 min grep pattern.

> **⚠️ Ported from public-ledger 2026-06-08.** The index lives in the shared
> `~/data/public-ledger/` depot regardless of which project invokes it.

> **⚠️ Cycle-coding silent-zero trap.** `fec_cycle` holds `20/22/24/26`, not
> `2020/2022/2024/2026`. A query like `WHERE fec_cycle IN (2024, 2026)` returns
> **zero rows with no error**. Always write `fec_cycle IN (24, 26)`; display the
> 4-digit year in output tables but query with the 2-digit code.

> **⚠️ Direction trap (LangworthyWatch-specific, validated 2026-06-07).** The
> FEC `pas2` schema's `cmte_id` (column 0) is the **filer / contributor**, not
> the recipient. To find PACs giving TO Langworthy, filter on
> `other_id IN ('C00817932','C00832188')` OR `cand_id = 'H2NY23228'`. Filtering
> by Langworthy's committee IDs alone finds outgoing transfers from the JFC,
> not incoming PAC contributions. The June 2026 SECURE Data Act fact-check
> shipped with a wrong "$0" donor finding because of this — the correction
> ($270,500 from 21 endorser-coalition PACs) was pushed after the bug was caught.

## Langworthy-specific reference

| Identifier | Value |
|---|---|
| Candidate ID | `H2NY23228` |
| Principal campaign cmte (LfC) | `C00817932` |
| JFC (LCVC) | `C00832188` |

Sub-second queries for:
- "What did X give, to whom, when, how much?" (donor rollup)
- "Who contributed to Langworthy in cycle 2024?" (incoming PAC sweep)
- "What sectors of the [Bill X] endorser coalition donate to Langworthy?" (sector overlap)
- "Everyone named Y in city Z cycle 2024" (disambiguation)
- "All committees where Z is treasurer" (treasurer/connected-org enumeration)

---

## Arguments

`$ARGUMENTS` is a free-text query. Typical forms:
- `"Folkman, Zachary"` — exact name lookup
- `"Chase Herro" Puerto Rico` — name + state disambiguator
- `"MANZANITA MANAGEMENT"` — LLC entity lookup
- `cmte C00817932 2024 top30` — top donors to Langworthy's principal cmte
- `langworthy incoming sector telecom` — sector-tagged incoming PAC sweep
- `treasurer "Crate, Bradley"` — all committees by treasurer name

Default behavior when no disambiguator is given: show the top 30 rows by
amount, rolled up by `(donor_name_norm, state, fec_cycle)`.

---

## Step 0 — Check the index exists

```bash
DB=~/data/public-ledger/federal/fec/fec_index.duckdb
if [[ ! -s "$DB" ]]; then
    echo "FEC DuckDB index missing. Build with:"
    echo "  cd ~/projects/public-ledger && python3 scripts/etl/build_fec_duckdb_index.py"
    echo "Falling back to grep (slow: 3-8 min per file)."
fi
```

If the index is missing, fall back to `grep` on the bulk pipe-delimited files
at `~/data/public-ledger/federal/fec/indiv{20,22,24,26}.txt` and
`pas2{24,26}.txt` — but warn the user the scan will take 3-8 min per cycle.

## Step 0.5 — How to run a query

No `duckdb` CLI is installed; use the Python module. Pattern:

```bash
python3 - <<'PY'
import os, duckdb
con = duckdb.connect(os.path.expanduser('~/data/public-ledger/federal/fec/fec_index.duckdb'), read_only=True)
q = """<SQL HERE>"""
for row in con.execute(q).fetchall():
    print(row)
con.close()
PY
```

Read-only always. Never INSERT/UPDATE/CREATE against the index via this skill.

---

## Step 1 — Normalize the query

Normalize the name the same way the index did (lowercase, strip non-alphanumerics):

```python
import re
def norm(s): return re.sub(r'[^a-z0-9]', '', s.lower())
```

FEC raw names are `LAST, FIRST MIDDLE`. `donor_name_norm` is the stripped form of
the whole raw string, so for a person query normalize `"Crate, Bradley"` →
`cratebradley` and match with a prefix (`donor_name_norm LIKE 'cratebradley%'`).
For LLC entity names, normalize the full string and prefix-match.

---

## Step 2 — Query patterns

### Incoming PAC contributions to Langworthy (LW-specific, MOST COMMON)

```sql
WITH incoming AS (
  SELECT cmte_id AS contrib_cmte_id, transaction_amt, transaction_dt
  FROM committee_to_candidate    -- pas2 table in the DuckDB index
  WHERE recipient_cmte_id IN ('C00817932','C00832188')
     OR recipient_cand_id = 'H2NY23228'
)
SELECT cm.cmte_nm,
       SUM(i.transaction_amt) AS total,
       COUNT(*)               AS n_tx
FROM incoming i
LEFT JOIN committees cm ON cm.cmte_id = i.contrib_cmte_id
GROUP BY cm.cmte_nm
ORDER BY total DESC
LIMIT 30;
```

If the DuckDB schema field names differ (older builds), use the raw bulk pas2
files directly — see the validated script at
`/tmp/bigtech_donor_scan.py` (referenced in the SECURE Data Act fact-check
commit `a69f3de`) for the working pattern.

### Donor rollup (most common for non-LW queries)

```sql
SELECT c.fec_cycle, c.cmte_id, cm.cmte_nm,
       SUM(c.transaction_amt)            AS total_dollars,
       COUNT(*)                          AS n_tx,
       MIN(c.transaction_dt)             AS first_dt,
       MAX(c.transaction_dt)             AS last_dt
FROM individual_contributions c
LEFT JOIN committees cm
       ON cm.cmte_id = c.cmte_id AND cm.fec_cycle = c.fec_cycle
WHERE c.donor_name_norm LIKE 'cratebradley%'
GROUP BY c.fec_cycle, c.cmte_id, cm.cmte_nm
ORDER BY total_dollars DESC
LIMIT 30;
```

### Sector overlap (LW-specific — endorser-coalition cross-check)

When a fact-check involves a bill or initiative with an industry endorser
coalition, cross-reference the coalition members against Langworthy's
incoming PAC list. The 2026-06-06 SECURE Data Act entry is the canonical
example — see its donor section for the sector breakdown format
(`telecom $121K / retail $77K / oil-energy $61K / Big Tech direct $3.5K`).

Pattern: get the coalition member list (often from the U.S. Chamber's support
letter), then filter `committees.cmte_nm` with `UPPER(cmte_nm) LIKE` clauses
against each member name. Tag matches by sector by hand.

---

## Step 3 — Output format

Always output one `## Summary` table (top rollup) followed by any anomalies
worth flagging. Amounts in the DuckDB index are **already in dollars** — print
them as-is.

Example for an LW donor-overlap query:

```
## FEC Donor Scan: SECURE Data Act coalition → Langworthy

| Cycle | PAC | Total | N Tx | Sector |
|-------|-----|-------|------|--------|
| 24+26 | CHARTER COMMUNICATIONS PAC | $35,000 | 12 | Telecom/Cable (NCTA) |
| 24+26 | NCTA PAC | $13,000 | 6 | Telecom trade association |
| ...  | ... | ... | ... | ... |

Anomalies / flags:
- 21 of the 57 endorser orgs have a PAC giving to Langworthy
- $0 from Meta/Amazon/Microsoft/Apple corporate PACs (Big Tech direct)
- Google NETPAC: $2K (2023, pre-bill)
```

---

## Step 4 — Cross-link to existing LangworthyWatch entries

After producing the rollup, grep `content/fact-checks/_index.md` and any
existing fact-checks for the committee IDs or PAC names that appeared:

```bash
cd langworthy-tracker
grep -l "CHARTER COMMUNICATIONS\|NCTA\|Comcast" content/fact-checks/*.md | head -5
```

Flag cross-references explicitly in the summary. The 2026-02-state-preemption-pattern
entry and 2026-06-06-langworthy-secure-data-act-hr8413 entry are the most
recent donor-pattern-relevant entries.

---

## When NOT to use

- **Schedule B disbursements / operating expenditures** — the indiv index
  holds *individual contributions only*. For Schedule B use the OpenFEC API
  (`api.open.fec.gov/v1/schedules/schedule_b/`) or download bulk
  `oth{cycle}.txt` files (only `oth26.txt` is currently in the depot).
- OpenFEC itemized filings with amendments — the bulk files are point-in-time
  snapshots; use OpenFEC for amendment-aware reads.
- Historical pre-2020 cycles — not in this index (older bulk has different
  column layout).

---

## Rules

- Amounts in the DuckDB index are **already in dollars** — do NOT divide by 100.
- `fec_cycle` is **two-digit** (`20/22/24/26`). `WHERE fec_cycle IN (2024, 2026)`
  returns **zero rows silently**.
- **For incoming PAC contributions to Langworthy, filter on `recipient_cmte_id`
  or `recipient_cand_id`, NOT on `cmte_id`** (which is the contributor).
- Always report amounts in actual dollars, never rounded.
- Always include N transactions and first/last dates for any rollup.
- Always report state and employer when looking up a person — they are the
  disambiguation lever for common names.
- Flag the **largest single transaction** separately when > $25K — that's
  often the newsworthy row, and rollups can hide it.
- Never INSERT/UPDATE against the index. Read-only (`read_only=True`).
