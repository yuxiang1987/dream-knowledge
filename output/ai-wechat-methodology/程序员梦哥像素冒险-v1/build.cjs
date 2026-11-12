const fs=require('fs'),path=require('path'),{spawnSync}=require('child_process');
const {createCanvas,loadImage,GlobalFonts}=require('../程序员拾梦闯关片头五案-v1/node_modules/@napi-rs/canvas');
const OUT=__dirname,W=1200,H=360,GROUND=306,FPS=25,D=5.6,HIT=1.48;
const clamp=x=>Math.max(0,Math.min(1,x));
const ease=x=>{x=clamp(x);return x*x*(3-2*x);};
const mix=(a,b,p)=>a+(b-a)*clamp(p);
function state(t){
  let dy=0,sx=1,sy=1,pose='idle';
  if(t>=.56&&t<.9){const p=ease((t-.56)/.34);sx=1+.08*p;sy=1-.1*p;}
  if(t>=.9&&t<HIT){const p=(t-.9)/(HIT-.9);dy=48*(2*p-p*p);pose='jump';}
  if(t>=HIT&&t<1.96){const p=(t-HIT)/.48;dy=48*(1-p*p);pose='jump';}
  if(t>=1.96&&t<2.32){const p=(t-1.96)/.36,b=Math.sin(Math.PI*p)*(1-p);sx=1+.16*b;sy=1-.16*b;}
  const bump=t>=HIT&&t<HIT+.32?12*Math.sin(Math.PI*(t-HIT)/.32):0;
  const starP=ease((t-HIT)/1.3),starA=ease((t-HIT)/.12)*(1-ease((t-4.64)/.48));
  return {t,pose,x:250,y:GROUND-dy,sx,sy,hero_height:pose==='jump'?117:128,block_y:76-bump,star_x:mix(292,1122,starP),star_y:mix(60,68,starP)-Math.sin(starP*Math.PI)*40,star_alpha:starA,lit:ease((t-HIT)/.2)*(1-ease((t-4.64)/.48))};
}
async function main(){
  GlobalFonts.registerFromPath('C:/Windows/Fonts/msyhbd.ttc','CN');
  GlobalFonts.registerFromPath('C:/Windows/Fonts/consolab.ttf','EN');
  const sprites={};for(const p of ['idle','jump']){fs.copyFileSync(path.join(OUT,'../程序员拾梦闯关片头五案-v1',`sprite-${p}.png`),path.join(OUT,`sprite-${p}.png`));sprites[p]=await loadImage(path.join(OUT,`sprite-${p}.png`));}
  const canvas=createCanvas(W,H),c=canvas.getContext('2d');
  function r(x,y,w,h,color){c.fillStyle=color;c.fillRect(Math.round(x),Math.round(y),Math.round(w),Math.round(h));}
  function polygon(points,color){c.fillStyle=color;c.beginPath();points.forEach(([x,y],i)=>i?c.lineTo(x,y):c.moveTo(x,y));c.closePath();c.fill();}
  function cloud(x,y,s=1){c.save();c.translate(x,y);c.scale(s,s);r(0,16,112,28,'#4d6392');r(12,4,84,44,'#4d6392');r(28,-8,28,52,'#4d6392');r(66,0,18,42,'#4d6392');r(4,16,104,22,'#fffdf1');r(16,8,76,30,'#fffdf1');r(32,-4,20,40,'#fffdf1');r(70,4,10,32,'#fffdf1');r(12,34,88,6,'#bbf0ed');r(24,40,68,4,'#8fd5e0');c.restore();}
  function hill(x,h,w,color){const y=GROUND;polygon([[x,y],[x,y-h*.25],[x+w*.13,y-h*.25],[x+w*.13,y-h*.52],[x+w*.27,y-h*.52],[x+w*.27,y-h*.8],[x+w*.42,y-h*.8],[x+w*.42,y-h],[x+w*.58,y-h],[x+w*.58,y-h*.8],[x+w*.73,y-h*.8],[x+w*.73,y-h*.52],[x+w*.87,y-h*.52],[x+w*.87,y-h*.25],[x+w,y-h*.25],[x+w,y]],'#37543a');polygon([[x+4,y],[x+4,y-h*.25+4],[x+w*.13+4,y-h*.25+4],[x+w*.13+4,y-h*.52+4],[x+w*.27+4,y-h*.52+4],[x+w*.27+4,y-h*.8+4],[x+w*.42+4,y-h*.8+4],[x+w*.42+4,y-h+4],[x+w*.58-4,y-h+4],[x+w*.58-4,y-h*.8+4],[x+w*.73-4,y-h*.8+4],[x+w*.73-4,y-h*.52+4],[x+w*.87-4,y-h*.52+4],[x+w*.87-4,y-h*.25+4],[x+w-4,y-h*.25+4],[x+w-4,y]],color);r(x+w*.45,y-h*.65,4,10,'#426540');r(x+w*.6,y-h*.45,4,8,'#426540');}
  function brick(x,y,s=48){r(x,y,s,s,'#563c42');r(x+4,y+4,s-8,s-8,'#ce704c');r(x+4,y+4,s-8,4,'#f7bb7d');r(x+4,y+s/2,s-8,4,'#663c3d');r(x+s/2,y+8,4,s/2-8,'#663c3d');r(x+s/3,y+s/2+4,4,s/2-8,'#663c3d');}
  function glyph(str,size,color,font='CN'){
    const p=createCanvas(Math.ceil(size*str.length+16),size+16),g=p.getContext('2d');g.font=`bold ${size}px ${font}`;g.textBaseline='top';g.fillStyle=color;g.fillText(str,4,2);return p;
  }
  const name=glyph('程序员梦哥',40,'#fff4cf'),nameShadow=glyph('程序员梦哥',40,'#713e3b');
  const tagline=glyph('折腾 AI，分享实用玩法',17,'#313c67');
  const ai=glyph('AI',17,'#68413c','EN'),aiLit=glyph('AI',17,'#fff7ce','EN');
  function stamp(im,x,y,s=2){c.imageSmoothingEnabled=false;c.drawImage(im,x,y,im.width*s,im.height*s);}
  function star(x,y,a,t){
    if(a<=0)return;c.save();c.globalAlpha=a;
    const grid=['......#......','.....###.....','....#####....','#############','.###########.','..#########..','...#######...','..#########..','..####.####..','.####...####.','.##.......##.'];
    const z=4;grid.forEach((row,j)=>[...row].forEach((v,i)=>{if(v==='#'){const inside=[[i-1,j],[i+1,j],[i,j-1],[i,j+1]].every(([a,b])=>grid[b]?.[a]==='#');r(x+(i-6)*z,y+(j-5)*z,z,z,inside?'#ffdf65':'#b47a32');}}));
    r(x-6,y-2,3,7,'#614639');r(x+5,y-2,3,7,'#614639');
    if(t>2.75){const q=.5+.5*Math.sin((t-2.75)*5);c.globalAlpha=a*q;r(x+25,y-15,3,9,'#fff4bd');r(x+22,y-12,9,3,'#fff4bd');}
    c.restore();
  }
  function scene(t){
    const s=state(t);c.globalAlpha=1;r(0,0,W,H,'#a9b6ff');
    cloud(38,36,.78);cloud(390,22,.55);cloud(1050,25,.64);cloud(850,245,.42);cloud(86,190,.46);
    hill(-30,72,168,'#7bb852');hill(355,48,172,'#8bc45e');hill(870,67,226,'#72aa4c');hill(1072,39,150,'#97c466');
    // 像素招牌：名称始终可见，动作结束后继续留给读者阅读。
    r(470,58,646,140,'#6e4650');r(476,52,634,140,'#ffe2a0');r(480,56,626,132,'#c86536');r(488,64,610,112,'#df7b3f');r(488,64,610,5,'#f6ad61');r(488,172,610,7,'#ac4d32');
    for(const x of [490,1091])for(const y of [66,170]){r(x,y,6,6,'#fff2c1');r(x+2,y+2,2,2,'#83504b');}
    stamp(nameShadow,568,77);stamp(name,564,71);
    stamp(tagline,578,216);
    // 动作触发后，由左至右点亮副标题下方的像素短线。
    r(588,261,374,4,'#8b98e0');if(s.lit>0)r(588,261,374*s.lit,4,'#fff0a2');
    brick(198,80,48);brick(330,80,48);
    r(257,s.block_y,70,68,'#654241');r(261,s.block_y+4,62,60,s.lit>.05?'#e6a543':'#f6c25e');r(265,s.block_y+8,54,5,'#fff0ac');r(265,s.block_y+56,54,7,'#be7739');
    for(const x of [265,314])for(const y of [s.block_y+17,s.block_y+48])r(x,y,3,3,'#9d6339');
    stamp(ai,263,s.block_y+16,2);if(s.lit>0){c.globalAlpha=s.lit;stamp(aiLit,263,s.block_y+16,2);c.globalAlpha=1;}
    // 地面阴影随离地高度收缩，身体在起跳前蓄力，落地后回弹。
    const shadow=1-(GROUND-s.y)/90;r(250-30*shadow,GROUND-3,60*shadow,5,'#6c71a6');
    const im=sprites[s.pose],hh=s.hero_height,ww=hh*im.width/im.height;c.save();c.translate(s.x,s.y);c.scale(s.sx,s.sy);c.imageSmoothingEnabled=false;c.drawImage(im,0,0,im.width,im.height,-ww/2,-hh,ww,hh);c.restore();
    if(t>=HIT&&t<HIT+.28){const p=(t-HIT)/.28;c.globalAlpha=1-p;for(let i=0;i<7;i++){const a=i*Math.PI/3.5;r(292+Math.cos(a)*(16+22*p),132+Math.sin(a)*(10+22*p),4,4,'#fff3ac');}c.globalAlpha=1;}
    if(t>=1.96&&t<2.24){const p=(t-1.96)/.28;c.globalAlpha=1-p;r(225-16*p,GROUND-6,7,4,'#ffe7b7');r(275+16*p,GROUND-8,7,4,'#ffe7b7');c.globalAlpha=1;}
    star(s.star_x,s.star_y,s.star_alpha,t);
    r(0,GROUND,W,4,'#593a42');r(0,GROUND+4,W,5,'#ffcc8c');
    for(let row=0;row<2;row++)for(let x=-28;x<W;x+=56)brick(x+(row%2)*28,GROUND+9+row*27,56);
    return s;
  }
  const frames=path.join(OUT,'_frames');fs.mkdirSync(frames,{recursive:true});const states=[];
  for(let i=0;i<D*FPS;i++){const t=i===D*FPS-1?0:i/FPS;states.push(state(t));scene(t);fs.writeFileSync(path.join(frames,`${String(i).padStart(4,'0')}.png`),canvas.toBuffer('image/png'));}
  scene(3.3);fs.writeFileSync(path.join(OUT,'poster.png'),canvas.toBuffer('image/png'));
  const sheet=createCanvas(1200,4*180),sc=sheet.getContext('2d');[0,.8,1.44,1.68,2.08,2.72,3.4,5.4].forEach((t,i)=>{scene(t);sc.drawImage(canvas,(i%2)*600,Math.floor(i/2)*180,600,180);});fs.writeFileSync(path.join(OUT,'keyframes.png'),sheet.toBuffer('image/png'));
  const mobile=createCanvas(375,113);scene(3.3);mobile.getContext('2d').drawImage(canvas,0,0,375,112.5);fs.writeFileSync(path.join(OUT,'mobile.png'),mobile.toBuffer('image/png'));
  const run=spawnSync('ffmpeg',['-y','-v','error','-framerate',String(FPS),'-i',path.join(frames,'%04d.png'),'-filter_complex','[0:v]split[a][b];[a]palettegen=max_colors=256:stats_mode=full[p];[b][p]paletteuse=dither=bayer:bayer_scale=3','-loop','0',path.join(OUT,'intro.gif')],{encoding:'utf8'});if(run.status!==0)throw Error(run.stderr);
  fs.writeFileSync(path.join(OUT,'manifest.json'),JSON.stringify({name:'程序员梦哥',tagline:'折腾 AI，分享实用玩法',width:W,height:H,fps:FPS,frame_count:D*FPS,duration_seconds:D,hit_at:HIT,ground:GROUND,block_bottom:144,method:'Existing pixel sprites; Canvas scene and FFmpeg GIF; no new image generation',wechat_verified:false,states},null,2)+'\n');
  fs.writeFileSync(path.join(OUT,'preview.html'),`<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>程序员梦哥 · 像素冒险</title><style>*{box-sizing:border-box}body{margin:0;background:#eef0fa;color:#353c65;font:15px/1.8 "Microsoft YaHei",sans-serif}main{max-width:1100px;margin:28px auto;background:#fff;padding:28px;border-radius:16px}h1{margin:0 0 6px;font-size:23px}h2{font-size:17px;margin-top:26px}p{color:#767c99}img{display:block;width:100%}.phone{width:375px;max-width:100%;border:1px solid #e3e6f0}.body{padding:18px 24px}button,a{display:inline-block;background:#fff;border:1px solid #d5dbed;border-radius:6px;padding:7px 13px;color:#4a65ac;font:inherit;text-decoration:none;margin:12px 8px 0 0}@media(max-width:650px){main{margin:0;padding:18px;border-radius:0}}</style><main><h1>程序员梦哥 · 像素冒险</h1><p>蓄力 → 跳起顶 AI 砖 → 星星归位 → 停留阅读，5.6秒循环。</p><img id="hero" src="intro.gif" alt="程序员梦哥像素小人跳起顶AI砖，星星飞到招牌旁"><button onclick="document.querySelectorAll('img[data-loop],#hero').forEach(im=>im.src='intro.gif?t='+Date.now())">从头播放</button><a href="intro.gif" download>下载 GIF</a><h2>375px 公众号首屏预览</h2><div class="phone"><img data-loop src="intro.gif" alt="375px像素片头"><div class="body"><b>你好，我是梦哥。</b><p>这里接文章第一段，进入今天的 AI 新玩法。</p></div></div><h2>动作关键帧</h2><img src="keyframes.png" alt="蓄力、起跳、顶砖、落地与停留八个时刻"><p>复用既有角色素材，代码制作动画。本地候选预览；公众号后台和真机效果待验收。</p></main></html>`);
  console.log(JSON.stringify({frames:D*FPS,gif_bytes:fs.statSync(path.join(OUT,'intro.gif')).size,duration:D}));
}
if(require.main===module)main().catch(e=>{console.error(e);process.exitCode=1});
module.exports={state};
