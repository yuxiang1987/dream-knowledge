# 程序员梦哥 · 像素闯关 v4 图标版

2026-11-13按用户要求制作的对照候选，v3文字版原样保留。两次顶砖改为弹出Codex黑底终端徽章与Claude橙底放射星，均为24×24格手绘像素化标记、3倍最近邻放大至72px，不是官方原始Logo。参照产品入口：https://openai.com/index/introducing-the-codex-app/ 与 https://claude.com/product/overview 。

- 0.64秒、2.04秒顶砖；图标从砖内弹起，0.48秒内回落停稳，2.52秒完整出现。砖面留空，无GPT Image 2.6文字与金币。
- 2.84秒、3.72秒发炮，分别在3.16秒、4.04秒命中；4.8—5.32秒降旗。
- 5.36—5.68秒图标和砖淡出；5.76—6.28秒渐显「折腾AI、少踩坑」，6.28—8.28秒静止两秒，随后淡出复位。
- GIF：1200×360、25fps、220帧、8.8秒循环。preview.html含375px对照预览；topic.png与mobile-topic.png为双图标定帧；poster.png与mobile.png为片尾；keyframes.png含十个时刻。

复用v3的16姿势动作表和Fusion Pixel字体，依赖保持相对路径，无新增生图。执行node build.cjs重建，Canvas包沿用五案v1目录，需FFmpeg。仓库根目录运行 python -m unittest discover -s scripts -p test_mengge_pixel_icons.py 。原v3回归测试仍适用。

仅为本地候选。关键帧审阅和自动检查不等于连续动图审美、公众号后台保存重载与真机验收；未改Skill、未设为默认、未发布。
