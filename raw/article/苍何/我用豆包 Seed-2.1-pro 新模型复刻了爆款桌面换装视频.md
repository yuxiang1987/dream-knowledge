---
title: "我用豆包 Seed-2.1-pro 新模型复刻了爆款桌面换装视频"
source: "https://mp.weixin.qq.com/s/lIj3A81po1StY5WYkTe6rg"
author:
  - "[[苍何]]"
published:
created: 2026-10-07
description:
tags:
  - "clippings"
---
苍何 苍何 *2026年9月17日 09:08*

这是苍何的第 599 篇原创！

大家好，我是苍何。

最近我发现这种桌面换装视频真的巨火，我在各大视频平台看，流量都很不错。

然后我随手一转发一条视频，随随便便就18 万多的曝光。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/zw8bZHsVSaDbj9icEj5GOe5gvoI8f5WBpE2cInvTlNezicfgUr11tQxC7ianiclqNpu5pKzXy0RJWkbCWCf0YWpWtAvckuPGzukDicTuSI7y2vNA/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

我真的超想复刻然后去发，但复刻一个爆款视频比复刻图片难多了。

昨天刚看到豆包 Seed-2.1-pro 更新了，在多模态 Coding 上有了显著的增强，刚好做一下测评。

这次2.1的多模态能力更新让我觉得很吃惊的是，直接可以解读出视频的细节，这个是网络上很火的一段视频。小姐姐换装桌面壁纸。

以下视频来源于

蕾娜有着柔软蓬松的金发

，时长00:30

<video src="https://mpvideo.qpic.cn/0b2emeamkaaab4amigfkibvfayodyvqqbria.f10002.mp4?dis_k=72ee826b548e134ba1777738e2af02f0&amp;dis_t=1791339898&amp;play_scene=10120&amp;auth_info=As/rxLd4QFRL2f/C1w5fd3BnEAUXcywwXC1NR2tOLDw8B0szbVBbGTxTOGoWYlJXZG0=&amp;auth_key=1b8322edaa047bc98a37ae574e04c712&amp;vid=wxv_4697090547390300161&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

下边是我使用新Seed-2.1-pro 模型解析视频细节后 加上 Doubao-Seedance-2.5 提示词直接复刻出来的。

，时长00:10

<video src="https://mpvideo.qpic.cn/0bc33ycjkaaediabeznoprvfjxwdsxpajfia.f10002.mp4?dis_k=85d979c7432d3c447bc8d236337555aa&amp;dis_t=1791339898&amp;play_scene=10120&amp;auth_info=VOHomaYoT1NKhfDJgltecHpmElUXJXpjCCIeQmtAej1qVE40agFUHj0PN2FDN1NQbmw=&amp;auth_key=4d0f345e4dc34ec8f7fba832ce29b04d&amp;vid=wxv_4697092028415967233&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

复刻过程很简单。直接把原始的视频加载到豆包工作模式。

然后使用提示词：

```
●●●提示词请输出以下结构化内容：1. 分镜时序与台词对照表- 提取每一段镜头的起始/结束时间戳。- 记录对应的台词文本、说话语气（如慵懒、俏皮、自信）与口型情绪状态。- 明确镜头间的人物出入画逻辑（从沙发坐姿离开镜头 $\rightarrow$ 换装后步行入画展示）。2. 核心视觉资产（一致性锁定）- 人物特征：面容、年龄感、固定发型与妆容细节。- 场景与光影：黑色极简背景、复古黑色皮质沙发、影棚摄影灯光（边缘轮廓光、柔和面光）。- 服装细节拆解：逐套梳理材质、剪裁、色彩及配饰标签（居家灰T、粉白芭蕾舞裙配长袜、机能战术背心工装裤等）。3. 端到端生成 Prompt 套装（Seedance2.5 适配）- 固定环境与角色描述：用于贯穿所有分镜的基底特征提示词。- 逐分镜动作+台词 Prompt：直接将台词与动作/表情强绑定的生成提示词（包含机位、动作走位、说话时的微表情）。- 多镜头连贯技巧：如何利用首尾帧（Start/EndFrame）或参考图，确保人物在“出画换装再入画”时面部与场景不漂移。
```

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/zw8bZHsVSaDObhia1nsics2UTvG2eyxbCrnGJ3KTepgpOYyQ8OFhre5iceInG1FHOSOYDQF6LvYicJA8GjOQibf3lnicO5JQlCoEdIUgCicSIrWQWU/640?from=appmsg#imgIndex=1)

给大家稍稍带入分析一下这个多模态的能力，大模型是怎么完成这件事情。

我们都知道，视频本质上就是 **一帧一帧的图片快速连续播放** ，利用人眼的 "视觉暂留" 现象，让大脑误以为画面在动。

那么知道这个原理以后，大模型在处理视频的时候，就反推过来抽帧的形式。

所以抽帧本质上就是 **从视频这摞 "图片序列" 里，挑出指定位置的那一张单独存出来** 。帧率越高，同样 1 秒内可挑的图片越多，动作细节越细腻。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/zw8bZHsVSaDFLGnF2IHbshibeNuSx86AAZStF3ITw6C5RyxrfgDTKMUccJ8liaJqtoPmEbLUPNAjzlCgKH1iczGMmGI9viaBSXIwE4Gph0tjzmY/640?from=appmsg#imgIndex=2)

豆包工作之前用 `ffmpeg -ss 5 -i video.mp4 -frames:v 1 out.jpg` ，意思就是：

- 跳到视频第 5 秒的位置
- 取出 **那一帧** （也就是第 150 张图片，30fps×5s=150）
- 保存成一张 JPG

看这里的思考过程就是：

![image.png](https://mmbiz.qpic.cn/mmbiz_png/zw8bZHsVSaAic6vGIsqssOroqzppD11OTiaRNvLIpVJK7Ixwrpjr8IqJULkeBLq9e3g6Y5Foiag3rTcyHFxQ12JzIg4cNULesRWxctUJX2TkmE/640?from=appmsg#imgIndex=3)

先澄清一个点， 抽帧策略 **不是均匀 5 秒一帧** ，而是 **关键帧采样。** 根据视频剧情节点选时间点。

下面来梳理一个流程图，看看就都懂了：

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/zw8bZHsVSaANibyAjW0JxGtGeMovX8LhmLMBfLG9zI9aTwMyx7xIy4dFh1NdcpXUzY1SVUCGIUxLicPxkDO20DJZMMRabz6RQibBQKNZGUp3RU/640?from=appmsg#imgIndex=4)

现在我把输出的提示去火山生成 体验界面生成。

![PixPin_2026-09-16_15-28-51.png](https://mmbiz.qpic.cn/sz_mmbiz_png/zw8bZHsVSaDIHgiax1bU6IJfZwEtMXJ38etPCA6foJ96Mx68yj8PG4ymt8Y2oibM6y7ibibAGMJBoezAIUOR9HhbY1LkHicYgmw3HsLZ45qxA1icQ/640?from=appmsg#imgIndex=5)

当然生成视频的平台都可以，更推荐Doubao-Seedance-2.5。懂的都懂，而且豆包工作配合Doubao-Seedance-2.5就很丝滑。

提示词如下：

```
●●●提示词： 时长10秒，比例16:9横屏，语言中文。 人物参考：仅参考图片1锁定五官、发型、肤色和人物身份；服装严格按下文变化。 人物要求：成年女主。 全程同一人物，不换脸、不改变身材比例；提高权重，优先死死锁住五官、发型、肤色、身份。 整体风格：超真实AI动态桌面互动视频，模拟电脑全屏桌面录屏。 底部保留简洁任务栏，左上角少量桌面图标；画面主体是一张会实时互动的动态壁纸。 黑色皮质沙发，冷色柔光，深色背景。 固定机位，全程一镜连续，不切镜、不推拉。 女主主要位于画面右侧，左侧留给语音字幕界面。 字幕界面（保留，覆盖「禁止文字」约束）：字幕必须出现于画面左侧中部，不能放在底部。 纤细现代无衬线中文字体，中等字号，无底框，轻微柔光和阴影。 女主说话：淡紫色文字，左侧显示扬声器图标。 男声说话：白色文字，左侧显示麦克风图标。 字幕下方始终有一条细小白色音频波形，随声音实时跳动。 所有字幕跟随发音逐字输入，约每字0.08—0.12秒，像键盘正在手动打字；当前句说完后停留约0.4秒，再整体淡出。 不能整句突然出现，不能提前显示后面的字。服装设计（三套造型统一只改领口：低圆领/浅V领，微露事业线，其余保持完整遮盖）： 初始造型：浅蓝色棉麻宽松家居上衣，深色休闲长裤，素颜，头发自然披散，素雅居家感。 第一套学生旗袍：淡青色短款改良旗袍（低圆领/浅V领，微露事业线，其余完整遮盖），白色蕾丝裙摆边，低跟玛丽珍鞋，双麻花辫，整体清新书卷气。 第二套上海滩名媛：酒红色丝绒长款旗袍（低圆领/浅V领，微露事业线，其余完整遮盖），金色刺绣花纹，珍珠项链，波浪卷发，红色高跟鞋，雍容华贵。SINGLE CONTINUOUS SHOT（00:00-00:10） 00:00-00:01.50 女主穿初始造型坐在黑色皮沙发右侧，腿上抱着黑色靠枕。 她双手轻轻整理头发，随后看向镜头，露出亲切微笑。 女主自然开口：「说吧，想看什么？」 字幕逐字显示：「说吧，想看什么？」 00:01.50-00:02.20 男主始终不露脸，仅有画外男声，语气直接而期待：「想看旗袍。」 女主安静听着，笑容加深，轻轻点头。 字幕逐字显示：「想看旗袍」 00:02.20-00:03.00 女主爽快回答：「好，等一下。」 她把靠枕放到一旁，右手撑住沙发起身，动作带轻快的「嗖」声，向右侧走出画面。 字幕逐字显示：「好，等一下。」 00:03.00-00:04.80 换装完全在画外完成。 伴随轻快的亮相音效，女主穿第一套淡青色学生旗袍从右侧重新走入。 她站得离镜头较近，画面主要呈现腰部、旗袍裙摆和玛丽珍鞋，头部自然超出画面上沿，轻轻转半身展示。 女主带着俏皮语气说：「怎么样？」 字幕逐字显示：「怎么样？」 00:04.80-00:05.50 男主画外音满意地回答：「嗯，不错。」 女主保持站姿，轻微转动腰身，让旗袍裙摆自然摆动。 字幕逐字显示：「嗯，不错」 00:05.50-00:06.30 女主轻快地说：「还有一套。」 说完立即转身向右侧离画，裙摆随动作摆动。 字幕逐字显示：「还有一套」 00:06.30-00:08.00 换装完全在画外完成。 随后响起一次短促流畅的换装「嗖」声，女主穿第二套酒红色名媛旗袍从右侧走入。 固定镜头先看到丝绒旗袍下摆、金色刺绣和红色高跟鞋，服装必须真实完整，不能在行走中融化或改变。 00:08.00-00:08.70 女主停在镜头右侧，略微调整站姿，让旗袍褶皱自然落下，询问：「这套呢？」 字幕逐字显示：「这套呢？」 00:08.70-00:09.30 男主画外音立即赞赏：「好看。」 女主听完轻轻笑一下。 字幕逐字显示：「好看」 00:09.30-00:10.00 女主保持眼神交流，轻轻偏头，嘴角维持俏皮微笑，说：「留哪套呢？」 字幕逐字显示：「留哪套呢？」 字幕完整停留。 波形逐渐归于平静，画面自然结束。 音频：女主真实现场人声，口型精确；男主为镜头外中文男声，不露脸。 保留轻微电子氛围音乐（对白时自动降低，权重提高）、换装「嗖」声、亮相提示音，所有对白清楚可辨。 表演约束：女主不是夸张卖萌。 微笑、点头、整理头发、展示服装均自然克制；开场亲切，第一次换装俏皮，第二次换装更自信，结尾带轻微捉弄感。 男声说话时女主必须闭嘴并自然聆听。
```

看看第一版本的出来的视频

，时长00:10

<video src="https://mpvideo.qpic.cn/0bc3eiax4aabfiapmcvl6jvfciwdpyrac7qa.f10002.mp4?dis_k=112ce3d3038747f7e804a5a881ea9694&amp;dis_t=1791339898&amp;play_scene=10120&amp;auth_info=Ir+LyxhDVx+OpJXSCFlzezoWAhR3emRTKk4RbRdxNmwEGjg9WVgaaARjPRNkVFNvMA==&amp;auth_key=1ada3474f33834d4dec8385ae9ab7585&amp;vid=wxv_4697093171665911809&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

看起来的画面不集中，服装单一，中远景，人物仅占 30%，全身偏小，我让豆包工作模式两个视频优化对比一下

从这个表的对比来看，优化方向也有了。下面进行优化。

整个优化对比也是使用了Seed-2.1-pro 的多模态对比优化来实现的，后面进过多轮的优化参数和实现。

这个是优化后的效果：

![PixPin_2026-09-16_14-56-03.png](https://mmbiz.qpic.cn/sz_mmbiz_png/zw8bZHsVSaAOBZiaLkuNTbA4qTQeGGmsYBicSHibAXYolQJVUR8MpQmWeFSEGJDGW9unriaeicSqicMOiciazyTFssEK8w4bABCQxIGUrQOM8EO4JYc/640?from=appmsg#imgIndex=6)

请看视频：

，时长00:10

<video src="https://mpvideo.qpic.cn/0bc33ycjkaaediabeznoprvfjxwdsxpajfia.f10002.mp4?dis_k=85d979c7432d3c447bc8d236337555aa&amp;dis_t=1791339898&amp;play_scene=10120&amp;auth_info=VOHomaYoT1NKhfDJgltecHpmElUXJXpjCCIeQmtAej1qVE40agFUHj0PN2FDN1NQbmw=&amp;auth_key=4d0f345e4dc34ec8f7fba832ce29b04d&amp;vid=wxv_4697092028415967233&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

最终实现了稳定的出视频效果，并且 豆包工作贴心的给我总结出来了做视频的skill，大家可以直接拿去稳定出视频。

![Gemini_Generated_Image_cpm21zcpm21zcpm2.jpeg](https://mmbiz.qpic.cn/mmbiz_jpg/zw8bZHsVSaDppMvhKvYPaFOYphFhUwkruKBTqV45toFOiaMVKwVKnric0PbGAz7GnjkkQkHmrKf1xGaSHHmTPRGTKhx2D1gDukPhZeOiahibE64/640?from=appmsg#imgIndex=7)

Doubao-Seed-2.1-pro最新版本多模态理解是覆盖3D的。

刚好最近迷恋上了开发小游戏。脑海里马上想到了 小时候玩的吃豆人。那时候玩的是二维像像素点一样的。

![PixPin_2026-09-15_23-40-30.png](https://mmbiz.qpic.cn/sz_mmbiz_png/zw8bZHsVSaCYDUGD7xFN7lLIj7BusqobX8Al20LTQ7NonmuEg2AY8PNaicag0YZq8EHBReJvnTxesJas6ZDb8ZDpFL15t0xG3PCdjMwkJtWI/640?from=appmsg#imgIndex=8)

小时候很喜欢玩这些解压小游戏。今天突然有一个想法：能不能把它复刻成一个3D 的吃豆人？毕竟现在AI什么都能搞。

跟着我一步一步来看，我是怎么完成一个3D 版在线的吃豆人。先卖个关子，整个制作过程涉及多种工具。

有制作音效的、制作模型的、制作白模的、制作摄像视角的。

先来第一步，我们要制作一个豆子的主角。这里我用到的是 Seed-2.1-pro。结合建模工具Blender。

用Seed-2.1-pro 操作Blender的 MCP 和 Computer User 你来检查视觉，让AI去操作画这个豆子人模型。

2.1Pro 在整个 Computer User 上做了极大的优化。整体提效和节省 token 数都要比 GPT6快不少。下面来看看

提示词是这样的。

```
●●●帮我下载 Blender 并安装对应的 MCP。然后调用它的 MCP 和Computer User.来完成一个3D 豆子人的模型。我要让豆子的嘴巴能张合，呈现出很拟人化的吃豆子的样子。
```

首先去配置 Seed-2.1-pro模型

![PixPin_2026-09-16_00-17-35.png](https://mmbiz.qpic.cn/mmbiz_png/zw8bZHsVSaDJHL88XwgU07UpZNkxgZg6U3AHvXCzjeOE42zcrIUKzZMmgHykW4K0KicSlw6JZNdhxtnjUyG44HNjXupDLk52T40BTXztWiboY/640?from=appmsg#imgIndex=9)

图片中的 Doubao-Seed-Evolving 就是和最新模型保持一致的能力 此时也就是Seed-2.1-pro 模型

![PixPin_2026-09-16_15-13-28.png](https://mmbiz.qpic.cn/mmbiz_png/zw8bZHsVSaDVS23M0PaAqBrXgnt3zCK4b4oZj5RdaIpMVAf49IePyFxEuibEPNaKaOPSVaic0KypibZVCjm9oDMUiawCXxbqY9KEdwuEKNIqYxQ/640?from=appmsg#imgIndex=10)

它就直接自己操作，巴拉巴拉地打开 Blender。进行构建

全程大约花了10分钟。有动画的，还在张着嘴巴吃东西的豆子人。就已经构建好了。

说实话，说说，我根本不懂怎么操作这个 Blender。它从安装到配置MCP。再通过 Compute User 检查豆子的样貌。我完全没参与。

看到真的很震惊。感觉AI又卷死了一个行业。大家可以看看下面这个录屏。

可以显示查看预览

![PixPin_2026-09-16_00-58-23.png](https://mmbiz.qpic.cn/sz_mmbiz_png/zw8bZHsVSaA3mcJP5pOwtr8E1aBz5G5aqhYuh6BVp2dmErnepBdLt9PfvKOt4lpGH0D3TPVASnhNCQfq3VpX3LBLDnVy0VXECGDc8V2sSrA/640?from=appmsg#imgIndex=11)

整个动效录屏：

，时长00:12

<video src="https://mpvideo.qpic.cn/0b2e6yamcaaapuaetzvkorvfb5wdyh3abqia.f10002.mp4?dis_k=4baf30e372e7e91c2a5e87b1f1b93b4b&amp;dis_t=1791339898&amp;play_scene=10120&amp;auth_info=AZePmYgvQwRP2vTAhF9dcS01RA8Scn9gXn9CRzpHLz8/WEhjPwJYSThQM2hFM1BROT8=&amp;auth_key=9846360a1ff46cf7bf8d14a98e368269&amp;vid=wxv_4697095366427852802&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

看着还有点搞笑，有了豆人，还需要有幽灵。还需要有轨道，有豆子。

说干就干，接着，让 Seed-2.1-pro 继续构建这些模型。我这里就不给大家一一录屏了，给大家截屏看看。

提示词：

```
●●●继续完善3D吃豆人所需要的棋盘和幽灵。
```

同样是酷酷的干活。并打开了Blender。看到了下面的演示图。整个过程中，我没有参与太多干扰。

![PixPin_2026-09-16_00-40-48.png](https://mmbiz.qpic.cn/mmbiz_png/zw8bZHsVSaBfiaTeQXYmjgTtamVy0soflkicTGvPZwqwzPIgv2fMRpyeBlJ2sOvicWc101s1wNXUTOTvjLVcED0kZiapWQlZnjFlJZBETsGmxjQ/640?from=appmsg#imgIndex=12) ![PixPin_2026-09-16_00-41-54.png](https://mmbiz.qpic.cn/sz_mmbiz_png/zw8bZHsVSaCJLiclzibMFFSlkwR44rpPFb4zb3H73t5bykiaiaiaF4awe83fZTjJhkw45denRC4FJtyFbZaz6EsBGtibHfZ7dPRTicO5krgLMfXyDQ/640?from=appmsg#imgIndex=13) ![PixPin_2026-09-16_00-42-34.png](https://mmbiz.qpic.cn/sz_mmbiz_png/zw8bZHsVSaDYPOpg1mFlMD1RggSB6H5iaogdvHGPwgZH5jkaIA1iaicQTSy8fj29FMGbQHAniaKPjnvmMu8cdLkG5mb47xpCeBqVGDcyfryia390/640?from=appmsg#imgIndex=14) ![PixPin_2026-09-16_00-41-06.png](https://mmbiz.qpic.cn/sz_mmbiz_png/zw8bZHsVSaCRmS0YPzjp39q0kYFhzKicSW64pT9tkc9Wf0Y6CcaCHsY1Vn3KicR5sbpcnliaDYJ1fLxFXW2h4hOhEfrKMRLAgYcTqqOGJsk37I/640?from=appmsg#imgIndex=15) ![PixPin_2026-09-16_00-42-13.png](https://mmbiz.qpic.cn/sz_mmbiz_png/zw8bZHsVSaA8KgvKvMISY7GUJE4S2IHznj8BGib27AnXl47ucNvWhMpNibuLazveJpj5myicyUV6kFaplaySfZk5txZXlWxNa9bpq3vkzdA3gA/640?from=appmsg#imgIndex=16) ![PixPin_2026-09-16_00-42-58.png](https://mmbiz.qpic.cn/mmbiz_png/zw8bZHsVSaBSlREicCmozQzQGEFKxLY332JOOcNI3obkTZic1QxCj6J7IO027CoMESSJuNc6yTZU8sIcmhT8rUIA5ibLmKvgtHEK4NnBVgU9lo/640?from=appmsg#imgIndex=17)

虽然没有想象中的那么立体真实。但是证实了一件事：AI 确实能操纵它来做3D 建模的事，只要进行多轮的调整。一定会得到非常精致的建模。

，时长00:54

<video src="https://mpvideo.qpic.cn/0bc3hid5caahr4afs4vnxrvfoowd2e5apuia.f10002.mp4?dis_k=b154723fbc708cc008373bb6c90c3874&amp;dis_t=1791339898&amp;play_scene=10120&amp;auth_info=U4/Bz7l8FVcbiPDC0goIIH8yGVVAIX05WC1JEjpAKjdtAkg5PFQOGmwCN2oTZgUAazg=&amp;auth_key=8fe3ba30ae3696b85ebe45daab37db25&amp;vid=wxv_4697096059142225923&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

好了，现在所有的建模都好了，现在我们就开始组建游戏的运动。我为了能快速玩上这个游戏，使用了下面这个技术栈。

整个技术栈使用的是 Blender + Vite + React + React Three Fiber ，这个不会也没关系。

```
●●●Vite├─ React│  ├─ React DOM：菜单 / HUD / 暂停 / 胜负 UI│  └─ React Three Fiber：3D 场景组件├─ Three.js：实际 WebGL 渲染能力├─ Zustand：游戏状态├─ Blender：角色建模，导出 GLB└─ Web Audio API：代码合成音效
```

大家要想复刻这个，完全不用关心它是什么，直接告诉 AI 就好。

告诉大家一个小技巧：可以先和 AI 聊你的 plan。再让它执行。

这是我跑出来的plan。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/zw8bZHsVSaCv1kaCCMEg2ytpLnAZt7xLGeKBJoHqMoOHf6dU4I4oiaRt4DvfzPf7KoZiaO5ecoN4aicO5Z0eaAMU3ST0KcPHFppckJrCKAYz1U/640?from=appmsg#imgIndex=18)

大家也可以直接把这个 plan 扔给 AI，让它直接复现，直接coding。

大概跑了有20分钟。长程任务不中断。

![PixPin_2026-09-16_01-02-37.png](https://mmbiz.qpic.cn/mmbiz_png/zw8bZHsVSaDk8kaTJJMHSEHl3cvzt7A36fxbR9npgNyI91KvL5phFM0HMq5GwbmOOGoqZkBUzCtoiaqTyGDxETRhaYsLK3UGuLbuibYBfwHWE/640?from=appmsg#imgIndex=19)

经过几次的修改 我的第一个小游戏就生成了，给大家录了一屏。看看这个动效。记得戴上耳机，有音效。

对了，如果大家要用音效，不能直接去扒官方的，会涉及侵权。这时候我使用的是 Google 的 Gemini 来生成音乐的。

提示词是这样的：

```
●●●原创复古街机游戏吃豆音效。两个短促电子音交替出现：低音、高音、低音、高音。使用柔和方波与三角波，清脆、圆润、有弹性，适合角色连续吃豆时快速重复播放。无旋律、无人声、无环境音、无混响尾音，不模仿任何现有游戏音效。
```

![PixPin_2026-09-16_01-07-41.png](https://mmbiz.qpic.cn/mmbiz_png/zw8bZHsVSaBRsqKAdYwjmJb41K4o7CL5p7JaUERD2wUGicxKvvMXYMfTUSAJwA6nPG7C9cBZdLhBxP4iaZ0riahzEUqWNOYuJj4yabgnQw0F1U/640?from=appmsg#imgIndex=20)

用Seed-2.1-pro。把音乐给整合一下。迫不及待给大家录了一屏，大家看看。

，时长00:23

<video src="https://mpvideo.qpic.cn/0bc3teaiyaaa2maait5k35vfbgodrsmqbdaa.f10002.mp4?dis_k=d4e10337a82200d189644642b1cf02a5&amp;dis_t=1791339898&amp;play_scene=10120&amp;auth_info=AJ6N1JZ6E1JLjffD0lsLe3owEQZHIHU4XS5ORmxEKz8+B0szalUIHzwHMGsTNwZbbjo=&amp;auth_key=1076ac78e9b29c5e0cf62521d861f0ac&amp;vid=wxv_4697094270556045315&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

整体来看，Seed-2.1-pro 模型的 Computer User 能力还是不错的。

包括编码能力，以及对整个游戏规则、节奏调优，以及游戏的操作跟手性，都能达到可用级别，关键费用便宜。

**从理解需求、修改代码到运行验证的端到端开发流程，Seed-2.1-pro新模型表现还挺不错的** 。

新模型也已经上线了，大家可以去试试测测。

苍何

邀请你前往腾讯公益一起捐

我为家乡上大分

275人捐赠

AI · 目录

作者提示: 个人观点，仅供参考