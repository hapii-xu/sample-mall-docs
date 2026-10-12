# sample-mall-docs

Sample Mall（示例商城 · 山野茶铺）的需求与项目文档仓库。PRD、迭代说明、需求池都在这里，可以直接作为 Tapestry 平台**知识库**的仓库来源导入。

| 仓库 | 说明 |
|---|---|
| [sample-mall-web](https://github.com/hapii-xu/sample-mall-web) | 前端：Vue 3，PC 官网 `/` + 移动 H5 `/m` |
| [sample-mall-server](https://github.com/hapii-xu/sample-mall-server) | 后端：Spring Boot 微服务（gateway / user / product / order） |
| sample-mall-docs（本仓库） | 需求文档 |

## 目录

```
prd/
  v0.1/
    PRD-v0.1.md          迭代 0.1 的 PRD（功能基线，需求编号 REQ-xxx）
    requirements.csv     由 PRD 生成，可导入平台「研发协同 → 工作项 → 导入（需求）」
iterations/
  v0.1.md                迭代 0.1 说明：目标、范围、交付物、验证结果
backlog.md               需求池：后续迭代候选功能
scripts/prd_to_csv.py    PRD → requirements.csv
```

## 约定

- **需求编号** `REQ-xxx` 跨版本稳定、不复用；新迭代新增需求顺延编号，修改已有需求时在新版本 PRD 中保留原编号并注明变更。
- **一迭代一份 PRD**：`prd/v<版本>/PRD-v<版本>.md`，内容是该迭代结束时的完整功能基线（不是增量）。
- 平台迭代名与文档版本对应：`v0.1 初始版本` ↔ `prd/v0.1`。
- PRD 修改后重新生成 CSV：`python scripts/prd_to_csv.py prd/v0.1/PRD-v0.1.md "v0.1 初始版本"`。
