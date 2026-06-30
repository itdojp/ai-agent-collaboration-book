# Source Notes

このファイルは、本文で参照する主要情報源と、章別に確認すべき論点を管理するためのメモである。公開前には、本文中の断定表現、URL、規格名、規制名、ツール仕様を再確認する。

- 最終整理日: 2026-06-29
- URL確認日: 2026-06-27
- 確認方針: 本文は特定ベンダーの詳細仕様ではなく、成果物と設計原則を中心にする。
- 優先ルール: 実導入時には、本書よりも自社規程、顧客契約、業界規制、個人情報保護、情報セキュリティ基準を優先する。
- 本文中の表記方針: 外部情報源を直接本文に長く埋め込まず、本文では出典キー `SRC-*` を示し、詳細URLは本ファイルで管理する。

## URL確認結果

確認ステータスの意味は以下である。

```text
Verified: 2026-06-27時点でページを確認できた
Redirected: 旧URLから別URLへ遷移するため、正規URLへ変更した
Planned: 本書公開予定URLなど、公開前で検証対象外
Limited: 一部有料・一部非公開など、公開範囲に制約がある
Verified empty repository: GitHub上で空リポジトリとして確認済み
```

### 既存シリーズ関連

| Source ID | 名称 | URL | 状態 | 本書での用途 |
|---|---|---|---|---|
| SRC-ITDO-KA | ITエンジニア知識アーキテクチャ | <https://itdojp.github.io/it-engineer-knowledge-architecture/> | Verified | シリーズ内での位置づけ、既存書籍接続 |
| SRC-ITDO-PUBLISHING | 出版ガイド | <https://itdojp.github.io/it-engineer-knowledge-architecture/publishing/> | Verified | 書籍構成、公開前レビュー、シリーズ標準 |
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

### 本書の予定URL

| Source ID | 名称 | URL | 状態 | 用途 |
|---|---|---|---|---|
| SRC-BOOK-PUBLIC-URL | 本書公開予定URL | <https://itdojp.github.io/ai-agent-collaboration-book/> | Planned | 公開後に確認する |
| SRC-BOOK-REPOSITORY | 本書リポジトリURL | <https://github.com/itdojp/ai-agent-collaboration-book> | Verified empty repository 2026-06-29 | 初回push前の公開リポジトリとして確認済み |

## 本文中の出典キー利用方針

本文では、外部資料の詳細URLを直接展開しない。外部根拠に依存する箇所では、次のようにSource Notesへ誘導する。

```text
出典キー: SRC-OWASP-LLM, SRC-OWASP-AGENTIC
詳細URLと確認日は source-notes.md を参照。
```

この方針により、将来URLや仕様が変わった場合でも、本文全体を改稿せずにSource Notesを更新できる。

## 章別メモ

### 第0章 本書の読み方

第0章は、既存章の導線、6層モデル、成果物、読者タイプ、演習の使い方を整理する導入章である。外部事実や規制解説を新たに追加しないため、特定の公開資料に依存しない。

確認観点:

- 自社のAI利用ポリシー、利用可能AIツール、情報分類、社外送信ルールに合わせる。
- 読者別ルートは標準案であり、社内ロールに応じて調整する。

### 第1章 AIエージェント協働とは何か

参照Source ID: `SRC-OPENAI-AGENTS`, `SRC-ANTHROPIC-CONTEXT`

AIエージェントを、チャットAI、ルールベース自動化、ワークフローと区別して説明する章である。特定実装ではなく、ツール、メモリ、状態、承認、ログを含む業務システムとして扱う。

確認観点:

- 利用するAI基盤のエージェント定義と矛盾しないか。
- 自律性、権限、外部影響、可逆性、観測性の説明が社内用語と整合するか。

### 第2章 AIに任せる仕事、任せない仕事

仕事選定、ROI、リスク、AI適用段階を扱う章である。

確認観点:

- 高リスク業務の例が、自社の業務、法務、セキュリティ上の禁止事項と整合するか。
- AI適用段階 `A0〜A5` の用語が社内のリスク分類と衝突しないか。

### 第3章 依頼を契約にする

Request Contractを扱う章である。ここでいう「契約」は法的契約ではなく、AIへの依頼仕様を意味する。

確認観点:

- 法務契約と誤解されないよう、必要に応じて「依頼仕様」と併記する。
- 社外提出物に使う場合は、出典、事実確認、社内承認条件を明示する。

### 第4章 Context Packを設計する

参照Source ID: `SRC-ANTHROPIC-CONTEXT`, `SRC-ANTHROPIC-TOOLS`, `SRC-OPENAI-AGENTS`

AIに渡す前提情報、資料、鮮度、確度、機密区分を扱う章である。

確認観点:

- RAG、メモリ、会話履歴、ツール結果の保存先と保持期間を確認する。
- Context Packに認証情報、顧客機密、不要な個人情報を含めない。

### 第5章 タスク分解と委任

AIへの丸投げを避け、Task Brief、Checkpoint、Stop / Escalation Rules、Restart Packetに分解する章である。

確認観点:

- チェックポイント、停止条件、エスカレーション条件が業務フローと整合するか。
- 本番、顧客、契約、法務、個人情報に関わるタスクをAIに単独完了させていないか。

### 第6章 AI出力レビューと評価

参照Source ID: `SRC-OPENAI-EVALS`, `SRC-OPENAI-AGENTS`

レビュー、評価、検証、承認の違いを扱う章である。

確認観点:

- レビュー基準が職種別に十分具体化されているか。
- 評価データセットやレビュー結果に機密情報が含まれる場合の扱い。

### 第7章 ツール・権限・HITL

参照Source ID: `SRC-OPENAI-HITL`, `SRC-ANTHROPIC-TOOLS`, `SRC-OPENAI-AGENTS`

ツール権限、HITL、承認パケット、Permission Testを扱う章である。

確認観点:

- ツール単位ではなく操作単位で権限を設計しているか。
- 第10章のUse Case Approval、Risk Acceptance、Security Exceptionと混同していないか。

### 第8章 ログ・トレース・継続改善

参照Source ID: `SRC-OPENAI-TRACING`, `SRC-OPENAI-AGENTS`

Agent Run Log、Trace Event Record、Improvement Backlogを扱う章である。

確認観点:

- ログに入力、出力、参照文書、ツール引数、承認コメント、個人情報が含まれる可能性を確認する。
- 保持期間、アクセス権、マスキング、削除条件を決める。

### 第9章 セキュリティとプライバシー

参照Source ID: `SRC-OWASP-LLM`, `SRC-OWASP-AGENTIC`, `SRC-NIST-AI-RMF`, `SRC-NIST-GENAI-PROFILE`

AIセキュリティの参照元として、OWASP Top 10 for LLM Applications、OWASP Top 10 for Agentic Applications、NIST AI RMFを想定する。本文は逐語的な解説ではなく、設計成果物へ落としたものとして扱う。

確認観点:

- Prompt Injection、Excessive Agency、Sensitive Information Disclosure、不安全な出力処理、MCP/外部ツールリスクを自社環境で確認する。
- DLP、SIEM、ログ基盤、ID管理、個人情報保護要件と整合させる。

### 第10章 ガバナンスと統制

参照Source ID: `SRC-ISO-42001`, `SRC-ISO-AIMS`, `SRC-NIST-AI-RMF`, `SRC-NIST-GENAI-PROFILE`, `SRC-EU-AI-LITERACY`, `SRC-OWASP-LLM`, `SRC-OWASP-AGENTIC`

ISO/IEC 42001、NIST AI RMF、EU AI Act AI Literacy Q&A、OWASP系リスクを参照軸として、台帳、リスク分類、承認、教育、インシデント対応、廃止へ落とす。

確認観点:

- 対象国、業界、顧客契約、個人情報保護、監査要件に応じて法務・セキュリティ・個人情報保護担当と確認する。
- AI System Inventory、Risk Register、Training Register、Audit Evidence PackのOwnerを定義する。

### 第11章 AI時代の判断力

参照Source ID: `SRC-LENNY-INNER-GAME`

Lenny's Newsletterで提示されるdiscernmentの観点を、Decision Brief、Decision Criteria Matrix、Kill Decision Sheet、Risk Acceptance Memoへ変換して扱う。

確認観点:

- 本章は法務、投資、労務、人事、医療、金融などの専門判断を代替しない。
- 高リスク判断では、社内規程、契約、法令、専門家レビューを確認する。

### 第12章 困難な会話と対立処理

参照Source ID: `SRC-LENNY-INNER-GAME`

Lenny's Newsletterで提示されるconflictの観点を、Connection Debt診断、Difficult Conversation Brief、Agreement Logへ変換して扱う。

確認観点:

- 人事、労務、ハラスメント、差別、法務、セキュリティ、不正調査、メンタルヘルスなどの専門対応を代替しない。
- 高リスクまたは安全性が関わる場合は、社内規程に従い専門部署へエスカレーションする。

### 第13章 失敗耐性と実験文化

参照Source ID: `SRC-LENNY-INNER-GAME`

Lenny's Newsletterで提示されるwillingness to failの観点を、AI実験設計シート、Failure Review Sheet、Learning Log、Pace / Spin Reviewへ変換して扱う。

確認観点:

- 実験レベルは `X0〜X5` を使う。
- 顧客影響、本番システム、個人情報、契約、法務、セキュリティに関わる実験は、社内規程に従う。

### 第14章 セルフトークと高レバレッジ環境

参照Source ID: `SRC-LENNY-INNER-GAME`

Lenny's Newsletterで提示されるpositive self-talkの観点を、Action Blocker診断、Self-talk Transcript、Minimum Action Contractへ変換して扱う。

確認観点:

- 本章は医療、心理療法、労務、人事、ハラスメント、メンタルヘルス対応を代替しない。
- 個人の記録を共有・評価に使う場合は、本人同意、利用目的、閲覧権限、保存期間を明確にする。

### 第15章 スキルマップと評価

第1章から第14章までで定義したAIエージェント協働能力を、評価、実技課題、学習パス、認定、権限付与へ接続する。

確認観点:

- 評価証拠レベルは `EV0〜EV5` を使う。
- 評価結果を査定、報酬、権限付与、ログ監視、人事評価へ接続する場合は、人事、労務、法務、個人情報保護、セキュリティ、監査の要件を確認する。

### 第16章 組織展開と教材化

参照Source ID: `SRC-EU-AI-LITERACY`, `SRC-ITDO-UX-PROFILES`, `SRC-ITDO-UX-MODULES`

本書の内容を社内教材、テンプレート、Office Hour、認定、KPI、90日展開計画へ変換する章である。

確認観点:

- 社内研修、教育履歴、認定結果、権限付与、評価利用、ログ利用を社内規程と整合させる。
- AI CoE、部門Owner、管理職、Security、Legal、HR、Platform / ITの役割分担を明確にする。

## 公開前再確認リスト

- [ ] URLが有効である。
- [ ] 規格名、法令名、団体名、ツール名が最新である。
- [ ] 特定ベンダー仕様に依存する記述をSource Notesまたは脚注で限定している。
- [ ] 医療、法律、労務、人事、金融、セキュリティの専門判断を代替する表現がない。
- [ ] Lenny's Newsletter由来の内容は、公開範囲で確認できる内容と実践仮説を分けている。
- [ ] 実験レベルは `X0〜X5`、評価証拠レベルは `EV0〜EV5` で統一されている。
- [ ] 付録Eの用語集と本文表記が一致している。
