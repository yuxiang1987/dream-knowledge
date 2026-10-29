import fs from 'node:fs';
import assert from 'node:assert/strict';
import test from 'node:test';
import {createRequire} from 'node:module';
const require=createRequire(new URL('../../../.local/verify-article-structure-spec/cli/package.json',import.meta.url));
const {JSDOM}=require('jsdom');
const article=fs.readFileSync(new URL('article-layout.wechat.html',import.meta.url),'utf8');
const single=fs.readFileSync(new URL('image-align-fix.preview.html',import.meta.url),'utf8');
function checkImage(image,window){
  const parent=image.parentElement;
  assert.equal(parent.tagName,'SECTION');
  assert.equal(parent.style.textAlign,'center');
  assert.equal(parent.style.width,'100%');
  assert.equal(parent.style.boxSizing,'border-box');
  assert.equal(parent.style.marginLeft,'0px');assert.equal(parent.style.marginRight,'0px');
  assert.equal(parent.style.paddingLeft,parent.style.paddingRight);
  assert.equal(parent.textContent.trim(),'');
  assert.equal(image.style.display,'inline-block');
  assert.equal(image.style.height,'auto');assert.equal(image.style.maxWidth,'100%');
  // 即使微信不保留auto外边距，仍有容器居中和行内块布局。
  image.style.removeProperty('margin');
  assert.equal(window.getComputedStyle(parent).textAlign,'center');
  assert.equal(window.getComputedStyle(image).display,'inline-block');
}
test('6张图具有独立的对称居中容器，不依赖auto外边距',()=>{
  const dom=new JSDOM(article);
  try{const images=dom.window.document.querySelectorAll('img');assert.equal(images.length,6);for(const im of images)checkImage(im,dom.window);}
  finally{dom.window.close();}
});
test('单张复制按钮只复制对应居中图片，不带正文或视频占位',async()=>{
  let payload;
  const dom=new JSDOM(single,{runScripts:'dangerously',beforeParse(w){
    w.Blob=globalThis.Blob;w.ClipboardItem=class{constructor(data){this.data=data;}};
    Object.defineProperty(w.navigator,'clipboard',{value:{write:async items=>{payload=await items[0].data['text/html'].text();}}});
  }});
  try{
    const buttons=dom.window.document.querySelectorAll('button[data-copy]');assert.equal(buttons.length,6);
    for(const button of buttons){
      await button.onclick();
      const copy=new JSDOM(payload);
      try{const images=copy.window.document.querySelectorAll('img');assert.equal(images.length,1);checkImage(images[0],copy.window);assert.equal(copy.window.document.body.textContent.trim(),'');}
      finally{copy.window.close();}
    }
  }finally{dom.window.close();}
});
