# REPRISE PROJET NEXTGEN — illustrations des modes d'emploi (12/11/2026)

## Objectif et règles
Moderniser les 6 étapes illustrées par produit FENEK, fidèles à `src/data/fenek-v3-manuals.json`, sans invention de dosage, durée, norme, certification, valeur de performance, logo ou information de sécurité. Toute la série reste **BROUILLON — non validé**. Les textes FR/AR/EN sont conservés dans les pages HTML, pas dans les images.

## Dépôt, branche et PR
- GitHub : `Verwolfy/nextgen-website` (privé).
- Branche de travail : `feat/lot139-140-professional-paint-illustrations-20261112`.
- PR en brouillon : https://github.com/Verwolfy/nextgen-website/pull/140, base `main`.
- `main` était à `d676565afc3353a439c76b1c2d5a038c8d042b11` au début de cette série.
- **Aucune fusion vers main ni déploiement Cloudflare confirmé.**

## Lots livrés sur la branche
- 139–140 : PAINT-INT-M, PAINT-INT-S, PAINT-INT-WA, PAINT-PRIM-A, PAINT-PRIM-FX.
- 141–143 : PAINT-TXT-F, PAINT-SOL-A, PAINT-ENT-L.
- 144–145 : PROOF-CM-O1P, PROOF-CM-O2P.
- 146–149 : PROOF-PU-1K, PROOF-ACR-RF, PROOF-EP-PRIM, PROOF-EP-SR.
- 150–154 : PROOF-EP-SB, PROOF-EP-INJ, PROOF-EP-ANC, PROOF-PU-INJ, PROOF-PU-SEAL.

**Total : 19 produits, 114 scènes vectorielles, gamme PROOF complète (11/11), 8 produits PAINT.** Les 50 WebP V3 améliorés déjà existants restent inchangés et associés à leur référence.

## Fichiers et règles techniques
- SVG créés dans `public/images/application-professional/<slug>-steps.svg`, planches 1620×720 en six cases (3×2, chacune 540×360).
- Registre `src/data/fenek-enhanced-artwork.json` : `professionalSvg`, `professionalSvgSha256`, `professionalSvgDimensions`, `professionalSourceType`, `professionalSceneWorkflowWith`.
- `src/components/FenekApplicationGuide.astro` choisit le SVG professionnel par `code+slug` et conserve le WebP remastérisé comme repli.
- `scripts/check_live_application_guides.py` vérifie les médias enregistrés, leur SHA et les fiches FR/AR/EN en lecture seule.
- Tests de lots : `tests/test_lot139_140_paint_professional_svg.py`, `tests/test_lot141_143_professional_paint.py`, `tests/test_lot144_145_cement_waterproofing.py`, `tests/test_lot146_149_proof_professional_svg.py`, `tests/test_lot150_154_remaining_proof_svg.py`.
- Documentation lot par lot sous `docs/LOT139_140*`, `LOT141_143*`, `LOT144_145*`, `LOT146_149*`, `LOT150_154*`.

## Contrôles réellement réalisés
- Tous les 19 enregistrements professionnels ont code/slug conforme au catalogue et à la notice V3, SHA-256 à 64 caractères et statut BROUILLON.
- Les 19 chemins de fichiers sont distincts ; les 19 SHA sont distincts ; aucun produit PROOF n'est manquant.
- Les 9 SVG des lots 146–154 ont été créés et relus sur GitHub : 6 panneaux et 6 badges code-produit chacun, SHA-256 calculés, pas d'image/script/lien externe. Les 5 du lot 150–154 ont aussi passé un contrôle d'équilibrage de balises.
- Avant cette session, les dix SVG des lots 139–145 avaient passé un audit statique équivalent.
- Aucune preuve d'exécution complète de `npm ci`, `npm run build`, des tests Python, de QA navigateur ou des tests live sur Cloudflare. Ne pas les présenter comme réussis.

## Blocage CI
Au commit `113e6f1ed765522371cc8b7e054f76eed1611dc0`, les quatre workflows PR GitHub Actions ont conclu `failure` (run IDs 43225683247, 43225682873, 43225682662, 43225682986). Les jobs observés se terminent sans étapes ni runner attribué, donc le résultat ne constitue PAS un diagnostic du code. `.github/workflows/site-check.yml` utilise déjà `runs-on: ubuntu-latest`. Hypothèses possibles à contrôler : quota/billing Actions, compte, service GitHub, permissions. Éviter toute modification de secrets ou de protections de branche sans nécessité et autorisation.

## Prochaines actions ordonnées
1. Résoudre l'échec de démarrage CI ; inspecter l'exécution Actions dans GitHub et son éventuel avis de quota/facturation ; lancer les véritables tests.
2. Exécuter `npm ci --no-audit --no-fund && npm run build`, `python -m unittest discover -s tests -q`, puis `python scripts/check_built_pages.py` et les audits.
3. Vérifier visuellement les 114 scènes, mobile 360 px et desktop, FR/AR/EN. Contrôler que chaque représentation respecte les six titres V3.
4. Seulement après vérifications suffisantes : fusionner PR #140, contrôler le commit déployé, les 19 SVG publics avec SHA, 50 WebP et 150 fiches de documentation.
5. Poursuivre **FENEK-BOND** (16 références) puis **FENEK-FLOW** (12 références) ; garder les anciens médias. Les **31 produits sans SVG professionnel** comprennent ces 28 références et les trois peintures de façade PAINT-FAC-M/EL/SX, déjà dotées de WebP professionnels au lot 138.
6. Continuer à considérer toutes les scènes comme des illustrations non contractuelles tant que le laboratoire n'a pas validé les FT/FDS.

## Éviter
- Ne pas annoncer que le code est en production.
- Ne pas fusionner avec CI en échec sans évaluation explicite des risques.
- Ne pas utiliser l'image ERP « lots C-H » produite par erreur dans une session précédente : elle ne correspond pas au site ni aux produits.
