# 大厂之外，EvoX让我看到了Agent的另一种可能

作者：路人甲TM

发布时间：2026-08-14 18:13

原文：https://mp.weixin.qq.com/s?__biz=MzIzMDQyMjcxOA%3D%3D&mid=2247519663&idx=1&sn=58d244b034970653df2b1a211cd174a1

原始快照：`raw/article/lurenjiaTM/最新60篇下载/大厂之外，EvoX让我看到了Agent的另一种可能-547c65d4-97ffa63be2.md`

---

2019年，人类第一次获得黑洞的图像。

完成这件事的，并不是一台大到不可思议的望远镜，而是分布在全球的八个射电观测站。

它们同时望向M87*，各自记录信号，再把数据放到一起，最终组成了一只「地球大小的眼睛」。

单独一座观测站看不清的东西，连接起来以后，人类看见了。

这件事真正反直觉的地方在于，想突破单体能力的上限，未必要把一个工具无限做大，让多个单元以正确的方式协同，同样能做到。

AI可能正走到类似的路口。

## 当一个Agent变成一支队伍

经常让AI干活的人应该都有体会，任务一长，它就容易乱。上下文越堆越多，前面的内容开始干扰后面的判断，做到一半，连最初的要求都可能顾不上了。

后来业界有了主Agent带一群Sub-Agent的做法，分工是有了，各路结果最后都得经主Agent汇总转述，一转手，信息就可能丢在半路。

所以Agent的下一步，是继续做一个更强的超级大脑，还是找到让一群智能体更好的协作的方式？

前一条路留给实验室去卷，后一条路已经有产品做出来了。

我最近体验的EvoX，给出了一种很有意思的做法。它有一个很重要的能力，叫蜂群模式。

蜂巢里没有哪只蜜蜂掌握全局，每只蜜蜂只干自己眼前那点活，采蜜的采蜜，筑巢的筑巢，整个蜂群却能把一件大事办成。EvoX的思路差不多。

![原文图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbDS8u1lJ0wBZ9FURlAIwjzUpZtKicbbgiapCl6Bu3PDnkLkzIlLhMsn6wePEsqMfG4X6ic0B37rGurEJS9lJFD9DLjsJZvZjJs6oI/640?wx_fmt=png&from=appmsg)

一个复杂任务丢进去，EvoX自动拆成一小块一小块，每块交给一个单独的Agent，几个Agent并行往前推。每个 Agent只接触自己需要的材料，不必背着一大段无关内容工作，长任务也更容易保持清醒。

最后各块结果原样返回，而不是要经某个agent转述一遍，前面说的丢信息的问题也就避开了。

最重要的是它还会把做过的任务和其中的经验留在本机。下次再碰到相似的工作，它可以接着已经跑通的部分继续做，之前踩过的坑也不用重新踩一遍。

机制说了这么多，到底好不好用，直接看我测的几个真实任务。

## 让EvoX造了一个小宇宙

为了看看一群Agent能把复杂任务做到什么程度，我给EvoX出了一道题。

造一个宇宙引力沙盒。

可以往宇宙中放入不同质量的星体，用拖拽决定它们的初始速度。星体会在引力作用下改变轨道，彼此靠近时可能发生碰撞。

还能调整时间流速，切换双星、三体和简化太阳系等预设，观察一个小型天体系统怎样从稳定走向混乱。

是不是听起来就很复杂感觉晕头转向了。

但EvoX经过两轮制作和升级，竟然真的做出来了，最后得到的效果大致是这样：

![原文图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/tp5fgmUBUbC2C4s7SxdMwmZsibFGlBDqX6leicFW9YU1HFO2j8ZLnKTG8ibJiaRq3KCVpQic2MksyTqn4XOEL6A3lzxUnJF7vLyj4BXPhy8Oyibyk/640?wx_fmt=gif&from=appmsg)

这样让人眼前一亮的作品看上去很适合拿来展示AI。几颗星球在屏幕上转起来，再加一点光晕和轨迹，画面很快就有了。

真正麻烦的地方在画面背后。

每颗星体的运动都要经过实时计算，参数稍有偏差，原本稳定的轨道就可能迅速飞散。碰撞也要符合基本物理规则，星体一多，还得兼顾浏览器性能。

这同时，拖拽、暂停、缩放等操作必须和模拟状态准确对应，画面再漂亮，也不能靠伪造物理效果来完成。

总的来说，这就是个足以让agent手忙脚乱的任务。

如果是让一个Agent从头包办，它需要频繁切换角色，任何一处疏漏，都可能让作品变成一个耐看但底层逻辑完全经不起推敲的错误。

那我们就来看看EvoX的蜂群能不能真的通过调用多Agent来轻松实现这个任务：

EvoX接到任务后，先派出四个Agent并行工作：有人研究轨道和碰撞，有人设计交互，有人负责视觉，还有人专门检查性能与异常。

![原文图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbBKp0Aek4ib2HB3FPYWDScfLBoHRwDL8BRHd7FIFj1b0lPGxelicEvJnoAjhxaysSymHFjSjspxwnkS0gVtGWgCmxv0VGuxBOriaA/640?wx_fmt=png&from=appmsg)

主Agent则统一确定架构、整合各方建议并完成代码。这样既保留了专业分工，也避免了几份代码直接拼接带来的混乱。

![原文图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbD9HUAx8yaTGRd39SX9dS9pLjT3DNLweWZ4Vle4MyeJVHTzJPUBkbvbs8DuXyU5ssn5eJ1Nnq6nzjHjZf6AOhXWWWfMsko07d0/640?wx_fmt=png&from=appmsg)

过程中也遇到了一些问题，当测试Agent发现后，它会按照反馈逐项修改，再重新检查一遍：

![原文图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbBLjibCbGtMhIRj5LG9uGp4U5L3YPxAHpUqsh5KV5cicf32D07hicATJAVjT1l0QsCKX4nQElU2dEaiace9ynFiaiagNdbjov1L4PcNA/640?wx_fmt=png&from=appmsg)

每个Agent做完自己的部分，还会有人接着挑错。这样才能保证最后交出来的作品才能既好看，也真的跑得稳。

第一轮结束时，一个可以玩的demo已经出来了：

可以看到画面中几颗星体沿着轨迹运动。左侧可以查看和添加星体，右侧能调整选中星体的质量与速度，再亲眼看着整个系统发生变化。下方还可以暂停、重置和改变时间流速。

这版demo出来，虽然还不算成品，我已经感觉到很惊喜了。界面设计整体做得简单高级，也能完成基本的运行。最重要的是，可以体验自己亲手改变这个小宇宙的运行。

第二轮的主要任务就是把demo优化成一个真正让人想玩的数字宇宙。

EvoX没有重新起步，它先读回第一轮留下的本地记忆，沿用已经跑稳的规则和操作方式，再继续补画面与功能。这就是它的自进化能力，做过的事会留下经验，下一次可以接着往前走。

![原文图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbDE9VgTtu2QqPdVqC2banSa0Seb53UN1vuPLqqTYGey4qN2JL4J7O9hdZLpr7GUVbHGRgEG8UjcXzQYicgjzKjNxfIrCT5GqgpI/640?wx_fmt=png&from=appmsg)

整个升级只用了半小时左右，比第一轮快了不少。

第二版明显更像一个完整的宇宙观测台：轨道更加醒目，还有双星、三体和简化太阳系可以直接切换，缩放、单步运行、碰撞开关和中文操作提示也补齐了。

## 用EvoX搭起一座巴别塔

上一个任务其实相对于视觉展现的话，更重要的是对于逻辑的打磨。所以接下来我又换了个方向，想看看EvoX能不能接住一个更重视觉表现的任务。

这个任务就让它让它造一座巴别塔：搭起一座九层高塔，周围要有云层和飞鸟，塔上还要能看见坡道与施工痕迹。日夜、风暴和镜头也要跟着变化。

这一次，EvoX派出了六个Agent。有人负责塔身和周围环境，有人处理天空、光线与天气，动态效果也交给了专门的 Agent。剩下的Agent继续打磨操作，并检查整个页面能不能稳定运行。

![原文图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbDYBrIzZcd6Jlvwlhkb6DQYXESkBCB3UHiakGMDich5UL9PI2Z1rf7Oe0We8ibicKpkV2vbW7AAA4dAAUWJjJiaeSdTVaIwVg3Bam1s/640?wx_fmt=png&from=appmsg)

这种分工很适合视觉创作。云怎么移动，雨落向哪里，闪电何时出现，都可以同时往前做。最后再把这些效果放回同一个场景里，让它们随着时间和天气一起变化。

最终出来的巴别塔，真的让我感受到了一些古老的史诗氛围：

拖动时间，画面会从白天进入黑夜；风暴加重后，云层也会变黑，雨和闪电接连出现；点击塔身，发光的古老文字会从砖墙间飞出。

再按下Confound Their Tongues，镜头拉远，雷电落向塔顶，画面也进入一段完整的神怒场景。

我在里面来回切换环境，确实有一点看电影的感觉。区别只在于，镜头和天气都握在自己手里。

## 从视觉效果回到真实工作

前两个案例看起来多少有点炫技，到了第三个，我想试一件更接近日常工作的事。

我让EvoX做了一次具身智能行业调研。行业调研这种活，其实随便找一个Agent，都能很快写出一份结果；但想把这件事做好，就得把问题拆得更细。

市场、技术、公司、用户和政策各有一套资料，数据年份和统计口径还经常对不上。只要其中一块查得不够扎实，最后的判断就很容易跑偏。

EvoX把这些问题交给五个Agent同时去查。有人看市场，有人追技术和产品，也有人专门研究公司、用户与政策。

每条重要结论都要留下来源和时间，碰到数据打架，再交给总控Agent重新核对。这个过程看下来真的感觉够靠谱。

![原文图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbDkAI7l0lITMseNIbk2Wicd8IQibcgLv0EZwkoibkXjiaAibcksn6Fz5GOHibjnYnP3gJavx7Vkx4hteJ6PTUCvecsB0sBZ4EFInzC4I/640?wx_fmt=png&from=appmsg)

我很喜欢这个过程里的一点是，它没有停在帮我搜点资料，而是继续把资料整理成一份完整报告，再做成可以筛选和对比的行业看板：

![原文图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbAv4mJribibEZwXGy6gdBUKMhXWwllxukXgOSzl8NM0UuAiaiagHpTISRLib8NIVA9cNic0QYHNBVxZrv5O91lAsHExjJuVbvavic9PZk/640?wx_fmt=png&from=appmsg)

看板做完以后，这次任务还可以再往前走一步。

我给结果点了赞，EvoX随即询问：要不要把这次做得比较好的方法沉淀成一个Gene。确认以后，它会从整个过程中提取真正值得复用的部分。

以后再遇到深度行业调研+结构化数据+可视化Dashboard这类任务，这个Gene就可以被自动召回并复用。

这个功能放在日常工作里很实用。周报、行业追踪和同类项目调研往往会反复出现，有了这份Gene，下一次就可以直接沿用已经验证过的方法，省下重新设计流程和反复踩坑的时间。

## 写在最后

三个案例跑完，我对EvoX的理解反而简单了。

它就像一支住在电脑里的工作小队。接到一件复杂任务以后，有人拆题，有人查资料，有人动手做，还有人负责挑错。每个人只盯住自己眼前的那一小块，最后再把成果交到一起。

EvoX做过一次测试：同一个模型回答563道题，单独做时正确率只有26%左右，换成蜂群一起做，正确率接近71%。模型还是那个模型，做事的方法变了，结果也跟着变了。

![原文图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbDsIV6bZTbwHpLMr7DGMOhbyLVNficMiacgMEc56xhv2fV7okNW1WC4icWiaxlIs2q527YSIHfOW1sjQHjAqG8Y0q1MQwTYk8JzlVg/640?wx_fmt=png&from=appmsg)

每个Agent只处理边界清楚的一小部分，彼此不会被越来越长的内容干扰。结果也按固定位置收集，减少了反复转述带来的遗漏。

这样的分工，可以先让一件复杂的事顺利做完。等到下一次再遇到类似任务，这支团队也不用把走过的路重新走一遍。

宇宙沙盒在做第二轮升级时，EvoX直接接着第一轮留下的成果和经验往下做，只用了半小时左右。这是我对自进化最直观的一次感受。

本地记忆之外，EvoX还可以连接EvoMap，把这种积累延伸到网络中。接入以后，它能够寻找其他Agent已经验证过的经验，再结合眼前的任务使用。

换句话说，它以后能继承的不只有自己做过的事，也包括整个Agent网络沉淀下来的有效办法。

![原文图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbAWllB5LnCcNpn8HVcQhOMan9FU1qHl38AncmeuFEtHPIYfSExuxfbKVzjzBU6amzsGaV6EwFk5Ds9mImOXfKqRu2ia3jIlHfMA/640?wx_fmt=png&from=appmsg)

现在我越来越觉得，多Agent协作很可能会成为接下来的一种大趋势。

未来使用AI时，我们也许只需要说清楚想完成什么。具体过程交给系统分工、推进，我们把精力留给判断和选择，看看结果有没有真正解决问题。

到了那时，AI更像一种新的工作环境，而不只是偶尔打开的工具。

所以如果你还没有真正开始用Agent，EvoX可以成为一个比较容易上手的起点。用自然语言把想法说出来，就能看着它一步步拆开落地。

如果你已经习惯用Agent辅助工作，那就更值得体验一下EvoX。它可能会让你重新想一遍，自己和AI之间还有什么更好的配合方式。

放到国产通用Agent赛道里看，EvoX来自一个创业团队，却已经拿出了足以进入第一梯队讨论的产品。它最后能不能成为黑马，还要看接下来的迭代，但至少这次体验以后，我愿意继续关注它。

EvoX目前也在邀请用户参与共创。如果你在使用中发现了问题，或者有特别想加入的功能，都可以提交建议。被采纳的想法会进入共建墙，还有积分或免费额度奖励。

EvoX Beta目前免费开放，注册无需邀请码。想亲自试试的话，可以通过评论区进入官网。
