# 折腾ai，分享实用玩法：文字闯关GIF

- `intro.gif`：1200×400，20fps，7.2秒，无限循环。
- `preview.html`：完整播放、重播、下载及375px手机宽度预览。
- `poster.png`、`keyframes.png`：终态与八个时刻的动作检查图。
- `build.cjs`、`manifest.json`：可重建源码、时间线及真实导出规格。
- `sprite-*.png`：复用此前根据用户同一头像生成的蓝卫衣角色；原始生成说明见相邻的「程序员拾梦闯关片头五案-v1」目录。
- `design-reference.png`：本聊天确认的静态视觉方向参考。

人物向右跑，起跳顶中ai砖块，灯泡道具出现；句子逐字点亮，人物落地后继续跑到右侧，挥手停留，最后柔和回到首帧。文字由Canvas绘制，保留「折腾ai，分享实用玩法」原样。

生成方式为已有imagegen角色素材＋Canvas逐帧渲染＋FFmpeg编码，不是Image 2.6原生动画输出。尚未操作公众号后台，微信转存与真机播放待验收。

重建：先在相邻「程序员拾梦闯关片头五案-v1」目录按其锁文件准备Canvas依赖，再运行 `node build.cjs`，需Windows微软雅黑字体和ffmpeg。`_frames/`为本地中间帧，不提交。
