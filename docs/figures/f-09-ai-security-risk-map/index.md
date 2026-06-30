---
title: "F-09: AIセキュリティリスクマップ"
source_path: "figures/f-09-ai-security-risk-map.md"
order: 480
book_section: "figures"
---
# F-09: AIセキュリティリスクマップ

![F-09: AIセキュリティリスクマップ](../assets/f-09-ai-security-risk-map.svg)

<details markdown="1">
<summary>Mermaidソース</summary>

```mermaid
flowchart TB
    AG[AIエージェント]

    IN[外部入力<br/>Web / メール / チケット / 文書]
    CTX[コンテキスト<br/>社内資料 / RAG / メモリ]
    TOOL[ツール<br/>API / DB / SaaS / MCP]
    OUT[出力<br/>コード / SQL / 顧客文面]
    LOG[ログ・トレース<br/>Run Log / 評価データ]
    SUP[外部供給元<br/>モデル / SaaS / MCP / プラグイン]

    IN -->|Prompt Injection| AG
    CTX -->|機密漏洩・汚染| AG
    TOOL -->|権限過大・誤操作| AG
    AG -->|不安全な出力処理| OUT
    AG -->|過剰記録| LOG
    SUP -->|サプライチェーンリスク| AG

    C1[制御<br/>Untrusted Input Rule]
    C2[制御<br/>Data Classification]
    C3[制御<br/>Permission / HITL]
    C4[制御<br/>Output Review]
    C5[制御<br/>Log Minimization]
    C6[制御<br/>Vendor / MCP Review]

    IN -.-> C1
    CTX -.-> C2
    TOOL -.-> C3
    OUT -.-> C4
    LOG -.-> C5
    SUP -.-> C6
```

</details>

AIエージェントのセキュリティは、モデル単体の問題ではない。入力、文脈、ツール、出力、ログ、外部供給元をまたぐ業務システムの設計問題である。

| 攻撃面 | 典型リスク | 対応する成果物 |
|---|---|---|
| 外部入力 | プロンプトインジェクション、偽指示 | Untrusted Input Handling Rule、Prompt Injection Test Sheet |
| コンテキスト | 機密投入、古い情報、メモリ汚染 | Data Classification and Handling Matrix、Context Pack |
| ツール | 権限過大、誤更新、不可逆操作 | ツール権限マトリクス、HITL承認フロー |
| 出力 | 未検証SQL、コード、顧客送信 | AI出力レビュー表、Review Issue Log |
| ログ | 個人情報・機密情報の残存 | Agent Run Log、ログマスキング方針 |
| 外部供給元 | SaaS、MCP、プラグインの信頼性 | External Tool / MCP Review Sheet、Vendor Review Record |

第9章では、このリスクマップを使って、AI Security ChecklistとPrivacy Impact Reviewを設計する。

## 関連章・利用箇所

### 関連章

- [第9章 セキュリティとプライバシー](../../chapters/chapter-09/): AI固有リスクを棚卸しする。

### 本文での利用箇所

- [第9章 セキュリティとプライバシー](../../chapters/chapter-09/): 入力、文脈、ツール、出力、ログ、外部供給元を攻撃面として確認する。

[← 図表索引へ戻る](../../figure-index/)
