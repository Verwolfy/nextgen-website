# Lots 146–149 — illustrations PROOF : membranes et primaires/résines

Date : 12 novembre 2026 · statut **BROUILLON — non validé par le laboratoire**

## Sources et restrictions
- Référentiel source : `src/data/fenek-v3-manuals.json` (six étapes, noms FR/AR/EN par produit), comparé au catalogue `src/data/catalogue-projets.json`.
- Illustrations éditoriales originales en SVG ; aucun texte technique incrusté, aucune proportion, dosage, temps, épaisseur, performance, certification ou logo reconstitué.
- Chaque planche : SVG 1620 × 720, six cellules 540 × 360 (3 × 2), code produit visible sur chaque cellule ; textes traduits en HTML.
- Association par `code + slug`, SHA-256 dans `src/data/fenek-enhanced-artwork.json` ; WebP remastérisés conservés intacts comme repli.

## Lots livrés sur la branche

| Lot | Référence | Six gestes représentés |
| --- | --- | --- |
| 146 | PROOF-PU-1K | Support sec/propre ; EPI/ventilation ; homogénéisation **sans eau** ; primaire conditionnel ; membrane uniforme ; points singuliers |
| 147 | PROOF-ACR-RF | Réparation/toiture ; gants/lunettes ; homogénéisation ; première couche ; renfort joints/relevés ; recouvrement après séchage |
| 148 | PROOF-EP-PRIM | Préparation mécanique ; EPI ; mélange A/B ; primaire uniforme ; sablage conditionnel ; recouvrement sans durée chiffrée |
| 149 | PROOF-EP-SR | Préparation sol ; EPI/ventilation ; mélange A/B ; versement de résine ; raclette crantée ; débullage et protection |

Fichiers ajoutés :
- `public/images/application-professional/fenek-proof-pu-1k-steps.svg`
- `public/images/application-professional/fenek-proof-acr-rf-steps.svg`
- `public/images/application-professional/fenek-proof-ep-prim-steps.svg`
- `public/images/application-professional/fenek-proof-ep-sr-steps.svg`

Tests ajoutés :
- `tests/test_lot146_149_proof_professional_svg.py` : correspondance des six titres V3 FR, présence AR/EN, six images dans le bon ordre, identité code/slug, structure 3 × 2, empreintes SHA, absence de références externes et d'allégations réglementaires.
- `tests/test_lot144_145_cement_waterproofing.py` : invariant de cardinalité modernisé, afin de rester valide lorsque davantage de références sont améliorées.
- `scripts/check_live_application_guides.py` : contrôle générique déjà présent pour l'ensemble des SVG enregistrés, des SHA publiés et des 150 pages trilingues, à exécuter après fusion.

## Contrôles effectivement faits
- Les 4 fichiers ont été créés dans GitHub, puis relus.
- Contrôle statique avant publication : **6 panneaux et 6 codes produits pour chaque SVG**, interdiction de lien/image/script externe, taille approximativement 9–12 Ko.
- SHA-256 des fichiers relus recalculé, associé à chaque entrée du registre.
- Les tests Python complets, le build Astro, la navigation visuelle et le déploiement réel **ne sont pas encore validés** : les GitHub Actions échouent au démarrage sans étapes.

## Suite
1. Vérifier et réparer la CI GitHub Actions au niveau du runner/compte.
2. Exécuter build Astro et tous les tests Python sur un runner réel, corriger les anomalies.
3. Examiner visuellement les 24 nouveaux dessins en FR/AR/EN, smartphone et desktop.
4. Maintenir PR #140 en brouillon tant que le feu vert n'est pas démontré ; après fusion, contrôler 14 SVG, 50 WebP et 150 fiches documentaires sur Cloudflare.
5. Poursuivre PROOF-EP-SB, PROOF-EP-INJ, PROOF-EP-ANC, PROOF-PU-INJ, PROOF-PU-SEAL, puis BOND et FLOW.

**Règle** : sans FT/FDS validées par le laboratoire, ne jamais qualifier les représentations d'instructions contractuelles ou certifiées.
