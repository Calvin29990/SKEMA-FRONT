from pathlib import Path
from PIL import Image
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
OUT = ROOT / "ubs-treasury-risk-presentation-8-slides.pptx"
MAP_SLIDE = ASSETS / "approved-map-slide-report-order.png"
NORMAL_HIDDEN_SLIDE = ASSETS / "approved-three-panel-slide.png"
DALTONS = ASSETS / "daltons-illustration.png"
UBS_LOGO = ASSETS / "ubs-logo-slide.png"
SKEMA_LOGO = ASSETS / "skema-logo.png"

SW, SH = 13.333333, 7.5
BG = "F7F7F3"
PANEL = "101315"
PANEL2 = "191E21"
NAVY = "18232B"
WHITE = "F7F8F6"
MUTED = "737B80"
SOFT = "A9B0B2"
RED = "C82036"
TEAL = "00A985"
GOLD = "D6A600"
BLUE = "2E91C1"
GREEN = "42A878"
BORDER = "CFD3D0"
GRID = "343B3E"


def C(hex_color):
    return RGBColor.from_string(hex_color)


def rect(slide, x, y, w, h, fill, line_color=None, line_width=0.8,
         shape=MSO_SHAPE.RECTANGLE):
    sh = slide.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    sh.fill.solid()
    sh.fill.fore_color.rgb = C(fill)
    if line_color:
        sh.line.color.rgb = C(line_color)
        sh.line.width = Pt(line_width)
    else:
        sh.line.fill.background()
    return sh


def line(slide, x1, y1, x2, y2, color=BORDER, width=1.0):
    sh = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT,
                                    Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    sh.line.color.rgb = C(color)
    sh.line.width = Pt(width)
    return sh


def txt(slide, value, x, y, w, h, size=12, color=NAVY, bold=False,
        align=PP_ALIGN.LEFT, valign=MSO_ANCHOR.MIDDLE, margin=0.02):
    sh = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = sh.text_frame
    tf.clear()
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(margin)
    tf.margin_top = tf.margin_bottom = Inches(margin)
    tf.vertical_anchor = valign
    p = tf.paragraphs[0]
    p.alignment = align
    p.space_before = Pt(0)
    p.space_after = Pt(0)
    r = p.add_run()
    r.text = value
    r.font.name = "Arial"
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.color.rgb = C(color)
    return sh


def add_img_fit(slide, path, x, y, w, h):
    """Fit the entire image into a box while preserving its exact aspect ratio."""
    with Image.open(path) as im:
        iw, ih = im.size
    aspect = iw / ih
    box_aspect = w / h
    if aspect > box_aspect:
        dw, dh = w, w / aspect
        dx, dy = x, y + (h-dh)/2
    else:
        dh, dw = h, h*aspect
        dx, dy = x + (w-dw)/2, y
    return slide.shapes.add_picture(str(path), Inches(dx), Inches(dy),
                                    width=Inches(dw), height=Inches(dh))


def add_header(slide, title, kicker, page, section):
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = C(BG)
    slide.shapes.add_picture(str(UBS_LOGO), Inches(0.42), Inches(0.13),
                             width=Inches(1.38), height=Inches(0.49))
    txt(slide, title, 2.02, 0.15, 9.65, 0.31, 17, NAVY, True)
    txt(slide, kicker, 2.02, 0.47, 9.65, 0.20, 9.3, RED, True)
    txt(slide, section, 2.02, 0.71, 9.65, 0.16, 7.4, MUTED)
    slide.shapes.add_picture(str(SKEMA_LOGO), Inches(12.35), Inches(0.12),
                             width=Inches(0.52), height=Inches(0.55))
    rect(slide, 0.42, 0.97, 12.48, 0.012, BORDER)
    rect(slide, 0.42, 7.17, 12.48, 0.010, BORDER)
    txt(slide, f"UBS  ×  SKEMA   /   {page:02d}", 11.40, 7.22, 1.45, 0.12,
        6.4, MUTED, True, align=PP_ALIGN.RIGHT)


def add_user_slide(prs, image):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = C(BG)
    add_img_fit(slide, image, 0, 0, SW, SH)
    return slide


def make_deck():
    prs = Presentation()
    prs.slide_width = Inches(SW)
    prs.slide_height = Inches(SH)
    blank = prs.slide_layouts[6]

    # 1 — European context. Exact user-approved slide, no overlays or edits.
    add_user_slide(prs, MAP_SLIDE)

    # 2 — Concealment mechanism. Exact user-approved slide, no overlays or edits.
    add_user_slide(prs, NORMAL_HIDDEN_SLIDE)

    # 3 — Causal bridge from failed controls to Treasury funding.
    s = prs.slides.add_slide(blank)
    add_header(s, "FROM CONTROL FAILURE TO TREASURY IMPACT",
               "SECTION 1.3  ·  FAILED CONTROLS & CASH TRANSMISSION", 3,
               "THE BRIDGE: HIDDEN POSITIONS → CASH IMPACT → LIQUIDITY PRESSURE")
    txt(s, "CENTRAL TREASURY QUESTION", 0.62, 1.28, 3.10, 0.22, 8.5, TEAL, True)
    txt(s, "How can UBS preserve liquidity and meet payments over the next three months?",
        3.48, 1.25, 9.12, 0.27, 10.4, NAVY, True)

    nodes = [
        ("CONTROL\nFAILURES", "Verification gaps", RED),
        ("HIDDEN\nPOSITIONS", "False offsets", GOLD),
        ("TRADING\nLOSSES", "USD 2.3bn", RED),
        ("SETTLEMENT\nOBLIGATIONS", "Dated cash due", BLUE),
        ("COLLATERAL\nCALLS", "Calls / delayed returns", GOLD),
        ("LIQUIDITY\nPRESSURE", "Buffer erosion", RED),
        ("FUNDING\nREQUIREMENT", "Timing gap", TEAL),
    ]
    x0, w, gap, y, h = 0.57, 1.48, 0.26, 2.12, 2.04
    for i, (title, sub, accent) in enumerate(nodes):
        x = x0 + i*(w+gap)
        rect(s, x, y, w, h, PANEL, PANEL)
        rect(s, x, y, w, 0.06, accent)
        rect(s, x+0.52, y+0.25, 0.50, 0.50, accent, shape=MSO_SHAPE.OVAL)
        txt(s, f"{i+1:02d}", x+0.52, y+0.37, 0.50, 0.20, 9, WHITE, True,
            align=PP_ALIGN.CENTER)
        txt(s, title, x+0.12, y+0.88, w-0.24, 0.48, 9.0, WHITE, True,
            align=PP_ALIGN.CENTER)
        txt(s, sub, x+0.10, y+1.52, w-0.20, 0.25, 7.2, SOFT,
            align=PP_ALIGN.CENTER)
        if i < len(nodes)-1:
            rect(s, x+w+0.06, y+0.93, gap-0.10, 0.22,
                 [GOLD, RED, BLUE, GOLD, RED, TEAL][i], shape=MSO_SHAPE.CHEVRON)

    # Process bar makes the report sequence explicit.
    rect(s, 0.62, 4.72, 12.05, 0.78, "E8ECE8", None)
    phases = [
        (0.82, 2.52, "OPERATIONAL EVENT", "control failure"),
        (4.30, 2.52, "CASH TRANSMISSION", "settlement + collateral"),
        (8.02, 2.52, "TREASURY RESPONSE", "forecast + funding"),
    ]
    for i, (x, ww, title, sub) in enumerate(phases):
        txt(s, title, x, 4.84, ww, 0.18, 7.7, [RED, BLUE, TEAL][i], True,
            align=PP_ALIGN.CENTER)
        txt(s, sub, x, 5.11, ww, 0.19, 8.1, NAVY, True, align=PP_ALIGN.CENTER)
    txt(s, "A headline trading loss is not itself the day-one cash need; the Treasury problem is the timing and location of obligations.",
        0.66, 6.02, 12.0, 0.40, 10.0, NAVY, True, align=PP_ALIGN.CENTER)
    txt(s, "Sources: FINMA 2012 §§23–41; FSA 2012 §§26–42. Potential channels are not asserted historical cash movements.",
        0.66, 6.68, 12.0, 0.19, 7.0, MUTED)

    # 4 — Incident timeline with requested Dalton illustration, not a trader portrait.
    s = prs.slides.add_slide(blank)
    add_header(s, "INCIDENT TIMELINE",
               "SECTION 1.2  ·  DISCOVERY, CONTAINMENT & FOLLOW-THROUGH", 4,
               "FOUR PHASES FROM 14 SEPTEMBER 2011")
    line(s, 0.78, 2.14, 9.32, 2.14, BORDER, 3)
    events = [
        (0.62, RED, "14 SEP 2011", "Discovery", "Unauthorised futures positions identified."),
        (2.84, GOLD, "15 SEP 2011", "Public announcement", "Initial loss estimate communicated."),
        (5.06, BLUE, "FOLLOWING DAYS", "Containment & hedging", "Positions managed; exposure reviewed."),
        (7.28, TEAL, "FOLLOWING WEEKS", "Investigation & remediation", "Control failures examined."),
    ]
    for x, accent, date, title, desc in events:
        center=x+0.95
        rect(s, center-0.13, 2.01, 0.26, 0.26, accent, shape=MSO_SHAPE.OVAL)
        rect(s, x, 2.50, 1.92, 1.57, PANEL, PANEL)
        rect(s, x, 2.50, 1.92, 0.05, accent)
        txt(s, date, x+0.12, 2.71, 1.68, 0.20, 7.8, accent, True)
        txt(s, title, x+0.12, 3.00, 1.68, 0.33, 9.0, WHITE, True)
        txt(s, desc, x+0.12, 3.43, 1.68, 0.48, 7.4, SOFT, valign=MSO_ANCHOR.TOP)
    # Dalton illustration, fit without distortion.
    rect(s, 9.72, 1.55, 3.12, 2.12, WHITE, BORDER)
    add_img_fit(s, DALTONS, 9.82, 1.63, 2.92, 1.64)
    txt(s, "ILLUSTRATIVE CARTOON", 9.84, 3.34, 2.87, 0.17,
        7.0, MUTED, True, align=PP_ALIGN.RIGHT)
    rect(s, 9.72, 4.02, 3.12, 0.91, PANEL, PANEL)
    txt(s, "UBS INVESTMENT BANK · LONDON ETF DESK", 9.91, 4.19, 2.72, 0.32,
        8.1, WHITE, True, align=PP_ALIGN.CENTER)
    txt(s, "Public announcement and subsequent response are distinct milestones.",
        0.66, 5.43, 8.75, 0.35, 9.0, NAVY, True)
    txt(s, "Dates and descriptions follow the incident chronology in FINMA, FSA and UBS disclosures.",
        0.66, 6.04, 8.75, 0.22, 7.3, MUTED)

    # 5 — Bloomberg-style model cash bridge.
    s = prs.slides.add_slide(blank)
    add_header(s, "TREASURY LIQUIDITY EVOLUTION",
               "SECTION 2.2  ·  CASH BRIDGE", 5,
               "ILLUSTRATIVE SCENARIO PATHS · USDm · NOT UBS ACTUAL CASH")
    # Dark Bloomberg-like plotting area.
    px, py, pw, ph = 0.62, 1.40, 9.70, 5.45
    rect(s, px, py, pw, ph, PANEL, PANEL)
    txt(s, "CASH POSITION  /  USD MILLIONS", px+0.20, py+0.16, 4.4, 0.20,
        8.2, WHITE, True)
    # Chart domain and grid
    left, right, top, bottom = px+0.72, px+9.40, py+0.75, py+4.70
    vmin, vmax = 500, 1200
    def ymap(v): return bottom - (v-vmin)/(vmax-vmin)*(bottom-top)
    for v in range(500, 1201, 100):
        yy=ymap(v)
        line(s, left, yy, right, yy, GOLD if v==700 else GRID,
             1.5 if v==700 else 0.55)
        txt(s, str(v), px+0.10, yy-0.09, 0.48, 0.17, 6.9,
            GOLD if v==700 else SOFT, v==700, align=PP_ALIGN.RIGHT)
    txt(s, "BUFFER 700", right-1.03, ymap(700)-0.23, 0.98, 0.17,
        6.8, GOLD, True, align=PP_ALIGN.RIGHT)
    labels=["14 Sep","15","16","17","18","19","20","30 Sep","Oct","Nov","14 Dec"]
    n=len(labels)
    xs=[left+i*(right-left)/(n-1) for i in range(n)]
    for i,lab in enumerate(labels):
        txt(s, lab, xs[i]-0.31, bottom+0.10, 0.62, 0.18, 6.3, SOFT,
            align=PP_ALIGN.CENTER)
    series=[
        ("NO INCIDENT", [1000,990,985,990,985,987,984,1004,1104,1054,1024], TEAL),
        ("INCIDENT BASE", [1000,915,805,775,765,772,774,769,909,849,824], BLUE),
        ("COMBINED STRESS", [1000,915,805,775,765,772,774,769,909,549,524], RED),
    ]
    for name,vals,color in series:
        pts=[(xs[i],ymap(v)) for i,v in enumerate(vals)]
        for (x1,y1),(x2,y2) in zip(pts,pts[1:]): line(s,x1,y1,x2,y2,color,2.0)
        for x,ypt in pts:
            rect(s,x-0.045,ypt-0.045,0.09,0.09,color,shape=MSO_SHAPE.OVAL)
    # Legend
    lx=px+0.80
    for name, _, color in series:
        line(s,lx,py+5.14,lx+0.28,py+5.14,color,2.2)
        txt(s,name,lx+0.34,py+5.04,1.45,0.20,6.8,WHITE,True)
        lx+=2.32
    # Funding-gap annotation on final stress point.
    xlast=xs[-1]
    line(s,xlast+0.12,ymap(524),xlast+0.12,ymap(700),RED,1.7)
    txt(s,"$176m\npeak gap",xlast-0.63,ymap(524)-0.55,0.70,0.44,7.0,RED,True,
        align=PP_ALIGN.CENTER)

    # Right-hand facts panel
    rect(s, 10.55, 1.40, 2.30, 5.45, PANEL2, GRID)
    rect(s, 10.55, 1.40, 2.30, 0.05, TEAL)
    txt(s,"MODEL INPUTS",10.74,1.63,1.92,0.22,8.8,WHITE,True)
    for i,(value,label,color) in enumerate([
        ("$1,000m","opening cash*",TEAL),
        ("$700m","minimum buffer*",GOLD),
        ("$765m","incident-base low",BLUE),
    ]):
        yy=2.14+i*0.83
        txt(s,value,10.74,yy,1.88,0.30,14,color,True)
        txt(s,label,10.74,yy+0.32,1.88,0.20,7.3,SOFT)
        if i<2: line(s,10.74,yy+0.66,12.64,yy+0.66,GRID,0.7)
    line(s,10.74,4.72,12.64,4.72,GRID,0.7)
    txt(s,"STRESS",10.74,4.92,1.88,0.18,7.7,RED,True)
    txt(s,"$549m on 30 Nov\n$524m on 14 Dec",10.74,5.17,1.88,0.53,8.5,WHITE,True)
    txt(s,"*Assumptions; replace with UBS Treasury ledger.",10.74,6.16,1.88,0.42,6.8,SOFT)
    txt(s,"Base case stays above buffer; stress falls below it. Funding need is measured against the assumed $700m buffer.",
        0.66,6.93,12.0,0.15,6.8,MUTED)

    # 6 — Stress scenarios and delayed funding source.
    s = prs.slides.add_slide(blank)
    add_header(s, "STRESS TESTS: RED & AMBER CASH SHOCKS",
               "SECTION 2.3  ·  COMBINED SENSITIVITY", 6,
               "SCENARIOS ARE ILLUSTRATIVE · USDm · NOT HISTORICAL UBS OUTCOMES")
    txt(s,"COMBINED STRESS INPUTS",0.64,1.29,4.0,0.22,8.8,MUTED,True)
    shocks=[
        (0.66,RED,"−100","Additional withdrawals"),
        (3.12,GOLD,"−100","Collateral return delayed"),
        (5.58,RED,"−50","Settlement accelerated"),
        (8.04,GOLD,"−50","Funding rollover fails"),
    ]
    for x,color,value,label in shocks:
        rect(s,x,1.67,2.18,1.08,PANEL,PANEL)
        rect(s,x,1.67,2.18,0.05,color)
        txt(s,value,x+0.16,1.91,0.80,0.35,18,color,True)
        txt(s,label,x+0.94,1.89,1.08,0.48,8.4,WHITE,True)
    # Simple waterfall of the combined hit, 849 -> 549.
    rect(s,10.50,1.67,2.24,1.08,"F4E9D0",None)
    txt(s,"−$300m",10.68,1.88,1.88,0.33,16,RED,True,align=PP_ALIGN.CENTER)
    txt(s,"combined cash shock",10.68,2.25,1.88,0.20,7.6,NAVY,True,align=PP_ALIGN.CENTER)
    # Bridge / outcome visualization
    rect(s,0.66,3.17,7.85,2.55,PANEL,PANEL)
    txt(s,"NOVEMBER CASH BRIDGE",0.88,3.35,4.0,0.21,8.5,WHITE,True)
    bx0, bybase, charttop=1.12,5.28,3.95
    lo,hi=450,900
    def yb(v): return bybase-(v-lo)/(hi-lo)*(bybase-charttop)
    for v in (500,600,700,800,900):
        yy=yb(v)
        line(s,bx0,yy,8.22,yy,GOLD if v==700 else GRID,1.25 if v==700 else 0.55)
        if v==700: txt(s,"BUFFER $700m",6.94,yy-0.22,1.18,0.17,6.8,GOLD,True,align=PP_ALIGN.RIGHT)
    points=[(1.55,849,"BASE\n$849m",TEAL),(3.04,799,"SETTLEMENT\n−$50m",RED),
            (4.48,699,"COLLATERAL\n−$100m",GOLD),(5.92,599,"WITHDRAWALS\n−$100m",RED),
            (7.30,549,"ROLLOVER\n−$50m",GOLD)]
    for i,(x,val,label,color) in enumerate(points):
        if i==0: top=yb(val); height=bybase-top
        else:
            prev=points[i-1][1]
            top=yb(prev); height=yb(val)-yb(prev)
        rect(s,x,top,0.70,max(0.08,height),color)
        txt(s,label,x-0.26,bybase+0.12,1.25,0.36,6.7,WHITE,True,align=PP_ALIGN.CENTER)
        if i<len(points)-1:
            nextx=points[i+1][0]
            line(s,x+0.71,yb(val),nextx,yb(val),SOFT,0.65)
    # Delayed liquidity source timeline and result
    rect(s,8.78,3.17,4.06,2.55,WHITE,BORDER)
    txt(s,"LIQUIDITY SOURCE TIMING",9.02,3.38,3.58,0.22,9.0,NAVY,True)
    txt(s,"Assumed $200m T+2 line",9.02,3.74,3.58,0.22,8.2,MUTED)
    line(s,9.35,4.52,12.34,4.52,TEAL,2.5)
    for x,date,caption,color in [(9.42,"25 NOV","Trigger",GOLD),(10.87,"29 NOV","Arrives",TEAL),(12.20,"30 NOV","First breach",RED)]:
        rect(s,x-0.09,4.43,0.18,0.18,color,shape=MSO_SHAPE.OVAL)
        txt(s,date,x-0.40,4.74,0.80,0.18,7.2,NAVY,True,align=PP_ALIGN.CENTER)
        txt(s,caption,x-0.44,4.97,0.90,0.24,6.8,MUTED,align=PP_ALIGN.CENTER)
    txt(s,"If source arrives late: $549m cash on 30 Nov, $151m below buffer; peak need $176m by 14 Dec.",
        0.68,6.09,12.0,0.36,9.0,NAVY,True)
    txt(s,"Facility availability and timing are assumptions. Test delayed liquidity arrival separately; do not count an unconfirmed source as cash.",
        0.68,6.61,12.0,0.25,7.1,MUTED)

    # 7 — Risk matrix, all categories from report
    s = prs.slides.add_slide(blank)
    add_header(s, "RISK MATRIX: LIKELIHOOD × IMPACT",
               "SECTION 3.1  ·  RESIDUAL EXPOSURE", 7,
               "ILLUSTRATIVE ANALYST SCORES · REASSESS AFTER CONTAINMENT")
    mx,my,cell=1.15,1.80,1.30
    # rows top to bottom: likely, possible, unlikely; columns low, medium, high impact.
    fill_rows=[["F1DCDD","F2D1C5","E8B8BC"],
               ["F1E9CB","EADBAB","E8C7A3"],
               ["E4EEE4","ECEDDB","F1E6D0"]]
    for row in range(3):
        for col in range(3):
            rect(s,mx+col*cell,my+row*cell,cell-0.04,cell-0.04,fill_rows[row][col],WHITE,1)
            score=(3-row)*(col+1)
            txt(s,str(score),mx+col*cell+0.06,my+row*cell+0.04,0.20,0.16,6.8,MUTED)
    for row,label in enumerate(["LIKELY","POSSIBLE","UNLIKELY"]):
        txt(s,label,0.28,my+row*cell+0.47,0.78,0.20,7.0,NAVY,True,align=PP_ALIGN.RIGHT)
    for col,label in enumerate(["LOW","MEDIUM","HIGH"]):
        txt(s,label,mx+col*cell,my+3*cell+0.03,cell-0.04,0.18,7.1,NAVY,True,align=PP_ALIGN.CENTER)
    txt(s,"LIKELIHOOD",0.22,1.49,1.0,0.18,7.0,MUTED,True,align=PP_ALIGN.RIGHT)
    txt(s,"IMPACT",mx+0.86,my+3*cell+0.28,1.48,0.18,7.2,MUTED,True,align=PP_ALIGN.CENTER)
    # Compact colored markers by score cell.
    markers=[
        (2,3,"O",RED), (2,3,"L",BLUE), (2,2,"M",GOLD),
        (2,2,"C",TEAL), (2,3,"F",RED), (1,2,"R",GREEN), (2,2,"G",GOLD),
    ]
    # use cell map: likelihood 3 top, 2 middle, 1 bottom; impact 1..3 left-right
    offsets={ (2,3):[(-0.28,-0.12),(0.0,-0.12),(0.28,-0.12)],
              (2,2):[(-0.27,0.18),(0,0.18),(0.27,0.18)],
              (1,2):[(0,0)] }
    taken={}
    for likelihood,impact,letter,color in markers:
        row=3-likelihood; col=impact-1
        cx=mx+col*cell+0.63; cy=my+row*cell+0.63
        key=(likelihood,impact); idx=taken.get(key,0); taken[key]=idx+1
        dx,dy=offsets[key][idx]
        rect(s,cx+dx-0.13,cy+dy-0.13,0.26,0.26,color,shape=MSO_SHAPE.OVAL)
        txt(s,letter,cx+dx-0.13,cy+dy-0.09,0.26,0.16,7.0,WHITE,True,align=PP_ALIGN.CENTER)
    # Risk legend / priorities
    rect(s,5.62,1.55,7.20,4.98,PANEL,PANEL)
    rect(s,5.62,1.55,7.20,0.05,RED)
    txt(s,"RISK REGISTER",5.87,1.78,3.0,0.22,10,WHITE,True)
    txt(s,"Likelihood × impact = score",9.10,1.80,3.43,0.18,7.8,SOFT,align=PP_ALIGN.RIGHT)
    items=[
        ("O","Operational","2 × 3 = 6",RED),
        ("L","Liquidity","2 × 3 = 6",BLUE),
        ("M","Market","2 × 2 = 4",GOLD),
        ("C","Counterparty","2 × 2 = 4",TEAL),
        ("F","Funding","2 × 3 = 6",RED),
        ("R","Reputational","1 × 2 = 2",GREEN),
        ("G","Legal / regulatory","2 × 2 = 4",GOLD),
    ]
    for i,(code,name,score,color) in enumerate(items):
        col=i//4; row=i%4
        x=5.88+col*3.33; y=2.24+row*0.72
        rect(s,x,y,0.32,0.32,color,shape=MSO_SHAPE.OVAL)
        txt(s,code,x,y+0.05,0.32,0.19,7.8,WHITE,True,align=PP_ALIGN.CENTER)
        txt(s,name,x+0.45,y,1.90,0.22,8.4,WHITE,True)
        txt(s,score,x+2.17,y,0.84,0.22,7.9,color,True,align=PP_ALIGN.RIGHT)
    line(s,5.88,5.28,12.54,5.28,GRID,0.8)
    txt(s,"TOP PRIORITIES",5.88,5.48,1.55,0.19,7.6,TEAL,True)
    txt(s,"O  ·  L  ·  F",7.50,5.43,1.70,0.27,10,WHITE,True)
    txt(s,"Operational control · buffer breach · funding rollover",9.08,5.47,3.39,0.25,7.6,SOFT)
    txt(s,"Scores are analyst assumptions, not UBS / regulator ratings; calibrate against approved Treasury buffer and reconciled positions.",
        0.64,6.78,12.0,0.20,7.0,MUTED)

    # 8 — CFO action plan
    s = prs.slides.add_slide(blank)
    add_header(s, "CFO ACTION PLAN: THREE PILLARS",
               "SECTION 3.2  ·  OWNERS, DEADLINES & BENEFITS", 8,
               "PRESERVE PAYMENT CAPACITY · GATE FUNDING ON EVIDENCE")
    actions=[
        (0.62,TEAL,"01","IMMEDIATE LIQUIDITY\nPROTECTION","Group Treasurer",
         "Initial view: 24h\nDaily to 14 Dec",
         "Verified headroom; staged funding before a modeled breach.",
         "Check facility access, collateral eligibility and T+2 arrival."),
        (4.66,RED,"02","EXPOSURE\nCONTAINMENT","IB COO + Market Risk + Treasury",
         "Start now\nDaily until reconciled",
         "Bound open positions; settle and collateral breaks independently.",
         "Close-out cost and cash release only when confirmed."),
        (8.70,GOLD,"03","GOVERNANCE &\nCONTROLS","CRO + IB COO\nInternal Audit validates",
         "Interim controls now\nProgramme by 14 Dec",
         "Dual verification; timely exception escalation; clear ownership.",
         "Manual dual sign-off until systems are remediated."),
    ]
    for x,color,num,title,owner,deadline,benefit,fallback in actions:
        rect(s,x,1.54,3.76,4.78,PANEL,PANEL)
        rect(s,x,1.54,3.76,0.06,color)
        rect(s,x+0.20,1.83,0.58,0.58,color,shape=MSO_SHAPE.OVAL)
        txt(s,num,x+0.20,1.99,0.58,0.22,10,WHITE,True,align=PP_ALIGN.CENTER)
        txt(s,title,x+0.95,1.81,2.54,0.66,10.6,WHITE,True)
        txt(s,"OWNER",x+0.22,2.77,3.25,0.17,7.1,color,True)
        txt(s,owner,x+0.22,2.99,3.28,0.42,8.5,WHITE,True)
        txt(s,"DEADLINE",x+0.22,3.56,3.25,0.17,7.1,color,True)
        txt(s,deadline,x+0.22,3.78,3.28,0.40,8.0,SOFT,True)
        line(s,x+0.22,4.32,x+3.52,4.32,GRID,0.8)
        txt(s,"EXPECTED BENEFIT",x+0.22,4.48,3.25,0.17,7.1,color,True)
        txt(s,benefit,x+0.22,4.70,3.28,0.63,8.2,WHITE,True,valign=MSO_ANCHOR.TOP)
        txt(s,"CONSTRAINT / FALLBACK",x+0.22,5.47,3.25,0.17,7.0,SOFT,True)
        txt(s,fallback,x+0.22,5.68,3.28,0.45,7.3,SOFT,valign=MSO_ANCHOR.TOP)
    rect(s,0.62,6.55,11.84,0.42,"E8ECE8",None)
    txt(s,"DECISION: protect cash capacity, verify every exposure and count funding only when its arrival is confirmed.",
        0.83,6.64,11.42,0.22,9.0,NAVY,True,align=PP_ALIGN.CENTER)

    prs.core_properties.title = "UBS 2011 Rogue Trading — Treasury Response"
    prs.core_properties.subject = "Eight-slide presentation aligned to report sections"
    prs.core_properties.author = "Corporate Treasury Management Team"
    prs.save(OUT)
    return OUT


if __name__ == "__main__":
    print(make_deck())
