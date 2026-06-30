# 図表SVG生成手順

本書では、公開サイトで Mermaid コードブロックがそのまま表示されないよう、主要図表をSVGとしてコミットします。編集元の Mermaid は各 Markdown に残し、公開ページではSVG画像を先に表示し、Mermaidソースは折りたたみ表示にします。

## 対象

- `concept-map.md`、`artifact-index.md`、`troubleshooting.md`
- `manuscript/ch01-ai-agent-collaboration.md`
- `figures/f-00-*.md` 〜 `figures/f-15-*.md` の主要図表
- `figures/f-05-level-prefixes.md` は Mermaid ではなく、`scripts/build_figures.py` 内の表データから静的SVGを生成する

生成先は次の通りです。

- `figures/assets/*.svg`: 公開サイトで参照するSVG
- `figures/assets/mermaid/*.mmd`: Markdown から抽出した Mermaid 入力
- `docs/figures/assets/*.svg`: `scripts/sync_published_docs.py` により公開ツリーへ同期される公開用コピー

## 生成コマンド

前提: Node.js 20以上、Python 3.11以上。Mermaid CLI は `@mermaid-js/mermaid-cli@11.16.0` を `npx` 経由で使用します。

```bash
npm ci
npm_config_cache=.codex-local/tmp/npm-cache \
PUPPETEER_CACHE_DIR=.codex-local/tmp/puppeteer-cache \
PLAYWRIGHT_BROWSERS_PATH=.codex-local/tmp/playwright-browsers \
npm run build:figures
npm run sync:docs
```

`build:figures` は上記キャッシュ変数を指定しない場合でも、リポジトリ配下の `.codex-local/tmp/` を既定の一時領域として使います。CIやローカル環境で別のキャッシュ場所を使う場合は、同じ環境変数で上書きできます。

## 検証

```bash
npm run check:figures
npm test
```

`check:figures` は、期待するSVGが存在すること、抽出済み `.mmd` が編集元 Markdown の Mermaid ブロックと一致すること、静的SVGがスクリプト内の表データと一致することを確認します。本文や図表の Mermaid を変更した場合は、必ず `npm run build:figures` と `npm run sync:docs` を再実行してください。
