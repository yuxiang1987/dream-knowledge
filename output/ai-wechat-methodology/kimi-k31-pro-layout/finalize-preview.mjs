import fs from 'node:fs';
import {preview} from '../../../.agents/skills/md-wechat-layout/scripts/render.mjs';
const folder=new URL('./',import.meta.url);
const html=fs.readFileSync(new URL('article-layout.wechat.html',folder),'utf8');
fs.writeFileSync(new URL('article-layout.preview.html',folder),preview(html,'Kimi K3.1 Pro · 晴蓝手记',['已内嵌开头封面及原稿5张图片；粘贴后检查图片转存。','4段视频保留占位，请在公众号后台对应位置插入。']));
