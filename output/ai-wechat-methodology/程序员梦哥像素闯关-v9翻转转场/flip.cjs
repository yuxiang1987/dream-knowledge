const START=5.46,END=6.13;
const clamp=x=>Math.max(0,Math.min(1,x));
function angleAt(time,delay){
  const p=clamp((time-START-delay)/.52);
  return 90*(p*p*(3-2*p));
}
function project(u,v,angle,perspective){
  const a=angle*Math.PI/180,k=perspective/(perspective+u*Math.sin(a));
  return {x:u*Math.cos(a)*k,y:v*k};
}
// 逐列投影到绕竖轴转动的平面，保留近侧/远侧不同高度的透视。
function drawFlip(c,image,x,y,w,h,angle,perspective=500){
  if(Math.abs(angle)>=89.999)return;
  c.save();c.imageSmoothingEnabled=false;
  if(Math.abs(angle)<.001){c.drawImage(image,x-w/2,y-h/2,w,h);c.restore();return;}
  for(let sx=0;sx<image.width;sx++){
    const u0=(sx/image.width-.5)*w,u1=((sx+1)/image.width-.5)*w;
    const p0=project(u0,0,angle,perspective),p1=project(u1,0,angle,perspective);
    const top=project((u0+u1)/2,-h/2,angle,perspective);
    const left=Math.round(x+p0.x),right=Math.round(x+p1.x);
    if(right>left)c.drawImage(image,sx,0,1,image.height,left,Math.round(y+top.y),right-left,Math.round(-top.y*2));
  }
  c.restore();
}
module.exports={START,END,angleAt,project,drawFlip};
