#!/usr/bin/env python3
"""
LangworthyWatch social-card toolkit — shared Pillow primitives for the house style.

Every card this project makes is a light 1080x1080 with a navy brand bar, an optional
gold verdict badge, panels/bullets/kicker, and a navy footer. Before this module each
card re-implemented all of that by hand (and colors/spacing drifted). Use this instead.

Design rules it enforces:
- House palette (below), navy bars, gold badge, no em dashes in RENDERED text.
- You write coordinates and font sizes in LOGICAL 1080-space; pass scale=2 or 3 to the
  Card constructor for supersampled (smooth) output and everything scales for free.
- save() auto-checks every rendered string for em dashes and raises if it finds one, and
  can drop a copy on the Desktop for posting.

Minimal usage:
    from lib.card import Card, NAVY, RED, GREEN
    c = Card()                                  # 1080x1080, light bg
    c.brand_bar()
    y = c.badge(64, "DOCUMENTED PATTERN")       # returns next y
    y = c.title(y, "A Seat at the Table")
    y = c.subtitle(y, "His own words, and the record.")
    y = c.divider(y)
    c.panel(44, y, c.w-44, y+120)               # rounded panel
    c.bullets(70, y, ["Point one", "Point two"], RED)
    c.kicker(c.h-190, "Light line.", "Bold punch line.")
    c.footer_bar()
    c.save("social-media/my_card.png", to_desktop=True)

Run this file directly for a smoke-test render.
"""
from PIL import Image, ImageDraw, ImageFont

# ---- house palette ---------------------------------------------------------
BG="#F5F7FA"; NAVY="#1E3A5F"; NAVY_DK="#152A44"; DARK="#1A202C"
GOLD="#D69E2E"; GOLD_BG="#744210"
RED="#E53E3E"; RED_DK="#9B2C2C"; GREEN="#276749"; ORANGE="#C05621"; BRONZE="#975A16"
MUTED="#718096"; LIGHT="#CBD5E0"; LIGHTGRAY="#A0AEC0"; BORDER="#E2E8F0"; WHITE="#FFFFFF"
FONT_DIR="/System/Library/Fonts/Supplemental/"


class Card:
    def __init__(self, w=1080, h=1080, bg=BG, scale=1):
        self.w, self.h, self.s = w, h, scale
        self.img = Image.new("RGB", (w*scale, h*scale), bg)
        self.d = ImageDraw.Draw(self.img)
        self._strings = []          # every rendered string, for the em-dash guard

    # ---- internals ----
    def _p(self, v):                # scale a scalar
        return int(round(v*self.s))
    def font(self, size, bold=False, impact=False):
        name = "Impact.ttf" if impact else ("Arial Bold.ttf" if bold else "Arial.ttf")
        try:
            return ImageFont.truetype(f"{FONT_DIR}{name}", size*self.s)
        except Exception:
            return ImageFont.load_default()

    # ---- primitives ----
    def text(self, x, y, s, size=17, bold=False, impact=False, fill=DARK, anchor="lm"):
        self._strings.append(s)
        self.d.text((self._p(x), self._p(y)), s, fill=fill,
                    font=self.font(size, bold, impact), anchor=anchor)
        return self

    def rect(self, x0, y0, x1, y1, fill=None, outline=None, width=2, radius=0):
        box=[self._p(x0), self._p(y0), self._p(x1), self._p(y1)]
        if radius:
            self.d.rounded_rectangle(box, radius=self._p(radius), fill=fill,
                                     outline=outline, width=self._p(width) if outline else 1)
        else:
            self.d.rectangle(box, fill=fill, outline=outline,
                             width=self._p(width) if outline else 1)
        return self

    def panel(self, x0, y0, x1, y1, fill=WHITE, outline=BORDER, radius=8, width=2):
        return self.rect(x0, y0, x1, y1, fill=fill, outline=outline, width=width, radius=radius)

    def brand_bar(self, text="LANGWORTHYWATCH.ORG", h=48):
        self.rect(0, 0, self.w, h, fill=NAVY)
        self.text(self.w/2, h/2, text, size=22, bold=True, fill=WHITE, anchor="mm")
        return self

    def footer_bar(self, text="langworthywatch.org  ·  NY-23 Accountability", h=50, fill=NAVY):
        self.rect(0, self.h-h, self.w, self.h, fill=fill)
        self.text(self.w/2, self.h-h/2, text, size=20, bold=True, fill=WHITE, anchor="mm")
        return self

    def badge(self, y, label, fill=GOLD_BG, outline=GOLD, text_fill=GOLD):
        """Gold verdict badge, centered. Returns next y."""
        f=self.font(20, bold=True)
        bb=self.d.textbbox((0,0), label, font=f)
        tw=(bb[2]-bb[0])/self.s+28; th=(bb[3]-bb[1])/self.s+12
        self.rect((self.w-tw)/2, y, (self.w+tw)/2, y+th, fill=fill, outline=outline, width=2, radius=5)
        self.text(self.w/2, y+th/2, label, size=20, bold=True, fill=text_fill, anchor="mm")
        return y+th+26

    def title(self, y, text, size=32, fill=NAVY):
        self.text(self.w/2, y+size/2, text, size=size, bold=True, fill=fill, anchor="mm")
        return y+size+4

    def subtitle(self, y, text, size=16, fill=MUTED):
        self.text(self.w/2, y+size/2, text, size=size, fill=fill, anchor="mm")
        return y+size+2

    def divider(self, y, margin=60, pad=16):
        self.d.line([(self._p(margin), self._p(y)), (self._p(self.w-margin), self._p(y))],
                    fill=BORDER, width=self._p(2))
        return y+pad

    def bullets(self, x, y, points, accent=RED, step=42, size=16, dot=9):
        """Distinct bulleted single-line points. Returns next y."""
        yy=y
        for p in points:
            self.d.ellipse([self._p(x), self._p(yy-4), self._p(x+dot), self._p(yy+dot-4)], fill=accent)
            self.text(x+dot+11, yy, p, size=size, fill=DARK, anchor="lm")
            yy+=step
        return yy

    def kicker(self, y, line1, line2, h=92, fill=NAVY):
        self.panel(44, y, self.w-44, y+h, fill=fill, outline=None, radius=8)
        self.text(self.w/2, y+30, line1, size=17, fill=LIGHTGRAY, anchor="mm")
        self.text(self.w/2, y+62, line2, size=18, bold=True, fill=WHITE, anchor="mm")
        return y+h

    def photo_hero(self, path, top=48):
        """Paste a photo scaled to full width below the brand bar. Returns its bottom y."""
        photo=Image.open(path).convert("RGB")
        pw,ph=photo.size
        neww=self.w*self.s; newh=int(ph*(neww/pw))
        photo=photo.resize((neww, newh), Image.LANCZOS)
        self.img.paste(photo, (0, self._p(top)))
        return top + newh/self.s

    # ---- output ----
    def save(self, path, to_desktop=False, name=None):
        offenders=[s for s in self._strings if "—" in s]
        if offenders:
            raise ValueError("Em dash (—) in rendered card text (house style forbids it): "
                             + " | ".join(offenders))
        out=self.img
        if self.s != 1:
            out=out.resize((self.w, self.h), Image.LANCZOS)
        out.save(path, "PNG", dpi=(144,144))
        print(f"Saved: {path}")
        if to_desktop:
            import os, shutil
            dst=os.path.expanduser(f"~/Desktop/{name or os.path.basename(path)}")
            shutil.copy(path, dst); print(f"Desktop copy: {dst}")
        return path


if __name__ == "__main__":
    c = Card()
    c.brand_bar()
    y = c.badge(64, "SMOKE TEST")
    y = c.title(y, "Card Toolkit Works")
    y = c.subtitle(y, "Shared primitives: badge, title, panel, bullets, kicker.")
    y = c.divider(y)
    c.panel(44, y, c.w-44, y+150)
    c.bullets(70, y+30, ["Consistent house style", "No em dashes (auto-checked)", "Supersample-ready"], RED)
    c.kicker(c.h-190, "Every card starts from here now.", "Less code, no style drift.")
    c.footer_bar()
    c.save("/tmp/card_toolkit_smoketest.png")
