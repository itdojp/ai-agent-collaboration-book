# CHAPTER_10_DRAFT_SUMMARY

## 更新対象

- `manuscript/ch10-governance.md`
- `appendices/a-templates.md`
- `appendices/b-checklists.md`
- `artifact-index.md`
- `exercises/exercise-bank.md`
- `source-notes.md`
- `planning/chapter-acceptance-criteria.md`
- `book-config.json`
- `title.md`
- `colophon.md`
- `MANIFEST.md`
- `changelog.md`

## 第10章の位置づけ

第10章「ガバナンスと統制」は、Control層の最後として、個別AIエージェントの安全設計を組織運用へ接続する章である。

第9章までに扱ったセキュリティ、プライバシー、ツール権限、ログ、評価を、以下の統制成果物へ変換した。

```text
AI Use Policy
AI Use Case Intake
AI System Inventory
Governance Level Matrix
AI Risk Register
Approval Workflow
AI System ADR
AI Vendor Review Record
AI Training Register
AI Audit Evidence Pack
AI Incident Runbook
AI Retirement Plan
```

## 中心メッセージ

```text
AIガバナンスは、AI利用を抑制するための制度ではない。
安全にスケールさせるための運用基盤である。

低リスク利用を速くし、高リスク利用を確実に制御する。
そのために、台帳、リスク分類、承認、証跡、教育、棚卸し、廃止を設計する。
```

## 追加した主な内容

- AIガバナンス、セキュリティ、運用の違い
- 外部フレームワークの使い方
- ガバナンス基本原則
- ガバナンス対象の定義
- AI利用ポリシー設計
- AI System Inventoryの設計
- G0〜G5のGovernance Level Matrix
- Use Case Approval / Tool Action Approval / Risk Acceptanceの区別
- AI System ADR
- AI Risk Register
- ベンダー、外部AI、MCP管理
- 教育とAIリテラシーの統制
- AI Audit Evidence Pack
- AI Incident Runbook
- 例外管理
- 変更管理
- 廃止と棚卸し
- AI CoEと部門責任者の役割
- コスト統制

## 追加した実務ケース

1. 社内AI活用の棚卸し
2. 顧客問い合わせ対応エージェントを本番化する
3. GitHub PR作成エージェント
4. 契約書レビュー補助AI
5. 外部MCPサーバーを追加する
6. AI利用ポリシー違反が発生した

## 追加・拡張した成果物

付録Aの A.10 を拡張し、以下を追加した。

```text
A.10.1 AI Use Policy
A.10.2 AI Use Case Intake
A.10.3 AI System Inventory
A.10.4 Governance Level Matrix
A.10.5 AI Risk Register
A.10.6 Approval Workflow
A.10.7 AI System ADR
A.10.8 AI Vendor Review Record
A.10.9 AI Training Register
A.10.10 AI Incident Runbook
A.10.11 AI Audit Evidence Pack
A.10.12 AI Retirement Plan
A.10.13 Governance Review Log
```

## 追加したチェックリスト・演習

- 付録Bに `B.13 ガバナンス・統制設計チェック` を追加
- Exercise Bank に `Exercise 10: ガバナンスと統制` を追加

## 更新メタ情報

- `book-config.json`: `0.10.0-draft`
- `title.md`: `0.10.0-draft`
- `colophon.md`: `0.10.0-draft`
- `MANIFEST.md`: `0.10.0-draft`
- `changelog.md`: `0.10.0-draft` を追加
- `planning/chapter-acceptance-criteria.md`: 第10章の完成条件を更新
- `source-notes.md`: 第10章の参照観点を追加
