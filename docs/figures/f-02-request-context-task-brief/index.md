---
title: "F-02: Request Contract / Context Pack / Task Brief の関係"
source_path: "figures/f-02-request-context-task-brief.md"
order: 410
book_section: "figures"
---
# F-02: Request Contract / Context Pack / Task Brief の関係

![F-02: Request Contract / Context Pack / Task Brief の関係](../assets/f-02-request-context-task-brief.svg)

<details markdown="1">
<summary>Mermaidソース</summary>

```mermaid
flowchart LR
    RC[Request Contract<br/>目的・成果物・制約・受け入れ条件]
    CP[Context Pack<br/>前提・経緯・資料・鮮度・機密区分]
    TB[Task Brief<br/>AIに委任する1作業単位]
    OUT[AI出力<br/>レビュー対象]
    REV[AI出力レビュー表<br/>採用・修正・差し戻し]

    RC --> TB
    CP --> TB
    TB --> OUT
    OUT --> REV
    REV -->|改善点| RC
    REV -->|不足情報| CP
```

</details>

Request Contractは「何をしてほしいか」、Context Packは「何を前提にするか」、Task Briefは「どの作業単位として委任するか」を定義する。

## 関連章・利用箇所

### 関連章

- [第3章 依頼を契約にする](../../chapters/chapter-03/): Request Contractを定義する。
- [第4章 Context Packを設計する](../../chapters/chapter-04/): 前提と制約を渡す。
- [第5章 タスク分解と委任](../../chapters/chapter-05/): Task Briefへ落とす。

### 本文での利用箇所

- [第3章 依頼を契約にする](../../chapters/chapter-03/): 第3章〜第5章で、Request、Context、Delegationの接続を説明する。

[← 図表索引へ戻る](../../figure-index/)
