# Lot 44 — Couverture documentaire des onze dernières références FENEK

Date : 3 novembre 2026. Statut : **comparaison externe sourcée**, non fiche de performance NextGen.

## Résultat

Le site propose 150 pages statiques d'information (50 références × FR/AR/EN). **44 sources tierces** sont désormais rattachées aux 50 références ; les 11 nouveaux rapprochements ont chacun une source fabricant officielle. La couverture signifie « au moins une référence à consulter » et **ne signifie pas équivalence chimique ni validation de propriétés**.

| Référence FENEK | Comparateur officiel | Valeur ou nature déclarée chez le tiers | Limite |
|---|---|---|---|
| BOND-GP-CSII | Mapei MapeWall Intonaco Base | Enduit GP-CS II à la chaux NHL, env. 15 kg/m²/cm | Liant à la chaux ≠ enduit ciment annoncé pour FENEK |
| BOND-M5 | Mapei Intomap Build M5 | Mortier de maçonnerie, classe fabricant M5 | Classe du tiers uniquement |
| BOND-M10 | Mapei MapeWall Muratura Fine | Mortier de maçonnerie G-M10, 4–4,5 L/25 kg chez Mapei | Formulation NHL spécifique au tiers |
| BOND-OC-CSIII | Weber weberpral TE | Enduit monocouche de façade, CSIII, sac 25 kg | Produit et conditions de façade propres à Weber |
| FLOW-CI | Sika FerroGard-901 | Adjuvant inhibiteur de corrosion pour béton armé | Aucune efficacité ou dosage FENEK attestés |
| PAINT-ENT-L | Mapei Dursilite Level | Pâte acrylique de lissage intérieur, 1,6–1,7 kg/m²/mm chez Mapei | Consommation dépendante du support |
| PAINT-PRIM-A | Jotun Majestic Primer | Primaire acrylique aqueux, préparation des murs | Formulation et compatibilités non établies pour FENEK |
| PAINT-PRIM-FX | Jotun Jotashield Penetrating Primer | Primaire acrylique solvanté pénétrant | Fonction comparable, chimie potentiellement différente |
| PAINT-TXT-F | Jotun Jotashield Tex Fine(TR) | Revêtement fin texturé acrylique extérieur | Aucune performance FENEK certifiée |
| PROOF-EP-SB | Sika Sikadur-31+ | Adhésif structurel époxy bicomposant | Normes/résistances seulement chez Sika |
| PROOF-PU-INJ | Sika Injection-201 CE | Résine PU injectable bicomposante, ratio Sika A:B 1:1 en volume | NE PAS utiliser ce dosage comme formule FENEK |

Les URL officielles, observations et notes sont stockées dans `src/data/market-comparisons.json` sous les identifiants `N01` à `N11`. Aucune FDS étrangère n'est présentée comme une FDS NextGen ; les formulations, essais, conditionnements et classes FENEK demeurent non approuvés.

## Analyse documentaire et réserves

- Les mélanges de données ne sont pas homogènes : classes cimentaires, mortiers de chaux, couches de peinture, résines époxy/PU et adjuvants ne permettent pas des moyennes communes fiables.
- Les fiches régionales des fabricants et documents historiques peuvent évoluer ; vérifier la date/version originale avant réemploi professionnel.
- Les PDF externes sont **liés**, non copiés dans le site ni fournis comme documents NextGen.
- Les sources PDF ont été localisées dans les portails officiels ; certains rendus de consultation visuelle PDF externes n'ont pas pu être récupérés par le moteur de consultation. Les informations reprises se limitent aux éléments textuels identifiables, à revoir si ces éditions sont remplacées.

## Livraison

- Page `/{fr,ar,en}/documentation/` : 50/50 références avec au moins un comparateur, mention explicite de correspondances partielles.
- Page `/{fr,ar,en}/documentation/{slug}/` : provenance du tiers, avertissement, limitation et lien fabricant.
- Test `tests/test_market_product_information.py` : 44 sources, 50/50, tous les onze identifiants présents, URL HTTPS et garde-fous.
- Tests navigateur Chromium et build statique à conserver, vérification et déploiement Cloudflare requis avant fusion.

## Suite recommandée

La couverture des comparateurs ne remplace pas les documents industriels NextGen. Maintenir les 150 fiches officieuses en PR #50 séparée et bloquée, jusqu'à obtenir compositions, essais réels, FDS, vérification des conditionnements et signature qualité. Ne pas inventer de valeurs.
