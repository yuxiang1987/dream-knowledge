const fs=require('fs'),path=require('path'),{spawnSync}=require('child_process');
const {createCanvas,loadImage,GlobalFonts}=require('../程序员拾梦闯关片头五案-v1/node_modules/@napi-rs/canvas');
const OUT=__dirname,W=1200,H=360,FPS=25,D=10,GROUND=318;
const TAGLINE='折腾ai，专业踩坑';
const clamp=x=>Math.max(0,Math.min(1,x));
const ease=x=>{x=clamp(x);return x*x*(3-2*x);};
const mix=(a,b,p)=>a+(b-a)*clamp(p);
const hits=[3.02,4.82],impacts=[1.38,5.86];
function state(time){
  const t=time>=9.5?0:time;
  let x=92,pose='idle',sx=1,sy=1,y=GROUND;
  for(const [a,b,from,to] of [[.35,.9,92,160],[1.5,2.38,160,410],[3.48,4.2,410,620],[5.98,7.16,620,1040]]){
    if(t>=b)x=to;else if(t>=a){x=mix(from,to,ease((t-a)/(b-a)));pose='run';break;}
  }
  for(const hit of hits){
    if(t>=hit-.54&&t<hit-.38){const p=ease((t-(hit-.54))/.16);sx=1+.1*p;sy=1-.1*p;pose='idle';}
    if(t>=hit-.38&&t<hit){const p=(t-(hit-.38))/.38;y-=48*(2*p-p*p);pose='jump';}
    if(t>=hit&&t<hit+.4){const p=(t-hit)/.4;y-=48*(1-p*p);pose='jump';}
    if(t>=hit+.4&&t<hit+.56){const p=(t-hit-.4)/.16,q=Math.sin(Math.PI*p)*(1-p);sx=1+.15*q;sy=1-.15*q;pose='idle';}
  }
  const shots=[{start:.92,end:1.38,from:210,to:300},{start:5.34,end:5.86,from:670,to:850}];
  const bullets=shots.filter(s=>t>=s.start&&t<s.end).map(s=>({x:mix(s.from,s.to,(t-s.start)/(s.end-s.start)),y:GROUND-36}));
  const alpha=time<9?1:time<9.5?1-ease((time-9)/.5):ease((time-9.5)/.5);
  return {t,x,y,pose,sx,sy,hero_height:pose==='jump'?90:96,bullets,shooting:(t>=.84&&t<1.46)||(t>=5.26&&t<5.96),monster_alive:impacts.map(v=>t<v),unlocked:hits.map(v=>t>=v),flag_y:mix(126,264,ease((t-7.2)/.72)),alpha};
}
async function main(){
  GlobalFonts.registerFromPath('C:/Windows/Fonts/msyhbd.ttc','CN');
  GlobalFonts.registerFromPath('C:/Windows/Fonts/consolab.ttf','EN');
  const sprites={};for(const p of ['idle','run','jump']){const f=`sprite-${p}.png`;fs.copyFileSync(path.join(OUT,'../程序员拾梦闯关片头五案-v1',f),path.join(OUT,f));sprites[p]=await loadImage(path.join(OUT,f));}
  const canvas=createCanvas(W,H),c=canvas.getContext('2d');
  const r=(x,y,w,h,color)=>{c.fillStyle=color;c.fillRect(Math.round(x),Math.round(y),Math.round(w),Math.round(h));};
  function text(s,x,y,size,color,font='CN'){c.font=`bold ${size}px ${font}`;c.fillStyle=color;c.textBaseline='middle';c.textAlign='center';c.fillText(s,x,y);}
  function poly(points,color){c.fillStyle=color;c.beginPath();points.forEach(([x,y],i)=>i?c.lineTo(x,y):c.moveTo(x,y));c.closePath();c.fill();}
  function cloud(x,y,s){c.save();c.translate(x,y);c.scale(s,s);r(0,12,98,25,'#b6d3e5');r(12,0,70,38,'#b6d3e5');r(29,-8,26,46,'#b6d3e5');r(4,12,90,20,'#ffffff');r(16,4,62,28,'#ffffff');r(33,-4,18,36,'#ffffff');r(12,29,72,5,'#d5edf0');c.restore();}
  function hill(x,h,w){poly([[x,GROUND],[x,GROUND-h*.3],[x+w*.18,GROUND-h*.3],[x+w*.18,GROUND-h*.64],[x+w*.35,GROUND-h*.64],[x+w*.35,GROUND-h],[x+w*.65,GROUND-h],[x+w*.65,GROUND-h*.64],[x+w*.82,GROUND-h*.64],[x+w*.82,GROUND-h*.3],[x+w,GROUND-h*.3],[x+w,GROUND]],'#9ebda9');r(x+w*.38,GROUND-h+4,w*.24,4,'#c9e3cb');}
  function ground(){r(0,GROUND,W,5,'#526c5f');r(0,GROUND+5,W,5,'#b7d393');r(0,GROUND+10,W,H-GROUND-10,'#ba8767');for(let y=GROUND+12;y<H;y+=22){r(0,y,W,3,'#edc8a2');for(let x=(y===GROUND+12?0:26);x<W;x+=52)r(x,y+3,3,19,'#7f6556');}}
  function puff(x,y,p,color){if(p<0||p>1)return;c.save();c.globalAlpha*=1-p;for(let i=0;i<9;i++){const a=i*Math.PI/4.5,rr=8+34*p;r(x+Math.cos(a)*rr,y+Math.sin(a)*rr,6*(1-p)+2,6*(1-p)+2,color);}c.restore();}
  function monster(x,t,index){
    x+=5*Math.sin(t*4+index);const y=GROUND-44,body=index?'#b96b5c':'#866aab',edge=index?'#794b49':'#504b78';
    r(x-20,y+8,40,32,edge);r(x-12,y,24,40,edge);r(x-16,y+10,32,27,body);r(x-8,y+4,16,32,body);
    r(x-13,y+16,10,10,'#fff7e8');r(x+3,y+16,10,10,'#fff7e8');r(x-7,y+18,4,7,edge);r(x+3,y+18,4,7,edge);
    r(x-10,y+31,20,3,edge);const step=Math.sin(t*10)>0?3:0;r(x-23,y+38-step,16,6,edge);r(x+7,y+35+step,16,6,edge);
  }
  function block(cx,hit,t,word){
    const bump=t>=hit&&t<hit+.28?10*Math.sin(Math.PI*(t-hit)/.28):0,y=112-bump,open=t>=hit;
    r(cx-58,y+4,116,68,'#56616a');r(cx-56,y,112,64,'#e3c087');r(cx-52,y+4,104,56,open?'#345770':'#f6d99b');r(cx-48,y+8,96,4,open?'#55758c':'#fff1ce');
    for(const dx of [-47,44])for(const dy of [19,47])r(cx+dx,y+dy,3,3,open?'#97b4c2':'#b58e54');
    text(open?word:'?',cx,y+34,open?29:36,open?'#fff6de':'#7f6747','EN');
    puff(cx,y+66,(t-hit)/.28,'#e6b64e');
  }
  function hero(s){
    const im=sprites[s.pose],hh=s.hero_height,w=hh*im.width/im.height;
    c.save();c.translate(s.x,s.y);c.scale(s.sx,s.sy);c.imageSmoothingEnabled=false;
    const bob=s.pose==='run'?Math.abs(Math.sin(s.t*24))*2:0;
    if(s.pose==='run'){
      const cut=.68;c.drawImage(im,0,0,im.width,im.height*cut,-w/2,-hh-bob,w,hh*cut);
      c.save();c.translate(0,-hh*(1-cut)-bob);c.scale(Math.sin(s.t*24)>0?1:-1,1);c.drawImage(im,0,im.height*cut,im.width,im.height*(1-cut),-w/2,0,w,hh*(1-cut));c.restore();
    }else c.drawImage(im,-w/2,-hh,w,hh);
    c.restore();
    if(s.shooting){const y=GROUND-44;r(s.x+13,y+3,26,17,'#35536a');r(s.x+31,y,23,14,'#496c84');r(s.x+48,y+2,9,10,'#223c53');r(s.x+17,y+16,8,8,'#35536a');}
  }
  function flag(s){
    r(1086,110,8,GROUND-110,'#829b9c');r(1088,110,3,GROUND-110,'#c2d8cf');r(1080,106,20,9,'#567b70');
    const y=s.flag_y;poly([[1085,y],[1017,y],[1029,y+18],[1017,y+36],[1085,y+36]],'#438a73');r(1063,y+12,8,12,'#eff6d6');
    r(1069,GROUND-8,43,8,'#667c70');
    if(s.t>=7.92){const p=ease((s.t-7.92)/.24);c.save();c.globalAlpha*=p;poly([[1123,252],[1129,258],[1142,243],[1147,248],[1129,268],[1118,257]],'#438a73');c.restore();}
  }
  function scene(time){
    const s=state(time);c.globalAlpha=1;r(0,0,W,H,'#edf5fa');
    cloud(42,75,.72);cloud(1004,39,.68);cloud(756,205,.43);
    hill(-36,44,180);hill(358,34,192);hill(725,46,180);hill(1093,57,150);
    text(TAGLINE,600,59,62,'#273f52');
    // 两个词分别由顶砖解锁；主文案不参与重置，随时滑入也能阅读。
    c.save();c.globalAlpha=s.alpha;
    block(440,hits[0],s.t,'dream');block(650,hits[1],s.t,'coder');
    flag(s);
    for(const [i,x] of [300,850].entries()){
      if(s.monster_alive[i])monster(x,s.t,i);else puff(x,GROUND-24,(s.t-impacts[i])/.4,i?'#ca8269':'#9c82b4');
    }
    r(s.x-19,GROUND-2,38,4,'#c1d4d8');hero(s);
    for(const b of s.bullets){r(b.x-17,b.y-3,14,6,'#ebc86b');r(b.x-8,b.y-6,12,12,'#344f66');r(b.x-5,b.y-8,7,16,'#344f66');r(b.x-5,b.y-5,4,4,'#9fc5d7');}
    for(const start of [.92,5.34]){const p=(s.t-start)/.15;if(p>=0&&p<1){const x=start<1?216:676;c.save();c.globalAlpha*=1-p;r(x,GROUND-42,8,12,'#f4c759');c.restore();}}
    c.restore();ground();return s;
  }
  const frames=path.join(OUT,'_frames');fs.mkdirSync(frames,{recursive:true});const states=[];
  for(let i=0;i<D*FPS;i++){const t=i===D*FPS-1?0:i/FPS;states.push(state(t));scene(t);fs.writeFileSync(path.join(frames,`${String(i).padStart(4,'0')}.png`),canvas.toBuffer('image/png'));}
  scene(8.5);fs.writeFileSync(path.join(OUT,'poster.png'),canvas.toBuffer('image/png'));
  const sheet=createCanvas(1200,5*180),sc=sheet.getContext('2d');[0,1.12,1.48,3.02,3.28,4.82,5.62,6.6,7.6,8.5].forEach((t,i)=>{scene(t);sc.drawImage(canvas,(i%2)*600,Math.floor(i/2)*180,600,180);});fs.writeFileSync(path.join(OUT,'keyframes.png'),sheet.toBuffer('image/png'));
  const mobile=createCanvas(375,113);scene(8.5);mobile.getContext('2d').drawImage(canvas,0,0,375,112.5);fs.writeFileSync(path.join(OUT,'mobile.png'),mobile.toBuffer('image/png'));
  const run=spawnSync('ffmpeg',['-y','-v','error','-framerate',String(FPS),'-i',path.join(frames,'%04d.png'),'-filter_complex','[0:v]split[a][b];[a]palettegen=max_colors=256:stats_mode=full[p];[b][p]paletteuse=dither=bayer:bayer_scale=3','-loop','0',path.join(OUT,'intro.gif')],{encoding:'utf8'});if(run.status!==0)throw Error(run.stderr);
  fs.writeFileSync(path.join(OUT,'manifest.json'),JSON.stringify({account:'程序员梦哥',visible_title:TAGLINE,brick_words:['dream','coder'],width:W,height:H,fps:FPS,frame_count:D*FPS,duration_seconds:D,ground:GROUND,brick_bottom:180,hits,impacts,flag_lowering:[7.2,7.92],reset:[9,10],method:'Existing character sprites, code-drawn monsters and scenery, Canvas/FFmpeg GIF',wechat_verified:false,states},null,2)+'\n');
  fs.writeFileSync(path.join(OUT,'preview.html'),`<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>程序员梦哥 · 像素闯关 v2</title><style>*{box-sizing:border-box}body{margin:0;background:#e9eff2;color:#2b4758;font:15px/1.8 "Microsoft YaHei",sans-serif}main{max-width:1100px;margin:28px auto;padding:28px;background:white;border-radius:16px}h1{font-size:23px;margin:0}h2{font-size:17px;margin-top:26px}p{color:#758995}img{display:block;width:100%}.phone{width:375px;max-width:100%;border:1px solid #e0e8ec}.body{padding:18px 24px}button,a{display:inline-block;margin:12px 8px 0 0;border:1px solid #d2dfe4;border-radius:6px;background:white;padding:7px 12px;color:#3d7089;font:inherit;text-decoration:none}@media(max-width:650px){main{margin:0;padding:18px}}</style><main><h1>折腾ai，专业踩坑</h1><p>炮弹打怪 → 顶出 dream → 顶出 coder → 降旗过关，10秒循环。</p><img data-loop src="intro.gif" alt="像素人物发炮打怪、顶出dream和coder，最后降旗"><button onclick="document.querySelectorAll('img[data-loop]').forEach(im=>im.src='intro.gif?t='+Date.now())">从头播放</button><a href="intro.gif" download>下载 GIF</a><h2>375px 文章预览</h2><div class="phone"><img data-loop src="intro.gif" alt="375px片头预览"><div class="body"><b>你好，我是梦哥。</b><p>这里接今天的文章。</p></div></div><h2>十个动作时刻</h2><img src="keyframes.png" alt="打怪、两次顶砖与降旗关键帧"><p>本地候选；复用既有角色、代码制作GIF，公众号后台及真机效果待验收。</p></main></html>`);
  console.log(JSON.stringify({frames:D*FPS,gif_bytes:fs.statSync(path.join(OUT,'intro.gif')).size,duration:D}));
}
if(require.main===module)main().catch(e=>{console.error(e);process.exitCode=1});
module.exports={state};
