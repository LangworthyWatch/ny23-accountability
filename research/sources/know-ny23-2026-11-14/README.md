# Know NY-23 sources, retained November 14, 2026

For `content/know-ny23.md`. Every figure on the page is reproduced by the three scripts here (run from this folder with `python3`).

## Scripts and outputs
- `acs_profile.py acs` → `out_acs_profile.txt`, `acs2025_ny23_profile.csv`. ACS 2025 1-year detailed tables for NY-23 (119th Congress lines, GEO_ID `5001900US3623`), New York (`0400000US36`), the US (`0100000US`) and all 26 NY districts (for ranks). Derived MOEs use the Census approximation formulas. Run with `NEIGHBORS=1` to print the neighboring districts and MOEs behind each "statistically tied" statement on the page.
- `trend_and_transfers.py .` → `out_trend_and_transfers.txt`, `ny23_towns_pop_2020_2025.csv`. Town and city population, 2020 base to 2025, summed over the 173 county subdivisions with at least 99.5% of their land in NY-23 (relationship file in `../redistricting-2026-11-13/`). Lockport (49.8% of land) and Wheatfield (6.9%) are partial and excluded from the sum. Also county population 2010-2025 and BEA transfer share by county.
- `bea_composition.py` → `out_bea_composition.txt`. CAINC35 2022 composition for the five whole counties (Allegany 36003, Cattaraugus 36009, Chautauqua 36013, Chemung 36015, Tioga 36107), and the five-county CAINC4 transfer share for 2004, 2014 and 2024.

- `acs_income_sources.py acs` → `out_acs_income_sources.txt`. District-wide shares of aggregate household income (B19025) from earnings, Social Security, retirement income, SSI and cash public assistance. Cash income only.

## Audit, November 14, 2026
An independent recomputation from the raw files matched every table value. Prose fixes made afterward:
- 65+ ties: with the direct 65+ count (B09020_001; NY-23 23.84 ± 0.51) only NY-3 (23.25 ± 0.74) is statistically tied; NY-24, NY-19 and NY-1 are significantly lower but within one point. With margins built by summing B01001 age cells (± 0.73, what `acs_profile.py` prints), all four test as tied. The page uses the direct margin (± 0.5) and names only NY-3 as tied.
- The 173 whole county subdivisions are 159 towns, 7 cities and 7 reservation areas; the three unchanged places are reservation areas.
- CAINC35 line 3000 is transfer receipts OF nonprofit institutions (received, not paid). The 3.3% outside line 2000 is that plus business payments to individuals.
- The BEA 30% covers the five whole counties only: 374,184 of the 749,487 residents of places wholly in the district (49.9%); whole Erie towns in the district hold 281,317. Medical benefits (line 2200) are 43.8% of the five-county 2022 total; `bea/CAINC35__definition.xml` describes them as payments for care. The card and caption were rebuilt on district-wide ACS figures for this reason.

## Data (extracts)
- `acs/acsdt1y2025-*.dat`: rows for the US, New York and NY's 26 districts, cut from the Census table-based summary files (2025 1-year). `ACS20251YR_Table_Shells.txt` holds the line labels. Note: in the 2025 shells, B15003 runs 001-023 (bachelor's = 020); the script matches labels rather than line numbers.
- `pep/sub-est2025_36.csv` (Vintage 2025 subcounty, New York, whole file); `pep/co-est2025-alldata_NY.csv` and `pep/co-est2020-alldata_NY.csv` (New York rows of the county files).
- `bea/CAINC4_NY_US.csv` (last updated February 5, 2026; 2024 data) and `bea/CAINC35_NY_US.csv` (last updated November 16, 2023; 2022 is the latest year in the download), US and New York rows; `bea/CAINC35__Footnotes.html` (footnote 2: public assistance medical care "Consists of Medicaid and other medical vendor payments").
- BEA glossary definition of personal current transfer receipts, read in a browser on November 14, 2026: "income payments to persons for which no current services are performed and net insurance settlements."

## Statistical ties (from `NEIGHBORS=1`)
- 65+: NY-23 23.8 ± 0.7; NY-3 23.3 ± 0.7; NY-24 23.2 ± 0.6. Highest point estimate, not a significant lead.
- Median age: NY-3 44.8, NY-1 44.5, NY-23 44.5. Not used as a rank.
- Veterans: NY-24 7.7 ± 0.5; NY-23 7.5 ± 0.5; NY-21 7.1 ± 0.5; next NY-22 5.1.
- Manufacturing: NY-24 12.9 ± 0.8; NY-23 12.2 ± 1.0; NY-26 10.7 ± 1.0.
- Median home value: NY-23 $209,900; NY-21 $212,300; NY-24 $215,100; next NY-22 $231,400 ± 5,360.

## Not used
- Census API (needs a key). QCEW (county and workplace-based; ACS residence-based industry is used instead). Long-run decennial county counts before 2010 (the census.gov `cencounts` text file returned 404).

## Archive status
`save_log.txt` and `verify_log.txt`: 16 captures made Nov 14, 2026, each verified by playback (HTTP 200, expected row or text present; the table-shells capture plays back gzip-compressed). `save_log2.txt`: the remaining ACS table files.
