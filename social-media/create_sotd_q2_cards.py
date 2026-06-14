#!/usr/bin/env python3
"""State of the District — Q2 2026 social carousel.
Slide 1: clean cover (launch). Slide 2: by-the-numbers, grouped by valence."""

from PIL import Image, ImageDraw, ImageFont

W = H = 1080
FONT_DIR = "/System/Library/Fonts/Supplemental/"

BG     = "#F5F7FA"
NAVY   = "#1E3A5F"
DARK   = "#1A202C"
GREEN  = "#276749"
RED    = "#9B2C2C"
MUTED  = "#718096"
BORDER = "#E2E8F0"
GOLD   = "#D69E2E"
WHITE  = "#FFFFFF"
ROW    = "#FFFFFF"
URL    = "langworthywatch.org/state-of-the-district/2026-q2/"


def font(name, size):
    try:
        return ImageFont.truetype(f"{FONT_DIR}{name}", size)
    except Exception:
        return ImageFont.load_default()


f_brand = font("Arial Bold.ttf", 22)
f_eyebrow = font("Arial Bold.ttf", 20)
f_title = font("Impact.ttf", 72)
f_title_sm = font("Arial Bold.ttf", 34)
f_sub = font("Arial Bold.ttf", 27)
f_tag = font("Arial.ttf", 23)
f_marq = font("Impact.ttf", 70)
f_marq_lbl = font("Arial Bold.ttf", 18)
f_marq_sub = font("Arial.ttf", 17)
f_cta = font("Arial Bold.ttf", 24)
f_sec = font("Arial Bold.ttf", 20)
f_fig = font("Impact.ttf", 40)
f_line = font("Arial.ttf", 20)
f_foot = font("Arial Bold.ttf", 19)
f_method = font("Arial.ttf", 16)


def base():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([(0, 0), (W, 48)], fill=NAVY)
    d.text((W // 2, 24), "LANGWORTHYWATCH.ORG", fill=WHITE, font=f_brand, anchor="mm")
    d.rectangle([(0, H - 48), (W, H)], fill=NAVY)
    d.text((W // 2, H - 24), URL, fill=WHITE, font=f_foot, anchor="mm")
    return img, d


# ── Slide 1 — cover ──────────────────────────────────────────────────────────
img, d = base()
d.text((W // 2, 150), "INAUGURAL ISSUE", fill=GOLD, font=f_eyebrow, anchor="mm")
d.text((W // 2, 232), "STATE OF THE DISTRICT", fill=NAVY, font=f_title, anchor="mm")
d.text((W // 2, 300), "Q2 2026  ·  NY-23", fill=DARK, font=f_sub, anchor="mm")
d.line([(180, 340), (W - 180, 340)], fill=BORDER, width=2)
d.text((W // 2, 388), "Documented conditions in NY-23, set against the", fill=MUTED, font=f_tag, anchor="mm")
d.text((W // 2, 416), "representative's record — improvements reported", fill=MUTED, font=f_tag, anchor="mm")
d.text((W // 2, 444), "as prominently as harms. The record, not a verdict.", fill=MUTED, font=f_tag, anchor="mm")

# three marquee stats
marq = [
    ("230+", "JOBS LOST", "eSolutions, Jamestown", NAVY),
    ("~450K", "ESSENTIAL PLAN CLIFF", "effective July 1", NAVY),
    ("+25%", "INCOME, CHAUTAUQUA", "credit where due", GREEN),
]
col_w = (W - 88) // 3
top = 520
for i, (fig, lbl, sub, c) in enumerate(marq):
    cx = 44 + col_w * i + col_w // 2
    d.text((cx, top + 40), fig, fill=c, font=f_marq, anchor="mm")
    d.text((cx, top + 96), lbl, fill=c, font=f_marq_lbl, anchor="mm")
    d.text((cx, top + 122), sub, fill=MUTED, font=f_marq_sub, anchor="mm")
    if i < 2:
        x = 44 + col_w * (i + 1)
        d.line([(x, top + 24), (x, top + 116)], fill=BORDER, width=1)

# CTA
cta_y = 720
d.rounded_rectangle([(120, cta_y), (W - 120, cta_y + 88)], radius=10, fill=NAVY)
d.text((W // 2, cta_y + 32), "Read the full Q2 report", fill=WHITE, font=f_cta, anchor="mm")
d.text((W // 2, cta_y + 62), "9 conditions · 8 counties · sources + fact-check links", fill="#CBD5E0", font=f_marq_sub, anchor="mm")

img.save("/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/state_of_district_q2_cover.png", "PNG", optimize=True)

# ── Slide 2 — by the numbers, grouped ────────────────────────────────────────
img, d = base()
d.text((W // 2, 86), "STATE OF THE DISTRICT — Q2 2026", fill=NAVY, font=f_title_sm, anchor="mm")
d.text((W // 2, 120), "By the numbers", fill=MUTED, font=f_method, anchor="mm")

cost = [
    ("230+", "jobs lost — eSolutions / Bush Industries, Jamestown"),
    ("~450K", "lose Essential Plan eligibility on July 1 (NY DOH)"),
    ("~40%", "higher ACA premiums than they'd otherwise be (NY DOH)"),
    ("$1.3M", "WSKG public-broadcasting cut — 21% of its budget"),
    ("$0", "to any named NY-23 hospital yet (of $212M to the state)"),
]
gain = [
    ("$60.5M", "FEMA award — Jasper-Troupsburg rebuild (MOSTLY TRUE)"),
    ("+25%", "Chautauqua median household income since 2019 (nominal)"),
]


def section(d, y, label, color):
    d.rounded_rectangle([(44, y), (W - 44, y + 34)], radius=6, fill=color)
    d.text((64, y + 17), label, fill=WHITE, font=f_sec, anchor="lm")
    return y + 34 + 8


def rows(d, y, items, fig_color):
    fig_w = 168
    tx = 44 + fig_w + 16
    rh = 70
    for fig, desc in items:
        d.rounded_rectangle([(44, y), (W - 44, y + rh)], radius=8, fill=ROW, outline=BORDER, width=2)
        d.text((44 + fig_w // 2, y + rh // 2), fig, fill=fig_color, font=f_fig, anchor="mm")
        d.line([(tx - 8, y + 14), (tx - 8, y + rh - 14)], fill=BORDER, width=1)
        d.text((tx, y + rh // 2), desc, fill=DARK, font=f_line, anchor="lm")
        y += rh + 7
    return y


y = 156
y = section(d, y, "WHAT IT COST", RED)
y = rows(d, y, cost, RED)
y += 8
y = section(d, y, "WHAT CAME IN / IMPROVED", GREEN)
y = rows(d, y, gain, GREEN)
y += 10
d.text((W // 2, y), "Attribution tiers throughout. Full report + sources online.", fill=MUTED, font=f_method, anchor="mm")

img.save("/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/state_of_district_q2_numbers.png", "PNG", optimize=True)
print("Saved: state_of_district_q2_cover.png + state_of_district_q2_numbers.png")
