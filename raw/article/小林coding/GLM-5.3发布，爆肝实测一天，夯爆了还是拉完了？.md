---
title: "GLM-5.3发布，爆肝实测一天，夯爆了还是拉完了？"
source: "https://mp.weixin.qq.com/s/OlR4YBJnZChkevspCUZqHQ"
author:
  - "[[小林coding]]"
published:
created: 2026-10-23
description:
tags:
  - "clippings"
---
小林coding 小林coding *2026年8月19日 14:32*

大家好，我是小林。

GLM-5.3 这次有多猛？先看一张刚更新的榜单。

Artificial Analysis 把编程、Agent 长任务、科学推理、复杂问答等 9 套测试揉在一起，做成了一张模型「综合卷」。GLM-5.3 拿到 60 分，前面就是 61 分的 GPT-5.6 Sol 和 62 分的 Claude Fable 5。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX0xiaDuibTXNicpF2VcTMJiaEl9eibX0BQOWP24WwdZ4QE4gOIuHed2Yct9wcmRYbtGBsU4jMZE5FxK8bGj8xMicME17Z8HE0NDUqmHY/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

怎么说呢，基本已经挤到一张桌子上了。开源模型里，GLM-5.3 还和 Kimi K3 并列第一。

但真正让我眼前一亮的，还是下面这张成本图。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX2NxY9vGc6UlxibHQ2Xa3iajfiaEy1nPQiaicibp99K1sticby5qsIftcE4Dj4iaLyq0hyWxAuJj6GqoXnzSg0zGUMPWKeqZAv3W21jZCE/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

GLM-5.3 用更小的参数规模跑到这一档，完成一个任务的平均成本大约是 0.6 美元，Claude Fable 5 则要 3 美元出头。同档能力，账单差了五倍左右，这个就有点狠了。

GLM-5.3 一发布，我立马爆肝一天，实测了一波。

## ────实测3D解密游戏────

下面这段画面是我拿 GLM-5.3 在 ZCode 里从零做的一个等距解谜游戏，风格参考《纪念碑谷》。

，时长00:36

<video src="https://mpvideo.qpic.cn/0bc3xyb2uaadfealtv4g5fvfhpwdvk7ahkqa.f10002.mp4?dis_k=c2ff128905e1ecd1d6e06f8836b1c762&amp;dis_t=1792736783&amp;play_scene=10120&amp;auth_info=dYuZhKMPMWhlgaaW5lpeYWQBLDhrGEE9OlRjMDMHO2ZLK0kCaAVsBwctLTkKeElbbg==&amp;auth_key=d71d6f286e270f8953101960531ef1b1&amp;vid=wxv_4655911123433504770&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

这个解密游戏的难点是要把视错觉做出来。两条路在三维空间里明明是断开的，可视角一转，它们在画面里就接上了，角色也能顺着这条「不存在的路」走过去。可以看到，GLM-5.3 很好的完成了这个任务。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX3YZ3hdu1ic4LZFxG2zaZ05LsADsaWwxmAeUaRJyFviavOAgTldjjibvoiaXxLQFTH7HR5NHkKqt4OtapjUicVdvb2jeyrxwl2OzEaI/640?wx_fmt=gif&from=appmsg#imgIndex=2)

我也把同一份提示词又交给了 Claude Fable 5 和 DeepSeek V4 Pro，你可以先看看三家模型各自的第四关，你们觉得哪一版更好？

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX1X48VgnnUzeQIhiaHfAmbibF1jqlXHRP0cajYzWRcPIPGKMyIEe9mzaM49ngKjN5lH1P8RE3WwIvdBqx0eAPhKbQJjxuhibjw9tE/640?wx_fmt=gif&from=appmsg#imgIndex=3)

GLM-5.3 和 Fable 5 实现出来的成品还是很接近的，游戏都是可玩的，不过，DeepSeek V4 Pro 的差距就比较明显了，画风相对简陋一些。

更关键的是，我要的机关应该在场景里，玩家直接去转动机关，DeepSeek V4 Pro 却把机关变成了屏幕底部的一排按钮。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX0Cw6nVMXBFIhPwto9NXic2LWe2qR5qg9YFLPPG5vn6zGTKZzRcSGwCxstC1JosTASVTU2ns7Fl7uSCOuKcoUibGDmzpIibP6kMxA/640?wx_fmt=gif&from=appmsg#imgIndex=4)

上面是 GLM-5.3，鼠标点的是场景里那个琥珀色把手，转盘转过来，断掉的路就接上了；下面是 DeepSeek V4 Pro 的同一关，场景里点不到东西，得把鼠标挪到屏幕最底下那排按钮上点。

做这个任务的耗时上，Fable 5 是做的最快的，用时 23 分钟；GLM-5.3 则是最慢的，用了 49 分钟；DeepSeek V4 Pro 是 39 分钟。

GLM-5.3 为什么这么慢？我盯着过程看了一遍，发现不少时间都花在模型自己测试、发现问题，再返工重做上。

我看了看代码。这套游戏每次构图时，都会拿当前相机，把能走的格子投影到屏幕上。两块格子的位移只要大致沿着视线方向，屏幕上又恰好隔着一格，寻路图里就会多出一条边。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX3NicBrGNicZsg2siaNyLJZtPsBmwJmIUWjMtBpWcg588JThj6CKpZLEv8dOODM4u40kU3m1qxQiaAvjbaGibsJCT3QbEWaXAFeokgA/640?wx_fmt=png&from=appmsg#imgIndex=5)

整个过程我只发了一次提示词，中间一次都没插手。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX0W3CDSrnFEEga1w7mqIq63IV7YJhU9wwibVZ3FfSw1hHNjyFOlksich5D1Te3EhfaHbtsnPIZaTuAmC8Yf3ethWFyzicXlOBdgL0/640?wx_fmt=png&from=appmsg#imgIndex=6)

GLM-5.3 在开发过程中，会自己验证哪里不对，持续去改进，这一点就让人感觉安全感很足。

比如 GLM-5.3 自己起了 dev server，在 ZCode 内置的浏览器里点格子验证，点着点着发现命中的老是相邻格，差了大概一格，于是回头做多点探针，把屏幕到格子的映射重新校准了一遍。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX1KMaVJ4xATFBpkK7Uv7rg0BPbCX4sadXicrFl8Ash0k6wu383SF5EINRk4uVyPg4zutyY3pATNOCWFpFBiatKs7yXEXMXoqib8uE/640?wx_fmt=png&from=appmsg#imgIndex=7)

四关里最复杂的是终章，所以这里直接跳到终章看它做到了什么程度。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX2JibesQnJfNDs5NnLv3jp4zVR7y8BMQZqSknibPqq8wKpnEoVR1OnX6HMSQa279It6TN0Lpa2Kxqs2UaaN21icQuUia1UJnC19udM/640?wx_fmt=gif&from=appmsg#imgIndex=8)

终章不仅有错觉接路、转盘、载人升降柱，升上去之后还有第二段错觉，GLM-5.3 完成的还是很不错的。

## ────实测钱包计费系统────

我也给 GLM-5.3 出了一个难题，直接做一套钱包计费系统。

我整理了这个 PRD 文档，一共十个接口的规格、七条业务规则、四个前端页面，再加上验收标准和交付物要求，大概是下面这个样子。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX2LAFRMgpEGSSWqX0RarorrpFBMYSlAmC2vtdpelPRzmGAoLUfpp2EzhdPcpmI5RdwQ1k5WA4DLbfISdkbIvbErNoTdokYbQ8s/640?wx_fmt=gif&from=appmsg#imgIndex=9)

业务规则里写了全是财务和客服口吻的硬性要求，比如余额不能为负、同一个 requestId 只能生效一次、一次资金操作要么全成要么全不成、用户只能看自己的账目。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX0wRk6qChHtJcrerTPSiaLg7ALHwAsn3LJUS32HNN967THsUz6ztPo8CPrTYPIf0j7SfnJkic30Ghe4e7BBrJsPvrqeTDqNgA2r0/640?wx_fmt=png&from=appmsg#imgIndex=10)

钱包系统还有个好处，验收非常直接。账本平不平，算一遍就知道；有没有超扣，翻流水就能查；越权有没有拦住，拿另一个用户的身份访问一下就清楚。

我也特地说明了结果必须在前端页面上看得见：账户页看余额，流水页看明细，对账页看差额。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX0r6CKgJULDYVqWCvBmcXdxFxzy4TmZgvFIbgYcFz15eMNZnWRqS1CDbQmicOJNicQvcpulicE5AZIib3B3ZYzVRIoHIibgL1ojbKo4/640?wx_fmt=png&from=appmsg#imgIndex=11)

当然，GLM-5.3 自己说做完了不算。我提前准备了验收标准，专门盯并发扣费、重复请求、异常恢复和越权访问这些最容易把账算乱的地方。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX3zHHicGYxlPvhWnnHwty1DyQF53nr5gVRQ3MPPgOh7diaiaKMqGHt7PpFvwg3f5vtK5xjJIxqYVactINYY2xPz8vorwXS3k6kM1w/640?wx_fmt=png&from=appmsg#imgIndex=12)

干了 20 多分钟之后，GLM-5.3 说系统已经做完了。6 张表、30 条测试全绿，还在空数据库里用 `npm run setup` 重新初始化了一遍，再用 curl 把 19 个接口场景全部测完。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX3lYdNEKGuPJgUTXl3Jvwic5ZGFGdqBVcpZC1mnwJvb7qibjfUbGfa3cUBsuK1ibseCicCpP8ibdzzoh7y63sLs9vGNvfaFDkRvV6g8/640?wx_fmt=png&from=appmsg#imgIndex=13)

GLM-5.3 开发过程中呢，并不是写完代码就直接说完成了，GLM-5.3 还会自验证。比如它自己跑了一遍就发现流水页没有加载出数据，随后自己检查浏览器报错，定位问题、修复代码，再重新跑了一遍测试。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX0RX1HIEIZbV8RllYceQWiaPnNLibUIZcAKfXTQRLCvM2VTURzTBkeICWicicLkVOdIFfFfWJ8oLYtWZEAyhFjzareM3gOg71lQb1w/640?wx_fmt=png&from=appmsg#imgIndex=14)

开发完成之后，我就成功登录钱包系统了。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX1Ta3hmYDvWYoHElIXBg40CRodvES1wOKnficibu8xAgrQpmichC3BBniaTjuQePrFs5NubOfVdxHgcGGLwSMRjgtLWbzmyiaWXxDMU/640?wx_fmt=gif&from=appmsg#imgIndex=15)

接着，充值 500，冻结 200，再从这张冻结单上扣掉 200，然后翻到流水页，充值和扣费两笔都在（冻结本身不单独记一笔流水，它挂在扣费那一笔的冻结单号上），最后拉一次对账，差额是 0，账实一致。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX0hhia1bricG0efKxFCHbkcWaueod4CXh5Tq3YlydaPzcjSWHkP2q8c7YQKPmV7nUIZOmxzUqyibqS4Wst2K700yLKujyas66c6mQ/640?wx_fmt=png&from=appmsg#imgIndex=16)

我接着翻代码，想看看 PRD 没提醒的那些工程细节，GLM-5.3 有没有主动想到。

还真有。数据库里加了 CHECK 约束，余额不能为负，流水的收支方向也被锁住了。账户安全这边，密码用 scrypt 存储，登录 token 则采用 32 字节随机值，服务端再从数据库里核验。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX0OJjKm7Yu2af449qOrQa6DxsovUqGR2kUQ3ZcE5Pofmem8Dia4l37dfkicZUw3jj12nHzE6YhYpJKVkIBNLILpCIP4yuNkqvqPg/640?wx_fmt=png&from=appmsg#imgIndex=17)

果然，GLM-5.3 考虑的还是很全面的。

### 200 个请求一起扣钱，账还能对上吗？

接下来我才真正开始下狠手。第一刀直接砍向并发扣费，同一时间打进 200 个请求，可账户里的钱只够成功 100 笔。这套钱包系统到底会放过多少笔？

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX0GKetQxRibWmqu7r1icPX75zau0owIuK8XZ6icFThE6V104CySHhQ9yTIWbsw4KHeAOMTPsGkYpgQC3tDcOaSBibdHmcffynQ7tQc/640?wx_fmt=gif&from=appmsg#imgIndex=18)

跑完以后，成功 100 笔、余额归零、扣费流水正好 100 条，一笔不多，一笔不少。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX3rLDEPhTBicAHjpoB9anXu36L9ic5yfgLDy6yr1SA0k9PvHaY14R9SzORt8kiaOmu0Kahk9ljHkc2o16npyibbAJBBh6VicCG4OwUs/640?wx_fmt=png&from=appmsg#imgIndex=19)

并发扣费守住以后，我继续打重发幂等。同一个 `request_id` 并发提交 50 次，50 次全部返回 2xx，流水却只新增了一条。

接着我一边持续扣费，一边直接 `kill -9` ，服务重启以后，401 条流水首尾相接，冻结金额清零，对账差额仍然是 0。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX24Rlvxf4mKLDhRicBJNzboGibAGQicoibQTRPaiaKCyWic6uC0haicqKwpYEgZAgKKdRzMSeEWbZx4032URIThThhh4L5tEAW3vMLBic0/640?wx_fmt=png&from=appmsg#imgIndex=20)

越权这轮其实就问一个问题，B 到底能不能碰到 A 的钱？我们让 B 去读 A 的流水，拿 A 的冻结单扣费和释放，再拿 A 的流水退款，最后把空 token 和伪造 token 也一起塞进去。

6 种越权场景，全部被拦住了。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX2OW5NoR9J6llbcniczHXybXPEWLlOKQJ9psRTaBN8Qg1ALEGGYx41Fx4W52LnnCQlWES52HQuIdghQZKaPUXnJwgG1xibSuSicZY/640?wx_fmt=png&from=appmsg#imgIndex=21)

跑完这一轮，我还真没想到，居然全过了。那就说明题出浅了，得继续加码。

第二轮我们把火力全压到同一个资源的竞态上。同一张冻结单同时扣费和释放，看会不会两边都成功；同一笔流水并发退款 8 次，看会不会把钱退超。

结果 40 张冻结单跑下来，没有一张出现扣费和释放同时成功，并发退款也没有多退一分钱。这一次，钱确实守住了。

### 代码里有没有安全风险？

账对上了，只能证明业务跑通，代码里有没有埋雷还得继续挖。我让 GLM-5.3 审一遍自己刚交的代码，最后拿出一份 118 行的白盒审查报告：7 条正式发现，4 条信息级备注。报告还专门标明了哪些结论来自静态分析，哪些经过了实际运行验证。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX0Xg9e8VmzEdWJvwictAUTahBhhUB4ibibBiboZVDmQfK4EgKe1fj2StXH6BicQRib45fF0NBrZOTQ0fez4TfZ3mSdickzByJbrM85nTY/640?wx_fmt=gif&from=appmsg#imgIndex=22)

所以这 7 条发现，我没有直接照单全收，而是逐条重新验证。结果 7 条全部成立，一条误报都没有。说实话，这一下确实有点超出我的预期。

第一条是 XSS。流水页里的 `requestId` 没有转义，直接塞进了 `innerHTML` 。我按照 GLM-5.3 给出的注入串发起充值，再打开流水页， `onerror` 真的执行了。GLM-5.3 只把这个漏洞定为中危，因为当前只能注入自己的账户，更接近 self-XSS。这个判断我认。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX3KZUL4lnu2ibM0yonMJYlsQ8ib8zL6vbYfa5kicZRpDQtk7Xwj81veQMa2O2IJ2S13UP3UbVFQyBoUicMhSPsCbH9H9pafzdkX4Wg/640?wx_fmt=png&from=appmsg#imgIndex=23)

第二条是登录时序侧信道。账号不存在时，接口会跳过 scrypt，耗时大约 0.4 毫秒；密码错误时则会完整校验一次，耗时大约 19 毫秒。攻击者只看响应时间，就可能猜出账号是否存在。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX0Oh2YHgJucdf9yLKRKRk3Vs75N0iaGupoWH8k8OxmUJgkztiaaAJmmpKs5dLwsBSHibPSMf095fF3UvgjTrtAia38Of8CrAub4bq4/640?wx_fmt=png&from=appmsg#imgIndex=24)

我把修复拿掉重新测试，两种情况的中位耗时分别是 1.52 毫秒和 22.36 毫秒，确实相差十几倍。装回修复以后，两边都稳定在 22 毫秒上下。这个漏洞，GLM-5.3 不仅找对了，也修对了。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX2icn5ibMujaUnhAxN2WNYXaAvpqqkvler3o7sbx6sCgtzegLdeJLDITvOAyIc44oqPpP4GTvqd2AxfmdHrQe2B2Fyb5mibqkeKDU/640?wx_fmt=png&from=appmsg#imgIndex=25)

最后，GLM-5.3 逐条修复了这 7 个问题，一共新增 17 条回归测试，测试总数从 30 涨到 47，全部通过。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX0XjQIb8b8VxM4icGv1uu9UoINIqJP3TK1o3nh7hTVoIsA7JwDIJHBAbJOLhRqnia7KbICUcAbKme7kyJajiaGP61rpljo3xOfIkM/640?wx_fmt=gif&from=appmsg#imgIndex=26)

GLM-5.3 还做了 13 轮回退演练：每修一个漏洞，就先撤掉补丁，确认对应测试会变红，再还原复测。我也随机抽了一条，把实现改回旧版本，新增测试当场失败；恢复修复后，47 条测试重新全绿。

报告里的 7 个问题修完以后，我又做了一轮上线前检查，结果撞上了一个报告之外的问题：一笔 600 元的冻结明明显示在页面上，扣费和释放的下拉框里却都找不到。钱没丢，但用户动不了。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX2kW2FWicdibLGdlVehftU4QQ6MXZ14CWXyruiaG0NAlwvtO9qzZibcAlCzeKdMYakwfCznOSezeMnqAnVicIiaXCw55g1cHx1uE6IMU/640?wx_fmt=png&from=appmsg#imgIndex=27)

顺着数据往下查，数据库和后端接口返回都正常，问题出在前端。前端只取最近 200 笔记录，又没有带上冻结状态，那笔 600 元的冻结单直接被并发测试产生的记录挤了出去。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX2H6w1aSnACH1ibcywiaelcrkAejrgD2ReaWGSMS3pK2tLFf0M3VlGhJJTQ4ARkPnn28j8Anz5pAPy7h6ycw1PRbc5RN4GbtV20Y/640?wx_fmt=png&from=appmsg#imgIndex=28)

还有一个很现实的问题，就是慢。修复安全问题又跑了将近半个小时，中间有一段时间，我确实只能盯着 GLM-5.3 等。

而且这一轮也暴露出了 GLM-5.3 的偏科。审后端时，连 19 毫秒的时序差都能顺藤摸瓜找出来。到了前端，GLM-5.3 主要盯住了那些通过 grep 就能搜出来的注入点，却漏掉了这笔被 200 条记录挤出去的冻结单。

怎么说呢，后端像拿着放大镜在看，前端更像匆匆扫了一眼。

GLM-5.3 还有一个边界：只会修复自审报告里列出的问题。比如交付验收文档里已经写明，同一个 `requestId` 换一个接口再次请求，系统仍会返回第一次请求的响应；但因为这个问题没有进入自审报告，后面的修复流程也没有处理。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX0HdufaZSY2Py9Luf6S0vJHOWqCIMnyzA6BxMk3IvKuopaSBApa9PAbWXtKiclh2IH2Pcnic1qicnwqu1W9PkvFRtALAfjmTuUrPA/640?wx_fmt=png&from=appmsg#imgIndex=29)

如果只看「账会不会算崩」这项验收，我愿意给 GLM-5.3 一个「通过」。不过真要上线，记得先修掉那笔无法操作的 600 元冻结，以及还没处理的幂等问题。

所以我们让 AI 干活时，不能看到一句「已经完成」就全盘接收。AI 主动反馈的边界和遗留问题，反而要一条条追下去。

## ────写在最后────

说实话，看着国产模型在 Coding 上追到 Fable 5 附近，我是挺爽的。

GLM-5.3 还有一个特别有意思的地方。GLM-5.3 沿用的还是 GLM-5.2 那套基座，参数量没有增加。GLM-5 系列采用 MoE 架构，每次推理只激活约 40B 参数。

从 GLM-5.2 到 GLM-5.3，基座没换，参数没涨，Coding 和长程任务却继续往前冲。靠的是什么？

官方给出的答案很直接，这一轮提升全部来自后训练。

所谓后训练，说白了，就是让模型真正下场干活。任务不再是一道孤立的编程题，而是一个有代码库、有工具、有失败、也有验收的真实环境。模型要自己分析问题、修改代码、运行测试，失败了再回来继续折腾。有些任务，换成一个有经验的工程师也得干上好几天。

GLM-5.3 已经证明，同一副底子，还能继续练出新的能力。国产模型能追到今天这个位置，当然很牛逼。更让人期待的是，这条后训练的路，明显还没走到头。

最后，来欣赏 GLM-5.3 国模一哥，制作的3D足球进球精彩动画。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX36wAOxx3dSWXuJiazFMl0IlEiaLkstdOPQ5MG3WIPFItfVicCrEwAZekzz3YEfXxLqhA4iaevg8lJMXkES5CO2CFds7qNKBG8f4LE/640?wx_fmt=gif&from=appmsg#imgIndex=30)

你就说，这带球过人的动作，够不够行云流水，这射门的弧度够不够帅。

AI 编程实战 · 目录