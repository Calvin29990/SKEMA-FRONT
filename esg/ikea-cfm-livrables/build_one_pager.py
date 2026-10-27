"""One-pager individuel (A4, une seule page recto) : moitié haute = carte du raisonnement,
moitié basse = synthèse.

ATTENTION : la question et la thèse sont un BROUILLON à remplacer par le point de vue
personnel de l'étudiant (exigence du cours : l'opinion doit être la sienne).
Usage : python3 build_one_pager.py
"""
import os
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "E-Focus-Finance-one-pager.pdf")
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
pdfmetrics.registerFont(TTFont("DV", os.path.join(FONT_DIR, "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("DVB", os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")))
DVI = "DV"  # pas de variante italique installée

W, H = A4
BLUE = HexColor("#0058A3")
YEL = HexColor("#FFDA1A")
INK = HexColor("#1A1A1A")
GREY = HexColor("#5F6368")
LIGHT = HexColor("#F3F5F8")
M = 44  # marge latérale
CW = W - 2 * M  # largeur utile


def st(name, size, leading=None, font="DV", color=INK, **kw):
    return ParagraphStyle(name, fontName=font, fontSize=size,
                          leading=leading or size * 1.3, textColor=color, **kw)


def para(c, text, s, x, y_top, w):
    text = text.replace(" %", "&nbsp;%")
    p = Paragraph(text, s)
    _, h = p.wrap(w, 1000)
    p.drawOn(c, x, y_top - h)
    return h


def rect(c, x, y, w, h, fill, radius=0):
    c.setFillColor(fill)
    if radius:
        c.roundRect(x, y, w, h, radius, stroke=0, fill=1)
    else:
        c.rect(x, y, w, h, stroke=0, fill=1)


def build():
    c = canvas.Canvas(OUT, pagesize=A4)
    c.setTitle("One-pager individuel - E focus finance (brouillon)")
    c.setAuthor("Calvin Minang")

    # En-tête
    rect(c, 0, H - 8, W, 8, BLUE)
    c.setFillColor(GREY)
    c.setFont("DV", 7.5)
    c.drawString(M, H - 24, "CFM · Sustainable Finance · One-pager individuel · Calvin Minang")
    c.drawRightString(W - M, H - 24, "Recto unique")

    # ---------- MOITIÉ HAUTE : carte du raisonnement ----------
    y = H - 40
    c.setFillColor(BLUE)
    c.setFont("DVB", 9)
    c.drawString(M, y - 8, "CARTE DU RAISONNEMENT")
    y -= 18

    # Question
    q = ("<b>Question.</b> Les fonds Article 8 et 9 (SFDR) réduisent-ils réellement les émissions "
         "de l'économie réelle, ou déplacent-ils seulement le problème ?")
    h = para(c, q, st("q", 10.5, 14), M + 10, y - 8, CW - 20)
    box_h = h + 16
    rect(c, M, y - box_h, CW, box_h, YEL, radius=6)
    para(c, q, st("q2", 10.5, 14), M + 10, y - 8, CW - 20)
    y = y - box_h - 10

    # Trois branches
    branches = [
        ("1 · Transparence ≠ impact",
         "Le SFDR impose une stratégie déclarée et des indicateurs de principales incidences négatives (PAI). "
         "L'Article 8 « promeut » des caractéristiques ; l'Article 9 vise un « objectif d'investissement durable ». "
         "Aucun des deux n'impose une baisse mesurée des émissions.",
         "Source : cours, Module 2 (SFDR, PAI, DNSH)"),
        ("2 · Coût du capital",
         "Un investisseur qui exclut ou pondère un émetteur fait monter son coût du capital. L'effet réel passe "
         "par les flux primaires : un achat sur le marché secondaire transfère une action sans financer de projet.",
         "Source : cours, Module 1 (exclusion, engagement) ; Module 3 (additionnalité)"),
        ("3 · Preuve et greenwashing",
         "L'alignement à la taxonomie UE mesure une éligibilité, pas une réduction d'émissions. Le cadre vise "
         "à la fois les risques financiers climatiques et le greenwashing : une même étiquette peut couvrir des effets très différents.",
         "Source : cours, Module 2 (Taxonomie UE, objectifs du cadre)"),
    ]
    gap = 10
    bw = (CW - 2 * gap) / 3
    bh = 178
    for i, (ttl, body, src) in enumerate(branches):
        x = M + i * (bw + gap)
        rect(c, x, y - bh, bw, bh, LIGHT, radius=6)
        rect(c, x, y - 4, bw, 4, BLUE, radius=2)
        para(c, ttl, st("bt", 9.5, 12, font="DVB", color=BLUE), x + 9, y - 14, bw - 18)
        hb = para(c, body, st("bb", 8.6, 11.6), x + 9, y - 42, bw - 18)
        para(c, src, st("bs", 7.2, 9, font="DV", color=GREY), x + 9, y - 46 - hb, bw - 18)
    y = y - bh - 10

    # Thèse
    thesis = ("<b>Ma thèse.</b> Non, pas automatiquement. Le SFDR améliore la transparence, pas l'impact. "
              "L'effet environnemental dépend de l'engagement actionnarial et de l'additionnalité du financement.")
    ht = para(c, thesis, st("th", 9.6, 13.5, color=white), M + 12, y - 9, CW - 24)
    box = ht + 18
    rect(c, M, y - box, CW, box, BLUE, radius=6)
    para(c, thesis, st("th2", 9.6, 13.5, color=white), M + 12, y - 9, CW - 24)
    y = y - box - 8

    # Ce qui me ferait changer d'avis
    flip = ("<b>Ce qui me ferait changer d'avis.</b> Si les PAI publiés montrent, sur plusieurs années, une baisse "
            "des émissions des portefeuilles Article 8/9 supérieure à celle des fonds classiques, vérifiable par "
            "une source publique.")
    hf = para(c, flip, st("fl", 8.6, 11.6), M + 10, y - 7, CW - 20)
    rect(c, M, y - hf - 14, CW, hf + 14, LIGHT, radius=6)
    para(c, flip, st("fl2", 8.6, 11.6), M + 10, y - 7, CW - 20)
    y_half = y - hf - 14  # bas de la moitié haute

    # Séparateur
    c.setStrokeColor(GREY)
    c.setDash(3, 3)
    c.setLineWidth(0.6)
    sep_y = y_half - 14
    c.line(M, sep_y, W - M, sep_y)
    c.setDash()

    # ---------- MOITIÉ BASSE : synthèse ----------
    y = sep_y - 16
    c.setFillColor(BLUE)
    c.setFont("DVB", 9)
    c.drawString(M, y - 8, "SYNTHÈSE")
    y -= 20

    summary = [
        "Un fonds classé Article 8 ou 9 ne prouve pas, à lui seul, qu'il réduit les émissions de l'économie réelle. "
        "Le SFDR est d'abord une obligation de transparence : stratégie déclarée, principales incidences négatives (PAI) "
        "et principe « do no significant harm » (DNSH). Cette transparence a une vraie valeur, car elle permet à "
        "l'épargnant de comparer. Mais elle décrit ce qu'un fonds déclare faire, pas ce que son capital produit.",

        "Mon point de vue est donc nuancé. Le levier environnemental passe moins par le label que par deux mécanismes. "
        "Le premier est l'engagement : vote en assemblée générale, dialogue, et escalade jusqu'à la cession. "
        "Le second est l'additionnalité : financer des projets qui n'auraient pas été financés sans ce capital. "
        "Un portefeuille bien noté peut détenir des actions déjà cotées, dont le prix change de main sans que le "
        "capital réel bouge. Dans ce cas, le fonds gagne en réputation sans réduire d'émissions.",

        "Je retiens donc que le SFDR est un outil nécessaire mais insuffisant. Pour qu'il tienne sa promesse, il "
        "faudrait relier les PAI à des trajectoires mesurées, publier des données vérifiables et distinguer le "
        "financement primaire du secondaire. Ma position peut être contestée sur un point : si les fonds Article 8/9 "
        "excluent finalement les émetteurs les plus émetteurs, la pression sur leur coût du capital peut suffire à "
        "changer leur comportement, même sans engagement actif. C'est le test que je proposerais aux données.",
    ]
    s_body = st("sb", 9.8, 13.8, leftIndent=0)
    for para_txt in summary:
        hp = para(c, para_txt, s_body, M, y, CW)
        y -= hp + 7

    # Pied de page
    c.setFillColor(GREY)
    c.setFont("DV", 7)
    foot = ("Sources : cours Sabrine Aouida, Modules 1 à 3 (« Skema Module 1 Sustainable Finance and impact investing »). "
            "Règlements à vérifier sur les textes officiels : SFDR (UE) 2019/2088 ; taxonomie (UE) 2020/852.")
    para(c, foot, st("ft", 7, 9, font="DV", color=GREY), M, 40, CW)

    c.save()
    print("écrit :", OUT, "| bas de synthèse y =", round(y, 1))


if __name__ == "__main__":
    build()
