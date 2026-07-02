#!/usr/bin/env python3
"""Social card: Liberty Strategies disclosure gap, July 2 2026. MISSING CONTEXT.
What the public can see vs cannot; office no-response strip. No em dashes."""

from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1080, 1080
FONT_DIR = "/System/Library/Fonts/Supplemental/"
BG="#F5F7FA"; NAVY="#1E3A5F"; DARK="#1A202C"; GREEN="#276749"; RED="#E53E3E"
ORANGE="#C05621"; GOLD="#D69E2E"; MUTED="#718096"; BORDER="#E2E8F0"; WHITE="#FFFFFF"

def font(n,s):
    try: return ImageFont.truetype(f"{FONT_DIR}{n}", s)
    except Exception: return ImageFont.load_default()
f_brand=font("Arial Bold.ttf",22); f_tag=font("Arial Bold.ttf",20); f_topic=font("Arial Bold.ttf",29)
f_label=font("Arial Bold.ttf",20); f_label_s=font("Arial Bold.ttf",16); f_big=font("Impact.ttf",62)
f_stat=font("Impact.ttf",36); f_sub_b=font("Arial Bold.ttf",19); f_sub=font("Arial.ttf",17)
f_small=font("Arial.ttf",16); f_xs=font("Arial.ttf",14); f_xs_b=font("Arial Bold.ttf",14)
f_src=font("Arial.ttf",15); f_footer=font("Arial Bold.ttf",20)

img=Image.new("RGB",(WIDTH,HEIGHT),BG); draw=ImageDraw.Draw(img)
draw.rectangle([(0,0),(WIDTH,48)],fill=NAVY)
draw.text((WIDTH//2,24),"LANGWORTHYWATCH.ORG",fill=WHITE,font=f_brand,anchor="mm")
y=62

tag="MISSING CONTEXT"; tb=draw.textbbox((0,0),tag,font=f_tag); tw,th=tb[2]-tb[0]+28,tb[3]-tb[1]+12
draw.rounded_rectangle([((WIDTH-tw)//2,y),((WIDTH+tw)//2,y+th)],radius=5,fill="#744210",outline=GOLD,width=2)
draw.text((WIDTH//2,y+th//2),tag,fill=GOLD,font=f_tag,anchor="mm"); y+=th+22
draw.text((WIDTH//2,y),"The Consulting Firm on His Disclosures",fill=NAVY,font=f_topic,anchor="mm"); y+=38
draw.line([(60,y),(WIDTH-60,y)],fill=BORDER,width=2); y+=16

claim_h=110
draw.rounded_rectangle([(44,y),(WIDTH-44,y+claim_h)],radius=8,fill="#FFFAF0",outline="#F6AD55",width=2)
draw.text((76,y+18),"ON HIS FEDERAL DISCLOSURES  ·  2022, 2024, 2025",fill=ORANGE,font=f_label_s,anchor="lm")
draw.text((76,y+50),"Spouse income source: Liberty Strategies LLC (Tonawanda, formed Jan 2019)",fill=DARK,font=f_sub,anchor="lm")
draw.text((76,y+80),"Amount listed: N/A. House rules require the source, not the number.",fill=DARK,font=f_sub,anchor="lm")
y+=claim_h+16

col_w=(WIDTH-44*2-16)//2; col_h=340; lx=44; rx=lx+col_w+16
draw.rounded_rectangle([(lx,y),(lx+col_w,y+col_h)],radius=8,fill="#EBF8F0",outline="#9AE6B4",width=2)
draw.text((lx+col_w//2,y+22),"WHAT THE PUBLIC COULD SEE",fill=GREEN,font=f_label_s,anchor="mm")
draw.text((lx+col_w//2,y+38),"through 2022, via FEC filings",fill=MUTED,font=f_xs,anchor="mm")
draw.text((lx+col_w//2,y+104),"$103,604",fill=GREEN,font=f_big,anchor="mm")
draw.text((lx+col_w//2,y+164),"from 3 NY GOP campaign committees",fill=DARK,font=f_sub_b,anchor="mm")
draw.text((lx+col_w//2,y+196),"Jacobs for Congress: $71,035",fill=DARK,font=f_sub,anchor="mm")
draw.text((lx+col_w//2,y+224),"Tom Reed PAC: $17,569",fill=DARK,font=f_sub,anchor="mm")
draw.text((lx+col_w//2,y+252),"Singletary 4 Congress: $15,000",fill=DARK,font=f_sub,anchor="mm")
draw.text((lx+col_w//2,y+292),"39 itemized payments, 2019 to 2022,",fill=MUTED,font=f_xs,anchor="mm")
draw.text((lx+col_w//2,y+310),"re-verified against the FEC API",fill=MUTED,font=f_xs,anchor="mm")

draw.rounded_rectangle([(rx,y),(rx+col_w,y+col_h)],radius=8,fill="#FFF5F5",outline="#FEB2B2",width=2)
draw.text((rx+col_w//2,y+22),"WHAT IT CANNOT SEE",fill=RED,font=f_label_s,anchor="mm")
draw.text((rx+col_w//2,y+38),"2023 to today",fill=MUTED,font=f_xs,anchor="mm")
draw.text((rx+col_w//2,y+104),"N/A",fill=RED,font=f_big,anchor="mm")
draw.text((rx+col_w//2,y+164),"the amount, every single year",fill=DARK,font=f_sub_b,anchor="mm")
draw.text((rx+col_w//2,y+196),"Clients since 2022: none appear in",fill=DARK,font=f_sub,anchor="mm")
draw.text((rx+col_w//2,y+224),"FEC or NY State election databases",fill=DARK,font=f_sub,anchor="mm")
draw.text((rx+col_w//2,y+252),"2023: absent from his filing entirely",fill=DARK,font=f_sub,anchor="mm")
draw.text((rx+col_w//2,y+292),"Yet the firm reappears as an income",fill=MUTED,font=f_xs,anchor="mm")
draw.text((rx+col_w//2,y+310),"source on the 2024 and 2025 filings",fill=MUTED,font=f_xs,anchor="mm")
y+=col_h+16

strip_h=104
draw.rounded_rectangle([(44,y),(WIDTH-44,y+strip_h)],radius=8,fill="#EDF2F7",outline=BORDER,width=2)
draw.text((WIDTH//2,y+22),"WE ASKED HIS OFFICE",fill=NAVY,font=f_label,anchor="mm")
third=(WIDTH-88)//3
for i,(val,l1,c) in enumerate([
    ("June 24","six questions submitted",NAVY),
    ("July 1","deadline we gave them",NAVY),
    ("Nothing","response received",RED),
]):
    cx=44+i*third+third//2
    draw.text((cx,y+56),val,fill=c,font=f_stat,anchor="mm")
    draw.text((cx,y+86),l1,fill=DARK,font=f_xs_b,anchor="mm")
y+=strip_h+16

kick_h=96
draw.rounded_rectangle([(44,y),(WIDTH-44,y+kick_h)],radius=8,fill=NAVY)
draw.text((WIDTH//2,y+32),"No allegation of wrongdoing. A spouse's career is normal and legal.",fill="#CBD5E0",font=font("Arial.ttf",17),anchor="mm")
draw.text((WIDTH//2,y+64),"The gap is what disclosure rules leave invisible: amounts, clients, current work.",fill=WHITE,font=font("Arial Bold.ttf",17),anchor="mm")
y+=kick_h+16
draw.text((WIDTH//2,y),"Sources: House Clerk financial disclosures  ·  FEC  ·  NY Dept. of State  ·  NYS Board of Elections",
          fill=MUTED,font=f_src,anchor="mm"); y+=24
draw.text((WIDTH//2,y),"langworthywatch.org/fact-checks/2026-06-24-liberty-strategies-disclosure/",
          fill=NAVY,font=f_src,anchor="mm")
draw.rectangle([(0,HEIGHT-50),(WIDTH,HEIGHT)],fill=NAVY)
draw.text((WIDTH//2,HEIGHT-25),"langworthywatch.org  ·  NY-23 Accountability",fill=WHITE,font=f_footer,anchor="mm")

out="/Users/zachbeaudoin/projects/Langworthywatch/langworthy-tracker/social-media/liberty_strategies_card.png"
img.save(out,"PNG",dpi=(144,144)); print(f"Saved: {out}")
