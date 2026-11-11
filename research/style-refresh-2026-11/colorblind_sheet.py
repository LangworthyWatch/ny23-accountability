#!/usr/bin/env python3
"""Colorblind check: each card under deuteranopia, protanopia and tritanopia (Machado et al. 2009, severity 1.0,
applied in linear RGB). Rows: current-style card, then the three v2 mockups."""
import os, numpy as np
from PIL import Image, ImageDraw, ImageFont
D = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(D, "..", "..")
M = {"deuteranopia": [[0.367322, 0.860646, -0.227968], [0.280085, 0.672501, 0.047413], [-0.011820, 0.042940, 0.968881]],
     "protanopia": [[0.152286, 1.052583, -0.204868], [0.114503, 0.786281, 0.099216], [-0.003882, -0.048116, 1.051998]],
     "tritanopia": [[1.255528, -0.076749, -0.178779], [-0.078411, 0.930809, 0.147602], [0.004733, 0.691367, 0.303900]]}
def sim(im, m):
    a = np.asarray(im.convert("RGB")).astype(np.float64) / 255
    lin = np.where(a <= 0.04045, a / 12.92, ((a + 0.055) / 1.055) ** 2.4)
    out = np.clip(lin @ np.array(m).T, 0, 1)
    srgb = np.where(out <= 0.0031308, out * 12.92, 1.055 * out ** (1 / 2.4) - 0.055)
    return Image.fromarray((srgb * 255).round().astype(np.uint8))
rows = [("Current style", os.path.join(ROOT, "social-media/mandate_card.png")),
        ("A one number", os.path.join(D, "mock-A-one-number.png")),
        ("B said vs record", os.path.join(D, "mock-B-said-vs-record.png")),
        ("C weekly", os.path.join(D, "mock-C-weekly-roundup.png"))]
T = 330; cols = ["normal"] + list(M)
sheet = Image.new("RGB", (160 + len(cols) * (T + 10), 40 + len(rows) * (T + 10)), "white")
dr = ImageDraw.Draw(sheet); f = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 15)
for j, cname in enumerate(cols): dr.text((160 + j * (T + 10), 12), cname, fill="black", font=f)
for i, (rname, p) in enumerate(rows):
    im = Image.open(p).convert("RGB")
    dr.text((8, 40 + i * (T + 10) + T // 2), rname, fill="black", font=f)
    for j, cname in enumerate(cols):
        x = im if cname == "normal" else sim(im, M[cname])
        sheet.paste(x.resize((T, T), Image.LANCZOS), (160 + j * (T + 10), 40 + i * (T + 10)))
sheet.save(os.path.join(D, "colorblind-sheet.png")); print("ok")
