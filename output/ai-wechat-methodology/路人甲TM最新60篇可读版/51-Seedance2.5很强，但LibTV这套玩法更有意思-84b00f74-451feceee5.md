# Seedance2.5很强，但LibTV这套玩法更有意思

作者：路人甲TM

发布时间：2026-08-08 17:53

原文：https://mp.weixin.qq.com/s?__biz=MzIzMDQyMjcxOA%3D%3D&mid=2247519369&idx=1&sn=43bcb0a9018f85401e5ba72b0e324337

原始快照：`raw/article/lurenjiaTM/最新60篇下载/Seedance2.5很强，但LibTV这套玩法更有意思-84b00f74-451feceee5.md`

---

前几天Seedance 2.5上线后，我本来没有抱太多的期待，甚至都没主动去测试，毕竟不是一个跳跃式的版本更新。

那几天我还都沉溺在测试H3当中，测了一个又一个案例。

但是就在我沉溺于H3之中的时候，接连好几个读者反馈，Seedance 2.5虽然贵但真的很厉害，你能不能去好好用用。

我这个人听劝。

恰好近期LibTV也刚上线了Seedance 2.5，而且价格不贵0.4/秒，可以敞开来用，很舒坦。

于是我今天整整在LibTV上面测了一整天，花了我一点点Money。

先说个总结：Seedance 2.5很厉害，比如真人的皮肤质感更好了、快动作武打戏更稳更强了。

但是如果能搭配LibTV刚上的几个新功能一起使用，能让你在做生成视频和短剧的时候，高兴的嗷嗷叫。

不仅能把模型的能力拉满，而且相比之前更省劲儿地做出更好的作品。

整个测试过程中，有几个让我爱不释手的新玩法：

1、看到你喜欢的视频，即使你无法专业描述，可以直接让它拉片拆解，一键复刻

2、大量零散的素材，喂给LibTV，它可以直接给你自动理解梳理并且剪辑

3、长视频可以直接生成5分钟的，哪几秒出问题，可以单独精准修改

接下来我会围绕上面几个点把实测成片、具体操作过程都放出来，当然也有翻车现场。

对了，开始前先消除可能的疑虑：有人说这么便宜能是真模型吗？

LibTV是火山官方的合作伙伴，所有生成视频都可以查到TaskID，所以不会有生成视频调用模型真实性的问题。

## 玩法一：5分钟视频，按秒修改

Seedance 2.5单次最长生成 30 秒的视频，LibTV又在这个基础上把时间延长到了 5 分钟。

而且对于生成的视频，如果有几秒要修改，LibTV可以直接精准修改，不需要让SD2.5直接再重新生成一次。

先来一个电影级蒸汽朋克风小短片：

我又做了一条皮克斯风格的动画，整体效果还不错，整体画面和运镜都可以。

但AI视频常见的问题，还是来了。

这条视频，前面的部分都可以，但是最后几秒的时候，小怪兽的手里突然多了个饼干。

正常情况下，我们要重新生成这整条视频重新生成，前面的时间和积分都会一起被消耗。

但现在在LibTV中，你可以直接框选那部分，直接精准修改。

我只选了有问题的几秒，重新描述这一段要怎么改。

![原文图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbCrYwgicAKuzaWqUOh5ibERiaYshM3Y4LvbNlO3Inb3s9e9ePzMmZgC6UoDq3yKVzBKAYsVlZRVicvf7MxYR9hgazt0AZicKbDkCChs/640?wx_fmt=png&from=appmsg)

上面是修改了结尾的：

修改以后，新的片段和前后的内容连接得很比较自然，完全没有卡顿，也没有硬接上的感觉。

另一个案例是一条文字创意视频。它用不同国家的语言和不同艺术呈现方式，去展现「生命力」三个字。

只有结果视频开头的文字顺序弄错了，后面的部分都没问题。

我只选中开头的时间段，限制修改文字，其他画面保持不变。改完以后，文字顺序正确了，新的片段也能和原视频融合在一起。

其实LibTV加上Seedance2.5整体还是稳的，30s的视频大部分都一遍直出，偶尔出现的问题画面片段重拍都能直接搞定。比如某几秒的画面、动作、文字和道具等等这些一般都很好修改。

但有些情况反复改也很难改过来的，比如精确计时。

我们做过一段画面变化很多的打斗的长视频，画面、配音、音效和不同角度的运镜都没有崩，但在最没想到的倒计时上出问题了，画面中的倒计时读秒是乱的。

尝试用片段重拍修改倒计时，因为倒计时出现的频次还比较高，几乎贯穿了生成的整个片段，而且修改后时间仍然不准确，一些原来比较出彩的片段也被一起改掉了。

这里面其实涉及到长视频生成的机制，Agent会一次生成很多个小片段，片段之间可以保持比较自然的衔接和统一风格，可这些片段没有形成一条连续的计时程序。

时间显示需要每个片段和下一个片段精确对应，模型很难完成这种计算，反复调整的成本反而更高。

所以这里也给大家避一个坑。

视频里如果需要出现计时、倒计时，最好把它作为后期特效，或者放进手持设备、地面投影这样的前景道具里。

## 玩法二：逐帧拉片，一键复刻同款视频

每次看到爆火视频，脑子里总会冒出我上我也行的想法。

但在实际操作中，却发现想法经常只是脑子里的一团感觉，想复刻但不知道如何下手。

尤其是我这种非专业导演出身的，其实不是特别理解某些视频火到底火在哪里。

而LibTV有个功能叫做：逐帧拉片。

这个功能，让普通人就算搞不明白别的视频好在哪里，你也能直接复刻它的方法论，可以自动拆解其中的画面风格、关键帧、运镜方式、叙事节奏、时间戳与背景音乐，然后将结果整理为可直接使用的参考素材组。

我很喜欢布达佩斯大饭店的风格，于是上传其中一个片段，选择智能拉片，一组结构化、全面、专业的逐帧拉片就呈现在面前，原本只可意会的东西，现在更加清晰了。

并且还不消耗额外的积分，大腿都要拍烂了。

![原文图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbCINgyiaUJwV7UTslGcOhTDUUq1eQ97Gdo0S4lsOkjiat4h7hoICF5qmbc0V5ktBS5B9AcQ4HvozxpWdLbrYwhY9O9t4QkNm3bSY/640?wx_fmt=png&from=appmsg)

拉片参考视频：布达佩斯大饭店

并且LibTV还能把结果整理成可直接用的参考分镜组。

然后，我用LibTV自带的Agent仿照其中一个分镜组的场景，学习它的运镜手法和表现风格，生成了一个类似的分镜视频。

只需要简单的提示词：

![原文图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbCOmsmXibGkrxcms1WzfC6GS5T7zXER4lb66MITiaL90ca2I65p5evsFANkra2JkKibN44hA6RbzMRX9icb6KnjOibgR0cOt33IXZEU/640?wx_fmt=png&from=appmsg)

![原文图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbBicnORz47kLNAMVM3QDaEkalO8pmia8EYod1icU4mRlBEdibvgXCFTZicHsQPKtlWKbAibYmX6TvMdlMCGH4Z5ibVqXsuIzia4nzvqZps/640?wx_fmt=png&from=appmsg)

成品：

成片出来，效果很是满意。

工具拆得好，人人都可以是大师。脑子里层出不穷的想法终于有了用武之地。

## 玩法三：碎片素材一站式成片

这个功能可以说解决了我的头等大难题了。

Seedance 2.5生成了丰富的素材，LibTV就能实现素材的自动剪辑。

之前往往都是视频模型生成了一堆视频，一堆素材，但是让人头疼的是素材太多了，我到底应该怎么剪辑啊。怎么配乐，怎么卡点，怎么切换面。

这事情，老实说对我来说可太难了，比做提示词难多了。

但是现在你只需要把素材扔进LibTV，再告诉它你想做什么，它就能帮你把零散镜头整理成一条能看的成片。它会根据内容去安排节奏、画面和表达重点。不是那种简单的拼凑。

用到智能剪辑下面有三个子功能：讲解视频、素材混剪、批量广告

![原文图片](https://mmbiz.qpic.cn/mmbiz_jpg/tp5fgmUBUbCjCZz1AYUwaGM3JK2xdickQrltwBfJKReOmeRbR6N603m5zbfnFvXqIntZVkQKA4c7xuniaxrtjic0GxX7IfybPnibeFsmTn6eajM/640?wx_fmt=jpeg&from=appmsg)

怎么用以及效果如何，下面的案例都有说明。

先来说说第一个功能，批量广告。

我一直喜欢苹果风格的宣传片。

画面简约，产品特点很纯粹，动效很流畅高级。

但让我自己复刻一个，费钱不说还难搞。

批量广告这个功能，简直是我们这些人的福星。

只需要输入一个简单提示词和一个参考视频，再放入自己的产品图，就能批量生成相近风格的广告片。

![原文图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbCdpr5uqtszm8HI0VEuoeIxO7DddJN5EKQ5LtiadKdvx4mI2iaHyXZib1hJa0AxLuGjLibNUEXRnPcvNjAhJBo5vnAzYyan59kJ8pg/640?wx_fmt=png&from=appmsg)

一条苹果风的煎饼果子广告片新鲜出炉！

为什么是煎饼果子。

因为刚好测的时候到饭点了，疯狂想吃煎饼果子哈哈。

不得不说，虽然是两个完全不同的产品，融入的太自然了，前面的动效剪辑，还有音效，也复刻的不错。

结果煎饼果子被拍成了我吃不起的样子，口水直流啊。

想进一步看一下它的适配度，又换了一个稍微有点离谱，产于1889年的板砖板砖：

效果还是很稳，苹果风的简约克制、流畅的动效，和刚刚好的音效。

板砖被拍得像镶了金边。

这里给大家提个醒，批量广告系统默认会生成三条，数量可以自己选择。

我做煎饼果子广告时生成了三条，除了有一条有点科技风，其他两条都很好。

批量广告很适合开网店的人。只要给它一套参考风格，就能顺着这个方向给不同商品出片。

第二个功能，讲解视频。

之前听朋友说宋代就有外卖了，我还在那嘎嘎乐，不信。

结果后面一查，还真有这么一个说法，打脸了。

想到可能大家很多也不知道外卖的雏形、起源，正好用这个主题做讲解视频。

用这个功能前，要做好咱们的视频素材。

我先把提示词发给Libtv自带的Agent，它先智能拆分出5个分镜，生成了5条视频，全程我只需要点点鼠标，确定Agent生成的分镜和道具图等等。

![原文图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbACUic4ZCcPWiccovszBUqXXqK1n32cjiaRsrDKcGwaMLX80CMUx7N1ydzpbqbTPMajuUmyeXo4JH5iaUguw0LD8s2iakOKqA4u6SCM/640?wx_fmt=png&from=appmsg)

我先让把5个送外卖的素材合成了一份完整的短片看下效果。

视频效果很不错，烟火气，吆喝声都有了，市井小民的生活百态跃然眼前。

上面更多是用画面讲故事，我又用上面的几个视频素材、准备好的逐字稿和一点音频参考，准备做一条有解说的科普视频。

![原文图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbCbuJ1r9myWiapGuYLn6bIHwpxOnvQficyaibGGFuokb83ricJKGMjcNe2REIlYuvmPspCicpLGtdgNicg1w6mqRG765BqZB7uzJNE44/640?wx_fmt=png&from=appmsg)

我惊讶地发现根据描述，它还能推荐不同的风格表达。

![原文图片](https://mmbiz.qpic.cn/mmbiz_jpg/tp5fgmUBUbB39Xiaib3RMxDDzHQhlG3HOtBDuu9ey1d3fgn5Q6HYu11WXAnS7G8QxTCHIxib98SUANf82CK9C1MicVnRddx9zc1x3uh2f0RN7jI/640?wx_fmt=jpeg&from=appmsg)

我测试了几种风格，最后生成了两条不错的。

视频生成出来以后，我发现口播内容和画面能不能接上，取决于每一拍怎么安排。

这里有一张拍点表，会把整条视频分成不同的拍，每一拍对应不同节奏，也可以逐拍编辑。

![原文图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbCB9xsqmC2xsNvX5EicwqZ9b1zPIsZ45vVvSrvicTH0RBTRGvkFfWibvibV0QzAM1RPPyGh8xxmysxNlpt3zeRDxGySvcDXzRc1sFY/640?wx_fmt=png&from=appmsg)

最后尝试了一下「素材混剪」，把现成的送外卖的这5个小分段交给LibTV重新剪辑。结果出来，全当一乐。

## 写在最后

这次全程我都是用的LibTV+Seedance2.5进行测试的，实测下来Seedance2.5的能力确实是有比较明显的提升的。

但是现在有点感觉大部分人对于视频模型的更新迭代都不是很感冒了，只要不是那种非常跳跃式的大更新，都声音平平。

别说你们，就连我自己可能都没那么感冒了。

反倒是以前我们觉得可能没那么重要的平台，现在却扮演着越来越重要的角色了。

LibTV出的这些能力，我是越用越顺手，它能解决很多模型本身不会去解决，或者说解决不了的问题。

除了这些非常有用的能力之外，平台端随时随地都可以用到最好用的模型。

你看它前几天刚上的H3，这会儿又把SD2.5上了。

多舒坦。

在上一篇Agent的测试文章中，我们有提到同样的模型，在不同的Harness下会有巨大的效果差异。

未来模型能力趋于相同，这点只会越来越明显。

目前，Seedance 2.5已经可以在LibTV使用。有个活动，720p限时58折，低至0.4元/秒，最高赠送60条免费生成。如果想用Seedance 2.5的，LibTV是个好地方。

我是路人甲，前数据分析、产品人，现创业者。关注AIGC人工智能，分享实用的AI应用。让AI变成你触手可及的生产力。
