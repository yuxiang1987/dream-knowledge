import fs from 'node:fs';
import {preview} from '../../.agents/skills/md-wechat-layout/scripts/render.mjs';
const folder=new URL('./',import.meta.url);
let html=fs.readFileSync(new URL('article-layout.wechat.html',folder),'utf8');
let count=0;
html=html.replace(/\*\*\s*([^<>]*?)\s*\*\*/g,(_,text)=>{count++;return `<strong style="font-size:inherit;line-height:inherit;font-family:inherit;vertical-align:baseline;color:#315b83;">${text}</strong>`});
fs.writeFileSync(new URL('article-layout.wechat.html',folder),html);
fs.writeFileSync(new URL('article-layout.preview.html',folder),preview(html,'DeepSeek · 图片压缩修正版',['图片已压缩，微信转存情况需再次粘贴确认。四段视频需在后台插入。']));
console.log('修复未解析加粗',count);
