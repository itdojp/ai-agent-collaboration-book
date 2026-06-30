# Figure Index: 図表計画

出版時には、章ごとに最低1つの図表を置く。図表は読者が記憶し、研修資料へ転用できるものに限定する。

各図表ページでは、公開サイトで最初にSVG画像を表示し、編集用のMermaidソースは折りたたみ表示にする。SVGは `scripts/build_figures.py` で再生成する。

## 図表IDから探す

図表IDだけを手がかりに、用途と関連章を確認できる早見表である。詳細なファイル名やSVGリンクは、後続の「優先図表」「追加図表」で確認する。

| ID | 用途 | 関連章・ページ |
|---|---|---|
| F-00 | AIエージェント協働の基本循環を説明する | 第1章 / Concept Map |
| F-01 | 6層モデルの全体像を示す | 第0章 / 第1章 |
| F-02 | Request Contract、Context Pack、Task Briefの接続を示す | 第3〜5章 |
| F-03 | レビュー、権限、ログ、ガバナンスへ進むControl層を示す | 第6〜10章 |
| F-04 | 判断、対話、実験、スキル、組織展開のHuman / Org層を示す | 第11〜16章 |
| F-05 | レベル接頭辞の読み替えを支援する | 第15章 / 付録E |
| F-06 | 90日展開の順序と判断点を示す | 第16章 |
| F-07 | ツール権限を段階的に設計する | 第7章 |
| F-08 | Agent Run Logの記録対象を追う | 第8章 |
| F-09 | AIセキュリティリスクの論点を俯瞰する | 第9章 |
| F-10 | ガバナンス運用の反復サイクルを示す | 第10章 |
| F-11 | AI提案と人間判断の責任境界を示す | 第11章 |
| F-12 | Connection Debtが蓄積する構造を示す | 第12章 |
| F-13 | 実験と学習の反復ループを示す | 第13章 |
| F-14 | 行動停止を分解して最小行動へつなぐ | 第14章 |
| F-15 | スキルレベルと証拠を対応づける | 第15章 |

## 優先図表

| ID | 図表名 | ファイル | SVG | 配置 | 状態 |
|---|---|---|---|---|---|
| F-00 | AIエージェント協働ループ | [figures/f-00-ai-agent-collaboration-loop.md](figures/f-00-ai-agent-collaboration-loop.md) | [SVG](figures/assets/f-00-ai-agent-collaboration-loop.svg) | concept-map.md / 第1章 | 追加済み |
| F-01 | 6層モデル | [figures/f-01-six-layer-model.md](figures/f-01-six-layer-model.md) | [SVG](figures/assets/f-01-six-layer-model.svg) | 第0章 / 第1章 | 追加済み |
| F-02 | Request Contract / Context Pack / Task Brief の関係 | [figures/f-02-request-context-task-brief.md](figures/f-02-request-context-task-brief.md) | [SVG](figures/assets/f-02-request-context-task-brief.svg) | 第3〜5章 | 追加済み |
| F-03 | Control層の流れ | [figures/f-03-control-layer-flow.md](figures/f-03-control-layer-flow.md) | [SVG](figures/assets/f-03-control-layer-flow.svg) | 第6〜10章 | 追加済み |
| F-04 | Human / Org層の流れ | [figures/f-04-human-org-layer-flow.md](figures/f-04-human-org-layer-flow.md) | [SVG](figures/assets/f-04-human-org-layer-flow.svg) | 第11〜16章 | 追加済み |
| F-05 | レベル接頭辞一覧 | [figures/f-05-level-prefixes.md](figures/f-05-level-prefixes.md) | [SVG](figures/assets/f-05-level-prefixes.svg) | 付録E / 第15章 | 追加済み |
| F-06 | 90日展開ロードマップ | [figures/f-06-90-day-rollout-roadmap.md](figures/f-06-90-day-rollout-roadmap.md) | [SVG](figures/assets/f-06-90-day-rollout-roadmap.svg) | 第16章 | 追加済み |

## 追加図表

| ID | 図表名 | ファイル | SVG | 配置 | 状態 |
|---|---|---|---|---|---|
| F-07 | 権限レベル梯子 | [figures/f-07-permission-ladder.md](figures/f-07-permission-ladder.md) | [SVG](figures/assets/f-07-permission-ladder.svg) | 第7章 | 追加済み |
| F-08 | Agent Run Logの流れ | [figures/f-08-agent-run-log-flow.md](figures/f-08-agent-run-log-flow.md) | [SVG](figures/assets/f-08-agent-run-log-flow.svg) | 第8章 | 追加済み |
| F-09 | AIセキュリティリスクマップ | [figures/f-09-ai-security-risk-map.md](figures/f-09-ai-security-risk-map.md) | [SVG](figures/assets/f-09-ai-security-risk-map.svg) | 第9章 | 追加済み |
| F-10 | AIガバナンス運用サイクル | [figures/f-10-ai-governance-cycle.md](figures/f-10-ai-governance-cycle.md) | [SVG](figures/assets/f-10-ai-governance-cycle.svg) | 第10章 | 追加済み |
| F-11 | 判断責任分界 | [figures/f-11-decision-responsibility-boundary.md](figures/f-11-decision-responsibility-boundary.md) | [SVG](figures/assets/f-11-decision-responsibility-boundary.svg) | 第11章 | 追加済み |
| F-12 | Connection Debtの蓄積構造 | [figures/f-12-connection-debt-structure.md](figures/f-12-connection-debt-structure.md) | [SVG](figures/assets/f-12-connection-debt-structure.svg) | 第12章 | 追加済み |
| F-13 | 実験学習ループ | [figures/f-13-experiment-learning-loop.md](figures/f-13-experiment-learning-loop.md) | [SVG](figures/assets/f-13-experiment-learning-loop.svg) | 第13章 | 追加済み |
| F-14 | Action Blocker構造 | [figures/f-14-action-blocker-structure.md](figures/f-14-action-blocker-structure.md) | [SVG](figures/assets/f-14-action-blocker-structure.svg) | 第14章 | 追加済み |
| F-15 | スキルレベルマップ | [figures/f-15-skill-level-map.md](figures/f-15-skill-level-map.md) | [SVG](figures/assets/f-15-skill-level-map.svg) | 第15章 | 追加済み |

## 図表作成ルール

- 1図1メッセージにする。
- 図表だけを見ても、何をすればよいか分かるようにする。
- UIや特定製品のスクリーンショットには依存しない。
- 変化しやすい製品仕様を図にしない。
- 社内研修スライドへ転用できる単純さにする。
