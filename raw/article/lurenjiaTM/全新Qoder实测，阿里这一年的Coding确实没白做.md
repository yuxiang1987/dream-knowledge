---
title: "全新Qoder实测，阿里这一年的Coding确实没白做"
source: "https://mp.weixin.qq.com/s/3rq8LPTqHOB3ZdfTIDu0oA"
author:
  - "[[路人甲TM]]"
published:
created: 2026-09-05
description:
tags:
  - "clippings"
---
路人甲TM 路人甲TM *2026年8月31日 19:50*

前段时间我测Qwen3.8-27B，在本地跑模型时给它配的Harness是Qoder CLI。

最近又来了一个新 Qoder 。名字都挨得很近，它们各自负责什么，我和大家一样真的被绕得有点晕。

最近我刚好有机会体验了一下这个新 Qoder ，也顺便把这条产品线自己捋了一遍。

简单讲，Qoder CLI 更偏终端开发 ， Qoder IDE 就是一套带 AI 的开发工具 。

至于新 Qoder ，阿里是把它过去一年在专业开发场景里磨出来的 coding 能力收拢到了一个桌面端里，而且开始把它交给更广泛的大众。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbCNcKbCepfUibefJLkJTAeqaFEhwJ3cFZYvUWcbEaQGRdmZCZom6Y5PS5sVNwQwsA734mLaO11wJu1P08HtUSjLzXIx3B8WcEVk/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

我一开始对它的预期其实不高。现在的产品太多了，很多体验下来，仍然只是换了个界面陪你聊天。

但新 Qoder 用下来，比我预想的有意思。你给它一个还不太完整的想法，它会自己把需求理解到位、做全程计划、动手实现，再检查做出来的东西能不能用。

以前只有开发者熟悉的那套实现能力，现在只要你知道自己想做什么， Qoder 就能助你成真。

接下来直接给大家看我体验 Qoder 跑通的几个案例，看看它到底能做到哪一步。

**把卧室拍给 Qoder ，它做了个能拖家具的改造工具**

最近不是快开学了嘛，我有个表弟准备出国留学了，刚租下来一个不大不小的房子。这也是他头一回背井离乡，一个人在外边租房住。

他给我拍了一张照片，我看了看布置还比较简陋，也没怎么规划。

我就想着不如就借 Qoder 来给他做个简单的可以灵活交互的装修规划器，只给它这张照片，看看他能不能做出我想要的样子：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbA6kHvgtGlT6PXohNiaULHAB7jUhULQ8xW8HDticyibdDmJSz5pMODQe6xvibB64WlMobicx7TfviaYseYNTaG7wLBnoj1GwUQXzgI3w/640?wx_fmt=png&from=appmsg#imgIndex=1)

我给的提示词也挺简单的，没有长篇大论，就想看看他的需求理解、图像分析的能力究竟怎么样：

```js
分析这张小卧室照片，为它制作一个可交互的房间改造规划器。保留现有单人床，目标是增加舒适的居家办公区和收纳空间，预算不超过5000元。请先识别房间结构和当前问题，再生成可拖拽、旋转家具的俯视布局网页，包含预算统计、改造前后切换和通道碰撞提醒。完成后用浏览器实际操作并验证。
```

Qoder 这个功能我挺喜欢的，叫做计划模式。它会在看完照片、理解完需求、整理出思路之后，直接把一整个计划给罗列出来，再通过计划安排后面的工作。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbDYYV9ApIoT6l3dhWeB6MWEaPCA7uU9scicAX9MXDsHpwCKspP7omHnstKEhjMdyGYfELliaGI4pEgOtC963jufOmkggDXmuCTZs/640?wx_fmt=png&from=appmsg#imgIndex=2)

计划一直挂在侧边栏，做到哪儿一眼就能看明白。代码写完后，它还会在内置浏览器里自己试一遍，有问题就回去改，省得我在终端和浏览器之间来回折腾。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/tp5fgmUBUbBuoH936TG5URLeJ0sIGibRytiaUtXxgQnCa0BeykMu0vVic3YswLbShicCibMB3NeE6WvAf081p1ecrm5Tia6iaVdZxlQWcTsibRFj5UM/640?wx_fmt=jpeg#imgIndex=3)

不到半个小时，这个东西就跑出来了，得到的结果我还挺惊喜的：是一个基于图片现有的布局做的可操作的网页，所有家具都能随手拖动、安排位置，费用会随着家具的增加而改变。

特别是关于家具的安放规则，我觉得它做得特别细：不能重叠的家具，它会给出红色警示；家具间距过窄的话，也会有相应的提醒。

，时长00:29

<video src="https://mpvideo.qpic.cn/0b2eciajiaaaoaajs3mv2jvfaewdsqjabfaa.f10002.mp4?dis_k=355a9f32d660820def5b2009e7011b05&amp;dis_t=1788571305&amp;play_scene=10120&amp;auth_info=Bsjm27JAQz9KwIzv7EQjG0JDZGVOMWkzSHJkRjNVVSU8X1FMfW1Ycj0ESDIEKS47Vkk=&amp;auth_key=108f0adff657e89665cb06981080908d&amp;vid=wxv_4673476652377767939&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

**随手画了张草图， Qoder 把它做成了 App**

上个案例里 Qoder 拿到的是一张真实的房间照片，具体的物品摆放、互动关系都还蛮清晰，它能完成得很好。这次我想把难度放在「理解草图」上，让 Qoder 将一个手绘草图做成 App UI:

这是个情绪打卡的 app ，草图的结构诸如首页、打卡、分享各个页面都很清楚了，但具体的页面跳转、互动模式这些细节都没有画出来。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbDH26v4vz8hlNjO8rnAhKbPNxbxa4ftkwicfE5CjTt4icDzF6xc115yQy1fJQeqI5T8eFURG1yUknO5N0FibZ5OELh9RMCKqjX2E4/640?wx_fmt=png&from=appmsg#imgIndex=4)

然后我给它简单的指令，让它把这样只有大概想法的草图做成一个完整的 APP：

```js
根据这张手绘草图，实现一个可以真实运行的中文移动端Web App。先识别页面结构和交互关系，生成实施计划。整体采用治愈系植物视觉风格，完成情绪打卡、植物成长、历史日历、数据洞察和分享卡片。完成后在浏览器中逐页操作测试，发现问题后修改并重新验证。
```

第一版出来时其实已经有模有样的了，页面之间能正常跳转，打卡后植物也有成长反馈。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tp5fgmUBUbDV9vUiavtfER70T6oOAgmQ0B9TKdWaWFiaDIl7J2YfStX7zsx3H8iasfcmdnTCLiaWDhbKIujlBIiaSFkxFUIS7AMAnLy5uRyGuic2Q/640?wx_fmt=png&from=appmsg#imgIndex=5)

真正上手试了一遍，还是发现了一些小问题。比如点击浇水以后，植物的根部发生了变化，叶片却没有跟着生长，页面里还有几个文字显示得不太对。

这些问题不算复杂，我也懒得重新整理一份修改清单，干脆按下输入框里的语音按钮，直接告诉 Qoder ：

我刚试了一遍，点击浇水后，植物的根部发生了变化，但叶片没有同步生长。我还看到了一些文字错误，比如花园的花、植物的植。你帮我一起解决一下。

，时长01:29

<video src="https://mpvideo.qpic.cn/0b2e5eajeaaa4majyyev3vvfb2odsluqbeqa.f10002.mp4?dis_k=470fe647a03a060cd16c0538b329649f&amp;dis_t=1788571305&amp;play_scene=10120&amp;auth_info=APOR5f1FRD4dw43t6UciHEZBbGIYODo0SndjGmNSUCA6WgBEeW1fc2oHSTABKi88Uks=&amp;auth_key=9c4dfff491fde260adaf3bdf353fba9f&amp;vid=wxv_4673479467124850693&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

说完以后， Qoder 就开始继续修改。等它改代码的时候，我顺手和屏幕上的这个宠物鸭互动了几下，没想到它也能直接听懂语音。

除了在输入框里说需求，我还可以对着这只桌宠直接告诉 Qoder 接下来要改什么，直接对着它把意见讲出来，像打电话一样讨论方案：

做的这个 App 中，首屏的副标题文字太小，内容也有点多。太阳和花盆看起来不够吸引人，再帮我调整一下，有没有什么建议。

，时长00:29

<video src="https://mpvideo.qpic.cn/0bc3liarwaabjiabj7uupbvfcwwddnnacgya.f10002.mp4?dis_k=38d80ff8d43bedcef0d646a41edc878a&amp;dis_t=1788571305&amp;play_scene=10120&amp;auth_info=BLzMm60WQjwckdjp6hUuTxAXNmwbOT0zRSM9TzMAXyU+WgMRKz5ZcWtVHDQCeCNvBB0=&amp;auth_key=20360e778546097d5653b24ac63e488a&amp;vid=wxv_4673483864819040258&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

又改过一轮之后，首屏确实顺眼了不少。原本只有大概结构的一张草图，就这样被一点点补全，最后变成了一个可以真正操作的 App 。

，时长00:32

<video src="https://mpvideo.qpic.cn/0bc3ziawyaabq4aghnmuefvfdswdntfac3aa.f10002.mp4?dis_k=e3dc8d83d5b8444ca026a63995e1b6ee&amp;dis_t=1788571305&amp;play_scene=10120&amp;auth_info=Ber20oZARDscx9i86kcjR0AWZDYaZDllTiNmRzFeVCU/C1lAe2lfdmsDHGECKi5nVBw=&amp;auth_key=c81bd956989363d88b836fac1379e5cd&amp;vid=wxv_4673484885612085258&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

**上传一首歌， Qoder 把它变成一个动态世界**

不知道大家平时都爱不爱听音乐，反正我自己是一个音乐发烧友。我平时用得最多的听歌软件里面有一个根据播放音乐实时波动的动效功能，其实这种东西也可以自己搓出来。

那就让 Qoder 来做一个声音交互网站，让画面跟着音乐变化：声音一响，页面里的颜色和动效跟着律动发生反应。

```css
用户可以上传本地音频，系统分析音量、节奏、音高和低中高频，让每一首歌生成属于自己的动态画面，而不是普通频谱可视化。先做4种明显不同的视觉风格：雨夜：适合忧郁、安静的歌，声音控制雨量、雾、涟漪和闪电。海浪沙滩：适合舒缓、治愈的歌，低频推动海浪，高频生成泡沫和水光。赛博朋克城市：适合电子、摇滚、Hip-hop，节拍控制霓虹、光轨、城市脉冲。烟气梦境：适合古风、Ambient、迷幻音乐，声音控制烟雾、墨迹和流体变化。要求不同歌曲最终呈现出的运动、节奏和画面状态明显不同；歌曲暂停后画面可以缓慢进入余韵状态，不要立刻静止。保留单文件HTML，本地读取音频，不上传服务器。
```

Qoder 还是照常先给出计划，再照着计划把网站做出来。先来看看出的第一版：

，时长00:19

<video src="https://mpvideo.qpic.cn/0bc3guaumaabwaaetq4uczvfcnodiy2qcrqa.f10002.mp4?dis_k=cea3c3c1e1b6d41b175ea744fdaf4c29&amp;dis_t=1788571305&amp;play_scene=10120&amp;auth_info=AdToyatBRWsbwIu860AuGBESM2BPM2VjGCY2HGYFViQ7C1cQe2xeJmwET2EDLSM4BRg=&amp;auth_key=b6e804e2837e704155fa72dfb9ee88fc&amp;vid=wxv_4673485821025665030&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

初版看起来挺炫，画面也一直在动，可我听了一会儿，总觉得哪里不对：音乐里的鼓点已经落下去了，画面还在按自己的节奏变化，有几处甚至完全没踩上点。

于是我就想在这版基础上改改，但音乐这块我也不是专业的，几轮折腾下来，不仅画面毫无改进还霸占了许多上下文内容。

差点就要继续和它大战三百回合，我却突然发现它有一个侧边任务功能：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tp5fgmUBUbBP2txeEiaGVt774vMmicX6SuHjt0xbNnFelBDBSEGRpNJdQrgh21opMVLu1ZHniciam7eESHFclZB355q1FNRDCedvsiaR09FFJIx8/640?wx_fmt=jpeg#imgIndex=6)

了解过后我发现，原来这个侧边任务和主任务共用同一个工作环境，可以直接看到现在跑的项目里的代码，又能和主任务并行运行。

它关掉以后就不会保留，拿来当个专业的监工正合适，像是临时找了个懂音频的人过来挑毛病。

我让侧边任务先别改代码，只检查画面为什么跟不上节拍：

![图片](https://mmbiz.qpic.cn/mmbiz_gif/tp5fgmUBUbC8dC2hLW6sMic1ZynwJNnmhLagL0icnzd1TRHveibYdS6thdgIicib2WPr9bz5JERV5fvnVJBTibAx7PAqk4cYeKK7exqRNfq1GezPw/640?wx_fmt=gif&from=appmsg#imgIndex=7)

它读完初版的交付后，把可能的问题和修改建议整理出来，再让它根据检查结果继续调整。

改完以后，画面的变化和音乐贴得更紧了，鼓点落下时也有了更明确的视觉反应：

，时长00:07

<video src="https://mpvideo.qpic.cn/0b2e5mai2aaabmaifquvcrvfb26drxvqbdia.f10002.mp4?dis_k=2a9d8b33f98eec236c9e2fe3d90cc8b3&amp;dis_t=1788571305&amp;play_scene=10120&amp;auth_info=Cd+Hg55HFGxPzIvvuhEpGkxDNjcUY28yHH5hRzdVVCczUQQRLG8PITgITzJSfCQ6WEk=&amp;auth_key=fa83e5584224ef53617292492af5b957&amp;vid=wxv_4673487349698363393&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

这整个过程让我觉得侧边任务真挺实用的。

主任务继续做东西，中途碰到一个具体问题，就单独开个任务帮它检查。查完再改，不用担心原来的工作被打断，又能省下来时间和 token 。

**结尾**

这几个任务跑完之后，我对 Qoder 这个产品的定位大概有了答案。

它适合手里有想法，能看出成品好不好，但自己不太会写代码的人；也适合专业开发者，因为它保留了足够的 coding 过程证据，可以进一步查验优化。

所以我现在再看 Qoder, beyond coding ，这句话就顺了。 Coding 依然负责真正的实现，但能调用它的人却变多了。以前属于少数人的专业能力，现在普通大众也可以从一个真实任务开始，把自己的 idea 做成能运行的东西。

如果你还没试过用 coding 自己做出个东西，那 Qoder 正适合你去体验一下；如果你已经玩过不少 coding 项目了，也可以试试它到底什么水平。

正好 Qoder 上线后可以每天领 500 积分，在社媒上分享还有额外激励，额度完全够跑。

领完积分以后免费玩一玩， Qoder 适不适合你，跑一遍就知道了。

我是路人甲，前数据分析、产品人，现创业者。关注AIGC人工智能，分享实用的AI应用。让AI变成你触手可及的生产力。