/**
 * Lot 193 — fail-closed FENEK media and guide gate in the Cloudflare build.
 * GitHub Actions runners currently fail before executing, so run these checks
 * inside the working Cloudflare Pages Node build instead.
 * No network, secrets or image generation. Read-only; all media are BROUILLON.
 */
import { readFileSync, existsSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT=resolve(dirname(fileURLToPath(import.meta.url)),'..');
const DIST=resolve(ROOT,'dist');
const LOCALES=['fr','en','ar'];
const expectedReview={
  'PROOF-PU-1K':{
    step:5,
    path:'/images/illustrations/application-premium/fenek-proof-pu-1k-scene-05-candidate-v1.webp',
    sha256:'f8a758381f5a510b03b9bd231700925d5a5b02935d264c2fdc47844915a6c14f',
    width:960,height:640
  },
  'PROOF-CM-O1P':{
    step:1,
    path:'/images/illustrations/application-premium/fenek-proof-cm-o1p-scene-01-candidate-v1.webp',
    sha256:'079bde85ae3e331bd2c654d8299ccde2e26a2141dce349b610130c080902a622',
    width:960,height:640
  }
};
const acr={
  code:'PROOF-ACR-RF',
  path:'/images/illustrations/application-premium/fenek-proof-acr-rf-steps-v4.webp',
  sha256:'438694daefa3b97b2ca3d36f38d6bea78fbedb7070203f81b6e06ef3a76fa433',
  width:1620,height:720
};
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
verifyMedia(acr.path,acr.sha256,[acr.width,acr.height]);
for(const candidate of Object.values(expectedReview)){
  verifyMedia(candidate.path,candidate.sha256,[candidate.width,candidate.height]);
}
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
    // Lot 203: official product pages display only the six original steps.
    // Draft candidates remain SHA-checked above but are never embedded into
    // FR/EN/AR official guides. Do not silently re-enable preview blocks.
    must(!html.includes('data-acrrf-v4-preview') &&
      !html.includes('data-acrrf-v4-step=') &&
      !html.includes('data-proof-partial-preview') &&
      !html.includes('data-proof-partial-step='),
      'Unapproved draft candidate embedded in official guide '+lang+'/'+code);
    pages++;
  }
}
// Unapproved artwork is permitted only in isolated noindex review pages.
// Verify the draft destinations as well as the original media SHA-256 above.
function reviewPage(relative) {
  const full=resolve(DIST,relative);
  must(existsSync(full),'Missing isolated draft review '+relative);
  const html=readFileSync(full,'utf8');
  must(html.includes('noindex,nofollow,noarchive'),'Draft review must be noindex '+relative);
  return html;
}
const acrReview=reviewPage('fr/avant-premiere/fenek-proof-acr-rf/index.html');
must(acrReview.includes('Brouillon') && acrReview.includes('non autorisée'),
  'ACR-RF review must remain explicitly unapproved');
must(count(acrReview,"--image:url('"+acr.path+"')")===6,
  'ACR-RF review must render six separate draft images');
const partialReview=reviewPage('fr/avant-premiere/lot187-proof/index.html');
must(count(partialReview,'V4 · brouillon')===2,
  'The two single-scene candidates must be visibly labelled as drafts');
for(const [code,candidate] of Object.entries(expectedReview)) {
  must(count(partialReview,'src="'+candidate.path+'"')===1,
    'One candidate image per reference in isolated review '+code);
  must(partialReview.includes(code.replace('PROOF-','FENEK-PROOF ')),
    'Isolated draft review missing product identity '+code);
}
must(pages===150,'Wrong localized guide total '+pages);
console.log('FENEK DEPLOYMENT GATE PASS: 50 products, 150 pages, 300 original stages, 50 sprite SHA-256, 3 premium candidate SHA-256, draft media preserved only in separate noindex reviews, no candidate embedded in official pages.');
