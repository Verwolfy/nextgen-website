# Lot BOND n° 4 — FENEK-BOND C2TE : sources, périmètre et vérifications

**Dossier de travail du 17 novembre 2026** · Destination : registre technique du dépôt, hors pages publiques. La désignation C2TE dans le catalogue n’est pas une preuve de conformité de la formulation FENEK ; les certifications et performances doivent être attestées séparément.

## Classe de référence EN 12004-1:2017

- **C2** : mortier-colle cimentaire de classe améliorée : adhérences en traction initiale, après eau, après chaleur et après gel/dégel **≥ 1,0 N/mm²** chacune.
- **T** : glissement vertical réduit à **≤ 0,5 mm** dans l’essai normatif.
- **E** : maintien d’une adhérence en traction **≥ 0,5 N/mm² après 30 minutes** de temps ouvert lors du test de classement ; le critère de temps ouvert standard reste **≥ 0,5 N/mm² après 20 minutes**.
- Pas de caractère **F** (prise rapide) ou **S1** (déformabilité) dans la désignation `C2TE`. Ne pas inférer leur présence.

Référence normative : [EN 12004-1:2017, description consultable](https://www.iteh.fr/catalog/standards/cen/48998e72-43b4-4ab9-9385-a9399c2c4689/en-12004-1-2017). La classification effective exige des résultats d’essais du laboratoire sur la formule finale.

## Trois fabricants et leurs données propres

| Fabricant / référence | Source et classe décrite | Exemples de valeurs fabricant (non transposables) |
| --- | --- | --- |
| **Sika** — SikaCeram-205 NG Grey (Nigeria) | [Page technique Sika Nigeria](https://nga.sika.com/en/construction/building-finishing/cementitious-tileadhesive/high-performancetileadhesivec2teclass/sikaceram-205-nggrey.html) — C2TE | Eau **5,5–6,0 L / 25 kg** ; temps ouvert ~**30 min à 20 °C** ; vie en pot ~**60 min à 30 °C** ; épaisseur **3–10 mm**, à considérer uniquement pour le produit Sika |
| **Mapei** — Adesilex P9 (Singapore) | [Fiche fabricant, édition 2025](https://cdnmedia.mapei.com/docs/librariesprovider52/products-documents/1_00102_adesilex-p9_en-sg_239753eba80c488db39837e281008913.pdf?sfvrsn=ce1afc04_0) — C2TE | Eau **29–31 %** en masse, soit **7,3–7,8 L/25 kg** ; temps ouvert **30 min** ; ajustement **45 min** ; consommation **2–5 kg/m²** selon peigne ; sol jointoyable après **24 h** ; données de marché régional |
| **Weber / Saint-Gobain** — weberset easy flex 218 (Malaisie) | [Page fabricant Weber](https://www.saint-gobain.my/products/weberset-easy-flex-218) — C2TE | Lit de collage **3–6 mm** ; préparation par surface maximale indicative de **1 m²** ; jointoiement **24 h** ; dosage d’eau non repris en l’absence de quantité vérifiée sur la page |
| **Sika** — SikaCeram-212 Non-Slip (Inde) | [Page technique Sika India](https://ind.sika.com/en/construction/tile-installationsystems/tile-adhesives/sikaceram-212-non-slip.html) — C2TE ; deuxième comparaison au sein du fabricant Sika | Eau gris **6,5–7 L/25 kg**, blanc **7–7,5 L/25 kg** ; temps ouvert **>30 min** ; ajustement ~**25 min à 27 °C** ; vie en pot **≥180 min à 27 °C** ; consommations simples **3–5,25 kg/m²** ; jointoiement sol **24–36 h** |

Les produits retenus sont des références indépendantes du produit FENEK et sont souvent vendus sur des marchés nationaux distincts. Les plages de consommation mélangent peignes et épaisseurs : elles ne peuvent pas être utilisées pour dimensionner les achats d’un chantier FENEK. Le **double encollage** est décrit comme une méthode à contrôler, sans nombre artificiel dérivé des valeurs de simple encollage.

## Implémentation

- `src/data/fenek-c2te-reference.ts` : 7 critères de classe, 6 repères comparatifs, textes FR/AR/EN.
- `src/components/FenekC2TEPilot.astro` : fiche Web et document A4, 4 rubriques, illustrations C2TE du catalogue validées par chemin et SHA, liens vers trois références voisines et demandes de contact.
- `src/pages/[lang]/documentation/[slug].astro` et `src/pages/[lang]/catalogue/[slug].astro` : affichage produit seulement pour le code `BOND-C2TE`, sans interférence avec les 46 autres fiches.
- `docs/INTERNE-validation-donnees.csv` : **58 lignes C2TE** de provenance individuelle et de synthèse avec statut interne `à valider par le fabricant/laboratoire`.
- `scripts/export_c1t_pdfs.py` : export hors réseau de 4 références × 3 langues = **12 PDF** à générer puis relire, jamais FT/FDS homologuées.

## Contraintes de publication

Le statut JSON `presentation_provisoire` et les deux booléens `certifie=false`, `commercialise=false` demeurent. Les contrôles `noindex` et formulaires de capture restent fermés. Conformément à la demande éditoriale, aucun paragraphe de fin récurrent sur les performances ou les seuils n’a été réintroduit dans la fiche ou son PDF ; la distinction technique apparaît dans les **intitulés des tableaux** et leurs données.
