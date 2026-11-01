# Lot 12 — Pages Gammes, À propos et Ressources

Date : 1er novembre 2026. Statut : **code de préproduction, sans publication Cloudflare**.

## Objectif

Après les lots 10 (navigation mobile) et 11 (galerie 3D sur l'accueil), renforcer les pages de second niveau du site NextGen Building Solutions en français, arabe RTL et anglais, sans inventer de produits, de performances, d'autorisations ou de documents homologués.

## Livrables

- `src/data/editorial.ts` : textes localisés, catégories éditoriales pour **Fenek-Bond, Fenek-Proof, Fenek-Flow et Fenek-Paint**, démarche de qualification présentée comme **en préparation**, distinction entre documents techniques en attente et concepts d'emballages.
- `src/components/RangeOverview.astro` : quatre cartes de gammes plus lisibles, thèmes génériques et réserve explicite, sans SKU.
- `src/components/AboutStory.astro` : trois étapes **proposées** (écoute du besoin, qualification des références, contrôle des documents), sans prétendre à une certification ou disponibilité de services.
- `src/components/ResourcesHub.astro` : trois cartes (fiches techniques, FDS, concepts 3D). Les premières sont indiquées *en attente de validation* et **ne comportent aucun lien de téléchargement fictif**. Seule la galerie 3D déjà existante est liée.
- `src/pages/[lang]/[section].astro` : connexion de ces trois composants aux routes existantes.
- `src/pages/[lang]/gammes/[slug].astro` : pages des 4 gammes × 3 langues détaillées avec zones éditoriales, réserve sur les SKU, accès aux maquettes et au contact ; l'état « catalogue vide » reste inchangé tant qu'aucun produit n'est approuvé.
- `src/styles/site.css` : grilles responsives, affichage mobile 320/390 px, couleur de gamme via variable CSS, focus clavier, prise en charge RTL et animations réduites.
- `tests/test_editorial_hubs.py` et `scripts/check_browser_pages.py` : tests structurels de non-publication et recette Chromium élargie de 30 à **48 contrôles de parcours page/langue/écran** ; captures internes supplémentaires des pages Gammes, À propos et Ressources sur téléphone.

## Tests attendus

```bash
npm ci
npm run build
python -m unittest discover -s tests -v
python scripts/check_built_pages.py
python scripts/preprod_static_audit.py
python scripts/check_browser_pages.py
```

Le dernier contrôle nécessite Chromium/Playwright et est exécuté automatiquement par le workflow GitHub `site-browser-recette.yml`.

## Garde-fous conservés

- Aucun produit ajouté dans `public/data/products.json` ; aucune donnée ERP fictive ni fiche FT/FDS non approuvée.
- Aucune collecte B2B : champs de formulaire toujours désactivés et API de prospects désactivée par défaut.
- Aucun changement de secrets, DNS, Cloudflare Pages, Supabase, RLS ni autorisation de mise en production.
- Les tests Chromium locaux ne prouvent ni la protection Cloudflare Access ni l'accès public du site. Les captures CI restent des artefacts privés de revue et **ne valent pas réception graphique humaine**.

## Suite prioritaire

Vérifier les CI de PR, fusionner uniquement si elles réussissent puis confirmer les CI de `main`. Revoir les captures internes FR/AR/EN et les ajustements visuels sur téléphone. Publication Cloudflare **NO-GO** jusqu'à validation Access sur toutes les URL et revue commerciale/juridique.
