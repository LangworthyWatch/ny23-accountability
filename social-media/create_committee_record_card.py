#!/usr/bin/env python3
"""Social card: 'A Seat at the Table' — Langworthy's E&C + Rules committee record
on the Medicaid cuts. DOCUMENTED PATTERN, July 3, 2026."""

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
f_body=font("Arial.ttf",16); f_stat=font("Impact.ttf",44); f_src=font("Arial.ttf",15)
f_footer=font("Arial Bold.ttf",20)

img=Image.new("RGB",(WIDTH,HEIGHT),BG); draw=ImageDraw.Draw(img)

draw.rectangle([(0,0),(WIDTH,48)],fill=NAVY)
draw.text((WIDTH//2,24),"LANGWORTHYWATCH.ORG",fill=WHITE,font=f_brand,anchor="mm")
y=64

tag="DOCUMENTED PATTERN"; tb=draw.textbbox((0,0),tag,font=f_tag); tw,th=tb[2]-tb[0]+28,tb[3]-tb[1]+12
draw.rounded_rectangle([((WIDTH-tw)//2,y),((WIDTH+tw)//2,y+th)],radius=5,fill="#744210",outline=GOLD,width=2)
draw.text((WIDTH//2,y+th//2),tag,fill=GOLD,font=f_tag,anchor="mm"); y+=th+26

draw.text((WIDTH//2,y),"'A Seat at the Table'",fill=NAVY,font=f_topic,anchor="mm"); y+=34
draw.text((WIDTH//2,y),"His own words for two powerful committees. Here is the record on the Medicaid cuts.",
          fill=MUTED,font=font("Arial.ttf",16),anchor="mm"); y+=16
draw.line([(60,y),(WIDTH-60,y)],fill=BORDER,width=2); y+=16

# Claim box — his self-description
claim_h=112
draw.rounded_rectangle([(44,y),(WIDTH-44,y+claim_h)],radius=8,fill="#FFFAF0",outline="#F6AD55",width=2)
draw.text((76,y+16),"HIS OWN WEBSITE  ·  langworthy.house.gov",fill=ORANGE,font=f_label_s,anchor="lm")
draw.text((76,y+46),'His Rules and Energy & Commerce seats mean "fighting to ensure',fill=DARK,font=f_sub,anchor="lm")
draw.text((76,y+72),'our rural communities have a seat at the table on major legislation."',fill=DARK,font=f_sub,anchor="lm")
y+=claim_h+16

# Two committees
col_w=(WIDTH-44*2-16)//2; col_h=238; lx=44; rx=lx+col_w+16
def bullets(x0, top, points, accent):
    yy = top+84
    for p in points:
        draw.ellipse([(x0, yy-4),(x0+9, yy+5)], fill=accent)
        draw.text((x0+20, yy), p, fill=DARK, font=f_body, anchor="lm")
        yy += 42
# left: E&C
draw.rounded_rectangle([(lx,y),(lx+col_w,y+col_h)],radius=8,fill="#FFF5F5",outline="#FEB2B2",width=2)
draw.text((lx+col_w//2,y+22),"ENERGY & COMMERCE",fill=RED,font=f_colh,anchor="mm")
draw.text((lx+col_w//2,y+42),"where the cuts were written",fill=MUTED,font=font("Arial.ttf",14),anchor="mm")
bullets(lx+26, y, [
    "Voted YES to advance the cuts",
    "NO on all 21 Democratic amendments",
    "Offered ZERO of his own"], RED)
# right: Rules
draw.rounded_rectangle([(rx,y),(rx+col_w,y+col_h)],radius=8,fill="#FFF5F5",outline="#FEB2B2",width=2)
draw.text((rx+col_w//2,y+22),"RULES COMMITTEE",fill=RED,font=f_colh,anchor="mm")
draw.text((rx+col_w//2,y+42),"which amendments reach the floor",fill=MUTED,font=font("Arial.ttf",14),anchor="mm")
bullets(rx+26, y, [
    "5 closed rules reported",
    "Blocked every floor vote to soften them",
    "YES to report each rule",
    "By name, in the record"], RED)
y+=col_h+16

# strip — what he voted to keep off the floor
strip_h=112
draw.rounded_rectangle([(44,y),(WIDTH-44,y+strip_h)],radius=8,fill="#EDF2F7",outline=BORDER,width=2)
draw.text((WIDTH//2,y+20),"AMENDMENTS HE VOTED TO KEEP OFF THE HOUSE FLOOR",fill=NAVY,font=f_label,anchor="mm")
items=["Strike the Medicaid cuts","Permanent ACA credits (Essential Plan)","$35 insulin cap","$313B SNAP cut"]
draw.text((WIDTH//2,y+56),"  ·  ".join(items[:2]),fill=DARK,font=font("Arial Bold.ttf",17),anchor="mm")
draw.text((WIDTH//2,y+84),"  ·  ".join(items[2:]),fill=DARK,font=font("Arial Bold.ttf",17),anchor="mm")
y+=strip_h+16

# kicker
kick_h=92
draw.rounded_rectangle([(44,y),(WIDTH-44,y+kick_h)],radius=8,fill=NAVY)
draw.text((WIDTH//2,y+28),"He said he would 'fight relentlessly to protect rural hospitals.'",
          fill=LIGHTGRAY,font=font("Arial.ttf",17),anchor="mm")
draw.text((WIDTH//2,y+58),"On the biggest rural-health bill of his term, he offered no amendment of his own.",
          fill=WHITE,font=font("Arial Bold.ttf",17),anchor="mm")
y+=kick_h+14

draw.text((WIDTH//2,y),"Sources: official House committee reports (H. Rept. 119-5, -106, -113, -152, -179, -372)",
          fill=MUTED,font=f_src,anchor="mm"); y+=24
draw.text((WIDTH//2,y),"langworthywatch.org/fact-checks/2026-07-03-committee-record-medicaid-seat-at-the-table/",
          fill=NAVY,font=font("Arial.ttf",14),anchor="mm")

draw.rectangle([(0,HEIGHT-50),(WIDTH,HEIGHT)],fill=NAVY)
draw.text((WIDTH//2,HEIGHT-25),"langworthywatch.org  ·  NY-23 Accountability",fill=WHITE,font=f_footer,anchor="mm")

out="/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/committee_record_card.png"
img.save(out,"PNG",dpi=(144,144)); print(f"Saved: {out}")
