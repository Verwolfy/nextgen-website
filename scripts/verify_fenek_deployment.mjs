/**
 * Lot 193 — fail-closed FENEK media and guide gate in the Cloudflare build.
 * GitHub Actions runners currently fail before executing, so run these checks
 * inside the working Cloudflare Pages Node build instead.
 * No network, secrets or image generation. Read-only; all media are BROUILLON.
 */
import { readFileSync, existsSync, readdirSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT=resolve(dirname(fileURLToPath(import.meta.url)),'..');
const DIST=resolve(ROOT,'dist');
const LOCALES=['fr','en','ar'];
function must(test, detail) {if(!test) throw new Error('FENEK predeployment gate: '+detail);}
function fromRoot(path){return readFileSync(resolve(ROOT,path),'utf8');}
function json(path){return JSON.parse(fromRoot(path));}
function count(text,marker){return text.split(marker).length-1;}
function sha256(buf){return createHash('sha256').update(buf).digest('hex');}
function webpSize(bytes) {
  must(bytes.length>=30 && bytes.toString('ascii',0,4)==='RIFF' && bytes.toString('ascii',8,12)==='WEBP','Invalid WebP header');
  const type=bytes.toString('ascii',12,16);
  if(type==='VP8 ') {
    must(bytes.toString('hex',23,26)==='9d012a','Invalid lossy VP8 frame start');
    return [bytes.readUInt16LE(26)&0x3fff,bytes.readUInt16LE(28)&0x3fff];
  }
  if(type==='VP8L'){
    must(bytes[20]===0x2f,'Invalid lossless VP8L frame');
    return [1+(((bytes[22]&0x3f)<<8)|bytes[21]),1+(((bytes[24]&0x0f)<<10)|(bytes[23]<<2)|((bytes[22]&0xc0)>>6))];
  }
  if(type==='VP8X'){
    return [1+bytes.readUIntLE(24,3),1+bytes.readUIntLE(27,3)];
  }
  throw new Error('FENEK predeployment gate: Unsupported WebP payload '+type);
}
function verifyMedia(path,digest,dimensions){
  must(path.startsWith('/images/')&&!path.includes('..'),'Invalid media path '+path);
  const full=resolve(DIST,path.slice(1));
  must(existsSync(full),'Missing media in dist: '+path);
  const bytes=readFileSync(full);
  must(sha256(bytes)===digest,'SHA-256 mismatch: '+path);
  const actual=webpSize(bytes);
  if(dimensions)must(actual[0]===dimensions[0]&&actual[1]===dimensions[1],
    'Wrong image dimensions: '+path+' '+actual.join('x'));
}
must(existsSync(DIST),'dist/ absent: run npm run build (Astro) first');
const catalog=json('src/data/catalogue-projets.json');
const manuals=json('src/data/fenek-v3-manuals.json');
const sprites=json('src/data/fenek-enhanced-artwork.json');
must(catalog.length===50 && manuals.length===50 && sprites.length===50,'Expected 50 catalogue/manual/sprite entries');
const guides=new Map(manuals.map(g=>[g.code,g]));
const artwork=new Map(sprites.map(g=>[g.code,g]));
must(guides.size===50&&artwork.size===50,'Duplicate guide/artwork reference');
const catalogCodes=new Set(catalog.map(p=>p.code));
must(catalogCodes.size===50,'Duplicate catalogue code');
must([...catalogCodes].every(code=>guides.has(code)&&artwork.has(code)),'Catalogue/guide/media identities disagree');
// Every current packaging visual comes from the same product-specific folder.
const PRODUCT_DIR=resolve(DIST,'images/illustrations/produits');
must(existsSync(PRODUCT_DIR),'Missing unified packaging illustrations');
const expectedProducts=new Set();
for(const p of catalog){
  const basename=p.code==='PROOF-CM-O2P'?'fenek-proof-cm-o2p-sac-20kg-v2':p.slug;
  const names=p.gamme==='flow'?[basename+'.webp',basename+'-card.webp']:[basename+'.webp'];
  for(const name of names){
    must(!expectedProducts.has(name),'Duplicate product illustration '+name);
    expectedProducts.add(name);
    const file=resolve(PRODUCT_DIR,name);
    must(existsSync(file),'Missing product-specific image '+p.code+' -> '+name);
    webpSize(readFileSync(file)); // WebP file structure, never accept a missing/HTML placeholder.
  }
}
const actualProducts=readdirSync(PRODUCT_DIR).filter(name=>name.endsWith('.webp'));
must(expectedProducts.size===62 && actualProducts.length===62 &&
     actualProducts.every(name=>expectedProducts.has(name)),
     'Expected 62 exact current WebPs for 50 BOND/PROOF/FLOW/PAINT references');
must(sha256(readFileSync(resolve(PRODUCT_DIR,'fenek-proof-cm-o2p-sac-20kg-v2.webp')))===
     '552f3f850fca117410d0268265f5f7db8c4506dcbc93620ba07529657ea291b7',
     'Corrected CM-O2P 20 kg image SHA-256 changed');
for(const retired of [
  'images/illustrations/application-premium',
  'images/illustrations/application/v3/fenek-bond-c1t',
  'images/illustrations/catalogue-projects',
  'images/illustrations/maquettes',
  'fr/avant-premiere/fenek-proof-acr-rf',
  'fr/avant-premiere/lot187-proof',
  'fr/avant-premiere/audit-50-illustrations'
]) must(!existsSync(resolve(DIST,retired)),'Retired media or preview still published '+retired);
let pages=0;
for(const product of catalog){
  const {code,slug}=product;
  const guide=guides.get(code),art=artwork.get(code);
  must(guide.slug===slug&&art.slug===slug,'Wrong slug mapping '+code);
  must(guide.sprite===art.sprite&&guide.sha256===art.sha256,'Manual and current artwork must share one exact media URL/SHA '+code);
  must(guide.status==='BROUILLON'&&art.status==='BROUILLON','Unapproved FT/FDS change '+code);
  must(guide.steps.length===6 && guide.steps.every((s,i)=>s.image===i+1),
    'Wrong six-step manual '+code);
  must(art.sprite===`/images/illustrations/application-upgraded/${slug}-steps.webp`,
    'Wrong current product sprite '+code);
  verifyMedia(art.sprite,art.sha256,[1620,720]);
  for(const lang of LOCALES){
    const path=resolve(DIST,lang,'documentation',slug,'index.html');
    must(existsSync(path),'Missing localized page: '+lang+'/'+slug);
    const html=readFileSync(path,'utf8');
    must(html.includes(`data-reference="${code}"`),'Wrong localized code '+lang+'/'+code);
    must(html.includes('data-application-count="6"'),'Wrong official guide count '+lang+'/'+code);
    must(count(html,'data-application-step=')===6 && count(html,'data-v3-step=')===6,
      'Six original illustrated steps missing '+lang+'/'+code);
    must(html.includes(art.sprite),'Current product sprite not linked '+lang+'/'+code);
    // Only verified guide sprites; all former premium reviews and zoom UI are retired.
    must(!html.includes('data-acrrf-v4-preview') &&
      !html.includes('data-acrrf-v4-step=') &&
      !html.includes('data-proof-partial-preview') &&
      !html.includes('data-proof-partial-step='),
      'Unapproved draft candidate embedded in official guide '+lang+'/'+code);
    must(!html.includes('fenek-v3-detail-link') &&
         !html.includes('application-premium/'),'Retired zoom or premium media in official guide '+lang+'/'+code);
    pages++;
  }
}
must(pages===150,'Wrong localized guide total '+pages);

// Every legacy image redirect must continue to resolve to a published asset.
// In particular, a generic :splat rule must never mask a missing product image.
const redirectLines=fromRoot('public/_redirects').split(/\r?\n/)
  .map(line=>line.trim()).filter(line=>line&&!line.startsWith('#'));
const redirectRules=[];
const redirectSources=new Set();
for(const line of redirectLines){
  const parts=line.split(/\s+/);
  must(parts.length===3 && parts[2]==='301','Invalid legacy redirect rule: '+line);
  const [source,target]=parts;
  must(!redirectSources.has(source),'Duplicate redirect source '+source);
  redirectSources.add(source);
  if(target.includes(':splat')){
    must(target.endsWith('/:splat'),'Unsupported wildcard redirect '+line);
    must(existsSync(resolve(DIST,target.slice(1,-6))),
      'Wildcard redirect destination folder missing: '+target);
  } else if(target.startsWith('/images/') || target.startsWith('/videos/')){
    must(existsSync(resolve(DIST,target.slice(1))),
      'Broken legacy image redirect '+source+' -> '+target);
  } else {
    must(target.endsWith('/') && existsSync(resolve(DIST,target.slice(1),'index.html')),
      'Broken retired preview redirect '+source+' -> '+target);
  }
  redirectRules.push({source,target});
}
function resolveLegacyRedirect(oldUrl){
  for(const {source,target} of redirectRules){
    if(source===oldUrl)return target;
    if(source.endsWith('/*') && oldUrl.startsWith(source.slice(0,-1)))
      return target.replace(':splat',oldUrl.slice(source.length-1));
  }
  return null;
}
let legacyChecked=0;
for(const p of catalog){
  const basename=p.code==='PROOF-CM-O2P'?'fenek-proof-cm-o2p-sac-20kg-v2':p.slug;
  const files=[basename+'.webp',...(p.gamme==='flow'?[basename+'-card.webp']:[])];
  for(const file of files){
    for(const oldRoot of ['/images/catalogue-projects/','/images/illustrations/catalogue-projects/']){
      const source=oldRoot+file;
      const dest=resolveLegacyRedirect(source);
      must(dest!==null && existsSync(resolve(DIST,dest.slice(1))),
        'Broken former catalogue image URL '+source+' -> '+dest);
      legacyChecked++;
    }
  }
}
must(legacyChecked===124,'Expected 124 checked old catalogue product URLs');

// The no-zoom decision applies to the whole generated website, not just guides.
const retiredPageTokens=[
  'Ouvrir en haute résolution','Open in high resolution',
  'Open full-resolution illustration','فتح الرسم بالحجم الكامل',
  'fenek-v3-detail-link','fullSizeC1T','fullResolution',
  '/images/illustrations/application-premium/',
  '/images/illustrations/application/v3/fenek-bond-c1t/',
  '/images/illustrations/catalogue-projects/',
  '/images/illustrations/maquettes/'
];
let htmlPagesChecked=0;
function inspectPublishedHTML(dir){
  for(const entry of readdirSync(dir,{withFileTypes:true})){
    const full=resolve(dir,entry.name);
    if(entry.isDirectory()){inspectPublishedHTML(full);continue;}
    if(!entry.isFile()||!entry.name.endsWith('.html'))continue;
    const html=readFileSync(full,'utf8');
    for(const token of retiredPageTokens)
      must(!html.includes(token),'Retired illustration/zoom reference in '+full+': '+token);
    htmlPagesChecked++;
  }
}
inspectPublishedHTML(DIST);
must(htmlPagesChecked>=150,'Unexpected number of published HTML pages: '+htmlPagesChecked);
console.log('FENEK legacy redirect and no-zoom audit PASS: '+redirectRules.length+
  ' redirects, '+legacyChecked+' old product URLs, '+htmlPagesChecked+' built HTML pages.');
console.log('FENEK DEPLOYMENT GATE PASS: 50 products, 150 localized guides, 300 stages, 50 verified guide sprites and 62 packaging WebPs, no premium/zoom/old directories.');
