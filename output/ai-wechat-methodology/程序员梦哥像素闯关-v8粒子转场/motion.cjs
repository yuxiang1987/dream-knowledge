const {gsap}=require('../程序员梦哥像素闯关-v6丝滑版/node_modules/gsap');
const names=['codex','claude','workbuddy','kimi','user07','minimax','deepseek'];
const targets=[[340,46],[440,44],[540,48],[640,46],[740,50],[260,116],[820,108]];
const order=[2,1,3,0,4,5,6];
const hero={x:110,lift:0,sx:1,sy:1};
const stage={bump:0,brickAlpha:1,flag:126,titleAlpha:0,titleOffset:16};
const icons=names.map((name,i)=>({name,x:540,y:116,alpha:0,scale:.5,angle:(i%2?1:-1)*10}));
const timeline=gsap.timeline({paused:true,defaults:{ease:'power2.out'}});
timeline.addLabel('approach',.04).addLabel('prepare',1.32).addLabel('hit',1.9).addLabel('scatter',1.92)
  .addLabel('flag',4.8).addLabel('clear',5.46).addLabel('footer',6.04);
timeline.to(hero,{sx:1.07,sy:.90,duration:.18},'prepare')
  .to(hero,{sx:.97,sy:1.05,duration:.12},1.5)
  .to(hero,{lift:48,duration:.4,ease:'power1.out'},1.5)
  .to(hero,{sx:1,sy:1,duration:.2},1.7)
  .to(hero,{lift:0,duration:.4,ease:'power1.in'},'hit')
  .to(hero,{sx:1.08,sy:.90,duration:.06,ease:'power1.out'},2.3)
  .to(hero,{sx:1,sy:1,duration:.16,ease:'power2.out'},2.36);
for(const [start,end,x] of [[.04,1.3,502],[3.14,4.66,960]])
  timeline.to(hero,{x,duration:end-start,ease:'power1.inOut'},start);
timeline.to(stage,{bump:14,duration:.09},'hit')
  .to(stage,{bump:-2,duration:.13,ease:'power1.in'},1.99)
  .to(stage,{bump:0,duration:.12,ease:'power1.out'},2.12);
// 中心先出，向两侧依次释放。横向展开与纵向抛物线分开控制。
timeline.to(order.map(i=>icons[i]),{alpha:1,duration:.1,stagger:.045,ease:'power1.out'},'scatter');
order.forEach((i,rank)=>{
  const start=1.92+rank*.045,v=icons[i],[x,y]=targets[i],apex=Math.min(y-2,64);
  timeline.to(v,{x,duration:.82,ease:'power2.out'},start)
    .to(v,{y:apex,duration:.46,ease:'power2.out'},start)
    .to(v,{y,duration:.36,ease:'power1.inOut'},start+.46)
    .to(v,{scale:1.04,duration:.42,ease:'power2.out'},start)
    .to(v,{scale:1,duration:.4,ease:'sine.inOut'},start+.42)
    .to(v,{angle:0,duration:.72,ease:'power2.out'},start);
});
timeline.to(stage,{flag:264,duration:.64,ease:'power2.inOut'},'flag')
  .set(stage,{brickAlpha:0},'clear')
  .to(stage,{titleAlpha:1,duration:.34,ease:'power1.out'},'footer')
  .to(stage,{titleOffset:0,duration:.52,ease:'power2.out'},'footer');
const fade={alpha:1};
const loop=gsap.timeline({paused:true});
loop.to(fade,{alpha:0,duration:.22,ease:'sine.inOut'},8.56)
  .to(fade,{alpha:1,duration:.22,ease:'sine.inOut'},8.78);
gsap.ticker.sleep();
function state(time){
  const t=time>=8.78?0:time;
  timeline.seek(t,true);loop.seek(time,true);
  let pose='idle',frame=2,bob=0;
  for(const [a,b] of [[.04,1.3],[3.14,4.66]])if(t>=a&&t<b){pose='walk';frame=Math.floor((t-a)/.075)%8;bob=[0,1,2,2,0,1,2,2][frame];}
  if(t>=1.32&&t<1.5){pose='crouch';frame=12;}
  if(t>=1.5&&t<1.9){pose='rise';frame=13;}
  if(t>=1.9&&t<2.3){pose='fall';frame=t<2.012?13:14;}
  if(t>=2.3&&t<2.52){pose='land';frame=15;}
  const s={t,x:hero.x,y:318-hero.lift-bob,sx:hero.sx,sy:hero.sy,pose,frame,
    bullets:[],monster_alive:[],unlocked:[false,t>=1.9,false],
    brick_centers:[420,540,660],interactive_brick:1,brick_scale:1,brick_y:82};
  s.topic=icons.map((v,i)=>({text:v.name,x:v.x,y:v.y,alpha:v.alpha,scale:v.scale,angle:v.angle,target:targets[i]}));
  s.particle_elapsed=t-5.46;s.particle_active=t>=5.46&&t<6.16;
  s.brick_bump=stage.bump;s.brick_alpha=stage.brickAlpha;s.flag_y=stage.flag;
  s.title_alpha=stage.titleAlpha;s.title_offset=stage.titleOffset;s.alpha=fade.alpha;
  return s;
}
module.exports={state,engine:gsap.version,labels:timeline.labels,targets,order};
