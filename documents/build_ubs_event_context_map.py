from pathlib import Path
import json
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parent
ASSETS=ROOT/'assets'
OUT=ROOT/'ubs-event-context-map.png'
W,H=1600,900
PAPER='#F7F7F4'; INK='#24323B'; MUTED='#68757C'; RULE='#C8CDCE'
PANEL='#101519'; PANEL_ALT='#161E23'; PANEL_RULE='#303A40'; MAP_BG='#0F1519'
LAND='#1A2429'; FOCUS_LAND='#222D33'; COAST='#46535A'; GEO_TEXT='#7D898F'
UBS_RED='#D71935'; BUBBLE='#758188'; BUBBLE_STROKE='#B2BABE'; WHITE='#F4F6F6'
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
MONO='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
fonts={}
def f(size,b=False,m=False):
    key=(size,b,m)
    if key not in fonts:fonts[key]=ImageFont.truetype(MONO if m else (BOLD if b else FONT),size)
    return fonts[key]
def text(x,y,s,size=16,color=INK,b=False,anchor=None,mono=False):
    d.text((x,y),s,font=f(size,b,mono),fill=color,anchor=anchor)
def line(x1,y1,x2,y2,color=RULE,width=1):d.line((x1,y1,x2,y2),fill=color,width=width)
def rect(box,fill,outline=None,width=1):d.rectangle(box,fill=fill,outline=outline,width=width)

im=Image.new('RGB',(W,H),PAPER); d=ImageDraw.Draw(im)
# Match the established UBS page header; remove only the white field around the UBS mark in memory.
logo=Image.open(ASSETS/'ubs-logo.png').convert('RGBA'); pixels=logo.load()
for yy in range(logo.height):
    for xx in range(logo.width):
        r,g,b,a=pixels[xx,yy]
        if r>246 and g>246 and b>246:pixels[xx,yy]=(255,255,255,0)
logo.thumbnail((188,66),Image.Resampling.LANCZOS); im.paste(logo,(48,23),logo)
sk=Image.open(ASSETS/'skema-logo.png').convert('RGBA');sk.thumbnail((74,74),Image.Resampling.LANCZOS);im.paste(sk,(1475,18),sk)
text(270,27,'WHY THE UBS EVENT MATTERS',28,INK,True)
text(270,68,'Contextualising the 2011 UBS trading loss within European banking incidents',14,UBS_RED,True)
text(270,98,'Treasury risk context  /  selected loss events',11,MUTED)
line(48,133,1552,133,RULE,2)

# Map panel and regional projection.
mx,my,mw,mh=50,155,940,540
rect((mx,my,mx+mw,my+mh),MAP_BG,'#3B464C',1)
map_base=im.copy()
lon0,lon1=-10.0,20.0; lat0,lat1=41.5,58.5
def xy(lon,lat):return (mx+(lon-lon0)/(lon1-lon0)*mw,my+(lat1-lat)/(lat1-lat0)*mh)
# Subtle geographic grid
for lon in [-5,0,5,10,15]:
    x=xy(lon,50)[0]; line(x,my,x,my+mh,'#1B252A',1)
for lat in [45,50,55]:
    y=xy(0,lat)[1]; line(mx,y,mx+mw,y,'#1B252A',1)

# Natural Earth 1:50m borders; surrounding countries muted, focal countries gently lifted.
with open(ASSETS/'natural-earth-50m-western-europe-context.geojson',encoding='utf-8') as fp:
    geo=json.load(fp)
geometries={feature['properties']['name']:feature['geometry'] for feature in geo['features']}
def draw_country(name,fill,stroke=COAST,width=1):
    geom=geometries[name]
    polys=geom['coordinates'] if geom['type']=='MultiPolygon' else [geom['coordinates']]
    for polygon in polys:
        ring=polygon[0]
        xs=[p[0] for p in ring]; ys=[p[1] for p in ring]
        if max(xs)<lon0 or min(xs)>lon1 or max(ys)<lat0 or min(ys)>lat1:continue
        pts=[xy(lon,lat) for lon,lat in ring]
        d.polygon(pts,fill=fill)
        d.line(pts+[pts[0]],fill=stroke,width=width,joint='curve')
for name in ['Portugal','Spain','Ireland','Belgium','Netherlands','Germany','Denmark','Czechia','Slovakia','Slovenia','Poland','Hungary','Italy','Austria','Luxembourg']:
    if name in geometries:draw_country(name,LAND,COAST,1)
for name in ['United Kingdom','France','Switzerland']:
    draw_country(name,FOCUS_LAND,'#65727A',1)

# Geographic labels, kept low-contrast and subordinate to event labels.
text(*xy(-3.4,53.2),'UNITED KINGDOM',9,GEO_TEXT,True,anchor='mm')



# Events and proportional area. Values used for area are approximate USD equivalents.
# Area is proportional to loss, hence radius is proportional to sqrt(value).
loss_usd={'CS':5.5,'JPM':6.2,'SG':4.9*1.4663,'UBS':2.3,'BARINGS':1.4}
maxr=65.0
radii={key:maxr*(value/max(loss_usd.values()))**0.5 for key,value in loss_usd.items()}

# City coordinates; circle centres are slightly offset within shared hub clusters for legibility.
city={
 'London':xy(-0.12,51.51),
 'Paris':xy(2.35,48.86),
 'Zurich':xy(8.54,47.38),
}
lx,ly=city['London']; px,py=city['Paris']; zx,zy=city['Zurich']
events={
 'JPM':(lx+25,ly-24,radii['JPM'],BUBBLE,'JPM','2012'),
 'BARINGS':(lx-78,ly+46,radii['BARINGS'],BUBBLE,'B','1995'),
 'SG':(px,py,radii['SG'],BUBBLE,'SG','2008'),
 'CS':(zx+53,zy-15,radii['CS'],BUBBLE,'CS','2021'),
 'UBS':(zx-50,zy+25,radii['UBS'],UBS_RED,'UBS','2011'),
}
# Leaders from precise city hub to offset circles.
for key,hub in [('JPM',city['London']),('BARINGS',city['London']),('SG',city['Paris']),('CS',city['Zurich']),('UBS',city['Zurich'])]:
    cx,cy,r,col,_,_=events[key];hx,hy=hub
    if abs(cx-hx)+abs(cy-hy)>1:line(hx,hy,cx,cy,'#88949A',1)
# Draw circles; UBS is the only saturated marker.
for key in ['BARINGS','JPM','SG','CS','UBS']:
    cx,cy,r,col,short,year=events[key]
    d.ellipse((cx-r,cy-r,cx+r,cy+r),fill=col,outline=WHITE if key=='UBS' else BUBBLE_STROKE,width=2 if key=='UBS' else 1)
    if key=='BARINGS':
        text(cx,cy-5,short,13,WHITE,True,anchor='mm')
        text(cx,cy+10,'95',7,WHITE,True,anchor='mm',mono=True)
    else:
        text(cx,cy-6,short,12,WHITE,True,anchor='mm')
        text(cx,cy+11,year,8,WHITE,True,anchor='mm',mono=True)
# Small location hubs and city labels.
for name,(hx,hy) in city.items():
    d.ellipse((hx-4,hy-4,hx+4,hy+4),fill=WHITE,outline=MAP_BG,width=1)
text(lx-6,ly+11,'LONDON',9,WHITE,True)
text(px+73,py+5,'PARIS',9,WHITE,True)
text(zx-15,zy+62,'ZURICH',9,WHITE,True)
# Direct-on-map event labels, sized small and unobtrusive.
text(lx-174,ly+89,'BARINGS · LEESON¹',8,'#C7CED1',True)
text(lx-18,ly-101,'JPMORGAN · LONDON WHALE',8,'#C7CED1',True)
text(px-77,py+radii['SG']+14,'SOCIÉTÉ GÉNÉRALE · KERVIEL',8,'#C7CED1',True)
text(zx-98,zy-radii['CS']-24,'CREDIT SUISSE · ARCHEGOS',8,'#C7CED1',True)
text(zx-radii['UBS']-77,zy+62,'UBS · 2011',8,UBS_RED,True)
# Map header/scale key; a dark strip keeps typography clear over northern coastlines.
rect((mx+1,my+1,mx+mw-1,my+36),MAP_BG)
text(mx+18,my+15,'EUROPEAN FINANCIAL HUBS',9,'#B7C0C4',True)
text(mx+mw-18,my+15,'CIRCLE AREA ∝ USD-EQUIVALENT LOSS',8,'#8F9BA1',True,anchor='ra',mono=True)

# Clip all country/circle art to the map frame.
clip=Image.new('L',(W,H),0);ImageDraw.Draw(clip).rectangle((mx,my,mx+mw,my+mh),fill=255)
im=Image.composite(im,map_base,clip);d=ImageDraw.Draw(im)
# Repaint map panel edge and top frame after clipping.
rect((mx,my,mx+mw,my+mh),None,'#3B464C',1)

# Right-side dark Bloomberg-style panel
rx,ry,rw,rh=1015,155,535,540
rect((rx,ry,rx+rw,ry+rh),PANEL,'#465158',1)
rect((rx,ry,rx+rw,ry+4),UBS_RED)
text(rx+23,ry+20,'SELECTED MAJOR TRADING LOSS EVENTS',14,WHITE,True)
text(rx+23,ry+48,'Headline loss · reported currency',9,'#A8B2B7')
text(rx+rw-23,ry+48,'SOURCE',7,'#89959B',True,anchor='ra',mono=True)
line(rx+22,ry+70,rx+rw-22,ry+70,PANEL_RULE,1)

def event_row(y,name,kind,value,source,accent=False):
    if accent:
        rect((rx+13,y-5,rx+rw-13,y+42),'#25171B')
        rect((rx+13,y-5,rx+17,y+42),UBS_RED)
    namecol=WHITE if accent else '#D1D7D9'
    valcol=UBS_RED if accent else '#C1C9CC'
    text(rx+26,y,name,11,namecol,True)
    text(rx+26,y+19,kind,8,'#859198')
    text(rx+rw-52,y+5,value,12,valcol,True,anchor='ra',mono=True)
    text(rx+rw-25,y+8,source,7,'#96A1A6',True,anchor='ra',mono=True)
    if not accent:line(rx+24,y+43,rx+rw-22,y+43,PANEL_RULE,1)

event_row(ry+83,'Credit Suisse (2021)','Archegos · prime brokerage','USD 5.5bn','[2]')
event_row(ry+132,'JPMorgan (2012)','London Whale · CIO portfolio','USD 6.2bn','[3]')
event_row(ry+181,'Société Générale (2008)','Kerviel · unauthorised positions','EUR 4.9bn','[4]')
event_row(ry+230,'UBS (2011)','ETF / Delta One · unauthorised','USD 2.3bn','[1]',True)
event_row(ry+279,'Barings (1995)','Leeson · concealed positions','USD 1.4bn','[5]')
# UBS badge statement
line(rx+22,ry+334,rx+rw-22,ry+334,PANEL_RULE,1)
rect((rx+23,ry+351,rx+109,ry+375),UBS_RED)
text(rx+66,ry+356,'UBS 2011',9,WHITE,True,anchor='mm',mono=True)
text(rx+123,ry+352,'One of the largest unauthorized trading losses',10,WHITE,True)
text(rx+123,ry+369,'recorded by a major European banking institution.',10,WHITE,True)
text(rx+23,ry+399,'Events differ; circle area tracks USD-equivalent loss.',8,'#A4AEB3')
text(rx+23,ry+439,'¹ Leeson traded in Singapore; London marks Barings HQ.',7,'#89959B')
text(rx+23,ry+453,'EUR conversion: ECB reference, 24 Jan 2008 (€1 = USD 1.4663) [6].',7,'#89959B')

# Executive takeaway: concise Treasury relevance, consistent with prior UBS styling.
line(48,728,1552,728,RULE,1)
text(52,746,'TREASURY LENS',9,UBS_RED,True)
text(52,768,'Delta One control failure: capital headroom, funding confidence and liquidity readiness.',16,INK,True)
text(52,806,'Sources: FINMA [1] · Credit Suisse Board Special Committee [2] · U.S. Senate PSI [3] · Société Générale [4] · RBA / BoE inquiry [5] · ECB FX [6].',8,MUTED)
text(52,826,'Loss values are approximate headline impacts; bank mechanisms and accounting bases differ. Barings’ official inquiry reports GBP amounts; USD 1.4bn is approximate.',7,MUTED)
text(1548,826,'DOCUMENTATION: documents/ubs-event-context-map-sources.md',7,MUTED,False,anchor='ra')

im.save(OUT)
print(OUT)
