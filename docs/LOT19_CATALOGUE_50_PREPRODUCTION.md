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

## Résultat d'exécution complémentaire — Supabase Production

**Écriture effectivement réalisée** sur le projet `wenydirqtmkywbxbxfal` le 1er novembre 2026 : 33 modèles de modes d'emploi fournis par l'Excel, appliqués par ID exact aux **50 fiches** dans la clé JSONB `contenu.fr.mode_emploi_brouillon` de `public.site_produits`. Cette écriture conserve le contenu source avec les repères `[LABO]` et n'affecte aucun statut de confirmation, aucune date de validation ni aucun champ `publie`.

La mise à jour SQL n'était autorisée que pour les 50 lignes `statut_technique=brouillon`, `produit_reel_confirme=false`, `publie=false`, avec une condition transactionnelle exigeant exactement 50 mises à jour (échec et annulation sinon). **Requête de vérification exécutée ensuite** : 50/50 modes FR brouillons présents, 50/50 contiennent `[LABO]`, 50/50 toujours brouillons techniques, 0 confirmés, 0 publiés, 0 FT validées, 0 FDS validées. Les descriptions FR/AR/EN préexistantes ont été conservées.

**Formats illustratifs après nouvelle passe QA** : 16 sacs 25 kg Bond, 14 seaux 20 kg (3 Proof + 11 Paint), 12 bidons 20 L Flow, 7 kits résines dont la contenance est non définie, 1 conditionnement Proof manquant. Les autres formats SKU demeurent listés dans les fiches. Les images sont des concepts non contractuels, **sans classe normative/mentions de sécurité artificielles**, et ne peuvent pas être imprimées comme emballages commerciaux.

### GitHub et contrôles
- [PR #15](https://github.com/Verwolfy/nextgen-website/pull/15) fusionnée sur `main` : commit `c5ef0e2660862238510d811b6649a38107c4590c`.
- Deux CI de PR réussies sur `08af5e48d4ed6d1609dacdb2928a966e0763d957` : [Astro/sécurité](https://github.com/Verwolfy/nextgen-website/actions/runs/41352258702) et [Chromium](https://github.com/Verwolfy/nextgen-website/actions/runs/41352258745).
- Deux CI après fusion réussies au SHA `c5ef0e2` : [Astro/sécurité](https://github.com/Verwolfy/nextgen-website/actions/runs/41352515834) et [Chromium](https://github.com/Verwolfy/nextgen-website/actions/runs/41352515874).
- 50 visuels 900 × 900 WebP contrôlés ; archive privée avec 50 visuels + `index.html` + JSON (52 fichiers), intégrité ZIP vérifiée, classeur enrichi 50 lignes et source Excel conservée.

