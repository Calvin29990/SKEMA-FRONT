# -*- coding: utf-8 -*-
"""06_entonnoir_acquisition.py — ENTONNOIR D'ACQUISITION FX (besoin canaux, 21/10/2026)
Layout déterministe : hauteur de chaque bande = max(colonne gauche, colonne droite).
Sorties : candidatures/CARTE-2026-10-21-entonnoir-acquisition-FX.png + .pdf"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

plt.rcParams.update({'font.family':'DejaVu Sans','text.color':'#1a1a1a'})
LAYERC='#2456a0'
XLIM=1.65

BANDS=[
 ("CLIENT FINAL",["PME/ETI export — marché adressable : 64 646 ≥ 5 M€ + 2,3 M < 5 M€ (Orbis)"],
  [],'#dcebe3'),
 ("CFO / DAF\nEXTERNALISÉ",["décideur interne · les DAF à temps","partagé prescrivent à leurs portefeuilles"],
  [('B',"Acting (réseau FR de DAF externalisés) → iBanFirst — écosystème affiché")],'#eef3f9'),
 ("EXPERT-COMPTABLE /\nFIDUCIAIRE",["prescripteur n°1 des PME — maillon quasi-vide ;","le canal passe par leurs OUTILS"],
  [('A',"Pennylane (plateforme des cabinets) → Airwallex — intégration native, bilatérale, 10/02/2026"),
   ('A',"Apporteurs commissionnés : programmes iBanFirst (dashboard) et Ebury (affiliation)"),
   ('B',"Libeo → Wise (02/2022, churn à revérifier) · fiduciaires → Amnis (CH) · Sage/Cegid = VIDE")],'#eef3f9'),
 ("ERP · COMPTA · E-COM",["là où le client travaille chaque jour —","marketplace d’apps = réassurance"],
  [('A',"NetSuite SuiteApp « Built for NetSuite » (18/10/2018) → Ebury — payer 130+ devises depuis l’ERP"),
   ('A',"Dynamics 365 via SKsoft (26/08/2025) → Corpay · Shopify App Store (21/07/2022) → Airwallex"),
   ('B',"Octopia/Cdiscount (répertoire bilatéral) → iBanFirst · AbbeyCross marketplace → Corpay"),
   ('C',"Xero/QuickBooks/Sage/… : bibliothèques d’intégrations (Ebury 30+, Moneycorp 29/08/2025)")],'#eef3f9'),
 ("TMS TRÉSORERIE",["le bureau du trésorier — celui qui possède","le TMS possède le flux"],
  [('A',"GTreasury (02/08/2023) → Convera · Cobase → Ebury (cotations + trades in-platform)"),
   ('A',"Agicap (TMS PME français, 06/2024) → iBanFirst"),
   ('X',"Kyriba : 0 FX tiers (capacité propre « Advanced FX » : Circle, JPM AM) · TIS verrouillé par StoneX")],'#eef3f9'),
 ("BANQUES & COURTIERS",["distribution captive, API ou white-label","= volume garanti sans prospection"],
  [('A',"BPCE apps (06/2018, ~15 M clients) → Wise · N26 / Swan → Wise"),
   ('A',"La Banque Postale (01/04/2021) → Ebury · Mondial Change white-label → Ebury (canal captif)"),
   ('A',"BNP Paribas Centric (10/09/2019, EMEA) → Kantox — canal captif du groupe"),
   ('A',"Citi / Silicon Valley Bank → Kantox (US) · Bank WIR → Amnis (CH)")],'#eef3f9'),
 ("ÉTAT / EXPORT",["le prescripteur institutionnel — Bpifrance est","LE nœud ; CCI-Business France routent vers lui"],
  [('A',"Bpifrance crédits export multidevises (18/02/2025) → iBanFirst"),
   ('A',"Plateforme cotation en ligne (27/09/2017) → relayée par iBanFirst ET Kantox — l’État distribue les deux"),
   ('A',"UFCC (fédération distributeurs chimie, ~100 adhérents import/export) → Kantox — canal caché")],'#eef3f9'),
 ("FINTECH FX — EXÉCUTION",["les rails décident déjà : Convera (150 partenaires, 18 Md$/an)","· Nium (Circle/Coinbase) · Wise Platform (Swift, 90+ banques)","· Currencycloud/Visa (Revolut, Starling)"],
  [],'#fdf1f0'),
]
VERDICT=("VERDICT — meilleur réseau de distribution corporate FX en France",
 ["1° Multiplicité vente indirecte : EBURY (banque + courtier captif + affiliés commissionnés + SuiteApp + réseaux business) — le plus de maillons tenus.",
  "2° Verrouillage : KANTOX-BNPP (canal captif ETI/EMEA) · WISE = distribution de MASSE retail (BPCE, N26, Swan) — pas du mid-market corporate.",
  "3° Pivot institutionnel : iBANFIRST (État × 2 canaux + Octopia + Agicap) · Invisible n°1 : CONVERA (18 Md$/an) · Menace : AIRWALLEX (Pennylane).",
  "→ Fenêtre ouverte : les experts-comptables traditionnels (Sage/Cegid, fiduciaires FR) ne sont tenus par PERSONNE — Pennylane y a déjà pris l'avance pour Airwallex."])

LL, SL, CL, GAP, PAD = 0.027, 0.022, 0.028, 0.014, 0.020   # hauteurs de ligne
H_HEAD=0.082; H_VER=0.030+0.034+len(VERDICT[1])*0.026+0.014  # titre + bandeau verdict

# hauteur de chaque bande
heights=[]
for label,sub,cells,fc in BANDS:
    nl=label.count('\n')+1
    left=nl*LL+len(sub)*SL+PAD
    right=(len(cells)*CL+0.012) if cells else 0.0
    heights.append(max(left,right,0.062))
T=sum(heights)+GAP*(len(BANDS)-1)
YLIM=H_HEAD+T+0.010+H_VER+0.016
fig=plt.figure(figsize=(16.54,16.54*YLIM/XLIM), dpi=150)
ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,XLIM); ax.set_ylim(0,YLIM); ax.axis('off')

ax.text(0.03,YLIM-0.032,"ENTONNOIR D'ACQUISITION FX CORPORATE — QUI PRESCRIT AU CLIENT ?",fontsize=17,fontweight='bold')
ax.text(0.03,YLIM-0.062,"Sources : feuille CANAUX-ACQUISITION (A = génère directement des clients · B = opportunités indirectes · C = techno sans preuve d'apport · ✗ = non retenu) — 21/10/2026",fontsize=9.5,color='#444')

ytop=YLIM-H_HEAD
for (label,sub,cells,fc),h in zip(BANDS,heights):
    y0=ytop-h
    ax.add_patch(FancyBboxPatch((0.03,y0),0.30,h,boxstyle='round,pad=0.004',fc=fc,ec='#9aa2ab',lw=1.2))
    ax.text(0.045,y0+h-0.014,label,fontsize=12.5,fontweight='bold',va='top',linespacing=1.1)
    nl=label.count('\n')+1
    for i,s in enumerate(sub):
        ax.text(0.045,y0+h-0.014-nl*LL-0.004-i*SL,s,fontsize=7.8,color='#444',va='top')
    for i,(cl,txt) in enumerate(cells):
        yc=y0+h-0.030-i*CL
        ax.text(0.36,yc,f"[{'✗' if cl=='X' else cl}]  {txt}",fontsize=9.2,va='top',
                color=('#1a1a1a' if cl=='A' else '#444' if cl=='B' else '#666' if cl=='C' else '#c0392b'),
                fontweight=('bold' if cl=='A' else 'normal'))
    ax.add_patch(FancyArrowPatch((0.185,y0-0.002),(0.185,y0-GAP+0.004),arrowstyle='-|>',mutation_scale=15,color=LAYERC,lw=1.5))
    ytop=y0-GAP

vy0=0.014; vh=H_VER
ax.add_patch(FancyBboxPatch((0.03,vy0),XLIM-0.06,vh,boxstyle='round,pad=0.005',fc='#fff8e6',ec='#d98e04',lw=1.6))
ax.text(0.045,vy0+vh-0.016,VERDICT[0],fontsize=12.5,fontweight='bold',va='top')
for i,t in enumerate(VERDICT[1]):
    ax.text(0.045,vy0+vh-0.052-i*0.026,t,fontsize=9.4,va='top',
            fontweight=('bold' if i==3 else 'normal'),color=('#8a5a00' if i==3 else '#1a1a1a'))

plt.savefig('candidatures/CARTE-2026-10-21-entonnoir-acquisition-FX.png')
plt.savefig('candidatures/CARTE-2026-10-21-entonnoir-acquisition-FX.pdf')
print('YLIM =',round(YLIM,3),'| fin bandes =',round(ytop+GAP,3),'| haut verdict =',round(vy0+vh,3))
