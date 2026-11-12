# 程序员梦哥 · 简洁片头 v1

2026-11-12，用户明确当前新公众号名为「程序员梦哥」，要求按已讨论的简洁方案出一版。旧「程序员拾梦」历史文件保留，新片头使用新名字。

- 左侧固定既有蓝卫衣圆形头像，右侧固定「程序员梦哥」。
- 下方「折腾 AI」与「分享实用玩法」各停留2秒，以0.6秒缓动、16px轻微上移交接，5.2秒循环。1200×260，375px宽显示时高81.25px。
- `intro.svg`：内嵌既有头像、文字转路径，SMIL（SVG自身声明式动画），无脚本、外链或字体依赖。
- `intro.gif`：同构图、同时间线的25fps导出；130帧，5.2秒，无限循环。
- `preview.html`：SVG、GIF和375px文章预览；`intro.wechat.html`为候选SVG正文片段。
- `poster.png`、`tagline-b.png`：两句文案定帧；`motion.json`：时间线和验收状态。
- `svg-poster.png`：原生SVG栅格化首帧检查；`mobile-comparison.png`：375px宽两种文案对照。浏览器工具拒绝本地file协议，未绕过限制，也未声称完成浏览器动态验收。

头像按原文件复制自`../程序员拾梦闯关片头五案-v1/avatar-reference.png`；通过SVG视口和Canvas绘制源区域使用头像，未编辑原始头像。没有调用或声称Image 2.6原生GIF生成。SVG与GIF分别由SMIL、Canvas/FFmpeg实现，尚未在公众号后台完成粘贴、保存重载和真机验收；本版为待用户审美反馈的候选。

## 重建

需要本机Node.js、FFmpeg、微软雅黑及既有`../程序员拾梦闯关片头五案-v1/node_modules/@napi-rs/canvas`。执行`node build.cjs`；中间帧放在忽略的`_frames/`。在仓库根目录执行`python -m unittest discover -s scripts -p test_mengge_simple_intro.py`。
