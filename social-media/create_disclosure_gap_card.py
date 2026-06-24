#!/usr/bin/env python3
"""Social card: The Disclosure Gap — donor-to-action pattern — DOCUMENTED PATTERN — June 24, 2026."""

from PIL import Image, ImageDraw, ImageFont

WIDTH  = 1080
HEIGHT = 1080
FONT_DIR = "/System/Library/Fonts/Supplemental/"

BG      = "#F5F7FA"
NAVY    = "#1E3A5F"
DARK    = "#1A202C"
GREEN   = "#276749"
RED     = "#E53E3E"
ORANGE  = "#C05621"
GOLD    = "#D69E2E"
MUTED   = "#718096"
BORDER  = "#E2E8F0"
WHITE   = "#FFFFFF"

def font(name, size):
    try:
        return ImageFont.truetype(f"{FONT_DIR}{name}", size)
    except:
        return ImageFont.load_default()

f_brand  = font("Arial Bold.ttf", 22)
f_tag    = font("Arial Bold.ttf", 20)
f_topic  = font("Arial Bold.ttf", 38)
f_subb   = font("Arial Bold.ttf", 21)
f_sub    = font("Arial.ttf", 20)
f_donor  = font("Arial Bold.ttf", 19)
f_amt    = font("Impact.ttf", 46)
f_action = font("Arial Bold.ttf", 20)
f_note_s = font("Arial.ttf", 14)
f_arrow  = font("Arial Bold.ttf", 30)
f_thread = font("Arial Bold.ttf", 21)
f_note_b = font("Arial Bold.ttf", 17)
f_note   = font("Arial.ttf", 17)
f_small  = font("Arial.ttf", 18)
f_footer = font("Arial Bold.ttf", 20)

img  = Image.new("RGB", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

# Header
draw.rectangle([(0, 0), (WIDTH, 48)], fill=NAVY)
draw.text((WIDTH // 2, 24), "LANGWORTHYWATCH.ORG", fill=WHITE, font=f_brand, anchor="mm")

y = 62

# Verdict badge
tag = "DOCUMENTED PATTERN"
tb = draw.textbbox((0, 0), tag, font=f_tag)
tw, th = tb[2]-tb[0]+28, tb[3]-tb[1]+12
draw.rounded_rectangle([((WIDTH-tw)//2, y), ((WIDTH+tw)//2, y+th)], radius=5,
                       fill="#744210", outline=GOLD, width=2)
draw.text((WIDTH//2, y+th//2), tag, fill=GOLD, font=f_tag, anchor="mm")
y += th + 12

# Topic
draw.text((WIDTH//2, y+20), "The Disclosure Gap", fill=NAVY, font=f_topic, anchor="mm")
y += 46
draw.line([(60, y), (WIDTH-60, y)], fill=BORDER, width=2)
y += 16

# Framing
draw.text((WIDTH//2, y+10), "Donations are public. His votes are public.", fill=DARK, font=f_subb, anchor="mm")
draw.text((WIDTH//2, y+38), "The link between them is the part his announcements leave out.", fill=MUTED, font=f_sub, anchor="mm")
y += 64

# Donor -> action rows
rows = [
    ("Seneca Nation",          "$10,100", "in the 2 years before the bill",
     ["Introduced a bill to strip New York's", "jurisdiction over Seneca Nation lands"]),
    ("Nursing-home operator",  "$68,700", "every dollar before the vote",
     ["Voted to block the federal nursing-", "home staffing rule for ten years"]),
    ("Corning employees (62)", "$65,775", "around the reconciliation bill",
     ["Voted for the bill that preserved its", "manufacturing tax credits"]),
    ("Homebuilders' PAC",      "$16,500", "2022 to 2026",
     ['Publicized their "Defender of', 'Housing" award']),
]

row_h, gap = 120, 12
for i, (donor, amt, note, action) in enumerate(rows):
    ry = y + i*(row_h+gap)
    draw.rounded_rectangle([(44, ry), (WIDTH-44, ry+row_h)], radius=8, fill=WHITE, outline=BORDER, width=2)
    # green left accent
    draw.rectangle([(47, ry+4), (55, ry+row_h-4)], fill="#9AE6B4")
    draw.text((80, ry+28), donor, fill=NAVY, font=f_donor, anchor="lm")
    draw.text((80, ry+68), amt, fill=GREEN, font=f_amt, anchor="lm")
    draw.text((80, ry+100), note, fill=MUTED, font=f_note_s, anchor="lm")
    draw.text((418, ry+60), "→", fill=MUTED, font=f_arrow, anchor="mm")
    draw.text((462, ry+46), action[0], fill=DARK, font=f_action, anchor="lm")
    draw.text((462, ry+78), action[1], fill=DARK, font=f_action, anchor="lm")

y += 4*(row_h+gap) + 6

# Thread line
draw.text((WIDTH//2, y+12), "In each announcement, the donor relationship is the part left out.",
          fill=NAVY, font=f_thread, anchor="mm")
y += 38

# Caveat box
cav_h = 86
draw.rounded_rectangle([(44, y), (WIDTH-44, y+cav_h)], radius=6, fill="#EDF2F7", outline=BORDER, width=1)
draw.text((WIDTH//2, y+26), "We are not claiming any donation bought a vote. Contributions are legal.",
          fill=DARK, font=f_note_b, anchor="mm")
draw.text((WIDTH//2, y+54), "The records are public. The connection is the part left unsaid.",
          fill=MUTED, font=f_note, anchor="mm")
y += cav_h + 18

# Sources + URL
draw.text((WIDTH//2, y), "Sources: FEC  ·  congress.gov  ·  clerk.house.gov roll-call votes",
          fill=MUTED, font=f_small, anchor="mm")
y += 26
draw.text((WIDTH//2, y), "langworthywatch.org/fact-checks/2026-06-24-disclosure-gap-donor-pattern/",
          fill=NAVY, font=f_small, anchor="mm")

# Footer
draw.rectangle([(0, HEIGHT-50), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH//2, HEIGHT-25), "langworthywatch.org  ·  NY-23 Accountability",
          fill=WHITE, font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/disclosure_gap_donor_pattern.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
