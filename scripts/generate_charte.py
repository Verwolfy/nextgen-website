#!/usr/bin/env python3
"""One-page identity reference for site design, based only on approved colors and original logo."""
from __future__ import annotations
import json
from html import escape
from pathlib import Path
from weasyprint import HTML
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'supports/charte'
brand=json.loads((BASE/'brand_tokens.json').read_text())
logo=(ROOT/'supports/assets/Logo1.jpg').resolve().as_uri()
colors=[('Bleu marine (Bond)', '#12295C'),('Vert (Proof)', '#0E9A5B'),('Gris-bleu (Flow)', '#71899B'),
        ('Bordeaux (Paint)', '#971B38'),('Gris clair indicatif', '#D3D7D8'),('Blanc', '#FFFFFF')]
boxes=''.join(f'<div class="token"><div class="swatch" style="background:{color}"></div><strong>{escape(label)}</strong><span>{color}</span></div>' for label,color in colors)
html=f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Charte de travail NextGen</title><style>
@page {{size:A4 landscape;margin:17mm}}body{{font-family:Inter,sans-serif;color:#12295C;margin:0}}
header{{display:flex;align-items:center;justify-content:space-between;border-bottom:4px solid #0E9A5B;padding-bottom:12px}}
img{{width:180px}}h1{{font-size:25px;margin:0}}h2{{font-size:15px;margin:16px 0 9px}}
p,li{{font-size:11px;line-height:1.5}}.tag{{background:#12295C;color:white;padding:7px 12px;font-size:10px}}
.palette{{display:grid;grid-template-columns:repeat(6,1fr);gap:12px}}.swatch{{height:83px;border:1px solid #d1d6de;margin-bottom:8px}}
.token{{font-size:9px;display:flex;flex-direction:column;gap:3px}}.token span{{color:#667585}}
.bottom{{display:flex;gap:36px}}.bottom>div{{flex:1}}.notice{{border-left:5px solid #971B38;background:#f6f7fa;padding:12px}}
.footer{{font-size:10px;color:#64748b;border-top:1px solid #ccd6de;margin-top:20px;padding-top:12px}}
</style></head><body>
<header><div><p style="letter-spacing:2px;font-weight:bold;color:#0E9A5B">IDENTITÉ VISUELLE / DOCUMENT INTERNE</p>
<h1>NextGen Building Solutions</h1><p>Charte de travail — maquettes uniquement</p></div><img src="{logo}"></header>
<h2>Palette officielle pour la conception web</h2><div class="palette">{boxes}</div>
<div class="bottom"><div><h2>Typographie</h2><p><b>Titres :</b> Inter Tight ExtraBold<br><b>Corps :</b> Inter Regular<br>
<b>Arabe / RTL :</b> Noto Sans Arabic</p><p>Icônes techniques au trait fin ; motifs moléculaires discrets.
Photographies scientifiques premium et matériaux industriels.</p></div>
<div><h2>Familles de produits</h2><p><b>Fenek-Bond :</b> mortiers & colles<br><b>Fenek-Proof :</b> étanchéité & résines<br>
<b>Fenek-Flow :</b> adjuvants<br><b>Fenek-Paint :</b> peintures</p>
<p>Les quatre gammes sont des marques du projet, non vérifiées comme marques déposées.</p></div>
<div><h2>Logo / règles d'usage</h2><p>Logo JPEG fourni : affichage tel quel, sans redessin IA, sans déformation, sur fond clair.
Pour les autres déclinaisons, SVG source ou validation graphique nécessaire.</p></div></div>
<div class="notice"><b>BROUILLON — NON VALIDÉ</b><p>Couleurs issues de décisions de conception et d'un JPG compressé.
Vérifier avec le fichier source avant fabrication et impression. Les étiquettes et supports sont non contractuels.</p></div>
<p class="footer">NextGen Building Solutions · Zone Industrielle, Sidi Khaled, Oued El-Berdi, Bouira · contact@nextgen-buildingsolutions.com</p>
</body></html>'''
(BASE/'charte-site.html').write_text(html,encoding='utf8')
HTML(string=html,base_url=str(ROOT)).write_pdf(BASE/'charte-site.pdf')
print('Charte HTML + A4 landscape PDF generated')
