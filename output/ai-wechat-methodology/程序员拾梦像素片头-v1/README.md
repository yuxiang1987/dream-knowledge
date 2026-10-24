# 程序员拾梦像素片头 v1

用户在2026-10-24提供自己的卡通头像，要求去除右下角豆包AI水印，并参照公众号文章开头制作像素风片头。两次头像编辑使用内置 image_gen，动画通过本目录 `build.cjs` 的原生 Canvas 与 SVG SMIL 制作，没有复制参考账号的角色、文字或动画源代码。

## 成品

- `avatar-clean.png`：去水印卡通头像。
- `avatar-pixel.png`：透明背景像素头像，保留黑发、圆眼镜和蓝色T恤。
- `intro.gif`：1246×220，6秒、20fps、无限循环，约1.6MB。
- `intro.svg`：内嵌头像的独立SVG动画，无外部字体、脚本或图片依赖。
- `intro.wechat.html`：仅包含片头的HTML片段。
- `preview.html`：完整尺寸、375px宽度预览，以及文字与方块定帧切换。
- `poster.png`、`cube-frame.png`：文字和方块两个阶段的定帧图。
- `prompts.json`：两次头像编辑的完整提示词。

文字为「程序员拾梦」「折腾 AI，分享实用玩法」。配色取自头像蓝衣服，时间线为文字停留、粒子散开、线框至实体方块旋转、文字重新聚合。第一帧和最后一帧回到相同构图。

## 使用

打开 `preview.html` 查看；GIF 可作为文章图片素材，SVG与HTML片段供编辑器集成。已核对本地浏览器的SVG显示、GIF导出和375px宽度预览；尚未在公众号后台保存或真机微信中验证，不能据本地结果宣称微信兼容已通过。

## 重新生成

需要 Node.js、`@napi-rs/canvas`、ffmpeg，以及 Windows 的微软雅黑粗体。源码中的字体路径对应本机，换系统需改为可用中文字体。设置 Node 包搜索路径后执行 `node build.cjs`，会重建本目录动画与预览。中间帧在 `_frames/`，已加入 Git 忽略。

参考形式来自用户指定文章：<https://mp.weixin.qq.com/s/gFnRQIwtVoBargkfc3lFFQ>。参考代码仅用于确认4秒循环、像素文字、粒子、透视网格与立方体的形式；本版独立实现为6秒循环。
