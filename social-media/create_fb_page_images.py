#!/usr/bin/env python3
"""Facebook page identity images, Nov 20, 2026 (house style v2.2).
- fb_profile.png: 1080x1080, the LW favicon mark (navy, white LW, amber rule), scaled to sit inside
  Facebook's circular crop.
- fb_cover.png: 1640x624, navy, site name + one-line description, centered so it survives the
  desktop and mobile crops and stays clear of the profile photo at lower left.
No photo of Rep. Langworthy: a page identity built on his face can read as his own page."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw, ImageFont
from lib.card import FONT_DIR

NAVY = (0x1E, 0x3A, 0x5F); WHITE = (255, 255, 255); AMBER = (0xD6, 0x9E, 0x2E)
GOLD_LIGHT = (0xF6, 0xD5, 0x8E); ON_NAVY = (0xC9, 0xD3, 0xE0)
OUT = os.path.dirname(os.path.abspath(__file__))
S = 2  # supersample


def font(name, px):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), int(px * S))


def centered(d, cx, y, text, f, fill):
    bb = d.textbbox((0, 0), text, font=f)
    d.text((cx * S - (bb[2] - bb[0]) / 2 - bb[0], y * S - bb[1]), text, font=f, fill=fill)
    return (bb[3] - bb[1]) / S


def profile(path):
    W = 1080
    im = Image.new("RGB", (W * S, W * S), NAVY); d = ImageDraw.Draw(im)
    f = font("Arial Black.ttf", 400)
    bb = d.textbbox((0, 0), "LW", font=f)
    tw, th = (bb[2] - bb[0]) / S, (bb[3] - bb[1]) / S
    bar_h, gap = 56, 70
    block = th + gap + bar_h
    y0 = (W - block) / 2
    centered(d, W / 2, y0, "LW", f, WHITE)
    bw = tw * 1.04
    d.rectangle([(W / 2 - bw / 2) * S, (y0 + th + gap) * S, (W / 2 + bw / 2) * S, (y0 + th + gap + bar_h) * S], fill=AMBER)
    im.resize((W, W), Image.LANCZOS).save(path)
    # circle-safety check: every corner of the mark must sit inside the inscribed circle
    r = W / 2
    corners = [(W / 2 - bw / 2, y0 + th + gap + bar_h), (W / 2 + bw / 2, y0 + th + gap + bar_h),
               (W / 2 - tw / 2, y0), (W / 2 + tw / 2, y0)]
    worst = max(((x - r) ** 2 + (y - r) ** 2) ** 0.5 for x, y in corners)
    print(f"Saved: {path}  (farthest corner {worst:.0f}px from center; circle radius {r:.0f}px)")


def cover(path):
    W, H = 1640, 624
    im = Image.new("RGB", (W * S, H * S), NAVY); d = ImageDraw.Draw(im)
    cx = W / 2
    y = 150
    y += centered(d, cx, y, "LANGWORTHYWATCH.ORG", font("Arial Bold.ttf", 30), GOLD_LIGHT) + 40
    y += centered(d, cx, y, "What NY-23’s congressman says,", font("Arial Bold.ttf", 62), WHITE) + 22
    y += centered(d, cx, y, "checked against the public record.", font("Arial Bold.ttf", 62), WHITE) + 44
    d.rectangle([(cx - 90) * S, y * S, (cx + 90) * S, (y + 8) * S], fill=AMBER)
    y += 8 + 36
    centered(d, cx, y, "Votes · Statements · Primary sources · Corrections", font("Arial.ttf", 28), ON_NAVY)
    im.resize((W, H), Image.LANCZOS).save(path)
    print(f"Saved: {path}")


if __name__ == "__main__":
    profile(os.path.join(OUT, "fb_profile.png"))
    cover(os.path.join(OUT, "fb_cover.png"))
