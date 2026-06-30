# F-14: Action Blocker構造

![F-14: Action Blocker構造](assets/f-14-action-blocker-structure.svg)

<details markdown="1">
<summary>Mermaidソース</summary>

```mermaid
flowchart LR
    TASK[必要な行動<br/>共有・レビュー依頼・実験開始]
    TALK[セルフトーク<br/>失敗したらまずい / まだ不十分]
    MIX[リスク混同<br/>実リスクと想像上のリスクが混ざる]
    BLOCK[行動停止<br/>先送り・過剰レビュー・抱え込み]

    TASK --> TALK --> MIX --> BLOCK

    DIAG[Action Blocker診断]
    SEP[実リスク / 想像上のリスクを分ける]
    SAFE[安全策<br/>レビュー観点・承認・範囲制限]
    MIN[Minimum Action Contract<br/>最小行動]
    SUPPORT[Support Request<br/>支援依頼]

    BLOCK --> DIAG --> SEP
    SEP --> SAFE --> MIN
    SEP --> SUPPORT --> MIN
    MIN --> TASK
```

</details>

セルフトークは、個人の気分だけではなく、実験速度、レビュー依頼、判断、共有を止める業務上の摩擦になる。重要なのは、自己批判をなくすことではなく、止まっている行動を特定し、レビュー可能な最小行動へ変換することである。

| ブロッカー | 典型文 | 変換先 |
|---|---|---|
| 完璧主義 | もっと完成してから出す | 80%ドラフトをレビュー依頼する |
| 評価不安 | 批判されたら終わり | レビュー観点を指定して依頼する |
| AI不安 | AIを使うと自分の価値が下がる | AIで浮いた時間の使途を決める |
| 過剰責任 | 自分で全部確認しないと危険 | 承認ゲートとレビュー者を置く |
| 先送り | 時間があるときにやる | 次の業務日までの最小行動を決める |

第14章では、Action Blocker診断、Self-talk Transcript、Minimum Action Contractを使って、行動停止を業務設計問題として扱う。

## 関連章・利用箇所

### 関連章

- [第14章 セルフトークと高レバレッジ環境](../manuscript/ch14-self-talk.md): 行動停止を業務設計問題として扱う。

### 本文での利用箇所

- [第14章 セルフトークと高レバレッジ環境](../manuscript/ch14-self-talk.md): セルフトーク、リスク混同、行動停止、最小行動への変換を確認する。

[← 図表索引へ戻る](../figure-index.md)
