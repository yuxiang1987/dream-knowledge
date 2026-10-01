---
title: "还在靠抽卡做视频？我用updream预演台告别抽卡"
source: "https://mp.weixin.qq.com/s/PjTgkaflEG1nnzRzMg-2Yg"
author:
  - "[[路人甲TM]]"
published:
created: 2026-09-10
description:
tags:
  - "clippings"
---
路人甲TM 路人甲TM *2026年8月18日 20:37*

最近迷上了惊悚题材的短剧。

红果上这类内容特别火，主角进副本、闯关、死了重来，一集几分钟，看得人停不下来。

刷多了就想自己也做一段试试，于是写了个本子，叫《回档后，我成为惊悚之神》。

主角林渊在医院醒来，血月挂在窗外，手背上浮着一串倒计时。

他很快明白过来，自己被困在一个惊悚副本里，死一次就回档一次，同一条走廊要反复跑，每次走法都不一样。

他得在倒计时归零之前找到出口。

本子写完我挺兴奋的，觉得这个设定很有画面感。

结果一动手就卡住了。

最难的是走廊那场追逐戏。

林渊在前面跑，裂口护士在他身后追，我要的是镜头跟在他侧后方，画面里既能看到他的狂奔的表情，也能看到身后越来越近的护士。

提示词写了几百字，抽了几次，出来的东西和我设想的还是有一些区别。

光靠提示词，人物的精准走位控不住，机位和运镜也调不准，群像的空间关系更是全靠抽卡。

后来我试了updream的预演台，用白模先把镜头和走位定下来，这几个问题才算解决。

先看看最后做出来的效果：

这段就是用预演台做的，下面说说整个过程。

### 上手：一张图生成3D场景

先说下预演台是干什么的。

你上传一张场景参考图，它自动解析空间结构，生成一个带深度信息的 3D 白模场景。

然后你在这个白模里摆机位、调运镜、拖人物走位，录制完之后白模视频直接回到画布，接着就能作为参考送进模型生成。

整个过程不用在几个软件之间来回导。

我传的是一张医院走廊的图。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbCQ635AiaG0YJUiclkGwsaZiciaviav7csQlbqR5YnTA3cJz9uvOnOicLcjVuiaLgVLlcqxSn7wZpc5FV62umYAkH6l4icfUjBwEibdmexA/640?wx_fmt=png&from=appmsg#imgIndex=0)

生成出来的白模还原度挺准的，走廊的纵深、两侧门的位置、天花板的高度，跟参考图基本能对上。

一张图直接出 3D 白膜场景这件事，我目前没见到别家做。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/tp5fgmUBUbDoQCIZVrLRnqvFGBtd6eTWS6Cjicv2LDKIuxMvKFPFbC1OqY5RqnIFAZGOZmj2VJQncFbBVme4RPeUF1ibKARWp12RH1h1xTGhU/640?wx_fmt=gif&from=appmsg#imgIndex=1)

真正花时间的是后面。

摆机位、设运动轨迹、拖人物走位这些操作，第一次用需要熟悉。

我前后花了两三个小时才算摸顺，中间翻了几次官方教程。

所以这个东西不算开箱即用，得先给自己留出学习的时间。

但两三个小时换来的是后面每个镜头都能自己定，我觉得这个投入是值的。

场景搭好之后，接下来就是看白模能控到什么程度。

我就从最简单的开始，一步步往上加难度。

### 第一组：静态白模

先从最简单的开始，只用白模定住空间和站位，不做运镜。

我做的是林渊在病房里醒来那一场。血月在窗外，人坐在病床上，这个镜头的关键是人和窗的位置关系。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbBdsWmE8AzEUuKhcmvykaNDKISZNok8X07cTJGCDK9vibeF5EB5pL2AzauMSeV3YtziauczbUvTfweB2xuz5RSZtQqORvD4z0fcg/640?wx_fmt=png&from=appmsg#imgIndex=2)

先把参考图丢进去，生成白模场景。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbDIz3iafoMFLdGV5S9PpSweews2dywXUfSTeBa2xBuicR2mc6DEiaHd2msfbGHJefOJviawcscGCLicltH1kyrz3Ex7IL1ibrrqic4sx8/640?wx_fmt=png&from=appmsg#imgIndex=3)

场景搭好之后，我在里面摆了三个机位。

先是全景交代环境。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbCqpAIlbQ0T2xb5HK5RbzbtXlubqRia3vqMQ0ss3MBVsS4JyyJaBgohRR22wloND1fml4tcriclpWAxzu461yiaI0T7nd4AVDP73A/640?wx_fmt=png&from=appmsg#imgIndex=4)

一个大特写给惊醒的瞬间。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbAwxoYygpOsPJfkU6ibsWdjmfnDxNFYW8kvVSZomxibYLIM2SkfkVx343V4AZHxt3wbfpeiaictwiaRkWyOchYdTU15esFDxwOic6nBs/640?wx_fmt=png&from=appmsg#imgIndex=5)

最后一个近景带出人坐起来的固定人物和床的位置关系。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbDcykxHAibx2tSaUziaAgPQSLuLqGP0Lpo9zEVKZZCp35ns5buYjGSIp94RdXAk9rpZYj0npHxKpkbm2C9D0GCcJxS35Ric4P4KO4/640?wx_fmt=png&from=appmsg#imgIndex=6)

看看效果：

几个机位都很准确，而且人物固定之后人物不会乱切位置。

这里能看出白模的一个好处： **场景搭一次，机位可以随便摆，可以多次利用** 。

三个机位如果用提示词写，等于要写三遍场景描述，还得指望模型每次理解得一样。

实际情况是很难一样的，三个镜头切在一起，观众一眼能看出不是同一个空间。

我也用纯提示词的方式做了两次，拿了一个还不错的版本

还是存在一些问题，提示词已经限定死了主角坐在床上，切一个镜头有时候坐在床上，有时候坐在床边，会有一定的割裂感。

白模是把场景先定死了，机位只是在这个空间里换个位置看，前后自然是一致的。

再说个更根本的问题。

你写的提示词，模型不是直接读的，中间 AI 还会润色一遍。

按下生成之前，没人知道模型最终读到的是什么。

白模不需要翻译。人在哪、物体在哪、什么遮挡什么，都是我自己在 3D 空间里摆出来的。

静态能定住，那加上镜头运动呢？

### 第二组：简单运镜白模

这组我做的是一个过肩镜头，从林渊背后慢慢往前推。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbBECT40zfjmqqZiaISqtibnfDPbI2ibuGkjReMFib4D6nJ0PCibgE6JxUFvswOMyq3v80FVeGdCPxDSuruwCRDStOqarVA3rtq7ETm4/640?wx_fmt=png&from=appmsg#imgIndex=7)

推移的起点、终点、速度，都在预演台里拖出来。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/tp5fgmUBUbBMGx7icH01IJibLicz2Tn0ibRBHYzlnc4sUpmD6OTRaFuCuqiaz1EL55db4G3nVtrlpRqPSyuvjDFT8o0cXHuh4lIFCQpy4NjbJssE/640?wx_fmt=gif&from=appmsg#imgIndex=8)

看看效果：

推镜的速度和人物保持的距离基本上都和我做出来的白模一致。

不过这种简单运镜，说实话提示词也能控得差不多，我平时就是这么干的。

真正难的是复杂运镜，以及让白模多机位切镜头。

### 第三组：复杂运镜白模

这一组是真正的难点。

我要做的是走廊追逐，十秒，中间有三次机位变化。

前两秒是俯拍，从高处慢慢推近到林渊的面部特写，要拍出他的惊恐。

第二到第四秒切到过肩镜头，跟着他的肩膀平移，把身后的裂口护士带出来。

第四秒之后进入追逐，两个人一前一后往前跑，距离一点点缩短。

这段的难点有两层，一层是运镜本身复杂，俯拍推近、过肩平移、跟随追逐，三种运动接在一起。

另一层是切镜，在人物运动的过程中换机位，还要保证换完之后空间关系不乱。

先看不用白模的版本。

我跑了四条，这个是相对比较满意的版本了。

问题出在追逐那一段。镜头跟着林渊跑，但身后的护士基本看不见，画面里只有他一个人在往前冲。

没有追的人在画面里，紧迫感就没了，看着更像是一个人在走廊里跑步。

惊悚戏最要紧的是被追的那种压迫感，而这个压迫感是靠你能看见它在你后面，而且越来越近给出来的。

这一点提示词很难描述准，模型不知道该把护士放在画面的哪个位置、离多远、什么时候进画。

然后是白模。

我在预演台里把三段镜头依次设好。

第一段机位从高处压下来往前推，第二段挪到林渊肩后做平移，第三段挂在他侧后方跟随。

两个人物各自拉出走位路径，护士的速度设得比林渊快一点，跑起来距离会自然缩短。

丢给模型生成，出来是这样。

三段镜头和白模里设的基本一致。

俯拍推近的落点、过肩平移的角度、追逐时的跟随路径，都对得上。

最关键的是护士的位置。

她一直在林渊肩膀后面，清清楚楚地跟在画面里，而且距离在缩短。

之前那个看不到人的问题解决了，被追的压迫感也就出来了。

这条我很满意，一次就成了。

### 跑完之后的几点体会

白模参考早就被验证过了。

ControlNet论文里明确指出纯文本难以精确表达空间布局和人物姿态，Seedance 2.5官方也强化了白模理解能力，还出了一套白模提示词规范。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbBfyqMqOSWq41QPXypMibAAIam9dGBlrFrSZGae5w4aon0rcGStXJNRxUmSK0HKetHvicjIRyo5ibTamXowQAQ51ezVdRzofcrA0Q/640?wx_fmt=png&from=appmsg#imgIndex=9)

问题是以前想用，要么学Blender建模，要么在ComfyUI里搭节点工作流，学习成本几个月起。

这也是为什么明知道好用，大部分人还是在硬写提示词。

但是预演台把这套流程搬到画布上，两三个小时就能上手。

Seedance 2.5生成一条30秒视频大约70块，一个复杂镜头平均要抽2到3次。

我这次加了白模的基本都是一次成片，没白模的对照组，基本上最少都要跑2-3次，最后那条也只是相对满意能用。

但白模作用不是让你不抽卡了。你把镜头、人物轨迹、人物位置固定住之后抽的次数会明显少，该调的还是得调。

白模上手使用有一定门槛，摆机位、设轨迹这些要先花时间熟悉，但是相对Blender 3D建模工作流，动辄两三个月的学习成本已经好很多了。

另外白模只能定空间和运动，人物长什么样、场景什么材质，还是得靠提示词和参考图控，两边要配合着用。

### 写在最后

做AI视频这一年，前期大家比的是画质，谁生成的画面更清楚更好看。

现在画质基本被模型解决了，开始比的是控制力。

同样的模型，同样的提示词，有人能把镜头做成自己想要的样子，有人只能一遍遍抽卡碰运气。差别就在能不能把脑子里的画面精确地交给模型。

白模是目前最有效的交付方式，预演台把这件事的门槛从几个月压到了几个小时。

updream现在有个千万积分预演台挑战赛，用白模创作可以参加，感兴趣的去看看。

我是路人甲，前数据分析、产品人，现创业者。关注AIGC人工智能，分享实用的AI应用。让AI变成你触手可及的生产力。