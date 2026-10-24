---
title: "保姆级WorkBuddy+飞书教程，手把手带你搭建全自动工作流（附完整PDF）。"
source: "https://mp.weixin.qq.com/s/ici1jKI0EiU02-6TMVAEyw"
author:
  - "[[大刘]]"
published:
created: 2026-10-08
description: "实操：全自动自媒体爆款内容管理分析方法"
tags:
  - "clippings"
---
大刘 爱AI的大刘 *2026年9月9日 17:04*

![头图](https://mmbiz.qpic.cn/sz_mmbiz_png/J1Cdba5GUc2KhLksRAu7aveQxo5kDoNsnic4qJpBRVTTqN9n5iaCAjH29KQqCAJLoSUenTM5jLsZnefpHYGia5Un09MKvWziawVV0hWVhsFnvHA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

你好，这是大刘的第 80 篇原创干货～

熟悉我的朋友都知道，我的工作，一直以来基本上都是 Agent 在飞书里自动帮我处理的。

包括但不限于公司工作、自媒体、FDE等等。效率拉满。

![取图工单：WorkBuddy左侧功能区，红框标出「专家」入口](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc09MU1Io2FNxqHt1EpyoqH62H2ic4UicgMibQ0wROTgvJlefrXiaFdPj4yqCZGmbdn4jrlQL90QvFRYZPn8iaG5VCtN3RVTLpiaxP9P0/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

我以前的解决方案是：Agent 控制飞书 CLI，配置就比较麻烦，使用也很需要技巧，所以我从来没有建议粉丝朋友们用上，就偷偷的自己爽（bushi

说实话，真心好用，但是对普通用户，门槛是真的高。

但是最近我发现，WorkBuddy 里面直接内置了飞书的连接器。

几乎把所有门槛，降到最低了。

所以我迫不及待搞篇 WorkBuddy + 飞书 的手把手教程。

帮大家搞定工作中绝大多数场景。同时，带大家实操做一套我的自媒体爆款分析管理自动流。

还是老规矩，强调一下：

整个实操过程中有大量的思考思路，强烈建议实操过程中多多思考～（个人认为这个更重要一些

我会先手把手带你装好，然后用几种类型的超实用任务（一定会覆盖你几乎所有的使用情况），串联起来整个的使用方法：

> 1\. 群处理、会议、日程联动方法。适合办公党。
> 
> 2\. 文档、表格联动方法。适合所有人。
> 
> 3\. 飞书妙记联动方法。适合所有会议/视频党。
> 
> 4\. 全自动自媒体爆款内容管理分析方法。（各种场景都通用，重点实操）
> 
> 5\. 远程用 AI 的工作方法。

**所以，强烈建议你，对着电脑实操** 。

先定个小目标，争取做到 **最快最系统** 教程。帮大家用 Workbuddy 把自己工作接管了。

话不多说，咱们现在开始。

## 一、Workbuddy接入飞书

01

以前 Agent 接飞书至少花个一小时，还容易出错。

现在 Workbuddy 把接飞书通过链接器给封好了，2分钟解决接入。

如果你还不会用WorkBuddy，看这篇 [保姆级教程](https://mp.weixin.qq.com/s?__biz=MzIyNzQ3MDM3Mw==&mid=2247486371&idx=1&sn=4858c277451c5d75965254b429c7558c&scene=21#wechat_redirect) 就行了。

连接器的入口有两个。

第一个是点左上功能区的专家，然后在顶部切到连接器这一页。

![取图工单：WorkBuddy左侧功能区，红框标出「专家」入口](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc2NA3Lc53eic0dfJ8XAk3ibad9RM2TnibGqibqYNTkZFRgV9dicxXy4DQChY8UkSn0lx1TzGKxWZnYZZGdFs0oXd29uriclOrEvYYmCw/640?wx_fmt=jpeg&from=appmsg#imgIndex=2) ![取图工单：专家页顶部的专家、技能、连接器三个标签，红框标出「连接器」](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc1Mf17KT9jTdrQNvs7Qnka6t20rl5kmvOHyYOTNk4hUbRpAOlOj0WoiarJmSf0mEXRXxibeoKIWIF3oLZD6NicsLK4ZDADkXUrciaA/640?wx_fmt=jpeg&from=appmsg#imgIndex=3)

第二个是在对话框下面那排选项里找，也能直接进。

![取图工单：对话框下方选项栏，红框标出连接器图标](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc1nzPYibAFf2ibJeuW0K5flr7jLpUranA4RUxhtdw59tS3icq7Fl1y9yR32I3jt4gueicsRMEPj2Sic2pCDMUBfv0wzBuSEhbcgiau0U/640?wx_fmt=jpeg&from=appmsg#imgIndex=4)

然后就是，点开通并授权。

![取图工单：「开通并授权」按钮所在页面，红框标注该按钮](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc2YnFhNEWUiceG3JKWRbFEjIVcLjOFL9rE6EBHNibSBPd2YT8ocDpjvHCibSL9yObEz2VicBibb6Qfyr1osHZ4Ba7vibGROeaPU8EKlE/640?wx_fmt=jpeg&from=appmsg#imgIndex=5)

点完它会把你带到飞书那边的授权页。

![取图工单：跳转后的飞书授权确认页全貌，含应用名称与请求的权限范围列表](https://mmbiz.qpic.cn/mmbiz_jpg/J1Cdba5GUc2Xju1yRxOE6XAd0tviaQxo5ML8cKabvsPfofrkRyGkclbWFFK4jcdbcAMK4ibzJpibrDRNBQaQllTiayIlqOj1OArGYyPT8Hs0icA0/640?wx_fmt=jpeg&from=appmsg#imgIndex=6)

这一页我建议你别急着点同意，先把权限列表从头到尾看一遍。

因为它要的东西，覆盖的是你飞书里相当大的一块。

看一眼的目的是，先简单了解下他能用哪些模块，当然，实际上，你看了就会发现，基本都能做。。。

![取图工单：跳转后的飞书授权确认页全貌，含应用名称与请求的权限范围列表](https://mmbiz.qpic.cn/mmbiz_jpg/J1Cdba5GUc1MZ0MXfN2O0ChicTuVDic0SmlYyPYqS6EsicxTj2Zjf7b5ZNA0mV0KGpEufZQCibgQnrlhKhVVWoDkbvia2RD56csvfJvTbF6tcmZ0/640?wx_fmt=jpeg&from=appmsg#imgIndex=7)

确认没问题，点创建。

回到WorkBuddy，看到连接器这里的状态变成启用状态，就成了。

![取图工单：连接器列表里飞书卡片显示「已连接」状态，红框标注](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc3jRrMxzKPTJLLicKHXVObMoYO2g3TUfX3K7JTaa038FGUibZ1oxKhP0IXXwvRAGxANATPWSEwULl2ebTYF7Aq86JgOMjSuKZmFI/640?wx_fmt=jpeg&from=appmsg#imgIndex=9)

可能大家之前用 Openclaw 配机器人、配飞书CLI的时候有试过，以前配置要装、要更新、还要自己调报错，没个小半天是搞不定的。

现在整个过程 2 分钟，不需要任何配置。

我觉得这个差距有点大。

接上飞书了，在开始做之前，我想先帮大家理解下 **WorkBuddy的连接器到底解决了什么** 。

其实现在的 AI 或者说 Agent 已经很聪明了。

但是最大的问题还是，我们每次用的时候都需要给它材料，这些材料可能来自于同事发的文件、邮箱收到的资料或者自己的文档。

这个事情，本身就很笨，但是事实就是，再聪明的AI，也解决不了这个问题。

连接器要解决的，就是这一件事。

就是给 WorkBuddy 一个访问这些软件的入口。

比如这里，接上飞书之后，WorkBuddy就能按你的权限，读你的飞书文档和知识库、群聊记录、多维表格、日程和会议，还有审批和任务，也能反过来在飞书里创建东西。

![取图工单：WorkBuddy连接器详情页，展示飞书连接器的能力说明区域](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc3xV5WLSxibAmvkTxYgP7F9M6b7c3Hdt5kVpUBAy3DSazdZObP9HAXI4kHBbeJo2wwZ9VJ6MuBZPd8hH9LHCcBgIRBx3fCWmeCQ/640?wx_fmt=jpeg&from=appmsg#imgIndex=10)

其实WorkBuddy的连接器很多，涉及到知识库、金融、炒股、生图生视频的各种软件连接。

我用得最有心得的有飞书和ima这两个。一个用来工作，一个用来知识管理。（如果有朋友需要的话，后续我也考虑分享一个用workbuddy和ima协作的高效系统教程）。

总之，用就对了。

## 二、接完之后，先改下配置

02

我知道你很急，但是你先别急，先跟着我调三个设置。

第一个是模型。

WorkBuddy这块的优势是内置了绝大多数国产大模型，腾讯混元、DeepSeek、GLM、Kimi都在里面。

但是！腾讯的旗舰模型 Hy4 现在是免费的，用它。

本着免费使劲薅的逻辑，把Max模式打开，然后上下文默认是300K，调到1M。

还是免费的。。。

![取图工单：模型选择下拉列表全貌，展示内置的各个国产模型](https://mmbiz.qpic.cn/mmbiz_jpg/J1Cdba5GUc3PQ9weKOL6WTAoTBbnYROWCfR3oShYiaX81IuqnvAaa2fgt4JFmSxVWEsVgldYJs50HxYkjzGFpRdCTPplgG1CyCkibic9ehibBKQ/640?wx_fmt=jpeg&from=appmsg#imgIndex=11)

第二个是权限。

WorkBuddy自己有两档，默认权限和完全访问权限，默认权限就是碰到高风险操作会停下来问你一句。

![取图工单：WorkBuddy权限选择菜单，展示默认权限与完全访问两个选项](https://mmbiz.qpic.cn/mmbiz_jpg/J1Cdba5GUc1JSMVYc3W5vzlDXghr8pbeRPka5x0uVU9pVEev6slcVZLqdInRtK7vWQ57Zpq3y7lKAoiaUiagbMhdsVxbzYvcq4Dnia7kN0EiamQ/640?wx_fmt=jpeg&from=appmsg#imgIndex=12)

这里要清楚一件事，WorkBuddy的权限和飞书的权限，是两回事。

WorkBuddy的权限管的是它能不能动你电脑上的文件。

飞书那边的权限，管的是它能读到你飞书里的哪些东西，而这个是跟着你的飞书账号走的。

我的建议就是，WorkBuddy这边的权限，先默认，熟悉之后，你自己都会开成允许完全访问。

第三个是工作空间。

工作空间你可以理解成项目文件夹。

选好之后，它读文件、存产出，都在这个目录里。

![取图工单：工作空间选择与新建界面](https://mmbiz.qpic.cn/mmbiz_jpg/J1Cdba5GUc1fDE0rybCViajv890YLwIGxgMAMQ1cjdY4KznaJ15rvLHU6V0jgI7VcQJT2icnYRkia29HgNZDzj131vNibQw7X3ibWb4ZHf3vAEkw/640?wx_fmt=jpeg&from=appmsg#imgIndex=13)

飞书这条线尤其要注意。

因为它从飞书拉回来的东西，最后很多是要在本地操作的。

所以，要特别注意。

一个项目对应一个文件夹，这一条你听我的就行。

## 实操一、群处理、会议、日程联动方法

03

估计是办公党最需要的部分了。

反正，我半天不看群，基本上就是 100+ 的未读消息。

![取图工单：工作空间选择与新建界面](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc1Y66aYFv3L9eHibAbvCPBg8ph8HrtoFQ1YB861ExCNtRU5qBYTzkJYL1wBJP7DxgDqibtia2pr9L76a0ibiaOKh8o1EsO3icGFOnIjM/640?wx_fmt=jpeg&from=appmsg#imgIndex=14)

所以，这是最基础，但是最有价值的功能。

**1\. 让它爬楼找重点。**

这是最轻的一个，适合拿来当第一个测试，验证连接通没通。

●●●

在飞书群【产品研发】里爬楼帮我看看这周主要要推进什么工作，有什么提到我的呢？

![取图工单：WorkBuddy对话框中发出该Prompt后的执行过程](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc3gvzuu0H9wQybP1jZDe7e4XtFyRPMnHETSWujVcFqZMQUp9MGHvszRZaibwhwgm24uia1RqwWnOZay281xrP8WibhscS6veYOeUQ/640?wx_fmt=jpeg&from=appmsg#imgIndex=15)

然后他就爬楼，总结了一周的消息。

![取图工单：WorkBuddy对话框中发出该Prompt后的执行过程](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc1FN9OJwd6P0E0lw0zBlAsdE62Ko8t74Q3KUp88icdT4ibfYUdHtWMibIQibBF19lBfiaVxz6HX5geczicALPaRicbEOavnYC3LWZJ4kk/640?wx_fmt=jpeg&from=appmsg#imgIndex=16)

**2\. 让它翻日程，找空档，把会订了。**

这也是我自己觉得很省事的一个，因为约会议这件事，来回问几个人的时间，真的很折磨。

比如说刚刚我们看了这周要推进的工作，需要和做产品的同学开会讨论下。

●●●

查下明天我和xxx的飞书日程，找出都空闲的2小时时段，并创建一个标题为【MVP 规划对齐】的日程，邀请他，再预定一间会议室。对了，再简单给我准备一套议题，发给参会的人

这条里面其实藏了五个动作，读三个人的日程、算交集、做文档、建日程、订会议室。

不确定的会和我确认。

![取图工单：WorkBuddy执行该任务时的Todo清单，能看到它逐步在干哪几件事](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc2N8lpzVpLe3iar2yzShAc01ibiardvLDhacbSmwvDGtJSrSPfdrDEbl3V5rxF0vg9q7tWHZsicVc6XpVoobD6TFjibUm6q2M457fvI/640?wx_fmt=jpeg&from=appmsg#imgIndex=17)

完成。

![取图工单：飞书日历里新建出来的那条日程，含参与人与会议室](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc12jibWLxdIHOaufgjFTV0wS23hM2SHn8j5icvUzNSFQg1pibktnvia3uGtwkKcoZf5m9mlOgFpG0icwJQrm4e8nMLutzyD3LTZ6Wbc/640?wx_fmt=jpeg&from=appmsg#imgIndex=18)

飞书上日程也有了。

![取图工单：飞书日历里新建出来的那条日程，含参与人与会议室](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc3xfeV1Tic6zzxbbz0ls4pxX7fW2qRlOjM2zWlwRv6UrvQ7VQdhWkv6SVWJEPQRPOkonter2ubOco4VfCShyibYnwLf1ksIia8qfg/640?wx_fmt=jpeg&from=appmsg#imgIndex=19)

爽！

## 实操二、文档、表格联动方法

04

其实这部分，和上面同理。

不过这里需要了解的是，要充分发挥 WorkBuddy 本身的看图、搜索这些能力。

比如说。

**让它读飞书里的文档，再补充一些资料进去。**

直接说文档名就行。

●●●

读一下飞书文档【MVP 规划对齐】，为我进行详细的自媒体自动化平台竞品分析，然后梳理整理到文档中。

![取图工单：WorkBuddy读取指定飞书文档的执行过程](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc0P3Cx2SGeOLOOiaebriaSuSt7B7H3arsBG5ibBFvX8TicgMNTMnBAwB5icUmEVlZ4mIetcJThAExpCvvDGACWTIMiaLgAicrmicf0Vyg4/640?wx_fmt=jpeg&from=appmsg#imgIndex=20)

大量的联网搜索，整理出来直接落回飞书。

![取图工单：WorkBuddy读取指定飞书文档的执行过程](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc32q0msoOnLxqLic7URZfr7sYIqjpfJQvY4XBoQYiac7iaTaQQeicSaPQsIudtULicia3BySonVkaicicqSdYkZCjxdzjjZX5J8XyzseKY/640?wx_fmt=jpeg&from=appmsg#imgIndex=21)

文档里也直接更新了。

![取图工单：WorkBuddy读取指定飞书文档的执行过程](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc0SHFLChHzfXQp2V475spibyHGNWrThR8VypyQafGgaHric0vhM0f7eoNN7CVcXJo0Xo4MXAtcdWMbibmD7X2YCGIGYk8RVD7fJDc/640?wx_fmt=jpeg&from=appmsg#imgIndex=22)

其实这样的场景我接触得特别多。

> 团队管理一个项目情况进度，快速迭代。
> 
> 个人知识梳理，不断丰富。

之前有很多企业都想要做这样的自动化系统，现在用WorkBuddy + 飞书就直接实现了。

对于表格、多维表格、知识库、飞书妙记，都一样。

读数据，写数据，甚至做计算，做分析，都是通过在WorkBuddy中发指令就行了。

这些都是基础能力。

其实可以看出来，通过不同能力的组合在不同的工作里面可以玩出花来。

那么接下来，就是终极实操了。

## 实操三、全自动自媒体爆款管理

05

这一节应该是精华用法了，自用的自媒体管理系统。

整个逻辑完全由 WorkBuddy + 飞书妙记 + 飞书知识库 + 飞书多维表格构成。

当然，也适合所有需要知识管理的场景。

做内容的朋友应该都懂，最耗时间的从来不是写，是前面那一堆选题、整理。而这些，其实大部分来自于爆款。

所以，看到爆款，整理存储，总结备用，这其实是所有自媒体人最重要的一步。

这个实操就解决这个问题。开始。

**1\. 准备爆款知识库。**

先建一个知识库。

●●●

为我在飞书创建一个爆款知识库，叫【爆款整理】，其中构建一个多维表格用来管理爆款，至少包含标题、加入时间、爆款发布时间、飞书妙记链接、爆款逐字稿、值得借鉴参考的内容等列

![取图工单：WorkBuddy读取指定飞书文档的执行过程](https://mmbiz.qpic.cn/mmbiz_jpg/J1Cdba5GUc2iavibSPh9dDSFxxuK4chCmhaQeibouqdyGRaCWDcd3NjA4HEzIjBWcesXuXG5WWAn7dvmITXF2cecCZMrn12f3II5kXPnYxib2Qc/640?wx_fmt=jpeg&from=appmsg#imgIndex=23)

打开飞书，能看到建好了。

![取图工单：WorkBuddy读取指定飞书文档的执行过程](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc0ZOOZ1hibLu2blBLTPaMymRRKwWqDh0omQBJuuuJjOofEwibMO8XjJMW21alLUvxg5Tmn4LsDjkicvy4L8VIrxOFQ7wmqUyMI2vk/640?wx_fmt=jpeg&from=appmsg#imgIndex=24)

后续，我们的所有内容都会自动管理到这个知识库中。

**2\. 搭建自动视频解析分析流。**

这里就需要用到一个视频下载的 Skill。我也为大家准备好了。

🔗：github.com/idiotLeoLYJ/Daliu-Awesome-Skills

安装方法也很简单，直接在 WorkBuddy 中发指令就行了。

●●●

为我安装github.com/idiotLeoLYJ/Daliu-Awesome-Skills中的视频下载 Skill。

![取图工单：WorkBuddy读取指定飞书文档的执行过程](https://mmbiz.qpic.cn/mmbiz_jpg/J1Cdba5GUc1MYcI53emiab612QKpZY8icAspTIyuhY5e1RlibWXLmXp5nBSYQGiauD2YmvLAoIkcicKnMhNwVgnX2UdmlaJq2X7hMJqhNviazpuFQ/640?wx_fmt=jpeg&from=appmsg#imgIndex=25)

那么以后，我们刷到比较好的视频，引入这个Skill，就可以让他下载。

![取图工单：WorkBuddy读取指定飞书文档的执行过程](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc08uiaQQmwmmwnyeNibjjdkBEibW4Mtg3muxX6yrRCG6vkKWmDOoEibK0R6ia3Dicz1cCvtg1a16icem7bVfHzLrMd6IlwicABVSXfkicLM/640?wx_fmt=jpeg&from=appmsg#imgIndex=26)

当然，我们的目标不是单纯的下载视频，核心是挖出来里面的脚本，然后管理到飞书里面，以后作参考。

所以，这里的提示词还需要更进一步。

●●●

/视频下载器  
  
1.为我下载这个视频：【视频链接】  
2.上传到飞书的妙记中为我整理逐字稿。  
3.将整理出的所有内容，根据【爆款管理】多维表格中的各列维度，新增一条。

![取图工单：WorkBuddy读取指定飞书文档的执行过程](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc231bssTbw7fkQpxUFOHFHibYE20hflhS69pjAOn9MibEnwIF0znnwOgvRCJ5eHLGowTUWRkUib7ebicUTCnYE7XmKRGCZvGFZbV2Q/640?wx_fmt=jpeg&from=appmsg#imgIndex=27)

这里给不熟悉的朋友简单讲一下飞书妙记这个超级无敌好用的功能。

简单的说，它的功能就是可以将任何上传的音频、视频快速整理出逐字稿。适用各种场景，特别是会议录音以及视频分析这种。

![取图工单：WorkBuddy读取指定飞书文档的执行过程](https://mmbiz.qpic.cn/mmbiz_jpg/J1Cdba5GUc2LqQH0zrViamhGo2zWHqE6BG5DicDetM5aRnSAFDkwFsWTOXcCYrhnKN2GM4weticqttSebXKibuRQOkD0IE4Lns8DMXGALxicKeib4/640?wx_fmt=jpeg&from=appmsg#imgIndex=28)

它嵌入在飞书中。

当然，WorkBuddy 也可以操作它。这就很爽了。

回到任务，发送之后，整个过程会产出好几个分析的内容。

![取图工单：WorkBuddy读取指定飞书文档的执行过程](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc2UZUfiahiaX8tD7BUqXTbIkFKTCGibBMfja0Pf17ZY8KmOfCbIicfN7ZWKa9wpniabCxPkrWs3OMSdpqrPhicuAiaADfclJPahFFexQQ/640?wx_fmt=jpeg&from=appmsg#imgIndex=29)

以及妙记中的视频和逐字稿。

![取图工单：WorkBuddy读取指定飞书文档的执行过程](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc1CkH0UHGMG3DAUxBZ3qyZwicIQOPdVw2YogFwAqw0gf0Va9fndhRohuvUNqCiaZWslCMYxnAPicXUwHfgdGhicGhDyBUC1ljLA5fQ/640?wx_fmt=jpeg&from=appmsg#imgIndex=30)

最后自动管理到了我们第一步创建的爆款管理多维表格里面。

![取图工单：WorkBuddy读取指定飞书文档的执行过程](https://mmbiz.qpic.cn/mmbiz_jpg/J1Cdba5GUc2GHSaupAfiaGx1ksvQicvxXsQjicmiabJqQElEyiaibkrYOEv2GufgSibiacSQkjmf5NiaEvLoq7aoK30XKwOaOBicmLHH3AibnV2dmy01ho/640?wx_fmt=jpeg&from=appmsg#imgIndex=31)

完美。

**3\. 每天为我规划选题和脚本。**

这里就用到 WorkBuddy 的自动化能力了。

构建一个每天自动从爆款管理多维表格里为我梳理爆款的定时任务。

●●●

从飞书多维表格【爆款管理】中，为我每天挑一个最适合我的爆款给我，并告诉我有哪些学习的角度

甚至推送到 WorkBuddy 小程序，手机端随时看。

![取图工单：WorkBuddy读取指定飞书文档的执行过程](https://mmbiz.qpic.cn/mmbiz_jpg/J1Cdba5GUc2skTjDicE1LBnOkWrNVpv6EeHnIx4JM4AXwlrooedYotr2XxAVoRAScSvMCB3o3Z57wUQSqBMB8PncKgiaKlJoLDv9yLL7nr7CE/640?wx_fmt=jpeg&from=appmsg#imgIndex=32)

**4\. 整套流程构建为一个Skill。**

上面就是一个标准的找爆款、分析爆款、推送素材的过程。

不过这4步，对每个视频都做上面三步，还是麻烦。

所以，可以做成一个Skill。

●●●

为我做一个Skill：爆款管理工作流。  
  
每次我给到你一个视频链接的时候，都自动完成；  
1.用视频下载器 Skill下载视频；  
2.上传到飞书妙记进行解析；  
3.将整理出的所有内容，根据【爆款管理】多维表格中的各列维度，新增一条。

![取图工单：WorkBuddy读取指定飞书文档的执行过程](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc1jkuKHibAjHJ4A8Hh55O1s9I218QKoWPXH5R7f2dqK3j1uicwkJAN04bn2MibUuY2mQj9icmibsvJBMBOoxABwDd6OPrSNR3944dgo/640?wx_fmt=jpeg&from=appmsg#imgIndex=33)

那以后，用的时候，复制一个链接，引用这个Skill。

![取图工单：WorkBuddy读取指定飞书文档的执行过程](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc0goj2OTEDaMMmyicRKQHJkgXh7gSziaiavCOLlmRMDhvSCnibpB1dGGicBv1G4P8a1eSbJZ6ibyTAckjP9vyUZS82KZemHs3snCptc8/640?wx_fmt=jpeg&from=appmsg#imgIndex=34)

全自动，爆款管理。

再加上每天自动推送爆款分析。

选题灵感这不就源源不断了嘛。

顺着这个逻辑，再增加，自动写脚本的方法，管理到飞书文档中。

基本整个自媒体自动工作流就搭建完了。

## 实操四、远程用 AI 工作方法

06

前面这套自动流程都是坐在电脑前干的。

但我们刷视频的时候，肯定是在手机上看得，不可能还得把链接发到电脑上，再用电脑调用skill操作。

所以，再结合上，远程连接 WorkBuddy。

这套躺着管理爆款的正确姿势就是：

刷手机，然后把链接转到手机上的 WorkBuddy，自动做。和分享给朋友一样简单。

![取图工单：WorkBuddy读取指定飞书文档的执行过程](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc3dOuDTAfsTWvD39b4obvibw1UH9cUAiatXe3ibSpEib6vD0fI18RBFmJIXbS37T9AR2xVBSACW5bLPv8lz9ibmSfWX5emVA4JTwmibc/640?wx_fmt=jpeg&from=appmsg#imgIndex=35)

后续也会自动管理到飞书的多维表格里，到时间给你推到手机上。

步骤也很简单。

**1\. 先把远程的两个开关打开。**

打开 WorkBuddy， 左下角头像旁边。

![取图工单：助理设置页，红框标出远程相关的开关](https://mmbiz.qpic.cn/mmbiz_jpg/J1Cdba5GUc13GvbEn54ulaoWAiciciaic3XUQL0prb9Yl1F9HquVBD1fyucfggMU7ENjps3MWwo4C2zB7nX011QszosHbAWdbcicu7cZUemRXNXg/640?wx_fmt=jpeg&from=appmsg#imgIndex=36)

两个都选上。

**2\. 手机上打开 WorkBuddy APP 或者 小程序。**

就，行了。

恭喜你，拥有一个 24 小时在线的爆款分析师。

## 写在最后

07

感谢大家一直以来都比较喜欢，这种手把手的教程。

不过，我依然想说，跟着做是必要的，但是更重要的是理解整个的思路。

因为，不是所有人都有这个自媒体的需求，但是如果能梳理出其中的原理和思路是可以复用到非常多的场景。

这也就是我们常常说的。

AI时代，那种可能性。

比如说，这个教程里面。

> WorkBuddy和飞书文档、表格、妙记等等配合的思路。
> 
> 再进一步，通过Skill化让流程可复用的思路。
> 
> 更进一步，随时随地都可以操作的思路。

我相信，这些思路可以用到非常多的场景。甚至WorkBuddy也可以接入很多产品，比如说炒股的、知识管理的、视频生成的、CRM、ERP等等等等。

![取图工单：助理设置页，红框标出远程相关的开关](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc01QMMS8G6icKERQSSlR3sUtI8vyX7nF37ZCyv0wHYgfLrvlQ5BoRFoXQuSGjfPqm5sVqgAmCibfjGe6budaB89RAKv12GNiccnTg/640?wx_fmt=jpeg&from=appmsg#imgIndex=37)

有了这些优秀的产品。

下次，我们可能轻松就做出来自动选股系统、自动知识梳理系统等等。

那一切的根源，就来源于我们对可能性的把握。

所以，别急着问我该用哪个，或者哪个最强。

先做起来。

跟着实操一个。

以上，既然看到这里了，  
如果觉得不错，随手点个赞、在看、转发三连吧，  
如果想第一时间收到推送，也可以给我个星标⭐～  
谢谢你看我的文章

**你的关注是我持续更新的动力～**

**我是谁**

我是 AI大刘，北大毕业，大模型研究方向，腾讯犀牛鸟，先后在腾讯、百度的大模型研发部门。现在斜杠青年：给多家国企做AI顾问 \\ OPC \\ 研究员 \\ 产品独立开发者 \\ Vibe Coder

爱AI的大刘

邀请你前往腾讯公益一起捐

筑梦藏乡行动计划

154人捐赠

WorkBuddy完全教程「连载中」 · 目录