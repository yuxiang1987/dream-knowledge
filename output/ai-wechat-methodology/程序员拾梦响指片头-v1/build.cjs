const fs=require('fs'),path=require('path');
const {spawnSync}=require('child_process');
const {createCanvas,loadImage,GlobalFonts}=require('@napi-rs/canvas');
const OUT=__dirname,W=1246,H=300,D=7.2,FPS=20,FOOT=266,SPRITE_H=176,CHAR_X=215,TEXT_X=790;
GlobalFonts.registerFromPath('C:/Windows/Fonts/msyhbd.ttc','BrandCJK');
const clamp=x=>Math.max(0,Math.min(1,x));
const ease=x=>{x=clamp(x);return x*x*(3-2*x)};
const f=n=>Math.round(n*1000)/1000;
function glyph(text,size){
 const c=createCanvas(size*text.length+40,size+24),x=c.getContext('2d');x.font=`bold ${size}px BrandCJK`;x.textBaseline='top';x.fillStyle='white';x.fillText(text,0,0);
 const a=x.getImageData(0,0,c.width,c.height).data,p=[];let minX=Infinity,minY=Infinity,maxX=0,maxY=0;
 for(let y=0;y<c.height;y++)for(let xx=0;xx<c.width;xx++)if(a[(y*c.width+xx)*4+3]>150){p.push([xx,y]);minX=Math.min(minX,xx);minY=Math.min(minY,y);maxX=Math.max(maxX,xx);maxY=Math.max(maxY,y)}
 return {points:p.map(([xx,y])=>[xx-minX,y-minY]),w:maxX-minX+1,h:maxY-minY+1};
}
const title=glyph('程序员拾梦',52),tag=glyph('折腾 AI，分享实用玩法',25);
function phase(t){
 const snap=clamp(1-Math.abs(t-2.15)/.34),blink=clamp(1-Math.abs(t-2.25)/.16);
 const reset=ease((t-6.15)/.7);
 let titleA=t<1.82?1:t<2.35?1-ease((t-1.82)/.53):reset;
 let tagA=t<2.02?0:t<2.52?ease((t-2.02)/.5):1-reset;
 const glitch=snap>0?Math.sin(t*87)*snap:0;
 return {t,snap,blink,titleA,tagA,glitch,x:CHAR_X+Math.sin(t*71)*snap*2,scale:1+snap*.025};
}
function alphaBox(image){
 const c=createCanvas(image.width,image.height),x=c.getContext('2d');x.drawImage(image,0,0);const a=x.getImageData(0,0,c.width,c.height).data;let l=c.width,t=c.height,r=0,b=0;
 for(let y=0;y<c.height;y++)for(let xx=0;xx<c.width;xx++)if(a[(y*c.width+xx)*4+3]>200){l=Math.min(l,xx);t=Math.min(t,y);r=Math.max(r,xx);b=Math.max(b,y)}
 return {x:l,y:t,w:r-l+1,h:b-t+1};
}
function rects(g,scale,cx,cy){return g.points.map(([x,y])=>`<rect x="${f(cx+(x-g.w/2)*scale)}" y="${f(cy+y*scale)}" width="${f(scale*.94)}" height="${f(scale*.94)}"/>`).join('')}
const timeline=Array.from({length:D*FPS+1},(_,i)=>i/(D*FPS));
const states=timeline.map(u=>phase(u*D));
function animate(attr,values){return `<animate attributeName="${attr}" values="${values.join(';')}" keyTimes="${timeline.map(f).join(';')}" dur="7.2s" repeatCount="indefinite"/>`}
function makeSvg(box,spriteW){
 const b=fs.readFileSync(path.join(OUT,'jumper.png')).toString('base64');
 let s=`<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" role="img" aria-label="像素人物在左侧打响指并眨眼，程序员拾梦切换为折腾 AI 分享实用玩法。"><rect width="${W}" height="${H}" fill="#fafdff"/><rect x="0" y="0" width="${W}" height="${H}" fill="url(#bg)" opacity=".8"/><defs><linearGradient id="bg" x1="0" x2="1"><stop stop-color="#ffffff"/><stop offset=".55" stop-color="#f0f9ff"/><stop offset="1" stop-color="#ffffff"/></linearGradient></defs>`;
 s+=`<g opacity=".5" fill="#b8e7ff"><circle cx="${CHAR_X}" cy="${FOOT+4}" r="58"/><circle cx="${TEXT_X}" cy="148" r="95" opacity=".12"/></g>`;
 s+=`<g shape-rendering="crispEdges">`;
 const titleX=TEXT_X,titleY=115,tagY=135;
 s+=`<g fill="#278fd7">${animate('opacity',states.map(v=>v.titleA))}${rects(title,2.25,titleX,titleY)}</g>`;
 s+=`<g fill="#247fc3" opacity=".7">${animate('opacity',states.map(v=>v.tagA))}${rects(tag,1.75,TEXT_X,tagY)}</g>`;
 s+=`</g><g>`;
 s+=`<g transform="translate(${CHAR_X} ${FOOT})"><g><svg x="${-spriteW/2}" y="-${SPRITE_H}" width="${spriteW}" height="${SPRITE_H}" viewBox="${box.x} ${box.y} ${box.w} ${box.h}" overflow="hidden"><image width="1024" height="1536" style="image-rendering:pixelated" xlink:href="data:image/png;base64,${b}"/></svg></g></g></g>`;
 s+='</svg>';return s;
}
async function main(){
 const image=await loadImage(path.join(OUT,'jumper.png')),box=alphaBox(image),spriteW=SPRITE_H*box.w/box.h;
 const canvas=createCanvas(W,H),ctx=canvas.getContext('2d');
 function drawPixels(g,cx,cy,scale,fill,alpha=1){ctx.globalAlpha=alpha;ctx.fillStyle=fill;for(const [x,y]of g.points)ctx.fillRect(cx+(x-g.w/2)*scale,cy+y*scale,scale*.94,scale*.94);ctx.globalAlpha=1}
 function drawSnap(v){
  if(v.snap<=0)return;const hx=v.x+49,hy=FOOT-78,r=12+v.snap*35;
  ctx.save();ctx.translate(hx,hy);ctx.globalAlpha=.22*v.snap;ctx.strokeStyle='#32b8f3';ctx.lineWidth=3;ctx.beginPath();ctx.arc(0,0,r,0,Math.PI*2);ctx.stroke();ctx.globalAlpha=.72*v.snap;ctx.lineWidth=2;ctx.beginPath();ctx.arc(0,0,r*.64,0,Math.PI*2);ctx.stroke();ctx.restore();
  ctx.fillStyle='#27b8f0';for(let i=0;i<8;i++){const a=-Math.PI*.95+i*Math.PI*1.9/7,rr=25+v.snap*8;ctx.globalAlpha=v.snap*(.55+.3*(i%2));ctx.fillRect(hx+Math.cos(a)*rr,hy+Math.sin(a)*rr,3+(i%3),3+(i%2));}ctx.globalAlpha=1;
  ctx.fillStyle='#fff';ctx.fillRect(hx-3,hy-3,6,6);ctx.fillStyle='#188fd2';ctx.fillRect(hx-1,hy-7,3,4);ctx.fillRect(hx+4,hy-2,4,3);
 }
 function drawBlink(v){
  if(v.blink<=0)return;const y=FOOT-109;
  ctx.globalAlpha=v.blink;ctx.fillStyle='#f7c6aa';
  for(const dx of [-22,22]){ctx.fillRect(v.x+dx-12,y-7,24,14);ctx.fillStyle='#24232a';ctx.fillRect(v.x+dx-10,y,20,3);ctx.fillStyle='#f7c6aa';}
  ctx.globalAlpha=1;
 }
 function render(t){
  const v=phase(t);ctx.setTransform(1,0,0,1,0,0);ctx.globalAlpha=1;ctx.imageSmoothingEnabled=false;ctx.fillStyle='#fafdff';ctx.fillRect(0,0,W,H);
  const grad=ctx.createLinearGradient(0,0,W,0);grad.addColorStop(0,'#fff');grad.addColorStop(.55,'#effaff');grad.addColorStop(1,'#fff');ctx.fillStyle=grad;ctx.fillRect(0,0,W,H);
  ctx.globalAlpha=.18;ctx.fillStyle='#9edfff';ctx.beginPath();ctx.arc(v.x,FOOT+4,58+v.snap*8,0,Math.PI*2);ctx.fill();ctx.globalAlpha=1;
  ctx.fillStyle='#c6eafa';ctx.fillRect(100,FOOT+6,230,3);
  // glitch shadows make the snap transition feel like a digital handoff.
  if(v.titleA>.01) {drawPixels(title,TEXT_X+v.glitch*3,115,2.25,'#ff709a',v.titleA*.35);drawPixels(title,TEXT_X-v.glitch*2,115,2.25,'#43d6f5',v.titleA*.35);drawPixels(title,TEXT_X,115,2.25,'#278fd7',v.titleA)}
  if(v.tagA>.01) {drawPixels(tag,TEXT_X+v.glitch*2,135,1.75,'#ff709a',v.tagA*.35);drawPixels(tag,TEXT_X-v.glitch,135,1.75,'#43d6f5',v.tagA*.35);drawPixels(tag,TEXT_X,135,1.75,'#247fc3',v.tagA)}
  ctx.save();ctx.translate(v.x,FOOT);ctx.scale(v.scale,1-v.snap*.025);ctx.drawImage(image,box.x,box.y,box.w,box.h,-spriteW/2,-SPRITE_H,spriteW,SPRITE_H);ctx.restore();
  drawBlink(v);drawSnap(v);
  ctx.fillStyle='#7ebce0';ctx.globalAlpha=.45;ctx.fillRect(v.x-30,FOOT+7,60,2);ctx.globalAlpha=1;
  return canvas.toBuffer('image/png');
 }
 fs.writeFileSync(path.join(OUT,'intro.svg'),makeSvg(box,spriteW));fs.writeFileSync(path.join(OUT,'poster.png'),render(0));
 for(const [n,t]of [['before-snap',1.3],['snap',2.15],['blink',2.25],['after-snap',2.7],['tagline',4.4]])fs.writeFileSync(path.join(OUT,n+'.png'),render(t));
 const frames=path.join(OUT,'_frames');fs.mkdirSync(frames,{recursive:true});for(let i=0;i<D*FPS;i++)fs.writeFileSync(path.join(frames,String(i).padStart(4,'0')+'.png'),render(i/FPS));
 const run=spawnSync('ffmpeg',['-y','-v','error','-framerate',String(FPS),'-i',path.join(frames,'%04d.png'),'-filter_complex','[0:v]split[a][b];[a]palettegen=max_colors=192:stats_mode=diff[p];[b][p]paletteuse=dither=bayer:bayer_scale=3','-loop','0',path.join(OUT,'intro.gif')],{encoding:'utf8'});if(run.status!==0)throw new Error(run.stderr);
 fs.writeFileSync(path.join(OUT,'intro.wechat.html'),'<section style="margin:0;padding:0;line-height:0">'+fs.readFileSync(path.join(OUT,'intro.svg'),'utf8')+'</section>');
 fs.writeFileSync(path.join(OUT,'motion.json'),JSON.stringify({width:W,height:H,duration_seconds:D,fps:FPS,frames:D*FPS,character:{x:CHAR_X,foot:FOOT,sprite_height:SPRITE_H},timeline:{snap_at:2.15,blink_at:2.25,title:'程序员拾梦',tagline:'折腾 AI，分享实用玩法'},states:states.map(v=>({...v,t:f(v.t)})),mobile_wechat_verified:false},null,2)+'\n');
 const buttons=[['播放','intro.gif'],['响指','snap.png'],['眨眼','blink.png'],['切换后','after-snap.png'],['副标题','tagline.png']].map(([a,b])=>`<button onclick="document.getElementById('hero').src='${b}?'+Date.now()">${a}</button>`).join('');
 fs.writeFileSync(path.join(OUT,'preview.html'),`<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>程序员拾梦 · 响指片头</title><style>body{margin:0;background:#eef7fc;color:#405a72;font:14px "Microsoft YaHei",sans-serif}main{max-width:1100px;margin:32px auto;padding:24px;background:#fff;border-radius:16px;box-shadow:0 8px 30px #b9d9e955}h1{font-size:21px}p{color:#7890a5}img{width:100%;display:block}button,a{font:inherit;background:#f1faff;color:#268dcc;border:1px solid #d7ecf8;padding:8px 12px;border-radius:7px;text-decoration:none;margin-right:7px;cursor:pointer}.phone{width:375px;max-width:100%;border:1px solid #e2edf5}nav{margin:20px 0}</style><main><h1>程序员拾梦 · 响指切换片头</h1><p>左侧像素人物 · 霓虹响指 · 眨眼 · 故障文字切换 · 7.2秒循环</p><img id="hero" src="intro.gif" alt="像素人物打响指后文字切换"><nav>${buttons}<a href="intro.gif" download>下载GIF</a><a href="intro.svg" download>下载SVG</a></nav><p>手机宽度预览</p><div class="phone"><img src="intro.gif" alt="375px宽度预览"></div><p>本地预览，公众号后台和真机微信效果尚未验收。</p></main></html>`);
 console.log(JSON.stringify({width:W,height:H,duration:D,frames:D*FPS,gif_bytes:fs.statSync(path.join(OUT,'intro.gif')).size,sprite_box:box}));
}
if(require.main===module)main().catch(e=>{console.error(e);process.exit(1)});
module.exports={phase,FOOT,SPRITE_H,CHAR_X,TEXT_X,D,FPS};
