# NextGen — Préparation du futur backend des demandes B2B (31 octobre 2026)

## Ce qui est codé
- Endpoint Cloudflare Pages Function `POST /api/lead` dans `functions/api/lead.js`, **inactif par défaut** (`NEXTGEN_LEADS_ENABLED` doit être exactement `true`).
- Refus explicite (`503`) tant que les secrets serveur, l'anti-bot Turnstile et la version de notice de confidentialité approuvée ne sont pas disponibles.
- Contrôles : même origine, JSON uniquement, limite de 8 Ko, champs autorisés, consentement obligatoire, validation email/téléphone, piège anti-bot et vérification Turnstile (hostname exact).
- Écriture côté serveur exclusivement dans `site_demandes` via un secret Supabase serveur, sans exposition de la clé dans le navigateur.
- Aucun e-mail, accusé de réception automatique ni écriture CRM dans cette version. Ne pas utiliser les données de `clients` ou `interactions` comme réceptacle sans circuit de qualification.
- Les formulaires visibles restent **désactivés** indépendamment du backend.

## Schéma proposé
- Fichier `sql/003_site_demandes_PROPOSITION_NON_EXECUTEE.sql` **non appliqué**.
- `site_demandes` doit rester strictement privé (RLS activé, aucun GRANT public).
- Historique de consentement (`consent_notice_version` et `consentement_le`) et statut de qualification ; aucun effacement automatique tant que la durée de conservation n'est pas légalement décidée.

## Prérequis obligatoires avant mise en service
1. Validation juridique de la notice, de la base légale, du transfert éventuel hors Algérie, des droits des demandeurs et de la durée de conservation.
2. Approbation expresse du SQL et contrôle de ses droits après application.
3. Configuration sécurisée Cloudflare Turnstile, secrets Cloudflare (`SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`, `TURNSTILE_SECRET_KEY`, `NEXTGEN_PRIVACY_NOTICE_VERSION`) et règles de limitation de fréquence ; aucune clé serveur dans les variables publiques Astro.
4. Tests de bout en bout en environnement isolé, contrôles des réponses et traitement des erreurs, décision d'activation `NEXTGEN_LEADS_ENABLED` seulement après résultats concluants.
5. Définition du traitement ERP : revue humaine d'une demande avant conversion en prospect/client, journaux d'audit et notification par un prestataire autorisé si nécessaire.

## Tests
- `node --test tests/lead_endpoint.test.mjs` : vérifications locales avec appels réseau simulés, aucune écriture réelle.
- `python -m unittest discover -s tests -v` : assure que les interfaces publiques ne collectent rien par défaut.
- Build Astro GitHub Actions ; pas de déploiement Cloudflare réalisé.
