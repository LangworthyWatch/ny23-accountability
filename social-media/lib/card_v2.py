#!/usr/bin/env python3
"""
LangworthyWatch card theme v2 (post-election refresh, proposed November 11, 2026).

Builds on lib/card.py (same Card primitives, same em-dash guard on save) with:
- A party-neutral palette. Navy is the brand; amber marks the finding; slate is the fair case;
  gray is context. Red appears only for a FALSE verdict. All text pairings pass WCAG AA
  (checked Nov 11, 2026; see research/style-refresh-2026-11/README.md).
- Arial Black for big numbers (it matches the favicon lettering) in place of Impact.
- An LW mark in the brand bar, a slimmer footer, larger default type.
- Three templates: one_number(), said_vs_record(), weekly_roundup().

Old cards keep using lib/card.py unchanged.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PIL import ImageFont
from lib.card import Card as _Card, FONT_DIR

# v2.1 (Nov 11): the first set's surfaces differed by a contrast ratio of ~1.06 and washed together.
# One white surface, a navy footer band, darker gray text, rules ~1.6:1, panel borders >= 3:1 (WCAG 1.4.11).
NAVY = "#1E3A5F"; INK = "#1A202C"; PAPER = "#FFFFFF"; WHITE = "#FFFFFF"
AMBER = "#D69E2E"; AMBER_TXT = "#8A5A0B"; AMBER_TINT = "#F8E7C2"; GOLD_LIGHT = "#F6D58E"
SLATE = "#3F5873"; SLATE_TINT = "#DCE5F0"; SLATE_LINE = "#7C8DA6"
GRAY = "#4A5568"; LINE = "#C3CCD8"; RED = "#C53030"; ON_NAVY = "#C9D3E0"
# v2.2 (Nov 11): content sits in a white framed panel on a tinted background (user request).
BACKDROP = "#DFE6EF"; FRAME_LINE = "#9AA9BD"; SHADOW = "#C5CFDC"
TOP_H = 64; FOOT_H = 86; FRAME_INSET = 22
CONTENT_TOP = TOP_H + FRAME_INSET; CONTENT_BOTTOM = 1080 - FOOT_H - FRAME_INSET
VERDICT_FILL = {"FALSE": RED}  # every other verdict uses navy; red is reserved for FALSE


class Card(_Card):
    def __init__(self, w=1080, h=1080, scale=2):
        super().__init__(w=w, h=h, bg=BACKDROP, scale=scale)

    def font(self, size, bold=False, impact=False):
        name = "Arial Black.ttf" if impact else ("Arial Bold.ttf" if bold else "Arial.ttf")
        try:
            return ImageFont.truetype(f"{FONT_DIR}{name}", int(size * self.s))
        except Exception:
            return ImageFont.load_default()

    # ---- frame -------------------------------------------------------------
    def mark(self, x, y, s=34):
        """LW tile (navy square, white LW, amber rule), same design as the favicon."""
        self.rect(x, y, x + s, y + s, fill=NAVY, outline=WHITE, width=1.5, radius=s * 0.18)
        self.text(x + s / 2, y + s * 0.44, "LW", size=s * 0.42, impact=True, fill=WHITE, anchor="mm")
        self.rect(x + s * 0.2, y + s * 0.74, x + s * 0.8, y + s * 0.80, fill=AMBER)
        return self

    def frame(self):
        """White content panel with a soft shadow and a defined edge, between the top bar and the footer."""
        x0, x1 = FRAME_INSET, self.w - FRAME_INSET
        y0, y1 = CONTENT_TOP, CONTENT_BOTTOM
        self.rect(x0 + 3, y0 + 5, x1 + 3, y1 + 5, fill=SHADOW, radius=10)
        self.rect(x0, y0, x1, y1, fill=WHITE, outline=FRAME_LINE, width=1.5, radius=10)
        return self

    def top_bar(self, kicker, h=TOP_H):
        self.frame()
        self.rect(0, 0, self.w, h, fill=NAVY)
        self.mark(40, (h - 36) / 2, 36)
        self.text(92, h / 2, "LANGWORTHYWATCH.ORG", size=19, bold=True, fill=WHITE, anchor="lm")
        self.text(self.w - 40, h / 2, kicker, size=16, bold=True, fill=GOLD_LIGHT, anchor="rm")
        return h

    def foot(self, sources, url, h=86):
        y0 = self.h - h
        self.rect(0, y0, self.w, self.h, fill=NAVY)
        self.rect(0, y0, self.w, y0 + 4, fill=AMBER)
        self.text(48, y0 + 32, sources, size=14, fill=ON_NAVY, anchor="lm")
        self.text(48, y0 + 60, url, size=16, bold=True, fill=WHITE, anchor="lm")
        return y0

    def tag(self, x, y, label, fill=NAVY, text_fill=WHITE, size=15):
        f = self.font(size, bold=True)
        bb = self.d.textbbox((0, 0), label, font=f)
        tw = (bb[2] - bb[0]) / self.s + 26
        self.rect(x, y, x + tw, y + size + 16, fill=fill, radius=4)
        self.text(x + 13, y + (size + 16) / 2, label, size=size, bold=True, fill=text_fill, anchor="lm")
        return x + tw

    def verdict(self, x, y, label):
        return self.tag(x, y, label, fill=VERDICT_FILL.get(label.upper(), NAVY))

    def wrap(self, x, y, text, width, size=20, bold=False, fill=INK, leading=1.32, impact=False):
        """Left-aligned word wrap in logical px. Returns the y below the last line."""
        f = self.font(size, bold, impact)
        words, line, lines = text.split(), "", []
        for w_ in words:
            trial = (line + " " + w_).strip()
            if self.d.textlength(trial, font=f) / self.s <= width:
                line = trial
            else:
                lines.append(line); line = w_
        if line:
            lines.append(line)
        for i, ln in enumerate(lines):
            self.text(x, y + i * size * leading, ln, size=size, bold=bold, fill=fill, anchor="lt", impact=impact)
        return y + len(lines) * size * leading


# ---- templates --------------------------------------------------------------
def _measure(c, text, width, size, bold=False, leading=1.32, impact=False):
    f = c.font(size, bold, impact)
    words, line, n = text.split(), "", 0
    for w_ in words:
        trial = (line + " " + w_).strip()
        if c.d.textlength(trial, font=f) / c.s <= width:
            line = trial
        else:
            n += 1; line = w_
    return (n + (1 if line else 0)) * size * leading


def one_number(number, unit_line, sentence, context, tag_label, sources, url, kicker, path,
               favor=False, dots=None):
    """Template A: one big number, one sentence, a context line, a source.
    dots=(filled, total) draws a strip of total dots with `filled` in navy, the rest open."""
    c = Card()
    top = c.top_bar(kicker) + FRAME_INSET; bottom = CONTENT_BOTTOM
    body = 40 + 250 + 44 + _measure(c, unit_line, 950, 34, True, 1.2) + 18 + _measure(c, sentence, 950, 24) \
        + 26 + _measure(c, context, 950, 19) + (110 if dots else 0)
    y = top + max(48, (bottom - top - body) / 2)
    if favor:   # amber tag for findings that cut his way ("HELD UP" for claims, "IN HIS FAVOR" for records)
        c.tag(64, y, tag_label, fill=AMBER, text_fill=INK)
    else:
        c.verdict(64, y, tag_label)
    y += 56
    c.text(60, y, number, size=210, impact=True, fill=NAVY, anchor="lt")
    y += 250
    if dots:
        filled, total = dots
        d = min(24, (c.w - 128) / total - 4); pitch = (c.w - 128) / total
        for k in range(total):
            x0 = 64 + k * pitch
            if k < filled:
                c.d.ellipse([c._p(x0), c._p(y), c._p(x0 + d), c._p(y + d)], fill=NAVY)
            else:
                c.d.ellipse([c._p(x0), c._p(y), c._p(x0 + d), c._p(y + d)], outline=AMBER_TXT, width=c._p(2.5))
        c.text(64, y + d + 26, f"Each dot is one roll call. Filled: voted. Open: missed.", size=16, fill=GRAY, anchor="lm")
        y += 110
    else:
        c.rect(64, y, 64 + 150, y + 10, fill=AMBER); y += 34
    y = c.wrap(64, y, unit_line, 950, size=34, bold=True, fill=INK, leading=1.2)
    y = c.wrap(64, y + 18, sentence, 950, size=24, fill=INK)
    c.wrap(64, y + 26, context, 950, size=19, fill=GRAY)
    c.foot(sources, url)
    return c.save(path)


def said_vs_record(title, said_items, record_points, fair_line, verdict, sources, url, kicker, path):
    """Template B: what he said (navy rule) beside what the record shows (amber rule).
    said_items = [(quote, source)], record_points = [(big, small)]."""
    c = Card()
    top = c.top_bar(kicker) + FRAME_INSET; bottom = CONTENT_BOTTOM
    col_w, gap = 456, 40
    lx, rx = 64, 64 + col_w + gap
    left_h = 52 + sum(_measure(c, f"\u201c{q}\u201d", col_w - 30, 28, leading=1.28) + 10 + _measure(c, s, col_w - 30, 16) + 34 for q, s in said_items)
    right_h = 52 + sum(54 + _measure(c, s, col_w - 30, 20, leading=1.28) + 30 for _, s in record_points)
    col_h = max(left_h, right_h)
    title_h = _measure(c, title, 952, 40, True, 1.15)
    fair_h = 40 + _measure(c, fair_line, c.w - 176, 18, leading=1.25) + 16
    body = 34 + 58 + title_h + 34 + col_h + 32 + fair_h
    y = top + max(36, (bottom - top - body) / 2)
    c.verdict(64, y, verdict); y += 58
    y = c.wrap(64, y, title, 952, size=40, bold=True, fill=NAVY, leading=1.15) + 34
    t0 = y
    c.rect(lx, t0, lx + 6, t0 + col_h, fill=NAVY)
    c.text(lx + 24, t0 + 14, "WHAT HE SAID", size=17, bold=True, fill=NAVY, anchor="lt")
    yy = t0 + 52
    for q, s in said_items:
        yy = c.wrap(lx + 24, yy, f"\u201c{q}\u201d", col_w - 30, size=28, fill=INK, leading=1.28)
        yy = c.wrap(lx + 24, yy + 10, s, col_w - 30, size=16, fill=GRAY) + 34
    c.rect(rx, t0, rx + 6, t0 + col_h, fill=AMBER)
    c.text(rx + 24, t0 + 14, "WHAT THE RECORD SHOWS", size=17, bold=True, fill=AMBER_TXT, anchor="lt")
    yy = t0 + 52
    for big, small in record_points:
        c.text(rx + 24, yy, big, size=42, impact=True, fill=NAVY, anchor="lt")
        yy = c.wrap(rx + 24, yy + 56, small, col_w - 30, size=20, fill=INK, leading=1.28) + 30
    y = t0 + col_h + 32
    c.rect(64, y, c.w - 64, y + fair_h, fill=SLATE_TINT, outline=SLATE_LINE, width=2, radius=6)
    c.text(88, y + 22, "WHAT CUTS HIS WAY", size=15, bold=True, fill=SLATE, anchor="lm")
    c.wrap(88, y + 40, fair_line, c.w - 176, size=18, fill=INK, leading=1.25)
    c.foot(sources, url)
    return c.save(path)


def weekly_roundup(week_label, rows, held_up, sources, url, path):
    """Template C: the weekly roundup. rows = [(section, big, line)]; held_up = (tag, big, line) or None.
    Rows are spread to fill the card."""
    c = Card()
    top = c.top_bar("WEEKLY") + FRAME_INSET; bottom = CONTENT_BOTTOM
    y = top + 46
    c.text(64, y, "THIS WEEK IN NY-23", size=20, bold=True, fill=AMBER_TXT, anchor="lt")
    y += 34
    c.text(64, y, week_label, size=46, bold=True, fill=NAVY, anchor="lt")
    y += 84
    box_h = 132 if held_up else 0
    avail = bottom - 40 - box_h - (24 if held_up else 0) - y
    row_h = max(140, avail / len(rows))
    for section, big, line in rows:
        c.rect(64, y, c.w - 64, y + 2, fill=LINE)
        c.text(64, y + 24, section.upper(), size=15, bold=True, fill=GRAY, anchor="lt")
        c.text(64, y + 54, big, size=46, impact=True, fill=NAVY, anchor="lt")
        c.wrap(330, y + 56, line, c.w - 64 - 330, size=21, fill=INK, leading=1.3)
        y += row_h
    if held_up:
        label, big, line = held_up
        y += 8
        c.rect(64, y, c.w - 64, y + box_h, fill=AMBER_TINT, outline=AMBER, width=2, radius=6)
        c.tag(84, y + 20, label, fill=AMBER, text_fill=INK, size=14)
        c.text(84, y + 68, big, size=40, impact=True, fill=NAVY, anchor="lt")
        c.wrap(330, y + 70, line, c.w - 64 - 330 - 20, size=20, fill=INK, leading=1.3)
    c.foot(sources, url)
    return c.save(path)
