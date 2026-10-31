#!/usr/bin/env python3
"""Generate five self-contained SVG *mockup* labels with exact binary JPG logo.

No synthetic normative claims. These are editable 2D design masters,
NOT production artwork and NOT lab-validated product labels.
"""
from __future__ import annotations
import base64
from html import escape
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
LOGO=base64.b64encode((ROOT/'supports/assets/Logo1.jpg').read_bytes()).decode('ascii')
TARGET=ROOT/'supports/etiquettes'
SAMPLES={
 'sac':('Fenek-Bond','Colle Carrelage','SAC · 25 kg','#12295C'),
 'seau':('Fenek-Paint','Satin Intérieur','SEAU · 20 kg','#971B38'),
 'bidon':('Fenek-Proof','Solution Étanchéité','BIDON · 10 L','#0E9A5B'),
 'fut':('Fenek-Flow','Adjuvant de formulation','FÛT · 200 L','#71899B'),
 'ibc':('Fenek-Flow','Superplastifiant','IBC · 1 000 L','#71899B'),
}

def build(name, args):
    gamme,produit,emballage,c=args
    # The image data is copied bit-for-bit; no logo redraw or reinterpretation.
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="560" viewBox="0 0 1000 560" role="img" aria-label="Étiquette d'exemple {escape(name)} non validée">
<rect width="1000" height="560" fill="#ffffff"/>
<rect x="0" y="0" width="1000" height="36" fill="{c}"/>
<rect x="0" y="520" width="1000" height="40" fill="#12295C"/>
<image x="38" y="51" width="257" height="142" href="data:image/jpeg;base64,{LOGO}"/>
<path d="M0 210H1000" stroke="#D3D7D8" stroke-width="2"/>
<g font-family="Inter, Arial, sans-serif">
<text x="48" y="272" fill="{c}" font-size="57" font-weight="800">{escape(gamme)}</text>
<text x="48" y="324" fill="#12295C" font-size="34" font-weight="700">{escape(produit)}</text>
<text x="48" y="381" fill="#45556B" font-size="28">{escape(emballage)}</text>
<text x="48" y="466" fill="#B42335" font-size="23" font-weight="800">SIMULATION - BROUILLON NON VALIDÉ</text>
<text x="48" y="494" fill="#667585" font-size="16">Étiquette indicative - dimensions et mentions à valider</text>
<text x="48" y="547" fill="white" font-size="16" font-weight="600">NextGen Building Solutions</text>
</g>
<g opacity="0.14" stroke="{c}" stroke-width="6" fill="none"><path d="M760 260l55-32 55 32v64l-55 32-55-32zM870 260l55-32 55 32v64l-55 32-55-32z"/></g>
</svg>'''
    return svg


def generate():
    TARGET.mkdir(parents=True,exist_ok=True)
    for name,args in SAMPLES.items():
        (TARGET/f'etiquette-{name}.svg').write_text(build(name,args),encoding='utf-8')
    print(f'Generated {len(SAMPLES)} SVG mockup labels with exact embedded original logo')


if __name__=='__main__':
    generate()
