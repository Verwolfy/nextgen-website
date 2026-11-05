# Lot 62 — Vérification du déploiement V2 (lecture seule)

Date : 5 novembre 2026. Dépôt : `Verwolfy/nextgen-website`.

## Résultat précédent confirmé

- Dernier commit `main` avant ce lot : `6c4b0c61263a3103f78e7984716fe12244017c7f` (lot 61).
- Vidéo Nexo/Geno V2 et poster présents dans le dépôt :
  - `public/videos/nextgen-nexo-geno-welcome.mp4`, **181 635 octets**.
  - `public/videos/nextgen-nexo-geno-poster.webp`, **17 244 octets**.
- Vidéo sans son ; version des URLs `?v=20261105` pour les navigateurs.
- CI du commit lot 61 :
  - Astro + sécurité : `42008101248` → `success`.
  - Chromium FR/AR/EN : `42008101228` → `success`.

## Vérification externe

Le 5 novembre 2026, les tentatives d'accès à `https://nextgen-buildingsolutions.com/fr/` et aux deux assets via le navigateur externe ne donnent pas de réponse exploitable. Le contrôle par le conteneur ne résout aucun de ces trois domaines :
- `nextgen-buildingsolutions.com`
- `www.nextgen-buildingsolutions.com`
- `nextgen-website-8te.pages.dev` (ancienne adresse déclarée dans le projet, non confirmée)

Il serait faux de conclure que le site est déployé ou de conclure qu'il est hors service uniquement sur cette base. La présence d'un domaine SSL « Active » ne prouve pas la publication d'un commit spécifique.

## Action corrective non intrusive

Ajout de `scripts/check_live_video_deployment.py` :
- trois requêtes de diagnostic par hôte au maximum : la page `/fr/`, puis uniquement si l'URL V2 est présente, le MP4 et le WebP ;
- toutes les requêtes sont des **GET anonymes bornés** à des hôtes connus du projet, sans identifiants ni suivis des redirections ;
- une authentification Cloudflare Access, une redirection, un échec DNS, une page ancienne et une vidéo V2 vérifiée sont des états distincts ;
- pour déclarer `v2_verified_anonymously_accessible`, le HTML doit référencer `?v=20261105` et **les deux SHA-256 des médias doivent correspondre exactement** aux fichiers du dépôt ;
- si HTTP 200 anonyme : indiquer explicitement que la page est accessible au public, peu importe `noindex` ;
- aucune action de déploiement, modification DNS, changement GitHub Secrets, fonction Cloudflare ou base ERP.

Ajout d'une GitHub Action `.github/workflows/live-video-readonly.yml` déclenchée sur `main` lors du changement des médias, du lecteur ou du diagnostic, et manuellement via `workflow_dispatch`. Le résultat est écrit en JSON `.ci-artifacts/lot62-live-check.json` et affiché dans le résumé du run GitHub.

Tests unitaires hors réseau : `tests/test_lot62_live_video_readonly.py`. Aucun secret, mail ni donnée privée traité.

## Distinguer les états

| Résultat | Signification |
|---|---|
| `v2_verified_anonymously_accessible` | V2 répond effectivement à cette URL **et la page est publique** |
| `access_protected_or_blocked` | Auth/accès bloqué ; on ne peut pas voir la version déployée sans session |
| `redirect_not_followed` | Redirection vers apex ou Cloudflare Access ; poursuivre manuellement |
| `v2_not_visible_on_home` | Page accessible, mais marqueur V2 absent |
| `html_updated_but_assets_not_v2` | Page modifiée, mais ancien média ou média inaccessible |
| `unreachable_from_runner` | DNS, réseau ou TLS indisponible ; aucune conclusion sur le site |

## Règles de publication inchangées

`docs/DEPLOIEMENT_CLOUDFLARE_RUNBOOK.md` et `docs/LOT8_CLOUDFLARE_PREPROD.md` interdisent une publication Cloudflare avant contrôle des accès, des textes juridiques et de la décision de lancement. Aucune autorisation de publication publique ne découle de « continue ». `main` peut être valide sans être publié. Les URL `pages.dev` peuvent être publiquement consultables par défaut ; `robots.txt` ne les protège pas.

## Prochaine étape / reprise projet

1. Vérifier les tests CI de la PR du lot 62, fusionner dans `main` si verts.
2. Sur `main`, regarder le run **NextGen — vérification HTTP V2 sans déploiement** : tableau de synthèse du job et archive JSON.
3. Si le site est protégé par Cloudflare Access, vérifier à partir du tableau de bord Cloudflare le commit de déploiement et la politique d'accès ; aucune connexion Cloudflare n'est disponible depuis cette conversation.
4. Si le résultat est HTTP 200 public et V2 valide, **ne pas activer le référencement ni les formulaires** sans approbations juridiques et commerciales.
5. Conserver en parallèle le lot 57 (sept kits PROOF non confirmés), sans y inventer de contenance.
6. Toujours préparer un fichier Markdown de reprise avant fin de discussion.

**Ne pas réécrire les domaines, redirections ou politiques Cloudflare en aveugle.**
