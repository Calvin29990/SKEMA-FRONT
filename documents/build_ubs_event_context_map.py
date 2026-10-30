from pathlib import Path
import json
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / 'assets'
OUT = ROOT / 'ubs-event-context-map.png'
W, H = 1600, 900
PAPER = '#FFFFFF'
LAND = '#E9EBEA'
BORDER = '#FFFFFF'
INK = '#183448'
MUTED = '#66747D'
GRID = '#D9DEDF'

FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
SERIF_BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
_fonts = {}

def font(size, bold=False, serif=False):
    key = (size, bold, serif)
    if key not in _fonts:
        path = SERIF_BOLD if serif else (BOLD if bold else FONT)
        _fonts[key] = ImageFont.truetype(path, size)
    return _fonts[key]

def text(draw, xy, value, size, color=INK, bold=False, anchor=None, serif=False,
         stroke_width=0, stroke_fill=PAPER):
    draw.text(xy, value, font=font(size, bold, serif), fill=color, anchor=anchor,
              stroke_width=stroke_width, stroke_fill=stroke_fill)

def load_logo(filename, remove_light_bg=False):
    image = Image.open(ASSETS / filename).convert('RGBA')
    if remove_light_bg:
        px = image.load()
        for y in range(image.height):
            for x in range(image.width):
                r, g, b, a = px[x, y]
                if min(r, g, b) > 238 and max(r, g, b) - min(r, g, b) < 24:
                    px[x, y] = (r, g, b, 0)
    bbox = image.getchannel('A').point(lambda a: 255 if a > 10 else 0).getbbox()
    return image.crop(bbox) if bbox else image

def fit(image, max_width, max_height):
    scale = min(max_width / image.width, max_height / image.height)
    return image.resize((max(1, round(image.width * scale)), max(1, round(image.height * scale))), Image.Resampling.LANCZOS)

def paste_logo_floating(canvas, logo, center, max_size):
    """Place the logo directly on the map, with no badge, circle or keyline."""
    mark = fit(logo, *max_size)
    x = round(center[0] - mark.width / 2)
    y = round(center[1] - mark.height / 2)
    canvas.alpha_composite(mark, (x, y))
    return mark.size

im = Image.new('RGBA', (W, H), PAPER)
d = ImageDraw.Draw(im)

# Compact title area; the European map and city marks remain dominant.
text(d, (42, 22), 'MAJOR EUROPEAN TRADING LOSS EVENTS', 24, INK, bold=True)
text(d, (43, 56), 'Selected benchmark trading-loss events relevant to the UBS 2011 case', 13, MUTED)
d.line((42, 88, 1558, 88), fill=GRID, width=1)

# Light-grey Europe base, with discreet national borders.
mx, my, mw, mh = 35, 105, 1530, 680
lon0, lon1 = -12.0, 20.0
lat0, lat1 = 42.0, 58.0

def xy(lon, lat):
    return (mx + (lon - lon0) / (lon1 - lon0) * mw,
            my + (lat1 - lat) / (lat1 - lat0) * mh)

geo_path = ASSETS / 'natural-earth-50m-western-europe-context.geojson'
with geo_path.open(encoding='utf-8') as handle:
    geo = json.load(handle)

def draw_geometry(geometry):
    polygons = geometry['coordinates'] if geometry['type'] == 'MultiPolygon' else [geometry['coordinates']]
    for polygon in polygons:
        ring = polygon[0]
        xs = [p[0] for p in ring]
        ys = [p[1] for p in ring]
        if max(xs) < lon0 or min(xs) > lon1 or max(ys) < lat0 or min(ys) > lat1:
            continue
        points = [xy(lon, lat) for lon, lat in ring]
        d.polygon(points, fill=LAND)
        d.line(points + [points[0]], fill=BORDER, width=2, joint='curve')

for feature in geo['features']:
    draw_geometry(feature['geometry'])

# Bank logos, one per requested city (12 total).
logos = {
    'HSBC': load_logo('hsbc-logo.png', True),
    'BARCLAYS': load_logo('barclays-logo.jpg', True),
    'LLOYDS': load_logo('lloyds-bank-logo.png'),
    'NATWEST': load_logo('natwest-logo.png', True),
    'SG': load_logo('societe-generale-logo.png'),
    'BNP': load_logo('bnp-paribas-logo.png', True),
    'CA': load_logo('credit-agricole-cib-logo.png'),
    'NATIXIS': load_logo('natixis-logo.png'),
    'UBS': load_logo('ubs-logo.png', True),
    'CS': load_logo('credit-suisse-logo.png'),
    'JULIUS': load_logo('julius-baer-logo.png'),
    'PICTET': load_logo('pictet-logo.png'),
}

# Logos float directly on the map; city names sit beneath them in bank colours.
def city_mark(key, city, center, color, logo_size=(78, 28), city_y=None,
              lloyds=False, city_font_size=11, city_color=None):
    global d
    if lloyds:
        paste_logo_floating(im, logos[key], (center[0] - 20, center[1] - 1), (34, 31))
        d = ImageDraw.Draw(im)
        text(d, (center[0] + 19, center[1]), 'LLOYDS', 10, color, bold=True,
             anchor='mm', stroke_width=1)
    else:
        paste_logo_floating(im, logos[key], center, logo_size)
    d = ImageDraw.Draw(im)
    label_y = city_y if city_y is not None else center[1] + logo_size[1] // 2 + 13
    text(d, (center[0], label_y), city.upper(), city_font_size,
         city_color or color, bold=True, anchor='mm', stroke_width=2)

# UK — coloured city labels sit directly beneath the transparent bank marks.
city_mark('NATWEST', 'Edinburgh', (458, 192), '#5E2750', (80, 24), 231)
city_mark('BARCLAYS', 'Manchester', (490, 282), '#00AEEF', (68, 31), 323)
city_mark('LLOYDS', 'Birmingham', (520, 365), '#00843D', (78, 30), 407, lloyds=True)
city_mark('HSBC', 'London', (605, 330), '#DB0011', (82, 25), 372)

# France — no logo circles; the city names remain clearly associated below each logo.
city_mark('BNP', 'Lille', (780, 340), '#00965E', (74, 34), 373)
city_mark('SG', 'Paris', (725, 490), '#E30613', (91, 32), 525)
city_mark('CA', 'Lyon', (840, 615), '#006B54', (88, 24), 657)
city_mark('NATIXIS', 'Marseille', (873, 710), '#003A70', (130, 38), 752,
          city_font_size=14, city_color='#6F2DA8')

# Switzerland — the four bank wordmarks are shown directly on the map.
city_mark('CS', 'Geneva', (900, 560), '#005EB8', (88, 25), 602)
city_mark('JULIUS', 'Basel', (970, 435), '#B89D4F', (84, 25), 477)
city_mark('UBS', 'Zurich', (1080, 500), '#E00000', (108, 40), 541)
city_mark('PICTET', 'Lugano', (1050, 640), '#006A52', (88, 25), 682)

# Event highlights use floating type only, without circles or containers.
def event_text(x, y, label, amount, color, label_size, amount_size):
    global d
    d = ImageDraw.Draw(im)
    text(d, (x, y), label, label_size, color, bold=True, stroke_width=3)
    text(d, (x, y + label_size + 5), amount, amount_size, color, bold=True, stroke_width=3)

# Barings 1995 — third in the visual hierarchy, with gold event type near London.
event_text(680, 385, 'BARINGS · 1995', 'USD -1.4bn', '#9A7000', 16, 30)
# Kerviel 2008 — second-largest red event emphasis beside the Paris / SG marker.
event_text(550, 560, 'KERVIEL · 2008', 'EUR -4.9bn', '#C1272D', 18, 38)
# Adoboli 2011 — largest callout, with the requested UBS-red accent by Zurich.
event_text(1170, 472, 'ADOBOLI · 2011', 'USD -2.3bn', '#E00000', 19, 42)

# Minimal footnote retains the factual distinction between Zurich HQ and the London desk.
d.line((42, 806, 1558, 806), fill=GRID, width=1)
text(d, (45, 815), "UBS's USD 2.3bn trading loss ranks among the most significant banking trading-loss events in Europe and illustrates how control failures can rapidly escalate into material financial and liquidity-management consequences.", 10, INK, bold=True)
text(d, (45, 841), "Source notes: FINMA · Société Générale · RBA / BoE inquiry. Adoboli's desk was London; Zurich is UBS group HQ. Barings is shown at its London home; Leeson's operation was Singapore.", 8, MUTED)

im.convert('RGB').save(OUT)
print(OUT)
