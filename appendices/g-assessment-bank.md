# 付録G: 認定・診断問題バンク

この付録は、第15章のスキルマップと評価体系に接続する問題バンクである。問題は、知識確認だけでなく、成果物作成、レビュー、判断、運用証跡まで含める。

## G.1 Lv1: AI Safe User

### 選択式

AIに入力してはいけない可能性が最も高いものはどれか。

A. 公開済み製品ページのURL  
B. 社内で公開済みの一般FAQ  
C. 認証情報、APIキー、秘密鍵  
D. 一般的な文章校正依頼  

正答: C

### 実技

次のAI利用を「許可 / 条件付き許可 / 要承認 / 禁止」に分類する。

```text
1. 公開情報を要約する
2. 顧客名を含む問い合わせメールを外部AIへ貼る
3. 顧客返信案を作り、人間が送信前に確認する
4. AIに本番DB削除SQLを生成・実行させる
```

## G.2 Lv2: Request / Context Designer

### 記述式

次の依頼をRequest Contractへ書き換えよ。

```text
競合調査して。明日の会議で使う。
```

評価観点:

- 目的が明記されているか
- 対象範囲と除外範囲があるか
- 出力形式があるか
- 情報鮮度と出典条件があるか
- 不明点の扱いがあるか
- 人間判断条件があるか

### 実技

与えられた議事録、営業メモ、FAQからContext Packを作成する。不要情報、古い情報、要確認事項を分離する。

## G.3 Lv3: AI Work Designer

### 実技課題

自分の業務から1件選び、以下を提出する。

```text
1. AI適用判断シート
2. Request Contract
3. Context Pack
4. AI出力レビュー表
5. Improvement Backlog項目を3件
```

合格条件:

- 業務目的が明確である。
- 低リスク・中リスク・高リスクが分類されている。
- AI出力をそのまま成果物として扱っていない。

## G.4 Lv4: AI Agent Operator

### 実技課題

顧客問い合わせ対応エージェントの運用設計を作成する。

提出物:

```text
1. Tool Permission Matrix
2. Tool Spec Card
3. HITL Approval Flow
4. Permission Test
5. Agent Run Log
6. AI Security Checklist
7. Prompt Injection Test Sheet
```

不合格例:

- CRM直接更新を承認なしで許可している。
- 顧客送信をAIに自動実行させている。
- ログのマスキング方針がない。

## G.5 Lv5: AI Team Lead

### 実技課題

チームのAI活用を90日で改善する計画を作る。

提出物:

```text
1. Role Skill Profile
2. Use Case Portfolio Board
3. Review Rule
4. Experiment Portfolio
5. Failure Review運用案
6. Connection Debt診断の使い方
7. KPI Dashboard
```

合格条件:

- 時間削減だけでなく、品質、リスク、実験数、失敗共有、廃棄判断をKPIに含めている。
- 管理職がレビュー、承認、判断、対立処理を担う設計になっている。

## G.6 Lv6: AI Governance Owner

### 実技課題

全社向けAIガバナンスの初期設計を作成する。

提出物:

```text
1. AI Use Policy
2. AI System Inventory
3. Governance Level Matrix
4. AI Risk Register
5. AI Vendor Review Record
6. AI Training Register
7. AI Incident Runbook
8. AI Audit Evidence Pack
9. 90-Day Rollout Plan
```

合格条件:

- ユースケース単位で台帳化している。
- 例外承認に期限とOwnerがある。
- 高リスク用途の承認、監査証跡、教育要件が明確である。

## G.7 採点補助

| 評価証拠 | 表記 | 例 |
|---|---|---|
| 自己申告 | EV0〜EV1 | 自己診断、受講記録 |
| 知識確認 | EV2 | 確認テスト、シナリオ問題 |
| 模擬成果物 | EV3 | 演習で作ったRequest Contract、レビュー表 |
| 実務成果物 | EV4 | 実案件でレビュー済みの成果物 |
| 運用証跡 | EV5 | Run Log、Approval Log、改善履歴、四半期レビュー |

原則として、Lv3以上の認定にはEV3以上、Lv4以上にはEV4またはEV5を求める。
