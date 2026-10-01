---
title: "阿里Qwen3.8-27B疯了：笔记本就能跑，能力却直逼Opus4.6"
source: "https://mp.weixin.qq.com/s/sStDNbM8GMlbSZFBl8iUWg"
author:
  - "[[路人甲TM]]"
published:
created: 2026-09-10
description:
tags:
  - "clippings"
---
路人甲TM 路人甲TM *2026年8月22日 22:56*

一个只有27B的模型，能有多强？

按过去的经验，这种体量的模型更像是大模型的轻量版：跑起来容易一些，能力也得跟着打折。

但Qwen3.8-27B出来后，这些天外网的讨论真是热闹非凡，我看得都替千问团队爽起来了：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/tp5fgmUBUbBmQZngQyKjqOjFPUU9OgAUdGM7dgYqA4FFvDxIWviaQVXvlrgZRXJvrx9EX7MibBq7Miatjnh8Uuj7fSNvCgiaKyo7GOoYgdANbvY/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

在AA榜单上，它拿到52分，和GPT-5.6 Luna Max同分。更夸张的是，在多项编程和Agent测试中，它也已经能咬住Opus 4.6 Max。

在推上更有网友把它称作是新模型的斩杀线：以后的新模型，如果体量比它大很多，能力却没有明显更强，就很难让人惊喜。

我觉得最吓人的还不只是性能这块，经过压缩后，Qwen3.8-27B可以装进普通的消费级显卡了。

用更激进的1-bit、2-bit量化后，竟然还有大佬把运行门槛直接推到了8GB级。当然，效果和速度会有所牺牲，但过去需要昂贵服务器才能体验的能力，现在离个人电脑已经很近了，这甚至可以算是本地AI的可用性拐点了。

简直是低配党的福音！

![图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbAia60KffWNS7KeCVy9UBZufn8sfezian5ic6PnSaANGIvEPJfABzPaZjlOv7wIwicIGHc6gp4vqSDyEibzomJczP80Dk7SnZw9yVHQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

说实话，我自己还从来没试过本地部署开源模型，但这次真是看得我开始手痒痒。

为了更完整地体验下Qwen3.8-27B，我还是不在自己的8GB小mac上折腾了。保险起见租了个云服务器部署上模型，跑几个案例大家一起看看这个看起来小得不太合理的模型，究竟能做到什么程度。

## 物理沙：先让规则跑起来

我给Qwen3.8-27B的第一个任务，是用原生HTML、CSS和JavaScript写一个遵循物理规则的落沙模拟器。大家先来看看整体效果：

，时长00:57

<video src="https://mpvideo.qpic.cn/0bc3f4cbuaaeuuagy3enorvfil6ddixqigqa.f10002.mp4?dis_k=a37cd89809566929f27d3c451778fa0c&amp;dis_t=1789027389&amp;play_scene=10120&amp;auth_info=MZS1x5p9QFZq4PO38VAgb2JACXJsFg5AJW0zWDdSSjkLZmo7RFRbGx0kN2oZPS1Pdko=&amp;auth_key=4e7acd4a030dd0b3611f4edf4d579a8f&amp;vid=wxv_4660734154375020547&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

这个还是蛮好玩的。沙子落下后会在障碍物上堆积，水受阻以后向两侧流动，沙子进入水中还会继续下沉。

酸液碰到沙子或墙体时，所在的格子一起消失。画笔支持连续拖动，也能随时暂停、更换材料和调整大小。

落沙模拟器能动起来并不难，难点在于让每一种材料都按规则移动。

我专挑了四个最容易看出差别的场景来逐项检查。因为即使效果能看得过去，有些细小的点得放大、减速才能看清是否真正遵循了物理规则。

我先检查了沙子会不会瞬移。正常情况下，一颗沙子每次更新只能下降一格。处理顺序写错以后，它可能在同一帧里被反复移动，肉眼看到的效果就是刚放下去便直接出现在底部。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/tp5fgmUBUbChRLnEI7adZeG7ul9bic9wvdu0QwQSCGCIOlq83icahAjq9qzyt8eqNC4WPe33PmGtgTCB3icOVFS5wetkHItgBWia6zbYBXN9lk0/640?wx_fmt=gif&from=appmsg#imgIndex=2)

沙子降落过关，再来看看水流是否会固定偏向一侧。

我在画布中央画了一道竖墙，再从墙的正上方持续倒水。水碰到墙顶以后，应当随机选择左右方向，最后在墙的两侧自然散开。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/tp5fgmUBUbCSSdBv2bnbiaa3IyjeJWMWW066VoASCsMf3ibL5ibib9gsuHAjfcmApWDpEDyf7fswcVq38cbtIXKH9fXuW23ABagOnwpEJCgut9s/640?wx_fmt=gif&from=appmsg#imgIndex=3)

可以看到水流是自然展开，没有长期偏向一边，过关。

接下来检查沙子和水的交换，沙子的密度更高，落入水中以后需要继续下沉，同时把原位置的水顶到上方。如果同一个格子在一轮里被处理多次，沙子和水就可能闪动或一次跳过好几格。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/tp5fgmUBUbDTeUZET5QoNGKhzMSawf80ltWE7FH0FFsUIdnvsqNynqVM3WiaicX9xCNjXLCNnxoS1SgYoTUyc7QpEyPVicF7mHYiblXar0bkSM4/640?wx_fmt=gif&from=appmsg#imgIndex=4)

可以看到一小块沙子从入水到落底，底部微散开，都符合规则。

最后一项是酸液反应。酸液碰到沙子或墙体时，只能溶解一个相邻目标，同时清除自己。它不能一帧吃掉一整片墙，也不能发生反应以后继续流动。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/tp5fgmUBUbA5ZFKKUYMtCxcmTUfmUfwUfibvzC60v7iaDP7f8I76MtYC6FH4vXjx0j1CI1FibW6X7AIvBj9XzXPr3XlQxBza30aGzb9bkLvGNU/640?wx_fmt=gif&from=appmsg#imgIndex=5)

能看到绿色的酸液先碰到沙再碰到墙，先后对两者侵蚀后消失。

这个案例重点看的其实不是页面视觉效果，而是模型能否把自然语言里的物理规则翻译成稳定的状态更新逻辑。

四项检查都通过，足以说明Qwen3.8-27B在算法理解、复杂规则遵循和完整前端实现上都做得比较扎实。

对一个单文件、零依赖的小项目来说，完成度比我预期更高。

## PDF建站：把一份产品手册变成品牌官网

第二个任务，我给Qwen3.8-27B一份虚构的家具品牌产品手册，让它把PDF里的品牌介绍、产品图片和商品信息，重新做成一个可以直接浏览的品牌独立站。

先看几页我给的产品PDF：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbBLsibfKtM8CdnmuPQWIaLdYCqsiadcV6h9uuevhRrgibomAXgvOgRKfIRgQC5cH59crIFpZ1J5ZYFgW0xiaZNDXPoBPSv0ft6JSX8/640?wx_fmt=png&from=appmsg#imgIndex=6)

这项任务首先考验的是模型的多模态文档理解，要从PDF里识别并整理我给的9件商品的所有信息，再把它们正确对应到网页中。来看看最终生成的网站：

，时长00:48

<video src="https://mpvideo.qpic.cn/0bc35abp2aaclqaiwmul6fvff2gd7xuaf7ia.f10002.mp4?dis_k=ed6300c08458ee29b22693cb053c30b7&amp;dis_t=1789027389&amp;play_scene=10120&amp;auth_info=YNiG7P18EAJiuvu//FAuPD5ACXZsE1xKdTpkWTVWEWxaND4/E1ULTxV+P2IUPSMcKko=&amp;auth_key=1aed0a5a957e2b9e04b13dffdb1c11e7&amp;vid=wxv_4660734847777439746&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

从整体效果看，它没有把PDF的内容很机械地一页页搬到网页上，而是重新组织成了更符合独立站阅读习惯的结构：

首页用品牌口号和客厅场景建立氛围，再展示精选系列和全部产品，后面补充品牌故事、材料工艺和服务信息。

原本分散在不同页面里的内容，被整理成了一条完整的浏览路径。

而且网站也不只是一个静态展示页。我们可以看到产品能按类别筛选，点击卡片会打开包含完整规格的详情弹窗，还可以把商品加入购物袋、调整数量并自动计算总价。

能做到这么细节确实挺出乎我意料。

这个案例真正考验的并不是单独的PDF识别或网页生成，而是模型能否连续完成信息提取与对应、网页结构规划，再进行视觉设计和前端代码生成。

从结果来看，这条链路基本被完整地接了起来。

## 地牢爬行者：随机生成一座真正能探索的地牢

最后一个案例，我让Qwen3.8-27B用一个HTML文件做成一个可以随机生成地图、自由探索并带有战争迷雾的地牢小游戏。

先来看整体效果：

，时长00:34

<video src="https://mpvideo.qpic.cn/0bc3qiaoiaaapeaje44janvfbawd4sbabzaa.f10002.mp4?dis_k=c1e0a8c6761f16457dff8a4a5a3c9f41&amp;dis_t=1789027389&amp;play_scene=10120&amp;auth_info=Nvu8ha4oE1Nquv2w/lRwaG1GBSM6RwxLJ21nXGFWEWYMYjg5RgYIHh1+OW0WOX1IeUw=&amp;auth_key=2a0b2da72b13383e742417b41daf8eb1&amp;vid=wxv_4660736041627418630&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

看起来只是一个简单的像素小游戏，背后其实要同时涉及地图随机生成、房间与走廊连通、角色碰撞和实时视野计算。

尤其是迷雾的设计，不能只在玩家周围画个圆，还要保证墙体可见、墙后的区域继续保持黑暗。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/tp5fgmUBUbAJKZMS1XQiaPDTpUa4ExXtIygQ8q867ybOwmF75NgCloYNfFcpWkgreH074Gr8I1eibILx8dNkj0icDgGwic2cWGtzibsicy3vbm82E/640?wx_fmt=gif&from=appmsg#imgIndex=7)

每次点击重新生成地图，房间的位置、大小和走廊也都会发生变化。不是会简单换一张预设地图，而是先把60×60的区域切分成多个空间，再生成房间并用走廊连接。

地图完成后还会进行一次连通检查，确保玩家不会出生在一块走不出去的孤岛里。

我比较惊喜的是Qwen3.8-27B这次也是一次就产出了这个结果，还把我给它的规则都实现得比较完整：每次都能生成不同且连通的地图，角色不会穿墙，视野会随着移动自然展开，走过的区域也会留下探索记录。

从这个案例，我主要是想测测模型的算法理解、空间计算和完整游戏开发能力，虽然只是一个demo式的像素小游戏，但是足以展现它的确有做出一套真正能够运行的探索规则的能力。

## 小模型，真的能办大事吗

这是我第一次自己部署开源模型，过程并没有想象中顺利。

从安装环境到把Qwen Code接上模型，中间踩了不少坑，后续也可以专开一栏给大家分享一下。

真正开始跑任务以后，速度也谈不上快，这几个案例都跑了大几个小时。

但真正让我意外的是结果。三个案例都是一次产出：物理规则没有乱，PDF里的内容被完整变成了网站，随机地牢也确实能生成、能探索。

尤其让我惊喜的是前端能力，它不只是会搭出一个好看的页面，还能把完整的算法、交互和细节一起补齐。

这正是小尺度模型最吸引我的地方。

它不一定在每一项上都比顶级的闭源模型更强，运行速度也有很大提升空间，但更小的体量意味着更低的部署门槛、更少的硬件成本，以及把模型真正放到自己设备上的可能，使大众离本地AI可用性更进一步。

这也正是Qwen 3.8-27B最有杀伤力的地方。它未必全面超过Opus 4.6了，也不需要如此。

但只要一个27B模型已经能把这些任务做到这个程度，那些体量更大、成本更高的新模型，就必须拿出足够明显的优势，才能证明自己值得。

所谓新模型的斩杀线，大概就是这个意思。