#!/usr/bin/env python3
"""Social card: AAPD / Medicaid CONTRADICTION — May 18, 2026."""

from PIL import Image, ImageDraw, ImageFont

WIDTH = 1080
HEIGHT = 1080
FONT_DIR = "/System/Library/Fonts/Supplemental/"

BG      = "#F5F7FA"
NAVY    = "#1E3A5F"
DARK    = "#1A202C"
RED     = "#E53E3E"
GREEN   = "#276749"   # for the "promise" side
MUTED   = "#718096"
BORDER  = "#E2E8F0"
GOLD    = "#D69E2E"
WHITE   = "#FFFFFF"

def font(name, size):
    try:
        return ImageFont.truetype(f"{FONT_DIR}{name}", size)
    except:
        return ImageFont.load_default()

def wrap(text, font_obj, max_w, draw):
    words = text.split()
    lines, line = [], []
    for w in words:
        test = " ".join(line + [w])
        bbox = draw.textbbox((0, 0), test, font=font_obj)
        if bbox[2] - bbox[0] <= max_w:
            line.append(w)
        else:
            if line:
                lines.append(" ".join(line))
            line = [w]
    if line:
        lines.append(" ".join(line))
    return lines

f_brand    = font("Arial Bold.ttf", 24)
f_tag      = font("Arial Bold.ttf", 22)
f_verdict  = font("Arial Bold.ttf", 36)
f_label    = font("Arial Bold.ttf", 24)
f_quote    = font("Arial.ttf", 30)
f_quote_b  = font("Arial Bold.ttf", 30)
f_big      = font("Impact.ttf", 130)
f_big_sub  = font("Arial Bold.ttf", 30)
f_sub      = font("Arial.ttf", 24)
f_source   = font("Arial.ttf", 20)
f_footer   = font("Arial Bold.ttf", 22)

img  = Image.new("RGB", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

# ── Header ──
draw.rectangle([(0, 0), (WIDTH, 52)], fill=NAVY)
draw.text((WIDTH // 2, 26), "LANGWORTHYWATCH.ORG", fill=WHITE, font=f_brand, anchor="mm")

y = 74

# ── Verdict badge ──
tag = "CONTRADICTION"
tb = draw.textbbox((0, 0), tag, font=f_tag)
tw = tb[2] - tb[0] + 28
th = tb[3] - tb[1] + 14
tx = (WIDTH - tw) // 2
draw.rounded_rectangle([(tx, y), (tx + tw, y + th)], radius=5, fill=RED)
draw.text((WIDTH // 2, y + th // 2), tag, fill=WHITE, font=f_tag, anchor="mm")
y += th + 12

# ── Topic ──
draw.text((WIDTH // 2, y), "Medicaid & Disability", fill=NAVY, font=f_verdict, anchor="mm")
y += 44

draw.line([(60, y), (WIDTH - 60, y)], fill=BORDER, width=2)
y += 20

# ── HIS PROMISE (left-tinted box) ──
box_h = 178
draw.rounded_rectangle([(44, y), (WIDTH - 44, y + box_h)], radius=8,
                        fill="#EBF8F0", outline="#9AE6B4", width=2)
draw.text((76, y + 18), "HE SAID — May 18, 2026", fill=GREEN, font=f_label, anchor="lm")
quote = '"I\'ll keep working to protect critical\nsupport systems and improve opportunities\nfor disabled Americans."'
draw.text((76, y + 48), quote, fill=DARK, font=f_quote)
y += box_h + 22

# ── VS ──
draw.text((WIDTH // 2, y), "▼  TEN MONTHS EARLIER  ▼", fill=MUTED, font=f_sub, anchor="mm")
y += 36

# ── HIS VOTE (red box) ──
box_h2 = 178
draw.rounded_rectangle([(44, y), (WIDTH - 44, y + box_h2)], radius=8,
                        fill="#FFF5F5", outline="#FEB2B2", width=2)
draw.text((76, y + 18), "HE VOTED — Roll Call 190, July 3, 2025", fill=RED, font=f_label, anchor="lm")
draw.text((76, y + 54), "YEA  on the One Big Beautiful Bill Act", fill=DARK, font=f_quote_b, anchor="lm")
draw.text((76, y + 94), "CBO: $840 billion in Medicaid cuts", fill=RED, font=f_quote_b, anchor="lm")
draw.text((76, y + 134), "10 million Americans lose coverage by 2034", fill="#4A5568", font=f_sub, anchor="lm")
y += box_h2 + 24

# ── AAPD response — navy box, large quote ──
f_aapd_label = font("Arial.ttf", 22)
f_aapd_quote = font("Arial Bold.ttf", 36)
aapd_box_h = 196
draw.rounded_rectangle([(44, y), (WIDTH - 44, y + aapd_box_h)], radius=8, fill=NAVY)
draw.text((WIDTH // 2, y + 22), "AAPD President & CEO Maria Town — on the same law:", fill="#A0AEC0", font=f_aapd_label, anchor="mm")
draw.text((WIDTH // 2, y + 72), '"This Is A Devastating Day', fill=WHITE, font=f_aapd_quote, anchor="mm")
draw.text((WIDTH // 2, y + 114), "for Disabled Americans.”", fill=WHITE, font=f_aapd_quote, anchor="mm")
draw.text((WIDTH // 2, y + 158), "— AAPD press release, July 3, 2025", fill=GOLD, font=f_aapd_label, anchor="mm")
y += aapd_box_h + 20

# ── Source line ──
draw.text((WIDTH // 2, y), "Sources: CBO pub. 61510  ·  clerk.house.gov Roll Call 190  ·  aapd.com",
          fill=MUTED, font=f_source, anchor="mm")
y += 26
draw.text((WIDTH // 2, y), "langworthywatch.org/fact-checks/2026-05-18-aapd-medicaid-disability-contradiction",
          fill=MUTED, font=f_source, anchor="mm")

# ── Footer ──
draw.rectangle([(0, HEIGHT - 56), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH // 2, HEIGHT - 28), "langworthywatch.org  ·  NY-23 Accountability", fill=WHITE, font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/aapd_medicaid_contradiction.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
