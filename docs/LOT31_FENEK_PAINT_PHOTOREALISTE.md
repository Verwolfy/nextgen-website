# Lot 31 — Publication des onze maquettes FENEK-PAINT photoréalistes

**Date** : 2026-11-02

## Demande et source
L'utilisateur fournit un exemple de packaging FENEK-PAINT (seau blanc, couvercle bordeaux, poignée métallique, bandeaux rouge/bleu, logo NEXTGEN, pictogramme renard), puis confirme une planche de onze rendus photoréalistes issus de ce concept et demande : « publie chaque produit à sa place dans le catalogue de la Fenek-Paint ».

**Source éditoriale** : la planche utilisateur `gamme_complète_fenek_paint_architecturale.png`, de **1122 × 1402 px**. Le fichier n'est pas une photographie de marchandise fabriquée. Les rendus sont des **simulations visuelles assistées par IA**, sans certification, mesures vérifiées, étiquettes validées ni garantie contractuelle.

## Import
La planche a été inspectée et les onze visuels de seaux **découpés individuellement**, en excluant les titres et légendes de la grille. Chaque cadrage comporte le **nom propre imprimé du produit correspondant** ; pas de récupération de blocs contenant un autre produit. Chaque visuel source a été redimensionné sans déformation sur une toile 800 × 800 et exporté en WebP.

| Code FENEK-PAINT | Fichier web public |
| --- | --- |
| ENT-L | `/images/catalogue-projects/fenek-paint-ent-l.webp` |
| FAC-EL | `/images/catalogue-projects/fenek-paint-fac-el.webp` |
| FAC-M | `/images/catalogue-projects/fenek-paint-fac-m.webp` |
| FAC-SX | `/images/catalogue-projects/fenek-paint-fac-sx.webp` |
| INT-M | `/images/catalogue-projects/fenek-paint-int-m.webp` |
| INT-S | `/images/catalogue-projects/fenek-paint-int-s.webp` |
| INT-WA | `/images/catalogue-projects/fenek-paint-int-wa.webp` |
| PRIM-A | `/images/catalogue-projects/fenek-paint-prim-a.webp` |
| PRIM-FX | `/images/catalogue-projects/fenek-paint-prim-fx.webp` |
| SOL-A | `/images/catalogue-projects/fenek-paint-sol-a.webp` |
| TXT-F | `/images/catalogue-projects/fenek-paint-txt-f.webp` |

Un manifeste `scripts/paint-packshots-concepts.json` consigne 11/11 **SHA-256**, longueurs et code/slug; `tests/test_lot31_paint_photorealistic.py` valide intégrité, RIFF/VP8, dimensions 800 × 800, unicité et association aux onze références. Les images binaires ont été importées à l'identique dans GitHub par API d'objets Git, avec validation de leur SHA-1 Git après transfert.

## Affichage
- `src/lib/catalogue-projets.ts` exige la présence de la maquette propre à chaque code PAINT ; le build échoue si l'une est absente (aucune répétition générique).
- `src/components/ConceptCatalogue.astro` et `src/pages/[lang]/catalogue/[slug].astro` affichent les **vrais WebP** plutôt que le composant de seau vectoriel du lot 30.
- `scripts/check_built_pages.py` et `scripts/check_browser_pages.py` contrôlent **11 cartes + 11 fiches × 3 langues**, chargement effectif 800 px, correspondance exacte des URL, proportions conservées et absence du montage 15 L ou des anciens seaux SVG sur ces pages.
- Le texte de mise en garde reste « présentation de projet / non homologué » et ne prétend pas que les images montrent des produits fabriqués.

## Limites et suite
- Les mentions FR/AR présentes dans les images sources sont des **brouillons de design**. Les conditions d'utilisation, homologations et formats imprimés devront être vérifiés avant commercialisation. Si une photographie de produit réel est souhaitée, des photos approuvées de produits fabriqués sont encore nécessaires.
- Zéro changement dans Supabase, ERP, secrets, Cloudflare DNS, `public/data/products.json=[]` et formulaires inactifs.
- Fusion sur `main` uniquement après deux CI verts sur le même SHA de PR; Cloudflare Pages déploie `main` automatiquement, mais il faut confirmer le SHA final dans son écran Deployments.
