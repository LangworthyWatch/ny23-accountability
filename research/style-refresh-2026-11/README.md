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

## v2.1 (Nov 11, after user feedback: "the card grays wash each other out")
The first set's surfaces were too close to tell apart: paper #F7F8FA against white measured 1.06:1; the slate tint against paper 1.06:1; the rule against paper 1.16:1. Changes:
- One white surface. The footer is now a navy band with an amber top rule.
- Gray text darkened to #4A5568 (7.5:1 on white).
- Rules darkened to #C3CCD8 (1.6:1) and drawn 2px wide.
- Fair-case panel fill #DCE5F0 with a #7C8DA6 border (3.4:1, which meets WCAG 1.4.11 for non-text elements).
- Amber tint #F8E7C2 with an amber border.
- Footer text #C9D3E0 on navy (7.6:1).
All text pairings still pass AA. The colorblind sheet was regenerated.

## v2.2 (Nov 11, user request: "a box to frame the information from the background")
- Content now sits in a white rounded panel with a soft shadow on a #DFE6EF backdrop, inset 22 px between the navy top bar and the navy footer band.
- Panel against the backdrop: 1.26:1 for the fill, plus a #9AA9BD border at 2.4:1 against white. The edge reads clearly; text contrast is unchanged.
- Templates lay out inside CONTENT_TOP and CONTENT_BOTTOM, so nothing touches the frame.
