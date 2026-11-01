# Lot 16 — Audit des captures, arabe professionnel et posters 3D

Date : 1er novembre 2026. Source : **7 captures fournies par l'utilisateur** (accueil, 3 cartes d'emballages, ressources, galerie 3D, à-propos, page des gammes en arabe). Les captures sont des rendus de pages, pas une preuve du moment ou des conditions de leur déploiement.

## Constats fondés sur les captures
1. En français, le hero sur grand écran affiche une typographie très imposante ; les maquettes d'emballages paraissent serrées et le portrait des mascottes dans « À propos » ressemble à une image brute sur fond blanc.
2. La galerie 3D affiche avant activation de grandes zones gris clair et un bouton « Afficher la 3D interactive » ; le code `ModelViewer.astro` disposait de WebP locaux `poster`, mais le **slot personnalisé** remplaçait le visuel par un simple bouton. Il s'agit d'une cause directement vérifiée par le code.
3. La navigation arabe affichait les termes génériques `المجموعات` (gammes), `الوثائق` (ressources) et `الموزعون` (rubrique réseau de distribution). Des formulations BTP étaient maladroites (notamment `الحشو`, sans précision de joints, `العزل` trop générique, `مراجع المنتجات`). Le screenshot montre un RTL global correct ; la disposition des deux premières cartes de droite à gauche est **normale**, pas une inversion.
4. Les noms FENEK en alphabet latin, l'abréviation IBC et les unités doivent être protégés contre la permutation bidi lorsque mêlés à l'arabe. L'adresse du pied de page était encore dans la version française.
5. Sur certaines captures, le bandeau fixe coupe le haut de contenu pendant le scroll ; ce phénomène ne démontre pas un défaut de contenu. La recette est étendue à des captures spécifiques pour lever l'incertitude.

## Corrections du code
- `src/data/site.ts` : révision éditoriale du contenu arabe, vocabulaires du bâtiment : **الفئات التقنية**, **شبكة التوزيع**, **الموارد**, **الملاط**, **لواصق البلاط**, **مواد ملء الفواصل**, **العزل المائي**, **إضافات الخرسانة**, **نشرات بيانات السلامة**. Les produits restent proposés comme pistes de gammes, non approuvés.
- `src/data/editorial.ts` et `src/data/showcase.ts` : rédaction naturelle en arabe et avertissements de non-validation conservés.
- `src/pages/[lang]/emballages.astro` : unités et types d'emballages arabes clarifiés ; maintien de « مسودة غير معتمدة » et de la mention non commerciale.
- `src/data/site.ts`, `src/layouts/Layout.astro`, `src/pages/[lang]/[section].astro` : adresse de la même entreprise localisée FR/AR/EN, sans nouvelle donnée géographique inventée.
- `src/components/RangeOverview.astro`, `src/pages/[lang]/index.astro`, `src/pages/[lang]/gammes/[slug].astro` : balises `<bdi dir="ltr">` autour des marques/gammes écrites en latin, titres de concepts `dir="auto"`.
- `src/components/ModelViewer.astro` : poster WebP natif **dans le bouton du slot poster** avant chargement GLB ; chargement 3D toujours volontaire via `reveal="interaction"`, URL GLB et poster strictement locales et validées.
- `src/styles/site.css` : mise en page du bouton de preview avec visuel, centrage et marges, limitation de taille d'illustration sur l'accueil, portrait encadré « À propos », grille hero moins dominante, meilleur interlignage RTL.
- `tests/test_lot16_arabic_visual.py` : tests de vocabulaire, URL de rendu, catalogue vide, assets locaux et protection `bdi`. `scripts/check_browser_pages.py` : checks Chromium des 5 posters, de leur décodage, texte arabe et captures desktop/mobile des emballages.

## Risques, interdictions et réception
- **Aucun produit réel, prix, FT/FDS ni certification ne sont ajoutés** ; `public/data/products.json = []`.
- Aucune collecte, aucun changement ERP/Supabase/SQL/RLS, secrets, DNS, Cloudflare Pages, règles Access ou lancement public.
- Les essais GitHub prouvent le build local CI **uniquement** ; après fusion, rien ne prouve la mise à jour du site public sans confirmation de la chaîne Cloudflare.
- Certains rendus peuvent dépendre du moteur du navigateur et des polices arabes disponibles : inspecter les captures de la nouvelle CI et corriger les divergences avant la diffusion.
- Revoir la langue arabe avec un rédacteur technique natif avant publication contractuelle.

## Exécution
```bash
npm ci
npm run build
python -m unittest discover -s tests -v
python scripts/check_built_pages.py
python scripts/check_browser_pages.py
```
Après deux CI vertes sur PR, merge sur `main`; contrôler les deux CI de `main` au SHA final et conserver une note de reprise.
