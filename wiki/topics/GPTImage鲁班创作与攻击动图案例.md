---
title: GPTImage鲁班创作与攻击动图案例
type: topic
tags: [公众号, GPTImage, 鲁班, 动图, 案例策划]
status: 进行中
sources: []
created: 2026-11-13
updated: 2026-11-13
---

# GPTImage鲁班创作与攻击动图案例

## 用户决定与来源

2026-11-13用户明确取消H3 Image选题，改为GPT Image 2.6，要求助手直接生成攻击特效GIF。沿用已喜欢的大鱼鲁班形象；前序皮肤、CP及CAD风格道具图由内置imagegen生成，不能据此认定它们使用了GPT Image 2.6。此前研究保留在[[topics/H3Image更新调研与案例建议]]。

sources为空：依据本次用户指令、工具返回、本机产物检查及下列在线官方文档，没有新增或修改raw。

## 当前入口与实际制作

[OpenAI官方图像指南](https://developers.openai.com/api/docs/guides/image-generation#generate-animated-gif-output)当次明确2.6支持图像API的GIF输出，图像编辑端点可用参考图。当前内置imagegen仅暴露提示、参考图和透明背景参数，没有模型ID、输出格式或帧参数。本机相关环境变量名称检查未发现OpenAI密钥，未搜读其他应用凭据，未调用独立OpenAI API。

1. 请求直接生成GIF，工具实际返回一张PNG，不当作动图交付。
2. 生成2列4行、8幅攻击关键帧：待机、蓄力、水弹出膛、飞行、飞出画面、消散和恢复。返回1024×1536静态帧图，模型ID未暴露。
3. FFmpeg按格提取关键帧、编码循环GIF并导出MP4。实际方式是“生成式关键帧＋本地逐帧合成”，不是已验证的GPT Image 2.6原生GIF。

本机Git忽略目录中的产物：

- [攻击循环GIF](../../output/gpt-image-luban-attack/attack-loop.gif)
- [MP4预览](../../output/gpt-image-luban-attack/attack-loop.mp4)
- [生成关键帧](../../output/gpt-image-luban-attack/attack-keyframes.png)
- [验证JSON](../../output/gpt-image-luban-attack/validation.json)

文件读取确认：GIF格式、512×384、64个编码帧、2560毫秒、无限循环、960411字节。8幅生成关键帧编码成多个定时帧，不宣称模型独立生成64个动作。已抽看帧图与GIF一帧，未记录连续播放人工审片结论，不宣称零漂移、首尾完全无缝或平台粘贴已通过。

## 尚未完成的验证

当前可用的是创作过程和真实GIF合成样片。文章若主张GPT Image 2.6原生GIF，仍需能指定模型的入口/API、真实多帧输出和请求/界面证据；本样片不能替代。转题不等于原生GIF测试完成，不等于正文已完成或已发布。

## 相关页面

- [[topics/H3Image更新调研与案例建议]]
- [[sources/卡尔Image动图玩法与一致性边界文章拆解]]
- [[topics/证据与边界库]]
