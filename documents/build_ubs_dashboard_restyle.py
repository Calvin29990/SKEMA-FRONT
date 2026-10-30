from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / 'assets'
OUT = ROOT / 'ubs-dashboard-ubs-palette.png'
W, H = 1600, 900

# Brand-led UBS palette, deliberately richer than monochrome black / white / red.
BG = '#EAE9E4'          # warm stone canvas
CARD = '#F8F7F3'        # soft ivory cards
CARD_ALT = '#F1F2EF'
INK = '#253642'         # blue-charcoal text
MUTED = '#71808A'
GRID = '#D3D8D6'
UBS_RED = '#D71935'
TEAL = '#147D78'
GREEN = '#34866A'
AMBER = '#D18A2F'
BLUE = '#426A8A'
PALE_RED = '#F8E8E9'
PALE_AMBER = '#F8F0E3'
PALE_GREEN = '#E8F1EC'

REG = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
fonts = {}
def font(size, bold=False):
    key=(size,bold)
    if key not in fonts: fonts[key] = ImageFont.truetype(BOLD if bold else REG, size)
    return fonts[key]

im = Image.new('RGB', (W,H), BG)
d = ImageDraw.Draw(im)

def text(x,y,s,size=16,color=INK,bold=False,anchor=None):
    d.text((x,y), s, font=font(size,bold), fill=color, anchor=anchor)
def line(x1,y1,x2,y2,color=GRID,width=1):
    d.line((x1,y1,x2,y2), fill=color, width=width)
def rounded(box,r=14,fill=CARD,outline=None,width=1):
    d.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)
def pill(x,y,label,color,bg):
    f=font(12,True); bb=d.textbbox((0,0),label,font=f); w=bb[2]+26
    d.rounded_rectangle((x,y,x+w,y+30),radius=15,fill=bg)
    d.text((x+13,y+7),label,font=f,fill=color)
    return w

def draw_ubs_logo(path, box):
    logo=Image.open(path).convert('RGBA')
    pix=logo.load()
    for yy in range(logo.height):
        for xx in range(logo.width):
            r,g,b,a=pix[xx,yy]
            if r>246 and g>246 and b>246:
                pix[xx,yy]=(255,255,255,0)
    logo.thumbnail(box, Image.Resampling.LANCZOS)
    im.paste(logo,(50,24),logo)

def draw_skema_logo(path):
    logo=Image.open(path).convert('RGBA')
    logo.thumbnail((78,78),Image.Resampling.LANCZOS)
    im.paste(logo,(1470,22),logo)

# Header
draw_ubs_logo(ASSETS/'ubs-logo.png',(192,72))
draw_skema_logo(ASSETS/'skema-logo.png')
text(275,30,'UBS INVESTMENT BANK  |  2011',31,INK,True)
text(275,74,'ETF Delta One Desk  ·  Risk escalation',20,UBS_RED,True)
text(275,108,'Operational risk  /  hidden exposure  /  control failure',13,MUTED)
line(50,150,1550,150,GRID,2)

# Header over the dashboard panels
text(54,166,'THREE CONTROL STATES',12,BLUE,True)
text(1547,166,'EXECUTIVE VIEW',12,MUTED,True,anchor='ra')

# Chart utility for the two illustrative comparison panels.
def draw_profile_card(x, title, status, status_color, status_bg, subtitle, bars, risks, control_limit=70, negative_from=None):
    y=192; w=478; h=536
    rounded((x,y,x+w,y+h),16,CARD,GRID,2)
    # Accent rule and heading
    d.rounded_rectangle((x,y,x+w,y+8),radius=5,fill=status_color)
    text(x+24,y+26,title,18,INK,True)
    pill(x+w-185,y+22,status,status_color,status_bg)
    text(x+24,y+60,subtitle,12,MUTED)
    # Chart frame
    cx=x+60; cy=y+108; cw=w-91; ch=250
    left=cy; bottom=cy+ch
    d.rounded_rectangle((cx-28,cy-10,cx+cw+10,bottom+9),radius=7,fill='#F5F5F1',outline='#E2E4E0',width=1)
    # horizontal guide lines + labels on a normalized index scale
    for val in (0,25,50,75,100):
        yy=bottom-(val/100)*ch
        line(cx,yy,cx+cw,yy,'#DEE2DF',1)
        text(cx-39,yy-8,str(val),9,MUTED,False,anchor='ra')
    # control line
    limy=bottom-(control_limit/100)*ch
    line(cx,limy,cx+cw,limy,AMBER,2)
    text(cx+5,limy-19,'CONTROL LIMIT',9,AMBER,True)
    # bars: visual index only; no currency claim
    n=len(bars); step=cw/n; bw=step*0.48
    zero=bottom-(50/100)*ch
    riskpts=[]
    for i,(v,risk) in enumerate(zip(bars,risks)):
        mid=cx+step*(i+.5)
        # P&L bars are normalized around 50; label explicitly as index below.
        yy=bottom-(max(0,min(100,v))/100)*ch
        top=min(yy,zero); bh=max(2,abs(zero-yy))
        if v>=50: col=TEAL if status!='RISK RISING' else (GREEN if i<6 else UBS_RED)
        else: col=UBS_RED
        d.rounded_rectangle((mid-bw/2,top,mid+bw/2,top+bh),radius=3,fill=col)
        ry=bottom-(max(0,min(100,risk))/100)*ch
        riskpts.append((mid,ry))
        if i in (0,3,6,10): text(mid,bottom+15,f'M{i+1}',8,MUTED,False,anchor='ma')
    # risk line with circular markers
    if len(riskpts)>1:
        d.line(riskpts,fill=BLUE,width=4,joint='curve')
        for px,py in riskpts:d.ellipse((px-4,py-4,px+4,py+4),fill=BLUE,outline=CARD,width=1)
    # chart labels + legend
    text(x+24,y+404,'Normalized activity / risk index · illustrative',10,MUTED)
    d.rounded_rectangle((x+25,y+438,x+38,y+451),radius=2,fill=TEAL)
    text(x+46,y+436,'Activity index',10,INK)
    line(x+164,y+445,x+192,y+445,BLUE,3)
    text(x+199,y+436,'Risk index',10,INK)
    line(x+304,y+445,x+331,y+445,AMBER,2)
    text(x+338,y+436,'Limit',10,INK)
    line(x+24,y+474,x+w-24,y+474,GRID,1)
    if status=='CONTROLLED':
        takeaway='Activity remains inside the control envelope.'
    else:
        takeaway='Escalating exposure calls for independent review.'
    text(x+24,y+491,takeaway,12,INK,True)

# Illustrative profiles are normalized and clearly identified as teaching scenarios.
draw_profile_card(54,'NORMAL TRADER','CONTROLLED',GREEN,PALE_GREEN,
                  'REFERENCE SCENARIO  ·  controls operating',
                  [53,61,58,66,62,71,68,74,69,79,73],
                  [22,25,27,31,29,34,38,41,39,43,40])
draw_profile_card(561,'AGGRESSIVE TRADER','RISK RISING',AMBER,PALE_AMBER,
                  'ILLUSTRATIVE SCENARIO  ·  controls under pressure',
                  [51,58,66,76,82,72,61,53,47,43,40],
                  [22,28,34,42,51,62,73,84,90,82,74])

# UBS factual panel. No invented historical monthly series.
x=1068; y=192; w=478; h=536
rounded((x,y,x+w,y+h),16,CARD,GRID,2)
d.rounded_rectangle((x,y,x+w,y+8),radius=5,fill=UBS_RED)
text(x+24,y+26,'KWEKU ADOBOLI',18,INK,True)
pill(x+w-160,y+22,'UBS · 2011',UBS_RED,PALE_RED)
text(x+24,y+60,'SOURCED PUBLIC FACTS  ·  NOT A MONTHLY SERIES',11,MUTED,True)
# Metric cards
rounded((x+24,y+99,x+224,y+185),10,'#F0F2EF','#DDE1DD',1)
rounded((x+236,y+99,x+w-24,y+185),10,PALE_RED,'#EFD4D7',1)
text(x+39,y+112,'PEAK LONG FUTURES',9,MUTED,True)
text(x+39,y+137,'USD 12.1bn',23,BLUE,True)
text(x+39,y+166,'8 August  ·  gross notional',9,MUTED)
text(x+251,y+112,'FINAL TRADING LOSS',9,UBS_RED,True)
text(x+251,y+137,'USD 2.3bn',23,UBS_RED,True)
text(x+251,y+166,'final reported loss',9,MUTED)
# Separate gross-notional comparison chart
chartx=x+55; charty=y+233; chartw=340; chartbottom=y+430; maxv=14
for val in (0,5,10):
    yy=chartbottom-(val/maxv)*150
    line(chartx,yy,chartx+chartw,yy,'#DEE2DF',1)
    text(chartx-12,yy-7,str(val),9,MUTED,False,anchor='ra')
text(chartx,charty-13,'FUTURES POSITIONS · USD bn, GROSS NOTIONAL',9,MUTED,True)
vals=[('LONG',12.1,BLUE,'8 AUG'),('SHORT',8.5,TEAL,'15 SEP')]
for i,(lab,val,col,date) in enumerate(vals):
    bx=chartx+75+i*170; bh=(val/maxv)*150
    d.rounded_rectangle((bx,chartbottom-bh,bx+80,chartbottom),radius=6,fill=col)
    text(bx+40,chartbottom-bh-28,f'{val:g}',13,INK,True,anchor='ma')
    text(bx+40,chartbottom+10,lab,10,INK,True,anchor='ma')
    text(bx+40,chartbottom+29,date,9,MUTED,False,anchor='ma')
# Short position fact and accurate caveat
rounded((x+24,y+475,x+w-24,y+510),8,'#EFF3F2','#DDE3E0',1)
text(x+38,y+484,'Peak short futures: USD 8.5bn · 15 September',10,TEAL,True)
text(x+24,y+516,'Gross notional is exposure—not P&L.',10,MUTED,True)

# Bottom insight ribbon
rounded((54,750,1546,853),14,'#DDE7E4','#CFD9D5',1)
text(78,768,'KEY OBSERVATION',11,UBS_RED,True)
text(78,790,'Control failure concealed positions and allowed risk to accumulate beyond effective oversight.',16,INK,True)
text(78,823,'Teaching profiles are illustrative; UBS panel uses sourced facts. Loss and gross exposure are separate measures.',11,MUTED)
# source/footer line
text(54,871,'Sources: FINMA UBS investigation summary (2012); FCA Final Notice (2012). UBS positions are gross notional, not P&L.',9,MUTED)
text(1545,871,'UBS  ×  SKEMA',9,BLUE,True,anchor='ra')

im.save(OUT,quality=96)
print(OUT)
