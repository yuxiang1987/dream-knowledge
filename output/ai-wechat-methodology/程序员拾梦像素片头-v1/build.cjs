// Native canvas renders the timeline; the matching SVG uses only SMIL animation.
const fs = require('fs');
const path = require('path');
const {createCanvas, loadImage, GlobalFonts} = require('@napi-rs/canvas');
const {spawnSync} = require('child_process');
const OUT = __dirname;
const W = 1246, H = 220, DURATION = 6, FPS = 20;
GlobalFonts.registerFromPath('C:/Windows/Fonts/msyhbd.ttc', 'BrandCJK');
const smooth = x => {x=Math.max(0,Math.min(1,x));return x*x*(3-2*x);};
const fmt = n => Math.round(n*100)/100;
const escape = s => s.replace(/&/g,'&amp;').replace(/"/g,'&quot;').replace(/</g,'&lt;');
const knots = [0,.28,.46,.74,.9,1];
function blend(t,values){
  const u=t/DURATION;
  for(let i=1;i<knots.length;i++)if(u<=knots[i]){
    const a=smooth((u-knots[i-1])/(knots[i]-knots[i-1]));
    return values[i-1]*(1-a)+values[i]*a;
  }
  return values.at(-1);
}
function pixels(text,size,x,y,scale,color){
  const canvas=createCanvas(Math.ceil(size*text.length*1.15),size+12);
  const c=canvas.getContext('2d'); c.font=`bold ${size}px BrandCJK`;
  c.fillStyle='#fff';c.textBaseline='top';c.fillText(text,0,0);
  const data=c.getImageData(0,0,canvas.width,canvas.height).data, result=[];
  for(let yy=0;yy<canvas.height;yy++)for(let xx=0;xx<canvas.width;xx++){
    if(data[(yy*canvas.width+xx)*4+3]<145)continue;
    const k=result.length;
    const px=x+xx*scale,py=y+yy*scale;
    const tx=850+Math.sin(k*2.399)*150,ty=92+Math.cos(k*1.71)*72;
    result.push({x:fmt(px),y:fmt(py),s:scale*.9,color:typeof color==='function'?color(xx):color,
      dx:fmt(tx-px),dy:fmt(ty-py)});
  }
  return result;
}
const dots=[...pixels('程序员拾梦',32,255,28,2.7,x=>x>95?'#2399e9':'#64748b'),
  ...pixels('折腾 AI，分享实用玩法',16,258,138,2.35,'#65788e'),
  ...pixels('</>',32,982,61,2.3,'#8ac9ec')];
const verts=[[-1,-1,-1],[1,-1,-1],[1,1,-1],[-1,1,-1],[-1,-1,1],[1,-1,1],[1,1,1],[-1,1,1]];
const faces=[{v:[0,1,2,3],n:[0,0,-1],fill:'#249fe8'},
  {v:[4,7,6,5],n:[0,0,1],fill:'#187dbd'},
  {v:[0,4,5,1],n:[0,-1,0],fill:'#73cdf8'},
  {v:[3,2,6,7],n:[0,1,0],fill:'#125c9e'},
  {v:[0,3,7,4],n:[-1,0,0],fill:'#4bb9f1'},
  {v:[1,5,6,2],n:[1,0,0],fill:'#1476b8'}];
function rotation(v,t){
  const a=.35+(t-2.2)*.62, tilt=-.24;
  const x=v[0]*Math.cos(a)+v[2]*Math.sin(a),z=-v[0]*Math.sin(a)+v[2]*Math.cos(a);
  return [x,v[1]*Math.cos(tilt)-z*Math.sin(tilt),v[1]*Math.sin(tilt)+z*Math.cos(tilt)];
}
function project(v,t){const [x,y,z]=rotation(v,t),p=1/(1+z*.16);return [fmt(855+x*52*p),fmt(105+y*52*p)];}
function cubeOpacity(t){return t<2.12?0:t<2.65?smooth((t-2.12)/.53):t<4.45?1:1-smooth((t-4.45)/.65);}
function faceOpacity(f,t){return cubeOpacity(t)*(rotation(f.n,t)[2]<-.025?1:0);}
const grid=[];
for(let i=0;i<=10;i++)grid.push([[560+i*60,184],[730+i*25,62]]);
for(const v of [0,.2,.38,.54,.68,.8,.9,1]){
 const y=62+v*v*122,half=125+v*v*175;grid.push([[855-half,y],[855+half,y]]);
}
const points = a => a.map(p=>p.join(',')).join(' ');
const anim=(attr,values,times=knots,extra='')=>`<animate attributeName="${attr}" values="${values.join(';')}" keyTimes="${times.join(';')}" dur="${DURATION}s" repeatCount="indefinite" ${extra}/>`;
const spline='calcMode="spline" keySplines="'+Array(knots.length-1).fill('0.333 0 0.667 1').join(';')+'"';
function makeSvg(image){
 let s=`<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" role="img" aria-label="程序员拾梦，折腾 AI，分享实用玩法。像素文字化为粒子，蓝色代码方块出现并旋转，六秒循环。"><rect width="1246" height="220" fill="white"/><image x="18" y="4" width="212" height="212" xlink:href="data:image/png;base64,${image}"/>`;
 s+='<g shape-rendering="crispEdges">'+anim('opacity',[1,1,0,0,1,1],knots,spline);
 for(const p of dots){
  s+=`<rect x="${p.x}" y="${p.y}" width="${fmt(p.s)}" height="${fmt(p.s)}" fill="${p.color}"><animateTransform attributeName="transform" type="translate" values="0 0;0 0;${p.dx} ${p.dy};${p.dx} ${p.dy};0 0;0 0" keyTimes="${knots.join(';')}" dur="6s" repeatCount="indefinite" ${spline}/></rect>`;
 }
 s+='</g>';
 const times=Array.from({length:121},(_,i)=>i/120),ts=times.map(u=>u*DURATION);
 s+='<g opacity="0">'+anim('opacity',ts.map(cubeOpacity),times);
 for(const [a,b]of grid)s+=`<path d="M${a.join(' ')}L${b.join(' ')}" fill="none" stroke="#cddae8" stroke-width="1"/>`;
 s+='<path d="M627 56V27H656M1054 27H1083V56M1083 149V178H1054M656 178H627V149" stroke="#9aaec5" stroke-width="2.5" fill="none"/>';
 s+='<ellipse cx="855" cy="180" rx="86" ry="9" fill="#def1fc"/>';
 s+='</g>';
 for(const f of faces){
  s+=`<polygon points="${points(f.v.map(i=>project(verts[i],2.3)))}" fill="${f.fill}" stroke="#c9ebfd" stroke-width="1.7" stroke-linejoin="round" opacity="0">`;
  s+=anim('points',ts.map(t=>points(f.v.map(i=>project(verts[i],t)))),times);
  s+=anim('opacity',ts.map(t=>fmt(faceOpacity(f,t)*smooth((t-2.3)/.55))),times)+'</polygon>';
 }
 // Wireframe appears just before the filled faces.
 const edges=[[0,1],[1,2],[2,3],[3,0],[4,5],[5,6],[6,7],[7,4],[0,4],[1,5],[2,6],[3,7]];
 for(const [a,b]of edges){
  s+=`<polyline fill="none" stroke="#459cd2" stroke-width="1.5" opacity="0">`;
  s+=anim('points',ts.map(t=>points([project(verts[a],t),project(verts[b],t)])),times);
  s+=anim('opacity',ts.map(t=>fmt(cubeOpacity(t)*(1-smooth((t-2.65)/.35)))),times)+'</polyline>';
 }
 // A tiny cursor keeps the identity frame recognizably about coding.
 s+='<g fill="#43aceb"><rect x="1128" y="82" width="7" height="40">'+anim('opacity',[1,1,0,0,1,1])+'</rect></g></svg>';
 return s;
}
async function main(){
 const avatar=await loadImage(path.join(OUT,'avatar-pixel.png'));
 const canvas=createCanvas(W,H),ctx=canvas.getContext('2d');
 const render=t=>{
  ctx.fillStyle='#fff';ctx.fillRect(0,0,W,H);ctx.imageSmoothingEnabled=false;
  ctx.drawImage(avatar,18,4,212,212);
  const shift=blend(t,[0,0,1,1,0,0]),alpha=blend(t,[1,1,0,0,1,1]);
  ctx.globalAlpha=alpha;
  for(const p of dots){ctx.fillStyle=p.color;ctx.fillRect(p.x+p.dx*shift,p.y+p.dy*shift,p.s,p.s);}
  ctx.fillStyle='#43aceb';ctx.fillRect(1128,82,7,40);ctx.globalAlpha=1;
  const op=cubeOpacity(t);
  if(op>0){
   ctx.globalAlpha=op;ctx.strokeStyle='#cddae8';ctx.lineWidth=1;
   for(const [a,b]of grid){ctx.beginPath();ctx.moveTo(...a);ctx.lineTo(...b);ctx.stroke();}
   ctx.strokeStyle='#9aaec5';ctx.lineWidth=2.5;
   const frame=[[627,56,627,27,656,27],[1054,27,1083,27,1083,56],[1083,149,1083,178,1054,178],[656,178,627,178,627,149]];
   for(const a of frame){ctx.beginPath();ctx.moveTo(a[0],a[1]);ctx.lineTo(a[2],a[3]);ctx.lineTo(a[4],a[5]);ctx.stroke();}
   ctx.fillStyle='#def1fc';ctx.beginPath();ctx.ellipse(855,180,86,9,0,0,Math.PI*2);ctx.fill();
   for(const f of faces){
    if(!faceOpacity(f,t))continue;
    ctx.globalAlpha=op*smooth((t-2.3)/.55);ctx.fillStyle=f.fill;ctx.strokeStyle='#c9ebfd';ctx.lineWidth=1.7;
    const a=f.v.map(i=>project(verts[i],t));ctx.beginPath();ctx.moveTo(...a[0]);for(const q of a.slice(1))ctx.lineTo(...q);ctx.closePath();ctx.fill();ctx.stroke();
   }
   if(t<3){
    ctx.globalAlpha=op*(1-smooth((t-2.65)/.35));ctx.strokeStyle='#459cd2';ctx.lineWidth=1.5;
    for(const [a,b]of [[0,1],[1,2],[2,3],[3,0],[4,5],[5,6],[6,7],[7,4],[0,4],[1,5],[2,6],[3,7]]){ctx.beginPath();ctx.moveTo(...project(verts[a],t));ctx.lineTo(...project(verts[b],t));ctx.stroke();}
   }
  }
  ctx.globalAlpha=1;return canvas.toBuffer('image/png');
 };
 const avatar64=fs.readFileSync(path.join(OUT,'avatar-pixel.png')).toString('base64');
 fs.writeFileSync(path.join(OUT,'intro.svg'),makeSvg(avatar64));
 fs.writeFileSync(path.join(OUT,'poster.png'),render(0));
 fs.writeFileSync(path.join(OUT,'cube-frame.png'),render(3.5));
 const temp=path.join(OUT,'_frames');fs.mkdirSync(temp,{recursive:true});
 for(let i=0;i<DURATION*FPS;i++)fs.writeFileSync(path.join(temp,`${String(i).padStart(4,'0')}.png`),render(i/FPS));
 const r=spawnSync('ffmpeg',['-y','-v','error','-framerate',String(FPS),'-i',path.join(temp,'%04d.png'),'-filter_complex','[0:v]split[a][b];[a]palettegen=max_colors=192:stats_mode=diff[p];[b][p]paletteuse=dither=bayer:bayer_scale=3','-loop','0',path.join(OUT,'intro.gif')],{encoding:'utf8'});
 if(r.status!==0)throw new Error(r.stderr);
 fs.writeFileSync(path.join(OUT,'intro.wechat.html'),'<section style="margin:0;padding:0;line-height:0">'+fs.readFileSync(path.join(OUT,'intro.svg'),'utf8')+'</section>');
 fs.writeFileSync(path.join(OUT,'preview.html'),`<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>程序员拾梦 · 像素片头 v1</title><style>body{font-family:"Microsoft YaHei",sans-serif;margin:0;background:#eef3f8;color:#40536a}main{max-width:1040px;margin:40px auto;padding:28px;background:white;border-radius:16px}h1{font-size:20px}p{font-size:14px;color:#748499}img{display:block;width:100%;height:auto}button,a{font:inherit;font-size:13px;padding:9px 14px;border:1px solid #d7e5f0;border-radius:8px;background:#f5faff;color:#2787c8;cursor:pointer;text-decoration:none;margin-right:8px}.phone{width:375px;max-width:100%;border:1px solid #d9e4ed;margin-top:24px}nav{margin:24px 0}</style><main><h1>程序员拾梦 · 像素片头 v1</h1><p>6 秒循环 · 蓝色 · 1246 × 220 · SVG / GIF</p><img id="hero" src="intro.svg" alt="程序员拾梦像素片头"><nav><button onclick="document.getElementById('hero').src='intro.svg?replay='+Date.now()">播放 SVG</button><button onclick="document.getElementById('hero').src='poster.png'">文字画面</button><button onclick="document.getElementById('hero').src='cube-frame.png'">方块画面</button><a href="intro.gif" download>下载 GIF</a></nav><p>手机宽度预览</p><div class="phone"><img src="intro.gif" alt="手机宽度 GIF"></div><p>公众号后台与手机预览尚未验收。GIF 可作为普通动图上传；SVG 版请在编辑器保存后检查是否保留动效。</p></main></html>`);
 fs.writeFileSync(path.join(OUT,'manifest.json'),JSON.stringify({width:W,height:H,duration_seconds:DURATION,fps:FPS,frames:DURATION*FPS,text:['程序员拾梦','折腾 AI，分享实用玩法'],avatar_tool:'built-in image_gen',mobile_wechat_verified:false,dots:dots.length},null,2)+'\n');
 console.log(JSON.stringify({width:W,height:H,frames:DURATION*FPS,dots:dots.length,gif_bytes:fs.statSync(path.join(OUT,'intro.gif')).size}));
}
main().catch(e=>{console.error(e);process.exit(1)});
