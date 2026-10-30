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

def text(draw, xy, value, size, color=INK, bold=False, anchor=None, serif=False):
    draw.text(xy, value, font=font(size, bold, serif), fill=color, anchor=anchor)

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

def paste_logo(canvas, logo, center, max_size):
    mark = fit(logo, *max_size)
    canvas.alpha_composite(mark, (round(center[0] - mark.width / 2), round(center[1] - mark.height / 2)))
    return mark.size

im = Image.new('RGBA', (W, H), PAPER)
d = ImageDraw.Draw(im)

# Compact title area, leaving the map as the main visual.
text(d, (42, 22), 'MAJOR EUROPEAN TRADING LOSS EVENTS', 24, INK, bold=True)
text(d, (43, 56), 'Selected benchmark trading-loss events relevant to the UBS 2011 case', 13, MUTED)
d.line((42, 88, 1558, 88), fill=GRID, width=1)

# Light-grey Europe base, with unobtrusive national borders.
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

# Ten bank identities, each used once and assigned to the requested city.
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
}

# Small square markers and clean logo plaques echo a football map, without circular pins.
def city_logo(key, city, lon, lat, color, offset, box_size=(116, 48), logo_size=(96, 30), halo=False, lloyds=False):
    global d
    x0, y0 = xy(lon, lat)
    cx, cy = x0 + offset[0], y0 + offset[1]
    w, h = box_size
    outline = '#E00000' if halo else color
    width = 3 if halo else 1
    d.rectangle((cx - w/2, cy - h/2, cx + w/2, cy + h/2), fill=PAPER, outline=outline, width=width)
    d.rectangle((cx - w/2, cy - h/2, cx - w/2 + 5, cy + h/2), fill=color)
    if lloyds:
        paste_logo(im, logos[key], (cx - 22, cy - 1), (34, 34))
        d = ImageDraw.Draw(im)
        text(d, (cx + 19, cy), 'LLOYDS', 10, color, bold=True, anchor='mm')
    else:
        paste_logo(im, logos[key], (cx + 2, cy), logo_size)
    d = ImageDraw.Draw(im)
    text(d, (cx, cy + h/2 + 5), city.upper(), 8, MUTED, bold=True, anchor='ma')
    return (cx, cy, w, h)

# United Kingdom. City placements are deliberately staggered for clear spacing.
city_logo('NATWEST', 'Edinburgh', -3.1883, 55.9533, '#5E2750', (-5, 3), (108, 46), (88, 25))
city_logo('BARCLAYS', 'Manchester', -2.2426, 53.4808, '#00AEEF', (-42, -17), (108, 46), (68, 32))
city_logo('LLOYDS', 'Birmingham', -1.8904, 52.4862, '#00843D', (-45, 30), (108, 46), lloyds=True)
city_logo('HSBC', 'London', -0.1276, 51.5072, '#DB0011', (42, -58), (112, 48), (88, 27))

# France. Société Générale and Crédit Agricole are emphasized by their marker colours.
city_logo('BNP', 'Lille', 3.0573, 50.6292, '#00965E', (23, -34), (108, 48), (78, 36))
city_logo('SG', 'Paris', 2.3522, 48.8566, '#E30613', (58, -22), (118, 50), (94, 34))
city_logo('CA', 'Lyon', 4.8357, 45.7640, '#006B54', (-5, -43), (120, 48), (98, 28))
city_logo('NATIXIS', 'Marseille', 5.3698, 43.2965, '#003A70', (28, -34), (120, 48), (98, 27))

# Switzerland. UBS receives the largest red halo; Credit Suisse remains a single Geneva logo.
city_logo('CS', 'Geneva', 6.1432, 46.2044, '#005EB8', (-2, -102), (108, 46), (88, 25))
city_logo('UBS', 'Zurich', 8.5417, 47.3769, '#E00000', (36, -50), (142, 60), (106, 39), halo=True)

# Only the three major incident figures are shown. Text labels, not extra bank logos.
def event_label(x, y, width, label, amount, color, amount_size=19, border=1):
    height = 49 if amount_size < 22 else 57
    d.rectangle((x, y, x + width, y + height), fill=PAPER, outline=color, width=border)
    d.rectangle((x, y, x + 5, y + height), fill=color)
    text(d, (x + 12, y + 6), label, 9, color, bold=True)
    text(d, (x + 12, y + 22), amount, amount_size, INK, bold=True)

# London: event tag sits below/right of the HSBC city logo; Barings itself has no second logo.
event_label(535, 410, 130, 'BARINGS · 1995', 'USD -1.4bn', '#D4A017', 17)
# Paris: the Kerviel event has the second-largest visual callout.
event_label(590, 536, 166, 'KERVIEL · 2008', 'EUR -4.9bn', '#C1272D', 21, 2)
# Zurich: largest incident highlight, beside UBS's red-halo logo.
event_label(1164, 526, 178, 'ADOBOLI · 2011', 'USD -2.3bn', '#E00000', 23, 3)

# Minimal footer; the requested takeaway is retained in small type.
d.line((42, 806, 1558, 806), fill=GRID, width=1)
text(d, (45, 816), "UBS's USD 2.3bn trading loss ranks among the most significant banking trading-loss events in Europe and illustrates how control failures can rapidly escalate into material financial and liquidity-management consequences.", 8, INK, bold=True)
text(d, (45, 841), 'Source notes: FINMA · Credit Suisse Special Committee · U.S. Senate PSI · Société Générale · RBA / BoE inquiry. Bank city positions follow the supplied brief; UBS Adoboli desk was London.', 7, MUTED)

im.convert('RGB').save(OUT)
print(OUT)
