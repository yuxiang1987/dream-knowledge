---
title: "DeepSeek Harness发布，爆肝实测一天，夯爆了还是拉完了？"
source: "https://mp.weixin.qq.com/s/DbEaleVPbVDFfhSUocTrKQ"
author:
  - "[[小林coding]]"
published:
created: 2026-10-23
description:
tags:
  - "clippings"
---
小林coding 小林coding *2026年8月15日 15:15*

大家好，我是小林。

这一周可太热闹了，DeepSeek 来了一波王炸级别的更新。

DeepSeek V4 Pro 正式版上线，还发布了期待已久的 DeepSeek Harness，依然是开源的！

DeepSeek Harness 开源短短 2 天，现在已拿下近 100k 个 Star。非常猛，照这个增速下去，说不定真有机会超过 OpenClaw 的 Star 数，哈哈。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX3J0ibZhXhOJswPQMzDolOPRVib2rqZibXljKykHjtC0YVcdceCq2RsfTu8XFAxMlCp8yArMaErAfJxysJMATlcAb2riarWlceW37k/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

Harness 这个词听起来可能有点陌生。简单来说，模型是大脑，Harness 就是模型的身体。所谓的 Agent，可以先粗略理解成「LLM + Harness」。

以前我们用 DeepSeek 模型，大多是把它接入其他 Agent。这次 DeepSeek 自己下场，做了一套给自家模型用的 Agent 框架。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX3UrHkOvjr0VC5oQ8ktsstEF0jyRm9nq70Siahb5BYgECJYW7UT58TT8YEwPQ1zfrvbYBb0icVFhlrXuhcSia0IfXnnDSv0iaDGCdg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

而且 DeepSeek Harness 的设计理念也非常酷，就五个字，一切皆插件。

怎么理解「一切皆插件」呢？DeepSeek Harness 里的模型、工具、策略、存储、沙箱、上下文管理和 UI 等能力，都像积木一样可以拆装。这套架构设计得很牛逼，自由度确实很高。

在 DeepSeek Harness 内测期间，已经有开发者做出了很多有意思的页面插件。

比如二次元风格。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX3NxAbxBp6Q0OaQd1ibIoSPBPY0VC70BpYT2l16RZiaQz6ibHVialoJQ3yH8jFvQEpaK6zKKib81JVic9KicO1rPBbOlf9znsDsyZ1hxk/640?wx_fmt=png&from=appmsg#imgIndex=2)

还有这样的 TUI。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX2E5Mgvm3DicQXB8lEK1MvciaLDoO9V2WezCun6gdC6fm8NXszvibZRzMbjZ7raeSF6FB03nS66azrRmlI5vImicm1o3Xoh6Iqkbh4/640?wx_fmt=png&from=appmsg#imgIndex=3)

甚至还有这种复古门户网页风，脑子里「是兄弟就来砍我」那句话又闪回了。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX19ZEGefEe4vibOWsMzRianOzAQGwxesq5ELugFmoF8cn3J9WtBAtxvNC0icJCUDqIIkw4UkPUXjr0GFcibaqGEl9fGaCsF9I9lEFE/640?wx_fmt=png&from=appmsg#imgIndex=4)

从我看到的设置页来说，目前社区插件已经很多了，往下滑都滑不完。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX0CXr2NQA6AOvIAPHBuDEJ32kic5Z7UPL1Xria7Ve8mKgMEVHhPx2KeJ18miaNnsf3U4Q6dX7TSE4FdRDD1j9Kwlesjjia9kibGXDu4/640?wx_fmt=gif&from=appmsg#imgIndex=5)

这些换皮肤，只是插件最表层的玩法。dsh 的插件还能更换系统提示词、注册新工具、接入 Skills、管理上下文，甚至改掉 Agent 的执行方式。简单来说，连 dsh 自己都可以重新组装。

说了这么多，我们来实战一把 DeepSeek Harness。下面我把它简称为 dsh。

## ────怎么使用 DeepSeek Harness？────

能让 AI 动手的就让 AI 动手，我们要成为 AI Native。直接打开你常用的 Agent，把下面这句话发给它就行了。

```
●  ●  ●

帮我安装 DeepSeek Harness https://www.deepseek.com/harness/
```

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX2FlbZToQONXJWm2NSAccwnz5ybGekayw7Ga3TicfkBwG98fsEicGwlFNcUibmDQG6ynqESv6voQnHTDo6ibrocGuOrPHkbGsnAl2I/640?wx_fmt=png&from=appmsg#imgIndex=6)

我这次大概花了 5 分钟就安装好了。安装完之后，执行下面这条命令。

```
●  ●  ●

dsh web
```

然后浏览器会直接打开这样一个网页。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX2ZGfgoMc24judO7wjdFNVJhgibMys7CLU0joYA59TRVWgtehYDhMSnnEB8WmjB0m9o2lZE7m8Y5PrntKbiaWu8pASIrm5eEWMa4/640?wx_fmt=png&from=appmsg#imgIndex=7)

我一开始有点懵逼。我以为 dsh 会像 Claude Code 这种 CLI Coding Agent，又或者像 Codex 这种桌面 Agent，没想到它打开的却是 Web UI。好家伙，DeepSeek 又创新了一波。

接下来，去 DeepSeek 官方 API 平台创建一个 API Key。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX0jRRuypIL7bDZFkJkx4t8NveXoicpjYRxCuPSZswgSQDX2YjrppzzCKtWZ7aB5sdRqU3cWSC3KgOg09jspLIKX9qrJhjx8Nx6Y/640?wx_fmt=png&from=appmsg#imgIndex=8)

把 Key 复制到 dsh 的网页里。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX07jfgRLpVxMUR1VicZsTEEOficapuTbz9y910ebaLuNCOqA33SOEIV9FtB4hbWODMEbPsw4HpV4juWYZtXfQQWJOnvfZ4AFBs7Y/640?wx_fmt=png&from=appmsg#imgIndex=9)

填好 API Key，dsh 就可以正常使用了。

对了，使用前记得先往 DeepSeek 账户里充点钱，调用模型消耗的 Token 是需要计费的。

## ────DeepSeek Harness 有什么功能？────

第一次打开 DeepSeek Harness，我先看了两个地方。左边是大家很熟悉的对话历史，中间是任务区，可以选工作目录和运行模式。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX3wJLLH5vGCpO5ymo5lD5ia92W66kyXPpxpM9sx7nREopgEsSJ3ibr8NJA3rnHibL75ibv3PUaE3nicuS5D4HibFN1N3WicBUOR1qVtwM/640?wx_fmt=png&from=appmsg#imgIndex=10)

dsh 必须先选择一个工作文件夹，才能进行对话。先在电脑上建好一个工作目录，再让 dsh 打开它。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX0YSd27P76G2KJYj7HPWc0tsBjaU3jicI19qINP9c9FIM66ZPmo2X4ia8KUjxqcAQ5WsI8caQhSMSZpZdkpuXgz4EyABKeqPibmMc/640?wx_fmt=png&from=appmsg#imgIndex=11)

接下来就可以正常对话，发起任务了。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX283HsrMvUZ4H7de8YJEibicG9MA5E4R5uBic8GibSz6q6X0vgXPo19eK2OHibX4D6zAwkWibyZggXT416eUia2SQZSolspJXxTliatiaJ8/640?wx_fmt=png&from=appmsg#imgIndex=12)

对话框右下角可以选择 DeepSeek 模型和推理等级。目前我在页面上看到的默认选项有 DeepSeek V4 Pro 和 DeepSeek V4 Flash。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX2k6OBWEq7wrCVrNdqibQyE7icaxMVicicptUtibchQNZvQQocMOU1sZVSH1rR11ibYITx8k6RsXasgq6tAjJc44EMI5WHoKy8uE7EnQ/640?wx_fmt=png&from=appmsg#imgIndex=13)

对话框的左下角也可以对工作目录进行权限控制。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX0j8t7YYdnIGgBqaJX8oiaLicZmQE54uTu0LiavFHIY2wC4Hanuu57w0jRdiacibIsqulSQ20icTicibibDVwRUsV1gNA6Q2MicBdFPB0pw4/640?wx_fmt=png&from=appmsg#imgIndex=14)

这三种权限，决定了 dsh 到底能不能动你的文件。

• 如果你只是想让它看看代码，选「Read Only」。它默认只能读，不能改。

• 需要它直接帮你修改项目，就选「Workspace Write」，这也是平时最常用的一档。dsh 可以修改当前工作目录里的文件，遇到超出范围的操作，会先问你一声。

• 至于「Full Access」，简单理解就是把护栏拆了。工作目录内外的文件它都能改，也不会再弹出确认。这个权限别随手开，只有你清楚它接下来要做什么时再用。

权限搞清楚后，再来看模式。dsh 这里不只有模型选项，还多了一组运行模式。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX2GGHIAjhh2dJ2oQex1sUbkWHRfsam6oGmPngzppPxU0dr72WnfsywgtKkicjyEpQm0QPmxya2xGOMbZuDAiaNeQkFUgdMSuEDzg/640?wx_fmt=png&from=appmsg#imgIndex=15)

这些模式是什么呢？其实不用被名字吓到，四种模式的区别没那么复杂。

• 标准模式 平时用这一档就够了。看文件、改代码、跑命令、查资料、调用 Skills、安排子 Agent，这些常见操作它都能做。如果你只是想让 dsh 完成一个正常的开发任务，直接选它。

• PTC 模式 适合步骤多、流程长的任务。它拥有标准模式的全部能力，区别是会把多次工具操作写成一段 TypeScript 程序，再串起来执行。这样中间数据不用一轮轮塞回模型，最后只把结果送回上下文。碰到工具调用特别多的任务，既能少几次来回沟通，也不容易把上下文越撑越大。比如批量处理文件、连续查询数据，或者跑一整套操作流程，用这个模式会更合适。

• 极简模式 只给模型留下两件基础工具。一个用来执行 Bash 命令，一个用来修改文件，其他能力全部拿掉。它更像是给模型做「裸机测试」，适合观察模型只靠命令行和文件编辑能做到什么。日常使用不用特意选它。

• 创造模式 给想自己定制 Agent 的人准备的。你可以查看 dsh 当前的运行环境、试验不同插件，再把需要的工具和能力组合成一套新的 Agent 模式。简单说，前面三种模式是拿来干活的，这一种是拿来「造模式」的。

如果你要配置插件，可以去设置页面里找。目前官方内置插件已经有 100 多个，后续数量还会继续增加。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX3d1Oaqv078ibIwbdkmfIJL1S3QOmgV0ziblQK0Buet4cCtRhpB9YpVrv8BJ2BpuibowFMXwXze90icMalKVgdzeZGkobelT3mmNUM/640?wx_fmt=png&from=appmsg#imgIndex=16)

到这里，dsh 的页面和基本功能就讲完了。

接下来，直接实测一波。这次我主要想看看，同一条提示词分别交给 dsh + DeepSeek V4 Pro 和 Codex + GPT-5.6 Sol，谁做出来的效果更好？

不要问我为什么不顺手测一下 Claude Fable 5？因为我的 Claude 前两周被封了（落泪 T T）。

## ────DeepSeek Harness 实测────

### 01｜八足蜘蛛运动动画

先看第一个实测，做一个八足蜘蛛行走的轨迹动画页面。这一次的提示词还挺长。

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX1BRFXdDPtvfDBRqcY63icBq6IoWYUiabVVbS02ZMmCdrMsFeDINIIucoZiaSx3QkgMgKxZIDBMsMxQNBsm6jXGM59ISf6M7Ze3c8/640?wx_fmt=png&from=appmsg#imgIndex=17)

dsh + DeepSeek V4 Pro(Max) 跑了 15 分钟把任务做完了。任务结束后，dsh 也会把本次任务的 Token 消耗和缓存命中等信息列出来。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX22EN1sQ1SGYwaAz7tYOt2KIV22NvOHr8fvPlp6Q0GBJEW2ScLEiaiaINP7Mbz2xY5ibg7AjFhcBR6DNcvvcrcWq1FJuJHUnXogxs/640?wx_fmt=png&from=appmsg#imgIndex=18)

还有一个设计我很喜欢，dsh 会展示本次任务的完整轨迹，可以回看它是怎么一步步干活的。这对想学习 Agent 执行过程的同学很有帮助，有点像浏览器开发者工具里的请求追踪。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX3TyykicXr1Z4fIEjS3e3OuE6ZsKZGv9Gb7BHaoEic52Tia5RwlwxlPHUWdKyJyZvP6MxeeeIy78bqPlO9Z0YEYFatb4mLGNF4NdQ/640?wx_fmt=gif&from=appmsg#imgIndex=19)

而且它记录的不只是最后的聊天内容。模型收到了什么提示词、调用了哪些工具、改了什么文件、怎么压缩上下文，这些过程都会留在任务轨迹里。所以哪一步出错了、Token 花在了哪里，基本都能顺着轨迹往回找。

但是没想到，我一打开网页就懵了，蜘蛛呢？这不是翻车了吗……

![【dsh + DeepSeek V4 Pro（Max）：首次生成，页面没有显示蜘蛛】](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX2rvTEicQy6JKADnzWWj2yneLeUdGqzyKeEiaNjDpUyRnfYUF2lYufvXhUYG5lKVdPVOAKGdgQvSwtoekic8IFaUjDkZ17eJE3Epo/640?wx_fmt=png&from=appmsg#imgIndex=20)

【dsh + DeepSeek V4 Pro（Max）：首次生成，页面没有显示蜘蛛】

我把相同的提示词丢给 Codex + GPT-5.6 Sol，不到 10 分钟就完成了，而且是一次直出。蜘蛛走路的轨迹很稳，腿部动作也比较自然。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX1eRoaiabU2AHIoSR7uyshKyh89aBqopz51XXQiaicLU3A6iadLEmmmwecqDyzGrakXU5nWRINHEANZjBVDs4fo0BUvYQH8XEyOjNM/640?wx_fmt=gif&from=appmsg#imgIndex=21)

▲ 【Codex + GPT-5.6 Sol：八足蜘蛛运动效果】

然后我让 dsh 排查一下，为什么网页没有显示蜘蛛。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX2KxZsDeCTdtJtNX4LAicp5OBOdfWPR8UJsw6vubU8ZsXck7kBQKD6pb6FdkOPic9alYPvz8FC4Q5ibGKFc7uAUibXK7plkrbwPMuY/640?wx_fmt=png&from=appmsg#imgIndex=22)

DeepSeek 的任务规划做得很好，它知道应该先去浏览器截图，看看页面的真实情况。但从这次任务的反馈看，DeepSeek V4 Pro 没法直接读图，所以它又绕了一弯，尝试用 PNG 解码器分析图片像素。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX04DG7UG1kovosfmCZt9jGmePOJsyhAFH0m3G24GVe1FcH0xicHCu90tZYlOAvrOFSkOsQgGL5JtHBwqRRbibIUgyDd38LMhiaumE/640?wx_fmt=png&from=appmsg#imgIndex=23)

dsh 排查问题的过程中，我本想再开一个新会话做其他测试，结果又发现一个体验很不好的地方。

当有一个任务正在执行时，我想开一个新会话，结果怎么点都没反应，新工作区也打不开。我当时还不知道这是 Bug，还是自己的使用姿势不太对……

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX31Akye1iaWSEUJbganZL4E5o8fkDDpQYJtRekkDqRHPqV3gEIQ4ibmUXSL3qaCt2ef6lzOfgR1QzpAT1K8Xet9YQQy0GQBEX3hM/640?wx_fmt=gif&from=appmsg#imgIndex=24)

我苦等了快 30 分钟，还是没有出结果……

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX3umNHd1F9bxWVemnrUx8RgzCtfCcicG8ib3KSxtGeQVZuwkdR7ZwEVr2tBzav46yT9h6omK41WO2WbWMm3QI9RqT0JQmv5HsED8/640?wx_fmt=png&from=appmsg#imgIndex=25)

等到 30 分钟后，我实在没耐心了，就刷新网页看看。结果你告诉我，dsh 很可能早就已经停止运行了？那我前面的等待了个寂寞？

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX1VfeVDeOBNyHABuuZ4vC7rSghibDXAXlKohZYvxomXNKT8FB1HtLj964cuQ05WnPjW2XNzq8v6KmKZ9KRiaEqFSibJw3unoNzDn4/640?wx_fmt=png&from=appmsg#imgIndex=26)

最让人迷惑的是，当时任务的执行时间还在一直增加。看起来任务还在跑，实际却已经没有结果了。不刷新网页，根本发现不了这个问题。

到这里我才恍然大悟。前面无法打开新会话和新建工作区时，dsh 大概就已经出问题了，只是页面没有及时告诉我。这一点真的很无奈。

不过 dsh 目前还在内测，出现问题也不意外。这种状态不同步的问题，希望后续能尽快修复。

测试还得继续。我回到终端，再次执行「dsh web」，重新启动 dsh 网页。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX3AtbUKGKYdhTSGcQudnUc9eJE1HZKOFPdicczcfypFnPTEDmCUeW7SiaicwjmzsP1AWibekce77SZplAwPEH1bgmoibafFXCPUUyZw/640?wx_fmt=png&from=appmsg#imgIndex=27)

继续排查蜘蛛没有显示出来的问题。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX2yJmrOjhS43J1Vy94REKwwVsPdnOUnKibwKxyG4RJERsdmTK3d0tAVdeUEwtriaqRibuBsZ4Kl5nVlkcAR0yQjq2UUbUCvyVU30o/640?wx_fmt=png&from=appmsg#imgIndex=28)

从这次任务的表现看，DeepSeek V4 Pro 处理这类需要看图的网页问题时，确实会比较吃力。这一轮排查足足花了 35 分钟。

下面就是 dsh + DeepSeek V4 Pro（Max）修复后的效果。蜘蛛行走的姿势挺稳，只是身形稍微小了一些。

![【dsh + DeepSeek V4 Pro（Max）：修复后的八足蜘蛛运动效果】](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX0GemSkuxibTiareDVfGdYqeAj0GYZLtyiaxUEnLByN5XQuKOKMiatLibjIy0iaQPdufN2fLkLDZWK2O4TeAgeiaUxmGeibibdCG4T6EWB8/640?wx_fmt=gif&from=appmsg#imgIndex=29)

【dsh + DeepSeek V4 Pro（Max）：修复后的八足蜘蛛运动效果】

▲ 【dsh + DS V4 Pro（Max）：八足蜘蛛运动效果】

然后我又开了一个新窗口，把 DeepSeek V4 Pro 的推理等级从 Max 降到 High，再跑一次相同任务。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX0ZttdEdt1ecb3SUMoP5icOeH2MQCnCyR1829YIXSSk6QMQdmaqgerUP2Ix2xO2M3EiaB3ZGwIDPMQrucVbDUmlZRRUbvOtPuyos/640?wx_fmt=png&from=appmsg#imgIndex=30)

这一次跑了 17 分钟，一次就生成成功了。八足蜘蛛已经可以正常行走，不过几条蜘蛛腿看起来有点黏在一起。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX2jJcfw4G4xImekg690RJibydBlrEu53icwql7QsO2GxSn1Xt6RDlcxQxg0TU3JPia5IDJDJsfxH1lZFS56zJHsTvLZF10UsKEVdo/640?wx_fmt=gif&from=appmsg#imgIndex=31)

▲ 【dsh + DS V4 Pro（High）：八足蜘蛛运动效果】

然后我又测了 dsh + DeepSeek V4 Flash（High）。这一版也是一次生成成功，只不过蜘蛛的腿明显更短。

![【dsh + DeepSeek V4 Flash（High）：八足蜘蛛运动效果】](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX0xd4EWlZMfrj2IA1dF4J9cJydNtc8SIbCBK5vCfXv3VdmyibkmqiaS8c4MuCAw41wVVOwFw7KiaKCMPFiacicviaTSUOHLoaQs5drDY/640?wx_fmt=gif&from=appmsg#imgIndex=32)

【dsh + DeepSeek V4 Flash（High）：八足蜘蛛运动效果】

▲ 【dsh + DS V4 Flash（High）：八足蜘蛛运动效果】

最后我录了一个更完整的对比视频。左上角是 GPT-5.6 Sol，左下角是 DeepSeek V4 Flash，右边上下两个都是 DeepSeek V4 Pro。大家可以重点看蜘蛛腿的步态和身体的稳定性。

，时长00:20

<video src="https://mpvideo.qpic.cn/0bc3paauwaabxiapa3t6bfvfc6gdjn4acsya.f10002.mp4?dis_k=6f7926aba715d1d9df707f54753b6bb4&amp;dis_t=1792736823&amp;play_scene=10120&amp;auth_info=DvnN2th/G1ZgksmixgdTJR0sJmAJNkARZBIvPG9WHjAwU2VkfnFGOQI+Qg0qJUQfFw==&amp;auth_key=de2c55508c73c9558a00bfdf355a89ae&amp;vid=wxv_4650036323066494979&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

严格来说，这一轮还是 GPT-5.6 Sol 的效果更好。不到 10 分钟就一次直出，走路的运动规律也更自然。

DeepSeek 在腿部细节上稍微差一点，但整体差距并没有大到离谱，至少没有出现蜘蛛腿飘起来的诡异感。

### 02｜3D体素风足球动画

第二个任务是 3D 体素风足球动画，我给 dsh 发了一小段提示词。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX0JQmg8l177Agoib0N1UzU3VaIS5wUBqnmtDa52e1IIQzNqUypB3uJoJ9QPohRZKNjBvXyK9p6fdMpjg2DgyP8GtKz1rDYaEBicE/640?wx_fmt=png&from=appmsg#imgIndex=33)

先看 dsh + DeepSeek V4 Pro 这一版，重点看带球和射门之间的动作有没有断掉。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX0e8SyFRXvAEZYDoulibzARIAWXTCCVotN3aqmkD0Qqzycls8ftTS2BdklFeIdq2nZfOdhvA6qJTicn39lqYqdqkXFtEebs3iaV4o/640?wx_fmt=gif&from=appmsg#imgIndex=34)

▲ 【dsh + DS V4 Pro：3D 体素风足球动画】

从带球过人到最后射门，整段动作基本是连起来的，非常丝滑。

再看 Codex + GPT-5.6 Sol 这一版。

，时长00:14

<video src="https://mpvideo.qpic.cn/0bc3yiaemaaaymapvvt76nvfbqwdi3baarqa.f10002.mp4?dis_k=25e7e44cce4ae7d7a2d46912fce19e2e&amp;dis_t=1792736823&amp;play_scene=10120&amp;auth_info=CKDLk5h3HAYxlprwyFBRcBwudGVdN0YRahd7b2tXQTQ2AjMyLX5BaVM6EV8kckZKFg==&amp;auth_key=886399487aea97d1c0615ca01d8ffbb8&amp;vid=wxv_4650037382396690440&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

GPT 这一版的画面更清晰，不过运动逻辑出了一个很明显的问题。第二名红方球员还没有和对方发生碰撞，就毫无征兆地自己倒地了。

![【Codex + GPT-5.6 Sol：球员无碰撞倒地的画面】](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX2woLruT7snVC6ywqp9T1mUpgADzbHuZLx0ibImh7pl3ZIeDqiatlFKXmHlPggOCXB1Cb3RRRsu9VkeJRTUVM2n8tND9R0NPkicDM/640?wx_fmt=gif&from=appmsg#imgIndex=35)

【Codex + GPT-5.6 Sol：球员无碰撞倒地的画面】

▲ 【Codex + GPT-5.6 Sol：球员无碰撞倒地的画面】

这一轮如果只看动作连贯性，我会投 DeepSeek 一票。GPT 赢在画面清晰度，但那次毫无征兆的倒地太出戏了。

### 03｜3D魔方

3D 魔方的提示词就比较简单，只有这么一段。

```
●  ●  ●

创建一个独立的 HTML 文件，
其中包含一个使用 Three.js（通过 CDN 引入）构建的、功能完整的 3D 魔方模拟器。
该魔方必须能够自动复原。
```

Codex + GPT-5.6 Sol（极高）跑了 11 分钟就做完了，中间没有任何修改，打开就能玩。我可以随意打乱魔方，然后点击自动复原，页面也会完整展示复原的动作过程。

，时长00:09

<video src="https://mpvideo.qpic.cn/0bc3ryanaaaavmag4wl7r5vfbdwd2chabuaa.f10002.mp4?dis_k=12c18b92f33c7e93031838ef209568a7&amp;dis_t=1792736823&amp;play_scene=10120&amp;auth_info=XLbb5Pp5QVVjlZ32zg0HfU0rImJfZRRMbkZ6OmdSQGBiVmBuKXEcOgE5FlkiLxBHRw==&amp;auth_key=a028cfdc8da3f861a0c6d2a9d87a8627&amp;vid=wxv_4650046583928193025&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

dsh + DeepSeek V4 Pro（Max）跑了一小时才做好。从任务轨迹看，期间跑了 500 轮测试，所以耗时比较长。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX11mRkUl9yHBQx8Vu3p0QWZ8ca4YI66QfxN4oNWiacTVaib75tHboMufb3W5MzCQBxTIQjeNp3WeicPNibZBH8cnzYZGVXJvOHfic7M/640?wx_fmt=png&from=appmsg#imgIndex=36)

我打开 dsh 做出来的页面，第一眼就觉得很酷。启动时，一个个方块会慢慢组合成完整魔方，3D 魔方的外观也很接近现实。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX0DkjwCZNbQevBQYGhl8VvskT3rVdL22rgOWiabk5a0ydOickUlyDv7kDlUkw504zp9r00N0Z00V1gECzVC9RiayYtaFF8339AoOk/640?wx_fmt=gif&from=appmsg#imgIndex=37)

▲ 【dsh + DS V4 Pro（Max）：3D 魔方启动效果】

还有一点很不错，可以直接用鼠标拖动魔方旋转，感觉真的像在玩魔方。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX3DURNuSBiboQZvJh5yll9wnDN3VtEA63eSXY8QE0KicxrJP0Q0Pq3XxrdHIF7AetrW7ET8axxC5ibEQvVVYm1jdXzOIaGUGicK5ek/640?wx_fmt=gif&from=appmsg#imgIndex=38)

▲ 【dsh + DS V4 Pro（Max）：鼠标拖动魔方】

GPT-5.6 Sol 这一版无法直接用鼠标拖动魔方，只能通过右侧操作台控制旋转。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX2QdKAd2JUOfSJeya2ibVuohCU3sv5dmdwPF2ASqQAoTag5muNAK0e0890VWTVkdFRuPbQOudACx4ccIqribibnZltrSNaib0ibYQes/640?wx_fmt=gif&from=appmsg#imgIndex=39)

▲ 【Codex + GPT-5.6 Sol：3D 魔方操作界面】

至于自动复原，DeepSeek 这一版也能把混乱状态的魔方自动回滚到默认状态，完成的不错。

，时长00:22

<video src="https://mpvideo.qpic.cn/0bc3pya5oaabj4agxv36f5vfc7wd257advya.f10002.mp4?dis_k=07410d94e419aa2c34df10128b1a7e62&amp;dis_t=1792736823&amp;play_scene=10120&amp;auth_info=CNCNit15HAJmlJihzgUBfUsoJWAFMxBHPkV9bzlQSDQ2XDJmfXBBbQQ4Ew4iJxZHQQ==&amp;auth_key=aef4b9383cb20b652eee7c9077fbebce&amp;vid=wxv_4650038194598526982&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

GPT 这一版的自动复原也符合提示词要求。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX3haf2iavnKXIUaHaTcsiaWNCqWRzNjMV4UcepFUxVIf40zT0IM2ypjAtdsibiaQjbxQMSgkBTgYWCvDJAWujvMBcQHZhksydLK1ws/640?wx_fmt=gif&from=appmsg#imgIndex=40)

▲ 【Codex + GPT-5.6 Sol：3D 魔方自动复原效果】

这一轮两边完成得都不错。GPT 胜在快，11 分钟就一次做成。DeepSeek 虽然耗时更长，却多做了可以直接用鼠标拖动魔方的交互，这一点 GPT 没有实现。

### 04｜跳一跳小游戏

第四个任务是跳一跳小游戏，我只给 dsh + DeepSeek V4 Pro 写了一条很短的提示词。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX3zxdibnYs0eibVKSIMApRALeA9ajgcfdtzEy1YmQzJ9HNNyZjSa5VB4YvOlPvZFpQOHoFpeSXJibzic9HFQxsbW6oa7p48x0UfcHg/640?wx_fmt=png&from=appmsg#imgIndex=41)

跑了 30 分钟，页面总算做出来了。我先自己玩一局。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX3ykRVvs56Yrtwjeeo2slKHn0icMpMKVAn24wJ9Tf3e4Micd56WxtyLvAvfhZrMWTrlr5uHLzKCI4SP0qNHxaHs55icwWQToGy4T0/640?wx_fmt=gif&from=appmsg#imgIndex=42)

没控制好，只拿了 2 分。搞错了，再来！

![【dsh + DeepSeek V4 Pro：跳一跳游戏，再次试玩】](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX2XEgWtE97D9WPOFJ8iafvWnVnsHlyfSwxqz8RKtv7rNCYtvXUVLoY7LNmHj6AkibPrNHPBTftKZH5DFgdA2AOics0rREFn8yH2f0/640?wx_fmt=gif&from=appmsg#imgIndex=43)

【dsh + DeepSeek V4 Pro：跳一跳游戏，再次试玩】

难度确实还蛮高的，但我玩下来没有遇到明显 Bug，核心玩法也还原出来了。

Codex + GPT-5.6 Sol 只用了 8 分钟，但它把游戏做成了横版。游戏可以正常玩，我也没遇到明显 Bug。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX21mHjtyG2XJDe2xJTK6DjjxULQzqmwVKx0JAdLcGWic7eSLibPEyIu8bfcSfrZKBDvoIic9BD4VPs5Krmurons31PiafiaohOwsBt8/640?wx_fmt=gif&from=appmsg#imgIndex=44)

这一轮 Codex 赢在速度，DeepSeek 则赢在还原度。如果按提示词想要的原版风格来判断，我会选 DeepSeek 这一版。

### 05｜滑动变阻器

最近刷短视频，我看到一个很好玩的项目叫「滑动变阻器」，用来展示梁圣的变化过程。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX0JsJBbo2HsfGGXesrBEUMNhrPS8ZB18Ia8E97fnUpD3AibXNqqhl1AJuJbSxT1TKG7Uv0piciaIhRyf33L0IVyKbnE7cpXEqoGjA/640?wx_fmt=gif&from=appmsg#imgIndex=45)

因为 DeepSeek 没有生图能力，我就想让它通过 ASCII 字符，做出滑动变阻器里的不同画面。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX20nkLIz9mRCiccVfkdCdvBznwdVno4FBsxh02YiagWREdF53n3lvf4D3rbGU2LwTsVxcyexKYAicTMYawbqcduHBHBTojYoSE6mw/640?wx_fmt=png&from=appmsg#imgIndex=46)

先看 DeepSeek 这一版的效果。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX0O5zsWSuCtgiarjoBxXpGFxWdFia2NRv96AicjafCg3cq4mHP1cX9DZaoUozNPfNTZfK1Pq7N1Chh4Sfsp91bicnOPJGiaynXeUxO0/640?wx_fmt=gif&from=appmsg#imgIndex=47)

你们别笑，就问你精髓是不是实现出来了。别忘了，DeepSeek 是瞎子模型，没有能力读图的，能做成这样已经不容易。

dsh 在执行任务的过程中，确实尝试把网页图片抓下来直接读取，但任务轨迹里显示这一步报错了。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX1EdBEDiaxPbA6t51pRHYerkIpUibBMz9f2jdpEPSb3ricC4icNuNvZRfibWZXQ8EoLuOQvVNWFoQ8ys9sEoyTFTichwrbeZwC4EP2uU/640?wx_fmt=png&from=appmsg#imgIndex=48)

不过它没有完全放弃，又换了一条路，尝试把图片转成文本再分析。从任务轨迹看，这次不算纯靠想象，它在借助工具绕过视觉限制。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX3oAQ4mmk2uaShFTDayM6xPUQbT9m4ejpX9JJgjS2NKqJYPU5p2zOPxibc9ibqRrHmISZAU9uwZLhaCEBGHYxwdWFhVIkGe9FwFo/640?wx_fmt=png&from=appmsg#imgIndex=49)

同样的提示词，我再发给具备视觉能力的 GPT-5.6 Sol，出来的效果是这样的。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX2smic8M29plZzbYoK6gyexgFjWmFMgbm30TdiaPQ3D4pL7lNCcOT6QAyyCNWXFWR0dODrp97du34CQKGKP5IFItNK2hxPIUXmZY/640?wx_fmt=gif&from=appmsg#imgIndex=50)

这一版和原图确实很像。但 GPT-5.6 Sol 是「长眼睛」的，可以直接看图，所以用 ASCII 字符复刻原图对它来说，多少有点降维打击了。

![【Codex + GPT-5.6 Sol：ASCII 画面细节】](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX3tq6WAZ1gqMOGqpmXw4dMPcclLgicQqMwa9YgwHdtHicJbkyt9YIAKutC69hVzs5RoibfeKY0fEEJEjMHzlAMlbr9lJjQew3EZ44/640?wx_fmt=png&from=appmsg#imgIndex=51)

【Codex + GPT-5.6 Sol：ASCII 画面细节】

这一轮 GPT 的复刻效果更好，DeepSeek 只是输在了自己不是多模态模型。

## ────价格怎么样？────

上面这些案例全部跑完，DeepSeek 模型一共消耗了 2.5 亿 Token。按我测试时还没涨价的价格来算，总成本差不多是 20 元，也就一杯奶茶钱。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX0GCXpvibGC5yJJmTcAX3bohzPjXVSmKfWJhfgmsOp2HPVY0BCoscsIa1q91LFwt3uwyAgzMp63kBib0vaYp8gkkOqsUKowfaVJ4/640?wx_fmt=png&from=appmsg#imgIndex=52)

就这价格，夸一声「梁圣」不过分吧？

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX1rDP8pQyFOIVCBjG3ozmjLCN7fGldXlI1gXUXAicHKdPTCq5jIf36mnSVdqGH4ia3d1t9AV2aMGhIM8heXeRNORd8Pia8fOj2icyI/640?wx_fmt=png&from=appmsg#imgIndex=54)

我这几次跑下来，缓存命中率基本都在 95% 以上。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX1C0v6CEXAGLznicTFZyNB6t3fXjh8JGNicjlFfeU9NlXbuea9zgG3GQf9WTkWKbibPibQABITvRsqOcSnQy5pIgGadEibrBw2MkA9Y/640?wx_fmt=png&from=appmsg#imgIndex=55)

不过上面这个成本是按涨价前的价格算的。如果换成新价格表，考虑到高峰时段的缓存输入价格涨了十二倍，空闲时段涨了六倍，同样的用量估计要上百元了。直接从一杯奶茶的钱，变成下餐馆的钱。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ysyAxM1rgX37ia1p2CImupJJicdKEG0U7JeGzibKib9ddypUIRZMDaZgZpFy2icib7ibTC6ZhuYSdE2WMeUuWkZPEia8dPqxWpF3mnqgzsumEyxy7j0/640?wx_fmt=jpeg&from=appmsg#imgIndex=56)

看到这个涨幅，你是不是已经想把滑动变阻器往左拉，直接滑成「梁子」了？

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX0D74K4ADohuTc8UAQ0FicJBgu3Lia07YUuF1eicmVMvkb5xlcGnx1zjhp29UHGnPCCg0mgngnCs4zhoO2T9mQHSqd8Ayq2PibMiaibc/640?wx_fmt=png&from=appmsg#imgIndex=57)

别着急滑，但是即使涨价之后，DeepSeek 依然便宜得有点离谱。

如果把同样的2.5亿token消耗量来算，换成 GPT-5.6 Sol API 按量计费，账单大约是 186 美元，折合人民币约1260元，依然接近 DeepSeek 的十倍。

所以，依然是梁圣！

## ────写在最后────

最后聊聊 DeepSeek Harness 的体验。

如果你是开发者，你肯定会很喜欢Deep SeekHarness的设计，首先是一切皆插件的设计理念，造就了你可以自由定制化dsh。

还有就是任务的执行过程明细都列的很清楚，还想看的更清楚，还可以去「轨迹」里回看任务完整的执行过程，非常适合帮助你理解任务的执行逻辑和工具调用顺序。

但 dsh 的风格天生偏向开发者，这也决定了它可能不适合普通人，比如你想拿它处理办公事务，大概率会用不习惯，那些硬核设置和功能，看不懂也用不来，而且目前也缺少那种一键安装的 Skill 市场。

还有不知道你们有没有这样的体验，dsh 是 Web 页面，浏览器里开了一堆 Tab，想切回 dsh 的工作页时，翻了半天都找不到是哪个，真的很痛苦。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX1oj4OonvWNaH8tHqBZ3UdazicXVfs8ITKt7Sqq2cyaIElTUdpKmiaT4INXlHqRguuhEgcic2kCLlm0UQicN416oQ3VZZaNvxQJ7XA/640?wx_fmt=png&from=appmsg#imgIndex=58)

到后面体验久了之后，我突然才悟到了！

我根本不用费劲去找那个页面，直接新开一个 Tab，输入「http://127.0.0.1:3080/」就能直达 dsh 工作页，任务记录一条都不会丢。，那些任务记录都不会丢失的。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX2Wicv6YZDiatSHNJ8VX7NId6eUEj38ga68RgF5n680iaNHr9KGJHHt84blzRz3Zy0zu92nQSB5510qd3ngic4uQJff2bicxVibmBWDI/640?wx_fmt=png&from=appmsg#imgIndex=59)

对了，还有一个更容易踩的坑！！

如果发现 dsh 卡在某个任务上很久，先别傻等。最好打开终端看一眼，确认 dsh web 到底还在不在运行，我实测的时候就踩过这个坑。

你看，我明明已经把 dsh web 进程关掉了，但页面里的「Deep diving」还在继续计时，看起来就像 DeepSeek 还在后台疯狂思考，极具迷惑性。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX1bHXciasFU0I84YlpL20bKlFNOAxCxZHcIXzDlWnq7YGEuoldq675yQttFShznKX4NBNk5ZjnlTNFIKvbnlLj3sZcRX7Z7dWX0/640?wx_fmt=gif&from=appmsg#imgIndex=60)

也就是说，你看到页面上的时间一直增加，不一定代表任务还活着，这个体验就挺割裂的。

不过吐槽归吐槽，我对 DeepSeek Harness 还是挺看好的。

DeepSeek Harness 最有价值的地方，是给社区留下了很大的改造空间，模型、工具、提示词、上下文和 UI 都能通过插件调整，大家可以围绕自己的真实需求，重新组装 Agent 的能力和工作方式。

等社区生态愈发疯狂，我都不敢想后面的 DeepSeek Harness 会有多恐怖。

这头黑鲸才刚刚下水，真正的故事可能才刚开始，共同见证。

AI 编程实战 · 目录

阅读原文