// 七枚图标均由整数像素形状直接绘制，不读取或采样截图。
const names=['codex','claude','workbuddy','kimi','user07','minimax','deepseek'];
function drawIcons(createCanvas){
  const icons=new Map();
  for(const name of names){
    const im=createCanvas(24,24),g=im.getContext('2d');
    const r=(x,y,w,h,color)=>{g.fillStyle=color;g.fillRect(x,y,w,h);};
    const poly=(points,color)=>{
      for(let y=0;y<24;y++)for(let x=0;x<24;x++){
        let inside=false;
        for(let i=0,j=points.length-1;i<points.length;j=i++){
          const [a,b]=points[i],[c,d]=points[j];
          if((b>y+.5)!==(d>y+.5)&&(x+.5)<(c-a)*(y+.5-b)/(d-b)+a)inside=!inside;
        }
        if(inside)r(x,y,1,1,color);
      }
    };
    const line=(points,color,width=2)=>{
      for(let i=1;i<points.length;i++){
        let [x,y]=points[i-1];const [tx,ty]=points[i],dx=Math.abs(tx-x),dy=-Math.abs(ty-y),sx=x<tx?1:-1,sy=y<ty?1:-1;
        let err=dx+dy;
        while(true){r(x,y,width,width,color);if(x===tx&&y===ty)break;const e=2*err;if(e>=dy){err+=dy;x+=sx;}if(e<=dx){err+=dx;y+=sy;}}
      }
    };
    const badge=color=>{r(2,0,20,24,color);r(0,2,24,20,color);};
    const white='#fff6df';
    if(name==='codex'){
      r(5,1,13,22,'#8374ff');r(2,5,20,14,'#8374ff');r(0,9,24,7,'#8374ff');
      r(5,0,11,4,'#a6a0ff');r(2,5,20,3,'#a09cff');r(3,17,18,3,'#6262fb');r(6,20,13,3,'#5355f7');
      line([[6,7],[9,11],[6,15]],white);r(13,15,7,2,white);
    }else if(name==='claude'){
      badge('#d97755');
      for(const [x,y] of [[12,3],[17,4],[20,8],[21,13],[19,18],[15,21],[10,20],[6,20],[3,15],[3,10],[5,6],[8,3]])
        line([[11,11],[x,y]],white);
      r(9,9,6,6,white);
    }else if(name==='workbuddy'){
      badge('#08c5a2');r(2,19,20,4,'#21c783');
      poly([[2,12],[6,11],[12,12],[16,9],[18,3],[20,2],[23,7],[23,10],[18,11],[12,16],[9,21],[3,23],[4,18]],'#dcfff0');
      poly([[9,16],[16,12],[22,12],[24,16],[23,22],[19,24],[11,24],[8,20]],'#20c895');
      line([[12,18],[13,20]],white);line([[18,16],[19,18]],white);
    }else if(name==='kimi'){
      badge('#151a25');r(5,5,3,15,'#ffffff');
      poly([[8,11],[12,11],[16,5],[19,5],[15,12],[12,14],[8,14]],'#ffffff');
      poly([[10,12],[15,12],[18,15],[18,20],[15,20],[15,16],[12,15],[10,15]],'#ffffff');
      r(19,4,3,3,'#3677ff');r(18,5,4,2,'#3677ff');
    }else if(name==='minimax'){
      badge('#f42b79');r(12,0,10,24,'#fb425f');r(20,2,4,20,'#ff6850');
      line([[3,12],[3,15],[5,15],[5,8],[6,7],[8,7],[8,19],[10,19],[10,5],[11,4],[13,4],[13,20],[15,20],[15,8],[16,7],[18,7],[18,15],[20,15],[20,10]],white,1);
    }else if(name==='deepseek'){
      // 蓝鲸轮廓、尾鳍、白色笑眼与喷水。
      poly([[2,12],[3,7],[7,4],[13,4],[17,7],[18,11],[22,9],[22,14],[19,17],[14,20],[7,20],[3,18]],'#4e63ff');
      poly([[3,10],[7,8],[7,13],[10,16],[8,18],[5,16]],'#eef4ff');
      poly([[13,16],[19,17],[16,21],[11,22],[5,20],[10,20]],'#3a7aff');
      r(12,8,3,1,'#ffffff');r(11,9,1,2,'#ffffff');r(15,9,1,2,'#ffffff');
      line([[18,6],[20,3]],'#3677ff',1);r(22,3,1,2,'#3677ff');r(21,7,2,1,'#3677ff');
    }else{
      // 用户第七张紫绿环形标记，仅按形状描绘，暂不猜产品名。
      poly([[2,5],[6,1],[12,0],[17,4],[23,11],[21,18],[14,23],[7,23],[1,19]],'#9e65ff');
      poly([[15,2],[23,11],[16,9]],'#343dff');
      poly([[16,9],[23,11],[23,15],[20,20],[14,23],[11,24],[15,17]],'#29d7ad');
      poly([[8,10],[13,8],[16,9],[16,15],[13,20],[9,23],[5,23],[4,19],[5,14]],'#f8fbff');
      poly([[1,18],[5,13],[8,11],[5,17],[4,22],[1,21]],'#6d38ee');
    }
    icons.set(name,im);
  }
  return icons;
}
module.exports={drawIcons,names};
