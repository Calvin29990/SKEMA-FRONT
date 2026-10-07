#!/usr/bin/env python3
"""md2pdf.py — rend un PDF A4 imprimable depuis un markdown allégé.

Utilisé pour les documents destinés à être imprimés puis remis en main propre
(recours ANBG, mémo des parents, courriel à adresser). Pas de dépendance hors
PyMuPDF.

Sous-ensemble markdown reconnu :
  # / ## / ###            titres
  -  ou *                 liste à puces   (les lignes "1." "2." sont traitées comme texte)
  >                       bloc cité (retrait + filet vertical)
  |  ... |                tableau (la 2e ligne "|---|" = séparateur, ignorée)
  ---                     filet
  <<<                     saut de page
  **gras**  *italique*    mise en ligne

Usage : python3 md2pdf.py entree.md sortie.pdf ["Pied de page"]
"""
import re
import sys

import pymupdf as fitz

MARGIN_L = MARGIN_R = 50.0
MARGIN_T = 54.0
MARGIN_B = 48.0
PAGE_W, PAGE_H = fitz.paper_size("a4")
BODY, SMALL = 9.7, 7.9
LEAD, LEAD_S = 12.9, 10.9

# Codes couleur de lecture : chaque couleur = un destinataire, repérable au bord de page.
ACCENTS = {
    "commun": ((0.11, 0.14, 0.20), "DOSSIER — TOUS ACTEURS"),
    "bleu":   ((0.09, 0.33, 0.62), "LECTURE CAMPUS FRANCE"),
    "vert":   ((0.02, 0.44, 0.30), "LECTURE ANBG"),
    "orange": ((0.76, 0.38, 0.04), "LECTURE SKEMA BUSINESS SCHOOL"),
    "rouge":  ((0.58, 0.10, 0.14), "CONSTATS DE DISCORDANCE"),
}
DIRECTIVE = re.compile(r"^\{\{(\w+)\}\}$")
# Polices TrueType embarquées (DejaVu) : « » — ° € et accents garantis à l'impression.
FD = "/usr/share/fonts/truetype/dejavu/"
F = {"r": "DJr", "b": "DJb", "i": "DJi", "bi": "DJb"}
FFILE = {"r": FD + "DejaVuSans.ttf", "b": FD + "DejaVuSans-Bold.ttf", "i": FD + "DejaVuSerif.ttf", "bi": FD + "DejaVuSans-Bold.ttf"}
FONTS = {k: fitz.Font(fontfile=v) for k, v in FFILE.items()}
TOKEN = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*)")


def runs_of(text):
    """'a **b** c' -> [('a ', 'r'), ('b', 'b'), (' c', 'r')]"""
    text = text.replace("`", "")  # les spans `code` ne sont pas rendus : on retire les marqueurs
    out = []
    for part in TOKEN.split(text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**") and len(part) > 4:
            out.append((part[2:-2], "b"))
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            out.append((part[1:-1], "i"))
        else:
            out.append((part, "r"))
    return out


def wrap(runs, width, size):
    """Découpe des runs en lignes tenant dans `width` (mots non cassables)."""
    words = []
    for text, st in runs:
        chunks = re.split(r"(\s+)", text)
        for ch in chunks:
            if ch:
                words.append((ch, st))
    lines, cur, cur_w = [], [], 0.0
    for word, st in words:
        if word.isspace():
            if cur:
                cur.append((" ", st))
                cur_w += FONTS[st].text_length(" ", size)
            continue
        w = FONTS[st].text_length(word, size)
        if cur and cur_w + w > width:
            lines.append(cur)
            cur, cur_w = [(word, st)], w
        else:
            cur.append((word, st))
            cur_w += w
    if cur:
        lines.append(cur)
    return lines or [[]]


def tint(color, ratio=0.90):
    return tuple(c + (1 - c) * ratio for c in color)


class Pdf:
    def __init__(self, footer=""):
        self.doc = fitz.open()
        self.footer = footer
        self.accent = ACCENTS["commun"]
        self.accent_key = "commun"
        self._tab_open_at = None
        self.pages_colors = {}
        self.page = None
        self.y = 0.0
        self.new_page()

    def new_page(self):
        if self.page is not None:
            self._close_tab()
        self.page = self.doc.new_page(width=PAGE_W, height=PAGE_H)
        self._reg = set()
        self.y = self.top = MARGIN_T
        self._tab = None
        if self.footer:
            r = self.page.rect
            self.page.insert_text((MARGIN_L, r.height - 26), self.footer, fontname=self.font("r"), fontsize=7.4, color=(0.42, 0.42, 0.42))
            self.page.draw_line(fitz.Point(MARGIN_L, r.height - 34), fitz.Point(r.width - MARGIN_R, r.height - 34), width=0.4, color=(0.72, 0.72, 0.72))

    def set_accent(self, key):
        self._close_tab()
        self.accent = ACCENTS.get(key, ACCENTS["commun"])
        self.accent_key = key
        self._tab_open_at = self.y

    def _mark(self):
        if self.page is not None:
            self.pages_colors.setdefault(id(self.page), set()).add(self.accent_key)

    def _open_tab(self):
        if self._tab is None:
            self._tab = [self._tab_open_at if self._tab_open_at is not None else self.y, self.y, self.page]
            self._mark()

    def _close_tab(self):
        if getattr(self, "_tab", None):
            y0, y1, pg = self._tab
            if y1 - y0 > 2 and pg is not None:
                c = ACCENTS.get(getattr(self, "accent_key", "commun"), ACCENTS["commun"])[0]
                pg.draw_rect(fitz.Rect(30, y0, 34.5, y1), color=None, fill=c)
            self._tab = None

    def extend_tab(self):
        if self._tab:
            self._tab[1] = self.y
        else:
            self._open_tab()

    def font(self, st):
        key = F[st]
        if key not in self._reg:
            self.page.insert_font(fontname=key, fontfile=FFILE[st])
            self._reg.add(key)
        return key

    @property
    def avail(self):
        return PAGE_W - MARGIN_L - MARGIN_R

    def need(self, h, first=False):
        if self.y + h > PAGE_H - MARGIN_B and not first:
            self.new_page()

    def text(self, runs, size, x, lead, color=(0, 0, 0)):
        for line in wrap(runs, self.avail - (x - MARGIN_L), size):
            self.need(lead)
            cx = x
            for word, st in line:
                self.page.insert_text((cx, self.y + size * 0.80), word, fontname=self.font(st), fontsize=size, color=color)
                cx += FONTS[st].text_length(word, size)
            self.y += lead
            self.extend_tab()

    def rule(self, gap=5.0, color=(0.75, 0.75, 0.75)):
        self.need(gap * 2 + 2)
        self.page.draw_line(fitz.Point(MARGIN_L, self.y + gap), fitz.Point(PAGE_W - MARGIN_R, self.y + gap), width=0.6, color=color)
        self.y += gap * 2 + 2

    def table(self, rows):
        size = SMALL
        gap = 5.0
        ncol = max(len(r) for r in rows)
        rows = [(r + [""] * ncol)[:ncol] for r in rows]
        total, floor = [0.0] * ncol, [18.0] * ncol
        for r in rows:
            for c, cell in enumerate(r):
                words = [(t, st) for t, st in runs_of(cell)]
                total[c] += sum(FONTS[st].text_length(t + " ", size) for t, st in words)
                for part in re.split(r"[\s/]+", re.sub(r"\*+", "", cell)):
                    if part:
                        floor[c] = max(floor[c], FONTS["r"].text_length(part, size) + 1)
        inner = self.avail - gap * (ncol + 1)
        s = sum(total) or 1.0
        cw = [max(floor[c], inner * total[c] / s) for c in range(ncol)]
        if sum(cw) > inner:
            excess = sum(cw) - inner
            slack = [max(0.0, cw[c] - floor[c]) for c in range(ncol)]
            tot_slack = sum(slack) or 1.0
            cw = [cw[c] - excess * slack[c] / tot_slack for c in range(ncol)]
        xs, acc = [MARGIN_L + gap], 0.0
        for w in cw:
            acc += w + gap
            xs.append(MARGIN_L + acc)
        x_right = xs[-1] + gap

        def cells_of(row, bold=False):
            out = []
            for c, cell in enumerate(row):
                runs = [(t, "b" if bold else st) for t, st in runs_of(cell)]
                out.append(wrap(runs, cw[c], size))
            return out

        def row_h(cells):
            return max(len(x) for x in cells) * LEAD_S + 7.0

        def put(row, bold=False):
            cells = cells_of(row, bold)
            h = row_h(cells)
            top = self.y
            if bold:
                self.page.draw_rect(fitz.Rect(MARGIN_L, top, x_right, top + h), color=None, fill=(0.92, 0.93, 0.95))
            for c, lines in enumerate(cells):
                yy = top + 5.0
                for line in lines:
                    cx = xs[c]
                    for word, st in line:
                        self.page.insert_text((cx, yy + size * 0.80), word, fontname=self.font(st), fontsize=size)
                        cx += FONTS[st].text_length(word, size)
                    yy += LEAD_S
            self.page.draw_rect(fitz.Rect(MARGIN_L, top, x_right, top + h), color=(0.76, 0.76, 0.76), width=0.4)
            for c in range(1, ncol):
                self.page.draw_line(fitz.Point(xs[c] - gap / 2, top), fitz.Point(xs[c] - gap / 2, top + h), width=0.3, color=(0.82, 0.82, 0.82))
            self.y += h
            self.extend_tab()

        head, body = rows[0], rows[1:]
        self.need(row_h(cells_of(head, True)) + 34)
        put(head, bold=True)
        for r in body:
            if self.y + row_h(cells_of(r)) > PAGE_H - MARGIN_B:
                self.new_page()
                put(head, bold=True)
            put(r)
        self.y += 8.0

    def draw_ribbons(self, with_ribbon=True):
        self._close_tab()
        if not with_ribbon:
            return
        for pg, keys in self.pages_colors.items():
            page = None
            for cand in self.doc:
                if id(cand) == pg:
                    page = cand
                    break
            if page is None:
                continue
            x = MARGIN_L
            for k in ("commun", "bleu", "vert", "orange", "rouge"):
                if k in keys:
                    c = ACCENTS[k][0]
                    page.draw_rect(fitz.Rect(x, 30, x + 13, 34.5), color=None, fill=c)
                    x += 15.5

    def save(self, path):
        self.doc.save(path, deflate=True)


def render(md, out, footer=""):
    pdf = Pdf(footer)
    lines = md.replace("\r\n", "\n").split("\n")
    i, first_para = 0, True
    while i < len(lines):
        raw = lines[i]
        ln = raw.strip()
        if ln.startswith("<!--"):
            if ln == "<!--PDF-STOP-->":
                break
            if not ln.endswith("-->"):
                while i < len(lines) and "-->" not in lines[i]:
                    i += 1
            i += 1
            continue
        if not ln:
            pdf.y += 4.0
            i += 1
            continue
        m_dir = DIRECTIVE.match(ln)
        if m_dir:
            pdf.set_accent(m_dir.group(1))
            first_para = True
            i += 1
            continue
        if ln == "<<<":
            pdf.new_page()
            first_para = True
            i += 1
            continue
        if ln == "---":
            pdf.rule()
            i += 1
            continue
        if ln.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{2,}:?", c or "-") for c in cells):
                    rows.append(cells)
                i += 1
            if rows:
                pdf.table(rows)
            continue
        m = re.match(r"^(#{1,3})\s+(.*)$", ln)
        if m:
            lvl, txt = len(m.group(1)), m.group(2)
            size, lead, before = {1: (15.0, 18.0, 8.0), 2: (12.0, 15.0, 11.0), 3: (10.8, 14.0, 9.0)}[lvl]
            if lvl == 1 and not first_para and pdf.y - pdf.top > 2:
                pdf.new_page()
            pdf.y += before
            if lvl == 1:
                while size > 9.5 and FONTS["b"].text_length(re.sub(r"\*+", "", txt), size) > pdf.avail - 26:
                    size -= 0.5
                tl = ["".join(x[0] for x in ln).strip() for ln in wrap(runs_of(re.sub(r"\*+", "", txt)), pdf.avail - 30, size)]
                band = len(tl) * (size + 3.5) + 11
                pdf.need(band)
                pdf.page.draw_rect(fitz.Rect(MARGIN_L, pdf.y, PAGE_W - MARGIN_R, pdf.y + band), color=None, fill=pdf.accent[0])
                lab = pdf.accent[1]
                if FONTS["b"].text_length(lab, 7.2) < pdf.avail - FONTS["b"].text_length(max(tl, key=len), size) - 30:
                    pdf.page.insert_text((PAGE_W - MARGIN_R - FONTS["b"].text_length(lab, 7.2) - 8, pdf.y + band - 7), lab, fontname=pdf.font("b"), fontsize=7.2, color=(0.85, 0.88, 0.94))
                yy = pdf.y + size + 6
                for line in tl:
                    pdf.page.insert_text((MARGIN_L + 9, yy), line, fontname=pdf.font("b"), fontsize=size, color=(1, 1, 1))
                    yy += size + 3.5
                pdf.y += band + 4
            else:
                pdf.need(lead + 8)
                pdf.text(runs_of(txt), size, MARGIN_L, lead, color=pdf.accent[0])
                if lvl == 2:
                    pdf.page.draw_line(fitz.Point(MARGIN_L, pdf.y - 1), fitz.Point(PAGE_W - MARGIN_R, pdf.y - 1), width=0.9, color=pdf.accent[0])
                    pdf.y += 2
            first_para = False
            i += 1
            continue
        if ln.startswith(">"):
            block = []
            while i < len(lines) and (lines[i].strip().startswith(">") or not lines[i].strip()):
                s = lines[i].strip()
                if s.startswith(">"):
                    block.append(s[1:].strip())
                    i += 1
                elif not s:
                    if i + 1 < len(lines) and lines[i + 1].strip().startswith(">"):
                        block.append("")
                        i += 1
                    else:
                        break
                else:
                    break
            top = pdf.y
            for para in "\n".join(block).split("\n\n"):
                if para.strip():
                    pdf.text(runs_of(para.strip()), BODY, MARGIN_L + 14, LEAD)
                    pdf.y += 3.0
            pdf.page.draw_line(fitz.Point(MARGIN_L + 3, top - 2), fitz.Point(MARGIN_L + 3, pdf.y), width=1.6, color=(0.55, 0.60, 0.70))
            pdf.y += 6.0
            first_para = True
            continue
        if ln.startswith(("- ", "* ")):
            pdf.text([("–  ", "r")] + runs_of(ln[2:]), BODY, MARGIN_L + 12, LEAD)
            first_para = True
            i += 1
            continue
        if ln.startswith("*") and ln.endswith("*") and len(ln) > 2 and not ln.startswith("**"):
            pdf.text(runs_of(ln), SMALL, MARGIN_L, 11.6, color=(0.32, 0.32, 0.32))
            i += 1
            continue
        pdf.text(runs_of(ln), BODY, MARGIN_L, LEAD)
        pdf.y += 2.0
        first_para = False
        i += 1
    pdf.draw_ribbons()
    pdf.save(out)
    print(f"OK {out} — {len(pdf.doc)} page(s)")


if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    foot = sys.argv[3] if len(sys.argv) > 3 else ""
    render(open(src, encoding="utf-8").read(), dst, foot)
