# Lot 42 — Retrait complet de la page Galerie visuelle (02/11/2026)

## Décision utilisateur
Supprimer le lien vers `https://nextgen-buildingsolutions.com/fr/maquettes/` et l'ensemble de sa page, dans les trois langues, car cette galerie isolée est inutile dans l'expérience client.

## Exécution
- Suppression du fichier source unique `src/pages/[lang]/maquettes.astro` (routes FR/AR/EN).
- Suppression du lien public « Voir aussi les 46 illustrations de conception (2D) » dans `src/components/ResourcesHub.astro`. La section conserve **une seule action** : « Demander une documentation » vers Contact.
- Suppression des styles dédiés à la grille de galerie 2D non utilisée.
- Mise à jour des contrôles statiques `scripts/check_built_pages.py` et `scripts/preprod_static_audit.py` : refus de toute page `dist/{fr,ar,en}/maquettes/`, tout en conservant les WebP.
- Mise à jour des vérifications navigateur `scripts/check_browser_pages.py` : les routes parcourues deviennent 42 couples route/viewport et plus aucun lien n'est attendu dans Ressources.
- Mises à jour des tests historiques `test_lot27_visual_concepts.py`, `test_lot40_hero_resources.py`, `test_editorial_hubs.py`, `test_lot16_arabic_visual.py`, `test_lot17_arabic_eyebrows.py` et `test_retired_visualization.py`.
- Documentation active de déploiement corrigée.

## À conserver impérativement
- **Les 46 images WebP** de `public/images/maquettes/` : elles restent de simples fichiers d'illustration utilisés par le catalogue.
- **Le slider de la page d'accueil** avec les maquettes 01, 02, 15, 16.
- Les 50 références éditoriales de catalogue et leurs illustrations.
- Les contenus FR/AR/EN, les avertissements, `noindex`, `robots.txt` et la séparation ERP/Supabase.

## Déploiement et validation
1. PR du lot 42 : contrôler le commit exact et les résultats de `verify`, `smoke`, `preproduction` et `Cloudflare Pages`. Ne pas contourner une erreur.
2. Fusionner vers `main` uniquement lorsque les contrôles requis sont verts.
3. Vérifier la CI et le déploiement post-fusion, puis s'assurer qu'aucun `dist/{lang}/maquettes/index.html` ne subsiste.
4. Effectuer si accessible les contrôles HTTP : anciennes routes galerie FR/AR/EN -> 404 ; Ressources et Accueil -> 200. Le déploiement historique et les caches ne sont pas effacés rétroactivement par Git.

## Prochaine amélioration
Auditer les pages clients et les tests de navigation. N'effectuer aucune modification ERP ou Supabase pour ce lot.
