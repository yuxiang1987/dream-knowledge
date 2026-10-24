const fs=require('fs'),path=require('path');
const {spawnSync}=require('child_process');
const {createCanvas,loadImage,GlobalFonts}=require('@napi-rs/canvas');
const OUT=__dirname,W=1246,H=300,D=8,FPS=20,BASE=156,SPRITE_H=112;
GlobalFonts.registerFromPath('C:/Windows/Fonts/msyhbd.ttc','BrandCJK');
const chars=[...'程序员拾梦'],centers=[300,460,620,780,940];
const route=[0,1,2,3,4,3,2,1,0];
const hops=route.slice(1).map((to,i)=>({from:route[i],to,start:.35+i*.85,end:.95+i*.85}));
const clamp=x=>Math.max(0,Math.min(1,x));
const ease=x=>{x=clamp(x);return x*x*(3-2*x);};
const f=n=>Math.round(n*1000)/1000;
function glyph(text,size){
 const c=createCanvas(size*text.length+30,size+20),x=c.getContext('2d');
 x.font=`bold ${size}px BrandCJK`;x.textBaseline='top';x.fillStyle='white';x.fillText(text,0,0);
 const a=x.getImageData(0,0,c.width,c.height).data,p=[];let minX=Infinity,minY=Infinity,maxX=0,maxY=0;
 for(let y=0;y<c.height;y++)for(let xx=0;xx<c.width;xx++)if(a[(y*c.width+xx)*4+3]>150){p.push([xx,y]);minX=Math.min(minX,xx);minY=Math.min(minY,y);maxX=Math.max(maxX,xx);maxY=Math.max(maxY,y);}
 return {points:p.map(([xx,y])=>[xx-minX,y-minY]),w:maxX-minX+1,h:maxY-minY+1};
}
const letters=chars.map(text=>glyph(text,36)),caption=glyph('折腾 AI，分享实用玩法',16);
function bounce(i,t){
 let y=0;
 for(const h of hops){const age=t-h.end;if(h.to===i&&age>=0&&age<.32)y+=7*Math.exp(-age*11)*Math.sin(age*24);}
 return y;
}
function state(t){
 t=Math.max(0,Math.min(D,t));let idx=0,x=centers[0],foot=BASE,sy=1,angle=0,dir=1,air=false,from=0,to=0,progress=0;
 const dy=chars.map((_,i)=>bounce(i,t));
 for(const h of hops){
  if(t<h.start){
   idx=h.from;dir=Math.sign(h.to-h.from);x=centers[idx];
   const q=ease((t-(h.start-.17))/.17);sy=1-.16*q;dy[idx]+=5*q;foot=BASE+dy[idx];break;
  }
  if(t<=h.end){
   const p=(t-h.start)/(h.end-h.start);air=true;from=h.from;to=h.to;progress=p;idx=from;
   dir=Math.sign(h.to-h.from);x=centers[from]+(centers[to]-centers[from])*p;
   foot=BASE+5*(1-p)-30*4*p*(1-p);
   sy=p<.15?.84+.23*ease(p/.15):1+.07*Math.sin(Math.PI*p);
   angle=dir*5*Math.sin(Math.PI*p);break;
  }
  idx=h.to;x=centers[idx];foot=BASE+dy[idx];dir=Math.sign(h.to-h.from);
 }
 if(!air){
  let last=null;for(const h of hops)if(t>=h.end&&h.to===idx)last=h;
  if(last){const age=t-last.end;if(age<.22)sy*=1-.12*Math.sin(Math.PI*age/.22);}
  if(t>7.2)dir=1;
 }
 const colors=chars.map((_,i)=>i===idx?'#258fdf':i<idx?'#82bfe7':'#63748b');
 if(air){colors[to]=progress>.75?'#42a4e4':'#63748b';}
 return {t,idx,x,foot,sy,sx:1/Math.sqrt(sy),angle,dir,air,from,to,progress,dy,colors};
}
function sparks(t){
 const p=[];
 for(const h of hops){const age=t-h.end;if(age<0||age>.34)continue;
  for(let i=0;i<5;i++){const a=Math.PI+(.16+i*.17)*Math.PI,r=7+age*76;p.push({x:centers[h.to]+Math.cos(a)*r,y:BASE+Math.sin(a)*r,s:3+(i%2),opacity:(1-age/.34)*.65});}
 }
 return p;
}
function alphaBox(image){
 const c=createCanvas(image.width,image.height),x=c.getContext('2d');x.drawImage(image,0,0);
 const a=x.getImageData(0,0,c.width,c.height).data;let left=c.width,top=c.height,right=0,bottom=0;
 for(let y=0;y<c.height;y++)for(let xx=0;xx<c.width;xx++)if(a[(y*c.width+xx)*4+3]>200){left=Math.min(left,xx);top=Math.min(top,y);right=Math.max(right,xx);bottom=Math.max(bottom,y);}
 return {x:left,y:top,w:right-left+1,h:bottom-top+1};
}
const rects=(g,scale)=>g.points.map(([x,y])=>`<rect x="${f((x-g.w/2)*scale)}" y="${f(y*scale)}" width="${f(scale*.94)}" height="${f(scale*.94)}"/>`).join('');
const timeline=Array.from({length:D*FPS+1},(_,i)=>i/(D*FPS));
const states=timeline.map(u=>state(u*D));
const animate=(attr,values)=>`<animate attributeName="${attr}" values="${values.join(';')}" keyTimes="${timeline.map(f).join(';')}" dur="8s" repeatCount="indefinite"/>`;
const transform=(type,values)=>`<animateTransform attributeName="transform" type="${type}" values="${values.join(';')}" keyTimes="${timeline.map(f).join(';')}" dur="8s" repeatCount="indefinite"/>`;
function makeSvg(box,spriteW){
 const encoded=fs.readFileSync(path.join(OUT,'jumper.png')).toString('base64');
 let s=`<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" role="img" aria-label="程序员拾梦像素小人在五个字上逐个跳跃，落地文字回弹，八秒循环。"><rect width="1246" height="300" fill="white"/>`;
 s+='<g shape-rendering="crispEdges">';
 letters.forEach((g,i)=>{
  s+=`<g id="letter-${i}" fill="${states[0].colors[i]}">${transform('translate',states.map(v=>`${centers[i]} ${f(160+v.dy[i])}`))}${animate('fill',states.map(v=>v.colors[i]))}`;
  s+=rects(g,2.75)+'<rect x="-17" y="-4" width="34" height="4"/>';
  s+='</g>';
 });
 s+=`<g transform="translate(623 269)" fill="#8b9caf">${rects(caption,1.65)}</g></g>`;
 s+='<ellipse fill="#c5e7fa" rx="19" ry="3">'+animate('cx',states.map(v=>f(v.x)))+animate('cy',states.map(v=>f(BASE+5+(v.air?0:v.dy[v.idx]))))+animate('opacity',states.map(v=>v.air?.35:.65))+'</ellipse>';
 s+='<g>';s+=transform('translate',states.map(v=>`${f(v.x)} ${f(v.foot)}`));
 s+='<g>'+transform('rotate',states.map(v=>f(v.angle)));
 s+='<g>'+transform('scale',states.map(v=>`${f(v.dir*v.sx)} ${f(v.sy)}`));
 s+=`<svg x="${-spriteW/2}" y="-112" width="${spriteW}" height="112" viewBox="${box.x} ${box.y} ${box.w} ${box.h}" overflow="hidden"><image x="0" y="0" width="1024" height="1536" style="image-rendering:pixelated" xlink:href="data:image/png;base64,${encoded}"/></svg></g></g></g>`;
 for(let j=0;j<hops.length*5;j++){
  const h=hops[Math.floor(j/5)],i=j%5;
  const values=timeline.map(u=>{const age=u*D-h.end,a=Math.PI+(.16+i*.17)*Math.PI,r=7+Math.max(0,age)*76;return {x:f(centers[h.to]+Math.cos(a)*r),y:f(BASE+Math.sin(a)*r),o:age<0||age>.34?0:f((1-age/.34)*.65)};});
  s+=`<rect width="${3+i%2}" height="${3+i%2}" fill="#49ade8">${animate('x',values.map(v=>v.x))}${animate('y',values.map(v=>v.y))}${animate('opacity',values.map(v=>v.o))}</rect>`;
 }
 return s+'</svg>';
}
async function main(){
 const image=await loadImage(path.join(OUT,'jumper.png')),box=alphaBox(image),spriteW=SPRITE_H*box.w/box.h;
 const canvas=createCanvas(W,H),ctx=canvas.getContext('2d');
 function render(t){
  const v=state(t);ctx.setTransform(1,0,0,1,0,0);ctx.globalAlpha=1;ctx.fillStyle='white';ctx.fillRect(0,0,W,H);ctx.imageSmoothingEnabled=false;
  letters.forEach((g,i)=>{ctx.fillStyle=v.colors[i];for(const [x,y]of g.points)ctx.fillRect(centers[i]+(x-g.w/2)*2.75,160+v.dy[i]+y*2.75,2.75*.94,2.75*.94);ctx.fillRect(centers[i]-17,BASE+v.dy[i],34,4);});
  ctx.fillStyle='#8b9caf';for(const [x,y]of caption.points)ctx.fillRect(623+(x-caption.w/2)*1.65,269+y*1.65,1.65*.94,1.65*.94);
  ctx.globalAlpha=v.air?.35:.65;ctx.fillStyle='#c5e7fa';ctx.beginPath();ctx.ellipse(v.x,BASE+5+(v.air?0:v.dy[v.idx]),19,3,0,0,Math.PI*2);ctx.fill();ctx.globalAlpha=1;
  ctx.save();ctx.translate(v.x,v.foot);ctx.rotate(v.angle*Math.PI/180);ctx.scale(v.dir*v.sx,v.sy);
  ctx.drawImage(image,box.x,box.y,box.w,box.h,-spriteW/2,-SPRITE_H,spriteW,SPRITE_H);ctx.restore();
  ctx.fillStyle='#49ade8';for(const p of sparks(t)){ctx.globalAlpha=p.opacity;ctx.fillRect(p.x,p.y,p.s,p.s);}ctx.globalAlpha=1;
  return canvas.toBuffer('image/png');
 }
 fs.writeFileSync(path.join(OUT,'intro.svg'),makeSvg(box,spriteW));
 fs.writeFileSync(path.join(OUT,'poster.png'),render(0));
 for(const [name,t]of [['takeoff',.35],['airborne',.65],['landing',.98],['last-letter',3.55]])fs.writeFileSync(path.join(OUT,name+'.png'),render(t));
 const frames=path.join(OUT,'_frames');fs.mkdirSync(frames,{recursive:true});
 for(let i=0;i<D*FPS;i++)fs.writeFileSync(path.join(frames,String(i).padStart(4,'0')+'.png'),render(i/FPS));
 const run=spawnSync('ffmpeg',['-y','-v','error','-framerate',String(FPS),'-i',path.join(frames,'%04d.png'),'-filter_complex','[0:v]split[a][b];[a]palettegen=max_colors=192:stats_mode=diff[p];[b][p]paletteuse=dither=bayer:bayer_scale=3','-loop','0',path.join(OUT,'intro.gif')],{encoding:'utf8'});
 if(run.status!==0)throw new Error(run.stderr);
 fs.writeFileSync(path.join(OUT,'intro.wechat.html'),'<section style="margin:0;padding:0;line-height:0">'+fs.readFileSync(path.join(OUT,'intro.svg'),'utf8')+'</section>');
 fs.writeFileSync(path.join(OUT,'motion.json'),JSON.stringify({width:W,height:H,duration_seconds:D,fps:FPS,frames:D*FPS,baseline:BASE,sprite_height:SPRITE_H,sprite_width:spriteW,sprite_box:box,route,hops,states:states.map(v=>({...v,t:f(v.t)})),mobile_wechat_verified:false},null,2)+'\n');
 const buttons=[['播放动图','intro.gif'],['起跳','takeoff.png'],['腾空','airborne.png'],['落地','landing.png'],['最后一个字','last-letter.png']].map(([text,file])=>`<button onclick="document.getElementById('hero').src='${file}?'+Date.now()">${text}</button>`).join('');
 fs.writeFileSync(path.join(OUT,'preview.html'),`<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>程序员拾梦 · 跳字片头</title><style>body{margin:0;background:#eff4f9;color:#42566e;font:14px "Microsoft YaHei",sans-serif}main{max-width:1100px;margin:32px auto;padding:24px;background:white;border-radius:14px}h1{font-size:21px}p{color:#7b8ca1}img{width:100%;height:auto;display:block}button,a{font:inherit;font-size:13px;background:#f2f9ff;color:#278ccb;border:1px solid #dcebf7;padding:8px 12px;border-radius:7px;text-decoration:none;margin-right:7px;cursor:pointer}nav{margin:20px 0}.phone{width:375px;max-width:100%;border:1px solid #e2edf5}</style><main><h1>程序员拾梦 · 在文字上跳一跳</h1><p>逐字跳跃 · 落地回弹 · 像素碎屑 · 8秒往返循环</p><img id="hero" src="intro.gif" alt="像素小人在程序员拾梦五个字上跳跃"><nav>${buttons}<a href="intro.gif" download>下载GIF</a><a href="intro.svg" download>下载SVG</a></nav><p>手机宽度预览</p><div class="phone"><img src="intro.gif" alt="375px宽度预览"></div><p>本地预览，公众号后台和真机微信效果尚未验收。</p></main></html>`);
 console.log(JSON.stringify({width:W,height:H,duration:D,gif_bytes:fs.statSync(path.join(OUT,'intro.gif')).size,sprite_box:box}));
}
if(require.main===module)main().catch(e=>{console.error(e);process.exit(1)});
module.exports={state,centers,hops,BASE,SPRITE_H};
