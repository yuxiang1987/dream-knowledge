# 自生长知识库

按 Karpathy 的 LLM Wiki 模式搭建的个人知识库。人负责丢资料和提问，AI 负责把资料编译成互相链接的知识页并持续维护。

## 目录

| 目录 | 内容 | 谁改 |
| --- | --- | --- |
| `raw/` | 原始资料，只读的事实来源 | 人放进去 |
| `wiki/` | AI 编译出来的知识页 | AI 维护 |
| `templates/` | 页面模板 | 人 + AI |
| `scripts/` | 检查脚本 | 人 + AI |
| `AGENTS.md` | 维护规范，整个库的「宪法」 | 人 + AI |

## 三种用法

**入库**：把文章、视频字幕、截图说明丢进 `raw/`，然后说一句「入库 raw/文件名」。AI 会读资料、写摘要页、更新相关概念页、刷新索引和日志。

**提问**：直接问。AI 会先查 `wiki/index.md` 定位页面，再带来源回答。有价值的答案会被写回知识库。

**体检**：说「体检知识库」，或直接运行 `python scripts/wiki_lint.py`。检查断链、孤页、缺失字段、来源文件是否存在等问题。

脚本输出为 UTF-8。在 Windows PowerShell 5.1 里如果看到乱码，先执行 `chcp 65001` 再运行。

## 在 Obsidian 里看

把 `E:\code\webchat` 作为仓库（vault）打开，就能用双链、图谱视图和关系网查看整个知识库。`wiki/index.md` 是入口。

## 工作空间公众号技能

项目级技能安装在 `.agents/skills/`，来源为 https://github.com/yuxiang1987/dream-skills，安装版本 `08267413a872aaf2a389cff65c29848497287afc`。

- `wechat-article-writing`：公众号案例策划、正文写作和改稿。
- `gzh-final-check`：最终定稿检查。
- `gzh-webchat-cover`：公众号横版封面。
- `md-wechat-layout`：Markdown 转微信公众号富文本排版；首次使用前在技能目录运行 `npm ci` 安装依赖。

这些目录是工作空间安装副本，技能源码仍由 dream-skills 仓库维护。可通过 `$技能名` 调用。

## 注意

另已安装本地 WorkBuddy 技能 `$wechat-viral-topic`（10万+爆款选题制造机），目录为 `.agents/skills/wechat-viral-topic/`，用于选题、标题与内容策划。来源为 `C:\Users\Administrator\.workbuddy\skills\wechat-viral-topic`，本次原样安装，未优化技能。

这个文件夹现在专门用作知识库，不建议再往里放无关代码项目，否则 `AGENTS.md` 的维护规范会跟着生效。
