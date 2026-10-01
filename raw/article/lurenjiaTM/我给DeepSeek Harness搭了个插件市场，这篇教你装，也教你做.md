---
title: "我给DeepSeek Harness搭了个插件市场，这篇教你装，也教你做"
source: "https://mp.weixin.qq.com/s/KvUdaaNcdcRPMn3DlRWAfQ"
author:
  - "[[路人甲TM]]"
published:
created: 2026-09-05
description:
tags:
  - "clippings"
---
路人甲TM 路人甲TM *2026年8月20日 19:44*

DeepSeek Harness开源那几天，数字涨得吓人。

发布当天1个半小时2.2 万星，一周冲到16.6万，是GitHub历史上增速最快的项目。

而除了DSH本身，还有一个有趣的现象，不到一星期，github上审核过可安装到dsh上的插件就有1300多个，带dsh-plugin标签的更是有近8000多个。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbAzxAjMquUiaClBibN4zwNVbFNTwicrLpV53vK4ugT4n7q6wfWf2aIoN9tojRnicTKCSoOeunNH4TbX2f8vPt9nlG0gNDbvnrGrBwQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

插件能被大规模迅速玩起来，源于DSH的核心设计理念「一切皆插件」

官方架构文档里有一段原话，大意是，产品的每一块都是插件。

模型适配器是插件，工具注册表是插件，会话日志是插件，连智能体循环本身也是插件，不存在一块特殊到需要单独打补丁的特权核心。

翻译成大白话就是，DSH从里到外没有一块零件是焊死的，就连DSH本身，也是由独立插件组成的。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbATjWtRavQ4rW3ZS87QqeNxBPtiacQnHoPQq4NiccyNrXLicgIH09WWcibGibOIDlbgqdC58wEKic1N6dGI8EwmyRy7zaS8fBnZqLdicY/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

有人说这是技术人的自嗨炫技，因为普通人根本不懂github，npm是什么。

我觉得可以换个角度想。

这对大多数普通用户是锦上添花，也给开发者更多创造的空间。

当插件社区越来越丰富，更多小众的需求也可以覆盖。

你可能只想要一个深色主题，或者一个实时看token消耗的窗口，现在有人做成插件你就能用，或者干脆自己搓一个，不再是官方做了才有。

现在你可以按偏好把DSH装成自己的样子，每个人的dsh都是个性化的，独一无二、适配个人习惯的。

比如装一个宠物插件，你的设置界面就会多出一个功能选项。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbBlkECE9GAdNQ6wSIicWXGZloMV6hQ4pVaxNO5dNxvxUib7YBJUTwbBnyZRDJgPqxowTuJ5Y2HMb2d1ibB5VQNu94yRBr6BOPG6JA/640?wx_fmt=png&from=appmsg#imgIndex=2)

而且DSH官方把Agent几乎所有的能力都做完了，在这个基础上做到可以随意组合插件，并且互不影响，这本身就是一件很牛掰的事。

DSH插件千千万是早晚的事，我自己实测了很多，给大家筛选了以下几个最实用的，附上安装方法，最后贡献一个我做的插件，怎么做的也会给大家讲明白。

## 先给大家一个精选插件集合

考虑到有不少朋友不太用github，为了让大家轻松愉快的安装插件，我也为此专门做了一个优质插件集合网页，收录了社区里各类DeepSeek Harness插件。

不用再打开github，可以像逛应用商店一样搜寻插件，也可以直接通过搜关键词找到你想要的插件。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbC1yoklFhCXXW9tNVGEhjBJPaquMFibEGXmSIC1brAjcqb0xTCDE6dneMsicTKDXA275qV9zibQkbhTpzWQfHyFKdTPsyNRpftPwA/640?wx_fmt=png&from=appmsg#imgIndex=3)

地址：ip.midonghub.com/dsh-plugin/

每个插件下都有基本说明介绍、原github地址，看上了可以复制命令安装，免去了自己去github上一个个搜索的麻烦。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbCOiceTicubPZ7skugKeKgULfo60IOTI5kcLfo6jDiamPYWmUzBnwyOz2nGZEHd9tU8ibE7UhYUhKTPLZRcqEg6SGTZqCl5tgr67UQ/640?wx_fmt=png&from=appmsg#imgIndex=4)

## 实用又好玩的插件清单

这些插件都可以在上面的DSH小卖铺找到，搜索，复制安装命令，在终端一键安装。

### 1\. DSH桌面端

一切皆插件，这个桌面端本身也是插件，和官方的harness没区别，更方便安装和使用，如果你之前已经用了web端，下载后聊天记录也会同步。

可以下面这条命令，发给你电脑上的其他Agent。装上桌面端后也可以直接让DSH给自己装插件，主打一个自进化，自己修自己。

```javascript
帮我安装GitHub上的DSH 插件 https://github.com/anywhere-labs/deepseek-harness-desktop
```

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbAAHATEg9w04oQA1byFSh68a97BDDClTTnHGIfVqKHpbxuCeUj6uAQTfuHlxEViaaKN8HSyvF1KYibtcvSGgQmn61Lv4ZJ4HUwwQ/640?wx_fmt=png&from=appmsg#imgIndex=5)

https://www.dshdesktop.cn

插件地址：anywhere-labs/deepseek-harness-desktop

### 2.任务跑完弹通知

用了DSH的朋友肯定都发现这个问题了：就是dsh跑完一个任务并不会自动通知，像我这种把指令丢完就容易抛之脑后做其他事的人就很容易过很久才想起这个任务。

所以发现这个问题我第一时间就在插件小卖部找到这个任务跑完就弹出通知的插件装上了：dsh-notification

让DSH自己安装后重启，在设置里启用并测试就能正常通知了：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbAibqMGmnETAPY5eicrLTwj8uqDTwyOtRflWd0M2GEibabD7BWfDtDa2rkVgfE40mh5AvGvedP3lZkW00dLd8te3BblOiaJRJHg66o/640?wx_fmt=png&from=appmsg#imgIndex=6)

地址：omdsh-dev/dsh-notification

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbBeoRO6niaN0ibcIrTYibGibX5w3hlbc7uILqte3JYA0yjVKLrO9d7SCOeW89yLa7ibmmeKfocP5zIQ6ibMX6UqsqbdpKeo0LUbeyvf0/640?wx_fmt=png&from=appmsg#imgIndex=7)

这只是一个插件的小应用例子，但是能看出插件是如何把DSH改造成任意你想让它成为的样子。

3.桌面UI全家桶

这是一个插件组合，包含桌面主题皮肤，任务看板，图像理解等多个插件，你可以直接安装全家桶，也可以只挑一两个安装。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbBqKbCDoRsNx1pocs0t8HPZsj8wMMxHTicKHVEtwPRD8hViaP21XAiasO0vNicHQNX2drdSyftIBvufjymTP6o7LTcWATXyPc8rVT0/640?wx_fmt=png&from=appmsg#imgIndex=8)

地址：zhu1090093659/dsh-web-ui

![图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbBM4W89olgcnzeUwGLicRZVOkib2eprhb2cKICVVq8nmvEX6nlrrAnwEHXcIjN2icVZ7O2ahtZdQJjsmh0204oGLpicdRAShBAxbm0/640?wx_fmt=png&from=appmsg#imgIndex=9)

我挑了三个，有好看的也有实用的，给大家讲讲。

第一个是主题皮肤。

桌面皮肤终于不是精简克制的蓝白色，你可以一打开DSH就看到可爱俏皮，爱偷吃的蓝色大肥鱼。

说到蓝色大肥鱼还挺有意思的，是网友对deepseek的爱称，源于deepseek识图模式出来后，有人把ds图标发给它，它的思考过程里写的「用户发了一张蓝色大肥鱼」。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbBg4Gk4IzUnAhrTaBuOjxpq2MjfVBE55IJnXmR9wnRXgsgGrkQNuChTkjcX9zyeFR9mt0QEwcuorHLoibdwbz8KKTmC0l4WEkc0/640?wx_fmt=png&from=appmsg#imgIndex=10)

还有下面这些，不仅仅是换个背景，而是直接换了一整套UI。

比如这个有初音未来主题的，谁还认得出这是DSH。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbBxCqxQVFxFU9PkoTP5YLjjI40gdAzLcKiaRKGIibBOXjQKibOtxic6Mg30rbnqicXiacdCvblomoSh321zwV1Ur96eUdqvY9AM96ISY/640?wx_fmt=png&from=appmsg#imgIndex=12)

甚至还有这种实时行情跑马灯，你以为我在写代码，其实我在看长桥港美股行情。

，时长00:04

<video src="https://mpvideo.qpic.cn/0bc3aea5uaabo4agm2mhrbvfcaod3iaqdwqa.f10002.mp4?dis_k=e1560307b620c090307d60d00e8aa52e&amp;dis_t=1788571874&amp;play_scene=10120&amp;auth_info=Z/aAvMVuCg5BwYeyj3Z2QzsSOWJON0IFe3cXVkM8IzVdLEpBZEURQzYFQ29nG3tjLxg=&amp;auth_key=6c92bd1d1725c85201b9ab081232f9b1&amp;vid=wxv_4657735931456798724&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

觉得还不够，主题皮肤插件里预设了12款皮肤，这下可以按自己的喜好装扮DSH了。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbC1uYTZtt75OwjhMJkH5utDlkh4JW70nticpRliaFoyYZ4leWzqvAAGBAhzpOTXJ28TFsFJN8N0lr90LN2WV8Gjwf1iblNShjnHibs/640?wx_fmt=png&from=appmsg#imgIndex=13)

@linxin666/dsh-client-ui-skin-center

前段时间在codex养宠物玩得很开心，现在DSH里也能养宠物了。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbDwEVtmo2KkIOaP5tnVLPlV3oZoCNGlKUV7U9Ca2Zy8HPcykAj6Ql9aTqQAJmZht6VEFUUIvUDl0RY59kp6GoIUu5g9bzAzRWE/640?wx_fmt=png&from=appmsg#imgIndex=14)

地址：linxin666/dsh-pet

宠物和你的对话状态是连接的，可以看到目前的状态，等待无聊的时候可以来点互动增加亲密度。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbCmCiciaic5ANKk9vngUBjduezc7GsbQc6Dlq2T4icibWUo78sZxDkGJibNicoRLKPamVHOyzKV5PLoXw8IbG17IJW3Xcpia0BiaLGvQ1kg/640?wx_fmt=png&from=appmsg#imgIndex=15)

第三个是文件预览。

这个插件功能很实用，对话中的文件集合在右侧，找文件的时候就不用一个一个对话翻了。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbDH7jDMw5soWIOQC1fNAE8vibgMXoq2LOX3pcFXs8bV7uDJhB9j5UvMlSiaYFTR3PvGmpPZgvuoAs44QYpejibBBULOPXA7EDUvbY/640?wx_fmt=png&from=appmsg#imgIndex=16)

地址：dsh-better-sidebar

### 4\. 浏览器助手

dsh-browser是一个Chrome侧边栏插件，装上之后 DSH 可以直接操控你已经打开的浏览器标签页，读网页、点按钮、滚动、跳转都能干。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbAlpTwsdMJ1Uicu3CXYAqQyyaSiaicicb9UKoiaT1NS4CL7sPuhb1GZQIhZy1SJ6cWX5BibtOmO6JWk7PsTyrNxY7kEJDWHPhDkJTN6c/640?wx_fmt=png&from=appmsg#imgIndex=17)

地址：Lum1104/dsh-browser

DSH 默认接的 DeepSeek 文本模型看不到图，这个插件把网页转成一段带编号的结构化文字，标题，正文等等，列出可点击控件，模型按编号去点，不需要视觉能力。

用它最直接的好处是：

不用把账号密码交给一个模拟浏览器，它直接在你已经登录的网站里干活。

比如我最近想换电脑，比价比得烦，就交给了 DSH。没装这个插件时，它只能把各平台的价格汇总给我，具体哪家，哪个链接还得我自己找。

现在打开淘宝京东的页面，发一条指令，它自己比价，直接帮我把东西加进购物车。

```js
帮我在京东和淘宝看看Macbook Air M4 M5，把你觉得还不错的加入购物车；对比一下价钱，不同配置目前的价格和优惠整理好发给我，给我购买建议
```

![图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbCZmvhscXzggiatxcr5YGypCxOuTxLWthn5k3PFaCbALZ1l75RtLjG3rpjQ928M1WBOkawj9xfwv0GoSLUnQvVv8j89E8wOMMNY/640?wx_fmt=png&from=appmsg#imgIndex=18)

## 怎么自己做一个插件- token计量

讲了这么多插件的概念，也看了一些好玩好用的插件，不知道大家会不会和我一样有点手痒痒，想看看能不能自己做一个插件玩玩。

这不，我先让dsh帮我评估一下自己动手做插件的难度，下面是它给我展示的三档难度框架：

```swift
简单档（纯 UI，只有 client 半）   ↓ 加 host 半（碰文件/命令/事件）进阶档（client + host 两半）← 以上分享的基本都在这   ↓ 加整个应用壳（Electron + Cordis 组合）宿主级（DSH Desktop 本体）
```

做个简单挡的静态ui也太没挑战性，反正有DSH帮我整，不如直接上进阶档。

刚好，17号DeepSeek刚涨价，我也很好奇涨到什么地步、烧钱烧能烧多少，就做了个在侧边框可以查看每个API在dsh的当日token消耗和对应的账户总余额的标签。

先看看效果：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbDCr2L472y2daf3ECPDFyhJ2fk9iathxvMCxCBLfAda3miaibRM7G7iavEWgNy3TnLebRpEg9eIHZicicVU23uXVQM5bV8hjq45Xdx7k/640?wx_fmt=png&from=appmsg#imgIndex=19)

下面再来一起看看整个孵化过程，看完你也能根据自己的需求做出个插件。

开始前先提醒大家使用「创造模式」，因为只有创造模式带 `dsh-tool-cordis` 工具，其他三个模式都没有，这是四种模式里唯一为插件开发设计的模式。

首先我先是用大白话尽量描述清楚我想要的这个插件效果和功能：

```js
在左侧栏设置的上方加一个小框，可以查看目前接入的模型api所在的账户在dsh的消费情况和账户总余额
```

接着让DSH根据描述先做需求理解，保证我们说的是同一件事，对齐下颗粒度

再做下难度判断，了解一下做出这个插件的可行性：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbABibrdxNIzmsfia7eGbLdDl9sIeJ2X3lXVjtqwq6h2LgDsHcviclCQORRdZ3owmUuVbyHWa16a6akUKxfYYjzE2rheubic04YZKgU/640?wx_fmt=png&from=appmsg#imgIndex=21)

接下来也别急着直接让dsh开始跑，直接跑出来了很可能不符合预期，token也都白花了。记得要先让它出几个效果图方案给你看方向：

![图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbBjxgND9j8erT7WTn5p6xus7jkm3IbUzWeibibdAgvAdM33aq4ibTLs6qAibnDialEzynz6dibAPGtL7xzuoYAyibHs1ibaZ95qpcO8vEc/640?wx_fmt=png&from=appmsg#imgIndex=22)

这三个就是dsh给我的三版初始方案了，我个人偏好第三个多账户的，可以平行看到接入的不同模型的账户，就在这个基础上修改一下就让dsh开始跑了。

别以为这就结束了，我本也以为需求沟通得差不多了，连效果图也够像样了，这么个小插件做出来应该不难。

可真没想到接下来的过程却没那么顺利，碰到了需求确认不足、环境查证不足、测试与真实脱节等等问题。

说到底是一个毛病，DSH 太急躁、太积极，急着推进，脱离了原本的指令。

这也是我在跑这个插件时才意识到的问题。

举个例子，在得到三个效果图方案后，我只接着询问了它图里的今日tokens是显示的dsh消耗还是账户总消耗，它在回答我的疑问之后并不是停下来等我给下一步指令，而是自行开始推进，直接在这一条回答里花了21分钟把第一版插件跑出来了。

结果当然是不尽人意。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbBTZMpLqiaNrZRNicw05MSXfZlesXwQCsqZjhY7HhhSYOX2SsIUQ7UdrK9hcGS4AibIa10GoqhLfgt0j1U3YdFwRrH7Iv9k4XBsuU/640?wx_fmt=png&from=appmsg#imgIndex=23)

类似这样的问题在整个过程里层出不穷，这是最致命的。

意识到DSH这个毛病之后，我开始在每条指令后面加约束，核心两条，不准自己扩展范围，遇到选择先问。

我这里也针对这个根因写了段约束提示词，直接复制这段加到每条指令末尾，能很大程度约束它不撞南墙不回头的冲劲：

```markdown
【执行约束 - 必读】1. 边界：只做我明确要求的事，禁止主动扩展范围、添加"顺手就能做"的改进、实现我未提及的功能。任何超出指令字面意思的动作都算越界。2. 确认：遇到歧义、多个可选方向、或任何需要拍板的决策时，先停下来用简洁的选项问我，禁止用"推荐选项"或你自己的判断替我做决定。我说"先别急/先讲方案"时，必须停手，只输出方案和影响，等我批准才动手。3. 节奏：分步推进，每完成一步先汇报结果和下一步计划，等我确认再继续。禁止一口气做完整条流水线。4. 验证：引用任何模式/方案前，先验证当前环境是否支持（服务清单、依赖机制、运行行为）。测试必须贴近真实运行，mock 与真实行为不一致时不得当作通过。5. 提问优于猜测：不确定就问，不猜。你的每一个假设都要说出来让我确认，而不是闷头执行。6. 如果你认为指令有更好的做法，用一句话提出建议并说明理由，然后等待我的决定——不得直接采用。
```

加了约束后给指令跑任务就顺畅不少，我的插件也就顺利做完了，在设置页还加上了账户计量的区块，可以更细得看到统计的每日按模型和会话的消耗明细。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbCQyQOXia0rc9oBCDweR81ZncAbXHvhbxiaI4CNjaWp2cG1x2tTyiaxl2nq4vzYqPpagoTkQiam6icvwAqLmMcyW94sxrKQib8NyLgug/640?wx_fmt=png&from=appmsg#imgIndex=24)

这个插件我也传上GitHub了，大家感兴趣的也可以装上监视你dsh的token消耗。

![图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbC99Qv9mJSvj84Ownnx1COptzCtdnJDMxzondKzkMiap6Uv8iaCFNSfuAVpd7cgJVUlY87cEneQZmY6no0mbjCgKabfN3d5Zia7qw/640?wx_fmt=png&from=appmsg#imgIndex=25)

## 热闹之外，还需要秩序

最后还是要诚实的泼点冷水。

DSH还是预览版，插件多了，问题也跟着多。

有的插件装上会不兼容，冲突导致崩溃，质量参差不齐，安全性也要打问号。

所以我的建议是，别随便装插件。

优先装社区持续管理、筛选过的插件，装之前再审查一遍。拿不准的时候，把下面这句话丢给 DSH，或者丢给你电脑上任何一个 Agent。

```js
帮我确认这个插件「地址」，检查它是不是真的 DSH 插件、源码有没有问题。
```

一切皆插件，意味着一切想法都可能进入这个产品，这让未来的 AI 长什么样，从此不光是开发者的事，每个用插件的人都在参与决定。

共建这个DSH生态本身很激动人心，但生态要持续健康发展，还有一段路要走。

敢把「核心可换」当作核心理念的产品不多，上一个这么干的是Emacs，一切皆Lisp，活了四十年。

DSH 能不能走到那一天，要看插件生态能不能在热闹之外，长出秩序。

最后想说说做这件事的人。

梁文锋说过很多次，他们的长期目标是 AGI，通用人工智能。我的感受是，对怎么抵达那里，他和他的团队心里大概已经有了答案，DSH 就是答案的一部分。

把一个能自进化的框架先放出来，让社区往里面装插件，或许也是一种尝试，让Agent的样子在真实使用中自己长出来。

不管过程怎么样，方向是确定的，子弹已经出膛，接下来就让子弹飞一会儿。