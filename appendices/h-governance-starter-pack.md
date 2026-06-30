# 付録H: ガバナンス・スターターパック

この付録は、社内利用を始める際に最初に作る統制文書の最小セットである。第10章の成果物を軽量化し、90日以内に運用へ載せることを目的にする。

## H.1 AI利用ポリシー1枚紙

```text
目的：
対象者：
利用可能なAIツール：
利用禁止AIツール：
入力してよい情報：
入力してはいけない情報：
AIに任せてよい作業：
AIに任せてはいけない判断：
人間承認が必要な操作：
ログ保存方針：
問い合わせ先：
違反時の対応：
次回改訂日：
```

## H.2 AI利用リスク分類表

| リスク | 例 | 扱い | 必要成果物 |
|---|---|---|---|
| 低 | 要約、下書き、社内メモ整理 | 利用可 | Request Contract、自己レビュー |
| 中 | 顧客向け文面案、社内データ分析 | レビュー必須 | Context Pack、AI出力レビュー表、Run Log |
| 高 | 契約、価格、本番変更、個人情報処理 | 承認必須 | HITL、Security Checklist、AI Risk Register |
| 禁止 | 認証情報投入、無承認外部送信、自動契約判断 | 不可 | 例外不可。必要なら経営・法務・セキュリティ判断 |

## H.3 AI System Inventory最小項目

```text
Inventory ID：
名称：
部門：
Business Owner：
System Owner：
Data Owner：
Risk Owner：
利用目的：
利用者：
入力データ：
出力先：
外部送信有無：
ツール連携：
RAG / メモリ：
リスク分類：G0 / G1 / G2 / G3 / G4 / G5
承認フロー：
ログ保存：
評価方法：
教育要件：
最終レビュー日：
廃止条件：
```

## H.4 承認ゲート

| 操作 | 承認者 | ログ | 関連成果物 |
|---|---|---|---|
| 顧客向けメール送信 | 業務責任者 | 送信前レビュー | HITL Approval Flow、Approval Log |
| 契約・SLAに関する表明 | 法務または責任者 | 承認記録 | Risk Acceptance Memo |
| 本番環境変更 | SRE / 運用責任者 | Change Log | Tool Permission Matrix、AI Incident Runbook |
| CRM更新 | 営業責任者 | 更新履歴 | Tool Spec Card、Approval Log |
| 外部AIツール追加 | 情シス / セキュリティ | ツール審査票 | AI Vendor Review Record |
| 外部MCP追加 | 情シス / セキュリティ / Data Owner | 接続審査ログ | External Tool / MCP Review Sheet |

## H.5 AI Risk Register最小項目

```text
Risk ID：
対象Inventory ID：
リスク内容：
影響：
発生可能性：
既存対策：
追加対策：
残リスク：
Risk Owner：
受容可否：
期限：
再確認日：
```

## H.6 AI Vendor Review最小項目

```text
ベンダー名：
サービス名：
用途：
入力データ：
データ保持：
学習利用：なし / あり / 要確認
保存地域：
監査ログ：あり / なし / 要確認
SSO / MFA：
契約条件確認日：
DPA：あり / なし / 要確認
サブプロセッサ：
インシデント通知：
判定：承認 / 条件付き承認 / 不承認 / 要追加確認
条件：
承認者：
次回レビュー日：
```

## H.7 AI Incident Runbook最小版

```text
検知条件：
重大度分類：Low / Medium / High / Critical
初動担当：
停止対象：AI利用 / ツール連携 / 外部送信 / RAG / APIキー
保全するログ：
影響確認項目：顧客 / 個人情報 / 本番 / 契約 / 金銭 / レピュテーション
通知先：
顧客連絡要否：
法務連携条件：
セキュリティ連携条件：
経営報告条件：
復旧条件：
再発防止：
台帳更新：
教育更新：
事後レビュー日：
```

## H.8 90日スターター運用

| 期間 | 作業 | 成果物 |
|---|---|---|
| 1〜2週 | AI利用棚卸し | AI System Inventory初版 |
| 2〜3週 | AI利用ポリシー公開 | AI Use Policy 1枚紙 |
| 3〜4週 | 高リスク用途の停止・承認 | Risk Register、Approval Workflow |
| 4〜6週 | 全社員向け基礎教育 | Training Register |
| 6〜8週 | 重点部門パイロット | Use Case Portfolio、Run Log |
| 8〜10週 | 失敗事例・改善登録 | Failure Review、Improvement Backlog |
| 10〜12週 | 四半期レビュー | Audit Evidence Pack、Quarterly Review Report |
