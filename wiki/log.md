# 操作日志

> 按时间追加，格式：`## [YYYY-MM-DD] 操作类型 | 标题`

## [2026-09-29] init | 知识库初始化

- 建立 `raw/`、`wiki/`、`templates/`、`scripts/` 结构
- 写入 `AGENTS.md` 维护规范（schema 层），三位一体：raw 只读、wiki 由 AI 维护、规范共同演进
- wiki 下设 sources、concepts、entities、topics、comparisons 五类目录
- 新增结构体检脚本 `scripts/wiki_lint.py`

## [2026-09-29] ingest | Karpathy LLM Wiki 原文

- 原始资料：`raw/karpathy-llm-wiki.md`
- 新增 [[sources/Karpathy-LLM-Wiki原文]]
- 新增 [[concepts/LLM-Wiki模式]]、[[concepts/知识库三层架构]]、[[concepts/知识库三个操作]]
- 新增 [[comparisons/RAG与LLM-Wiki]]
- 记录评论区提出的"编译产物会自信地出错"风险，作为后续人工抽查的依据

## [2026-09-29] ingest | 公众号定位与写作风格规范

- 原始资料：`raw/style-card.md`、`raw/style-dna.md`（来源为本机公众号生产线文档的快照）
- 追加原始资料：`raw/account-profile.md`（账号档案快照，补充内容承诺、边界和待确认项）
- 新增 [[sources/公众号定位与写作风格规范]]
- 新增 [[concepts/公众号写作风格DNA]]
- 新增 [[entities/程序员拾梦]]
- 新增 [[topics/公众号内容生产线]]
