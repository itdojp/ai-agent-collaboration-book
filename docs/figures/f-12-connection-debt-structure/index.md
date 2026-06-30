---
title: "F-12: Connection Debtの蓄積構造"
source_path: "figures/f-12-connection-debt-structure.md"
order: 510
book_section: "figures"
---
# F-12: Connection Debtの蓄積構造

![F-12: Connection Debtの蓄積構造](../assets/f-12-connection-debt-structure.svg)

<details markdown="1">
<summary>Mermaidソース</summary>

```mermaid
flowchart LR
    U[言うべきことを言わない]
    A[前提がズレる]
    B[バックチャネルが増える]
    R[責任境界が曖昧になる]
    T[信頼が下がる]
    S[意思決定が遅れる]
    Q[AI出力品質の問題に見える]

    U --> A --> B --> R --> T --> S --> Q --> U

    I1[介入1<br/>Connection Debt診断]
    I2[介入2<br/>Difficult Conversation Brief]
    I3[介入3<br/>Agreement Log / Follow-up Contract]

    U -.-> I1
    A -.-> I2
    R -.-> I3
```

</details>

Connection Debtは、重要な相手に言うべきことを言わないことで蓄積する組織負債である。AI導入が進むと、未合意の前提や責任境界がAI出力の品質問題に見えやすくなる。

| 蓄積段階 | 兆候 | 必要な介入 |
|---|---|---|
| 言えていない | 懸念を本人に伝えず、周囲にだけ話す | Connection Debt診断 |
| 前提がズレる | 営業、開発、CS、管理職で期待が違う | Conflict Type Map |
| バックチャネル化 | 会議外で不満が増える | Backchannel Control Rule |
| 責任境界不明 | 誰が決めるか不明なままAIに作業させる | Difficult Conversation Brief |
| 信頼低下 | レビューが人格評価に見える | Perspective Map |
| 意思決定停滞 | 判断が会議で決まらず先送りされる | Agreement Log、Follow-up Contract |

第12章では、AIを「対話の代替」ではなく、対立構造の整理と直接会話の準備に使う。
