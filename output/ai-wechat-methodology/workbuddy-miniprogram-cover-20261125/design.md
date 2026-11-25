# WorkBuddy 健身小程序文章封面

- 日期：2026-11-25。
- 原稿：`raw/article/程序员梦哥/WorkBuddy + huashu skill 手搓健身小程序（附提示词）.md`，只读。
- 文章标题：不用敲一行代码！手把手教你用 WorkBuddy 做微信小程序，从高保真原型到手机真机能用（附全套提示词）。
- 当前主标题：`不用敲一行代码` / `做微信小程序`；副标题：`WorkBuddy · 从原型到手机真能用`。按用户反馈，直接提取文章标题中的开发门槛、任务与可用成果，增强封面与标题的关联。
- 命题：不用敲代码，也能把小程序从原型做到手机可用。炭黑与青柠绿沿用正文方案 C 的颜色，右侧从线框走向实体手机，能量环呼应健身案例。
- 底图：内置 `imagegen` 生成无字示意画面；手机界面为抽象视觉，不是产品实际截图。不含正式上线、免审核长期可用等主张。
- 排字：调用 `gzh-webchat-cover/scripts/compose_cover.py`，本目录包装脚本仅增加明确换行；微软雅黑粗体，保留产品官方大小写。
- 当前交付：`cover-v2.png`，900×383，RGB PNG；`thumbnail-v2.png` 为缩略检查图。`background.png` 为沿用的无字底图，未重新生图。保留第一版 `cover.png` 与 `thumbnail.png` 供对照。
- 验证：`python output/ai-wechat-methodology/workbuddy-miniprogram-cover-20261125/verify_delivery.py`；人工检查完整图及缩略图。未验证公众号各展示位的裁剪。

## 最终底图提示词

```text
Create a premium editorial cover BACKGROUND for a Chinese WeChat tutorial about building a fitness mini-program by chatting with WorkBuddy. Wide cinematic banner, aspect ratio 2.35:1, aim 1800x766. No text anywhere, no letters, no numbers, no logos, no watermarks.

Composition: left 51 percent is quiet near-black warm charcoal negative space, subtle matte paper-like texture, mostly flat dark tones for later typography. All objects in the right 47 percent, kept within the top and bottom 6 percent safe margins. One hero physical smartphone, entire phone silhouette visible, tall portrait orientation, front facing with very slight premium product photography perspective, centered at about 76% of width, height 83% of canvas, not clipped. Minimal graphite metal edges with gentle silver rim light. Dark screen shows an ABSTRACT, TEXT-FREE fitness dashboard: one large luminous acid lime circular activity progress ring in the upper middle, three tiny metric indicator dots below, simple restrained charcoal rounded rectangle cards, a wide lime action pill, four small minimalist bottom navigation marks. All screen content is abstract visual suggestion, not a replica product UI; NO text, NO fake text, NO numbers. A very faint transparent grey wireframe rectangle behind and slightly left of the phone echoes the same ring, with a subtle thin arrow leading to the solid phone, visually suggesting prototype becoming usable app. Do not add a second physical phone. Matte black podium under the phone, soft contact shadow, thin acid lime light reflection on the stage, restrained soft warm grey studio light. Color palette #15181D, #1D2229, off-white specular accents, acid lime #C6F24E. Premium calm technology tutorial cover, precise composition, realistic 3D studio product shot, sharp edges, restrained bloom, editorial elegance. No people, no robot, no code, no keyboard, no stickers, no extra decorative icons, no blue or purple gradient.
```
