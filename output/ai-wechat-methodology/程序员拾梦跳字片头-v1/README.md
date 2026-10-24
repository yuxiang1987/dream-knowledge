# 程序员拾梦 · 跳字片头 v1

根据用户「像跳一跳一样，在文字上跳」的方向制作。沿用黑发、圆框眼镜、笑脸、蓝衣服的像素身份，用 image_gen 将原像素头像延展为完整小人，再以原生代码制作动画。

动作：蓄力下蹲 → 逐字跳跃 → 被踩中的字亮蓝色并回弹 → 落地像素碎屑 → 沿原路返回。文字是「程序员拾梦」，副标语是「折腾 AI，分享实用玩法」。这是一版候选，尚待用户选择。

- `intro.gif`：1246×300，8秒，20fps，160帧，无限循环，约0.93MB。
- `intro.svg`：独立SVG，嵌入完整头像素材，SMIL循环，不依赖脚本、外链图片或字体。
- `preview.html`：动图、起跳/腾空/落地定帧与375px宽度预览。
- `intro.wechat.html`：包裹SVG的HTML片段；微信编辑器是否保留相关动画尚待粘贴验收。
- `poster.png` 等PNG：关键帧；`jumper.png`：透明全身角色；`prompts.json`：生图提示词。
- `motion.json`：运动数据；`build.cjs`：可重建源码；`_frames/`：忽略的中间帧目录。

已检查本地GIF播放、关键帧、落脚位置、角色不出画、首尾闭合及SVG资源完整性。尚未在公众号后台或真机微信验收。

重建需要 Node.js、`@napi-rs/canvas`、FFmpeg，以及 Windows 微软雅黑粗体。执行 `node build.cjs`；自动化验收在仓库根目录执行 `python -m unittest discover -s scripts -p test_brand_jump_intro.py`。旧像素片头和三款右侧动效保留在相邻目录。
