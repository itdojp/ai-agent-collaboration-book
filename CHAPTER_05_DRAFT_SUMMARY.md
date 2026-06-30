# CHAPTER 05 DRAFT SUMMARY

## 対象

- 第5章「タスク分解と委任」
- バージョン: `0.5.0-draft`
- 作成日: 2026-06-27

## 章の位置づけ

第5章は、本書の6層モデルにおける **Delegation** 層の中核章である。

```text
Work
  ↓
Request
  ↓
Context
  ↓
Delegation  ← 第5章
  ↓
Control
  ↓
Human / Org
```

第3章の Request Contract と第4章の Context Pack を受け取り、複雑な仕事を AI に委任可能な Task Brief へ分解する。

## 中心メッセージ

```text
AIへの委任は、丸投げではない。
委任とは、AIに任せる処理、人間が決める判断、
途中で確認する地点、止める条件、引き継ぐ条件を設計することである。
```

## 追加した主要論点

- 委任の定義
- 丸投げと委任の違い
- Request Contract / Context Pack / Task Brief の関係
- 1タスク1成果物の原則
- 作業と判断の分離
- 入力と出力の固定
- 中間成果物の設計
- 完了条件と停止条件の違い
- タスク分解の7ステップ
- タスク粒度の調整
- 委任レベル 0〜5
- チェックポイント設計
- 停止条件設計
- エスカレーション条件設計
- 依存関係設計
- 長い作業における Restart Packet

## 追加した実務ケース

1. 障害報告書の作成
2. 競合調査から社内提案書へ
3. 顧客問い合わせ対応
4. 開発タスクの分解

## 追加・拡張した成果物

- Task Brief
- Task Breakdown
- Checkpoint Plan
- Stop / Escalation Rules
- Restart Packet

## 更新した関連ファイル

- `manuscript/ch05-task-delegation.md`
- `appendices/a-templates.md`
- `appendices/b-checklists.md`
- `artifact-index.md`
- `exercises/exercise-bank.md`
- `book-config.json`
- `changelog.md`

## 第6章への接続

第5章で Task Brief、Checkpoint Plan、Stop / Escalation Rules を作ることで、第6章の AI出力レビューと評価に必要な受け入れ条件と中間成果物が揃う。

第6章では、AIが作った成果物をどうレビューし、事実、根拠、論理、リスク、再現性をどう評価するかを扱う。
