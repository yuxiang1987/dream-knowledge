// 复用既有头像；SVG 与 GIF 共用文字、位置和 smoothstep 时间线。
const fs = require('fs');
const path = require('path');
const {spawnSync} = require('child_process');
const canvasModule = require.resolve('@napi-rs/canvas', {paths: [path.join(__dirname, '../程序员拾梦闯关片头五案-v1')]});
const {createCanvas, loadImage, GlobalFonts, convertSVGTextToPath} = require(canvasModule);
const OUT = __dirname, W = 1200, H = 260, FPS = 25, D = 5.2;
const NAME = '程序员梦哥', A = '折腾 AI', B = '分享实用玩法';
GlobalFonts.registerFromPath('C:/Windows/Fonts/msyhbd.ttc', 'MengBold');
GlobalFonts.registerFromPath('C:/Windows/Fonts/msyh.ttc', 'MengRegular');
const ease = x => { x = Math.max(0, Math.min(1, x)); return x*x*(3-2*x); };
function state(t) {
  if (t < 2) return {a: 1, b: 0, ay: 0, by: 16};
  if (t < 2.6) { const p = ease((t-2)/.6); return {a: 1-p, b: p, ay: -16*p, by: 16*(1-p)}; }
  if (t < 4.6) return {a: 0, b: 1, ay: 16, by: 0};
  const p = ease((t-4.6)/.6); return {a: p, b: 1-p, ay: 16*(1-p), by: -16*p};
}
function textPaths(text, font, size, x, y, fill) {
  const svg = convertSVGTextToPath(`<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="260"><text x="${x}" y="${y}" font-family="${font}" font-size="${size}" fill="${fill}">${text}</text></svg>`).toString();
  return svg.replace(/^[\s\S]*?<svg\b[^>]*>/, '').replace(/<\/svg>\s*$/, '');
}
function animate(attribute, values, times, type) {
  const tag = type ? 'animateTransform' : 'animate';
  const extra = type ? ` type="${type}"` : '';
  return `<${tag} attributeName="${attribute}"${extra} values="${values}" keyTimes="${times}" calcMode="spline" keySplines="${Array(times.split(';').length-1).fill('0.333333 0 0.666667 1').join(';')}" dur="5.2s" repeatCount="indefinite"/>`;
}
async function main() {
  fs.copyFileSync(path.join(OUT, '../程序员拾梦闯关片头五案-v1/avatar-reference.png'), path.join(OUT, 'avatar-reference.png'));
  const avatar = await loadImage(path.join(OUT, 'avatar-reference.png'));
  const encoded = fs.readFileSync(path.join(OUT, 'avatar-reference.png')).toString('base64');
  const title = textPaths(NAME, 'MengBold', 66, 340, 119, '#21364d');
  const lineA = textPaths(A, 'MengRegular', 42, 342, 185, '#247bd3');
  const lineB = textPaths(B, 'MengRegular', 42, 342, 185, '#247bd3');
  const staticSvg = `<defs><clipPath id="avatar-circle"><circle cx="176" cy="130" r="82"/></clipPath></defs><rect width="1200" height="260" fill="#ffffff"/><rect x="24" y="18" width="1152" height="224" rx="32" fill="#f2f8ff"/><circle cx="176" cy="130" r="89" fill="#ffffff"/><g clip-path="url(#avatar-circle)"><svg x="94" y="48" width="164" height="164" viewBox="73 26 124 124"><image width="252" height="173" href="data:image/png;base64,${encoded}"/></svg></g>${title}`;
  const aGroup = `<g id="tagline-a" opacity="1">${animate('opacity','1;1;0;0;1','0;0.384615385;0.5;0.884615385;1')}<g>${animate('transform','0 0;0 0;0 -16;0 16;0 16;0 0','0;0.384615385;0.5;0.501;0.884615385;1','translate')}${lineA}</g></g>`;
  const bGroup = `<g id="tagline-b" opacity="0">${animate('opacity','0;0;1;1;0','0;0.384615385;0.5;0.884615385;1')}<g>${animate('transform','0 16;0 16;0 0;0 0;0 -16','0;0.384615385;0.5;0.884615385;1','translate')}${lineB}</g></g>`;
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="260" viewBox="0 0 1200 260" role="img" aria-label="程序员梦哥；折腾 AI，分享实用玩法"><title>程序员梦哥 · 简洁片头</title><desc>固定头像与账号名；两句介绍各停留2秒，以0.6秒缓动切换。5.2秒循环。</desc>${staticSvg}${aGroup}${bGroup}</svg>`;
  fs.writeFileSync(path.join(OUT, 'intro.svg'), svg);
  fs.writeFileSync(path.join(OUT, 'intro.wechat.html'), `<section style="margin:0 0 20px;width:100%;line-height:0">${svg}</section>\n`);
  const canvas = createCanvas(W, H), ctx = canvas.getContext('2d');
  function render(t) {
    const s = state(t);
    ctx.resetTransform(); ctx.globalAlpha = 1; ctx.fillStyle = '#ffffff'; ctx.fillRect(0,0,W,H);
    ctx.fillStyle = '#f2f8ff'; ctx.beginPath(); ctx.roundRect(24,18,1152,224,32); ctx.fill();
    ctx.fillStyle = '#ffffff'; ctx.beginPath(); ctx.arc(176,130,89,0,2*Math.PI); ctx.fill();
    ctx.save(); ctx.beginPath(); ctx.arc(176,130,82,0,2*Math.PI); ctx.clip();
    ctx.drawImage(avatar,73,26,124,124,94,48,164,164); ctx.restore();
    ctx.font = '66px MengBold'; ctx.fillStyle = '#21364d'; ctx.fillText(NAME,340,119);
    ctx.font = '42px MengRegular'; ctx.fillStyle = '#247bd3';
    ctx.globalAlpha = s.a; ctx.fillText(A,342,185+s.ay);
    ctx.globalAlpha = s.b; ctx.fillText(B,342,185+s.by); ctx.globalAlpha = 1;
    return canvas.toBuffer('image/png');
  }
  const frameDir = path.join(OUT,'_frames'); fs.mkdirSync(frameDir,{recursive:true});
  for(let i=0;i<D*FPS;i++) fs.writeFileSync(path.join(frameDir,`${String(i).padStart(4,'0')}.png`),render(i === D*FPS-1 ? 0 : i/FPS));
  fs.writeFileSync(path.join(OUT,'poster.png'),render(0));
  fs.writeFileSync(path.join(OUT,'tagline-b.png'),render(3.5));
  const run = spawnSync('ffmpeg',['-y','-v','error','-framerate',String(FPS),'-i',path.join(frameDir,'%04d.png'),'-filter_complex','[0:v]split[a][b];[a]palettegen=max_colors=256:stats_mode=full[p];[b][p]paletteuse=dither=bayer:bayer_scale=3','-loop','0',path.join(OUT,'intro.gif')],{encoding:'utf8'});
  if(run.status !== 0) throw new Error(run.stderr);
  const preview = `<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>程序员梦哥 · 简洁片头 v1</title><style>*{box-sizing:border-box}body{margin:0;background:#edf1f5;color:#26394c;font:15px/1.8 "Microsoft YaHei",sans-serif}main{max-width:1000px;margin:36px auto;padding:32px;background:white;border-radius:20px}h1{font-size:25px;margin:0 0 8px}h2{font-size:16px;margin:28px 0 12px}p{color:#6c7a89;margin:0 0 20px}object,img{display:block;width:100%;height:auto}.phone{width:375px;max-width:100%;border:1px solid #e4eaf0;background:white}.article{padding:12px 24px 24px;font-size:15px;line-height:1.8}.article p{margin:14px 0 0;color:#657587}a,button{display:inline-block;padding:7px 13px;border:1px solid #d4e2ef;border-radius:7px;margin:0 6px 8px 0;color:#247bd3;background:white;font:inherit;text-decoration:none}small{color:#85909c}@media(max-width:650px){main{margin:0;padding:20px;border-radius:0}}</style><main><h1>程序员梦哥 · 简洁片头</h1><p>固定头像与名字，文字轻轻滑动切换。5.2秒一轮。</p><h2>SVG 原版</h2><div id="svg-preview">${svg}</div><h2>375px 文章预览 · SVG</h2><div class="phone">${svg}<div class="article"><b>你好，我是梦哥。</b><p>这里接文章的第一段。片头轻轻打个招呼，接下来就进入今天的内容。</p></div></div><h2>GIF 对照</h2><img src="intro.gif" alt="程序员梦哥简洁片头GIF"><h2>375px GIF</h2><div class="phone"><img src="intro.gif" alt="375px宽度GIF"></div><h2>保存文件</h2><a href="intro.svg" download>下载 SVG</a><a href="intro.gif" download>下载 GIF</a><a href="intro.wechat.html" download>下载 SVG 正文片段</a><p><small>本地候选预览；公众号后台粘贴、保存重载和真机效果待验收。SVG片段需通过支持SVG的富文本导入方式使用，复制源码文字不会得到动画。</small></p></main></html>`;
  fs.writeFileSync(path.join(OUT,'preview.html'),preview);
  fs.writeFileSync(path.join(OUT,'motion.json'),JSON.stringify({name:NAME,taglines:[A,B],width:W,height:H,fps:FPS,duration_seconds:D,frame_count:D*FPS,timeline:{a_hold:[0,2],a_to_b:[2,2.6],b_hold:[2.6,4.6],b_to_a:[4.6,5.2]},avatar_source:'../程序员拾梦闯关片头五案-v1/avatar-reference.png',method:'Existing avatar, native SVG SMIL paths, Canvas/FFmpeg GIF; no new image generation',wechat_verified:false},null,2)+'\n');
  console.log(JSON.stringify({svg_bytes:Buffer.byteLength(svg),gif_bytes:fs.statSync(path.join(OUT,'intro.gif')).size,frames:D*FPS,duration:D}));
}
main().catch(e=>{console.error(e);process.exitCode=1});
