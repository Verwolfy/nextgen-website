# NextGen — Lot 121 — Étapes d'application illustrées pour les 50 références FENEK

Date : 9 novembre 2026 — dépôt `Verwolfy/nextgen-website`
Branche : `feat/lot121-illustrated-application-guides-20261109`

## Périmètre et statut
Les 50 références sont **des concepts de catalogue et des fiches produit provisoires**, non des fiches techniques approuvées. La base existante contient 16 BOND, 12 FLOW, 11 PROOF et 11 PAINT. Aucun produit commercialisé, aucune FT/FDS FENEK certifiée n'a été publié.

La demande porte sur une présentation plus lisible et utile, adaptée à chaque référence, mais sans inventer les valeurs qui sont `[valeur à confirmer]` dans les modes opératoires préparatoires du dépôt. Les vraies caractéristiques, les classes et prescriptions d'utilisation doivent être approuvées par le laboratoire avant d'être publiées comme fiche technique.

## Sources exploitées
**Source interne, effectivement consultée :**
- `src/data/catalogue-projets.json` : 50 codes, descriptions FR/AR/EN, domaines et méthodes FR préparatoires avec champs volontairement non validés.
- `src/data/fenek-guides.ts` et `src/data/fenek-application-context.ts` : contraintes éditoriales et contexte distinct par code.
- `src/data/fenek-qualification-notes.ts` : 50 critères de qualification complémentaires.
- Six dessins utilisateur `1.jpeg` à `6.jpeg` reçus le 9 novembre, dans l'ordre : préparation du fond, eau, malaxage, temps de repos/reprise, peignage, pose.

**Limite de disponibilité :**
- Le dépôt évoque « 365 PDF de référence FR/AR/EN » dans ses commentaires, mais les PDF techniques originaux individuels n'étaient **pas accessibles lors de cette opération** dans les fichiers disponibles au projet. Aucun résultat de recherche fichier n'a fourni la FT définitive de chacune des 50 formulations FENEK. Les synthèses déjà codées ont été exploitées comme références éditoriales, et non comme données certifiées.
- La documentation des fabricants externes sert **d'exemple de procédé courant**, jamais de preuve de performances des formulations FENEK.

**Vérifications externes de procédés, à ne pas recopier comme spécifications FENEK :**
- MAPEI : `https://cdnmedia.mapei.com/docs/librariesprovider21/line-technical-documentation-documents/tile-s-installers-manual255ae97679c562e49128ff01007028e9.pdf` (préparation, malaxage, peigne, temps ouvert et contrôle du transfert).
- Sika UK : `https://gbr.sika.com/en/construction/concrete-repair/application-support/application-guides.html` (diagnostic, réparation béton, cure).
- Sika UK : `https://gbr.sika.com/en/construction/concrete-repair/projects/New-Build-Concrete-Repair/sustainable-solutions-for-new-build-concrete-repair.html` (réparation, contrôle du fond, nécessité de se référer à la FT).
- ARDEX : `https://helpcentre.ardex.co.uk/hc/en-gb/articles/7561868381341-P51` (primaire, adaptation à la porosité, toujours consulter la FT).
- Sika : `https://usa.sika.com/retail/en/learn/blog/blog-proper-surface-preparation.html` (préparation des joints et supports).

## Mise en œuvre

### Références mortiers-colles : illustrations utilisateur 1 → 6
- `BOND-C1T`, `BOND-C1TE`, `BOND-C2FT`, `BOND-C2TE`, `BOND-C2TE-S1`.
- Les six illustrations fournis sont convertis en sprite WebP 3×2 de 315×210 pixels, 5 902 octets, SHA256 `55197582655ba03f9de8d933047236e63efbd5df27a1acde136c5fc342059b1c`, archive textuelle contrôlée dans `src/assets/tile-application-6.webp.base64`.
- `scripts/install_application_art.mjs` restaure l'image originale issue du lot, vérifie strictement le hash, puis la rend disponible dans `public/images/application/tile-application-6.webp` avant le build Astro.
- Les six étapes sont préparation du support, eau de gâchage, malaxage, repos **uniquement si FT**, étalement au peigne, pose/contrôle. Aucune quantité/durée non approuvée n'est publiée.

### Autres produits
Le champ d'affectation `applicationModeByCode` relie **exactement 50 références** à des procédures qualitatives par famille et sous-procédé. Chaque page conserve aussi un point de qualification spécifique à son code via `applicationContextFor`.

- BOND : joints, ragréages, enduits, maçonnerie, calage, réparation béton.
- FLOW : adjuvants du béton, cure de surface et latex d'adhérence. Les doses et mélanges nécessitent essais et FT.
- PROOF : étanchéité, systèmes cimentaires, résines, injection spécialisée, scellement chimique, mastic, sols époxy. Aucune procédure d'injection, de ratio chimique ou de scellement dimensionnant n'est établie en l'absence de qualification.
- PAINT : peintures murales et sol, primaires, enduits, revêtements texturés.

Pour ces familles, des icônes vectorielles personnalisées (hors images industrielles externes) accompagnent quatre phases par type. Les recommandations restent **génériques et conditionnelles**.

### Composants modifiés
- `src/data/fenek-application-steps.ts` : données éditoriales et traductions FR/AR/EN, 50 codes.
- `src/components/FenekApplicationGuide.astro` : cartes illustrées et numérotées, responsive, RTL, thèmes clair/sombre, note et contrôle par référence.
- `src/pages/[lang]/documentation/[slug].astro` : remplace les trois étapes génériques ; accordéon ouvert par défaut.
- `src/components/FenekPrintableSheet.astro` : synthèse imprimable A4 en trois phases conservée pour préserver une page ; les parcours illustrés complets sont disponibles en ligne.
- `scripts/install_application_art.mjs` et `package.json` : packaging WebP vérifié sans CDN.
- `tests/test_lot121_illustrated_guides.py` : audit du mapping exact et de la sécurité.
- `scripts/check_application_guides.py` intégré à `scripts/check_built_pages.py` : 150 pages et asset SHA.

## Confidentialité et limites
Aucune écriture Supabase, aucun changement RLS, publication de FT/FDS privées, de valeurs de laboratoire, tarifs ni formulaire actif. Les pages conservent statut provisoire et `noindex`. Les illustrations sont des dessins de gestes génériques, pas une preuve de performance ou de dosage.

## Recette avant fusion
```bash
npm ci --no-audit --no-fund
npm run build
python -m unittest discover -s tests -q
python scripts/check_built_pages.py
python scripts/check_browser_pages.py
```
Plus GitHub Actions Lighthouse et sécurité. La mise en ligne Cloudflare suit `main` et doit être vérifiée après fusion.

## Validation technique à effectuer ultérieurement
Par référence : identité de la formulation, eau/masse, ordre de mélange, temps de repos autorisé, temps ouvert, classe, épaisseurs, outils et sécurité, cure, conditions atmosphériques, normes et dosages exacts. Le présent lot **n'approuve aucun de ces paramètres**.

## Livraison finale — 09/11/2026
- PR #120 fusionnée dans `main` : commit `44560a0220fad66094f4e7e9a48c8eda06025d75`.
- Dernier commit contrôlé : `c8333c6423558e4a8871a38bab9f5517b52478cb`.
- GitHub Actions build et sécurité **SUCCESS** (run `42648782262`), navigateur Chromium **SUCCESS** (run `42648782299`), Lighthouse local **SUCCESS** (run `42648782296`), moniteur Cloudflare hors-ligne **SUCCESS** (run `42648782387`).
- CI : **295 tests unitaires**, **150 fiches produit FR/AR/EN** vérifiées ; empreinte SHA-256 de l'illustration utilisateur conforme. Le rendu imprimable A4 a été préservé à **une page**.
- Les sources originales des FT/FDS industrielles des 50 formulations ne sont toujours pas disponibles/validées. Les guides sont illustratifs, non certifiants.
- La validation du domaine Cloudflare se fait indépendamment via le workflow du lot 120 ; aucune réussite de déploiement live n'est déduite de la fusion.
