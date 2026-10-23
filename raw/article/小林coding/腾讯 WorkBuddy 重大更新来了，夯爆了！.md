---
title: "腾讯 WorkBuddy 重大更新来了，夯爆了！"
source: "https://mp.weixin.qq.com/s/w_CmfI0QSqowccCZE07GHg"
author:
  - "[[小林coding]]"
published:
created: 2026-10-23
description:
tags:
  - "clippings"
---
小林coding 小林coding *2026年8月13日 17:36*

大家好，我是小林。

我家那只养了 6 年的猫，这几天突然闹肚子，还没走到猫砂盆，就直接拉在地上了。更炸裂的是，刚帮它洗完，结果又拉了，还在烘干机里一直拉。。。。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX0icUu3Ggics6lpJtHZSlicZwtqoxNCUJEyoMiap2qwMb5g0CFdicMCWVC1NgpotLn1icJsEYSISCUBdnE6NBbKxH0UujRSRicZQUluB8/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

整个家里都是💩的味道，场面非常炸裂，我就不贴图了，怕影响你们观看。

然后我们火速带猫去看病，花了 1500+ 大洋，医生初步判断可能是胃肠炎。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX2SjdtaZOPZu0ONMNiaLbKanU3nD9KJCiaWBeLXdekUWCH0375RibNFtawbaBI2bX7hDic6fUKUOSGCz8cmwPmwsoM1UswMYguUww8/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

医生也给猫开了药，叮嘱我们每天按时喂药，多观察猫咪的饮食和体重变化。

这时候问题就来了。我们有时一忙起来，就会忘记喂药了。

为了解决这个问题，我就想，干脆开发一个「家有宠物」APP，专门在手机上记录猫咪的饮食、喂药、体重等情况，避免漏喂药。

说起来简单，但真要开发一个 APP，流程还是挺复杂的。有没有更简单的方式，能实现我这个需求呢？

刚好我看到 WorkBuddy 新上线了「资料库」功能，可以存放 MD、HTML、CSV 等多种格式的文件，而且还是云端存储的。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX1IturrKaEGiaYqDvKyowtcIfGoV7SibHx6zgibibBuicKCbYZUmozDmMwqBI1rbcwqTRvu3uQPOfJsvsOgP5M3ujk4bK4r8HqXzSgA/640?wx_fmt=png&from=appmsg#imgIndex=2)

这个资料库的呢，还支持二次编辑 HTML，既可以人工编辑，也可以用 AI 编辑，一下子把 HTML 的使用门槛打了下来。基于资料库做出来的 HTML 页面还可以直接发布上线，再把资料库里的 CSV 文件当作轻量数据表使用，不需要自己搭建和部署服务器，很快就能做出一个「轻应用」。

所以，我就想基于 WorkBuddy 的「资料库」搭建一个「家有宠物」工作台。随后我爆肝了一天，就把「家有宠物」APP 开发完成了，先给大家看看成品。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX0tYATibEAaJwia2DZlx1DjibuZRck2SicV8xsicwa3ueT3HXKvKIAibm9VnvN1XS7G78Ptwh3JRSM4lrmb4ibJ1RyBegMiaDmf8mTRbBk/640?wx_fmt=png&from=appmsg#imgIndex=3)

我家一共有三只宠物，我分别给每只宠物建立了档案，还实现了「喂食记录、喂药记录、体重记录、消费记录、医疗记录」这些功能。家里宠物的日常情况，都能在这个 APP 里记下来。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX0QOEibqic8AdIKBZhoNR1MZAiaIGst0ibk8yXwpBS5G2FxCjUFfIJDk3atN1WbDgrnpcqN8LS5e3Yn2AhFHAEGWUSYeyuaNC1a2pI/640?wx_fmt=gif&from=appmsg#imgIndex=5)

比如最近，小弟这只猫得了胃肠炎，需要每天喂药，所以我在「家有宠物」APP 里设置了一个喂药疗程，每天要喂两次药。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX1d3ecj8EaETqibEV8KwTuUG5JT1BOuV6tvQVcGEPkwWm8Aq51AzbG7aq9TA8sdYaTEcAibXH9wuDcT24ZMwAWaDZJxGpB27dicic0/640?wx_fmt=png&from=appmsg#imgIndex=6)

这样一来，在首页的「今日待办」里就能看到喂药提醒。喂完药后，可以在这里打个卡，免得忘了今天到底喂没喂，也能避免漏喂。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX1fRIqBLgYvO3PcxZVdCeV90WrBEduAjI2kAJa4ak5uvgqhgHiaheXFJicOfKGnH2gk2oEaYnEzBvB5P4G6NoUenjSJXlpF31Nb0/640?wx_fmt=png&from=appmsg#imgIndex=7)

除此之外呢，还可以记录每一只宠物的饮食和体重变化。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX0aNp8Tba3UWn1PpQ2gSQsRAt1k2FsD1iaFqxNPXcOanAbyo1mqiaeAIt9YVPwEBm0mCZLUDCFUO5k50d7Aialyv5fke3ysaLYzkQ/640?wx_fmt=gif&from=appmsg#imgIndex=8)

所有数据都会存到 WorkBuddy 的「资料库」里，完全省去了自己搭建后端、部署服务器的过程。效率高多了。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX0CHVJ74yiczz0LuTibsnhzeXq8WUnxjHke2yzbwNoNJhOOhsic7VkMAm5CaZQMSo3NrBDwSZk7cZUSdtCnxiahznLhLRzaJjf4eUo/640?wx_fmt=gif&from=appmsg#imgIndex=10)

而且网站开发完后，还可以直接发布。这样我就能把地址发给家里人，谁喂了药、谁喂了猫粮，都可以直接打开「家有宠物」APP 记录，非常方便。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX0CmK3t0ctFIGtbeZ7c4WOhvEDI8giacrk7Pp9Z6Vh9BrT9Qk9FIz2pibSok2x3YXeEIUDmV3coXyPqo3gvkSS2MTmtYQTFbsf60/640?wx_fmt=png&from=appmsg#imgIndex=11)

不用专门部署网站，直接通过这个链接就能访问。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX0gHh8F5UTKelN9bVpkhQicO9ynXSLickj0ktCQhpBrlEaZJqcYTjzrD7PHox760GAFF3txzcP0TDsV0lznEDlgk85nxNNHu12mg/640?wx_fmt=png&from=appmsg#imgIndex=12)

甚至还可以把这个地址保存到手机桌面，当成一个 APP 来用，日常记录起来更顺手。

，时长00:16

<video src="https://mpvideo.qpic.cn/0b2euyaecaaateacdct4dzvfbjwdigtaaqia.f10002.mp4?dis_k=87bcb5b262a6609da08b438fe635fd2c&amp;dis_t=1792736876&amp;play_scene=10120&amp;auth_info=aI3g48FzXxUbrOvuq1dJWWQ1G0xtYxIyNS0faDZQMUhWbDYSG34CenkAYEFHdV5jbg==&amp;auth_key=2a323127bea40be0d3605f6360a9b027&amp;vid=wxv_4646344747991711746&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

接下来，小林就带你们看看，我是怎么一步步实现这个「家有宠物」工作台的。说不定你们看完之后，也能搭建出自己想要的工作台。

全场保姆级教学，话不多说，开始！

## ────实战「家有宠物」工作台────

### 1｜创建资料库的空间

首先，在 WorkBuddy 左侧找到「资料库」，点击后就能进入资料库的工作页面。接着创建一个工作台空间，再取个名字，我这里就叫它「家有宠物工作台」。后续开发过程中产生的内容，都会放到这个空间里。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX0TdJtJDO1lMnKwo7BflpmATzSX09teJ7fV7PgNvzJ8odsJibezelG5AicJVe5tHg5brH2XLTmetCK35H9k4dqwQ6eBR0PjB4MeE/640?wx_fmt=png&from=appmsg#imgIndex=13)

空间创建好后，在「家有宠物工作台」页面点击「添加到任务」。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX1tm9bDNpkQYqDvvGUqx8cDVpSW1RIdjHUNlUGQFuKv8DkBcliaxGXruCMRGbTrnwv0nOrhqgD7HEEdlSiaLibPM8SYGpIMSB05XI/640?wx_fmt=png&from=appmsg#imgIndex=14)

这样，我们就可以在对话框里调用这个资料库空间进行开发了。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX0B0qVKSVVQ99AE4icK9QswNX0csxHDArLvD184o2KCv1NMYaVGVicibEFaKb12AYiczjcR3DsbVfbueFty8mNEZ8icuNGVjCEXTd9U/640?wx_fmt=png&from=appmsg#imgIndex=15)

### 2｜产品文档设计

按我自己的习惯，不会一上来就让 AI 开发一个完整项目，而是先拆步骤，再分批开发。

第一步，我先让 WorkBuddy 根据我的要求，帮我写一份产品说明文档。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX27f9OScTWc3hjswe6hk3D96MEM7KnFDc2cZngLFH8G9CVAj4ibCLGNeF8IUUqN0SErF7zTMBdPC28j1k4QdrKtKQSX36vTHGS0/640?wx_fmt=png&from=appmsg#imgIndex=16)

如果你担心自己写的提示词不够全面，也可以点击 WorkBuddy 右下角的提示词增强。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX3tmoYTUyucxPdTRJ6Hfpiab5bWFwIFGRd88h37TAkuZr3OQ7H8lo55tSPqlcVW0wfxeqibjuY4JwoA9frhkkjDiaJNOWk0C4IeeQ/640?wx_fmt=gif&from=appmsg#imgIndex=17)

提示词增强后，确实变得更全面了一些，接着就把它丢给 WorkBuddy 去干活。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX0uPalk8bdq6zpO51SagyQicFnrLkFXOAG6IiahYTOiaLh2E7lsdEkibU2fiaTibmIYWTf0aYbSE0ianII7jericVCiap9RYFvTgwtN900M/640?wx_fmt=gif&from=appmsg#imgIndex=18)

干完活后，它会直接产出一份详细的产品说明文档。我们打开后，先看看文档里列出的功能是否符合自己的需求。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX0pwTsdNLkud2XuDF6Bib87pgmDkQTE52zu4icD47EQEgUkG0IrdNXptdibMY769bRpcDw9SCVd4icaytnazIyg8g47Nb9rJjGqMiao/640?wx_fmt=png&from=appmsg#imgIndex=19)

如果遇到功能遗漏，可以直接人工编辑文档，也可以选中产品文档里的内容添加评论。比如我这里想在「医疗记录」这个功能里，增加一个「喂药提醒和记录」。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX1ibDPhMteo7s7rflXhUQiacSmzwc3G6UEBH1IqDbnp1wPTEPojiarMa9E9AOT892FcSrUSugvZe2piahFxu3Ste9er25oZPInocaQ/640?wx_fmt=png&from=appmsg#imgIndex=20)

我就选中「医疗记录」这部分内容添加评论，然后点击「AI 编辑」。需求写完后，会直接发送到 WorkBuddy 的任务框里。

不得不说，这个人机协作的体验很顺手，哪里需要调整，就在哪里把需求讲清楚，WorkBuddy 也更容易改到点上。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX2iaxbIbKT0b8Kmia8qZYBCNNcF75GQmhPDSlPibYxXsicic1gu6cQQmu0BiaWFxSMSTKqz9m6Iv4xeY8q2ts0lKWlziawia1zZCiaHw4Oc/640?wx_fmt=png&from=appmsg#imgIndex=22)

完成产品文档设计之后，下一步就是做 UI 原型图。

### 3｜UI 原型图设计

UI 原型图的提示词我也写得很简单。考虑到后续要在手机上使用，所以原型图的布局和交互逻辑得符合手机端 APP 的使用习惯。至于页面风格，我这里直接指定了「微信」风格。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX0d0eXxNRtStNbvdDtU9cwEvSvwVLfb4NgCOicMmmXNTyuqGEichu2uQeFVa4hGwOOkjG1Q77awRTL52a4ZSIrw1v3aqhenX8XIo/640?wx_fmt=png&from=appmsg#imgIndex=24)

最终设计出来的效果如下：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX3uEb3OcYoelmLAsCic6Oo31PNhNcXIMbHjlqAHEVwN0ah3nxYnZhJ2P7uw9ic0bfQE76DLjSgNTf30rN0VVdOibe3HpTtqWUW8ng/640?wx_fmt=gif&from=appmsg#imgIndex=25)

你们觉得如何？我是觉得蛮 OK 的，确实很符合微信的风格，整体简约又实用。

### 4｜开发工作台

完成产品文档和原型图的设计后，现在就可以真正进入开发了。

我的提示词如下。这里要注意一点，一定要写上「基于资料库能力」，因为只有明确这一点，WorkBuddy 才会调用对应的资料库 Skill。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX0mFZ3DhGs96k7APbB0oh7dp4Rh3Ieia4xWR6EkJ0HQd2SHy5oFHEnicXTTmavHUuVRxqHNn3nnrIXpA2Q2sq7G9OiaN8eThIcCia0/640?wx_fmt=png&from=appmsg#imgIndex=26)

开发过程中，会先建立数据库表。这里 WorkBuddy 根据产品文档的需求，建了 6 张表。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX2NUwnicmjxPpWFkFLibR1NBrXRfmG0L0xHqj15Q3OdiaMK7ttXBvU8MMibXGZdFy0VchWekmfDbgNKp1Fx77Ca2GicKEl9gtCmRBtc/640?wx_fmt=png&from=appmsg#imgIndex=27)

建完数据库表后，回到资料库页面，就能看到「家有宠物工作台」这个空间里已经创建好了 6 个 CSV 文件。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX0nIkrM6KGZN7khYJhSiaADicQ83ppoMOGU689RF9lsSOWb0DDCibv0OoNiaWaGnV2OLM3WNNXkP592rSzjibjlyWHLuAxKrQ6Dzemw/640?wx_fmt=png&from=appmsg#imgIndex=28)

这些 CSV 文件，你可以理解为网站的数据库表。后续在网站上操作产生的数据，都会存储到 CSV 表格里。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX1BN4EqmqI7vEiaxA9vkpHNPyGINVr1jhZJBj3gfwAf46RiaaDxp0icl4WE1fY4RQUpML0nJTHkavpk9cO9JceiclI6gic5QRHpnp00/640?wx_fmt=gif&from=appmsg#imgIndex=29)

完成开发后，就可以体验这个「家有宠物」工作台了，基本跟原型图设计时的样子一致。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX3EiayWVB0LOuplAl9nxL6XgYae7JSaJ9cJFZg6Jk5zGO1rN4M6PYTRo0enKE0gfCibfLfcAMKprArkNkpIAdF82J6xc8m6YTAtE/640?wx_fmt=gif&from=appmsg#imgIndex=30)

这时候切回资料库，你会看到「家有宠物工作台」空间里多了一个 HTML 文件，这个文件就是我们的网站。HTML 文件下面还存着 6 个 CSV 文件，这些就是网站的数据库表。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX05okibicBpL77RCOYTnH29a1Xics6m2DvtLSbgj1bawgunnmB17kplEK2KEmFjc28dP25cQdWanKaqQFvAhBBeEqOzHkwXEUfySA/640?wx_fmt=png&from=appmsg#imgIndex=31)

至此，整个「家有宠物」APP 就开发完成了，接下来做一些功能测试。

### 5｜功能测试

我把家里两只猫的信息添加进去。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX0EWQsuMCV1puErpAEVrucvvtbhQ5uPooTGzlJWOI0OEEMmzU4G2eBic9B80iczQ2uJGiavic2RsvoVI9tKZIHVVK94bQlPklLWWSA/640?wx_fmt=png&from=appmsg#imgIndex=32)

这时候，宠物档案页面就能显示我家两只猫的档案了。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX2yfrZUp3X0ibytXYedPqHzAKvEnNEqcu9G53YAzACmo84cgNGohyIvZ8tUvicjSRsU7gQibAuADa3AHScDnb2dRriaRMILudJnOq4/640?wx_fmt=png&from=appmsg#imgIndex=33)

然后回到资料库，点开「家有宠物工作台」空间里的 CSV 文件，可以看到刚才添加的宠物档案数据都已经保存进去了。这说明 APP 和数据库已经打通了。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX0TCaTvjMiayG43ic0x9cTHkJg8icHNzeO9I5icsUDcSataQMpLQc0MISuNynqJE0BFpibk67hmPWCvxQquslnVrVicobIBpChgLiamh4/640?wx_fmt=png&from=appmsg#imgIndex=34)

随后，我也给最近生病的猫创建了一个喂药疗程，每日 2 次，功能也没问题。

喂食记录功能也没问题。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX3YndDd3ia9TqWWv8vZxzzzQpBNOkG0zjz60zwuzgMG1jlxacY9eeFZZ4GibkJRbib9G8MUIKOKtvb0DooIiahW9lDclyL0YAD7Rib4/640?wx_fmt=gif&from=appmsg#imgIndex=36)

消费记录功能也 OK。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX374tEbgSoicoha5enxazPnIAHibf7jKwULVh6ibqLka7EvjGcLxDib82h0uOfqkldkTlsibehIgbHPQE15eUYtPvvD1ozMibbqYXBQ8/640?wx_fmt=gif&from=appmsg#imgIndex=37)

### 6｜发布网站

功能测试没问题后，我们就可以直接发布网站了。

在资料库里找到 HTML 文件，点击右上角的分享，接着开启「发布为网站」，网站就上线了。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX0EicJ69c2OnW8nM3YTtiaia2rfFVuMoY01VNntd9kdq9AicR5BZ4YRjpsaSnUKjw4RRmULxkcDaPOj4qkRPRILuGtxBekdDx1aZmw/640?wx_fmt=png&from=appmsg#imgIndex=38)

对的，就是这么简单。不需要自己部署服务器，也不需要注册域名，发布后的链接，谁都可以直接访问。

你还可以把这个网页地址保存到手机桌面，当成应用来用，体验跟 APP 也差不多。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX2AYatSXCXlyG7FibIveD7gHlgLuPek39z4yPOX2x7BYdPYbAzicOvHBjf2FgfNsJZJ0sacobkrDpUlYYTRN9oO3esp6kLHVkFes/640?wx_fmt=png&from=appmsg#imgIndex=39)

后续想继续打磨网站也很简单。打开资料库里的 HTML 文件，然后点击右上角的编辑，哪里不满意，就直接在对应位置评论。多人协作时，这个功能很好用，谁有意见，谁就直接写下来。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX2QZ7vc3kjg04MdE1LYXjpn98auEGicIv5X6LpsiapZWDT2ymZEibkTzIwQyibEe8fgNqN8icrFRnT0aPLy5NLDAt7a8CJ3h0Oky0FU/640?wx_fmt=png&from=appmsg#imgIndex=40)

后面的事就交给 WorkBuddy，让它根据评论内容去修改，人机协作的效率一下就上来了。

## ────我还做了哪些有意思的轻应用？────

### 博客笔记网站

之前就有读者问我，怎么搭建一个博客网站？放在以前，可能得买服务器、开发项目、注册域名、备案域名才能搞定，流程繁琐，周期还长。

现在你完全可以基于 WorkBuddy 资料库的能力，直接做一个博客网站。比如这里，我把自己的大模型面试题笔记，全都上传到了资料库里。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX3txcgYgcCIsGvvMUVfRLlzgc0kV20vPcyPf56l10QrvRa6o6I7IhDOnqqotwbElXkqfWEEV6dDtpibbQhXMGy113m7MXt72Eic8/640?wx_fmt=png&from=appmsg#imgIndex=41)

接着，我还是按照前面提到的流程，把产品设计、原型图设计、网站开发走了一遍，很快就做出了一个「暖纸手帐风格」的大模型面试笔记网站。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX3lvaPU6dVOzsuaTpWPfeHF0vwPye6hQHKXHWvibBUq9s4ABRicZV45Jp1vgP6aBMGtk12icK56icmrc0hgMC6jtRb3A58ib5sC5PNg/640?wx_fmt=gif&from=appmsg#imgIndex=42)

还做了一个 7 天冲刺学习计划。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX1wGcOJHHAo5uib3TaKwLIDoXOia1RWR0qN36We2vRzDGExncEgpIXwNUtgTtotDN5ePWLqAg96ThpZIgkv30I4UicKSuqYAYic5WA/640?wx_fmt=png&from=appmsg#imgIndex=44)

内容列得非常清楚，还把高频面试题都做成了冲刺计划。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX1H3PwbiaGibEndXrQv197lTmib48EQG11a6CPV4tia8gKmP0uDrHqQfoI85KkFB27cxmYukQKTG4p19UgukRW05IcD3IcQwNYhVGM/640?wx_fmt=gif&from=appmsg#imgIndex=45)

然后我觉得，光看还少了个练习环节，所以又让 WorkBuddy 做了一套练习题。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX0j6ewym5HdqnvdQXIY9rEE7qJwNGnfEaJxoXU0vOiaXFKAByywgYMdSiaDGyvmQwHypE7DstERClKUN01Rf4OZcHbS63MH8eGxs/640?wx_fmt=png&from=appmsg#imgIndex=46)

这样复习完大模型面试题后，还能做针对性的自测，面试突击的效率直接翻倍！

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ysyAxM1rgX2iakdCmpnsa74zPCib6TzERd1wHNa9YfuCvMg5OSibnGfkvlAJH87vCyosNhELCI5l8pDoIscxUiceVQxObd1bApx3cUQZY9H0yZ4/640?wx_fmt=gif&from=appmsg#imgIndex=47)

### 旅游攻略网站

盘点了一下，这几年我和女朋友去过的地方还蛮多的，但之前的旅游攻略都记在手机备忘录里，看起来没那么美观。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX2KEb4mr3np1opgeUAsbibYpT1s2YTKaoJphnQ20c4WD7MnM08d9tScez4KoeC3btNS4ddxWibY5ckhKSA3sxiaFTUCX7iaGNyeVvU/640?wx_fmt=png&from=appmsg#imgIndex=48)

所以，我也基于 WorkBuddy 资料库的能力，把这几年的旅游攻略都放进了资料库。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ysyAxM1rgX0iaqstP0D6T7jJFIYZ13Z8kYnNdKaCxJxNibcHxDDk0Gm8qDCdpc2kdxPib23JCljbMdLx9JpO2eXIjyX22zt2tYN3OpjqqJicjBY/640?wx_fmt=png&from=appmsg#imgIndex=49)

随后，我又用 WorkBuddy 开发了一个旅游攻略网站，把我们解锁过的城市都记录下来，有种在游戏里解锁地图的成就感。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ysyAxM1rgX2aO8QopNxk7QIaKQFYInibDFhTr6picpqdDbBvuHSMJMZqj95VUgKuSn5gTfMZ9oe8PhZUApUWNvCuKLSbfDPfM6vyn6kEZNDAo/640?wx_fmt=png&from=appmsg#imgIndex=50)

每个城市的攻略也做成了可视化，以后再找攻略时，就直观多了。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ysyAxM1rgX2b50esgMsUqODIvQat9YCjsiaecGbicWu3EecFLs3umNTfaguZW9CAiabVMkPZfiatwY6Tr1oxwMPicsydPiarKgicDKqN6ZURJZTsjc/640?wx_fmt=gif&from=appmsg#imgIndex=51)

## ────写在最后────

看到这里，大家应该能感受到，WorkBuddy 的「资料库」不只是存文件的网盘，更像一个能被 AI 持续读写的云端空间。产品文档、HTML 页面和 CSV 数据放进去后，AI 就能基于这些资料做出「轻应用」。

以前做一个网站，要经历设计、开发、买服务器、注册域名和部署上线，流程复杂，后续还要维护。

现在建表、开发和调试都可以交给 WorkBuddy；网站做好后，不用单独部署，发布成链接就能分享，保存到手机桌面后，用起来也和 APP 差不多。

我觉得更有意思的是「人机双写」。无论 MD 文档还是 HTML 页面，都能直接选中内容，让 AI 按要求修改。

多人协作时，大家还能围绕原文评论、讨论，一起编辑同一份 HTML。AI 对 MD 文档的修改会先进入审阅状态，确认后才写入正文。人负责提想法和把关，AI 负责执行，不用再在对话框和文档间来回复制粘贴。

轻应用里新增、修改的数据，也会同步保存到资料库中。像我给猫添加档案、记录喂药和体重，背后的 CSV 数据都会跟着更新，真正把「网页展示」和「数据存储」打通了。

所以，如果你也有一个想做的小工具，就可以用这套方式快速落地。普通人也能和 WorkBuddy 一起，做出属于自己的「轻应用」。

AI 编程实战 · 目录