import fs from 'node:fs';
import assert from 'node:assert/strict';
import test from 'node:test';
import {createRequire} from 'node:module';
const require=createRequire(new URL('../../../.local/verify-article-structure-spec/cli/package.json',import.meta.url));
const {JSDOM}=require('jsdom');
const page=fs.readFileSync(new URL('article-layout.preview.html',import.meta.url),'utf8');
for(const fallback of [false,true])test(fallback?'完整预览备用复制保留全部图文与滚动':'完整预览正常复制保留全部图文与滚动',async()=>{
 let payload;
 const dom=new JSDOM(page,{runScripts:'dangerously',beforeParse(w){
  w.Blob=globalThis.Blob;w.ClipboardItem=class{constructor(data){this.data=data;}};
  Object.defineProperty(w.navigator,'clipboard',{value:{write:async items=>{if(fallback)throw new Error('模拟Clipboard API不可用');payload=await items[0].data['text/html'].text();}}});
  w.document.execCommand=command=>{assert.equal(command,'copy');payload=w.document.getElementById('content').innerHTML;return true;};
 }});
 try{
  const original=dom.window.document.getElementById('content');
  await dom.window.document.getElementById('copy').onclick();
  assert.ok(payload);const copied=new JSDOM(payload);
  try{
   assert.equal(copied.window.document.body.textContent,original.textContent);
   const images=[...copied.window.document.querySelectorAll('img')];
   assert.equal(images.length,6);
   assert.deepEqual(images.map(i=>i.src),[...original.querySelectorAll('img')].map(i=>i.src));
   for(const image of images){assert.equal(image.parentElement.style.textAlign,'center');assert.equal(image.style.display,'inline-block');}
   const code=[...copied.window.document.querySelectorAll('section[style*="max-height:320px"]')];
   assert.equal(code.length,3);for(const block of code){assert.equal(block.style.maxHeight,'320px');assert.equal(block.style.overflow,'auto');}
   assert.ok(copied.window.document.querySelectorAll('span[data-reading-tail]').length>10);
   assert.equal(copied.window.document.querySelectorAll('button,header').length,0);
  }finally{copied.window.close();}
 }finally{dom.window.close();}
});
