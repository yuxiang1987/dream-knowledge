const fs=require('fs'),path=require('path'),{spawnSync}=require('child_process');
const {createCanvas,loadImage,GlobalFonts}=require('../程序员拾梦闯关片头五案-v1/node_modules/@napi-rs/canvas');
const OUT=__dirname,W=1200,H=360,FPS=50,D=8.8,GROUND=318;
const TAGLINE='分享AI、少踩坑',TOPIC=['codex','claude','workbuddy','kimi','user07','minimax','deepseek'];
const clamp=x=>Math.max(0,Math.min(1,x));
const ease=x=>{x=clamp(x);return x*x*(3-2*x);};
const mix=(a,b,p)=>a+(b-a)*clamp(p);
const hits=[.8],impacts=[3.16,4.04];
const {state,engine,labels,targets,order}=require('./motion.cjs');
async function main(){
  const fontFile=path.join(OUT,'../程序员梦哥像素闯关-v3/fonts/fusion-pixel-12px-proportional-zh_hans.ttf.woff2');
  if(!GlobalFonts.registerFromPath(fontFile,'Pixel'))throw Error('Pixel font registration failed');
  const sheet=await loadImage(path.join(OUT,'../程序员梦哥像素闯关-v3/action-sheet.png'));
  const src=createCanvas(sheet.width,sheet.height),scrop=src.getContext('2d');scrop.drawImage(sheet,0,0);
  const pixels=scrop.getImageData(0,0,sheet.width,sheet.height).data,boxes=[];
  for(let i=0;i<16;i++){
    const x0=Math.floor((i%4)*sheet.width/4),x1=Math.floor((i%4+1)*sheet.width/4),y0=Math.floor(Math.floor(i/4)*sheet.height/4),y1=Math.floor((Math.floor(i/4)+1)*sheet.height/4);
    let l=x1,r=x0,top=y1,b=y0;for(let y=y0;y<y1;y++)for(let x=x0;x<x1;x++)if(pixels[(y*sheet.width+x)*4+3]>110){l=Math.min(l,x);r=Math.max(r,x);top=Math.min(top,y);b=Math.max(b,y);}
    boxes.push({x:l,y:top,w:r-l+1,h:b-top+1,anchor:((x0+x1)/2)-l});
  }
  const scale=128/boxes[2].h;
  const canvas=createCanvas(W,H),c=canvas.getContext('2d');
  const r=(x,y,w,h,color)=>{c.fillStyle=color;c.fillRect(Math.round(x),Math.round(y),Math.round(w),Math.round(h));};
  const glyphs=new Map();
  function text(s,x,y,size,color){
    const key=s+color;let glyph=glyphs.get(key);
    if(!glyph){
      const tmp=createCanvas(600,24),g=tmp.getContext('2d');g.font='12px Pixel';g.textBaseline='top';g.fillStyle=color;g.fillText(s,2,0);
      const im=g.getImageData(0,0,tmp.width,tmp.height);let l=tmp.width,top=24,right=0,bottom=0;
      for(let yy=0;yy<24;yy++)for(let xx=0;xx<tmp.width;xx++){const i=(yy*tmp.width+xx)*4;im.data[i+3]=im.data[i+3]>127?255:0;if(im.data[i+3]){l=Math.min(l,xx);right=Math.max(right,xx);top=Math.min(top,yy);bottom=Math.max(bottom,yy);}}
      g.putImageData(im,0,0);glyph=createCanvas(right-l+1,bottom-top+1);glyph.getContext('2d').drawImage(tmp,l,top,glyph.width,glyph.height,0,0,glyph.width,glyph.height);glyphs.set(key,glyph);
    }
    const n=Math.max(1,Math.round(size/12));c.imageSmoothingEnabled=false;c.drawImage(glyph,Math.round(x-glyph.width*n/2),Math.round(y-glyph.height*n/2),glyph.width*n,glyph.height*n);
  }
  // 在24×24格上绘制自制像素化标记，再以3倍最近邻放大。
  const icons=new Map();
  for(const name of TOPIC){
    const ext='png';
    const source=await loadImage(path.join(OUT,'../程序员梦哥像素闯关-v5工具箱/icons',name+'-source.'+ext));
    const im=createCanvas(24,24),g=im.getContext('2d');
    g.fillStyle='#fff9ec';g.fillRect(2,0,20,24);g.fillRect(0,2,24,20);
    g.drawImage(source,1,1,22,22);
    const pix=g.getImageData(0,0,24,24);
    for(let i=0;i<pix.data.length;i+=4){for(let j=0;j<3;j++)pix.data[i+j]=Math.round(pix.data[i+j]/32)*32;pix.data[i+3]=pix.data[i+3]>127?255:0;}
    g.putImageData(pix,0,0);icons.set(name,im);
  }
  for(const [name,im] of icons){
    const imout=createCanvas(24,24);imout.getContext('2d').drawImage(im,0,0);fs.writeFileSync(path.join(OUT,name+'-pixel.png'),imout.toBuffer('image/png'));
  }
  function icon(v){
    c.save();c.translate(v.x,v.y);c.rotate(v.angle*Math.PI/180);c.scale(v.scale,v.scale);
    c.imageSmoothingEnabled=false;c.drawImage(icons.get(v.text),-36,-36,72,72);c.restore();
  }
  function poly(points,color){c.fillStyle=color;c.beginPath();points.forEach(([x,y],i)=>i?c.lineTo(x,y):c.moveTo(x,y));c.closePath();c.fill();}
  function cloud(x,y,s){c.save();c.translate(x,y);c.scale(s,s);r(0,12,98,25,'#5887bc');r(12,0,70,38,'#5887bc');r(29,-8,26,46,'#5887bc');r(4,12,90,20,'#ffffff');r(16,4,62,28,'#ffffff');r(33,-4,18,36,'#ffffff');r(12,29,72,5,'#c2f0ff');c.restore();}
  function hill(x,h,w){poly([[x,GROUND],[x,GROUND-h*.3],[x+w*.18,GROUND-h*.3],[x+w*.18,GROUND-h*.64],[x+w*.35,GROUND-h*.64],[x+w*.35,GROUND-h],[x+w*.65,GROUND-h],[x+w*.65,GROUND-h*.64],[x+w*.82,GROUND-h*.64],[x+w*.82,GROUND-h*.3],[x+w,GROUND-h*.3],[x+w,GROUND]],'#5bc84c');r(x+w*.38,GROUND-h+4,w*.24,4,'#b4f275');}
  function ground(){r(0,GROUND,W,5,'#89421e');r(0,GROUND+5,W,5,'#ffe5a0');r(0,GROUND+10,W,H-GROUND-10,'#ed7940');for(let y=GROUND+12;y<H;y+=22){r(0,y,W,3,'#ffc588');for(let x=(y===GROUND+12?0:26);x<W;x+=52)r(x,y+3,3,19,'#914221');}}
  function puff(x,y,p,color){if(p<0||p>1)return;c.save();c.globalAlpha*=1-p;for(let i=0;i<9;i++){const a=i*Math.PI/4.5,rr=8+34*p;r(x+Math.cos(a)*rr,y+Math.sin(a)*rr,6*(1-p)+2,6*(1-p)+2,color);}c.restore();}
  function monster(x,t,index){
    x+=5*Math.sin(t*4+index);c.save();c.translate(x,GROUND);c.scale(1.25,1.25);x=0;const y=-44,body=index?'#f2754e':'#a576e4',edge=index?'#8d3d28':'#58408d';
    r(x-20,y+8,40,32,edge);r(x-12,y,24,40,edge);r(x-16,y+10,32,27,body);r(x-8,y+4,16,32,body);
    r(x-13,y+16,10,10,'#fff7e8');r(x+3,y+16,10,10,'#fff7e8');r(x-7,y+18,4,7,edge);r(x+3,y+18,4,7,edge);
    r(x-10,y+31,20,3,edge);const step=Math.sin(t*10)>0?3:0;r(x-23,y+38-step,16,6,edge);r(x+7,y+35+step,16,6,edge);
    c.restore();
  }
  function block(cx,hit,t,s,interactive=true){
    if(!interactive){
      const y=s.brick_y;r(cx-58,y,116,68,'#9c4b20');r(cx-55,y+3,110,62,'#ec7940');
      for(const yy of [4,31,58])r(cx-55,y+yy,110,3,'#ffcc8a');
      for(const [dx,dy] of [[-20,7],[32,7],[-45,34],[8,34]])r(cx+dx,y+dy,3,24,'#9c4b20');
      return;
    }
    const bump=s.brick_bump,open=t>=hit;
    c.save();c.translate(cx,s.brick_y-bump);c.scale(s.brick_scale,s.brick_scale);cx=0;const y=0;
    r(cx-58,y+4,116,68,'#9c4b20');r(cx-56,y,112,64,'#f49a2c');r(cx-52,y+4,104,56,open?'#ffbc3e':'#ffd15c');r(cx-48,y+8,96,4,open?'#ffe68a':'#fff3a7');
    for(const dx of [-47,44])for(const dy of [19,47])r(cx+dx,y+dy,3,3,'#a55822');
    if(!open)text('?',cx,y+34,36,'#633516');
    puff(cx,y+66,(t-hit)/.28,'#fff2a3');
    c.restore();
  }
  function hero(s){
    const b=boxes[s.frame];
    c.save();c.translate(s.x,s.y);c.scale(s.sx,s.sy);c.imageSmoothingEnabled=false;
    c.drawImage(sheet,b.x,b.y,b.w,b.h,-b.anchor*scale,-b.h*scale,b.w*scale,b.h*scale);
    c.restore();
  }
  function flag(s){
    c.save();c.translate(-82,0);
    r(1086,110,8,GROUND-110,'#47834c');r(1088,110,3,GROUND-110,'#ceefa4');r(1080,106,20,9,'#2e723e');
    const y=s.flag_y;poly([[1085,y],[1017,y],[1029,y+18],[1017,y+36],[1085,y+36]],'#20ad50');r(1063,y+12,8,12,'#ffffff');
    r(1069,GROUND-8,43,8,'#44883f');c.restore();
    if(s.t>=5.44){const p=ease((s.t-5.44)/.24);c.save();c.globalAlpha*=p;poly([[1055,252],[1061,258],[1074,243],[1079,248],[1061,268],[1050,257]],'#20ad50');c.restore();}
  }
  function scene(time){
    const s=state(time);c.globalAlpha=1;r(0,0,W,H,'#9bd8ff');
    cloud(42,75,.72);cloud(1004,39,.68);cloud(756,205,.43);
    hill(-36,44,180);hill(358,34,192);hill(725,46,180);hill(1093,57,150);
    // 像素图标从砖内弹出、轻轻回落后停住，降旗后与砖一起退场。
    c.save();c.globalAlpha=s.alpha;
    c.save();c.globalAlpha*=s.brick_alpha;
    for(const v of s.topic){c.save();c.globalAlpha*=v.alpha;icon(v);c.restore();}
    s.brick_centers.forEach((x,i)=>block(x,hits[0],s.t,s,i===s.interactive_brick));
    c.restore();
    c.save();c.globalAlpha*=s.title_alpha;text(TAGLINE,600,130+s.title_offset,70,'#193d72');c.restore();
    flag(s);
    for(const [i,x] of [740,880].entries()){
      if(s.monster_alive[i])monster(x,s.t,i);else puff(x,GROUND-24,(s.t-impacts[i])/.4,i?'#ffaf62':'#cfacff');
    }
    r(s.x-19,GROUND-2,38,4,'#70b365');hero(s);
    for(const b of s.bullets){r(b.x-17,b.y-3,14,6,'#ebc86b');r(b.x-8,b.y-6,12,12,'#344f66');r(b.x-5,b.y-8,7,16,'#344f66');r(b.x-5,b.y-5,4,4,'#9fc5d7');}
    for(const start of [2.84,3.72]){const p=(s.t-start)/.15;if(p>=0&&p<1){const x=start<3?654:798;c.save();c.globalAlpha*=1-p;r(x,GROUND-58,8,12,'#f4c759');c.restore();}}
    for(const land of [1.2]){const p=(s.t-land)/.2;if(p>=0&&p<1){c.save();c.globalAlpha*=1-p;r(s.x-24-p*12,GROUND-5,7,4,'#ffe3a0');r(s.x+20+p*12,GROUND-5,7,4,'#ffe3a0');c.restore();}}
    c.restore();ground();return s;
  }
  const frames=path.join(OUT,'_frames');fs.mkdirSync(frames,{recursive:true});const states=[];
  for(let i=0;i<Math.round(D*FPS);i++){const t=i===Math.round(D*FPS)-1?0:i/FPS;states.push(state(t));scene(t);fs.writeFileSync(path.join(frames,`${String(i).padStart(4,'0')}.png`),canvas.toBuffer('image/png'));}
  scene(6.5);fs.writeFileSync(path.join(OUT,'poster.png'),canvas.toBuffer('image/png'));
  scene(2);fs.writeFileSync(path.join(OUT,'topic.png'),canvas.toBuffer('image/png'));
  const contact=createCanvas(1200,5*180),sc=contact.getContext('2d');[0,.9,1.12,1.4,2,2.96,3.84,5.12,6,6.5].forEach((t,i)=>{scene(t);sc.drawImage(canvas,(i%2)*600,Math.floor(i/2)*180,600,180);});fs.writeFileSync(path.join(OUT,'keyframes.png'),contact.toBuffer('image/png'));
  const mobile=createCanvas(375,113);scene(6.5);mobile.getContext('2d').drawImage(canvas,0,0,375,112.5);fs.writeFileSync(path.join(OUT,'mobile.png'),mobile.toBuffer('image/png'));
  scene(2);mobile.getContext('2d').drawImage(canvas,0,0,375,112.5);fs.writeFileSync(path.join(OUT,'mobile-topic.png'),mobile.toBuffer('image/png'));
  const run=spawnSync('ffmpeg',['-y','-v','error','-framerate',String(FPS),'-i',path.join(frames,'%04d.png'),'-filter_complex','[0:v]split[a][b];[a]palettegen=max_colors=256:stats_mode=full[p];[b][p]paletteuse=dither=bayer:bayer_scale=3','-frames:v',String(Math.round(D*FPS)),'-loop','0',path.join(OUT,'intro.gif')],{encoding:'utf8'});if(run.status!==0)throw Error(run.stderr);
  fs.writeFileSync(path.join(OUT,'manifest.json'),JSON.stringify({account:'程序员梦哥',visible_title:TAGLINE,topic_words:[],topic_icons:TOPIC,icon_style:'user supplied seven original icons, sampled on a 24px grid and rendered at 3x nearest neighbor',icon_size:72,brick_words:[],typography:{family:'Fusion Pixel 12px Proportional zh_hans',base_px:12,footer_scale:6,font_file:'../程序员梦哥像素闯关-v3/fonts/fusion-pixel-12px-proportional-zh_hans.ttf.woff2'},width:W,height:H,fps:FPS,frame_count:Math.round(D*FPS),duration_seconds:D,ground:GROUND,brick_bottom:150,hits,impacts,topic_pop_duration:.82,icon_stagger:.045,icon_order:order,icon_targets:targets,topic_settled:1.91,flag_lowering:[4.8,5.44],brick_fade:[5.46,5.78],title_reveal:[5.84,6.36],brand_hold:[6.36,8.36],reset:[8.36,8.8],animation_engine:{name:'GSAP',version:engine,labels},sprite_boxes:boxes,sprite_scale:scale,method:'Reused imagegen 16-pose sheet; GSAP paused timelines sampled at 50fps, Canvas and FFmpeg GIF',wechat_verified:false,states},null,2)+'\n');
  fs.writeFileSync(path.join(OUT,'preview.html'),`<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>程序员梦哥 · 像素闯关 v6丝滑版</title><style>*{box-sizing:border-box}body{margin:0;background:#e9eff2;color:#2b4758;font:15px/1.8 "Microsoft YaHei",sans-serif}main{max-width:1100px;margin:28px auto;padding:28px;background:white;border-radius:16px}h1{font-size:23px;margin:0}h2{font-size:17px;margin-top:26px}p{color:#758995}img{display:block;width:100%}.phone{width:375px;max-width:100%;border:1px solid #e0e8ec}.body{padding:18px 24px}button,a{display:inline-block;margin:12px 8px 0 0;border:1px solid #d2dfe4;border-radius:6px;background:white;padding:7px 12px;color:#3d7089;font:inherit;text-decoration:none}@media(max-width:650px){main{margin:0;padding:18px}}</style><main><h1>七款 AI 工具 · 动效优化版</h1><p>顶一次中间砖，七款 AI 工具像素图标散开 → 发炮打怪 → 降旗 → 分享AI、少踩坑，8.8秒循环，50fps。图标从中心向两侧依次抛出、回落停稳。</p><img data-loop src="intro.gif" alt="像素人物顶中间砖弹出七款AI工具图标，降旗后显示分享AI、少踩坑"><button onclick="document.querySelectorAll('img[data-loop]').forEach(im=>im.src='intro.gif?t='+Date.now());document.querySelectorAll('img[data-loop-old]').forEach(im=>im.src='../程序员梦哥像素闯关-v5工具箱/intro.gif?t='+Date.now())">从头播放</button><a href="intro.gif" download>下载 GIF</a><h2>375px 文章预览</h2><div class="phone"><img data-loop src="intro.gif" alt="375px片头预览"><div class="body"><b>你好，我是梦哥。</b><p>这里接今天的文章。</p></div></div><h2>上一版对照</h2><img data-loop-old src="../程序员梦哥像素闯关-v5工具箱/intro.gif" alt="上一版25fps动效"><h2>十个动作时刻</h2><img src="keyframes.png" alt="一次顶砖、工具散开、打怪与降旗关键帧"><p>本地候选；复用既有角色、代码制作GIF，公众号后台及真机效果待验收。</p></main></html>`);
  console.log(JSON.stringify({frames:Math.round(D*FPS),gif_bytes:fs.statSync(path.join(OUT,'intro.gif')).size,duration:D}));
}
if(require.main===module)main().catch(e=>{console.error(e);process.exitCode=1});
module.exports={state};
