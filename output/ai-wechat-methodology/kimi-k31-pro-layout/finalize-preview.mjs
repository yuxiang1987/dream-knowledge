import fs from 'node:fs';
import {preview} from '../../../.agents/skills/md-wechat-layout/scripts/render.mjs';
const folder=new URL('./',import.meta.url);
const html=fs.readFileSync(new URL('article-layout.wechat.html',folder),'utf8');
let page=preview(html,'Kimi K3.1 Pro · 晴蓝手记',['已内嵌开头封面及原稿5张图片；粘贴后检查图片转存。','4段视频保留占位，请在公众号后台对应位置插入。']);
page=page.replace('max-height:450px;overflow-y:auto!important','max-height:320px;overflow-y:auto!important;box-sizing:border-box;scrollbar-gutter:stable;scrollbar-width:auto;scrollbar-color:#8bb7d7 #edf5fa');
page=page.replace('长代码窗口预览限高 450px，可滚动；复制时保留全部内容','提示词窗口最高 320px，超出后在窗口内滚动；复制保留全文');
const scrollbars=`<style>
article section[style*="padding:14px 16px"]::-webkit-scrollbar{width:8px}
article section[style*="padding:14px 16px"]::-webkit-scrollbar-track{background:#edf5fa;border-radius:4px}
article section[style*="padding:14px 16px"]::-webkit-scrollbar-thumb{background:#8bb7d7;border-radius:4px}
</style>`;
page=page.replace('<header>',scrollbars+'<header>');
fs.writeFileSync(new URL('article-layout.preview.html',folder),page);
