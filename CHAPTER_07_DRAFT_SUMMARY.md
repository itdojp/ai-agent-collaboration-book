# CHAPTER_07_DRAFT_SUMMARY

## 対象

第7章「ツール・権限・HITL」を公開初稿相当へ拡張した。

## 中心メッセージ

```text
AIにツールを使わせるとは、AIに権限を渡すことである。
権限設計なしにツールを接続してはいけない。

AIに何を実行させるかより先に、
何を実行させないか、どこで止めるか、誰が承認するか、何を記録するかを決める。
```

## 主な追加内容

```text
・AIがツールを使うことによるリスク変化
・ツール、アクション、権限、スコープ、HITL、承認ゲート、承認パケットの定義
・no-access / read-only / draft-only / proposal-only / approval-required / limited-write / write / admin の権限モデル
・ツール単位ではなく操作単位で権限を設計する考え方
・ツール利用リスクの判定軸
・下書き、提案、実行の分離
・HITLの定義と承認パケット設計
・HITLが必要な操作の分類
・承認者の決め方
・AI向けTool Spec Cardの設計原則
・スコープ設計、APIキー、認証情報の扱い
・実行前確認、実行後確認、失敗時挙動
・レート制限、冪等性、ドライラン、差分プレビュー、ロールバック
・Permission Test
```

## 追加した実務ケース

```text
1. 顧客返信エージェント
2. GitHub PR作成エージェント
3. 障害一次対応エージェント
4. 営業CRM更新エージェント
5. 社内ナレッジ更新エージェント
```

## 追加・拡張した成果物

付録Aの A.7 を拡張し、以下を追加した。

```text
A.7.1 ツール権限マトリクス
A.7.2 Tool Spec Card
A.7.3 HITL承認フロー
A.7.4 Tool Approval Request
A.7.5 禁止操作リスト
A.7.6 Permission Test
A.7.7 記入例: 顧客問い合わせ対応エージェント
```

Artifact Index に以下を追加した。

```text
Tool Spec Card
Tool Approval Request
禁止操作リスト
Permission Test
```

## 追加したチェックリスト・演習

付録Bに以下を追加した。

```text
B.10 ツール権限・HITL設計チェック
```

Exercise Bankに以下を追加した。

```text
Exercise 07: ツール権限とHITL設計
```

## 更新したメタ情報

```text
book-config.json: 0.7.0-draft
MANIFEST.md: 0.7.0-draft
title.md: 0.7.0-draft
colophon.md: 0.7.0-draft
changelog.md: 0.7.0-draft
planning/chapter-acceptance-criteria.md: 第7章の完成条件を更新
```
