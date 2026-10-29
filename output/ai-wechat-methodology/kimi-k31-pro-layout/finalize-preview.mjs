import fs from 'node:fs';
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
