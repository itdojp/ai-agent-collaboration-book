---
title: "AIエージェント協働の仕事術"
source_path: "index.md"
order: 0
book_section: "home"
---
# AIエージェント協働の仕事術

## 人間・業務・AIをつなぐ実践フレームワーク

AIエージェントを、単なるチャットツールではなく、業務成果を生む協働システムとして扱うための実践書です。依頼、コンテキスト、委任、検証、権限、判断、組織展開を一連の仕事術として設計します。

## 想定読者

- AIエージェントを業務改善、資料作成、調査、レビュー、運用補助へ導入したい実務担当者
- AI活用の品質、権限、ログ、セキュリティ、ガバナンスを設計する管理者・推進担当者
- チーム内のAI利用を標準化し、教育、評価、KPI、認定へ展開したいマネージャー
- GitHub Copilot、ChatGPT、Claude、Gemini、社内AI基盤などの活用を業務プロセスに組み込みたいエンジニア・情シス担当者

## 対象外・前提

本書は特定AIサービスの操作マニュアルではありません。各サービスの最新仕様、料金、利用規約、管理画面の詳細は公式情報を確認してください。契約判断、人事評価、医療・法務・金融判断、本番変更、顧客への自動送信など高リスク領域では、組織の承認プロセス、法務・セキュリティ確認、専門家レビューを前提にします。

## 所要時間と読み方

- 最短導入: [Quick Start](quickstart/) を使い、90分で1つの業務を試します。
- 実務適用: 第1章〜第8章で依頼、委任、レビュー、ログまでを整えます。
- 組織展開: 第9章〜第16章でセキュリティ、ガバナンス、人間側能力、研修・評価へ広げます。
- テンプレート利用: 付録A〜Hを必要な成果物から逆引きします。

## 学習成果

本書を読むと、次のことができるようになります。

- AIに任せる仕事と任せない仕事を切り分ける
- AIへの依頼を Request Contract として仕様化する
- Context Pack で前提情報、制約、情報鮮度を渡す
- 大きな業務を Task Brief へ分解し、停止条件と人間確認を設計する
- AI出力をレビューし、採用・修正・差し戻しを判定する
- ツール権限、HITL、ログ、セキュリティ、ガバナンスを設計する
- AI時代の判断力、対立処理、失敗耐性、実験文化を業務に組み込む
- 社内教材、スキル評価、認定、KPIへ展開する

## まず使うページ

- [Quick Start: 90分で本書の型を使う](quickstart/)
- [Concept Map: AIエージェント協働の全体像](concept-map/)
- [Artifact Index: 本書で作る成果物](artifact-index/)
- [Troubleshooting Flow: 詰まったときの切り分け](troubleshooting/)
- [Figure Index: 図表計画](figure-index/)

## 目次

### 導入

- [第0章 本書の読み方](reading-guide/)

### Part I: AIエージェント協働の基礎

- [第1章 AIエージェント協働とは何か](chapters/chapter-01/)
- [第2章 AIに任せる仕事、任せない仕事](chapters/chapter-02/)

### Part II: 依頼・コンテキスト・委任

- [第3章 依頼を契約にする](chapters/chapter-03/)
- [第4章 Context Packを設計する](chapters/chapter-04/)
- [第5章 タスク分解と委任](chapters/chapter-05/)

### Part III: 検証・ツール・運用

- [第6章 AI出力レビューと評価](chapters/chapter-06/)
- [第7章 ツール・権限・HITL](chapters/chapter-07/)
- [第8章 ログ・トレース・継続改善](chapters/chapter-08/)

### Part IV: セキュリティ・ガバナンス

- [第9章 セキュリティとプライバシー](chapters/chapter-09/)
- [第10章 ガバナンスと統制](chapters/chapter-10/)

### Part V: 人間側能力

- [第11章 AI時代の判断力](chapters/chapter-11/)
- [第12章 困難な会話と対立処理](chapters/chapter-12/)
- [第13章 失敗耐性と実験文化](chapters/chapter-13/)
- [第14章 セルフトークと高レバレッジ環境](chapters/chapter-14/)

### Part VI: 組織展開

- [第15章 スキルマップと評価](chapters/chapter-15/)
- [第16章 組織展開と教材化](chapters/chapter-16/)

### 付録

- [付録A: 成果物テンプレート集](appendices/appendix-a/)
- [付録B: チェックリスト集](appendices/appendix-b/)
- [付録C: スキル評価ルーブリック](appendices/appendix-c/)
- [付録D: 職種別ユースケース集](appendices/appendix-d/)
- [付録E: 用語集](appendices/appendix-e/)
- [付録F: ワークショップ設計](appendices/appendix-f/)
- [付録G: 認定・診断問題バンク](appendices/appendix-g/)
- [付録H: ガバナンス・スターターパック](appendices/appendix-h/)

### 実践・演習

- [Recurring Case: 法人向けバックアップサービスのAI活用](examples/recurring-case/)
- [Exercise Bank: 演習問題集](exercises/exercise-bank/)
- [Source Notes: 出典候補と確認メモ](source-notes/)

## 更新方針

本文で扱うAIツール、モデル、管理機能、法規制、契約条件は変化します。本書は、特定ベンダーの一時的な画面仕様ではなく、依頼・文脈・検証・権限・判断・組織展開の設計原則を中心に記述します。実務適用時は、2026年6月時点の本書記述だけでなく、組織の最新ルールと各サービスの公式情報を確認してください。

## フィードバックとリポジトリ資料

執筆計画、レビュー記録、Codex作業メモなどの制作資料は、書籍サイトの読者導線には含めず、[GitHubリポジトリ](https://github.com/itdojp/ai-agent-collaboration-book)で参照できる形にします。誤り、改善提案、追加したいユースケースは GitHub Issues で受け付けます。

## ライセンス

© 2026 ITDO Inc. Content licensed under CC BY-NC-SA 4.0. Commercial use requires a separate agreement.
