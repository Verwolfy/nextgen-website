# Lot 19 — Préparation des 50 fiches catalogue et maquettes emballages

Date : 1er novembre 2026.

## Audit des 50 références
- Fichier utilisateur : `Catalogue_Produits_NextGen_BROUILLON.xlsx`, 50 lignes de données (Bond 16, Proof 11, Flow 12, Paint 11). **Toutes** au statut `BROUILLON – à valider par le laboratoire`.
- Supabase PROD `wenydirqtmkywbxbxfal` : `site_produits` contient 50 fiches, `statut_technique=brouillon` sur 50, `produit_reel_confirme=false` sur 50, `publie=false` sur 50, **0 FT validée, 0 FDS validée** au contrôle. `produits` compte 56 références ERP et `sku_conditionnement` 149 SKU, mais seuls les 50 IDs source font partie du présent lot.
- Source Excel : pour chaque ID une description de travail et un mode d'emploi contenant des variables `[LABO]` ; **aucun dosage, rendement, cure, temps de prise, classe normative ou avis juridique n'est approuvé**. Les normes citées par la source sont des objectifs génériques à vérifier, non des preuves de conformité.
- Conditionnements observés dans Supabase : Bond, sacs de 5/10/25 kg ; Flow, bidons 5/20 L, fûts 200 L et IBC 1000 L ; Paint, seaux 5/10/20 kg ; Proof, seaux 5/20 kg pour certains produits, kits résines à contenance non définie et au moins un produit sans SKU défini. **Les formats sont des entrées de référentiel ERP, pas une preuve d'offre disponible.**

## Livrables internes de conception
- Classeur enrichi `Catalogue_Produits_NextGen_RELECTURE_50.xlsx` : 50 fiches, description issue de l'Excel, mode d'emploi provisoire conservant les `[LABO]`, conditionnement selon les SKU, statut NON PUBLIÉ.
- Archive privée `NextGen_Catalogue_50_PREPRODUCTION.zip` : 50 images WebP de propositions d'emballages, différenciées par code/nom/gamme, une page HTML locale de revue filtrable et un JSON local de 50 fiches. Les images sont issues d'un compositing sur 4 bases de packshots photoréalistes sans prétendre être des emballages effectivement fabriqués.
- Le présent lot GitHub **n'intègre pas** les 50 brouillons dans `public/data/products.json`, qui doit rester `[]` tant que les validations techniques et le contrôle de la publication ne sont pas achevés.

## Code du site et contrôle de publication
- `scripts/sync_catalogue.py` n'autorise désormais la publication d'une fiche qu'avec `mode_emploi` FR/AR/EN non vide, sans `[LABO]` ni HTML, en plus des conditions préexistantes `produit_reel_confirme=true`, `statut_technique=valide`, `statut_commercial=valide`.
- `src/lib/products.ts` requiert `mode_emploi` dans chaque traduction, et `src/pages/[lang]/produits/[slug].astro` l'affiche uniquement pour les produits déjà passés dans le pipeline d'approbation. Libellés FR/AR/EN ajoutés.
- `tests/test_sync_catalogue.py` couvre l'absence de mode, les `[LABO]` et l'injection HTML. Aucune activation de formulaire/CRM, aucun nouveau secret, aucun déploiement Pages.
- Les mentions de préparation `noindex`, protection de sync, produits réels confirmés et absence de prix restent requises.

## Bloquants avant publication des 50
1. Fiches techniques approuvées : caractéristiques, classes et applicabilité, y compris la concordance exacte nom/code/usage.
2. Mode d'emploi définitif de chaque produit : dosage en fonction du conditionnement, préparation support, durée de mélange et temps d'application, sécurité, équipements, séchage/cure.
3. FDS et vérification réglementaire et bilingue pour chaque formulation/étiquette.
4. Conditionnements et matériaux réellement disponibles (kits à définir, incohérences éventuelles entre poids et volumes), photos/packshots validés.
5. Validation qualité, technique et commerciale datée pour chaque fiche, et **protection Cloudflare Access** et revue de diffusion préalable.

Objectif utilisateur : qualité 9/10. **Il s'agit d'un objectif de revue, pas d'un score technique ou graphique indépendant attesté aujourd'hui.** Les simulations sont soumises à approbation humaine.
