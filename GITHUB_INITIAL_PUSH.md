# GitHub初回投入手順

対象リポジトリ: <https://github.com/itdojp/ai-agent-collaboration-book>

## 前提

- リポジトリは作成済み。
- 初回push前の空リポジトリを想定する。
- GitHub Pagesは、push後に `main` branch / root で有効化する。

## 手順A: このパッケージをそのままpushする

```bash
git clone git@github.com:itdojp/ai-agent-collaboration-book.git
cd ai-agent-collaboration-book

# このパッケージの中身をリポジトリ直下へコピー
# 例: rsync -av --delete /path/to/ai-agent-collaboration-book-import-ready/ ./

git add .
git commit -m "Add initial draft of AIエージェント協働の仕事術"
git push origin main
```

HTTPSを使う場合:

```bash
git clone https://github.com/itdojp/ai-agent-collaboration-book.git
```

## 手順B: 既にclone済みの場合

```bash
cd ai-agent-collaboration-book
rsync -av --delete /path/to/ai-agent-collaboration-book-import-ready/ ./
git status
git add .
git commit -m "Add initial draft of AIエージェント協働の仕事術"
git push origin main
```

## GitHub Pages設定

push後、GitHubで以下を設定する。

```text
Settings
  → Pages
  → Build and deployment
  → Source: Deploy from a branch
  → Branch: main
  → Folder: / (root)
  → Save
```

公開予定URL:

```text
https://itdojp.github.io/ai-agent-collaboration-book/
```

## 初回push後の確認

```bash
# リポジトリURL
open https://github.com/itdojp/ai-agent-collaboration-book

# Pages有効化後
open https://itdojp.github.io/ai-agent-collaboration-book/
```

確認観点:

- `index.md` が表示される
- `manuscript/` 配下の章リンクが辿れる
- `appendices/`、`figures/`、`review/` への相対リンクが切れていない
- `book-config.json` の `repository.url` と `publicUrl` が正しい
- 親サイト側の掲載リンクが公開URLへ向いている
