---
title: "F-01: 6層モデル"
source_path: "figures/f-01-six-layer-model.md"
order: 400
book_section: "figures"
---
# F-01: 6層モデル

![F-01: 6層モデル](../assets/f-01-six-layer-model.svg)

<details markdown="1">
<summary>Mermaidソース</summary>

```mermaid
flowchart TB
    W[Work<br/>どの仕事にAIを使うか]
    R[Request<br/>AIに何を依頼するか]
    C[Context<br/>AIに何を渡すか]
    D[Delegation<br/>どう分解し、どこで止めるか]
    CTRL[Control<br/>どう検証し、どう制御するか]
    H[Human / Org<br/>人間が何を判断し、どう学習するか]

    W --> R --> C --> D --> CTRL --> H
```

</details>

6層モデルは、章構成と成果物体系を整理するための背骨である。

## 関連章・利用箇所

### 関連章

- [第0章 本書の読み方](../../reading-guide/): 読み進め方と章構成を確認する。
- [第1章 AIエージェント協働とは何か](../../chapters/chapter-01/): 6層モデルの全体像を理解する。

### 本文での利用箇所

- [第0章 本書の読み方](../../reading-guide/): 読者別導線と成果物体系の見取り図として使う。
- [第1章 AIエージェント協働とは何か](../../chapters/chapter-01/): 本書の中核フレームワークとして使う。

[← 図表索引へ戻る](../../figure-index/)
