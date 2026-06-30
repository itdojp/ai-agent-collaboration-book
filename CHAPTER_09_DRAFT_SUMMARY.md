# CHAPTER_09_DRAFT_SUMMARY

## 対象

第9章「セキュリティとプライバシー」を公開初稿相当へ拡張した。

## 中心メッセージ

```text
AIエージェントのセキュリティは、モデルだけの問題ではない。
入力、文脈、ツール、出力、ログ、メモリ、人間承認、外部サービスをまたぐ
業務システム全体の設計問題である。
```

## 主な追加内容

```text
・AIエージェントの攻撃面
・主要リスク12分類
・情報分類とデータ最小化
・プロンプトインジェクションの業務設計
・不安全な出力処理
・過剰なエージェンシーと最小権限
・RAG / ベクトルDBのセキュリティ
・メモリと長期文脈の扱い
・外部ツール、MCP、プラグイン、SaaSの審査
・ログ、トレース、評価データのプライバシー
・人間の過信と承認疲れ
・セキュリティレベル S0〜S5
・セキュリティ設計の8ステップ
```

## 追加した実務ケース

```text
1. 外部FAQを読ませる
2. 顧客問い合わせ対応エージェント
3. AIがSQLを生成する
4. 社内ナレッジ更新エージェント
5. 外部MCPサーバーを追加する
6. ログが情報漏洩源になる
```

## 追加・拡張した成果物

```text
AI Security Checklist
Data Classification and Handling Matrix
Untrusted Input Handling Rule
Prompt Injection Test Sheet
AI Privacy Impact Review
External Tool / MCP Review Sheet
Security Exception Record
AI Incident Trigger Matrix
```

## 更新ファイル

```text
manuscript/ch09-security-privacy.md
appendices/a-templates.md
appendices/b-checklists.md
artifact-index.md
exercises/exercise-bank.md
planning/chapter-acceptance-criteria.md
book-config.json
title.md
colophon.md
MANIFEST.md
changelog.md
```

## 次章への接続

第9章では、個別ユースケースのセキュリティ・プライバシー設計を扱った。第10章では、これをAI利用ポリシー、AI System Inventory、リスク分類、承認フロー、監査、インシデント対応へ接続する。
