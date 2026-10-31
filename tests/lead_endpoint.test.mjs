import test from 'node:test';
import assert from 'node:assert/strict';
import {onRequestPost, onRequestGet} from '../functions/api/lead.js';
const address = 'https://www.nextgen-buildingsolutions.com/api/lead';
const valid = { kind:'quote',business:'Compagnie',contact:'Responsable',phone:'+213 554 603 410',email:'contact@example.com',wilaya:'Bouira',commune:'Oued El-Berdi',product:'Fenek',package:'25 kg',quantity:'50',message:'Demande',consent:true,token:'test-token-abcdef',website:'' };
const env = { NEXTGEN_LEADS_ENABLED:'true',TURNSTILE_SECRET_KEY:'secret',SUPABASE_SERVICE_ROLE_KEY:'private',SUPABASE_URL:'https://wenydirqtmkywbxbxfal.supabase.co',NEXTGEN_PRIVACY_NOTICE_VERSION:'reviewed-test-only-v1' };
function request(body=valid, headers={}) {
  return new Request(address,{method:'POST',headers:{origin:'https://www.nextgen-buildingsolutions.com','content-type':'application/json',...headers},body:JSON.stringify(body)});
}
test('GET rejected and feature disabled by default without transmission', async () => {
  assert.equal((await onRequestGet()).status,405);
  const old=globalThis.fetch;globalThis.fetch=()=>{throw Error('outbound forbidden')};
  try {const result=await onRequestPost({request:request(),env:{}});assert.equal(result.status,503);assert.equal((await result.json()).code,'LEADS_NOT_ACTIVE');}
  finally {globalThis.fetch=old;}
});
test('origin, method and JSON content-type guarded',async()=>{
  assert.equal((await onRequestPost({request:request(valid,{origin:'https://attacker.example'}),env})).status,403);
  assert.equal((await onRequestPost({request:request(valid,{'content-type':'text/plain'}),env})).status,415);
});
test('consent, honeypot and data validation prevent access',async()=>{
  for(const input of [ {...valid,consent:false},{...valid,website:'bot'}, {...valid,extra:'danger'}, {...valid,phone:'bad'}, {...valid,kind:'distributor',quantity:'50'} ]) {
    assert.equal((await onRequestPost({request:request(input),env})).status,400);
  }
});
test('failed challenge prevents database write',async()=>{
  const old=globalThis.fetch;let called=0;
  globalThis.fetch=async()=>{called++;return new Response(JSON.stringify({success:false,hostname:'www.nextgen-buildingsolutions.com'}),{status:200})};
  try{assert.equal((await onRequestPost({request:request(),env})).status,403);assert.equal(called,1)}finally{globalThis.fetch=old}
});
test('valid challenge stores only approved fields and excludes token',async()=>{
  const old=globalThis.fetch;const calls=[];
  globalThis.fetch=async(u,init)=>{calls.push({url:String(u),init});if(calls.length===1)return new Response(JSON.stringify({success:true,hostname:'www.nextgen-buildingsolutions.com'}),{status:200});return new Response(null,{status:201})};
  try{const resp=await onRequestPost({request:request(),env});assert.equal(resp.status,201);assert.equal(calls.length,2);const saved=JSON.parse(calls[1].init.body);assert.equal(saved.type_demande,'quote');assert.equal(saved.consentement,true);assert.equal(saved.consent_notice_version,'reviewed-test-only-v1');assert.equal(saved.entreprise,'Compagnie');assert.ok(!JSON.stringify(saved).includes('test-token'));assert.ok(!JSON.stringify(saved).includes('private'));}finally{globalThis.fetch=old}
});
test('malformed or oversize bodies do not reach Turnstile',async()=>{
  const old=globalThis.fetch;globalThis.fetch=()=>{throw Error('should not fetch')};
  try{const massive={...valid,message:'x'.repeat(8200)};assert.ok([400,413].includes((await onRequestPost({request:request(massive),env})).status));const malformed=new Request(address,{method:'POST',headers:{origin:'https://www.nextgen-buildingsolutions.com','content-type':'application/json'},body:'{bad'});assert.equal((await onRequestPost({request:malformed,env})).status,400);}finally{globalThis.fetch=old}
});
