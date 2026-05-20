#!/usr/bin/env python3
"""OG image v3: Clean brand + recolored NY-23 map from original asset."""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np

WIDTH = 1200
HEIGHT = 630
FONT_DIR = "/System/Library/Fonts/Supplemental/"

NAVY = "#1E3A5F"
WHITE = "#FFFFFF"
ACCENT = "#2B6CB0"
GOLD = "#D69E2E"
MUTED = "#A0AEC0"
LIGHT_BLUE = "#EBF4FF"
OFF_WHITE = "#F5F7FA"

def font(name, size):
    try:
        return ImageFont.truetype(f"{FONT_DIR}{name}", size)
    except:
        return ImageFont.load_default()

def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

# Load and process the original map
orig = Image.open("/Users/zachbeaudoin/Downloads/langworthy_watch_ny23_119.png").convert("RGBA")
orig_arr = np.array(orig)

# Identify map regions by color:
# Background (beige): ~(230, 226, 220) - R>220, G>215, B>210, close together
# NY-23 (dark green): R<100, G>100, B<100 — the highlighted district
# Other districts (light sage): R~190-210, G~200-215, B~185-200
# District borders (gray lines): darker than sage but not as dark as NY-23

# Create masks
r, g, b, a = orig_arr[:,:,0], orig_arr[:,:,1], orig_arr[:,:,2], orig_arr[:,:,3]

# NY-23 district: distinctly greener/darker than surroundings
ny23_mask = (g > 120) & (r < 120) & (b < 120) & (a > 200)

# Other state area: sage green (R:180-220, G:195-225, B:180-210)
state_mask = (r > 160) & (r < 230) & (g > 180) & (g < 230) & (b > 160) & (b < 215) & (a > 200)
# Exclude background (where R,G,B are all very close and high)
not_bg = ~((r > 220) & (g > 218) & (b > 210) & ((r.astype(int) - b.astype(int)) < 25))
state_mask = state_mask & not_bg & ~ny23_mask

# Border lines: darker than state, lighter than NY-23
border_mask = (r > 100) & (r < 185) & (g > 110) & (g < 200) & (b > 95) & (b < 190) & (a > 200)
border_mask = border_mask & ~ny23_mask & ~state_mask & not_bg

# Build recolored map
ny23_color = hex_to_rgb(GOLD)       # Gold for NY-23 (the focus)
state_color = hex_to_rgb("#C5D1DE")  # Light steel blue for rest of state
border_color = hex_to_rgb("#9BAFCA") # Slightly darker for borders
bg_color = hex_to_rgb(WHITE)         # White background

new_arr = np.full_like(orig_arr, 255)  # Start white
new_arr[:,:,3] = 255  # Full opacity

# Apply colors
new_arr[ny23_mask] = [*ny23_color, 255]
new_arr[state_mask] = [*state_color, 255]
new_arr[border_mask] = [*border_color, 255]

map_img = Image.fromarray(new_arr, "RGBA")

# Crop to just the map area (trim whitespace)
# Find bounding box of non-white pixels
non_white = np.any(new_arr[:,:,:3] != 255, axis=2)
rows = np.any(non_white, axis=1)
cols = np.any(non_white, axis=0)
if rows.any() and cols.any():
    rmin, rmax = np.where(rows)[0][[0, -1]]
    cmin, cmax = np.where(cols)[0][[0, -1]]
    # Add small padding
    pad = 20
    rmin = max(0, rmin - pad)
    rmax = min(new_arr.shape[0], rmax + pad)
    cmin = max(0, cmin - pad)
    cmax = min(new_arr.shape[1], cmax + pad)
    map_img = map_img.crop((cmin, rmin, cmax, rmax))

# Scale map to fit right side of OG image
map_target_h = HEIGHT - 40  # Leave some margin
map_ratio = map_img.width / map_img.height
map_target_w = int(map_target_h * map_ratio)
if map_target_w > 650:  # Cap width
    map_target_w = 650
    map_target_h = int(map_target_w / map_ratio)
map_img = map_img.resize((map_target_w, map_target_h), Image.LANCZOS)

# --- Build the OG image ---
img = Image.new("RGB", (WIDTH, HEIGHT), WHITE)
draw = ImageDraw.Draw(img)

# Paste map on right side (slightly extending off edge for dynamic feel)
map_x = WIDTH - map_target_w + 40  # Let it bleed slightly right
map_y = (HEIGHT - map_target_h) // 2
img.paste(map_img, (map_x, map_y), map_img)

# Semi-transparent overlay gradient from left to make text area clean
# Draw a white-to-transparent gradient over the left portion
overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
overlay_draw = ImageDraw.Draw(overlay)
# Solid white on left, fading out
for x in range(600):
    alpha = 255 if x < 450 else int(255 * (1 - (x - 450) / 150))
    overlay_draw.line([(x, 0), (x, HEIGHT)], fill=(255, 255, 255, alpha))
img_rgba = img.convert("RGBA")
img_rgba = Image.alpha_composite(img_rgba, overlay)
img = img_rgba.convert("RGB")
draw = ImageDraw.Draw(img)

# --- Text content (left side) ---
f_brand = font("Arial Bold.ttf", 54)
f_tagline = font("Arial.ttf", 24)
f_tagline_bold = font("Arial Bold.ttf", 24)
f_district = font("Arial Bold.ttf", 16)
f_url = font("Arial Bold.ttf", 22)
f_subtitle = font("Arial.ttf", 18)

# Brand
y = 140
draw.text((60, y), "LangworthyWatch", fill=hex_to_rgb(NAVY), font=f_brand, anchor="lm")

# Gold accent line
draw.rectangle([(60, y + 35), (180, y + 41)], fill=hex_to_rgb(GOLD))

# Tagline — the key message
y += 70
draw.text((60, y), "Statements vs. voting record.", fill=hex_to_rgb("#1A202C"), font=f_tagline_bold, anchor="lm")
y += 34
draw.text((60, y), "Public data. No opinion.", fill=hex_to_rgb("#4A5568"), font=f_tagline, anchor="lm")

# District label
y = HEIGHT - 110
draw.text((60, y), "NY-23  \u00b7  119th Congress", fill=hex_to_rgb(GOLD), font=f_district, anchor="lm")
y += 28
draw.text((60, y), "Southern Tier & Western New York", fill=hex_to_rgb(MUTED), font=f_subtitle, anchor="lm")

# URL
draw.text((60, HEIGHT - 35), "langworthywatch.org", fill=hex_to_rgb(ACCENT), font=f_url, anchor="lm")

# Save
out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/static/images/og-image.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
print(f"Size: {img.size}")
