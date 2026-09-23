#!/usr/bin/env python3
"""
Prépare un gros PDF pour la traduction automatique gratuite.

DeepL et Google Traduction refusent les fichiers trop gros. Le Hull en fait
892 pages : il faut le découper. Ce script produit des morceaux qui passent.

    python3 tools/pdf_prep_traduction.py hull.pdf --out morceaux/

Options utiles :
    --chapitres 4 5 7 11 15 19 20   n'extrait que ces chapitres (voir --sommaire)
    --pages 88-130                   extrait une plage de pages
    --taille 9                       taille max d'un morceau en Mo (défaut 9)
    --sommaire                       affiche les signets du PDF et sort

Dépendance :  pip install --break-system-packages pypdf
"""
import argparse
import os
import sys

try:
    from pypdf import PdfReader, PdfWriter
except ImportError:
    sys.exit(
        "pypdf manquant. Installe-le avec :\n"
        "    pip install --break-system-packages pypdf"
    )

MO = 1024 * 1024


def lire_signets(reader):
    """Retourne [(titre, page0), ...] a plat, dans l'ordre du document."""
    plats = []

    def descendre(noeuds):
        for n in noeuds:
            if isinstance(n, list):
                descendre(n)
            else:
                try:
                    plats.append((n.title.strip(), reader.get_destination_page_number(n)))
                except Exception:
                    pass

    try:
        descendre(reader.outline)
    except Exception:
        pass
    return plats


def poids_pages(reader, pages):
    """Estime le poids d'une selection en l'ecrivant en memoire."""
    import io

    w = PdfWriter()
    for p in pages:
        w.add_page(reader.pages[p])
    buf = io.BytesIO()
    w.write(buf)
    return buf.tell()


def ecrire(reader, pages, chemin):
    w = PdfWriter()
    for p in pages:
        w.add_page(reader.pages[p])
    with open(chemin, "wb") as f:
        w.write(f)
    return os.path.getsize(chemin)


def decouper(reader, pages, limite):
    """Coupe la liste de pages en blocs qui tiennent sous la limite d'octets.

    On estime d'abord un nombre de pages par bloc a partir d'un echantillon,
    puis on verifie chaque bloc pour de vrai et on le redivise s'il deborde.
    Peser un PDF coute cher : on evite de le faire a chaque page.
    """
    # 1. estimation sur un echantillon de 20 pages (ou moins)
    ech = pages[: min(20, len(pages))]
    poids_ech = poids_pages(reader, ech)
    par_page = max(poids_ech / len(ech), 1)
    n = max(int(limite / par_page), 1)

    # 2. blocs provisoires
    blocs = [pages[i:i + n] for i in range(0, len(pages), n)]

    # 3. verification reelle, on redivise ce qui deborde encore
    finaux = []
    for bloc in blocs:
        while bloc and poids_pages(reader, bloc) > limite and len(bloc) > 1:
            moitie = len(bloc) // 2
            finaux.append(bloc[:moitie])
            bloc = bloc[moitie:]
        if bloc:
            finaux.append(bloc)

    # 4. un bloc redivise peut etre bien plus petit que la limite, on recolle
    fusionnes = []
    for bloc in finaux:
        if fusionnes and poids_pages(reader, fusionnes[-1] + bloc) <= limite:
            fusionnes[-1] = fusionnes[-1] + bloc
        else:
            fusionnes.append(bloc)
    return fusionnes


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf", help="le PDF a preparer")
    ap.add_argument("--out", default="morceaux", help="dossier de sortie")
    ap.add_argument("--taille", type=float, default=9.0, help="Mo max par morceau")
    ap.add_argument("--pages", help="plage de pages, ex 88-130")
    ap.add_argument("--chapitres", nargs="+", help="numeros de chapitres a extraire")
    ap.add_argument("--sommaire", action="store_true", help="liste les signets et sort")
    a = ap.parse_args()

    if not os.path.exists(a.pdf):
        sys.exit(f"Fichier introuvable : {a.pdf}")

    reader = PdfReader(a.pdf)
    if reader.is_encrypted:
        try:
            reader.decrypt("")
        except Exception:
            sys.exit(
                "PDF protege par DRM. Un fichier VitalSource ou Adobe DE ne peut\n"
                "pas etre traite : lis-le dans l'application de l'editeur."
            )

    total = len(reader.pages)
    signets = lire_signets(reader)

    if a.sommaire:
        if not signets:
            print("Aucun signet dans ce PDF (probablement un scan).")
        for titre, page in signets:
            print(f"  p.{page + 1:<5} {titre}")
        print(f"\n{total} pages au total.")
        return

    # --- selection des pages -------------------------------------------------
    if a.pages:
        d, _, f = a.pages.partition("-")
        pages = list(range(int(d) - 1, min(int(f or d), total)))
        etiquette = f"pages-{a.pages}"
    elif a.chapitres:
        if not signets:
            sys.exit("Pas de signets : utilise --pages a la place.")
        pages, trouves = [], []
        for num in a.chapitres:
            debut = None
            for i, (titre, page) in enumerate(signets):
                mots = titre.replace(".", " ").split()
                if mots and mots[0].lstrip("Chapitre").strip() == num or (
                    len(mots) > 1 and mots[0].lower().startswith("chap") and mots[1] == num
                ):
                    debut = page
                    fin = signets[i + 1][1] if i + 1 < len(signets) else total
                    break
            if debut is None:
                print(f"  ! chapitre {num} introuvable dans les signets")
                continue
            pages += list(range(debut, fin))
            trouves.append(num)
        if not pages:
            sys.exit("Aucun chapitre trouve. Lance --sommaire pour voir les titres.")
        etiquette = "ch" + "-".join(trouves)
    else:
        pages = list(range(total))
        etiquette = "complet"

    pages = sorted(set(pages))
    os.makedirs(a.out, exist_ok=True)
    limite = int(a.taille * MO)

    print(f"Source      : {a.pdf}  ({total} pages, {os.path.getsize(a.pdf) / MO:.1f} Mo)")
    print(f"Selection   : {len(pages)} pages  [{etiquette}]")
    print(f"Limite      : {a.taille} Mo par morceau\n")

    blocs = decouper(reader, pages, limite)
    base = os.path.splitext(os.path.basename(a.pdf))[0]

    for i, bloc in enumerate(blocs, 1):
        nom = f"{base}_{etiquette}_{i:02d}.pdf"
        chemin = os.path.join(a.out, nom)
        poids = ecrire(reader, bloc, chemin)
        print(f"  {nom}   p.{bloc[0] + 1}-{bloc[-1] + 1}   {poids / MO:.1f} Mo")

    print(f"\n{len(blocs)} morceau(x) dans {a.out}/")
    print("\nEnvoie-les un par un sur https://www.deepl.com/translator/files")
    print("(5 fichiers par mois en gratuit) ou https://translate.google.com/?op=docs")
    print("(illimite, qualite moindre, mise en page souvent cassee).")


if __name__ == "__main__":
    main()
