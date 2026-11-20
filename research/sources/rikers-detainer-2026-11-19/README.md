# Rikers detainer release (Jaundoo): source packet

Research for a possible fact-check of Rep. Langworthy's official-page Facebook post (about Nov 17, 2026) on the NY Post/DHS story. All files fetched **2026-11-19** with plain curl. `.txt` files are text extracted from the `.html`/`.pdf` beside them. None of these URLs has been archived to Wayback yet. Archive them before publishing.

## 1. The underlying case

| File | URL |
|---|---|
| `dhs_2026-11-17_sanctuary_insanity_new_york.{html,txt}` | https://www.dhs.gov/news/2026/11/17/sanctuary-insanity-dhs-calls-out-sanctuary-politicians-new-york-releasing-illegal |
| `nypost_2026-11-17_jaundoo.{html,txt}` | https://nypost.com/2026/11/17/us-news/delon-raymond-jaundoo-an-illegal-migrant-accused-of-attempted-murder-released-from-rikers-island-despite-ice-detainer-dhs/ |

Key lines from the DHS release (Release Date November 17, 2026; page last updated 11/18/2026):
- "On April 29, 2026, ICE lodged a detainer asking the New York Department of Corrections to not release Delon Raymond Jaundoo, an illegal alien from Guyana, after he had been arrested in Brooklyn for the charges of attempted murder, first-degree assault ... second-degree criminal possession of a weapon: loaded firearm."
- "His criminal history includes a prior arrest for third-degree assault"
- "New York sanctuary politicians refused to honor ICE's detainer and RELEASED Jaundoo from Rikers Island back onto the streets on November 7. He currently remains at large."
- "Jaundoo lawfully entered the United States under the Obama Administration, but illegally overstayed his authorized period after it expired in January 2015."
- Mullin: "Under Governor Kathy Hochul, New York has become a hotbed of illegal alien crime."
- DHS says Hochul proposed legislation "which she signed into law in May 2026. The law took effect on August 25, 2026."

Key lines from the NY Post article (byline "Fox News", published 2026-11-17T08:42:09Z, headline per og:title "Illegal migrant accused of attempted murder at large after Rikers release despite ICE detainer: DHS"):
- "ICE ... lodged an immigration detainer for Jaundoo on April 29, which the New York City Department of Correction declined to honor, allowing him to be released from Rikers Island."
- "a state law signed by Gov. Kathy Hochul took effect in August barring local authorities from cooperating with federal immigration officials."
- Hochul spokesperson: "By law, New York State always notifies federal immigration enforcement of any non-citizen serving a State prison sentence."

Neither source says why or how he was released on Nov 7 (bail, court order, dismissal), or what became of the charges. Neither mentions any conviction.

## 2. NYC rules (Rikers / NYC DOC)

| File | URL |
|---|---|
| `nyc_local_law_2014-58.{pdf,txt}` | https://intro.nyc/local-laws/2014-58 (redirects to the Legistar PDF of Local Law 58 of 2014, which amends Admin Code §9-131 for DOC) |
| `nyc_local_law_2014-59.{pdf,txt}` | https://intro.nyc/local-laws/2014-59 (Local Law 59 of 2014, which amends §14-154 for NYPD) |
| `nyc_local_law_2017-228.{pdf,txt}` | https://intro.nyc/local-laws/2017-228 (Local Law 228 of 2017, which adds §10-178 and amends §9-131(f) reporting) |
| `usa_v_city_of_new_york_edny_1-25-cv-04084_2026-10-15.{pdf,txt}` | https://www.govinfo.gov/content/pkg/USCOURTS-nyed-1_25-cv-04084/pdf/USCOURTS-nyed-1_25-cv-04084-0.pdf |

- LL 58/2014, §9-131(a)(3): "'Department' shall mean the New York city department of correction"
- LL 58/2014, §9-131(b): the department "may only honor a civil immigration detainer by holding a person beyond the time when such person would otherwise be released ... if: i. federal immigration authorities present the department with a judicial warrant ... and ii. a search ... indicates ... that such person: A. has been convicted of a violent or serious crime, or B. is identified as a possible match in the terrorist screening database."
- The list of "violent or serious crime" includes 125.25 and "a felony attempt ... to commit any crime specified". This turns on a *conviction* (within 5 years), and a pending charge does not count.
- EDNY decision (Judge Reyes, Oct 15, 2026): "New York City's Department of Correction ... may honor a section 287.7 detainer request only if (a) federal immigration authorities provide a 'judicial warrant' and (b) the individual 'has been convicted of a violent or serious crime' ..."
- EDNY: "even if this Court eliminated sections 9-131(b), 9-205(b), 14-154(b) ... New York City officers would still be unable to execute a section 287.7 detainer request to maintain custody of a non-citizen without a judicial warrant."
- EDNY: "The New York legislature 'could enact a statute authorizing ... law enforcement officers to arrest people pursuant to federal civil immigration detainers'". Disposition: "the Court grants Defendants' motion to dismiss."
- Defendants include "NEW YORK CITY DEPARTMENT OF CORRECTION, STANLEY RICHARDS" (Commissioner) and Mayor Mamdani.

amlegal (codelibrary.amlegal.com) returned 403, so I could not retrieve the current consolidated Admin Code text. The EDNY opinion's quotation of §9-131(b) (Oct 2026) is the most recent statement of the text in this packet.

## 3. State law

| File | URL |
|---|---|
| `wells_v_demarco_2018_NYSlipOp_07740_nyclu-copy.{pdf,txt}` | https://www.nyclu.org/uploads/2018/11/people_ex_rel_wells_francisvdemarco.pdf (NYCLU-hosted copy of the slip opinion; nycourts.gov returned a Cloudflare challenge page) |
| `ag_2026-02_immigration-enforcement-guidance.{pdf,txt}` | https://ag.ny.gov/sites/default/files/2026-02/oag-immigrationenforcement-guidance.pdf |
| `nysenate_2025_S9005C.{html,txt,pdf}`, `nysenate_2025_S9005C_pdf.txt` | https://www.nysenate.gov/legislation/bills/2025/S9005/amendment/C ; https://legislation.nysenate.gov/pdf/bills/2025/S9005C |
| `nysenate_law_CVR_28-2_protect-our-courts.{html,txt}` | https://www.nysenate.gov/legislation/laws/CVR/28*2 |
| `nysenate_2025_S2235.{html,txt}`, `nysenate_2025_A3506.{html,txt}` | https://www.nysenate.gov/legislation/bills/2025/S2235 ; .../2025/A3506 (New York for All) |
| `doj_2026-06_complaint-ny-mask-ban-287g.{html,txt}` | https://www.justice.gov/opa/pr/justice-department-files-complaint-challenging-new-york-mask-ban-and-identification |
| `ag_2026-08_statement-lawsuit-287g-ban.{html,txt}` | https://ag.ny.gov/press-release/2026/attorney-general-james-and-governor-hochul-release-statement-lawsuit-challenging |

- Wells (2d Dept, Nov 14, 2018): "we conclude that New York state and local law enforcement officers are not authorized by New York law to effectuate arrests for civil law immigration violations." The opinion also has a heading: "Detention Pursuant to an ICE Detainer or Warrant Constitutes an Arrest".
- AG guidance (updated Jan 2025): "State law bars state and local law enforcement officers from arresting and detaining individuals for civil immigration violations alone—even if federal immigration authorities have issued a detainer"; "LEAs have authority to honor such detainers if the federal authorities present a judicial warrant."
- S9005C: signed "chap.55" on May 27, 2026. Part LL, Subpart A, is the "Local Cops, Local Crimes Act" (Exec. Law §170-k). It bars entering or remaining in "any agreement pursuant to section 287(g)" and any agreement "to house or detain individuals for federal civil immigration violations". §170-k(6): "Nothing in this section shall be construed to prohibit ... complying with any state or federal court order or judicial warrant".
- S9005C, Part LL, Subpart C, GML §996(5): "'Municipal government' ... shall not include a local correctional facility". Police and peace officers are excluded from "municipal government employee" (§996(6)). The 2026 law's detainer-related limits therefore do not reach local jail officers.
- CVR §28 (Protect Our Courts Act) bars civil arrest of people attending court "unless such civil arrest is supported by a judicial warrant or judicial order". It covers courthouses, not jail release.
- New York for All (S2235B/A3506) is still in committee: Senate "In Senate Committee ... Codes", last action Feb 09, 2026; Assembly "In Assembly Committee".
- DOJ (June 23, 2026) sued the State, Hochul, and James over the mask ban, identification rules and the "banning [of] cooperative 287(g) agreements".

Not retrieved: Executive Order 170 (2017). The governor's site returns 404 for every URL I tried.

## 4. Hochul authority and statements

| File | URL |
|---|---|
| `gov_new-laws-stand-against-ice-overreach.{html,txt}` | https://www.governor.ny.gov/news/governor-hochul-highlights-new-laws-protect-new-yorkers-and-stand-against-ice-overreach (May 29, 2026) |
| `gov_2026-08-25_local-cops-local-crimes-in-effect.{html,txt}` | https://www.governor.ny.gov/news/keeping-new-yorkers-safe-governor-hochul-announces-local-cops-local-crimes-provision-banning |
| `gov_2026-08-25_rush-transcript.{html,txt}` | https://www.governor.ny.gov/news/video-audio-photos-rush-transcript-governor-hochul-announces-implementation-her-new-law-stand |
| `gov_introduces-local-cops-local-crimes-act.{html,txt}`, `gov_2026-02-09_growing-support.{html,txt}` | governor.ny.gov releases from Jan and Feb 2026 introducing the Act |
| `nysenate_law_COR_45.{html,txt}` | https://www.nysenate.gov/legislation/laws/COR/45 (State Commission of Correction powers) |

- Aug 25, 2026 transcript: "Once they're convicted and do their time, we work with ICE to ensure they're deported. And I'll repeat that New York State will never become a sanctuary for criminals."
- The same transcript: "local police will assist ICE only if a real crime has been committed. But on civil immigration matters, ICE is on their own."
- The Feb 9, 2026 release heading says the Act "Would Not Prohibit Local Law Enforcement or State Police From Continuing To Work With Federal Law Enforcement in Criminal Investigations".
- Correction Law §45: the State Commission of Correction can "Advise and assist the governor", "Make recommendations", and "Visit, inspect and appraise". None of these is a power to set a jail's detainer policy.

## Post screenshot
The operator's screenshot of the November 17, 2026 post shows the Post's photo of the charged man (a booking photo). It is deliberately NOT stored in the repo. The original is the operator's own capture; the post text is quoted in the entry.

## Archives
`urls.txt` lists the 8 sources cited in the entry; `save_log.txt` records Save Page Now responses. Verify by playback before adding links.
