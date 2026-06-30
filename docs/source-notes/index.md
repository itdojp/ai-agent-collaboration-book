---
title: "References and Source Notes"
source_path: "source-notes.md"
order: 60
book_section: "resources"
---
# References and Source Notes

このページは、本文で使う Source ID と主要参照先を読者向けにまとめた参考文献・出典管理ページである。本文では外部URLを長く展開せず、必要な箇所で `SRC-*` の出典キーを示し、詳細URLと確認状態をこのページで管理する。

- 最終整理日: 2026-07-01
- URL確認日: 外部資料 2026-06-27 / 本書公開URL・リポジトリ 2026-07-01
- 確認方針: 本文は特定ベンダーの詳細仕様ではなく、成果物と設計原則を中心にする。
- 優先ルール: 実導入時には、本書よりも自社規程、顧客契約、業界規制、個人情報保護、情報セキュリティ基準を優先する。
- 内部レビュー観点: 章別確認メモと制作レビューリストは、読者向け参考文献と分離し、リポジトリ資料 [review/SOURCE_NOTES_INTERNAL.md](https://github.com/itdojp/ai-agent-collaboration-book/blob/main/review/SOURCE_NOTES_INTERNAL.md) で管理する。

## 確認ステータス

状態欄の意味は以下である。

```text
Verified: 記載の確認日時点でページを確認できた
Redirected: 旧URLから別URLへ遷移するため、正規URLへ変更した
Limited: 一部有料・一部非公開など、公開範囲に制約がある
```

## 参考文献一覧

### 既存シリーズ関連

| Source ID | 名称 | URL | 状態 | 本書での用途 |
|---|---|---|---|---|
| SRC-ITDO-KA | ITエンジニア知識アーキテクチャ | <https://itdojp.github.io/it-engineer-knowledge-architecture/> | Verified | シリーズ内での位置づけ、既存書籍接続 |
| SRC-ITDO-PUBLISHING | 出版ガイド | <https://itdojp.github.io/it-engineer-knowledge-architecture/publishing/> | Verified | 書籍構成、公開レビュー、シリーズ標準 |
| SRC-ITDO-QUICKSTART | 新規書籍クイックスタート | <https://itdojp.github.io/it-engineer-knowledge-architecture/publishing/new-book-quickstart.html> | Verified | 新刊立ち上げ手順 |
| SRC-ITDO-UX-PROFILES | UX Profiles v1 | <https://itdojp.github.io/it-engineer-knowledge-architecture/publishing/ux-profiles.html> | Verified | `ux.profile` と必須モジュール設計 |
| SRC-ITDO-UX-CORE | UX Core Specification v1 | <https://itdojp.github.io/it-engineer-knowledge-architecture/publishing/ux-core.html> | Verified | 共通UI・章構成・トップページ構成 |
| SRC-ITDO-UX-MODULES | UX Modules Catalog v1 | <https://itdojp.github.io/it-engineer-knowledge-architecture/publishing/ux-modules.html> | Verified | quickStart、readingGuide、figureIndex等のモジュール管理 |
| SRC-ITDO-AGENT-BOOK | AIエージェント実践: Prompt / Context / Harness Engineering | <https://itdojp.github.io/ai-agent-engineering-book/> | Verified | 技術実践書への接続 |
| SRC-ITDO-AI-COMM | AIエージェント・コミュニケーション実践ガイド | <https://itdojp.github.io/ai-communication-book/> | Verified | 既存生成AIコミュニケーション系書籍との責務分離 |
| SRC-ITDO-AI-MIND | AI時代のプロフェッショナルITエンジニアの思考法 | <https://itdojp.github.io/ai-era-engineers-mind-book/> | Verified | 技術リーダーの判断・責任境界への接続 |

### AIエージェント設計・評価

| Source ID | 名称 | URL | 状態 | 本書での用途 |
|---|---|---|---|---|
| SRC-OPENAI-AGENTS | OpenAI Agents Guide | <https://developers.openai.com/api/docs/guides/agents> | Verified | エージェント、ツール、状態、ガードレール、評価、観測性の参照軸 |
| SRC-OPENAI-HITL | OpenAI Agents SDK Human-in-the-loop | <https://openai.github.io/openai-agents-python/human_in_the_loop/> | Verified | HITL、ツール承認、承認パケット設計の参照軸 |
| SRC-OPENAI-TRACING | OpenAI Agents SDK Tracing | <https://openai.github.io/openai-agents-python/tracing/> | Verified | トレース、Run、ツール実行ログ、観測性の参照軸 |
| SRC-OPENAI-EVALS | OpenAI Evals Guide | <https://developers.openai.com/api/docs/guides/evals> | Redirected | 評価ケース、回帰評価、評価設計の参照軸。旧 `platform.openai.com/docs/guides/evals` は開発者ドキュメントへ遷移する |
| SRC-ANTHROPIC-CONTEXT | Anthropic: Effective context engineering for AI agents | <https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents> | Verified | Context Pack、長時間タスク、コンテキスト管理の参照軸 |
| SRC-ANTHROPIC-TOOLS | Anthropic: Writing effective tools for AI agents | <https://www.anthropic.com/engineering/writing-tools-for-agents> | Verified | Tool Spec Card、ツール設計、ツール返却情報の参照軸 |

### セキュリティ・ガバナンス

| Source ID | 名称 | URL | 状態 | 本書での用途 |
|---|---|---|---|---|
| SRC-OWASP-LLM | OWASP Top 10 for LLM Applications 2025 | <https://genai.owasp.org/llm-top-10/> | Verified | LLMアプリケーションの主要リスク分類 |
| SRC-OWASP-LLM-LEGACY | OWASP Top 10 for Large Language Model Applications project page | <https://owasp.org/www-project-top-10-for-large-language-model-applications/> | Verified | OWASP GenAI Security Projectの入口。本文では正規参照を `SRC-OWASP-LLM` に寄せる |
| SRC-OWASP-AGENTIC | OWASP Top 10 for Agentic Applications 2026 | <https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/> | Verified | エージェント型AI固有のリスク分類 |
| SRC-NIST-AI-RMF | NIST AI Risk Management Framework | <https://www.nist.gov/itl/ai-risk-management-framework> | Verified | Govern / Map / Measure / Manage を含むAIリスク管理の参照軸 |
| SRC-NIST-GENAI-PROFILE | NIST AI 600-1: Generative AI Profile | <https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence> | Verified | 生成AI固有リスクをAI RMFへ重ねる参照軸 |
| SRC-ISO-42001 | ISO/IEC 42001:2023 | <https://www.iso.org/standard/42001> | Verified | AIマネジメントシステムの標準への参照 |
| SRC-ISO-AIMS | ISO overview: AI management systems | <https://www.iso.org/artificial-intelligence/ai-management-systems> | Verified | ISO/IEC 42001の説明補助 |
| SRC-EU-AI-LITERACY | EU AI Act AI Literacy Q&A | <https://digital-strategy.ec.europa.eu/en/faqs/ai-literacy-questions-answers> | Verified | AIリテラシー、教育設計、ロール別学習の参照軸 |

### 人間側能力・チーム設計

| Source ID | 名称 | URL | 状態 | 本書での用途 |
|---|---|---|---|---|
| SRC-LENNY-INNER-GAME | Lenny's Newsletter: The new inner game | <https://www.lennysnewsletter.com/p/the-new-inner-game-your-unfair-advantage> | Limited | discernment、conflict、willingness to fail、positive self-talk、NBA-ificationの参照軸。記事は有料部分を含むため、本書では公開範囲で確認できた内容と実践仮説を分けて扱う |

### 本書公開情報

| Source ID | 名称 | URL | 状態 | 用途 |
|---|---|---|---|---|
| SRC-BOOK-PUBLIC-URL | 本書公開URL | <https://itdojp.github.io/ai-agent-collaboration-book/> | Verified 2026-07-01 | 公開サイトの正本URL |
| SRC-BOOK-REPOSITORY | 本書リポジトリURL | <https://github.com/itdojp/ai-agent-collaboration-book> | Verified 2026-07-01 | 公開済みリポジトリ、Issues、Pull Requests、更新履歴 |

## 本文中の出典キー利用方針

本文では、外部資料の詳細URLを直接展開しない。外部根拠に依存する箇所では、次のようにSource Notesへ誘導する。

```text
出典キー: SRC-OWASP-LLM, SRC-OWASP-AGENTIC
詳細URLと確認日は source-notes.md を参照。
```

この方針により、将来URLや仕様が変わった場合でも、本文全体を改稿せずにSource Notesを更新できる。

## 読者向け利用上の注意

- 本ページは、本文の背景にある参照先と確認状態を示すための索引であり、各資料の全文解説ではない。
- 外部資料、規格、法令、ベンダー仕様は将来変更され得る。実務適用時は、必ず一次情報、自社規程、顧客契約、対象国・業界の規制を確認する。
- `Limited` の資料は公開範囲に制約がある。本文では、公開範囲で確認できる内容と実務上の変換仮説を分けて扱う。
