# Lot 113 — Contrôle quotidien et renouvellement vérifié du fil NextGen

Date : 7 novembre 2026. Dépôt : `Verwolfy/nextgen-website`.

## Problème initial
Le bandeau FR/AR/EN est un jeu statique de 8 actualités, sans appel réseau depuis le navigateur. Le cache peut conserver le HTML mais les éléments expirés sont masqués au chargement. Les taux de change étaient manuels et devenaient obsolètes.

## Nouvelle architecture

### Cotations Banque d'Algérie — AUTOMATISÉES
- Source officielle : `https://www.bank-of-algeria.dz/taux-de-change-journalier/`.
- `scripts/refresh_ticker_daily.py` lit la page source côté GitHub Actions et isole date et valeurs USD/EUR par table HTML.
- Protection : dates non futures et de moins de 6 jours ; valeurs en plage prudente ; EUR > USD ; URL sans redirection externe ; refus d'une date antérieure à celle déjà publiée.
- Deux entrées mises à jour ensemble avec **traductions déterministes FR/AR/EN** (formules prédéfinies, sans service de traduction ni génération risquée).
- La cotation est affichée comme telle, sans la qualifier de vente, puisque la valeur affichée n'est pas explicitement typée dans l'extrait de la page.
- Date de publication du record = date officielle, expiration = J+7. Aucun changement si les données restent identiques (week-end et jours fériés).
- Si la source est indisponible, aucun nouveau taux n'est fabriqué.

### Articles APS — AVEC CONTRÔLE ÉDITORIAL
- Les six faits datés APS (5 BTPH, 1 innovation) restent rédigés et traduits à partir d'articles individuels identifiés.
- Le workflow quotidien signale les entrées expirant sous sept jours via **une seule issue GitHub réutilisable**.
- Pas de renouvellement ni de traduction automatique d'un nouvel article sans preuve source et texte FR/AR/EN validés ; cela éviterait des erreurs factuelles.
- Les articles expirés restent cachés par les contrôles serveur et navigateur, même en présence d'un cache HTML.
- Le ratio de 8 items reste 5 BTPH / 2 économie / 1 innovation. C'est 62,5 % / 25 % / 12,5 %, proche du 60/25/15 demandé.

### Exécution et contrôles GitHub
- Workflow : `.github/workflows/ticker-daily-verified.yml`, planifié **chaque jour à 06:37 UTC**, ou à la demande.
- `permissions: contents: write, issues: write` ; aucun secret commercial et aucune API de traduction tierce.
- Avant un commit automatique sur `main` : unitaires complets, vérification noindex/sécurité, build Astro FR/AR/EN, recette Chromium et contrôles statiques.
- Pousse **uniquement** `src/data/nextgen-ticker.ts` si les valeurs vérifiées ont réellement changé.
- Publication Cloudflare non pilotée par GitHub Actions : dépend du déclenchement de déploiement Cloudflare déjà configuré pour `main`. Ne pas confondre test CI et confirmation du site public.
- Journal privé de chaque vérification dans `.ci-artifacts/ticker-daily.json` (artifact GitHub 14 jours).

### Cotations mises à jour au 7 novembre 2026
Publication officielle du **6 novembre 2026** :
- USD/DZD = **136,1078**
- EUR/DZD = **152,0801**
- Source Banque d'Algérie ci-dessus.
- Les records existants du 5 novembre ont été remplacés et leurs dates d'expiration fixées au 13 novembre.

### Innovation actualisée
APS du **5 novembre 2026** : filière cimentière, amélioration de qualité et **développement du ciment vert discutés**. Source :
`https://www.aps.dz/fr/economie/industrieenergie-et-mines/mw3m83lp-kourtel-preside-une-seance-de-travail-avec-les-representants-des-entreprises-publiques-et-privees-de-production-de-ciment`.
Aucune affirmation de production industrielle de ciment vert réalisée. Texte FR/AR/EN traduit de façon conservative.

## Fichiers à vérifier
- `src/data/nextgen-ticker.ts`
- `scripts/refresh_ticker_daily.py`
- `tests/test_lot113_daily_ticker.py`
- `.github/workflows/ticker-daily-verified.yml`
- Tests existants lots 104, 106 conservés/adaptés.

## Limites et prochaine discussion
- Actualisation quotidienne **automatique pour deux devises seulement**. Les articles BTPH/innovation ont alerte d'échéance et nécessitent une nouvelle sélection éditoriale vérifiée.
- Surveiller les premiers déclenchements planifiés, accès HTTP à Banque d'Algérie depuis GitHub Actions, comportement de la branche `main` protégée, apparition de l'issue de renouvellement et exécution complète des tests.
- Vérifier le déploiement Cloudflare après chaque nouveau commit : aucun déploiement direct ou modification DNS/Cloudflare Access effectué.
- Ne pas prétendre que tous les articles APS sont automatiquement remplacés ou traduits à ce stade.
