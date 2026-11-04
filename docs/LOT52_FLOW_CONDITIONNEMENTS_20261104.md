# Lot 52 — Conditionnements confirmés pour la gamme FENEK-FLOW

Date : 4 novembre 2026. Dépôt : `Verwolfy/nextgen-website`.

## Décision utilisateur

L'utilisateur confirme explicitement pour **toute la gamme FENEK-FLOW** les **quatre** conditionnements suivants :

- **Bidon 5 L**
- **Bidon 20 L**
- **Fût 200 L**
- **IBC 1 000 L**

Ces quatre formats sont appliqués aux **12 références FLOW** : AC, AE, CI, CURE, LAT, RT, SP-HR, SP-PF, SP-RT, VMA, WP et WR-N.

## Modifications

1. `src/data/catalogue-projets.json` : les quatre conditionnements en volumes, dans l'ordre confirmé, sont présents pour chaque FLOW. `poids_net: null` est conservé faute de densité produit vérifiée. Les 16 BOND restent en sac de 25 kg et les autres familles inchangées.
2. `docs/catalogue-interne/conditionnements_50_A_CONFIRMER.json` : les 12 FLOW sont indiqués comme **confirmés par l'utilisateur pour leur format**, datés du 4 novembre 2026. `format_nominal` et `unite_vente` sont mis à jour. Matière d'emballage, masse nette et validations commerciales/industrielles demeurent **non confirmées / en attente**.
3. `tests/test_lot52_flow_packaging.py` : contrôles de cohérence des 12 × 4 formats, du maintien des statuts provisoires et du mode de génération des pages et exports trilingues.

Les pages produit, les pages de documentation FR/AR/EN et les sorties A4 utilisent directement la source centralisée du catalogue : pas de copie indépendante à corriger.

## Garde-fous

- **Volume ≠ masse** : aucune conversion des litres en kilogrammes sans densité validée.
- Aucun `SKU` ERP émis, aucun nouveau statut `certifie` ou `commercialise`, aucune écriture Supabase.
- Le fait que le conditionnement soit confirmé par l'utilisateur ne signifie **pas** que les emballages sont déjà fabriqués, commercialisés, ni que leurs étiquettes sont réglementairement approuvées.
- Le contrôle sur le domaine hébergé ne peut être assimilé aux vérifications GitHub ; le déploiement doit être vérifié séparément.

## Suite

1. Terminer CI `verify` et `smoke` sur la PR et sur `main`, fusionner si les deux sont verts.
2. **Demander le conditionnement de la gamme FENEK-PAINT** (11 références). Les formats actuellement hypothétiques sont seaux **5, 10, 20 kg** ; les faire confirmer ou modifier.
3. Puis qualifier les 11 références FENEK-PROOF par type de conditionnement, particulièrement les kits et cartouches.
4. Obtenir les documents de formulation/essais/HSE propres à NEXTGEN avant toute publication de FT ou FDS officielles.

Voir également `docs/LOT51_BOND_CONDITIONNEMENT_25KG_20261104.md` (16 BOND : sac de 25 kg).
