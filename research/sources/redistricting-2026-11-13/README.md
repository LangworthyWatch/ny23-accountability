# Redistricting sources, retained November 13, 2026

For `content/fact-checks/2026-11-13-who-drew-ny23-redistricting.md`.

## His statements
- `wzmq-2026-06-15.html` / `.txt`: Erie News Now Washington Bureau story on WZMQ, June 15, 2026 ("once every decade," "a gerrymander that's led to them taking two seats," "the courts put fair maps on the table, that we ran on").
- `debate-2026-10-06-frame-53m05s-langworthy.png` and `debate-2026-10-06-clip-52m52s-whisper.txt`: WETM debate (YouTube hP1B2-qMPAQ), 52:52-53:08. The frame shows him at the podium answering. The same speaker gave the preceding answer on Hochul and Wall Street. The full auto-transcript is at `research/transcripts/2026-10-06-ny23-debate-wetm-youtube-hP1B2-qMPAQ.srt` (line 857). The opponent's reply is not quoted, per site rule.
- `wivb-2025-08-05.txt`, `nygop-2022-04-27-coa.json`, `nygop-2022-05-21-special-master.json` (WordPress API copies of nygop.org statements). WSKG Feb 2, 2022 is in the research agent's scratch copy only and is cited live.

## Courts
- `harkenrider-coa-2022-04-27.pdf` / `.txt`: Court of Appeals, 2022 NY Slip Op 02833. Troutman's partial dissent calls the gerrymandering holding "advisory," so that holding rests on four judges.
- `mcallister-order-2022-05-20.pdf` / `.txt`: Steuben County Supreme Court order adopting the special master's maps (filed May 21, 2022, 12:17 AM), with the Cervas report.
- `hoffmann-coa-2023-12-12.pdf` / `.txt`.
- `scotus-25a914-2026-03-02.pdf`, `williams-stipulation-2026-03-19.pdf`: NY-11 voting-rights case, stayed and then dismissed with prejudice.

## Maps and laws
- `struck-2022-S8172A-A9039A.pdf`: the struck map's district text.
- `ch92-2024-A9310-S8653.pdf`, `assembly-A09310-actions.txt`: the 2024 map, signed Feb 28, 2024 (Chapter 92).
- `wamc-2024-02-26.txt` (commission vote 9-1 on Feb 15, 2024; Legislature rejects it), `wamc-2024-02-28.txt` (passage 115-33 and 45-17).
- `S10637A-2026.pdf` / `.txt`, `assembly-A11553-actions.txt`: 2026 constitutional amendment, first passage June 3, 2026. Bracketed text is deleted matter; new § 5-c allows mid-decade congressional changes "not subject to any of the provisions of sections four or five-b."
- `spectrum-2026-11-12.txt`: Hochul, "We're halfway there."
- `cnhi-2024-03-niagara.txt`: news corroboration of the 2024 Niagara changes.
- `BILLSTATUS-119hr4889.xml`, `BILLSTATUS-119hr7219.xml`, `BILLS-119hr*ih.htm`: federal bills to bar mid-decade redistricting. L000600 is not a cosponsor of either. `clerk-discharge-petition-21.html`: one signature (Kiley) as of Nov 13, 2026.

## Data
- `tab20_cd11820_*_st36.txt`, `tab20_cd11920_*_st36.txt`: Census relationship files. The 118th Congress = 2022 court map; the 119th = 2024 map.
- `ny23_boundary_diff.py`: reproduces the town-level diff (land area) with whole-town 2020 base populations from `sub-est2024_36.csv`. Split towns (West Seneca in 2022; Lockport and Wheatfield now) have no population split, because the files give land area only.
- `downballot-2020pres-by-2022-lines.csv` (2020 president on 2022 court lines; despite the column of 2023 incumbents, NY-23 = Trump 57.6, Biden 40.4) and `downballot-2024-2020pres-by-current-lines.csv`.
- `fivethirtyeight-2022-02-20-archived.txt` (struck map, NY-23 R+26) and `fivethirtyeight-2022-06-04-archived.txt` (court map, NY-23 R+23). These are a different measure from the Downballot figures.
- `pgp-report-card-special-master-2022.json` (A overall; partisan A, geographic A, competitiveness C) and `pgp-report-card-struck-2022-legislative.json` (D overall, Democratic advantage). No grade was located for the 2024 map.
- `clerk-statistics2024.pdf`: official 2024 House results. Two-party margins: NY-4 D +2.3, NY-19 D +2.2, NY-22 D +9.1, NY-3 D +3.6.
- `crec-2024-02-28-H731-suozzi-swearing-in.htm`: Suozzi sworn in Feb 28, 2024.
- `ny_cd119_compactness_polsby_popper.csv`: computed from Census cb_2024 CD119 500k shapes in EPSG:5070. NY-23 ranks 20th of 26. Not used in the entry, because the shoreline penalty makes it a weak signal.

## Not used / unverified
- Cook PVI (R+12 in the 2022 edition, R+10 in the 2025 edition per Ballotpedia): not confirmed on Cook. Not used.
- Whether NYGOP funded the Harkenrider suit: not established.
- A Princeton "F" for the struck map at the time (RepresentUs release): the current JSON says D. The entry uses D.

## Archive status
Captures listed in the entry were verified by playback (expected text present in the id_ copy) on Nov 13, 2026. Refused: Hoffmann PDF (nycourts, 520), WIVB (520); Google Sheets captures hold no data, so the Downballot CSVs are the retained copies. The plain nyassembly.gov URLs archive without actions; the `&Summary=Y&Actions=Y` URLs were used.
