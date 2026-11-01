# NextGen — Cloudflare Pages : préparation du lot 8 (NON DÉPLOYÉ)

Date : 1er novembre 2026 — statut **NO-GO de prévisualisation publique**.

## Décision technique

Préférer un **projet Cloudflare Pages intégré à GitHub** une fois la protection d'accès et la cible de déploiement établies et autorisées. NE PAS connecter le dépôt maintenant : Cloudflare Pages peut publier automatiquement le contenu de `main` sur une adresse `*.pages.dev`. Les previews de branches sont **publiques par défaut** et nécessitent Cloudflare Access. La politique de previews n'assure pas à elle seule la protection du domaine principal `<project>.pages.dev` ni d'un domaine personnalisé.

À confirmer/autoriser par l'exploitant :
1. Projet Cloudflare réel et compte propriétaire, domaine de test dédié et branche non-production.
2. Cloudflare Access installé, policy de refus par défaut et règle de test accessible uniquement aux comptes autorisés ; tester anonymement le **refus 401/403 ou redirection Access** avant de diffuser une URL.
3. Bloquer ou désactiver le déploiement automatique de `main`. Confirmer le statut du domaine principal pages.dev et ne pas le considérer comme privé automatiquement.
4. Configuration Astro : Node 22, `npm ci && npm run build`, répertoire de sortie `dist`, racine du dépôt. Les Pages Functions `functions/api/lead.js` ne sont pas activées par le site statique ; elles doivent être revues séparément.
5. Ne pas utiliser la méthode Direct Upload pour contourner les règles d'accès ; le mode de liaison Git et Direct Upload a des contraintes de migration.
6. **Ne pas installer** SUPABASE_SERVICE_ROLE_KEY, NEXTGEN_LEADS_ENABLED, TURNSTILE_SECRET_KEY ni aucun autre secret sensible dans l'environnement de prévisualisation avant l'approbation juridique et le contrôle de la politique d'accès.
7. Ne pas modifier les DNS Namecheap ni publier `nextgen-buildingsolutions.com` sans autorisation spécifique.

## Ce que le code assure dès maintenant

- `public/_headers` : headers défensifs de pages statiques et `X-Robots-Tag: noindex, nofollow, noarchive` sur toutes les URL.
- `public/robots.txt` : `Disallow: /`, et `Layout.astro` : meta robots noindex.
- Ces instructions **n'empêchent pas** des utilisateurs non autorisés d'accéder au site. Seul le contrôle d'accès en amont peut rendre une prévisualisation privée.
- `scripts/preprod_static_audit.py` : vérifie les headers, 42 routes, non-publication de produits de test, 5 modèles GLB et absence de fichiers internes dans `dist`. Génère les hashes SHA-256 des assets sans aucune connexion réseau.
- `.github/workflows/preprod-build-only.yml` : build en CI GitHub et archivage **du manifeste seulement**, aucun upload Cloudflare ni token de déploiement.

## Conditions bloquantes restantes

- Vérifier en lecture réelle l'hébergement Streamlit : le diagnostic HTTP anonyme obtenu sur `https://nextgent-erp.streamlit.app/` est **303**. La présence du code dans `main` ne démontre pas la publication du commit ni l'affichage après authentification.
- Finaliser la notice de confidentialité FR/AR/EN, la durée de conservation, la base légale, les sous-traitants et les transferts potentiels de données. Documents actuels : **BROUILLON NON VALIDÉ**.
- Vérifier puis autoriser les réductions de privilèges service_role en base à part ; pas de nouvelle migration SQL dans ce lot.
- Recette en préproduction protégée des requêtes d'échec Turnstile, rate-limiting, consentement et stockage ; pas de données personnelles réelles.
- Le site public et le catalogue commercial restent inactifs jusqu'à la décision de publication.

## Documentation technique (2026)

- Pages preview et Access : https://developers.cloudflare.com/pages/configuration/preview-deployments/
- Pages Git integration : https://developers.cloudflare.com/pages/configuration/git-integration/
- Pages headers : https://developers.cloudflare.com/pages/configuration/headers/
- Build Astro : https://developers.cloudflare.com/pages/configuration/build-configuration/

**Aucune action décrite dans cette note ne constitue un déploiement ou une autorisation de mise en ligne.**
