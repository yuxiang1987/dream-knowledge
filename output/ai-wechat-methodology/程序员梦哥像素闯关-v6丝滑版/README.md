# 程序员梦哥 · 像素闯关 v6 动效优化版

2026-11-13按用户要求安装greensock/gsap-skills并实际接入GSAP优化动作。v5三砖工具箱保留对照；构图、角色、用户指定的七枚图标和「分享AI、少踩坑」文案沿用。本版不新增生图。

## 动效变化

- 真实GSAP 3.15.1暂停时间线驱动：统一标签组织准备、顶砖、散开、降旗、清场和片尾，每帧按固定时间seek取值，再用原Canvas场景绘制，FFmpeg编码GIF。没有依赖实时时钟或计时器截屏。
- 角色顶砖前短促下蹲，起跳拉伸，落地压缩回弹；中间砖上弹14px，再轻微回落归位。仍然只顶中间一块。
- 图标从中心向外依次释放，次序为中心、邻近两侧、外侧，再到最远两枚，间隔0.045秒。各枚图标分别控制横向减速展开、纵向先升后落、0.5倍至正常大小、轻微旋转回正；1.91秒全部停稳，不持续乱晃。七枚原始像素图与v5完全一致。
- 降旗改用渐入渐出的速度曲线，4.8—5.44秒完成；5.46—5.78秒砖和图标退场；5.84—6.36秒口号渐显并上移，6.36—8.36秒完整静止两秒，再淡出复位。复位处理保持首尾相同。
- 从25fps提高到50fps：1200×360、440帧、8.8秒无限循环GIF，1676328字节，每帧20ms。编码帧率不代表所有微信客户端都会以相同速度实际播放。

## 文件与复现

- intro.gif为新版；preview.html提供重播、375px文章预览及上一版GIF对照。
- topic.png、mobile-topic.png为散开后定帧；poster.png、mobile.png为片尾；keyframes.png为十个时刻。
- motion.cjs是实际GSAP动作时间线；build.cjs复用场景、生成逐帧PNG并编码；manifest.json保存每帧状态、GSAP版本及时间标签。
- package.json、package-lock.json锁定GSAP；在本目录执行npm ci --ignore-scripts，然后npm run build。既有Canvas依赖来自五案v1目录，字体与动作表复用v3，七张用户源图复用v5，另需FFmpeg。_frames和node_modules均忽略。
- 根目录运行python -m unittest discover -s scripts -p test_mengge_pixel_gsap.py。新增检查真实依赖与随机顺序取帧一致性、中心向外出场、图标旋转时不裁边及停稳后无重叠、与v5图标逐字节相同、退场次序、旧版本复位时刻不会提前复位、50fps实际GIF延时、首尾闭合与片尾两秒静止。

## 技能安装

使用Codex自带skill-installer从 https://github.com/greensock/gsap-skills 全局安装8个技能，目录位于C:/Users/Administrator/.codex/skills/下：gsap-core、gsap-timeline、gsap-scrolltrigger、gsap-plugins、gsap-utils、gsap-react、gsap-performance、gsap-frameworks。下轮对话可自动识别；本轮已直接读取并应用core、timeline、performance指导。skills-install.json记录安装目录、源仓库和SKILL.md指纹。没有修改公众号Skill或dream-skills源码仓库。

相关23项自动检查通过，并目视检查关键帧与手机定帧。逐帧、文件和时间线检查不替代用户连续观感、公众号后台保存重载和真机播放验收。未设为默认片头、未发布。
