# NY-23 Fact-Check Landmines

Curated list of the confusable entities on this beat — the adjacencies where a
*correctly-sourced* fact gets attached to the *wrong neighbor*. This is the
recombination error class: not a fabricated number, but a true fact joined to
the wrong program, district, vote, or list. `/claim-audit` reads this file and
checks every attribution in a draft against it.

When two items below look alike in a draft, **stop and verify the join** — that
is exactly where errors breed. Update this file whenever a new confusable pair
causes (or nearly causes) a correction; it is the institutional memory for
"things people get wrong here."

---

## 1. Programs — Medicaid ≠ SNAP (both are in OBBBA; both have "work requirements")

The single most dangerous pair. Both are cut by the same bill (H.R. 1 / OBBBA),
both gained "work requirements," both have age bands — so details cross-contaminate.

| Detail | Belongs to | Do NOT attach to |
|---|---|---|
| "Community engagement" work requirement, **ages 19–64**, begins **Dec 31 2026** | **Medicaid** | SNAP |
| Six-month eligibility redeterminations (expansion pop.), begin **Jan 2027** | **Medicaid** | SNAP |
| Work requirement age cap raised to **64** (from 54), narrowed exemptions | **SNAP** (ABAWD) | Medicaid |
| Admin cost-shift **50% → 25% federal** (state/county pays more), begins **2027** | **SNAP** | Medicaid |
| ~**$187B** national reduction (FRAC) | **SNAP** | Medicaid |
| ~**$911B** federal Medicaid cut over 2025–34 (CBO via KFF); ~**$137B** *rural* Medicaid (KFF) | **Medicaid** | SNAP |

Rule of thumb: "community engagement" = Medicaid; "ABAWD"/cost-shift/$187B = SNAP.

## 2. The two OBBBA roll calls (both H.R. 1, both Langworthy AYE)

| | Roll Call 145 | Roll Call 190 |
|---|---|---|
| Date | **May 22, 2025** | **July 3, 2025** |
| Stage | initial House passage | final passage (post-Senate) |
| Margin | 215–214-ish (2 GOP Nays) | **218–214** (2 GOP Nays) |
| Vote question | "On Passage" | "On Concurring… / final passage" |
| Langworthy | **Yea** (verbatim, [roll145.xml](https://clerk.house.gov/evs/2025/roll145.xml)) | **Aye** (verbatim, [roll190.xml](https://clerk.house.gov/evs/2025/roll190.xml)) |

Only two Republicans (Davidson-OH, Massie-KY) voted Nay on **both**. Don't swap the
dates or margins; don't cite RC145 where RC190's 218–214 final-passage fact is meant.
Verify any roll call with `python .claude/scripts/verify_fact.py rollcall <year> <num> <surname>`.

## 3. "At-risk hospital" lists — three different studies, different numbers

| List | Count | Scope | Method | Schuyler named? |
|---|---|---|---|---|
| **Public Citizen** ("Big Ugly Threat") | 446 national / **45 NY** / 29 outside NYC-LI | nationwide CMS cost reports | ≥20% Medicaid-CHIP revenue + negative 2022–24 net margins | **Yes** |
| **Fiscal Policy Institute** | **8 in NY-23** (most of any NY district) | NY-23 specifically | Medicaid reliance | (district-level) |
| AOL / "45 NY hospitals at risk" | 45 NY | NY | varies | (e.g., St. James Hornell) |

Cite Public Citizen for the *Schuyler named* hook; cite FPI for the *8-in-NY-23* district
fact. Don't merge the counts ("45" is NY-statewide, "8" is NY-23-only — not the same denominator).

## 4. RHTP award ≠ the Medicaid cut

- **$212M** = `$212,058,207`, New York's **Year-1 RHTP award** (CMS, Dec 2025), 12th-largest state. A one-time *inflow*.
- The Medicaid **cuts** are a separate, larger *outflow* from the same bill (KFF: RHTP offsets ~**37%** of ~$137B rural Medicaid cuts; 64% of cuts land after FY2030 when RHTP ends).
- Never describe the $212M as offsetting/covering the cuts without the KFF offset framing. Defer the cut math to `2026-06-02-rural-health-transformation-212m.md`; don't introduce a *new* conflicting Medicaid dollar figure in other entries (the HANYS ~$13.5B/yr is *statewide all-hospital annual*, a different denominator — label it as such).

## 5. OCR / "Justice Denied" numbers — national vs. New York

| Number | Means | Don't confuse with |
|---|---|---|
| **172** | national pending **seclusion/restraint** cases (0 agreements) | the NY total |
| **627** | **New York** total pending OCR cases (Figure 2) | the 172 national restraint figure |
| **1** | NY's total resolution agreements 2025 (all types) | a restraint-specific agreement |
| **112 / 507** | national agreements 2025 / 2024 | per-state counts |
| ~**90%** dismissed; 7 of 12 offices closed | GAO-26-108320 | the HELP report's figures |

NY "627 pending / 1 agreement" = total across **all** discrimination types (Fig. 2), not restraint-specific.

## 6. Langworthy's committees (119th Congress)

He sits on **exactly three**: **Energy & Commerce** (Health, Energy, Environment subcmtes), **Oversight & Government Reform**, and **Rules**. Source: [clerk.house.gov/members/L000600](https://clerk.house.gov/members/L000600).

- He is **NOT on the Agriculture Committee** — despite introducing ag/rural bills and doing ag events. Don't infer Ag membership from ag activity.
- The E&C + Rules pairing is unusual (both normally "exclusive") but real — verified.

---

## 7. NY-23 county membership (the canonical set)

NY-23 (119th Congress) comprises these **8 counties** for tagging purposes:

**Allegany · Cattaraugus · Chautauqua · Chemung · Erie · Schuyler · Steuben · Tioga**

- **Whole counties:** Chemung, Allegany, Cattaraugus, Chautauqua, Tioga.
- **Partial:** Erie (Southtowns only — Eden, Boston, Collins, Orchard Park, Gowanda; NOT Buffalo/Cheektowaga/West Seneca/Lackawanna, which are NY-26), Schuyler, Steuben. Niagara has a small NY-23 sliver — treat as **edge, verify**.

**NOT in NY-23 (common traps):** **Yates**, **Wyoming**, **Seneca**, **Ontario**, **Tompkins**, **Cortland**, **Broome**, **Monroe**, **Livingston**, **Genesee**, **Niagara** (mostly NY-26).

### The catchment/BOCES trap

A service area that *includes* an NY-23 county is **not** "five NY-23 counties." Examples that have bitten us:

- **Bath VA** catchment = Allegany, Chemung, Schuyler, Steuben, **Yates** → 4 NY-23 + Yates. Say "serves Schuyler (among its catchment)," not "five NY-23 counties."
- **Cattaraugus-Allegany-Erie-Wyoming BOCES** name includes **Wyoming**, which is **not** NY-23. A BOCES serving N counties ≠ N NY-23 counties.

Check any county claim with `python .claude/scripts/verify_fact.py county <name> [name...]`.
