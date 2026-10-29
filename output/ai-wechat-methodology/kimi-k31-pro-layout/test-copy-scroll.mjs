import fs from 'node:fs';
import assert from 'node:assert/strict';
import test from 'node:test';
import {createRequire} from 'node:module';
const require=createRequire(new URL('../../../.local/verify-article-structure-spec/cli/package.json',import.meta.url));
const {JSDOM}=require('jsdom');
const page=fs.readFileSync(new URL('article-layout.preview.html',import.meta.url),'utf8');
function checkPayload(html){
  const dom=new JSDOM(html);
  const windows=dom.window.document.querySelectorAll('section[style*="padding:14px 16px"]');
  assert.equal(windows.length,3);
  for(const block of windows){
    assert.equal(block.style.maxHeight,'320px');
    assert.equal(block.style.overflow,'auto');
  }
  dom.window.close();
}
test('富文本剪贴板携带三个窗口的内联限高与滚动样式',async()=>{
  let payload;
  const dom=new JSDOM(page,{runScripts:'dangerously',beforeParse(w){
    w.Blob=globalThis.Blob;
    w.ClipboardItem=class{constructor(data){this.data=data;}};
    Object.defineProperty(w.navigator,'clipboard',{value:{write:async items=>{payload=await items[0].data['text/html'].text();}}});
  }});
  try{
    await dom.window.document.getElementById('copy').onclick();
    checkPayload(payload);
    assert.match(dom.window.document.getElementById('status').textContent,/已复制富文本/);
  }finally{dom.window.close();}
});
test('备用复制分支不再解除正文窗口的限高',async()=>{
  let copied=false;
  const dom=new JSDOM(page,{runScripts:'dangerously',beforeParse(w){
    Object.defineProperty(w.navigator,'clipboard',{value:{write:async()=>{throw new Error('模拟剪贴板API不可用');}}});
    w.document.execCommand=command=>{
      assert.equal(command,'copy');
      checkPayload(w.document.getElementById('content').innerHTML);
      assert.equal(w.document.querySelector('section[style*="padding:14px 16px"]').style.maxHeight,'320px');
      copied=true;return true;
    };
  }});
  try{await dom.window.document.getElementById('copy').onclick();assert.equal(copied,true);}
  finally{dom.window.close();}
});
