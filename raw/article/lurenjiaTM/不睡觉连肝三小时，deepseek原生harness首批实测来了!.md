---
title: "不睡觉连肝三小时，deepseek原生harness首批实测来了!"
source: "https://mp.weixin.qq.com/s/2O2nLCXXnIyUovNvP1NOnA"
author:
  - "[[路人甲TM]]"
published:
created: 2026-09-10
description:
tags:
  - "clippings"
---
路人甲TM 路人甲TM *2026年8月14日 01:21*

就在刚刚，DeepSeek发布了自家的Harness。

梁圣上午发布V4 pro正式版，晚上又来偷袭，真不给友商活路了？梁圣的含金量还在上升...

![图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbBUDXNmBN8Le6QrUVSUl0W3Yq7VDOzd93Zwq9vVo4OJsTGzFs1Y8RcqZVlibB9ojpzDMzSicQr7kpfeSmJ3WqMRO5EEmduTEv9DA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

我已经迫不及待想感受一下DeepSeek的V4 pro正式版搭配自家的Harness会有多强了，深夜爆肝3小时先帮大家测实测探探水。

先说怎么快速用上

直接跟你的codex或其他agent发这个指令：

```swift
帮我从官方 npm 包安装 DeepSeek Harness。包名是 @deepseek-ai/dsh，官方仓库是 https://github.com/deepseek-ai/deepseek-harness 。请先核对包信息，再检查 Node.js 和 npm 环境，安装最新版本，启动 Web UI，并通过 HTTP 请求验证页面可以正常访问。完成后告诉我安装版本和启动命令。
```

我立马让codex一步到位给我安装好

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbCVYFGZxZjFnUpWgia3ZzjbibJMjDvgNfGFJMEtic3xVNU1SaJLoXicM1PqXqEA3cfmNEDpbotguNhwtpSk751Jx7aOtI3yXoMIWNc/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

Harness长什么样以及有哪些功能

打开之后需要先接入ds自家的API，然后就进入了这个页面，非常的简洁。

别看界面简单，一套 Agent Harness 该有的功能，它基本都配齐了。

它可以读取和修改工作区文件、执行命令、搜索网页、调用工具和 Skills，也能管理任务计划和上下文，把复杂任务拆给多个子代理一起处理。会话、权限、沙箱和运行轨迹也都有对应入口。

简单理解，它已经具备了一套 Agent 真正动手干活所需要的基本能力。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbA6G6hr55fDIF1snnYbmoHMldicN24l9kUCGNmYty1YWMHRiaVgBiaLIY7vX94O1emhqc2zIv0uVahae0um8iamKXl3Jo6myHPicAkA/640?wx_fmt=png&from=appmsg#imgIndex=2)

再一起来细看这个主界面：

![图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbCfs5gU1icicfDmGdWRCnCOFCbHok7KibIvAznwRsomU2M1YbuhFWSY4132WquLnW8BakgKvVoa3Mfjft323MuVhCia49PKd0EK6n4/640?wx_fmt=png&from=appmsg#imgIndex=3)

蓝色框中的就是自己选择的文件夹，也是ds将会处理的任务区

右下方的红色框中可以选择模型和思考强度

绿色框中是有三个选项，就是一个权限的设置，分别是只读、可以在工作文件夹中干活以及完全放开权限。

别急，我一会就把默认的工作区操作权限改成完全放开。

无视风险，继续操作.jpg

这些都是老朋友，没什么好说的，但是上方的红色框值得展开说说，这是ds自己的特色：

![图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbBDkPhXN8Dp8oK2GzB88JtbMszI92h32LoW5urzZRjbYH8ibYMGFhwePLLvzgibkkiaUGIzLYrehyfSKBpZGgeBr8nDYPUmiaw6dO8/640?wx_fmt=png&from=appmsg#imgIndex=4)

可以看到这里有四种模式可以选择，乍一看完全是一头雾水，我们直接来看看它自己是如何给小白解释的：

![图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbC5PNm7DKpOIRuutBBr7dHew9zhtrlKicdB49ibb6u5cguNlwycPiaMmo49brZ52sEnIvvNyCChvsGqvbsvJAuwX3z2JEV3LletibQ/640?wx_fmt=png&from=appmsg#imgIndex=5)

简单来说，实在不知道选啥就默认标准模式，它覆盖了90%的需求。

根据具体需求，你也可以选择其他模式：

1. 批量任务：要做一些批量任务、做一连串的固定操作，就选PTC模式
2. 专心写代码：只想让 AI 专心地改代码，不要任何其他花哨的功能，就选极简模式
3. 自定义：要是想把模式改成自己顺手的，或者干脆做一个新模式，就选创造模式来实现

DeepSeek 官方还反复强调了一个设计理念，叫「一切皆插件」

模型、工具、Skills、会话、文件系统、沙箱、多 Agent 协作，甚至界面本身，都可以像积木一样拆开组合。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbDtjhJvcICyQ0ICMCibHy8pLntKcEoCL1od4ZchQs6XEYiaNDBH0Eo4PxfT90H8y0rE20HuHNlTYZEpswWhUOWj9ZkNgx49VQHmY/640?wx_fmt=png&from=appmsg#imgIndex=6)

举个最直观的例子，你可以通过插件给 Harness 增加一个任务进度面板，运行后直接显示在界面里，不需要时也能随时停用或删除，不用修改整套系统。

这部分的可玩空间其实很大，不过我这次还没有细测，就先讲到这里。

后面有时间我准备单独再玩一遍，看看它到底能把 Harness 改到什么程度。

介绍完了功能，来看看这个harness在实际任务中表现如何。

## 实测看看效果

### case1 3D 黑洞引力模拟器

之前我用Claude和hermes都接过deepseek，这次终于能把deepseek接到自己家的harness上了，这个案例统一使用deepseekv4pro模型，接入不同的harness，横向对比效果。

Claude harness 用时25min

，时长00:14

<video src="https://mpvideo.qpic.cn/0bc3iaaukaabj4al3hd4n5vfcqgdivaacria.f10002.mp4?dis_k=a962de42f783c294940aae7de9eff1b2&amp;dis_t=1789027472&amp;play_scene=10120&amp;auth_info=WPyJpf4yVVw6142glQoaExBAPAx6O2VLHio7SjB6PktiLk0xERlOEU0TSX19ZxczBEo=&amp;auth_key=4033284e0ee3b52fd4afad3fd22717f0&amp;vid=wxv_4648096294828474369&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

Claude的harness还是比较权威，跑得很快，而且整体的视觉效果我觉得也是最好的，交互需求都实现了。

Deepseek harness 用时40min

，时长00:15

<video src="https://mpvideo.qpic.cn/0b2exuaekaaa5ual25d5znvfbpodiw6qaria.f10002.mp4?dis_k=9537e4820fbd6ba73b68a18eafa08d37&amp;dis_t=1789027472&amp;play_scene=10120&amp;auth_info=UoGD3opmWl0+iIn2y19LFkhMOQl7amlLSHthHWUqZkhoeEtoEU1BEElMTSsjMkY2XEY=&amp;auth_key=88b9819b43236aa43caaee15bd94cf92&amp;vid=wxv_4648097374945558528&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

这个视觉效果整体感觉真的非常炫酷，根据黑洞质量、时间、速度的变化也非常丝滑，就是速度稍微有一点慢，运行了 40 分钟。

Hermes harness 用时42min

，时长00:09

<video src="https://mpvideo.qpic.cn/0bc3huaakaaa24ape6l5wjvfapodau6qabia.f10002.mp4?dis_k=574f2f97b928457f12a87dc2e041785f&amp;dis_t=1789027472&amp;play_scene=10120&amp;auth_info=UMDnoIgwAQo63tz3xANNR0ROPlgsOGhOGiQxQWd9MBlqKBxoRxgaR00aGCosbkBnUEQ=&amp;auth_key=237a1d2f546b54a45764288ed1925057&amp;vid=wxv_4648095670011428866&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

Hermes 就比较拉了，大概用的时间和 Deepseek harness 差不多，但是出来的效果很不好，比较零散，细节也很少。

这个案例虽然不能代表全部，但至少可以看出来，harness本身对模型做任务的影响还是很大的。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tp5fgmUBUbA9VnUKPJjek5ZFgaL2kFSSf5FCHEEwkMkp3DMmaWwiaqos2T6JLsPN8LSMM6u97G4uJ1DOaaLrDAAeXrI7YLN46gibSmfBvVRBI/640?wx_fmt=jpeg&from=appmsg#imgIndex=7)

这样测下来看，相比 Claude 在速度上肯定还是有一些差距，效果上我觉得可以持平，和Hermes相比就完胜了，预测在中上水平，并且这个还是预览版，正式版很值得期待啊。

### case2 创新模式：做一个自定义agent

我对创造模式的理解很简单。

其他模式是让Agent直接干活，创造模式则先把这个Agent配出来。它能做什么，平时按什么规矩做，都可以提前写好，以后遇到同类任务直接调用。

为了看看这套玩法能不能落地，我让它创建了一个门店宣传助手，专门给不懂代码的小店老板制作宣传网页。它会主动询问店名、主营产品和宣传风格，页面要适合浏览，做完还要启动检查。

```
这个 Agent 面向不懂代码的小店老板，主要负责制作餐饮、咖啡店、甜品店等线下门店的宣传网页。
```

这个任务并不是一口气跑通的，过程中出了一段小插曲。

DeepSeek一度反复执行 `Bash noop` ，思考里明明已经提醒自己应该调用 `preset_ops` ，下一步却又回到了同一个占位动作。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbCNdq5ibzAjPov6zzTe1picaHH3CrG1HDkh3yZI3Gib8UOEkoiayxFXj3AbWr64lm6plaUwwKe5SHb5hPHiakw0pAdvNBW32tkXlFh4/640?wx_fmt=png&from=appmsg#imgIndex=9)

我随后终止任务并追问原因。

它解释完后就终止了循环，它改用文件系统继续操作，最终生成了预设文件，也通过了加载检查。

这个问题没有让任务失败，但过程确实不够顺，看到连续几次相同操作时最好及时打断。

新建会话以后，可以看到「门店宣传助手」直接成了模式选择里的一个选项，可以和其他模式一样直接选择。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbA0tvTRoicZEyQ3S5vMtXtEYb1U9tVtOQGTKPsY0ZM47Lr5PDz2X6tlPK6picKzQXGMrmaV7IQJ5Pc8BVcezTCeCDIRn92z3D0lk/640?wx_fmt=png&from=appmsg#imgIndex=10)

来试试这个agent，我故意只给了它一句信息不完整的需求：

> 帮我给新开的甜品店做一个宣传网页。

其他什么信息都没提供，它先向我补问关键信息，问题数量控制在了三项以内。这个反应正好符合创建预设时写下的规则。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbBDTIE8xQHqGafk36IqkxsUVHnCTuXFqQX6vt47sUTRas9l7Uvg3OGqPqicb6Kyr2chhWOh1Ay2w30oWIvSUE14On1uwNZ6nPO0/640?wx_fmt=png&from=appmsg#imgIndex=11)

补齐信息后，它继续完成了网页，并检查了显示和页面运行情况，用时3分钟。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbDaiaibd6iaKHP3hVzGHmFS30LalvodzfVwFYR39nT9K3o1p90OYM7Yj5ibaquJWpwphC9fcdGTNiaqB1sy1cjsN82Y3voGiapibcHPhI/640?wx_fmt=png&from=appmsg#imgIndex=12)

，时长00:12

<video src="https://mpvideo.qpic.cn/0bc3tmauqaabvmalgdl4nzvfdg6djcnqcsaa.f10002.mp4?dis_k=ee1dff56044ad9a6d6e2ea8b2726041c&amp;dis_t=1789027472&amp;play_scene=10120&amp;auth_info=WOywu2YDAD3c3/TFC0wQEhxvD3o4N0xOLTdNMiw+Hm1+SzVCGRhNShgbKS1mQTAGFg==&amp;auth_key=7d1f08352d654e23a5e33f8f7abc7162&amp;vid=wxv_4648109727825264640&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

其实标准模式同样能做出一张不错的甜品店网页，而自定义Agent的优势在重复使用。

店铺信息每次都可以换，提问方式、手机适配和交付检查这些固定要求已经留在预设里，不用开一个新会话就重说一遍。

偶尔做一次网页，直接选标准模式更省事。

经常处理同类任务的创作者、小团队，或者想研究Agent工具与行为配置的人，会更适合花时间折腾创造模式。

### case3 复杂数据处理

最后我决定跑一个复杂的数据处理任务，分别将DeepSeek v4pro接入在目前国内最好用的WorkBuddy和ds的原生harness中，各自进行几乎一样的任务，看看哪个更强。

左手边是ds原生，让它处理四川卷下，右手边是WorkBuddy，让它处理四川卷上。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbBm4akOSE7A8nLgF2eoQ2CsLAIwhLYqBgpibibyXCK9bibpeaS3FwqZRvQD8HFbIcvYBy4ama9dps0icnK1piajAZarkbRa2yRTFMs0/640?wx_fmt=png&from=appmsg#imgIndex=13)

33分钟后，在WorkBuddy中的ds模型交出了答卷

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbCUQk4A3sxx8pibjG4a6EhIG3DQSpJ2TyzIaFiaxn69YibfdoRzRXoMOalTtC17IfTcjIicPYHqq78pmeBeW1dsXvmheMK2JycAbiaI/640?wx_fmt=png&from=appmsg#imgIndex=14)

不仅顺利完成了任务，还发现了已有处理流程中存在的问题，给出了自己的修改建议。

处理完毕的文件我也大致浏览了一遍，扫过去没发现问题。ds的模型能力确实可圈可点。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbAYWuAPhCHrlibDXFUDDcuiaUj14jJLQkPafb8I5DMkDn1oImVCc0qibNSRjhKTJtoZZwVDDDicYQn8YnbzXhJ51vjZMBSAwQlaaiaw/640?wx_fmt=png&from=appmsg#imgIndex=15)

转头再看看ds原生harness这边，结果发现在跑了二十分钟后报错停下来了，无奈让它继续。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbD7RxsAAGorPDHLktuZ5Z63oV086pibDzSiaG8jOCiaEUBUM5QpPrSzDYewDeybfh1a2kmJhHQwnwsG9zW1wHtsXH2JZVfvUIYpsY/640?wx_fmt=png&from=appmsg#imgIndex=16)

最终耗时将近50分钟也顺利完成了任务，我检查了一下产出数据，质量上和前篇一样，没什么问题。

但是怎么说呢，确实没有达到我的预期。

### 小结

原本以为ds的模型接入自家的harnsee中会呈现出很强的效果，实际体验下来

任务确实能做，质量也没什么问题，但是耗时比接入其他成熟模型多了不少。

不过ds官方也说了，现在属于公测阶段，说明目前这确实还不是一个完全成熟的产品。

只是一直以来ds模型的强大让我，可能也让大家，对这个harness的期望拔得很高，对比之下有了些许失望。

不过我愿意再等等，相信ds的正式版原生harnsee会给我带来真正的惊喜。