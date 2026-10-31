# NextGen Building Solutions — Site B2B

**LOT 1 / SUPPORTS LOCAUX — SQL DE PUBLICATION APPLIQUÉ EN PRODUCTION LE 31 OCTOBRE 2026.**

Site dédié, distinct de l'ERP `Verwolfy/erp-mortier`. Le répertoire contient **la base d'intégration et les supports du lot 1** ; le site Astro trilingue sera développé au lot 2. Aucune publication/donnée personnelle ne doit être envoyée avant recette et validation.

## Invariants

- **Jamais** de requête Supabase depuis le navigateur ; extraction côté GitHub Actions seulement, avec clé serveur dans GitHub Secrets.
- Produit réel confirmé **ET** approbation laboratoire **ET** approbation commerciale avant publication. Les 6 produits `PF-001` à `PF-006` existants sont des tests exclus du modèle.
- Aucune divulgation des tables ERP, recettes, coûts, prix, clients, fournisseurs, employés.
- Aucun contenu 3D, fiche technique ou FDS fictif sur le site public ; les supports générés sont des **BROUILLONS** internes.
- Après accord écrit « SQL VALIDÉ », seule la migration SQL de publication privée a été exécutée en PRODUCTION : table, vue et permissions ; aucune donnée ERP modifiée, aucun DNS ni déploiement.

## Structure

- `sql/001_site_publication_PROPOSITION_NON_EXECUTEE.sql` : **source historique de la migration déjà appliquée**, conservée pour traçabilité. Ne pas exécuter de nouveau. Voir `docs/ETAT_AVANCEMENT.md`.
- `scripts/sync_catalogue.py` : export JSON public minimal et copie contrôlée PDF/images/GLB depuis Supabase Storage.
- `scripts/check_public_content.py` : bloque champs sensibles/prix non autorisés.
- `.github/workflows/sync-site.yml` : nuits + déclenchement manuel/event externe ; **non déployé**.
- `supports/` : logo original, charte, étiquettes SVG éditables, FT trilingues en HTML et PDF de démonstration, trames FDS.
- `public/data/products.json` : `[]` à l'origine ; **aucun produit fictif en ligne**.

## Exécution locale de la recette

```bash
python -m pip install -r requirements-sync.txt
python -m unittest discover -s tests -v
python scripts/check_public_content.py
```

## Secrets à créer sur le nouveau dépôt GitHub

`SUPABASE_URL` et `SUPABASE_SERVICE_ROLE_KEY` (jamais dans ce dépôt). **La vue privée existe désormais et ses droits SQL ont été contrôlés ; configurer ces secrets uniquement dans GitHub dès que le dépôt dédié existe.**

Le bouton Streamlit « Publier » n'est pas implanté au lot 1. Dans un lot ultérieur, il déclenchera `repository_dispatch` via un token GitHub à permissions minimales ; aucun secret supplémentaire dans le code. Cloudflare Pages pourra être lié au dépôt après approbation de publication.

## Risques / points ouverts

- Dépôt privé GitHub `Verwolfy/nextgen-website` désormais créé et accessible ; import progressif. Les PDF et images des maquettes internes ne doivent pas être traités comme des supports validés ni inclus dans le site public.
- Migration production : appliquée le 31 octobre 2026 avec accord explicite, sous `20261031204336_nextgen_site_publication_private_20261031`. Tout changement ultérieur reste soumis à approbation.
- FTP/FT labo, FDS et marque : aucune donnée validée ; ne pas mettre les exemples en ligne.
- Le logo source est un JPG ; usage du fichier exact, sans redessin IA. Les documents ne sont pas des étiquettes industrielles de production.
- Génération de formulaires avec accusé + CRM à 0 € : à valider juridiquement et techniquement en lot 3.

## Lot 2 — squelette Astro FR/AR/EN (en cours)

- Astro 6.4.6, sorties 100% statiques, aucune API Supabase navigateur.
- Pages /fr, /ar (RTL), /en, gamme, catalogue, fiche produit, distributeurs, contact et mentions non définitives.
- Aucune fiche de produit fictif ; les documents présents dans `supports/` ne sont pas servis par `public`.
- Build : `npm install && npm run build` sur Node 22.
- Pas encore de build local exécuté : installation npm impossible dans l'environnement de génération ; CI GitHub chargée de l'évaluer.
- `package-lock.json` présent sur GitHub ; utiliser `npm ci && npm run build` pour reproduire le build.
- Robots et meta noindex activés jusqu'à l'autorisation de lancement.
