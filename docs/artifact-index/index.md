---
title: "Artifact Index: 本書で作る成果物"
source_path: "artifact-index.md"
order: 30
book_section: "additional"
---
# Artifact Index: 本書で作る成果物

本書は概念理解だけを目的にしない。章ごとに、現場で使う成果物を作る。

| 成果物 | 用途 | 初出 | 主な利用者 |
|---|---|---|---|
| 本書活用計画 / Reading Route Plan | 読者タイプ、対象業務、読む章、最初に作る成果物、30日以内の小実験を決める | 第0章 | 全読者 |
| AIエージェント協働ブループリント | 人間、業務、AIの責任境界を最初に整理する | 第1章 | 全社員、管理職 |
| AI適用判断シート | AIに任せる仕事を選ぶ | 第2章 | 全社員、管理職 |
| AIエージェント依頼書 / Request Contract | AIへの依頼を目的、成果物、制約、受け入れ条件まで含む仕様にする | 第3章 | 全社員 |
| Acceptance Criteria | AI出力を受け入れる条件を定義する | 第3章 | 全社員、管理職 |
| Context Pack | 前提、制約、情報鮮度、不確実性、機密区分を渡す | 第4章 | 全社員、業務担当者 |
| Task Brief | 個別タスクの入力、出力、受け入れ条件、停止条件を定義する | 第5章 | 業務担当者、管理職 |
| Task Breakdown | 複雑な業務を複数の委任可能タスクへ分解する | 第5章 | 業務担当者、管理職 |
| Checkpoint Plan | AIが次へ進む前に人間が確認する地点を定義する | 第5章 | 業務担当者、管理職 |
| Stop / Escalation Rules | AIが停止する条件と、誰に渡すかを定義する | 第5章 | 業務担当者、管理職、AI推進担当 |
| Restart Packet | 中断後に別セッション・別担当者が作業を再開できる状態を残す | 第5章 | 業務担当者、管理職 |
| AI出力レビュー表 | AI出力を成果物として採用できるか判定する | 第6章 | 全社員、管理職 |
| Review Issue Log | レビューで見つけた問題をSeverity付きで記録し、改善先へ接続する | 第6章 | 全社員、管理職、AI推進担当 |
| Evaluation Plan | AI活用の仕組みとしての品質、回帰評価、禁止出力を評価する | 第6章 | エンジニア、AI推進担当 |
| ツール権限マトリクス | AIがどのツールでどの操作をどの条件で実行できるかを制御する | 第7章 | エンジニア、情シス、AI推進担当 |
| Tool Spec Card | AIが誤用しにくいツール仕様を定義する | 第7章 | エンジニア、AI推進担当 |
| HITL承認フロー | 人間承認を業務に組み込む | 第7章 | 管理職、AI推進担当 |
| Tool Approval Request | AIのツール実行前に承認者へ提示する承認パケットを作る | 第7章 | 管理職、承認者、AI推進担当 |
| 禁止操作リスト | AIに実行させない操作を明文化する | 第7章 | 管理職、情シス、セキュリティ |
| Permission Test | 権限設計が実際に機能するかをテストする | 第7章 | エンジニア、AI推進担当、セキュリティ |
| Agent Run Log | AIエージェントの1回の業務実行を、依頼、前提、出力、レビュー、承認、改善までRun単位で記録する | 第8章 | エンジニア、AI推進担当、管理職 |
| Trace Event Record | モデル呼び出し、検索、ツール実行、承認、エラーなどのイベントを追跡する | 第8章 | エンジニア、AI推進担当 |
| Tool Execution Log | AIが呼び出したツールの操作、スコープ、権限、承認、実行結果を記録する | 第8章 | エンジニア、情シス、AI推進担当 |
| Approval Log | HITL承認の判断内容、承認者、条件、実行内容との差分を記録する | 第8章 | 管理職、AI推進担当、監査担当 |
| Run Review Report | 複数Runを定期的に振り返り、傾向と改善アクションを整理する | 第8章 | 管理職、AI推進担当 |
| Improvement Backlog | ログ、レビュー、評価、インシデントから生じた改善項目を管理する | 第8章 | AI推進担当、管理職、エンジニア |
| Observability Design Sheet | AIエージェント導入前に、ログ、トレース、保持期間、アクセス権、Run Reviewを設計する | 第8章 | エンジニア、AI推進担当、情シス |
| Metrics Dashboard Definition | 利用、品質、リスク、効率、学習の指標を定義する | 第8章 | 管理職、AI推進担当 |
| AI Security Checklist | AI固有リスクを確認する | 第9章 | 全社員、セキュリティ |
| Data Classification and Handling Matrix | AI入力、Context Pack、RAG、ログ、評価データへの情報利用可否を決める | 第9章 | 全社員、情シス、セキュリティ |
| Untrusted Input Handling Rule | 外部文書、メール、PDF、Web、RAG文書を命令ではなくデータとして扱うルールを定義する | 第9章 | 全社員、AI推進担当 |
| Prompt Injection Test Sheet | 外部入力内の悪意ある命令にAIが従わないことをテストする | 第9章 | エンジニア、AI推進担当、セキュリティ |
| AI Privacy Impact Review | 個人情報、顧客情報、従業員情報を扱うAI利用のプライバシー影響を確認する | 第9章 | 管理職、法務、セキュリティ |
| External Tool / MCP Review Sheet | 外部ツール、MCP、プラグイン、SaaS連携のリスクを審査する | 第9章 | エンジニア、情シス、セキュリティ |
| Security Exception Record | 通常ルールからの例外を期限付きで記録する | 第9章 | 管理職、セキュリティ、AI推進担当 |
| AI Incident Trigger Matrix | AI利用を停止・エスカレーションする条件を定義する | 第9章 | セキュリティ、AI推進担当、管理職 |
| AI Use Policy | 社内AI利用の許可、条件付き許可、要承認、禁止、インシデント時連絡先を定義する | 第10章 | 経営層、AI推進担当、全社員 |
| AI Use Case Intake | 新しいAI利用を始める前に、目的、データ、外部送信、ツール連携、顧客影響を整理する | 第10章 | 全社員、管理職、AI推進担当 |
| AI System Inventory | 社内AI利用をユースケース単位で台帳化し、Owner、データ、権限、リスク、統制、廃止条件を管理する | 第10章 | AI CoE、情シス、管理職 |
| Governance Level Matrix | AI利用をG0〜G5などの統制レベルに分類する | 第10章 | AI推進担当、管理職、セキュリティ |
| AI Risk Register | AI利用に関するリスク、統制、残リスク、Owner、期限を管理する | 第10章 | AI推進担当、Risk Owner |
| Approval Workflow | Use Case Approval、Tool Action Approval、Risk Acceptance、Exceptionの承認経路を定義する | 第10章 | 管理職、AI推進担当、承認者 |
| AI System ADR | AI利用の重要な設計判断、代替案、残リスク、停止条件を記録する | 第10章 | エンジニア、AI推進担当、管理職 |
| AI Vendor Review Record | 外部AI、SaaS、MCP、ベンダーのデータ保持、認証、監査ログ、契約条件を審査する | 第10章 | 情シス、法務、セキュリティ |
| AI Training Register | ロール別のAIリテラシー、確認テスト、実技課題、再受講期限を管理する | 第10章 | AI推進担当、管理職、人事 |
| AI Incident Runbook | AI起因インシデント時の検知、停止、保全、通知、復旧、再発防止を定義する | 第10章 | セキュリティ、AI推進担当、管理職 |
| AI Audit Evidence Pack | 台帳、リスク、承認、評価、ログ、教育、ベンダー審査、インシデント対応証跡を束ねる | 第10章 | 監査担当、AI推進担当 |
| AI Retirement Plan | AI利用、プロンプト、RAG、API、ツール権限、ログ、ベンダー契約を安全に廃止する | 第10章 | AI推進担当、情シス、管理職 |
| Decision Brief | 判断対象、判断者、判断基準、選択肢、判断理由、検証指標を1枚で整理する | 第11章 | 管理職、経営層、AI推進担当 |
| Decision Criteria Matrix | 判断基準、重み、最低条件を明示し、AI分析の前提にする | 第11章 | 管理職、経営層、AI推進担当 |
| Option Evaluation Table | 複数選択肢を同じ判断基準で比較する | 第11章 | 管理職、業務責任者、AI推進担当 |
| Kill Decision Sheet | 施策、プロンプト、RAG、エージェント、ワークフローを続けるか、縮小するか、やめるか判断する | 第11章 | 管理職、AI推進担当 |
| Risk Acceptance Memo | 残リスクを受容する場合に、期限、Owner、監視指標、再評価条件を記録する | 第11章 | 管理職、Risk Owner、AI推進担当 |
| Decision Review Log | 判断後に、結果だけでなく判断プロセスを振り返り、改善へ接続する | 第11章 | 管理職、AI推進担当 |
| 判断前チェックリスト | AI提案の採否を人間が判断する | 第11章 | 管理職、経営層 |
| Connection Debt診断 | 対立回避による負債を可視化する | 第12章 | 管理職、リーダー |
| Conflict Type Map | 対立を、事実、優先順位、範囲、責任、品質、リスク、価値観、行動、関係、権限に分類する | 第12章 | 管理職、リーダー、AI推進担当 |
| Difficult Conversation Brief | 困難な会話の目的、扱う論点、業務影響、要望、相手への質問を整理する | 第12章 | 管理職、リーダー |
| Perspective Map | 相手の合理性、制約、恐れている失敗、共通目的を整理する | 第12章 | 管理職、リーダー、業務担当者 |
| Conversation Plan | 会話の順序、決めること、決めないこと、合意候補を設計する | 第12章 | 管理職、リーダー |
| Agreement Log | 会話後の合意、未合意、Owner、期限、更新すべき成果物を記録する | 第12章 | 管理職、リーダー、業務担当者 |
| Follow-up Contract | 会話後のアクション、成功条件、確認方法、再会話条件を定義する | 第12章 | 管理職、リーダー |
| Backchannel Control Rule | 本人に話すべき論点を本人以外にだけ話し続けないためのルールを定義する | 第12章 | 管理職、リーダー |
| 20 Experiments Sheet | 大きなAI活用目標を複数の小実験へ分解し、最初の案への執着を避ける | 第13章 | 全社員、企画、開発、AI推進担当 |
| Experiment Portfolio | 効率化、品質、学習、統制、廃棄の実験バランスを管理する | 第13章 | 管理職、AI推進担当 |
| Pace / Spin Review | 実験速度と空回りを診断し、摩擦と安全策を調整する | 第13章 | 管理職、リーダー、AI推進担当 |
| Learning Log | 実験から得た学習を再利用可能な条件、避けるべき条件、次の仮説として残す | 第13章 | チーム、AI推進担当 |
| Experiment Kill Criteria | 実験を続ける、変える、停止する、廃棄する、展開禁止にする条件を定義する | 第13章 | 管理職、AI推進担当 |
| Side Quest Charter | 低リスク・短期間・限定範囲の探索実験の入口と出口を定義する | 第13章 | 全社員、管理職、AI推進担当 |
| AI実験設計シート | 仮説、最小実験、実験レベル、成功条件、失敗条件、停止条件、やめる条件を定義する | 第13章 | 全社員、企画、開発、AI推進担当 |
| Failure Review Sheet | 失敗を責任追及ではなく、仮説、Context、Request、Tool、Review、Governance、Humanの改善へ変換する | 第13章 | チーム、管理職、AI推進担当 |
| Action Blocker診断 | 行動停止を、実リスク、想像上のリスク、安全策、最小行動へ分解する | 第14章 | 個人、管理職 |
| Self-talk Transcript | 行動前後のセルフトークを書き出し、前提、反証、行動を止めない言い換えを整理する | 第14章 | 個人、管理職 |
| Review vs Self-criticismチェック | レビュー指摘を成果物、プロセス、判断、リスク、人格評価に分け、自己批判を切り離す | 第14章 | 全社員、管理職 |
| Minimum Action Contract | 24時間以内または次の業務日までに実行する最小行動を契約化する | 第14章 | 全社員、管理職 |
| Support Request | レビュー、壁打ち、判断補助、リスク確認を依頼するための相談パケットを作る | 第14章 | 全社員、管理職 |
| Energy / Attention Budget | 高レバレッジ環境で注意資源を使いすぎないよう、見るレビュー、見ないレビュー、止める作業を決める | 第14章 | 個人、管理職 |
| Manager Coaching Note | 管理職が行動停止を人格問題ではなく業務設計問題として扱う | 第14章 | 管理職 |
| Skill Map | AIエージェント協働能力を12領域、Lv1〜Lv6、証拠レベルで整理する | 第15章 | 管理職、AI推進担当、経営層 |
| Role Skill Profile | ロール別に必要能力、目標レベル、必須成果物、実技課題、再評価周期を定義する | 第15章 | 管理職、AI推進担当 |
| Skill Diagnosis Form | 自己診断、扱う情報、AI利用希望、不安、提出済み成果物を収集する | 第15章 | 全社員、管理職、AI推進担当 |
| Practical Assessment Pack | ロール別・レベル別の実技課題、合格基準、不合格例を定義する | 第15章 | AI推進担当、評価者 |
| Evidence Portfolio | 評価対象者の成果物、証拠レベル、強み、不足、推奨学習を束ねる | 第15章 | 管理職、AI推進担当、評価者 |
| Learning Gap Handoff | 評価で見つかった不足領域、業務リスク、再評価成果物を第16章の展開設計へ引き渡す | 第15章 | 管理職、AI推進担当 |
| Certification Decision Record | 認定結果、許可されるAI利用範囲、再提出条件、再評価日を記録する | 第15章 | AI推進担当、管理職、評価者 |
| Evaluator Calibration Record | 評価者間の判定差分を記録し、模範解答、NG例、採点基準を更新する | 第15章 | AI推進担当、評価者 |
| スキル評価ルーブリック | 能力領域ごとのLv1〜Lv6判定基準を定義する | 第15章 | 管理職、AI推進担当、評価者 |
| Rollout Charter | AIエージェント協働の展開目的、対象、成功条件、停止条件、意思決定を定義する | 第16章 | 経営層、AI推進担当 |
| AI Enablement Operating Model | AI CoE、部門Owner、管理職、Champion、Security、HR、Platformの役割とRACIを定義する | 第16章 | 経営層、AI推進担当、管理職 |
| Role-based Learning Path | ロール別に学ぶ章、教材、実技課題、成果物、認定、権限付与を定義する | 第16章 | AI推進担当、HR、管理職 |
| Curriculum Blueprint | 教材ごとの学習目標、構成、評価、更新方針を定義する | 第16章 | AI推進担当、HR |
| Workshop Design Sheet | ワークショップの時間割、演習、使用テンプレート、提出物を設計する | 第16章 | AI推進担当、ファシリテーター |
| Training Content Inventory | 教材のOwner、状態、更新日、関連ポリシー、関連テンプレートを管理する | 第16章 | AI推進担当、HR |
| AI Enablement Portal Map | 教材、テンプレート、FAQ、ユースケース、認定、ガバナンス、KPIの社内導線を設計する | 第16章 | AI推進担当、情シス |
| Office Hour Runbook | 現場相談を受付、分類し、FAQ、教材、ポリシー、改善バックログへ接続する | 第16章 | AI推進担当、AI Champion |
| Use Case Portfolio Board | AI活用案をIdea、Experiment、Production、Retireなどのステージで管理する | 第16章 | AI推進担当、管理職 |
| AI Enablement KPI Dashboard | Adoption、Skill、Productivity、Quality、Risk、Governance、Experiment、Cost、Human / Orgを測定する | 第16章 | 経営層、AI推進担当 |
| 90-Day Rollout Plan | 設計、教材作成、パイロット、評価、展開判断を90日で進める計画を作る | 第16章 | AI推進担当、管理職 |
| Change Communication Plan | 対象者別に、AI展開の目的、誤解、チャネル、反応確認方法を定義する | 第16章 | AI推進担当、HR、管理職 |
| Community of Practice Charter | AI Championや実践者のコミュニティの目的、活動、失敗共有ルールを定義する | 第16章 | AI推進担当、AI Champion |
| Quarterly Review Report | KPI、ユースケース、インシデント、学習、次四半期計画をレビューする | 第16章 | 経営層、AI推進担当 |
| Enablement Retrospective | 組織展開そのものを振り返り、やめる教材、変える運用、次の改善を決める | 第16章 | AI推進担当、管理職 |

## 成果物の依存関係

```mermaid
flowchart TB
    R0[本書活用計画] --> Z[AIエージェント協働ブループリント] --> A[AI適用判断シート] --> B[AIエージェント依頼書 / Request Contract]
    B --> B2[Acceptance Criteria]
    B --> C[Context Pack]
    B2 --> E[AI出力レビュー表]
    C --> D0[Task Breakdown]
    D0 --> D[Task Brief]
    D0 --> D1[Checkpoint Plan]
    D0 --> D2[Stop / Escalation Rules]
    D --> D3[Restart Packet]
    D --> E[AI出力レビュー表]
    D1 --> E
    E --> E1[Review Issue Log]
    E1 --> E2[Evaluation Plan]
    E2 --> F[Agent Run Log]
    D2 --> G[ツール権限マトリクス]
    D --> G
    G --> G1[Tool Spec Card]
    G --> G2[禁止操作リスト]
    G1 --> H[HITL承認フロー]
    G2 --> H
    H --> H1[Tool Approval Request]
    H1 --> H2[Permission Test]
    H2 --> F[Agent Run Log]
    F --> F1[Trace Event Record]
    F --> F2[Tool Execution Log]
    F --> F3[Approval Log]
    F1 --> F4[Run Review Report]
    F2 --> F4
    F3 --> F4
    F4 --> I[Improvement Backlog]
    F --> S0[AI Security Checklist]
    G --> S0
    S0 --> S1[Data Classification and Handling Matrix]
    S0 --> S2[Prompt Injection Test Sheet]
    S0 --> S3[External Tool / MCP Review Sheet]
    S0 --> S4[AI Incident Trigger Matrix]
    S0 --> X[AI System Inventory]
    X --> GV0[AI Use Policy]
    X --> GV1[Governance Level Matrix]
    GV1 --> GV2[AI Risk Register]
    GV2 --> GV3[Approval Workflow]
    GV3 --> GV4[AI System ADR]
    GV4 --> GV5[AI Audit Evidence Pack]
    GV5 --> GV6[AI Retirement Plan]
    GV2 --> GV7[AI Incident Runbook]
    GV3 --> GV8[AI Vendor Review Record]
    GV3 --> GV9[AI Training Register]
    I --> E2[Evaluation Plan]
    I --> J[AI実験設計シート]
    E --> L0[Decision Brief]
    L0 --> L[判断前チェックリスト]
    L0 --> L1[Decision Criteria Matrix]
    L1 --> L2[Option Evaluation Table]
    L --> L3[Kill Decision Sheet]
    L --> L4[Risk Acceptance Memo]
    L --> M[やめる判断 / 続ける判断]
    M --> L5[Decision Review Log]
    L5 --> I[Improvement Backlog]
    L0 --> C0[Connection Debt診断]
    C0 --> C1[Conflict Type Map]
    C1 --> C2[Difficult Conversation Brief]
    C2 --> C3[Perspective Map]
    C2 --> C4[Conversation Plan]
    C4 --> C5[Agreement Log]
    C5 --> C6[Follow-up Contract]
    C5 --> I[Improvement Backlog]
    C5 --> J[AI実験設計シート]
    J --> J1[20 Experiments Sheet]
    J --> J2[Experiment Portfolio]
    J --> J3[Pace / Spin Review]
    J --> J4[Experiment Kill Criteria]
    J --> J5[Side Quest Charter]
    J --> K[Failure Review Sheet]
    K --> K1[Learning Log]
    K1 --> I[Improvement Backlog]
    K1 --> E2[Evaluation Plan]
    K1 --> GV6[AI Retirement Plan]
    J3 --> AB[Action Blocker診断]
    C0 --> AB
    L5 --> AB
    AB --> AB1[Self-talk Transcript]
    AB --> AB2[Review vs Self-criticismチェック]
    AB --> AB3[Minimum Action Contract]
    AB3 --> SR[Support Request]
    AB3 --> I[Improvement Backlog]
    AB3 --> K1[Learning Log]
    GV9 --> SM[Skill Map]
    K1 --> SM
    AB3 --> SM
    SM --> RSP[Role Skill Profile]
    RSP --> SDF[Skill Diagnosis Form]
    RSP --> PAP[Practical Assessment Pack]
    PAP --> EP[Evidence Portfolio]
    SDF --> EP
    EP --> LGH[Learning Gap Handoff]
    LGH --> CDR[Certification Decision Record]
    CDR --> GV9[AI Training Register]
    SM --> RC[Rollout Charter]
    RC --> OM[AI Enablement Operating Model]
    OM --> RLP[Role-based Learning Path]
    RLP --> CB[Curriculum Blueprint]
    CB --> WDS[Workshop Design Sheet]
    CB --> TCI[Training Content Inventory]
    TCI --> PORTAL[AI Enablement Portal Map]
    PORTAL --> OH[Office Hour Runbook]
    OH --> UCP[Use Case Portfolio Board]
    UCP --> KPID[AI Enablement KPI Dashboard]
    KPID --> PLAN[90-Day Rollout Plan]
    PLAN --> QRR[Quarterly Review Report]
    QRR --> ER[Enablement Retrospective]
    ER --> I[Improvement Backlog]
```

## 執筆上の注意

本文で新しい概念を出したら、原則として次のどれかへ落とす。

- テンプレート項目
- チェックリスト項目
- 演習問題
- ルーブリック評価基準
- ガバナンス運用項目

落とし先がない概念は、読者の行動につながらない可能性が高い。
