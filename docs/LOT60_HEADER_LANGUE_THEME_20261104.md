# Lot 60 — En-tête langue compacte + jour/nuit NextGen

Date : 2026-11-04. Dépôt : `Verwolfy/nextgen-website`.

## Instruction utilisateur
« change le fonctionnement du bouton langue pour qu'il ressemble à la photo et ajoute un switch pour le mode jour/nuit en optimisant soigneusement le mode nuit à la charte graphique ».

L'image présente un interrupteur à pastille, une icône soleil et un petit menu « langue / Fr » à chevron sur un fond gris clair.

## Modifications
1. `src/components/HeaderPreferences.astro` — switch natif `role=switch` accessible, icône soleil/lune synchronisée avec l'état, menu de langue `<details><summary>` compact avec trois liens vers FR / AR / EN conservant la route et le RTL. Les liens restent utilisables **sans JavaScript**. Fermeture au clic extérieur / Échap.
2. `src/components/ThemeInit.astro` — préférence `nextgen-ui-theme` lue dès le `<head>`, avant rendu ; le thème système `prefers-color-scheme` sert de valeur de départ, sans suivi ni réseau. Si `localStorage` est bloqué, le switch continue à fonctionner pour la page active.
3. `src/layouts/Layout.astro` — nouveaux composants affichés sur toutes les pages localisées, métadonnées `theme-color` selon l'appareil, feuille de style complémentaire.
4. `src/styles/theme.css` — palette nuit réservée à l'écran (bleu nuit `#081726`, surfaces `#10283d`, texte `#eef7fc`, vert `#79e2b4`), y compris header, navigation, cartes, formulaires désactivés, catalogue, fiches produit, documentation, vidéo et footer. **Pas de modification du style d'impression A4**.
5. `tests/test_lot60_header_theme.py` — structure, traductions, disponibilité sans JS, persistance et sécurité de publication.
6. `scripts/check_browser_pages.py` — test navigateur des trois langues en mode jour/nuit, du changement de langue sans perte de thème, persistance après rechargement, préférences système, clavier/Échap, absence de défilement horizontal à 320 px et fonctionnement de la langue sans JS.

## Points de contrôle
- Contraste clair sur fond bleu nuit ; surfaces distinguées par des bordures `#3b566c`. Vert NextGen en accent et non en fond généralisé.
- Le mode sombre n'inverse **jamais** les images, les étiquettes des produits ou les mascottes, et ne doit pas affecter les documents imprimés.
- Comportement responsive testé 320, 390 et 1280 px.
- Aucune dépendance supplémentaire, aucune API externe et aucune nouvelle information produit.
- `noindex,nofollow`, robots `Disallow: /`, formulaires désactivés, données ERP/Supabase, et code de publication inchangés.

## Suite
1. Attendre les workflows GitHub `NextGen Astro build + security checks` et `NextGen protected browser recipe` sur la PR. Corriger toute régression identifiée sans désactiver les tests.
2. Fusionner dans `main` après succès, puis vérifier les workflows post-fusion et le SHA exact.
3. Ne pas affirmer le déploiement public tant que le domaine hébergé n'a pas été vérifié.
4. Continuer indépendamment la documentation et les tailles des 7 kits PROOF via le lot 57.

**Note de reprise :** nouveau composant `HeaderPreferences` et `ThemeInit`, thème dans `theme.css`. Reproduire les contrôles FR/AR/EN lors de futures modifications du header ou du CSS.
