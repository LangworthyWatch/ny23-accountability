#!/usr/bin/env python3
"""Social card: Essential Plan cliff, July 1 2026. ~450,000 NYers lose free coverage.
Claim '400,000 lose insurance today' is MOSTLY TRUE (understated); affordability +
CBO money-shift context. Light house style, 1080x1080, no em dashes."""

from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1080, 1080
FONT_DIR = "/System/Library/Fonts/Supplemental/"
BG="#F5F7FA"; NAVY="#1E3A5F"; DARK="#1A202C"; GREEN="#276749"; RED="#E53E3E"
ORANGE="#C05621"; GOLD="#D69E2E"; MUTED="#718096"; BORDER="#E2E8F0"; WHITE="#FFFFFF"; LIGHTGRAY="#A0AEC0"

def font(n,s):
    try: return ImageFont.truetype(f"{FONT_DIR}{n}", s)
    except Exception: return ImageFont.load_default()
f_brand=font("Arial Bold.ttf",22); f_tag=font("Arial Bold.ttf",20); f_topic=font("Arial Bold.ttf",29)
f_label=font("Arial Bold.ttf",20); f_label_s=font("Arial Bold.ttf",16); f_big=font("Impact.ttf",64)
f_stat=font("Impact.ttf",38); f_sub_b=font("Arial Bold.ttf",21); f_sub=font("Arial.ttf",18)
f_small=font("Arial.ttf",17); f_xs=font("Arial.ttf",14); f_xs_b=font("Arial Bold.ttf",14)
f_src=font("Arial.ttf",15); f_footer=font("Arial Bold.ttf",20)

img=Image.new("RGB",(WIDTH,HEIGHT),BG); draw=ImageDraw.Draw(img)
draw.rectangle([(0,0),(WIDTH,48)],fill=NAVY)
draw.text((WIDTH//2,24),"LANGWORTHYWATCH.ORG",fill=WHITE,font=f_brand,anchor="mm")
y=62

# verdict badge (gold = MOSTLY TRUE)
tag="MOSTLY TRUE"; tb=draw.textbbox((0,0),tag,font=f_tag); tw,th=tb[2]-tb[0]+28,tb[3]-tb[1]+12
draw.rounded_rectangle([((WIDTH-tw)//2,y),((WIDTH+tw)//2,y+th)],radius=5,fill="#744210",outline=GOLD,width=2)
draw.text((WIDTH//2,y+th//2),tag,fill=GOLD,font=f_tag,anchor="mm"); y+=th+26
draw.text((WIDTH//2,y),"Health Coverage Cliff  ·  July 1, 2026",fill=NAVY,font=f_topic,anchor="mm"); y+=40
draw.line([(60,y),(WIDTH-60,y)],fill=BORDER,width=2); y+=16

# claim box
claim_h=96
draw.rounded_rectangle([(44,y),(WIDTH-44,y+claim_h)],radius=8,fill="#FFFAF0",outline="#F6AD55",width=2)
draw.text((76,y+16),"THE CLAIM  ·  circulating today",fill=ORANGE,font=f_label_s,anchor="lm")
draw.text((76,y+52),'"400,000 New Yorkers lose their health insurance today."',fill=DARK,font=f_sub,anchor="lm")
draw.text((76,y+78),"Right event, right date. The real number is higher.",fill=MUTED,font=f_small,anchor="lm")
y+=claim_h+16

# two columns: claimed vs data
col_w=(WIDTH-44*2-16)//2; col_h=250; lx=44; rx=lx+col_w+16
draw.rounded_rectangle([(lx,y),(lx+col_w,y+col_h)],radius=8,fill="#EBF8F0",outline="#9AE6B4",width=2)
draw.text((lx+col_w//2,y+22),"WHAT WAS FREE",fill=GREEN,font=f_label_s,anchor="mm")
draw.text((lx+col_w//2,y+86),"$0",fill=GREEN,font=f_big,anchor="mm")
draw.text((lx+col_w//2,y+142),"Essential Plan premium",fill=DARK,font=f_sub_b,anchor="mm")
draw.text((lx+col_w//2,y+174),"low cost sharing, covered",fill=DARK,font=f_sub,anchor="mm")
draw.text((lx+col_w//2,y+200),"~450,000 to 470,000 people",fill=DARK,font=f_sub,anchor="mm")
draw.text((lx+col_w//2,y+224),"at 200-250% of poverty line",fill=MUTED,font=f_small,anchor="mm")
draw.rounded_rectangle([(rx,y),(rx+col_w,y+col_h)],radius=8,fill="#FFF5F5",outline="#FEB2B2",width=2)
draw.text((rx+col_w//2,y+22),"WHAT REPLACES IT",fill=RED,font=f_label_s,anchor="mm")
draw.text((rx+col_w//2,y+86),"$250/mo",fill=RED,font=font("Impact.ttf",52),anchor="mm")
draw.text((rx+col_w//2,y+142),"plus a $2,500 deductible",fill=DARK,font=f_sub_b,anchor="mm")
draw.text((rx+col_w//2,y+174),"even after tax credits",fill=DARK,font=f_sub,anchor="mm")
draw.text((rx+col_w//2,y+200),"~10% of income in premiums",fill=DARK,font=f_sub,anchor="mm")
draw.text((rx+col_w//2,y+224),"for someone earning $31,300",fill=MUTED,font=f_small,anchor="mm")
y+=col_h+16

# affordability strip
strip_h=132
draw.rounded_rectangle([(44,y),(WIDTH-44,y+strip_h)],radius=8,fill="#EDF2F7",outline=BORDER,width=2)
draw.text((WIDTH//2,y+20),"CAN THEY AFFORD THE ALTERNATIVE?",fill=NAVY,font=f_label,anchor="mm")
third=(WIDTH-88)//3
for i,(val,l1,l2,c) in enumerate([
    ("17%","bought a plan before","at these prices (history)",RED),
    ("up to 80%","may go uninsured","instead (Step Two Policy)",RED),
    ("$0 to $250","free plan to paid plan","for the near poor",NAVY),
]):
    cx=44+i*third+third//2
    draw.text((cx,y+64),val,fill=c,font=f_stat,anchor="mm")
    draw.text((cx,y+98),l1,fill=DARK,font=f_xs_b,anchor="mm")
    draw.text((cx,y+118),l2,fill=MUTED,font=f_xs,anchor="mm")
y+=strip_h+16

# money-shift navy strip (CBO)
money_h=118
draw.rounded_rectangle([(44,y),(WIDTH-44,y+money_h)],radius=8,fill=NAVY)
draw.text((WIDTH//2,y+20),"WHERE THE MONEY WENT  ·  CBO, enacted law, 2026-2034",fill=GOLD,font=f_label_s,anchor="mm")
half=(WIDTH-88)//2
draw.text((44+half//2,y+58),"-$900B",fill="#FEB2B2",font=f_stat,anchor="mm")
draw.text((44+half//2,y+90),"cut from Medicaid + SNAP",fill=WHITE,font=f_xs_b,anchor="mm")
draw.text((44+half+half//2,y+58),"+$3.3T",fill="#9AE6B4",font=f_stat,anchor="mm")
draw.text((44+half+half//2,y+90),"added via tax cuts (skewed to top)",fill=WHITE,font=f_xs_b,anchor="mm")
y+=money_h+14

# NY-23 kicker
draw.text((WIDTH//2,y),"NY-23: Rep. Langworthy voted Aye on H.R. 1 (Roll Call 190). About 26,000 Western",
          fill=DARK,font=font("Arial.ttf",16),anchor="mm"); y+=24
draw.text((WIDTH//2,y),"New Yorkers lose Essential Plan coverage. The state names H.R. 1 as the direct cause.",
          fill=DARK,font=font("Arial Bold.ttf",16),anchor="mm"); y+=30
draw.text((WIDTH//2,y),"Sources: NY DOH  ·  Fiscal Policy Institute  ·  Step Two Policy  ·  CBO  ·  House Clerk",
          fill=MUTED,font=f_src,anchor="mm"); y+=24
draw.text((WIDTH//2,y),"langworthywatch.org/fact-checks/2026-07-01-essential-plan-cliff-450k/",
          fill=NAVY,font=f_src,anchor="mm")
draw.rectangle([(0,HEIGHT-50),(WIDTH,HEIGHT)],fill=NAVY)
draw.text((WIDTH//2,HEIGHT-25),"langworthywatch.org  ·  NY-23 Accountability",fill=WHITE,font=f_footer,anchor="mm")

out="/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/essential_plan_cliff_card.png"
img.save(out,"PNG",dpi=(144,144)); print(f"Saved: {out}")
