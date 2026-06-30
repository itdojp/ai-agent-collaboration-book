---
title: "付録E: 用語集"
source_path: "appendices/e-glossary.md"
order: 330
book_section: "appendices"
---
# 付録E: 用語集

本付録は、本書で使う主要用語、成果物名、レベル接頭辞を標準表記として固定するための用語集である。日本語名と英語名がある場合、初出では併記し、以後は本文の文脈に応じてどちらかを使う。

## E.1 基本概念

| 用語 | 定義 |
|---|---|
| AIエージェント | 目的に応じて複数ステップで処理し、必要に応じてツール、外部情報、メモリ、承認を使うAI利用形態 |
| チャットAI | ユーザー入力に対して回答や文章を生成する対話型AI |
| ワークフロー | あらかじめ決められた手順に沿って処理する自動化 |
| RAG | Retrieval-Augmented Generation。外部文書やナレッジを検索し、生成に使う仕組み |
| MCP | Model Context Protocol。AIと外部ツール・データソースを接続するためのプロトコルとして使われる概念 |
| HITL | Human-in-the-loop。AIの処理途中に人間確認、承認、差し戻し、停止を入れる設計 |
| ガードレール | AIの入力、出力、ツール実行、権限、承認を制御する仕組み |
| AIエージェント協働ループ | 仕事選定、依頼、文脈、委任、検証、権限制御、ログ改善、人間判断を循環させる本書の基本ループ |
| 6層モデル | Work / Request / Context / Delegation / Control / Human・Org の6層でAI協働を設計する枠組み |

## E.2 成果物名

| 日本語名 | 英語名 | 主な章 | 定義 |
|---|---|---:|---|
| 本書活用計画 | Reading Route Plan | 0 | 読者が本書をどう使うかを決める計画 |
| AIエージェント協働ブループリント | AI Agent Collaboration Blueprint | 1 | 人間、業務、AI、権限、レビュー、ログの全体像 |
| AI適用判断シート | AI Use Case Fit Sheet | 2 | AIに任せる仕事をリスクとROIで判断するシート |
| AIエージェント依頼書 | Request Contract | 3 | AIへの依頼を目的、入力、制約、出力、品質基準、人間確認条件を含む仕様として定義したもの |
| コンテキストパック | Context Pack | 4 | AIに渡す前提情報、過去経緯、制約、関連資料、機密区分を構造化したもの |
| タスク概要 | Task Brief | 5 | AIに任せる作業単位を定義した文書 |
| タスク分解表 | Task Breakdown | 5 | 大きな業務をサブタスクへ分解した表 |
| AI出力レビュー表 | AI Output Review Sheet | 6 | AI出力を目的、事実、根拠、論理、リスクで確認する表 |
| レビュー課題ログ | Review Issue Log | 6 | AI出力レビューで見つけた問題をSeverity付きで残すログ |
| 評価計画 | Evaluation Plan | 6 | AI活用の品質を継続的に測るための評価計画 |
| ツール仕様カード | Tool Spec Card | 7 | AIが使うツールの目的、入力、出力、禁止操作、失敗時挙動を定義するカード |
| ツール権限マトリクス | Tool Permission Matrix | 7 | ツール操作ごとの権限、承認、ログを定義する表 |
| HITL承認フロー | HITL Approval Flow | 7 | AI実行中に人間承認を入れる流れ |
| Permission Test | Permission Test | 7 | AIが権限外操作をしないか確認するテスト |
| 実行ログ | Agent Run Log | 8 | AIエージェントの入力、出力、参照情報、ツール実行、承認、失敗を記録するログ |
| トレースイベント記録 | Trace Event Record | 8 | Run内の個別イベントを記録する単位 |
| 改善バックログ | Improvement Backlog | 8 | Runレビューや失敗から改善項目を蓄積するバックログ |
| AIセキュリティチェックリスト | AI Security Checklist | 9 | AI利用のセキュリティ・プライバシー観点を確認するチェックリスト |
| AIシステム台帳 | AI System Inventory | 10 | 組織内のAI利用を管理する台帳 |
| AIリスク登録簿 | AI Risk Register | 10 | AI利用ごとのリスク、Owner、対応、残リスクを管理する表 |
| AI System ADR | AI System ADR | 10 | AIシステム利用・設計上の重要判断を記録するADR |
| 判断メモ | Decision Brief | 11 | AI提案の採用、修正、棄却、実験化、停止を判断する文書 |
| 判断基準マトリクス | Decision Criteria Matrix | 11 | 判断基準と重みを整理する表 |
| やめる判断シート | Kill Decision Sheet | 11 | 施策やAI利用を停止・縮小・廃棄するための判断シート |
| リスク受容メモ | Risk Acceptance Memo | 11 | 残リスクを認識したうえで受容する記録 |
| Connection Debt診断 | Connection Debt Assessment | 12 | 言うべきことを言わないことで蓄積している組織負債を診断するシート |
| 困難な会話メモ | Difficult Conversation Brief | 12 | 困難な会話の目的、事実、論点、合意候補を整理する文書 |
| 合意ログ | Agreement Log | 12 | 会話後の合意事項、未決事項、次アクションを記録するログ |
| AI実験設計シート | AI Experiment Design Sheet | 13 | 仮説、最小実験、成功条件、失敗条件、やめる条件を定義するシート |
| 失敗レビューシート | Failure Review Sheet | 13 | 失敗を責任追及ではなく学習として整理するシート |
| Side Quest Charter | Side Quest Charter | 13 | 公式ロードマップ外の小実験の目的、制約、停止条件を定義する文書 |
| 行動ブロッカー診断 | Action Blocker Assessment | 14 | 行動停止の原因を実リスク、想像上のリスク、最小行動へ分解するシート |
| セルフトーク記録 | Self-talk Transcript | 14 | 頭の中の自己批判や不安を書き出す記録 |
| 最小行動契約 | Minimum Action Contract | 14 | 次に実施する最小行動、期限、レビュー依頼先を定義する文書 |
| ロール別スキル定義 | Role Skill Profile | 15 | 職種ごとの必要能力と到達レベルを定義する表 |
| 実技評価パック | Practical Assessment Pack | 15 | 評価課題、提出物、採点基準を含む評価セット |
| Evidence Portfolio | Evidence Portfolio | 15 | 認定判断に使う成果物、ログ、レビュー証跡の束 |
| 展開憲章 | Rollout Charter | 16 | AIエージェント協働を組織展開する目的、範囲、責任者を定義する文書 |
| AIイネーブルメント運用モデル | AI Enablement Operating Model | 16 | AI CoE、部門責任者、情シス、セキュリティ、管理職の役割分担 |
| AI Enablement Portal | AI Enablement Portal | 16 | 教材、テンプレート、FAQ、ポリシー、Office Hourを集約する社内ポータル |

## E.3 レベル接頭辞一覧

| 領域 | 表記 | 主な章 | 意味 |
|---|---|---:|---|
| AI適用段階 | A0〜A5 | 2 | AIをどの程度業務へ組み込むか |
| 権限レベル | P0〜P7 | 7 | no-accessからadminまでの権限段階 |
| 観測性レベル | O0〜O5 | 8 | ログ、トレース、評価、改善の成熟度 |
| セキュリティレベル | S0〜S5 | 9 | AI利用に必要なセキュリティ管理の重さ |
| ガバナンスレベル | G0〜G5 | 10 | 台帳、承認、監査、教育の統制度 |
| 判断レベル | J0〜J5 | 11 | AI出力をどう人間判断へ接続するか |
| Connection Debtレベル | C0〜C5 | 12 | 未処理対立・未伝達事項の重さ |
| 実験レベル | X0〜X5 | 13 | 個人メモ実験から展開前検証までの実験重さ |
| 評価証拠レベル | EV0〜EV5 | 15 | 自己申告から運用証跡までの評価証拠の強さ |
| スキルレベル | Lv1〜Lv6 | 15 | 個人・チーム・全社設計能力の到達段階 |

## E.4 リスク・統制用語

| 用語 | 定義 |
|---|---|
| プロンプトインジェクション | 外部文書や入力に含まれる悪意ある指示によって、AIの挙動が乗っ取られるリスク |
| 不安全な出力処理 | AI出力を検証せず、コード、SQL、コマンド、メールなどに利用すること |
| 過剰なエージェンシー | AIに必要以上の自律性、権限、実行範囲を与えること |
| Approval Packet | 承認者が判断するために必要な差分、根拠、リスク、影響範囲のまとまり |
| Security Exception | 通常禁止または制限される利用を、期限付き・条件付きで例外承認すること |
| Risk Acceptance | 残リスクを認識し、Ownerを置いたうえで受容する判断 |
| AI Incident | AI利用に起因する誤出力、誤送信、情報漏洩、権限誤用、顧客影響などの事象 |

## E.5 人間・組織系用語

| 用語 | 定義 |
|---|---|
| Discernment | AIが提示する情報や選択肢を、人間の目的、責任、制約、リスクと照合して採否判断する能力 |
| Connection Debt | 重要な相手に伝えるべきことを伝えず、期待、懸念、対立、責任境界が未整理のまま蓄積する負債 |
| Pace | 仮説から試行、学習までの速度 |
| Spin | 不安、迷い、調整過多、責任回避によって空回りしている度合い |
| Action Blocker | 自己批判、不安、完璧主義などにより行動が止まっている要因 |
| Review Only | まだ採用判断をせず、レビュー対象として扱う状態 |
| Draft | 完成物ではなく、レビューと改善のための下書き |
