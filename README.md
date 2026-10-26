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

## TikHub 本机凭据

公众号采集脚本 `scripts/download_benchmark_articles.py` 的凭据读取顺序为：显式 `--key-file`、`TIKHUB_API_KEY` 环境变量、本仓库 `.local/tikhub.json`。本机配置使用 JSON 对象，字段名为 `api_key`，值为用户自己的令牌。

`.local/tikhub.json` 仅保存在当前电脑，已加入 Git 忽略，禁止提交或在日志中记录令牌。后续在本知识库调用 TikHub 时，可复用脚本中的 `read_key()`；换电脑需要重新配置。可用 `git check-ignore .local/tikhub.json` 检查忽略规则。采集脚本默认目标是路人甲账号，不要用它的默认下载命令采集其他账号。

## 在 Obsidian 里看

把 `E:\code\webchat` 作为仓库（vault）打开，就能用双链、图谱视图和关系网查看整个知识库。`wiki/index.md` 是入口。

## 工作空间公众号技能

项目级技能安装在 `.agents/skills/`，来源为 https://github.com/yuxiang1987/dream-skills，各技能独立版本与全文件哈希见 `scripts/installed_skills.json`。

- `wechat-article-writing`：公众号案例策划、正文写作和改稿。
- `gzh-final-check`：最终定稿检查。
- `gzh-webchat-cover`：公众号横版封面。
- `md-wechat-layout`：Markdown 转微信公众号富文本排版；首次使用前在技能目录运行 `npm ci` 安装依赖。
- `gzh-topic-planning`：选题编辑，六类来源＋八类切入点，至多3候选推荐1个。
- `gzh-benchmark-deconstruct`：对标文章拆解，逐篇 source＋案例卡，默认增量入库。
- `gzh-benchmark-radar`：对标雷达，采集未入库文章、算阅读基线、聚同题事件、出候选素材；每日 9:30 由 Orca 自动化 `对标雷达每日9:30` 调用 `scripts/ingest.py daily`。

这些目录是工作空间安装副本，技能源码仍由 dream-skills 仓库维护。可通过 `$技能名` 调用。

## 注意

已移除工作区安装的 `wechat-viral-topic`，改用自有 `gzh-topic-planning`（公众号选题编辑）：从六类来源搜集线索，结合账号历史比较至多3个候选，推荐一个最小实测任务；不承诺爆款，不套用H5规则或统一评分门槛。技能源码与同步记录见 `scripts/installed_skills.json`；流水线S1使用新技能，正式标题交由 `wechat-article-writing`。

这个文件夹现在专门用作知识库，不建议再往里放无关代码项目，否则 `AGENTS.md` 的维护规范会跟着生效。
