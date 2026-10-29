import fs from 'node:fs';
import assert from 'node:assert/strict';
import test from 'node:test';
import {createRequire} from 'node:module';
const require=createRequire(new URL('../../../.local/verify-article-structure-spec/cli/package.json',import.meta.url));
const {JSDOM}=require('jsdom');
const html=fs.readFileSync(new URL('article-layout.wechat.html',import.meta.url),'utf8');
const copyPage=fs.readFileSync(new URL('paragraph-wrap-fix.preview.html',import.meta.url),'utf8');
test('全文中文段尾做短语不拆行处理，不添加硬换行或拆开英文',()=>{
  const dom=new JSDOM(html);
  try{
    const paragraphs=[...dom.window.document.querySelectorAll('p')];
    const tail=dom.window.document.querySelectorAll('span[data-reading-tail]');
    assert.ok(tail.length>10);
    for(const span of tail){
      assert.match(span.textContent.trim(),/^[\p{Script=Han}]{4,6}[。！？]$/u);
      assert.equal(span.style.whiteSpace,'nowrap');
      assert.equal(span.style.fontSize,'inherit');assert.equal(span.style.lineHeight,'inherit');
      assert.equal(span.closest('code'),null);
    }
    const kart=paragraphs.find(p=>p.textContent.startsWith('这个案例整体中规中矩'));
    assert.ok(kart.querySelector('span[data-reading-tail]'));
    assert.equal(kart.querySelector('br'),null);
    const models=paragraphs.find(p=>p.textContent.startsWith('说实话，最近一直在看洋模型打架'));
    assert.equal(models.querySelector('br'),null);
    assert.match(models.textContent,/Fable 5\.1，OpenAI 发布了 Astra/);
    assert.equal(models.innerHTML.includes('Open<span'),false);
  }finally{dom.window.close();}
});
test('段落按钮复制全文和防孤字样式，不包含图片或视频占位',async()=>{
  let payload;
  const dom=new JSDOM(copyPage,{runScripts:'dangerously',beforeParse(w){
    w.Blob=globalThis.Blob;w.ClipboardItem=class{constructor(data){this.data=data;}};
    Object.defineProperty(w.navigator,'clipboard',{value:{write:async items=>{payload=await items[0].data['text/html'].text();}}});
  }});
  try{
    const button=[...dom.window.document.querySelectorAll('button[data-copy]')].find(b=>dom.window.document.getElementById(b.dataset.copy).textContent.startsWith('这个案例整体中规中矩'));
    assert.ok(button);await button.onclick();
    const pasted=new JSDOM(payload);
    try{
      assert.equal(pasted.window.document.querySelectorAll('p').length,1);
      assert.equal(pasted.window.document.querySelectorAll('img,video').length,0);
      assert.ok(pasted.window.document.querySelector('span[data-reading-tail]'));
      assert.equal(pasted.window.document.body.textContent,'这个案例整体中规中矩，赛道、对手、驾驶和结算都做出来了，也能正常跑完一场比赛。');
    }finally{pasted.window.close();}
  }finally{dom.window.close();}
});
