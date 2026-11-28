# WorkBuddy × animate 公众号封面

- 日期：2026-11-28。
- 文章：[一个神仙 Skill，让WorkBuddy出 7 种风格 Vibe 科普动画(附实操)](https://zcnocjmf11ov.feishu.cn/wiki/JiLrwE9l0i7kRDkqTxOccvFpn1f?fromScene=spaceOverview)。通过飞书页面读取标题、导语及四个案例。
- 主标题：7 种风格／科普动画。副标题：WorkBuddy × animate Skill。
- 设计：炭黑背景，左文右图；右侧一组扇形画框呈现正文的数学、手绘、像素与剪纸案例，突出多画风的创作成果。画框为概念插画，不是真实成片截图。正文实操为四个案例，七种指文章所述技能支持的风格数。
- 工具：gzh-webchat-cover；内置 image_gen 生成无字背景；技能 compose_cover.py 处理尺寸和遮罩，compose.py 用微软雅黑叠加精确中文。
- 成品：cover.png，900×383，RGB PNG；thumbnail.png，360×153 缩略检查图。
- 验证：test_cover.py 两项测试通过，检查 PNG 格式尺寸及文字边界；人工查看成品与缩略图，标题可读、四种画风可辨。没有进行公众号上传或平台裁剪实测。
- 复现：在仓库根目录运行 `python output/wechat-cover-animate-20261128/compose.py`；验证运行 `python output/wechat-cover-animate-20261128/test_cover.py`。

## 背景生成提示词

```text
Use case: ads-marketing. Asset type: text-free background for a Chinese WeChat article cover, final aspect ratio 2.35:1, wide panoramic banner. Primary request: portray the creative result of making science-explainer animation videos in multiple visual styles, using a single elegant fanned deck of four animated-film frames as the main subject. Layout: LEFT 48% is empty calm near-black charcoal with subtle warm studio falloff, reserved for a large two-line title added later. On RIGHT 52%, a beautifully art-directed compact fan of FOUR large landscape picture cards, filling the right half without crossing the outer 5% safe margins. Each card should have a distinctly different artwork style and simple easily recognizable subject. Front largest card: bold premium pixel art of a microchip on a navy grid with orange pixel details and a tiny charming orange pixel creature. Second card slightly above: cream lined sketchbook drawing of a globe and a sailboat with a small orange hand-drawn character. Third card: black-background elegant cyan/gold vector rising exponential curve and folded paper towards a small moon. Fourth card: layered cut-paper collage of a seashell, coin and paper note, warm coral/teal/cream tactile paper. Unify them as one sculptural fan/deck rather than four isolated panels, no screen hardware and no UI chrome. A subtle timeline-like trail of tiny illuminated squares under the deck may suggest animation. Style: high-end editorial mixed-media product still life with sharp beautiful illustrated frames, crisp cut edges, restrained soft realistic shadows, tactile materials, sophisticated depth, energetic but uncluttered. Palette: charcoal and warm ivory with one vibrant orange/coral accent, cyan limited to card art. Lighting: soft cinematic studio light, no neon. All cards large enough to read at thumbnail size, avoid microdetail. NO text, NO letters, NO numbers, NO typography, NO logos, NO watermark, NO robots, NO code rain, NO purple gradients. This is a conceptual illustration of the article's four case themes, not a screenshot.
```
