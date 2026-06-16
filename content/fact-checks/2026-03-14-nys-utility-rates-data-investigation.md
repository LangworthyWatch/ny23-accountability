---
title: "Who's Really Driving Your Electric Bill? A Data Investigation into NY Utility Rates"
date: 2026-03-14
draft: false
topic: "Energy / Utility Costs"
claim_date: "Ongoing (2023–2026)"
source: "PSC Rate Case Filings, FERC Form 1, EIA, SEC Proxy Statements, Census ACS"
source_url: "https://dps.ny.gov/electric-gas-cases"
archived_url: "https://web.archive.org/web/20260324194221/https://dps.ny.gov/electric-gas-cases"
verdict: "DOCUMENTED PATTERN"
tags: ["energy", "utility-costs", "nyseg", "national-grid", "rate-hike", "clcpa", "data-investigation", "executive-compensation", "lobbying"]
counties: ["steuben", "chemung", "allegany", "cattaraugus", "tioga", "schuyler", "chautauqua", "district-wide"]
---

**New York's electricity rates are 57.4% above the national average. Utilities are now requesting additional increases of 11–19% on top of already high prices. The dominant political explanation — that clean energy mandates are driving the increases — does not match the data from the utilities' own filings.** This investigation compiles rate case documents submitted to the Public Service Commission, federal financial filings, federal energy price data, and Census income data to show what is actually inside these rate increases, who benefits, and who bears the cost. All source documents are publicly available; data files are available for download below.

*This entry is a companion to: [Langworthy Blames Clean Energy for Costs That Natural Gas and Utility Profits Actually Drive](/fact-checks/2026-02-20-energy-costs-dunkirk/), [The Energy Choice Act Would Benefit the Heating Fuel Industry That Drafted It](/fact-checks/2026-02-25-energy-choice-act/), and [NYSEG Requested a $450M Dividend While Seeking a Rate Hike](/fact-checks/2026-02-25-nyseg-rate-hike-silence/).*

---

## Why This Matters in NY-23

NY-23 covers Steuben, Chemung, Tioga, Schuyler, Allegany, Cattaraugus, Chautauqua, and part of Erie County — primarily rural upstate territory served by NYSEG (a subsidiary of Avangrid Inc.) and parts of National Grid. **NYSEG is currently requesting a rate increase of 18.4%** — the steepest pending request among New York's major electric utilities.

Incomes in these counties run below the state median. A larger share of household income goes to electricity than in wealthier downstate counties. That means rate increases are not an abstract policy debate here; they show up directly in whether families can pay their bills.

**The question this data investigation asks: what are these rate increases actually for?**

---

## Section 1: What Rate Increases Actually Pay For

Utilities must file detailed cost justifications with the PSC whenever they request a rate increase. This investigation analyzed 8 rate case filings totaling **$4.0 billion in combined requested increases** across Con Edison, National Grid, NYSEG, RG&E, Central Hudson, Orange & Rockland, and PSEG Long Island.

<iframe src="/graphics/viz_cost_breakdown.html" width="100%" height="620" frameborder="0" scrolling="no" title="NY utility rate increase cost breakdown"></iframe>

**In plain language:** The chart above shows what the utilities say they need the money for. The largest drivers are:

| Cost Category | Amount Requested | Share |
|---------------|-----------------|-------|
| Infrastructure & Capital Investment | $1,355M | **33.7%** |
| Operations & Maintenance | $672M | 16.7% |
| Storm Recovery & Resiliency | $504M | 12.5% |
| Return on Equity (Shareholder Profit) | $408M | 10.1% |
| Property Taxes | $348M | 8.6% |
| Depreciation | $242M | 6.0% |
| Labor & Benefits | $91M | 2.3% |
| Vegetation Management | $50M | 1.3% |
| **Clean Energy Programs** | **$187M** | **4.7%** |
| Other | $167M | 4.1% |

Clean energy programs — the System Benefits Charge, the Clean Energy Fund, and CLCPA-related surcharges — account for **$187 million of the $4.0 billion total**, or **4.7%**. The three largest real cost drivers (infrastructure, operations, and storm costs) are **14 times larger** than all clean energy costs combined.

The System Benefits Charge adds approximately **$3.36/month** to an average residential bill — roughly 2.1% of the total monthly bill.

**[Download full rate case cost data (CSV)](/data/power-investigation/cost_decomposition.csv)**

---

## Section 2: How NY Rates Compare to Inflation and the National Average

<iframe src="/graphics/viz_rate_vs_inflation.html" width="100%" height="550" frameborder="0" scrolling="no" title="NY electricity rates vs inflation and US average"></iframe>

**In plain language:** The chart above compares New York residential electricity prices to U.S. inflation (CPI) and the national average price. Key findings:

- NY residential rates grew **49.2%** from 2015 to 2025 vs. **34.7%** CPI inflation — running 1.06% per year faster than general inflation
- NY pays **26.49 cents/kWh** vs. the U.S. average of **16.83 cents/kWh** — a gap of **57.4%**
- Rate growth **accelerated sharply** after 2020 even as the System Benefits Charge (the clean energy surcharge) grew by only **0.14 cents/kWh** — accounting for just 1.8% of the total price increase over that period
- NY households pay **$696/year more** than the national average at typical usage (7,200 kWh/year)

The clean energy surcharge grew from approximately 0.38 cents/kWh to 0.52 cents/kWh over this period — a small fraction of the overall price trajectory.

**[Download full rate history data (CSV)](/data/power-investigation/rate_increase_history.csv)**

---

## Section 3: Who Bears the Burden — Upstate Counties Pay More as a Share of Income

Rate increases are not equally felt. Electricity bills take a larger share of income in lower-income communities. Because NY-23 counties have below-average incomes, the same rate increase hits harder here than in Westchester or Manhattan.

<iframe src="/graphics/viz_consumer_burden_map.html" width="100%" height="750" frameborder="0" scrolling="no" title="NY electricity burden by county"></iframe>

**In plain language:** This map shows electricity costs as a percentage of median household income, by county (using EIA service territory prices and Census ACS 2022 income data). Darker colors indicate higher burden.

Key findings from this analysis:

- **Lowest-income quartile** (average income ~$58K): faces a **14.1% average rate increase** under pending cases, with electricity costing **2.99% of annual income**
- **Highest-income quartile** (average income ~$101K): faces a **5.7% average rate increase**, with electricity costing **1.85% of annual income**
- The lowest-income quartile pays **1.6 times more** as a percentage of income
- **NYSEG territory** — which covers most of NY-23 — is requesting the **steepest increase at 18.4%** while serving some of the state's lowest-income counties
- Bronx County shows the highest single-county burden at 4.17% of median income; upstate rural counties in the Southern Tier follow closely

**[Download full county burden data (CSV)](/data/power-investigation/consumer_impact_by_county.csv)**

---

## Section 4: Executive Pay vs. Consumer Bills

<iframe src="/graphics/viz_exec_comp_vs_rates.html" width="100%" height="500" frameborder="0" scrolling="no" title="Utility CEO compensation vs consumer rates"></iframe>

**In plain language:** While consumer electricity prices rose 42% between 2015 and 2024, CEO compensation at the three largest utility parent companies serving New York grew **64%** — from $28.5 million combined to $46.8 million combined (per SEC proxy statement filings).

| Metric | 2015 | 2024 | Change |
|--------|------|------|--------|
| Consumer electricity rates (NY avg) | ~17.7 ¢/kWh | ~25.1 ¢/kWh | +42% |
| Top 3 utility CEO comp (combined) | $28.5M | $46.8M | **+64%** |
| National Grid CEO specifically | — | — | **+78.6%** |

Over the same period, utility shareholders received **$36.8 billion in dividends** — more than five times the total revenue collected through the clean energy surcharge ($7.0B over the same period).

FERC Form 1 data for 5 major NY utilities (2018–2024):
- **Combined 2024 revenue**: $36.5 billion
- **Combined net income**: $3.9 billion
- **Dividend payout ratio**: 74% of net income → shareholders
- **Average PSC-authorized Return on Equity**: 9.05% — a guaranteed profit in every rate case, regardless of service quality

Rate base (the capital investment on which the guaranteed 9%+ return is calculated) grew 48–64% across utilities from 2018 to 2024. Each dollar added to rate base generates guaranteed profit — creating a structural incentive to invest in infrastructure rather than hold costs down.

---

## Section 5: The Lobbying Machine

New York's utilities and energy trade associations are active participants in Albany lobbying, with filings tracked through COELIG/JCOPE (the state ethics disclosure system).

<iframe src="/graphics/viz_utility_donations.html" width="100%" height="550" frameborder="0" scrolling="no" title="Energy sector lobbying and political activity"></iframe>

**In plain language:** Energy sector entities filed **1,754 lobbying registrations** between 2015 and 2024. Total reported lobbying spend: **$75.7 million** ($71.7M compensation + $4.0M reimbursement). Of that, **$62.9 million (87.7%)** was specifically identified as related to rate cases and energy policy.

Top lobbying spenders among energy entities (from public COELIG/JCOPE disclosures):

| Entity | Total Lobbying Spend | Rate-Case-Related |
|--------|---------------------|------------------|
| Business Council of NYS | $8.91M | Significant (broad energy/business policy) |
| Entergy Corp | $5.58M | Indian Point decommissioning |
| National Grid | $5.50M | 91 filings, $3.61M rate-related |
| NRG Energy | $4.72M | 79 filings, 92% rate-related |
| Constellation/Exelon | $4.67M | 98 filings, nuclear plant policy |
| Avangrid (NYSEG + RG&E) | $4.65M | 176 filings (highest filing count) |
| PSEG | $4.53M | 160 filings |
| Consolidated Edison | $4.06M | 65 filings, 92% rate-related |

Annual lobbying spend by energy entities nearly **tripled** from $3.4 million (2011) to $8.4 million (2024).

The PSC commissioners who approve or reject these rate requests are appointed by the Governor and confirmed by the State Senate, with no more than three commissioners permitted to be members of the same political party. The PSC Chair, Rory M. Christian, previously worked at KeySpan Energy (now National Grid) and Exelon Energy — two regulated utilities currently before the PSC on rate cases — as well as the Environmental Defense Fund. Three of the seven current commissioners (Bright, Valova, and Sheehan) come from clean energy nonprofit or advocacy backgrounds. This revolving-door structure is a matter of public record; the commissioner biographies are posted on the PSC website.

---

## Section 6: What the Clean Energy Charge Actually Is

The "clean energy surcharge" that legislators and advocates frequently invoke is primarily the **System Benefits Charge (SBC)**, which funds energy efficiency programs, low-income assistance, and renewable development. It is not where utility profits come from.

<iframe src="/graphics/viz_clean_energy_share.html" width="100%" height="750" frameborder="0" scrolling="no" title="Clean energy share of NY rate increases"></iframe>

**In plain language:** The SBC adds approximately $3.36/month to an average bill. The entire clean energy component across all 8 rate cases ($187M) is smaller than the profit component ($408M in guaranteed Return on Equity) and dwarfed by infrastructure costs ($1.355B). If the SBC were eliminated entirely, a typical residential bill would drop by about $3.36/month — while the infrastructure-driven increases already in the pipeline would more than replace it.

---

## Section 7: Consumer Complaints Surge

PSC consumer complaint data (2019–2024) shows:

- Statewide complaints grew **84%**: 24,146 (2019) → 44,538 (2024)
- **Billing complaints** dominate at 67% of all complaints, up from 56% in 2019 — and grew **120%**
- **NYSEG**: +95% complaint growth — the same utility now requesting an 18% rate increase
- **RG&E**: +94% complaint growth — same parent company (Avangrid)
- **Central Hudson**: +153% complaint surge in 2022 from a billing system migration failure

The surge in billing complaints correlates directly with the 2022–2024 wave of aggressive rate case filings.

---

## What This Data Does Not Show

This investigation documents cost structures and financial data from public sources. It does not prove that any specific rate increase was improperly approved or that any individual regulator acted improperly. The PSC is a quasi-judicial body; its rate case proceedings are formal and adversarial, with consumer and utility intervenors.

What this data shows:
- The stated justification for rate increases (clean energy) is quantifiably small (4.7%) compared to actual cost drivers
- Rate growth has exceeded inflation over the past decade
- Consumer complaint volume has grown dramatically alongside rate increases
- Executive compensation has grown faster than consumer rates over the same period
- Shareholders receive far more in dividends than ratepayers pay in clean energy surcharges

**What this data does not show:** Whether regulatory decisions were influenced by the industry lobbying spend documented above, or whether rate increases were approved or denied appropriately relative to the law. The PSC routinely cuts rate requests (roughly 30% on average) — the amounts above are requested, not approved.

---

## Section 8: Langworthy's Energy Sector Donors

Rep. Langworthy has repeatedly blamed clean energy mandates for high utility costs while not publicly engaging with the NYSEG rate case that would raise bills for his own constituents. FEC campaign finance records show energy sector connections to his congressional campaign:

| Donor (by employer) | Type | Donated to Langworthy | Context |
|---------------------|------|----------------------|---------|
| Avangrid Inc. | Regulated utility | $1,500 (1 donation) | Parent company of NYSEG, currently requesting 18.4% rate increase in NY-23 |
| United Refining Co. | Petroleum refinery | $21,900 (5 donations) | Warren, PA petroleum refinery with NY operations |

**In plain language:** Avangrid — the parent company of NYSEG, which is currently before the PSC requesting the steepest rate increase of any major NY utility — has donated to Langworthy's campaign. Langworthy has blamed clean energy policies for high energy bills. The data above shows clean energy accounts for 4.7% of NYSEG's rate increase request. Infrastructure and capital investment account for 33.7%.

These amounts are relatively small within Langworthy's overall fundraising. The pattern is one of access, not scale. FEC individual contribution records are public at [fec.gov](https://www.fec.gov/data/receipts/?committee_id=C00817932).

*For broader documentation of Langworthy's campaign finance donors, see the [LangworthyWatch campaign finance section](/campaign-finance/).*

---

## Questions This Raises

1. NYSEG is requesting an 18.4% rate increase while serving NY-23's lowest-income counties. What is Rep. Langworthy's position on the NYSEG rate case currently before the PSC?
2. Infrastructure and operations — not clean energy — are the dominant cost drivers. What is Langworthy's position on requiring utilities to justify capital investment programs before adding them to rate base?
3. If eliminating the System Benefits Charge entirely would save ~$3.36/month on an average bill, while NYSEG's pending infrastructure request would add far more, which is the more effective cost-control lever?
4. New York's PSC commissioners are appointed by the Governor and confirmed by the State Senate. Should the appointment process include additional disclosure requirements for commissioners with prior industry or advocacy backgrounds?
5. Consumer complaints to the PSC grew 84% over five years at the same utilities now requesting more rate increases. Should complaint volume be a factor in rate case proceedings?

---

## Sources and Data

All data in this investigation is from publicly available government sources. Raw data files are provided for independent verification.

**Primary sources:**
* PSC Rate Case Filings (dps.ny.gov): 8 cases, 2023–2025, cases 25-E-0072, 24-E-0322, 25-E-0375, 25-E-0379, 23-E-0418, 23-E-0065, 25-E-0190, 24-E-0413
* [EIA Electric Power Monthly](https://www.eia.gov/electricity/monthly/) — historical residential electricity prices by state
* [FERC Form 1](https://www.ferc.gov/industries-data/electric/general-information/electric-industry-forms/form-1-electric-utility-annual-report) — annual utility financial reports
* [SEC DEF 14A Proxy Statements](https://www.sec.gov/cgi-bin/browse-edgar) — executive compensation (Con Edison, Avangrid/Iberdrola, National Grid, Fortis Inc)
* [COELIG/JCOPE Lobbying Disclosures](https://www.jcope.ny.gov/) — lobbyist registration and activity reports
* [Census ACS 2022 5-Year Estimates](https://data.census.gov/) — county median income and housing units
* [FEC Individual Contributions — Langworthy for Congress (C00817932)](https://www.fec.gov/data/receipts/?committee_id=C00817932) — campaign donation records

**Downloadable data:**
* [Rate case cost decomposition (per case)](/data/power-investigation/cost_decomposition.csv)
* [Aggregate cost breakdown (all 8 cases)](/data/power-investigation/cost_decomposition_aggregate.csv)
* [Rate increase history vs inflation and US average](/data/power-investigation/rate_increase_history.csv)
* [Consumer electricity burden by county (56 counties)](/data/power-investigation/consumer_impact_by_county.csv)
* [Rate case outcomes — PSC approval rates](/data/power-investigation/rate_case_outcomes.csv)
* [CEO compensation vs. consumer rates](/data/power-investigation/ceo_compensation_vs_rates.csv)
* ["Clean energy" narrative vs. actual cost drivers](/data/power-investigation/narrative_vs_reality.csv)

[All datasets and methodology](/data/)

---

**Note:** This entry documents publicly available data from government filings and federal databases. All calculations are based on the stated sources and are available for independent verification via the download links above. This investigation does not make claims about individual conduct or motivation — it documents cost structures, financial data, and publicly disclosed lobbying activity.

*Published: March 14, 2026. Data through fiscal year 2024–2025 where available.*

*Last updated: March 14, 2026*
