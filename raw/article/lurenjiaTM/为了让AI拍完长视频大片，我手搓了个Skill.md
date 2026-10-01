---
title: "为了让AI拍完长视频大片，我手搓了个Skill"
source: "https://mp.weixin.qq.com/s/kAO14KDfIRgapmsljv3smw"
author:
  - "[[路人甲TM]]"
published:
created: 2026-09-10
description:
tags:
  - "clippings"
---
路人甲TM 路人甲TM *2026年9月8日 18:06*

现在的AI视频，单看几秒钟，已经很强了。

人物光影很精致也很漂亮，特效也是多得很。随手截一帧发出来，确实有点大片的意思。

可我最近折腾长视频，时长稍微一长，就会出现一堆问题。

比如人物刚刚还在大厅中央，下一段已经莫名其妙出现在二楼；摄影机本来一直跟着主角往前走，场景一变，镜头方向也跟着瞬移了；又或者说桌上的杯子前一秒还在人物手里，下一秒突然跑到笼子上。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/tp5fgmUBUbAPWqJSHApdWArHGCDf6GnwADwOFq1RZcV0bSpNPk0sDPDLY3ibvEzs5bKTwVjLzKy87cR4kxlvCBsbXHes6UvVbk6CaiapGAFds/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

人物没有变化，衣服也没变，但是动作却像中间被谁剪掉了一截，非常唐突。

这就很难受了。这种问题单独截出来看，可能不算特别严重。连续播放以后，人物和道具只要有一点对不上，立马感觉这个视频瑕疵太多了。

所以我干脆在LibTV里搓了一个长视频导演Skill，彻底解决同类的问题。

先看一个最直观的对比。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/tp5fgmUBUbBQ1LB4BcZHe3O5ChJlClpKE8aHvJor4k5GS9nLzg4MEiaaibN8KeNnicu22e0KS5gCtxkaheskjLicr3GySuhFJWT34icEyXAzrUZ0/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

上面未使用skill的这一版里，杯子前后的位置明显不一样；而下面用skill整理过后，杯子的位置终于接上了，前后看起来也顺了很多。

但如果它只是帮我记住「杯子别乱跑」，那其实也没什么意思。

它真正做的，是在正式生成以前，先替我把整条长视频该怎么往下拍想清楚。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbDJ3bbcibXl9wREPxLuLzwLWFnsibG5PMAvtvLQKjqr7EapxFP3LQicTpPMbcwamI3j5rjIa0pOraYt4SW1FsRHnE3bRWSROwib7Ts/640?wx_fmt=png&from=appmsg#imgIndex=2)

## 先别急着生成，导演得把故事过一遍

现在这个Skill我也已经放到LibTV的Skill库里了，搜「连续长镜头导演」就能找到。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbByNHp1sIg3aBiccjrQrpJlD8EA7xvoPFuS3PYU4pMicvhM5BLdaMiaYzaew2M8zQIJ700LiaQkoUvFzGDtaDrV31ibmFZ3XrbAwTicw/640?wx_fmt=png&from=appmsg#imgIndex=3)

点进去以后，直接丢一段普通的自然语言故事给它就行。它不会马上开拍，而是先把人物、事件和空间整理成一份导演执行包，等你确认以后，再继续生成视频。

展示一下效果，我这次拿来测试的是一场魔法学院事故。

镜头从大厅一路走进长廊，有人碰翻杯子，一只小魔法生物受惊逃跑，掉在地上的魔法书又放出一群蝴蝶。

摄影机要跟着这些意外一直往前走，把几个人和几个空间全部连接在一起。

故事只有一分钟左右，拆开以后却很麻烦。

里面很多细节的事情只要漏掉一处，后面的画面就接不上。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/tp5fgmUBUbAuMxF5FokGwISDehSI70uKDqoZfk02wClgpybicN4ibtDkGdKAJRNLOoay46B2JJzhxB8lDZggibDQrJQBCHwfODiat8esB26GwOE/640?wx_fmt=gif&from=appmsg#imgIndex=4)

Skill先处理的就是这些关系。它会把前后事件怎样衔接、空间怎样连起来、关键变化怎样出现在画面里，全都提前理一遍。

随后，整个故事会被拆成几个前后相连的视频节点。每一段推进一部分剧情，也给下一段留下明确的入口。

人物、道具、场景和摄影机都要接住上一段的状态，不能到新节点就集体失忆。

这一步做完，长视频才算完全衔接丝滑了。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbDjLtclqxMChR3aS5ic3tD0amYTRibZWwMia14VchE2ZkFm8tGia3ibFeiadbON7lCFKQJbN9gaV0nG9jUeTYMkHd8UKXWatRhKVTiczk/640?wx_fmt=png&from=appmsg#imgIndex=5)

## 人物和场景先钉住，少让模型临场猜

只把剧情拆还不够。人物、场景、道具也很关键。

在正生成视频以前，Skill会先做人物、道具和场景的参考图，用锚点图把这些视觉信息固定住。后面的每个视频节点都看同一套参考，不用拿到一段文字以后重新猜一遍。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbByefwa4N3wCxcLoe90diaZXLjDj3y9FqjCwQP1FF15cL05KL0gVibd50YZZyRsjWmv5J8ltUWF3oScNo3VOxEicFcGMd6wN0fa7w/640?wx_fmt=png&from=appmsg#imgIndex=6)

这套节点化的做法还有一个特别实际的好处。

哪一段翻车，就修哪一段。

这次做到尾声时，模型突然把前面的3D风格做成了2D平面动画。单看也能看，放回整条视频里就像临时换了一部片。

我只改了这一段的要求，让它继续保持前面的3D视觉风格，再重新生成这个节点。

其他四段不用陪着重抽。

五个节点都通过以后，再把它们合成一条完整视频。相比每次从头生成，这种方式省下来的耐心，可能比省下来的时间还值钱。

我又做了一版对照，差别一眼就能看出来

为了确认这个Skill到底有没有用，我拿完全相同的故事，跳过Skill又生成了一版。

对照组的单段画面依然很好看。人物、特效和场景都没有明显掉档。可一口气从头看到尾，问题就藏不住了。

有些动作被直接省略，人物和空间之间的转换也更突然。上一段刚留下的状态，下一段未必会接着处理。每个镜头都像同一个故事，连在一起却不像同一次拍摄。

两版放在一起，有Skill的版本更像摄影机一路跟着事情走下去。对照组也漂亮，只是走着走着容易断片。

看到这里，我才算确认，长视频的稳定感真不是靠某一帧有多惊艳。观众会一直记着刚才发生了什么，只要下一个镜头没接住，那点违和感马上就出来了。

## 转场也不能只靠一句「镜头切过去」

前后接得上以后，我还想再优化一些。

这些生成的视频之间的连接最好别让观众明显感觉到镜头正在换。

所以这个Skill会从当前画面里找动作和视觉线索，再借着它们把注意力带到下一个人物或场景。

比如下面这个公寓里的小片段。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/tp5fgmUBUbCVejZnOBrH5oHr262uTibic3vjYDyFw7Swib3Z24ibzpn67YdY87WcrpnBrnG3bws5yYfxEUbWc3PgYzysrYt3vTvDHmWibE7kCKuc/640?wx_fmt=gif&from=appmsg#imgIndex=7)

猫先接过客厅里的注意力，随后往厨房走，摄影机就跟着它一起转过去。这里没有硬切，镜头的方向来自画面里已经发生的动作，观众很自然就会跟着猫看向厨房。

这样出来的转场会更像一个连续发生的动作，而不是两个镜头被硬接在一起。

另一个我很喜欢的，是乐队指挥这一段。主角推门进去，摄影机从她背后慢慢推进，接着绕到侧面，最后逐渐拉远，把金碧辉煌的房间完整带出来。

整个过程没有切镜，机位却一直在变。推进、环绕和拉远被串在同一次运动里，镜头终于有了一点真导演的感觉。

## 管得太细，AI反而不会演了

做到这一步，我还踩了一个挺典型的坑。

刚开始为了求稳，我会把人物镜头这些动作描述得特别详细。我当时想得很朴素，要求越具体，模型应该越不容易跑偏。

结果规则越多，视频越僵。

快节奏和动作激烈的片段尤其明显。人物像在逐项完成任务，动作慢了，画面原本那股劲也没了。

后来我把控制范围收了回来。会影响前后连续性的东西提前定住，动作里的小细节交给模型发挥。画面自然了不少，出了问题也容易判断该回到哪个节点修改。

AI视频现在依然很看运气。同一个故事多生成几次，动作完整性和细节表现都可能不同。这个Skill也做不到让每一次结果完全照着预想来。

它能做的，是把最容易让长视频崩掉的几件事先理顺。故事别断，人物别突然变，摄影机知道接下来往哪里走。

这已经能少抽很多次卡了。

## 其实这个Skill，自己也能搓

如果你也想自己做一个类似的Skill，LibTV里现在有两种方式。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbDWvC3Zvic6Irfy3f2EyMddjZY9PvUia1NNsjWbibr1icnC9VVTu1FAb4WZGibCEGTQDCTBWgJwHRlfNq2enziapsEECWGEdgtmiaSDzs/640?wx_fmt=png&from=appmsg#imgIndex=8)

一种是直接导入已有Skill。手里如果已经有写好的.md文件或者完整文件夹，直接上传就能用，比较适合已经在别的平台或者本地调过Skill的人。

另一种更简单，直接和Agent对话创建。你只需要告诉它「我想做一个什么样的Skill、希望它解决什么问题、执行时大概怎么走」，然后边聊边改就行。

我这个「连续长镜头导演」其实就是一路这样磨出来的。

最开始只是想解决前后镜头接不上的问题，后来就是一边用、一边改。哪里容易出错就补哪里，管得太细了就再往回删，慢慢才变成现在这个版本。

所以做Skill这件事本身也没想象中那么玄学。

很多时候不是你一上来就知道该写什么，而是先让它跑起来，再拿结果反过来改。

## 写在最后

自己手搓的这个Skill，它不仅帮我解决了连续性的问题，它也改变了我做长视频时的方式。

现在，一段普通故事可以先被整理成导演执行包，再拆成一组能继续拍下去的视频节点。

我最喜欢的地方也很简单。那些原本听起来很专业的一镜到底、群像调度和连续运镜，现在我根本不需要去读懂这么多专业的术语。

打开LibTV，我不用研究一长串复杂提示词，也不用硬学一套镜头术语。先把脑子里的故事写下来，交给Skill整理，再看它一段一段变成画面。

这种感觉确实挺爽。

以前我只想让AI生成一个好看的镜头。现在，我真的离「做出一段属于自己的大片」又近了一点。

我是路人甲，前数据分析、产品人，现创业者。关注AIGC人工智能，分享实用的AI应用。让AI变成你触手可及的生产力。