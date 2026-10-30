from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parent
ASSETS=ROOT/'assets'
OUT=ROOT/'ubs-uk-france-bank-map.png'
W,H=1600,900
PAGE='#F7F7F4'; INK='#20323D'; MUTED='#6B7981'; RULE='#C8D0D2'
WATER='#E9F0F1'; LAND='#E5E6E0'; UK_FILL='#D4E1DC'; FR_FILL='#DCE6E8'; BORDER='#AAB5B5'
UBS_RED='#D71935'; GREEN='#13866E'; DARK='#30373D'; WHITE='#FFFFFF'; MAPLINE='#BDC6C5'
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'; MONO='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
fonts={}
def f(n,b=False,m=False):
    k=(n,b,m)
    if k not in fonts:fonts[k]=ImageFont.truetype(MONO if m else (BOLD if b else FONT),n)
    return fonts[k]
def txt(x,y,s,n=16,c=INK,b=False,anchor=None,m=False):d.text((x,y),s,font=f(n,b,m),fill=c,anchor=anchor)
def line(a,b,c,e,color=RULE,width=1):d.line((a,b,c,e),fill=color,width=width)
def rect(box,fill,outline=None,width=1):d.rectangle(box,fill=fill,outline=outline,width=width)

im=Image.new('RGB',(W,H),PAGE);d=ImageDraw.Draw(im)
# UBS and SKEMA logos
logo=Image.open(ASSETS/'ubs-logo.png').convert('RGBA');p=logo.load()
for yy in range(logo.height):
    for xx in range(logo.width):
        r,g,b,a=p[xx,yy]
        if r>246 and g>246 and b>246:p[xx,yy]=(255,255,255,0)
logo.thumbnail((172,61),Image.Resampling.LANCZOS);im.paste(logo,(42,24),logo)
sk=Image.open(ASSETS/'skema-logo.png').convert('RGBA');sk.thumbnail((70,70),Image.Resampling.LANCZOS);im.paste(sk,(1480,18),sk)

txt(248,28,'UK & FRANCE  |  BANKING RESULTS 2011',28,INK,True)
txt(248,68,'UBS unauthorized-trading loss highlighted separately',16,UBS_RED,True)
txt(248,98,'Public group net income at major UK / French banking hubs',12,MUTED)
line(42,132,1558,132,RULE,2)

# Map projection (schematic regional frame; callouts identify cities and reporting groups).
mx,my,mw,mh=45,165,935,615
rect((mx,my,mx+mw,my+mh),WATER,'#D2DADB',1)
_map_base=im.copy()
lon0,lon1=-12.0,11.5; lat0,lat1=41.3,59.2
def xy(lon,lat):return (mx+(lon-lon0)/(lon1-lon0)*mw,my+(lat1-lat)/(lat1-lat0)*mh)
def poly(coords,fill,outline=BORDER,width=2):
    d.polygon([xy(lon,lat) for lon,lat in coords],fill=fill)
    d.line([xy(lon,lat) for lon,lat in coords+[coords[0]]],fill=outline,width=width,joint='curve')

# Natural Earth 1:50m country boundaries; neighboring land is muted, UK and France highlighted.
import json
with open(ASSETS/'natural-earth-50m-uk-france-context.geojson',encoding='utf-8') as _fp:
    _geodata=json.load(_fp)
_geos={feature['properties']['name']:feature['geometry'] for feature in _geodata['features']}
def draw_country(name,fill,outline,width=1):
    geometry=_geos[name]
    polygons=geometry['coordinates'] if geometry['type']=='MultiPolygon' else [geometry['coordinates']]
    for polygon in polygons:
        ring=polygon[0]
        xs=[p[0] for p in ring];ys=[p[1] for p in ring]
        if max(xs)<lon0 or min(xs)>lon1 or max(ys)<lat0 or min(ys)>lat1:continue
        pts=[xy(lon,lat) for lon,lat in ring]
        d.polygon(pts,fill=fill)
        d.line(pts+[pts[0]],fill=outline,width=width,joint='curve')
for _name in ['Spain','Ireland','Belgium','Netherlands','Germany','Luxembourg','Switzerland']:
    draw_country(_name,LAND,BORDER,1)
draw_country('United Kingdom',UK_FILL,'#7F9991',2)
draw_country('France',FR_FILL,'#8A9DA1',2)
# Map labels
txt(*xy(-4.3,57.8),'SCOTLAND',10,'#70827F',True,anchor='mm')
txt(*xy(-2.7,52.7),'ENGLAND & WALES',10,'#70827F',True,anchor='mm')
txt(*xy(1.6,46.1),'FRANCE',16,'#74878B',True,anchor='mm')

# Cities / bank hubs
cities={'EDINBURGH':(-3.19,55.95),'LONDON':(-0.12,51.51),'PARIS':(2.35,48.86)}
for name,(lon,lat) in cities.items():
    cx,cy=xy(lon,lat)
    d.ellipse((cx-8,cy-8,cx+8,cy+8),fill=INK,outline=WHITE,width=3)
    # small label offsets for clear placement
    if name=='EDINBURGH':txt(cx+12,cy-28,name,10,INK,True)
    elif name=='LONDON':txt(cx+14,cy+10,name,10,INK,True)
    else:txt(cx+14,cy-24,name,10,INK,True)
# Sign dots visually distinguish financial results; no proportional size encoding.
for cx,cy,color,offsets in [
    (*xy(-0.12,51.51),UBS_RED,[(-18,-18)]),
    (*xy(-0.12,51.51),GREEN,[(0,-18),(18,-18)]),
    (*xy(-0.12,51.51),DARK,[(0,18)]),
    (*xy(-3.19,55.95),DARK,[(16,14)]),
    (*xy(2.35,48.86),GREEN,[(-21,17),(-7,17),(7,17),(21,17)])]:
    for dx,dy in offsets:
        d.ellipse((cx+dx-4,cy+dy-4,cx+dx+4,cy+dy+4),fill=color,outline=WHITE,width=1)

# Clip every map layer to its panel; keep adjoining-country context inside the frame.
_clip=Image.new('L',(W,H),0)
ImageDraw.Draw(_clip).rectangle((mx,my,mx+mw,my+mh),fill=255)
im=Image.composite(im,_map_base,_clip);d=ImageDraw.Draw(im)

# Right-hand P&L rail
rx,ry,rw,rh=1010,165,545,615
rect((rx,ry,rx+rw,ry+rh),'#FFFFFF','#D2D7D7',1)
txt(rx+24,ry+20,'UBS INCIDENT  /  LONDON ETF DESK',10,UBS_RED,True)
txt(rx+24,ry+43,'≈ −USD 2.3bn',25,UBS_RED,True)
txt(rx+24,ry+78,'Unauthorized-trading loss · disclosed September 2011 [1]',9,MUTED)
line(rx+20,ry+106,rx+rw-20,ry+106,RULE,1)
txt(rx+24,ry+119,'PEER FY2011 GROUP NET INCOME',10,INK,True)
txt(rx+rw-24,ry+120,'AS REPORTED',8,MUTED,True,anchor='ra')

# Each row carries its own reporting currency; no FX conversion or cross-currency bubble sizing.
def row(y,bank,metric,color,loc='',source=''):
    if loc:txt(rx+24,y+3,loc.upper(),7,MUTED,True)
    txt(rx+24,y+14,bank,11,INK,True)
    if source:txt(rx+24+len(bank)*7.1,y+16,source,7,MUTED,True)
    txt(rx+rw-24,y+12,metric,11,color,True,anchor='ra')
    line(rx+24,y+36,rx+rw-24,y+36,'#E5E8E7',1)

# UK peers
textx=rx+24;txt(textx,ry+145,'UNITED KINGDOM',9,'#66746F',True)
row(ry+165,'HSBC','+USD 16.797bn',GREEN,'London','[2]')
row(ry+207,'Barclays','+GBP 3.007bn',GREEN,'London','[3]')
row(ry+249,'Lloyds','−GBP 2.787bn',DARK,'London','[4]')
row(ry+291,'RBS','−GBP 1.997bn',DARK,'Edinburgh','[5]')
# France peers
line(rx+20,ry+343,rx+rw-20,ry+343,RULE,1)
txt(textx,ry+355,'FRANCE',9,'#66746F',True)
row(ry+375,'BNP Paribas','+EUR 6.050bn',GREEN,'Paris','[6]')
row(ry+417,'Société Générale','+EUR 2.385bn',GREEN,'Paris','[7]')
row(ry+459,'Crédit Agricole Group','+EUR 0.812bn',GREEN,'Paris','[8]')
row(ry+501,'Natixis','+EUR 1.562bn',GREEN,'Paris','[9]')

# Legend and data caveat
line(rx+20,ry+551,rx+rw-20,ry+551,RULE,1)
for i,(lab,col) in enumerate([('positive peer result',GREEN),('negative peer result',DARK),('UBS incident loss',UBS_RED)]):
    xx=rx+24+i*167
    d.ellipse((xx,ry+565,xx+10,ry+575),fill=col)
    txt(xx+16,ry+562,lab,7,MUTED)

# Summary: ensure loss and annual results are not conflated.
line(42,800,1558,800,RULE,1)
txt(50,816,'READING THE MAP',9,UBS_RED,True)
txt(50,836,'UBS is a one-off trading loss; peer figures are full-year consolidated net income. They are different measures, shown separately.',10,INK,True)
txt(50,858,'Values remain in each bank’s reported currency. Map shows UK/France hubs; UBS marker is the London ETF desk.',8,MUTED)
txt(1548,858,'Sources and definitions: documents/ubs-uk-france-bank-map-sources.md',8,MUTED,False,anchor='ra')

im.save(OUT)
print(OUT)
