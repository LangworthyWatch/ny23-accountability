#!/usr/bin/env python3
"""State of the District — Q2 2026 social carousel.
Slide 1: clean cover (launch). Slide 2: by-the-numbers, grouped by valence.

Rendered at 3x and downsampled with LANCZOS (supersampling) for crisp text.
"""

from PIL import Image, ImageDraw, ImageFont

SC = 3                      # supersample factor
W = H = 1080               # logical (output) dimensions
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
        return ImageFont.truetype(f"{FONT_DIR}{name}", size * SC)
    except Exception:
        return ImageFont.load_default()


# scale helpers (logical -> supersampled device pixels)
def P(v):
    return int(round(v * SC))


def XY(x, y):
    return (P(x), P(y))


def BOX(x1, y1, x2, y2):
    return [XY(x1, y1), XY(x2, y2)]


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
    img = Image.new("RGB", (P(W), P(H)), BG)
    d = ImageDraw.Draw(img)
    d.rectangle(BOX(0, 0, W, 48), fill=NAVY)
    d.text(XY(W // 2, 24), "LANGWORTHYWATCH.ORG", fill=WHITE, font=f_brand, anchor="mm")
    d.rectangle(BOX(0, H - 48, W, H), fill=NAVY)
    d.text(XY(W // 2, H - 24), URL, fill=WHITE, font=f_foot, anchor="mm")
    return img, d


def finish(img, name):
    img = img.resize((W, H), Image.LANCZOS)
    out = f"/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/{name}"
    img.save(out, "PNG", optimize=True)


# ── Slide 1 — cover ──────────────────────────────────────────────────────────
img, d = base()
d.text(XY(W // 2, 150), "INAUGURAL ISSUE", fill=GOLD, font=f_eyebrow, anchor="mm")
d.text(XY(W // 2, 232), "STATE OF THE DISTRICT", fill=NAVY, font=f_title, anchor="mm")
d.text(XY(W // 2, 300), "Q2 2026  ·  NY-23", fill=DARK, font=f_sub, anchor="mm")
d.line([XY(180, 340), XY(W - 180, 340)], fill=BORDER, width=P(2))
d.text(XY(W // 2, 388), "Documented conditions in NY-23, set against the", fill=MUTED, font=f_tag, anchor="mm")
d.text(XY(W // 2, 416), "representative's record. Improvements reported", fill=MUTED, font=f_tag, anchor="mm")
d.text(XY(W // 2, 444), "as prominently as harms. The record, not a verdict.", fill=MUTED, font=f_tag, anchor="mm")

marq = [
    ("230+", "JOBS LOST", "eSolutions, Jamestown", NAVY),
    ("~450K", "ESSENTIAL PLAN CLIFF", "effective July 1", NAVY),
    ("$60.5M", "FEMA AWARD", "his claim checks out", GREEN),
]
col_w = (W - 88) // 3
top = 540
for i, (fig, lbl, sub, c) in enumerate(marq):
    cx = 44 + col_w * i + col_w // 2
    d.text(XY(cx, top + 40), fig, fill=c, font=f_marq, anchor="mm")
    d.text(XY(cx, top + 96), lbl, fill=c, font=f_marq_lbl, anchor="mm")
    d.text(XY(cx, top + 122), sub, fill=MUTED, font=f_marq_sub, anchor="mm")
    if i < 2:
        x = 44 + col_w * (i + 1)
        d.line([XY(x, top + 24), XY(x, top + 116)], fill=BORDER, width=P(1))

cta_y = 748
d.rounded_rectangle(BOX(120, cta_y, W - 120, cta_y + 88), radius=P(10), fill=NAVY)
d.text(XY(W // 2, cta_y + 32), "Read the full Q2 report", fill=WHITE, font=f_cta, anchor="mm")
d.text(XY(W // 2, cta_y + 62), "conditions across 8 counties · sources + fact-check links", fill="#CBD5E0", font=f_marq_sub, anchor="mm")

finish(img, "state_of_district_q2_cover.png")

# ── Slide 2 — by the numbers, grouped ────────────────────────────────────────
img, d = base()
d.text(XY(W // 2, 86), "STATE OF THE DISTRICT · Q2 2026", fill=NAVY, font=f_title_sm, anchor="mm")
d.text(XY(W // 2, 120), "By the numbers", fill=MUTED, font=f_method, anchor="mm")

cost = [
    ("230+", "jobs lost: eSolutions / Bush Industries, Jamestown"),
    ("~450K", "lose Essential Plan eligibility on July 1 (NY DOH)"),
    ("~40%", "higher ACA premiums than they'd otherwise be (NY DOH)"),
    ("$1.3M", "WSKG public-broadcasting cut, 21% of its budget"),
    ("$0", "to any named NY-23 hospital yet (of $212M to the state)"),
    ("+50%", "severe VA staffing shortages in a year (VA-wide, OIG)"),
]
gain = [
    ("$60.5M", "FEMA award: Jasper-Troupsburg rebuild (MOSTLY TRUE)"),
]


def section(d, y, label, color):
    d.rounded_rectangle(BOX(44, y, W - 44, y + 34), radius=P(6), fill=color)
    d.text(XY(64, y + 17), label, fill=WHITE, font=f_sec, anchor="lm")
    return y + 34 + 8


def rows(d, y, items, fig_color):
    fig_w = 168
    tx = 44 + fig_w + 16
    rh = 74
    for fig, desc in items:
        d.rounded_rectangle(BOX(44, y, W - 44, y + rh), radius=P(8), fill=ROW, outline=BORDER, width=P(2))
        d.text(XY(44 + fig_w // 2, y + rh // 2), fig, fill=fig_color, font=f_fig, anchor="mm")
        d.line([XY(tx - 8, y + 14), XY(tx - 8, y + rh - 14)], fill=BORDER, width=P(1))
        d.text(XY(tx, y + rh // 2), desc, fill=DARK, font=f_line, anchor="lm")
        y += rh + 8
    return y


y = 168
y = section(d, y, "WHAT IT COST", RED)
y = rows(d, y, cost, RED)
y += 10
y = section(d, y, "WHAT CAME IN / IMPROVED", GREEN)
y = rows(d, y, gain, GREEN)
y += 14
d.text(XY(W // 2, y), "Attribution tiers throughout. Full report + sources online.", fill=MUTED, font=f_method, anchor="mm")

finish(img, "state_of_district_q2_numbers.png")
print("Saved cover + numbers (3x supersampled).")
