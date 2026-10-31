#!/usr/bin/env python3
"""Create editable trilingual A4 demo technical sheets and blank SDS structures.

ALL documents are internal, NOT APPROVED for commercial or safety publication.
No performance numbers, certification or hazard categories are invented.
"""
from __future__ import annotations

from html import escape
from pathlib import Path
from weasyprint import HTML

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'supports'
LOGO = (BASE / 'assets/Logo1.jpg').resolve().as_uri()

PRODUCTS = [
    ('fenek-bond-colle-carrelage', 'Fenek-Bond Colle Carrelage', 'فينك-بوند لاصق البلاط',
     'Fenek-Bond Tile Adhesive', 'bond', 'Sac 25 kg', 'كيس 25 كغ', '25 kg bag'),
    ('fenek-flow-superplastifiant', 'Fenek-Flow Superplastifiant', 'فينك-فلو ملدن فائق',
     'Fenek-Flow Superplasticizer', 'flow', 'Cubi IBC 1 000 L', 'حاوية IBC سعة 1000 لتر', '1,000 L IBC'),
    ('fenek-paint-satin-interieur', 'Fenek-Paint Satin Intérieur', 'فينك-باينت طلاء داخلي ساتاني',
     'Fenek-Paint Interior Satin', 'paint', 'Seau 20 kg', 'دلو 20 كغ', '20 kg bucket'),
]
COLORS = {'bond': '#12295C', 'proof': '#0E9A5B', 'flow': '#71899B', 'paint': '#971B38'}

D = {
 'fr': {
  'label':'FICHE TECHNIQUE', 'draft':'BROUILLON – NON VALIDÉ',
  'warning':'DOCUMENT DE DÉMONSTRATION INTERNE — NE PAS UTILISER SUR CHANTIER',
  'sub':'Données techniques absentes : validation laboratoire requise avant publication.',
  'placeholder':'[À COMPLÉTER PAR LE LABO]',
  'sections':['Description','Domaines d’application','Caractéristiques techniques','Préparation du support',
              'Mise en œuvre','Consommation / dosage','Conditionnement','Stockage / durée de conservation',
              'Précautions','Mentions légales et validation'],
  'intro':'Référence fictive de travail. Aucune propriété de performance n’est validée.',
  'application':'Application à définir et à faire approuver par l’équipe technique.',
  'pack':'Format indicatif de démonstration, à confirmer par l’équipe industrielle.',
  'techkeys':['Propriété', 'Valeur / méthode'],
  'contact':'Contact technique : contact@nextgen-buildingsolutions.com · +213 554 603 410',
  'factory':'Usine : Zone Industrielle, Sidi Khaled, Oued El-Berdi, Bouira, Algérie',
 },
 'en': {
  'label':'TECHNICAL DATA SHEET', 'draft':'DRAFT – NOT APPROVED',
  'warning':'INTERNAL DEMONSTRATION DOCUMENT — NOT FOR JOBSITE USE',
  'sub':'Technical data unavailable: laboratory approval is required before publication.',
  'placeholder':'[TO BE COMPLETED BY THE LAB]',
  'sections':['Description','Areas of application','Technical characteristics','Substrate preparation',
              'Application procedure','Consumption / dosage','Packaging','Storage / shelf life',
              'Precautions','Legal notices and approval'],
  'intro':'Concept product for design purposes. No performance claims have been verified.',
  'application':'Intended uses must be defined and approved by the technical team.',
  'pack':'Indicative demonstration pack; final format requires industrial approval.',
  'techkeys':['Characteristic', 'Value / test method'],
  'contact':'Technical contact: contact@nextgen-buildingsolutions.com · +213 554 603 410',
  'factory':'Plant: Industrial Zone, Sidi Khaled, Oued El-Berdi, Bouira, Algeria',
 },
 'ar': {
  'label':'بطاقة البيانات التقنية', 'draft':'مسودة – غير معتمدة',
  'warning':'وثيقة تجريبية داخلية — يمنع استخدامها في الورشات',
  'sub':'البيانات التقنية غير متوفرة، ويلزم اعتماد المخبر قبل النشر.',
  'placeholder':'[تُستكمل من طرف المخبر]',
  'sections':['الوصف','مجالات الاستعمال','الخصائص التقنية','تحضير السطح',
              'طريقة التطبيق','الاستهلاك / الجرعة','التعبئة','التخزين ومدة الصلاحية',
              'الاحتياطات','المعلومات القانونية والاعتماد'],
  'intro':'منتج تصوري لأغراض التصميم. لم يتم إثبات أي أداء تقني.',
  'application':'يحدد الفريق التقني الاستعمالات المناسبة ويعتمدها لاحقاً.',
  'pack':'حجم تعبئة توضيحي، ويخضع للموافقة الصناعية النهائية.',
  'techkeys':['الخاصية', 'القيمة / طريقة الاختبار'],
  'contact':'الاتصال التقني: contact@nextgen-buildingsolutions.com · +213 554 603 410',
  'factory':'المصنع: المنطقة الصناعية، سيدي خالد، وادي البردي، البويرة، الجزائر',
 }
}


def css(color: str, rtl: bool) -> str:
    return f'''<style>
@page {{ size: A4; margin: 14mm 15mm 16mm; @bottom-center {{content: 'NextGen Building Solutions · DOCUMENT NON VALIDÉ'; color: #7b8794; font: 8pt sans-serif;}} }}
* {{ box-sizing: border-box; }}
html, body {{ font-family: {'"Noto Sans Arabic", sans-serif' if rtl else 'Inter, sans-serif'}; color:#12295C; font-size:9pt; margin:0; }}
body {{ direction:{'rtl' if rtl else 'ltr'}; }}
.top {{ display:flex; align-items:center; justify-content:space-between; gap:18px; border-bottom:4px solid {color}; padding-bottom:10px; }}
.logo {{ width:129px; height:auto; display:block; }}
.heading {{ flex:1; text-align:{'left' if rtl else 'right'}; }}
h1 {{ font-size:20pt; line-height:1.16; margin:3px 0; font-weight:800; color:{color}; }}
h2 {{ font-size:12pt; font-weight:800; border-bottom:1px solid #ccd4df; padding-bottom:5px; margin:12px 0 6px; color:{color}; }}
p {{ margin:4px 0; line-height:1.5; }}
.banner {{ padding:10px 12px; margin:14px 0 10px; background:#12295C; color:white; font-weight:bold; text-align:center; border-radius:4px; }}
.warn {{ font-size:9pt; color:#a61c31; font-weight:800; margin:7px 0; }}
.product {{ border-inline-start:5px solid {color}; padding:11px 12px; background:#f1f4f7; margin-bottom:10px; }}
.product strong {{ font-size:14pt; display:block; margin-bottom:3px; }}
.grid {{ display:grid; grid-template-columns:1fr 1fr; column-gap:14px; }}
.segment {{ break-inside:avoid; margin-bottom:4px; }}
.placeholder {{ color:#b42335; font-weight:800; line-height:1.55; }}
table {{ width:100%; border-collapse:collapse; margin:6px 0; }}
th,td {{ border:1px solid #d3dae2; padding:6px 8px; text-align:{'right' if rtl else 'left'}; }}
th {{ background:#f1f4f7; font-weight:700; }}
.footer {{ border-top:1px solid #d3dae2; padding-top:7px; margin-top:9px; color:#596679; font-size:8pt; }}
</style>'''


def sheet_html(product: tuple, lang: str) -> str:
    ident, fr, ar, en, gamme, pack_fr, pack_ar, pack_en = product
    d = D[lang]
    name = {'fr':fr, 'ar':ar, 'en':en}[lang]
    pack = {'fr':pack_fr, 'ar':pack_ar, 'en':pack_en}[lang]
    p = '<span class="placeholder">' + escape(d['placeholder']) + '</span>'
    headings = d['sections']
    blocks = [
        '<p>' + escape(d['intro']) + '</p>',
        '<p>' + escape(d['application']) + '</p>',
        '<table><thead><tr><th>' + escape(d['techkeys'][0]) + '</th><th>' + escape(d['techkeys'][1]) + '</th></tr></thead>'
        '<tbody>' + ''.join('<tr><td>' + escape(x) + '</td><td>' + p + '</td></tr>' for x in
         ({'fr':['Résistance / adhérence','Temps de prise / séchage','Densité / consistance'],
           'ar':['المقاومة / التلاصق','زمن الشك / الجفاف','الكثافة / القوام'],
           'en':['Strength / adhesion','Setting / drying time','Density / consistency']}[lang])) + '</tbody></table>',
        '<p>' + p + '</p>', '<p>' + p + '</p>', '<p>' + p + '</p>',
        '<p>' + escape(pack) + '</p>', '<p>' + p + '</p>',
        '<p>' + p + '</p>', '<p>' + p + '</p>',
    ]
    segments = ''.join(f'<section class="segment"><h2>{escape(h)}</h2>{body}</section>' for h,body in zip(headings,blocks))
    return f'''<!doctype html><html lang="{lang}" dir="{'rtl' if lang=='ar' else 'ltr'}"><head><meta charset="utf-8">
<title>{escape(name)} — {escape(d['draft'])}</title>{css(COLORS[gamme], lang=='ar')}</head><body>
<header class="top"><img class="logo" src="{LOGO}" alt="Logo officiel NextGen"><div class="heading">
<div>{escape(d['label'])}</div><h1>{escape(name)}</h1><div>NextGen Building Solutions · {escape(gamme.upper())}</div></div></header>
<div class="banner">{escape(d['draft'])}</div>
<div class="product"><strong>{escape(name)}</strong>{escape(pack)} · {escape(d['sub'])}</div>
<div class="warn">{escape(d['warning'])}</div><div class="grid">{segments}</div>
<footer class="footer">{escape(d['contact'])}<p>{escape(d['factory'])}</p></footer>
</body></html>'''


SDS_SECTIONS = {
 'fr':['Identification de la substance/du mélange et de la société', 'Identification des dangers', 'Composition / informations sur les composants',
       'Premiers secours', 'Mesures de lutte contre l’incendie', 'Mesures à prendre en cas de dispersion accidentelle',
       'Manipulation et stockage', 'Contrôles de l’exposition / protection individuelle', 'Propriétés physiques et chimiques',
       'Stabilité et réactivité', 'Informations toxicologiques', 'Informations écologiques', 'Considérations relatives à l’élimination',
       'Informations relatives au transport', 'Informations réglementaires', 'Autres informations'],
 'ar':['تحديد المادة أو الخليط والمؤسسة','تحديد الأخطار','التركيب ومعلومات المكونات','الإسعافات الأولية','تدابير مكافحة الحريق',
       'تدابير التسرب العرضي','التداول والتخزين','التحكم في التعرض / الحماية الفردية','الخصائص الفيزيائية والكيميائية',
       'الثبات والتفاعلية','المعلومات السمية','المعلومات البيئية','اعتبارات التخلص','معلومات النقل','المعلومات التنظيمية','معلومات أخرى'],
 'en':['Identification of the substance/mixture and undertaking','Hazards identification','Composition / information on ingredients',
       'First-aid measures','Firefighting measures','Accidental release measures','Handling and storage','Exposure controls / personal protection',
       'Physical and chemical properties','Stability and reactivity','Toxicological information','Ecological information',
       'Disposal considerations','Transport information','Regulatory information','Other information']
}


def sds_html(lang: str) -> str:
    d=D[lang]
    secs=''.join(f'<section class="segment"><h2>{i}. {escape(t)}</h2><p class="placeholder">{escape(d["placeholder"])}</p></section>'
                 for i,t in enumerate(SDS_SECTIONS[lang],1))
    return f'''<!doctype html><html lang="{lang}" dir="{'rtl' if lang=='ar' else 'ltr'}"><head><meta charset="utf-8">
<title>FDS SDS - {escape(d['draft'])}</title>{css('#12295C',lang=='ar')}</head><body>
<header class="top"><img class="logo" src="{LOGO}" alt="Logo officiel NextGen">
<h1>{'نموذج صحيفة بيانات السلامة' if lang=='ar' else ('FICHE DE DONNÉES DE SÉCURITÉ - GABARIT' if lang=='fr' else 'SAFETY DATA SHEET - TEMPLATE')}</h1></header>
<div class="banner">{escape(d['draft'])}</div><div class="warn">{escape(d['warning'])}</div>
<p>{escape(d['sub'])}</p><div class="grid">{secs}</div>
<footer class="footer">{escape(d['contact'])}</footer></body></html>'''


def generate() -> int:
    total=0
    for prod in PRODUCTS:
        for lang in D:
            html = sheet_html(prod,lang)
            base=BASE/'ft'/'html'/f'{prod[0]}-{lang}.html'
            base.parent.mkdir(parents=True,exist_ok=True)
            base.write_text(html,encoding='utf-8')
            pdf=BASE/'ft'/'pdf'/f'{prod[0]}-{lang}.pdf'
            pdf.parent.mkdir(parents=True,exist_ok=True)
            HTML(string=html,base_url=str(ROOT)).write_pdf(pdf)
            total+=1
    for lang in D:
        html=sds_html(lang)
        base=BASE/'fds'/f'fds-structure-{lang}.html'
        base.write_text(html,encoding='utf-8')
        HTML(string=html,base_url=str(ROOT)).write_pdf(BASE/'fds'/f'fds-structure-{lang}.pdf')
        total+=1
    print(f'Generated {total} draft PDFs (9 demo FT and 3 blank FDS templates)')
    return total


if __name__ == '__main__':
    generate()
