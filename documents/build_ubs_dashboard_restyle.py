from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / 'assets'
OUT = ROOT / 'ubs-dashboard-ubs-palette.png'
W, H = 1600, 900

# White Treasury Committee slide + dark Bloomberg-style terminal chart panels.
PAGE = '#F7F7F4'
INK = '#24323B'
MUTED = '#65727A'
RULE = '#C9CECF'
UBS_RED = '#D71935'
CHART = '#101417'
CHART_RULE = '#293238'
CHART_TEXT = '#B8C1C5'
GREEN = '#00B386'
RED = '#F04452'
AMBER = '#FFB000'
CYAN = '#48B8D0'
WHITE = '#F3F5F5'
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
MONO = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'

im = Image.new('RGB',(W,H),PAGE)
d = ImageDraw.Draw(im)
_cache={}
def f(size,bold=False,mono=False):
    key=(size,bold,mono)
    if key not in _cache:
        _cache[key]=ImageFont.truetype(MONO if mono else (BOLD if bold else FONT),size)
    return _cache[key]
def txt(x,y,s,size=16,color=INK,bold=False,anchor=None,mono=False):
    d.text((x,y),s,font=f(size,bold,mono),fill=color,anchor=anchor)
def rule(x1,y1,x2,y2,color=RULE,width=1): d.line((x1,y1,x2,y2),fill=color,width=width)
def box(rect,color,outline=None,width=1): d.rectangle(rect,fill=color,outline=outline,width=width)
def dash(x1,y1,x2,y2,color,width=1,dash=7,gap=5):
    if abs(y2-y1)<1:
        x=x1
        while x<x2:
            d.line((x,y1,min(x+dash,x2),y2),fill=color,width=width);x+=dash+gap
    else:
        y=y1
        while y<y2:
            d.line((x1,y,x2,min(y+dash,y2)),fill=color,width=width);y+=dash+gap

def place_logo(src,xy,maxsize,remove_white=False):
    logo=Image.open(src).convert('RGBA')
    if remove_white:
        px=logo.load()
        for yy in range(logo.height):
            for xx in range(logo.width):
                r,g,b,a=px[xx,yy]
                if r>246 and g>246 and b>246:px[xx,yy]=(255,255,255,0)
    logo.thumbnail(maxsize,Image.Resampling.LANCZOS)
    im.paste(logo,xy,logo)

# Committee-style masthead: airy white canvas, logos, fine rules.
place_logo(ASSETS/'ubs-logo.png',(48,26),(188,66),True)
place_logo(ASSETS/'skema-logo.png',(1471,23),(76,76),False)
txt(270,29,'UBS INVESTMENT BANK  |  2011',28,INK,True)
txt(270,68,'ETF DELTA ONE DESK  ·  RISK ESCALATION',16,UBS_RED,True)
txt(270,98,'Treasury Committee briefing  /  operational risk, hidden exposure and controls',12,MUTED)
rule(48,135,1552,135,RULE,2)
txt(52,153,'THREE CONTROL STATES',10,MUTED,True)
txt(1548,153,'COMMITTEE VIEW  ·  SOURCE-LED',10,MUTED,True,anchor='ra')

# Terminal chart panel frame: square corners, tight typography, restrained grid.
def panel_frame(x,title,status,status_color,subtitle):
    y=179;w=480;h=573
    box((x,y,x+w,y+h),CHART,'#657078',1)
    box((x,y,x+w,y+4),UBS_RED if status=='UBS 2011' else status_color)
    txt(x+18,y+17,title,15,WHITE,True)
    txt(x+w-16,y+19,status,10,status_color,True,anchor='ra',mono=True)
    txt(x+18,y+43,subtitle,9,CHART_TEXT,False,mono=True)
    rule(x+16,y+67,x+w-16,y+67,CHART_RULE,1)
    return y,w,h

def chart_grid(x,y,w,h,labels=True):
    for n,val in enumerate((0,25,50,75,100)):
        yy=y+h-(val/100)*h
        rule(x,yy,x+w,yy,CHART_RULE,1)
        if labels:txt(x-9,yy-6,str(val),8,CHART_TEXT,False,anchor='ra',mono=True)

def profile_panel(x,title,status,status_color,subtitle,bars,risks,variant='normal'):
    y,w,h=panel_frame(x,title,status,status_color,subtitle)
    px=x+49;py=y+99;pw=w-68;ph=300;bottom=py+ph
    txt(x+18,y+77,'ACTIVITY INDEX   /   RISK VS LIMIT %',8,CHART_TEXT,False,mono=True)
    chart_grid(px,py,pw,ph)
    threshold=70;ty=bottom-(threshold/100)*ph
    dash(px,ty,px+pw,ty,AMBER,1,7,5)
    txt(px+5,ty-16,'LIMIT 70%',8,AMBER,True,mono=True)
    step=pw/len(bars);barw=step*.45;zero=bottom-ph*.50;pts=[]
    for i,(v,risk) in enumerate(zip(bars,risks)):
        mid=px+step*(i+.5)
        yy=bottom-(max(0,min(100,v))/100)*ph
        top=min(yy,zero);bh=max(2,abs(zero-yy))
        col=GREEN if v>=50 else RED
        d.rectangle((mid-barw/2,top,mid+barw/2,top+bh),fill=col)
        ry=bottom-(max(0,min(100,risk))/100)*ph
        pts.append((mid,ry))
        if i in (0,3,6,9,11):txt(mid,bottom+10,f'{i+1:02d}',7,CHART_TEXT,False,anchor='ma',mono=True)
    if len(pts)>1:
        d.line(pts,fill=AMBER,width=2,joint='curve')
        for qx,qy in pts:d.ellipse((qx-2,qy-2,qx+2,qy+2),fill=AMBER)
    # Compact terminal legend and explicit provenance label.
    yy=y+443
    box((x+18,yy+2,x+29,yy+10),GREEN);txt(x+35,yy-2,'P&L INDEX',8,CHART_TEXT,False,mono=True)
    rule(x+134,yy+6,x+157,yy+6,AMBER,2);txt(x+164,yy-2,'RISK INDEX',8,CHART_TEXT,False,mono=True)
    dash(x+280,yy+6,x+304,yy+6,AMBER,1,5,3);txt(x+311,yy-2,'LIMIT',8,CHART_TEXT,False,mono=True)
    rule(x+18,y+470,x+w-18,y+470,CHART_RULE,1)
    txt(x+18,y+486,'ILLUSTRATIVE PROFILE  ·  NOT UBS HISTORICAL DATA',8,AMBER,True,mono=True)
    if variant=='normal':
        txt(x+18,y+514,'Activity remains within the control envelope.',10,WHITE,True)
    else:
        txt(x+18,y+514,'Risk crosses limit; independent escalation is required.',10,WHITE,True)

# Reference profiles are explicitly illustrative, not reconstructed UBS histories.
profile_panel(52,'NORMAL TRADER','CONTROLS ON',GREEN,
              'REFERENCE CASE  /  CONTROLLED ACTIVITY',
              [53,61,58,66,62,71,68,74,69,79,73,76],
              [22,25,27,31,29,34,38,41,39,43,40,42],'normal')
profile_panel(560,'AGGRESSIVE TRADER','WARNING',AMBER,
              'TEACHING CASE  /  CONTROL PRESSURE',
              [51,58,66,76,82,72,61,53,47,43,40,36],
              [22,28,34,42,51,62,73,84,90,82,74,78],'aggressive')

# UBS facts panel: two sourced gross-notional peaks, not a false monthly series.
x=1068;y,w,h=panel_frame(1068,'KWEKU ADOBOLI  /  UBS','UBS 2011',UBS_RED,
                         'PUBLIC FACTS  /  POSITION PEAKS AND FINAL LOSS')
# clear source labels at top of chart
box((x+18,y+83,x+w-18,y+139),'#1B2226','#39454C',1)
txt(x+30,y+94,'FINAL TRADING LOSS',8,CHART_TEXT,True,mono=True)
txt(x+30,y+111,'USD 2.3bn',21,UBS_RED,True)
txt(x+w-30,y+116,'FINAL REPORTED LOSS',8,CHART_TEXT,False,anchor='ra',mono=True)
px=x+54;pw=w-82;bottom=y+405;ph=217
for val in (0,5,10,15):
    yy=bottom-(val/15)*ph
    rule(px,yy,px+pw,yy,CHART_RULE,1)
    txt(px-9,yy-6,str(val),8,CHART_TEXT,False,anchor='ra',mono=True)
txt(px,y+153,'GROSS FUTURES NOTIONAL  /  USD bn',8,CHART_TEXT,False,mono=True)
vals=[('LONG',12.1,'08 AUG',CYAN),('SHORT',8.5,'15 SEP',GREEN)]
for i,(lab,val,date,col) in enumerate(vals):
    bx=px+62+i*170;bh=(val/15)*ph
    d.rectangle((bx,bottom-bh,bx+75,bottom),fill=col)
    txt(bx+37,bottom-bh-22,f'{val:.1f}',11,WHITE,True,anchor='ma',mono=True)
    txt(bx+37,bottom+10,lab,8,WHITE,True,anchor='ma',mono=True)
    txt(bx+37,bottom+25,date,8,CHART_TEXT,False,anchor='ma',mono=True)
rule(x+18,y+458,x+w-18,y+458,CHART_RULE,1)
txt(x+18,y+475,'LONG PEAK  USD 12.1bn  /  8 AUG',9,CYAN,True,mono=True)
txt(x+18,y+497,'SHORT PEAK  USD 8.5bn  /  15 SEP',9,GREEN,True,mono=True)
txt(x+18,y+527,'Gross notional is exposure—not P&L.',9,WHITE,True)

# Clean white committee takeaway and source line (no decorative pills or gradients).
rule(52,780,1548,780,RULE,1)
txt(54,798,'KEY OBSERVATION',10,UBS_RED,True)
txt(54,819,'Control failure concealed positions and allowed risk to accumulate beyond effective oversight.',15,INK,True)
txt(54,850,'Comparative trader profiles are illustrative. UBS position peaks are gross notional; final loss is USD 2.3bn.',10,MUTED)
txt(54,875,'Sources: FINMA UBS investigation summary (2012); FCA Final Notice (2012).',9,MUTED)
txt(1546,875,'UBS  ×  SKEMA',9,INK,True,anchor='ra')

im.save(OUT,quality=96)
print(OUT)
