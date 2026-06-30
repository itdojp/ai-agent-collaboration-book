# Source Notes URL確認・外部出典表記調整サマリー

- 対象版: 0.22.0-revised
- 更新後版: 0.23.0-revised
- 作業日: 2026-06-27

## 実施内容

1. `source-notes.md` をSource IDベースに再構成した。
2. 主要外部URLを、以下の状態に分類した。

```text
Verified: 2026-06-27時点でページ確認済み
Redirected: 旧URLから正規URLへ整理
Planned: 本書公開予定URL・予定リポジトリなど公開前（2026-07-01時点では本書URL・リポジトリをVerifiedへ更新済み）
Limited: 有料記事等により公開範囲に制約あり
```

3. 本文中の外部出典表記を、URL直書きではなく `SRC-*` 形式へ統一した。
4. 第9章と第10章の外部フレームワーク記述から、Source Notesへ明示的に誘導する文を追加した。
5. 第1章、第4章、第6章〜第14章、第16章の章末 `Source Notes` に参照Source IDを追加した。
6. OpenAI Evalsの参照先は、旧 `platform.openai.com/docs/guides/evals` から正規URL `https://developers.openai.com/api/docs/guides/evals` へ整理した。
7. OWASP LLM Top 10の参照先は、正規参照を `https://genai.owasp.org/llm-top-10/` に寄せ、旧OWASPプロジェクトページは入口として残した。
8. NIST Generative AI Profileの参照先として、NIST公開ページ `https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence` を追加した。

## 確認済みSource ID

### 既存シリーズ

```text
SRC-ITDO-KA
SRC-ITDO-PUBLISHING
SRC-ITDO-QUICKSTART
SRC-ITDO-UX-PROFILES
SRC-ITDO-UX-CORE
SRC-ITDO-UX-MODULES
SRC-ITDO-AGENT-BOOK
SRC-ITDO-AI-COMM
SRC-ITDO-AI-MIND
```

### AIエージェント設計・評価

```text
SRC-OPENAI-AGENTS
SRC-OPENAI-HITL
SRC-OPENAI-TRACING
SRC-OPENAI-EVALS
SRC-ANTHROPIC-CONTEXT
SRC-ANTHROPIC-TOOLS
```

### セキュリティ・ガバナンス

```text
SRC-OWASP-LLM
SRC-OWASP-LLM-LEGACY
SRC-OWASP-AGENTIC
SRC-NIST-AI-RMF
SRC-NIST-GENAI-PROFILE
SRC-ISO-42001
SRC-ISO-AIMS
SRC-EU-AI-LITERACY
```

### 人間側能力

```text
SRC-LENNY-INNER-GAME
```

## 本書公開URL・リポジトリの公開後更新

Issue #3対応時点（2026-07-01）で以下を公開済みとして確認し、`source-notes.md` では `Verified 2026-07-01` へ更新した。

```text
SRC-BOOK-PUBLIC-URL
SRC-BOOK-REPOSITORY
```

## 注意事項

- Source Notesは、本文の出典管理を軽量化するための管理ファイルである。法令・規格・ベンダー仕様の全文解説ではない。
- Lenny's Newsletterの記事は一部有料のため、本文では公開範囲で確認できた内容と、社内実務へ変換した実践仮説を分ける。
- ISO、NIST、OWASP、EU AI Act、OpenAI、Anthropicの仕様・公開情報は将来変更され得る。公開後も定期レビュー時に再確認する。
