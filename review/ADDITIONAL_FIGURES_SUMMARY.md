# 追加図表F-07〜F-15反映サマリー

反映版: `0.22.0-revised`  
作成日: 2026-06-27

## 追加した図表

| ID | 図表名 | ファイル | 主な配置 |
|---|---|---|---|
| F-07 | 権限レベル梯子 | `figures/f-07-permission-ladder.md` | 第7章 |
| F-08 | Agent Run Logの流れ | `figures/f-08-agent-run-log-flow.md` | 第8章 |
| F-09 | AIセキュリティリスクマップ | `figures/f-09-ai-security-risk-map.md` | 第9章 |
| F-10 | AIガバナンス運用サイクル | `figures/f-10-ai-governance-cycle.md` | 第10章 |
| F-11 | 判断責任分界 | `figures/f-11-decision-responsibility-boundary.md` | 第11章 |
| F-12 | Connection Debtの蓄積構造 | `figures/f-12-connection-debt-structure.md` | 第12章 |
| F-13 | 実験学習ループ | `figures/f-13-experiment-learning-loop.md` | 第13章 |
| F-14 | Action Blocker構造 | `figures/f-14-action-blocker-structure.md` | 第14章 |
| F-15 | スキルレベルマップ | `figures/f-15-skill-level-map.md` | 第15章 |

## 反映したファイル

- `figure-index.md`: F-07〜F-15を未作成から追加済みに変更。
- `manuscript/ch07-tool-permission-hitl.md`〜`manuscript/ch15-skill-map.md`: 各章へ関連図表リンクを追加。
- `MANIFEST.md`: 追加図表ファイルを追加。
- `README.md`: 現在のドラフト状態と次作業を更新。
- `book-config.json`, `title.md`, `colophon.md`, `changelog.md`: 版を `0.22.0-revised` へ更新。

## 未対応

図表はMarkdown + Mermaid形式で追加した。出版媒体で画像ファイルが必要な場合は、Codex CLIまたはビルドパイプラインでSVG/PNGへレンダリングする。
