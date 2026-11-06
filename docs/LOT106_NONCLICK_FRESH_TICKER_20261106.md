# Lot 106 — Fil BTPH/Économie/Innovation non cliquable, daté et limité dans le temps
Date : 2026-11-06 ; dépôt : Verwolfy/nextgen-website.

## Choix
Validation utilisateur : proportion cible 60 % BTPH, 25 % économie, 15 % innovation ; aucune actualité cliquable ; 3 langues FR/AR/EN.

## Implémentation
- 8 faits indépendants affichés : 5 BTPH, 2 taux de change, 1 innovation (répartition entière la plus proche : 62,5 % / 25 % / 12,5 %).
- Référentiel éditorial contient source URL et date de publication (provenance vérifiable dans GitHub) mais le composant public n'émet aucun lien ni target=_blank sur le bandeau.
- Les données périmées sont écartées au build et de nouveau dans le navigateur (sans réseau) sur les pages statiques déjà déployées ; sinon message localisé « informations en cours d'actualisation ».
- Dates d'expiration éditoriales : 21 jours environ pour BTPH, 7 jours pour les deux cours, exception innovation historique jusqu'au 20/11/2026. Ce ne sont pas des garanties d'actualisation.
- Pas d'appel aux API tierces côté visiteur, pas de script publicitaire, aucune donnée de marché inventée.
- Maintien de pause/lecture de la vidéo, du CTA catalogue, des 3 langues, RTL et reduced motion.
- L'actualisation future des faits impose de nouveaux contrôles de source avant la mise à jour du dépôt ; ce lot ne prétend PAS réaliser une collecte automatisée.

## Références publiées et vérifiées le 6 novembre 2026
1. APS 31/10/2026 : 95 opérations routières dans 24 wilayas, 853,5 km :
https://www.aps.dz/fr/algerie/developpement/mvwf185y-lancement-et-mise-en-service-de-95-projets-de-developpement-du-reseau-routier-a-travers-24-wilayas
2. APS 22/10/2026 : 253 326 logements dont travaux commencés jusqu'à fin septembre :
https://www.aps.dz/fr/economie/habitat-et-infrastructure/mvju9svb-plus-de-896-milliards-de-da-de-credits-de-paiement-proposes-au-secteur-de-l-habitat
3. APS 31/10/2026 : distribution annoncée de 133 780 logements et aides :
https://www.aps.dz/fr/economie/habitat-et-infrastructure/mvw8zwu1-distribution-de-133-780-logements-a-travers-le-pays-a-partir-de-dimanche
4. APS 03/11/2026 : lancement AEP El Eulma et 15 communes :
https://www.aps.dz/fr/algerie/developpement/mw0tqlwj-bouzegza-donne-le-coup-d-envoi-du-projet-d-aep-d-el-eulma-et-de-15-autres-communes
5. Banque d'Algérie (page d'accueil consultée 06/11/2026) : cours officiel de vente du 05/11/2026, EUR 152,76 DZD et USD 135,94 DZD :
https://www.bank-of-algeria.dz/
6. APS 20/04/2026 : usine de ciment Chlef, lancement d'un projet de valorisation énergétique des déchets :
https://www.aps.dz/fr/algerie/developpement/mo7ar2xh-lancement-d-un-projet-de-valorisation-energetique-des-dechets

## Protection
Aucune modification DNS, Cloudflare Access, noindex, formulaires, intégrations ERP/Supabase, produits FENEK non certifiés ou vidéo originale.

## Limite importante
Le site est un build Astro statique. Ce lot filtre la fraîcheur mais ne renouvelle PAS automatiquement le fichier d'actualités. Une véritable mise à jour quotidienne nécessite un pipeline serveur vérifié distinct.
