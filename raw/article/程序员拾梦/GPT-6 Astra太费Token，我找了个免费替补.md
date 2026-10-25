---
title: "GPT-6 Astra太费Token，我找了个免费替补"
source: "https://mp.weixin.qq.com/s/lakKP9d3MsF3VW9PNXnksw"
author:
  - "[[程序员拾梦]]"
published:
created: 2026-10-07
description: "自从 GPT-6 Astra 出来之后，我就一直处于 Vibe Coding 上头状态。"
tags:
  - "clippings"
---
程序员拾梦 程序员拾梦 *2026年9月21日 21:30*

自从 GPT-6 Astra 出来之后，我就一直处于 Vibe Coding 上头状态。

**但是 GPT-6 Astra 的 Token 消耗太快了，动不动额度就见底，而且迟迟等不到重置卡，这多少让我有点受不了。**

我就在想，有没有可以免费使用的大模型，能在 Codex 的 Token 用完时临时顶上。

没想到还真让我找到一个： **Agnes AI** 。

准确来说，Agnes AI 不是单一模型，而是一套覆盖文本、编程、生图和视频的多模态模型。最重要的是 **免费** 。

不要看它免费就以为是小作坊产的，其实它是由新加坡的 Sapiens AI 推出。并且它的Agnes-3.0-Flash、Agnes-Image-2.0、Agnes-Video-2.5三款模型在Artificail Analysis的排行中都比较靠前。

既然这么能打还免费，我就想测一测它的实际表现到底怎么样。

这次我没有直接在 Codex 中接入 Agnes AI 的 API，而是用了它自带的编程 Agent——AgnesCode。因为这样更简单，下载安装并登录后就能使用，不需要单独配置 Agnes API。如果想在 Codex 中接入 Agnes API，也可以安装 Codex++，再配置 API Key 和 Base URL。不过，这样比较折腾，我就没弄。

![图片](https://mmbiz.qpic.cn/mmbiz_png/BBnmXtwleomnuNiasbmqltM1vsF264RqytDYB2X3jqHObrbSDCkhQ07RsaoqDkRtTYYbxllZdF8tlC6gBmtpBC31wXO57ticrDT1X38uxxLks/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

01

PART

生图和生视频能力

SECTION

为了同时测试它的生图和视频能力，我特意选择了最近很火的“东方巨物美学”AI 短剧风格。

因为这类短剧需要先生成多张以巨型建筑为主体的画面，再利用图生视频做成每段 4 秒左右的动态镜头，最后剪辑合成，正好可以把两项能力串起来测试。

咱们先来看看成品：

，时长00:20

<video src="https://mpvideo.qpic.cn/0b2ejqam6aaa7eaojo5rofvfatgdz5gabtya.f10002.mp4?dis_k=ccf07ab1bb69dfd7a8c8ebbc3690babd&amp;dis_t=1791342107&amp;play_scene=10120&amp;auth_info=U+jtq2s5BBi/jtWScCE/WnE6R1IULHllTGAaFSFaeDd1HxpofCJJb3wSZDocLB9Oew==&amp;auth_key=b23c88c39203228933d4dfeebecd47b7&amp;vid=wxv_4704393219986653184&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

从最终成片来看， **整体氛围和宏大尺度基本做出来了。**

而且整体过程也算比较顺利。下面来看看生成过程。

我先把下面这段提示词交给 Agnes，让它沿用这种风格扩写出四组提示词，再分别生成对应的图片。

text

一座中国天界的巨型门关，四根雕刻着升龙的朱红巨柱从翻涌白云中拔地而起，深色木构飞檐形成高耸的建筑框景，浓密古松围合下方两角，一位原创白衣女子独自站在黑色镜面般的水台上；近对称的中央开口显露阳光照亮的高耸积云与蓝天，暖色侧光擦过朱漆，与冷色云影形成对比，具有礼仪性的静谧感、电影级幻想环境关键帧、精确的倒影、清晰可读的建筑，体块与统一透视。

下面是生成的图片效果：

![图片](https://mmbiz.qpic.cn/mmbiz_png/BBnmXtwleolSicUgNsY1uu2rLemHnqI3KlT0f7DGnBx2Ar0bgiah6nn7IKGTL1lUpsQ79Zmrtp2qyBNqGnFiaicDwzW4I46ZRWxVFj88Dy706ibI/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=1)

然后，我让它根据每张图片生成一段人物向前行走的 4 秒视频，总共是4段。下面是提示词：

text

画面中人物向前缓慢行走，人物动作流畅。跟随视角，超长焦镜头，镜头匀速缓慢向前推进，运镜全程丝滑匀速，无抖动、卡顿，不切换镜头。云雾缓缓飘动，天空云层细腻，空间纵深感极强；通过超长焦的空间压缩，形成强烈的压迫感和史诗级视觉效果。电影级光影质感，大气磅礴，超真实。

无论是生成图片还是视频，整个生成过程还算比较顺利，只有最后一张图让我做了一次调整。一个免费的模型能做成这样，我觉得可以了。

接下来，再看看它的 Coding 能力怎么样。

02

PART

Vibe Coding 能力

SECTION

这次我用两个小项目测试它的 Vibe Coding 能力：一个是 **复古太空射击游戏** ，另一个是 **通过敲键盘学习英语的网站** 。

复古太空射击游戏

我给了它一段提示词，让它制作一款复古风格的太空射击游戏。玩家驾驶太空战机，可以发射子弹，也可以吃敌方战机被击毁后掉落的装备来升级火力。

![图片](https://mmbiz.qpic.cn/mmbiz_png/BBnmXtwleolYuvc0ZzseOhDNlTqM3YXaKJ0cmdiavTGfOJkcwnqpn12912OIlkIEWA5CzBqwUoDdopUvRcgKzFGM78p5wicweEia8PI6nCxBY8/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=2)

先来看第一个版本的效果：

，时长00:53

<video src="https://mpvideo.qpic.cn/0bc3zmdscaah3maaw75wazvfps6dehfqoiia.f10002.mp4?dis_k=71409cd882a8869389c28f2d04b4ff3a&amp;dis_t=1791342107&amp;play_scene=10120&amp;auth_info=BJ2qmtQCa1NOttrQyHlxPFRwaBgFG3QiNExjShNyXSw6IxtIay9wHjl1RmFgFXwcQHo=&amp;auth_key=513157adc7d3b3e88e72975abd59b124&amp;vid=wxv_4704386159849013252&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

其实，第一个版本已经具备了基本功能，比如发射子弹、吃装备升级，Boss 也做出来了。但是敌人的造型实在有点丑，都是三角形和圆形来代替，这次我觉得Agnes 多少有点偷懒了。

**另外，大家把注意力放在模型表现上就好，关注点别放在我的游戏操作上。**

所以我又让它继续修改：重新生成敌机素材，同时修复 Boss 血条等问题。

![图片](https://mmbiz.qpic.cn/mmbiz_png/BBnmXtwleom59ELHibQ6NOoQWvKtFpLy9Mc9gC2hLGXTYYibNEc44iaica128vQfReZMiaiaZ1icZFaibLcEODy2fDibYUtfkaGl9alDPqUxEutgyXnE/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=4)

经过几轮修改后，再来看一下成品：

，时长00:54

<video src="https://mpvideo.qpic.cn/0bc3xyaiwaaaqqakcz5rjvvfbpwdro7abcya.f10002.mp4?dis_k=67ee00ce7e17520e94f8010949dd63ba&amp;dis_t=1791342107&amp;play_scene=10120&amp;auth_info=VJSChuoHbQIbv4nXlXYmbFt9bBFTGnknPkQ0SE52UCpqc04Zay52T2x8FWY9GitMT3c=&amp;auth_key=981e95c443273fe12ac27ab048995ed8&amp;vid=wxv_4704386861320814594&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

这一版就顺眼多了：敌人的造型更完整，Boss 血条也修复了。吃备时，它还主动加入了吸附效果，这样就不会先得生硬，这个细节确实不错。

03

PART

敲键盘学英语的网站

SECTION

除了游戏，我还让它做了一个通过敲键盘学习英语的网站。网站收录了一些常用英语词汇，包括四六级词汇和程序员常用词汇等。

而且网站自带虚拟键盘，可以边敲边背，还提供默写模式；输入错误的单词也可以记录到错题本里。 下面是提示词：

提示词

帮我做一个英语学习网站，类似 Qwerty Learner，功能如下：

1\. 打字练习：显示单词，用户输入拼写

2\. 词库选择：CET-4/6、GRE、IELTS、编程词汇

3\. 默写模式：只显示音标和释义，用户输入单词

4\. 发音功能：点击播放单词发音

5\. 统计显示：WPM、正确率、时间

6\. 深色/浅色模式切换

7\. 按键音效

8\. 可视化键盘（按键时高亮）

9\. 错题本：记录错误单词

10\. 暂停/继续功能

使用的技术你可以自行选择，严格按照上面的功能执行

这是最终效果：

，时长00:19

<video src="https://mpvideo.qpic.cn/0bc3vycueaafd4agrjnuvnvfllwdikxakqqa.f10002.mp4?dis_k=14e714a21d9885dbb16d83b5ee09b7c1&amp;dis_t=1791342107&amp;play_scene=10120&amp;auth_info=CcCn0JMAbgJJvo3VwnAnZFRwa0VUQXx3Ykw2GkInDH43J0oYOyl1Tz59EWRqHCpEQHo=&amp;auth_key=f8af706ac62542f756bb04f770021821&amp;vid=wxv_4704388859051425794&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

这个项目也不是一句话就生成的。第一个版本仍有一些 Bug，比如默写模式中的英语单词显示乱码、错题本里的开始按钮无法正常使用等。不过，这些都是正常现象，经过几轮沟通和修改，这些问题都修复了。

///

LAST

最后

SECTION

最后总结一下。

这次测试中，Agnes AI基本上很好的完成了生图、生视频和两个Vibe Coding的小项目的测试。

当然，这次测试的项目比较简单，比如视频生成中没有测试人物一致性，多镜头衔接这些老大难问题，ViveCoding也没有测一些复杂的功能。但是作为一个替补模型，尤其是一个免费模型，我觉得能力已经够用了。

至少对于我来说，它是一个值得放进备用工具里的选择。

我是 拾梦，持续分享 AI 工具、效率软件和实用黑科技。

作者提示: 个人观点，仅供参考