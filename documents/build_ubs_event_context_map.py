from pathlib import Path
import json
from math import sqrt
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parent
ASSETS=ROOT/'assets'
OUT=ROOT/'ubs-event-context-map.png'
W,H=1600,900
PAPER='#F7F7F4'; INK='#24323B'; MUTED='#68757C'; RULE='#C8CDCE'
MAP_WATER='#FBFBF8'; MAP_LAND='#E2E4DE'; MAP_COAST='#BFC7C0'; WHITE='#FFFFFF'
PANEL='#101519'; PANEL_RULE='#303A40'
UBS_RED='#D71935'; CS_TEAL='#258675'; JPM_BLUE='#2476A8'; SG_PLUM='#8D3D68'; BARINGS_GOLD='#A9842E'
UK_FILL='#BDD7E6'; FR_FILL='#E6C1C8'; CH_FILL='#BCD0E1'
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
SERIF='/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
MONO='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
fonts={}
def f(size,b=False,m=False,serif=False):
    k=(size,b,m,serif)
    if k not in fonts:fonts[k]=ImageFont.truetype(SERIF if serif else (MONO if m else (BOLD if b else FONT)),size)
    return fonts[k]
def text(x,y,s,size=16,color=INK,b=False,anchor=None,mono=False,serif=False):
    d.text((x,y),s,font=f(size,b,mono,serif),fill=color,anchor=anchor)
def line(x1,y1,x2,y2,color=RULE,width=1):d.line((x1,y1,x2,y2),fill=color,width=width)
def rect(box,fill,outline=None,width=1):d.rectangle(box,fill=fill,outline=outline,width=width)
def rounded(box,fill,outline=None,width=1,radius=6):d.rounded_rectangle(box,radius=radius,fill=fill,outline=outline,width=width)
def crop_logo(path,remove_white=False):
    im=(path.copy() if isinstance(path,Image.Image) else Image.open(path)).convert('RGBA');p=im.load()
    if remove_white:
        for yy in range(im.height):
            for xx in range(im.width):
                r,g,b,a=p[xx,yy]
                if r>245 and g>245 and b>245:p[xx,yy]=(r,g,b,0)
    bbox=im.getchannel('A').point(lambda a:255 if a>12 else 0).getbbox()
    return im.crop(bbox) if bbox else im
def fit(im,maxw,maxh):
    ratio=min(maxw/im.width,maxh/im.height)
    return im.resize((max(1,round(im.width*ratio)),max(1,round(im.height*ratio))),Image.Resampling.LANCZOS)

im=Image.new('RGB',(W,H),PAPER);d=ImageDraw.Draw(im)
# UBS header identity, matching the established executive presentation.
mark=crop_logo(ASSETS/'ubs-logo.png',True);mark.thumbnail((188,66),Image.Resampling.LANCZOS);im.paste(mark,(48,23),mark)
sk=Image.open(ASSETS/'skema-logo.png').convert('RGBA');sk.thumbnail((74,74),Image.Resampling.LANCZOS);im.paste(sk,(1475,18),sk)
text(270,27,'MAJOR EUROPEAN TRADING LOSS EVENTS',27,INK,True)
text(270,68,'Selected benchmark trading-loss events relevant to the UBS 2011 case',14,UBS_RED,True)
text(270,98,'European banking  /  nominal headline impacts',11,MUTED)
line(48,133,1552,133,RULE,2)

# Bank marks. Barings Bank historically used a heraldic crest; retain a period-neutral wordmark.
logos={
 'CS':crop_logo(ASSETS/'credit-suisse-logo.png'),
 'JPM':crop_logo(ASSETS/'jpmorgan-chase-logo.png'),
 'SG':crop_logo(ASSETS/'societe-generale-logo.png'),
 'UBS':crop_logo(ASSETS/'ubs-logo.png',True),
}
barings=Image.new('RGBA',(460,100),(255,255,255,0));bd=ImageDraw.Draw(barings)
bd.text((8,3),'BARINGS',font=f(68,True,serif=True),fill=BARINGS_GOLD)
logos['BARINGS']=crop_logo(barings)
brand={'CS':CS_TEAL,'JPM':JPM_BLUE,'SG':SG_PLUM,'UBS':UBS_RED,'BARINGS':BARINGS_GOLD}

# Stylized western-Europe map: relevant countries in colour, all other countries grey.
mx,my,mw,mh=150,145,1300,650
rect((mx,my,mx+mw,my+mh),MAP_WATER)
map_base=im.copy()
lon0,lon1=-12.0,20.0;lat0,lat1=42.0,58.0
def xy(lon,lat):return (mx+(lon-lon0)/(lon1-lon0)*mw,my+(lat1-lat)/(lat1-lat0)*mh)
with open(ASSETS/'natural-earth-50m-western-europe-context.geojson',encoding='utf-8') as fp:geo=json.load(fp)
geometries={feature['properties']['name']:feature['geometry'] for feature in geo['features']}
def draw_country(name,fill,stroke=MAP_COAST,width=1):
    geom=geometries[name];polys=geom['coordinates'] if geom['type']=='MultiPolygon' else [geom['coordinates']]
    for polygon in polys:
        ring=polygon[0];xs=[q[0] for q in ring];ys=[q[1] for q in ring]
        if max(xs)<lon0 or min(xs)>lon1 or max(ys)<lat0 or min(ys)>lat1:continue
        pts=[xy(lon,lat) for lon,lat in ring]
        d.polygon(pts,fill=fill)
        d.line(pts+[pts[0]],fill=stroke,width=width,joint='curve')
# Paint context first. Only UK, France and Switzerland receive event-territory fills.
for name in ['Portugal','Spain','Ireland','Belgium','Netherlands','Germany','Denmark','Czechia','Slovakia','Slovenia','Poland','Hungary','Italy','Austria','Luxembourg']:
    if name in geometries:draw_country(name,MAP_LAND,MAP_COAST,1)
draw_country('United Kingdom',UK_FILL,WHITE,2)
draw_country('France',FR_FILL,WHITE,2)
draw_country('Switzerland',CH_FILL,WHITE,2)
# Subtle country name labels, no pins or leader lines.
text(*xy(-3.8,54.1),'UNITED KINGDOM',9,'#64747C',True,anchor='mm')
text(*xy(0.2,45.8),'FRANCE',10,'#78666B',True,anchor='mm')
text(944,652,'SWITZERLAND',8,'#667583',True,anchor='mm')

# Relative-loss circles are area-proportional in approximate USD equivalent.
# EUR 4.9bn uses ECB 24-Jan-2008 reference USD 1.4663/EUR for sizing only.
loss_usd={'CS':5.5,'JPM':6.2,'SG':4.9*1.4663,'UBS':2.3,'BARINGS':1.4}
rmax=50.0
radii={k:rmax*sqrt(v/max(loss_usd.values())) for k,v in loss_usd.items()}
# Country badge anchors: both London events share the UK; both Zurich events share Switzerland.
centres={
 'JPM':(xy(-0.05,52.15)[0]+18,xy(-0.05,52.15)[1]-5),
 'BARINGS':(xy(-1.25,51.55)[0]-45,xy(-1.25,51.55)[1]+28),
 'SG':xy(2.35,48.86),
 'CS':(xy(8.54,47.38)[0]+42,xy(8.54,47.38)[1]-9),
 'UBS':(xy(8.54,47.38)[0]-43,xy(8.54,47.38)[1]+17),
}

# Main map circles are event badges, not location pins: logos sit inside each selected territory.
def event_badge(key,year,amount,event_label,amount_label_pos=None):
    global d
    cx,cy=centres[key];r=radii[key];col=brand[key]
    # Country-colour disc, proportional by area to headline USD-equivalent loss.
    d.ellipse((cx-r,cy-r,cx+r,cy+r),fill=col,outline=WHITE,width=2)
    # White inset logo tile improves legibility while keeping the country/event hue visible.
    inner_w=max(34,2*r-12);inner_h=max(16,int(r*.62))
    rounded((cx-inner_w/2,cy-inner_h/2-5,cx+inner_w/2,cy+inner_h/2-5),WHITE,None,0,4)
    logo=fit(logos[key],inner_w-8,inner_h-4)
    im.paste(logo,(round(cx-logo.width/2),round(cy-logo.height/2-5)),logo)
    d=ImageDraw.Draw(im)
    # Short year and city/event label directly adjacent to the badge.
    text(cx,cy+r*.61,year,8,WHITE,True,anchor='mm',mono=True)
    if amount_label_pos:
        ax,ay=amount_label_pos
    else:
        ax,ay=cx+r+5,cy-r*.2
    label_w=88 if len(amount)<11 else 98
    rounded((ax-4,ay-3,ax+label_w,ay+17),WHITE,col,1,5)
    text(ax+2,ay,amount,9,col,True)
    text(cx,cy-r-13,event_label,7,col,True,anchor='mm')

# Place badges fully within the highlighted country silhouettes, with modest offsets in shared hubs.
# UK: London Whale and Barings / Leeson.
event_badge('JPM','2012','USD 6.2bn','JPMORGAN',(centres['JPM'][0]-36,centres['JPM'][1]+radii['JPM']+5))
event_badge('BARINGS','1995','~USD 1.4bn','BARINGS',(centres['BARINGS'][0]-83,centres['BARINGS'][1]+radii['BARINGS']+1))
# France: Paris / Île-de-France, Société Générale.
event_badge('SG','2008','EUR 4.9bn','SOCIÉTÉ GÉNÉRALE',(centres['SG'][0]-47,centres['SG'][1]+radii['SG']+5))
# Switzerland: UBS and Credit Suisse remain in Zurich; badge positions are offset for legibility.
event_badge('CS','2021','USD 5.5bn','CREDIT SUISSE',(centres['CS'][0]+radii['CS']+4,centres['CS'][1]-8))
event_badge('UBS','2011','USD 2.3bn','UBS',(centres['UBS'][0]-10,centres['UBS'][1]+radii['UBS']+4))
# Headquarters and desk locations are clarified in the footer; badge offsets are for legibility.
# Map title and compact scale note.
text(mx+16,my+14,'WESTERN EUROPE  /  SELECTED BANKING EVENTS',9,MUTED,True)
text(mx+mw-16,my+14,'CIRCLE AREA ∝ USD-EQUIVALENT LOSS',8,MUTED,True,anchor='ra',mono=True)
# Clip the country art and badges to the map canvas.
clip=Image.new('L',(W,H),0);ImageDraw.Draw(clip).rectangle((mx,my,mx+mw,my+mh),fill=255)
im=Image.composite(im,map_base,clip);d=ImageDraw.Draw(im)

# Executive takeaway: one concise line over a restrained UBS-red rule.
line(48,808,1552,808,RULE,1)
text(52,822,'EXECUTIVE TAKEAWAY',8,UBS_RED,True)
text(52,839,"UBS's USD 2.3bn trading loss ranks among the most significant banking trading-loss events in Europe and illustrates how control failures can rapidly escalate into material financial and liquidity-management consequences.",10,INK,True)
text(52,866,'Sources: FINMA [1] · Credit Suisse Board Special Committee [2] · U.S. Senate PSI [3] · Société Générale [4] · RBA / BoE inquiry [5] · ECB FX [6].',7,MUTED)
text(1548,866,'Institutional bases: Barings—London; UBS & Credit Suisse—Zurich; Société Générale—Paris. JPMorgan event and UBS loss desk—London; Leeson traded in Singapore.',7,MUTED,False,anchor='ra')

im.save(OUT)
print(OUT)
