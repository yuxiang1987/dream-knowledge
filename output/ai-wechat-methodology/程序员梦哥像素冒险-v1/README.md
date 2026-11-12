# 程序员梦哥 · 像素冒险 v1

用户在2026-11-12提供像素游戏画面作风格参考，要求制作「梦哥的AI冒险」候选。新名字为「程序员梦哥」；副标题为「折腾 AI，分享实用玩法」。

蓝紫天空、像素云、绿色小山、砖块地面与橙色招牌。左侧蓝卫衣小人蓄力、起跳顶AI砖、落地缓冲；星星飞到招牌旁，停留后淡去，回到起始画面。标题和副标题始终可见。

- `intro.gif`：1200×360、25fps、140帧、5.6秒、无限循环。
- `preview.html`：动图、重播、下载、375px文章预览与关键帧。
- `poster.png`、`mobile.png`：最终停留画面与375px定帧；`keyframes.png`：八个动作时刻。
- `manifest.json`：动作时间线与验收状态；`build.cjs`：重建源码。
- `sprite-idle.png`、`sprite-jump.png`：复用既有蓝卫衣角色素材，与旧资源逐字节一致。

## 制作与验证边界

场景与运动由Canvas代码绘制、FFmpeg编码GIF，复用此前imagegen制作的角色素材，没有新调用生图或Image 2.6原生GIF。该版未交付SVG，不将GIF误称为SVG动画。

起跳蓄力0.56—0.9秒，0.9—1.48秒上升，1.48秒顶砖，1.96秒落地，至2.32秒回稳。星星1.48—2.78秒飞向招牌，停留至4.64秒再淡去。5.12秒后静止回到首帧构图，循环末帧与首帧相同。

本地查看关键帧、375px定帧并检查导出；用户审美反馈、公众号后台保存重载及真机播放待验收。未改Skill、未设为默认片头、未发布。

## 重建

需Node.js、FFmpeg、微软雅黑和既有`../程序员拾梦闯关片头五案-v1/node_modules/@napi-rs/canvas`。执行`node build.cjs`；中间帧在忽略的`_frames/`中。仓库根目录运行`python -m unittest discover -s scripts -p test_mengge_pixel_adventure.py`。
