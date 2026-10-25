---
title: "Flash模型又添一员大将：实测MiniMax M3.1"
source: "https://mp.weixin.qq.com/s/af7_9F_3oeeqzB2YmqUilQ"
author:
  - "[[夕小瑶编辑部]]"
published:
created: 2026-10-03
description:
tags:
  - "clippings"
---
夕小瑶编辑部 夕小瑶科技说 *2026年9月30日 15:28*

上周，OpenRouter 又来了一只飞快的兔子。

一个叫 Space Bunny Alpha 的匿名模型悄悄上线，1M 上下文，能看图、能看视频，思考强度五档可调，免费。

**免费、1M 上下文，** 开发者当然不会放过。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/0hd8MxUumHPl2eXMBUxbNIK4l5PibqSqlaqTsiayQhDxA17X6L3yCOZLN8r0I8rkqOictfl3V6vo4J494eTibkicbx1bCElYHR9U9iaKQJMnVIVe4/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

没几天，就蝉联OpenCode榜首第一名。

社区开始给它做指纹测试，一组 24 项的对比，全部对上了 MiniMax 家族的特征。

9月27日，MiniMax Code正式上线 M3.1-Flash-Preview，同样的 1M 上下文，同样原生支持文字、图片、视频输入，思考强度也同样五档可调。

![图片](https://mmbiz.qpic.cn/mmbiz_png/0hd8MxUumHNsP6Jk8B5K1O3Ed4Q3mg4LMUpiccg0fLP7shlWAiaEqu6ibyAXtUeUR0v1DA7ib7cziccRh5G5CaBCdDOBjNyKS5JaqeYzEoZpPYEg/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

官方没有公布跑分，目前只能在MiniMax Code和Token Plan里用。模型定位是：

**Flash级别，速度快，干活靠谱，主力场景是Coding。**

这两个月，Flash这条赛道格外挤。DeepSeek V4.1 Flash占着位置，我们前阵子刚测过的 GLM-5.3-Flash（牛来）又把价格打到了地板。

既然没有跑分可看，我们就直接上实测。我在MiniMax Code里开了几个任务，全部拉到max档。

## ◈一、Coding：接手一个真实的线上项目

第一个是我自己的一个小项目，给服装店用的 AI 试衣间。

顾客上传全身照，挑一件衣服，一键看上身效果，项目已经上线，问题是衣柜太空了。

打开首页，一共就4件衣服。

，时长00:15

<video src="https://mpvideo.qpic.cn/0bc3tqdjqaag44aejnn5ofvfnhgdtcoangaa.f10002.mp4?dis_k=68659c482cc9604d0a02dc4b6293b5cc&amp;dis_t=1791020892&amp;play_scene=10120&amp;auth_info=Epj024kJFH9GvL2+olwNTURcIDoRV09zInpfZUlfZF0sIzoeRiEPMjF/axg3NgBtUFY=&amp;auth_key=38444e4fa324b3ea3aced1a5161ed322&amp;vid=wxv_4716147572732706817&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

好在我手里还有一个NAS相册，存了这些天保存的衣服图片。不过，里面混着聊天截图、文档各种杂七杂八的东西。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/0hd8MxUumHNZK5oVPG9g5rRDLt8uBicU2c5UwqlnFmD4Sd5D0YSvd49ejPUmRnE7QRwicKBXicVnqL0BzNGBQhBrKY9CUxgzX5WgPuP7SHhYibM/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=2)

4000多张图片，首先需要把服装照片筛选出来，但是这个工作量可就大了去了。

我一想，这个筛选工作完全可以交给Flash级别的模型来做。

于是，我要求：

> 接手服务器上的 tryon-shop，从相册里筛出至少100件不同的衣服，去重、建档、上架，让首页从「四件样衣」变成一个真正能逛的衣橱。同一件衣服的不同角度只能算一件，不许拿重复照片凑数。

这是个很典型的真实工程活。

代码虽然是现成的，模型需要先读懂再修改，素材也是乱的，需要先认出哪张是衣服、哪几张其实是同一件。

先给大家看模型的产出结果，最终是这样的：

，时长00:19

<video src="https://mpvideo.qpic.cn/0bc3vaap6aaahqacgdn3mjvfbkgd76uab7ya.f10002.mp4?dis_k=416c44c2b2f787f8850e61058edb007b&amp;dis_t=1791020892&amp;play_scene=10120&amp;auth_info=QPnu1bkAFClL6+q08g0IQ0pbcmYZA08kcChbMkcIOQx+Jm4fRCgPZDwoPBJnZwVjXlE=&amp;auth_key=6978b228f893fcc9d9e0f05e19f8de35&amp;vid=wxv_4716147988421984258&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

我要的是至少 100 件衣服，改造后的首页真的给我补全了。分类标签也有了数字：上装 51、套装 45、裙装 36、裤装 23。每页 24 件，一共 8 页，非常完美。每件还配了中文名和品类角标。

M3.1是怎么完成的呢？

这 4000 多张图，模型先把照片压成缩略图，然后每200张拼成一张 20×10 的「联系表」，再把这些表分给一批子 Agent分头去看。

**前前后后，它一共派出去 30 个子 Agent。**

，时长00:04

<video src="https://mpvideo.qpic.cn/0bc37mc4maafk4abve565vvfl66dy35qlrqa.f10002.mp4?dis_k=890f2ff46b2b8fa831a36a343f40aab8&amp;dis_t=1791020892&amp;play_scene=10120&amp;auth_info=EcPGoLgNEixNue+ypl1cFkoKdWYSBx5ycHhYM0wLaV4vdztFSCAJYTp6ORQzN1E2XgA=&amp;auth_key=0ee5d5248907d6bca855b40d60536ea6&amp;vid=wxv_4716148387266691073&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

每个子 Agent 只盯自己手里那几张表：哪一格是衣服，是上装还是套装，看完把结果交回主 Agent。

主 Agent 负责汇总、去重。

当然，看图只是前半截，后半截是实打实的代码活。

为了让网站兼容这些图片，它在原项目里补了一套批量导入：新增导入脚本和后台接口，每批 25 件自动拆开，还做了重复图片的去重。

除此之外，M3.1还在首页做了搜索、分类、分页的功能。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/0hd8MxUumHPPMNXDdBPdiaTRFpnYkRkFibTQlfZzy23RzAfR3OmKwkSHh1O2f8o66fxQjlu74JR6QFtoVemjVicAZJPu76F41e0xdgln3px5Y0/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=3)

非常实用，系统用起来也没什么特明显的bug。

接手复杂代码考的是细心。下一个任务，考验眼睛。

## ◈二、多模态：看懂一段机器人做饭的视频

前面筛衣服，它看的是一张张静态照片。这一次，换成连续的视频。

视频比照片多了一个维度：时间。

视频相对就更难一点。机器人采回来的视频，要有人一段段标记清楚：哪一秒拿起了什么，哪只手在动，这一步到底做成没有。

这是具身智能团队每天都在干的苦活。我找了斯坦福 Mobile ALOHA 的官方演示视频：机器人自己做一盘虾，77 秒，一镜到底。

，时长01:17

<video src="https://mpvideo.qpic.cn/0bc3ryacqaaageapjzf3qnvfbdwdfchaakaa.f10002.mp4?dis_k=15bb804f1ce6fb975fb6b24847b70071&amp;dis_t=1791020892&amp;play_scene=10120&amp;auth_info=QIqyrtMCQChH773goVwLQhQOLWkUUB13JCtfP0taP1l+Jm5MQSxbZTAsa0Y0NgZiAAQ=&amp;auth_key=12832baf2393c91baf9231792331ca2e&amp;vid=wxv_4716148709254676480&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

我要求：

> 完整看完这段视频，按实际动作变化拆解，每一段写清底座、左臂、右臂各自在干什么，物体处于什么状态。标出加油、放虾、拿铲、翻虾、倒入碗等事件；视频里没看清的写「无法确认」，不许补全。

M3.1 交回来的是一张 Excel：

，时长00:14

<video src="https://mpvideo.qpic.cn/0bc3leeduaaixeaon5ftdrvfqwodhjmqqoqa.f10002.mp4?dis_k=2f57349cf950e9f80022e1388737de1e&amp;dis_t=1791020892&amp;play_scene=10120&amp;auth_info=FKfz7uVUF31M67Dl9gZbRBdVcmYRBk1zIyhYP0dablkqc2gYQn8MMDsoZkNjbFZkA18=&amp;auth_key=c86866777a0a3bbdb462f88820aed652&amp;vid=wxv_4716149266241028096&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

时间码表拆得很细。每一行都分开写了机器人底座、左臂、右臂各自的动作。

单看右臂，几乎每一格都写着「收拢待机」。

加油、放虾这几步，都是左臂一只手干完的。

这种细节，我们只看视频很容易滑过去，但一拆成表格就藏不住了。

表格最后，它还单独列了一页「关键事件」：加油、放虾、翻虾、倒进碗……

每件事从第几秒到第几秒，一眼就能找到。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/0hd8MxUumHNTYU8Atfiah9UPZ9ZlRRH76uibJs0QKqVz2GUObPDFFStefT7FUZJblrWbAOgXPRicKh8jA7W9d98KthvP54sY71zRDFs2sb9nDk/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=4)

最有意思的是标粉的两行。一行是「翻虾」，它写的是：没看到，没法确认。

视频里虾始终没离开过锅面，它就不说翻过了。

另一行是「把锅放回灶上」，它写的是：没发生。锅最后被放在了台面上。

**对标注数据来说，一格诚实的「无法确认」，比十格编出来的「是」更值钱。**

接着，我让它把这张表做成一个能拖、能回放的网页。

> 基于时间码表，做一个单文件、离线可打开的「Cook Shrimp 任务回放台」。左边视频，右边事件时间轴，拖动时视频、关键帧、事件卡同步；四个任务阶段用不同颜色标出，无法确认的阶段显示灰色。不要伪造机器人控制器。

，时长00:30

<video src="https://mpvideo.qpic.cn/0b2ejqabsaaawaaml2v3nzvfatgddfgaagia.f10002.mp4?dis_k=00ffa5899506043e3837d7f8057dad1d&amp;dis_t=1791020892&amp;play_scene=10120&amp;auth_info=EdaSwocGRCwe6rG/qQpeQkJYJzsSDkx2Ii4NP09YagovcmgZQClfYWkpZxk8YFNiVlI=&amp;auth_key=213cfc6bc6e512d098b2aa7e248480f2&amp;vid=wxv_4716149738956341249&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

页面左边播视频，右边是一条四色进度带，对应准备、翻面、移动、倒入碗四个阶段。「翻面」那一段是灰色的，还打了个问号，因为前面那张表里，它就没能确认。

视频往前播，右边的事件卡跟着一张张亮起来。每张卡都附了一行「无法确认」，写清这一步哪里看不清。

回放台把表格里的每一格诚实，原样搬进了交互里。

## ◈三、数据可视化：城市在夜里亮起来了吗

前两个任务，输入都是人眼能直接看懂的照片和视频。

这一次，我给它的是一堆人眼看不懂的数字。

同一片北京，我要求模型把 2015 年 11 月和 2020 年 11 月的两份卫星夜光栅格做一个对比。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/0hd8MxUumHOoo2l6APakhIhByicYkJl3h9SDgliaSIrcbEFAqDSKCy66bhdjKINft3lzbSkxRqLNe5icP3drG7LEE6CdPEUOHK6DBxqq6VWcHg/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=5)

我要求：

> 先读文件、出数据质量报告，再做一个离线单页，标题叫「城市在夜里亮起来了吗？」。把夜光栅格抬成一块 3D 地形，拖动年份就能看到北京在夜里怎么亮起来；支持左右对比、拖动擦除和变化图三种模式。

，时长00:15

<video src="https://mpvideo.qpic.cn/0bc3jubxaaadlmak255yajvfgtodobgqg4aa.f10002.mp4?dis_k=0024ddc6829ffe2f195ef63ed6224ada&amp;dis_t=1791020892&amp;play_scene=10120&amp;auth_info=RN/bw7AHEH4bu+qwqA1XEhQJJjgQD0okIC9YYhtbb1x6dz0cQCkLM2x4PBY9Z1oyAAM=&amp;auth_key=8afe7d7f65cf0205425a78586288c287&amp;vid=wxv_4716150164108115968&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

页面打开，一条竖线从左往右扫过去，线左边是2015，右边是2020。线扫过的地方，城区的光斑一下子铺开。

地图上还叠了一层北京的城市骨架：二环到六环、中关村、奥林匹克公园、天安门、CBD、首都机场，左下角有一个小地图，用橙框标出当前裁剪的范围。

看起来非常清晰。

## ◈四、金融：一个市场观测台

最后是金融场景。

我要求：

> 用本地的 A 股数据做一个「市场天气台」。先检查数据是否新鲜、字段是否齐全，再做页面。从市场宽度、波动、回撤、板块轮动一路点到单只股票，每个数字都要能说清怎么算的。数据过期就不许写「今日行情」，不给任何买卖建议。

，时长00:19

<video src="https://mpvideo.qpic.cn/0bc3keaciaaaniapsgv3szvfauoderiqajaa.f10002.mp4?dis_k=a55404fee4e57da2ef08baae3b55a076&amp;dis_t=1791020892&amp;play_scene=10120&amp;auth_info=EdPnxNEHF35P6+/j9QsLQUUIdWxEUE95JHgKYkwPaFsvJm5LESwMMzgoOUVgYQZhUQI=&amp;auth_key=04b52fbcfc41fa7532ce2efb06d1975e&amp;vid=wxv_4716150792716812289&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

页面最顶上一行，先交代数据本身：数据截止2026年9月28日，标的4603只。

下面是四张卡片。

市场宽度：当天中位数收益 −1.71%，805只涨、3687只跌、100只平。

往下是一张「行业地图」。103 个行业，每个是一个圆点：越往右，最近一个月涨得越多；越往上，价格起伏越大。点哪个行业，哪个就亮起来。图下面还特意写了一句：右上角不等于「值得买」。

点进一个行业，比如林业，能看到它不同时间段的涨幅：近三个月涨了两成多，最近一个月却几乎没动。一眼就知道，这一波涨是之前的事了。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/0hd8MxUumHMQZpwazvBU2PO5hLHuqApkKl3pOqlzR5kJzQ5uhnhEFlltyBbv8IL3rWHymVMaaN6nfv6WJgp56WHRfwSz6OvjfheGpPMoGTE/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=6)

再点一层，就是这个行业里的每一只股票，点哪只都能看它的 K 线。

## ◈五、速度与成本

跑完 M3.1，我们把同样的 prompt 原样交给 DeepSeek V4.1 Flash 和 GLM-5.3-Flash，各跑一遍。

试衣那个任务没放进对比，先看用时：

![图片](https://mmbiz.qpic.cn/mmbiz_png/0hd8MxUumHOE2Aibquyna7PUFJDa1UzGArfSu843RvhGib5rZgNZMeRxqOvsfmYkzGd0U8dbI3m10OficSB371lJI0ZrerwpZWmp9C6yqRCRrk/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=7)

单看用时，DeepSeek 最快，四项里拿了三个第一；GLM 最慢，北京夜光跑了一个半小时，最后也没把页面交出来。

不过三家都是几个任务同时开跑，用时里还混着跑命令、开浏览器、截图的时间，只能看个大概。

**成品质量上，差距很小。**

做虾视频，三家都拆出了带时间码的动作表，思路差不多。在最难判断的「翻虾」上，M3.1和DeepSeek标成了无法确认，GLM 则给出了翻面的判断。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/0hd8MxUumHMPZa6qNmbronAH5lGy2HUq7X7rsKNJ6RWctChaiajPQ5GlcRgR3kxARGpqpzYibwC2BV20iatEEib6WibKcgv0RQF73uexw4Kc6q6g/640?wx_fmt=gif&from=appmsg#imgIndex=8)

北京夜光，M3.1 和 DeepSeek 算出来的变亮比例都是 27.6%，数据完全对得上。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0hd8MxUumHOGFicrq1icshLd5VX4ZMQFul8Ex7BWGxFD9UQBjH2ILaaSt3Y24bQyuuxuKgGCz4iaiaf6BIs02XI8P7MvuyCmicUzP7IXRSeu7wuo/640?wx_fmt=jpeg&from=appmsg&watermark=1#imgIndex=9)

回放台三家都做出了能拖、能回放的页面，交互也差不多，M3.1 的页面更简洁一些。

A 股观测台，三家都做到了先查数据、再出页面，各有各的细节。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/0hd8MxUumHPNwgFNCqsgS6nSdMfzowV8talwRyZAgJiaa2Rs5lQX278DskKDhFwu7Zg5A7N0ibrlLJ7gpEmccJeAX4mxu8F20IwbKPO0hqzia0/640?wx_fmt=jpeg&from=appmsg&watermark=1#imgIndex=10)

再看花费。

DeepSeek 这一批花了约 10 元，GLM 约 21 元。M3.1 用的是 Max 档 Token Plan，每月 119 元，一个下午用掉周额度的 10% 左右，折下来不到 3 元。

需要说明的是，GLM 这边走的是智谱官方 API 按量计费；如果换成智谱的 Coding Plan 包月套餐，同样的活会划算很多。

价格方面，M3.1 目前只能走 MiniMax Code 和 Token Plan，官方没有公布 API 单价。作为参照，上一代 M3 的 API 价格是每百万输入 0.3 美元、输出 1.2 美元。

![图片](https://mmbiz.qpic.cn/mmbiz_png/0hd8MxUumHNBOEq5EgcZXLFkqlbwJOuMnOALuw0sBk2j64C2V2iaStKy8LuQHY4bXc9aju4mV6ibwW6wumgvuHOS8NnDpFuqH3wtLIoODGcibQ/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=11)

速度方面，直接说结论：这批任务里 DeepSeek 最快，M3.1 次之，GLM 最慢。M3.1 在 A 股观测台上是三家里最快的，其余三项排在 DeepSeek 后面。

把这几个成品放在一起看，M3.1的智力未必顶尖，但作为一个 Flash 档的干活模型， **DeepSeek V4.1 Flash 这回，又多了一个对手。**

![图片](https://mmbiz.qpic.cn/mmbiz_png/5fknb41ib9qEyDKnkjcT4bd38ljNdEGscMzUYibunoJ8KWC3aUv6EUpdes1rbU2Kp7TQXqFwMicLuciaz9q7tiaI3UQ/640?wx_fmt=png&from=appmsg#imgIndex=12)