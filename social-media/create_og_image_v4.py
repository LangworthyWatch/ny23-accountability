#!/usr/bin/env python3
"""OG image v4: Clean crop of map from original + new brand text."""

from PIL import Image, ImageDraw, ImageFont
import numpy as np

WIDTH = 1200
HEIGHT = 630
FONT_DIR = "/System/Library/Fonts/Supplemental/"

NAVY = "#1E3A5F"
GOLD = "#D69E2E"
ACCENT = "#2B6CB0"
MUTED = "#A0AEC0"

def font(name, size):
    try:
        return ImageFont.truetype(f"{FONT_DIR}{name}", size)
    except:
        return ImageFont.load_default()

def hex_to_rgb(h):
    return tuple(int(h.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))

# Load original map image
orig = Image.open("/Users/zachbeaudoin/Downloads/langworthy_watch_ny23_119.png").convert("RGBA")

# Crop to just the map portion (right side of image, skip the text on the left)
# Original is 1635x959. The map starts around x=580, text/legend is left of that.
map_crop = orig.crop((580, 30, 1620, 870))

# Convert to numpy for recoloring
arr = np.array(map_crop)
r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]

# In the cropped region, identify:
# Beige background: high R, high G, high B, all close together (R>220, G>215, B>205)
bg_mask = (r > 215) & (g > 210) & (b > 200) & (np.abs(r.astype(int) - g.astype(int)) < 20)

# NY-23 (dark teal/green): clearly darker and greener
ny23_mask = (g > 100) & (r < 130) & (b < 130) & (a > 200) & ~bg_mask

# State area (sage/light green): moderate values, greener than beige
state_mask = (r > 140) & (r < 225) & (g > 160) & (g < 230) & (a > 200) & ~bg_mask & ~ny23_mask
# Filter out remaining text artifacts (text tends to have R≈G≈B, gray-ish)
green_bias = g.astype(int) - ((r.astype(int) + b.astype(int)) // 2)
state_mask = state_mask & (green_bias > -5)  # Must have at least slight green tint

# Border lines
border_mask = (r > 90) & (r < 170) & (g > 100) & (g < 185) & (a > 200) & ~bg_mask & ~ny23_mask & ~state_mask

# Any remaining text artifacts - treat as background
# Text pixels that snuck through: typically have equal R,G,B (grayscale)
gray_diff = np.abs(r.astype(int) - g.astype(int)) + np.abs(g.astype(int) - b.astype(int))

# Recolor
new_arr = np.full_like(arr, 255)  # White background
new_arr[:,:,3] = 255

# State in light steel blue
steel = hex_to_rgb("#C8D5E3")
new_arr[state_mask] = [*steel, 255]

# Borders slightly darker
border_c = hex_to_rgb("#A8BDD0")
new_arr[border_mask] = [*border_c, 255]

# NY-23 in gold
gold_c = hex_to_rgb(GOLD)
new_arr[ny23_mask] = [*gold_c, 255]

# Make background transparent
new_arr[bg_mask] = [255, 255, 255, 0]

# Also make pure white transparent (text remnants on white)
white_mask = (r > 240) & (g > 240) & (b > 240)
new_arr[white_mask] = [255, 255, 255, 0]

map_recolored = Image.fromarray(new_arr, "RGBA")

# Find non-transparent bounding box
alpha_arr = new_arr[:,:,3]
non_transparent = alpha_arr > 10
rows = np.any(non_transparent, axis=1)
cols = np.any(non_transparent, axis=0)
if rows.any() and cols.any():
    rmin, rmax = np.where(rows)[0][[0, -1]]
    cmin, cmax = np.where(cols)[0][[0, -1]]
    map_recolored = map_recolored.crop((cmin-5, rmin-5, cmax+5, rmax+5))

# Scale to fit
target_h = HEIGHT - 60
ratio = map_recolored.width / map_recolored.height
target_w = int(target_h * ratio)
if target_w > 680:
    target_w = 680
    target_h = int(target_w / ratio)
map_recolored = map_recolored.resize((target_w, target_h), Image.LANCZOS)

# --- Build final OG image ---
img = Image.new("RGBA", (WIDTH, HEIGHT), (255, 255, 255, 255))

# Place map on right, slightly overflowing
map_x = WIDTH - target_w + 60
map_y = (HEIGHT - target_h) // 2
img.paste(map_recolored, (map_x, map_y), map_recolored)

# Soft white fade from left over map edge so text stays clean
fade = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
fade_draw = ImageDraw.Draw(fade)
for x in range(WIDTH):
    if x < 480:
        a = 255
    elif x < 620:
        a = int(255 * (1 - (x - 480) / 140))
    else:
        a = 0
    fade_draw.line([(x, 0), (x, HEIGHT)], fill=(255, 255, 255, a))
img = Image.alpha_composite(img, fade)

# Convert to RGB for drawing text
draw = ImageDraw.Draw(img)

# --- Text ---
f_brand = font("Arial Bold.ttf", 58)
f_tagline = font("Arial.ttf", 26)
f_tagline_bold = font("Arial Bold.ttf", 26)
f_district = font("Arial Bold.ttf", 17)
f_url = font("Arial Bold.ttf", 24)
f_sub = font("Arial.ttf", 19)

# Brand name
draw.text((55, 155), "LangworthyWatch", fill=hex_to_rgb(NAVY), font=f_brand, anchor="lm")

# Gold rule
draw.rectangle([(55, 195), (185, 201)], fill=hex_to_rgb(GOLD))

# Tagline
draw.text((55, 230), "Statements vs. voting record.", fill=hex_to_rgb("#1A202C"), font=f_tagline_bold, anchor="lm")
draw.text((55, 264), "Public data. No opinion.", fill=hex_to_rgb("#4A5568"), font=f_tagline, anchor="lm")

# District
draw.text((55, HEIGHT - 100), "NY-23  \u00b7  119th Congress", fill=hex_to_rgb(GOLD), font=f_district, anchor="lm")
draw.text((55, HEIGHT - 75), "Southern Tier & Western New York", fill=hex_to_rgb(MUTED), font=f_sub, anchor="lm")

# URL
draw.text((55, HEIGHT - 35), "langworthywatch.org", fill=hex_to_rgb(ACCENT), font=f_url, anchor="lm")

# Save as RGB
final = img.convert("RGB")
out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/static/images/og-image.png"
final.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
