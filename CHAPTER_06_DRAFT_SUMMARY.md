# CHAPTER 06 DRAFT SUMMARY

## 対象

- 第6章「AI出力レビューと評価」

## 実施内容

第6章を Control 層の入口として、公開初稿相当へ拡張した。

中心メッセージは次のとおりである。

```text
AI出力は、レビューされるまで成果物ではない。
レビューとは、AI出力を受け入れ条件に照らして検査し、
事実、根拠、論理、リスク、不確実性を分離し、
採用できる部分、修正すべき部分、捨てるべき部分を決めることである。
```

## 追加した主な内容

- AI出力、レビュー済み出力、承認済み成果物、評価済み仕組みの区別
- レビュー、評価、検証、承認の違い
- レビューで使う入力: Request Contract、Acceptance Criteria、Context Pack、Task Brief、AI出力、利用先
- レビュー強度 L0〜L5
- 目的適合性、事実正確性、根拠、論理、網羅性、実行可能性、リスク、不確実性、再利用性のレビュー観点
- 採用、修正後採用、差し戻し、不採用、エスカレーションの判定
- Severity: Blocker / Critical / Major / Minor / Nit
- Review Issue Log
- Evaluation Plan
- 評価ケース、評価指標、回帰評価
- AI自己レビュー、別AIレビューの使い方と限界
- レビュー結果を Request Contract、Context Pack、Task Brief、権限設計、評価ケースへ戻す改善サイクル

## 追加した実務ケース

- 競合比較表のレビュー
- 顧客返信案のレビュー
- 障害報告書のレビュー
- 提案書ドラフトのレビュー

## 更新した成果物

- 付録A.6: AI出力レビュー表 / Review Issue Log / Evaluation Plan を拡張
- 付録B.9: AI出力レビュー前チェックを追加
- Artifact Index: Review Issue Log を追加し、Evaluation Plan への接続を更新
- Exercise Bank: Exercise 06 を追加
- Chapter Acceptance Criteria: 第6章の完成条件を更新

## 現在の状態

第1章〜第6章までが初稿相当になった。

次章では、第6章のレビュー結果を踏まえて、第7章「ツール・権限・HITL」で、AIがどのツールをどこまで使ってよいか、人間承認をどこに入れるかを扱う。
