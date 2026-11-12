# Lot 184 — repli WebP effectif et contrôle de publication des illustrations

12 novembre 2026 — PR #140 en **brouillon**. Guide et médias **BROUILLON**, non approuvés techniquement.

## Défaut confirmé et correction
Avant ce lot, `FenekApplicationGuide.astro` utilisait `background-image:var(--v3-professional,var(--v3-sprite))`. Cela sélectionnait le WebP seulement si la variable CSS `--v3-professional` était absente ; si la variable était présente, mais le SVG renvoyait une erreur HTTP, le WebP ne s'affichait pas.

Le CSS utilise désormais deux couches superposées :
```css
background-image:var(--v3-professional,none),var(--v3-sprite);
background-size:300% 200%,300% 200%;
background-position:var(--sprite-position),var(--sprite-position);
background-repeat:no-repeat,no-repeat;
```
Le SVG est prioritaire, le WebP existe sous la première couche si le SVG est absent ou ne charge pas. Les deux images utilisent la même case du sprite 3×2. **Point QA à vérifier** : les marges transparentes des SVG peuvent révéler de petits fragments du WebP sous-jacent ; ne pas approuver sans rendu navigateur.

## Audit post-build ajouté
Fichier `scripts/check_professional_artwork_built.py`, appelé automatiquement à la fin de `scripts/check_built_pages.py` après `check_application_guides()`. Le script réalise un contrôle **en lecture** du dossier `dist/` :
- 50 WebP remastérisés : existence, en-têtes RIFF/WEBP et SHA-256 identiques au manifeste.
- 47 SVG professionnels : existence, SHA-256, syntaxe XML, `viewBox` 1620×720, six panneaux, absence de script/image externe.
- 150 fiches FR/AR/EN : présence d'un guide, référence exacte, six illustrations, liaison aux médias WebP/SVG avec empreintes et styles correspondants.
- Les trois façades PAINT-FAC-M/EL/SX gardent leur WebP professionnel, sans SVG nouveau.
- Bilan attendu : 97 médias + 150 pages + 300 illustrations correctement raccordées.

## Tests de non-régression
Trois anciens tests ont été adaptés à la nouvelle règle CSS :
- `tests/test_lot139_140_paint_professional_svg.py`
- `tests/test_lot141_143_professional_paint.py`
- `tests/test_lot183_global_50_professional_artwork.py`

Nouveau `tests/test_lot184_robust_artwork_fallback.py` : vérifie la priorité des deux couches, les tailles et positions identiques du sprite, la présence de l'audit post-build et son raccordement à la pipeline.

## Observations et blocages
Les fichiers et intégrations ont été relus dans GitHub et leurs signatures textuelles concordent. **Ne pas prétendre avoir exécuté** `npm run build`, la suite Python, le nouvel audit `dist/` ou une simulation d'échec réseau dans un navigateur. Le dépôt privé n'est pas clonable depuis l'environnement local (DNS github.com indisponible) et les workflows GitHub Actions échouent sur `main` aussi bien que sur la PR, avec zéro étape sur le job inspecté.

## Prochaines actions
1. Diagnostiquer les runners GitHub Actions/quotas et rétablir leur exécution.
2. Exécuter `python -m unittest discover -s tests -q`, `npm ci --no-audit --no-fund && npm run build`, `python scripts/check_built_pages.py` (inclut désormais lot 184).
3. Tester le repli navigateur en bloquant volontairement un SVG sur un site de prévisualisation, vérifier que le WebP apparaît sans mauvais recadrage ; examiner également 360 px, desktop, FR/AR/EN/RTL.
4. Fusionner PR #140 et vérifier Cloudflare uniquement après validation des contrôles. Conserver toutes les FT/FDS et images comme brouillons jusqu'à approbation technique.
