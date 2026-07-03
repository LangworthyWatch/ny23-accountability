#!/usr/bin/env python3
"""Social card: 'Not a Calendar Day' — Langworthy's Rules Committee votes that kept
the House from voting to end the tariffs. DOCUMENTED PATTERN, July 3, 2026."""

from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1080, 1080
FONT_DIR = "/System/Library/Fonts/Supplemental/"
BG="#F5F7FA"; NAVY="#1E3A5F"; DARK="#1A202C"; GREEN="#276749"; RED="#E53E3E"
ORANGE="#C05621"; GOLD="#D69E2E"; MUTED="#718096"; BORDER="#E2E8F0"
WHITE="#FFFFFF"; LIGHTGRAY="#A0AEC0"

def font(n,s):
    try: return ImageFont.truetype(f"{FONT_DIR}{n}", s)
    except Exception: return ImageFont.load_default()

f_brand=font("Arial Bold.ttf",22); f_tag=font("Arial Bold.ttf",20); f_topic=font("Arial Bold.ttf",30)
f_label=font("Arial Bold.ttf",20); f_label_s=font("Arial Bold.ttf",16)
f_colh=font("Arial Bold.ttf",19); f_sub=font("Arial.ttf",18); f_small=font("Arial.ttf",17)
f_body=font("Arial.ttf",16); f_src=font("Arial.ttf",15); f_footer=font("Arial Bold.ttf",20)

img=Image.new("RGB",(WIDTH,HEIGHT),BG); draw=ImageDraw.Draw(img)

draw.rectangle([(0,0),(WIDTH,48)],fill=NAVY)
draw.text((WIDTH//2,24),"LANGWORTHYWATCH.ORG",fill=WHITE,font=f_brand,anchor="mm")
y=64

tag="DOCUMENTED PATTERN"; tb=draw.textbbox((0,0),tag,font=f_tag); tw,th=tb[2]-tb[0]+28,tb[3]-tb[1]+12
draw.rounded_rectangle([((WIDTH-tw)//2,y),((WIDTH+tw)//2,y+th)],radius=5,fill="#744210",outline=GOLD,width=2)
draw.text((WIDTH//2,y+th//2),tag,fill=GOLD,font=f_tag,anchor="mm"); y+=th+26

draw.text((WIDTH//2,y),"'Not a Calendar Day'",fill=NAVY,font=f_topic,anchor="mm"); y+=34
draw.text((WIDTH//2,y),"How his committee kept the House from voting to end the tariffs.",
          fill=MUTED,font=font("Arial.ttf",16),anchor="mm"); y+=16
draw.line([(60,y),(WIDTH-60,y)],fill=BORDER,width=2); y+=16

# The device
dev_h=118
draw.rounded_rectangle([(44,y),(WIDTH-44,y+dev_h)],radius=8,fill="#EDF2F7",outline=BORDER,width=2)
draw.text((76,y+16),"THE DEVICE",fill=NAVY,font=f_label_s,anchor="lm")
draw.text((76,y+46),'A special rule declared that, for the rest of 2025, each day "shall not',fill=DARK,font=f_sub,anchor="lm")
draw.text((76,y+72),'constitute a calendar day" for the National Emergencies Act clock.',fill=DARK,font=f_sub,anchor="lm")
draw.text((76,y+98),"No clock = no forced floor vote to end the tariffs.",fill=MUTED,font=f_small,anchor="lm")
y+=dev_h+16

# two votes
col_w=(WIDTH-44*2-16)//2; col_h=210; lx=44; rx=lx+col_w+16
for (cx,head,sub,lines) in [
    (lx,"MARCH 2025","H.Res.211  ·  H. Rept. 119-15",[
        "Blocked a vote to end the",
        "Canada / Mexico / China tariffs",
        "",
        "Langworthy: NAY to strike it,",
        "YEA to report the rule"]),
    (rx,"APRIL 2025","H.Res.313  ·  H. Rept. 119-56",[
        "Blocked a vote to end the",
        'global "Liberation Day" tariffs',
        "",
        "Langworthy: NAY to strike it,",
        "YEA to report the rule"]),
]:
    draw.rounded_rectangle([(cx,y),(cx+col_w,y+col_h)],radius=8,fill="#FFF5F5",outline="#FEB2B2",width=2)
    draw.text((cx+col_w//2,y+22),head,fill=RED,font=f_colh,anchor="mm")
    draw.text((cx+col_w//2,y+42),sub,fill=MUTED,font=font("Arial.ttf",13),anchor="mm")
    for i,t in enumerate(lines):
        draw.text((cx+22,y+70+i*26),t,fill=DARK,font=f_body,anchor="lm")
y+=col_h+16

# result strip
res_h=112
draw.rounded_rectangle([(44,y),(WIDTH-44,y+res_h)],radius=8,fill="#FFFAF0",outline="#F6AD55",width=2)
draw.text((WIDTH//2,y+22),"THE RESULT",fill=ORANGE,font=f_label,anchor="mm")
draw.text((WIDTH//2,y+54),"No House vote to end the Canada tariffs until Feb. 11, 2026 (about a year).",
          fill=DARK,font=font("Arial Bold.ttf",17),anchor="mm")
draw.text((WIDTH//2,y+82),"He voted NO then too. Nine days later, the Supreme Court ruled the tariffs illegal.",
          fill=DARK,font=font("Arial.ttf",16),anchor="mm")
y+=res_h+14

# kicker
kick_h=88
draw.rounded_rectangle([(44,y),(WIDTH-44,y+kick_h)],radius=8,fill=NAVY)
draw.text((WIDTH//2,y+26),"His own district was paying: the Bush Industries plant in Jamestown closed in",
          fill=LIGHTGRAY,font=font("Arial.ttf",16),anchor="mm")
draw.text((WIDTH//2,y+54),"2026, its filing naming tariffs. He twice voted to keep the House from voting.",
          fill=WHITE,font=font("Arial Bold.ttf",17),anchor="mm")
y+=kick_h+12

draw.text((WIDTH//2,y),"Sources: official House committee reports (H. Rept. 119-15, 119-56)",
          fill=MUTED,font=f_src,anchor="mm"); y+=24
draw.text((WIDTH//2,y),"langworthywatch.org/fact-checks/2026-07-03-rules-committee-tariff-vote-blockade/",
          fill=NAVY,font=font("Arial.ttf",14),anchor="mm")

draw.rectangle([(0,HEIGHT-50),(WIDTH,HEIGHT)],fill=NAVY)
draw.text((WIDTH//2,HEIGHT-25),"langworthywatch.org  ·  NY-23 Accountability",fill=WHITE,font=f_footer,anchor="mm")

out="/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/tariff_blockade_card.png"
img.save(out,"PNG",dpi=(144,144)); print(f"Saved: {out}")
