# Lots 95–97 — Mesures Chromium locales, accessibilité RTL et audit CSS

Date : 2026-11-05. Repo : Verwolfy/nextgen-website.

## Contexte
- PR #92 : performances de démarrage et Data Saver, audit statique CSS/médias, validée/fusionnée.
- PR #93 : doublon né d'un travail concurrent, fermé sans fusion pour éviter tout conflit.
- PR #94 : lien d'évitement clavier FR/AR/EN, test à 320 px sans JS, fusionnée sur main au commit `1021922d5dfe82ff609e325f33c9840d8134022b`, après succès des deux CI PR.

## Lot 95 — Baseline navigateur synthétique
- `scripts/measure_v3_local_browser.py` sert uniquement le dossier local Astro `dist` sur `127.0.0.1` et lance Chromium avec `prefers-reduced-motion: reduce`.
- Collecte pour 8 parcours : 3 accueils mobiles FR/AR/EN ; accueil FR à 320 px et sur desktop ; catalogue FR mobile ; fiche EP-ANC FR desktop ; Contact AR mobile.
- Mesure par `PerformanceObserver` : dernier candidat LCP, cumul des décalages de mise en page non liés aux interactions, temps `navigation`, volume de ressources et présence éventuelle d'une requête MP4 en mode réduit.
- **Aucune métrique observée en CI ne doit être appelée Core Web Vitals terrain** : réseau et CPU CI ne représentent pas les visiteurs, aucun throttling étalonné, aucune session réelle. Aucun seuil LCP/CLS n'est utilisé pour bloquer le déploiement.
- Les vérifications structurelles (HTTP 200, absence de débordement de plus de 4 px, aucune demande MP4 en mode réduit) restent bloquantes.

## Lot 96 — Recette mobile et RTL
- Inclut explicitement accueil FR à 320 px, AR/EN 390 px et Contact arabe.
- Empêche tout chargement à partir de sites tiers pendant les mesures.
- Conserve les tests Chromium existants FR/AR/EN, clavier, Data Saver, contraste et menus.

## Lot 97 — Audit de poids CSS
- Le rapport collecte le nombre, le poids compilé et une **estimation gzip** de toutes les feuilles CSS `dist/_astro`, complémentaire à l'audit source du lot 93.
- Permet de comparer les versions et de déterminer ensuite quels sélecteurs supprimer sans risque de casser les thèmes sombre et RTL.
- Aucune suppression aveugle de CSS en l'absence de preuves de non-utilisation.

## CI et fichier de sortie
- Nouvelle étape dans `.github/workflows/site-browser-recette.yml`, après les tests Chromium existants, puis artefact privé `nextgen-v3-local-browser-metrics` conservé sept jours.
- JSON : `.ci-artifacts/lot95-97-browser-metrics.json`.
- Test statique : `tests/test_lots95_97_v3_synthetic_metrics.py`.
- L'exécution ne modifie ni domaine Cloudflare, ni DNS, ni protection `noindex`, ni bases ERP/Supabase. Aucun formulaire ou certificat produit créé.

## Suite automatique
1. Faire valider la compilation/sécurité et Chromium sur PR ; corriger avant fusion.
2. Fusionner sur main avec contrôle de SHA et vérifier les CI après fusion.
3. Exploiter le JSON des mesures pour fixer des priorités réelles de chargement et CSS, sans inventer de gains.
4. Pour des objectifs formels LCP/INP/CLS, compléter par Lighthouse étalonné et données terrain représentatives ; exiger les validations avant toute mise en ligne de fiches techniques.
