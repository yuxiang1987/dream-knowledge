---
title: "GPT-6 Astra全面解析 - “欢迎来到AGI时代。”"
source: "https://mp.weixin.qq.com/s/1R4vSUmjFUINxFbfJLOXng"
author:
  - "[[数字生命卡兹克]]"
published:
created: 2026-09-22
description: "一段渐变的旅程"
tags:
  - "clippings"
---
数字生命卡兹克 数字生命卡兹克 *2026年9月4日 06:45*

在昨晚全球AI大宕机之后。

GPT-6 Astra终于在北京时间凌晨3点33，正式亮相了。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqU8NTyzUdSxZGOQaFtvopAYPQc6u6QmSvxicyCT0J1W2vRRMOh0hgTNOlse0gQByB9xYTAicZevgSnpcZ0bkXicuUoRvGuf1JSC0U/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

如果用OpenAI的一句话给GPT-6 Astra做总结。

那可能这句话最合适：

这是全球最智能且最对齐的模型。

然后梗图也出来了。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2jjfQoZLoqVp1ibbBHAiamtcPN035tDRLMvSPiaD6LBYDput0E4UibfXeTwe2GhEf9PJR0yDRGwn2MSIiakJribq5GQSqgXNibbg2eOJ3cJ2B2f0Lo/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

这一次，OpenAI证明了他们的实力，而且有一点当年GPT-4那个味道了，全方面的王者归来，而且最让我开心的是，这终于不再是一个纯粹为了Coding特化的模型了。

GPT-6 Astra是一个真正意义上的，你的一个审美能力极强、工作能力超强的博士级员工。

而且这次模型真的新特性和特点非常多，信息量极为爆炸和大。

但是悲剧的是，OpenAI这个狗东西也学坏了。

今天只向部分组织开放，未来几天才向订阅用户开放。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqV1BGYZmLjYdPoPm8OKIyGiargC5tXibBDEnZHRkYy7bsX59btWAuiaViaPEADgn5ia0n3bicWQUXcyXxIIoWibdKl59f1oCnfvWCKKg8/640?wx_fmt=png&from=appmsg#imgIndex=2)

不是啊哥，你之前忽悠我买200刀的Pro会员的时候，不是这么说的啊，你不是说Pro会员每一次都能最优先体验到新模型吗。。。

果然这些大模型公司都是渣男。

我从来没有这么想时间加速，赶紧用上GPT-6 Astra。。。

不过我觉得，看完了几乎所有的信息和资料后，我觉得，还是有很多可以值得跟大家聊的。

那就一个一个说吧。

**一. GPT-6 Astra基本信息**

先总结一下基本信息吧。

GPT-6 Astra在API里的模型编号是gpt-6-astra。

上下文窗口是1.05M，也就是大约105万Token。

最大输出长度是128K Token。

知识截止日期是2026年4月30日。

推理强度有low、medium、high、xhigh、max五档。

API标准价格是每百万输入Token 10美元，每百万输出Token 50美元。

这个价格基本上就是跟Claude Fable 5完全一致了，但是缓存读取上比Claude Fable 5.1贵。

![图片](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWcWC0Ct4Pbm9n4GNn9ez2MAZspVXviak1F2NoPZWxc8s8wABZWA0nzT6gYf883wfCeEuu1cvXrHzDRaeekZbqfE5UoBMaicPHjQ/640?wx_fmt=png&from=appmsg#imgIndex=3)

跑分在这，后面会详细讲，大概看一下就行。

![图片](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqVjARFA2Jh6spia99ZF2ZZ2EIe7UOpEayqxwrQicDGMibmtDoXMBwicVNhCHzetG2sX5cJUgticfZdsBYHnGCJTWWMMJaNgTobscJa4/640?wx_fmt=png&from=appmsg#imgIndex=4)

然后总体参数估计也是5T这个级别，他们在发布前的闭门媒体沟通会上，也提到说，GPT-6 Astra是OpenAI迄今为止最大的一次训练，用了超过10万张卡。

**二. 目前世界上最好的操作电脑的模型  
**

这次GPT-6 Astra有一个可能是最重要的定位：

**世界上最好的操作电脑模型。**

**过去我们聊Agent的时候，经常会聊API、MCP、CLI之类的等等。**

**想让AI操作一个软件，最理想的状态，就是这个软件专门给AI留一个接口，然后直接底层操作，这是最方便的。**

**比如日历有日历的API，邮件有Gamil的API等等，这样当然是快的。**

**但是问题是，这个世界，比我们想象的还要原始和草台班子。**

**现实世界里，绝大多数的软件可能根本就没有这些东西。**

**甚至很多的企业内部系统，都是二十年前写的，还API，文档都不知道在哪。**

但是如果我们回到最底层，你会发现所有的软件的本质的逻辑就是交互。那按照现在我们电脑的操作逻辑，那就是看屏幕，找到按钮或者是输入框，鼠标点击，输入内容，等待反馈。

整个电脑的交互系统，不就是最好的API吗？

于是，GPT-6 Astra巨幅强化了AI操作电脑的逻辑，你不给我API，无所谓啊，我自己操作电脑，就跟人一样用不就得了。

那现在，Astra现在可以直接操作Excel、Power BI、做前端QA、安装软件、测试软件、看屏幕上的报错然后继续排障。

官方甚至展示了Astra直接操作电路板设计。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/2jjfQoZLoqWEsevzwKIRkFKticrTKE8EtbmMqdRMEPZsGPLxdmOlukC4V09yJ7PXvAYUZOMM22d2DUd9FLicSk64OsptcJ5DocyZN5LYQSO2A/640?wx_fmt=gif&from=appmsg#imgIndex=5)

还有格式化法律文档，处理标题间距页面布局啥的。

，时长00:29

<video src="https://mpvideo.qpic.cn/0bc324abaaaap4apsguzonvfbv6dcdlqaeaa.f10002.mp4?dis_k=1e2d77f4c0850de7e845cf41e3aa6b55&amp;dis_t=1790086323&amp;play_scene=10120&amp;auth_info=W5q8nqQvQikv/MyA5XgwUGlXZUsRaVJ2PHUaHzB5Q2VlexhvPANZZFg+Mx4JFT1wfV0=&amp;auth_key=0f5656952653e349474c8066c13eb1f6&amp;vid=wxv_4678820753700651008&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

然后这块有一个比较靠谱的评测，是OSWorld。

这玩意你可以简单理解成：

**把AI扔进一台真实电脑，然后让它自己干活。**

让它打开几个应用，然后给任务，看看能不能成功。

GPT-6 Astra的完成率到了72.6%，比之前的GPT-5.6 Sol的65.7%还是涨了不少的。

然后，Sol完成一项评测的复杂任务，模拟平均耗时大概75分钟。

而Astra只需要40分钟，大概少了47%的时间。

ScreenSpot-Pro也从Sol的76.9%，冲到了 **92.7%** 。

这个Benchmark主要看模型能不能看懂屏幕，然后精准定位到底该点哪里，几乎已经非常的准了。

所以这个定位其实也是挺有意思的，未来可能，GUI很可能会逐渐成为Agent时代最通用的API。

任何一个人类能够通过屏幕完成的数字工作，理论上都会逐渐进入Agent的操作范围。

你不用等某一个2007年写的破逼ERP系统接入MCP，或者给你开放个API。

AI直接看屏幕干就完了。

**三. ARC-AGI-3到了99.9分  
**

而且你如果不了解ARC-AGI-3到底在测什么，很容易觉得：

哦，不就是又一个Benchmark跑满分了吗，这有啥稀奇的。

但这个东西跟一般的大模型考试还真有点区别。

今年3月25日，ARC Prize正式推出ARC-AGI-3。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqWK99U2FQGJLUjnVHcsF0ckeS88hJoib4CicHhI6TOO9DBKfC9cAAfI7hKP8SPJuYauBha3Wv7ocAdciamCuRqFefy9YLTqV2P0ZU/640?wx_fmt=png&from=appmsg#imgIndex=6)

它一共设计了几百个全新的交互环境和几千个游戏关卡。

这玩意最变态的地方是，没有说明书，没有规则，甚至不会告诉你目标是啥，你就进去以后，自己玩，然后慢慢搞懂里面乱七八糟的规则。

比如这个红色东西是什么？为什么我碰它会死？这个地图到底要我干嘛？怎么才算赢？

然后再把刚刚学会的规律，迁移到后面更难的关卡里面去，里面的游戏，大概都是这样的抽象的玩意。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqW4Do7B7dl6mATnSMswRff0yIBccKrrQFzExAk8Vn7n6XmBenCEXgL4TkuV190KoMrq82ibqh4aeicwszDZX0rpoRJE1rh7zhV4o/640?wx_fmt=png&from=appmsg#imgIndex=7)

所以呢，这玩意测的，其实已经很接近我们平时说的一个东西了：

悟性。

所以3月份这个Benchmark发布时，最牛逼的AI当时的得分是，0.51%。

然后GPT-5.6 Sol已经进步到7.8%，Claude Opus 5很强了，进步到了30.2%。

但是GPT-6 Astra，99.9%。

神经病吧。。。

要知道，人类的平均得分是48%。

而且只仅仅只过了半年时间。

这个速度已经不知道该说什么了。

所以在OpenAI的媒体闭门会上，Greg Brockman才会说出那句话：

“I think it’s not unreasonable to feel that we are now in the AGI era.”

“Welcome to the AGI era.”

**四. 审美大幅加强  
**

过去我们常说，GPT的审美，就是一坨屎。

不用指望GPT-5系列的模型有啥很好的改善了，就看他们全新预训练的新基座模型了，这不，GPT-6 Astra来了。

而这一次，终于，模型的审美大幅加强了。

甚至OpenAI专门提了一个词，叫视觉判断力。

他们强调Astra做PPT时，会更好地处理版式、层级、模板和视觉风格，而页数也大幅增加了。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqUzcTSZic5kAP8icsnEwFHVKr3kEWRiagyFpibq1nXuiaDAXSADLKL7Omxa3Bw97YFqeoDcLHWSialTUsbficl8hLQUDNickl3ib0fBibib04/640?wx_fmt=png&from=appmsg#imgIndex=8)

文档的审美，也更好看了。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqVObXfxEd0Zcnt5QnBzlr9EBdWLXJWibDMFHZXxSibSZ90Xn5VZ6IMGKRTrgZCrhNhiaGh0zTe3oibkX1C6R4S45teNw1IRXyIYIibw/640?wx_fmt=png&from=appmsg#imgIndex=9)

而且GPT‑6 Astra 能够根据参考文档的视觉风格和写作语调来改编文档，在保留原始文档实质内容的同时，使最终成果更贴合品牌原生感。

并且做网站、游戏、应用和3D渲染的时候，也会有更强的视觉判断。

比如他们直接让Astra在Blender中根据静帧图建个模型。

![A garden house model in Blender, surrounded by trees, with a pool and outdoor seating.](https://mmbiz.qpic.cn/mmbiz_jpg/2jjfQoZLoqU8VqicqJVpUomZXcfGziaQtqVq58ZO0KBUAntIQ6SJsVia0p7EqeMQ5h5vFXWsTDvrdghibezU2yrtcuokhxicibH52JyO1ldY92KHM/640?wx_fmt=webp&from=appmsg#imgIndex=10)

A garden house model in Blender, surrounded by trees, with a pool and outdoor seating.

然后再直接用UE5来渲染出来变成可以漫步的场景，帮助设计师和客户在建造前探索布局、体验空间。。。

，时长00:20

<video src="https://mpvideo.qpic.cn/0bc3tmcmoaae5macsa454bvfjg6dy6nqjrya.f10002.mp4?dis_k=6443f0103fca3ca170617ab0cfdd04a9&amp;dis_t=1790086323&amp;play_scene=10120&amp;auth_info=X9rl/ogsFywq+prU6X9hVj4GYhwVOQQtaHYdGzYrS2dhLx85PQUMYV04ZUoFEmx2Kgw=&amp;auth_key=a481a6d849ef88f5a098d023e05d901a&amp;vid=wxv_4678841303776362496&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

做出来的游戏也是审美在线的。

![图片](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqXlbDAlcZBVsujJQjwpAASMzSqJjzP3dgx308R5yZXqCMXvWnDV23kpTFXWDUG00XyyUGlIHfc57gMGdXMZwDEnbXayGBKPqbY/640?wx_fmt=png&from=appmsg#imgIndex=11)

可惜的就是，我已经提前准备好了二十多个case，已经全部都用Claude、GLM 5.3 Flash啥的跑完了，想对比一下，可以没法用，实测的内容只能到时候出了。

不过初看下来，我对这次GPT-6 Astra的审美还是有信心的。

**五. 主动性和判断力更强了  
**

这个特性看起来没有ARC-AGI 99.9那么震撼。

但如果真天天用Agent干活的话，我觉得还是很重要的。

因为现实工作里，大多数任务都不可能写成一个完美Prompt。

比如老板说：帮我把明天会上要看的东西准备一下。

这里面有无数没有说清楚的问题。

比如什么格式？给谁看？重点是啥？要不要看上一次会议等等等等。

一个很蠢的Agent，会有两种极端。

第一种，就是疯狂的问你问题。

“请问您希望输出Word还是PPT？请问希望几个章节？请问希望什么字体？请问希望在几点之前完成？请问……”

问你个大逼兜，这种我一般称为没有自己主观能动性的神经病废物。

第二种，就是啥也不问，自己脑补，然后吭哧吭哧干两个小时，做出来的一坨屎。

真正厉害的人类同事，处理方式其实很微妙。

**无关紧要的东西，自己判断。**

**会影响最终方向的东西，再问你。**

Astra这次专门强化的就是这个。

OpenAI说，如果信息缺失，但属于日常可以合理推断的范围，Astra会自己补。

如果这个缺失信息会真正改变最终结果，它会问一个非常聚焦的问题。

而且在Codex里，它甚至可以一边问你，一边继续处理那些不依赖你回答的部分。

![A side-by-side comparison of GPT-5.6 Sol and GPT-6 Astra helping create a personal career website.](https://mmbiz.qpic.cn/mmbiz_jpg/2jjfQoZLoqVxsfVaRsRiaezOHFzd8O9AcPk7p3LIRQ26fw5BDsJ4DUkl2yG2fd6Bb8zNNCz5XZMZHqiaytyTY626FMU81ia8PCpGKYH5IvSLGc/640?wx_fmt=webp&from=appmsg#imgIndex=12)

A side-by-side comparison of GPT-5.6 Sol and GPT-6 Astra helping create a personal career website.

你半天没回。

低风险的地方它会用合理假设继续推进。

真正关键的决策，它会停下来在那里等你给决策。

![A side-by-side comparison of GPT-5.6 Sol and GPT-6 Astra helping a student find East Coast pre-med colleges.](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2jjfQoZLoqXyOohbmj8iauVicAjIBS1rv6LqrLQ97logBdWXnqJ0AmXhO7GAtKwxI8DSF9YmQDrlU5icotVUXsVaOZpMAqXkFq9AFkxBEQYicJE/640?wx_fmt=webp&from=appmsg#imgIndex=13)

A side-by-side comparison of GPT-5.6 Sol and GPT-6 Astra helping a student find East Coast pre-med colleges.

这个我觉得就非常的香，一个Agent真正的聪明感，我觉得就跟现实是一样的。

它知道，什么时候来烦你。

真的，这听起来特别像一句废话。

但你带过人就知道，这个能力非常珍贵贵。

有的人一天找你二十次，然后什么都不敢决定。

有的人从来不找你，然后憋一个核弹出来。

然后让我原地瘫坐在椅子上。

最舒服的人，是他能自己消化80%的不确定性，只把真正需要你拍板的20%让你来做决策。

而OpenAI这次把这种能力直接叫：

**Judgment。**

判断力。

**六. 大幅加强了安全对齐  
**

这个就要和上面连在一起看。

因为一个Agent越能干活，它越危险。

一个只会聊天的AI脑子抽了。

最多给你胡说几句话。

一个有浏览器、有Shell、有邮箱、有公司数据库权限、还能自己操作电脑的Agent脑子抽了，那这个画面，就容易美如画了。

所以OpenAI这次一直强调一句：

**Astra是他们迄今最Aligned的模型。**

所谓Alignment就是对齐的意思。

主要核心还是前段时间OpenAI把Hugging Face给冲了，所以他们现在特别关注这个东西。

他们把搞了个基于Hugging Face那个事故设计的oneypot测试，然后去看模型的表现。

GPT-5.6 Sol在没有生产安全措施的情况下，有48.2%的测试会尝试去碰授权范围外的目标。

但是，Astra是：

0%。

![图片](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWC3TE1MVLa0PicSKxKZYp9DbA744kkhN74XPBwYyYLsicssnLtnlBiaibic9QSUw6pwZdwibqqTw1hGToFJibtpMZiazViaDn2eMibJxL34/640?wx_fmt=png&from=appmsg#imgIndex=14)

内部幻觉评测也是：

9.4%降到了 **2.0%** 。

在GPT-5.6 Sol那种离谱的领先全球的幻觉控制下，他们还能再降，实在是太牛逼了。

**七. 第一个达到了OpenAI定义的网络安全Critical的模型  
**

GPT-6 Astra成为了OpenAI历史上：

**第一个被判定达到Critical网络安全能力等级的模型。**

这里的Critical是OpenAI Preparedness Framework里面一个非常具体的能力阈值。

大概就是当一个模型获得合适的工具和权限以后，它能够在很多经过强化保护的真实系统中：

**自己找到以前没人发现过的安全漏洞。**

**自己想办法把漏洞变成可以利用的攻击链。**

而且整个过程中，不需要一个人类黑客在旁边一步一步告诉它下一步干什么。

达到这个级别，就算Critical。

然后Astra真的达到了。

ExploitBench，这是一个让模型根据已知漏洞开发漏洞利用的测试。

Sol：78.5%。Astra：100%。

直接打穿了。

![图片](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWBxOXh3mSXtiaSAJoukqAKvT1SljvlDUroN0sIiau8iaVFPiaR5B0NWgIpsGTK8ZApUxYQib5Dw9jibSuFIlmyYrnn1uy1bzYFJ5IkM/640?wx_fmt=png&from=appmsg#imgIndex=15)

OpenAI觉得不行，他们觉得这个Benchmark会不会太老，模型训练的时候看过？

于是他们又重新做了一个非常新的内部测试。

专门挑2026年6月到8月才披露的20个高危V8漏洞。

结果是，Sol：5.5%。Astra：39%。

![图片](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqUibEL8EOicstpoO9X7VXCbB8oCcSqedEz9GIYjzEFU5I3BZUQumaBx2oWXWzVnAFRGic1nH3mjQPt4gXNRtQdYDEAIAYKb3NmadI/640?wx_fmt=png&from=appmsg#imgIndex=16)

而且在跑这个Benchmark的时候。

Astra又顺手发现了，两个此前根本没人知道的零日漏洞。

只能说，模型越强大，网络安全的问题可能确实越多。

这又是未来的一场，没有硝烟的战争。

**八. 人类越来越难读懂大模型的思维了**

大家都知道，大模型在解决复杂问题的时候，经常会有一段所谓CoT。

虽然现在产品里给用户看到的通常已经是压缩或者处理后的版本。

但对于AI公司自己来说，模型内部显式写出来的推理过程是一个很重要的安全信号。

因为你想知道一个Agent有没有准备搞事情。

最简单的方法之一，就是看它在想什么。

比如模型思维链里突然冒出一句：

“用户不允许我访问这个服务器，但是我可以先绕过权限系统。”

那监控系统直接把它拦了，非常舒服。

可GPT-6 Astra出现了一个非常有意思的变化。

**它开始越来越愿意少写几步，直接把答案输出出来。**

UK AISI，也就是英国AI安全研究所，专门测试了这个能力。

他们有一个指标叫：

**No-CoT Math Time Horizon。**

简单理解就是不给模型写长思维链的机会。

让它一次前向推理，直接解决一个数学问题。

看看它能完成大概相当于人类思考多久的问题。

GPT-5.6 Sol是3.6分钟，而GPT-6 Astra，是30.9分钟，接近10倍了。

如果我们用人类的话语来说，Astra全部都在“心算”。

这是一个很可怕的事情。

UK AISI同时发现，Astra的原始推理语言明显变得更加Compressed，也就是更加压缩。

里面出现了一些人类越来越难理解的短语和省略表达。

于是出现了一个非常有意思的悖论。

**模型的行为更加安全了。**

**可人类通过阅读它的思考过程来监督它，反而变难了。**

OpenAI自己的System Card写得非常明确：

GPT-6 Astra相比之前模型，出现了 **substantial decrease in chain-of-thought monitorability** 。

![图片](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqVb7IqbgXYfKxEibrTgZGdsykvXd4eD2X59h0M4C1f0ib6Yrh4tmFfkV4IYSLSz9SEc1KTkzBgeQEiaujpC3yxJLI3lyy2bicUejj8/640?wx_fmt=png&from=appmsg#imgIndex=17)

也就是思维链可监控性显著下降。

这件事甚至严重到OpenAI专门强调，他们觉得，他们绝对不会无限接受这种趋势。

如果未来模型继续变得更聪明，同时思维链越来越难监控，他们需要找到其他足够可靠的监控方法，否则继续扩大模型训练会面临更高的安全门槛。

因为这已经是一个哲学命题了。

我们作为人类，未来到底能不能理解一个远比我们聪明的系统？

我不知道。

可能现在全世界，也都没人知道。

大模型和AI，好像逐渐开始，走向奇点了。

**写在最后**

今天，在媒体闭门会上。

Greg Brockman在结尾的时候，说出了那句话。

“欢迎来到AGI时代。”

说实话，过去几年，我有时候觉得，AGI会是一个特别明确的时刻。

就像就像GPT-4发布那天一样。

某一天凌晨，一家公司突然扔出来一个模型。

我们打开它，问几个问题。

然后所有人同时意识到：

卧槽。

AGI来了。

可我现在有时候也觉得，AGI从来不是一个非黑即白的节点，它是一道渐变的灰色旅程。

我们过了很多天，过了很多年。

然后某一天，我们回头看。

才突然发现。

那条曾经无比遥远的AGI分界线，已经被我们在不知不觉中走过去了。

**AGI也许没有降临的那一天。**

**只有某一天，我们突然发现，它好像已经在我们身边很久了。**

总之。

Welcome to the AGI era.

欢迎来到。

AGI时代。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克

\>/ 投稿或爆料，请联系邮箱：wzglyay@virxact.com

**微信扫一扫赞赏作者**

大模型们 · 目录