const fs=require('fs');
const path=require('path');
const {spawnSync}=require('child_process');
const {createCanvas,loadImage}=require('@napi-rs/canvas');
const {dots,blend,cubeOpacity,makeSvg}=require('./build.cjs');
const ROOT=__dirname, OUT=path.join(ROOT,'variants'), W=1246,H=220,FPS=20;
const blue='#269ee8',deep='#50758e',light='#dcedf8';
const clamp=x=>Math.max(0,Math.min(1,x));
const ease=x=>{x=clamp(x);return x*x*(3-2*x);};
const f=x=>Math.round(x*100)/100;
const times=Array.from({length:121},(_,i)=>i/120);
const animate=(name,values)=>`<animate attributeName="${name}" dur="6s" repeatCount="indefinite" keyTimes="${times.join(';')}" values="${values.join(';')}"/>`;
const animTransform=(type,values)=>`<animateTransform attributeName="transform" type="${type}" dur="6s" repeatCount="indefinite" keyTimes="${times.join(';')}" values="${values.join(';')}"/>`;
// Each frame describes primitives shared by SVG and canvas, so both exports agree.
function windowScene(t){
 const s=[],u=t-2.12;
 s.push({type:'rect',x:642,y:34,w:426,h:150,fill:'#f7fbff',stroke:'#84bddf',line:2});
 s.push({type:'rect',x:644,y:36,w:422,h:25,fill:'#e7f3fc'});
 [0,1,2].forEach((j)=>s.push({type:'rect',x:657+j*15,y:45,w:6,h:6,fill:['#79a5c2','#46b1eb','#a1d2ec'][j]}));
 s.push({type:'path',p:[[691,90],[679,102],[691,114]],stroke:blue,line:5});
 const rows=[{x:716,y:86,w:172},{x:716,y:106,w:240},{x:716,y:126,w:198},{x:716,y:146,w:135}];
 rows.forEach((a,i)=>{
  const progress=ease((u-.28-i*.18)/.45);
  s.push({type:'rect',x:a.x,y:a.y,w:a.w*progress,h:7,fill:i===2?'#7bbade':blue});
 });
 const q=ease((u-1.1)/.5);
 s.push({type:'path',p:[[990,126],[1001,137],[1021,112]],stroke:'#30a3bf',line:5,opacity:q});
 const cx=716+135*ease((u-.82)/.45);
 s.push({type:'rect',x:cx+8,y:143,w:5,h:13,fill:blue,opacity:Math.sin(u*11)>0?1:.2});
 return s;
}
function folderScene(t){
 const s=[],u=t-2.12;
 for(const x of [654,978]){
  s.push({type:'path',p:[[x,79],[x+36,79],[x+46,91],[x+94,91],[x+94,156],[x,156]],closed:true,
   fill:x===654?'#ebf7ff':'#d8f0ff',stroke:'#4daddd',line:2.5});
  s.push({type:'path',p:[[x+1,102],[x+94,102]],stroke:'#84c8ea',line:2});
 }
 s.push({type:'path',p:[[760,128],[957,128]],stroke:'#c8e4f5',line:2,dash:[4,7]});
 s.push({type:'path',p:[[945,120],[957,128],[945,136]],stroke:'#85bddf',line:2});
 for(let i=0;i<4;i++){
  const p=clamp((u-.15-i*.23)/1.1);
  const x=738+242*p,y=105-Math.sin(p*Math.PI)*(22+i*3);
  const a=ease(p/.12)*(1-ease((p-.83)/.17));
  s.push({type:'rect',x,y,w:15,h:19,fill:i%2?'#78c9ef':blue,opacity:a});
  s.push({type:'rect',x:x+3,y:y+5,w:9,h:2,fill:'#fff',opacity:a});
 }
 const n=Math.floor(ease((u-1)/.8)*4);
 for(let i=0;i<n;i++)s.push({type:'rect',x:994+i*15,y:125,w:10,h:18,fill:'#46afe5'});
 return s;
}
const seeds=Array.from({length:30},(_,i)=>({a:i*2.39996,r:58+((i*37)%70),s:3+(i%3)*2}));
function sparkScene(t){
 const s=[],u=t-2.12,q=ease((u-.25)/.8);
 s.push({type:'ellipse',cx:855,cy:118,rx:147,ry:42,stroke:'#dfedf7',line:1.5});
 seeds.forEach((p,i)=>{
  const a=p.a+u*.42,r=p.r*(1-q*.6);
  const x=855+Math.cos(a)*r,y=105+Math.sin(a)*r*.64;
  s.push({type:'rect',x:x-p.s/2,y:y-p.s/2,w:p.s,h:p.s,fill:i%3?'#70c3ee':blue,opacity:.45+.4*(i%2)});
 });
 const scale=ease((u-.35)/.7)*(.94+.05*Math.sin(u*4));
 const star=[[0,-56],[10,-23],[24,-12],[56,0],[24,12],[10,24],[0,56],[-10,24],[-24,12],[-56,0],[-24,-12],[-10,-23]];
 s.push({type:'path',p:star.map(([x,y])=>[855+x*scale,105+y*scale]),closed:true,fill:blue,stroke:'#7acff5',line:2});
 s.push({type:'rect',x:849,y:99,w:12,h:12,fill:'#e4f8ff',opacity:q});
 return s;
}
const variants=[{id:'code-window',name:'代码窗口',scene:windowScene,description:'窗口展开，代码逐行刷出，光标闪动。'},
 {id:'file-flow',name:'文件夹与数据流',scene:folderScene,description:'像素文件从一个文件夹流向另一个文件夹。'},
 {id:'spark-orbit',name:'像素火花汇聚',scene:sparkScene,description:'像素粒子环绕、聚拢，形成蓝色四芒火花。'}];
const attrs=p=>`fill="${p.fill||'none'}" stroke="${p.stroke||'none'}" stroke-width="${p.line||1}" stroke-linejoin="miter" ${p.dash?'stroke-dasharray="'+p.dash.join(' ')+'"':''}`;
function sceneSvg(scene){
 const frames=times.map(u=>scene(u*6));
 // The folder fill bars are kept as invisible primitives before they arrive.
 const length=Math.max(...frames.map(a=>a.length));
 let svg='<g opacity="0">'+animate('opacity',times.map(u=>f(cubeOpacity(u*6))));
 for(let i=0;i<length;i++){
  const sample=frames.find(a=>a[i])?.[i];if(!sample)continue;
  const list=frames.map(a=>a[i]||{...sample,opacity:0});
  const props=attrs(sample);
  if(sample.type==='rect'){
   svg+=`<rect ${props}>`;
   for(const [a,k]of [['x','x'],['y','y'],['width','w'],['height','h']])svg+=animate(a,list.map(p=>f(p[k])));
   svg+=animate('opacity',list.map(p=>p.opacity??1))+'</rect>';
  }else if(sample.type==='ellipse'){
   svg+=`<ellipse cx="${sample.cx}" cy="${sample.cy}" rx="${sample.rx}" ry="${sample.ry}" ${props}/>`;
  }else{
   const d=p=>'M'+p.p.map(q=>q.map(f).join(' ')).join('L')+(p.closed?'Z':'');
   svg+=`<path ${props}>`+animate('d',list.map(d))+animate('opacity',list.map(p=>p.opacity??1))+'</path>';
  }
 }
 return svg+'</g>';
}
function drawScene(ctx,primitives){
 for(const p of primitives){
  ctx.save();ctx.globalAlpha*=p.opacity??1;ctx.fillStyle=p.fill||'transparent';ctx.strokeStyle=p.stroke||'transparent';ctx.lineWidth=p.line||1;
  ctx.setLineDash(p.dash||[]);
  if(p.type==='rect'){if(p.fill)ctx.fillRect(p.x,p.y,p.w,p.h);if(p.stroke)ctx.strokeRect(p.x,p.y,p.w,p.h);}
  else{ctx.beginPath();if(p.type==='ellipse')ctx.ellipse(p.cx,p.cy,p.rx,p.ry,0,0,Math.PI*2);
   else{ctx.moveTo(...p.p[0]);for(const v of p.p.slice(1))ctx.lineTo(...v);if(p.closed)ctx.closePath();}
   if(p.fill)ctx.fill();if(p.stroke)ctx.stroke();}
  ctx.restore();
 }
}
async function main(){
 fs.mkdirSync(OUT,{recursive:true});
 const avatar=await loadImage(path.join(ROOT,'avatar-pixel.png'));
 const avatar64=fs.readFileSync(path.join(ROOT,'avatar-pixel.png')).toString('base64');
 const base=makeSvg(avatar64);
 const canvas=createCanvas(W,H),ctx=canvas.getContext('2d');
 const manifest=[];
 for(const v of variants){
  const render=t=>{
   ctx.globalAlpha=1;ctx.fillStyle='#fff';ctx.fillRect(0,0,W,H);ctx.imageSmoothingEnabled=false;ctx.drawImage(avatar,18,4,212,212);
   const shift=blend(t,[0,0,1,1,0,0]);ctx.globalAlpha=blend(t,[1,1,0,0,1,1]);
   for(const p of dots){ctx.fillStyle=p.color;ctx.fillRect(p.x+p.dx*shift,p.y+p.dy*shift,p.s,p.s);}
   ctx.fillStyle='#43aceb';ctx.fillRect(1128,82,7,40);
   ctx.globalAlpha=cubeOpacity(t);drawScene(ctx,v.scene(t));ctx.globalAlpha=1;
   return canvas.toBuffer('image/png');
  };
  const right=sceneSvg(v.scene);
  const svg=base.replace(/<!--right-motion:start-->[\s\S]*?<!--right-motion:end-->/,right)
   .replace('蓝色代码方块出现并旋转',v.description.replace(/。$/,''));
  fs.writeFileSync(path.join(OUT,v.id+'.svg'),svg);
  fs.writeFileSync(path.join(OUT,v.id+'-poster.png'),render(0));
  fs.writeFileSync(path.join(OUT,v.id+'-still.png'),render(3.5));
  const frames=path.join(ROOT,'_frames',v.id);fs.mkdirSync(frames,{recursive:true});
  for(let i=0;i<120;i++)fs.writeFileSync(path.join(frames,`${String(i).padStart(4,'0')}.png`),render(i/FPS));
  const r=spawnSync('ffmpeg',['-y','-v','error','-framerate',String(FPS),'-i',path.join(frames,'%04d.png'),'-filter_complex','[0:v]split[a][b];[a]palettegen=max_colors=192:stats_mode=diff[p];[b][p]paletteuse=dither=bayer:bayer_scale=3','-loop','0',path.join(OUT,v.id+'.gif')],{encoding:'utf8'});
  if(r.status!==0)throw new Error(r.stderr);
  manifest.push({id:v.id,name:v.name,description:v.description,width:W,height:H,duration_seconds:6,fps:FPS,frames:120,gif_bytes:fs.statSync(path.join(OUT,v.id+'.gif')).size,mobile_wechat_verified:false});
 }
 fs.writeFileSync(path.join(OUT,'manifest.json'),JSON.stringify(manifest,null,2)+'\n');
 const cards=manifest.map((v,i)=>`<article><h2>${String.fromCharCode(65+i)} · ${v.name}</h2><p>${v.description}</p><img src="${v.id}.gif" alt="${v.name}动画"><nav><a href="${v.id}.gif" download>GIF</a><a href="${v.id}.svg" download>SVG</a><button onclick="this.parentElement.previousElementSibling.src='${v.id}-still.png'">定帧</button><button onclick="this.parentElement.previousElementSibling.src='${v.id}.gif?'+Date.now()">重播</button></nav></article>`).join('');
 fs.writeFileSync(path.join(OUT,'preview.html'),`<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>程序员拾梦 · 右侧动效三款</title><style>body{margin:0;background:#eef3f8;color:#42556c;font:15px "Microsoft YaHei",sans-serif}main{max-width:1100px;margin:28px auto;padding:0 20px}h1{font-size:22px}h2{font-size:17px;margin:0}p{color:#7c8ba0;font-size:13px}article{background:white;border-radius:12px;padding:20px;margin:18px 0}img{display:block;width:100%;height:auto}nav{margin-top:12px}a,button{border:1px solid #d9e8f3;background:#f4faff;color:#328bc6;border-radius:7px;text-decoration:none;padding:6px 12px;margin-right:8px;font:13px "Microsoft YaHei",sans-serif;cursor:pointer}</style><main><h1>右侧动效 · 三款对比</h1><p>头像、文字、蓝色和6秒循环一致。原方块版保留。公众号后台与真机微信尚未验收。</p>${cards}<p><a href="../intro.gif">原版旋转方块</a></p></main></html>`);
 console.log(JSON.stringify(manifest));
}
main().catch(e=>{console.error(e);process.exit(1)});
