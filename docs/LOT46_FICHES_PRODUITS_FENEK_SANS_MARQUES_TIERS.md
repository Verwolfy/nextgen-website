# Lot 46 — Fiches produits FENEK autonomes, site sans marques concurrentes

Date : 3 novembre 2026. Repository : `Verwolfy/nextgen-website`.

## Demande et décision
L'utilisateur souhaite retirer du site l'ensemble des références à d'autres fabricants et les grands encadrés défensifs, puis présenter une documentation FENEK autonome en FR/AR/EN.

L'ancienne page `/{lang}/documentation/{slug}/` affichait les noms de fabricants tiers, leurs résultats et avertissements en premier plan. Ce n'était pas une fiche NextGen et l'expérience visuelle était confuse.

**Modification :** 150 fiches FENEK avec uniquement des informations effectivement rattachées aux 50 références du catalogue éditorial NextGen. Nouveau format « Fiche produit » (pas « fiche technique officielle », faute de rapports industriels). La présentation contient la désignation, la famille, la description, les domaines d'application, les visuels associés à la bonne référence, les conditionnements **envisagés**, et un canal pour obtenir les données techniques du produit. Mise en page premium et responsive, support de l'impression PDF.

## Pourquoi ne pas transférer les valeurs de concurrents en performances NextGen
Les fiches tierces ne prouvent pas les formulations de FENEK, ni ses résistances, temps d'utilisation, consommations, classements, FDS ou dosages. Les moyennes de produits de formulations et marchés différents ne peuvent être présentées comme des mesures de laboratoire FENEK. Des dosages incorrects peuvent entraîner des défauts de chantier et des problèmes de sécurité.

En conséquence, les comparatifs sont retirés du code **servi au public**. Les éléments nécessaires à une qualification technique réelle nécessitent essais NextGen, analyse HSE et contrôle qualité. Le site évite les gros messages de mise en garde tout en conservant une phrase de portée non contractuelle près des formats, et les informations de contact technique.

## Implémentation
- `src/pages/[lang]/documentation/[slug].astro` : refonte FENEK-only, 150 pages, images exactes via `conceptPackshot`, identité, domaines, formats catalogue, contact et impression A4.
- `src/pages/[lang]/documentation/index.astro` : index des 50 références, texte professionnel localisé FR/AR/EN, sans marques externes et sans encart d'alerte.
- `src/data/editorial.ts` et `src/components/ResourcesHub.astro` : dénomination honnête « Fiches produits FENEK », lien direct vers les 50 fiches, voie distincte de contact pour FDS.
- `src/styles/site.css` : mise en page A4, accessible et responsive, tableaux de paramètres qualitatifs, styles RTL.
- Suppression dans la branche des 4 fichiers `src/data/market-comparisons.json` et `src/data/market-locales/*.json` ; suppression des 2 tests devenus obsolètes sur les anciennes comparaisons. Les études historiques restent dans Git et les documents internes non servis, pour maintenir la traçabilité et ne pas effacer les sources.
- `scripts/check_browser_pages.py` et `scripts/check_built_pages.py` : affirment l'absence de références à des marques externes, la présence du vrai visuel par référence, 50 fiches × 3 langues, impression et liens.
- `tests/test_lot46_fenek_only_docs.py` : garde-fous sur la non-publication de valeurs et FDS inventées.

## Limites et interdictions
- Les 50 produits sont toujours `presentation_provisoire`, `certifie:false`, `commercialise:false`, et `public/data/products.json=[]`. Aucune autorisation de commercialisation ni de certification.
- Les poids et volumes affichés sont ceux du catalogue éditorial, pas des conditionnements réels approuvés.
- Les PDF imprimables sont des **fiches produits** sans données d'essais garanties, et non des fiches techniques réglementaires ou FDS.
- Le site reste `noindex,nofollow` et `robots.txt Disallow: /` jusqu'à validation officielle.
- Aucun changement Supabase, ERP, CRM, domaine, fiches juridiques ou intégrations.
- Les marques d'autres fabricants subsistent éventuellement dans l'historique Git et les études **internes**, mais doivent être absentes de toute page HTML publiée.

## Vérification et fusion
1. Contrôler `verify`, `smoke` (Chromium FR/AR/EN desktop/mobile), et `Cloudflare Pages` sur la tête exacte de PR.
2. Corriger les tests si nécessaire, sans neutraliser le contrôle d'absence de marques externes.
3. Fusionner dans `main` uniquement avec les trois contrôles réussis.
4. Vérifier post-fusion les mêmes contrôles et le SHA `main`.
5. Si consultation HTTP externe possible : ouverture de `/fr/documentation/`, `/ar/documentation/`, `/en/documentation/`, plus les 50 fiches, impression et absence des noms concurrents.

## Prochaine étape
Obtenir des données mesurées et documents industriels NextGen. Les formulations, performances et FDS ne doivent être introduites comme officielles qu'avec preuves et validation. Garder la PR #50 historique en brouillon tant que ces preuves manquent.
