大鼻哥嘚吧嘚 大鼻哥嘚吧嘚 *2026年9月30日 13:43*

Codex自从更新了新模型GPT-6 Astra后

强是很强

但是非常不经用，跑两三个任务，Plus的5小时额度就干完了

当然我肯定是没有更多的预算开Pro

因此只能干等或者换其他的AI

不过偶然间看到有人分享原来网页版Codex额度和Codex客户端是分开的

是两套完全独立的配额

而且还能通过让它连接我们本地的电脑文件夹

要知道codex网页版默认是不支持读写本地电脑的

如果能接上那不就是妥妥的备用油箱嘛

那既然知道了这个信息

我们要尽可能把它吃干抹净

绝不能让它在哪里吃灰

## 核心原理

整条链路是这样的：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3FELVDA8zrReNMFmaW7tPric1VR7yW1CF8Ts10Dd6mgmRNDZhrTc8ttZ3ImXv51iadWT6rJh3b5OFqAonCdft4WA9DqDFsAuskMFYQudN8aCs/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

说白了就是我们默认只有开头（ChatGPT网页）和结尾（本地文件），中间OpenAI安全隧道和本机WebCodex没有，所以需要配

WebCodex的作用：让ChatGP 网页版（Chat模式）直接读写你电脑上的文件夹、跑命令、改文件。

这个链路最核心的价值是网页版Chat的额度和Codex的额度是分开算的，当Codex的5小时额度用完了，网页端还能继续干活。

这里有一点要搞清楚：

我们通过这种方式接入后，是在ChatGPT网页使用的，而不是在Codex上使用

为了让这个连接路径更简单可视化，有大神把做了一个软件只需要配置几个信息就可以用了，并且开源出来放到Github上

![图片](https://mmbiz.qpic.cn/mmbiz_png/3FELVDA8zrRKpsicVJZxolE2gpv0tpyXIaiczmQScv88IQ0WNAPyOIzjSZTBVxorxrLHuvKneDNm1g3iaCUia9GNQjMPLfyEDoMYkm1kPA3TXeY/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=1)

但是依然有门槛，我觉得这种技术大神，都陷入了自己的知识诅咒，以为只要发出来大家就会

而对于非技术人员，找到这个开源项目，也大概率不会用

那大鼻哥也是研究了很久，才把链路跑通，下面就把这个保姆级教程分享给大家

## 安装WebCodex

第一步，先到这个项开源地址下载安装

可以按照下面的流程去下载安装包

如果不知道自己电脑应该选哪个安装包，也可以直接把项目地址发给Workbuddy或者豆包工作，让它帮你安装

AI就会自动去获取你电脑的信息，并从项目地址里找到对应的安装包并安装

安装后打开会看到这样的一个界面

![图片](https://mmbiz.qpic.cn/mmbiz_png/3FELVDA8zrR9yDICdVs6J0ic7Libv6dIF4UFvUqcPTqUr2xOic9iaIibsZoK8QGtziaBBGg8BGpI4V2eWryBxzHv87SqUPVEuYSaDQMwwZdPXgumE/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=2)

添加项目等服务全部就绪

在上面的首页里，直接点选【在此电脑使用WebCodex】

接着会进入下一个页面

![图片](https://mmbiz.qpic.cn/mmbiz_png/3FELVDA8zrT83icnSX9V0ia37CQL59wricKlKmCEKvqCvwq1n1fkwUuibFEI0ib4LTyjvSEibPnCUO3NcTXdnaaJRhdwOfpT6ArFDj4B2UB5Ssk7A/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=3)

这个页面种只做一件事，那就是告诉WebCodex你允许AI碰哪个文件夹

点击页面右边的【选择文件夹】

![图片](https://mmbiz.qpic.cn/mmbiz_png/3FELVDA8zrTmOO0TEmiaOud8TF4mIlGKDDXupmvOhzyyBmPdwKEaQgQ4V6yb6G8RyDWiaDm0yII8GSwQl7VLabNnIgbCKvpBkiavO3Lhwg9gicA/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=4)

选择后是这样的

![图片](https://mmbiz.qpic.cn/mmbiz_png/3FELVDA8zrQj6ThJTicnSFba1gec34wR8GRLxO1iaCiaXQQ3eLV7VwkyziauyNzFsTaU9sXgYaDibk4YAGsqNKiakze9kSSknrib9CnNDibkg5iaFp64/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=5)

原来的【选择文件夹】变成了【更改文件夹】，选错了可以改

确认没问题后，就可以点击蓝色按钮【配置WebCodex】

首页就变成了这样

![图片](https://mmbiz.qpic.cn/mmbiz_png/3FELVDA8zrQ7wCxKMMXwAGMJ9PQiakXRzxHTyST9ok7bGLdwu5BGiawtzq7Yot0IRrSNkayEvIhcvic4K34RqtOSBdrraQSsMd32LqnhAA6LBs/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=6)

这一步的验收标准是看到这三个状态才算过关

1/Runtime已就绪

2/Server运行中

3/Running运行中

如果你的项目没有出现在首页，可以点击【添加项目】重新选一次目录即可

完成后，这个软件要保持开着，别关

## 去OpenAI平台创建Tunnel（隧道）

来到tunnels页面后，选右上角的【Create tunnel】

![图片](https://mmbiz.qpic.cn/mmbiz_png/3FELVDA8zrQicY9YvU6hpsaCKvvepkqVlH7ASicibvTvEUvpys81RsAbPVXcgS4ZiaH64g5YfOBicSnPtvt3sB7EopCufUCW8AP1Aj5Ia5icLeCbk/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=7)

> Name，随便填，比如webcodex-mcp（方便自己记就行）
> 
> Description：也随便填，描述清楚是给这个WebCodex用的就行
> 
> Organizations：选你自己的 Personal（个人）组织
> 
> ChatGPT workspaces：选你自己的目标工作空间

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3FELVDA8zrQMHgNohphchnf7ebFO9hoDAApOiaiavQSyozrQItmicQJP4kba0JSS4yroDic5YkUWKyHGuBWVicmGm4yM5gz9ics9ibMR6JaEXL9zVE/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=8)

如上图，设置完点击【Create】，会出现一串以"tunnel\_"开头的ID。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3FELVDA8zrTZfhBCkY5CLZEhRZUxeKSYayyH4tE6FnHaBGvAHuOQa1nMiaDphPApR1cjkibGleajBqp648ic0VHT1CibOfjyvKguCjNyo0WWtFM/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=9)

保存好这个ID，后面会用到

## 创建隧道专用的API Key

来到API Keys的页面，创建过API Key是这样的

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3FELVDA8zrR8TmBz5OVL5Jv5sM8cYfvNp3lNuNHwkNHyMQ3b0n0yPfByRbCtUUGbs28PuGja0icL2ntCU67prFgnlrP0vJM6Tm0ichr7ttRgo/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=10)

第一次打开是这样的

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3FELVDA8zrQgZQOazRxkwGw0sLic8HibQ2RsgtGkuTo4jlOaa4y0139ERhROHbT3EwzHlj60GGzIt420ovFTGoMR1AImicYqjtibdZdxOt0wqsM/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=11)

不管有没有用过，我们都选【Create new secret key】创建一个新的

> Owned by：选You
> 
> Name：填WebCodex-Tunnel
> 
> Project：选Default project
> 
> 有效期：按需选择（建议选个有限期限，更安全）
> 
> Permissions：选Restricted（受限）

![图片](https://mmbiz.qpic.cn/mmbiz_png/3FELVDA8zrQrze5nsfjxDXpGPp2ZzFOrL96vtUznjlbiaeNcMt8Tl6VZGufsfqdzgvNlCHRjvG8yKZkdckEeOFV1bqHgtKyBykYCSO9ND2dM/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=12)

> 往下滑在权限列表里找到Tunnels，勾Read和Use，其余全部保持None

![图片](https://mmbiz.qpic.cn/mmbiz_png/3FELVDA8zrQjGGd0uh4tVMCBibrvzO6hnsRwv1Yjibl0j9yJxaibibOSVK5J8AwibwOMAUD9nY6Z00j0rUaU9mmEohLT4docDv1ymCc6OBNhq3DY/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=13)

点击创建后，就会自动弹出一个密钥，我们把这个密钥也保存下来

![图片](https://mmbiz.qpic.cn/mmbiz_png/3FELVDA8zrRMEWgavuibcWicqwe0bgw7CMkbK2DBR9nXmcRXibanJJMbEeVf8gG3q1ia0hyPwTgLGCnewMmwV9RhIOt2iaGNKJStysIKbQ50u6KM/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=14)

注意，这个密钥只显示这一次，关掉弹窗就再也看不到了，只能重新新建

另外，也不要把这个密钥随便发给AI，更不要截图外发

## 把ID和key填回Webcodex，启动隧道

回到前面下载安装的Webcodex，选择左侧菜单栏的【连接】—再点右上角【添加连接】

![图片](https://mmbiz.qpic.cn/mmbiz_png/3FELVDA8zrR4nvJuQt7f67QBcYMEJico7zibPbrMF1pucrA1xcgTdZXV6tutQyfc0UQ0jOicGia24DiaaW961LOYMqMdBqM3AEYZaPNRBibvjZcGA/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=15)

在弹出的表单里由三项必填

> 名称自己取随便填
> 
> 前面保存下来的Tunnel ID、API Key

![图片](https://mmbiz.qpic.cn/mmbiz_png/3FELVDA8zrT6GtCicb9Pic7eVwkiadOAl9HZG2Jbwvkt1R6R0AY1TZFHVxmcvfgHia6R46fd1t1EO9elzpAHvV59n0VRY7NNo2anic5wxND8X0wg/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=16)

保存勾选【自动勾选】，点击【保存并应用】

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3FELVDA8zrTWxPgcm7HRGY6NNXfpgAwJnxnDx9iaKicLJ8pNX5M2gsaWudU2LFuxaricpe4nGHxVssNhhEy7amzR5u05wgibwKuKJXxZMs3kA3g/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=17)

## ChatGPT网页：开开发者模式+创建MCP插件

打开网页版GPT→ 右上角头像 → 设置 → 【账户安全与登录】（有的版本叫【安全与登录】）→ 往下翻，找到并开启【开发者模式】

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3FELVDA8zrTaclGgN0EGWTKsl9JzsiaFwwNDedrZ8loWzt0Zl0HuacoIQgqUEmLDjoiaxAB5hj22FnkzXqHNeKU18jEvFA5kJpajPeq5dbIn8/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=18)

接下来进入创建MCP插件页面，右上角【添加】 →【创建MCP应用】

![图片](https://mmbiz.qpic.cn/mmbiz_png/3FELVDA8zrQwpALT6bwJEU0pNtTUDSibfoWbz2QCSjfvtA2PHAiboibicBpnkoicg9JFPibLrOkmo7xoLIufRgIH12PQPuficic6d62vpVSEibKuvt8M/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=19)

> 名称：填WebCodex
> 
> 描述：随便填，比如访问本机 WebCodex 中已配置的项目
> 
> 连接：选隧道，选择你刚建的隧道
> 
> 身份验证：选【无需身份验证】
> 
> 勾选风险提示的确认框，点【创建】

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3FELVDA8zrT630g7zibSw1yub2lYVsNJGlEJdjWZlSy1WDY13uT9icCW4zHYoQSvUWzzOic1rW0CpevzrCic59fvmnM6ttib58UVXYBmUMrCztyg/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=20)

在弹出来的【连接WebCodex】确认框时，继续点【连接】

![图片](https://mmbiz.qpic.cn/mmbiz_png/3FELVDA8zrQ5RhnhG0UWjOfzVvaZZ20LDAxo7sVGLOcvz0lmaJJBI77kURsWszrkkianeqeaCq5eFW7URJeRM6gdFG7K1Nib1ezeJicwibucGc0/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=21)

成功后，回看到已安装的列表下多了一个WebCodex，就证明可以用了

![图片](https://mmbiz.qpic.cn/mmbiz_png/3FELVDA8zrStLicZnUse68G3WlCwhLFlyibt4cGVjvo7GnHMCqbTTqOW8C8HYuhDXIQhpma2y9R57VCww8O4LibSeoSxNFicic8nUdRd3oyTLswY/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=22)

## 真实验收

回到网页ChatGPT中新建一个聊天窗口，点击输入框左边的➕，能从工具列表中选出WebCodex

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3FELVDA8zrQ0SQ7U5VJWOEBxh1LW5pTPftTJnkLWXAZBEH3UhY3vc4OibSHEiaqA3YkBN1FjiaXYaic3xASd7BjDAMdMQCoA5FZlQBrCcIShH7I/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=23)

给它输入指令，先看看能不能读取我们电脑里的文件

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3FELVDA8zrSa3xnTSY0YE2dFmbwspfd3yaXZic2Tg9UWsW1jnVj16Z2xVaJZ5Eq4icNMSibCaxLfjt67oludPJjLTJWcyO81Q1iaicI3b9ibyEfqc/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=24)

这里它能访问的目录，就是我们在WebCodex里设置的文件夹，它说能看到，但是具体是什么没说，再追问让它列出来

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3FELVDA8zrQaHgq1hCuLJ5bxKTzREt2ribiapfQqXok9GV82oiaTOSCpI5NO4I1VepLhIYibchsCR2I1kvcibKsqSJ7EgiaC9ZhtKCXwmp2rYpnZ4/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=25)

文件夹的目录，都被它清清楚楚的列出来真实目录树，说明网页GPT连接电脑文件夹的这个连接通了

这里有个注意事项，必须选聊天模式，如果选工作模式，消耗的就是Codex的额度，等于白折腾

还有就是如果点击➕没有找到WebCodex，可以用小老鼠@艾特出来

![图片](https://mmbiz.qpic.cn/mmbiz_png/3FELVDA8zrRvmtMvkydXIWGHVZx0TS4dvZxbXwmfwVWicI86tbUVIyic0diacy9Nd8Rc7dI1pFtBo313BqQ4xGSIsxOiaBMaSTnDbolL3sVicVfU/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=26)

然后我是PLUS的订阅，只能使用GPT5.6 Sol和GPT5.5

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3FELVDA8zrROAfL9Laf9zKCxLJO9wIBcebd7ibru2fg6icXk8CRNAFdDibSlgzrpBzUJaGrSP2h4Nic4kE2bJyensaJk3qNIXyKiak8EGeysiaVVI/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=27)

为了证明它的实力，大鼻哥又让它用GPT-Image-2生成10张单词闪卡图片，并保存到电脑中

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3FELVDA8zrSRz3icOU7NVlDcr9Gice2zwyTV4ylv6JUM65dDY0ZrYe30CcyTibmHGgGX9Mc0QpM3LIcGd9tVR9Ok39abYfvRWW6IDecMFEjc30/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=28)

打开电脑本地文件夹，确实存好了，足以证明网页PGT读写编辑本地文件的链路完全打通了

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3FELVDA8zrRF7hHFEjA41LywLALfWfk0l8dYnBuJ6SLbLqOmoCsZfJ1Q4JHLc8TMyaR0ibZd4nibT5d4YxQbbwAiaxKtDuC7TejYJYECEuE37s/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=29)

## 常见问题排查

如果你在安装和使用有遇到一些问题，可以对照下面的问题排查表

① 插件创建时报「无法发现 OAuth 设置」

身份验证改选「无需身份验证（No Auth）」，重新创建。

② ChatGPT 里选了 WebCodex 但执行失败 / 无响应

按顺序检查：Desktop 是否在运行（彻底退出了就全断了）→ 连接页隧道是否显示「运行中」→ 是否在 Chat 标签下对话。

③ 说得出路径，但好像没真读文件

判断是否真的读了，看对话里的「工具调用记录」（会显示检查工作目录的调用），以及最终产物是否真的出现在本地文件夹。光回复路径不等于读取成功。

④ 之前配好过，今天突然连不上

最常见：电脑重启后 Desktop 没开。打开 Desktop，确认首页 Server / Runner 都是「运行中」、隧道是「就绪」，再回网页重试。Tunnel ID、channel 和本地项目都是可复用的，不需要重建。

⑤ 它能读到工作区之外的文件吗？

能读到哪些路径，取决于开放的工具、Runner 和当前 Windows 用户的文件权限，不是只看注册的项目目录。所以敏感文件永远别放在容易被碰到的位置。

⑥ 适合做长期项目吗？

可以。隧道、项目和本地文件都可复用，今天做到一半明天能接着干。但 Chat 模式是一轮一轮工作的，受上下文长度、网络、电脑休眠影响。真要连续跑几小时的大迁移、大重构，还是交给 Work / Codex 模式。

## 写在最后

在我写完这篇文章后，GPT-6.1 Sol也出来了

![图片](https://mmbiz.qpic.cn/mmbiz_png/3FELVDA8zrTFPM8gWMenibPXFxcUs4m8Avic6Ub9lNg8X8AbHrh1HrMs8XaPulHMHVCO2tPhSVbN5hP4DNoV7QPibjoSEaNyqzegmwW0KxASxQ/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=30)

虽然还没有深度使用

不过能力大概率比GPT-6.1强，对应的额度消耗估计也更多

当我们额度不够时，有些简单的小任务

可以直接用WebCodex来实现

你别看GPT5.6 Sol在GPT模型家族靠后了

但是能力依旧能吊打很多知名模型

并不是我吹别人的好

而是大鼻哥用真实的实测一遍遍得出来的结论

我奇怪的是，他们一边喊着AI发展要慢下来

一边频繁更新新模型

太他喵双标了

我是大鼻哥，一个央企在职AI产品经理。分享实用AI工具、有用AI知识。