# 50 questions : Excel avancé

Niveau visé : CDI junior. Ces questions sont originales. Les « pièges Maki » sont estimés à partir d'entraînements publics, et non à partir d'un test réel.

## Tableau de référence

Utilisez ce tableau pour les questions qui s'y réfèrent (feuille « Ventes », lignes 2 à 6) :

| | A | B | C |
|---|---|---|---|
| 1 | Produit | Région | Ventes |
| 2 | P1 | Paris | 100 |
| 3 | P2 | Lyon | 200 |
| 4 | P3 | Paris | 150 |
| 5 | P4 | Lille | 50 |
| 6 | P5 | Lyon | 300 |

Les questions sont numérotées de 1 à 50. Lisez l'énoncé en entier avant de répondre.

---

## Partie 1 : fonctions de base (1 à 10)

**1.** Quel est le résultat de =SOMME(C2:C6) ?
A) 700 B) 800 C) 850 D) 900
**Réponse : B.** 100 + 200 + 150 + 50 + 300 = 800.
**Piège Maki :** la ligne 1 contient des titres. Vérifiez que la plage commence bien à la ligne 2.

**2.** Quel est le résultat de =MOYENNE(C2:C6) ?
A) 140 B) 150 C) 160 D) 200
**Réponse : C.** 800 / 5 = 160.
**Piège Maki :** la moyenne divise par le nombre de cellules numériques, pas par un chiffre arbitraire.

**3.** Quel est le résultat de =MEDIANE(C2:C6) ?
A) 150 B) 160 C) 200 D) 300
**Réponse : A.** Valeurs triées : 50, 100, 150, 200, 300. La médiane est 150.
**Piège Maki :** la médiane n'est pas la moyenne. Triez toujours avant de lire la valeur centrale.

**4.** Quel est le résultat de =NB(C2:C6) ?
A) 0 B) 4 C) 5 D) 6
**Réponse : C.** Cinq cellules numériques.
**Piège Maki :** NB compte les nombres. NBVAL compte toutes les cellules non vides.

**5.** Quel est le résultat de =NBVAL(A2:A6) ?
A) 4 B) 5 C) 6 D) 0
**Réponse : B.** Cinq produits.
**Piège Maki :** ne confondez pas NBVAL (cellules non vides) et NB (valeurs numériques).

**6.** Quel est le résultat de =MAX(C2:C6)-MIN(C2:C6) ?
A) 200 B) 250 C) 300 D) 350
**Réponse : B.** 300 − 50 = 250.
**Piège Maki :** l'écart entre le maximum et le minimum n'est pas la moyenne des écarts.

**7.** Quel est le résultat de =SOMME(C2:C6)/COUNT(C2:C6) ?
A) 800 B) 160 C) 5 D) 150
**Réponse : B.** Cela revient à la moyenne.
**Piège Maki :** COUNT est en anglais, la version française est NB. Dans un test en français, utilisez NB.

**8.** Quel est le résultat de =ARRONDI(1234,5;-2) ?
A) 1 200 B) 1 230 C) 1 235 D) 1 300
**Réponse : A.** Avec des décimales égales à −2, l'arrondi se fait à la centaine : 1 234,5 → 1 200.
**Piège Maki :** les décimales négatives arrondissent à la centaine, pas aux dizaines.

**9.** Quel est le résultat de =ARRONDI.SUP(2,1;0) ?
A) 2 B) 3 C) 2,5 D) 2,1
**Réponse : B.** ARRONDI.SUP va toujours vers le haut.
**Piège Maki :** ARRONDI.INF va vers le bas, même pour 2,9.

**10.** Quel est le résultat de =MOD(17;5) ?
A) 3 B) 2 C) 3,4 D) 12
**Réponse : B.** 17 = 3 × 5 + 2, le reste est 2.
**Piège Maki :** MOD renvoie le reste, QUOTIENT renvoie la partie entière de la division (ici 3).

---

## Partie 2 : fonctions conditionnelles (11 à 20)

**11.** Quel est le résultat de =SOMME.SI(B2:B6;"Paris";C2:C6) ?
A) 100 B) 250 C) 300 D) 450
**Réponse : B.** 100 + 150 = 250.
**Piège Maki :** la plage de somme est en troisième argument, la plage de critère en premier.

**12.** Quel est le résultat de =NB.SI(C2:C6;">100") ?
A) 2 B) 3 C) 4 D) 5
**Réponse : B.** Valeurs supérieures à 100 : 200, 150, 300.
**Piège Maki :** 100 n'est pas strictement supérieur à 100. Il n'est pas compté.

**13.** Quel est le résultat de =MOYENNE.SI(B2:B6;"Lyon";C2:C6) ?
A) 200 B) 250 C) 300 D) 500
**Réponse : B.** (200 + 300) / 2 = 250.
**Piège Maki :** la moyenne conditionnelle ne divise pas par le total des lignes, seulement par le nombre de lignes retenues.

**14.** Quel est le résultat de =SOMME.SI.ENS(C2:C6;B2:B6;"Paris";C2:C6;">120") ?
A) 100 B) 150 C) 250 D) 300
**Réponse : B.** Parmi les lignes Paris, seule 150 est supérieure à 120.
**Piège Maki :** la première plage de l'argument SOMME.SI.ENS est la plage de somme, pas la première plage de critère.

**15.** Quel est le résultat de =NB.SI.ENS(B2:B6;"Lyon";C2:C6;">250") ?
A) 0 B) 1 C) 2 D) 3
**Réponse : B.** Seule la ligne 6 (Lyon, 300) remplit les deux critères.
**Piège Maki :** chaque couple plage/critère doit avoir la même taille.

**16.** Quel est le résultat de =SI(C3>=150;"OK";"KO") ?
A) OK B) KO C) VRAI D) 200
**Réponse : A.** C3 vaut 200, donc la condition est vraie.
**Piège Maki :** le résultat est un texte, pas un nombre. Il ne peut pas être sommé.

**17.** Quel est le résultat de =SI(ET(B2="Paris";C2>50);"Oui";"Non") ?
A) Oui B) Non C) VRAI D) 100
**Réponse : A.** B2 vaut Paris et C2 vaut 100, donc les deux conditions sont vraies.
**Piège Maki :** ET exige que toutes les conditions soient vraies. OU suffit qu'une seule le soit.

**18.** Quel est le résultat de =SI(OU(B6="Lille";C6>250);"A";"B") ?
A) A B) B C) VRAI D) 300
**Réponse : A.** C6 vaut 300, donc la condition C6>250 est vraie.
**Piège Maki :** avec OU, une seule condition vraie suffit.

**19.** Quel est le résultat de =SIERREUR(RECHERCHEV("P9";A2:C6;3;FAUX);0) ?
A) #N/A B) 0 C) P9 D) Vide
**Réponse : B.** P9 n'existe pas, la recherche renvoie une erreur, SIERREUR la remplace par 0.
**Piège Maki :** SIERREUR masque toutes les erreurs. Utilisez-la avec précaution pour ne pas cacher un vrai problème.

**20.** Quel est le résultat de =SI(C2>=100;"Haut";SI(C2>=50;"Moyen";"Bas")) pour C2=100 ?
A) Haut B) Moyen C) Bas D) 100
**Réponse : A.** 100 ≥ 100 est vrai.
**Piège Maki :** la borne est incluse avec >=. Avec > seul, 100 donnerait Moyen.

---

## Partie 3 : recherche (21 à 30)

**21.** Quel est le résultat de =RECHERCHEV("P4";A2:C6;3;FAUX) ?
A) P4 B) Lille C) 50 D) 300
**Réponse : C.** P4 est en ligne 5, la colonne 3 (Ventes) contient 50.
**Piège Maki :** le numéro de colonne est relatif à la plage (A2:C6), pas à la feuille.

**22.** Quel est le résultat de =RECHERCHEV("Lille";B2:C6;2;FAUX) ?
A) Lille B) 50 C) #N/A D) 4
**Réponse : B.** RECHERCHEV regarde toujours la première colonne de la plage, ici B (Régions). Lille est en B5. Le numéro de colonne 2 renvoie donc la colonne C de la même ligne, soit 50.
**Piège Maki :** la plage commence en B, donc la colonne 2 est C. Si vous croyez que la colonne 2 est B, vous répondez « Lille ». Ce n'est pas le cas ici.

**23.** Quel est le résultat de =INDEX(C2:C6;EQUIV("Lyon";B2:B6;0)) ?
A) 200 B) 300 C) 250 D) #N/A
**Réponse : A.** EQUIV renvoie la première position de Lyon (2), INDEX renvoie la 2e valeur de C : 200.
**Piège Maki :** EQUIV renvoie la première occurrence seulement.

**24.** Quel est le résultat de =EQUIV("Lille";B2:B6;0) ?
A) 3 B) 4 C) 5 D) 50
**Réponse : B.** Lille est en 4e position de la plage B2:B6.
**Piège Maki :** la position est relative à la plage choisie, pas à la ligne de la feuille (5).

**25.** Quel est le résultat de =INDEX(A2:A6;EQUIV(MAX(C2:C6);C2:C6;0)) ?
A) P2 B) P5 C) P4 D) P3
**Réponse : B.** Le maximum est 300, en 5e position, donc INDEX renvoie P5.
**Piège Maki :** on combine une recherche de valeur maximale et un index. C'est un schéma classique en épreuve.

**26.** Quel est le résultat de =RECHERCHEV("P1";A2:C6;2;FAUX)&" - "&RECHERCHEV("P1";A2:C6;3;FAUX) ?
A) P1 - 100 B) Paris - 100 C) Paris100 D) 100 - Paris
**Réponse : B.** Région de P1 (Paris), suivi de « - », puis les ventes de P1 (100).
**Piège Maki :** le & concatène du texte. Le nombre est converti en texte.

**27.** Quelle formule renvoie la région de P3 ?
A) =RECHERCHEV(B4;A2:C6;2;FAUX)
B) =RECHERCHEV("P3";A2:C6;2;FAUX)
C) =RECHERCHEV("P3";B2:C6;1;FAUX)
D) =RECHERCHEV("Paris";A2:C6;1;FAUX)
**Réponse : B.** P3 est dans la première colonne de A2:C6, et la région est en colonne 2.
**Piège Maki :** l'option A est fausse car B4 contient Paris, pas P3, et la recherche de texte est exacte.

**28.** Quel est le résultat de =RECHERCHEV("P2";A2:C6;3) (sans FAUX) ?
A) 200 B) Une valeur approchée, potentiellement fausse C) #N/A D) 300
**Réponse : B.** Sans FAUX, la recherche est approchée et suppose que la première colonne est triée. Ici elle ne l'est pas.
**Piège Maki :** l'absence de FAUX est la cause de beaucoup d'erreurs de formules. Mettez toujours FAUX pour une recherche exacte.

**29.** Quel est le résultat de =RECHERCHEV("P5";A2:C6;3;FAUX) ?
A) 300 B) 200 C) 50 D) Lyon
**Réponse : A.** P5 est en ligne 6, ventes 300.
**Piège Maki :** la réponse D est une région, qui est en colonne 2.

**30.** Quelle formule renvoie 200 (ventes de P2) à partir d'une recherche sur la colonne de droite ?
A) =INDEX(C2:C6;EQUIV("P2";A2:A6;0))
B) =INDEX(A2:A6;EQUIV("P2";C2:C6;0))
C) =RECHERCHEV("P2";C2:C6;1;FAUX)
D) =EQUIV("P2";C2:C6;0)
**Réponse : A.** EQUIV trouve P2 en position 2 de A2:A6, INDEX renvoie la 2e valeur de C.
**Piège Maki :** l'option B est fausse car on cherche P2 dans les ventes (C) au lieu des noms (A).

---

## Partie 4 : texte, dates, calculs (31 à 40)

**31.** Quel est le résultat de =GAUCHE("Deloitte";3) ?
A) Del B) Deloitte C) loi D) Dell
**Réponse : A.** GAUCHE renvoie les 3 premiers caractères.
**Piège Maki :** GAUCHE part du début, DROITE de la fin.

**32.** Quel est le résultat de =STXT("Consultant";3;4) ?
A) Cons B) nsul C) sult D) ulta
**Réponse : B.** STXT part du 3e caractère (n), et prend 4 caractères : n-s-u-l.
**Piège Maki :** le 1er argument est la chaîne, le 2e la position de départ, le 3e le nombre de caractères.

**33.** Quel est le résultat de =NBCAR("Lille") ?
A) 4 B) 5 C) 6 D) 0
**Réponse : B.** Cinq caractères.
**Piège Maki :** NBCAR compte les espaces aussi.

**34.** Quel est le résultat de =TEXTE(0,25;"0%") ?
A) 0,25 B) 25% C) 0,25% D) 25
**Réponse : B.** Le format % multiplie par 100 et ajoute le symbole.
**Piège Maki :** le résultat est du texte.

**35.** Dans une cellule, =DATE(2026;11;10)-DATE(2026;11;1) renvoie :
A) 9 B) 10 C) 1 D) 0
**Réponse : A.** Différence de 9 jours (de 1er au 10).
**Piège Maki :** la différence de dates donne un nombre de jours, pas une date. Pour compter jours inclus, ajoutez 1.

**36.** Quel est le résultat de =MOD(-7;3) ?
A) −1 B) 2 C) 1 D) −2
**Réponse : B.** Dans Excel, MOD prend le signe du diviseur. −7 = −3 × 3 + 2.
**Piège Maki :** dans d'autres langages, le résultat peut être −1. Excel renvoie 2.

**37.** Quel est le résultat de =ENT(-2,5) ?
A) −2 B) −3 C) 2 D) −2,5
**Réponse : B.** ENT renvoie l'entier inférieur, donc −3.
**Piège Maki :** ENT n'arrondit pas à l'entier le plus proche, il descend vers −∞.

**38.** Quel est le résultat de =PUISSANCE(2;5) ?
A) 10 B) 25 C) 32 D) 7
**Réponse : C.** 2^5 = 32.
**Piège Maki :** la puissance n'est pas une multiplication (2 × 5).

**39.** Quel est le résultat de =GRANDE.VALEUR(C2:C6;2) ?
A) 200 B) 300 C) 150 D) 100
**Réponse : A.** Deuxième plus grande valeur : 200.
**Piège Maki :** le 2e argument est le rang, pas une valeur.

**40.** Quel est le résultat de =RANG.EQ(C3;C2:C6;0) (C3 = 200) ?
A) 1 B) 2 C) 3 D) 5
**Réponse : B.** 300 est premier, donc 200 est deuxième.
**Piège Maki :** avec 0 en dernier argument, le rang est décroissant (1 = plus grande valeur).

---

## Partie 5 : TCD, mise en forme, raccourcis, cas pratiques (41 à 50)

**41.** Pour obtenir les ventes totales par région, quel outil utilisez-vous ?
A) Une mise en forme conditionnelle
B) Un tableau croisé dynamique
C) Un filtre seul
D) Un graphique en secteurs
**Réponse : B.** Le TCD regroupe et totalise sans formules.
**Piège Maki :** le filtre cache des lignes, il ne totalise pas.

**42.** Quel raccourci active le filtre automatique sur une plage ?
A) Ctrl + Maj + L B) Ctrl + L C) Alt + F D) F4
**Réponse : A.**
**Piège Maki :** F4 répète la dernière action ou alterne les références absolues.

**43.** Quel raccourci insère la date du jour ?
A) Ctrl + ; B) Ctrl + D C) Alt + = D) F2
**Réponse : A.**
**Piège Maki :** Ctrl + Maj + ; donne l'heure.

**44.** Quel raccourci insère la somme automatique ?
A) Alt + = B) Ctrl + S C) Ctrl + Maj + S D) Alt + Entrée
**Réponse : A.**
**Piège Maki :** Alt + = est un raccourci rapide, mais il ne remplace pas la vérification du périmètre.

**45.** Pour formater une cellule avec séparateur de milliers et deux décimales, quel raccourci ouvre la boîte de dialogue ?
A) Ctrl + 1 B) Ctrl + F C) Ctrl + P D) Alt + F1
**Réponse : A.**
**Piège Maki :** le format affiche la valeur, il ne change pas le calcul.

**46.** Dans une formule, quelle touche bascule une référence de A2 à $A$2 ?
A) F2 B) F4 C) F9 D) Maj + F4
**Réponse : B.**
**Piège Maki :** F9 recalcule la formule, F2 passe en mode édition.

**47.** Un tableau affiche #VALEUR!. Quelle est la cause la plus probable ?
A) Division par zéro
B) Un texte dans une opération arithmétique
C) Une référence supprimée
D) Une valeur introuvable
**Réponse : B.** #VALEUR! signale un type incorrect, par exemple un texte additionné à un nombre.
**Piège Maki :** #DIV/0! = division par zéro, #REF! = référence supprimée, #N/A = valeur introuvable.

**48.** Un dirigeant veut voir les ventes Paris et Lyon séparément dans un même tableau. Quelle option est la plus rapide ?
A) Filtrer chaque région et recopier le résultat
B) Un TCD avec Région en lignes et Ventes en valeurs
C) Trier les ventes croissantes
D) Une formule SI imbriquée sur chaque ligne
**Réponse : B.**
**Piège Maki :** le TCD actualise les valeurs quand les données changent, la recopie non.

**49.** Quel est le résultat de =SOMME.SI(B2:B6;"<>Lyon";C2:C6) ?
A) 800 B) 300 C) 450 D) 250
**Réponse : B.** Lignes hors Lyon : Paris (100 + 150) et Lille (50), soit 300.
**Piège Maki :** le critère "<>Lyon" exclut toutes les lignes Lyon. Oublier Lille (et compter 250) est une erreur fréquente.

**50.** Quel est le résultat de =SI(NBVAL(C2:C6)=5;"Complet";"Incomplet") ?
A) Complet B) Incomplet C) 5 D) VRAI
**Réponse : A.** Cinq cellules non vides.
**Piège Maki :** NBVAL compte aussi les textes. Pour compter uniquement les nombres, utilisez NB.
