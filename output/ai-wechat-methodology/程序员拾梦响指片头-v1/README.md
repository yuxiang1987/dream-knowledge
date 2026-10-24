# 程序员拾梦 · 响指片头 v1

这一版把「跳一跳」改成固定站位的像素人物：人物留在左侧，右侧先显示「程序员拾梦」；响指时出现蓝色霓虹环、像素火花和轻微故障抖动，随后眨眼，标题退场并切换为「折腾 AI，分享实用玩法」。循环末尾平滑回到首帧。

- `intro.gif`：1246×300，7.2秒，20fps，144帧，无限循环。
- `intro.svg`：嵌入角色素材的独立SVG；`intro.wechat.html`：可复制片段。
- `preview.html`：动图、响指、眨眼、切换后和副标题定帧，以及375px手机宽度预览。
- `jumper.png`：复用已确认的透明全身像素角色；`build.cjs`：可重建源码；`motion.json`：时间线数据。

本地已检查角色固定在左侧、响指环与火花、眨眼遮罩、标题切换、GIF首尾闭合和SVG资源完整性。公众号后台和真机微信效果仍待粘贴验收。

执行 `node build.cjs` 可重建；自动化检查在仓库根目录执行 `python -m unittest discover -s scripts -p test_brand_snap_intro.py`。
