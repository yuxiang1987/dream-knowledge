const fs = require('fs');
const path = require('path');
const {spawnSync} = require('child_process');
const {createCanvas, loadImage, GlobalFonts} = require('../程序员拾梦闯关片头五案-v1/node_modules/@napi-rs/canvas');
const W=1200, H=400, FPS=20, D=7.2, GROUND=350, HERO=128;
const words=['折','腾','ai','，','分','享','实','用','玩','法'];
const widths=[78,78,110,64,78,78,78,78,78,78];
const clamp=v=>Math.max(0,Math.min(1,v));
const ease=v=>{v=clamp(v);return v*v*(3-2*v);};
const mix=(a,b,t)=>a+(b-a)*clamp(t);
function state(t) {
  let x, y=GROUND, pose='run';
  if(t<1.2) x=mix(-70,365,ease(t/1.2));
  else if(t<2.2){x=365;y-=60*Math.sin(Math.PI*(t-1.2));pose='jump';}
  else if(t<4.5)x=mix(365,1040,ease((t-2.2)/2.3));
  else {x=1040;pose='wave';}
  return {x,y,pose,hit:t>=1.7,reset:ease((t-6.55)/.55)};
}
async function main(){
  GlobalFonts.registerFromPath('C:/Windows/Fonts/msyhbd.ttc','Chinese');
  const sprites={};
  for(const pose of ['run','jump','wave'])sprites[pose]=await loadImage(path.join(__dirname,`sprite-${pose}.png`));
  const canvas=createCanvas(W,H),ctx=canvas.getContext('2d');
  function rect(x,y,w,h,c){ctx.fillStyle=c;ctx.fillRect(Math.round(x),Math.round(y),Math.round(w),Math.round(h));}
  function text(s,x,y,size,color){ctx.fillStyle=color;ctx.font=`bold ${size}px Chinese`;ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(s,x,y);}
  function cloud(x,y){const c='#deedfc';rect(x,y+12,72,3,c);rect(x+10,y+3,45,3,c);rect(x+18,y-6,25,3,c);rect(x+8,y+6,3,9,c);rect(x+53,y+6,3,9,c);}
  function masonry(x){rect(x,320,64,30,'#6699d0');rect(x+3,323,58,24,'#c6e0fa');rect(x+4,332,56,3,'#8ab6e2');rect(x+30,322,3,11,'#8ab6e2');rect(x+16,334,3,12,'#8ab6e2');}
  function bulb(t){
    if(t<1.7)return;
    const a=ease((t-1.7)/.3),x=365,y=48+(1-a)*36;
    ctx.save();ctx.globalAlpha=a;
    rect(x-12,y-10,24,22,'#c8902b');rect(x-17,y-5,34,12,'#c8902b');
    rect(x-10,y-8,20,18,'#ffe7a1');rect(x-15,y-3,30,8,'#ffe7a1');
    rect(x-7,y+10,14,9,'#244e7a');rect(x-5,y+12,10,3,'#b8d9f5');
    rect(x-2,y-3,4,14,'#dfa92f');
    const flash=t<2.2?1-clamp((t-1.7)/.5):.3;
    ctx.globalAlpha=a*flash;
    for(const [dx,dy] of [[-25,-12],[25,-12],[0,-26],[-29,7],[29,7]])rect(x+dx-2,y+dy-2,4,6,'#edbd4e');
    ctx.restore();
  }
  function character(s,t){
    const im=sprites[s.pose],w=HERO*im.width/im.height;
    let x=Math.round(s.x-w/2),y=Math.round(s.y-HERO);
    ctx.save();ctx.imageSmoothingEnabled=false;
    if(s.pose==='run'){
      const step=Math.sin(t*20),upper=.68;
      y-=Math.round(Math.abs(step)*3);
      ctx.drawImage(im,0,0,im.width,im.height*upper,x,y,w,HERO*upper);
      ctx.save();ctx.beginPath();ctx.rect(x,y+HERO*upper,w,HERO*(1-upper));ctx.clip();
      ctx.translate(s.x,y+HERO*upper);ctx.scale(step>0?1:-1,1);
      ctx.drawImage(im,0,im.height*upper,im.width,im.height*(1-upper),-w/2,0,w,HERO*(1-upper));ctx.restore();
    } else ctx.drawImage(im,x,y,Math.round(w),HERO);
    ctx.restore();
  }
  function scene(t){
    const s=state(t);rect(0,0,W,H,'#f7fbff');
    cloud(52,80);cloud(1080,122);
    masonry(35);masonry(1110);
    rect(0,GROUND,W,3,'#245d98');rect(0,GROUND+3,W,10,'#d6e9fc');
    for(let x=0;x<W;x+=44)rect(x,GROUND+3,2,10,'#adcff0');
    let x=144;
    words.forEach((word,i)=>{
      const a=ease((t-1.7-i*.18)/.32),bounce=i===2&&t>=1.7&&t<2?8*Math.sin(Math.PI*(t-1.7)/.3):0;
      const y=94-bounce,w=widths[i],gold=i===2&&!s.hit;
      rect(x,y+5,w,64,gold?'#d6b15f':'#326ba6');
      rect(x+2,y+2,w-4,58,gold?'#ffedb7':'#e8f3ff');
      rect(x+5,y+5,w-10,3,'#ffffff');
      rect(x+4,y+54,w-8,6,gold?'#f1ce7f':'#b9dafa');
      text(word,x+w/2,y+(word==='，'?29:31),word==='ai'?42:43,'#8aa3bd');
      ctx.save();ctx.globalAlpha=a;
      text(word,x+w/2,y+(word==='，'?29:31),word==='ai'?42:43,'#143b68');
      rect(x+4,y+60,w-8,4,'#64b3f0');ctx.restore();
      x+=w+5;
    });
    bulb(t);character(s,t);return s;
  }
  const first=createCanvas(W,H);scene(0);first.getContext('2d').drawImage(canvas,0,0);
  const frames=path.join(__dirname,'_frames');fs.mkdirSync(frames,{recursive:true});
  const states=[];
  for(let i=0;i<D*FPS;i++){
    const t=i/FPS,s=scene(t);
    if(s.reset){ctx.globalAlpha=s.reset;ctx.drawImage(first,0,0);ctx.globalAlpha=1;}
    fs.writeFileSync(path.join(frames,`${String(i).padStart(4,'0')}.png`),canvas.toBuffer('image/png'));
    states.push({t,...s});
  }
  scene(5.5);fs.writeFileSync(path.join(__dirname,'poster.png'),canvas.toBuffer('image/png'));
  const strip=createCanvas(W,800),st=strip.getContext('2d');
  [0,.7,1.7,2.2,3,4,5.5,7.15].forEach((t,i)=>{scene(t);const s=state(t);if(s.reset){ctx.globalAlpha=s.reset;ctx.drawImage(first,0,0);ctx.globalAlpha=1;}st.drawImage(canvas,(i%2)*600,Math.floor(i/2)*200,600,200);});
  fs.writeFileSync(path.join(__dirname,'keyframes.png'),strip.toBuffer('image/png'));
  const gif=spawnSync('ffmpeg',['-y','-v','error','-framerate',String(FPS),'-i',path.join(frames,'%04d.png'),'-filter_complex','[0:v]split[a][b];[a]palettegen=max_colors=192:stats_mode=full[p];[b][p]paletteuse=dither=bayer:bayer_scale=3','-loop','0',path.join(__dirname,'intro.gif')],{encoding:'utf8'});
  if(gif.status!==0)throw Error(gif.stderr);
  fs.writeFileSync(path.join(__dirname,'manifest.json'),JSON.stringify({width:W,height:H,fps:FPS,duration_seconds:D,frames:D*FPS,text:words.join(''),animation_method:'Canvas frames encoded by FFmpeg; not native Image 2.6 GIF',sprite_source:'../程序员拾梦闯关片头五案-v1/',mobile_wechat_verified:false,gif_bytes:fs.statSync(path.join(__dirname,'intro.gif')).size,states},null,2)+'\n');
  fs.writeFileSync(path.join(__dirname,'preview.html'),'<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>折腾ai，分享实用玩法 · GIF</title><style>body{font:16px system-ui;background:#edf2f7;color:#173a65;max-width:1000px;margin:40px auto;padding:20px}img{display:block;width:100%;margin:20px 0}a,button{color:#245d98;margin-right:16px}.phone{width:375px;max-width:100%;background:white}small{display:block;margin-top:24px}</style><h1>折腾ai，分享实用玩法</h1><img id="gif" src="intro.gif" alt="像素小人跑动起跳顶砖后落地停留"><button onclick="document.getElementById(\'gif\').src=\'intro.gif?t=\'+Date.now()">从头播放</button><a href="intro.gif" download>下载GIF</a><h2>375px手机宽度</h2><div class="phone"><img src="intro.gif" alt="手机宽度预览"></div><small>代码合成GIF，人物素材来自此前的imagegen生成资产。微信后台与真机播放尚未验收。</small></html>');
  console.log(`GIF ready: ${fs.statSync(path.join(__dirname,'intro.gif')).size} bytes`);
}
if(require.main===module)main().catch(e=>{console.error(e);process.exit(1);});
module.exports={state};
