# Lots 150 à 154 — illustrations métiers des derniers produits FENEK PROOF

Date : 12 novembre 2026 · état **BROUILLON**, sans validation du laboratoire.

## Objectif et source
Finir les cinq fiches Fenek-Proof non encore dotées d'une série SVG professionnelle. Les six intitulés et descriptions FR/AR/EN de chaque référence proviennent exclusivement de `src/data/fenek-v3-manuals.json` et restent affichés en HTML dans `FenekApplicationGuide.astro`, sans texte de mode opératoire figé dans l'image.

## Séries livrées
| Lot | Produit | Enchaînement représenté |
|---|---|---|
| 150 | PROOF-EP-SB | Faces propres/rugueuses, EPI, mélange A/B, encollage deux faces, assemblage et pression, durcissement |
| 151 | PROOF-EP-INJ | Fissure et injecteurs, EPI, obturation, mélange A/B, injection progressive, dépose et rebouchage |
| 152 | PROOF-EP-ANC | Perçage, brossage/soufflage, EPI, cartouche purgée, injection au fond, insertion de la tige |
| 153 | PROOF-PU-INJ | Fuite et injecteurs, EPI/ventilation, préparation de la résine, injection à la pompe, contrôle/réinjection, rebouchage |
| 154 | PROOF-PU-SEAL | Nettoyage du joint, EPI, fond de joint, primaire conditionnel, extrusion du mastic, lissage/protection |

Chaque produit dispose de sa propre planche SVG de **1620 × 720** divisée en **6 cases de 540 × 360**. Chaque case comporte uniquement un numéro d'étape et le code produit en plus du dessin. Le pictogramme d'origine reste accessible comme repli WebP.

## Registre et contrôles
- Création des cinq fichiers dans `public/images/application-professional/` :
  - `fenek-proof-ep-sb-steps.svg`
  - `fenek-proof-ep-inj-steps.svg`
  - `fenek-proof-ep-anc-steps.svg`
  - `fenek-proof-pu-inj-steps.svg`
  - `fenek-proof-pu-seal-steps.svg`
- Association productuelle exacte et SHA-256 : `src/data/fenek-enhanced-artwork.json`.
- Contrôles effectués : cinq fichiers relus sur GitHub ; SHA-256 recalculés ; six panneaux et six codes produits chacun ; balises équilibrées, sans liens/images/scripts externes.
- Test ajouté : `tests/test_lot150_154_remaining_proof_svg.py`, incluant la vérification des 11 séries SVG PROOF.
- **11/11 produits PROOF** ont un SVG spécifique. **19/50 produits** du catalogue entier ont un SVG professionnel, soit **114 scènes** ; les 50 WebP antérieurs sont conservés.

## Interdictions et limites
Aucune valeur de performance, durée de cure, dosage, certification, norme, logo ou preuve marketing ne doit être fabriquée ou déduite des dessins. Le statut est **BROUILLON**. Ces images sont uniquement des représentations éditoriales, non des instructions d'application contractuelles.

Le build Astro, les tests Python et la QA navigateur/Cloudflare n'ont pas été prouvés : GitHub Actions échoue au démarrage des jobs sans étapes et sans runner attribué. Ne pas déclarer la CI « verte » et ne pas fusionner dans `main` à ce stade.

## Prochaine phase
1. Débloquer la CI et tester `npm ci && npm run build`, `python -m unittest discover -s tests -q`.
2. Visualiser les 114 scènes à 360 px, tablette, desktop, FR/AR/EN ; comparer les gestes aux notices V3.
3. Fusionner PR #140 seulement après contrôle et vérifier les 19 SVG publics, les 50 WebP et les 150 fiches trilingues.
4. Continuer les autres séries de la gamme FENEK-BOND puis FENEK-FLOW.
