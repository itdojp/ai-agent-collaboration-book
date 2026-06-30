# Codex CLI向け 横断レビュー対応タスク

## Queue R1: 機械的統一

```text
対象: 全ファイル
作業:
1. 第13章の実験レベル X0〜X5 を X0〜X5 へ変更する。
2. 第15章の評価証拠レベル X0〜X5 を EV0〜EV5 へ変更する。
3. 付録A、付録C、Artifact Index、Exercise Bank、book-config.jsonも同時に更新する。
4. 付録Eにレベル接頭辞一覧を追加する。
検証:
- grep -R "実験レベル旧表記" . がヒットしない
- grep -R "評価証拠レベル旧表記" . がヒットしない
- grep -R "X0" . と grep -R "EV0" . が必要箇所でヒットする
```

## Queue R2: 章末セクション統一

```text
対象: manuscript/*.md
作業:
1. 章末Source Notes見出しを "## Source Notes" に統一する。
2. "## 章内のSource Notes旧表記" を "## Source Notes" に変更する。
3. 第14章と第16章にSource Notes節を追加する。
4. 第9章に "## 典型的な失敗" と "## 設計原則" を追加する。
5. 第10章に "## 設計原則" を追加する。
6. 第14章に "## 設計原則" を追加する。
検証:
- 章末セクション順がCHAPTER_MATRIX_REVIEW.mdの推奨順に概ね一致する
```

## Queue R3: 付録D〜H拡張

```text
対象:
- appendices/d-use-cases.md
- appendices/e-glossary.md
- appendices/f-workshop-design.md
- appendices/g-assessment-bank.md
- appendices/h-governance-starter-pack.md
作業:
1. 付録Dに関連章、成果物、承認条件、禁止事項、リスクレベルを追加する。
2. 付録Eに成果物名、レベル接頭辞、統制用語を追加する。
3. 付録Fを第16章のワークショップ設計と整合する。
4. 付録GにLv1〜Lv6別問題を追加する。
5. 付録Hを第10章のAI Use Policy、Inventory、Risk Register、Incident Runbookと整合する。
```

## Queue R4: Source Notes再構成

```text
対象: source-notes.md
作業:
1. 全体方針、既存シリーズ、外部資料、章別メモ、公開前再確認リストに再構成する。
2. 第1章〜第8章の章別メモを追加する。
3. 第14章、第16章の章別メモと本文章末Source Notesを対応させる。
4. 確認日欄を追加する。
注意:
- 最新確認はCodex CLI側でWeb確認または手動確認する。
```

## Queue R5: 図表追加

```text
対象:
- figure-index.md
- concept-map.md
- 各章本文
作業:
1. AIエージェント協働ループをMermaidで整える。
2. 6層モデル図を追加する。
3. Request Contract / Context Pack / Task Brief の関係図を追加する。
4. Control層の流れ図を追加する。
5. Human / Org層の流れ図を追加する。
6. レベル接頭辞一覧表を追加する。
```

## Queue R6: 章間重複圧縮

```text
対象:
- manuscript/00-reading-guide.md
- manuscript/ch10-governance.md
- manuscript/ch15-skill-map.md
- manuscript/ch16-org-rollout.md
作業:
1. 第0章を10,000〜12,000字程度へ圧縮する。
2. 第15章は能力定義・評価に集中させる。
3. 第16章は展開運用・教材化に集中させる。
4. 第10章はテンプレート詳細を付録へ寄せる。
```

## Queue R7: 補助資料更新

```text
対象:
- README.md
- quickstart.md
- concept-map.md
- troubleshooting.md
- planning/issue-backlog.md
作業:
1. READMEの現在状態と次作業を0.18.0-reviewに更新する。
2. Quick Startを90分版と3時間版に分ける。
3. Concept Mapに第12章・第14章の位置づけを追加する。
4. Troubleshootingにセキュリティ、ガバナンス、評価、対立処理の分岐を追加する。
5. planning/issue-backlog.mdにレビュー由来Issueを統合する。
```
