# Lot 26 — Consultation directe des maquettes 3D NextGen

Date : 02/11/2026. Périmètre : dépôt du site, sans Cloudflare, DNS, Supabase, RLS, modification commerciale ou activation de formulaire.

## Résultat technique attendu

Les cinq fichiers GLB existants dans `supports/3d/glb` sont utilisés sans les réinventer : `sac-25kg`, `seau-20kg`, `bidon-20l`, `fut-200l`, `ibc-1000l`. Leurs textures sont embarquées ; les aperçus WebP correspondent aux ressources présentes dans `supports/3d/previews`. Le build les copie vers `dist/models-demo/` et `dist/images/3d-demo/` via `scripts/copy_public_assets.mjs`.

Chacune des cinq maquettes dispose désormais d'une page interactive individuelle, en français, arabe RTL et anglais :

- `/{lang}/emballages/sac-25kg/`
- `/{lang}/emballages/seau-20kg/`
- `/{lang}/emballages/bidon-20l/`
- `/{lang}/emballages/fut-200l/`
- `/{lang}/emballages/ibc-1000l/`

Depuis l'accueil, les trois cartes visuelles principales ouvrent directement leur visionneuse ; depuis la galerie `/{lang}/emballages/`, cinq liens donnent accès aux cinq pages. La visionneuse est locale, mobile, déclenchée par l'utilisateur, avec rotation, zoom et image de repli. Un téléchargement du GLB d'étude est proposé sans le présenter comme un modèle de fabrication validé.

**Important :** GLB réel = vrai fichier géométrique interactif, **pas** produit industriel validé. Aucun plan coté, homologation, vérification des conditionnements ni conformité réglementaire n'est démontré. Ces cinq formes sont des *simulations de design*. Ne jamais associer automatiquement un GLB de démonstration à une fiche commerciale réelle ni publier les 50 fiches de projet comme des références certifiées.

## Contrôles et publication

- `tests/test_lot26_individual_3d.py` : signatures GLB, manifeste, route statique générée pour cinq modèles, prévisualisation et liens internes, séparation catalogue public.
- `tests/test_home_showcase.py` : vérifie les liens directs.
- `scripts/check_built_pages.py` : contrôle les 15 pages, présence GLB et poster, liens locaux, langues, `noindex`, zéro formulaire.
- `scripts/check_browser_pages.py` : navigation de la galerie vers la visionneuse, lecture des attributs du modèle, retour mobile et absence de débordement.

Lancer la CI du dépôt (Astro/sécurité, Chromium) après PR. Ne fusionner que si les deux contrôles de la tête de PR sont réussis. **Fusion GitHub != déploiement Cloudflare.** Maintenir le NO-GO Cloudflare tant que l'accès aux domaines principal et preview n'est pas protégé et la publication juridiquement/commercialement approuvée.

## Suite

1. Vérifier les deux CI et la consultation des 15 pages dans l'artefact de build privé.
2. Importer les 20 vrais WebP FENEK-BOND uniquement depuis le ZIP approuvé et contrôlé (lot 25).
3. Valider Cloudflare Access et juridique avant toute mise en ligne publique ou toute activation de collecte.
