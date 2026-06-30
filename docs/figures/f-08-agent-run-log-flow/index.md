---
title: "F-08: Agent Run Logの流れ"
source_path: "figures/f-08-agent-run-log-flow.md"
order: 470
book_section: "figures"
---
# F-08: Agent Run Logの流れ

![F-08: Agent Run Logの流れ](../assets/f-08-agent-run-log-flow.svg)

<details markdown="1">
<summary>Mermaidソース</summary>

```mermaid
flowchart LR
    RC[Request Contract<br/>目的・成果物・制約]
    CP[Context Pack<br/>前提・資料・鮮度]
    TB[Task Brief<br/>委任単位]

    RUN[Agent Run Log<br/>Run ID / Correlation ID]

    TE[Trace Event Record<br/>モデル応答・状態遷移]
    TL[Tool Execution Log<br/>ツール・引数・結果]
    AL[Approval Log<br/>承認者・判断・理由]
    RL[Review / Evaluation Log<br/>指摘・判定・スコア]

    RR[Run Review Report<br/>何が起きたか]
    IB[Improvement Backlog<br/>次に直すこと]

    RC --> RUN
    CP --> RUN
    TB --> RUN
    RUN --> TE
    RUN --> TL
    RUN --> AL
    RUN --> RL
    TE --> RR
    TL --> RR
    AL --> RR
    RL --> RR
    RR --> IB
    IB --> RC
    IB --> CP
    IB --> TB
```

</details>

ログは、最終出力を保存するだけでは不十分である。依頼、前提、委任単位、ツール実行、承認、レビュー、失敗、改善アクションをRun単位で接続する。

| 記録単位 | 目的 | 注意点 |
|---|---|---|
| Run ID | 一連のAI実行を追跡する | 顧客影響・本番影響があるRunは必ず付与する |
| Trace Event | 処理過程を説明する | 機密情報の過剰記録を避ける |
| Tool Execution | 何を実行したかを残す | 引数、対象、結果、エラーを残す |
| Approval | 誰が何を承認したかを残す | 承認理由と却下理由を残す |
| Review / Evaluation | 出力品質を改善へ戻す | 指摘を前工程へ接続する |

第8章では、この流れを使って、再現、説明、監査、改善に使える実行証跡を設計する。

## 関連章・利用箇所

### 関連章

- [第8章 ログ・トレース・継続改善](../../chapters/chapter-08/): Run単位の証跡を設計する。

### 本文での利用箇所

- [第8章 ログ・トレース・継続改善](../../chapters/chapter-08/): 依頼、前提、ツール実行、承認、レビュー、改善バックログを接続する。

[← 図表索引へ戻る](../../figure-index/)
