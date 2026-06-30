# AIエージェント協働の仕事術

## 人間・業務・AIをつなぐ実践フレームワーク

本リポジトリは、IT Engineer Knowledge Architecture シリーズの書籍『AIエージェント協働の仕事術』の公開リポジトリです。

- 公開サイト: <https://itdojp.github.io/ai-agent-collaboration-book/>
- リポジトリ: <https://github.com/itdojp/ai-agent-collaboration-book>
- ライセンス: CC BY-NC-SA 4.0（商用利用には別途契約が必要）
- 公開版: [v1.0.0](https://github.com/itdojp/ai-agent-collaboration-book/releases/tag/v1.0.0)

本書は、AIエージェントを「便利なチャット」ではなく、業務成果を出すための協働システムとして扱います。対象読者はエンジニアに限定しません。業務担当者、マネージャー、AI推進担当、情シス・セキュリティ担当、経営層までを含みます。

## 本書の一文定義

AIエージェント協働とは、業務目的を明確化し、依頼・コンテキスト・権限・レビュー・人間判断を設計することで、AIの出力と行動を組織成果へ変換する仕事術です。

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

## 読者向け主要ページ

| ファイル | 公開サイト | 用途 |
|---|---|---|
| [index.md](index.md) | [トップ](https://itdojp.github.io/ai-agent-collaboration-book/) | 書籍トップと目次 |
| [quickstart.md](quickstart.md) | [Quick Start](https://itdojp.github.io/ai-agent-collaboration-book/quickstart/) | 90分で最小実践する導線 |
| [concept-map.md](concept-map.md) | [Concept Map](https://itdojp.github.io/ai-agent-collaboration-book/concept-map/) | 本書の中核フレームワーク |
| [artifact-index.md](artifact-index.md) | [Artifact Index](https://itdojp.github.io/ai-agent-collaboration-book/artifact-index/) | 目的別・職種別入口を含む成果物索引 |
| [troubleshooting.md](troubleshooting.md) | [Troubleshooting](https://itdojp.github.io/ai-agent-collaboration-book/troubleshooting/) | AI活用が詰まったときの切り分け |
| [figure-index.md](figure-index.md) | [Figure Index](https://itdojp.github.io/ai-agent-collaboration-book/figure-index/) | 図表IDから用途・関連章を追う索引 |
| [source-notes.md](source-notes.md) | [References and Source Notes](https://itdojp.github.io/ai-agent-collaboration-book/source-notes/) | 参考文献・出典管理 |

## ディレクトリ構成

| パス | 役割 |
|---|---|
| `docs/` | GitHub Pages 用 Jekyll 公開ツリー。共通 book レイアウト、ナビゲーション、検索データを含む。 |
| `manuscript/` | 章本文の編集元。第0章〜第16章を配置。 |
| `appendices/` | 付録A〜Hの編集元。 |
| `figures/` | 図表説明ページの編集元。SVG生成物は `figures/assets/` に配置する。 |
| `examples/`, `exercises/` | 継続ケースと演習問題の編集元。 |
| `planning/`, `review/` | 執筆計画、レビュー記録、親サイト掲載メモなどのリポジトリ資料。書籍サイトの主要導線には含めない。 |
| `scripts/` | 図表SVG生成、公開ツリー同期、リンク検証、メタデータ検証のスクリプト。 |

`docs/` の Markdown は `scripts/sync_published_docs.py` で編集元から生成します。本文を変更した場合は、編集元ファイルを更新してから `npm run sync:docs` を実行してください。Mermaid図表のSVG生成手順は [FIGURE_BUILD.md](FIGURE_BUILD.md) を参照してください。

## ローカル検証

前提: Node.js 20以上、Python 3.11以上、Ruby 3.3/Bundler。

```bash
npm ci
python -m pip install -r requirements.txt
bundle install
npm run build:figures
npm run sync:docs
npm test
npm audit --audit-level=moderate
npm run build
```

CI では `.github/workflows/ci.yml` の `Book QA` が、GitHub Pages では `.github/workflows/pages.yml` が同等の同期・検証・Jekyll ビルドを実行します。

## 公開と親サイト連携

- GitHub Pages は `docs/` を Jekyll の source としてビルドし、`_site` を Pages artifact としてデプロイします。
- 親サイト `itdojp/it-engineer-knowledge-architecture` への掲載案は [planning/parent-site-integration.md](planning/parent-site-integration.md) を参照してください。
- 執筆計画、Codex作業メモ、レビュー反映記録は GitHub 上のリポジトリ資料として保持し、読者向けサイトの主要ナビゲーションには含めません。

## ライセンス

© 2026 ITDO Inc. Content licensed under CC BY-NC-SA 4.0. Commercial use requires a separate agreement.
