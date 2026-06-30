# 第3章・第4章 執筆サマリー

0.4.0-draft

## 対象

- `manuscript/ch03-request-contract.md`
- `manuscript/ch04-context-design.md`
- `appendices/a-templates.md`
- `artifact-index.md`
- `changelog.md`
- `book-config.json`

## 第3章「依頼を契約にする」

第3章は、Request層の中核章として拡張した。単なるプロンプト改善ではなく、AIへの依頼を実務仕様として扱うための章にしている。

主な追加内容は以下。

```text
・Request Contract の定義
・プロンプト、依頼文、Request Contract、Acceptance Criteria、Task Brief の違い
・最小 Request Contract
・依頼モード：Explore / Produce / Review / Transform / Compare / Plan / Execute-assist
・成果物を先に決める設計
・出力形式を後工程から決める考え方
・Acceptance Criteria の作り方
・不明点の扱い：質問、仮定、要確認、複数案、停止
・制約条件と人間確認条件
・Request Contract の粒度
・競合調査、顧客返信案、AI出力レビューの実務ケース
・Request Contract の作成手順とレビュー観点
・典型的な失敗と設計原則
・チェックリスト、演習、演習判定基準、章の受け入れ基準
```

## 第4章「Context Packを設計する」

第4章は、Context層の中核章として拡張した。資料丸投げではなく、AIに渡す前提情報を制御文書として整理する章にしている。

主な追加内容は以下。

```text
・Context Pack の定義
・Request Contract と Context Pack の違い
・コンテキストの種類
・良いコンテキストの条件
・資料丸投げと Context Pack の違い
・情報鮮度ラベル
・確定、推定、仮定、要確認の分離
・情報源の信頼度
・機密区分と情報最小化
・RAG、メモリ、ツール結果、会話履歴との関係
・長い作業におけるコンテキスト管理
・再開用 Context Pack
・Context Pack の作成手順
・競合調査、障害一次対応の実務ケース
・Context Pack の更新とレビュー観点
・典型的な失敗と設計原則
・チェックリスト、演習、演習判定基準、章の受け入れ基準
```

## 付録・索引の更新

`appendices/a-templates.md` では、A.3 と A.4 を本文に合わせて拡張した。

```text
A.3 AIエージェント依頼書 / Request Contract
  - フル版テンプレート
  - 最小版
  - 受け入れ条件テンプレート
  - 競合調査の記入例

A.4 Context Pack
  - フル版テンプレート
  - 情報鮮度ラベル
  - 確度分類
  - 更新履歴テンプレート
```

`artifact-index.md` では、Request Contract と Acceptance Criteria の位置づけを明確化し、AI出力レビュー表への依存関係を追加した。

## 現時点の状態

第1章〜第4章まで、書籍の前半基盤である Work / Request / Context が初稿相当になった。次に執筆する第5章では、Request Contract と Context Pack を前提に、複雑な仕事を Task Brief へ分解し、チェックポイント、停止条件、エスカレーション条件を設計する。
