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

## 鲁班七号四技能调研与特效概念

用户要求先调研技能、再分别生成相应动图。2026-11-13读取[王者荣耀官网鲁班七号页](https://pvp.qq.com/web201605/herodetail/112.shtml)技能介绍，并与近期第三方技能整理交叉检查。确认为一个被动与三个主动；官网页面另有明显不匹配的加点标签，且数值与第三方记录不一致，本次不采用数值、不称当前客户端完整复刻，只沿用稳定的技能名称、触发和动作机制。

| 技能 | 查到的核心机制 | 本次大鱼同人特效 |
| --- | --- | --- |
| 被动：火力压制 | 第五次普攻或技能后的下一次普攻强化为扫射，扫射有三段伤害 | 只展示触发后的三段青蓝泡泡/水能量扫射，不把短片写成完整普攻计数演示 |
| 一技能：河豚手雷 | 向指定位置抛掷，范围伤害与减速，并获取命中目标视野 | 手投小鲸鱼外形手雷，经过抛物线落地，爆出圆形水花与涟漪；没有额外眩晕 |
| 二技能：无敌鲨嘴炮 | 沿方向发射炮弹，能击退身前近距离目标 | 单枚鲸形水能量弹直线飞行，近处无脸训练假人被推开；不把远距离目标都画成必然击退 |
| 大招：空中支援 | 召唤向前移动的飞艇，提供范围视野并持续投弹 | 鲸鱼飞艇在上方移动，支援圆圈跟随，向圈内连续落下水弹；是缩短的特效演示，不等同游戏持续时间或精确投弹频率 |

制作使用内置imagegen分别生成4张2×4关键帧图，每组8幅图，人工抽看姿态顺序和主要视觉区别；FFmpeg切格、按节奏编码四份GIF/MP4。脸、装备和细节可能有生成漂移，不宣称逐帧完全一致；视野和减速等游戏逻辑仅作视觉意象，没有运行游戏或验证伤害判定。仍不是已验证的GPT Image 2.6原生GIF。

交付在本机Git忽略目录：

- [四技能合集GIF](../../output/gpt-image-luban-skills-v1/four-skills.gif)
- [四技能合集MP4](../../output/gpt-image-luban-skills-v1/four-skills.mp4)
- [被动扫射](../../output/gpt-image-luban-skills-v1/passive.gif)
- [一技能抛掷](../../output/gpt-image-luban-skills-v1/skill1.gif)
- [二技能直射与近身击退](../../output/gpt-image-luban-skills-v1/skill2.gif)
- [大招移动投弹](../../output/gpt-image-luban-skills-v1/skill3.gif)
- [提示词](../../output/gpt-image-luban-skills-v1/生成提示词.md)

文件目标与实检：前三组各512×384、2秒、50编码帧；大招512×384、2.72秒、68编码帧，全部无限循环。编码帧数不是模型独立生成动作数；完整性检查、逐帧不同状态和总时长记录在目录manifest与validation中。未进行实际游戏或微信公众号粘贴验证。

## 相关页面

- [[topics/H3Image更新调研与案例建议]]
- [[sources/卡尔Image动图玩法与一致性边界文章拆解]]
- [[topics/证据与边界库]]
