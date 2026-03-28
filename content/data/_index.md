---
title: "Open Data"
description: "Download the datasets behind our fact-checks. Verify everything yourself."
---

# Open Data

Every claim on this site is backed by public records. This page provides downloadable datasets so you can verify our work independently. All files are CSV format, openable in Excel, Google Sheets, or any spreadsheet application.

**Data principles:**
- All data comes from public records (NYS Authority Budget Office, NYSBOE campaign finance filings, FEC, Congress.gov, NY PSC rate cases)
- No personal information is included beyond what appears in public filings
- We show our work. If we say "74 IDA beneficiaries donated to the Langworthy apparatus," you can download the 74 rows and check each one

For the methodology behind our cross-reference analyses, see our [Methodology](/methodology/) page.

---

## IDA / Subsidy Accountability

These datasets document Industrial Development Agency tax exemptions in NY-23 and their relationship to political donations. All data comes from the NYS Authority Budget Office ([data.ny.gov dataset 9rtk-3fkw](https://data.ny.gov/Transparency/Public-Authorities-Reporting-Information-System-PA/9rtk-3fkw)) and NYS Board of Elections campaign finance filings.

| Dataset | Rows | Description | Download |
|---------|------|-------------|----------|
| IDA-to-Langworthy Pipeline | 74 | Every IDA beneficiary that donated to the Langworthy political apparatus, with exemption amounts and donation-to-exemption ratios | [CSV](/data/ida/langworthy_ida_pipeline.csv) |
| NY-23 County Scorecards | 8 | IDA project counts, exemptions, per-household burden, and donor stats for each NY-23 county | [CSV](/data/ida/langworthy_county_scorecards.csv) |
| NY-23 Property Tax Impact | 8 | Per-household property tax shift caused by IDA exemptions in each NY-23 county | [CSV](/data/ida/langworthy_property_tax_impact.csv) |
| Broken Job Promises | 108 | IDA projects in NY-23 that failed to deliver promised employment targets | [CSV](/data/ida/langworthy_jobs_deficit.csv) |
| Suspiciously Timed Donations | 248 | Donations to Langworthy apparatus that occurred close to IDA project approvals | [CSV](/data/ida/timeline_suspicious_patterns.csv) |
| WARN Act Crossref | 25 | Companies receiving IDA tax exemptions that subsequently issued WARN Act layoff notices | [CSV](/data/ida/warn_ida_crossref.csv) |
| Triple Dippers | 111 | Companies receiving IDA + Empire State Development + PPP subsidies simultaneously | [CSV](/data/ida/triple_dippers.csv) |

**Related fact-checks:**
- [IDA Donor-Exemption Pattern](/fact-checks/2026-03-21-ida-donor-exemption-pattern/) — 74 beneficiaries, $246K donated, $66.2M in exemptions
- [OBBBA / IDA Vote](/fact-checks/2026-03-21-obbba-ida-vote/) — Making IDA-friendly tax provisions permanent
- [Campaign Finance Patterns](/fact-checks/2026-02-07-campaign-finance-patterns/) — IDA beneficiary donation flows

**Primary sources:** [NYS ABO PARIS Data](https://data.ny.gov/Transparency/Public-Authorities-Reporting-Information-System-PA/9rtk-3fkw) | [NYSBOE Campaign Finance](https://publicreporting.elections.ny.gov/) | [The Public Ledgers: IDA Investigation](https://thepublicledgers.org/investigations/)

---

## School District Impact

IDA tax exemptions reduce the property tax base that funds public schools. These datasets quantify that impact at the district level.

| Dataset | Rows | Description | Download |
|---------|------|-------------|----------|
| NY School District Impact | 478 | Every NY school district: IDA revenue lost, per-pupil impact, property tax base affected | [CSV](/data/school-districts/ny_district_impact.csv) |
| Bad Deals | 141 | IDA projects statewide that failed to deliver promised jobs — with the gap between promises and reality | [CSV](/data/school-districts/ny_jobs_bad_deals.csv) |

81 of the 478 districts are in NY-23 counties (Allegany, Cattaraugus, Chautauqua, Chemung, Schuyler, Steuben, Tioga). Filter the `county` column to find your district.

**Primary sources:** [NYS ABO PARIS Data](https://data.ny.gov/Transparency/Public-Authorities-Reporting-Information-System-PA/9rtk-3fkw) | [Census F-33 School Finance Data](https://www.census.gov/programs-surveys/school-finances.html)

---

## NY Utility Rate Investigation

These datasets support our investigation into New York electricity rate increases and what's actually driving them. All data comes from NY Public Service Commission rate cases, NYISO, and utility annual reports.

| Dataset | Rows | Description | Download |
|---------|------|-------------|----------|
| Rate Case Outcomes | 8 | PSC approval rates for utility rate increase requests — near-rubber-stamp record | [CSV](/data/power-investigation/rate_case_outcomes.csv) |
| CEO Compensation vs. Rates | 30 | Utility CEO pay growth compared to consumer rate increases over time | [CSV](/data/power-investigation/ceo_compensation_vs_rates.csv) |
| "Clean Energy" Narrative vs. Reality | 7 | What utilities claim drives costs vs. what rate case filings actually show | [CSV](/data/power-investigation/narrative_vs_reality.csv) |
| Cost Decomposition by Utility | 50 | What's actually in rate increases: infrastructure, profits, storms, clean energy, by utility | [CSV](/data/power-investigation/cost_decomposition.csv) |
| Cost Decomposition (Aggregate) | 11 | Same data aggregated across all utilities | [CSV](/data/power-investigation/cost_decomposition_aggregate.csv) |
| Consumer Impact by County | 19 | Annual electricity cost burden relative to median income, by county | [CSV](/data/power-investigation/consumer_impact_by_county.csv) |
| Rate Increase History | 11 | NY vs. national electricity rates over time | [CSV](/data/power-investigation/rate_increase_history.csv) |

**Related fact-checks:**
- [NY Utility Rates Data Investigation](/fact-checks/2026-03-14-nys-utility-rates-data-investigation/) — Clean energy = 4.7% of rate increases; infrastructure, profits, and storms = 63%
- [NYSEG Rate Hike Silence](/fact-checks/2026-02-25-nyseg-rate-hike-silence/) — $500M+ rate increase with no statement from Langworthy
- [Dunkirk Energy Costs](/fact-checks/2026-02-20-energy-costs-dunkirk/) — National Grid profits +43%; gas costs +29%

**Primary sources:** [NY DPS Rate Case Filings](https://www3.dps.ny.gov/W/PSCWeb.nsf/All/C4A4CAEBB6CDB10A85257687006F39ED) | [NYISO](https://www.nyiso.com/) | [EIA Electricity Data](https://www.eia.gov/electricity/data.php)

---

## Campaign Finance

| Dataset | Rows | Description | Download |
|---------|------|-------------|----------|
| Top Contributors (2024) | 38 | Top individual and PAC contributors to Langworthy for Congress, 2024 cycle | [CSV](/data/top-contributors-2024.csv) |
| Top Industries (2024) | 20 | Top contributing industries, 2024 cycle | [CSV](/data/top-industries-2024.csv) |

**Related fact-checks:**
- [Campaign Finance Patterns](/fact-checks/2026-02-07-campaign-finance-patterns/) — 46% individual, 44% PAC; only 3.5% small donors

**Primary sources:** [FEC: Langworthy for Congress (C00817932)](https://www.fec.gov/data/candidate/H2NY23133/) | [OpenSecrets: Nick Langworthy](https://www.opensecrets.org/members-of-congress/nick-langworthy/summary?cid=N00050227)

---

## Voting Record

| Dataset | Rows | Description | Download |
|---------|------|-------------|----------|
| Complete Voting Record | 2,410 | Every roll call vote cast by Rep. Langworthy, exported from Congress.gov | [CSV](/data/voting-record/langworthy_votes.csv) |

**Primary source:** [Congress.gov: Rep. Langworthy Roll Call Votes](https://www.congress.gov/member/nicholas-langworthy/L000600)

---

## How to Use This Data

**Open a CSV file:**
- **Excel/Google Sheets:** Download the file, then open it. All files use standard CSV format.
- **Filter to your county:** Most IDA and school district files have a `county` column. Use your spreadsheet's filter function to see just your area.
- **Sort by impact:** Sort the `ratio` column in the IDA pipeline file to see which beneficiaries got the most exemptions per dollar donated.

**Verify a claim:**
1. Find the fact-check that makes the claim
2. Download the relevant dataset from this page
3. The fact-check's methodology section (where available) explains how we got from the raw data to the finding
4. For underlying government data, follow the "Primary sources" links to the agency databases

**Report an error:**
If you find an error in any dataset, email langworthywatch@gmail.com. We will correct it and note the correction.

---

*All datasets derived from public records. Last updated: March 28, 2026.*
