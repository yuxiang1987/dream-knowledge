---
title: "MiniMax 杀进 Flash 混战，我拿五个项目试了试"
source: "https://mp.weixin.qq.com/s/Ut1zEeucpgYeA5cmqkS6FA"
author:
  - "[[董道力]]"
published:
created: 2026-10-03
description: "Flash 模型又多了一个玩家。"
tags:
  - "clippings"
---
董道力 硅星人Pro *2026年9月30日 09:49*

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/gdEn3pxzatS8Wh4CgcDngVaw8HkktaNXAa1FhAX84leoQORxtn1VltQDgbT18AhnjT97j37bnmVSyicm3Rd7tGMfrKwLuPiaHAqrhMGicxiaAAs/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

作者 *｜* 董道力  
微信 *｜* ddl941110

MiniMax 也推出 Flash 模型。

9 月 28 日，M3.1 Flash Preview 上线 MiniMax Code、MiniMax Token Plan。

Flash 这个模型生态位最近备受关注。DeepSeek V4.1 Flash、GLM5.3 Flash、MiMo V2.6 Flash 相继发布。Google 六周内连发三代 Flash，OpenAI 的 GPT6 Luna 虽然不带 Flash 后缀，也盯上了高频任务和更低的使用成本。

为什么大家都往这里挤？因为 AI 开始真正干活了，其使用成本也不得不被考虑了。用户一个需求，Agent 却要读文件、改代码、调工具、跑测试，消耗大量 Tokens。如果让旗舰模型从头跑到尾，价格感人，而且这些日常步骤，也不需要用旗舰模型的能力。

所以 Flash 模型的密集出现，本质上是一场“干活模型”的争夺：能力要够用，响应要够快，用户还能承担费用，三个条件里只要有一条不达标，用户就很难天天用它。

MiniMax 这次能不能挤进这个位置？

![图片](https://mmbiz.qpic.cn/mmbiz_png/gdEn3pxzatRV7iazibqActUfQ4ETFelWBrsYia6ickab2BPWApcH3LN4JSQv5X4KiakQkFUXEkImrec22tgdXcF8Xok6QasP6cu46LS3RqOghxQs/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

1

**实测 MiniMax M3.1 Flash Preview**

首先既然是 Flash 模型输出速度就不能慢，经过测试，在 MiniMax Code 环境下，用 M3.1 Flash Preview max 1M 上下文，速度比较稳定，无论思考时间长还是短，可以稳定 100 tokens/s。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/gdEn3pxzatRciasAhAqNxUBDPwH7uAByVbRGzibFVIBob6IafJEf0wrpGUmUxLszTYlxhwaPfBkpDP1uysPHyqgXDxaia4k3Lzhr190Y4ogr9A/640?wx_fmt=png&from=appmsg#imgIndex=2)

但输出快不代表项目完成的快，我们测试了几个适合 Flash 模型的任务，M3.1 在那边框框输出，但任务完成得并不算快。

1

**Coding+前端测试**

首先我们做了两个 Coding 偏向前端的任务，分别是 SVG 联动动画和地球模拟沙盘。

**测试 1 三联动 SVG**

任务是一款赛车游戏，要求页面里有一台打开的笔记本，在屏幕上运行赛车。用户可以用电脑的实体键盘、画面中的笔记本键盘，或旁边的手柄来驾驶。

任务的难点在于让三种操作共用一套游戏状态。按住实体键盘的加速键，画面中的对应键帽和手柄按钮会同步亮起，赛车提速，速度表随之上升。

深究了一下 M3.1 Flash Preview 的代码，它将输入处理、驾驶逻辑和画面更新分开组织，再通过共享状态实现联动。这样，不同控制方式可以复用同一套驾驶逻辑，画面反馈也有统一的数据依据，抓住了这道题的关键。

，时长00:25

<video src="https://mpvideo.qpic.cn/0bc3fyc54aafhaalmofz6rvfklwd3yxalxqa.f10002.mp4?dis_k=76bd139da78541185609ca0b2b84c7f6&amp;dis_t=1791020913&amp;play_scene=10120&amp;auth_info=cs7hzZ5/JEBC0r+MkB8jeDgTQTsNJ2Y8SV83NU94bzVMdz8dOVI/DTUFDUoscC5YLBk=&amp;auth_key=e83d7459f170227f5bdde768d53ecbc9&amp;vid=wxv_4716747160636243971&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

但如果你留心视频中左侧对话框，就能看到视频中项目其实还没有完成。录完视频后，M3.1 Flash Preview 仍在继续思考、截图检查项目，甚至还说要把之前写过的 bug 检查一下。但结果其实什么都没改，没什么错误。

这既是偏长思考带来的代价，也是它“严谨”的另一面，会检查自己的输出，只是暂时还不太懂得适可而止。

**测试 2 地球宇宙环境模拟**

第二个任务是模拟地球宇宙沙盒，比单纯的 SVG 更加复杂些。用户可以进入正常地月、近距离岩质卫星和强潮汐三种情景，调整卫星质量、地心距离、地球大小与自转速度，也可以改变陨石的大小、速度和撞击位置。

M3.1 Flash Preview 把强潮汐下的地球做得很有冲击力，地表逐渐开裂，亮光从裂缝中透出，碎片不断飞散。有个细节，仔细看地球，海平面还会随着卫星运动，有节奏地起伏。

地表开裂的光效、碎片的飞散、海面的起伏与仪表读数，风格统一，在视觉审美上不廉价，也不是堆特效，而是让场景氛围形成整体。此外，画面也与参数仪表联动起来，我把卫星拉近或推远，仪表上的潮汐读数随之变化。

，时长01:27

<video src="https://mpvideo.qpic.cn/0bc3ruabsaaa6mahcu543vvfbdoddggqagia.f10002.mp4?dis_k=d401e312bf27a8faf4dd31937f9569fc&amp;dis_t=1791020913&amp;play_scene=10120&amp;auth_info=cLSMr+1zdUVG077Znh92KzpBFG8NLzA/GFU1YEYvNmZOI2JNaVtuCDEEDB8icHsLLks=&amp;auth_key=5e89f6ff6b21104ebda729679dd8eeb6&amp;vid=wxv_4716748914526273541&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

1

**多模态测试**

MiniMax M3 是一个从第零步开始多模态训练的原生多模态模型，而 M3.1 Flash Preview 继承了这一点。接下来，我们分别测试一下 M3.1 Flash Preview 对于图片和视频的理解能力。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/gdEn3pxzatRGeH9DnIxbQIhicMDiasvg3doPcLmjk3SNd3Kp21GgCPB0mHY1Pllj1rtntYzWLpVtbmQSTn20QtYicWIgU0dwLqgZNQmPZykoDY/640?wx_fmt=png&from=appmsg#imgIndex=3)

**测试 3 手绘地图变成 3D 导图**

我上传了一张奇幻风格手绘地图，并要求他改成 3D 导览。

![图片](https://mmbiz.qpic.cn/mmbiz_png/gdEn3pxzatQJ7AibDia6cqMJqk7OBSC5MJeKRjlBGib2Kfviaq1OehiaZibUyKGiabsAyr2w9Hn5hJiaoXOJ4Szict5SR1NvNGnXPfNW8mSic2iahwYXuQ/640?wx_fmt=png&from=appmsg#imgIndex=4)

，时长01:10

<video src="https://mpvideo.qpic.cn/0bc3pudxgaahq4abxxf3djvfo7odon6qo4ya.f10002.mp4?dis_k=fc957c285c947f6dcb9661390906914a&amp;dis_t=1791020913&amp;play_scene=10120&amp;auth_info=Jsrq3q98f0IZ2r3Wlk10KW1IED1dLDpoHV42Nhh/M2MYfjBIaVFkD24NDxAqInkJeUI=&amp;auth_key=d3f5fa5e03d632596e85d1adc3a3b85b&amp;vid=wxv_4716750993357553665&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

从视频中可以看到，M3.1 Flash Preview 不但还原了地图的整体样子，比如湖泊港口位置、河流走向、周围树林环绕，还给地图上没有标记的城市取了名字。

有个细节，地图上标记了指南针，M3.1 Flash Preview 在 3D 导览中一并还原了。而且导览的画风很好看，有低多边形 3D 微缩沙盘画风的奇幻地图。配上羊皮纸式的文字界面，带一点复古冒险游戏的味道。

可见，M3.1 Flash Preview 在多模态上做了取舍：输出端有所收敛，换来更快的速度，理解端依然扎实，能读懂一张手绘地图的地形、方位和画风，再据此重新创作。

**测试 4 根据视频生成 NASA 维修手册**

除了图片，M3.1 Flash Preview 也支持视频输入。这项测试使用公开的 NASA NICER 维修训练视频，要求模型只根据视频中的画面和声音，写出一份可供复盘训练过程的手册。

手册需按时间顺序说明补片的取用、定位、插入、锁定确认、拉拽检查和工具移除等动作，为关键步骤标注视频时间，并区分“画面可见”“对话提及”和“视频无法确认”的信息。

，时长04:11

<video src="https://mpvideo.qpic.cn/0bc3uuaesaaabeaia7f3gjvfbjodjgsqasia.f10002.mp4?dis_k=2787b797876ea054679eb82145362d55&amp;dis_t=1791020913&amp;play_scene=10120&amp;auth_info=c4/a0bJ/d0YV2b3dw0wgfTlJEmgJJzVlSVFnYE58YzZNfmMcYFBsC2IODxt/Iy1dLUM=&amp;auth_key=0f19a996abd18e5038c1551f84a218c4&amp;vid=wxv_4716066788105666563&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

M3.1 Flash Preview 成功把维修训练整理成了有时间码的操作线索：WIF-24 上锁、BRT 插入、拉力测试，以及 NICER 收尾评估，都能在记录中找到对应位置。

它还捕捉到“a couple of patches”指两个补片，并标出疑似语音识别错误。更难得的是，模型明确区分了对话能确认的信息与画面无法核实的动作，没有为了凑出完整手册而编造细节。面对专业视频，这种梳理流程、保留证据边界的能力很实用，也很让人安心。

![图片](https://mmbiz.qpic.cn/mmbiz_png/gdEn3pxzatQwhqHVKatKaNLXjeT5shtCsnEqjhKZibF9q4l84cGFDNKpticCynZOe1Qojp3jQKyjBpDWSdS37gCW9CJHM1FKT7ntG7Lic2jPP0/640?wx_fmt=png&from=appmsg#imgIndex=5)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/gdEn3pxzatQjP17logF9XEH40NKkGeWHiaygh4vDUQOSMOMrTymylEThYtcic5y8UqBB9glZepaUl15a5xl0oSEbx4yAzeJTRnbwCNUYriarwk/640?wx_fmt=png&from=appmsg#imgIndex=6)

1

**金融可视化能力**

最后一项测试则是最近各大 AI 公司都在竞争的金融领域，无论是 OpenAI 还是 Anthropic 都延伸自己模型在公司金融分析，个人理财助手上的业务。

**测试 5 财报核验**

金融分析最难的地方，是把看似矛盾的数字解释清楚。我上传 MiniMax 的 2026 年中报和 2025 年年报，要求 M3.1 Flash Preview 交付一套本地可运行的业绩核验工具。它顺利完成了 PDF 数据入库、带来源页码的查询以及可视化页面等基础功能。

![图片](https://mmbiz.qpic.cn/mmbiz_png/gdEn3pxzatTrTM7bnXUFBwGT0aW7ic4a7Ss3avOGquWX8zCL4FO3GLeqP9Q5mowpImvDe8Fpl6TbKdiaRibK9ianvZVUK9f8BzoonictHWMTBc00/640?wx_fmt=png&from=appmsg#imgIndex=7)

而真正体现分析能力的是亏损拆解。以中报中的 2025 年上半年数据为基期，2026 年上半年期内亏损从约 4.02 亿美元收窄至 3.58 亿美元，经调整净亏损却从约 1.39 亿美元扩大至 2.93 亿美元。

模型顺着调节项找到了原因：金融负债公允价值亏损减少约 2.23 亿美元，抵消了其他损益项目的压力，经调整口径加回这项亏损后，研发开支增加约 1.73 亿美元等变化就更清楚地显现出来。

他没有简单地描述现象，而是把相关的数据列出来，形成完整的思考过程，看来 M3.1 Flash Preview 确实是有思考。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/gdEn3pxzatRliaTH6MUMPmTM5hQ8lsdwx21QGQV4y1Gc2rUIhengnvMbjqU8NGKctVzkXDUBaPc7m04Q5JvakcFHnLEU8NbGSTcJWaU20yRU/640?wx_fmt=png&from=appmsg#imgIndex=8)

1

**模型的第二战场**

通过五项测试，我们可以认为，MiniMax 已经具备在多个 AI 高频场景中争夺工作入口的产品实力。

M3.1 Flash Preview 前端审美良好，代码能力扎实，多模态理解能力强，金融分析这样复杂的场景也有一战之力。其处理的已经不只是“快速写一段代码”，而是需要组织信息、安排交互、检查结果的完整任务。

它的做法也很有特点：遇到复杂任务，会把需求拆细，借助搜索和工具补足信息，再反复检查成品。这或许正是 Flash 追赶旗舰的一条路径。当然，这也不是没有代价，M3.1 Flash Preview 有时候会在简单问题上想太多，用更多的思考时间，换取更优质的答案。

但其稳定快速的输出速度，又刚好补上多想几轮所需的时间。根据 artificialanalysis 数据，Mimo V2.6 Flash 和 GLM5.3 Flash 的输出速度只有 50+tokens/秒。虽然 M3.1 Flash Preview 还没有在相同环境下测试过速度，但其在 MiniMax Code 中能长时间稳定输出 100+tokens/秒。

M3.1 Flash Preview 跑下来，性能与效率平衡超出预期。上周爆火的匿名模型 Space Bunny，上线三天冲上双榜第一，多项证据指向 M3.1。如果属实，可以侧面证明很多用户和我测试下来有同样的体感，M3.1 Flash Preview 已经可以成为开头所说的“干活模型”。何况它还只是 Preview 版本，后面的打磨空间值得期待。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/gdEn3pxzatSRMlPJan8yg8eFZagVwZDEZko9eYtDUH9X46ib7upd1FqfHzEjZbZGS6cofell4jKSDRWUBCoChQ9yVaeyyN2ricmhy1VLUjZFU/640?wx_fmt=jpeg&from=appmsg#imgIndex=9)

**[![图片](https://mmbiz.qpic.cn/mmbiz_png/gdEn3pxzatSgnERxDMDaibsSkcJf9E7uwXcFdLKsyvD1E2GDyIm7qspyGkB4Qp5RjnvAKibYuwTqN9mN0ibZ8N9EndH8TnQA36PrcZXIhXOicNo/640?wx_fmt=png&from=appmsg#imgIndex=12)](https://mp.weixin.qq.com/s?__biz=MzkyNjU2ODM2NQ==&mid=2247633660&idx=1&sn=ddaf91bc6b41fe9da6cc0c34b486e7a2&scene=21#wechat_redirect)**

**点个 **“爱心”** ，再走吧**

阅读原文