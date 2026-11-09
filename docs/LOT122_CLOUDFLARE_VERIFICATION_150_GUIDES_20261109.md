# NextGen — Lot 122 : vérification de la totalité des guides en production

Date : 9 novembre 2026. Dépôt : `Verwolfy/nextgen-website`.

## Contexte et preuve Cloudflare

L'utilisateur a transmis une capture de Cloudflare Pages confirmant :
- `main` commit de fusion `44560a0` du lot 121 : déploiement **Production réussi** ;
- `main` commit `dc025bc` (fermeture documentaire lot 121) : **Production réussi** ;
- le déploiement Preview `c8333c6` a échoué, sans empêcher la réussite des déploiements de production.

La capture confirme le statut de déploiement, mais **pas** la présence et l'affichage de chaque élément HTML dans le navigateur. Dans l'environnement assistant, les domaines `nextgen-buildingsolutions.com` et `nextgen-website-8te.pages.dev` restent inaccessibles par DNS ; il faut employer les runners GitHub Actions disposant d'une connectivité réseau.

## Diagnostic

Le moniteur du lot 120 (`scripts/check_live_production.py`) contrôlait déjà le SHA exact déployé, le site en trois langues, les pages de catalogue, la recherche Pagefind et les restrictions de publication. Il **ne contrôlait pas les 150 pages des guides du lot 121** ni le fichier original d'illustrations.

## Corrections de surveillance du lot 122

- `scripts/check_live_application_guides.py` : contrôle en lecture seule du WebP `/images/application/tile-application-6.webp` par SHA-256 `55197582655ba03f9de8d933047236e63efbd5df27a1acde136c5fc342059b1c`. Puis téléchargement HTTP GET des 50 fiches × 3 langues.
- Vérifications de chaque page : code correct, langue et direction RTL, indexation Pagefind sous `kind:sheet`, `noindex`, présence d'une seule séquence de mise en œuvre, 6 étapes illustrées pour cinq colles-carrelage ou 4 étapes avec pictogrammes pour les autres produits, numérotation, alternatives accessibles des images, note contextuelle propre à la référence.
- Parcours HTTP concurrents limités à six threads pour éviter les requêtes excessives. Aucun POST ni mutation.
- `.github/workflows/cloudflare-live-production-smoke.yml` : nouveau contrôle inséré **après** la comparaison exacte du SHA déployé et **avant** les parcours Chromium ; s'exécute sur chaque push `main`, quotidiennement et à la demande.
- `tests/test_lot122_cloudflare_illustration_live.py` : cas positifs/négatifs hors ligne et périmètre 50×3 ; inclus aux tests de la PR.

## Risques et limites

- Les 50 références sont des présentations provisoires, et leurs FT/FDS industrielles ne sont toujours pas validées ; le moniteur ne leur confère aucune certification.
- Les vérifications HTTP ne prouvent pas le rendu visuel pixel par pixel ou l'exactitude technique de prescriptions absentes des fiches FENEK.
- Aucune modification Supabase, Cloudflare DNS, Cloudflare Access, produits publiés, RLS, secrets, données de laboratoire ou index Pagefind.
- La confirmation du test sur le **vrai domaine** n'est acquise qu'après un job `Production release + FR/AR/EN search` vert sur `main`. Une PR verte ne suffit pas à cette confirmation.
- Le workflow de monitoring est lecture seule ; en cas d'échec il passe au rouge et ne déclenche aucun rollback.

## Recette avant fusion

Les contrôles CI existants doivent être verts : tests Python, build Astro, contrôles HTML trilingues, Chromium, Lighthouse, et nouveau test de contrat hors ligne. Après fusion, vérifier le workflow de production et son résultat réel ; si inobservable, ne pas le déclarer confirmé.

## Liens de référence

- PR de livraison précédente : https://github.com/Verwolfy/nextgen-website/pull/120
- Guides du lot 121 : `docs/LOT121_GUIDES_APPLICATION_ILLUSTRES_20261109.md`
- Moniteur lot 120 : `docs/LOT120_CLOUDFLARE_LIVE_MONITORING_20261109.md`

## Validation GitHub et livraison finale — 09/11/2026
- PR **#121 fusionnée** sur `main` : commit de fusion `9a3bf287c65772175912b4766b0d20071a420d34`.
- Dernier commit testé sur PR : `de9f74f5cfc0abe1e1372bdce2e7c39bdb3c503d`.
- GitHub Actions `NextGen Astro build + security checks` : **SUCCESS** (run `42650722109`), **300 tests unitaires**, index Pagefind et 150 pages statiques contrôlés.
- GitHub Actions `NextGen - Cloudflare live production smoke (read-only)` : **SUCCESS** sur PR (run `42650722328`) ; 3 contrats du lot 120 + 5 tests du lot 122 passés. La partie **production est skipped sur PR**, conformément à la protection prévue.
- Scripts et workflow vérifiés directement sur `main` après la fusion.
- Chromium et Lighthouse avaient réussi sur le lot 121, qui n'est pas modifié par ce lot de surveillance ; les workflows correspondants n'ont pas été déclenchés par les changements limités aux contrôles de production.
- **Attention : le premier contrôle HTTP de 150 pages réellement exécuté sur `main` n'a pas pu être consulté via les outils disponibles ici. Il serait incorrect de déclarer ce contrôle réussi.**
- Accès à consulter : https://github.com/Verwolfy/nextgen-website/actions/workflows/cloudflare-live-production-smoke.yml
