# CHAPTER 15 Draft Summary

## 対象章

第15章 スキルマップと評価

## 版

0.15.0-draft

## 実施内容

第15章を、Human / Org層のうち **Capability / Assessment** を扱う章として執筆した。

中心メッセージは以下である。

```text
AIエージェント協働能力は、プロンプト力だけではない。
仕事選定、依頼設計、コンテキスト設計、委任、レビュー、ツール権限、ログ、セキュリティ、ガバナンス、判断、対話、実験、行動、組織展開に分かれる。

評価では、自己診断だけに頼らない。
成果物、実技課題、運用証跡を見る。
職種やリスクに応じて到達目標を変える。
評価結果は、Learning Gap Handoffとして第16章の研修、OJT、Office Hour、認定運用へ引き渡す。
```

## 第15章に追加した主な内容

```text
・評価してはいけないもの
・評価原則
・12能力領域
・6層モデルと評価対象の対応
・Lv1〜Lv6のレベル定義
・領域別ルーブリック
・職種別到達目標
・Role Skill Profile
・評価証拠レベル：EV0〜EV5
・Skill Diagnosis Form
・Practical Assessment Pack
・レベル別実技課題
・Evidence Portfolio
・Learning Gap Handoff
・Certification Criteria
・Certification Decision Record
・評価ワークフロー
・評価者設計
・評価者校正
・プライバシーと評価の注意点
・スキルマップ作成手順
```

## 追加した実務ケース

第15章には、以下の4ケースを入れた。

```text
1. CS担当者をLv3へ上げる
2. マネージャーをAI Team Leadへ上げる
3. エンジニアをAI Agent Operatorへ上げる
4. AI推進担当をAI Governance Ownerへ上げる
```

## 追加・拡張した成果物

付録Aに以下を追加した。

```text
A.15.1 AI Agent Collaboration Skill Map
A.15.2 Role Skill Profile
A.15.3 Skill Diagnosis Form
A.15.4 Practical Assessment Pack
A.15.5 Evidence Portfolio
A.15.6 Learning Gap Handoff
A.15.7 Certification Decision Record
A.15.8 Evaluator Calibration Record
A.15.9 記入例: CS担当者のRole Skill Profile
```

付録C「スキル評価ルーブリック」を、以下を含む詳細版へ更新した。

```text
・Lv1〜Lv6定義
・評価証拠レベル：EV0〜EV5
・12領域別のLv1〜Lv6ルーブリック
・認定別の合格基準
・評価者向け採点観点
・不合格にすべき例
・評価者校正
・更新方針
```

Artifact Index には、以下を追加した。

```text
Skill Map
Role Skill Profile
Skill Diagnosis Form
Practical Assessment Pack
Evidence Portfolio
Learning Gap Handoff
Certification Decision Record
Evaluator Calibration Record
スキル評価ルーブリック
```

## 追加したチェックリスト・演習

付録Bに以下を追加した。

```text
B.18 スキルマップ・評価設計チェック
```

Exercise Bankには以下を追加した。

```text
Exercise 15: スキルマップと評価
```

演習では、CS担当者、開発者、マネージャーの3ロールを対象に、以下を作成する課題にしている。

```text
1. Role Skill Profile
2. 12能力領域ごとの目標レベル
3. Practical Assessment Pack
4. 評価証拠レベルの設計
5. Evidence Portfolio
6. Learning Gap Handoff
7. Certification Decision Record
8. 評価者校正の進め方
9. マスキング方針
10. 第16章への引き渡し条件
```

## 更新したメタ情報

以下を更新した。

```text
book-config.json: 0.15.0-draft
README系バージョン表記: 0.15.0-draft
MANIFEST.md: CHAPTER_15_DRAFT_SUMMARY.mdを追加
changelog.md: 0.15.0-draftを追加
planning/chapter-acceptance-criteria.md: 第15章の完成条件を更新
source-notes.md: 第15章の参照観点を追加
artifact-index.md: 第15章成果物を追加
```

## 次章への接続

第16章では、第15章のスキルマップと評価体系を、社内教材、ワークショップ、認定制度、Office Hour、KPI、90日展開計画へ変換する。

## 0.20.0-revisedでの重複圧縮

- 第15章は、詳細な研修・学習パス運用を扱わず、能力定義、評価証拠、不足領域、認定判定に責務を限定した。
- `Learning Gap Handoff`を`Learning Gap Handoff`へ置き換え、第16章のRole-based Learning Pathとの重複を解消した。
- 認定については、合格基準と判定記録を第15章、導入順序・権限付与・台帳反映を第16章へ分離した。
