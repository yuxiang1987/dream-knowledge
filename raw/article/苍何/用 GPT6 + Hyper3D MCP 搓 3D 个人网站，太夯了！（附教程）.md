---
title: "用 GPT6 + Hyper3D MCP 搓 3D 个人网站，太夯了！（附教程）"
source: "https://mp.weixin.qq.com/s/kjopmKS2uct9SR87IhUVoQ"
author:
  - "[[苍何]]"
published:
created: 2026-10-07
description: "建议收藏"
tags:
  - "clippings"
---
苍何 苍何 *2026年9月15日 21:21*

这是苍何的第 597 篇原创！

大家好，我是苍何。

最近，我想给自己的个人网站换个玩法。

之前的网站比较常规，点开页面、浏览内容，看完就走了。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/zw8bZHsVSaBxoQsnnJEOhCSvvrHsAntLrNeAavyBOGNlabuFDU09whX7ZrUTaE7LZeIc5BibSVHygH1bOSYv5J5zygEz3mdBr1w2RPMgO4Ek/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

我花了一些时间，把个人网站变成了一颗可以到处逛的 3D 小星球，里面住着小精灵，还藏着等你发现的宝物。我给它起了个名字叫「苍何的小宇宙」，哈哈哈。

![苍何的小宇宙：个人网站的最终效果](https://mmbiz.qpic.cn/sz_mmbiz_png/zw8bZHsVSaASNcYPdBQwibibwMSlGclRrT3z9kqkBib9g1Xeia5icdIM3g8HwGO0vPdX6FIWs27Wzxh5Lia2Rp6PMrXsh6fobQyoUIwRx8mzicbXiaU/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

这个小宇宙的代码由 Codex 完成，主角和小精灵的 3D 模型则通过 Hyper3D MCP 生成，再由 Codex 接入网站。

先带大家逛一圈。进入这个小宇宙后，你可以操控「苍何」在星球上自由探索。

如果不知道往哪走，还可以呼叫小精灵，让它带你前往不同的房间。和它们互动，还能收到专属明信片。

![与小精灵互动后获得的专属明信片](https://mmbiz.qpic.cn/sz_mmbiz_png/zw8bZHsVSaCeiaLqAHKUCQaNicODBl57YATFXomq6Jab0mQYuPRxpNLK59gSa5QiccvIUiagM6uglh1EommjDDgbJIGgib6wMuVezaVNY7I2yEfQ/640?from=appmsg#imgIndex=2)

每到达一个地标，你还能解锁一件对应的宝物，把探索路上的小收获装进口袋。

![探索地标并收集宝物](https://mmbiz.qpic.cn/sz_mmbiz_png/zw8bZHsVSaBXoWorEFNgxiaMKAkJJSRnjJuTmjWK7oCptlCtM35CBWM9EuicdSh6I1a8uegqjUVYIiaClFPteV5POGfHu403iaTCWRXuKZjKJ2k/640?from=appmsg#imgIndex=3)

这些角色和道具是怎么做出来、又怎么放进网站的？下面展开讲讲。

**1\. 为什么接 Hyper3D MCP**

做这个网站，我想把自己的形象和之前设计的小宠物都放进去。

参考图是有了，还得把它们做成能放进场景里的 3D 模型。

Hyper3D 也是我个人一直在使用的 AI 3D工具，生成质量十分在线，所以我第一时间想到可以使用 Hyper3D，刚好他们最近还推出了MCP，可以直接在 Codex 中使用,，十分方便。

而且经过我的对比，GPT-6 在制作 3D 人物角色模型上效果很难达到要求，接上 Hyper3D Rodin 这样的专业 3D 生成就很有必要，一方面可以快速批量生成可用的 3D 资产，另一方面还能接上大量的 token。

![通过 Codex 调用 Hyper3D MCP，从参考图生成模型、对话调整，再接入 3D 网站](https://mmbiz.qpic.cn/sz_mmbiz_png/zw8bZHsVSaBDmQx8vM4ic0zrzicLO2olkhx0icrbOgQVf03TRNiaS36whflsPdiaHI7y4wFQE1XQnjgJXwibqKRG3hibUnRsMd4NibBeK2IBH5gaAYU/640?from=appmsg#imgIndex=4)

这样，做网站的过程中需要哪个角色，就能接着把它做出来、放进去，少了自己在几个工具之间来回搬模型的步骤。

有些模型还需要拆开处理，我也用到了 Hyper3D 的 BANG 拆件功能。后面做角色和收藏品时，再展开讲这一步。

**2\. 先把 Hyper3D MCP 接进 Codex**

这次我用的是 Codex，模型选的是 GPT-6 Astra。

> 登录 /hyper3d.ai/workspace/rodin，右上角就能找到 MCP 入口。

![Hyper3D 工作台右上角的 MCP 入口](https://mmbiz.qpic.cn/mmbiz_png/zw8bZHsVSaBEOkVMlwJokQbsUwmmOvCHJHQOyhicMGHOicETicg6LWaOU4breflXPAnIGXsKnbsgj3DtDpnwozWlguEdEgd1VNAPicM0iadn0TNI/640?from=appmsg#imgIndex=5)

点开后，复制弹窗里的配置提示词。

![Hyper3D MCP 配置弹窗与复制提示词按钮](https://mmbiz.qpic.cn/mmbiz_png/zw8bZHsVSaDUtb0bzjiadud9H4M1UQeiaLHALPtIBBbddk1ubsDiaQsuTpI6xLfnjxftdP5VXL9RibgO2icUrYK2vE2Mj49EwTbgcBicUfamEzGOs/640?from=appmsg#imgIndex=6)

把这段提示词发给 Codex，让它完成配置，并按提示在浏览器里登录 Hyper3D、选择工作空间和完成 OAuth 授权。

```
●●●Please configure Hyper3DMCP in the client I am using (Codex or ClaudeCode): server name hyper3d,StreamableHTTPURL https://api.hyper3d.com/api/mcp,withOAuth. Usethis client's configuration method, preserve other settings, and reuse or update any existing entry. Guide me through browser authorization, then verify the connection and list available tools. Tell me if a restart is needed.
```

配置完成后，我让 Codex 检查连接、列出可用工具。下面能看到生成模型、查询状态、获取结果和拆件等工具已经加载。

![Codex 确认 Hyper3D MCP 配置与授权完成，并列出可用工具](https://mmbiz.qpic.cn/sz_mmbiz_png/zw8bZHsVSaA9nibZnP3o1SEMOFmOWHKrOaYiaY78HLwBBNFiaJ0kGPic1NRUULpUa1yicqK9oQy8QCA4uyKic5OwT79iarH6P7SYMQLVd9xrgyjPLw/640?from=appmsg#imgIndex=7)

我按提示新开了一个会话，先用一个头盔测试：生成一个写实的中古骑士头盔，带磨损金属材质，用于游戏资产。

![在 Codex 中调用 Hyper3D 生成头盔并取回模型结果](https://mmbiz.qpic.cn/sz_mmbiz_png/zw8bZHsVSaBaL7RMCgnciaXa8tuhxOhmlHUzH5ndEHwroC6WMAAuPREzdc3cUiaG64yrutjY9nia4Bgzv3zJe2KdHFEjJHFqQzqkdE1XSRKQicM/640?from=appmsg#imgIndex=8)

任务完成后，Codex 返回了模型结果页和 GLB 文件。点开看看，金属表面的划痕和磨损都做出来了。

![Hyper3D 生成的金属头盔及模型下载选项](https://mmbiz.qpic.cn/mmbiz_png/zw8bZHsVSaCpt55rq3ZBODDX1xUZibp8VP6cxbqOIjHpiblz053RomqdXlHLwPQBSWdxh3AF2kV7I1gCTx7Mm2JhqlhiaXtYL28Gr1wfDkJly4/640?from=appmsg#imgIndex=9)

到这里，从 Codex 发起生成、再取回模型的流程就跑通了。接下来，把它用到自己的小宇宙里。

**3\. 把「苍何」做成 3D 角色，再接进网站**

网站原型这边，我先把个人介绍、作品和想展示的内容交给 Codex，让它规划星球和地标，搭出能移动、能触发互动的版本。

下面是接入正式模型前的效果。交互已经能跑，但人物还是基础占位模型。

，时长00:15

<video src="https://mpvideo.qpic.cn/0bc3hydvgaahueakyefp5rvfopwdkm7aouya.f10002.mp4?dis_k=7cf9f28ffd59cdbde6c66c782e686668&amp;dis_t=1791339950&amp;play_scene=10120&amp;auth_info=C/jBoAxhZj6w4cGSD1FgYFQmaW5PSmMxXDAzZldhYR4tHgF9cXorSTomaVNjXEB0Xg==&amp;auth_key=c5f2bff96d3d29d41242ff713d966ad9&amp;vid=wxv_4695407781955338242&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

要把里面的主角换成「苍何」，先准备好角色形象。

我把自己的形象图交给 Codex，让它整理成适合这个小宇宙的低多边形 Q 版风格。下面这一步得到的是参考图片，后面再用它生成 3D 模型。

![先准备低多边形 Q 版角色参考图，此时尚未生成 3D 模型](https://mmbiz.qpic.cn/sz_mmbiz_png/zw8bZHsVSaALkyI3umjDiaGiaSGNU0tc1sK99x4w5AZQeuMOJSOGasBVPehQuyBIOiaSticegibtmOsKdfUyDf0dVlBY0bIjbqDCJzKqxfCpqiaFc/640?from=appmsg#imgIndex=10)

有了参考图，再让 Codex 通过 Hyper3D MCP 调用 Rodin，生成对应的 3D 角色。

第一版模型出来后，整体形象已经对上了，但眼神有点呆，少了一些灵动感。转一圈看看效果：

![Hyper3D 生成的第一版角色模型预览](https://mmbiz.qpic.cn/sz_mmbiz_gif/zw8bZHsVSaBKBAZPDoBRFuxZSiasH287yNH1YsKJffXgWpHKiau2Uxo9NmuBSNJURKPfZoAOX3Cw1DUibGQSH9waJkW9ISBATBLiciau4MLlhgIE/640?from=appmsg#imgIndex=11)

我直接把问题告诉 Codex，让它继续调用 Hyper3D 调整，保留原来的造型和配色，把眼神优化一下。

![提出眼神修改要求后，Codex 返回新版 Hyper3D 模型](https://mmbiz.qpic.cn/sz_mmbiz_png/zw8bZHsVSaDmwwPq31eVYNhTspZxNqvjYkCx5n1eF1wKtFvWm5MgeicpiaOAPx3EFcZH0w2VspAmbZvTWj1xfe3rm8R1kADjgpWO015jFbicok/640?from=appmsg#imgIndex=12)

第二版明显顺眼多了。下面是调整后的模型预览，可以和前面那版对照着看。

![调整眼神后的第二版角色模型预览](https://mmbiz.qpic.cn/mmbiz_gif/zw8bZHsVSaAibEE4XibNUe3GKfgzYxjPzflGwycVtp0U1a5vqIB0jcEmOuqibptlpszmrtZhXpCBhuSGia4kttDznj2QUV1VMzichm0cMW0hHicicw/640?from=appmsg#imgIndex=13)

确认效果后，我让 Codex 把新版模型接进网站，替换原来的主角。

刚才还在模型预览里转圈的「苍何」，这就站到自己的小星球上了。

![Hyper3D 生成的角色模型接入网站后的效果](https://mmbiz.qpic.cn/mmbiz_png/zw8bZHsVSaAJe0KUI2OsvxJsZDYBbbiavPia7gaWLxceNiak8bXAM9vxHj16hRvia0PVodIjFPyP60BVuP1blmSCicZ4ibH7NhhGo0NGLIicMXdofg/640?from=appmsg#imgIndex=14)

**4\. 批量生成小精灵，让它们住进不同区域**

小精灵用的也是这套流程。它们的参考形象，来自我之前在 WeSight 里设计的小宠物。

先看准备好的参考图，机器人、水滴、火焰和小木箱，各有各的样子。

![用于生成小精灵 3D 模型的角色参考图](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zw8bZHsVSaA4RdCmVu10RR1Zvm3BumeGCjlXFxRYybc4Rk9psu9vPOmrV8ZTOUNQlKt39QLRafichoNKf1t6a1yXrhYVCdibbORiaiaVf3dtQ7c/640?from=appmsg#imgIndex=15)

我把参考图和风格要求一起交给 Codex，让它通过 Hyper3D MCP 连续提交生成任务、查询进度，再把模型结果取回来。

生成后，还要逐个看看造型和画风是否协调。下面这段视频，就是这批小精灵的模型效果。

，时长00:17

<video src="https://mpvideo.qpic.cn/0bc3dubauaack4aauovlarvfehodbioqecqa.f10002.mp4?dis_k=6474da05833d82f102a3c41e2a0e91d8&amp;dis_t=1791339950&amp;play_scene=10120&amp;auth_info=Io2yhoEINGRs4uuSx1xQZzJaKGo6HRdkM1FuZjEGYDAcfkpWKiEvKRtoLDoGMF1HJlA=&amp;auth_key=400bc05dce478e2a79877a45df6a4d43&amp;vid=wxv_4695410648242077698&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

确认效果后，我让 Codex 把模型下载为 GLB 格式，再接入对应区域，配上靠近、对话和带路等互动。

为了实现最好的效果，我干脆将房屋建筑这些元素，也用 Hyper3D Rodin 重新生成更换了进去，给星球做了个整体升级。这样一来，小精灵就真正住进了这个小宇宙。下面能看到接入后的样子:

![小精灵模型接入各个区域后的场景效果](https://mmbiz.qpic.cn/sz_mmbiz_png/zw8bZHsVSaBt7wHShJdED2Tvfp4ae6ntcgQp1B6AmCse0luY2icepO7victC5nxV09lLeku6Hn5ibzibdBOL19zbz5yYnpoLLl9yEZT0eKAmcYU/640?from=appmsg#imgIndex=16)

**5\. 用 BANG 拆件，继续处理模型**

模型放进网站以后，还有一些细节需要处理。比如「苍何」刚接入时，移动起来像幽灵一样在星球表面漂移，脚底没有真实的行走动作。

，时长00:13

<video src="https://mpvideo.qpic.cn/0bc3sidk2aagryak2ofpkzvfnewdvwjanlia.f10002.mp4?dis_k=c4614bfa23c8553ed4b9d9b36f944f8d&amp;dis_t=1791339950&amp;play_scene=10120&amp;auth_info=d/Go46IDM2k/tO+Vzg1dMG4GfWo7GEdnZQVkZmFabTdJKh5QKSsoJEg+KD0PYVAQegw=&amp;auth_key=63a90c72f05c96ee639fb621f79750f3&amp;vid=wxv_4695409875969376260&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

这次我想把角色的不同部件分开处理，就用到了 Hyper3D 的 BANG 拆件功能。

**BANG 可以把一个完整模型拆成多个独立部件，方便后续单独编辑、重组或使用。**

我让 Codex 先通过 Hyper3D MCP 完成拆件，再把部件交给 Blender，进行骨骼绑定和行走动画制作。下面这段对话里，也能看到这两步的分工。

![通过 Hyper3D MCP 拆件，再由 Blender 完成骨骼绑定与行走动画](https://mmbiz.qpic.cn/mmbiz_png/zw8bZHsVSaCiaZiawsEpvVUt4f3WNSjPrjYoBaG5oicydlkz0LcMp98kyfu5kbzjCtiaFhn4FxooyezaMicj2kxlwjicmaziaxVlic5ayt2CMdAyiamk/640?from=appmsg#imgIndex=17)

拆件后，头、躯干和四肢等部件可以分开处理。接着在 Blender 中完成绑定和动画，处理过程是这样的：

，时长00:18

<video src="https://mpvideo.qpic.cn/0b2eruamiaaaliamj5njtjvfbdodysgqbraa.f10002.mp4?dis_k=a762e7c573f39cdb969971f5b23b3104&amp;dis_t=1791339950&amp;play_scene=10120&amp;auth_info=IL7pmOMHYGE7srvBxFtaZ2ZWf2k7GxYyYFFhZmRRYWEeLUNScit7LEw4fGkFN1dHclw=&amp;auth_key=a88de75c093d7111067f6680e1df6937&amp;vid=wxv_4695413014886563841&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

这一套处理下来，角色终于能贴着星球表面正常走路，不再一路漂移。

拆出来的部件也可以用到别的玩法里。这次我还用 BANG 的拆件能力制作了收藏品，把它们放进八个地标，让访客边逛边收集。

下面是收藏品和收集互动的效果：

，时长00:11

<video src="https://mpvideo.qpic.cn/0bc3v4dbmaagomaotnfokrvfnl6dc2xqmfqa.f10002.mp4?dis_k=035fa175080205b68c54fea392851388&amp;dis_t=1791339950&amp;play_scene=10120&amp;auth_info=C9PErShjNjjm6srFAVxnZVombj4cFWQyU2NlOlJqMk8tTFwoJ3h7T2wtYgRtUUdxUA==&amp;auth_key=8099f12e77e725c928deb1607d849bab&amp;vid=wxv_4695408789662203912&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

最后再补上配乐和一些交互细节，这个小宇宙就慢慢完整了。

**最后，从一个模型开始**

这次做完，我觉得挺顺手的一段，就是把参考图交给 Codex，通过 Hyper3D 生成角色，再把模型接进网站。

眼神不满意，就提要求再改；需要一批小精灵，就按参考图继续生成；模型还要进一步处理，就拆件后接着编辑。

从想法到模型，再到网页里的角色，这条流程就这样一步步跑通了。

想试试，可以从一个模型开始：进入 Hyper 3D 工作台的 MCP 入口，复制配置提示词到 Codex，按提示完成授权，再生成你的第一个角色或道具。

目前我看 Hyper3D MCP 活动还有福利： **免费领取 10 个 Credits，以及 1 美元体验 Creator 创作者会员首月。** 具体领取资格与续费价格，以活动页面显示为准。

![Hyper3D MCP 活动权益：10 个免费 Credits，Creator 首月 1 美元](https://mmbiz.qpic.cn/mmbiz_jpg/zw8bZHsVSaBVmXwibIq9Os0RyZ53Lzx2gqdFllWMM0L9EOCN8h8rMNOMibKtmZU9bvAtQQj9MuIiafeLongptSDCJokS0JHFaZOuNEGaxIkxqY/640?from=appmsg#imgIndex=18)

如果觉得有用，点个「赞」和「在看」支持一下。

苍何

邀请你前往腾讯公益一起捐

我为家乡上大分

275人捐赠

AI · 目录

作者提示: 个人观点，仅供参考