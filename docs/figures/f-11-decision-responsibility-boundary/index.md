---
title: "F-11: 判断責任分界"
source_path: "figures/f-11-decision-responsibility-boundary.md"
order: 500
book_section: "figures"
---
# F-11: 判断責任分界

```mermaid
flowchart LR
    subgraph AI[AIが支援できること]
        A1[情報収集]
        A2[選択肢生成]
        A3[比較表作成]
        A4[反証・プレモーテム]
        A5[ドラフト作成]
    end

    subgraph HUMAN[人間が引き受けること]
        H1[目的と判断基準を決める]
        H2[価値判断・優先順位を決める]
        H3[残リスクを受ける/受けない]
        H4[採用・修正・棄却・停止を決める]
        H5[説明責任を持つ]
    end

    subgraph ARTIFACT[判断成果物]
        D1[Decision Brief]
        D2[Decision Criteria Matrix]
        D3[Risk Acceptance Memo]
        D4[Decision Review Log]
    end

    A1 --> D1
    A2 --> D2
    A3 --> D2
    A4 --> D3
    A5 --> D1

    D1 --> H1
    D2 --> H2
    D3 --> H3
    H4 --> D4
    H5 --> D4
```

AIは判断材料を作れるが、判断責任を引き受けることはできない。AI時代の判断力は、AI提案を信じる力ではなく、何を採用し、何を捨て、何を止め、どのリスクを誰が受けるかを明示する力である。

| 領域 | AIに任せられること | 人間が決めること |
|---|---|---|
| 目的 | 目的案の整理 | 最終目的、優先順位 |
| 情報 | 調査、要約、比較 | 信頼できる根拠の採用 |
| 選択肢 | 案、反対意見、リスク列挙 | 採用、棄却、保留、実験化 |
| リスク | リスク候補の抽出 | 残リスクの受容または拒否 |
| 説明 | 説明文の下書き | 誰にどう説明し、責任を持つか |

第11章では、この責任分界をDecision Brief、Kill Decision Sheet、Risk Acceptance Memoへ落とす。
