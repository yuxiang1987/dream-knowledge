# 实测腾讯Hy4 preview，这一次，模型变强终于不只是参数上的变化

作者：路人甲TM

发布时间：2026-08-29 22:48

原文：https://mp.weixin.qq.com/s?__biz=MzIzMDQyMjcxOA%3D%3D&mid=2247520764&idx=1&sn=a63cc92ab4c66a9c6523abfab1820266

原始快照：`raw/article/lurenjiaTM/最新60篇下载/实测腾讯Hy4 preview，这一次，模型变强终于不只是参数上的变化-b8f47b2a-415ac6dc3c.md`

---

在WorkBuddy月访问量突破2000万，成为国内访问量最多的智能体后，腾讯又推出自研的更强模型，Hy4 preview。

总参数770B，激活参数49B，上下文长度达到1M。在腾讯公布的内部盲测中，Hy4 preview的平均得分略高于GLM 5.3和Kimi K3，已经进入开源模型第一梯队。

![原文图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbCpgYpGpc9Wsh4ubdSGKdCneiaX86jXW0YbWGIgEYfL8jS67O1OiayGyyHtibXP8UIcAx6ibGrCNgTJMlLAxGicia6XMqyajia4Og2axA/640?wx_fmt=png&from=appmsg)

大家不用记住这些参数，简单来说，就是Hy4 preview能记住更长的资料，更有能力完成需要反复思考、调用工具和持续执行的复杂任务。

新模型更强了这类话，我们已经听得有点麻了。但这次实际用下来，我确实感受到了肉眼可见的变化。

按照国际惯例，Hy4 preview在WorkBuddy里又免费了，限时两周，Hy3的免费期也延长到了9月底。

![原文图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbBO0JicqWBUhDEKL91Wlfrs7jtu8Eyck8xiagxHAOibmGc1ZCeIE6DIhYBSGv2vcmmNzY0btto54knpy1ZyHrvBhga0WmXfExRtJ0/640?wx_fmt=png&from=appmsg)

我抓紧时间跑了几项真实任务。一部分是代码生成，包括3D游戏和网页。另一部分是大家更常用的搜索调研和PPT制作。

我不知道从Hy3到Hy4 preview，腾讯到底干了啥。我只知道这次升级确实不一样，能力提升不是一点半点。

能明显感受到Hy4 preview在审美，3D渲染能力，搜索准确性，处理又长又复杂的任务上都做得更好了，还有个我觉得很重要的点：

Hy4 preview感人的交付能力。

它不只是完成其中一个环节，还会继续调用工具，把结果推到可以使用和交付的状态。比如游戏可以直接部署，PPT也能在线修改，手动修改还不额外消耗积分。

具体效果下面都会讲，话不多说，直接看实测。

### 3D游戏

Hy3刚出的时候，我做过一次详细的测评，当时做了个3D无限跑酷游戏。

为了方便对比，我用Hy4 preview又做了一次，同样的提示词，同样在WorkBuddy中。

当时用Hy3做出一个流畅运行的3D游戏，已经觉得很惊喜了。

这次使用Hy4 preview，最直接的感受就是顺。只给了一段简单的提示词，从写代码到完成自测和交付，只用了一轮对话。

它会主动检查游戏能否正常启动和操作，碰撞，暂停和重开等机制是否生效。后面让它修改跑步姿势并补充音效，也都是一次完成。

![原文图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbAIcJcic2VRwJrYO3qibXibiauMBFb0YK8ia6QtI8y1wxOFRCaXRML93CictfZMPI8wL0fo7ticMLzib0LKYW61ABgs6PSHCYaolD3aUNk/640?wx_fmt=png&from=appmsg)

做这种简单跑酷的3D游戏，对Hy4 preview来说已经很简单了，我就又在这个基础上加了难度。

让它制作一个模拟第一视角骑士在雨夜送外卖的游戏。

相比沿着固定路线前进的跑酷游戏，这个任务需要同时处理驾驶操作，城市路线和动态车流，还要加入碰撞，音效和飞行等玩法。画面也要兼顾雨夜氛围和明快的粉色元素，整体复杂了不少。

和前面的跑酷游戏一样，Hy4 preview收到任务后，会先理解需求并检查环境，然后制定计划，写代码并进行测试。

收到任务→理解需求→检查环境→制定计划→编写实现→自动测试和修复→验收交付

我希望用第一视角来玩这款游戏，也想加入一些更好玩的功能。外卖骑士速度快在游戏里做成一个强功能，可以飞。

视觉上，我想和碰撞雨夜城市的冷色和速度感做一些反差，要求车辆和骑士服都是粉色的，道路两边要有樱花树。

先看效果：

Hy4 preview的指令理解还是很强的，任务要求全部都实现了，而且超出预期。

场景是城市夜景，做得非常漂亮，开头还做了好看的粉色樱花树。

游戏机制方面，整体的骑行机制都很完整。界面UI很有设计感，不会遮挡视线，左下角还有一个导航地图。

骑行过程中，背景音乐和音效也会随着游戏进程发生变化。

![原文图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbDjmvDTLU3TxCAapibeoDySrvBaPhlm0XBdTNOAlqcibLlpcAY38fzMZ6vzPsgkWV7t2lPzxR8PluenRQS46QmM7Jb9r2l6cp2nc/640?wx_fmt=png&from=appmsg)

另外，3D场景的实时渲染速度很快，几乎看不到白模，碰撞检测之类也做得挺好。

场景加载速度很快，进入游戏后没有材质缺失或白模的问题，车辆不会直接穿过障碍物，基础的碰撞和减速反馈也都到位。

很好玩，忍不住连玩了两把，体会到了一把雨夜骑士速达的刺激。

### 游戏之外，我又让它复刻了一座巴别塔

这里是想更极致地测一下前端能力，看它对参考页面视觉特征的理解，测试动画，动效和交互。

过程就不多说了，和上面概括的流程类似，从规划任务一直到测试：

Hy4 preview会把这个流程跑完，再把成品发送给你，是一个完成率比较高效的过程。

虽然是一个纯HTML页面，但是效果一点都不随便。

这个点击进去的时候，我是非常震撼的。开屏页就很有氛围感。

塔的结构很精致，塔上还有一些在搬运工具的人，在不点击的状态下，画面是缓慢转动的。

点击塔身有种钟声，并弹出对应塔层的介绍。

可以调节时间，画面会呈现不同的光线并适配不同的光影，塔自身的灯光亮度也很细节地做了对照，还可以调整风暴的强度，切换视角。

交互过程中配有音效，加上画面动画和文字特效，沉浸感非常足，很有电影感。

![原文图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbBRMp21F3h7qjYOh1VpAKDywIrT3f1mhAO9cjVa1L07MoIhonyf4YccmvOKveX2X4cy7s8ebib0oYgm2bJC8vagRvHnAkSUZQN4/640?wx_fmt=png&from=appmsg)

不过，一个网页也不能只做得好看，完成度还要看能不能好用。它真的要被普通人拿来使用，事情会复杂得多，也更重要。

所以在这之后，我又做了一个可以改房间装修的3D网页。

### 在线装修:房屋改造实验室

这是一个普通人能够自己尝试装修方案的工具。它既要有可以观看的3D房间，也要让预算和页面交互真正起作用。

房间的3D布局是完整的，我要求的三种装修风格也都做了出来。

可以选择不同预算，查看对应的家具推荐和装修效果。还可以调整时间，观察房间在白天，黄昏和夜晚的光线变化。

页面里还有改造前后的对比功能。拖动中间的分割线，就能直观看到房间发生了哪些变化。

![原文图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbAjX7CricD0wHtxgg6sXJAmecgNge7ZUOyDsZEvbiasvPicKZY7hfP2icSVTvTeEAZamu77oo7tDzdLJaC1WbXX162Vys1u4MELNIo/640?wx_fmt=png&from=appmsg)

完成选择后，可以把家具清单复制到剪贴板，也可以导出当前房间的图片。网页还补充了房间改造规则和空间收纳建议。

这里有不少功能是Hy4 preview根据我的需求继续延展出来的，把3D房间的预算，装修效果和最终清单都联系了起来，账单一目了然。

Hy4 preview对包含多种功能的复杂任务拆解能力很强，执行力也很强，比如开始的时候我没有说要上线，它直接帮我部署上线了：

![原文图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbDmKmEPVCtpbarT7XnyRcxf9skyHOVv11AEAD1arn4bzt3kSK4icarRp82WOfwjAp5ZJfxGKGrJPjnWF3gNVGEgMQxJdSAosR1o/640?wx_fmt=png&from=appmsg)

主动完成上线值得肯定，但确实遇到了一些问题。

比如前面的游戏和网页大多在20分钟左右完成，这个任务运行了40分钟依然没有给出最终结果。我检查思考过程后才发现，是它一直在重复自检和测试。

![原文图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbDt4bwREO2wGv1dKAnHwEwGGQmKMdk3sr9ZP1BpZkpOm2P7hVBgzKXs8v8DIj10Fz0ld4SichnvHE58CKibCPB69fQxfgkZviahNc/640?wx_fmt=png&from=appmsg)

腾讯混元官方也提到，Hy4 preview目前存在复杂任务思考时间过长，以及过度自我验证的倾向。

这个问题在简单任务中不太明显，任务变长以后就会直接影响等待时间。好在部署之后也是可以改的，最终还是完成了整个项目，现在的体验我还挺满意的。

### 办公任务

最后，我把一个真正费时间的办公任务交给了Hy4 preview。

在日常工作中，搜索和调研几乎很难避开。自己去不同渠道寻找资料已经很费时间，把收集到的信息整理成汇报和PPT，又是一件繁琐的事。

所以这次，我把搜索调研和PPT制作一起交给Hy4 preview。

让它作为公司战略顾问，调研是否要实行4天工作制，并把调研结果做成PPT汇报。

现在很多模型都能联网搜索，但搜索不等于调研。AI在搜索中很容易出现幻觉，有时给出的结论看起来很完整，实际却没有可靠依据。

这就需要模型判断资料是否可信，能不能把不同来源的信息整理清楚，并根据证据得出合理结论。

我在检查混元的搜索结果时，重点看了信息来源，以及每个重要结论有没有依据。

它会优先使用官方，权威或一手资料，也会关注资料的发布时间和适用范围。在涉及规定的部分，它还会进一步参考相应的法律条文。

搜索范围也比较广，除了中文资料，还补充了一部分海外来源。重要结论基本都有数据支撑，给出的建议也会说明适用条件和限制。

![原文图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbA0XnM82yZZWVEor3N0IaG3FdGYiaNQ33UmGzC1I5K8LibgrHZXVSCGopW5SObfXleYb0203LrlBRyNbQVt3ujSVVp97j5xTPxKk/640?wx_fmt=png&from=appmsg)

进入PPT制作阶段以后，开头提到的交付能力就表现得更明显了。

刚开始制作时，它先给了我五种视觉风格，让我选择更接近自己偏好的方向。

![原文图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbDqdH5R5FicUo8KnAcH322vDlGswX9Sx7JDTBB4kVaPfS7BvHjJHcs9mHSflyicfPLicViaFr2rvp6SxPKCf0X3yzs7iam6OPMP7hVE/640?wx_fmt=png&from=appmsg)

从整个过程来看，它会先用HTML搭建内容和版式，再调用工具生成可以编辑的PPT。最后交付是能够下载和修改的文件。

![原文图片](https://mmbiz.qpic.cn/mmbiz_png/tp5fgmUBUbCMR9icL6P2YTQNWa4wG9FBqHy705gVgzyUEKYySE9fQ4yaGf8PJYqpKDiaibkkibzhaukKGibEDFeXkLIBrZuqPVZlKMhurA5ALGow/640?wx_fmt=png&from=appmsg)

在WorkBuddy里，用户还可以直接在右侧面板手动修改PPT内容。手动修改不消耗积分，修改完成后，也能继续让模型在现有版本上调整。

甚至还会考虑到深色的打印问题，谁懂这也太细节了。

![原文图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbDPGEqLMQHRibfZPhrwpUWkhosiawfXK1qrKvsKRwibic8kXxXsxm17zkSYfBSPxTpQqgX3G4IkdhlebvzZt8SbaJtsmx64g8NpicNc/640?wx_fmt=png&from=appmsg)

单独完成一次搜索，或者做出几页好看的PPT，现在都不算特别稀奇。

Hy4 preview更让我意外的地方，是它会以最终交付为目标，把搜索，资料整理和PPT制作连接起来。中间遇到的问题也会主动检查，最后给出一份可以继续修改的文件，整个过程确实省心很多。

### 写在最后

Hy4 preview给了我很多惊喜，但它目前也并不完美。

游戏初版里的路线，碰撞和难度都需要反复调整。3D网页在复杂功能较多时，也会花很长时间自检。办公任务中的重要数据和结论，仍然值得人工抽查。

大家在实际使用时，可能还会遇到其他问题。毕竟这只是Hy4的预览版本，还有继续提升的空间。

腾讯愿意先把预览版放出来，让真实用户去发现问题，本身也是模型继续改进的一部分。

混元团队负责人姚顺宇此前谈到AI发展时，用过一个很形象的比喻。

「做AI方法论已经变得非常成熟，寻找问题变得更加困难。

过去比如说我们做下围棋，会发明像AlphaGo这样的方法，但它可能只适合用来下围棋或棋类，不能做其他事情。

有了预训练和后训练之后，我们像有了一个万能的锤子，可以去砸任何钉子。」

对我来说，Hy4 preview更像是那把还在变得更成熟的锤子。

游戏，网页和办公任务等这些真实生产场景，才是用来检验它的钉子。

Hy4 preview在国内旗舰模型中定价最低，看价格也适合长期用，现在Hy4 preview还在WorkBuddy里限时免费，手头的事情，这两周刚好可以拿来锤锤。

![原文图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbDiarh1TQUIp8mZv8kMc1mJAa6Ggc1pueptj9nuJyes1ucfIGtOY8DsookBClJnxeKricI7BtrWmOic23j9IvzdjX0Xh6bzJpWMicM/640?wx_fmt=png&from=appmsg)

期待Hy4正式版起飞～

我是路人甲，前数据分析、产品人，现创业者。关注AIGC人工智能，分享实用的AI应用。让AI变成你触手可及的生产力。
