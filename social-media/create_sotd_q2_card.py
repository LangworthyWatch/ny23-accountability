#!/usr/bin/env python3
"""Social card: State of the District — Q2 2026 (digest cover). Neutral house palette."""

from PIL import Image, ImageDraw, ImageFont

WIDTH = 1080
HEIGHT = 1080
FONT_DIR = "/System/Library/Fonts/Supplemental/"

BG     = "#F5F7FA"
NAVY   = "#1E3A5F"
DARK   = "#1A202C"
GREEN  = "#276749"
ORANGE = "#C05621"
MUTED  = "#718096"
BORDER = "#E2E8F0"
GOLD   = "#D69E2E"
WHITE  = "#FFFFFF"
ROW    = "#FFFFFF"


def font(name, size):
    try:
        return ImageFont.truetype(f"{FONT_DIR}{name}", size)
    except Exception:
        return ImageFont.load_default()


f_brand  = font("Arial Bold.ttf", 22)
f_title  = font("Impact.ttf", 60)
f_sub    = font("Arial Bold.ttf", 24)
f_tag    = font("Arial.ttf", 19)
f_tag_b  = font("Arial Bold.ttf", 19)
f_fig    = font("Impact.ttf", 44)
f_cat    = font("Arial Bold.ttf", 15)
f_line   = font("Arial.ttf", 18)
f_line_b = font("Arial Bold.ttf", 18)
f_foot   = font("Arial Bold.ttf", 19)
f_method = font("Arial.ttf", 16)

img  = Image.new("RGB", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

# ── Header ──
draw.rectangle([(0, 0), (WIDTH, 48)], fill=NAVY)
draw.text((WIDTH // 2, 24), "LANGWORTHYWATCH.ORG", fill=WHITE, font=f_brand, anchor="mm")

# ── Title block ──
draw.text((WIDTH // 2, 96), "STATE OF THE DISTRICT", fill=NAVY, font=f_title, anchor="mm")
draw.text((WIDTH // 2, 142), "Q2 2026  ·  NY-23  ·  Inaugural Issue", fill=DARK, font=f_sub, anchor="mm")
draw.text((WIDTH // 2, 178),
          "Documented conditions, set against the record —", fill=MUTED, font=f_tag, anchor="mm")
draw.text((WIDTH // 2, 200),
          "improvements reported with the same prominence as harms.", fill=MUTED, font=f_tag, anchor="mm")

# ── Digest rows ──
# (figure, fig_color, category, cat_color, line1, line2)
rows = [
    ("230+",  NAVY,   "JOBS",            NAVY,
     "eSolutions / Bush Industries closure, Jamestown —",
     "insolvency filing names U.S. tariffs among four causes"),
    ("~450K", NAVY,   "HEALTHCARE",      NAVY,
     "lose expanded Essential Plan eligibility on July 1 —",
     'NY DOH: "a direct result of H.R. 1"'),
    ("~40%",  NAVY,   "HEALTHCARE",      NAVY,
     "higher ACA premiums than they would otherwise be",
     "(NY Dept. of Health)"),
    ("$60.5M", NAVY,  "FEDERAL $ IN",    NAVY,
     "FEMA award to rebuild Jasper-Troupsburg's flooded school —",
     '"helped secure" claim rated MOSTLY TRUE'),
    ("$1.3M", ORANGE, "FEDERAL $ OUT",   ORANGE,
     "WSKG public broadcasting cut — 21% of its budget",
     "(Rescissions Act, H.R. 4)"),
    ("$0",    ORANGE, "STILL PENDING",   ORANGE,
     "to any named NY-23 hospital, of the $212M in rural-health",
     "funds that reached New York State"),
    ("+25%",  GREEN,  "CREDIT WHERE DUE", GREEN,
     "Chautauqua County median household income since 2019",
     "(nominal; ~9–10% after inflation)"),
]

y = 228
row_h = 92
gap = 6
fig_col_x = 56          # left edge of figure column
fig_col_w = 196         # width reserved for the figure
text_x = fig_col_x + fig_col_w + 18

for fig, fig_c, cat, cat_c, l1, l2 in rows:
    draw.rounded_rectangle([(44, y), (WIDTH - 44, y + row_h)], radius=8,
                           fill=ROW, outline=BORDER, width=2)
    # figure (vertically centered in the row)
    draw.text((fig_col_x + fig_col_w // 2, y + row_h // 2), fig,
              fill=fig_c, font=f_fig, anchor="mm")
    # thin divider between figure and text
    draw.line([(text_x - 10, y + 16), (text_x - 10, y + row_h - 16)], fill=BORDER, width=1)
    # category + two description lines
    draw.text((text_x, y + 18), cat, fill=cat_c, font=f_cat, anchor="lm")
    draw.text((text_x, y + 46), l1, fill=DARK, font=f_line, anchor="lm")
    draw.text((text_x, y + 70), l2, fill=DARK, font=f_line, anchor="lm")
    y += row_h + gap

# ── Method line ──
y += 6
draw.text((WIDTH // 2, y),
          "Attribution tiers throughout. Full report + sources + fact-check links online.",
          fill=MUTED, font=f_method, anchor="mm")

# ── Footer ──
draw.rectangle([(0, HEIGHT - 48), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH // 2, HEIGHT - 24),
          "langworthywatch.org/state-of-the-district/2026-q2/",
          fill=WHITE, font=f_foot, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/state_of_district_q2.png"
img.save(out, "PNG", optimize=True)
print(f"Saved: {out}")
