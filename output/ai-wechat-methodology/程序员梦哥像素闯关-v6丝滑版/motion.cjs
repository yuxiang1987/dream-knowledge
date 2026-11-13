const {gsap}=require('gsap');
const {state:baseState}=require('../程序员梦哥像素闯关-v5工具箱/build.cjs');
const names=['codex','claude','workbuddy','kimi','user07','minimax','deepseek'];
const targets=[[340,46],[440,44],[540,48],[640,46],[740,50],[260,116],[820,108]];
const order=[2,1,3,0,4,5,6];
const hero={x:502,lift:0,sx:1,sy:1};
const stage={bump:0,brickAlpha:1,flag:126,titleAlpha:0,titleOffset:16};
const icons=names.map((name,i)=>({name,x:540,y:116,alpha:0,scale:.5,angle:(i%2?1:-1)*10}));
const timeline=gsap.timeline({paused:true,defaults:{ease:'power2.out'}});
timeline.addLabel('prepare',.22).addLabel('hit',.8).addLabel('scatter',.82)
  .addLabel('flag',4.8).addLabel('clear',5.46).addLabel('footer',5.84);
timeline.to(hero,{sx:1.07,sy:.90,duration:.18},'prepare')
  .to(hero,{sx:.97,sy:1.05,duration:.12},.4)
  .to(hero,{lift:48,duration:.4,ease:'power1.out'},.4)
  .to(hero,{sx:1,sy:1,duration:.2},.6)
  .to(hero,{lift:0,duration:.4,ease:'power1.in'},'hit')
  .to(hero,{sx:1.08,sy:.90,duration:.06,ease:'power1.out'},1.2)
  .to(hero,{sx:1,sy:1,duration:.16,ease:'power2.out'},1.26);
for(const [start,end,x] of [[1.4,1.8,602],[3.28,3.54,746],[4.16,4.74,960]])
  timeline.to(hero,{x,duration:end-start,ease:'power1.inOut'},start);
timeline.to(stage,{bump:14,duration:.09},'hit')
  .to(stage,{bump:-2,duration:.13,ease:'power1.in'},.89)
  .to(stage,{bump:0,duration:.12,ease:'power1.out'},1.02);
// 中心先出，向两侧依次释放。横向展开与纵向抛物线分开控制。
timeline.to(order.map(i=>icons[i]),{alpha:1,duration:.1,stagger:.045,ease:'power1.out'},'scatter');
order.forEach((i,rank)=>{
  const start=.82+rank*.045,v=icons[i],[x,y]=targets[i],apex=Math.min(y-2,64);
  timeline.to(v,{x,duration:.82,ease:'power2.out'},start)
    .to(v,{y:apex,duration:.46,ease:'power2.out'},start)
    .to(v,{y,duration:.36,ease:'power1.inOut'},start+.46)
    .to(v,{scale:1.04,duration:.42,ease:'power2.out'},start)
    .to(v,{scale:1,duration:.4,ease:'sine.inOut'},start+.42)
    .to(v,{angle:0,duration:.72,ease:'power2.out'},start);
});
timeline.to(stage,{flag:264,duration:.64,ease:'power2.inOut'},'flag')
  .to(stage,{brickAlpha:0,duration:.32,ease:'power1.inOut'},'clear')
  .to(stage,{titleAlpha:1,duration:.34,ease:'power1.out'},'footer')
  .to(stage,{titleOffset:0,duration:.52,ease:'power2.out'},'footer');
const fade={alpha:1};
const loop=gsap.timeline({paused:true});
loop.to(fade,{alpha:0,duration:.22,ease:'sine.inOut'},8.36)
  .to(fade,{alpha:1,duration:.22,ease:'sine.inOut'},8.58);
gsap.ticker.sleep();
function state(time){
  const t=time>=8.58?0:time;
  timeline.seek(t,true);loop.seek(time,true);
  const s=baseState(Math.min(t,8.5)),u=t-(t<3.28?2.84:3.72),recoil=u>=0&&u<.16?-5*Math.sin(Math.PI*u/.16):0;
  s.t=t;
  s.x=hero.x+recoil;s.sx=hero.sx;s.sy=hero.sy;
  if(t>=.4&&t<=1.2)s.y=318-hero.lift;
  s.topic=icons.map((v,i)=>({text:v.name,x:v.x,y:v.y,alpha:v.alpha,scale:v.scale,angle:v.angle,target:targets[i]}));
  s.brick_bump=stage.bump;s.brick_alpha=stage.brickAlpha;s.flag_y=stage.flag;
  s.title_alpha=stage.titleAlpha;s.title_offset=stage.titleOffset;s.alpha=fade.alpha;
  return s;
}
module.exports={state,engine:gsap.version,labels:timeline.labels,targets,order};
