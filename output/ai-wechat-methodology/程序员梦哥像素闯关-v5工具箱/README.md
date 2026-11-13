# 程序员梦哥 · 像素闯关 v5 工具箱

2026-11-13按用户新构思新增候选，v3文字版、v4双图标版保留。三块砖并排，左右为普通砖，中间为唯一可顶的问号砖；人物只顶一次，七个工具图标从中砖内错峰弹出，向上和两侧散开后停住。片尾按最新反馈改为「分享AI、少踩坑」。

## 动作与文件

- 0.8秒顶中间砖；Codex、Claude、WorkBuddy、Kimi、用户图7、MiniMax、DeepSeek依次间隔0.04秒释放，每个图标用0.76秒完成上弹和回落，1.8秒全部停稳。左右普通砖不弹、不显示问号、不解锁。
- 保留发炮打怪、4.8—5.32秒降旗；5.36—5.68秒图标和三块砖一起退场，5.76—6.28秒渐显「分享AI、少踩坑」，完整静止两秒后淡出复位。
- intro.gif：1200×360、25fps、220帧、8.8秒循环。preview.html含375px文章宽度预览；topic.png、mobile-topic.png为工具散开定帧；poster.png、mobile.png为片尾；keyframes.png为十个时刻。
- 七枚图标均以24×24像素格、硬边透明度和最近邻方式以3倍整数比例放大至72px。*-pixel.png保存像素图标；icons/保存七份用户原图与附件名、接收日期、SHA256记录。

## 图标依据与复现

本轮先完成官方站点临时图标版本，用户随后提供七张指定图，最终全部替换为用户原图：WorkBuddy、紫蓝色Codex、Claude、Kimi、MiniMax、DeepSeek及第7张紫绿环形标记。第7张不猜产品名，以user07保存。相较早先文字清单，最终图中不额外加入GLM/Z.ai和豆包。icons/sources.json保存七张附件名与源文件指纹。只做小尺寸像素采样并接入既有Canvas动画，不重新生成或改绘Logo；原图逐张保留。

执行node build.cjs重建，复用v3动作表和Fusion Pixel字体，Canvas依赖五案v1目录，需FFmpeg。执行 python -m unittest discover -s scripts -p test_mengge_pixel_toolbox.py 验证。本版未新增生图，未改Skill、未设为默认、未发布。自动检查和关键帧目视审阅不替代连续观感、公众号后台保存重载及真机验收。
