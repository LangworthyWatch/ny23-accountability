#!/usr/bin/env python3
"""State of the District Q2 — county carousel slides 2 & 3.
Slide 2: "The Federal Squeeze on NY-23" (district-wide backbone + his record).
Slide 3: "NY-23 County Heat Ranking" (each county's single named hook).
Slide 1 is the existing state_of_district_q2_cover.png.
Rendered at 3x + LANCZOS for crisp text."""

from PIL import Image, ImageDraw, ImageFont

SC = 3
W = H = 1080
FONT_DIR = "/System/Library/Fonts/Supplemental/"

BG     = "#F5F7FA"
NAVY   = "#1E3A5F"
DARK   = "#1A202C"
GREEN  = "#276749"
RED    = "#9B2C2C"
ORANGE = "#C05621"
MUTED  = "#718096"
BORDER = "#E2E8F0"
GOLD   = "#D69E2E"
WHITE  = "#FFFFFF"
ROW    = "#FFFFFF"
URL    = "langworthywatch.org/state-of-the-district/2026-q2/"


def font(name, size):
    try:
        return ImageFont.truetype(f"{FONT_DIR}{name}", size * SC)
    except Exception:
        return ImageFont.load_default()


def P(v):
    return int(round(v * SC))


def XY(x, y):
    return (P(x), P(y))


def BOX(x1, y1, x2, y2):
    return [XY(x1, y1), XY(x2, y2)]


f_brand  = font("Arial Bold.ttf", 22)
f_title  = font("Impact.ttf", 52)
f_sub    = font("Arial.ttf", 19)
f_item   = font("Arial Bold.ttf", 23)
f_mag    = font("Arial.ttf", 17)
f_chip   = font("Arial Bold.ttf", 15)
f_rank   = font("Impact.ttf", 34)
f_county = font("Arial Bold.ttf", 24)
f_hook   = font("Arial.ttf", 18)
f_foot   = font("Arial Bold.ttf", 19)
f_note   = font("Arial.ttf", 16)


def base():
    img = Image.new("RGB", (P(W), P(H)), BG)
    d = ImageDraw.Draw(img)
    d.rectangle(BOX(0, 0, W, 48), fill=NAVY)
    d.text(XY(W // 2, 24), "LANGWORTHYWATCH.ORG", fill=WHITE, font=f_brand, anchor="mm")
    d.rectangle(BOX(0, H - 48, W, H), fill=NAVY)
    d.text(XY(W // 2, H - 24), URL, fill=WHITE, font=f_foot, anchor="mm")
    return img, d


def finish(img, name):
    img = img.resize((W, H), Image.LANCZOS)
    img.save(f"/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/{name}",
             "PNG", optimize=True)


def chip(d, x_right, y_mid, text, color):
    """Draw a right-aligned record chip centered vertically at y_mid."""
    bb = d.textbbox((0, 0), text, font=f_chip)
    tw = (bb[2] - bb[0]) / SC
    pad = 12
    w = tw + pad * 2
    h = 30
    x1 = x_right - w
    d.rounded_rectangle(BOX(x1, y_mid - h / 2, x_right, y_mid + h / 2), radius=P(5), fill=color)
    d.text(XY(x1 + w / 2, y_mid), text, fill=WHITE, font=f_chip, anchor="mm")


# ── Slide 2 — the federal squeeze (backbone + his record) ────────────────────
img, d = base()
d.text(XY(W // 2, 84), "THE FEDERAL SQUEEZE ON NY-23", fill=NAVY, font=f_title, anchor="mm")
d.text(XY(W // 2, 120), "District-wide federal actions — and how Langworthy voted", fill=MUTED, font=f_sub, anchor="mm")

# (item, magnitude, tag, tag_color)
rows = [
    ("One Big Beautiful Bill", "$911B Medicaid cut · ~$187B SNAP · +7.5M uninsured", "VOTED AYE ×2", RED),
    ("Rural Health Transformation", "$212M one-time — vs. NY's ~$13.5B/yr hospital losses", "CREDIT-CLAIMED", ORANGE),
    ("USDA farm bailout", "$12B, ~92% to row crops — NY-23 dairy/grape mostly excluded", "SILENT", MUTED),
    ("Local Food for Schools", "~$1B cut — Broome-Tioga BOCES lost $289,630", "SILENT", MUTED),
    ("Rural Energy (REAP)", "grants re-frozen March 31, 2026", "SILENT", MUTED),
    ("Civil-rights office (OCR)", "ED civil-rights office gutted; NY office closed; ~90% dismissed", "SILENT", MUTED),
]

y = 150
rh = 116
gap = 8
for item, mag, tag, tc in rows:
    d.rounded_rectangle(BOX(44, y, W - 44, y + rh), radius=P(8), fill=ROW, outline=BORDER, width=P(2))
    d.text(XY(70, y + 34), item, fill=DARK, font=f_item, anchor="lm")
    d.text(XY(70, y + 70), mag, fill=MUTED, font=f_mag, anchor="lm")
    chip(d, W - 64, y + 34, tag, tc)
    y += rh + gap

d.text(XY(W // 2, y + 8), "One bill he voted for, one award he claims — and silence on the rest.",
       fill=MUTED, font=f_note, anchor="mm")

finish(img, "state_of_district_q2_backbone.png")

# ── Slide 3 — county heat ranking ────────────────────────────────────────────
img, d = base()
d.text(XY(W // 2, 84), "NY-23 COUNTY HEAT RANKING", fill=NAVY, font=f_title, anchor="mm")
d.text(XY(W // 2, 120), "Q2 2026 · by federal-policy exposure (not yet closures)", fill=MUTED, font=f_sub, anchor="mm")

# (county, hook)
counties = [
    ("CHAUTAUQUA", "grape belt left out of the farm bailout; hospitals Medicaid-exposed"),
    ("CHEMUNG", "Arnot Health, the regional safety-net, exposed to the Medicaid cuts"),
    ("SCHUYLER", "Schuyler Hospital named on Public Citizen's at-risk list"),
    ("CATTARAUGUS", "Seneca Nation tribal health + Salamanca's local-food cut"),
    ("ALLEGANY", "Jones & Cuba Memorial Medicaid-fragile; BRIC flood funds in limbo"),
    ("ERIE SOUTHTOWNS", "Eden & Collins farms excluded from the row-crop bailout"),
]

y = 156
rh = 96
gap = 8
for i, (county, hook) in enumerate(counties, start=1):
    d.rounded_rectangle(BOX(44, y, W - 44, y + rh), radius=P(8), fill=ROW, outline=BORDER, width=P(2))
    # rank circle
    cx, cy, r = 96, y + rh / 2, 30
    d.ellipse(BOX(cx - r, cy - r, cx + r, cy + r), fill=NAVY)
    d.text(XY(cx, cy - 1), str(i), fill=WHITE, font=f_rank, anchor="mm")
    d.text(XY(150, y + 34), county, fill=NAVY, font=f_county, anchor="lm")
    d.text(XY(150, y + 66), hook, fill=DARK, font=f_hook, anchor="lm")
    y += rh + gap

d.text(XY(W // 2, y + 10), "Also: Steuben — Bath VA staffing cuts  ·  Tioga — Broome-Tioga's $289,630 food-program loss",
       fill=MUTED, font=f_note, anchor="mm")

finish(img, "state_of_district_q2_counties.png")
print("Saved backbone + counties (3x supersampled).")
