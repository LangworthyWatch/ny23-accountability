# Hochul-record triage (Oct 15, 2026): Langworthy campaign videos L1, L2, L4, L5, L6

Research only. Nothing in `content/` was edited. Verdicts below are proposals.

Covered elsewhere (not duplicated here): gas/propane ban, fracking, PA-vs-NY energy prices, CLCPA,
E&C bills, COLA/OBBBA tax, Celiac bill.

## Speaker identification (failure mode 6)

| Clip | Page / date | What the frames show | Speaker | Confidence |
|---|---|---|---|---|
| L6 | "Nick Langworthy" campaign page, Oct 9 | WETM 18 debate set, lower third "REP. NICK LANGWORTHY (R) US HOUSE NY DIST. 23" (`frames/L6_4.6s.jpg`) | Langworthy, WETM debate Oct 6 (debate SRT 17:11-17:20) | Confirmed |
| L5 | campaign page, Oct 9 | WETM set, Langworthy on camera (`frames/L5_9.2s.jpg`, `L5_30.7s.jpg`) | Langworthy, WETM debate Oct 6 (debate SRT 23:27-24:05) | Confirmed |
| L1 | campaign page, Oct 15 | Static photo of Langworthy over "77 WABC ON THE AIR" graphic; audio only | Langworthy (first person "where I'm from in the Buffalo area"; posted by his page) | Probable; audio over a still, voice not independently matched |
| L2 | campaign page, Oct 15 | Same WABC still graphic; 11.7 s of audio | Presumed Langworthy (same WABC segment packaging) | UNCONFIRMED: could be the host. Hedge or confirm from the full WABC audio |
| L4 | campaign page, Oct 14 | Spectrum News 1 "DEBATE FOR GOVERNOR / RACE FOR NEW YORK GOVERNOR" lower third, Bruce Blakeman on camera (`frames/L4_4.1s.jpg`) | Blakeman, NY1/Spectrum gubernatorial debate Oct 13 | Confirmed (CBS NY recap quotes the Escalade line to Blakeman, `debate-cbsny-recap.txt`) |

"Ronamak" in the L6 Whisper output = "run amok" (on-screen caption reads "GOVERNMENT RUN AMOK AND").

L1 re-transcribed with Whisper `medium.en` (scratch): the line is **"Taxes have gone up eight billion dollars
in your watch"** and "You know where the [eight] billion went to? Illegal migrants." The base model's
"a billion" is a mishearing of "eight billion." CONFIRMED by the burned-in captions
(`frames/L1cap_montage.jpg`, 40-49 s): "TAXES HAVE GONE UP / $8 BILLION / ON YOUR WATCH ... YOU KNOW
WHERE THE / 8 BILLION WENT TO".

## Files

- `transcripts/L*.srt` - timestamped Whisper base.en transcripts of the clips.
- `frames/` - stills used for speaker ID.
- `gov-debate-2026-10-13/` - audio of the full Spectrum News debate (YouTube gr9YwmtWxXw) + Whisper SRT.
- `debate-*.txt`, `blakeman-*.txt` - retained text of debate recaps and Blakeman campaign statements.
- `taxes/fy25|26|27fp-en.pdf/.txt` - DOB Enacted Budget Financial Plans (via openbudget.ny.gov; budget.ny.gov resets curl).
- `census/` - Census Vintage 2025 state and county components-of-change CSVs + `ny-pop-components-v2025.txt` summary.
- `migrants/` - OSC asylum-seeker spending tracker, NY1/CBS on the NYC debit-card pilot, PolitiFact on the $2.4B FY2025 allocation.
- `elliott/` - full NYU Wagner Buffalo Blizzard report (via Wayback) + text.
- `wood-heat/` - S5391 bill text, WHEC fact check, CLCPA Final Scoping Plan (2022) PDF/text.
- `utility/` - Post-Journal on Hochul asking PSC to reject Con Ed hikes.
- `wayback-save-log.txt`, `wayback-verified.txt` - archive submissions and playback verification.

Earlier evidence reused from `research/sources/debate-2026-10-06/claims/` (L9-*, L16-*, L31-*, L33-*).

## Findings by claim (proposed verdicts)

### L6 - Langworthy, WETM debate Oct 6 (clip 0:04-0:14; debate SRT 17:11-17:20)
"Your electric bill has doubled as Kathy Hochul's public service commission has raised rates 48 times."
Caption: "Her failed policies raised your taxes, caused utility bills to skyrocket, and forced businesses and people to flee."

- (a) "48 times": a Blakeman campaign tally. Blakeman July 22, 2026 statement ("hiked utility rates 48 times",
  WLEA; `../../debate-2026-10-06/claims/L9-blakeman-statement-48-times-wlea-jul-2026.txt`); City & State sponsored
  interview Oct 2026 ("48 utility rate hikes, 48 in just four years", `blakeman-cityandstate-sponsored-48.txt` l.115).
  Feb 11, 2026 NYGOP acceptance release said **36** ("the Hochul Administration's 36 utility rate hikes",
  `blakeman-nygop-acceptance-8B.txt` l.34; same "36 times" on junipercivic). Blakeman repeated it at the Oct 13
  debate ("Donald Trump didn't raise utility rates 48 times", gov-debate SRT ~13:22). No methodology published;
  not traced to any PSC count. Multi-year joint-proposal rate plans (e.g., NYSEG's prior plan: cumulative 62%
  electric delivery increases over three years, per site entry 2026-02-25) mean "rate increases" can be counted
  per utility, per service, per rate-year step, so the count is undefined. GAP: no PSC docket tally done.
- (b) "doubled": EIA EPM Table 5.6.B, NY residential avg price 19.44 c/kWh (2021) -> 26.39 (2025) = +36%;
  YTD Jan-Jul 2026 29.38 (+51% vs 2021 full year, seasonal mismatch, do not present as like-for-like).
  Files in `../../debate-2026-10-06/claims/L9-eia-*`. Not doubled statewide. NY-23 utility-specific typical-bill
  series (NYSEG/National Grid 2021 vs 2026) NOT pulled: GAP. Context: PSC commissioners are gubernatorial
  appointees confirmed by the Senate (site entry 2026-03-14 l.144); DPS attributes recent increases to supply
  (commodity) costs (site entry 2026-08-19 l.155); PSC Sept 2025: climate programs 5-9.5% of bills
  (2026-02-25 entry). Hochul publicly asked the PSC to reject Con Ed's 2025 request (`utility/postjournal-*`).
- (c) "raised your taxes": DOB FY2026 Enacted Financial Plan (`taxes/fy26fp-en.txt` l.889, 959-973, 1960-1964):
  first five PIT brackets cut 20 bp, ~$1B/yr to 8.3M filers (77%); the 2021 top rates (filers >$2.1M; enacted
  under Cuomo, tax year 2021) extended through 2032 (+$3.6B in FY2029). FY2027 plan (`taxes/fy27fp-en.txt`
  l.360, 885, 977-984): 7.25% top corporate rate extended through 2029 (+$1.1-1.58B/yr), H.R.1 decoupling
  (+$1.4B FY2027), tips exemption. MCTMT payroll-tax increases (FY2024, FY2026) apply only in the MTA region,
  not NY-23 counties (fy26 l.2618-2624; fy27 l.2540-2545). Increases under Hochul = extensions/targeted business
  and top-earner taxes; broad middle-class rates went down.
- (d) "people flee": Census Vintage 2025 (`census/ny-pop-components-v2025.txt`), periods 7/2021-6/2025:
  NY pop 19,835,345 -> 20,002,427 (+167,082); net domestic migration -719,579; net international +719,224;
  natural increase +158,957. Domestic out-migration real but shrinking (-284,910 in 2022 to -137,586 in 2025);
  total population grew. NY-23's seven whole counties (excl. Erie): -8,907 total, domestic -3,538,
  natural -6,587 (deaths > births drive most of the loss), international +1,555.
- Proposed: bill "doubled" MOSTLY FALSE; "48 times" NOT SUPPORTED; "raised your taxes" MISLEADING;
  "flee" MISSING CONTEXT (domestic out-migration true; population up).

### L1 - Langworthy on 77 WABC (audio over still; posted Oct 15; clip 0:40-0:53)
"Taxes have gone up $8 billion on your watch ... You know where the 8 billion went to? Illegal migrants."
- Debate: Spectrum News / NY1, Oct 13, 2026 (only debate). YouTube gr9YwmtWxXw; Whisper SRT in
  `gov-debate-2026-10-13/`. Hochul (~3:31): "largest middle-class rate cut in 70 years"; at ~57:22 "I've cut
  middle-class tax rates to the lowest it's been in 70 years"; Blakeman in crosstalk (~57:25-57:33):
  "...up eight billion dollars since you've been governor" (medium.en re-run). Separately Blakeman (~2:35):
  "Kathy Hochul has spent eight billion dollars of your money on illegal migrants for free food, free housing,
  free transportation and a free cell phone."
- Origin of tax "$8B": Blakeman campaign figure since at least Feb 11, 2026 ("more than $8 billion in tax hikes",
  NYGOP release). No calculation published. GAP: not reconstructable; DOB figures above sum to multi-billion
  only by adding out-year, targeted, mostly extension items.
- Migrant spending: OSC tracker: state emergency asylum spending $3.34B through Sept 30, 2026; plan $3.9B
  SFY2023-27; FY2027 enacted budget "no new appropriations" (`migrants/osc-asylum-seeker-spending-report.txt`
  l.82-83). FY2025 allocation $2.4B over two years (PolitiFact). NYC's own total $9.66B (Council, debate folder L31).
- Proposed: MISLEADING / NOT SUPPORTED. Langworthy fuses two different Blakeman $8B figures (tax total and
  migrant spending) into a causal chain; state migrant spending is $3.34B and no tax was earmarked to it.

### L2 - WABC audio (posted Oct 15): "you get food, you get luxury housing, you get a phone ... better than
anyone that lost their job. That's a taxpaying New Yorker." Speaker UNCONFIRMED (see table).
- NYC (not state) ran a prepaid food-card pilot for ~2,600 families in city-funded hotels without kitchens,
  ~$350/week for a family of four, ended Jan 2025 (`migrants/ny1-*`, `cbsny-*`). Shelters/HERRCs were emergency
  hotels and congregate sites; no source found for "luxury" or for state-provided phones. Echoes Blakeman's
  debate line ("free cell phone"). Proposed: MOSTLY FALSE (phones NOT SUPPORTED), hold until speaker confirmed.

### L4 - Speaker: Bruce Blakeman, Spectrum/NY1 debate Oct 13 (gov-debate SRT ~14:52; CBS NY recap). Not Langworthy.

### L5 - Langworthy, WETM Oct 6 (clip 0:00-0:46; debate SRT 23:27-24:05)
- "69 lives": official toll 47 (46 Erie + 1 Niagara); NYU Wagner report l.307 "46 residents in Erie County";
  WIVB ME breakdown: 18 outdoors, 12 no power/heat, 7 delayed EMS, 4 vehicles, 4 snow-clearing, 1 drowning.
  Origin of 69 not found (GAP). FALSE.
- "baseboard electric heat only": no source ties deaths to heating type. NYU: ~20,000 Buffalo National Grid
  customers out Dec 23-25, "This often meant a loss of heat as well" (`elliott/nyu.txt` l.446-450) - outages
  disable gas/oil furnaces too; full restoration 11:30 pm Dec 28 (l.1779). NOT SUPPORTED.
- "911 collapsed": supported in substance: backlog of 1,100 emergency calls, county dispatch software could
  view 25 calls at once; county announced Dec 24 EMS could not reach people; 7 deaths from delayed EMS
  (NYU l.516-522). MOSTLY TRUE.
- "proposals in New York to ban wood heat": no bill found. Bills found protect wood burning (S5391/A210
  cooking fuels; A2003 "Rural Energy Freedom Act", search result only). CLCPA Final Scoping Plan discusses wood
  smoke PM2.5 and projects reduced wood combustion via electrification, no ban recommendation
  (`wood-heat/scoping-plan-final-2022.txt` l.5096-5137, 6152, 6184); DEC 2021 statement to WHEC: state "is not
  considering legislation that would ban heating your home with firewood". NOT SUPPORTED (null result hedged:
  nysenate.gov blocks curl; full-text bill search not run).

## Verified Wayback snapshots (playback 200, content checked)
See `wayback-verified.txt`. NOT verified: Yahoo/Watertown recap (save 520), WIVB (save 520),
S5391 PDF snapshot (2.5 KB stub; treat as unarchived).
