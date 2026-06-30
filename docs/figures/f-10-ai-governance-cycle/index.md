---
title: "F-10: AIガバナンス運用サイクル"
source_path: "figures/f-10-ai-governance-cycle.md"
order: 490
book_section: "figures"
---
# F-10: AIガバナンス運用サイクル

```mermaid
flowchart LR
    INTAKE[Use Case Intake<br/>利用申請]
    INV[AI System Inventory<br/>台帳化]
    CLASS[Risk Classification<br/>G0〜G5分類]
    APPROVE[Approval Workflow<br/>承認・例外・ADR]
    OPERATE[Operate<br/>運用・教育・権限付与]
    MONITOR[Monitor / Audit<br/>KPI・証跡・監査]
    REVIEW[Quarterly Review<br/>改善・棚卸し]
    RETIRE[Retire / Continue<br/>廃止・継続・拡大]

    INTAKE --> INV --> CLASS --> APPROVE --> OPERATE --> MONITOR --> REVIEW --> RETIRE
    RETIRE -->|新規・変更| INTAKE
    REVIEW -->|改善要求| OPERATE
```

AIガバナンスは、AI利用を止めるためではなく、安全にスケールさせるための運用サイクルである。低リスク利用は速く通し、高リスク利用は台帳、承認、証跡、教育、廃止まで管理する。

| サイクル | 主な問い | 成果物 |
|---|---|---|
| Intake | 何にAIを使うのか | AI Use Case Intake |
| Inventory | 誰が何を使っているか | AI System Inventory |
| Classification | どの統制レベルか | Governance Level Matrix、AI Risk Register |
| Approval | 誰が何を承認するか | Approval Workflow、AI System ADR |
| Operate | 教育・権限・運用は十分か | AI Training Register、Office Hour Runbook |
| Monitor | 品質・リスク・コストは見えているか | KPI Dashboard、Audit Evidence Pack |
| Review | 続けるか、直すか、止めるか | Quarterly Review Report、AI Retirement Plan |

第10章では、このサイクルをAI CoE、部門責任者、情シス、法務、セキュリティの運用責任へ接続する。
