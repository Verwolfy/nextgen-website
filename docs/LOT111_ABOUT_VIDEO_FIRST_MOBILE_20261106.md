# Lot 111 — Vidéo « À propos » affichée en premier sur mobile et bureau

Date : 2026-11-06. Dépôt : `Verwolfy/nextgen-website`.

## Décision utilisateur
La vidéo provisoire Nexo/Geno de la page « À propos de NextGen » doit être le **premier contenu sous l'en-tête**, avant le titre, la description, la mission et les trois étapes, en particulier sur mobile, comme l'expérience de la page d'accueil.

## Implémentation
- `src/pages/[lang]/[section].astro`: affiche un bandeau vidéo dédié `about-video-intro` **juste après** la balise Layout et **avant** `page-head`, uniquement si `section === 'a-propos'`.
- Utilise `AboutVideo` pour FR / AR / EN et le MP4 `/videos/nextgen-about-v1.mp4` déjà uploadé manuellement par l'utilisateur dans `main` (commit `f23af0e`, taille 969032 octets).
- Fallback image si média absent au build ; évite une erreur 404.
- `src/components/AboutStory.astro`: image/vidéo supprimée de la grille pour ne garder que la mission, les réserves éditoriales et trois étapes ; plus de lecteur dupliqué.
- `src/components/AboutVideo.astro`: vidéo plus large (max 860px, largeur complète sur téléphone), ratio 16:9, poster paysage local Nexo/Geno déjà existant. `preload=none`, contrôles natifs et pause automatique selon visibilité, Data Saver et reduced motion.
- Bandeau avec fond dégradé premium et faible marge sur mobile (10px), titre et description immédiatement après. Aucune modification aux pages autres que « À propos ».

## Validation
- Tests unitaires lots 110 et 111, sécurité noindex et inventaire provisoire intact.
- Recette Playwright sur FR/AR/EN, tailles 320×720 et 1280×900 : vidéo visible, **premier enfant de main**, média au-dessus du H1 et de la mission, aucun débordement horizontal et pas de duplication.
- CI build/sécurité, Chromium et Lighthouse avant fusion, puis vérification post-fusion.
- Cloudflare Pages : vérifier publication du SHA final séparément de GitHub CI.

## Protection
Aucun changement aux accès Cloudflare, DNS, secrets, formulaires, intégrations ERP/Supabase, produits FENEK provisoires ou fichiers vidéo originaux.

## Prochaine discussion
Confirmer le déploiement dans Cloudflare et la vidéo placée tout en haut sur `https://nextgen-buildingsolutions.com/fr/a-propos/`, `/ar/a-propos/` et `/en/a-propos/`; renouveler les trois versions linguistiques vidéo une fois générées et validées.
