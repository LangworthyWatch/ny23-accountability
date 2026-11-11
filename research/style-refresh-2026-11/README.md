# Card style refresh (proposed Nov 11, 2026)

Files: mock-A-one-number.png, mock-B-said-vs-record.png, mock-C-weekly-roundup.png, colorblind-sheet.png (row 1 is the current style, the Nov 4 mandate card); make_mockups.py; colorblind_sheet.py. The theme is social-media/lib/card_v2.py.

## Palette and WCAG contrast (all text pairs pass AA, at 4.5:1 or better)
| Pair | Ratio |
|---|---|
| Ink #1A202C on white / paper | 16.3 / 15.4 |
| Navy #1E3A5F on white / paper | 11.5 / 10.8 |
| Gray #5A6678 on white / paper | 5.8 / 5.5 |
| Amber text #8A5A0B on white / amber tint | 5.9 / 5.4 |
| Slate #3F5873 on slate tint | 6.5 |
| White on navy | 11.5 |
| Light gold #F6D58E on navy | 8.1 |
| Red #C53030 on white (FALSE only) | 5.5 |
Bright amber #D69E2E is used for fills only, never for text on light backgrounds.

## Colorblind simulation (Machado 2009, severity 1.0)
- Current style: the red highlight bars turn olive under deuteranopia and protanopia and stay legible by brightness, but the meaning of red against green (the claim and record panels, the green fair-case strip) is lost.
- v2: amber stays clearly separate from navy under all three types. Under tritanopia, amber shifts toward pink, but labels carry the meaning. The missed vote on card A is an open circle, a shape difference rather than a color difference.

## Why
Red marked "him" on the current cards and reads as partisan coding. Red against green fails readers with red-green color blindness, about 1 in 12 men. Impact read as tabloid; Arial Black matches the favicon.
