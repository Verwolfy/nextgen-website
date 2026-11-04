# Lot 60 — Sélecteur de langue et mode jour/nuit NextGen

Date : 2026-11-04. Dépôt : `Verwolfy/nextgen-website`.

## Besoin et référence
L'utilisateur a transmis une image présentant : interrupteur pillule clair/sombre à gauche, pictogramme de soleil, sélecteur de langue compact « Fr » avec intitulé discret « langue » et chevron. Il demande le même fonctionnement sur le site NextGen et un vrai mode nuit harmonisé à la charte.

## Modifications
- `src/components/HeaderPreferences.astro` : switch accessible `role=switch`, état `aria-checked`, labels FR/AR/EN, icône soleil/lune, et menu natif `details/summary` avec liens des trois langues. Changement de langue préservant la même route et son suffixe ; fermeture par Echap et clic à l'extérieur.
- `src/components/ColorSchemeInit.astro` : script synchrone dans `head` appliquant `data-theme` avant le rendu CSS, évite le flash blanc. Préférence initiale du système via `prefers-color-scheme`, mémorisée en `localStorage` au clic sur le switch. Si stockage bloqué : changement local de thème sans planter. Si aucun choix enregistré : suit les changements système.
- `src/layouts/Layout.astro` : importe les composants et le fichier `src/styles/theme.css`, remplace les trois anciens liens linguistiques.
- `src/styles/theme.css` : palette nuit bleu marine / vert NextGen, contrastes revus pour en-tête, navigation mobile, cartes du catalogue, détails produits, documents, accordéons, filtres, formulaires, CTA, bas de page. Supports RTL et 320 px. Conserve l'illustration et les images produits sans inversion. Ne change pas les fichiers de marque, FENEK, PDF d'export.
- `tests/test_lot60_theme_language_controls.py` : tests structurels, localisation, couleur, conservation des garde-fous.
- `scripts/check_browser_pages.py` : vérifie le menu et les trois routes, passage jour/nuit, palette et persistance après rafraîchissement, dans FR/AR/EN et mobile/desktop.

## Garde-fous
- Conserver `noindex`, `robots.txt`, les formulaires désactivés et les données ERP inchangées.
- Ne pas déduire la publication sur le domaine public de la fusion GitHub.
- Respecter `prefers-reduced-motion` et les personnes sans JavaScript : le sélecteur linguistique fonctionne nativement; le thème automatique initial est calculé dans `head`.
- Le thème d'écran ne modifie pas l'export imprimé A4 : `@media print` conserve un fond blanc.

## Livraison / reprise
1. Attendre les deux workflows (Astro + sécurité et navigateur Chromium), corriger les tests si des défauts réels sont détectés.
2. Fusionner PR si succès, revérifier les workflows sur `main`.
3. Vérifier le domaine hébergé après un déploiement autorisé ; aucun déploiement Cloudflare implicite.
4. Travaux parallèles : vidéo Nexo/Geno temporaire sur la bannière `main` ; lot 59 a retiré sa légende. PR #66 des sept kits PROOF à confirmer reste indépendante.
