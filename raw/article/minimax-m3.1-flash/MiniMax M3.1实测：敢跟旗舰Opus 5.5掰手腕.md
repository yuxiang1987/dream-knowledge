---
title: "MiniMax M3.1实测：敢跟旗舰Opus 5.5掰手腕"
source: "https://mp.weixin.qq.com/s/nmoMhTgKXneY3Lxhnm5Zlw"
author:
  - "[[苗正]]"
published:
created: 2026-10-03
description: "审美在线的Flash模型"
tags:
  - "clippings"
---
苗正 字母榜 *2026年10月1日 22:29*

![图片](https://mmbiz.qpic.cn/mmbiz_png/nn4fiaIib6wsvQUjNWwuDg2uRNmFtmxm5QHDTTz0xromvYe6SerrqtXdnnT62KibIic6B0BEP2wTqRMSOgR3MbNStptUjd3Uf8PYqGcLlaLaMxg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

过去一两周开发者圈里突然冒出来一个叫Space Bunny的模型，在OpenRouter和OpenCode上口碑炸了，大家都在猜背后是谁，有人说是OpenAI，有人说是谷歌。

不久后，M3.1 Flash Preview也随之上线。两者参数、定位高度匹配。

社区开发者做了多组独立测试（24组、50组探针字符串），Space Bunny的token计数行为和MiniMax M系列一致。在大家的实测中，M3.1 Flash Preview也秉承了M系列“量大管饱速度快”的特点。

M3.1 Flash Preview支持文本、图像和视频输入。这次我们重点看它如何结合代码与工具，把视觉要求做成动画、网页和交互作品。

凭借多模态能力的领先，M3.1 Flash Preview对布局、配色、材质、动画与场景氛围的把握，在前端场景中基本能持平Opus 5.5。 ![图片](https://mmbiz.qpic.cn/mmbiz_png/nn4fiaIib6wsv1ewueoD1kOPKnjboV7wSckaDHoF1w71G1SzZfyteWQicY9Y5dIM4NEzQ7muXIvicDlxJyZzxkQFJUwp5ENpghfWicWKJr5O34Mw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

M3.1 Flash是MiniMax M系列的最新一员，它的定位是主力模型，负责干活。

最近各个模型厂都在卷的Flash模型战场，M3.1 Flash Preview虽然挂着Flash的名字，但是它实际干活的表现，在大部分设计类场景下，都能持平Opus 5.5这样的旗舰模型。

![图片](https://mmbiz.qpic.cn/mmbiz_png/nn4fiaIib6wsticic1zW0pe4pn01aeCBnLeZNobr8Bou6KkDRiaSUULoEhKVYvFjDegMplvMW9MOibF0IypJXKiamoRBkVwlewwLicvmiafq4okvoQMU/640?wx_fmt=png&from=appmsg#imgIndex=2)

就连OpenCode的联合创始人Dax，也对其前端设计给了充分肯定，认为它和Opus 5.5对齐的。

M3.1 Flash最大的特点是，网上有一个案例，用M3.1 Flash Preview一次成型一个博客系统，平均速度约160 token/s，整轮消耗约7000万token。

这是一个非常复杂的长程任务，说明M3.1 Flash Preview不只是反应快，还能在长任务里持续稳定地输出。

![图片](https://mmbiz.qpic.cn/mmbiz_png/nn4fiaIib6wsuSoF8Icoic2X0ptV3rsfCeIJficuBfW0Pee3bb6U6SZ6IAZk8sqULHicpyajbfSTx6QaqBAyaVxvo93XzFCmwfrmODcmBaemrcEU/640?wx_fmt=png&from=appmsg#imgIndex=3)

多模态方面，M3.1 Flash能够实现“有图就有码”。即你给它一张图，它就能把代码写出来。

更难得的是它的审美在线。

M3.1 Flash Preview能把握整体风格与细节，让布局、配色、材质、动画和场景氛围拧成一个整体。也能搭复杂的3D场景，处理多部件结构、动态效果、用户操作与状态变化。

最后一点，也是最容易被忽略，M3.1 Flash Preview严谨、靠谱，能检查自己的视觉输出，并继续修正。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/nn4fiaIib6wsvhXnNCY2YKpw7zkc1H7bZ0ibiaebe0QMiaWATlybSvryNxfe0NIz3Tdt0x5qlEacicUXRc2zQSJJdP7On8MZJAibHic07icibL8ae0OFE/640?wx_fmt=png&from=appmsg#imgIndex=4)

最近Claude Opus 5.5在设计和商业视频制作方面表现很突出，再加上它是目前全球最顶尖的模型之一，所以在实测环节中，采用同一道题、同一个提示词，分别交给Claude Opus 5.5和MiniMax M3.1 Flash Preview，不调参、不挑图，直接看各自的成品。

**第一组｜纯代码 UI 动效片（一镜到底 motion design）**

这组提示词就是验证模型能不能不用After Effects、不用素材，纯靠代码做出一支Dribbble级的界面动效短片。

这题两个模型最大的区别在于中后部份图表的表示。Opus 5.5选择了分段表示，M3.1 Flash选择了完整表示，并且鼠标放在线条上时，会提示当前的数值。

提示词：给出 8～12 个界面状态和一首约 120 BPM 的免版税配乐，要求“一个元素、从不剪切”——同一个形状在改变尺寸、圆角与颜色的过程中，用短模糊把内容切换成下一个状态，全部交互由光标驱动、真实点击与拖拽。

Opus 5.5

，时长00:14

<video src="https://mpvideo.qpic.cn/0bc3lqab6aaaceaffkv64jvfaxgdd5oaahya.f10002.mp4?dis_k=cdd13d224e1d082eade90a0c6bd8dba2&amp;dis_t=1791020800&amp;play_scene=10120&amp;auth_info=KMiTgwwffWOT6LWWWixrNm9OYhcAKT4VSBYge30JY08OOg5wIQQwFH0+F283IUsiZQ==&amp;auth_key=63d461f27f307ee85e86cbcc7bf9f63b&amp;vid=wxv_4718831156295778310&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

M3.1 Flash Preview

，时长00:22

<video src="https://mpvideo.qpic.cn/0bc3dyco4aaeimakjuv2ivvfihwd5ypaj3qa.f10002.mp4?dis_k=5cd373f4d98ed70720111c11dadce020&amp;dis_t=1791020800&amp;play_scene=10120&amp;auth_info=dpyCq+sIHXs1nrXhll0kbmE+GzYfU3k/Eh8QJyYpWTJIDjpZdiEGNkJwY0NvMClOdTQ=&amp;auth_key=5d25f408c25d1645e7f61c01c576404c&amp;vid=wxv_4718818531910647814&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

**第二组｜纯代码像素动画（160×90 复古跑酷）**

这是一个压力测试，在“小画布 ＋ 固定调色板 ＋ 零外部素材”的前提下，模型能不能手搓出一段16位机质感的像素动作 demo。

从实际表现来看，两者的整个场景、动作和效果都表现得很好。区别在于，M3.1 Flash是把主要角色的比例放大，并且画面中射出的激光也不再只有水平方向，有些会朝上发射，显得更多样。

提示词：用原生 JS ＋ Canvas 2D 写一个自包含单文件 HTML，全程无外部素材、无库、无网络请求，自动演示并无缝循环。场景是一段横版疾走——橙色像素小人（精确到 12×8 像素、四帧跑腿循环、姿势参数化）在宇宙里一条七色虹桥上朝右狂奔。

Opus 5.5

，时长00:18

<video src="https://mpvideo.qpic.cn/0bc3yiagwaaanmacplv6ybvfbqwdnpbaa2ya.f10002.mp4?dis_k=b75272b1308ed1003b470b1dee831235&amp;dis_t=1791020800&amp;play_scene=10120&amp;auth_info=IcCj0K8NGX5il7XhllskaWBsHjAeUnlqExtMd3IrWDcfWmtYdiACMxV5Y0NvNilJdGY=&amp;auth_key=592b36ada1e5b3ce3ff9d48335c27e00&amp;vid=wxv_4718828396627623937&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

M3.1 Flash Preview

，时长00:20

<video src="https://mpvideo.qpic.cn/0bc3u4ahaaaacmadsnf655vfbj6doctqa4aa.f10002.mp4?dis_k=264ded37d64e1acabc2a9292f0cc8574&amp;dis_t=1791020800&amp;play_scene=10120&amp;auth_info=carCrN5aSHg1kbnhwwt3ODFtGGYXAnE8EE4XJ3ssXDZPW2oOJHZTNUJ/b0M6ZnoYJWc=&amp;auth_key=312b47af23ff001420efd703d6ec10a0&amp;vid=wxv_4718815703339139073&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

**第三组｜一首歌 → 一整支音乐动画（视觉设计／“Claude-Pop”）**

光是图片转码还不够，毕竟多模态不是只有视觉，听觉也是很重要的一环。所以这一组，就是验证模型能不能把一首现成的歌，做成一支有完整视觉设计、能当“虚拟偶像单曲 MV”传播的动画短片。关键在于审美、角色与整片调度，而不是单点特效。

这题很有意思，两个模型采用了完全不同的风格。从实际表现来看，Opus 5.5的镜头几乎是固定的，没有分镜，反倒是M3.1 Flash的2D更有表现力一些。

提示词：输入是一段 MP4 音频与原曲链接（“Claude-Pop”——一首关于 AI 加速与奇点临近的流行歌《I'm Upping My P(Doom)》），要求为它生成一整支音乐动画，视觉风格以 K-pop 为锚点、刻意避开 Pixar 式的“糖水感”，同时兼顾社交平台上的传播审美。

Opus 5.5

，时长02:36

<video src="https://mpvideo.qpic.cn/0bc3fuabcaaauyafyxf6crvfalodcewqaeia.f10002.mp4?dis_k=869e54994d0bbb79f7fcf71c4f982816&amp;dis_t=1791020800&amp;play_scene=10120&amp;auth_info=e6uB8sMLQnZlw73mkAgjYDU5TGRIB3ltQhhNfHEhWjRFW2cPdCZZOxIta0RpZS5AITM=&amp;auth_key=dd980b6606e0bf6831e047bcd2633334&amp;vid=wxv_4718832184034590726&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

M3.1 Flash Preview

，时长02:36

<video src="https://mpvideo.qpic.cn/0b2eiuab4aaatqafizf6sbvfaroddzcqahqa.f10002.mp4?dis_k=e5b8127c188df8008dd31276858f3321&amp;dis_t=1791020800&amp;play_scene=10120&amp;auth_info=Lv/auhRJeDKWtbyWDCxpYzZOYx0BejlARkF8JSpYMEwIawh5I1I1RXhjHm9hIUl3PA==&amp;auth_key=3d6c045cecee4a4b561bda80ceae7ff4&amp;vid=wxv_4718820620103270401&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

除此之外，我也用M3.1 Flash Preview尝试了一些带有交互性质的提示词，且均不允许模型使用任何外部素材。所有展示均为提示词一次生成，不做任何二次改动。

我要求M3.1 Flash给我做一个模拟毛笔的工具，但是要求它先自己画一个背景出来，且我能在上面进行修改。一次交付后，我就已经能在上面作画了，而且表现力也非常接近实际的毛笔。

提示词：你同时担任水墨画师、WebGL 图形工程师与交互设计师。请从零做一个可在浏览器实时“作画”的水墨山水场景，命名《氤氲》：用户移动鼠标或手指即执笔，落笔成山、拖笔成水、点按成苔，画面由代码实时生成水墨效果。请直接交付可运行文件，不要只给方案、代码片段或静态图；合理之处自行决定，不要步步来问。

，时长00:30

<video src="https://mpvideo.qpic.cn/0bc3gieiuaaineamhb5wubvfqmwdrizarcqa.f10002.mp4?dis_k=acda2f52e02e38bcb3d0fff9b9dc7bb1&amp;dis_t=1791020800&amp;play_scene=10120&amp;auth_info=Ir+CoexbTn00l7/hwVJ2OjE9TjdIVi43FEcQJ3R7CTMcDjoLc3RVMEN5aUM4P3saJTc=&amp;auth_key=3405d788826ddddb208460df09be34fa&amp;vid=wxv_4718814202918813697&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

这道题同样为图转码，我给了M3.1 Flash一张《赛博朋克2077》的截图，让它生成一个类似的街道，并且还要能控制天气、效果。演示中可以控制雨滴、窗户、光源、地面反射等等，尤其是它为了突出科幻背景，还制作了几辆飞行的汽车。

提示词：我上传给你一张截图，用 Three.js（importmap 从 CDN 加载 three，或零依赖原生 WebGL1）做一个可在浏览器实时漫游的“赛博朋克雨夜都市”3D 场景，命名 CYBER RAIN。全部几何、材质、灯光、纹理都用代码程序化生成，不得下载或热链任何现成模型、贴图、字体或外部服务；刷新即开，不依赖任何后端。

，时长00:39

<video src="https://mpvideo.qpic.cn/0b2ecuab6aaa7yafoef6m5vfafodd4kqahya.f10002.mp4?dis_k=6fcd55e76ab05bf0b29bc169b7bca3b0&amp;dis_t=1791020800&amp;play_scene=10120&amp;auth_info=da6n3pYJHnhnxu+0xwhyaTE8E2VNAX43FEkWJyIqCTJLCz0OdCcFNRAoORY+ZX9JJTY=&amp;auth_key=81857eca7f83a62ea0b8cc3f5fa92050&amp;vid=wxv_4718812324525211650&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

最后一个是音乐软件，多模态不是只有视觉，听觉也很重要。于是我为了测试M3.1 Flash对音频的理解，让它做了一个根据音量、鼓点、重音展现动画效果的播放器。

令我意外的是，其实我的提示词很简陋，但M3.1 Flash不仅能根据音乐本身做出可视化效果，还能在我调整音量的时候做出回应。此外，它还设置了三个按钮，以改变波浪的颜色。

提示词：用原生 HTML + Web Audio API + Canvas 2D 或 WebGL 做一个实时音乐可视化“现场”，命名 THE WAVE。允许用户上传一首本地音频（或用内置合成器生成一段演示音乐），播放时画面随声音实时律动；不依赖外部 CDN 或付费 API。

，时长00:21

<video src="https://mpvideo.qpic.cn/0bc3smeh2aai2uadcofwlnvfre6dpwjqq7ia.f10002.mp4?dis_k=c6a4d631eb5775c545e59a8eac59166c&amp;dis_t=1791020800&amp;play_scene=10120&amp;auth_info=INLs/+wMSH40xbizxV93bGc7TzIXUXBrFx1BfXIvXWEeWz9eJSRTM0MrbhE8MnpMczE=&amp;auth_key=5e537ebea1b8259338ed8bd79c4b5e7a&amp;vid=wxv_4718826743317626881&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

![图片](https://mmbiz.qpic.cn/mmbiz_png/nn4fiaIib6wstTjEKjkX1zBOcOt4079EG76LFl3qvSvfDzCQDicnicoJ0EZJpGc5p9EH7gsGjnEtADSluHvSd78bXsfia9m43UoSicA4aj1GdYddA/640?wx_fmt=png&from=appmsg#imgIndex=5)

从官方定位来看，M3.1 Flash Preview是MiniMax M系列的最新主力，面向的是Agent推理、工具调用、代码与长上下文任务。

但它真正值得说的，不是“又便宜又快”。因为这本来就是Flash这个系列应该做的，难的是在这个价位上，还能把活干得漂亮。

通常一提Flash，大家默认能力要打折，尤其碰上设计、动效、成片这类既吃审美、又要求端到端交付的活，Flash 档往往使不上劲：要么质感不够，要么只给素材、给不了成品。

M3.1 Flash打破的正是这个预期。

它把参照物直接抬到Opus 5.5这里，靠的不是参数，而是实打实的视觉与创意交付。像素动画、音乐动画、广告成片、界面动效，这些过去被视为旗舰专属、要人接力好几天的活，它能用纯代码一口气走完。

所以它的定位不是“又一个更便宜的Flash”，是第一个能在创意赛道上跟旗舰正面过招的Flash。把旗舰级的创意产能，装进Flash的价格带。

换句话说，它真正想证明的，是用 Flash 的成本，也能拿到接近Opus 5.5的创意输出。

M3.1 Flash Preview的意义就是把“够用的聪明＋Flash级的价格 ＋高推理强度下依然快＋稳定交付”拧成一股。拥有了能比拼旗舰模型的多模态理解能力，让M3.1 Flash Preview的价值又高了一个维度。

不过，M3.1 Flash在审美、前端设计上的表现，并不是凭空冒出来的。

MiniMax在这条线上早有铺垫，比如此前发布的MiniMax H3，这是一个开源的视频模型，一次生成就能同时产出画面与同步立体声音频，在人物口型、运镜和风格化上优势明显。

随后发布的MiniMax Design，则是围绕H3搭起来的多模态创作Harness，把广告投放、电商素材、品牌宣传、KOC 内容、短视频、Motion Graphic、3D资产到影视后期，全都接进了真实生产流程。

AI公司Genspark利用M3做了post train推出了针对ppt场景的slide模型，也佐证了M3系列在原生多模态理解和设计审美上的优异表现。

换句话说，“审美”和“把一件事做成片”本就是MiniMax的看家本事。

先在视频侧被验证，再沉淀进Design，如今延续到了语言模型身上。

最能直接落地的是品牌与广告。素材里那条“四格分镜→10 秒成片”就是典型。

一张故事板丢进去，成片由程序直接渲染出来。过去这是美术、动画、后期接力好几天的活，现在可以当天出片当天改。

同一条片子还能顺手切成十几个不同版本，先跑一轮投放，再决定给谁放量。省下的不只是外包费，更是决策速度。

再看产品与营销。

过去，一支几分钟的动画短片往往需要一个月的制作时间，还需要大量的素材。

M3.1 Flash Preview只需要纯代码就能做出Dribbble级的界面动效，还能按需批量产出，边际成本几乎为零。

M3.1 Flash Preview的出现，也是对游戏、前端这些需要交互和审美并存的行业的一次冲击。

一个人加一个便宜得多的模型，就能顶过去一个“美术＋程序”的小组，尤其是对独立开发者和小工作室，把原本请不起的外包，直接收进自己的Harness里。

再加上设计稿一键变可交互 demo、数据截图一键变可视化，从立项到交付的每一环都在被压缩，节省了大量成本。

这些加在一起，就成了M3.1 Flash Preview。

欢迎在评论区留言~  
如需开白请加小编微信：dongfangmark

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nn4fiaIib6wss7CnMmbakJUfKE6eQCVpGOyZtSLXiaAoqBg4bicEMQ150Q5xyL6PYvuoohJtH1TyG6HhbpjOyZdnelO2U0M3qbDU0G4ZB9qBBwQ/640?wx_fmt=jpeg&from=appmsg#imgIndex=11)

MiniMax · 目录