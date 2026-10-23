---
title: "Qwen3.8-Flash发布，新斩杀线！熬夜爆肝实测一天，夯爆了还是拉完了？"
source: "https://mp.weixin.qq.com/s/tm47dTXZB0QP3DqjjzgLzA"
author:
  - "[[小林coding]]"
published:
created: 2026-10-23
description:
tags:
  - "clippings"
---
小林coding 小林coding *2026年8月27日 21:37*

大家好，我是小林。

就在昨晚，阿里发布了 Qwen3.8-Flash。

而且这次依旧开源，对应的开源权重叫 Qwen3.8-Flash-Next。这里的 Next，指的是一套全新的模型架构，未来的 Qwen4 也会沿用。简单来说，阿里这次提前把 Qwen4 的底子放出来了。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX1IiaKqXw30Nr7rAFOLb5Z1oDA5rnfGZTRjkdNVLJyibARSRGVJ6bEgnKey7jkiceahP5ta6mbSOUZGibmF8wAvShXSIL6E6AJxubo/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

Qwen3.8-Flash 的主模型有 125B 参数，但每次生成 Token，真正参与计算的只有 6B 参数。

你没看错，就是 6B。

这里容易误解，不是说整个模型只有 6B，而是它每次回答问题，只需要调动其中 6B 参数参与计算。参与计算的参数少了，生成的速度会更快，成本也能降下来。

另外，Qwen3.8-Flash 原生支持 262K 上下文，可以扩展到 1M，还具备多模态能力。

只激活 6B，能力会不会跟着缩水？

官方给出的答案有点猛。在多项编程、专业工作和多模态评测中，Qwen3.8-Flash 已经超过 Opus 4.6，整体表现开始逼近 Opus 4.8。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX3iaN1lvHEtNFqzsf6hUEoDXRg6xib9RI749I9gDv2Liaib0FQnIeJg6dYl1TboMfz6w1p5XK5EQxp8pHE3relu8I3W8ThktBic5FF4/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

具体来看，测试智能体编程能力的 SWE-bench Pro，Qwen3.8-Flash 比 Opus 4.6 高了 9.1 分。在专业工作任务 JobBench 中，Qwen3.8-Flash 比 Opus 4.6 高出接近 20 分。

讲真，一个每次只激活 6B 参数的模型，性能却能摸到 Opus 4.8 这个位置，确实有点离谱。

最关键的是价格。

Qwen3.8-Flash 的价格，比Opus4.6 便宜超过 97.5%！

Qwen3.8-Flash 每百万 Token 输入只要 0.8 元，输出只要 2.7 元，甚至比 DeepSeek-V4-Flash 高峰时段的三分之一还低。

而且 Qwen3.8-Flash 每百万 Token 的缓存命中价格，低至 0.1 元。

看明白了吗？这么一看，Qwen3.8-Flash 能力够强，调用成本也足够低。

这一次，大模型的新「斩杀线」，又被 Qwen 往下压了一截。

为此，小林我也爆肝实测了一晚上，我是在 Qoder 上测试的，目前已经可以用 Qwen3.8-Flash 模型了。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX0c16LwCtcUapUqUfJBBKCfC9W95iawZldpibS4UJBC0q3cJchBYphqlFZmficqZgNZlibbZBTE2TPywgyqARLiae2zUY75nia5ibiaefs/640?wx_fmt=png&from=appmsg#imgIndex=2)

接下来一起看看，Qwen3.8-Flash 的实际表现到底怎么样？

## ────实测 Qwen3.8-Flash────

### 01｜飞机大战游戏

相信飞机大战是很多人的童年游戏了，所以第一个测试，我就让 Qwen3.8-Flash 做一个飞机大战小游戏，回顾一下童年。

我写的提示词也很简单，整个需求只有几句话。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX2J0A7maG47JTiaeDIcjmrzQuHFfKxicq4xlxo3MCLyd8OY6ialKR8EiarlCFx4WiaGMiaicBTxyxyc2Tfo6eoT7wmh1wg8AkF0DMBVvg/640?wx_fmt=png&from=appmsg#imgIndex=3)

一轮对话之后，游戏就做出来了。先看页面效果，整体完成度还是挺高的。霓虹风格很统一，开场界面和游戏界面该有的信息也都有，没有那种临时拼出来的粗糙感。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX36ibzic0H6iaRFVjhHoGB7Tib68WjNh964IlialtL3ibkCOz5KxbDfdx44aUFbLxXDqP2qTSaTDk8UqgQPr62gnzV4YzY0ZdMibibybk0/640?wx_fmt=png&from=appmsg#imgIndex=4)

更重要的是，这个游戏不只是能打开，而是真的能玩。操作起来还是很丝滑，三种武器切换也很自然，而且每种武器的弹道、特效和玩法都有明显区别。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX1gHfQ7oIuujp4vyicibba94QYxBiauoXXr0UNAeWiaKDIickYOwHl9SvYpMk5XeNZaYtvZ6GrMiaUNvq6ZeCfbwCbUTibkYFvicPFtJibU/640?wx_fmt=gif&from=appmsg#imgIndex=5)

比较让我惊喜的是，这些武器的具体效果，我在提示词里都没有说明，是 Qwen3.8-Flash 自己设计出来的。

它还补上了击杀掉落 Buff、武器升级、连击和分数倍率。吃到 Buff 之后，火力提升很明显，游戏的正反馈做得不错。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX1gO2OqKdibTwXFiadc7qOhvCfZnZLs1eO7NjowPokib9S53wkbvldHDgZAEmEcm8bOPaVfEuOgZJmHHzk2W1tR5C0ibdusXy9rLq8/640?wx_fmt=gif&from=appmsg#imgIndex=6)

大约一分钟后，Boss 正常登场，而且难度还不低。我本来想顺手录个通关画面，结果打了半天还是没过去，看来游戏没问题，菜的是我。

，时长00:56

<video src="https://mpvideo.qpic.cn/0bc3zqbmoaacdyabcqunvjvfftgdy7gafrya.f10002.mp4?dis_k=9fdc399535672637cf62ab87a2b20ce5&amp;dis_t=1792736732&amp;play_scene=10120&amp;auth_info=ALrOqZFVPgRNypKfinR1a15+bRZVRXtzZxY9TxZwC3w+Jh1NIF9jay9mGTBmVmJRVA==&amp;auth_key=7a2c223207d5b6ca38145ed71039682b&amp;vid=wxv_4667744743643381765&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

这一项测试，我对 Qwen3.8-Flash 做出来的效果还是很满意的。

一次对话，它就把画面、操作和游戏玩法都做完整了。提示词里没有说清楚的细节，它也主动补了进去，最后交付的不是一个只能看的页面，而是一款完整可玩的小游戏。

### 02｜八足蜘蛛运动轨迹

第二个测试，是很多模型都会翻车的「八足蜘蛛运动轨迹」。

这类案例最难的就是八条腿的配合，稍微处理不好，走起来就会像八条腿各玩各的。

结果 Qwen3.8-Flash 一轮生成之后，我打开之后的第一反应就是：卧 x，这么强的吗？

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX1RQKw6SxUA6hE5OGxB38CEC4ibCkNtTWBbHHibhrac00YrvG3JVWZgnkKfcjibSFwK3dyVojSRQahLIaxibOaoRw1qvZEzk2c0zVY/640?wx_fmt=gif&from=appmsg#imgIndex=7)

八条腿会分成两组交替支撑，遇到起伏的地形，脚能稳稳踩住，身体也会跟着地面上下调整，整个运动过程非常自然。

为什么我反应这么大？因为这个案例，我之前也用 ChatGPT 5.6 Sol 测试过。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX0Oa778q7tmU3D2AAXpAUZad44DADZUXMnWZibTMH6T7RJicfxGee18414PxKmhF0ibNaAUko4N2nS0CicXeubzbCj0ZSwOicP62tlo/640?wx_fmt=gif&from=appmsg#imgIndex=8)

两段效果放在一起看，Qwen3.8-Flash 已经非常接近 ChatGPT 5.6 Sol 了，甚至蜘蛛外形和地形适应这些细节，我感觉还更精致一点。

要知道，Qwen3.8-Flash 只是一款 Flash 模型，能和 GPT 5.6 Sol 做到这个程度，确实有点超出我的预期。

再看看 DeepSeek-V4-Flash 的效果。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX3BXHKP2JefW8pCPrMic0fj6wR80Vb8zico8Fk80Oy1uErqTAof8icxZa2xibJic51zozbmDUtq5pg0kWlb9cgksH14r9nM2dMVLZw8/640?wx_fmt=gif&from=appmsg#imgIndex=9)

DeepSeek 生成的蜘蛛，八条腿看起来会僵一些，身体也有种贴着地面滑过去的感觉。对比之下，更能看出 Qwen3.8-Flash 对八条腿协调运动的处理有多好。

这一轮测试，Qwen3.8-Flash 给我的惊喜挺大。它不仅把蜘蛛做出来了，还处理好了八条腿的配合、身体重心和地形变化。作为一款 Flash 模型，这个效果确实很强。

### 03｜3D 游戏

第三个挑战，直接把难度拉到 3D。

我先让 Qwen3.8-Flash 做了一个 3D 魔方模拟器。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX3nrHTVaJGtg57y7tk6BK8yialo7xBrTqTz8x30tFBbePxEvj2ajLMY2Xq92FRTxE4nDp4aibgVJhjWJmz69IuVISVzVUOicVqcGc/640?wx_fmt=png&from=appmsg#imgIndex=10)

一轮生成之后，魔方不仅可以自由旋转视角，还能直接拖动色块。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX1CsI2ic7LERxg0dE1Nuxv40oicOicibYsibEtvcK7ianeOBszptgNjaibMBk91bpotsdDrgU5IfzOvIQoLzYNdrFsgibjnDZsgWZm2x4Q/640?wx_fmt=gif&from=appmsg#imgIndex=11)

顺时针、逆时针和 180 度旋转都可以自己选择。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX0BoHSZEicBankeyJddMhmS8Nu86cemyAl9dUzz11iaLBW9W1tnxwT5VIHztNHWdpQ1gcSSxh3fiafjLTkE2CTyw80Dbsyl5HGvQU/640?wx_fmt=gif&from=appmsg#imgIndex=12)

把魔方彻底打乱之后，点击自动复原，它也能一步步正确还原。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX3iamiakq8Bd9gsaeTQhqFrvtFF2b3kDujDQ7eJYrcgwicWDIrCibV7X2dYZNzS5Mtib8aJto11t88eVAegmhftfhgt53rvH2URTD8Y/640?wx_fmt=gif&from=appmsg#imgIndex=13)

这个结果让我挺满意。3D 魔方最容易出问题的地方，就是转着转着色块状态乱了，或者操作方式没做完整，但 Qwen3.8-Flash 这一版都正常实现了。

我之前也用相同的提示词测试过其他模型。目前一轮对话生成的版本里，Qwen3.8-Flash 是我体验最好的。

比如 GPT 5.6 Sol 生成的版本，只能通过右侧面板转动魔方，不能直接拖动色块，也不能自定义旋转方向。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX1XRJEVuVShXoLgozvGia291lFpu8MMZibSpqXYB7ia3I9EwLP30icIS0icT98wfXbq4GLRkRYtPQHJSMW6rP48IusqjVBt4icRPS4yg/640?wx_fmt=gif&from=appmsg#imgIndex=14)

接着，我又让它做了一个 3D 网球游戏。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX15AFmicOwLN7NNYu13nRBBL1iaeSBEqFkxSjL5SYEz1d9Lh02eT2yuWXFT5A72XQkIlJJibSy9cmwJHbFiajkMrbcA2x3xGPUcib8E/640?wx_fmt=png&from=appmsg#imgIndex=15)

出来的场景还挺大，球场、海边、棕榈树和观众席全都有

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX1zd5hJzqNc4G0Au5mPNhlVksYYaEhfVzZC4IibfkLmLy9iaSkRqYQP6AAuXuu8f8b0bLAiaHgxzfwClDzWicSXD6T4dKicxo6WfUiaI/640?wx_fmt=png&from=appmsg#imgIndex=16)

这个游戏也是完整可玩的。可以正常发球、击球，球出界之后，系统也会把分数判给对方。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX3GddUsPJOWQVV9eqZVALvJKCOkbRhmib3rPIMfdvI3e0IJoozeQ93QwjNMhVqQyty7OIvZXpKzRgwHadO6WvlYauIxLMr05LaI/640?wx_fmt=gif&from=appmsg#imgIndex=17)

注意看，场外的观众和天空中的海鸥也不是静止的，细节完成度还不错。

而且游戏的平击、上旋和削球三种击球方式都做出来了

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX0o1lVWkVuiavd7CScKGEJdAjALqjzSL1TesV5bplW68Exu4MIEdQMUicugvPelKVGzJibgX1f1Zicp4pkTDPtkvY81f7pMR9x6YDY/640?wx_fmt=png&from=appmsg#imgIndex=18)

我完整玩了一局，和 NPC 打得有来有回。最后比分来到 6 比 6，我没控制好力度，把球打出了界外，直接输掉了比赛。看来我的游戏水平确实还得练练。

，时长01:54

<video src="https://mpvideo.qpic.cn/0b2ej4af6aaa2uaitx4pibvfat6dl5hqaxya.f10002.mp4?dis_k=40459a488628a668388ee1aae5154cbf&amp;dis_t=1792736732&amp;play_scene=10120&amp;auth_info=BLee1o4GblJHkp+SgXdxZA1+aBkFG3UkY0VkGRJ3WHs6JhoeLQkzPSU+FD1tVWZeBw==&amp;auth_key=5495826613389ca2af0e8c98192db1d3&amp;vid=wxv_4667743810091663362&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

最后，我还测试了一个实时 3D 角色控制网页。角色可以行走、奔跑、攻击和格挡。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX1ibI0AoMfu8GAINH0DQvN0H6TQtb3qUFbdbAKOgJOhdhib1wxndjSM068LJe7Wq9WAaB7pP2nOc9XguezRNa1Yibq6aYjgdU1FCs/640?wx_fmt=gif&from=appmsg#imgIndex=19)

也能切换不同的武器。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX34rEQuGrF4slC3wMTshOe7hUylgzPOIg1ICY44cAgpSyBpSibrqxvMlmmQlMasy79ic22icj3ic4hahwtcrC4F9wqrQljStc9icB4I/640?wx_fmt=gif&from=appmsg#imgIndex=20)

查看骨骼效果也是 ok。虽然人物长得有点抽象，但功能确实都做出来了。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX0GcBO18mrlVg2ySBvh3QCXqt1YQ2xyibHKjRaTpXrQpibpD6xCw1HtIrjib9TwiaMLRFarz5zNfVub9VmnhdWibyEbBS5LfG4ibmuRI/640?wx_fmt=gif&from=appmsg#imgIndex=21)

这一轮挑战，Qwen3.8-Flash 连续做了三个不同的 3D 项目，核心功能都实现了，实测过程中也没有遇到明显的 Bug。

尤其是 3D 魔方和网球游戏，不光页面能展示，里面的交互和规则也能正常运行。作为一款 Flash 模型，这个 3D 开发能力算很强的了。

### 04｜电影级动效网页

游戏测试完，我又给 Qwen3.8-Flash 上了一点视觉压力，让它做一个电影感的模型发布网站。

提示词确实比前面长一些，我要求它用连续的镜头运动、巨型文字、动态数字和粒子效果，把整个网页做成一部可以滚动播放的数字电影。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX2leO69ic0icSBlP3lno0SuoiaqHW5tPFAnNib6aQxibDxCujdtU0gBvGHd9Ccqico2dZDLYlRAdvClibXeKBaKMOrvtvG51Zp6MDmvJA/640?wx_fmt=gif&from=appmsg#imgIndex=22)

成品打开之后，第一眼还挺震撼。整个页面以黑色和冷蓝色为主，大量粒子、光线和文字会随着滚动不断重组，视觉风格非常统一。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX1tqINcDNlkA9Qia8Qlvxvib55blwDMiaYCEjicibdBkGjrfyzGKCicGM2bufWVicvT07UHy7cOr2riaPgjLic5UxUZibw2J7QYJVWzKDGcU/640?wx_fmt=png&from=appmsg#imgIndex=23)

尤其是大标题出现的时候，粒子会跟着聚拢和散开，再配上缓慢推进的镜头，确实有一种科技发布片的感觉。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX0tuGLEurXKE1tN2FN5SayVqzJFaaJvcYyNTQbEQYw4slUeMcPNV5Aia8tAJibsrYGEGxEchEKXVWviaUvDHZ4jSibNfeVTpgjHib7c/640?wx_fmt=png&from=appmsg#imgIndex=24)

而且它做的内容量还挺大，不是滚动几下就结束。我已经在快速往下滑了，完整动画依然播放了接近一分钟。

，时长00:59

<video src="https://mpvideo.qpic.cn/0b2e2iah6aaawyakt5upcjvfbuwdp7jaa7ya.f10002.mp4?dis_k=6b754fdf88900419172b6d58316e1ecb&amp;dis_t=1792736732&amp;play_scene=10120&amp;auth_info=UsaY4lE4UEvHzc7feXtlXHhqEA8SenNkQmFNT3FYeGt0HRt7D2U/KWtGYTNbbF9W&amp;auth_key=ef337efd02d7429e7425f762f4753492&amp;vid=wxv_4667742903887216641&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

这一个任务最让我满意的，就是它没有只做一个好看的首屏，而是把多个章节和转场全部串了起来，滚动过程中也没有明显卡顿。

这个效果直接放到产品发布会的大屏上，我觉得都能撑得住场面。

### 05｜ 解决真实需求

最后一个测试，我把 Qwen3.8-Flash 直接放进了小林简历（jianli.xiaolinnote.com）的真实代码仓库。

前几天，有读者反馈简历编辑器的列表只支持一种黑色圆点，希望子层级能像 Word 一样显示不同符号。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX1Io5H9MGqYrwo99ibcZRib5Nw3hW1FXgvpnVlNyWNZ1bvrKUvj5BWyxicencdDaf9RY9ETiaK8uMiceVzjFvY4GWp5lFiaibME8PdhC8/640?wx_fmt=png&from=appmsg#imgIndex=25)

小林简历的代码文件不少，我没有告诉 Qwen3.8-Flash 应该修改哪个文件，也没有描述具体的实现方式。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX3RfhqSiapUwwxaSibQ5YS4sjicVptoaWJVX9GlXM3NWSV1FjxDVmMuxwJRo3IHrz1pVRF7dU9aZ1nIeSSz3KPHFl1QBNGojTe2JU/640?wx_fmt=png&from=appmsg#imgIndex=26)

我只把读者反馈的截图丢给它，然后说了一句：「修复一下这个问题。」

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX17hS7WQjOSRhYteWicf2Fibyz6VKgF1UQlLhNRlmxnScxC7Tk6VUrvode14DuCZWvMqU3rqA0BZWF5VaUIPPab3bCamypES4zSM/640?wx_fmt=png&from=appmsg#imgIndex=27)

接下来，它自己找到对应代码，完成修改，运行项目，再打开浏览器检查效果。

注意，提交任务之后我没有再介入，浏览器也是它自己打开验证的。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX2khicR4GcKgkDZVNxFfbaD7dTBvfjOudichylOSDibzyS82sr1DKSZ5JErwqBefvq1y4BcvwY20yrFJygYGCDUTFccc4YxPgaAA0/640?wx_fmt=gif&from=appmsg#imgIndex=28)

一轮任务结束，简历编辑器已经支持多层级列表。

第一层是实心圆点，第二层会自动切换成空心圆点，简历预览里的效果也同步更新了。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX2m9ibliapBynqjf3usS1UlQvUMY4p92nUXibqErBWxqJBiaY5qhTkuKyPBwEwBs9RXgVtgffpxeh9uOBtv3dDOKTzozRD6LicX8vog/640?wx_fmt=gif&from=appmsg#imgIndex=29)

只给一张反馈截图，它就能自己找代码、修改、运行和验证，最后把需求完整交出来。整个过程已经形成了一个完整的任务闭环。

这一下，确实有 Agent 那味了。

## ────写在最后────

这一轮测下来，Qwen3.8-Flash 的表现确实超过了我的预期。

从 2D 游戏、八足蜘蛛、3D 场景，到电影感网页，最后再把它放进小林简历的真实代码仓库，它都把任务接住了。

尤其是最后一个需求。

我只给了它一张读者反馈的截图，没有告诉它应该修改哪个文件。它自己找到代码、完成修改、运行项目，再打开浏览器检查效果，一轮就把需求解决了。

这个过程给我的感受很直接，Qwen3.8-Flash 虽然不是旗舰型号，但旗舰模型能干的活，它已经能接住不少。价格还低了一大截，跑这种需要多轮调用的 Agent 任务，优势会更加明显。

以后选模型，估计不能只盯着谁的跑分最高了。谁能用更低的成本，把任务完整交出来，可能更值得关注。

所以你要问我，这次大模型新的「斩杀线」是谁？

我觉得，Qwen3.8-Flash 已经站上去了。

更有意思的是，Qwen3.8-Flash-Next 只是 Qwen4 新架构的一次提前预演。

一个预演版本已经能做到这个程度，未来 Qwen4 的表现，确实值得期待。

AI 编程实战 · 目录