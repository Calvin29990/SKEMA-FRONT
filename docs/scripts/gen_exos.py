#!/usr/bin/env python3
"""Génère les banques d'exercices (skema-training/memos/exos/*.md).

Tout ce qui est calculable (numérique, déductif, concentration, mailing) est
**généré** : les réponses proviennent du calcul, pas d'une recopie.
L'anglais et le verbal viennent de données relues (exos/en_data.py, exos/verbal_data.py).

Usage : python3 skema-training/scripts/gen_exos.py
"""
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
OUT = os.path.join(HERE, "..", "memos", "exos")
os.makedirs(OUT, exist_ok=True)

from exos.en_data import AIS, VOC, ORT          # noqa: E402
from exos.verbal_data import PASSAGES           # noqa: E402

L = ["A", "B", "C", "D"]


def fmt(x):
    """1200.0 -> 1200 ; 78.8 -> 78,8 (affichage français)."""
    t = f"{x:.1f}".rstrip("0").rstrip(".")
    return t.replace(".", ",") if "." in t else t


def opts(correct, distractors, rnd):
    """Mélange déterministe ; renvoie (lignes d'options, lettre correcte)."""
    pool = [correct] + list(distractors)
    seen, uniq = set(), []
    for p in pool:
        if p not in seen:
            seen.add(p)
            uniq.append(p)
    while len(uniq) < 4:                       # évite les doublons de libellé
        uniq.append(str(rnd.randint(2, 99)))
    rnd.shuffle(uniq)
    letter = L[uniq.index(correct)]
    return " · ".join(f"{L[i]}) {uniq[i]}" for i in range(4)), letter, uniq


def head(num, title, intro, sections):
    out = [f"# {num} — Exercices : {title}", "", intro, ""]
    out.append("> **Mode d'emploi :** cache la ligne « → » avec le pouce, réponds, vérifie, "
               "et **lis le piège même quand tu as juste** : c'est lui qui fait la différence. "
               "Chrono cible indiqué par section. Note tes erreurs et rejoue-les le lendemain.")
    out.append("")
    out.append("| Section | Items | Chrono cible |")
    out.append("|---|---|---|")
    for s in sections:
        out.append(f"| {s[0]} | {s[1]} | {s[2]} |")
    out.append("")
    return out


# ─────────────────────────────────────────── 01 ANGLAIS ───────────────────────────────────────────
def gen_anglais():
    rnd = random.Random(7)
    o = head("EX-01", "Anglais (3 sections)",
             "Entraînement volontaire **avant** le test : 3 sections comme le vrai test "
             "(Aisance · Vocabulaire · Orthographe), avec le piège de chaque item. "
             "Objectif : reconnaissance instantanée, zéro contresens.",
             [("A. Aisance / phrases", len(AIS), "≤ 15 s/item"),
              ("B. Vocabulaire par définition", len(VOC), "≤ 10 s/item"),
              ("C. Orthographe", len(ORT), "≤ 6 s/item")])

    o += ["---", "", "## A. Aisance / phrases — complète le trou", "",
          "*Piège général : les leurres sont des prépositions/français littéral. "
          "Ne traduis pas : retrouve l'expression figée.*", ""]
    for i, (s, good, dis, trap) in enumerate(AIS, 1):
        line, letter, _ = opts(good, dis, rnd)
        o += [f"**{i}.** {s}", f"{line}",
              f"→ **{letter}) {good}** — *Piège :* {trap}", ""]

    o += ["---", "", "## B. Vocabulaire — quel mot correspond à la définition ?", "",
          "*Piège général : les leurres ressemblent au mot cible (defer/infer/confer) ou en sont "
          "le contraire. Lis la définition en entier avant de choisir.*", ""]
    for i, (d, good, dis, trap) in enumerate(VOC, 1):
        line, letter, _ = opts(good, dis, rnd)
        o += [f"**{i}.** {d}", f"{line}",
              f"→ **{letter}) {good}** — *Piège :* {trap}", ""]

    o += ["---", "", "## C. Orthographe — quelle graphie est correcte ?", "",
          "*Piège général : consonnes doubles, voyelles inversées (ie/ei), « b » et « p » muets "
          "qui s'écrivent quand même.*", ""]
    for i, (good, bad1, bad2, trap) in enumerate(ORT, 1):
        pool = [good, bad1, bad2]
        rnd.shuffle(pool)
        letter = L[pool.index(good)]
        line = " · ".join(f"{L[k]}) {pool[k]}" for k in range(3))
        o += [f"**{i}.** {line}", f"→ **{letter}) {good}** — *Piège :* {trap}", ""]

    o += ["---", "", "## Comptage et seuil de réussite", "",
          f"- Total : **{len(AIS) + len(VOC) + len(ORT)} items** "
          f"(A {len(AIS)} · B {len(VOC)} · C {len(ORT)}).",
          "- Seuil visé : **≥ 95 %** en A et B, **≥ 98 %** en C (l'orthographe est binaire).",
          "- Toute erreur → copie l'item dans `english/en-3-fautes-de-base.md` (section « mes erreurs ») "
          "et rejoue-le à J+1, J+3, J+7.", ""]
    write("exos-01-anglais.md", o)
    return len(AIS) + len(VOC) + len(ORT)


# ─────────────────────────────────────────── 02 NUMÉRIQUE ───────────────────────────────────────────
def gen_numerique():
    rnd = random.Random(20251003)
    items = []

    def add(kind, q, data, correct, dis, trap, look):
        items.append((kind, q, data, correct, dis, trap, look))

    # ROE
    for i in range(13):
        eq = rnd.choice([420, 650, 750, 900, 1050, 1200, 1800, 2000, 2400, 3200, 4000, 5000])
        roe = rnd.choice([6.4, 7.5, 8.0, 9.2, 10.5, 11.8, 12.5, 14.2, 16.0, 18.6])
        ni = round(eq * roe / 100, 1)
        assets = round(eq * rnd.choice([1.8, 2.4, 3.2, 4.0, 5.5]), 1)
        rev = round(eq * rnd.choice([2.2, 3.0, 4.5, 6.0]), 1)
        add("ROE", "Quel est le ROE (return on equity) ?",
            f"Résultat net = {fmt(ni)} M€ · Capitaux propres = {fmt(eq)} M€ · "
            f"Actif total = {fmt(assets)} M€ · Chiffre d'affaires = {fmt(rev)} M€",
            f"{roe:.1f} %",
            [f"{ni / assets * 100:.1f} %", f"{ni / rev * 100:.1f} %", f"{roe * 10:.1f} %"],
            "le dénominateur est **les capitaux propres** : l'actif total et le CA sont des leurres "
            "placés exprès dans le texte.",
            "ligne « Capitaux propres / Shareholders' equity » (pas « Total assets »).")
    # Capitalisation
    for i in range(13):
        p = rnd.choice([12.4, 18.75, 24.5, 31.2, 45.6, 62.0, 88.5, 104.0])
        out_sh = rnd.choice([8.5, 12.0, 18.4, 24.0, 36.5, 52.0, 74.5, 96.0])
        iss = round(out_sh + rnd.choice([1.2, 2.5, 4.0, 6.5]), 1)
        auth = round(iss + rnd.choice([5.0, 10.0, 20.0, 40.0]), 1)
        add("Capitalisation", "Quelle est la capitalisation boursière ?",
            f"Cours = {p:.2f} € · Actions en circulation (outstanding) = {fmt(out_sh)} M · "
            f"Actions émises = {fmt(iss)} M · Actions autorisées = {fmt(auth)} M",
            f"{p * out_sh:,.0f} M€".replace(",", " "),
            [f"{p * iss:,.0f} M€".replace(",", " "), f"{p * auth:,.0f} M€".replace(",", " "),
             f"{p * out_sh / 1000:,.1f} Md€".replace(",", " ")],
            "seules les **outstanding** comptent ; « emitted/authorized » gonflent le résultat.",
            "ligne « shares outstanding » (pas authorized / issued).")
    # Effectifs
    for i in range(13):
        n0 = rnd.choice([1200, 1850, 2400, 3600, 5200, 6800, 9400, 12500])
        g = rnd.choice([4.0, 6.5, 8.0, 12.5, 15.0, 22.0])
        n1 = round(n0 * (1 + g / 100))
        add("Effectifs", "Combien d'employés l'année suivante ?",
            f"Effectif initial = {n0} · Croissance = +{g:.1f} %",
            f"{n1:,} employés".replace(",", " "),
            [f"{round(n0 * g / 100):,} employés".replace(",", " "),
             f"{n0:,} employés".replace(",", " "),
             f"{round(n0 * (1 - g / 100)):,} employés".replace(",", " ")],
            "le piège n°1 est de donner **l'augmentation** au lieu du nouvel effectif.",
            "l'effectif de départ, puis applique +g % (pas le chiffre de la hausse seul).")
    # Outlook
    for i in range(13):
        rev = rnd.choice([40, 65, 120, 180, 250, 400, 620])
        m = rnd.choice([8.0, 12.0, 15.0, 18.5, 22.0])
        g = rnd.choice([5.0, 7.5, 10.0, 14.0, 20.0])
        dprof = rev * m * g / 10000
        add("Outlook", "De combien le profit change-t-il ?",
            f"CA = {fmt(rev)} M€ · Marge = {m:.1f} % · Hausse du CA prévue = +{g:.1f} % (marge inchangée)",
            f"+{dprof:.2f} M€",
            [f"+{rev * g / 100:.2f} M€", f"+{rev * m / 100:.2f} M€", f"+{dprof * 10:.2f} M€"],
            "on te propose la hausse du **CA** ou le **niveau** du profit ; il faut la variation du profit.",
            "CA × marge = profit initial, puis profit × hausse du CA.")
    # Marge
    for i in range(13):
        rev = rnd.choice([180, 240, 320, 450, 600, 850, 1200])
        cost = round(rev * rnd.choice([0.62, 0.71, 0.78, 0.83, 0.88]), 1)
        mg = (rev - cost) / rev * 100
        add("Marge", "Quelle est la marge (en % du chiffre d'affaires) ?",
            f"CA = {fmt(rev)} M€ · Coûts = {fmt(cost)} M€",
            f"{mg:.1f} %",
            [f"{cost / rev * 100:.1f} %", f"{(rev - cost) / cost * 100:.1f} %",
             f"{100 - mg / 10:.1f} %"],
            "coûts/CA = le **complément** de la marge ; (CA−coûts)/coûts = le markup.",
            "(CA − coûts) ÷ CA, jamais ÷ coûts.")

    o = head("EX-02", "Numérique (raisonnement chiffré)",
             "65 items dans les 5 familles du test. Les chiffres changent à chaque item : "
             "c'est la **méthode** qu'il faut fixer, pas le résultat.",
             [("ROE", 13, "≤ 25 s"), ("Capitalisation", 13, "≤ 20 s"),
              ("Effectifs", 13, "≤ 20 s"), ("Outlook", 13, "≤ 25 s"), ("Marge", 13, "≤ 20 s")])
    kind = None
    n = 0
    for k, q, data, correct, dis, trap, look in items:
        if k != kind:
            kind = k
            n = 0
            o += ["---", "", f"## {k}", ""]
        n += 1
        line, letter, _ = opts(correct, dis, rnd)
        o += [f"**{n}.** {q}", f"*Données :* {data}", line,
              f"→ **{letter}) {correct}** — *Piège :* {trap}",
              f"*Où regarder :* {look}", ""]
    o += ["---", "", "## Seuil", "",
          "- Vise **≥ 85 %** et surtout **0 erreur de dénominateur** (ROE/marge) : "
          "c'est là que tu perds des points, pas sur le calcul.",
          "- Si tu calcules juste mais choisis mal : tu es tombé dans un leurre → relis la ligne « Où regarder ».", ""]
    write("exos-02-numerique.md", o)
    return len(items)


# ─────────────────────────────────────────── 03 VERBAL ───────────────────────────────────────────
def gen_verbal():
    o = head("EX-03", "Verbal (Vrai / Faux / On ne peut pas dire)",
             "10 textes × 6 affirmations = 60 items. **Règle d'or : ce qui n'est pas écrit n'existe pas.** "
             "Les calculs sur deux chiffres donnés sont autorisés ; les causes, dates et généralisations "
             "non écrites valent « On ne peut pas dire ».",
             [("10 textes", 60, "≤ 40 s/item (texte compris)")])
    LABEL = {"T": "VRAI", "F": "FAUX", "CS": "ON NE PEUT PAS DIRE"}
    n = 0
    for title, text, sts in PASSAGES:
        o += ["---", "", f"## Texte — {title}", "", text, ""]
        for st, ans, trap in sts:
            n += 1
            o += [f"**{n}.** {st}",
                  f"A) Vrai · B) Faux · C) On ne peut pas dire",
                  f"→ **{LABEL[ans]}** — *Piège :* {trap}", ""]
    o += ["---", "", "## Seuil", "",
          "- Vise **≥ 90 %**. Compte séparément tes erreurs **FAUX** (tu as contredit le texte) et "
          "**ON NE PEUT PAS DIRE** (tu as inventé une info) : les deux n'ont pas le même remède.",
          "- Erreur « CS raté » → tu as utilisé une connaissance du monde : interdite ici.", ""]
    write("exos-03-verbal.md", o)
    return n


# ─────────────────────────────────────────── 04 INDUCTIF ───────────────────────────────────────────
def gen_inductif():
    items = []

    # 25 suites numériques, 5 familles × 5
    for k in range(5):
        a, d = 4 + k, 3 + k
        t = [a + i * d for i in range(5)]
        items.append((t, t[-1] + d,
                      [t[-1] + 2 * d, t[-1] + d + 1, t[-1]],
                      "écart constant +" + str(d), "rejouer le dernier écart au lieu de le vérifier."))
    for k in range(5):
        t, x = [], 3 + k
        for _ in range(5):
            t.append(x)
            x *= 2
        items.append((t, t[-1] * 2, [t[-1] + t[-1] - t[-2], t[-1] * 3, t[-1] + 2],
                      "×2 à chaque pas", "ajouter la dernière différence au lieu de doubler."))
    for k in range(5):
        p, q = 2 + k, 5 + k
        t, x, i = [], 1, 0
        while len(t) < 5:
            t.append(x)
            x += p if i % 2 == 0 else q
            i += 1
        nxt = t[-1] + (p if (len(t) - 1) % 2 == 0 else q)
        items.append((t, nxt, [t[-1] + q, t[-1] + p + q, t[-1] + 1],
                      f"alternance +{p} / +{q}", "continuer la mauvaise branche de l'alternance."))
    for k in range(5):
        base = 1 + k
        t = [(base + i) ** 2 for i in range(5)]
        items.append((t, (base + 5) ** 2, [(base + 5) ** 2 - 5, (base + 5) ** 2 + 4, t[-1] + (t[-1] - t[-2])],
                      "carrés consécutifs", "prolonger l'écart arithmétique au lieu de voir les carrés."))
    for k in range(5):
        t = [2 + k, 3 + k]
        while len(t) < 5:
            t.append(t[-1] + t[-2])
        items.append((t, t[-1] + t[-2], [t[-1] * 2, t[-1] + t[-3], t[-1] + 3],
                      "somme des deux précédents (Fibonacci)", "doubler le dernier terme au lieu d'additionner les deux."))

    o = head("EX-04", "Inductif (suites et matrices)",
             "50 items : 25 suites numériques, 10 suites de lettres, 15 matrices 2×2. "
             "**Cherche toujours la règle avant de regarder les réponses proposées** — les options "
             "contiennent le résultat de la règle mal appliquée.",
             [("Suites numériques", 25, "≤ 20 s"), ("Suites de lettres", 10, "≤ 15 s"),
              ("Matrices 2×2", 15, "≤ 25 s")])

    o += ["---", "", "## A. Suites numériques — quel terme vient ensuite ?", ""]
    for i, (t, ans, dis, rule, trap) in enumerate(items, 1):
        line, letter, _ = opts(str(ans), [str(d) for d in dis], random.Random(i))
        o += [f"**{i}.** {' , '.join(str(x) for x in t)} , **?**", line,
              f"→ **{letter}) {ans}** — *Règle :* {rule}. *Piège :* {trap}", ""]

    LET = [
        ("A , C , E , G , **?**", "I", ["H", "J", "F"], "+2 dans l'alphabet", "compter +1 (H) au lieu de +2."),
        ("B , E , H , K , **?**", "N", ["M", "L", "O"], "+3 dans l'alphabet", "s'arrêter à M (+2)."),
        ("Z , X , V , T , **?**", "R", ["S", "Q", "P"], "−2 (alphabet à l'envers)", "revenir en arrière d'une seule lettre."),
        ("A , B , D , G , K , **?**", "P", ["O", "N", "Q"], "écarts +1 +2 +3 +4 +5", "répéter le dernier écart (+4 → O)."),
        ("C , F , I , L , **?**", "O", ["N", "M", "P"], "+3", "confondre la position et la lettre."),
        ("A , Z , B , Y , C , **?**", "X", ["W", "D", "Y"], "deux suites entrelacées (montante / descendante)",
         "suivre la mauvaise des deux suites."),
        ("M , N , P , S , W , **?**", "B", ["A", "Z", "C"], "écarts +1 +2 +3 +4 +5 (on boucle après Z)",
         "oublier que l'alphabet boucle après Z."),
        ("D , H , L , P , **?**", "T", ["S", "R", "U"], "+4", "compter les lettres et non les rangs."),
        ("T , S , Q , N , J , **?**", "E", ["F", "D", "G"], "écarts −1 −2 −3 −4 −5", "garder l'écart −4."),
        ("G , J , M , P , **?**", "S", ["R", "T", "Q"], "+3", "s'arrêter une lettre avant."),
    ]
    o += ["---", "", "## B. Suites de lettres", ""]
    for i, (q, ans, dis, rule, trap) in enumerate(LET, 1):
        line, letter, _ = opts(ans, dis, random.Random(100 + i))
        o += [f"**{i}.** {q}", line,
              f"→ **{letter}) {ans}** — *Règle :* {rule}. *Piège :* {trap}", ""]

    def grid(cells):
        return ("```\n"
                "┌──────┬──────┐\n"
                f"│  {cells[0]:<4}│  {cells[1]:<4}│\n"
                "├──────┼──────┤\n"
                f"│  {cells[2]:<4}│  {cells[3]:<4}│\n"
                "└──────┴──────┘\n```")

    GRID = [
        (["→", "↓", "←", "?"], "↑", ["→", "↓", "←"],
         "flèche tournée de 90° dans le sens horaire à chaque case",
         "lire en colonnes au lieu de lire en ligne : la rotation est continue → ← puis ↑."),
        (["●", "●●", "●●●", "?"], "●●●●", ["●●●●●", "●●", "●●●"],
         "nombre de points +1 par case", "confondre lignes et colonnes : ici on lit en ligne."),
        (["▲", "▼", "▲", "?"], "▼", ["▲", "◀", "●"],
         "alternance haut / bas", "chercher une rotation compliquée là où il y a une simple alternance."),
        (["■", "□", "■", "?"], "□", ["■", "▲", "●"],
         "alternance plein / vide", "oublier que la case 4 reprend l'état de la case 2."),
        (["◀", "▲", "▶", "?"], "▼", ["◀", "▲", "◀"],
         "rotation anti-horaire (gauche→haut→droite→bas)", "inverser le sens de rotation."),
        (["●", "○", "●", "?"], "○", ["●", "◐", "□"],
         "alternance noir / blanc", "répondre « noir » par habitude de la case 1."),
        (["1", "2", "4", "?"], "8", ["6", "7", "5"],
         "×2 à chaque case", "ajouter 2 (arithmétique) au lieu de doubler (géométrique)."),
        (["▲", "▲▼", "▲▼●", "?"], "▲▼●■", ["▲▼", "▲▼●●", "■●▼▲"],
         "on empile un symbole de plus à chaque case", "ne regarder que le dernier symbole ajouté."),
        (["→", "→", "↓", "?"], "↓", ["→", "←", "↑"],
         "le motif se répète par paires (2 cases identiques)", "poursuivre la rotation au lieu de voir la paire."),
        (["■", "■■", "■■■", "?"], "■■■■", ["■■■■■", "■■■", "■"],
         "+1 carré par case", "compter les symboles de la ligne du bas seulement."),
        (["●", "●●", "●", "?"], "●●", ["●", "●●●", "○"],
         "motif 1-2-1-2", "prolonger la croissance au lieu de voir l'aller-retour."),
        (["◀", "◀", "◀", "?"], "▶", ["◀", "▲", "▼"],
         "trois cases identiques puis inversion", "répéter le même symbole une 4e fois."),
        (["1", "3", "5", "?"], "7", ["6", "8", "9"],
         "nombres impairs (+2)", "prendre la suite des entiers."),
        (["▲", "■", "●", "?"], "▲", ["■", "●", "▼"],
         "cycle de 3 formes qui recommence", "chercher une progression alors que c'est un cycle."),
        (["○", "◐", "●", "?"], "○", ["◐", "●", "◑"],
         "remplissage progressif puis retour au départ", "continuer le remplissage (◑) au lieu de boucler."),
    ]
    o += ["---", "", "## C. Matrices 2×2 — quelle case remplace « ? » ?", ""]
    for i, (cells, ans, dis, rule, trap) in enumerate(GRID, 1):
        line, letter, _ = opts(ans, dis, random.Random(200 + i))
        o += [f"**{i}.**", grid(cells), line,
              f"→ **{letter}) {ans}** — *Règle :* {rule}. *Piège :* {trap}", ""]

    o += ["---", "", "## Seuil", "",
          "- Vise **≥ 80 %**. En dessous : tu cherches la règle trop tard. Écris d'abord la règle "
          "en 5 mots (« +3 », « ×2 », « rotation horaire »), puis réponds.", ""]
    write("exos-04-inductif.md", o)
    return len(items) + len(LET) + len(GRID)


# ─────────────────────────────────────────── 05 DÉDUCTIF ───────────────────────────────────────────
def gen_deductif():
    rnd = random.Random(31)
    items = []
    for i in range(17):
        T = rnd.choice([500, 750, 1000, 1500, 2500, 5000])
        above = rnd.random() < 0.5
        V = round(T * rnd.choice([1.2, 1.5, 2.0]), 0) if above else round(T * rnd.choice([0.4, 0.6, 0.8]), 0)
        n = 2 if above else 1
        items.append((
            f"Toute facture supérieure à {T:,} € doit porter **deux** signatures.".replace(",", " "),
            f"Une facture de {V:,.0f} € porte {n} signature(s).".replace(",", " "),
            "La facture a été autorisée correctement.",
            "VRAI" if (V > T) == (n == 2) else "FAUX",
            "compare le montant au seuil **avant** de regarder le nombre de signatures ; "
            "« supérieure à » exclut l'égalité."))
    for i in range(17):
        T = rnd.choice([500, 1000, 2000, 3000])
        above = rnd.random() < 0.5
        V = round(T * rnd.choice([1.3, 1.8]), 0) if above else round(T * rnd.choice([0.5, 0.7]), 0)
        items.append((
            f"Toute facture supérieure à {T:,} € doit être vérifiée par l'équipe finance.".replace(",", " "),
            f"Une facture de {V:,.0f} € porte deux signatures.".replace(",", " "),
            "Cette facture a été vérifiée par l'équipe finance.",
            "ON NE PEUT PAS DIRE",
            "les signatures ne sont **pas** la vérification finance : l'info manque, même si le seuil est dépassé."))
    for i in range(17):
        H = rnd.choice([11, 14, 16, 17])
        late = rnd.random() < 0.5
        h = H + rnd.choice([1, 2]) if late else H - rnd.choice([1, 2])
        items.append((
            f"Les commandes passées avant {H}:00 sont expédiées le jour même.",
            f"Une commande a été passée à {h}:00.",
            "La commande a été expédiée le jour même.",
            "FAUX" if late else "VRAI",
            "« avant 14:00 » = strictement avant : 14:00 pile n'est pas inclus."))
    for i in range(17):
        Y = rnd.choice([2, 3, 5])
        svc = Y + rnd.choice([1, 2]) if rnd.random() < 0.5 else max(1, Y - rnd.choice([1, 2]))
        items.append((
            f"Les salariés ayant plus de {Y} ans d'ancienneté peuvent postuler au programme.",
            f"Un salarié a {svc} ans d'ancienneté.",
            "Ce salarié peut postuler au programme.",
            "VRAI" if svc > Y else "FAUX",
            "« plus de 3 ans » exclut exactement 3 ans : lis l'inégalité, pas le chiffre."))

    o = head("EX-05", "Déductif (règle → cas)",
             "68 items : une règle, un cas, une affirmation. Tu n'as **aucune** connaissance à apporter : "
             "applique la règle mécaniquement. Le piège est toujours le même trio : seuil inclus/exclu, "
             "info manquante, règle partielle appliquée à un autre critère.",
             [("Seuil + action", 17, "≤ 20 s"), ("Seuil + info manquante", 17, "≤ 20 s"),
              ("Règle horaire", 17, "≤ 15 s"), ("Règle d'éligibilité", 17, "≤ 15 s")])
    n = 0
    for rule, case, st, ans, trap in items:
        n += 1
        o += [f"**{n}.**", f"*Règle :* {rule}", f"*Cas :* {case}",
              f"*Affirmation :* {st}",
              "A) Vrai · B) Faux · C) On ne peut pas dire",
              f"→ **{ans}** — *Piège :* {trap}", ""]
    o += ["---", "", "## Seuil", "",
          "- Vise **100 %** sur les 34 premiers items : la déduction pure ne souffre aucune erreur.",
          "- Les items « ON NE PEUT PAS DIRE » sont volontairement regroupés : entraîne-toi à les "
          "repérer (règle qui parle d'un critère **différent** de celui du cas).", ""]
    write("exos-05-deductif.md", o)
    return len(items)


# ─────────────────────────────────────────── 06 CONCENTRATION ───────────────────────────────────────────
def gen_concentration():
    rnd = random.Random(99)
    o = head("EX-06", "Concentration / attention",
             "50 items de comptage et de repérage. **Ne compte pas dans ta tête : pointe avec le doigt "
             "(ou le curseur) ligne par ligne.** La vitesse vient de la méthode, pas de la précipitation.",
             [("Comptage de lettres", 25, "≤ 15 s"), ("Lignes contenant un motif", 15, "≤ 20 s"),
              ("Repérage d'intrus", 10, "≤ 15 s")])

    def show(rows):
        return "```\n" + "\n".join("  ".join(rows[r][c] for c in range(len(rows[0])))
                                  for r in range(len(rows))) + "\n```"

    LETTERS = "QDPOBG"
    o += ["---", "", "## A. Comptage — combien de fois la lettre apparaît-elle ?", ""]
    n = 0
    for i in range(25):
        rows = [[rnd.choice(LETTERS) for _ in range(6)] for _ in range(6)]
        target = rnd.choice(LETTERS)
        cnt = sum(row.count(target) for row in rows)
        while cnt < 2 or cnt > 14:
            rows = [[rnd.choice(LETTERS) for _ in range(6)] for _ in range(6)]
            cnt = sum(row.count(target) for row in rows)
        n += 1
        dis = [cnt + 1, cnt - 1, cnt + 2]
        line, letter, _ = opts(str(cnt), [str(d) for d in dis if d > 0], rnd)
        o += [f"**{n}.** Combien de **{target}** ?", show(rows), line,
              f"→ **{letter}) {cnt}** — *Piège :* les leurres sont à ±1 : un oubli ou un double comptage "
              "suffit à te piéger. Compte **ligne par ligne**, jamais en diagonale.", ""]

    o += ["---", "", "## B. Combien de lignes contiennent au moins deux fois le symbole ?", ""]
    SYM = "●○■▲"
    for i in range(15):
        rows = [[rnd.choice(SYM) for _ in range(5)] for _ in range(5)]
        target = rnd.choice(SYM)
        cnt = sum(1 for row in rows if row.count(target) >= 2)
        n += 1
        dis = [cnt + 1, max(cnt - 1, 0), min(cnt + 2, 5)]
        line, letter, _ = opts(str(cnt), [str(d) for d in dis], rnd)
        o += [f"**{n}.** Lignes avec au moins **2 × {target}** :", show(rows), line,
              f"→ **{letter}) {cnt}** — *Piège :* on te demande des **lignes**, pas des occurrences : "
              "une ligne avec trois symboles ne compte qu'une fois.", ""]

    o += ["---", "", "## C. Intrus — quel symbole apparaît le moins souvent ?", ""]
    for i in range(10):
        pool = ["◆", "◇", "✦", "✧"]
        counts = {s: 0 for s in pool}
        rows = []
        for r in range(5):
            row = []
            for c in range(5):
                s = rnd.choice(pool)
                counts[s] += 1
                row.append(s)
            rows.append(row)
        odd = min(counts, key=lambda s: counts[s])
        if sum(1 for s in pool if counts[s] == counts[odd]) > 1:
            counts[odd] -= 0  # égalité improbable ; on garde min()
        n += 1
        dis = [s for s in pool if s != odd][:3]
        line, letter, _ = opts(odd, dis, rnd)
        o += [f"**{n}.** Quel symbole est le **moins fréquent** ?", show(rows), line,
              f"→ **{letter}) {odd}** ({counts[odd]} fois ; "
              + ", ".join(f"{s} = {counts[s]}" for s in pool if s != odd) + ") — "
              "*Piège :* ne te fie pas à l'impression visuelle : un symbole peut sembler rare "
              "parce qu'il est regroupé. Compte les quatre.", ""]

    o += ["---", "", "## Seuil", "",
          "- Vise **≥ 95 %** : ce test mesure la fiabilité, pas l'intelligence. "
          "Une erreur de comptage coûte autant qu'une question sautée.",
          "- Chronomètre-toi par bloc de 10 : la régularité (même temps sur chaque item) vaut mieux "
          "que des à-coups.", ""]
    write("exos-06-concentration.md", o)
    return n


# ─────────────────────────────────────────── 07 MAILING ───────────────────────────────────────────
P_HIGH = [
    ("atlas", lambda d: d > 2, "ATLAS envoyé il y a **plus de 2 jours**"),
    ("boreal_direct", lambda d: d > 5, "BOREAL adressé **directement** à M. Martin il y a **plus de 5 jours**"),
    ("cascade", lambda d: True, "tout ce qui concerne **CASCADE**"),
]
P_MED = [
    ("atlas", lambda d: d <= 2, "ATLAS envoyé dans les **2 derniers jours**"),
    ("boreal_direct", lambda d: d <= 5, "BOREAL direct dans les **5 derniers jours**"),
    ("support", lambda d: True, "adressé à **marketing.support@interlan.com**"),
]
ACTION = {
    "atlas": "FORWARD → **Keira Sanders**",
    "boreal_direct": "FORWARD → **Daniel Knowles**",
    "support": "envoyer un **accusé de réception**",
    "cascade": "**tu es personnellement responsable** (pas de transfert)",
    "other": "**rien** (pas de ton périmètre, non critique)",
    "other_crit": "FORWARD → **Walter Durenga** (ton manager)",
}


def prio(tag, days, crit):
    if crit:
        return "LOW", "other_crit", "critique mais **hors périmètre** : ni ATLAS/BOREAL/CASCADE ni support"
    for t, f, why in P_HIGH:
        if tag == t and f(days):
            return "HIGH", t, why
    for t, f, why in P_MED:
        if tag == t and f(days):
            return "MEDIUM", t, why
    return "LOW", "other", "aucune règle HIGH ni MEDIUM ne s'applique"


def gen_mailing():
    rnd = random.Random(555)
    FROM = {
        "atlas": ["Keira Sanders", "Walter Durenga", "ATLAS Project Office"],
        "boreal_direct": ["Daniel Knowles", "Walter Durenga", "BOREAL Coordination"],
        "cascade": ["Priya Raman", "Lena Fischer", "CASCADE Quality Team"],
        "support": ["marketing.support@interlan.com", "Trade Fair Office", "Newsletter Desk"],
        "other": ["Internal Audit", "Facilities", "Office Supplies Ltd"],
    }
    SUBJ = {
        "atlas": ["ATLAS — timeline", "ATLAS — budget note", "ATLAS — steering pack", "ATLAS — customer list"],
        "boreal_direct": ["BOREAL — annexes", "BOREAL — payment terms", "BOREAL — supplier list", "BOREAL — contract draft"],
        "cascade": ["CASCADE — test round", "CASCADE — sample labels", "CASCADE — customer complaint"],
        "support": ["Stand booking", "Newsletter request", "Delivery note", "Mailbox notice"],
        "other": ["Badge renewal", "Expense sample", "Canteen survey"],
    }
    TO = {"support": "marketing.support@interlan.com"}

    cases = []
    tags = ["atlas", "boreal_direct", "cascade", "support", "other"]
    for tag in tags:
        for days in [0, 1, 2, 3, 4, 5, 6, 7, 8, 10]:
            cases.append((tag, days, False))
    for _ in range(10):
        cases.append(("other", rnd.choice([0, 2, 3, 9, 12]), True))

    o = head("EX-07", "Mailing / traitement des e-mails",
             f"{len(cases)} e-mails à trier : priorité + action. Les règles sont celles du test, "
             "rappelées ci-dessous. **Lis toujours le destinataire avant l'expéditeur** : "
             "c'est lui qui décide pour la boîte support.",
             [("Cas à trier", len(cases), "≤ 20 s")])

    o += ["### Rappel des règles", "",
          "**HIGH** : ATLAS envoyé il y a **> 2 jours** · BOREAL envoyé **directement** à M. Martin il y a "
          "**> 5 jours** · tout e-mail **CASCADE**.",
          "**MEDIUM** : ATLAS dans les **2 derniers jours** · BOREAL direct dans les **5 derniers jours** · "
          "tout e-mail adressé à **marketing.support@interlan.com**.",
          "**LOW** : tout le reste.",
          "**Actions** : ATLAS → Keira Sanders · BOREAL → Daniel Knowles · support → accusé de réception · "
          "CASCADE → toi-même · critique mais hors de ton périmètre → Walter Durenga.", ""]

    n = 0
    for tag, days, crit in cases:
        n += 1
        p, act, why = prio(tag, days, crit)
        sender = rnd.choice(FROM[tag])
        subj = rnd.choice(SUBJ[tag])
        to = TO.get(tag, "tom.martin@interlan.com")
        o += [f"**{n}.** De : **{sender}** → À : **{to}** · reçu il y a **{days} jour(s)** · "
              f"Objet : *{subj}*" + (" · **critique**" if crit else ""),
              "Priorité : A) HIGH · B) MEDIUM · C) LOW — puis l'action.",
              f"→ **{p}** · Action : {ACTION[act]} — *Pourquoi :* {why}.",
              ""]
    o += ["---", "", "## Les 5 pièges qui coûtent le plus", "",
          "1. **CASCADE = toujours HIGH**, même reçu ce matin : la règle ne parle pas de délai.",
          "2. **2 jours / 5 jours sont des seuils** : « plus de 2 jours » exclut exactement 2 jours "
          "(→ MEDIUM), et « plus de 5 jours » exclut 5 jours.",
          "3. **support** se repère au **destinataire** (marketing.support@…), jamais à l'expéditeur.",
          "4. **CASCADE ne se transfère pas** : l'action est « tu es responsable », pas « forward ».",
          "5. Un e-mail **critique hors périmètre** n'est pas HIGH : il part chez **Durenga**, en LOW.", ""]
    write("exos-07-mailing.md", o)
    return n


def write(name, lines):
    p = os.path.join(OUT, name)
    with open(p, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"{name}: {len(lines)} lignes")


if __name__ == "__main__":
    tot = 0
    for fn in (gen_anglais, gen_numerique, gen_verbal, gen_inductif,
               gen_deductif, gen_concentration, gen_mailing):
        tot += fn()
    print(f"TOTAL items générés : {tot}")
