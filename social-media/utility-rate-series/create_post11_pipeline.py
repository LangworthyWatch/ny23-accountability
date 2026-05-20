#!/usr/bin/env python3
"""Post 11: THE FULL CIRCLE — Fossil fuel donations, Langworthy's legislation, your bill."""

from PIL import Image, ImageDraw, ImageFont

WIDTH = 1080
HEIGHT = 1350
FONT_DIR = "/System/Library/Fonts/Supplemental/"

BG = "#F5F7FA"
CARD = "#FFFFFF"
NAVY = "#1E3A5F"
DARK = "#1A202C"
RED = "#E53E3E"
GREEN = "#38A169"
GOLD = "#D69E2E"
MUTED = "#718096"
ACCENT = "#2B6CB0"
LIGHT_BORDER = "#E2E8F0"
LIGHT_RED = "#FFF5F5"
LIGHT_BLUE = "#EBF4FF"
LIGHT_GOLD = "#FFFFF0"
DARK_GRAY = "#4A5568"


def font(name, size):
    try:
        return ImageFont.truetype(f"{FONT_DIR}{name}", size)
    except:
        return ImageFont.load_default()


f_brand = font("Arial Bold.ttf", 22)
f_tag = font("Arial Bold.ttf", 18)
f_headline = font("Arial Bold.ttf", 38)
f_big = font("Impact.ttf", 110)
f_big_label = font("Arial.ttf", 22)
f_donors = font("Arial.ttf", 19)
f_node_title = font("Arial Bold.ttf", 24)
f_node_detail = font("Arial.ttf", 18)
f_node_stat = font("Arial Bold.ttf", 18)
f_arrow_label = font("Arial Bold.ttf", 18)
f_arrow_sym = font("Arial Bold.ttf", 36)
f_sidebar_title = font("Arial Bold.ttf", 17)
f_sidebar_detail = font("Arial.ttf", 16)
f_evidence = font("Arial.ttf", 21)
f_evidence_bold = font("Arial Bold.ttf", 21)
f_kicker = font("Arial Bold.ttf", 25)
f_source = font("Arial.ttf", 17)
f_footer = font("Arial Bold.ttf", 20)

img = Image.new("RGB", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(img)

# ==== TOP BRAND BAR ====
draw.rectangle([(0, 0), (WIDTH, 56)], fill=NAVY)
draw.text((WIDTH // 2, 28), "LANGWORTHYWATCH.ORG", fill="#FFFFFF",
          font=f_brand, anchor="mm")

# ==== TAG PILL ====
y = 82
tag = "FOLLOW THE MONEY"
tb = draw.textbbox((0, 0), tag, font=f_tag)
tw = tb[2] - tb[0]
th = tb[3] - tb[1]
draw.rounded_rectangle(
    [((WIDTH - tw) // 2 - 16, y), ((WIDTH + tw) // 2 + 16, y + th + 14)],
    radius=6, fill=GOLD)
draw.text((WIDTH // 2, y + (th + 14) // 2), tag, fill="#FFFFFF",
          font=f_tag, anchor="mm")

# ==== HEADLINE ====
y = 135
draw.text((WIDTH // 2, y), "The Fossil Fuel Pipeline", fill=DARK,
          font=f_headline, anchor="mm")
draw.text((WIDTH // 2, y + 48), "Behind Your Rate Increase", fill=RED,
          font=f_headline, anchor="mm")

# ==== BIG NUMBER ====
y = 218
draw.text((WIDTH // 2, y), "$66,466", fill=GOLD, font=f_big, anchor="mt")
bbox = draw.textbbox((WIDTH // 2, y), "$66,466", font=f_big, anchor="mt")
y_after_num = bbox[3] + 6
draw.text((WIDTH // 2, y_after_num),
          "in Oil & Gas donations to Langworthy (2024 cycle)",
          fill=MUTED, font=f_big_label, anchor="mm")
draw.text((WIDTH // 2, y_after_num + 28),
          "Koch Industries PAC  |  Marathon Petroleum  |  United Refining ($21,900)",
          fill=DARK, font=f_donors, anchor="mm")

# ==== FLOW DIAGRAM ====
# Four nodes: Industry → Langworthy → H.R. 3699 (NEFI) → Your Bill
# Plus a rate case sidebar callout

node_left = 70
node_right = 700       # narrower to leave room for sidebar
node_height = 88
arrow_gap = 8          # between node bottom and arrow
node_gap = 50          # total vertical gap between nodes (including arrow)
y_flow = 395

nodes = [
    {
        "title": "Oil & Gas Industry",
        "detail": "$66,466 donated to Langworthy \u2014 2024",
        "stat": "Koch PAC  |  Marathon  |  United Refining",
        "fill": ACCENT,
        "detail_color": "#D0E4FF",
        "stat_color": "#FFD700",
    },
    {
        "title": "Rep. Nick Langworthy",
        "detail": "Champions H.R. 3699 \u2014 Energy Choice Act",
        "stat": "Lobbies against clean energy mandates",
        "fill": NAVY,
        "detail_color": "#A0C4E8",
        "stat_color": "#FFD0D0",
    },
    {
        "title": "H.R. 3699 \u2014 Written by NEFI",
        "detail": "NEFI: the fossil fuel industry's trade group",
        "stat": "30+ fossil fuel endorsers  |  LCV score: 0%",
        "fill": RED,
        "detail_color": "#FFD0D0",
        "stat_color": "#FFFFFF",
    },
    {
        "title": "Your Electricity Bill",
        "detail": "NY-23: 49.7% above national average",
        "stat": "No rate relief legislation proposed",
        "fill": DARK_GRAY,
        "detail_color": "#E0E0E0",
        "stat_color": GOLD,
    },
]

arrow_labels = ["donates to", "sponsors", "drafted by NEFI"]

for i, node in enumerate(nodes):
    ny = y_flow + i * (node_height + node_gap)

    # Node box
    draw.rounded_rectangle(
        [(node_left, ny), (node_right, ny + node_height)],
        radius=10, fill=node["fill"])

    # Title
    draw.text((node_left + 20, ny + 16), node["title"],
              fill="#FFFFFF", font=f_node_title, anchor="lm")
    # Detail
    draw.text((node_left + 20, ny + 42), node["detail"],
              fill=node["detail_color"], font=f_node_detail, anchor="lm")
    # Stat
    draw.text((node_left + 20, ny + 65), node["stat"],
              fill=node["stat_color"], font=f_node_stat, anchor="lm")

    # Arrow between nodes (except after last)
    if i < len(nodes) - 1:
        arrow_y = ny + node_height + arrow_gap
        cx = (node_left + node_right) // 2

        # Triangle arrowhead
        tri_y = arrow_y + 18
        draw.polygon(
            [(cx - 10, tri_y), (cx + 10, tri_y), (cx, tri_y + 12)],
            fill=GOLD)

        # Arrow label
        label = arrow_labels[i]
        draw.text((cx + 22, tri_y + 4), label, fill=MUTED,
                  font=f_arrow_label, anchor="lm")

# ==== RATE CASE SIDEBAR ====
# Callout showing the pending rate case his constituents face
sidebar_x = node_right + 20
sidebar_y = y_flow + node_height + 15
sidebar_w = WIDTH - 60 - sidebar_x
sidebar_h = node_height + node_gap + 20

draw.rounded_rectangle(
    [(sidebar_x, sidebar_y),
     (sidebar_x + sidebar_w, sidebar_y + sidebar_h)],
    radius=8, fill=LIGHT_RED, outline=RED, width=2)

draw.text((sidebar_x + sidebar_w // 2, sidebar_y + 14),
          "RATE CASE", fill=RED, font=f_sidebar_title, anchor="mm")
draw.text((sidebar_x + sidebar_w // 2, sidebar_y + 34),
          "NYSEG seeks", fill=DARK, font=f_sidebar_detail, anchor="mm")
draw.text((sidebar_x + sidebar_w // 2, sidebar_y + 54),
          "18.4%", fill=RED, font=f_sidebar_title, anchor="mm")
draw.text((sidebar_x + sidebar_w // 2, sidebar_y + 74),
          "increase for", fill=DARK, font=f_sidebar_detail, anchor="mm")
draw.text((sidebar_x + sidebar_w // 2, sidebar_y + 92),
          "NY-23 customers", fill=DARK, font=f_sidebar_detail, anchor="mm")

# Dashed connector line from sidebar to Node 2 area
# (simple horizontal line from sidebar left edge to node right edge)
connector_y = sidebar_y + sidebar_h // 2
# Draw dashed line as series of short segments
dash_len = 8
gap_len = 6
x_start = node_right
x_end = sidebar_x
x = x_start
while x < x_end:
    x2 = min(x + dash_len, x_end)
    draw.line([(x, connector_y), (x2, connector_y)], fill=GOLD, width=2)
    x += dash_len + gap_len

# ==== HE SAYS / THE RECORD CARDS ====
last_node_bottom = y_flow + len(nodes) * (node_height + node_gap) - node_gap + node_height

# Divider above cards
y_div = last_node_bottom + 20
draw.line([(100, y_div), (WIDTH - 100, y_div)], fill=LIGHT_BORDER, width=2)

y_cards = y_div + 16
card_h = 128
col_w = 470    # (1080 - 60 - 60 - 20 gap) / 2
lx = 60
rx = lx + col_w + 20  # = 550

# Left card: LANGWORTHY SAYS (light blue)
draw.rounded_rectangle(
    [(lx, y_cards), (lx + col_w, y_cards + card_h)],
    radius=10, fill=LIGHT_BLUE, outline=ACCENT, width=2)
draw.text((lx + col_w // 2, y_cards + 18),
          "LANGWORTHY SAYS:", fill=ACCENT, font=f_sidebar_title, anchor="mm")
draw.text((lx + col_w // 2, y_cards + 46),
          "Clean energy mandates", fill=DARK, font=f_node_detail, anchor="mm")
draw.text((lx + col_w // 2, y_cards + 66),
          "make electricity unaffordable", fill=DARK, font=f_node_detail, anchor="mm")
draw.text((lx + col_w // 2, y_cards + 92),
          "Champions H.R. 3699:", fill=DARK, font=f_node_detail, anchor="mm")
draw.text((lx + col_w // 2, y_cards + 112),
          "\"energy choice\" for natural gas", fill=ACCENT, font=f_node_stat, anchor="mm")

# Right card: THE RECORD (light red)
draw.rounded_rectangle(
    [(rx, y_cards), (rx + col_w, y_cards + card_h)],
    radius=10, fill=LIGHT_RED, outline=RED, width=2)
draw.text((rx + col_w // 2, y_cards + 18),
          "THE RECORD:", fill=RED, font=f_sidebar_title, anchor="mm")
draw.text((rx + col_w // 2, y_cards + 46),
          "H.R. 3699 drafted by NEFI", fill=DARK, font=f_node_detail, anchor="mm")
draw.text((rx + col_w // 2, y_cards + 66),
          "\u2014 a fossil fuel trade group", fill=DARK, font=f_node_detail, anchor="mm")
draw.text((rx + col_w // 2, y_cards + 92),
          "30+ fossil fuel endorsers", fill=DARK, font=f_node_detail, anchor="mm")
draw.text((rx + col_w // 2, y_cards + 112),
          "2024 LCV score: 0%", fill=RED, font=f_node_stat, anchor="mm")

# ==== KICKER ====
y_kicker = y_cards + card_h + 18
draw.text((WIDTH // 2, y_kicker),
          "Energy Choice Act (H.R. 3699): drafted by NEFI,",
          fill=DARK, font=f_kicker, anchor="mm")
draw.text((WIDTH // 2, y_kicker + 34),
          "endorsed by 30+ fossil fuel companies.",
          fill=DARK, font=f_kicker, anchor="mm")

# ==== SOURCE ====
y_src = y_kicker + 72
draw.text((WIDTH // 2, y_src),
          "Sources: FEC (fec.gov), NYSBOE, OpenSecrets, LCV, COELIG/JCOPE",
          fill=MUTED, font=f_source, anchor="mm")
draw.text((WIDTH // 2, y_src + 22),
          "Full investigation: langworthywatch.org",
          fill=MUTED, font=f_source, anchor="mm")

# ==== FOOTER BAR ====
draw.rectangle([(0, HEIGHT - 56), (WIDTH, HEIGHT)], fill=NAVY)
draw.text((WIDTH // 2, HEIGHT - 28), "langworthywatch.org",
          fill="#FFFFFF", font=f_footer, anchor="mm")

out = "/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/utility-rate-series/post11_pipeline.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {out}")
