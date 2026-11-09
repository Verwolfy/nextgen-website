## 2 novembre 2026 — Lot 24 : les 12 véritables emballages FENEK-FLOW sont sur main

- [PR #19](https://github.com/Verwolfy/nextgen-website/pull/19), garde-fou des 24 assets, fusion `e2052945ce75e3a2227ab89791861951fc56a8c2`; [PR #20](https://github.com/Verwolfy/nextgen-website/pull/20), **24 fichiers binaires réellement transférés**, fusion `f1e0ca10f2a700bfb2a58434fe0c17ae9739d57e`.
- Contrôle réel de l'API GitHub `public/images/catalogue-projects?ref=main` après fusion : **24 WebP, 12 slugs, 1 818 364 octets**, empreintes SHA Git identiques aux sources de l'archive privée de conversation. La prise en charge des images spécifiques et l'absence d'étirement viennent des lots 21–23.
- CI sur tête corrigée de la PR #20 `5890c9531b13c1ee26bef384384a3d35abcfb051` : [Astro/sécurité réussi](https://github.com/Verwolfy/nextgen-website/actions/runs/41453201528), [Chromium FR/AR/EN réussi](https://github.com/Verwolfy/nextgen-website/actions/runs/41453201515). L'échec initial Chromium était une assertion prématurée de `loading=lazy`, réparée avec `await im.decode()`.
- Captures de la recette `41453201515` téléchargées, WR-N inspectée sur desktop français et mobile FR/AR : produit visible, pas de bidon écrasé, avertissement de maquette non contractuelle conservé. `WR-N` bien écrit sur le visuel.
- Relais de transfert privé temporaire utilisé uniquement pour la copie base64 GitHub puis **supprimé**. `scripts/create_flow_packshots_pr.sh` n'est plus nécessaire pour ce lot importé, seulement pour un futur réimport.
- Documentation détaillée : `docs/LOT24_FLOW_12_IMAGES_GITHUB.md`. **Ne pas réutiliser les notes des lots 21–23 « WebP manquants » comme état courant**.
- Le catalogue commercial homologué `public/data/products.json` demeure `[]`; 50 fiches éditoriales de prévalidation. Aucun déploiement Cloudflare ou configuration Access/DNS/ERP/Supabase/secrets déclenché dans cette session. La visibilité sur le domaine public n'a pas été vérifiée.

### Suite immédiate
Attester les 2 CI du dernier `main` après documentation, examiner les 12 rendus sur le domaine réellement déployé si accessible et protégé, puis poursuivre les maquettes des autres gammes avec contrôle technique et commercial avant toute homologation.

---

## 2 novembre 2026 — Lot 22 : packshots FENEK-FLOW vérifiés, upload binaire restant

- [PR #18](https://github.com/Verwolfy/nextgen-website/pull/18) fusionnée sur `main`, commit `5df6b6d773768bf12ee659dc45a6c47a57ad4518`. CI de PR **2/2 réussies** : [Astro/sécurité](https://github.com/Verwolfy/nextgen-website/actions/runs/41443116845), [Chromium](https://github.com/Verwolfy/nextgen-website/actions/runs/41443117048).
- Archive **locale de conversation**, non poussée : `NextGen_FENEK_FLOW_12_packshots_lot21.zip` contenant 12 fichiers 1120×1120 et 12 fichiers 560×560 WebP avec hashes distincts. Audit agrandi de `WR-N` : sa vraie étiquette porte bien « WR-N » (fausse lecture SP-HR sur miniature). Aucun remplacement requis.
- `scripts/flow-packshots-approved.json` : empreintes de 24 images attendues. `scripts/install_flow_packshots.py` : chemins, taille, RIFF/VP8, dimensions, intégrité SHA256 par rapport au référentiel **versionné GitHub**, vérification complète avant écriture et mode `--verify`. `src/lib/catalogue-projets.ts` refuse d'utiliser une variante seule si carte/détail ne sont pas toutes deux présentes. `tests/test_lot21_flow_packshots.py` et `tests/test_lot22_approved_flow_images.py` couvrent les garde-fous.
- **Limite majeure** : `public/images/catalogue-projects/` ne figure pas dans le dépôt : les 24 octets WebP **ne sont pas encore transférés**. Le site utilise encore les visuels génériques de secours. Tests sur PR ne prouvent pas leur publication.
- Prochaine étape : depuis un clone GitHub authentifié, exécuter `python scripts/install_flow_packshots.py /chemin/NextGen_FENEK_FLOW_12_packshots_lot21.zip`, `python scripts/install_flow_packshots.py --verify`, puis committer les 24 fichiers sur branche assets, PR et CI. Ensuite contrôler le rendu réel FR/AR/EN et les proportions des bidons.
- Invariants : présentation éditoriale provisoire des 50 références, non homologation technique ; `public/data/products.json=[]`; aucun prix/dosage/certificat inventé, formulaire ou collecte activé, ni intervention ERP/Supabase/SQL/RLS, DNS, secrets ou Cloudflare Pages/Access.

---

## 1er novembre 2026 — Lot 20 : catalogue de 50 fiches acceptées pour présentation

- Approbation **éditoriale provisoire** demandée par l'utilisateur : les 50 références du classeur Excel et de `public.site_produits` ont été acceptées pour alimenter le site, **révisables ultérieurement**. Ne pas assimiler cet accord à une validation technique ou commerciale.
- **Supabase PROD** projet `wenydirqtmkywbxbxfal` : ajout d'un attribut JSON `contenu.validation_editoriale_projet` sur **50/50** enregistrements, statut `accepte_pour_presentation_provisoire`, date 2026-11-01, révocable. Vérification SQL après écriture : **50 accords, 0 produits confirmés, 0 publiés**, aucun changement RLS, schéma, FT/FDS ou sécurité.
- [PR #16](https://github.com/Verwolfy/nextgen-website/pull/16) **fusionnée** sur `main` au SHA `bc333bf5f208263da130af155ec0dbdc52861ce6`. Elle ajoute les 50 produits de projet en catalogue visible sur les trois langues FR/AR/EN, 150 pages de détail, descriptions spécifiques, formats provenant de SKU Supabase, brouillons FR avec `[valeur à confirmer]`, guides indicatifs AR/EN sans dosage inventé, avertissements non homologués et images génériques.
- Une référence `PROOF-PU-SEAL` n'a pas de format de conditionnement ERP défini : la page signale ce manque, sans inventer de poids. Les formats affichés sont des hypothèses de référentiel, pas des stocks disponibles.
- Code `src/data/catalogue-projets.json`, `src/lib/catalogue-projets.ts`, `src/data/catalogue-content.ts`, `src/components/ConceptCatalogue.astro`, `src/pages/[lang]/catalogue/[slug].astro`, CSS, recette Chromium élargie, `tests/test_lot20_catalogue_projects.py`, documentation `docs/LOT20_CATALOGUE_50_PRESENTATION.md`.
- **2 CI sur PR réussies** : [build Astro/sécurité](https://github.com/Verwolfy/nextgen-website/actions/runs/41354741585) et [Chromium](https://github.com/Verwolfy/nextgen-website/actions/runs/41354741729). CI du dernier `main` à contrôler.
- Catalogue officiel certifié toujours `public/data/products.json=[]`, collecte inactive, `noindex` conservé. Aucune modification DNS/Cloudflare Pages/Access, secret, prix/marge, RLS ou ERP. La fusion sur GitHub ne prouve pas le déploiement du site public.

---

## 1er novembre 2026 — Lot 18 : relecture arabe BTP, audit des captures

- **[PR #14](https://github.com/Verwolfy/nextgen-website/pull/14)** fusionnée sur `main` (merge SHA `1ba3c5088e224ad61f8446840933dc11752dfb4b`) après correction et deux CI réussies sur head `071913a8a2ddb51b901c994f57c24ad11cd7e570` : [Astro/sécurité](https://github.com/Verwolfy/nextgen-website/actions/runs/41349078803) et [Chromium](https://github.com/Verwolfy/nextgen-website/actions/runs/41349079000).
- `AboutStory.astro` : suppression du doublon d'introduction tout en conservant le processus et la réserve sur les services/produits. Tests arabes historiques réconciliés avec les libellés améliorés, ajout `tests/test_lot18_arabic_polish.py` et `docs/LOT18_ARABE_BTP_RELECTURE.md`.
- PR #13 fermée car sa tête PR restait `3ab89d3` malgré une branche mise à jour ; PR #14 a été créée au **SHA final exact** pour déclencher les CI. Ne pas fusionner à nouveau PR #13.
- Les étiquettes imprimées sur les maquettes et autres visuels contractuels restent de simples simulations non approuvées ; validation humaine francophone/arabophone BTP recommandée avant mise en ligne commerciale.
- Invariants conservés : dépôt privé, catalogue `public/data/products.json=[]`, `noindex`, formulaires/API désactivés, aucun prix, certification, FT/FDS ou donnée technique inventé, aucun déploiement Cloudflare ou modification DNS/ERP/Supabase/SQL/RLS/secrets. Les CI `main` après ce journal doivent être vérifiées séparément.

---

## 1er novembre 2026 — Lot 17 : finitions des légendes éditoriales FR/AR/EN

- **[PR #12](https://github.com/Verwolfy/nextgen-website/pull/12)** fusionnée au commit `d817ecee2809a6e02c2323f65772685c180bd51d`.
- Relecture des captures de lot 16 : deux mentions anglaises persistaient sur les pages arabes (**FENEK COLLECTION** sur l'accueil, **NextGen · Design study** sur les emballages). Elles sont désormais localisées FR/AR/EN, sans traduire les noms des marques.
- `src/pages/[lang]/index.astro` : `Collection FENEK / فئات FENEK / FENEK collection`, `dir="auto"`.
- `src/pages/[lang]/emballages.astro` : `Étude de conception / تصاميم أولية / Design study` après la marque NextGen.
- `scripts/check_browser_pages.py` : vérification réelle des légendes arabes en Chromium. `tests/test_lot17_arabic_eyebrows.py` bloque leur régression ; documentation `docs/LOT17_LIBELLES_ARABES.md`.
- **2 CI PR réussies sur head `2684ae0300be1dbc24fa5be978a06074a22dbd0c`** : [Astro/sécurité](https://github.com/Verwolfy/nextgen-website/actions/runs/41348268501) et [Chromium](https://github.com/Verwolfy/nextgen-website/actions/runs/41348268419).
- **Aucun** déploiement Pages/DNS/Access, collecte, changement ERP/Supabase, produit/tarif/FT/FDS commercial ajouté. `public/data/products.json=[]`, `noindex`.
- Dernier SHA `main` après mise à jour documentaire à revalider 2/2. Les étiquettes imprimées en anglais dans les **images de maquettes** sont conservées : composants graphiques non contractuels à revoir ultérieurement avec approbation design, et non texte de l'interface.

---


- **[PR #11](https://github.com/Verwolfy/nextgen-website/pull/11)** fusionnée sur `main`, commit merge `03e8314236a0efaeba2adfbbc976daf69ede08ba`.
- Arabe réécrit : rubriques **الفئات التقنية / الموارد / شبكة التوزيع**, lexique mortiers, colles à carrelage, joints et étanchéité ; textes éditoriaux de gamme / ressources / emballages améliorés, adresse localisée. Marques FENEK protégées du réordonnancement RTL par `bdi dir="ltr"`; distinction correcte de poids kg vs capacité litres.
- **CI PR finale (head `034b33c3d9e71110f2c848196b828dcaf233187b`) 2/2 réussies** : [Astro/sécurité](https://github.com/Verwolfy/nextgen-website/actions/runs/41347775698) et [Chromium](https://github.com/Verwolfy/nextgen-website/actions/runs/41347775713). Captures privées de la première passe de PR (run [41347456040](https://github.com/Verwolfy/nextgen-website/actions/runs/41347456040), artefact `13100166303`) **récupérées et examinées** : affichage de posters confirmé sur `ar-desktop-emballages`, cartes lisibles et bidi correct sur `ar-desktop-gammes`. Les dernières finitions unités/titres ont ensuite obtenu 2 CI vertes.
- **Invariants :** `public/data/products.json=[]`, maquettes non contractuelles, aucun produit/tarif/FT/FDS/certification inventé, formulaires/API de leads désactivés, `noindex`, aucune modification ERP/Supabase/SQL/RLS, secrets, DNS, Cloudflare Pages ni publication.
- **CI après fusion à vérifier distinctement** ; URL publique non vérifiée dans cette session, build GitHub ≠ mise en ligne Cloudflare. Un relecteur arabe professionnel reste recommandé avant approbation commerciale.

---

## 1er novembre 2026 — Lot 14 : parcours Contact et Distributeurs, aucune collecte

- **[PR #9](https://github.com/Verwolfy/nextgen-website/pull/9)** fusionnée sur `main`, commit merge `827adc374685c0193e440b7de7e465afa314d005`.
- Pages Contact et Distributeurs désormais centrées sur **trois canaux directs** (`mailto:`, `tel:`, WhatsApp) dans les trois langues FR/AR/EN. Coordonnées reprises du dictionnaire `brand`, sans inventer d'identités ou de nouveaux numéros. Les liens ouvrent seulement les applications choisies par l'utilisateur.
- Mention explicite que l'e-mail et WhatsApp sont des services externes et que **la réception effective des messages n'a pas été vérifiée** dans cette préproduction. Ne pas présenter un numéro affiché comme testé fonctionnellement.
- `src/components/LeadForm.astro` : champs et bouton **tous désactivés**, désormais contenus dans un accordéon `details` fermé par défaut ; aucune balise `form`, aucun envoi, aucun script, aucun nouvel appel API.
- Sur Distributeurs, CTA prioritaire vers les canaux actifs et second lien vers l'aperçu de candidature désactivé. Nouveaux fichiers : `src/components/ContactChannels.astro`, `src/data/contact-channels.ts`, `tests/test_lot14_contact_journey.py`, `docs/LOT14_PARCOURS_CONTACT_DISTRIBUTEURS.md`. CSS responsive/RTL/focus.
- Recette Chromium élargie : liens e-mail/téléphone/WhatsApp, absence de formulaire actif, contrôles disabled, affichage replié / ouvert, absence de débordement à 390px et 320px, captures internes supplémentaires Contact/Distributeurs. Mise à jour `tests/test_lead_forms.py` conformément à la séparation des canaux et de l'aperçu.
- **2 CI sur PR réussies avant fusion**, head `d2933640e630a09d9ec943718e4ff2d78c080155` : [Astro + sécurité](https://github.com/Verwolfy/nextgen-website/actions/runs/41338615668), [Chromium](https://github.com/Verwolfy/nextgen-website/actions/runs/41338615721).
- **Aucun** produit, prix, dossier fiscal/comptable, qualification réglementaire ou FT/FDS inventé ; `public/data/products.json = []`. Réception `/api/lead` non activée. **Aucun** SQL/RLS, secret, ERP, DNS, Cloudflare Pages ou Access modifié. Publication Cloudflare et collecte restent NO-GO sans approbations.

### Suite prioritaire
Vérifier les CI du dernier commit `main` après mise à jour du journal, consulter les captures du parcours Contact en particulier à 320px FR/AR/EN, puis préparer les prérequis de confidentialité et la protection effective Cloudflare Access **avant tout déploiement**.

---

## 1er novembre 2026 — Lot site 13 : accueil contrôlé visuellement

- **[PR #8](https://github.com/Verwolfy/nextgen-website/pull/8) fusionnée**, SHA merge `6e11017b227a1bcbbf0f1951c2133daa144205cf`.
- **21 captures privées du lot 12 réellement récupérées et étudiées** depuis le run Chromium [41331800296](https://github.com/Verwolfy/nextgen-website/actions/runs/41331800296), artefact GitHub ID `13093227397`. Constats : navigation mobile lisible, mascottes auparavant mal intégrées au fond sombre, pays non localisé en AR/EN et rubrique `LAB · FIELD · TRAINING` pouvant suggérer une offre technique active.
- Réponse de code : `src/data/editorial.ts` et `src/pages/[lang]/index.astro` — repère géographique FR/AR/EN, état explicite **site en préparation, aucun produit réel approuvé**, CTA direct « Nous contacter » (et équivalents AR/EN), approche présentée comme démarche **proposée** avec réserve sur les services et les résultats labo.
- CSS `src/styles/site.css` : mise en scène volontaire des portraits blancs d'origine dans un cadre clair arrondi ; assets sources conservés strictement inchangés. Contrôles `tests/test_lot13_home_visual.py` et `scripts/check_browser_pages.py` incluant 320px, en plus des contrôles 390px.
- **2 CI PR réussies sur `a676a69584ba639b16e33575573dc8baaf1d3e75`** : [build/sécurité](https://github.com/Verwolfy/nextgen-website/actions/runs/41332623363), [Chromium](https://github.com/Verwolfy/nextgen-website/actions/runs/41332623414). Artefact de **24 captures** après correction, ID `13093838508`, téléchargé et inspecté (FR/AR et vues 320px + desktop) : cadrage mieux intégré et statuts lisibles. Les captures 320px montrent le menu déplié volontairement après interaction de recette.
- Documentation `docs/LOT13_AUDIT_VISUEL_ACCUEIL.md` ; aucune publication Cloudflare, données métier, tarifs, fiches non approuvées, SQL, secret, collecte ou permission modifiés.
- **CI de fusion et du dernier commit `main` à contrôler** séparément des CI sur PR. Capture Chromium et build réussi ne prouvent pas le déploiement Cloudflare ; lancement/publication soumis aux validations Access + juridique.

---

## 1 novembre 2026 — Priorité site, lot 12 : pages Gammes, À propos, Ressources

### Changements réels
- [PR #7](https://github.com/Verwolfy/nextgen-website/pull/7) fusionnée sur `main` (commit de fusion `9f35c1a71c350613830423d59efe44593b3014b0`).
- Trois composants nouveaux : `RangeOverview.astro`, `AboutStory.astro` et `ResourcesHub.astro`. Les pages centrales sont plus lisibles et utilisables sur mobile ; aucune fausse FT/FDS cliquable.
- `src/pages/[lang]/gammes/[slug].astro` enrichi pour 4 gammes × 3 langues ; maintien du message « catalogue en préparation » en l'absence de produits approuvés.
- CSS responsive (320/390 px, RTL, focus clavier, mouvement réduit) et recette Chromium étendue de **30 à 48 combinaisons** route/langue/format, avec captures internes additionnelles Gammes/À propos/Ressources.
- `tests/test_editorial_hubs.py`, `tests/test_mobile_navigation.py` adapté après déplacement de l'image des mascottes dans le composant À propos. Documentation `docs/LOT12_HUBS_EDITORIAUX_FR_AR_EN.md`.
- **CI sur PR après correction :** [build/sécurité](https://github.com/Verwolfy/nextgen-website/actions/runs/41331612676) `completed/success` et [recette Chromium](https://github.com/Verwolfy/nextgen-website/actions/runs/41331612642) `completed/success`. Les CI après fusion doivent être attestées distinctement.

### Interdictions préservées
- Aucun ajout à `public/data/products.json` (`[]`), aucun SKU produit ni prix, aucun résultat labo ou homologation, aucune FT/FDS inventée.
- Formulaires B2B et backend de collecte **inactifs** ; ni accès client Supabase, ni secrets modifiés.
- Aucun changement SQL/RLS/GRANT, DNS ni publication Cloudflare. Le site reste **NO-GO pour toute mise en ligne publique** tant que les domaines `pages.dev`/previews ne sont pas effectivement protégés par Access et que les validations juridiques/métier restent ouvertes.

### Suite
1. Contrôler les CI des derniers commits `main` et les captures internes des pages enrichies.
2. Continuer l'amélioration visuelle sans publier les données non qualifiées.
3. Conserver un jalon explicite avant toute configuration Cloudflare, collecte ou annonce de disponibilité des produits.

---


### Développements fusionnés sur `main`
- **Lot 10, navigation mobile accessible** : PR [#5](https://github.com/Verwolfy/nextgen-website/pull/5), commit `875ec757c3c642ec9a5f3e6d75ae9ff62d2146cd`. Menu natif `details/summary` sans JS sous 980px, rubriques Ressources incluses, support clavier et RTL, lisibilité à 320px, focus visible, libellés et textes alternatifs FR/AR/EN.
- Lot 10 **CI sur la fusion** : [build/sécurité](https://github.com/Verwolfy/nextgen-website/actions/runs/41329332313) et [Chromium](https://github.com/Verwolfy/nextgen-website/actions/runs/41329332312) : `completed/success`. Un premier test de navigation trop immédiat a été corrigé avec `wait_for_url` avant la fusion.
- Lot 11 **CI sur la branche PR** : [build/sécurité](https://github.com/Verwolfy/nextgen-website/actions/runs/41329533696) et [Chromium](https://github.com/Verwolfy/nextgen-website/actions/runs/41329533617) : `completed/success`. Les contrôles du commit de fusion doivent être confirmés séparément.
- Tests nouveaux : `tests/test_mobile_navigation.py`, `tests/test_home_showcase.py` ; recette navigateur élargie. Documentation : `docs/LOT10_NAVIGATION_MOBILE.md`, `docs/LOT11_ACCUEIL_GALERIE_3D.md`.

### Garde-fous inchangés
- `public/data/products.json` reste `[]`. Pas de produit fictif, de tarif ni de garantie technique ou homologation inventée.
- Formulaires de devis et distributeurs **désactivés** ; réception des demandes inactivée. Pas d'échange automatique de données ERP ou Supabase au navigateur.
- **Aucun déploiement Cloudflare, DNS, activation de collecte, modification RLS/GRANT, migration SQL ou secret**, et aucune approbation juridique prétendue.
- La CI GitHub prouve un build statique contrôlé, **pas** une mise en ligne effective. Le site reste en développement, déploiement externe NO-GO jusqu'à protection Access et validations métier/juridiques.

### Prochaine priorité site
1. Confirmer les CI du dernier commit `main`.
2. Revoir les captures internes desktop/mobile après la galerie et corriger d'éventuels défauts visuels réels.
3. Préparer la préproduction accessible uniquement après protection Cloudflare Access explicitement confirmée pour URL principale et previews ; vérifier la partie légale avant collecte ou publication officielle.
4. Poursuivre le contenu FR/AR/EN, mais uniquement sur des caractéristiques et produits documentés.

---

# NEXTGEN — Etat d'avancement (Phase 4, lot 1)

Date : 31 octobre 2026. Décisions : **GO PHASE 4** reçu ; **SQL VALIDÉ** reçu et migration privée du site appliquée sur la production Supabase.

## Résultat vérifié

- Dépôt de travail local `nextgen-website` créé, distinct de `erp-mortier`, **pas encore sur GitHub**.
- SQL `001_site_publication_PROPOSITION_NON_EXECUTEE.sql` approuvé par « SQL VALIDÉ », puis **appliqué sur la production** sous migration `20261031204336_nextgen_site_publication_private_20261031`. Fichier initial conservé à titre d'archive source ; ne pas le rejouer.
- Schéma proposé protège les six `PF-001..006` tests : exclusion, statut réel confirmé et double validation obligatoires, vue export sans rôle anon.
- `scripts/sync_catalogue.py` créé : lecture API privée avec `service_role`, filtrage précis, validation 3 langues, copie d'assets depuis le même Supabase Storage seulement, aucune redirection HTTP, plafonds de taille et contrôle de signatures.
- `.github/workflows/sync-site.yml` : nuit + déclenchement manuel + `repository_dispatch` ; GitHub Secrets requis. **Aucun workflow distant exécuté.**
- Support : 5 masters SVG + 5 rendus PNG ; 9 PDF FT brouillon + HTML éditables ; 3 PDF trames FDS vierges + HTML ; charte PDF + HTML + tokens JSON.
- `public/data/products.json` = `[]` : **aucun produit ERP fictif exposé**.
- Logo original (`Logo1.jpg`) inséré tel quel comme asset binaire dans les SVG, comparé à la source dans les tests.
- Contrôles PDF : 12 documents PDF d'une page, ouvrables, texte disponible, PDF arabe rendu RTL et visuellement contrôlé ; feuille charte PDF une page.
- Unittest local : **19 réussites, 0 échec**. Tests avec maquettes HTTP, pas de test d'accès réel à une vue inexistante.

## Vérifications non réalisées / non revendiquées

- Pas de dépôt GitHub distant (outil GitHub fourni sans action de création de dépôt, et dépôt cible absent à la lecture).
- Table `public.site_produits` et vue `public.site_products` **créées et contrôlées en production** ; aucun secret GitHub configuré, aucune publication Cloudflare.
- Pas de synchronisation de données réelles : la table de publication et la vue sont vides ; les 6 produits ERP restent fictifs et exclus par contrainte.
- Pas de validation juridique des FDS / FT / identité de marque.
- Pas de test Lighthouse, site Astro (lot 2), formulaire ou ERP Streamlit (lot 3), DNS (lot 4).

## Blocages exigeant autorisation

1. **Autorisation SQL obtenue et exécutée.** Toute modification additionnelle du schéma / GRANT / RLS requiert une nouvelle approbation explicite.
2. Compte GitHub : créer un dépôt **privé** `Verwolfy/nextgen-website`, `main`, puis importer l'archive (ou fournir un outil GitHub disposant du droit `create repository`).
3. Les secrets `SUPABASE_URL` et `SUPABASE_SERVICE_ROLE_KEY` seront configurés uniquement dans GitHub Secrets, après revue sécurité.

## Prochaine action

Créer le dépôt GitHub privé dédié (indisponible via le connecteur actuel), y pousser les livrables et configurer les secrets côté GitHub après revue ; puis lot 2 : Astro et premières pages trilingues. Tester la requête REST avec la vraie clé serveur dans un environnement sécurisé, ainsi que le refus REST anonyme, dès que l'infrastructure est disponible. Aucune mise en ligne publique sans approbation distincte.

## Validation SQL production — 31 octobre 2026

- Accord explicite utilisateur : **« SQL VALIDÉ »**.
- Projet : `wenydirqtmkywbxbxfal` (PRODUCTION).
- Migration enregistrée : `20261031204336_nextgen_site_publication_private_20261031` ; réponse de l'outil `apply_migration` : `success=true`.
- `public.site_produits` existe, RLS `true`, 0 ligne, aucune politique RLS.
- `public.site_products` existe, option `security_invoker=true`, 0 ligne.
- `anon` : `SELECT`, `INSERT`, `UPDATE`, `DELETE` refusés sur la table et la vue ; `authenticated` : `SELECT` refusé. `service_role` : `SELECT` autorisé.
- Toutes les **89 / 89** tables `public` ont le RLS activé ; **0** table lisible directement par `anon`.
- Tables ERP `produits` et `sku_conditionnement` inchangées : **6 produits et 7 SKU**.
- Contraintes présentes : interdiction `PF-001` à `PF-006` ; double validation ; drapeau réel ; contrôle des PDF validés.
- Conseiller Supabase : 85 avis **INFO** `rls_enabled_no_policy`, aucun WARN/ERROR. [Explication](https://supabase.com/docs/guides/database/database-linter?lint=0008_rls_enabled_no_policy).
- Tests locaux relancés : `python -m unittest discover -s tests -v` → **19 tests OK** ; `python scripts/check_public_content.py` → `0 approved products, no forbidden fields`.
- Vérification API REST avec les vrais jetons non réalisée (secrets non disponibles dans cette session). Pas de Cloudflare / DNS / déploiement.

## 31 octobre 2026 — Dépôt du site créé

- `Verwolfy/nextgen-website`, privé, branche `main`, accès en écriture vérifié.
- Import des sources du lot 1 en cours ; les assets binaires internes non validés sont volontairement séparés du site public.
- Prochaine étape : import source, vérification du commit distant et CI ; puis lot 2 Astro.
- Aucune nouvelle modification SQL / ERP / DNS dans cette étape.

## Lot 2 — base Astro éditée, non déployée

- Ajout squelette Astro 6.4.6, 3 langues, 4 gammes, catalogue vide, pages produit statiques générées uniquement depuis JSON approuvé.
- Aucun formulaire actif, aucun prix, aucune mention ISO ni référence chantier inventée.
- Source du logo officielle, duo Nexo/Geno transféré en version WebP optimisée.
- CI GitHub prévue pour installer dépendances et tester le build. En attente de preuve CI.
- Statut public: BLOQUÉ en attente approbation DNS, documents légaux, sécurité des formulaires.

## 31 octobre 2026 — GitHub confirmé, site en lot 2

- Dépôt : `Verwolfy/nextgen-website` privé, branche `main`, sources du lot 1 et assets vérifiés sur GitHub.
- Commit Astro `0d5d8a3883436af2c0447901003dc57288314dd4`, CI `41242720347` **completed/success**, tests Python, installation npm, build Astro et assertions de non-publication réussis.

## 31 octobre 2026 — verrouillage npm confirmé

- Workflow lockfile `41242871708` : completed/success, commit automatique du `package-lock.json`, SHA main `5c82718e9f35b3613bf5813114ad0ea5806c1b26`.
- Workflow Astro `41242871617` : completed/success, tests et compilation statique sur commit `0b046a01...` ; 28 tests locaux réussis.
- Build CI passe désormais à `npm ci` pour imposer le lockfile. Aucune publication Cloudflare/DNS.


- Génération locale de cinq modèles GLB (sac 25 kg, seau 20 kg, bidon 20 L, fût 200 L, cuve IBC 1000 L), tous <3 Mio et validés par import trimesh ; géométrie simplifiée non contractuelle.
- Textures d'étiquettes provenant des originaux de la phase 1, logo utilisateur inchangé ; étiquettes explicitement fictives.
- Deux angles rendus pour chaque modèle, PNG et WebP ; optimisation légère pour les mobiles.
- Page Astro de présentation conceptuelle FR/AR/EN et visionneuse réutilisable uniquement pour modèles source approuvée dans les fiches produits.
- `@google/model-viewer` et `three` fixés dans les dépendances du site ; fichier lockfile GitHub doit être régénéré en CI.
- Tests locaux `python -m unittest discover -s tests -v` : 34 réussis ; cela ne prouve pas encore le nouveau build CI ni l'interface réelle.
- Aucune modification de Supabase, du dépôt ERP, Cloudflare ou du DNS ; aucune fiche fictive publiée.
- Prochaine action : transfert GitHub des sources et binaires, validation CI `npm ci` + build trilingue + vérification post-build des 5 GLB/10 WebP. Ensuite, tests navigateur et éventuel déploiement de prévisualisation protégé avant feu vert public.


- Modèles indicatifs et non contractuels : sac 25 kg, seau 20 kg, bidon 20 L, fût 200 L, IBC 1000 L ; texture issue des vraies étiquettes NG (logo utilisateur conservé).
- CI `41244943125` **completed/success** : 34 tests Python, npm ci, build Astro FR/AR/EN, GLBs et aperçus dans dist, garde d'exclusion produits fictifs. https://github.com/Verwolfy/nextgen-website/actions/runs/41244943125
- Dépendances verrouillées : `@google/model-viewer@4.4.0` / `three@0.183.0`, correction d'un conflit ERESOLVE initial. Sources dans `docs/LOT2_3D.md`.
- Aucun déploiement, DNS, accès public Cloudflare, changement Supabase ou ERP. Vérification en navigateurs réels et rendus photoréalistes à réaliser ultérieurement.

## 31 octobre 2026 — Lot 3 : formulaires et backend B2B préparatoire

- Formulaires distincts devis / candidature distributeur intégrés en FR/AR/EN dans `src/components/LeadForm.astro` et `src/data/lead-forms.ts`. Tous les champs, la case de consentement et le bouton sont **désactivés** ; aucun envoi ni collecte depuis le navigateur. Contacts `mailto:` / WhatsApp disponibles.
- Commit formulaires `5ad6766d3e291f056605de6806a0d8fee2416bca`. Preuve : CI https://github.com/Verwolfy/nextgen-website/actions/runs/41245582877 **completed/success** (38 tests Python, build Astro, contrôles sécurité).
- Endpoint Cloudflare Pages `functions/api/lead.js` ajouté au commit `6da7f865edac83ed56ce9a16a0e18969145454d5` : **503 par défaut**. Pas d'écriture ni d'e-mail ; protection origine + JSON limité + consentement + Turnstile et serveur secret requis seulement après activation volontaire.
- Schéma `sql/003_site_demandes_PROPOSITION_NON_EXECUTEE.sql` : **non appliqué en PROD**. Les évolutions RLS/GRANT doivent recevoir autorisation spécifique. Aucune table CRM existante modifiée.
- CI du backend https://github.com/Verwolfy/nextgen-website/actions/runs/41245795152 **completed/success** : 38 tests Python et 6 tests Node simulés, `npm ci`, build trilingue, vérifications d'absence de contenu fictif public.
- Prochaines tâches : validation juridique de l'information/consentement et de la durée de conservation, revue du SQL, tests de préproduction, Turnstile et anti-abus, workflow CRM après qualification humaine, test multi-navigateurs / mobile / accessibilité. Aucun déploiement Cloudflare ou DNS autorisé à ce stade.

## 31 octobre 2026 — Application autorisée SQL 003 en production

- Accord utilisateur : **« SQL 003 VALIDÉ »**. Projet Supabase PROD : `wenydirqtmkywbxbxfal` ; projet TEST inchangé.
- Migration **appliquée**, résultat `success=true` : `20261031220121_nextgen_site_demandes_private_20261031` ; SQL source : `sql/003_site_demandes_PROPOSITION_NON_EXECUTEE.sql` (nom historique conservé, **ne pas rejouer**).
- Création **additive** de `public.site_demandes` (20 colonnes) et `site_demandes_statut_cree_idx`. **0 ligne**, aucune demande réelle ou simulée introduite. Aucune table ERP préexistante touchée.
- Post-contrôles SQL : RLS activé, 0 politique publique, accès SELECT/INSERT/UPDATE/DELETE refusé à `anon` et `authenticated` ; `service_role` dispose d'accès serveur. 90/90 tables du schéma `public` avec RLS, 0 table publique directement lisible par `anon`.
- **Réserve de privilèges :** les privilèges par défaut Supabase ont conservé `DELETE` et `TRUNCATE` (ainsi que d'autres droits) à `service_role` malgré l'intention `GRANT SELECT, INSERT, UPDATE` du SQL. **Aucun REVOKE correctif appliqué** : changement supplémentaire de GRANT/ACL soumis à autorisation distincte.
- Conseiller Supabase : 86 avis INFO `rls_enabled_no_policy`, aucun WARN/ERROR. https://supabase.com/docs/guides/database/database-linter?lint=0008_rls_enabled_no_policy
- Site et backend : `functions/api/lead.js` renvoie toujours **503** sans `NEXTGEN_LEADS_ENABLED=true`, formulaires Astro désactivés. Aucun e-mail envoyé, aucune mise en ligne Cloudflare, aucun DNS touché.
- **À faire avant collecte réelle** : notice confidentialité et version approuvée, registre des traitements, durée de conservation, revue transfrontalière, secrets serveur + Turnstile, limitation de débit, tests en préproduction et revue opérateur CRM. Les tests d'intégration REST avec clés réelles ne sont pas réalisés.

## 31 octobre 2026 — Lot 4 : préparation CRM, contrôle anti-abus et confidentialité

- SQL 003 **déjà appliqué** sous migration `20261031220121_nextgen_site_demandes_private_20261031`. Aucun nouveau SQL, DML, GRANT ou RLS exécuté durant ce lot. Dernier relevé SQL en lecture seule : `site_demandes=0`, `site_products=0`.
- `scripts/crm_qualification.py` : outil **lecture seule** de métadonnées B2B `demande_id,type_demande,statut,cree_le` avec résumé de volumes non nominatif ; projet de conversion vers `clients` et `interactions` **sans écriture** et avec approbation humaine.
- `functions/api/lead.js` : toujours inactif par défaut (503) ; ajoute `NEXTGEN_EXPECTED_HOSTNAME` et `NEXTGEN_TURNSTILE_ACTION` obligatoires, compare aussi l'hostname/action Siteverify et borne les appels réseau à 8 secondes.
- `docs/CONFIDENTIALITE_BROUILLON_FR_AR_EN.md` : notice trilingue uniquement interne, **non validée et non publiée** ; les informations légales, durée de conservation et transferts restent à confirmer.
- `docs/LOT4_CRM_GOUVERNANCE.md` et `docs/LOT4_POINT_INTEGRATION_ERP.md` : gouvernance et lecture seule du CRM existant dans `Verwolfy/erp-mortier` ; aucun code ERP modifié.
- Commit de code `8ed290c3bb97c0a802185ec0706bb2b0868f4975` ; CI https://github.com/Verwolfy/nextgen-website/actions/runs/41246868156 **success** : **47 tests Python + 9 tests JavaScript, build Astro, garde de non-publication**.
- Second commit documentaire `4d3701d2d54ee489912f901132df3ca4580703fd` ; aucun déploiement Cloudflare/DNS, aucun formulaire actif, aucun envoi d'e-mail, aucun produit fictif publié.
- Point critique inchangé : `service_role` conserve des droits `DELETE` et `TRUNCATE` par héritage Supabase. Changement ACL seulement après autorisation SQL distincte.
- Prochain lot : panneau CRM ERP en lecture seule puis workflow de qualification à double contrôle ; validation juridique, anti-abus, préproduction et tests réels avant toute activation commerciale.


## 1 novembre 2026 — Lot 5 : onglet NextGen dans le CRM ERP

- ERP : \`Verwolfy/erp-mortier\`, PR [#31](https://github.com/Verwolfy/erp-mortier/pull/31) **fusionnée** sur \`main\`, commit \`6a64c882f00ce6f295e98eead3ba856fe3a6e67e\`.
- Nouvel onglet « Demandes NextGen » ajouté dans \`modules/crm/views.py\`. Service \`modules/crm/site_requests.py\` en lecture seule.
- **Activation BLOQUÉE par défaut** : \`[nextgen] crm_inbox_read_enabled=true\` dans les secrets Streamlit sera nécessaire **après** validation de l'information juridique, des permissions et des tests d'exploitation. Le flag n'a pas été configuré.
- Requête privée limitée à \`demande_id,type_demande,statut,cree_le\` et 100 lignes visibles ; aucun champ de coordonnées personnelles demandé, aucun client ou opportunité créé.
- Sécurité : revalidation du compte actif depuis \`users\`, droit \`CRM/lecture\` frais, refus sans session et sur erreur, aucun SQL et aucune écriture CRM.
- CI ERP ciblée : https://github.com/Verwolfy/erp-mortier/actions/runs/41293090843 (31 tests réussis).
- CI ERP complète : https://github.com/Verwolfy/erp-mortier/actions/runs/41293155671 (**2102 tests réussis**, 2 avertissements non bloquants).
- Base Supabase PRODUCTION inchangée. Le site Web Cloudflare, les formulaires et la synchronisation publique restent inactifs. Prochaine phase : notice + base légale et conservation validées ; audit accès détaillés ; workflow de qualification humaine ; tests en préproduction.

## 1 novembre 2026 — Lot 6 : préproduction sans collecte
- ERP PR #32 fusionnée : deux verrous secrets obligatoires et stricts pour lire la boîte CRM.
- Streamlit : observation GitHub anonyme HTTP 303 ; déploiement réel après connexion non confirmé.
- Cloudflare : endpoint sécurisé avec rate-limiter obligatoire/HMAC et projet Supabase précisément épinglé ; formulaires restent désactivés.
- Supabase : aucune écriture ni migration SQL supplémentaire.
- Critères de lancement : docs/LOT6_PREPRODUCTION_GATE.md ; NO-GO collecte.


## 1 novembre 2026 — Lot 8 : portes de préproduction (NO-GO déploiement)

- PR site [#2](https://github.com/Verwolfy/nextgen-website/pull/2) **fusionnée** sur `main`, commit `d91e5715d3911e68061b537430200fbdf9ce8e76`.
- `public/_headers` : nosniff, anti-iframe, referrer-policy, permissions-policy et X-Robots-Tag noindex. **N'est PAS un contrôle d'accès**.
- `scripts/preprod_static_audit.py` : vérifie 42 pages générées, catalogue vide, form désactivé, 5 GLB et absence d'artefacts internes dans `dist`, génère SHA-256 sans réseau.
- `.github/workflows/preprod-build-only.yml` : build & garde-fous, archive **uniquement le manifeste privé interne**, jamais de commande Wrangler/API Cloudflare.
- `tests/test_preprod_static_audit.py` : tests unittest sur les headers et restrictions de formulaires.
- **CI PR** : `41297423184` Astro + sécurité et `41297423154` build-only : success ; dernier contrôle post-fusion à enregistrer.
- Cloudflare Pages : les previews sont publiques par défaut ; Cloudflare Access doit être établi AVANT de créer ou connecter le site. L'Access de preview ne protège pas automatiquement le domaine principal pages.dev. `docs/LOT8_CLOUDFLARE_PREPROD.md` détaille les vérifications et les autorisations.
- Streamlit ERP : observation anonyme HTTP **303**, déploiement de l'onglet après authentification **non vérifié**.
- Aucun appel Cloudflare, aucune migration/écriture Supabase, aucun secret, aucune collecte, aucune modification DNS ni publication réelle.

## 1 novembre 2026 — Lot 9 : contrôles d'accès préproduction et repère ERP

- Site PR [#3](https://github.com/Verwolfy/nextgen-website/pull/3) **fusionnée** en squash : `c1f12d85499f42d48056ba2e0b78cd77808fa160`.
- Six tests offline nouveaux sur les hostnames, redirections Access, erreurs anonymes et déploiements non autorisés ; CI PR `41298541770` **success**. Contrôle intégré au workflow principal.
- Site : `audit_preview_access.py` valide les origines hors réseau par défaut, puis seulement avec `--execute` peut lancer des GET anonymes sur des domaines Pages précisément fournis. Pas de Cloudflare intégré ni de domaine de test connu ; **aucun GET réel effectué**.
- ERP : PR [#33](https://github.com/Verwolfy/erp-mortier/pull/33) **fusionnée**, commit `222bffb7e10f4c244475390d3f63cacc979e8d68`. Onglet CRM avec `SOF-NEXTGEN-CRM-20261101-L9`, sans ouverture du flag ni données privées.
- ERP CI `41298643013` **success** : 37 tests ciblés et **2 144 tests ERP**, 1 warning non bloquant. Présence effective dans Streamlit Cloud toujours non confirmée (HTTP 303 anonyme).
- Préproduction Access, publication Cloudflare Pages, DNS, SQL, secrets, e-mails et formulaire de collecte : **aucune activation**. Conformité juridique et durée de conservation toujours à approuver.


## 1 novembre 2026 — Remplacement opérationnel du catalogue ERP PROD à partir du fichier Excel

- Commande explicite : **« écrase les produits et matières premières déjà présents dans la bdd principale avec les nouvelles références. valide tous les produits ajoutés »**.
- Source : `Catalogue_Produits_NextGen_BROUILLON.xlsx` ; SHA-256 `f932299f798145e0a7e9d6d3ea4337ea5766e72f2492dcf50d08e0890ef0474d`.
- Import transactionnel DML **exécuté avec succès** dans Supabase PROD `wenydirqtmkywbxbxfal`. SQL historique `nextgen_import_catalogue_prod_DML_20261101.sql` stocké dans le dossier de reprise, **ne pas réexécuter**.
- 50 références FENEK actives dans `produits` (Bond 16, Proof 11, Flow 12, Paint 11). La demande utilisateur constitue une **approbation commerciale du catalogue ERP**, pas une preuve technique de conformité/laboratoire.
- 97 familles/matières premières candidates ajoutées en `NG-MP-001` à `NG-MP-097` avec `actif=NON` et sans fournisseur, prix, HS code, stock fictif, grade, recette, dosages ou unité de stockage inventés.
- Les six `PF-001..PF-006` et douze `MP-001..MP-012` existants sont passés en `actif=NON`, **conservés physiquement** car des SKU, factures, commandes, stocks, recettes et mouvements les référencent. Aucune suppression de transactions ni réattribution d'identifiants.
- 50 fiches `site_produits` privées insérées ; `statut_commercial=valide`, `statut_technique=brouillon`, `produit_reel_confirme=false`, `publie=false`. Vue `site_products` : **0 produit**. Aucune classe normative, performance, conformité, FT ou FDS validée.
- Corrections d'import consignées : `PROOF-PU-INJ` et `PROOF-PU-SEAL` reclassées dans les résines polyuréthane, sans modifier le classeur source.
- Post-contrôle DB : 50 actifs + 6 inactifs produits, 97 nouvelles matières candidates + 12 anciennes inactives, recettes 1, lignes recette 2, anciens SKU 7, ordres fabrication 1. Liens historiques toujours présents ; 90/90 tables publiques RLS, aucune table lisible directement par `anon`.
- Référentiel détaillé des produits et matières dans `docs/catalogue-interne/` (dépôt privé GitHub), **jamais copié vers `public/` ou `dist/`**. Contenu français source, traduction générique AR/EN non validée, valeurs `[LABO]` restant à déterminer.
- Restent : confirmer réalité des produits, qualité et provenance des matières, recettes et essais laboratoire, véritables traductions, emballages / SKU et documents techniques avant de libérer la publication. Aucun formulaire ni Cloudflare DNS activé.


## 1 novembre 2026 — Traductions des 50 fiches et prévisualisation interne

- Le classeur source `Catalogue_Produits_NextGen_BROUILLON.xlsx` et les 50 fiches FR ont servi à générer 50 traductions **spécifiques** AR/EN ; textes non validés par traducteur technique ni laboratoire.
- Supabase PROD `wenydirqtmkywbxbxfal` : mise à jour **strictement de la colonne `contenu`** sur les 50 lignes de `site_produits` en transaction ; préconditions obligatoires : `statut_commercial=valide`, `statut_technique=brouillon`, `publie=false`, `produit_reel_confirme=false`. Exécution SQL : 50 lignes modifiées, 0 produit publié.
- Post-contrôle sur Supabase : 50/50 fiches protégées et spécifiques en FR/AR/EN ; **0 lien externe** pour des PDF/visuels/GLB non approuvés ; la vue publiable reste vide par construction.
- `docs/catalogue-interne/fiches_..._TRILINGUES_NON_PUBLIEES.json` : 5 lots de 10 contenus privés. `docs/catalogue-interne/conditionnements_50_A_CONFIRMER.json` : hypothèses sans poids, volume ou SKU confirmé.
- `tests/test_private_catalogue_drafts.py` : tests de 50 IDs uniques, langue, avertissement laboratoire, absence de publication et de faux conditionnements. Tous les contrôles Astro/Chromium du commit `229cddcc949e810ba81f4c42d4b6940bdf8e30c3` sont passés.
- Livrables hors du répertoire `public/` : HTML filtrable pour revue interne des 50 fiches, PDF imprimable de 50 pages FR/AR/EN avec logo original et mention **BROUILLON — NON HOMOLOGUÉ** ; aucun PDF officiel FT/FDS créé, aucune documentation prétendument certifiée.
- Les 97 matières premières restent des familles candidates et ne sont pas publiées. Confirmer fournisseur, grades, emballages, résultats labo, conditionnements SKU réels, traduction professionnelle, noms/classes normatives avant tout GO public.


## 01/11/2026 — Lot Cloudflare : prête pour connexion Git, non déployée

- PR #4 fusionnée, commit `f3038b79449b85f8bccf954e081f2f7f1769b51c`.
- Fichier `.node-version` = 22.23.4 et `public/_routes.json` inclut seulement `/api/lead`.
- Test `scripts/check_cloudflare_release.py` valide répertoire de compilation, routes, 3 langues, aucune fiche publique, API fail-closed, zero formulaires actifs.
- CI site post-fusion `41311184684` : **success** ; artifact GitHub privé `nextgen-cloudflare-dist-review` généré (68 fichiers, statique uniquement).
- Procédure dédiée `docs/DEPLOIEMENT_CLOUDFLARE_RUNBOOK.md` et README mis à jour.
- Compte Cloudflare non connecté ; aucun déploiement, DNS, secret, activation Leads ou modification Supabase n'a eu lieu.
- **Blocage résiduel** : relier le compte Cloudflare et établir Access pour les origines pages.dev si la préproduction doit être privée, puis confirmer les comptes autorisés et contrôler l'URL réelle.


## 02/11/2026 — Lot 26 : accès direct aux cinq GLB de conception

- Tests ajoutés et étendus : `tests/test_lot26_individual_3d.py`, `tests/test_home_showcase.py`, `scripts/check_built_pages.py`, `scripts/check_browser_pages.py`. Documentation : `docs/LOT26_VISIONNEUSES_3D.md`.
- Aucune publication Cloudflare/DNS/Access, aucune écriture Supabase/ERP, aucun produit publié, aucun formulaire activé.
- Suite : confirmer le succès des deux CI sur le même SHA, fusionner la PR, revérifier `main`, puis importer les 20 WebP BOND uniquement depuis le ZIP approuvé. Toute mise en ligne requiert la protection Access réelle et les validations commerciales/juridiques.

## 09/11/2026 — Lot 118 : recherche globale indexée (option B)
- Choix utilisateur validé : loupe animée près du logo, panneau déroulant, filtres Produits / Applications / Fiches produit / Pages, FR/AR/EN.
- Implémentation sur branche `feat/lot118-global-pagefind-search-20261109` : composant `SiteSearch.astro`, configuration Pagefind v1.5.2 après build Astro, classement par type et UI clavier/mobile/nuit.
- Environnement de recherche : HTML statique public uniquement ; zéro export Supabase, zéro publication de produits ou de fiches techniques privées.
- Contrôles ajoutés : `scripts/check_search_index.py`, vérification de build et parcours Chromium C1T dans les 3 langues.
- Document de conception et recette : `docs/LOT118_RECHERCHE_PAGEFIND_20261109.md`.
- À vérifier impérativement : compilation et jobs PR GitHub, corrections nécessaires, fusion sur `main`, disponibilité effective de l'index sur le déploiement Cloudflare.
