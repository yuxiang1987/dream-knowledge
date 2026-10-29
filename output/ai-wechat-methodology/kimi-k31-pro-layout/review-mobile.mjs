import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { chromium } from 'file:///C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.mjs';
const here=path.dirname(new URL(import.meta.url).pathname.replace(/^\/(?=[A-Za-z]:)/,''));
const folder=decodeURIComponent(here);
const browser=await chromium.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'});
try {
  const page=await browser.newPage({viewport:{width:375,height:900},deviceScaleFactor:1});
  await page.goto(pathToFileURL(path.join(folder,'article-layout.preview.html')).href);
  // 只隐藏预览页工具栏与警告，正文CSS保持原样。
  await page.addStyleTag({content:'header,aside{display:none!important}article{margin-top:0!important}'});
  await page.locator('article img').first().waitFor({state:'visible'});
  const report=await page.locator('article').evaluate(el=>({
    viewport:innerWidth,scrollWidth:document.documentElement.scrollWidth,
    images:[...el.querySelectorAll('img')].map(i=>({loaded:i.complete&&i.naturalWidth>0,width:i.getBoundingClientRect().width,height:i.getBoundingClientRect().height})),
    longParagraphs:[...el.querySelectorAll('p')].filter(p=>p.textContent.trim()&&!p.querySelector('img')&&!p.closest('section[style*="padding:14px 16px"]')).map(p=>({text:p.textContent.trim(),lines:Math.round(p.getBoundingClientRect().height/parseFloat(getComputedStyle(p).lineHeight))})).filter(p=>p.lines>5),
    headings:[...el.querySelectorAll('h2')].map(h=>h.textContent)
  }));
  await page.screenshot({path:path.join(folder,'mobile-top-375.png')});
  await page.locator('h2').first().scrollIntoViewIfNeeded();
  await page.screenshot({path:path.join(folder,'mobile-section-375.png')});
  const code=page.locator('section[style*="padding:14px 16px"]').first();
  if(await code.count()){await code.scrollIntoViewIfNeeded();await page.screenshot({path:path.join(folder,'mobile-prompt-375.png')});}
  fs.writeFileSync(path.join(folder,'mobile-review.json'),JSON.stringify(report,null,2));
  console.log(JSON.stringify(report,null,2));
} finally {await browser.close();}
