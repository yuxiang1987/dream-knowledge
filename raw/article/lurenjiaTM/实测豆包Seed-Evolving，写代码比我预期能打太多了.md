---
title: "实测豆包Seed-Evolving，写代码比我预期能打太多了"
source: "https://mp.weixin.qq.com/s/X_4EGbWcS6vdP_y6tmPGQg"
author:
  - "[[路人甲TM]]"
published:
created: 2026-09-05
description:
tags:
  - "clippings"
---
路人甲TM 路人甲TM *2026年9月2日 10:52*

近期在做很多模型测评的时候，评论区都会零星有人提到字节的Doubao-Seed-Evolving模型。好几个人说能不能测测这个模型，感觉它coding能力还挺强的。

起初我也没咋在意，但是近期，我又听到了同事和我推荐这个模型。

于是我就花了不少时间去测了这个模型，结果不测不知道，测了才知道：这玩意还真能打。

这个模型只有一个版本号，接入时使用同一个API key统一调用Doubao-Seed-Evolving，在模型升级时就可以自动实现升级。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbBSND8KJjhiayuOW2FPRJVe1H8jMru71pdNgueDT9CUjHUGVNhYWa02UJMSTfoI4Qia4bVBx0obq3ibye1jj9new4kGxDx8Hq18wk/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

我去看了它最近的几次更新，不得不说迭代频率挺高的，也不是挤牙膏。就比如最近的几次更新就有⽀持1M超⻓上下⽂、⻓程任务能⼒提升和VLM视觉检索能力显著增强等。

这次测评，我测评了很多案例，重点做了一个知识图谱和推理游戏，发现他对长程复杂任务的处理能力和稳定性都很棒。

那效果究竟如何，接下来就让我们一起来看看吧。

## 一、根据史书做一个知识图谱和wiki

前段时间在GitHub上刷到了一个将史记做成可交互、可探索的知识图谱的项目。

其实我一直对历史很感兴趣，但是受限于正史中错综复杂的人物和国家关系以及枯燥的描述，我对历史的了解和学习一直只停留在高中课本和偶尔看到的历史事件或者人物的科普视频之中。所以我也想复刻一下这个项目。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbDeSWLUaQ9HGnbrIRMX4ovf2h9TEQpYzfdLsol7vMbcfvG5cPP8CdsBrrGszGxv0JHcouoPiaZ081M5mq1CRFhELqPXEpMaPF2Q/640?wx_fmt=png&from=appmsg#imgIndex=1)

史书知识图谱这件事，其实挺难的。

因为模型不仅要从大量文本里识别人名、政权、地点和事件，还要理清人物之间的关系、事件发生的时间，以及同一个称谓在不同上下文里到底指向谁。更麻烦的是，它面对的不是几段孤立文本，而是一整本史书。

这既考验长文本阅读，也考验模型能不能在一个漫长的任务里始终记住目标、保持一致。

所以我干脆把原项目的代码仓库，连同一整本三国志，一起丢给了Doubao-Seed-Evolving

我就想看看，它能不能先读懂这个项目过去是怎么处理问题的，再把这套经验复用到新的史料上，最终独立完成从文本解析、实体识别、关系抽取，到知识图谱构建的整套流程。

说真的，我也不知道它能不能行.

经过了近八个小时的全力运转，任务完成了。先来看看成果。

，时长00:38

<video src="https://mpvideo.qpic.cn/0bc3hqc5eaaf7eak3rmsx5vfkpgd2i6aluqa.f10002.mp4?dis_k=6dd79cabfd93b3b662de6f88bc958e4c&amp;dis_t=1788571272&amp;play_scene=10120&amp;auth_info=KeHHxo4GKAJlz6WMylJxYhFqbRk5ZTgZbn4ZZUUbImkTGk11LS4zTxILYVEiP3xCBWA=&amp;auth_key=d8b5351e6113b95ffe920630b24a20ec&amp;vid=wxv_4676166957396918279&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

整体效果比我预期中好不少。

在传记原文、人物、事件和地点页面中，需要识别的实体都完成了标注。点击任意实体，就能跳转到对应页面。搜索功能也支持按照人名、地名、事件和原文词句进行检索，并自动标出相关内容。

它不只是搭了一个Wiki外壳，而是把整本三国志都做了一遍结构化处理。

全书共65卷，合计2149段陈寿正文，已经全部完成结构化处理。经过合并和去重后，最终整理出1944个标准化事件和2151条跨传记载。

其中，88个事件能在两篇以上的传记中相互印证，39个事件拥有三篇以上的记载，还有17个事件出现在五篇以上的传记中。

更重要的是，对三国志全文都实现了逐字保留，抽取出来的人物、事件和关系也都能回到原文核验。

人物部分则建立了2265个人物实体和2727条人物关系。最终生成4312个Wiki页面，包含各种专题页面和知识图谱。

不过在知识图谱的构建方面还是有一点小问题，由于实体很多，知识图谱的可视化经常加载失败

![图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbDXGyITVntEKY5beWKH5w9gYPUibhJ2XGgxK5lfgP1iadz8nYCQrSgI9aAYSJo7TK9lg5DTiaf1DSSlTZsqpXIOgN3KxGicPxs3fSc/640?wx_fmt=png&from=appmsg#imgIndex=2)

于是我把问题又重新交给了Doubao-Seed-Evolving，让它帮我进行优化。

，时长00:21

<video src="https://mpvideo.qpic.cn/0bc3uia7iaabk4aiw5ewyfvfdiwd6srad5aa.f10002.mp4?dis_k=80ae94253a2fd2af7cff16395134de4c&amp;dis_t=1788571272&amp;play_scene=10120&amp;auth_info=a8755wF4VTXKoo+aBX9pSjxlHzVkaU47Ik0zGUF3OUBNFXQpeWMYQg5mUnJockleNg==&amp;auth_key=7d412dfca1bf68688a4f691d47db1266&amp;vid=wxv_4676167755606523904&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

不一会修改好的版本就出来了，知识图谱中包含有三种节点类别：人物、事件和地点，两者之间的有向连线上还标有两者之间的互动。

很难想象这么长时间且复杂的任务中间仅停止过三次，一次是询问我是继续进行第三批的处理，还是先看初期成果。

第二次是电脑休眠让任务中断了这锅确实不该Doubao-Seed-Evolving背，不过连上网之后模型还是可以丝滑接上之前的任务继续处理。

最后一次是同时有十个agent运行产生的交通堵塞

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbDOUiciaTkejtB5gGibq9z0TGWnGIqclkZzZn74BeOQfQoo04bzHd7ttKicwtqgouiaHhIkpadsMKcI9pjaxMKxvqHehzIM1BFAHZs8/640?wx_fmt=png&from=appmsg#imgIndex=3)

整体看下来，八个小时的长程任务，异常的中断次数只有一次，还不错

那再来看看这个项目的实现过程是怎么样的

，时长00:14

<video src="https://mpvideo.qpic.cn/0bc3a4abeaaabqajeuexhnvfab6dcidqaeqa.f10002.mp4?dis_k=92cd946b062816a129bc5dacb016eece&amp;dis_t=1788571272&amp;play_scene=10120&amp;auth_info=f8qa/9ICKwVhxKOKyVAoORE5ZRpkZW8fYSgeNkVMdWlFSEZ+fiswSBYAZ1chPSUZBTM=&amp;auth_key=4765e9f8f2eae526d0220f108780b0eb&amp;vid=wxv_4676168136717418498&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

在这个阶段我给模型的输入中甚至没有包含文件，我让它自己扫描我的电脑找到要求的文件后，按照我拷贝到本地的仓库结合三国志自己判断可以复用的Skill、代码和处理流程。

让我惊喜的是Doubao-Seed-Evolving还根据原有的skill按照实际需要进行了修改，后续就可以把跨传事件关联和史料冲突判断等认知任务交给Skill处理。

还有一个比较值得说的点就是Doubao-Seed-Evolving的结果检查能力

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbBOibVd71FB7pic4DTArr57ZgE6ibqcLQgAz5UicuDW5rZ1kEdD0icSWkia33WgBK9SNmPX54GcV0OicqzoY6qr5K8mTa9Q0tP0cVAT9s/640?wx_fmt=png&from=appmsg#imgIndex=4)

虽然划分了很多的子agent并行多个任务，但是对于每个完成的任务都会按照最初制定的标准进行判断，合规之后才入库。

全部任务跑完后看了一眼后台，零零散散用了快3亿token，缓存命中率还能保持在94%以上，不错不错。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbC1mwdMN7zV6mhk8iaV5TvKvjT03rsEiaSmnuPrIx0aHe8pj5iaN4xN1ic6Cjcu7uia9Qibolfyx2O1mkIe7AHKiaEsiaBdUQV3SAQibC6g/640?wx_fmt=png&from=appmsg#imgIndex=5)

## 二、一句话生成一个网页推理游戏

看过我K3那篇文章的朋友都知道我是个推理小说迷，最近又了解到一种ARG替代现实游戏，简单来说，就是一个网页解谜游戏，不过这个游戏需要让玩家模糊现实和虚拟的边界，也就是说效果要很真实有代入感。

所以这种游戏的制作是很考验模型的前端能力和推理能力的。

我就把这个作为给Doubao-Seed-Evolving的第二个考题：

先是一句话让它帮我生成游戏方案。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbA7jYsXibf3Jb3clP4KmCxHIGJkoKWEFt27zBk52RwhiazIQYSJ44RLwxMvyTHFlwPskckPNicaVtwHkRFN8ulbPlicVySAMRw0tSE/640?wx_fmt=png&from=appmsg#imgIndex=6)

它很快给出了一套游戏方案。一款让玩家穿梭于新闻、博物馆、手机多终端多网页，寻找线索、破解文物失窃案并营救失踪女友的网页ARG

这个阶段最直观的感觉是快，不到十分钟，它就把博物馆、论坛、终端等网页一起铺开了。

第一版页面也能用，但不太像现实常见的网站，没有真实感。可能是模型手里没有明确参照，信息泛泛，生成的画面一眼就是很AI

所以我后来把国家博物馆官网拿给它看，让它照着重做博物馆部分。改完以后的网页明显更真实。

，时长00:14

<video src="https://mpvideo.qpic.cn/0bc3aaclyaaetqadzwutwbvfiagdxqaajpaa.f10002.mp4?dis_k=a632086c7446cbde6cb9886de6dbbc96&amp;dis_t=1788571272&amp;play_scene=10120&amp;auth_info=eMOZ7MJWLlFlnqPQxAx/PhY/ME5jYzVMOSxOYExAdWhCSkBwLH81HBJaZw0sYXIeAjU=&amp;auth_key=65c0661e14e4236e9d7536c8f76589c6&amp;vid=wxv_4676170562669592577&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

这么一看模型其实能看懂网页什么最重要，尤其是是这个模型，视觉能力也表现不错。

所以后面为了更具有现实感，我直接导入一批参考素材图，让它基于此进行膨胀，生成了完整的游戏。

入口是一张建邺晚报。头条写文物失窃，实习生林晚仍然失联。

玩家点开她留下的手机，从短信里看到她失踪前的最后几句话，再去相册找第一次约会的日期。日期倒过来以后，可以登录博物馆内网。

，时长00:50

<video src="https://mpvideo.qpic.cn/0b2ej4ajoaaaruabouux6vvfat6ds5hqbfya.f10002.mp4?dis_k=d8c5e51143e8480f9eae2fd7ec2fb24b&amp;dis_t=1788571272&amp;play_scene=10120&amp;auth_info=e73cpq4KelJqmKCMzlItbRZqZkpjMjgYPCIeZxlNcjpBTRF+eyVhHx1cZFEmPyBNAmA=&amp;auth_key=d8f455b3e5b9a286aba87f57c5431af5&amp;vid=wxv_4676171201462091785&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

打开内网，我们能发现还连着许多其他页面。每个都可以打开，风格也各不相同。

但是这些页面各自能打开还不够。玩家在一个页面发现的数字线索，到了另一个页面必须还能用；发现的证据会有所记录进而影响到其他页面，更有甚者，影响一长串网站状态。

页面越做越多，1M的长上下文保障了模型仍能继续处理同一批人物和页面依赖，我不用每次都把整个故事重新讲一遍。

对于复杂项目，这种能在同一件事上持续工作很久的能力很有用。

但是大窗口依然会漏细节，这个问题后面很快就出现了。

比如说监控回放只有黑屏，没有视频。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbBIiaULp8CXjBJxoicVpqm9711EfW62qV5qH4SICmk8ictAkgvN10mzusY1dtfChTpibVjGibwvrJt0sWt2olMEhibZnUlicblgX7USbw/640?wx_fmt=png&from=appmsg#imgIndex=7)

我就直接截图给模型让它修改。

很快就修好了，黑屏消失，原视频出现了。

，时长00:15

<video src="https://mpvideo.qpic.cn/0bc3kaa7caabluahaamwyrvfcugd6fiad4ia.f10002.mp4?dis_k=aa0bfa67bf15b00d2666aa1ea6fed9a0&amp;dis_t=1788571272&amp;play_scene=10120&amp;auth_info=LfS+36gAelBhy/ffnVV4PxI/MkllOW1KOXtNMBoZdTwXGEVzLS1hHRYPMwJ1OHUfBjU=&amp;auth_key=efb15472eecfa2daae5ca7e33ed9416a&amp;vid=wxv_4676172453109252096&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

这样子的修改大大节省我们和模型battle的时间，不要废话，直接甩图。

毕竟只看代码，模型可能会说视频已经存在。看过截图以后，它才能意识到视频位置虽然存在，却还是没有出现。

再比如，一些细小时间点的错误。

最终设定很简单。今天是2026年8月11日，失窃发生在7月24日凌晨，林晚失踪至今18天。

在整个过程中模型曾经把今天写成8月29日，也把案发日和当前日期的前后关系弄反。我连续提醒了两三次，模型才把新闻日期，手机日期这些统一。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbBzicVUz39EQkicibBNFxrbyax1JGbIpayicZjRShgLqPAfEcQUY07sDicSwyMqiaEg2GKXmjsptHBjn3EV75Sc2HDDndHNoE9SIRwcs/640?wx_fmt=png&from=appmsg#imgIndex=9)

这正好说明了长上下文的边界。窗口很大，可以装下很多文件，但是不代表模型会在一次要求完成后，自动进行全局检查。

所以如果项目里有日期、金额这些数字，我建议以后会把它们单独整理成表，每次改完跑项目，再走一遍表格进行核对。

靠模型在长对话里自己记住，风险还是太大。

然后3D是这次最明显的短板，视觉效果明显没有跟上。

，时长00:21

<video src="https://mpvideo.qpic.cn/0b2ejyajqaaao4abtn4x6nvfatwdtbhabgaa.f10002.mp4?dis_k=a77a62e856fb520a1e4dadaf4de63409&amp;dis_t=1788571272&amp;play_scene=10120&amp;auth_info=bZPLkDt4BDLMpN2YVS07FT0wSTczOEphe0plHU5xbk1LQiAtKGNJRQhgAHA4IBsBNw==&amp;auth_key=037a84d8ecffa3e4109b7be08d2ca9d0&amp;vid=wxv_4676173197564805127&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

展厅主要由很简单的几何体组成，灯光压得太暗，墙面、展柜和地面缺少真实材质。

如果不是游戏提示身处博物馆三号厅，眼前更像一间还没来得及布光的测试房。

这块和我之前测K3的差距很直观。所以我同样拿一句话让K3重新帮我设计了一个3D展厅。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbCxEP47T02Z79lKicfxNhNibSulrgiagPwszIm4rTbCSegKHVyPwZtKC0Eh92GYB8wg9Iy22GmGSdtRrWAlvZO3DkOLBoMn8F3yQE/640?wx_fmt=png&from=appmsg#imgIndex=10)

结果很明显，整体布局结构都会更合理一些。

，时长00:26

<video src="https://mpvideo.qpic.cn/0b2ewaajeaaa4uabgd4xhzvfbmgdskyabeqa.f10002.mp4?dis_k=e11c762668a521eaca8d9c9544e8fb38&amp;dis_t=1788571272&amp;play_scene=10120&amp;auth_info=ebTftZIAL1UwnPmNxVdwb0c9MRRnYj9CPStMMUtOcT1DRhVzfSw0GEdYPVAtOn1PUzc=&amp;auth_key=e212b10a9ec128d5f6ab6a4a1050f0d6&amp;vid=wxv_4676173664055492611&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

Doubao-Seed-Evolving能把3D场景搭起来，却做不到只靠几轮自然语言就把它打磨成一个有说服力的3D展厅。想要更好的结果，仍然需要专门的模型参考进行反复调试。

## 三、让模型查清一个行业首创

前面两个案例主要测的是Coding和长程任务能力，最后我又给Doubao-Seed-Evolving出了一道完全不同的题。

事实核查。

事情是这样的，苹果发布iPhone 14时，说自己的卫星紧急求救服务是智能手机行业首创。但华为Mate 50明明早一天发布了北斗卫星消息，这算不算苹果吹牛？

为了增加难度，我还丢给它12篇有标题党嫌疑的媒体文章，以及苹果、华为的官方材料，让它自己搜索、判断和交叉验证。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbDpr4W0ZkibB7V7lkM3NicFlg38Qqwic4x5vxacjZCTOjLOaC9uRIKLgWJC0013kTshGBGToqX52Yrr55khZt2HiatJbMzjzt2XKsQ/640?wx_fmt=png&from=appmsg#imgIndex=11)

这次任务前后跑了半个多小时，调用了五十多次工具。从Apple官网一路查到Globalstar提交给SEC的文件，最后给了我一份挺完整的报告。

，时长00:13

<video src="https://mpvideo.qpic.cn/0b2emaagoaaauyaomxexffvfaygdm5qaazya.f10002.mp4?dis_k=5fef223e7643b00ad226c6fd54aaa544&amp;dis_t=1788571272&amp;play_scene=10120&amp;auth_info=eMeRxsMGelU3z/PfnwIvPkY9NU1gNThObXwYNE5KcG5CSEB1LS1hGEALNwJ3byIeUjc=&amp;auth_key=a888c5fd2a90680c8f8750fd9bf7d95e&amp;vid=wxv_4676175564209225729&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

它做得最好的一点，是没有掉进谁早一天谁就赢这个坑。

事实上这是两个截然不同的服务，苹果解决的是出事了怎么叫救援，华为解决的是没信号了怎么给熟人报平安。

它甚至还能反过来检查我提供的文章，发现其中一篇把iPhone写成只能发不能收，和Apple官方资料直接矛盾。

看到这里，我觉得它还挺能打的。

但我后来逐条复核，还是发现了一些问题。Mate 50明明是9月21日开售，它写成了9月28日。华为在9月21日就启动了北斗卫星消息众测招募，它却把开放时间推到了11月。

不过它虽然使用了这个错误的时间，却还是在文末作为仍无法从公开信息确认的事项列了出来

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbD0HLWLF1e65LiampxmicuspeEOt0QWlCo49p6D711jxJUDicfOAD7XEJoIa5o2ibDN4Y024JO8GtAaia8B0iaapJEOQVO3VMC3EkLoA/640?wx_fmt=png&from=appmsg#imgIndex=12)

既然标注出来那也可以原谅

所以这次测试给我的感受很有意思。Doubao-Seed-Evolving确实能搜索大量资料能识别不同来源之间的冲突并对未确认的信息做出标注。

其次模型幻觉也很少，我看了好几遍报告我给它挖的坑就只发现了，它一边承认自己没有查遍全球所有小众设备，一边又非常肯定地说苹果就是全球第一个。

没找到反例，和已经证明全球第一，中间还是隔着一条河的

当然就先使用了错误的信息再到文末进行标注的做法我很不喜欢，要是我没看到最后呢。除此之外整体感受还是不错的。

## 写在最后

测了这么久，回到最初的问题：Doubao-Seed-Evolving到底能不能打？

我的结论很简单，能打而且还挺好用。

这个模型给我印象最深的就是它的长程任务处理能力，能在一个复杂项目上持续工作很久。

无论是处理整本三国志，还是维护多个相互关联的游戏页面，它的长上下文、任务稳定性和截图修Bug能力都很实用。并且只有一个持续更新的模型版本，也省去了反复选择和迁移的麻烦。

到了最后的事实核查测试中，它又证明了自己搜索、交叉验证以及较强的抗幻觉能力，甚至能发现我提供的文章里存在错误。

当然，它也不是没有短板。

在多个agent多任务并行时，任务可能会中断速度也会变慢；3D场景的基本框架已经搭起来了，只是在材质、光影和空间氛围上，还需要进一步打磨。

但如果你要做的是文件多、流程长、需要不断迭代的复杂项目

Doubao-Seed-Evolving确实值得试试。

我是路人甲，前数据分析、产品人，现创业者。关注AIGC人工智能，分享实用的AI应用。让AI变成你触手可及的生产力。