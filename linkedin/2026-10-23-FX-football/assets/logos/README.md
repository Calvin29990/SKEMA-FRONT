# Où déposer les logos officiels

Dépose ici les écussons en PNG (fond transparent, 200–400 px) avec exactement ces noms,
puis relance `python build_post_clubs_v3.py` :

| fichier | club |
|---|---|
| `ol.png` | Olympique Lyonnais |
| `asm.png` | AS Monaco |
| `om.png` | Olympique de Marseille |
| `tfc.png` | Toulouse FC |
| `sdr.png` | Stade de Reims |
| `psg.png` | Paris Saint-Germain |
| `losc.png` | LOSC Lille |
| `rcl.png` | RC Lens |
| `srfc.png` | Stade Rennais FC |
| `ogcn.png` | OGC Nice |
| `rcsa.png` | RC Strasbourg Alsace |
| `pfc.png` | Paris FC |

Le script détecte automatiquement le fichier : si le logo est là, il remplace le monogramme.
Sinon il garde le monogramme aux couleurs du club — c'est le rendu actuel, volontairement
utilisable sans risque juridique.
