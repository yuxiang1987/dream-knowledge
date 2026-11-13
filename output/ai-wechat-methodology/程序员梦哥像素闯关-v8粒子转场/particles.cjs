// 固定像素格拆分，颜色/纹理直接来自本场景的原绘图标与砖块图层。
const START=5.46,END=6.16;
const clamp=x=>Math.max(0,Math.min(1,x));
function makeParticles(data,width,height){
  const particles=[],step=8;
  for(let y=0;y<height;y+=step)for(let x=0;x<width;x+=step){
    const w=Math.min(step,width-x),h=Math.min(step,height-y);
    let visible=false;
    for(let yy=y;yy<y+h&&!visible;yy++)for(let xx=x;xx<x+w;xx++)if(data[(yy*width+xx)*4+3]){visible=true;break;}
    if(!visible)continue;
    const seed=((x*73856093)^(y*19349663))>>>0;
    const a=(seed%997)/997,b=((seed>>>8)%991)/991;
    particles.push({x,y,w,h,delay:clamp((x-216)/650)*.12+a*.12,life:.46,
      dx:(a-.35)*70,dy:8+b*30});
  }
  return particles;
}
function sample(p,elapsed){
  const q=clamp((elapsed-p.delay)/p.life),drift=q*(2-q);
  return {x:p.x+p.dx*drift,y:p.y+p.dy*drift,scale:1-.88*q*q,alpha:1-q*q,progress:q};
}
module.exports={makeParticles,sample,START,END};
