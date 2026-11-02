# Lot 33 — Retrait de l'affichage public des procédures incomplètes

Date : 2 novembre 2026. Suite de l'audit trilingue [#33](https://github.com/Verwolfy/nextgen-website/issues/33).

## Problème
Chaque fiche des 50 références était compilée en 3 langues avec une rubrique déroulante « Mode d’emploi source (brouillon français) ». Le HTML statique conservait les instructions et leurs chaînes `[valeur à confirmer]` (152 mentions uniques dans la source française, soit 456 rendues sur 150 pages). Le volet masqué visuellement restait consultable par les visiteurs et les robots.

## Modification précise
- `src/pages/[lang]/catalogue/[slug].astro` n'importe plus `guidance` et ne génère plus de procédure à étapes ou de bloc déroulant `concept-source-method`. Les consignes de dosage, de durée de séchage, de mélange et d'application à valeurs absentes **ne figurent plus dans le HTML du site**.
- Les contenus `mode_fr_preparatoire` restent dans `src/data/catalogue-projets.json`, sans modifier leurs valeurs ou leurs états techniques (non approuvés). Ce fichier source n'est pas servi dans `dist`.
- La notice de documentation technique du produit demeure visible, afin de ne pas inciter un particulier ou un professionnel à appliquer les maquettes sans notice produit.
- Aucune modification des images, des mentions légales, des informations de certification, des produits ERP/Supabase, des DNS ou des paramètres Cloudflare.

## Vérifications
- `scripts/check_built_pages.py` parcourt les **150 fiches compilées** FR/AR/EN et exige zéro trace des placeholders, des procédures sources FR et des deux sections retirées.
- `scripts/check_browser_pages.py` contrôle sur ordinateur et mobile, dans les trois langues, l'absence des procédures au DOM et la présence de notices.
- `tests/test_lot20_catalogue_projects.py` exige que les données internes soient toujours conservées, mais qu'elles ne soient pas incluses dans le template public.

## Déploiement
- PR dédiée, fusion sur `main` uniquement après deux CI GitHub vertes.
- Cloudflare Pages est relié à `main` : vérifier les 150 pages en build et au moins des échantillons sur le domaine public après déploiement. Ne pas confondre fusion GitHub avec publication Cloudflare.
- Les autres mentions de conception / « non contractuel », les formulations légales incomplètes et les avertissements éventuellement imprimés dans des images ne sont pas couverts par ce lot.
