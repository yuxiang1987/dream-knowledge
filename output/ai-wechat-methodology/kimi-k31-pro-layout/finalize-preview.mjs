import fs from 'node:fs';
import {createRequire} from 'node:module';
const require=createRequire(new URL('../../../.local/verify-article-structure-spec/cli/package.json',import.meta.url));
const {JSDOM}=require('jsdom');
import {preview} from '../../../.agents/skills/md-wechat-layout/scripts/render.mjs';
const folder=new URL('./',import.meta.url);
let html=fs.readFileSync(new URL('article-layout.wechat.html',folder),'utf8');
// 滚动样式必须写入被复制的正文，而非只写在预览页样式表。
let changed=0;
html=html.replace(/<section style="([^"]*)">/g,(tag,style)=>{
  if(!style.includes('padding:14px 16px')) return tag;
  changed++;
  const kept=style.split(';').filter(p=>p.trim()&&!/^\s*(max-height|overflow(?:-[xy])?|box-sizing|-webkit-overflow-scrolling)\s*:/.test(p));
  return `<section style="${kept.join(';')};max-height:320px;overflow:auto;box-sizing:border-box;-webkit-overflow-scrolling:touch;">`;
});
if(changed!==3) throw new Error(`预期3个提示词窗口，实际匹配${changed}个`);
// 独立图片使用明确的居中容器，不继承普通正文段落的左对齐或边距。
const imageBlocks=[];
html=html.replace(/<(p|section) style="[^"]*">(\s*<img\b[^>]*\/?>\s*)<\/\1>/g,(_,tag,image)=>{
  image=image.replace(/style="([^"]*)"/,(_,style)=>{
    const kept=style.split(';').filter(p=>p.trim()&&!/^\s*(display|margin(?:-(?:left|right|top|bottom))?|vertical-align)\s*:/.test(p));
    return `style="${kept.join(';')};display:inline-block;vertical-align:middle;margin:0 auto;"`;
  });
  const block=`<section style="width:100%;box-sizing:border-box;margin-left:0;margin-right:0;margin-top:30.4px;margin-bottom:30.4px;padding:0 32px;text-align:center;text-indent:0;font-size:0;line-height:0;letter-spacing:0;">${image.trim()}</section>`;
  imageBlocks.push(block);
  return block;
});
if(imageBlocks.length!==6) throw new Error(`预期6张独立图片，实际匹配${imageBlocks.length}张`);
// 中文段尾保留4至6字及句末标点一起换行，减少只剩一两个字的尾行。
// 不添加br、不改正文、不拆英文单词，也不进入提示词代码窗口。
const paragraphBlocks=[];
let tailCount=0;
html=html.replace(/<p style="([^"]*)">([\s\S]*?)<\/p>/g,(whole,style,body)=>{
  if(body.includes('<img')||body.includes('（嵌入文件：')) return whole;
  const fragment=JSDOM.fragment(`<p style="${style}">${body}</p>`);
  const p=fragment.firstElementChild;
  for(const previous of p.querySelectorAll('span[data-reading-tail]')) previous.replaceWith(...previous.childNodes);
  const walker=p.ownerDocument.createTreeWalker(p,4);
  let last=null;
  while(walker.nextNode()) if(walker.currentNode.data.trim()) last=walker.currentNode;
  const match=last?.data.match(/([\p{Script=Han}]{4,6}[。！？])([ \t\r\n]*)$/u);
  if(match){
    const tail=last.splitText(match.index);
    const span=p.ownerDocument.createElement('span');
    span.setAttribute('data-reading-tail','');
    span.setAttribute('style','white-space:nowrap;font-family:inherit;font-size:inherit;line-height:inherit;vertical-align:baseline;word-break:normal;overflow-wrap:normal;');
    tail.replaceWith(span);span.append(tail);tailCount++;
  }
  paragraphBlocks.push(p.outerHTML);
  return p.outerHTML;
});
if(tailCount===0) throw new Error('未找到可处理的中文段尾');
fs.writeFileSync(new URL('article-layout.wechat.html',folder),html);
let page=preview(html,'Kimi K3.1 Pro · 晴蓝手记',['提示词正文已加入320px限高和滚动样式，复制时携带；微信粘贴及手机效果待验证。','已内嵌6张图片；4段视频需在公众号后台对应位置插入。']);
page=page.replace('max-height:450px;overflow-y:auto!important','max-height:320px;overflow-y:auto!important;box-sizing:border-box;scrollbar-gutter:stable;scrollbar-width:auto;scrollbar-color:#8bb7d7 #edf5fa');
page=page.replace('body.copying article section[style*="padding:14px 16px"]{max-height:none;overflow-y:visible!important}','');
page=page.replace('长代码窗口预览限高 450px，可滚动；复制时保留全部内容','提示词最高320px，复制携带滚动样式与完整内容；微信效果待确认');
const scrollbars=`<style>
article section[style*="padding:14px 16px"]::-webkit-scrollbar{width:8px}
article section[style*="padding:14px 16px"]::-webkit-scrollbar-track{background:#edf5fa;border-radius:4px}
article section[style*="padding:14px 16px"]::-webkit-scrollbar-thumb{background:#8bb7d7;border-radius:4px}
</style>`;
page=page.replace('<header>',scrollbars+'<header>');
fs.writeFileSync(new URL('article-layout.preview.html',folder),page);

// 供已有微信草稿只替换图片，避免覆盖已手工插入的视频。
const labels=['封面','Kimi官方说明','模型成绩图','布料图案','用量截图','古城四张参考图'];
const cards=imageBlocks.map((block,i)=>`<article><h2>${i+1}. ${labels[i]}</h2><button data-copy="image-${i}">复制这张居中图片</button><section id="image-${i}">${block}</section></article>`).join('');
const imagePage=`<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>图片居中替换</title>
<style>body{margin:0;background:#f3f5f4;font-family:system-ui}header,article{max-width:677px;margin:20px auto;padding:20px;background:white}h2{font-size:18px}button{padding:10px 16px;cursor:pointer}#status{display:block;margin-top:12px}</style>
<header>仅替换图片：点击对应按钮，粘贴到微信中原图片的位置，无需覆盖整篇文章或已插入的视频。<span id="status">微信转存与居中效果仍需粘贴后确认。</span></header>${cards}
<script>for(const button of document.querySelectorAll('button[data-copy]'))button.onclick=async()=>{
const content=document.getElementById(button.dataset.copy);let ok=false;
try{await navigator.clipboard.write([new ClipboardItem({'text/html':new Blob([content.innerHTML],{type:'text/html'}),'text/plain':new Blob([''],{type:'text/plain'})})]);ok=true;}catch{
const selection=getSelection(),range=document.createRange();range.selectNodeContents(content);selection.removeAllRanges();selection.addRange(range);try{ok=document.execCommand('copy')}catch{}selection.removeAllRanges();}
document.getElementById('status').textContent=ok?'已复制居中图片，请粘贴到微信对应位置。':'复制失败，请选中下方单张图片后按Ctrl+C。';};</script></html>`;
fs.writeFileSync(new URL('image-align-fix.preview.html',folder),imagePage);

const paragraphs=paragraphBlocks.map((block,i)=>`<article><h2>段落 ${i+1}</h2><button data-copy="paragraph-${i}">复制这一段</button><section id="paragraph-${i}">${block}</section></article>`).join('');
const paragraphPage=imagePage.replace('<title>图片居中替换</title>','<title>段尾防孤字替换</title>').replace(/<header>[\s\S]*?<\/header>[\s\S]*?(?=<script>)/,`<header>按原文顺序排列。只复制需要调整的段落，替换微信中的对应段落，保留现有图片和视频。英文保留完整单词，行末仍可能有自然留白。<span id="status">中文段尾已做防孤字处理，实际断行随手机字号和屏宽变化。</span></header>${paragraphs}`).replace('已复制居中图片，请粘贴到微信对应位置。','已复制段落，请替换微信中对应段落。').replace('复制失败，请选中下方单张图片后按Ctrl+C。','复制失败，请选中该段文字后按Ctrl+C。');
fs.writeFileSync(new URL('paragraph-wrap-fix.preview.html',folder),paragraphPage);
