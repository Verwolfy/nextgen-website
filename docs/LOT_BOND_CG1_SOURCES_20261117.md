# Lot BOND n° 6 — FENEK-BOND CG1

**17 novembre 2026.** Dossier interne de traçabilité de la fiche trilingue CG1. Les valeurs présentées sont soit des **critères de classe EN 13888-1:2022**, soit des **données de produits tiers** ; aucune n’est une mesure de laboratoire FENEK.

## Norme applicable

La référence CG1 désigne un **mortier de jointoiement cimentaire à prise normale** selon EN 13888-1:2022, et non un adhésif EN 12004. Le tableau 1a exige :
- résistance à l’abrasion ≤ 2 000 mm³ ;
- flexion à sec et après gel/dégel ≥ 2,5 N/mm² ;
- compression à sec et après gel/dégel ≥ 15 N/mm² ;
- retrait ≤ 3 mm/m ;
- absorption après 30 min ≤ 5 g et après 240 min ≤ 10 g.

Source : [aperçu officiel EN 13888-1:2022, tableau 1a](https://cdn.standards.iteh.ai/samples/69726/869381c268db40a29e0e52e9eb38b561/SIST-EN-13888-1-2022.pdf); méthodes EN 13888-2:2022. Ces seuils ne qualifient pas automatiquement la formule FENEK. CG2WA est une classe avec caractéristiques supplémentaires (A/W) qui ne doivent **pas** être attribuées à CG1.

## Vérification croisée de produits CG1

| Fabricant / comparable | Données utilisées | Source |
| --- | --- | --- |
| Sika — **SikaCeram-500 TG** | CG1 ; joints jusqu’à 4 mm ; eau 30 % de la poudre ; vie en pot 45–60 min à 25 °C ; nettoyage 60 min ; passage ≥ 24 h ; température +5 à +45 °C | [Fiche fabricant](https://gcc.sika.com/en/construction/building-finishing/tiling-system/tile-grout/sikaceram-500-tg.html) |
| Building Adhesives / BAL — **BAL Grout** | CG1 ; joints jusqu’à 3 mm ; 60 min de vie en pot ; prise 24 h | [Fiche fabricant](https://www.bal-adhesives.com/product/bal-grout/) |
| Saint-Gobain Weber — **weberjoint wall** | Classification annoncée « CG1 A » ; **usage mural seulement** ; sacs 5/10/12,5 kg | [Fiche fabricant](https://www.uk.weber/weberjoint-wall) |
| Bostik — **CeraBest Fuga 105** | CG1 EN 13888 ; joint cimentaire ; présentation 20 kg | [Fiche fabricant](https://www.bostik.com/egypt/en/catalog/product/construction/emea/egypt/product-bostik-CeraBest-Fuga-105/) |

**Important en interne :** les délais de nettoyage, largeurs de joints, eau, températures et conditionnements ci-dessus sont propres aux références concurrentes citées. Aucune prescription de gâchage ou d’usage n’est extrapolée à FENEK. Les concurrents ne sont pas cités dans le HTML public.

## Modifications

- Nouvelle source de données `src/data/fenek-cg1-reference.ts` (8 exigences et 6 repères, FR/AR/EN).
- Composant dédié `src/components/FenekCG1Pilot.astro`, fiche A4 imprimable, illustration du guide CG1 et maillage CG1/CG2WA.
- Intégration dans les deux routes produit et le générateur PDF (6 références × 3 langues = **18** fichiers potentiels).
- Vérification par tests Node, build Astro, audits statiques et navigateur CI ; publication de binaires PDF différée jusqu’à revue graphique.
- Noindex conservé, `certifie:false`, `commercialise:false`, pas de paragraphe répétitif retiré des autres lots.
