# 程序员拾梦 · 闯关片头五案

按用户2026-11-09提供的新头像制作：黑发、圆框眼镜、蓝色卫衣、胸前星星；由内置 image_gen 延展为透明全身像素角色，四个动作共用一张角色表。游戏场景及动画由 Canvas 代码制作。

打开 [五案动画预览](preview.html)，每版都有重播、GIF/MP4下载、关键帧和375px手机宽度预览。

| 方案 | 小剧情 | 动画 |
| --- | --- | --- |
| 01 顶问号砖块 | 跑入、跳跃顶砖，AI电脑弹出并展开品牌 | [GIF](01-question/intro.gif) |
| 02 水管传送 | 出管、跑动、入管，再从另一出口进入AI工作台 | [GIF](02-pipe/intro.gif) |
| 03 收集金币 | 连跳收集五枚金币，依次变成「程序员拾梦」 | [GIF](03-coins/intro.gif) |
| 04 跳台升旗 | 两级跳台、跨越缺口、升起品牌旗帜 | [GIF](04-flag/intro.gif) |
| 05 吃星星变身 | 星星弹出，追到星星后跳跃并拖出彩色像素尾迹 | [GIF](05-star/intro.gif) |

规格：1200×360，20fps，8秒，无声循环；每版末尾交叉淡回初始场景。GIF用于动效候选审阅，MP4便于播放检查；本地导出与关键帧已检查，公众号后台转存、真机显示和实际文章适配尚未验收。五案尚待用户选择，不表示已采用。按本轮先看效果的节奏保留旧版，待用户选定后处理旧文件。

`avatar-reference.png`是用户输入的原头像；`spritesheet.png`是生成的角色表；`sprite-*.png`是按四个单元裁出的动画素材；`prompts.json`记录完整生图提示词；`manifest.json`记录规格和时间线；`comparison.png`为每版定格与动作帧对照。

重建：在本目录执行 `npm ci --no-audit --no-fund`，然后 `node build.cjs`。需要 Node、FFmpeg，以及Windows微软雅黑和Consolas字体。

验证：仓库根目录执行 `python -m unittest discover -s scripts -p test_brand_platformer_intros.py`。
