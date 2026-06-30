# AIエージェント協働の仕事術

## 人間・業務・AIをつなぐ実践フレームワーク

本リポジトリは、IT Engineer Knowledge Architecture シリーズに追加する新刊『AIエージェント協働の仕事術』の執筆リポジトリです。

本書は、AIエージェントを「便利なチャット」ではなく、業務成果を出すための協働システムとして扱います。対象読者はエンジニアに限定しません。業務担当者、マネージャー、AI推進担当、情シス・セキュリティ担当、経営層までを含みます。

## 本書の一文定義

AIエージェント協働とは、業務目的を明確化し、依頼・コンテキスト・権限・レビュー・人間判断を設計することで、AIの出力と行動を組織成果へ変換する仕事術です。

## 本書の位置づけ

- Professional Foundations と AIエージェント実践書の間をつなぐ横断書籍
- プロンプト、コンテキスト、委任、検証、権限、ガバナンス、人間側能力を統合する書籍
- 後続の社内研修、e-learning、ワークショップ、認定課題の原典
- 既存の『AIエージェント実践』『GitHub AgentOps 実践ガイド』『AI時代のプロフェッショナルITエンジニアの思考法』への橋渡し

## 中核フレームワーク

本書は、次の6層でAIエージェント協働を扱います。

| 層 | 問い | 主な成果物 |
|---|---|---|
| Work | どの仕事にAIを使うか | AI適用判断シート |
| Request | AIに何を依頼するか | AIエージェント依頼書 |
| Context | AIに何を渡すか | Context Pack |
| Delegation | どう分解し、どこで止めるか | Task Brief |
| Control | どう検証し、どう制御するか | レビュー表、権限マトリクス、Run Log |
| Human / Org | 人間が何を判断し、どう学習するか | 判断チェックリスト、実験設計、スキルマップ |

詳細は [Concept Map](concept-map.md) を参照してください。

## まず読むファイル

| ファイル | 用途 |
|---|---|
| [index.md](index.md) | 書籍トップと目次 |
| [quickstart.md](quickstart.md) | 90分で最小実践する導線 |
| [concept-map.md](concept-map.md) | 本書の中核フレームワーク |
| [artifact-index.md](artifact-index.md) | 本書で作る成果物一覧 |
| [troubleshooting.md](troubleshooting.md) | AI活用が詰まったときの切り分け |
| [figure-index.md](figure-index.md) | 図表計画 |
| [codex-cli-plan.md](codex-cli-plan.md) | Codex CLIでの作業計画 |
| [writing-guide.md](writing-guide.md) | 執筆ルール |
| [source-notes.md](source-notes.md) | 出典候補と確認メモ |
| [review/REVIEW_APPLIED_SUMMARY.md](review/REVIEW_APPLIED_SUMMARY.md) | 横断レビュー反映状況 |

## 現在のドラフト状態

- 版: 0.24.0-import-ready
- 第0章〜第16章まで初稿相当
- 第15章・第16章の重複圧縮を反映済み
- 第0章を導入章として圧縮済み
- 追加図表F-07〜F-15を追加済み
- 横断レビューP1修正を反映済み
- 用語・レベル体系を統一済み（実験レベルX0〜X5、評価証拠レベルEV0〜EV5）
- Source Notes整理、優先図表追加、付録D〜H拡張を反映済み
- 次の主要作業: GitHub初回push、GitHub Pages設定、親サイトへの掲載、公開前校正

## GitHub初回投入

リポジトリ: <https://github.com/itdojp/ai-agent-collaboration-book>

初回投入手順は [GITHUB_INITIAL_PUSH.md](GITHUB_INITIAL_PUSH.md) を参照してください。

## Codex CLI での次作業

1. 本パッケージを `itdojp/ai-agent-collaboration-book` にpushする。
2. GitHub Pagesを `main` branch / root で有効化する。
3. `docs/PARENT_SITE_INTEGRATION.md` の掲載案を使い、親サイト `it-engineer-knowledge-architecture` へ追加する。
4. 公開前校正、Source Notesの公開後再確認、本文の表記最終調整を行う。
5. 必要に応じて `planning/codex-task-queue.md` を更新する。
