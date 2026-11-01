# Lot 20 — Catalogue des 50 fiches éditoriales approuvées pour présentation

Date : 2026-11-01. Dépôt privé, pas de déploiement Cloudflare déclenché depuis ChatGPT.

## Autorisation et état de la source

L'utilisateur accepte les 50 fiches Excel/Supabase, leurs descriptions de travail et les conditionnements pour **alimenter le site**, avec possibilité de changement ultérieur. Cette autorisation est **éditoriale et révocable** ; elle ne constitue pas la preuve d'essais, de conformité d'une norme, d'une FDS, d'une autorisation de mise en vente ou de sécurité d'application.

En production Supabase `wenydirqtmkywbxbxfal`, 50 lignes de `public.site_produits` ont reçu dans `contenu.validation_editoriale_projet` l'état `accepte_pour_presentation_provisoire` avec date 2026-11-01. **Après écriture contrôlée : 50/50 accords, 0/50 produits confirmés et 0/50 publiés par les indicateurs de certification.** Aucun flag `produit_reel_confirme`, `publie`, `fiche_technique_validee` ou `fds_validee` n'est modifié.

## Site GitHub

- `src/data/catalogue-projets.json` : extraction allowlist des 50 noms, codes, catégories, descriptions FR/AR/EN, usages, modes FR préparatoires et conditionnements ERP. 152 paramètres `[LABO]` remplacés textuellement par `[valeur à confirmer]` : **aucune valeur ajoutée**.
- Un seul produit n'a pas de conditionnement défini dans la base : `PROOF-PU-SEAL`. Sur le site, le format apparaît comme **à préciser**.
- `src/lib/catalogue-projets.ts` : vérifie exactement 50 slugs distincts et les marqueurs `certifie=false`, `commercialise=false`. Ce chemin est séparé de `src/lib/products.ts` et de la publication certifiée `public/data/products.json`, qui reste `[]`.
- `src/data/catalogue-content.ts` : messages localisés FR/AR/EN et étapes de préparation *génériques*, non quantitatives, par familles techniques ; ce ne sont ni des modes d'emploi spécifiques approuvés ni une traduction validée des 50 modes FR. Les modes français source sont disponibles dans un accordéon avec mise en garde.
- `src/components/ConceptCatalogue.astro` et `src/pages/[lang]/[section].astro` : page Catalogue alimentée en 50 cartes par gamme, navigation native, badge de présentation provisoire.
- `src/pages/[lang]/catalogue/[slug].astro` : 150 pages statiques de description et conditionnements, méthodes indicatives, lien de contact, avertissements techniques.
- CSS responsive / RTL / navigation clavier et tests structurels ; recette Chromium : 50 cartes et 24 parcours de fiches sur bureau/mobile en 3 langues, avec captures.

## Limites d'illustration

Pour le site, l'image affichée reste **une illustration générique de la catégorie** issue des cinq posters 3D existants, accompagnée d'une mention qui interdit de la confondre avec l'étiquette ou le conditionnement précis de la référence. Les 50 images composites WebP de travail sont disponibles dans l'archive de préproduction locale précédente, **mais ne sont pas incorporées dans cette PR**. Qualité photoréaliste 9/10 non prouvée et non annoncée.

## Tests et restrictions

```bash
npm ci && npm run build
python -m unittest discover -s tests -v
python scripts/check_built_pages.py
python scripts/preprod_static_audit.py
python scripts/check_browser_pages.py
```

Maintenir `noindex,nofollow` et `public/data/products.json=[]` ; ne pas activer les formulaires ni l'API leads. Aucune donnée de prix/marge, recette ERP, matière première, fournisseur, secrets ou SQL de certification n'est exportée. **Aucun déploiement Pages, DNS, Access, RLS ou changement ERP** dans cette PR. Ne pas confondre fusion GitHub et mise à jour du domaine public.

## Suite

1. Attester 2 CI vertes sur PR et 2 sur HEAD `main` après fusion.
2. Inspecter les captures des 150 fiches échantillonnées (en particulier textes AR, 320px et bannière).
3. Réaliser l'import propre des 50 photos composites de préproduction vers le dépôt, après contrôle graphique, puis corriger l'aspect trop illustratif. Pour du 9/10 réel, chaque référence exige un packshot produit, bonne géométrie, état de surface, typographie et distinction de formats, sans codes de conformité ou pictogrammes fictifs.
4. Après validation laboratoire, réviser les données individuelles et passer séparément dans le flux certifié ; aucune autorisation implicite en masse.
