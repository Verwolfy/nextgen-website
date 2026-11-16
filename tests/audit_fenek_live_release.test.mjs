import test from 'node:test';
import assert from 'node:assert/strict';
import {inspectGuide,inspectWebP,validateSource,verifyLiveRelease} from '../scripts/audit_fenek_live_release.mjs';

const sha='a'.repeat(40), digest='b'.repeat(64);
const art={code:'BOND-GR-HR',slug:'fenek-bond-gr-hr',sha256:digest,
 sprite:'/images/illustrations/application-upgraded/fenek-bond-gr-hr-steps.webp'};
const doc='<section data-reference="'+art.code+'" data-application-count="6" data-v3-enhanced-sprite="'+
 art.sprite+'" data-v3-enhanced-hash="'+art.sha256+'">'+
 Array.from({length:6},(_,i)=>'<li data-application-step="'+(i+1)+'"><div data-v3-step="'+(i+1)+'"></div></li>').join('')+
 '</section>';
function fakeFetch(commit=sha, includeGuide=true){
 const resources=new Map([
  ['/deployment.json',JSON.stringify({application:'nextgen-website',branch:'main',commit})],
  ...(includeGuide?[['/fr/documentation/fenek-bond-gr-hr/',doc]]:[])
 ]);
 return async url=>({ok:resources.has(url.pathname),status:resources.has(url.pathname)?200:404,
  text:async()=>resources.get(url.pathname)});
}
test('guide validates six numbered steps and correct sprite',()=>{
 assert.doesNotThrow(()=>inspectGuide(doc,art.code,art.sprite,art.sha256));
 assert.throws(()=>inspectGuide(doc.replace('step="4"','step="9"'),art.code,art.sprite,art.sha256),/step numbering/);
 assert.throws(()=>inspectGuide(doc,art.code,art.sprite,'0'.repeat(64)),/wrong artwork SHA/);
 assert.throws(()=>inspectGuide(doc.replace('<div data-v3-step="3"></div>',''),art.code,art.sprite,art.sha256),/missing rendered six scenes/);
});
test('media SHA lock rejects invalid bytes',()=>{
 assert.throws(()=>inspectWebP(Buffer.from('invalid'),digest,art.code),/invalid WebP/);
});
test('deployment drift rejected before looking up guide',async()=>{
 await assert.rejects(verifyLiveRelease({origin:'https://nextgen-buildingsolutions.com/',expectedCommit:sha,
  catalog:[art],expectedProducts:1,artwork:[art],fetcher:fakeFetch('c'.repeat(40))}),/DEPLOYMENT DRIFT/);
});
test('quick mode verifies a real official documentation page, not a retired review',async()=>{
 const report=await verifyLiveRelease({origin:'https://nextgen-buildingsolutions.com/',expectedCommit:sha,
  catalog:[art],expectedProducts:1,artwork:[art],fetcher:fakeFetch()});
 assert.equal(report.status,'PASS');
 assert.equal(report.products,1);
 assert.equal(report.pagesChecked,1);
 assert.equal(report.mediaChecked,0);
});
test('missing official documentation page fails closed',async()=>{
 await assert.rejects(verifyLiveRelease({origin:'https://nextgen-buildingsolutions.com/',expectedCommit:sha,
  catalog:[art],expectedProducts:1,artwork:[art],fetcher:fakeFetch(sha,false)}),/HTTP 404/);
});
test('non-HTTPS origin rejected',async()=>{
 await assert.rejects(verifyLiveRelease({origin:'http://example.org/',expectedCommit:sha,
  catalog:[art],expectedProducts:1,artwork:[art],fetcher:fakeFetch()}),/HTTPS/);
});
test('complete 50-product source manifest required by default',async()=>{
 await assert.rejects(verifyLiveRelease({origin:'https://nextgen-buildingsolutions.com/',expectedCommit:sha,
  catalog:[],artwork:[],fetcher:fakeFetch()}),/expected exactly 50/);
});
test('source duplicate and corrupted hash are rejected',()=>{
 assert.throws(()=>validateSource([art,art],[art,art],2),/duplicate catalog/);
 assert.throws(()=>validateSource([art],[{...art,sha256:'wrong'}],1),/artwork\/slug\/hash mismatch/);
});
