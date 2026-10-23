洛洛 洛洛AI说 *2026年9月14日 15:05*

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/smYNP8B0KCkfG199nprXY5Pl8rIKy7YvSzL3HGZCufOnnBib2GgtaGeZyMUDX1LrWBYq7OaQsjicwHHennEwPzQuoiaRuRwCjbj9HuicSDR1cVM/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

洛洛的第37篇原创文章

大家好，我是洛洛。

2026年9月3日，OpenAI正式发布了GPT-6 Astra，官方给它的定位是“面向最难的端到端工作”，总裁Greg Brockman在发布会上直接说了一句，“欢迎进入AGI时代。”对普通人来说，更关心的其实是三个问题，这东西我该怎么用？它到底强在哪？怎么用才能少烧Token、少花冤枉钱？这篇文章我们直接从实测出发，把GPT-6 Astra的使用方法、真实能力和省Token技巧一次讲明白。

![图片](https://mmbiz.qpic.cn/mmbiz_png/smYNP8B0KCkVkS95gbbqrrVDBBAMw4ZKjQ2K1h5uHiaH9icfWyKlAy3pm1eUJxmlAVX9y9OweojSr8j39ErsYWfZXmQJCNQLgzyckKdT2utb0/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

**GPT-6 Astra上手指南**

首先准备一个支持GPT-6 Astra模型的账户，ChatGPT Plus或Pro订阅账户就可以。

工作模式，可选择GPT-6 Astra模型和强度。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/smYNP8B0KClcfJDl8eNWhia3icQgccLOYs22hS2FUDjCnN3nCQFN1ZrHgajJJ3nABVicD7wrzAboWShbKV5zJDyicU4v6pdqbVO9ib8akfbpKItI/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

或点击网页版左边的Codex下载客户端应用。

![图片](https://mmbiz.qpic.cn/mmbiz_png/smYNP8B0KCngSicYrcwKBgWQboYZHtuxCC82a4d187sZO27aLnSupTdLojw6iaCDQlFq0NSZCJS4BfZk5UZs0ibMbHXRw3kGKKib20ia76oGjf0M/640?wx_fmt=png&from=appmsg#imgIndex=3)

在Codex左上角可切换ChatGPT和Codex，可选择ChatGPT里的工作模式或者切换成Codex。GPT-6 Astra目前主要支持ChatGPT工作和Codex使用，Chat模式暂不支持该模型。

![图片](https://mmbiz.qpic.cn/mmbiz_png/smYNP8B0KCkR36ceg0rF8ibMccaUFskfo8pMz5zXJhm2ribohRkTYldMTKN22L7ar24PiaU9T2pCa2LYfNdrpamna53jdSGAeQMAzfna0hasSI/640?wx_fmt=png&from=appmsg#imgIndex=4)

打开后在工作或Codex里的模型选择里找到“GPT-6 Astra”就能用了。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/smYNP8B0KCmWP9uKKalQV8bH0uw7cBUgIJfiaFXY8ma61lVx0keGxllBOBhnmAflvQt8pHbKuww1DWseb8iaskDZk70zlic89omA1vOVv6ibYHs/640?wx_fmt=png&from=appmsg#imgIndex=5)

选择GPT-6 Astra模型后，有一个五档等级的滑块：轻度、中、高、极高、Ultra，这个推理等级通俗来说就是“让AI动多少脑子”，它决定模型内部“想多久”，也直接决定你的账单。等级越高，思考越深入，效果越好，但花的钱也越多、速度越慢。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/smYNP8B0KCkkN5SWHj1SHohOePbZqr6z7VZ4esdD3icj7JJEicNRr0gbDzW61AanyWyyWibfYFiaOfUUo2GJkWbpcg4OPNgicjahiaWJxekNMuZyg/640?wx_fmt=png&from=appmsg#imgIndex=6)

了解了怎么使用模型后，我们拿几个case测试一下GPT-6 Astra的表现如何。

![图片](https://mmbiz.qpic.cn/mmbiz_png/smYNP8B0KCmXJia8tRO8plTlY67B58ECFVSxE09FpOOZ2AP690H20dcd8eu3dGVtwvhZt2ef05KNicegAk3StXwh5HYRb9gh9GpmOkgBNIo3g/640?wx_fmt=png&from=appmsg#imgIndex=7)

**GPT-6 Astra VS Fable 5.1**

本次测试使用Codex客户端+Plus账号“GPT-6 Astra 高/极高”模式，对应Claude Fable 5.1 的“High/Extra”模式。每个案例均配了图片与视频，图片用于快速预览，想了解更多细节，可观看视频。

**Case1：AI天气桌宠**

让模型生成一个桌面天气桌宠小组件，一个可爱的卡通小女孩站在卡通街道上，她的衣服会随天气自动变化，场景也随天气变化，还会告诉你今天该穿什么、带什么。由于涉及天气API调用、SVG角色绘制、多套穿搭系统、复杂动画状态管理，推理等级我选高。

提示词：

用HTML5 + CSS3 + 原生JavaScript 开发一个桌面天气桌宠小组件，桌宠形象是卡通小女孩，根据用户地理位置获取实时天气，动态生成对应天气的街道场景，她的衣服、动作和表情随天气变化，同时给出基于天气的穿搭建议。

要求：

1. 单个HTML文件，可直接在浏览器运行
2. 用electron-builder打包为macOS桌面应用

先看组件的icon，读者老师更喜欢哪个呢？

![图片](https://mmbiz.qpic.cn/mmbiz_png/smYNP8B0KClNhW55FsUcicia6zKibGU5ia4J0YqiafZbKWKg2OjE2RxLMOIH2cMVOzssHzdF6XvZTI1iclNzewQtmuIicDbk27bSaVzc3tq8In6eFQ/640?wx_fmt=png&from=appmsg#imgIndex=8)

GPT-6 Astra分宽版和窄版界面，分别对比一下左边GPT-6 Astra和右边Claude Fable 5.1的主界面，我没有提要求，GPT-6 Astra有展示当前时间，Claude Fable 5.1没有展示。

![图片](https://mmbiz.qpic.cn/mmbiz_png/smYNP8B0KCkX0sAesjgqG7QlPiaBxkAB3SUzu9c6rA53uUtA2aaFqDaKNHl21yjVZUZt7c72wnh2NP6KqFBkdUYoRf8J5u1opwLzUH04gpO0/640?wx_fmt=png&from=appmsg#imgIndex=9)

天气数据同步准确，使用同一数据源Open-Meteo，GPT-6 Astra每15分钟自动更新，Fable 5.1每30分钟更新。

两者都可搜索城市。但GPT-6 Astra无法获取定位城市，Claude Fable 5.1可以。

人物表情和动作，GPT-6 Astra有6种演示模式。Claude Fable 5.1可通过天气、温度、风速、时段交叉组合出更多模式。两者动作表情、穿搭都与温度天气匹配，Claude Fable 5.1的动作表情更丰富。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/smYNP8B0KCl2wDtIeA9CtUmXs9VD6TcHpBHBnaHSTtwROYcQSLHMseGibsBh6zfjPXtpZFctR4kkcgWJPVvqIicHCMtZ4nvo5COl1Sxgx6LC8/640?wx_fmt=gif&from=appmsg#imgIndex=11)

▲Claude Fable 5.1的动作表情更丰富

想要查看和对比更多细节，可以查看以下视频。

，时长01:17

<video src="https://mpvideo.qpic.cn/0b2elualyaaa6iamwxff4zvfaxodxroqbpaa.f10002.mp4?dis_k=db7464dec2fcd6b0d2481bdf7468be04&amp;dis_t=1792737296&amp;play_scene=10120&amp;auth_info=WIn2/sUWTCF/6sChkjImax00CSpoOREaYS4dNzYuH29mUGJBTRsRTh0YLSM0EDFRFw==&amp;auth_key=539966122d49bb1bb9c9b605b0d061de&amp;vid=wxv_4691525386885496834&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

▲Claude Fable 5.1

，时长00:46

<video src="https://mpvideo.qpic.cn/0bc3w4cskaaf2aafflnajnvfln6dew3qkjia.f10002.mp4?dis_k=b43d620eae79d409f6332373fedaefdd&amp;dis_t=1792737296&amp;play_scene=10120&amp;auth_info=WsmEl5VAH3Quu5L4lTFyOxtiDXpoP0UaY3lMbTYsTWZkVGVKTkpCG0xJf3ozE2UBEQ==&amp;auth_key=9e4b1e4efd5f6864ad2ce17bb202e27f&amp;vid=wxv_4691524176661200897&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

▲GPT-6 Astra

再看消耗，GPT-6 Astra跑完这个case，消耗了Plus账户55%的5小时额度和9%的周额度。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/smYNP8B0KCnd5XXazL6cIZZGUWiciccMK4XpHYXcQYZxVZbbOtLGZSzoMYDF3akCFN77DkLw2eTCA8PIoibGVanU5SzL2a8EMbrIs0Ry8gghd0/640?wx_fmt=png&from=appmsg#imgIndex=13)

**Case 2：橘猫横版跳跃小游戏**

用HTML5+JavaScript生成网页游戏，由于涉及多步骤代码生成、资源生成和软件操作，推理等级我选“高”。

提示词：

用 HTML5+JavaScript做一个完整可玩的横版跳跃小游戏，主角是一只橘猫，在城市屋顶上奔跑跳跃，收集鱼干金币，躲避鸽子敌人和掉落的花盆。3 个关卡，难度递增，第 3 关有 Boss 战（一只大狗）。

要求：

角色和场景用简洁的像素风格，配色温暖；

导出HTML5网页版；

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/smYNP8B0KCkVpPJJODlzMLG8bwD93kur9gxmgRO53NPEcCSjZRZu0s4npHx7emvia4FcO0Loich0ojYTvA4nAYSVJcR1ic0xibObicWxYCPxHzc0/640?wx_fmt=png&from=appmsg#imgIndex=14)

GPT-6 Astra

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/smYNP8B0KClAoJaHrJONL6oaXSEkn7A2VKd1mxicFC5T5grJ07DicOIacP57zOecI3ibFXd824Koxyrgn4jsw3ary3VEwmVRQfslK7zXI1fboE/640?wx_fmt=png&from=appmsg#imgIndex=15)

Claude Fable 5.1

GPT-6 Astra游戏界面简洁，配色优美，操作灵敏流畅，音效匹配。Claude Fable 5.1游戏进行中有bug，角色腾空后不下落，到房顶后又掉下去，碰到小鱼干也不会拾取。任务完整度上，GPT-6 Astra完胜。

，时长00:09

<video src="https://mpvideo.qpic.cn/0bc3ceawgaabeeabxefefzvfceodmmiqcyya.f10002.mp4?dis_k=53e3fd94d5b5b4a29db45aa401c932aa&amp;dis_t=1792737296&amp;play_scene=10120&amp;auth_info=BfnPlt0RSXN475Wgw2V3PkxlWy04aUxLZikZYTAsHG07BjRNSRgUHBodeCJlR2AERg==&amp;auth_key=be32018646573af65aa89c5c28e348bc&amp;vid=wxv_4691527554283880448&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

▲Claude Fable 5.1游戏bug

想要查看和对比更多细节，可以查看以下视频。

，时长00:20

<video src="https://mpvideo.qpic.cn/0bc3biabsaaaxaagdo5fervfacwddefaagia.f10002.mp4?dis_k=76db5430fdc81b81608c8adcf3a62f43&amp;dis_t=1792737296&amp;play_scene=10120&amp;auth_info=cpOu9F5JIyu4xfjGZXBrSmEIejw4QUwyeh83aikfZzNUZkEfQRRMSUooemBHZ1FA&amp;auth_key=0580df0641808f400ba8ea6cd5f9691b&amp;vid=wxv_4691529735036993543&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

▲Claude Fable 5.1

，时长00:04

<video src="https://mpvideo.qpic.cn/0b2etealeaaatqamxwvfozvfbgodwkmqbmqa.f10002.mp4?dis_k=b9cabc23a417b6be1842eca8b7e05bfb&amp;dis_t=1792737296&amp;play_scene=10120&amp;auth_info=DYH6wcwQSX8q6ZOpxTVwPRtvXX88bkdMYyhKYzAuHzozWmJLGRoUEEgbfitjF2cHEQ==&amp;auth_key=2e11643e5b803445e071e1047cda33b0&amp;vid=wxv_4691531121120198661&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

▲GPT-6 Astra

跑完这2个case后，Codex的5小时额度就只剩20%了，各位读者老师可以直观感受一下额度的消耗速度。

![图片](https://mmbiz.qpic.cn/mmbiz_png/smYNP8B0KCmoTKwnKObdTEVS0FkLeDqHztGJyTugXB6MK67Ezq0dYMoJsNH7Rian7OVG3g0zT0YlWYB2YlUIkoHCTC6xqiaX7M4FeV69QMk68/640?wx_fmt=png&from=appmsg#imgIndex=16)

跑个题，GPT的文字功底还是不错的，天气桌宠和橘猫小游戏里的文案有故事性和感染力。

**Case 3：AI室内设计师**

给一张户型图，让模型使用插件computer use操作Blender（免费开源3D 软件）创建3D场景、摆放家具、渲染出图，最后生成一个可以在浏览器里旋转查看的交互式3D页面。因为涉及多步骤脚本编写和3D软件操作，推理等级设置为“极高”，仅次于最高档Ultra。

考虑到前面case额度的消耗速度，我提前准备了Blender和Three.js等。大家可以用Chat模式让GPT帮大家下载和安装，不消耗Codex的额度。以下是我的操作准备。

提前让Chat模式帮我下载和安装Blender。

![图片](https://mmbiz.qpic.cn/mmbiz_png/smYNP8B0KCmnL7iaor2vsfxiaFDKSF8AtBhmp4HX0fWLbyvhebKNDwbngS2Vm64jRbmpwgJprHZSkLUvAlDXYwsqUS3FATWVxKj1PViaDiciaib5s/640?wx_fmt=png&from=appmsg#imgIndex=17)

点击Codex左边的“插件”，搜索并安装“Computer Use”。

![图片](https://mmbiz.qpic.cn/mmbiz_png/smYNP8B0KCl2kGYbTztnGiazFFrziakmy1gDM93tuXKMAuXepDMWrqGmBVibqI4NU6mOoCqHlpcx1y1zEV8Khiaaoz7ty6ibqN7HqKOKNZMepcqU/640?wx_fmt=png&from=appmsg#imgIndex=19)

Codex客户端设置里，找到电脑操控，把“任意应用”和“锁屏操作”打开，这样电脑进入锁屏状态，Codex也能继续执行进行中的任务。

![图片](https://mmbiz.qpic.cn/mmbiz_png/smYNP8B0KCk7ajjaEVrnt1Aib24UF0rZu1SV4XeRt7xvE39eyqwNONc3SicczmDzYlsQFmneAh8LUl2YwkWSlQ4Tmh3ojqahLzpnPlMxNE8NU/640?wx_fmt=png&from=appmsg#imgIndex=20)

接下来开始跑任务。

提示词：

根据这张户型图，使用computer use操作Blender做3D建模渲染、Three.js做交互式预览，生成一套可交互的完整的全屋3D设计方案。

要求：

1. 风格为北欧简约，严格按图上的房间数量、相对位置和大致比例建模
2. 墙体、门、窗都要有，门窗位置和图上一致
3. 每个房间放置基本家具（卧室有床、客厅有沙发、厨房有橱柜等）
4. 支持第一人称视角，用 WASD 移动、鼠标转视角
5. 输出HTML文件和工程文件，不要解释说明
6. 所有代码和资源内联在一个 HTML 文件里，不依赖外部文件输出

**GPT-6 Astra:**

![图片](https://mmbiz.qpic.cn/mmbiz_png/smYNP8B0KCmic1vNbqpzTE8nzOYWyjDoMic1TTH5TUdUJia80cruy3bpA6C5mJT3vJnXDWpETjshIwp4Zicvo0DcR3ILJYksudbxDRjNG7icPBSw/640?wx_fmt=png&from=appmsg#imgIndex=21)

除了卫生间家具摆放不合理外，大部分家具布局合理，渲染效果真实自然，交互流畅，视角清晰。我回溯查看GPT-6 Astra的生成过程，它写道“通行检查已通过：10 个空间均可从客厅步行到达，所有房间落点都避开家具和门扇。已调整厨房通往北阳台、卧室 B 通往卫生间 A 的通道”，“房间连通性检查已通过”。我没有在提示词里要求它，它主动做了。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/smYNP8B0KCm5KOXbt49wnveVFIFFIvD0AZ1ibR0kRQHjmriaRVSdQTkpNoTILVOFZ5O6dTOoQUWNY2mI52ib4W7FRqRDTLBDg3MmImUnv6AcgQ/640?wx_fmt=png&from=appmsg#imgIndex=23)

▲卫生间摆放不合理

**Claude Fable 5.1：**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/smYNP8B0KClzPNndWmPehA1EibZotBk1iapRUKM2HyMO1hsSwt9SM1a6TR0hic9YY44oha39O8OY64uWX5XONA6xbpafkkibvP1c9Lrn5icriaV8Q/640?wx_fmt=png&from=appmsg#imgIndex=24)

家具布局不合理，卧室家具摆放相互重叠。

![图片](https://mmbiz.qpic.cn/mmbiz_png/smYNP8B0KCmYppl62vcrHuEN4gbOv8rD10sbiaZ1Iibge3IjS58icpic1SglVicwrLDU6qb22qjUiaick4jpzs05oyXAhwf4qHgYMliaAdxKXdnK854/640?wx_fmt=png&from=appmsg#imgIndex=25)

家具布局影响通行和开关门。

![图片](https://mmbiz.qpic.cn/mmbiz_png/smYNP8B0KClNKmkxn3z7mCHdgT1cvickFaofu5K7g5eicrwxfEhrkjRcicmkpjfY2ictVib8ejJaMqAjvw9Z24aj9FvgY1AuZDN3b2INCiabVC3xg/640?wx_fmt=png&from=appmsg#imgIndex=27)

3D漫游操作也不灵敏顺畅。

想要查看和对比更多细节，可以看以下视频。

，时长00:29

<video src="https://mpvideo.qpic.cn/0bc3tiadkaaacuaeyu5fczvfbgwdgwnaania.f10002.mp4?dis_k=a7241e922033daa174d4c62b440c72ae&amp;dis_t=1792737296&amp;play_scene=10120&amp;auth_info=C8Gy69xFGiV86sb6x2V3OhhhDCpvaExNMCxIZzZ5HG41VjJNH09HSh4YK3hhR2AAEg==&amp;auth_key=76beb083d8a5c8f1501cc779cb8f9bb9&amp;vid=wxv_4691533443438837761&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

▲Claude Fable 5.1

，时长01:00

<video src="https://mpvideo.qpic.cn/0bc3n4aleaaaguamxv5fcrvfa36dwjxqbmqa.f10002.mp4?dis_k=5c31e10b5c54fcfe6f5d1615e7422aa2&amp;dis_t=1792737296&amp;play_scene=10120&amp;auth_info=Csq+44VAGXIt6cKrwjZ3bUw1DS87PEUdN39OYDR7Gzo0BGMdTU9EHU8bLylkFGBXRg==&amp;auth_key=17cc36083d95b10faafe2096bf19a42f&amp;vid=wxv_4691532550740410368&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

▲GPT-6 Astra

这一轮GPT-6 Astra累计花费了近2.6倍的5小时额度。耗时也较长，任务总执行花费了1小时，包括等待额度重置的总自然时间花费了14小时。

三个任务跑完，GPT-6 Astra的任务完成质量、审美都在线，尤其是橘猫小游戏和室内设计这两个case与Claude Fable 5.1的差异尤为明显。

三个任务共消耗了GPT-6 Astra 3.4个5小时额度，一半的周额度。亮眼表现背后，资源开销值得关注，接下来让我们看看有哪些节省Token的技巧。

![图片](https://mmbiz.qpic.cn/mmbiz_png/smYNP8B0KCkbPg7FfX8hjIGxibK2FJd6XWzW27gC2kdAc2lYTUABSL4qtFXssY04o9FtcCHLR7z7P037vusODW1aw74PrRJ5sESAibkbWYMtE/640?wx_fmt=png&from=appmsg#imgIndex=29)

**怎么省Token?4个技巧少花冤枉钱**

GPT-6 Astra能力很强，但用起来不便宜。刚上手的新用户很容易不管什么任务都直接把模型和推理强度拉满。结果就是大量Token花在了根本不需要“满血Astra”的任务上。想控制成本，该省的地方省，该花的地方再花，下面分享4个比较实用的技巧。

**技巧1：别用大炮打蚊子，先给任务分级**

不是所有任务都需要GPT-6 Astra+最高推理强度。像简单翻译、格式转换、会议纪要整理等轻量任务，便宜模型通常就够了，成本也更便宜。

使用前先给任务简单分个级。简单任务，如分类、提取、简单翻译、格式转换，用便宜模型。中等任务，如写文章、总结资料、常规分析，用“中”档。复杂任务，如复杂推理、长文档处理、多步骤操作、需要自主规划执行的工作，再考虑“高”或“极高”。可以先用够用的档位或先用 “中” 档试跑，效果不够再往上加。

当然，如果任务本身非常重要，或者你的时间成本远高于Token成本，直接拉高推理强度减少试错也很合理。

另外还要注意不同模式的额度机制。Chat和工作/Codex是两套独立额度池，Chat不会占用工作/Codex额度，工作与Codex共用Agent额度，可以简单任务优先走Chat模式，节约Agent额度。预算充足的朋友可以忽略这条。

**技巧2：一次性把需求说清楚，减少无效上下文**

省Token的第二个关键是减少无效上下文。输入的每一个Token都会计费，很多提示词带有大量寒暄铺垫“你好呀，我最近遇到一个问题...”，这些内容不会提高结果质量，却会消耗额度。更高效的写法是直接告诉AI任务目标、约束条件与输出格式，去掉多余客套，效果不变，Token消耗更少。

同时避免“挤牙膏式”逐轮提问，每次追问会持续带上全部上下文，不断扣费，还容易让AI跑偏，产生额外修正成本。所以能一次说清楚的需求，尽量一次说清楚，初稿出来以后，再针对关键问题修改。

处理长日志、大文档时，尽量上传文件或提供路径，让Agent按需检索相关内容，而不是把全文一次性粘进上下文，这样通常能减少不必要的上下文消耗。

**技巧3：控制输出长度，别让AI写一堆你根本不看的东西**

输出同样会消耗Token，在不影响交付质量的前提下，可以直接在提示词里限定输出字数上限，减少冗余文本。

**技巧4：利用缓存，但别迷信“一个对话聊到底”**

GPT-6 Astra支持提示词缓存，命中缓存的输入价格仅为普通输入的 1/10。所以同一组相关任务，优先在同一个对话窗口连续执行，复用缓存，不要每一个小任务新建对话。但长对话越往后上下文越长，单次请求成本会持续上涨，有些场景新开对话反而更省钱。另外，缓存存在有效期，超时自动清除，无法复用。

还有一个高频坑，同一窗口切换不同模型，原有缓存失效，上下文重新计费。但Astra 支持模型不变时调整推理强度，会尽可能复用已有缓存。

归根结底，省Token并不是想办法“少用 AI”，而是把最贵的模型、最高的推理强度和最长的上下文，用在真正值得的地方。

![图片](https://mmbiz.qpic.cn/mmbiz_png/smYNP8B0KCkKop6DMKJia6tDHPxNBFhHJzR01Zcy8ZeTDkHI8bfmlcQLwX5DSKnB4Js5aibemZp5G2Yc288Gsic4b9AvyjAoQrqh5wmgfibnnYI/640?wx_fmt=png&from=appmsg#imgIndex=31)

**洛洛有话说**

这次GPT-6 Astra让我印象最深的是Computer Use操作，比如控制Blender完成室内设计，整体任务完成度都比较高。其在代码、视觉理解、软件操作和连续决策混在一起的复杂任务里，综合能力确实比我预期更强。

在做室内设计时，我没有要求它检查动线和房间之间的连通性，GPT-6 Astra主动做了这一步。GPT-6 Astra能主动检查这些问题，说明在这个任务里是能够把一些现实世界的常识和约束带进任务。这种“常识”，决定了最终交付结果到底只是看起来完成了，还是真的能用。

当然，强大的代价也很直接，额度消耗是真的快。推理越复杂、任务链越长、Computer Use操作越多，使用额度往往上涨也越快。室内设计这个case整个任务实际运行约1小时，却横跨了3个5小时额度窗口，包括额度等待总自然时间花费14小时，累计消耗相当于259%的单窗口额度，周额度也一次用掉了41%。所以好钢用在刀刃上，GPT-6 Astra更适合用在真正需要它能力的地方，简单任务没必要交给最强模型。

至于GPT-6 Astra是不是已经接近AGI，个人觉得还太早。给目标、检查关键节点，还得人来。

读者老师们，关于GPT-6 Astra，你已经用过了吗？实际体验怎么样？有哪些惊喜，又踩过哪些坑，我们评论区聊聊~

作者：洛洛&anan

编辑&校对：洛洛&anan

AI应用测评 · 目录

作者提示: 个人观点，仅供参考