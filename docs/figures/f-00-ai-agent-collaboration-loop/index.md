---
title: "F-00: AIエージェント協働ループ"
source_path: "figures/f-00-ai-agent-collaboration-loop.md"
order: 390
book_section: "figures"
---
# F-00: AIエージェント協働ループ

![F-00: AIエージェント協働ループ](../assets/f-00-ai-agent-collaboration-loop.svg)

<details markdown="1">
<summary>Mermaidソース</summary>

```mermaid
flowchart LR
    A[仕事を選ぶ<br/>Work] --> B[依頼を契約にする<br/>Request]
    B --> C[前提を渡す<br/>Context]
    C --> D[分解して委任する<br/>Delegation]
    D --> E[出力をレビューする<br/>Review]
    E --> F[権限と承認で制御する<br/>Permission / HITL]
    F --> G[ログから改善する<br/>Observability]
    G --> H[人間が判断し実験で学習する<br/>Human / Org]
    H --> A
```

</details>

この図は本書全体の基本ループである。AI活用を単発のプロンプトではなく、業務成果へ変換する反復プロセスとして扱う。

## 関連章・利用箇所

### 関連章

- [第1章 AIエージェント協働とは何か](../../chapters/chapter-01/): AIエージェント協働ループの基本概念を確認する。

### 本文での利用箇所

- [Concept Map](../../concept-map/): 本書全体の反復ループとして参照する。
- [第1章 AIエージェント協働とは何か](../../chapters/chapter-01/): チャット利用と業務協働システムの違いを説明する。

[← 図表索引へ戻る](../../figure-index/)
