---
title: "付録F: ワークショップ設計"
source_path: "appendices/f-workshop-design.md"
order: 340
book_section: "appendices"
---
# 付録F: ワークショップ設計

書籍を社内研修へ展開するためのワークショップ設計例である。第16章の教材体系と整合し、単なる講義ではなく、成果物を作る設計にする。

## F.1 設計原則

1. 研修の成果を「理解」ではなく「提出物」で測る。
2. 低リスク利用と高リスク利用を分ける。
3. テンプレート、チェックリスト、レビュー、Office Hourへ接続する。
4. 管理職には、レビュー、承認、判断、対立処理、実験文化を必ず含める。
5. エンジニアには、ツール、権限、ログ、評価、セキュリティを必ず含める。

## F.2 2時間版: 全社員向けAIエージェント協働入門

| 時間 | 内容 | 使用章 | 成果物 |
|---:|---|---:|---|
| 0:00-0:15 | AIエージェント協働の基本 | 0,1 | 概念理解 |
| 0:15-0:35 | AIに任せる仕事、任せない仕事 | 2 | AI適用判断シート |
| 0:35-1:00 | Request Contract作成 | 3 | AIエージェント依頼書 |
| 1:00-1:25 | Context Pack作成 | 4 | Context Pack |
| 1:25-1:50 | AI出力レビュー | 6 | AI出力レビュー表 |
| 1:50-2:00 | 次回アクション | 8,13 | Improvement Backlog |

合格条件:

- 入力禁止情報を判別できる。
- Request Contractに目的、出力形式、制約がある。
- Context Packに鮮度と要確認事項がある。
- AI出力をそのまま採用しない。

## F.3 3時間版: 6層Quick Start

| 時間 | 6層 | 内容 | 成果物 |
|---:|---|---|---|
| 0:00-0:20 | Work | 対象業務選定 | AI適用判断シート |
| 0:20-0:45 | Request | 依頼仕様化 | Request Contract |
| 0:45-1:10 | Context | 前提整理 | Context Pack |
| 1:10-1:35 | Delegation | タスク分解 | Task Brief / Stop Rules |
| 1:35-2:05 | Control | レビュー・権限・ログ | レビュー表 / HITL / Run Log |
| 2:05-2:30 | Security | 情報分類・外部入力 | AI Security Checklist |
| 2:30-2:50 | Human / Org | 判断・実験化 | Decision Brief / AI実験設計シート |
| 2:50-3:00 | Improvement | 改善登録 | Improvement Backlog |

## F.4 半日版: 業務担当者向け実務適用

| 時間 | 内容 | 成果物 |
|---:|---|---|
| 0:00-0:30 | 業務棚卸し | 業務候補リスト |
| 0:30-1:15 | AI適用判断 | ROI / リスク分類 |
| 1:15-2:00 | Request Contract / Context Pack | 依頼書、Context Pack |
| 2:00-2:45 | Task Brief | サブタスク表 |
| 2:45-3:30 | レビュー演習 | レビュー表、Review Issue Log |
| 3:30-4:00 | 小実験設計 | AI実験設計シート、Kill Criteria |

## F.5 管理職向け: チーム運用設計

| 時間 | 内容 | 成果物 |
|---:|---|---|
| 0:00-0:30 | チームのAI利用状況棚卸し | Use Case Portfolio |
| 0:30-1:15 | レビュー基準設計 | チームレビュー表 |
| 1:15-2:00 | 権限・承認設計 | HITLフロー、承認条件 |
| 2:00-2:45 | 判断・対立処理 | Decision Brief、Connection Debt診断 |
| 2:45-3:30 | 実験文化設計 | Experiment Portfolio、Failure Review運用 |
| 3:30-4:00 | 90日計画 | 部門展開計画 |

## F.6 エンジニア向け: AgentOps基礎

| 時間 | 内容 | 成果物 |
|---:|---|---|
| 0:00-0:30 | エージェント実行系の構成 | アーキテクチャメモ |
| 0:30-1:15 | Tool Spec Card | Tool Spec Card |
| 1:15-2:00 | 権限・HITL・Permission Test | 権限マトリクス、テスト |
| 2:00-2:45 | Run Log / Trace | Agent Run Log、Trace Event Record |
| 2:45-3:30 | Security Checklist | Prompt Injection Test、MCP審査票 |
| 3:30-4:00 | Evaluation Plan | 評価ケース、回帰評価方針 |

## F.7 研修評価

| 観点 | 測定方法 | 証拠 |
|---|---|---|
| 理解 | 確認テスト | EV2 |
| 実践 | 作成テンプレートのレビュー | EV3 |
| 定着 | 30日後のテンプレート利用率 | EV4 |
| 効果 | 作業時間、品質、手戻り、実験数 | EV4 |
| 安全性 | ルール違反、インシデント、承認漏れ | EV4〜EV5 |
| 組織運用 | Office Hour、台帳、KPI、四半期レビュー | EV5 |
