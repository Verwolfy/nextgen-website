# NextGen — Lot 4 : préparation de la qualification CRM (31/10/2026)

## État et périmètre

- Base Supabase PRODUCTION : migration `20261031220121_nextgen_site_demandes_private_20261031` effectivement appliquée, table privée `public.site_demandes` vide au dernier contrôle. **Ne pas rejouer la migration SQL 003.**
- Nouveau script `scripts/crm_qualification.py` : **lecture seule** des métadonnées `demande_id`, `type_demande`, `statut`, `cree_le` ; l'export courant ne contient aucun nom, téléphone ni e-mail. Les résultats synthétiques ne contiennent pas de données d'identification.
- Fonction pure `propose_crm_draft` : prépare une structure compatible avec `public.clients` / `public.interactions`, **sans créer d'ID et sans écriture**. À utiliser uniquement dans une future interface ERP à accès restreint, après dédoublonnage et validation humaine.
- `functions/api/lead.js` : `503` par défaut, besoin de `NEXTGEN_EXPECTED_HOSTNAME` et `NEXTGEN_TURNSTILE_ACTION`. Échec si hostname de la requête ou hostname/action Turnstile ne correspondent pas aux valeurs configurées. Délai réseau borné à 8 secondes. Les tests n'effectuent aucun envoi réel.
- `public/data/products.json` reste `[]`; les produits fictifs, les documents labo fictifs et les visuels non contractuels sont exclus des contenus commerciaux.

## Circuit CRM à réaliser (aucune écriture automatique)

1. Une demande réelle est reçue dans `site_demandes` **après** activation séparée des formulaires et validation conformité.
2. L'administrateur ERP habilité consulte la demande, vérifie son origine, le consentement, la nécessité de traiter le contact et les doublons dans `clients`.
3. Il choisit de rejeter, fermer, rattacher à un client existant ou créer un dossier nouveau ; toute écriture future doit être journalisée avec l'identité du validateur, un horodatage et la demande source.
4. Les champs `clients.client_id` et `interactions.interaction_id` sont attribués par les mécanismes de l'ERP. Ils ne sont **jamais inventés dans le site**.
5. Après décision métier et contrôle de conformité, une notification commerciale ou un accusé de réception pourrait être ajouté, mais **aucun email n'est envoyé actuellement**.

## Commande de diagnostic (serveur sécurisé uniquement)

```bash
export SUPABASE_URL='https://<reference-projet>.supabase.co'
# Fournir SUPABASE_SERVICE_ROLE_KEY dans les secrets serveur ; ne jamais coller la clé dans les logs ou dans le dépôt.
python scripts/crm_qualification.py --limit 200
```

Sortie : comptages non nominatifs par type/statut, indicateur de troncature lorsque la limite est atteinte, mode `READ_ONLY`.

## Critères bloquants avant activation

- Notice de confidentialité trilingue et base légale validées ; registre des traitements et responsable opérationnel désignés.
- Durée de conservation et procédure de suppression / traitement des droits définies ; aucune purge automatique imaginée.
- Vérification des transferts éventuels de données hors Algérie (Cloudflare, Supabase, autres sous-traitants), au regard de la loi n° 18-07 modifiée par la loi n° 25-11 du 24/07/2025.
- Clés serveur stockées exclusivement dans Cloudflare Secrets. Configuration par environnement : `NEXTGEN_LEADS_ENABLED`, `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`, `TURNSTILE_SECRET_KEY`, `NEXTGEN_PRIVACY_NOTICE_VERSION`, `NEXTGEN_EXPECTED_HOSTNAME`, `NEXTGEN_TURNSTILE_ACTION`. Limitation de débit et tests anti-abus nécessaires avant activation.
- Tests bout en bout en environnement protégé ; **aucune mise en ligne DNS ni activation de formulaire dans ce lot**.

## Réserves sécurité documentées

- Supabase applique un héritage de privilèges permettant aussi `DELETE` et `TRUNCATE` à `service_role` sur `site_demandes`. Réduction de ces droits soumise à autorisation SQL spécifique. Aucune modification effectuée ici.
- Les API Cloudflare et Supabase exigent une validation serveur : le navigateur ne reçoit jamais les secrets ni les demandes privées.
- La fonction pure `propose_crm_draft` produit de la PII **en mémoire** lorsqu'elle reçoit un enregistrement nominatif ; ne jamais la logger ni l'exécuter côté client ou dans une CI avec des demandes réelles.

## Références externes consultées

- Cloudflare Turnstile Siteverify : https://developers.cloudflare.com/turnstile/get-started/server-side-validation/
- Cloudflare Pages — variables et bindings : https://developers.cloudflare.com/pages/functions/bindings/
- Texte légal modificatif : https://natlex.ilo.org/dyn/natlex2/r/natlex/fe/details?p3_isn=118858

## Durcissement Lot 6 (2026-11-01)

- Le serveur Cloudflare refuse maintenant toute réception si le binding de limitation de fréquence `NEXTGEN_RATE_LIMITER` manque, si son secret HMAC `NEXTGEN_RATE_LIMIT_SALT` est trop court, ou si le service limite/refuse la requête. La clé du compteur est dérivée par HMAC du numéro de téléphone normalisé ; le numéro en clair n'est pas transmis au compteur. Le contrôle fonctionne après Turnstile, avant l'écriture. Il **ne remplace pas** les règles WAF globales contre les abus.
- La variable `NEXTGEN_SUPABASE_PROJECT_REF` doit correspondre exactement à l'URL racine Supabase configurée ; tout autre projet ou chemin est refusé, sans émission de la clé serveur. Les secrets restent à configurer uniquement après validation de l'infrastructure.
- Exiger une preuve de configuration effective du binding Cloudflare (et de la limite choisie) avant d'activer la fonctionnalité ; aucun binding ni secret réellement configuré à ce jour.
