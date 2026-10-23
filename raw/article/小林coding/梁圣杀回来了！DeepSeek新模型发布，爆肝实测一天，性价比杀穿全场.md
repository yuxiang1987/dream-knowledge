---
title: "梁圣杀回来了！DeepSeek新模型发布，爆肝实测一天，性价比杀穿全场"
source: "https://mp.weixin.qq.com/s/j6kFJ4OzYh2VCzkXpe-yzA"
author:
  - "[[小林coding]]"
published:
created: 2026-10-23
description:
tags:
  - "clippings"
---
小林coding 小林coding *2026年10月18日 10:46*

大家好，我是小林。

前两天 DeepSeek 崩了近 5 个小时，随后直接把过去一周的消耗金额全都返还了，这补偿是真大方啊。

结果刚崩完没两天，DeepSeek 就在昨天官宣，V4.1 Flash 正式升级到 DeepSeek-V4.1-Flash-1017 版本。

别看名字只是多了个日期，对比上一版，模型性能全方位起飞。

最亮眼的是在 DeepSWE 编程测试里，V4.1-Flash-1017拿下了77%最高分，超过GPT-5.6 Sol、Claude Opus 5。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ysyAxM1rgX0NCQvUT5qwFAFgwWCF8LU1hMTN2y3j8QIhMnwr6GtGayPCMkU2ItZFrJBkxOgjjj1FxCOL0WbiamdtJt8vgAkkM6ibE9HQnpuWQ/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

不过并不代表全面碾压 Claude Opus 5，表格里有一半多的测试项，第一依然是 Claude Opus 5。

更直观的是下面这张图，横轴是每个任务花多少钱，纵轴是通过率。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ysyAxM1rgX1yqickw5fodV1Dx0b40vYfgibHyHF7PdvMYPIGoPzfib2yibcMYb8RmHB2HHs8qK4VJWUZebVQ5ibAsCrHibmuibEiaZEzypSJp5jzlV8/640?wx_fmt=jpeg&from=appmsg#imgIndex=1)

你看左上角那个蓝点，就是 V4.1-Flash-1017。通过率最高，每个任务却只要一块多钱。 而 GPT-6 Astra、Claude Opus 5 这些，通过率比它还低一点，每个任务要花大几十块。

也就是说，同样跑一个 Opus 5 任务的钱，V4.1-Flash-1017 能跑 60个左右，通过率还更高。

你就说，这性价比离不离谱？这是什么超级斩杀线。。

一句话总结，V4.1-Flash-1017能力往上涨，每个任务的花费往下降，API单价还没涨，熟悉的性价比杀手又回来了。

有意思的是，DeepSeek这次主打「许愿式编程」。也就是说，我们可以少写点提示词，也能做出不错的效果。

这是因为新版本用了基于自反馈的强化学习训练，从0做游戏、3D 建模这类完整项目的能力大幅提升，在 DeepSeek Harness 里只要很少的提示词和几轮交互，项目就能直接跑起来。

我也第一时间上手折腾了一轮，这次确实有惊喜，后面不少实测案例的提示词都是只有一句话。

## ────实测Deepseek-V4.1-Flash-1017────

这次实测，我用的是 DeepSeek Harness 桌面端。

想跟着试的朋友，先把客户端更新到 0.2.1-rc.2 或更高版本，再选中带「1017」标记的 DeepSeek V4.1 Flash。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX2sANicnoHocia7icSTd2AwMu6WaIZ6XlWu5WQCehTgbRDFlc7ehTnXhxRI2USeFuOBAhulhCVaDhic9LgGQ9DoMTTcUsEZsCb7rRY/640?wx_fmt=png&from=appmsg#imgIndex=2)

这次 DeepSeek 还专门针对自家的 Harness 做了模型优化，不愧是自己的亲儿子。

下面展示的案例，都是用 DeepSeek Harness +DeepSeek V4.1 Flash 1017(High) 模型实测出来的效果，一起看看到底如何？

### 01 | 奔跑的斑马

鹈鹕骑自行车这道题，你们是不是都看腻了？

刚好最近又有一个 SVG 测试火起来了，画一匹奔跑的斑马。

别看就一匹马，斑马身上全是黑白条纹，一跑起来条纹得跟着身体动，稍微画不好就特别出戏。

那必须拿来考考 DeepSeek-V4.1-Flash-1017，提示词就这么一句话。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX1gMqa8DUpL1aIlJSy2Z1TibqL1WtJNt6IfticSCcbDXcScsEM6uKM963zuwNLZbOfbc7xWW5scakaVa2FMxIVicFnICcyVNTAkl4/640?wx_fmt=png&from=appmsg#imgIndex=3)

来，你们看看这效果怎么样？

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX2kxNgzVxm9E6JvC27fuVKlibmuGy10eNibhVzhoXicD85wiagSd3S8JjRqaAmcgfmiageL03dK5XE1WLb13BOnRucbQiaqXnXMwHfQ0/640?wx_fmt=gif&from=appmsg#imgIndex=4)

跑步的姿态挺自然，身上的条纹也没乱，背景的夕阳和草原也给配上了。

你就说，这一句话换来的效果，是不是还不错捏？

不过，怎么能少了咱们的老朋友鹈鹕呢？这次不骑自行车了，直接让它骑斑马。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX3aOCU89oGzvIExBj8G6wHqSUbbbJsW5nCBCdwQmNJK6gFZDhUQdB2UQ4P34CqSdCJXeyjSoys8iauIrXBb5KHQHP8jFkQzSia1w/640?wx_fmt=png&from=appmsg#imgIndex=5)

鹈鹕的样子没崩。更让我意外的是，马鞍和缰绳都画出来了，鹈鹕脖子上还系了条小红围巾。这些我一个字都没提，全是 DeepSeek 自己脑补的，考虑真周全了，还真有种许愿式编程的感觉了。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX3qOic05XeerYunNKzOrUheLZvFiblkGqkFFx0QoA7hHEm8mvyXKwKnmeAnN6PrADsTOSumwfDf2a3Kp5rQibkKumy0FXQuYicOiczw/640?wx_fmt=gif&from=appmsg#imgIndex=6)

而且你们注意看鹈鹕的腿，靠里的那只是有透视感的，说明它是真的跨坐在马的另一边。这种细节都抠到了，你们觉得这匹斑马能打几分？

### 02 | 3D 地铁跑酷游戏

还记得 DeepSeek-V4.1-Flash 刚发布那会，我让它做过一个 3D 地铁跑酷吗？

当时做出来的游戏能正常玩，没啥 bug，就是画面黑乎乎的，看着有点素。

，时长00:30

<video src="https://mpvideo.qpic.cn/0bc3jyaegaaajqagdqgujfvfatwdinhaaqya.f10002.mp4?dis_k=6128187093cfa8656d20ba1a2c8df0fb&amp;dis_t=1792736309&amp;play_scene=10120&amp;auth_info=DqHn1csNOAdg9ffN+29fUnU6DGseRjAPcSBvShkvMx4weWBPIAdlaAJZfGIXTUhofw==&amp;auth_key=a55cab12a7413e800ebde2a533ffbb18&amp;vid=wxv_4742834461464215557&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

然后下面这个是 GPT-6 Astra 实现的版本。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX0sqMdovEAvJwydiaLmQnh92ICp0bt95JPCxpHQb8yPBDkibpusxrLKj6r1IXmwGdeh95KBtAxcwGW2sHdnygBwX7Fj9B1aoGTq4/640?wx_fmt=gif&from=appmsg#imgIndex=7)

这次我把同一句提示词原封不动丢给 DeepSeek-V4.1-Flash-1017，它闷头干了 40 分钟。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX36WIa7o08rbW5DzZJnDxLFxpL3YUbDv6zvYbXI4eZTicOFT71j4awNjwgJ5qb9j1ANEmlHAA9hzp55s2c7VwjWD42B2ot4XTAE/640?wx_fmt=png&from=appmsg#imgIndex=8)

来，你们先看看这次的效果。游戏的画面明亮了很多，而且游戏特效也会更多，跑顺了会弹出「FLOW ×2」的连击，路上还能捡护盾和磁铁。

，时长00:30

<video src="https://mpvideo.qpic.cn/0bc3heahyaaafaaf6vwuuzvfaoodpq4qa7aa.f10002.mp4?dis_k=eae34c32c5ef6a236f730c9a11003a23&amp;dis_t=1792736309&amp;play_scene=10120&amp;auth_info=DN/whJsGbFIxoaaeqzhUVy4+DjEYQDBYKCRpShsqMEwycWBMcg8xPVMNLTFHGkNtJA==&amp;auth_key=078d71d476c5e28a1f24438de06152aa&amp;vid=wxv_4742839003912175620&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

很明显，Deepseek-V4.1-Flash-1017 比之前的做出来的效果更好，场景的质感和光影的效果都远超之前，这么一对比，是不是觉得deepseek这次进步还是挺大的。

不过对比 GPT-6 Astra，V4.1-Flash-1017 实现的两边街景并不会随着角色跑起来有变化。

### 03 | 马里奥卡丁车

再来一个经典的3D马里奥赛车游戏，先来回顾 GPT-6 Astra 做出来的效果。

，时长00:53

<video src="https://mpvideo.qpic.cn/0bc35eaa4aaa3eanhke3rzvfb2odb3uqadqa.f10002.mp4?dis_k=d2e22d9d0e0ca7a5b4c05929190fbf7b&amp;dis_t=1792736309&amp;play_scene=10120&amp;auth_info=Voj/xssFOgM2pPef+DhVUSk0WGJIFTUPfndvHkl+M0loejhMeg9nbFQIfDAUGkJrIw==&amp;auth_key=628c2ae04eaac6ab86753873cbb5555e&amp;vid=wxv_4680966227521978368&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

同样的提示词，我丢给了DeepSeek

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX2V6TKwoeF9pGUoDKkgwnbOUwia8JwUOEzK3IgeTkrVgI0CONnKoGMGwX3Pncj87KGCRwXvKZWdWYl8TmpbmpB4wfxsrBicoUmpM/640?wx_fmt=png&from=appmsg#imgIndex=9)

DeepSeek-V4.1-Flash-1017 吭哧吭哧干了 1 个小时，一次性直出，打开还先给了个角色选择页，8 个角色任你挑。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX1NFb0YziavaRu0DRBAOhpnkVokQ7NdGJJRIUialiaNg8HLwrUB5ZS0ia0ibaZxicq3IfbTFXnbrkWTTXGgr3fricj3tznKRlt8iahGxKA/640?wx_fmt=png&from=appmsg#imgIndex=10)

游戏能完整跑完三圈，路上吃到的道具也都能用，落日赛道的光影也很出片。对比 GPT-6 Astra 实现的那版的，你们更喜欢哪个效果？

，时长01:20

<video src="https://mpvideo.qpic.cn/0bc3xuabkaaarqadowougbvfbpodcw6qafia.f10002.mp4?dis_k=08b53772d59d6c3de782c091d5471119&amp;dis_t=1792736309&amp;play_scene=10120&amp;auth_info=X4TIkpYBa1BhoqzL8j9SUHo6DjYYHDJYKiU+GUolMR9hcTAZdgs2PwMOJ2QeHUVqcA==&amp;auth_key=e6f6f104cfa787a12363e6db560f352f&amp;vid=wxv_4742835248919789569&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

最可恶的是，眼看离终点就剩一米，我还一直领先，结果后面的 NPC 甩过来一个减速乌龟，我就在终点线前被减速了，最后只拿了个第二。。

你们说气不气人？不过这节目效果，我选择原谅。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX2SW2WObUsq3PNu7nEmQuhxZychndCcPFuPbqAbmRTsIuoZZxtH20Glhch6WdsLug9ia66slkhJkwbAPIc7FGwMxmcfYXnpGSiao/640?wx_fmt=gif&from=appmsg#imgIndex=11)

那首发版的 DeepSeek-V4.1-Flash 当时做得怎么样呢？同一句提示词，你们自己看。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX2273EWdBtiaT5k1z8sKmFnibDkaAhwnqrkyOhCGtkrsxce0G2RyAtdicaYSDIrHVr6ia9NBIqUXW71yicb2pqV8Uxay062IiclZiaAUY/640?wx_fmt=gif&from=appmsg#imgIndex=12)

完全玩不了。跑道是歪的，我的车一动不动，NPC 倒是一发车就冲出去了。

一个多月前的 DeepSeek-V4.1-Flash 还玩不了，现在 DeepSeek-V4.1-Flash-1017 已经能出很完整的游戏，这进步，你们品，你们细品

### 04 | SpaceX 机械臂夹火箭

马斯克 SpaceX 用「筷子」夹火箭的视频，估计不少人都刷到过。我就让 DeepSeek-V4.1-Flash-1017 把这个过程模拟了一遍，你们先看看效果。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX05nEwvXzwUNFQz0rmzdiaL9ZGAiaC3yo2xTVz5LsjufEeSfv9VB7x2xUNlP2ZF0aoemfbd0knJicADpTmbnvdBEBbtvSWHWoddRg/640?wx_fmt=gif&from=appmsg#imgIndex=13)

完整过程我也录下来了。助推器缓缓落下，机械臂一合拢，稳稳夹住。火箭的金属质感也很到位，是不是挺像那么回事的？

，时长00:31

<video src="https://mpvideo.qpic.cn/0bc3qqafoaaanmahln6uunvfbbgdk6caavya.f10002.mp4?dis_k=83d23d7bc83b0dd8c10e3b1bbccca52c&amp;dis_t=1792736309&amp;play_scene=10120&amp;auth_info=DcbP6qNVPwBlofbD+TlVUCk6XjEVFjReLXJiH0wtZk8zeWMfIFxibwcNfWwVG0JqIw==&amp;auth_key=0c398851e5f0eeb57a1d7b6199ad8ade&amp;vid=wxv_4742838446371848200&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

提示词也是很简单，就一句话，我想做个xxx动画，跟许愿式编程没什么区别。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX2VyHWrogYBF6kI7ZnEXicJPwcic87XS9KBrAvxmoCiaf1s416LOEBjRyoorIZGgKN1ncia14zVo4nxRyvBdAIuVOV7Hor2XEkTUIs/640?wx_fmt=png&from=appmsg#imgIndex=14)

### 05 | 3D 清明上河图

再来个有难度的，3D 版的《清明上河图》。

我还让 Deepseek-V4.1-Flash-1017 复刻了清明上河图的3D版本，还是很惊艳的，河面上的船是会自己游动的。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX2Sp4l0u517tMtvbGPpRw3GOGTMoOreibt4fthCDCrMpliaJSVsxia4KTug62O3QbAfogiaRkaYMu4seXvU902hsXmIcvH6oibiaQotw/640?wx_fmt=gif&from=appmsg#imgIndex=15)

虹桥上挤满了人，河边的街市也都建出来了，细节和丰富度都做到位了。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX3M4KeeMZkyhprs648jNMTE8rIgwiaiaZU5FOlk7rOONOVeyXmDYGSNMzcnZY4XicUmXHAVYbSpenzPYibRFcTia2icnSasQ9ibJMVwWI/640?wx_fmt=gif&from=appmsg#imgIndex=16)

提示词也是比较简单的，干了有30分钟。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX03B9h0ZngmCFzNm2VEf8Vw0yDhXA3z8ibjhtXyRhIUOrGG3jy0ySWd9lQ1zSkr8MyONXr5b4GoG22NOyQETzPqR2nUuib3r5tvE/640?wx_fmt=png&from=appmsg#imgIndex=17)

### 06 | 千与千寻海上小火车

看过《千与千寻》的朋友，应该都忘不了电影里那段海上小火车。我找了一张参考图，让 DeepSeek-V4.1-Flash-1017 做一个千与千寻风格的海上小火车。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX1hQQSVZbMPpQZEOGysF6vjm8VNakbPMZ7GKNGaTfzp2XTrflqVh9F1Vn6RsQne0sFMKvRtXYM0nouHrE6uZMmm4xEibXgwd0w8/640?wx_fmt=png&from=appmsg#imgIndex=18)

这是出来的效果，水面上能看到火车的倒影，天上的海鸥也在飞，看着挺温馨的。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX0QhP8rGx9dzzDqMAl1IcUyJx4odMzibuSbmeub48egE2OiaLA3aaaYBNwJ8WytfAICibzNahB6lDZrtVVHp09QlMP5FjoomZkuY4/640?wx_fmt=gif&from=appmsg#imgIndex=19)

还能切换昼夜，到了晚上，火车头的车灯会亮起来。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX1mNnUUofX6dZLJWD8QichQJfk5Nic1m3lhA4iaUy6jkrBIehMOPoDIK2BafTHEq1D4PictRfv5kjRqnlKmXf85UoTCP8HWZzYwfA4/640?wx_fmt=gif&from=appmsg#imgIndex=20)

### 07 | iPhone Duo 折叠屏

今年苹果不是出了首款折叠屏 iPhone Duo 嘛，我就想看看，DeepSeek-V4.1-Flash-1017 能不能靠写代码把它的 3D 模型还原出来。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX1Pg7zjEhk7Fl0UE1uF1AAUEBe4pumibCCicdRoyc4AwY2TNWL6vSIic4sv1QBAibY8weeXcC0bpQvqA4urOkLorbadTWQ0ibic9JgSc/640?wx_fmt=png&from=appmsg#imgIndex=21)

折叠和展开都做出来了。你们觉得像不像 iPhone Duo？

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX1YVdUIxvR848DHgDHVLM29qJ2TaicP7Bgf5LwIsRfGUFicueUO60phLDxiaKobOf6qr6cD9wWJbzhwa65xnPIO63Luq5dTVFj7PA/640?wx_fmt=gif&from=appmsg#imgIndex=22)

一键还能拆开，里面的零件一个个都摆了出来。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX10nBrI3ibs0h1DgxVZXcXuCXiaXdGxfvQkicy2cib9W4SaAE7Pcst1wLIWXVpGpTVhWV9ctbKy6RDCAPV5oyXoDdM9ibExmLAiaLreo/640?wx_fmt=gif&from=appmsg#imgIndex=23)

### 08 | 雨夜便利店街角

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX0WmtVMBUdvm5IjGTF41qYXQlNvXtT6UpoQxqk4zicqDjFAZaQlCduAcXcYZ5XJT7698XsHdhUym0YMjHpHq5RdIdULOpVTRjOI/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10)

同样的提示词，我让 DeepSeek-V4.1-Flash-1017 也做了一版。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX1lT65Z551eRMYGv75Op7UhAvOGQSN73VVZfHHZoW8ga69YIYFaqPKiaer8icDtGmFVxqmuSSKnGJ5A0dQYccHzmyMa14Q0zGWUo/640?wx_fmt=gif&from=appmsg#imgIndex=25)

你们觉得哪个更好？

我觉得 DeepSeek 一点不输。它不只做了便利店，还把周围的建筑、马路和斑马线都搭了出来，整个街角比 GPT 那版丰富不少。

不过要说地面的雨水反光，GPT 那版确实更胜一筹。

### 09｜锦鲤鱼塘

先来回顾 GPT-6 Astra 之前实现的锦鲤鱼塘效果。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX2F2sTs3YTGEyAw4J4cKsGMSEq4FDgFncD1k9grNbg2bo6W9xMmvldeCFMAzr7yLvZ42ou0EFnj34z22FicR3SRV85EFyicUbs7U/640?wx_fmt=gif&from=appmsg#imgIndex=26)

相同的提示词，来看看 DeepSeek-V4.1-Flash-1017 做的如何？

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX3yD9leEgrphefJ56icvsndI6RyPqjF1CiaxtufwcgLCfqdGicFb5eqP5ghe73vGk94SfpM6ToibC9JCjyF9Jicc14XCE5ibYn7f0Aicw/640?wx_fmt=png&from=appmsg#imgIndex=27)

这就有点翻车了，这鱼怎么感觉像泥鳅。。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX0veWnJJSuTq4zwVicKs6ticvfOegYbfnMDGYHQM5tgd82uvBajzQibd4hLo4Oe3jjeAQyRvdcWImBdW9lLXKenSbkk2NAo2y6FKI/640?wx_fmt=gif&from=appmsg#imgIndex=28)

这时我突然想到，V4.1-Flash-1017是做3D建模方面做了升级，而这个鱼塘是平面型，可能没有针对优化？

所以我脑洞一开，让 deepseek 实现 3D 版日式锦鲤池。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX283ia3sn2gcice0byCtXO0Sa2bHVeeuIAgTAUJskibXhib3t20j9dC9WanN8PP8E5pI0TO9Vk7UMPHx0T2tAsABSHsc5SzHC072og/640?wx_fmt=png&from=appmsg#imgIndex=29)

出来的效果，确实比平面型的鱼塘好了一些。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX2HVjyibpfCDBQTk2r7iaZ6mxgcreC9TLRzrk7vCxNZY5LqGzzeMFduBBaCBhCOXEIVP1uzB4gKYciaMsXzq4bPmWRtGAm4wCWrUw/640?wx_fmt=gif&from=appmsg#imgIndex=30)

但是就是这鱼怎么是倒着游的感觉。。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX3GQicEbuhwRAGNOMBJmke4w8g4qg04ZRhgUY6JCcr9Zeia31Kh0lgtJr1zgSu89bCGNWZYwD356uQumNqTvAhjgW7xyMdDd5hR4/640?wx_fmt=gif&from=appmsg#imgIndex=31)

好吧虽然可以多一嘴就能让deepseek 修复，但是本轮的测试，就是要看一次性直出的效果。

## ────写在最后────

这一轮测下来，DeepSeek-V4.1-Flash-1017 这次的进步，真是肉眼可见，对比旧版本，交出来的东西却明显上了一个台阶。

全部实测都是简单的提示词，就一次性就做出来了完整的成品，尤其是3D建模和游戏方面做出来的效果还是比较出色的。

AI 编程实战 · 目录