# Changelog

## Unreleased

- Artifact Indexの先頭に目的別入口・職種別入口を追加し、成果物一覧を長大表から章領域別の短いカード形式へ再構成。
- Quick Startの3時間版を横長表から時間帯別ステップへ変更し、Web表示で読みやすくした。
- Figure Indexに図表IDから用途・関連章を追う早見表を追加。

## 0.23.0-revised - 2026-06-27

- Source NotesのURL確認結果を、Source ID、正規URL、状態、用途の表へ再構成。
- 旧 `platform.openai.com/docs/guides/evals` 表記を、正規URL `developers.openai.com/api/docs/guides/evals` へ整理。
- OWASP LLM Top 10は正規参照を `genai.owasp.org/llm-top-10/` に寄せ、旧OWASPプロジェクトページは入口として整理。
- NIST Generative AI Profileの正規参照として `SRC-NIST-GENAI-PROFILE` を追加。
- 本文中の外部出典表記を `SRC-*` 形式へ統一し、第9章・第10章の外部フレームワーク記述からSource Notesへ誘導。
- 第1章、第4章、第6章〜第14章、第16章のSource Notesへ参照Source IDを追加。
- Lenny's Newsletter由来の内容は `Limited` として扱い、公開範囲で確認できた内容と実践仮説を分離する注意を追記。
- README、title、colophon、MANIFEST、book-configを `0.23.0-revised` に更新。

## 0.22.0-revised - 2026-06-27

- 追加図表F-07〜F-15を `figures/` 配下に追加。
- 第7章〜第15章へ関連図表リンクを追加。
- `figure-index.md` の追加候補を追加済み図表へ更新。
- `review/ADDITIONAL_FIGURES_SUMMARY.md` を追加。
- README、title、colophon、MANIFEST、book-configを `0.22.0-revised` に更新。


## 0.21.0-revised - 2026-06-27

- 第0章「本書の読み方」を導入章として圧縮。
- 旧版の詳細ケース、章別詳細説明、成果物詳細を後続章、Artifact Index、付録D〜Gへの参照に整理。
- 文字数を約19,800字から約9,100字へ削減し、導入章としての読みやすさを優先。
- `CHAPTER_00_DRAFT_SUMMARY.md` を圧縮後の内容に更新。
- `review/CHAPTER_00_COMPRESSION_SUMMARY.md` を追加。
- `review/REVIEW_APPLIED_SUMMARY.md` のR-010を完了に更新。
- README、title、colophon、MANIFEST、book-configを `0.21.0-revised` に更新。


## 0.20.0-revised - 2026-06-27

- 第15章と第16章の重複圧縮を実施。
- 第15章の責務を、能力定義、評価証拠、不足領域の引き渡し、認定判定へ限定。
- 第16章の責務を、教材化、Role-based Learning Path、Office Hour、KPI、認定運用、90日展開計画へ限定。
- `Learning Path Matrix`を`Learning Gap Handoff`へ置き換え、第16章の`Role-based Learning Path`との責務衝突を解消。
- 第15章・第16章双方に責務境界表を追加。
- 認定について、第15章は合格基準と判定記録、第16章は導入順序、権限付与、台帳反映、再評価、例外処理を扱うように整理。
- 付録A、Artifact Index、Exercise Bank、Chapter Summary、book-configを更新。

## 0.19.0-revised - 2026-06-27

- 横断レビュー結果のP1修正を本文へ反映。
- 第13章の実験レベルを `X0〜X5` に変更し、第15章の評価証拠レベルを `EV0〜EV5` に変更。
- 全章の `Source Notes` 見出しを統一し、第0章、第14章、第16章へSource Notesを追加。
- 第9章へ `典型的な失敗` と `設計原則` を追加。
- 第10章、第14章へ `設計原則` を追加。
- 第7章へ、第10章との承認責務分離表を追加。
- Quick Startへ3時間版の6層モデル拡張導線を追加。
- 付録D〜Hを本文の成熟度に合わせて拡張。
- 付録Eへ用語集、成果物名、レベル接頭辞一覧を追加。
- `figures/` 配下に優先図表7点を追加し、`figure-index.md` を更新。
- `source-notes.md` を全体方針、主要参照ソース、章別メモ、公開前再確認リストへ再構成。
- 反映状況を `review/REVIEW_APPLIED_SUMMARY.md` として追加。

## 0.18.0-review

- 第0章〜第16章、付録、補助資料を対象に全章横断レビューを実施。
- `review/CROSS_CHAPTER_REVIEW.md` を追加。
- `review/ISSUE_BACKLOG_FROM_REVIEW.md` を追加。
- `review/TERMINOLOGY_REVIEW.md` を追加。
- `review/CHAPTER_MATRIX_REVIEW.md` を追加。
- `review/CODEX_REVIEW_TASKS.md` を追加。
- 公開前P1課題として、レベル接頭辞衝突、章末Source Notes統一、第9章・第10章・第14章・第16章の章末整備、付録D〜H拡張、Source Notes再構成、図表追加を整理。

## 0.17.0-draft - 2026-06-27

- 第0章「本書の読み方」を公開初稿相当へ拡張。
- 第0章に、読者別導線、3つの読み方、6層モデル、成果物の流れ、共通ケース、実務ケース、典型的な読み方の失敗、設計原則、Reading Route Plan、チェックリスト、演習、既存シリーズへの接続、更新前提を追加。
- 付録Aに「本書活用計画 / Reading Route Plan」を追加。
- 付録Bに「本書活用開始チェック」を追加。
- Artifact Index に「本書活用計画 / Reading Route Plan」を追加し、成果物依存関係に接続。
- Exercise Bank に第0章演習を追加。
- book-config、README、title、colophon、MANIFEST、Chapter Acceptance Criteria、source-notesを更新。

## 0.16.0-draft - 2026-06-27

- 第16章「組織展開と教材化」を公開初稿相当へ拡張。
- 第16章に、組織展開のゴール、展開対象者分類、教材体系、MVP教材20点、Role-based Learning Path、AI Enablement Operating Model、AI Enablement Portal、Office Hour、Use Case Portfolio、90日展開計画、2時間ワークショップ、認定制度、KPI、継続改善サイクル、典型的な失敗を追加。
- 第16章に、CS部門、開発チーム、管理職研修の展開ケースを追加。
- 付録AにA.16系テンプレートを追加。
- 付録BにB.19「組織展開・教材化チェック」を追加。
- Artifact Indexに第16章成果物を追加。
- Exercise BankにExercise 16を追加。
- source-notes.md、chapter-acceptance-criteria.md、book-config.json、MANIFEST.md、title.md、colophon.mdを更新。

## 0.15.0-draft - 2026-06-27

- 第15章「スキルマップと評価」を公開初稿相当へ拡張。
- 第15章に、評価原則、12能力領域、6層モデルとの対応、Lv1〜Lv6のレベル定義、職種別到達目標、Role Skill Profile、評価証拠レベル、Skill Diagnosis Form、Practical Assessment Pack、Evidence Portfolio、Learning Path Matrix、Certification Design、評価ワークフロー、評価者校正、プライバシー上の注意を追加。
- CS担当者、マネージャー、エンジニア、AI推進担当の4ケースを追加。
- 付録Aに、Skill Map、Role Skill Profile、Skill Diagnosis Form、Practical Assessment Pack、Evidence Portfolio、Learning Path Matrix、Certification Decision Record、Evaluator Calibration Record、記入例を追加。
- 付録Bに「スキルマップ・評価設計チェック」を追加。
- 付録C「スキル評価ルーブリック」を詳細版へ更新。
- Artifact Indexに第15章成果物を追加し、成果物依存関係を更新。
- Exercise Bankに第15章演習を追加。

## 0.14.0-draft - 2026-06-27

- 第14章「セルフトークと高レバレッジ環境」を公開初稿相当へ拡張。
- 第14章に、セルフトークの定義、セルフトークの業務影響、健全な品質基準と完璧主義の違い、健全なレビューと自己批判の違い、行動ブロッカー分類、Action Blocker診断、Self-talk Transcript、Review vs Self-criticismチェック、Minimum Action Contract、AI依頼パターンを追加。
- AI活用実験の共有が遅れるケース、AIへの不安で学習が止まるケース、管理職が部下のAI活用をレビューできないケース、失敗レビューが人格評価になるケースを追加。
- 付録Aに、Action Blocker診断、Self-talk Transcript、Review vs Self-criticismチェック、Minimum Action Contract、Support Request、Energy / Attention Budget、Manager Coaching Note、記入例を追加。
- 付録Bに「セルフトーク・高レバレッジ環境チェック」を追加。
- Artifact Indexに第14章成果物を追加し、成果物依存関係を更新。
- Exercise Bankに第14章演習を追加。

## 0.13.0-draft - 2026-06-27

- 第13章「失敗耐性と実験文化」を公開初稿相当へ拡張。
- 第13章に、効率化・改善・実験・展開の区別、実験レベルX0〜X5、AI実験設計シート、20 Experiments Sheet、Experiment Portfolio、Pace / Spin、Failure Review Sheet、Learning Log、Side Quest Charterを追加。
- 営業提案、顧客返信案生成AI、RAG改善、開発PR作成エージェント、対立の実験化の5ケースを追加。
- 付録AにA.13系テンプレートを追加し、旧A.32〜A.34をA.13/A.14へ整理。
- 付録Bに「失敗耐性・実験文化チェック」を追加。
- Artifact Indexに20 Experiments Sheet、Experiment Portfolio、Pace / Spin Review、Learning Log、Experiment Kill Criteria、Side Quest Charterを追加。
- Exercise Bankに第13章演習を追加。

## 0.12.0-draft - 2026-06-27

- 第12章「困難な会話と対立処理」を公開初稿相当へ拡張。
- 第12章に、対立の定義、Connection Debtの定義、対立の種類、Connection DebtレベルC0〜C5、Conflict Type Map、Difficult Conversation Brief、Perspective Map、Conversation Plan、Agreement Log、Follow-up Contract、Backchannel Control Ruleを追加。
- 開発と営業の対立、AIレビューをめぐる対立、管理職が部下に言うべきことを避けているケース、セキュリティと事業部の対立、AI導入に対する現場の抵抗の5ケースを追加。
- 付録Aに、Connection Debt診断、Conflict Type Map、Difficult Conversation Brief、Perspective Map、Conversation Plan、Agreement Log、Follow-up Contract、Backchannel Control Rule、記入例を追加。
- 付録Bに「困難な会話・対立処理チェック」を追加。
- Artifact Index に第12章成果物を追加し、成果物依存関係を更新。
- Exercise Bank に第12章演習を追加。

## 0.11.0-draft - 2026-06-27

- 第11章「AI時代の判断力」を公開初稿相当へ拡張。
- 第11章に、判断力の定義、AIに任せられる判断補助と人間が担う判断、判断の種類、判断レベルJ0〜J5、Decision Brief、判断前チェックリスト、Decision Criteria Matrix、Option Evaluation Table、AI依頼パターン、判断回避、感情と判断、やめる判断、実験化判断、リスク受容判断、判断後レビューを追加。
- 顧客返信案生成AIの全社展開判断、AIによるCRM更新判断、使われていないRAGの廃止判断、AI提案書の部分採用判断の4ケースを追加。
- 付録Aに、Decision Brief、判断前チェックリスト、Decision Criteria Matrix、Option Evaluation Table、Kill Decision Sheet、Risk Acceptance Memo、Decision Review Log、記入例を追加。
- 付録Bに「AI時代の判断力チェック」を追加。
- Artifact Index に第11章成果物を追加し、成果物依存関係を更新。
- Exercise Bank に第11章演習を追加。

## 0.10.0-draft - 2026-06-27

- 第10章「ガバナンスと統制」を公開初稿相当へ拡張。
- 第10章に、AIガバナンスとセキュリティ・運用の違い、外部フレームワークの使い方、ガバナンス基本原則、ガバナンス対象、AI利用ポリシー、AI System Inventory、G0〜G5のGovernance Level Matrix、承認フロー、AI System ADR、AI Risk Register、ベンダー・外部AI・MCP管理、教育とAIリテラシー、監査証跡、AI Incident Runbook、例外管理、変更管理、廃止と棚卸し、組織体制、コスト統制を追加。
- 社内AI活用の棚卸し、顧客問い合わせ対応エージェント本番化、GitHub PR作成エージェント、契約書レビュー補助AI、外部MCPサーバー追加、AI利用ポリシー違反の6ケースを追加。
- 付録AのAI System Inventoryを、AI Use Policy、AI Use Case Intake、Governance Level Matrix、AI Risk Register、Approval Workflow、AI System ADR、AI Vendor Review Record、AI Training Register、AI Incident Runbook、AI Audit Evidence Pack、AI Retirement Plan、Governance Review Logを含む形に拡張。
- 付録Bに「ガバナンス・統制設計チェック」を追加。
- Artifact Index に第10章成果物を追加し、成果物依存関係を更新。
- Exercise Bank に第10章演習を追加。


## 0.9.0-draft - 2026-06-27

- 第9章「セキュリティとプライバシー」を公開初稿相当へ拡張。
- 第9章に、AIエージェントの攻撃面、主要リスク12分類、情報分類、データ最小化、プロンプトインジェクション、不安全な出力処理、過剰なエージェンシー、RAG / ベクトルDB、メモリ汚染、外部ツール / MCP審査、ログ・トレースのプライバシー、人間の過信、セキュリティレベルS0〜S5、設計8ステップを追加。
- 外部FAQ、顧客問い合わせ対応、AI生成SQL、社内ナレッジ更新、外部MCPサーバー追加、ログ情報漏洩の6ケースを追加。
- 付録Aに、AI Security Checklist、Data Classification and Handling Matrix、Untrusted Input Handling Rule、Prompt Injection Test Sheet、AI Privacy Impact Review、External Tool / MCP Review Sheet、Security Exception Record、AI Incident Trigger Matrixを追加。
- 付録Bに「セキュリティ・プライバシー設計チェック」を追加。
- Artifact Index に第9章成果物を追加し、成果物依存関係を更新。
- Exercise Bank に第9章演習を追加。


## 0.8.0-draft - 2026-06-27

- 第8章「ログ・トレース・継続改善」を公開初稿相当へ拡張。
- 第8章に、Run単位の観測、Run ID / Correlation ID、Agent Run Log、Trace Event Record、Tool Execution Log、Approval Log、Review / Evaluation Log、ログ最小化、保持期間、アクセス権、失敗分類、Improvement Backlog、Metrics Dashboard、Run Reviewを追加。
- 顧客返信の誤分類、チケット大量作成、古い資料を参照した提案書、承認内容と実行内容の差分の4ケースを追加。
- 付録AのAgent Run Logを、Trace Event Record、Tool Execution Log、Approval Log、Run Review Report、Improvement Backlog、Observability Design Sheet、Metrics Dashboard Definition、記入例を含む形に拡張。
- 付録Bに「ログ・トレース・継続改善チェック」を追加。
- Artifact Index に Trace Event Record、Tool Execution Log、Approval Log、Run Review Report、Improvement Backlog、Observability Design Sheet、Metrics Dashboard Definitionを追加し、成果物依存関係を更新。
- Exercise Bank に第8章演習を追加。

## 0.7.0-draft - 2026-06-27

- 第7章「ツール・権限・HITL」を公開初稿相当へ拡張。
- 第7章に、ツール利用リスク、権限モデル、操作単位の権限設計、HITL承認、承認パケット、Tool Spec Card、スコープ設計、APIキー管理、失敗時挙動、レート制限、ドライラン、差分プレビュー、ロールバック、Permission Testを追加。
- 顧客返信、GitHub PR作成、障害一次対応、営業CRM更新、社内ナレッジ更新の5ケースを追加。
- 付録Aのツール権限マトリクスを、Tool Spec Card、HITL承認フロー、Tool Approval Request、禁止操作リスト、Permission Test、記入例を含む形に拡張。
- 付録Bに「ツール権限・HITL設計チェック」を追加。
- Artifact Index に Tool Spec Card、Tool Approval Request、禁止操作リスト、Permission Test を追加し、成果物依存関係を更新。
- Exercise Bank に第7章演習を追加。

## 0.6.0-draft - 2026-06-27

- 第6章「AI出力レビューと評価」を公開初稿相当へ拡張。
- 第6章に、AI出力と成果物の区別、レビュー・評価・検証・承認の違い、レビュー強度 L0〜L5、基本レビュー観点、Severity、Review Issue Log、Evaluation Plan、評価ケース、回帰評価を追加。
- 競合比較表、顧客返信案、障害報告書、提案書ドラフトの4ケースを追加。
- 付録Aの AI出力レビュー表を、Review Issue Log、Evaluation Plan、レビュー強度、記入例を含む形に拡張。
- 付録Bに「AI出力レビュー前チェック」を追加。
- Artifact Index に Review Issue Log を追加し、成果物依存関係を更新。
- Exercise Bank に第6章演習を追加。

## 0.5.0-draft - 2026-06-27

- 第5章「タスク分解と委任」を公開初稿相当へ拡張。
- 第5章に、委任の定義、丸投げとの違い、Request Contract / Context Pack / Task Brief の関係、1タスク1成果物、委任レベル、チェックポイント設計、停止条件設計、エスカレーション条件設計、依存関係設計、Restart Packet を追加。
- 障害報告書、競合調査、顧客問い合わせ対応、開発タスクの4ケースを追加。
- 付録Aの Task Brief を、Task Breakdown、Checkpoint Plan、Stop / Escalation Rules、Restart Packet を含む形に拡張。
- 付録Bに「タスク委任前チェック」を追加。
- Artifact Index に Task Breakdown、Checkpoint Plan、Stop / Escalation Rules、Restart Packet を追加し、成果物依存関係を更新。
- Exercise Bank に第5章演習を追加。

## 0.4.0-draft - 2026-06-27

- 第3章「依頼を契約にする」を公開初稿相当へ拡張。
- 第3章に、Request Contract の定義、依頼モード、成果物設計、受け入れ条件、不明点の扱い、人間確認条件、競合調査・顧客返信・AI出力レビューのケースを追加。
- 第4章「Context Packを設計する」を公開初稿相当へ拡張。
- 第4章に、Context Pack の定義、コンテキスト種別、情報鮮度、確定・推定・仮定・要確認の分離、RAG・メモリ・ツール結果の扱い、長い作業での再開設計、競合調査・障害一次対応のケースを追加。
- 付録Aの Request Contract / Context Pack テンプレートを本文に合わせて拡張。
- Artifact Index に Acceptance Criteria を追加し、成果物依存関係を更新。

## 0.3.0-draft - 2026-06-27

- 第1章「AIエージェント協働とは何か」を公開初稿相当へ拡張。
- 第1章に、AIエージェント協働の定義、チャットAI・ワークフローとの差分、責任境界、協働ループ、最小構成、顧客問い合わせ対応ケース、AIエージェント協働ブループリントを追加。
- 第2章「AIに任せる仕事、任せない仕事」を公開初稿相当へ拡張。
- 第2章に、業務5分解、AIに向く仕事の判定軸、ROI・リスク評価、適用段階、仕事選定手順、競合調査・顧客問い合わせ対応ケース、AI適用判断シート記入例を追加。
- 各章に章内のSource Notes旧表記、演習判定基準、付録への参照を追加。

## 0.2.0-draft - 2026-06-25

- 中核フレームワークとして「AIエージェント協働ループ」と6層モデルを追加。
- `quickstart.md`、`concept-map.md`、`artifact-index.md`、`troubleshooting.md`、`figure-index.md` を追加。
- 付録F〜Hとして、ワークショップ設計、認定・診断問題バンク、ガバナンス・スターターパックを追加。
- `examples/recurring-case.md` と `exercises/exercise-bank.md` を追加。
- `planning/chapter-acceptance-criteria.md`、`planning/codex-task-queue.md`、`planning/style-decisions.md`、`planning/research-backlog.md` を追加。
- 全章に「章の位置づけ」と「章の受け入れ基準」を追加。
- README、index、book-config を v0.2 構成に更新。

## 0.1.0-draft - 2026-06-25

- 初期スターターを作成。
- 16章構成、付録A〜E、Codex CLI作業計画を作成。

## 0.24.0-import-ready

GitHub初回投入用に調整。

- `GITHUB_INITIAL_PUSH.md` を追加
- `docs/PARENT_SITE_INTEGRATION.md` を追加
- `.gitignore` を追加
- READMEの次作業をGitHub初回push向けに更新
- `source-notes.md` の本書リポジトリURLを確認済み扱いに更新
- `book-config.json`、`title.md`、`colophon.md` の版表記を更新

