# Lot 57 — Qualification des sept kits FENEK-PROOF

Date : 4 novembre 2026. Dernière base vérifiée : `main` au commit `9a111c7ca20a959d2e107719d89583ae9e80f649` (lot 56).

## Résultat de l'audit

**Aucune composition, contenance ou masse nette FENEK n'a été confirmée pour les sept références ci-dessous.** Le catalogue affiche actuellement « Kit résine - Contacter nous pour plus d'informations » pour chacune, et le registre interne marque `format_nominal=NON CONFIRMÉ` et `validation_production_emballage=EN ATTENTE`.

| Code FENEK | Famille de produit | Sources comparatives dans les archives PDF transmises | Langues des analogues | État du conditionnement FENEK |
|---|---|---|---|---|
| PROOF-CM-O2P | Système d'étanchéité cimentaire | MEDACIM STA ; GRANIPROT MORTIER E | FR/EN/AR | Non confirmé |
| PROOF-EP-ANC | Résine de scellement / ancrage | MEDAPOXY AN ; MEDAPOXY REP | FR/EN/AR | Non confirmé |
| PROOF-EP-INJ | Résine d'injection | MEDAPOXY INJECT 812 | FR/EN/AR | Non confirmé |
| PROOF-EP-PRIM | Primaire époxy | MEDAPOXY PRIMER ; MEDAPOXY PRIMER AC | FR/EN/AR | Non confirmé |
| PROOF-EP-SB | Résine de collage | MEDAPOXY COLLE | FR/EN/AR | Non confirmé |
| PROOF-EP-SR | Revêtement de sol époxy | MEDAPOXY SOL HRC ; MEDAPOXY SOL FM AP | FR/EN/AR | Non confirmé |
| PROOF-PU-INJ | Injection polyuréthane | Aucun analogue suffisamment pertinent trouvé | Aucun | Non confirmé |

Attention : les PDF mentionnés sont des fiches de **fabricants tiers**. Ils servent à identifier les thèmes et les questions documentaires, pas à prouver la composition, le dosage, le volume, le poids ou la classe du produit FENEK. La présence d'une catégorie « kit résine » dans le catalogue est une hypothèse éditoriale, **pas une validation industrielle**.

## Informations à obtenir, par référence

1. Emballage réel : kit A+B, sac + bidon, seau, cartouche, bidon ou autre (ne pas supposer que tous sont bicomposants).
2. Masse nette ou volume nominal **par composant**, avec unités ; poids/volume total commercial.
3. Nombre de composants et méthode de regroupement/vente ; ratio de mélange **seulement** s'il existe une fiche de formulation approuvée.
4. Pour la fiche technique officielle : composition réelle, essais et valeurs vérifiées ; pour la FDS : validation HSE indépendante.
5. Une éventuelle matière d'emballage ne doit pas être inférée de sa forme.

## Ordre de confirmation utilisateur (une question à la fois)

1. PROOF-CM-O2P — conditionnement réel et contenance.
2. PROOF-EP-ANC — conditionnement réel et contenance.
3. PROOF-EP-INJ — conditionnement réel et contenance.
4. PROOF-EP-PRIM — conditionnement réel et contenance.
5. PROOF-EP-SB — conditionnement réel et contenance.
6. PROOF-EP-SR — conditionnement réel et contenance.
7. PROOF-PU-INJ — conditionnement réel et contenance.

Commencer par **FENEK-PROOF CM-O2P**. Demander quel est son emballage et le contenu net de chacun des composants, **s'il comporte plusieurs composants**.

## État des autres références

- BOND (16) : sac unique 25 kg, confirmé.
- FLOW (12) : bidons 5/20 L, fût 200 L et IBC 1 000 L, confirmés.
- PAINT (11) : seaux 5/10/20 kg, confirmés.
- PROOF : ACR-RF, CM-O1P, PU-1K en seaux 5/20 kg ; PU-SEAL en **cartouche 300 mL** ; les sept références listées restent à préciser.

Les 50 références sont actuellement en `presentation_provisoire`, non certifiées et non commercialisées ; aucun SKU ERP créé à partir de cet audit.

## Reprise du travail

Une fois chaque réponse obtenue, modifier uniquement les conditionnements confirmés dans `src/data/catalogue-projets.json` et le registre `docs/catalogue-interne/conditionnements_50_A_CONFIRMER.json` ; prévoir la traduction FR/EN/AR et des tests de non-régression. Ne pas changer les drapeaux de certification ou la base Supabase. Réaliser PR, tests GitHub, fusion si verts. Le déploiement du site est distinct et non confirmé.

Sources locales de cet audit : `LOT50_FENEK_sources_et_conditionnements_20261104.json` et les archives de fiches techniques FR/EN/AR fournies dans le projet. Ces sources ne doivent pas être publiées dans le site.
