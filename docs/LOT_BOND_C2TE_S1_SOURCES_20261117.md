# Lot BOND n° 5 — FENEK-BOND C2TE-S1

**Date :** 17 novembre 2026 · Fiche informative FR/AR/EN. Sources des produits concurrents enregistrées dans `docs/INTERNE-validation-donnees.csv`. Aucun résultat de laboratoire FENEK n'est affirmé.

## Classe normative

Dans la désignation **C2TE-S1**, les critères EN 12004-1:2017 et les essais associés sont :

- C2 : adhérence en traction initiale et après eau, chaleur, gel/dégel, chaque fois ≥ 1,0 N/mm².
- T : glissement vertical ≤ 0,5 mm.
- E : adhérence en traction ≥ 0,5 N/mm² après 30 min de temps ouvert en laboratoire ; le critère normal à 20 min reste décrit.
- S1 : **déformation transversale ≥ 2,5 mm et < 5 mm**, et non S2. Source : [EN 12004-1:2017](https://www.iteh.fr/catalog/standards/cen/48998e72-43b4-4ab9-9385-a9399c2c4689/en-12004-1-2017), table de classement ; méthode d'essai EN 12004-2:2017.

## Vérification croisée des fabricants

| Comparable | Classe déclarée | Paramètres tirés du fabricant | Source |
| --- | --- | --- | --- |
| **SikaCeram-288 MY** (Malaisie) | C2TE S1 | eau 5,75–6,5 L/25 kg ; déformation S1 ; résistance C2 ; temps ouvert voisin de 30 min | [Sika](https://mys.sika.com/en/construction/tile-setting/tile-adhesives/sikaceram-288-my.html) |
| **Mapei Keraflex Maxi S1 Zero** (FT anglaise) | C2TE S1 | eau 29–31 % masse, soit 7,25–7,75 L/25 kg en conversion ; vie en pot >8 h à +23°C ; jointoiement mural 4–8 h | [Mapei FT](https://cdnmedia.mapei.com/docs/librariesprovider27/products-documents/1_keraflex-maxi-s1-zero_tds_en_750c3273df01499babe75f0a024e0f26.pdf?sfvrsn=2496ee9_0) |
| **Weber weberset SPF** (Royaume-Uni) | C2TE-S1 | mortier à prise normale ; compatible avec les sols chauffants et certaines préparations de supports déformables suivant système Weber | [Weber](https://www.uk.weber/weberset-spf) |

Les doses d'eau, durées et rendements sont des références documentaires de **formulations tierces**, jamais des prescriptions applicables à FENEK. Il n'y a ni classe F ni S2 implicite. La déformabilité S1 ne supprime jamais le besoin de joints de mouvement.

## Travaux intégrés

- `src/data/fenek-c2tes1-reference.ts` : 8 critères de classe (dont S1) et 6 repères, localisés.
- `src/components/FenekC2TES1Pilot.astro` : fiche dédiée, tableaux, guide illustré, impression A4 et liens.
- `src/pages/[lang]/documentation/[slug].astro` et `src/pages/[lang]/catalogue/[slug].astro` : raccordement localisé.
- `scripts/export_c1t_pdfs.py` : désormais 5 pilotes × 3 langues = **15 feuilles PDF** exportables localement à partir de l'Astro construit.
- `tests/c2tes1_pilot.test.mjs` et contrôles navigateur : tests de régression, médias et sorties PDF.

Maintien du **noindex** global, des protections API et des statuts internes `certifie:false`, `commercialise:false`, `statut:presentation_provisoire`. Le paragraphe répétitif supprimé à la demande du client n'est pas réintroduit.
