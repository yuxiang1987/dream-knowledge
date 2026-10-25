---
title: "和 Opus 5.5 同题交卷，MiniMax M3.1 让 Flash 开始超纲了"
source: "https://mp.weixin.qq.com/s/pslYXu1mU2QbT5kZdefA-Q"
author:
  - "[[发现明日产品的]]"
published:
created: 2026-10-03
description: "从智能的高度，到使用的广度"
tags:
  - "clippings"
---
发现明日产品的 APPSO *2026年10月2日 14:02*

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/dCG7OC48IfLqyZeoaHNhXEhcVy0zTwhKV7Hcmic3CxVDRbZoK0ZNW6iaTHB8OyRDiaFCrvA8Hicav4tZO2U6VbxUtic6QYzgyWNJjvkDicw9aqAeY/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

中秋刚过，国庆又到，AI 圈却没有跟着放假。

新模型依然一个接一个地上线。旗舰模型忙着刷新能力上限，主打速度和性价比的模型则在争夺用户的日常工作。不过，随着后者的能力不断提升，两者之间的分工也开始变得模糊。

过去需要请出旗舰模型的任务，如今交给一个名字里带着 Flash 的模型，究竟能做到什么程度？前端创作是一个很直观的观察窗口，配色、排版、动画和交互做得怎么样，把作品放在一起就能看出差别。

上个月，Anthropic 推出了 Claude Opus 5.5。我们在 X 上看到，有人用它做动态作品集，有人让它画水墨动画。这些由代码做出来的作品，已经有了各自的风格。

最近，APPSO 发现一款国产模型也开始成为 X 网友的新宠，这是上线不久的 MiniMax M3.1 Flash Preview。

![Image](https://mmbiz.qpic.cn/mmbiz_png/dCG7OC48IfLZJ3JPAlJUgUiahkWtj7pRs5yS9AzFC6N0WMjHfgfEFsv7y1UCbSspVEBLeMhONG5VeXw3ic9lZicYPftteYZiaKjpiaE3GknKOvu4/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

此前以 Space Bunny 为名受到开发者关注的匿名模型，也被网友精准关联到了 MiniMax M 系列。就连 OpenCode 的联合创始人 Dax，也建议大家用测试 Opus 5.5 的题目来试试 Space Bunny。

![Image](https://mmbiz.qpic.cn/mmbiz_png/dCG7OC48IfIQbZpxbiblKcepjPibECpCXsZBuLIYwvYSOcVLZMgbs9TbYnChLNLqAmoIoYdhccYFUVEJjGJwL6cibqjyB3ic4jBSHwh5L8z2Lvo/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

虽然不知道「太空兔」是否就是 MiniMax 家的，但M3.1 Flash Preview 名字里带着 Flash，很容易让人先想到速度和性价比，但我们更想验证，它在前端创作上，能否与 Opus 5.5 这样的旗舰模型一较高下。

于是，我们在 MiniMax Code 里沿用 Opus 5.5 优质案例的公开提示词，比较作品的视觉风格、动效编排与整体完成度，再通过更多题材观察它的多维度能力。当作品摆在眼前，Flash 模型能否做出接近旗舰水准的成品，就有了更直观的答案。

![Image](https://mmbiz.qpic.cn/mmbiz_png/dCG7OC48IfJBxrZkJjXeOUSN6D8SALSiatHLpaichxluCoA1xN8TEmDhibX3n7T3e1WhtDt3uveLp03RFn6vc6LdNaia0fp94Y0hlH9zcTQ0Uo0/640?wx_fmt=png&from=appmsg#imgIndex=3)

### 同题不同解，设计不分高下

给模型的要求很简单，做一段 15 秒的动态设计作品集，让人看出你是一个出色的动效设计师，最后交付一个 MP4 文件。

没有指定配色、字体，也没有写分镜。除了成片时长和用途，具体怎么设计，基本交给模型决定。

M3.1 Flash 生成的片子里，米白色大字铺满黑色背景，荧光绿从字母背后亮起。文字退场，圆环和三角形沿轨道运动，接着出现波形、跳动的数字和能力列表。短短 15 秒，字体、几何图形和数据动效轮番出现，始终沿用黑底与荧光绿的搭配。

![Image](https://mmbiz.qpic.cn/sz_mmbiz_gif/dCG7OC48IfLuWZ2NM5mOKpLWpKibT1bAdJMrTjSM2qS8wOwkvAwuPFgPUXukLGW0k1N3MaSfmqibt1QOyYt91pd1Vzl2ONq88cLwRiaEbQM3vY/640?wx_fmt=gif&from=appmsg#imgIndex=4)

▲ M3.1 Flash 动态设计作品集。

这个创意来自 X 上的一支 Opus 作品集。我们沿用了作者公开的提示词，只追加了 MP4 交付要求。

![Image](https://mmbiz.qpic.cn/mmbiz_gif/dCG7OC48IfJibytggjA6aVibyYag82d4dicIZgzfH2dTAMAjN9RCliaxjLWMIz8qOLxlELmAqn1sIEIyfOfrEcDGmdLQut2EfROSQL4qngcOUBg/640?wx_fmt=gif&from=appmsg#imgIndex=5)

▲ 左边是原作者标注的 Opus 5.5 作品，右边是我们用 M3.1 Flash 打造的成片。

左边的 Opus 把大字排版、缓动曲线和色块变换轮番摆出来，像在展示一组动效练习；右边的 M3.1 Flash 则把圆环、波形和数字放进黑底荧光绿的视觉体系里，更有科技主题短片的感觉。

如果要给一个科技项目选方向，我会更偏向 M3.1 Flash 这版。大字、细线和图表的大小、疏密都在变化，配色始终统一，各个段落之间也有视觉上的联系。Opus 展示的动效种类更直观，M3.1 Flash 则把几个段落组织得更像同一支片子。

至少在这项任务里，M3.1 Flash Preview 已经具备与 Opus 5.5 同台比较的前端创作能力，而且在风格统一与作品组织上，给出了更符合我需求的结果。选择它，并不需要先说服自己接受一个明显逊色的设计。

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/dCG7OC48IfKB9SfSsia4xBoAjXMWckP3hqbGAwzBFqkDsshSuKxQCBOJrfbh7iaxU8wC4SvzAzP8zTIY530DnkbCibYrdKsh7q280bLg0l48Xc/640?wx_fmt=png&from=appmsg#imgIndex=6)

▲ AI 生成示意图，Logo 来自 MiniMax 官方品牌资料。

### 对多模态的理解，藏在场景细节里

一支科技短片做得漂亮，还不足以说明模型能够应对不同的设计意图。继续换题材，才能观察它会不会始终沿用同一套视觉习惯。

「人生的意义」是另一个来自 X 网友 @HarveenChadha 的创意。交给 M3.1 Flash 后，它变成了一支手绘短片。

米色纸张上铺着绿色山丘，一个小人开始追问这一切是为了什么。接着，场景换成方格纸，沿路出现「更多」「更快」「完美」的路牌。走了一圈，画面里的问号反而变得更大。

![Image](https://mmbiz.qpic.cn/mmbiz_gif/dCG7OC48IfJpckQagxXlyny5yToicsbKkP6bHejsELYxruR8820cGGrHCUUx4Uw5pRstjqG1NlicuffFbBo2WkKEXJDge5mn1D2NX5Jzz0yrQ/640?wx_fmt=gif&from=appmsg#imgIndex=7)

问号逐渐分解，故事落到了几件小事上。有人准备了食物，一个笑话逗乐了朋友，种下的植物长了出来，还有雨天、猫和自己做的一件小作品。

模型把这些片段排成一面纸片墙。前面还在寻找一个很大的答案，后面已经开始观察一顿饭、一株植物。

我觉得这一段最合适的设计，是它选了手账的形式。纸片、铅笔线和小插画贯穿前后，既能承载开场的追问，也适合记录后面那些不起眼的日常。画面形式与故事内容之间有了联系，观众更容易跟着它的叙述往下看。

接着我们也尝试复刻网友 @akokoi1 用 Opus 5.5 制作的《小蝌蚪找妈妈》的案例，效果如下：

![Image](https://mmbiz.qpic.cn/mmbiz_gif/dCG7OC48IfIdelebBqkECMAX3d0ZlTQib67WiadXriaVtFFI1vCiaaCpzj8NL7ttDOpjWRs2JkTjoZGAa3RNjN1GvwoM2yxqSmaoo0pMFodCiaoI/640?wx_fmt=gif&from=appmsg#imgIndex=8)

浅色纸面上，荷叶的叶脉清晰可见。蝌蚪拖着细细的尾巴游过池塘，沿路遇见鱼、鸭子、乌龟和螃蟹，最后来到青蛙身边。字幕伴着故事出现，水墨、纸张和绿色荷叶组成了全片的底色。

沿用 Opus 5.5 案例的创作要求，M3.1 Flash 也呈现出了完整的水墨故事。相比复刻某一帧画面，它更能让纸张质感、角色运动与字幕叙事贯穿全片，共同维持这种风格。

在另一个纽约天际线测试案例中，我选择把画面的变化交给了一条时间轴。

起初，橙红色的天空映在水面上，桥和楼群挡住部分夕阳。拖动底部时间轴，天空渐暗，楼里的窗灯一盏盏亮起来，河面也从暖色反光变成了细碎的夜景倒影。

![Image](https://mmbiz.qpic.cn/mmbiz_gif/dCG7OC48IfK9nMYO1sbgx6QUicib2RgmkTY8Z7iaqiaZRKicKDRN3DrECcdEyic3L47Fv1icQ1bKyHce2vTLibI5twW1icqa0Yu6fiaWSlwS24CcBezR0/640?wx_fmt=gif&from=appmsg#imgIndex=9)

我更喜欢这一版对水面的处理。白天能看到大块的暖色，到了夜里，亮起来的窗户又在水上留下细碎的光。桥、楼群、天空和倒影随着同一条时间轴变化，停在不同时间，也能得到不同的画面。

动态短片由模型安排观看顺序，交互作品则把一部分控制权交给用户。时间轴拖到哪里，场景都需要给出对应的状态，天空、灯光和水面之间也要保持协调，而到了游戏里，画面还需要随着玩家的操作持续变化。

我们又把要求推进到一款街机卡丁车游戏，明亮的蓝天、翠绿草地与红白路肩组成赛道，选车、竞速和结算则串起了完整的比赛流程。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/dCG7OC48IfIPge7UOcu99dSbBqsfwAQqNFOBLKtib1kFBqSuGZiaHDa6Lo7qIiaGQynm1RTK4RBf3bYEMDmV1xaVib1bCtmNJHMBAdSDFoG0hS0/640?wx_fmt=gif&from=appmsg#imgIndex=10)

水下探索游戏换了一种节奏，潜艇缓缓驶过被海水吞没的植物园，青绿色雾气、悬浮颗粒和探照灯共同交代出远近层次。潜艇转向时保留的惯性，与靠近地标后逐渐出现的扫描提示，让探索过程有了沉静的氛围，也给玩家留下了发现细节的空间。

![Image](https://mmbiz.qpic.cn/mmbiz_gif/dCG7OC48IfKnVRicYyPia1vDHhOdA7Tb80ng3zuibHicKicya2qOnXsg0ILoG5dko8bibxFNxwoXXGibNEmX3dzCL6PuNPgo7ibKGhJMnffsiaJ8tZ7g/640?wx_fmt=gif&from=appmsg#imgIndex=11)

小幽灵的叙事游戏则把场景藏进深秋农庄的夜色，篝火照亮附近的玉米和木栅栏，屋内的暖光与绿色门光引导着调查方向。

我喜欢它保留的大量黑色空间，有限的光照让兔子、遗物和灯这些小物件更显眼，也让每一次靠近和互动都有了故事感。

![Image](https://mmbiz.qpic.cn/sz_mmbiz_gif/dCG7OC48IfJ4QphBUYk9DGdda7iay5HTIEUZ6icySodKhLWX6lx8JPBAKqGZxCwrCVM2DPYzLmJFibsA27I0ulI421zAh5wbLFichkhUpLyZCdk/640?wx_fmt=gif&from=appmsg#imgIndex=12)

前端作品的要求，正是在这些细节里变得复杂。视觉设计、动画逻辑和用户操作共同决定体验，单独把某一个部分做好，还不足以完成整个作品。

从动态作品集到手绘、水墨，再到交互场景与游戏原型，M3.1 Flash Preview 与 Opus 5.5 的设计各有取舍，Flash 的定位没有成为作品完成度上的明显劣势，并展现出能围绕不同的创意组织画面，并让设计服务于观看、操作与探索的价值。

### 从智能的高度，到使用的广度

当 M3.1 Flash Preview 在前端创作上交出了足以与 Opus 5.5 掰手腕的结果，选择 Flash 的依据也随之增加。除了速度和成本，作品本身的设计与完成度，同样可以成为使用它的理由。

前端表现背后，是设计理解、审美与代码能力的共同作用。

据悉，M3 系列从预训练起点就进行多模态混合训练，视觉与代码的协同也是理解其前端能力的一个观察方向。创作者可以把更多具体设计交给模型，将精力放在确定方向和判断效果上。

![Image](https://mmbiz.qpic.cn/mmbiz_png/dCG7OC48IfLgCjxO6F2Tpht7rGFBbRMl7Br6JQFyMDk1SeCJdKoo1tXTO6VQm9Kg78nG5U1KPl11GXbqKltfxtDDpib5fke6EafXHgmJvia8M/640?wx_fmt=png&from=appmsg#imgIndex=13)

对多数日常任务而言，用户已经没有必要时刻调用最强的旗舰模型。

随着 Agent 开始连续执行搜索、整理、调用工具和生成内容，单次回答的聪明程度已经无法独自决定整体体验。一个任务可能需要连续调用模型数十次，等待时间与调用成本都会在完整流程中不断累积。

此外，前面的前端案例也对应着具体的工作需求，动态作品集可以展示设计能力，手绘与水墨短片可以提供创意样稿，小游戏则可以验证活动玩法。把想法变成可观看、可操作的作品，能让团队更快地讨论方案，再根据反馈调整。

配色、动效与交互的每次修改，都可能带来新一轮模型调用。以 Coding 为主力场景的 MiniMax M3.1 Flash Preview，如果能持续交付符合需求的效果，速度与成本的优势就能帮助创作者在有限预算内尝试更多方案。

尤其考虑到速度、质量和价格依旧是不可能三角，但 Flash 模型正在改变三者之间的交换比例。许多过去只有旗舰模型能够处理的编程任务，如今已经可以用更低的成本和更快的速度完成。模型的能力上限仍然重要，能够稳定进入开发流程的能力，才更容易转化为实际生产力。

![Image](https://mmbiz.qpic.cn/mmbiz_png/dCG7OC48IfIlr6eicMc25TmADksOAiaegzcicRv4neFXfeFGS7FzRehu2SmALHtcpuX78QXicogsmdbDFjVIibEHMVwS6tglszFQrzsemsutQiaBQ/640?wx_fmt=png&from=appmsg#imgIndex=14)

从这个角度看，Flash 模型之于旗舰模型，有些像 PC 兼容机之于大型机。

大型计算系统曾将昂贵的计算能力集中在少数机构，PC 兼容机则依靠标准化和规模生产，让计算能力进入办公室与普通家庭。当智能也成为随时可以调用的标准组件，一个更庞大的应用市场才会出现。

PC 普及以后，产业价值逐渐向操作系统、芯片和软件生态延伸；Flash 模型普及以后，AI 的价值也可能更多流向 Agent、工作流、专有数据和应用入口。

旗舰模型继续探索智能的边界，MiniMax M3.1 Flash Preview 这类模型则把已经验证的能力带入高频开发场景，而未来更丰厚的利润，可能属于那些真正知道如何使用这些智能的产品。