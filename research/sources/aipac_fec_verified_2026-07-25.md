# AIPAC / pro-Israel money to Langworthy — verified FEC pull

**Pulled:** 2026-07-25
**Status:** money side VERIFIED against primary FEC data. Legislative record pending.
**Why this file exists:** the OpenFEC API rate-limits DEMO_KEY at 40 calls/hour and these
figures took most of an hour's budget to assemble. Do not re-query to re-derive them.

---

## Committee IDs

| Entity | FEC ID | Notes |
|---|---|---|
| AIPAC PAC | C00797670 | "American Israel Public Affairs Committee Political Action Committee" |
| NorPAC | C00247403 | separate pro-Israel PAC, not an AIPAC entity |
| United Democracy Project (UDP) | C00799031 | AIPAC's super PAC |
| Langworthy for Congress | C00817932 | principal campaign committee |
| Langworthy Congressional Victory Cmte | C00832188 | joint fundraising |
| Circle the Wagons PAC | C00827881 | leadership PAC |
| Langworthy Leadership & Accountability Fund | C00934109 | joint fundraising |
| Langworthy Molinaro Victory Cmte | C00888073 | joint fundraising |
| Langworthy for Congress (earlier) | C00732784 | earlier committee, not used in these totals |

**Overmatch warning:** a `%AIPAC%` name search also hits **SHIELD AI POLITICAL ACTION
COMMITTEE (SAIPAC)**, C00782532, which is the defense-tech firm Shield AI and is
unrelated. Exclude it. Also present in the committee table but irrelevant here:
"CITIZENS AGAINST AIPAC CORRUPTION" (C00879080) and "REJECT AIPAC PAC" (C00876649),
both anti-AIPAC committees.

---

## Headline figures — from AIPAC's OWN Schedule B disbursements

Source: OpenFEC `/schedules/schedule_b/?committee_id=C00797670&recipient_name=LANGWORTHY`,
all 84 rows paged. This is AIPAC reporting what it sent, so it captures sub-$200
contributions the recipient never itemizes.

| Channel | Amount | Detail |
|---|---|---|
| **Direct PAC contributions** | **$25,000** | 5 × $5,000, net of two voided entries |
| **Bundled / earmarked through AIPAC** | **$76,016** | 75 contributions |
| **Total routed via AIPAC** | **$101,016** | |

Direct PAC contributions, itemized:

| Date | Amount | Note |
|---|---|---|
| 2022-07-14 | $5,000 | |
| 2022-07-21 | −$5,000 | VOID |
| 2022-07-21 | $5,000 | |
| 2022-08-29 | $5,000 | |
| 2022-10-20 | $5,000 | |
| 2022-10-20 | −$5,000 | VOID |
| 2024-04-05 | $5,000 | |
| 2024-10-03 | $5,000 | |
| 2025-09-29 | $5,000 | |
| **Net** | **$25,000** | $10,000 in 2022, $10,000 in 2024, $5,000 in 2025 |

Bundled money by calendar year: 2022 $9,750 · 2023 $2,000 · 2024 $38,556 ·
2025 $25,695 · 2026 $16.

Bundled contribution size distribution (n=75): under $500 → 23; $500–999 → 5;
$1,000–1,999 → 30; $2,000–2,999 → 14; $3,000+ → 3. Median $1,000, mean $1,014,
max $3,300 (the individual per-election maximum; only 2 contributions hit it).

**AIPAC money went only to LANGWORTHY FOR CONGRESS** (C00817932) — all 84 rows.
No AIPAC money to the leadership PAC or any joint fundraising committee.

---

## NorPAC

Source: same endpoint, committee_id=C00247403.

- **Direct contributions: $0.**
- **Bundled: $17,249** across 2 lump disbursements, all to Langworthy for Congress.
- One NorPAC contribution of $1,000 was itself routed *through AIPAC* as conduit
  (AIPAC Schedule B, 2023-08-07, "EARMARK OF NORPAC FEC ID C00247403").

---

## United Democracy Project — the load-bearing negative

**Zero.** OpenFEC `/schedules/schedule_e/?candidate_id=H2NY23133` returns
`pagination.count = 0`: there are **no independent expenditures for or against
Langworthy from any committee, ever**. UDP — AIPAC's super PAC, the vehicle that
spent heavily against candidates in 2024 — has never spent a dollar on his race.

This is the single most important corrective to the claims circulating in his
Facebook comments. It is checkable and it is false.

---

## Proportion — share of itemized individual money

Source: local DuckDB index `~/data/public-ledger/federal/fec/fec_index.duckdb`,
table `individual_contributions`, committee C00817932, `memo_cd IS NULL`.

| Cycle | Itemized individual $ | Via AIPAC conduit | Share |
|---|---|---|---|
| 2022 | $549,666 | $9,500 | 1.7% |
| 2024 | $818,296 | $34,118 | 4.2% |
| 2026 (partial) | $572,975 | $25,500 | 4.5% |
| **All** | **$1,940,937** | **$69,118** | **3.6%** |

NorPAC conduit across all cycles: $15,649 (0.8%).

---

## The $76,016 vs $69,118 discrepancy — reconciled, do not treat as an error

AIPAC's Schedule B says it routed **$76,016**; the campaign's Schedule A shows
**$69,118** carrying AIPAC's conduit ID. The ~$6,898 gap breaks down as:

- 2024 cycle accounts for ~$6,438 of it. Three contributions AIPAC reports routing do
  not appear under AIPAC's conduit ID in the campaign's itemization: a $3,300
  (2024-02-28), a $2,000 (2024-05-22), and the $1,000 NorPAC earmark (2023-08-07).
- The remainder is sub-$200 contributions ($1, $5, $9, $16, $22, $100 lines appear on
  AIPAC's Schedule B) that fall below the recipient's itemization threshold.

Both numbers are correct measures of different things. **Cite AIPAC's own Schedule B
($76,016 bundled / $101,016 total) as the headline** — it is AIPAC's own accounting of
what it routed — and disclose the campaign-side figure rather than picking silently.

---

## Editorial decisions already made (2026-07-25)

- **Aggregate only. Do not publish the names of the 75 bundled individual donors.**
  They are private citizens whose only act was a small legal contribution. The names
  carry an identifiable ethnic pattern and publishing them would function as a target
  list while serving no accountability purpose. Report totals, cycles, size
  distribution, and geography only.
- Entry framing: **what the record actually shows, including debunking** the
  overstated claims — the zero super-PAC spending and the ordinary-sized direct PAC
  contribution both belong up front.

---

## Cross-reference: the site's existing figure is low

`content/campaign-finance/_index.md` reports AIPAC at **$31,550** and NorPAC at
**$15,649**, sourced to **OpenSecrets** and scoped to the 2024 cycle only. That is
roughly a third of the cross-cycle primary-source figure. Same aggregator-over-primary
pattern that produced the Landa `$68,700` error corrected on 2026-07-25. That page
should be updated or explicitly scoped when the AIPAC entry publishes.
