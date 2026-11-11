# NextGen — Lot 125 : correction du sac FENEK-PROOF CM-O2P à 20 kg

Date : 11 novembre 2026  
Dépôt : `Verwolfy/nextgen-website`  
Branche : `fix/lot125-cm-o2p-sac-20kg-20261111`

## Décision utilisateur
« Corrige la maquette du FENEK-PROOF CM-O2P, le sac fait 20 Kg. »

## Diagnostic vérifié
- Le produit concerné est uniquement `PROOF-CM-O2P` / `fenek-proof-cm-o2p`, gamme PROOF.
- `src/data/catalogue-projets.json` présentait le format erroné `Kit : sac 30 kg + bidon 10 kg`.
- L'illustration archivée `public/images/maquettes/maquette-37.webp` (blob Git `eea49dc00e63d7668d88504b17a310ec2783c017`) présentait le marquage **« KIT 30 KG » sur le sac** et **« 10 KG » sur le bidon**.
- L'utilisateur indique que **le sac de poudre pèse 20 kg**. Le bidon de 10 kg reste inchangé ; le kit complet fait donc **30 kg au total**.
- Contrôle Supabase en lecture seule : la ligne `PROOF-CM-O2P` existe dans `site_produits`, n'a pas de champ `contenu.conditionnements` et demeure `produit_reel_confirme=false`, `publie=false`. Aucune mise à jour Supabase requise pour cette maquette éditoriale.

## Corrections prévues / réalisées sur branche
- `src/data/catalogue-projets.json` : `Kit : sac 20 kg + bidon 10 kg`.
- `src/lib/catalogue-projets.ts` : traduction explicite des éléments et du total en FR/AR/EN ; aiguillage uniquement de ce code vers le nouveau visuel.
- `public/images/maquettes/maquette-37-sac-20kg.svg` : **maquette conservant l'intégralité du WebP original** incorporé sans altération ; recouvrement local du texte de poids erroné par une étiquette « SAC 20 KG ». Le bidon reste visuellement et textuellement « 10 KG ». Pas de nouveaux bénéfices ou de composition inventée. L'original `maquette-37.webp` reste archivé.
- `scripts/check_built_pages.py` et `tests/test_lot125_cm_o2p_20kg.py` : couverture de l'image, des 50 références et de l'intégrité du visuel original.
- `scripts/check_browser_pages.py` : parcours FR/AR/EN, image effectivement décodée, poids correct et absence de débordement.

## Restrictions
- Édition d'une maquette de présentation ; **ne constitue pas une validation commerciale, technique ou réglementaire** du produit.
- Aucun changement de la formulation, de la fiche technique, de la FDS, des produits publiés, de Supabase/RLS, des commandes ou des secrets.
- Les 49 autres références et leurs visuels sont inchangés.
- Le déploiement Cloudflare ne sera déclaré confirmé qu'avec un contrôle du commit publié ou un résultat de workflow live.

## Recette CI
```bash
npm ci --no-audit --no-fund
npm run build
python -m unittest discover -s tests -q
python scripts/check_built_pages.py
python scripts/check_browser_pages.py
```

## Continuité
Vérifier les validations CI de PR, corriger leurs erreurs si nécessaire, fusionner la PR sur `main` seulement si tous les contrôles requis sont verts. Contrôler ensuite GitHub Actions/Cloudflare et notifier la différence entre code fusionné et production servie.
