# Lots 81–83 — Intégration V3 Motion + Industry (démarrage)

Date : 2026-11-05. Dépôt : Verwolfy/nextgen-website. Base GitHub main : af8d883dbc3573144f9c98169bbc2a85e5f43506.

## Demande utilisateur
« commence » à la suite de la validation de principe de la V3 « Motion + Industry », en demandant de conserver **l'animation originale Nexo/Geno sur l'accueil**. Intégration automatique par lots, sans publication de caractéristiques techniques non validées.

## Changements effectués dans ce premier bloc
- **Lot 81 — Éditorial et identité** : src/data/home-v3.ts centralise les textes FR/AR/EN du nouvel accueil, les disclaimers, le statut de maquette et les trois étapes BTPH.
- **Lot 82 — Motion hero** : src/pages/[lang]/index.astro utilise une grille sémantique et responsive : titre → vraie vidéo → descriptif / CTA sur mobile ; titre+texte à gauche et vidéo à droite sur ordinateur. Le MP4 Nexo/Geno et son poster restent les fichiers d'origine.
- **Lot 83 — Graphisme / parcours** : src/styles/v3.css introduit la palette premium bleu nuit / vert menthe, une navigation visuellement plus nette, les quatre gammes FENEK, 3 références illustrées et les parcours B2B, tout en conservant le thème sombre et RTL. La section démarche utilise le SVG de fabrication déjà présent dans le site au lieu de redoubler la mascotte.
- src/components/HeroWelcomeVideo.astro : nouveau cadre vidéo, indicatif de durée/localisation FR/AR/EN ; lecture manuelle accessible en mode « réduire les animations » (sans lecture automatique en reduced-motion). Les URLs et empreintes de la source MP4/WebP sont conservées.
- src/layouts/Layout.astro importe la couche CSS V3 après les styles principaux, sans toucher à noindex, aux URLs, aux protections, aux liens ni au footer.
- tests/test_v3_motion_industry_home.py + scripts/check_browser_pages.py : source vidéo/poster, indicateurs FR/AR/EN, statut provisoire, ordre vidéo mobile, 3 références et sécurité.

## Garde-fous
- **50 références FENEK** inchangées et toujours des **présentations provisoires**.
- 3 exemples : FENEK-BOND C1T, FENEK-PROOF EP-ANC, FENEK-FLOW AC, tirés du catalogue central. Les aperçus sont conceptuels.
- EP-ANC : cartouche double A/B de 600 mL **au total** ; volumes individuels et ratio technique non confirmés.
- Ne pas créer FT/FDS, inventer certification, capacités de production ou commercialisation ; ne pas activer les formulaires, SEO, indexation.
- **Ne pas modifier** Supabase, ERP, Cloudflare, DNS ou Cloudflare Access. Une fusion GitHub n'est pas un déploiement prouvé.
- Maquette source locale : /mnt/data/NEXTGEN_V3_MAQUETTE_ANIMATION.html et reprise /mnt/data/REPRISE_NEXTGEN_REFONTE_V3_ANIMATION_20261105.md.

## Vérifications avant fusion
1. GitHub Actions « NextGen Astro build + security checks » et « NextGen protected browser recipe ».
2. Revue des tests historiques liés à l'accueil, aux médias, à la traduction, au thème et à la navigation.
3. Après fusion, tests identiques sur main et, si possible, contrôle HTTP anonyme du site public et du MP4 existant en lecture seule.
4. Restera à intégrer les autres vues V3 (catalogue complet, fiches, solutions, entreprise, distribution, ressources, contact) en lots séparés avec tests de non-régression, sans changer la publication des produits.

Aucune donnée de facturation, logistique, juridique, technique ou d'ERP n'a été modifiée.
