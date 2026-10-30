from pathlib import Path
from PIL import Image
import xlsxwriter
from pptx import Presentation
from pptx.chart.data import CategoryChartData
from pptx.dml.color import RGBColor
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
PPTX_OUT = ROOT / "ubs-treasury-risk-presentation-8-slides.pptx"
XLSX_OUT = ROOT / "ubs-illustrative-liquidity-model.xlsx"
MAP_SLIDE = ASSETS / "approved-map-slide-report-order.png"
NORMAL_HIDDEN_SLIDE = ASSETS / "approved-three-panel-slide.png"
DALTONS = ASSETS / "daltons-illustration.png"
UBS_LOGO = ASSETS / "ubs-logo-slide.png"
SKEMA_LOGO = ASSETS / "skema-logo.png"

SW, SH = 13.333333, 7.5
BG = "F7F7F3"
NAVY = "18232B"
BLACK = "101315"
DARK = "252B2F"
WHITE = "FFFFFF"
MUTED = "68747B"
SOFT = "A9B0B2"
RED = "C82036"
TEAL = "008F72"
GOLD = "C49500"
BLUE = "287FA8"
GREEN = "4F8A64"
GRID = "C9CECB"
LIGHT = "E8ECE8"
PALE_RED = "F6E2E3"
PALE_AMBER = "F8F0D9"
PALE_GREEN = "E6F0E9"
FONT = "Arial"

DATES = ["14 Sep", "15", "16", "17", "18", "19", "20", "30 Sep", "Oct", "Nov", "14 Dec"]
NO_INCIDENT = [1000, 990, 985, 990, 985, 987, 984, 1004, 1104, 1054, 1024]
INCIDENT_BASE = [1000, 915, 805, 775, 765, 772, 774, 769, 909, 849, 824]
COMBINED_STRESS = [1000, 915, 805, 775, 765, 772, 774, 769, 909, 549, 524]
BUFFER = 700


def C(value):
    return RGBColor.from_string(value)


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


def line(slide, x1, y1, x2, y2, color=GRID, width=1.0):
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
    r.font.name = FONT
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.color.rgb = C(color)
    return sh


def add_img_fit(slide, path, x, y, w, h):
    """Fit the complete image without crop or distortion."""
    with Image.open(path) as im:
        iw, ih = im.size
    aspect, box_aspect = iw/ih, w/h
    if aspect > box_aspect:
        dw, dh = w, w/aspect
        dx, dy = x, y+(h-dh)/2
    else:
        dh, dw = h, h*aspect
        dx, dy = x+(w-dw)/2, y
    return slide.shapes.add_picture(str(path), Inches(dx), Inches(dy),
                                    width=Inches(dw), height=Inches(dh))


def header(slide, title, kicker, page, section):
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = C(BG)
    slide.shapes.add_picture(str(UBS_LOGO), Inches(.42), Inches(.13),
                             width=Inches(1.38), height=Inches(.49))
    txt(slide, title, 2.02, .15, 9.65, .31, 17, NAVY, True)
    txt(slide, kicker, 2.02, .47, 9.65, .20, 9.3, RED, True)
    txt(slide, section, 2.02, .71, 9.65, .16, 7.4, MUTED)
    slide.shapes.add_picture(str(SKEMA_LOGO), Inches(12.35), Inches(.12),
                             width=Inches(.52), height=Inches(.55))
    line(slide, .42, .97, 12.90, .97, GRID, .9)
    line(slide, .42, 7.17, 12.90, 7.17, GRID, .7)
    txt(slide, f"UBS  ×  SKEMA   /   {page:02d}", 11.40, 7.22, 1.45, .12,
        6.4, MUTED, True, align=PP_ALIGN.RIGHT)


def add_user_slide(prs, image):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    s.background.fill.solid()
    s.background.fill.fore_color.rgb = C(BG)
    add_img_fit(s, image, 0, 0, SW, SH)
    return s


def build_model_workbook():
    wb = xlsxwriter.Workbook(str(XLSX_OUT))
    wb.set_properties({
        "title": "UBS 2011 illustrative Treasury liquidity model",
        "subject": "Cash bridge and stress assumptions; not historical UBS Treasury data",
        "author": "Corporate Treasury Management Team",
    })
    navy = "18232B"
    red = "C82036"
    teal = "008F72"
    gold = "C49500"
    muted = "68747B"
    grid = "D9DEDB"
    pale = "F1F4F1"
    fmt_title = wb.add_format({"bold": True, "font_size": 16, "font_color": navy})
    fmt_sub = wb.add_format({"font_color": muted, "font_size": 10, "text_wrap": True})
    fmt_head = wb.add_format({"bold": True, "font_color": "FFFFFF", "bg_color": navy,
                              "border": 1, "border_color": "FFFFFF", "text_wrap": True,
                              "valign": "vcenter"})
    fmt_input = wb.add_format({"bg_color": "FFF2CC", "border": 1, "border_color": grid,
                               "num_format": '#,##0;[Red](#,##0);–'})
    fmt_num = wb.add_format({"border": 1, "border_color": grid,
                             "num_format": '#,##0;[Red](#,##0);–'})
    fmt_num_bold = wb.add_format({"bold": True, "border": 1, "border_color": grid,
                                  "num_format": '#,##0;[Red](#,##0);–'})
    fmt_label = wb.add_format({"border": 1, "border_color": grid})
    fmt_note = wb.add_format({"font_color": muted, "italic": True, "text_wrap": True})
    fmt_section = wb.add_format({"bold": True, "font_color": "FFFFFF", "bg_color": teal})
    fmt_red = wb.add_format({"bold": True, "font_color": red, "border": 1, "border_color": grid,
                             "num_format": '#,##0;[Red](#,##0);–'})

    # README / evidence classification
    ws = wb.add_worksheet("Read me")
    ws.set_column("A:A", 27); ws.set_column("B:B", 94)
    ws.write("A1", "UBS 2011 · Treasury liquidity model", fmt_title)
    ws.merge_range("A2:B2", "Illustrative teaching model built in Python / Excel. It is not UBS historical Treasury data.", fmt_sub)
    notes = [
        ("Central question", "How should UBS Treasury preserve liquidity and meet payment obligations over the three months after concealed trading losses are discovered?"),
        ("Model horizon", "14 Sep–14 Dec 2011; daily in the first week, then period-end snapshots."),
        ("Evidence: public", "Incident dates, unauthorised trading, reported USD 2.3bn loss and control findings."),
        ("Inputs: assumed", "Opening cash USD 1,000m; minimum buffer USD 700m; receipts, payments, settlements, collateral, costs and stress shocks."),
        ("Outputs: calculated", "Scenario closing cash, first buffer breach, and peak funding need. Reproduce from the Cash Bridge formulas."),
        ("Cash balance", "Accessible opening cash + receipts − payments − settlement outflow + signed collateral movement − costs + confirmed funding."),
        ("Funding gap", "max(0, minimum buffer − cash before funding). A trading loss is not automatically a same-day cash payment."),
        ("Use limitation", "Replace all yellow inputs with dated, entity-level Treasury ledger records before treating any funding gap as a UBS result."),
        ("Sources", "FINMA 2012; FSA 2012; UBS Q3 2011 disclosures. Model schema follows the illustrative cash bridge in the presentation."),
    ]
    for i,(a,b) in enumerate(notes,4):
        ws.write(i-1,0,a,fmt_head if i==4 else fmt_label)
        ws.write(i-1,1,b,fmt_sub if i==4 else fmt_label)
        ws.set_row(i-1,36 if len(b)>85 else 26)
    ws.freeze_panes(3,0)

    # Cash bridge with visible formulas and model inputs.
    cash = wb.add_worksheet("Cash Bridge")
    cash.freeze_panes(3,1)
    cash.set_column("A:A", 16)
    cash.set_column("B:K", 18)
    cash.merge_range("A1:K1", "Cash bridge · illustrative USD millions", fmt_title)
    cash.merge_range("A2:K2", "Yellow cells are assumed inputs. Closing cash is formula-driven; positive collateral movement is cash returned to UBS.", fmt_sub)
    headers=["Period","Base receipts","Base payments","Incident settlement\noutflow","Collateral\nmovement (+/−)","Incident costs","No-incident\nclose","Incident-base\nclose","Stress\nadjustment","Stress\nclose","Minimum\nbuffer"]
    for c,h in enumerate(headers): cash.write(2,c,h,fmt_head)
    cash.set_row(2,36)
    rows=[
        ("14 Sep · open",0,0,0,0,0),
        ("15 Sep",120,130,55,-20,0),
        ("16 Sep",90,95,80,-25,0),
        ("17 Sep",110,105,45,10,0),
        ("18 Sep",100,105,20,15,0),
        ("19 Sep",90,88,5,10,0),
        ("20 Sep",95,98,15,20,0),
        ("30 Sep",500,480,50,30,5),
        ("October",1800,1700,50,100,10),
        ("November",1600,1650,20,20,10),
        ("1–14 Dec",800,830,0,10,5),
    ]
    expected_no=[1000,990,985,990,985,987,984,1004,1104,1054,1024]
    expected_base=[1000,915,805,775,765,772,774,769,909,849,824]
    expected_stress=[1000,915,805,775,765,772,774,769,909,549,524]
    for idx,row in enumerate(rows,3):
        period,receipts,payments,settlement,collateral,costs=row
        cash.write(idx,0,period,fmt_label)
        vals=[receipts,payments,settlement,collateral,costs]
        for j,v in enumerate(vals,1): cash.write_number(idx,j,v,fmt_input)
        cash.write_number(idx,10,700,fmt_input)
        if idx==3:
            cash.write_formula(idx,6,"=1000",fmt_num_bold,1000)
            cash.write_formula(idx,7,"=1000",fmt_num_bold,1000)
            cash.write_number(idx,8,0,fmt_input)
            cash.write_formula(idx,9,"=H4+I4",fmt_num_bold,1000)
        else:
            prev=idx-1
            excelrow=idx+1
            cash.write_formula(idx,6,f"=G{excelrow-1}+B{excelrow}-C{excelrow}",fmt_num,expected_no[idx-3])
            cash.write_formula(idx,7,f"=H{excelrow-1}+B{excelrow}-C{excelrow}-D{excelrow}+E{excelrow}-F{excelrow}",fmt_num,expected_base[idx-3])
            stress_adj=-300 if period=="November" else 0
            cash.write_number(idx,8,stress_adj,fmt_input)
            cash.write_formula(idx,9,f"=J{excelrow-1}+B{excelrow}-C{excelrow}-D{excelrow}+E{excelrow}-F{excelrow}+I{excelrow}",fmt_num_bold,expected_stress[idx-3])
    cash.write("A16","Assumptions",fmt_section)
    cash.write("B16","Opening cash",fmt_label); cash.write_number("C16",1000,fmt_input)
    cash.write("D16","Minimum buffer",fmt_label); cash.write_number("E16",700,fmt_input)
    cash.merge_range("F16:K16","Opening cash and buffer are teaching assumptions, not published UBS Treasury data.",fmt_note)
    cash.write("A18","Peak gap",fmt_label)
    cash.write_formula("B18","=MAX(0,E16-MIN(J4:J14))",fmt_red,176)
    cash.write("C18","Peak gap = buffer less minimum stress close",fmt_note)
    # Excel chart
    chart=wb.add_chart({"type":"line"})
    chart.add_series({"name":"No incident","categories":"='Cash Bridge'!$A$4:$A$14","values":"='Cash Bridge'!$G$4:$G$14","line":{"color":teal,"width":2.25},"marker":{"type":"circle","size":4,"border":{"color":teal},"fill":{"color":teal}}})
    chart.add_series({"name":"Incident base","categories":"='Cash Bridge'!$A$4:$A$14","values":"='Cash Bridge'!$H$4:$H$14","line":{"color":"287FA8","width":2.25},"marker":{"type":"circle","size":4,"border":{"color":"287FA8"},"fill":{"color":"287FA8"}}})
    chart.add_series({"name":"Combined stress","categories":"='Cash Bridge'!$A$4:$A$14","values":"='Cash Bridge'!$J$4:$J$14","line":{"color":red,"width":2.5},"marker":{"type":"circle","size":4,"border":{"color":red},"fill":{"color":red}}})
    chart.add_series({"name":"Minimum buffer","categories":"='Cash Bridge'!$A$4:$A$14","values":"='Cash Bridge'!$K$4:$K$14","line":{"color":gold,"width":1.5,"dash_type":"dash"},"marker":{"type":"none"}})
    chart.set_title({"name":"Scenario closing cash vs minimum buffer"})
    chart.set_y_axis({"name":"USD millions","min":500,"max":1200,"major_unit":100,"major_gridlines":{"visible":True,"line":{"color":"D9DEDB"}}})
    chart.set_x_axis({"label_position":"low","num_font":{"size":8}})
    chart.set_legend({"position":"bottom","font":{"size":8}})
    chart.set_size({"width":920,"height":420})
    chart.set_chartarea({"border":{"none":True},"fill":{"color":"FFFFFF"}})
    chart.set_plotarea({"border":{"none":True},"fill":{"color":"FFFFFF"}})
    cash.insert_chart("A20",chart)
    cash.freeze_panes(3,1)

    stress=wb.add_worksheet("Stress Tests")
    stress.set_column("A:A",30); stress.set_column("B:B",17); stress.set_column("C:C",67)
    stress.merge_range("A1:C1","Combined stress · 30 Nov 2011 (illustrative)",fmt_title)
    stress.merge_range("A2:C2","Scenario inputs are assumed; the $2.3bn public loss is not entered as a single cash outflow.",fmt_sub)
    for c,h in enumerate(["Shock","Cash impact (USDm)","Illustrative timing / explanation"]): stress.write(2,c,h,fmt_head)
    shocks=[("Accelerated / increased settlement",-50,"Cash outflow brought forward or increased on 30 Nov."),
            ("Collateral return delayed",-100,"Expected collateral receipt falls beyond the model horizon."),
            ("Additional withdrawals",-100,"Incremental customer outflow in the stress period."),
            ("Funding maturity not renewed",-50,"Scheduled funding rollover unavailable on 30 Nov.")]
    for i,(a,b,c) in enumerate(shocks,3): stress.write(i,0,a,fmt_label); stress.write_number(i,1,b,fmt_input); stress.write(i,2,c,fmt_label)
    stress.write("A8","Total shock",fmt_head); stress.write_formula("B8","=SUM(B4:B7)",fmt_num_bold,-300); stress.write("C8","Additional delayed-liquidity-source timing is tested separately below.",fmt_label)
    stress.write("A10","Incident-base November close",fmt_label); stress.write_number("B10",849,fmt_input)
    stress.write("A11","Stress November close",fmt_label); stress.write_formula("B11","=B10+B8",fmt_red,549)
    stress.write("A12","Buffer",fmt_label); stress.write_number("B12",700,fmt_input)
    stress.write("A13","30 Nov shortfall",fmt_label); stress.write_formula("B13","=MAX(0,B12-B11)",fmt_red,151)
    stress.write("A14","14 Dec stress close",fmt_label); stress.write_number("B14",524,fmt_input)
    stress.write("A15","Peak funding need",fmt_label); stress.write_formula("B15","=MAX(0,B12-B14)",fmt_red,176)
    stress.merge_range("A17:C17","Funding timing test",fmt_section)
    for i,(a,b,c) in enumerate([("Assumed line","USD 200m","Availability / collateral conditions must be verified."),("Trigger","25 Nov","Trigger at least T+2 business days before the modeled breach."),("Illustrative arrival","29 Nov","T+2 assumption; not a historical UBS commitment."),("First breach","30 Nov","If the source arrives later, it cannot prevent the first shortfall.")],18):
        stress.write(i-1,0,a,fmt_label); stress.write(i-1,1,b,fmt_label); stress.write(i-1,2,c,fmt_label)

    risk=wb.add_worksheet("Risk Register")
    risk.set_column("A:A",25); risk.set_column("B:C",15); risk.set_column("D:D",15); risk.set_column("E:E",57)
    risk.merge_range("A1:E1","Residual risk register · illustrative ratings",fmt_title)
    risk.merge_range("A2:E2","Likelihood and impact are analyst assumptions for the 14 Sep–14 Dec horizon; re-score after containment.",fmt_sub)
    for c,h in enumerate(["Risk","Likelihood (1–3)","Impact (1–3)","Score","Why it matters"]): risk.write(2,c,h,fmt_head)
    risk_rows=[("Operational",2,3,"Unreconciled breaks could hide open positions."),
               ("Liquidity",2,3,"Settlement / collateral peak versus approved buffer."),
               ("Market",2,2,"Adverse price movement before positions close."),
               ("Counterparty",2,2,"Collateral return or receivable may be delayed."),
               ("Funding",2,3,"A maturity inside the horizon may not roll."),
               ("Reputational",1,2,"Outflows or tighter terms in a confidence stress."),
               ("Legal / regulatory",2,2,"Investigation and remediation timing / cost.")]
    for i,(name,l,impact,why) in enumerate(risk_rows,3):
        risk.write(i,0,name,fmt_label); risk.write_number(i,1,l,fmt_input); risk.write_number(i,2,impact,fmt_input)
        risk.write_formula(i,3,f"=B{i+1}*C{i+1}",fmt_num_bold,l*impact); risk.write(i,4,why,fmt_label)
    risk.merge_range("A12:E12","Scoring key",fmt_section)
    risk.merge_range("A13:E13","Likelihood: 1 unlikely · 2 possible · 3 likely. Impact: 1 headroom erosion <25% · 2 ≥25% without breach · 3 cash below buffer. The 25% cutoff is proposed, not UBS policy.",fmt_note)

    actions=wb.add_worksheet("CFO Actions")
    actions.set_column("A:A",29); actions.set_column("B:B",30); actions.set_column("C:C",29); actions.set_column("D:D",48); actions.set_column("E:E",45)
    actions.merge_range("A1:E1","CFO action plan · owners, timing and decision output",fmt_title)
    for c,h in enumerate(["Pillar","Owner","Deadline","Expected benefit / deliverable","Constraint / fallback"]): actions.write(2,c,h,fmt_head)
    action_rows=[
        ("Immediate liquidity protection","Group Treasurer","Initial view in 24h; daily to 14 Dec","Verified accessible cash, dated 13-week forecast and pre-positioned funding.","Confirm facility access, collateral eligibility and arrival; fallback only if independently verified."),
        ("Exposure containment","IB COO + Market Risk + Treasury","Start now; daily until reconciled","Independently reconcile open positions, settlements and collateral breaks.","Close-out cost / cash release only when confirmed; keep conservative overlay until then."),
        ("Governance & controls","CRO + IB COO; Internal Audit validates","Interim controls now; programme by 14 Dec","Dual verification, clear ownership and timely escalation of exceptions.","Manual dual sign-off until system controls are remediated."),
    ]
    for i,row in enumerate(action_rows,3):
        for c,val in enumerate(row): actions.write(i,c,val,fmt_label)
        actions.set_row(i,54)
    actions.freeze_panes(3,0)
    wb.close()


def make_deck():
    prs=Presentation()
    prs.slide_width=Inches(SW); prs.slide_height=Inches(SH)
    blank=prs.slide_layouts[6]

    # Slide 1: user's map is retained as one intact image.
    add_user_slide(prs,MAP_SLIDE)

    # Slide 2: explain the actual concealment mechanism, not just the loss outcome.
    s=prs.slides.add_slide(blank)
    header(s,"HOW HIDDEN POSITIONS ESCAPED CONTROLS",
           "SECTION 1.2  ·  CONCEALMENT MECHANISM",2,
           "REAL FUTURES EXPOSURE VS THE APPARENT INTERNAL RISK VIEW")
    # Conceptual divergence chart. No invented exposure amounts or scale.
    cx,cy,cw,ch=.65,1.44,8.55,4.96
    rect(s,cx,cy,cw,ch,WHITE,GRID,.8)
    txt(s,"RELATIVE EXPOSURE  ·  SCHEMATIC, NOT TO SCALE",cx+.20,cy+.14,5.2,.18,7.5,MUTED,True)
    left,right,top,bottom=cx+.66,cx+8.20,cy+.78,cy+4.02
    for yy in [top,top+(bottom-top)/3,top+2*(bottom-top)/3,bottom]:
        line(s,left,yy,right,yy,"E4E8E5",.55)
    # A growing true position, while the reported view stays artificially low.
    actual=[(left,bottom-.18),(left+1.25,bottom-.48),(left+2.50,bottom-.93),
            (left+3.75,bottom-1.48),(left+5.05,bottom-2.20),(left+6.35,top+.22)]
    reported=[(left,bottom-.18),(left+1.25,bottom-.25),(left+2.50,bottom-.32),
              (left+3.75,bottom-.37),(left+5.05,bottom-.43),(left+6.35,bottom-.49)]
    # Light fill between the lines communicates the concealed gap.
    gap_colors=["F8EEEE","F6E5E5","F4DADA","F1CDCF","EFC3C7"]
    for i in range(len(actual)-1):
        x1=actual[i][0];x2=actual[i+1][0]
        upper1=actual[i][1];upper2=actual[i+1][1]
        lower1=reported[i][1];lower2=reported[i+1][1]
        topavg=min(upper1,upper2);bottomavg=max(lower1,lower2)
        rect(s,x1,topavg,x2-x1,max(.04,bottomavg-topavg),gap_colors[i])
    for pts,color,width in [(actual,RED,2.5),(reported,BLUE,2.2)]:
        for a,b in zip(pts,pts[1:]): line(s,a[0],a[1],b[0],b[1],color,width)
        for x,y in pts: rect(s,x-.055,y-.055,.11,.11,color,shape=MSO_SHAPE.OVAL)
    txt(s,"REAL LONG INDEX FUTURES",left+.20,top+.04,3.0,.22,8.2,RED,True)
    txt(s,"Reported risk appears limited",left+4.05,bottom-.67,3.10,.22,8.0,BLUE,True)
    txt(s,"Unseen exposure",left+3.55,top+1.04,1.85,.20,8.0,RED,True,align=PP_ALIGN.CENTER)
    txt(s,"Positions build",left,bottom+.16,1.70,.20,7.1,MUTED)
    txt(s,"14 SEP 2011 · DISCOVERY",right-2.45,bottom+.16,2.45,.20,7.1,NAVY,True,align=PP_ALIGN.RIGHT)
    # Facts at right; simple numbered explanation rather than decorative cards.
    tx=9.52
    txt(s,"WHAT HAPPENED",tx,1.55,3.20,.23,9.4,NAVY,True)
    line(s,tx,1.88,12.73,1.88,RED,1.8)
    facts=[
        ("01","REAL POSITION","Long index futures remained open in the market."),
        ("02","FALSE HEDGE","Fictitious deferred-settlement ETF entries were booked internally as offsets."),
        ("03","APPARENT RISK","Risk reports appeared limited while real exposure kept growing."),
        ("04","DISCOVERY","14 September 2011 · reported loss USD 2.3bn."),
    ]
    for i,(n,title,desc) in enumerate(facts):
        yy=2.07+i*1.02
        txt(s,n,tx,yy,.38,.22,8.5,[RED,GOLD,BLUE,RED][i],True)
        txt(s,title,tx+.47,yy,2.72,.22,8.2,NAVY,True)
        txt(s,desc,tx+.47,yy+.28,2.72,.52,8.1,MUTED,valign=MSO_ANCHOR.TOP)
        if i<3: line(s,tx+.47,yy+.88,12.73,yy+.88,GRID,.55)
    txt(s,"Sources: FINMA 2012 §§11–18; FSA 2012 §§23–25. The chart is conceptual; it is not a historical exposure series.",
        .66,6.68,12.0,.22,7.0,MUTED)

    # Slide 3 — branching cash-transmission map with a feedback loop to controls.
    s=prs.slides.add_slide(blank)
    header(s,"FROM CONTROL FAILURE TO TREASURY IMPACT",
           "SECTION 1.3  ·  OPERATIONAL RISK → CASH → FUNDING",3,
           "FOLLOW THE EXPOSURE AS IT SPLITS INTO SETTLEMENT AND COLLATERAL NEEDS")
    txt(s,"A process map: one control failure creates market exposure, then two cash channels converge on liquidity.",
        .68,1.18,12.0,.28,9.5,NAVY,True)
    # Nodes are circles with labels; split/merge paths make the causal logic visible.
    def node(cx,cy,num,title,sub,color,label_y=None,label_x=None,label_w=1.75):
        rect(s,cx-.37,cy-.37,.74,.74,color,shape=MSO_SHAPE.OVAL)
        txt(s,num,cx-.37,cy-.16,.74,.28,13,WHITE,True,align=PP_ALIGN.CENTER)
        if label_y is None: label_y=cy+.43
        if label_x is None: label_x=cx-label_w/2
        txt(s,title,label_x,label_y,label_w,.36,8.5,NAVY,True,align=PP_ALIGN.CENTER)
        if sub:
            txt(s,sub,label_x,label_y+.36,label_w,.25,7.4,color,True,align=PP_ALIGN.CENTER)
    def arrow(x1,y1,x2,y2,color,angle):
        line(s,x1,y1,x2,y2,color,2.1)
        tri=rect(s,x2-.10,y2-.10,.20,.20,color,shape=MSO_SHAPE.ISOSCELES_TRIANGLE)
        tri.rotation=angle
    # Main sequence
    node(1.24,3.02,"1","CONTROL FAILURE","Verification gap",RED,label_w=1.85)
    node(3.42,3.02,"2","HIDDEN POSITIONS","False offsets",RED,label_w=1.90)
    node(5.63,3.02,"3","TRADING LOSS","USD 2.3bn",RED,label_w=1.75)
    # Branch into the two cash-transmission channels.
    node(7.40,2.08,"4A","SETTLEMENT","Cash due",GOLD,label_y=2.47,label_w=1.68)
    node(7.40,4.02,"4B","COLLATERAL","Calls / delayed returns",GOLD,label_y=4.43,label_w=1.90)
    node(9.50,3.02,"5","LIQUIDITY PRESSURE","Buffer at risk",GOLD,label_w=2.05)
    node(11.73,3.02,"6","TREASURY RESPONSE","Funding action",TEAL,label_w=2.00)
    arrow(1.62,3.02,3.02,3.02,RED,90)
    arrow(3.80,3.02,5.23,3.02,RED,90)
    arrow(5.97,2.82,7.00,2.25,RED,45)
    arrow(5.97,3.22,7.00,3.83,RED,135)
    arrow(7.78,2.24,9.12,2.83,GOLD,135)
    arrow(7.78,3.84,9.12,3.22,GOLD,45)
    arrow(9.88,3.02,11.35,3.02,TEAL,90)
    # Feedback path: funding response leads to redesigned controls.
    line(s,11.73,3.42,11.73,5.76,TEAL,1.8)
    line(s,11.73,5.76,1.24,5.76,TEAL,1.8)
    left_tri=rect(s,1.14,5.66,.20,.20,TEAL,shape=MSO_SHAPE.ISOSCELES_TRIANGLE);left_tri.rotation=270
    txt(s,"ENHANCED CONTROLS & MONITORING",4.42,5.46,4.62,.22,8.1,TEAL,True,align=PP_ALIGN.CENTER)
    txt(s,"A trading loss becomes a Treasury issue only when it generates cash obligations through settlements, collateral requirements or funding constraints.",
        .68,6.20,12.0,.52,9.8,NAVY,True,align=PP_ALIGN.CENTER)


    # Slide 4: timeline with Dalton metaphor and fuller event interpretation.
    s=prs.slides.add_slide(blank)
    header(s,"INCIDENT TIMELINE","SECTION 1.2  ·  DISCOVERY, DISCLOSURE & RESPONSE",4,
           "THE POSITIONS ACCUMULATED BEFORE THE SEPTEMBER DISCOVERY")
    line(s,.76,2.02,9.16,2.02,GRID,2.1)
    events=[
        (.70,RED,"14 SEP","DISCOVERY","Unauthorised positions identified."),
        (2.86,RED,"15 SEP","PUBLIC DISCLOSURE","UBS announces an initial loss estimate."),
        (5.02,GOLD,"FOLLOWING DAYS","CONTAINMENT","Positions reviewed; hedging and risk reduction actions."),
        (7.18,TEAL,"FOLLOWING WEEKS","INVESTIGATION","Control failures analysed; remediation launched."),
    ]
    for x,color,date,title,desc in events:
        center=x+.92
        rect(s,center-.11,1.91,.22,.22,color,shape=MSO_SHAPE.OVAL)
        txt(s,date,x,2.25,1.86,.22,8.1,color,True)
        txt(s,title,x,2.57,1.86,.40,8.6,NAVY,True)
        txt(s,desc,x,3.04,1.86,.62,8.1,MUTED,valign=MSO_ANCHOR.TOP)
    # Dalton illustration supports, but does not replace, the chronology.
    rect(s,9.57,1.48,3.25,1.91,WHITE,GRID,.8)
    add_img_fit(s,DALTONS,9.66,1.57,3.07,1.58)
    txt(s,"ILLUSTRATIVE CARTOON",9.68,3.20,3.02,.14,6.8,MUTED,True,align=PP_ALIGN.RIGHT)
    txt(s,"Hidden positions accumulated before being uncovered in September 2011.",
        9.58,3.58,3.22,.48,8.2,NAVY,True)
    # Small escalation graphic: compact bars make the Dalton metaphor explicit.
    bx=9.73; by=5.37
    barh=[.22,.40,.62,.88]
    for i,h in enumerate(barh):
        xx=bx+i*.67
        rect(s,xx,by-h,.48,h,[TEAL,GOLD,RED,RED][i])
    txt(s,"SMALL",9.72,5.49,.48,.14,6.2,MUTED,True,align=PP_ALIGN.CENTER)
    txt(s,"GROWING",10.39,5.49,.48,.14,6.2,MUTED,True,align=PP_ALIGN.CENTER)
    txt(s,"LARGER",11.06,5.49,.48,.14,6.2,MUTED,True,align=PP_ALIGN.CENTER)
    txt(s,"DISCOVERY",11.73,5.49,.66,.14,6.0,RED,True,align=PP_ALIGN.CENTER)
    line(s,.70,4.14,12.78,4.14,GRID,.8)
    txt(s,"TREASURY TAKEAWAY",.72,4.42,1.72,.19,7.7,RED,True)
    txt(s,"The discovery date starts the response horizon; it does not make prior losses a same-day cash payment.",
        2.55,4.37,6.55,.36,9.2,NAVY,True)
    rect(s,.70,5.15,8.40,.79,PALE_AMBER)
    txt(s,"14 Sep 2011",.92,5.30,1.32,.20,8.2,GOLD,True)
    txt(s,"Three-month Treasury response horizon",2.40,5.28,4.80,.22,9.1,NAVY,True)
    txt(s,"FINMA 2012; FSA 2012; UBS disclosures. The Dalton image is illustrative, not an incident photograph.",
        .72,6.55,11.98,.20,7.0,MUTED)

    # Slide 5: native PowerPoint / Excel line chart plus narrative interpretation.
    s=prs.slides.add_slide(blank)
    header(s,"TREASURY LIQUIDITY EVOLUTION","SECTION 2.2  ·  CASH BRIDGE",5,
           "ILLUSTRATIVE USDm SCENARIOS · NOT HISTORICAL UBS TREASURY CASH")
    chartdata=CategoryChartData(); chartdata.categories=DATES
    chartdata.add_series("No incident",NO_INCIDENT)
    chartdata.add_series("Incident base",INCIDENT_BASE)
    chartdata.add_series("Combined stress",COMBINED_STRESS)
    chartdata.add_series("Minimum buffer",[BUFFER]*len(DATES))
    chart=s.shapes.add_chart(XL_CHART_TYPE.LINE_MARKERS, Inches(.62), Inches(1.30),
                             Inches(12.05), Inches(3.78), chartdata).chart
    chart.has_title=False; chart.has_legend=True
    chart.legend.position=XL_LEGEND_POSITION.BOTTOM; chart.legend.include_in_layout=False
    chart.legend.font.name=FONT; chart.legend.font.size=Pt(8.5)
    va=chart.value_axis; va.minimum_scale=500;va.maximum_scale=1200;va.major_unit=100
    va.has_major_gridlines=True
    va.tick_labels.font.name=FONT;va.tick_labels.font.size=Pt(8);va.tick_labels.font.color.rgb=C(MUTED)
    ca=chart.category_axis;ca.tick_labels.font.name=FONT;ca.tick_labels.font.size=Pt(8);ca.tick_labels.font.color.rgb=C(MUTED)
    colors=[TEAL,BLUE,RED,GOLD]
    for i,ser in enumerate(chart.series):
        ser.format.line.color.rgb=C(colors[i]);ser.format.line.width=Pt(2 if i<3 else 1.3)
        if i<3:
            ser.marker.style=2;ser.marker.size=4
            ser.marker.format.fill.solid();ser.marker.format.fill.fore_color.rgb=C(colors[i])
            ser.marker.format.line.color.rgb=C(colors[i])
        else:
            ser.marker.style=1;ser.format.line.dash_style=4
    # Narrative, not bullets: explain why each path moves.
    narratives=[
        (.68,TEAL,"NO INCIDENT","Normal receipts and payments keep modeled cash above the assumed $700m buffer; minimum $984m."),
        (4.72,BLUE,"INCIDENT BASE","Additional settlement and collateral needs reduce headroom; minimum $765m, no modeled breach."),
        (8.76,RED,"COMBINED STRESS","Withdrawals and delayed collateral returns push cash below buffer on 30 Nov; peak gap $176m by 14 Dec."),
    ]
    for x,color,title,body in narratives:
        txt(s,title,x,5.23,3.78,.20,8.1,color,True)
        line(s,x,5.50,x+3.74,5.50,color,1.4)
        txt(s,body,x,5.63,3.78,.78,8.5,NAVY,valign=MSO_ANCHOR.TOP)
    txt(s,"Cash bridge formula: opening accessible cash + receipts − payments − settlement outflow + signed collateral movement − costs. Funding gap = max(0, buffer − cash before funding).",
        .68,6.63,12.0,.25,7.0,MUTED)

    # Slide 6 — stress test waterfall, quantified and visually tied to the buffer.
    s=prs.slides.add_slide(blank)
    header(s,"STRESS TEST: WHEN DOES CASH FALL BELOW THE BUFFER?",
           "SECTION 2.3  ·  COMBINED SCENARIO",6,
           "ILLUSTRATIVE USDm · STRESS INPUTS ARE ASSUMPTIONS, NOT UBS ACTUAL CASH FLOWS")
    txt(s,"$849m   −   $50m   −   $100m   −   $100m   −   $50m   =   $549m",
        .72,1.18,12.0,.46,18,NAVY,True,align=PP_ALIGN.CENTER)
    # Waterfall occupies most of the slide; the horizontal buffer line makes the breach immediate.
    px,py,pw,ph=.70,1.83,8.67,3.52
    rect(s,px,py,pw,ph,WHITE,GRID,.8)
    left,right=px+.62,px+pw-.22
    top,bottom=py+.32,py+2.72
    vmin,vmax=450,900
    def yv(v): return bottom-(v-vmin)/(vmax-vmin)*(bottom-top)
    for value in (500,600,700,800,900):
        yy=yv(value)
        line(s,left,yy,right,yy,RED if value==700 else "E2E6E3",1.45 if value==700 else .55)
        txt(s,str(value),px+.06,yy-.08,.42,.16,6.8,RED if value==700 else MUTED,
            value==700,align=PP_ALIGN.RIGHT)
    steps=[
        (1.32,849,849,"INCIDENT BASE","$849m",BLUE),
        (2.47,849,799,"SETTLEMENT","−$50m",GOLD),
        (3.62,799,699,"COLLATERAL","−$100m",GOLD),
        (4.77,699,599,"WITHDRAWALS","−$100m",RED),
        (5.92,599,549,"ROLLOVER","−$50m",RED),
    ]
    barw=.62
    for i,(x,before,after,label,value,color) in enumerate(steps):
        if i==0:
            by=yv(before);height=bottom-by
        else:
            by=yv(before);height=yv(after)-yv(before)
        rect(s,x,by,barw,max(height,.075),color)
        txt(s,value,x-.16,by-.26,.94,.18,8.0,color,True,align=PP_ALIGN.CENTER)
        txt(s,label,x-.28,bottom+.11,1.18,.26,6.5,NAVY,True,align=PP_ALIGN.CENTER)
        if i<len(steps)-1:
            line(s,x+barw,yv(after),steps[i+1][0],yv(after),MUTED,.8)
    # End-state cash column and visible gap to buffer.
    fx=7.58
    rect(s,fx,yv(549),.72,bottom-yv(549),RED)
    txt(s,"$549m",fx-.15,yv(549)-.27,1.02,.20,9,RED,True,align=PP_ALIGN.CENTER)
    txt(s,"STRESS CLOSE",fx-.25,bottom+.11,1.22,.26,6.5,NAVY,True,align=PP_ALIGN.CENTER)
    line(s,fx+.80,yv(700),fx+.80,yv(549),RED,2.0)
    txt(s,"$151m\nshortfall",fx+.89,yv(700)+.02,.82,.38,7.2,RED,True)
    # Right callout: what the breach means.
    rect(s,9.62,1.83,3.02,3.52,PALE_RED,GRID,.8)
    txt(s,"30 NOVEMBER",9.86,2.08,2.54,.20,8.0,RED,True)
    txt(s,"$549m",9.86,2.43,2.54,.48,24,RED,True)
    txt(s,"vs. $700m buffer",9.86,2.93,2.54,.23,9.2,NAVY,True)
    line(s,9.86,3.31,12.40,3.31,RED,1.2)
    txt(s,"14 DECEMBER",9.86,3.52,2.54,.19,7.7,MUTED,True)
    txt(s,"$524m cash  ·  $176m peak funding need",9.86,3.81,2.54,.46,9.2,NAVY,True)
    txt(s,"ASSUMED FUNDING TIMING",9.86,4.46,2.54,.18,7.0,MUTED,True)
    # T+2 timing strip
    txt(s,"Assumed $200m T+2 source",.78,5.73,2.20,.20,8.0,NAVY,True)
    line(s,3.15,5.86,11.70,5.86,GRID,2.0)
    timeline=[(3.42,"25 NOV","Trigger",GOLD),(7.05,"29 NOV","Arrival",TEAL),(10.92,"30 NOV","First breach",RED)]
    for x,date,label,color in timeline:
        rect(s,x-.10,5.76,.20,.20,color,shape=MSO_SHAPE.OVAL)
        txt(s,date,x-.43,6.05,.86,.18,7.4,color,True,align=PP_ALIGN.CENTER)
        txt(s,label,x-.52,6.28,1.05,.18,7.0,MUTED,align=PP_ALIGN.CENTER)
    txt(s,"If the source arrives after the breach, it cannot prevent the first shortfall. Verify facility access, collateral eligibility and settlement dates.",
        .72,6.68,12.0,.22,7.0,MUTED)


    # Slide 7 — full heatmap, with the risk names written directly in their cells.
    s=prs.slides.add_slide(blank)
    header(s,"RISK MATRIX","SECTION 3.1  ·  LIKELIHOOD × IMPACT",7,
           "RESIDUAL RATINGS ARE ANALYST JUDGEMENTS FOR THE THREE-MONTH HORIZON")
    mx,my,cw,ch=.88,1.65,2.30,1.42
    # Rows: likely / possible / unlikely; columns: low / medium / high impact.
    fills=[["F1C9CD","E9AEB4","DD8E99"],
           ["F4E6BE","F0D998","E9C56F"],
           ["D7E9DC","E4ECD8","F0E6C7"]]
    cell_text=[
        ["","",""],
        ["","Market · 4\nCounterparty · 4\nLegal / regulatory · 4",
         "Operational · 6\nLiquidity · 6\nFunding · 6"],
        ["","Reputational · 2",""]
    ]
    for r in range(3):
        for c in range(3):
            x=mx+c*cw;y=my+r*ch
            rect(s,x,y,cw-.05,ch-.05,fills[r][c],WHITE,1.4)
            score=(3-r)*(c+1)
            txt(s,str(score),x+.10,y+.07,.25,.18,7.2,MUTED,True)
            if cell_text[r][c]:
                color=RED if c==2 else (GOLD if c==1 else GREEN)
                txt(s,cell_text[r][c],x+.14,y+.31,cw-.33,ch-.43,9.0,color,True,
                    align=PP_ALIGN.CENTER)
    for r,label in enumerate(["LIKELY","POSSIBLE","UNLIKELY"]):
        txt(s,label,.08,my+r*ch+.53,.70,.20,7.5,NAVY,True,align=PP_ALIGN.RIGHT)
    txt(s,"LIKELIHOOD",.08,1.38,.70,.18,7.0,MUTED,True,align=PP_ALIGN.RIGHT)
    for c,label in enumerate(["LOW","MEDIUM","HIGH"]):
        txt(s,label,mx+c*cw,my+3*ch+.03,cw-.05,.20,7.7,NAVY,True,align=PP_ALIGN.CENTER)
    txt(s,"IMPACT",mx+2.15,my+3*ch+.32,1.0,.18,7.0,MUTED,True,align=PP_ALIGN.CENTER)
    # Right-side priority logic adds meaning without repeating a coded legend.
    tx=8.25
    txt(s,"PRIORITY EXPOSURES",tx,1.72,4.35,.25,10,NAVY,True)
    line(s,tx,2.08,12.66,2.08,RED,1.8)
    priority_rows=[
        ("01","OPERATIONAL","Unreconciled breaks can hide open positions."),
        ("02","LIQUIDITY","Dated settlement and collateral needs can breach the buffer."),
        ("03","FUNDING","Maturing sources may not roll before cash is due."),
    ]
    for i,(num,title,desc) in enumerate(priority_rows):
        yy=2.34+i*1.03
        txt(s,num,tx,yy,.42,.22,8.4,RED,True)
        txt(s,title,tx+.52,yy,3.80,.22,8.8,NAVY,True)
        txt(s,desc,tx+.52,yy+.30,3.80,.44,8.0,MUTED,valign=MSO_ANCHOR.TOP)
        if i<2:line(s,tx+.52,yy+.84,12.64,yy+.84,GRID,.65)
    txt(s,"No risk is currently scored likely in the base assessment.",tx,5.54,4.30,.36,8.2,NAVY,True)
    # Explicit color key for an audience new to heatmaps.
    rect(s,.88,6.38,.22,.18,GREEN);txt(s,"Lower",1.17,6.36,.72,.20,7.2,MUTED)
    rect(s,2.05,6.38,.22,.18,GOLD);txt(s,"Monitor",2.34,6.36,.88,.20,7.2,MUTED)
    rect(s,3.38,6.38,.22,.18,RED);txt(s,"Priority",3.67,6.36,.92,.20,7.2,MUTED)
    txt(s,"Score = likelihood × impact (1–3). Analyst ratings, not UBS / regulator scores; calibrate impact to the approved buffer and re-score after containment.",
        5.08,6.32,7.56,.32,7.0,MUTED)


    # Slide 8: consulting-style 3-pillar roadmap.
    s=prs.slides.add_slide(blank)
    header(s,"CFO ACTION PLAN","SECTION 3.2  ·  THREE PILLARS",8,
           "SEQUENCE ACTIONS FROM CASH VISIBILITY TO LASTING CONTROL")
    pillars=[
        (.67,TEAL,"IMMEDIATE","WITHIN 24h","LIQUIDITY ASSESSMENT","Owner  ·  Group Treasurer",
         "Build a dated cash view; confirm accessible liquidity and funding arrival.",
         "Benefit  ·  No unexpected cash breach"),
        (4.72,GOLD,"CONTAINMENT","DAYS","POSITION RECONCILIATION","Owner  ·  COO + Risk + Treasury",
         "Independently match positions, settlements and collateral; track unresolved breaks daily.",
         "Benefit  ·  Reduce uncertainty"),
        (8.77,RED,"PREVENTION","3 MONTHS","GOVERNANCE UPGRADE","Owner  ·  CRO",
         "Strengthen independent verification, exception escalation and control ownership.",
         "Benefit  ·  Prevent recurrence"),
    ]
    for x,color,phase,when,title,owner,action,benefit in pillars:
        # Flat consulting-column layout, with a single accent rule and timeline marker.
        txt(s,phase,x,1.62,3.62,.22,8.3,color,True)
        txt(s,when,x+2.45,1.62,1.17,.22,7.6,MUTED,True,align=PP_ALIGN.RIGHT)
        line(s,x,1.94,x+3.62,1.94,color,2.0)
        txt(s,title,x,2.20,3.62,.49,12,NAVY,True)
        txt(s,owner,x,2.92,3.62,.33,8.2,color,True)
        # execution track
        line(s,x+.10,3.55,x+.10,5.65,GRID,2.0)
        rect(s,x+.02,3.62,.17,.17,color,shape=MSO_SHAPE.OVAL)
        txt(s,action,x+.34,3.47,3.25,.94,9.2,NAVY,True,valign=MSO_ANCHOR.TOP)
        line(s,x+.34,4.62,x+3.62,4.62,GRID,.7)
        txt(s,benefit,x+.34,4.82,3.25,.45,8.6,color,True)
        if phase=="IMMEDIATE":
            txt(s,"Fallback · use only confirmed, accessible funding.",x+.34,5.45,3.25,.48,7.7,MUTED)
        elif phase=="CONTAINMENT":
            txt(s,"Fallback · retain a conservative overlay until breaks close.",x+.34,5.45,3.25,.48,7.7,MUTED)
        else:
            txt(s,"Fallback · manual dual sign-off until controls are live.",x+.34,5.45,3.25,.48,7.7,MUTED)
    # Shared objective anchors the three pillars.
    rect(s,.67,6.24,11.72,.62,LIGHT)
    txt(s,"OBJECTIVE",.89,6.39,1.18,.19,7.6,RED,True)
    txt(s,"Maintain liquidity above the minimum buffer throughout the Treasury horizon.",
        2.16,6.34,9.94,.28,10,NAVY,True,align=PP_ALIGN.CENTER)
    txt(s,"Count funding only when availability, collateral and arrival time are verified.",
        .68,6.93,12.0,.15,6.9,MUTED,align=PP_ALIGN.CENTER)

    prs.core_properties.title="UBS 2011 Rogue Trading · Treasury Response"
    prs.core_properties.subject="Eight-slide Treasury presentation with analytical Excel/Python visuals"
    prs.core_properties.author="Corporate Treasury Management Team"
    prs.save(PPTX_OUT)
    return PPTX_OUT


if __name__=="__main__":
    build_model_workbook()
    print(make_deck())
    print(XLSX_OUT)
