#!/usr/bin/env python3
"""LangworthyWatch favicon: navy tile, white LW (Arial Black), gold rule. Colors from assets/css/bundle.css
(--color-primary #1e3a5f) and social-media/lib/card.py (GOLD #D69E2E). Writes into static/."""
import os
from PIL import Image, ImageDraw, ImageFont
NAVY = (0x1E, 0x3A, 0x5F); GOLD = (0xD6, 0x9E, 0x2E); WHITE = (255, 255, 255)
FONT = "/System/Library/Fonts/Supplemental/Arial Black.ttf"
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")

def master(n=1024, rounded=True, rule=True):
    im = Image.new("RGBA", (n, n), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    if rounded: d.rounded_rectangle([0, 0, n - 1, n - 1], radius=int(n * 0.18), fill=NAVY)
    else: d.rectangle([0, 0, n, n], fill=NAVY)
    f = ImageFont.truetype(FONT, int(n * 0.50))
    text = "LW"
    bb = d.textbbox((0, 0), text, font=f)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    # fit width to 78% of tile
    if tw > n * 0.80:
        f = ImageFont.truetype(FONT, int(n * 0.50 * (n * 0.80) / tw)); bb = d.textbbox((0, 0), text, font=f)
        tw, th = bb[2] - bb[0], bb[3] - bb[1]
    y_text = (n - th) / 2 - bb[1] - (n * 0.06 if rule else 0)
    d.text(((n - tw) / 2 - bb[0], y_text), text, font=f, fill=WHITE)
    if rule:
        rh = n * 0.075; ry = y_text + bb[1] + th + n * 0.07
        d.rectangle([(n - tw) / 2, ry, (n + tw) / 2, ry + rh], fill=GOLD)
    return im

big = master(1024)
big.save(os.path.join(ROOT, "research/favicon/favicon-master-1024.png"))
sizes = {}
for s in (16, 32, 48):
    src = master(512, rounded=True, rule=(s >= 32))   # drop the rule at 16 px so the letters keep the room
    sizes[s] = src.resize((s, s), Image.LANCZOS)
sizes[16].save(os.path.join(ROOT, "static/favicon-16x16.png"))
sizes[32].save(os.path.join(ROOT, "static/favicon-32x32.png"))
master(512, rounded=True).resize((48, 48), Image.LANCZOS).save(
    os.path.join(ROOT, "static/favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)],
    append_images=[sizes[16], sizes[32]])
# Apple touch icon: opaque, square corners (iOS applies its own mask)
master(1024, rounded=False).resize((180, 180), Image.LANCZOS).convert("RGB").save(os.path.join(ROOT, "static/apple-touch-icon.png"))
for s in (192, 512):
    master(1024, rounded=False).resize((s, s), Image.LANCZOS).convert("RGB").save(os.path.join(ROOT, f"static/icon-{s}.png"))
# preview sheet: each size at 1x and enlarged 8x nearest-neighbor, on light and dark
sheet = Image.new("RGB", (1100, 520), (250, 250, 250))
x = 20
for s in (16, 32, 48):
    im = sizes[s] if s != 48 else master(512).resize((48, 48), Image.LANCZOS)
    for bg, yoff in (((250, 250, 250), 20), ((32, 33, 36), 270)):
        tile = Image.new("RGB", (s * 5 + 40, 230), bg)
        tile.paste(im, (10, 10), im)
        big8 = im.resize((s * 4, s * 4), Image.NEAREST) if s <= 48 else im
        tile.paste(big8, (10, 40 + s), big8)
        sheet.paste(tile, (x, yoff))
    x += s * 5 + 60
sheet.paste(big.resize((240, 240), Image.LANCZOS), (840, 20), big.resize((240, 240), Image.LANCZOS))
sheet.save(os.path.join(ROOT, "research/favicon/preview.png"))
print("ok")
