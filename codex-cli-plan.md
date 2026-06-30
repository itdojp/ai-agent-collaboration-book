# Codex CLI 作業計画

## 目的

このスターターを、IT Engineer Knowledge Architecture シリーズの新規書籍リポジトリ `ai-agent-collaboration-book` として成立させる。

## 前提

- 対象リポジトリ: `itdojp/ai-agent-collaboration-book`
- 公開URL: `https://itdojp.github.io/ai-agent-collaboration-book/`
- 既存シリーズの `templates/book/` と `book-config.json` の形式に合わせる。
- 本スターターは完全な入稿原稿ではない。初稿化、リンク整備、ビルド検証、レビュー対応が必要。

## 追加された作業支援ファイル

- `quickstart.md`: 最小実践導線
- `concept-map.md`: 中核フレームワーク
- `artifact-index.md`: 成果物一覧
- `troubleshooting.md`: 詰まりどころの切り分け
- `planning/codex-task-queue.md`: Codex CLI用の逐次タスク
- `planning/chapter-acceptance-criteria.md`: 章別完成条件

## Phase 1: リポジトリ作成・初期配置

```bash
# 1. 新規リポジトリを作成後、作業ディレクトリへ移動
mkdir ai-agent-collaboration-book
cd ai-agent-collaboration-book

# 2. 本スターターのファイルをコピー
# 3. 既存シリーズのテンプレートと比較し、不足ファイルを補完
# 4. book-config.json の repository.url と publicUrl を確認
```

Codex CLI への指示例:

```text
既存の it-engineer-knowledge-architecture/templates/book の構成に合わせて、現在のファイル群を新規書籍リポジトリとして整形してください。book-config.json、README.md、title.md、copyright.md、preface.md、manuscript/*.md、appendices/*.md を維持し、必要な index やナビゲーションファイルが不足していれば追加してください。本文の語調は既存の ai-agent-engineering-book に寄せ、過度な宣伝表現を削ってください。
```

## Phase 2: 目次・章ファイル整備

- 各章に `objectives` 相当の冒頭セクションを追加する。
- 章末に `まとめ` と `次に読む導線` を追加する。
- 付録へのリンクを張る。
- 既存書籍への相互リンクを追加する。

Codex CLI への指示例:

```text
book-config.json の chapters と manuscript 配下のファイル名が一致しているか確認し、公開サイトで目次化しやすい構成に整えてください。各章の冒頭に「この章で扱う能力」、末尾に「まとめ」「次に読む導線」を追加してください。
```

## Phase 3: 本文拡張

優先順:

1. 第1章から第4章を公開可能な初稿にする。
2. 第5章から第10章を実務運用・ガバナンス寄りに拡張する。
3. 第11章から第14章の人間側能力を、精神論ではなく業務設計として書き直す。
4. 第15章、第16章を社内教材化・認定設計へ接続する。

Codex CLI への指示例:

```text
第1章から第4章を、各章 4,000〜6,000字程度の初稿に拡張してください。各章は「典型的な失敗」「設計原則」「実務ケース」「作成する成果物」「演習」を必ず含めてください。AIツール仕様や法規制など変化しやすい内容は、source-notes.md の一次情報確認を促す表現にしてください。
```

## Phase 4: 出典・レビュー

- `source-notes.md` を本文リンクへ反映する。
- 第三者著作物の引用を最小化する。
- Lenny's Newsletter 由来の知見は「実践仮説」として扱う。
- セキュリティ、法務、プライバシーは最終レビュー対象にする。

Codex CLI への指示例:

```text
source-notes.md を参照し、本文中の外部事実・標準・フレームワーク・ツール仕様の説明に出典注記を追加してください。引用は短くし、本文では要約を中心にしてください。変化しやすい情報には「最終導入時に公式情報を確認する」旨を入れてください。
```

## Phase 5: Knowledge Architecture への追加

親リポジトリ `it-engineer-knowledge-architecture` で以下を更新する。

- README.md の書籍一覧
- English catalog が必要なら英語名を追加
- 学習ロードマップ
- Professional Foundations または新カテゴリ `AI Agent Enablement`
- CHANGELOG.md

Codex CLI への指示例:

```text
it-engineer-knowledge-architecture の README.md と roadmap 関連ファイルに、新刊『AIエージェント協働の仕事術』を追加してください。カテゴリは AI Agent Enablement とし、Professional Foundations と AIエージェント実践の間に配置してください。既存の書籍一覧、学習ロードマップ、CHANGELOG に矛盾が出ないようにしてください。
```

## Definition of Done

- 目次から全章・付録へリンクできる。
- `book-config.json` がシリーズ仕様に合っている。
- 各章が最低限の標準構成を満たす。
- 付録テンプレートが本文から参照されている。
- ライセンス、奥付、更新履歴がある。
- 公開前レビュー・チェックリストのコア項目を満たす。
- 変化しやすい事実には出典確認メモがある。
