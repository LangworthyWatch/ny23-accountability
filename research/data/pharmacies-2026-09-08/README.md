# NY-23 pharmacy layer from the NYSED pharmacy-establishment registry (pulled Sept 8, 2026)

**Source.** New York State Education Department, Office of the Professions, Online Verification Search, profession "Pharmacy Establishment (020)". The public search app (eservices.nysed.gov/professions/verification-search) calls `https://api.nysed.gov/rosa/V2/findPharmacies`; the registry reports itself "current as of September 08, 2026 02:15 PM" (data import Sept 8, 2026 01:48 PM). Full statewide pull retained as `nysed_pharmacy_registry_full_2026-09-08.json.gz` (26,594 establishment records, all types, historical and current).

**Enumeration.** The endpoint is a substring name search with no wildcard or county filter. Every letter A–Z and digit 0–9 was queried (pageSize 1000) and results were deduplicated on `registrationNumber`; the unique count stopped growing at 26,549 by "S" and finished at 26,594 (a name of only digits or punctuation would be missed; none expected).

**Fields used.** `status` (Active / Discontinued / Transfer / Not Active / Not Registered), `deletedDate`, `successorRegistrationNumber`, `type` (Pharmacy, Wholesaler, Wholesaler/Repacker, Manufacturer, Storekeeper, Outsource Facility), `county`, `address`.
- **Active** = status "Active" only.
- **Transfer** = the registration passed to a successor number (ownership change, same location). Treated as neither active nor a closure.
- **Closure** = status "Discontinued" or "Not Active", `deletedDate` on/after Jan 1, 2023, no successor registration.
- **Community pharmacy** = type "Pharmacy" whose trade or legal name does not match a hospital / medical center / health system / nursing / rehab / skilled / infusion / home care / hospice / correctional / dialysis / oncology / LTC / health center / clinic / VA / health-care-facility / operating-company pattern. This is a name heuristic; the excluded names are visible in `ny23_pharmacies_all_registry_records.csv` (`community` column). The Lionel R. John Health Center pharmacy in Salamanca (Seneca Nation) is classified institutional by this rule and is noted wherever it matters.

**District assignment.** Allegany, Cattaraugus, Chautauqua, Chemung, Schuyler, Steuben and Tioga are wholly in NY-23. Erie and Niagara are split: every Erie/Niagara record that is Active or ended since 2023 was geocoded (Census Bureau batch geocoder, Public_AR_Current, then point-in-polygon to the 119th-Congress district via the coordinates endpoint). Addresses the geocoder could not match were assigned only when the town is wholly inside or outside the district (Irving, Collins → in; West Seneca, Buffalo, Cheektowaga, Lewiston, Niagara Falls, Middleport, Newfane → out). **Eleven addresses remain unresolved and are excluded**: CVS West Seneca (3098 Orchard Park Rd), Rite Aid Buffalo (1625 Broadway), Middleport Family Health Center, 5300 Military Rd Lewiston, 6001 Shimer Dr Lockport, 8745 and 8015 Niagara Falls Blvd, 6000 Transit Rd at French Rd Depew, Tops Cheektowaga, Tops 7200 Niagara Falls Blvd, 1010 East & West Rd West Seneca. All but two are in towns outside the district; the Lockport and Depew ones could fall either way.

**Files.**
- `ny23_pharmacy_county_table.csv` — active (all types), active community, community closures since 2023, of which Rite Aid; by county (NY-23 portion for Erie and Niagara).
- `ny23_active_community_pharmacies.csv` — the 102 active community pharmacies.
- `ny23_community_pharmacy_closures_2023plus.csv` — the 28 community closures with dates and remaining active community pharmacies in the same ZIP.
- `ny23_zips_left_without_community_pharmacy.csv` — closures after which the ZIP has zero active community pharmacies (a ZIP proxy, not a drive-time analysis; suburban ZIPs such as Lancaster border others with pharmacies).
- `ny23_pharmacies_all_registry_records.csv` — every registry record in the nine counties, with district and classification columns.

**Caveats.** Registration status is administrative: a store can stop dispensing before its registration is discontinued, and the deletedDate is the registration end, not necessarily the last day open. Rite Aid's registrations ended June–October 2025 as its stores closed under the May 2025 Chapter 11. ZIP-level "none remaining" is a proxy for access, not a measured distance.
