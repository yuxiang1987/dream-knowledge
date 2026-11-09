const fs = require('fs');
const path = require('path');
const {spawnSync} = require('child_process');
const {createCanvas, loadImage, GlobalFonts} = require('@napi-rs/canvas');
const OUT = __dirname, W = 1200, H = 360, GROUND = 308, FPS = 20, D = 8;
GlobalFonts.registerFromPath('C:/Windows/Fonts/msyhbd.ttc', 'Chinese');
GlobalFonts.registerFromPath('C:/Windows/Fonts/consolab.ttf', 'Game');
const clamp = v => Math.max(0, Math.min(1, v));
const ease = v => { v = clamp(v); return v*v*(3-2*v); };
const mix = (a,b,p) => a+(b-a)*clamp(p);
const jump = (t,a,b,h) => t>a && t<b ? Math.sin(Math.PI*(t-a)/(b-a))*h : 0;
const variants = [
  {id:'01-question',name:'顶问号砖块',caption:'今天，又有什么新玩法？',note:'跳跃顶砖 → AI 道具弹出 → 品牌展开',color:'#1768df'},
  {id:'02-pipe',name:'水管传送',caption:'进入今天的 AI 世界',note:'探头出管 → 横向跑动 → 传送到 AI 工作台',color:'#16845f'},
  {id:'03-coins',name:'收集金币',caption:'把灵感，一个个捡起来',note:'连续跳跃 → 五枚金币翻成账号名 → 星星归位',color:'#a86212'},
  {id:'04-flag',name:'跳台升旗',caption:'这一关，我来试试',note:'两级跳台 → 跨越缺口 → 升起品牌旗帜',color:'#1768df'},
  {id:'05-star',name:'吃星星变身',caption:'灵感启动，让想象发光',note:'星星弹出 → 追逐获得能力 → 彩色尾迹写出品牌',color:'#7053c1'},
];
function state(k,t) {
  let x=130,y=GROUND,pose='idle',reveal=0;
  if(k===0){x=t<1.15?mix(-65,340,ease(t/1.15)):340;y-=jump(t,1.35,2.25,62);pose=t<1.15?'run':t<2.25&&t>1.35?'jump':t>3.2?'wave':'idle';reveal=ease((t-3)/.7);}
  if(k===1){
    x=t<1?165:t<2.5?mix(165,525,ease((t-1)/1.5)):t<3.25?525:mix(760,670,ease((t-3.25)/.8));
    y=t<1?mix(GROUND+145,GROUND,ease(t)):t<2.5?GROUND-jump(t,1,1.6,28):t<3.25?mix(GROUND,GROUND+145,ease((t-2.5)/.65)):mix(GROUND+145,GROUND,ease((t-3.25)/.65));
    pose=t<1?'idle':t<2.5?'run':t>4?'wave':'idle';reveal=ease((t-3.6)/.7);
  }
  if(k===2){x=t<.5?130:t<4.7?mix(130,975,(t-.5)/4.2):975;const u=(t-.5)/.84,cycle=u-Math.floor(u);y-=t>.5&&t<4.7?Math.sin(Math.PI*cycle)*62:0;pose=t>.5&&t<4.7?'jump':t>=4.7?'wave':'idle';reveal=ease((t-4.65)/.4);}
  if(k===3){
    if(t<1){x=mix(95,325,ease(t));y=mix(GROUND,260,ease(t))-jump(t,0,1,85);}
    else if(t<2){x=mix(325,435,ease(t-1));y=mix(260,216,ease(t-1))-jump(t,1,2,76);}
    else if(t<3.25){x=mix(435,650,ease((t-2)/1.25));y=mix(216,GROUND,ease((t-2)/1.25))-jump(t,2,3.25,98);}
    else{x=650;y=GROUND;}
    pose=t<3.25?'jump':'wave';reveal=ease((t-3.35)/1.2);
  }
  if(k===4){x=t<1.2?160:t<2.7?mix(160,410,ease((t-1.2)/1.5)):t<4.5?mix(410,1020,ease((t-2.7)/1.8)):1020;y-=jump(t,2.7,4.5,62);pose=t<1.2?'idle':t<2.7?'run':t<4.5?'jump':'wave';reveal=ease((t-3)/1.5);}
  return {x,y,pose,reveal};
}
async function main(){
  const sheet=await loadImage(path.join(OUT,'spritesheet.png'));
  const source=createCanvas(sheet.width,sheet.height), sc=source.getContext('2d');sc.drawImage(sheet,0,0);
  const data=sc.getImageData(0,0,sheet.width,sheet.height).data, sprites={}, boxes={};
  // Crop each generated pose independently so differing poses retain matched head scale.
  for(const [i,key] of ['idle','run','jump','wave'].entries()){
    const x0=Math.floor((i%2)*sheet.width/2),y0=Math.floor(Math.floor(i/2)*sheet.height/2);
    let l=x0+sheet.width/2,r=x0,t=y0+sheet.height/2,b=y0;
    for(let y=y0;y<y0+Math.floor(sheet.height/2);y++)for(let x=x0;x<x0+Math.floor(sheet.width/2);x++)if(data[(y*sheet.width+x)*4+3]>100){l=Math.min(l,x);r=Math.max(r,x);t=Math.min(t,y);b=Math.max(b,y);}
    const c=createCanvas(r-l+1,b-t+1);c.getContext('2d').drawImage(sheet,l,t,r-l+1,b-t+1,0,0,r-l+1,b-t+1);
    fs.writeFileSync(path.join(OUT,`sprite-${key}.png`),c.toBuffer('image/png'));sprites[key]=c;boxes[key]={x:l,y:t,w:c.width,h:c.height};
  }
  const canvas=createCanvas(W,H),ctx=canvas.getContext('2d');
  function rect(x,y,w,h,c){ctx.fillStyle=c;ctx.fillRect(Math.round(x),Math.round(y),Math.round(w),Math.round(h));}
  function text(str,x,y,size=22,color='#173250',align='left',font='Chinese'){ctx.fillStyle=color;ctx.font=`bold ${size}px ${font}`;ctx.textAlign=align;ctx.textBaseline='middle';ctx.fillText(str,x,y);}
  function cloud(x,y,s=1){ctx.save();ctx.translate(x,y);ctx.scale(s,s);rect(0,12,78,15,'#fff');rect(12,0,25,28,'#fff');rect(37,6,27,22,'#fff');ctx.restore();}
  function star(x,y,size=20,color='#ffd657'){
    ctx.fillStyle=color;ctx.beginPath();for(let i=0;i<10;i++){const a=-Math.PI/2+i*Math.PI/5,r=i%2?size*.46:size;const xx=x+Math.cos(a)*r,yy=y+Math.sin(a)*r;i?ctx.lineTo(xx,yy):ctx.moveTo(xx,yy);}ctx.closePath();ctx.fill();
    if(size>13){rect(x-5,y-3,3,6,'#6c4b25');rect(x+3,y-3,3,6,'#6c4b25');}
  }
  function coin(x,y,t,size=17){const w=Math.max(4,Math.abs(Math.cos(t*5))*size*1.4);rect(x-w/2-3,y-size, w+6,size*2,'#bd761a');rect(x-w/2,y-size+3,w,size*2-6,'#ffcf47');rect(x-w/2+3,y-size+6,Math.max(2,w*.22),size*2-12,'#fff0a2');}
  function spark(x,y,t,color='#ffc841') {for(let i=0;i<8;i++){const a=i*Math.PI/4,r=12+t*42;rect(x+Math.cos(a)*r,y+Math.sin(a)*r,4,4,color);}}
  function brick(x,y,s=48,question=false,used=false){
    rect(x,y,s,s,'#654224');rect(x+3,y+3,s-6,s-6,used?'#a5a3a0':question?'#ffc653':'#d99154');rect(x+5,y+5,s-10,4,used?'#c6c3bf':'#ffe29b');
    if(question){if(!used)text('?',x+s/2,y+s/2+2,s*.72,'#704c26','center','Game');for(const dx of [7,s-10])for(const dy of [8,s-11])rect(x+dx,y+dy,3,3,'#8b5b28');}
    else{rect(x+3,y+s/2,s-6,3,'#9e623b');rect(x+s/2,y+6,3,s/2-6,'#9e623b');rect(x+s/3,y+s/2+4,3,s/2-8,'#9e623b');}
  }
  function pipe(x,top,w=88){rect(x-w/2+7,top+21,w-14,GROUND-top-21,'#185d45');rect(x-w/2+11,top+21,w-23,GROUND-top-21,'#42a877');rect(x-w/2+17,top+21,12,GROUND-top-21,'#8cdfa7');rect(x-w/2,top,w,28,'#16543f');rect(x-w/2+4,top+4,w-8,18,'#49b982');rect(x-w/2+10,top+5,13,16,'#a3ebba');}
  function computer(x,y,scale=1){ctx.save();ctx.translate(x,y);ctx.scale(scale,scale);rect(-34,-28,68,47,'#173c6c');rect(-29,-23,58,35,'#e1f6ff');text('AI',0,-4,25,'#1768df','center','Game');rect(-6,19,12,8,'#173c6c');rect(-24,27,48,5,'#173c6c');ctx.restore();}
  function character(x,y,pose,t,scale=1){
    const im=sprites[pose],h=140*scale,w=h*im.width/im.height;
    ctx.save();ctx.imageSmoothingEnabled=false;
    if(pose==='run'){y-=Math.abs(Math.sin(t*16))*4;ctx.translate(x,y);ctx.scale(Math.sin(t*16)>.1?1:.94,1);x=0;y=0;}
    ctx.drawImage(im,Math.round(x-w/2),Math.round(y-h),Math.round(w),Math.round(h));ctx.restore();
  }
  function base(k,t){
    const colors=['#eef8ff','#edf9f5','#fff8e8','#eff7ff','#f5f0ff'];rect(0,0,W,H,colors[k]);
    cloud(50,75,.8);cloud(470,54,.6);cloud(1040,78,.8);
    // Restrained square hills keep the strip light enough for the article's first screen.
    for(const [x,w,h] of [[0,160,30],[470,150,22],[1040,180,38]]){rect(x,GROUND-h,w,h,k===1?'#daeee2':'#dcecf2');rect(x+22,GROUND-h-12,w-44,12,k===1?'#daeee2':'#dcecf2');}
    rect(0,GROUND,W,7,'#72b488');rect(0,GROUND+7,W,45,'#ecd9b8');
    for(let x=0;x<W;x+=48){rect(x,GROUND+13,46,2,'#ddc19b');rect(x+22,GROUND+15,2,15,'#ddc19b');rect(x,GROUND+31,46,2,'#ddc19b');}
    text(`SHIMENG / WORLD 0${k+1}`,36,26,17,'#607a92','left','Game');
    text(['DISCOVER','EXPLORE','COLLECT','CHALLENGE','POWER UP'][k],1164,26,17,variants[k].color,'right','Game');
  }
  function brand(k,a,x=760,y=163){
    if(a<=0)return;ctx.save();ctx.globalAlpha=a;ctx.translate(0,(1-a)*10);
    text('程序员拾梦',x,y,66,'#173a65','center');text('折腾 AI，分享实用玩法',x,y+58,26,'#567a99','center');
    rect(x-21,y-55,42,5,variants[k].color);ctx.restore();
  }
  function scene(k,t){
    base(k,t);const s=state(k,t);
    if(k===0){
      const hit=t>=1.8,bounce=jump(t,1.8,2.15,12);brick(310,59-bounce,60,true,hit);brick(250,59,54);brick(376,59,54);
      if(t>1.8&&t<3.7){const u=ease((t-1.8)/1.5),xx=mix(340,650,u),yy=mix(35,128,u)-Math.sin(u*Math.PI)*14;ctx.globalAlpha=1-ease((t-3.2)/.5);computer(xx,yy,.75);ctx.globalAlpha=1;}
      if(t>1.8&&t<2.25){ctx.globalAlpha=1-(t-1.8)/.45;spark(340,60,(t-1.8)*2);ctx.globalAlpha=1;}
      character(s.x,s.y,s.pose,t);brand(k,s.reveal,800,166);
    }
    if(k===1){
      // Clip the character at the pipe mouths during entering and exiting.
      ctx.save();ctx.beginPath();ctx.rect(0,0,W,GROUND);ctx.clip();
      if(t<1){ctx.save();ctx.beginPath();ctx.rect(95,0,140,225);ctx.clip();character(s.x,s.y,s.pose,t);ctx.restore();}
      else if(t<2.5)character(s.x,s.y,s.pose,t);
      else if(t<3.25){ctx.save();ctx.beginPath();ctx.rect(450,0,150,225);ctx.clip();character(s.x,s.y,s.pose,t);ctx.restore();}
      else{ctx.save();ctx.beginPath();ctx.rect(0,0,W,t<3.95?225:GROUND);ctx.clip();character(s.x,s.y,s.pose,t);ctx.restore();}ctx.restore();
      pipe(165,225);pipe(525,225);pipe(760,225);
      if(t>2.6&&t<3.7){ctx.globalAlpha=Math.sin(clamp((t-2.6)/1.1)*Math.PI);for(let i=0;i<12;i++)rect(550+i*16,245+Math.sin(i)*7,6,6,'#48ad90');ctx.globalAlpha=1;}
      ctx.save();ctx.globalAlpha=s.reveal;rect(330,87,285,114,'#fff');rect(330,87,285,7,'#94d9b8');computer(390,137,.7);text('AI 工作台',460,128,27,'#237c5e');text('代码  /  视频  /  Agent',354,178,18,'#6b8e82');ctx.restore();
      brand(k,s.reveal,945,129);
    }
    if(k===2){
      const letters=[...'程序员拾梦'];
      for(let i=0;i<5;i++){const x=215+i*169,at=.5+(i+.5)*.84,a=ease((t-at)/.25);if(a<1){ctx.globalAlpha=1-a;coin(x,183,t+i,21);ctx.globalAlpha=1;}
        if(a>0){ctx.globalAlpha=a;text(letters[i],x,139-(1-a)*15,70,'#215e9f','center');ctx.globalAlpha=1;}
        if(t>at&&t<at+.4){ctx.globalAlpha=1-(t-at)/.4;spark(x,178,(t-at)*1.5);ctx.globalAlpha=1;}}
      character(s.x,s.y,s.pose,t);
      if(t>4.8){const u=ease((t-4.8)/.7);star(mix(1040,975,u),mix(75,231,u),mix(22,7,u));}
      ctx.save();ctx.globalAlpha=s.reveal;text('折腾 AI，分享实用玩法',550,227,27,'#748297','center');ctx.restore();
      text(`COINS  ${Math.min(5,Math.max(0,Math.floor((t-.92)/.84)+1))} / 5`,36,59,16,'#9f7b38','left','Game');
    }
    if(k===3){
      rect(490,GROUND,95,52,'#eff7ff');rect(490,GROUND+7,95,45,'#c5dcea');
      for(let i=0;i<2;i++)brick(280+i*45,260,45);for(let j=0;j<2;j++)for(let i=0;i<2;i++)brick(390+i*45,216+j*46,45);
      rect(703,66,6,GROUND-66,'#4e7195');star(706,60,10);
      const fy=mix(246,96,s.reveal),fw=mix(60,370,s.reveal);rect(710,fy,fw,78,'#226ed3');rect(716,fy+6,fw-12,66,'#3c86e8');
      if(s.reveal>.7){ctx.globalAlpha=(s.reveal-.7)/.3;text('程序员拾梦',710+fw/2,fy+39,45,'#fff','center');ctx.globalAlpha=1;}
      character(s.x,s.y,s.pose,t);
      ctx.save();ctx.globalAlpha=s.reveal;text('这一关，我来试试',905,218,29,'#345d86','center');text('AI CODING  /  AGENT  /  VIDEO',905,256,17,'#7990aa','center','Game');ctx.restore();
      if(t>3.6&&t<4.8){ctx.globalAlpha=1-ease((t-4)/.8);spark(1100,102,(t-3.6)*.7,'#e8b954');ctx.globalAlpha=1;}
    }
    if(k===4){
      brick(92,68,52,true,t>=.5);
      if(t>.5&&t<2.7){const u=clamp((t-.5)/2.2),xx=mix(118,410,u),yy=t<1.2?mix(58,275,(t-.5)/.7)-jump(t,.5,1.2,45):275-jump(t,1.2,2.7,40);star(xx,yy,22);}
      if(t>=2.7&&t<4.7){
        const colors=['#5c95e9','#7c6edf','#d979bd','#efbe50'];
        for(let j=0;j<4;j++){ctx.globalAlpha=.42;const lag=.18+j*.09,trail=state(k,Math.max(2.7,t-lag));rect(trail.x-44,trail.y-73+j*9,44,5,colors[j]);ctx.globalAlpha=1;}
        for(let j=0;j<9;j++){const age=j*.09,ss=state(k,Math.max(2.7,t-age));ctx.globalAlpha=.5*(1-j/10);star(ss.x-45,ss.y-90+Math.sin(j*3)*30,5,colors[j%4]);ctx.globalAlpha=1;}
      }
      brand(k,s.reveal,620,153);
      if(t>=2.7){ctx.save();ctx.globalAlpha=t<3?1-ease((t-2.7)/.3):0;spark(s.x,s.y-70,(t-2.7)*2,'#c2a33e');ctx.restore();}
      character(s.x,s.y,s.pose,t);if(t>4.5)star(1020,145+Math.sin(t*3)*3,16,'#f0c154');
    }
    return s;
  }
  const manifest={width:W,height:H,fps:FPS,duration_seconds:D,frames:FPS*D,avatar:'avatar-reference.png',generator:'built-in image_gen',sprite_boxes:boxes,mobile_wechat_verified:false,variants:[]};
  const contact=createCanvas(1200,5*220),cc=contact.getContext('2d');cc.fillStyle='#fff';cc.fillRect(0,0,1200,1100);
  for(let k=0;k<5;k++){
    const v=variants[k],dir=path.join(OUT,v.id);fs.mkdirSync(dir,{recursive:true});const frames=path.join(OUT,'_frames',v.id);fs.mkdirSync(frames,{recursive:true});
    scene(k,0);const start=createCanvas(W,H);start.getContext('2d').drawImage(canvas,0,0);
    const states=[];
    for(let i=0;i<FPS*D;i++){
      const t=i/FPS,s=scene(k,t);if(t>=7.35){ctx.globalAlpha=ease((t-7.35)/.6);ctx.drawImage(start,0,0);ctx.globalAlpha=1;}
      fs.writeFileSync(path.join(frames,`${String(i).padStart(4,'0')}.png`),canvas.toBuffer('image/png'));states.push({t,...s});
    }
    scene(k,5.8);fs.writeFileSync(path.join(dir,'poster.png'),canvas.toBuffer('image/png'));
    const strip=createCanvas(1200,720),st=strip.getContext('2d');
    for(let j=0;j<8;j++){scene(k,[0,.8,1.7,2.3,3.1,4,5.7,7.95][j]);st.drawImage(canvas,(j%2)*600,Math.floor(j/2)*180,600,180);}
    fs.writeFileSync(path.join(dir,'keyframes.png'),strip.toBuffer('image/png'));
    const args=['-y','-v','error','-framerate',String(FPS),'-i',path.join(frames,'%04d.png')];
    const gif=spawnSync('ffmpeg',[...args,'-filter_complex','[0:v]split[a][b];[a]palettegen=max_colors=192:stats_mode=diff[p];[b][p]paletteuse=dither=bayer:bayer_scale=3','-loop','0',path.join(dir,'intro.gif')],{encoding:'utf8'});if(gif.status!==0)throw Error(gif.stderr);
    const mp4=spawnSync('ffmpeg',[...args,'-c:v','libx264','-pix_fmt','yuv420p','-crf','20','-movflags','+faststart',path.join(dir,'intro.mp4')],{encoding:'utf8'});if(mp4.status!==0)throw Error(mp4.stderr);
    manifest.variants.push({...v,states,gif_bytes:fs.statSync(path.join(dir,'intro.gif')).size});
    cc.fillStyle='#173a65';cc.font='bold 20px Chinese';cc.fillText(`${k+1}. ${v.name}`,28,k*220+28);scene(k,5.8);cc.drawImage(canvas,0,k*220+40,600,180);scene(k,k===0?1.8:k===1?1.7:k===2?2.7:k===3?2.4:3.5);cc.drawImage(canvas,600,k*220+40,600,180);
    console.log(`${v.id}: GIF ${manifest.variants[k].gif_bytes} bytes, MP4 ready`);
  }
  fs.writeFileSync(path.join(OUT,'comparison.png'),contact.toBuffer('image/png'));
  fs.writeFileSync(path.join(OUT,'manifest.json'),JSON.stringify(manifest,null,2)+'\n');
  const cards=variants.map((v,k)=>`<article id="v${k+1}"><div class="label"><span>0${k+1}</span><div><h2>${v.name}</h2><p>${v.note}</p></div></div><img class="hero" src="${v.id}/intro.gif" alt="${v.name}八秒循环动画"><div class="controls"><button onclick="replay(this)">重播这一版</button><a href="${v.id}/intro.gif" download>下载 GIF</a><a href="${v.id}/intro.mp4" download>下载 MP4</a><a href="${v.id}/keyframes.png" target="_blank">查看关键帧</a></div><details><summary>375px 手机宽度预览</summary><div class="phone"><img src="${v.id}/intro.gif" alt="375px宽度预览"></div></details></article>`).join('');
  fs.writeFileSync(path.join(OUT,'preview.html'),`<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>程序员拾梦 · 五种闯关片头</title><style>*{box-sizing:border-box}body{margin:0;background:#edf2f6;color:#193852;font-family:"Microsoft YaHei",sans-serif}main{max-width:1100px;margin:auto;padding:38px 22px 70px}header{margin-bottom:30px}h1{font-size:29px;margin:10px 0}header p{color:#687e91;line-height:1.8}nav{display:flex;gap:10px;flex-wrap:wrap}nav a,.controls a,button{padding:9px 13px;border:1px solid #d8e3eb;border-radius:8px;background:#fff;color:#2664a0;text-decoration:none;font:inherit;cursor:pointer}article{background:#fff;border:1px solid #dce5ec;border-radius:16px;margin:24px 0;padding:24px;scroll-margin:20px}.label{display:flex;align-items:center;gap:15px}.label>span{font:32px monospace;color:#9bb1c5}h2{font-size:22px;margin:0 0 6px}.label p{font-size:13px;color:#7a8a99;margin:0}.hero{display:block;width:100%;margin:22px 0 16px;border-radius:8px}.controls{display:flex;gap:9px;flex-wrap:wrap;font-size:13px}details{margin-top:20px;color:#698297;font-size:13px}.phone{width:375px;max-width:100%;margin-top:15px;border:1px solid #dde7ee;background:#fff}.phone img{width:100%;display:block}footer{font-size:12px;color:#7d8e9d;line-height:1.9}@media(max-width:600px){main{padding:20px 12px}article{padding:14px}.label p{line-height:1.6}h1{font-size:23px}}</style></head><body><main><header><small>程序员拾梦 / BRAND INTRO EXPLORATIONS</small><h1>同一个拾梦，五种开场</h1><p>新头像 · 蓝色卫衣像素小人 · 每版 8 秒循环。点击重播可从头看完整动作。</p><nav>${variants.map((v,k)=>`<a href="#v${k+1}">0${k+1} ${v.name}</a>`).join('')}</nav></header>${cards}<footer>本地动画候选，等待选型。公众号后台转存与真机播放尚未验收。旧片头本轮保留。</footer></main><script>function replay(b){const img=b.closest('article').querySelector('.hero');img.src=img.getAttribute('src').split('?')[0]+'?t='+Date.now()}</script></body></html>`);
}
if(require.main===module)main().catch(e=>{console.error(e);process.exit(1)});
module.exports={state,variants,W,H,FPS,D};
