# FENEK-BOND C2FT — dossier de recherche et validation éditoriale

**Lot BOND n° 3 — 17 novembre 2026.** La rédaction ci-dessous est une analyse de classement, non un rapport d'essais sur la formulation FENEK. Les URLs fabricants figurent exclusivement dans les documents internes de travail et non dans les fiches visibles par les visiteurs.

## Signification technique de C2FT

La désignation **EN 12004-1:2017 C2FT** correspond à :
- **C2** : adhérence améliorée, quatre résistances en traction chacune **≥ 1,0 N/mm²** (initiale, après eau, après chaleur, après gel/dégel).
- **F** : prise rapide : **adhérence précoce ≥ 0,5 N/mm² à 6 h au plus**, et critère d'adhérence **≥ 0,5 N/mm² après 10 min de temps ouvert** selon le protocole normatif.
- **T** : glissement vertical réduit **≤ 0,5 mm**.
- **Ni E ni S1** ne figurent dans la désignation `BOND-C2FT` du catalogue ; ne jamais leur attribuer ces classes par extrapolation à partir d'autres produits.

Source normative : [EN 12004-1:2017, aperçu public](https://cdn.standards.iteh.ai/samples/59328/3b98abf59fe44a6d9dc04b7c711de762/SIST-EN-12004-1-2017.pdf). Recouper contre la version normative intégrale avant qualification réglementaire.

## Trois comparables officiels, distincts du produit FENEK

| Fabricant / fiche | Classe annoncée | Eau de gâchage du produit concurrent | Durée pratique / pose / jointoiement | Source |
| --- | --- | --- | --- | --- |
| **Mapei — Keraquick** | C2FT S1 | Gris **22–24 %**, blanc **23–25 %** en masse, soit **5,5 à 6,25 L/25 kg** pour comparaison seulement | Vie en pot **30 min**, temps ouvert **15–20 min**, jointoiement **2–3 h**, adhérence après 6 h **0,8 N/mm²** | [Mapei, FT Keraquick](https://cdnmedia.mapei.com/docs/librariesprovider21/products-documents/103_keraquick_gba988d87279c562e49128ff01007028e9.pdf?sfvrsn=24974429_0) |
| **Weber — weberset rapid plus ECO (gris)** | C2FT | **3,8 à 4,4 L par sac de 20 kg**, soit **4,75–5,5 L/25 kg** en conversion | Vie en pot **30 min** ; limiter l'encollage à ce qui se pose en **10 min** ; densité de consommation **~1,5 kg/m²/mm**, jointoiement **~2 h** | [Weber, FT rapid plus ECO](https://www.uk.weber/files/gb/2018-03/11.024_weberset_rapid_plus_ECO_grey.pdf), [Weber, page produit](https://www.uk.weber/weberset-rapid-plus) |
| **Sika — SikaCeram Flexible Rapid Set (blanc)** | **C2FT S1 blanc uniquement ; C2FE gris** | Rapport volumique « 1 part eau / 4 parts poudre » non converti en masse pour éviter tout mélange d'unités | Temps ouvert **20–30 min**, ajustement **10 min**, jointoiement **2–3 h** ; consommation Sika variant avec le peigne | [Sika, FT Flexible Rapid Set](https://gbr.sika.com/dms/getdocument.get/3938c613-8497-42a5-9912-a06a1055a0af/sikaceram-flexiblerapidsettileadhesive.pdf) |

**Décisions rédactionnelles.** Les valeurs publiées sont réparties en « exigences normatives de classe » et « repères quantitatifs de produits comparables ». Les temps d'ajustement, de gâchage et de jointoiement sont différents du temps ouvert normalisé, et varient avec le climat. L'exemple Sika **gris n'est pas C2FT** : seule sa variante blanche a été retenue pour la comparaison des classes.

La plage comparative de gâchage **4,75–6,25 L/25 kg** correspond aux seules formules Mapei et Weber citées, calculées à masse égale ; elle n'est jamais présentée comme une prescription FENEK. Aucune plage simple/double encollage n'a été fabriquée : le seul rendement publié au tableau, **~1,5 kg/m²/mm**, provient de la FT Weber, avec son libellé explicite.

## Implémentation

- `src/data/fenek-c2ft-reference.ts` : 7 critères normatifs et 6 indicateurs de famille, tous trilingues.
- `src/components/FenekC2FTPilot.astro` : fiche Astro FR/AR/EN, tableau de classe distinct du benchmark, six schémas propres au code C2FT, actions commerciales, comparaison BOND, impression A4.
- `docs/INTERNE-validation-donnees.csv` : les 40 observations classées, sourcées et avec statut interne de validation.
- `scripts/export_c1t_pdfs.py` : export des trois pilotes BOND, soit neuf versions A4 une fois les fichiers générés et vérifiés.
- `tests/c2ft_pilot.test.mjs`, `scripts/check_built_pages.py` et `scripts/check_browser_pages.py` : contrôles isolés du lot.

## Garde-fous

Le catalogue conserve `certifie=false`, `commercialise=false` et `statut=presentation_provisoire` en stockage interne ; les pages demeurent `noindex`, et aucune FT ou FDS fabricant n'est simulée. Le paragraphe de fin supprimé sur demande n'est **pas réintroduit** dans le nouveau modèle. La validation fabricant/laboratoire reste nécessaire avant communication de performances FENEK réelles.
