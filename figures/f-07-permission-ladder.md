# F-07: 権限レベル梯子

![F-07: 権限レベル梯子](assets/f-07-permission-ladder.svg)

<details markdown="1">
<summary>Mermaidソース</summary>

```mermaid
flowchart TB
    P0[P0: no-access<br/>アクセス不可]
    P1[P1: read-only<br/>参照のみ]
    P2[P2: draft-only<br/>下書きのみ]
    P3[P3: proposal-only<br/>変更案のみ]
    P4[P4: approval-required<br/>承認後に実行]
    P5[P5: limited-write<br/>限定書き込み]
    P6[P6: write<br/>広範な書き込み]
    P7[P7: admin<br/>管理者操作]

    P0 --> P1 --> P2 --> P3 --> P4 --> P5 --> P6 --> P7

    H[HITL必須領域] -.-> P4
    H -.-> P5
    H -.-> P6
    H -.-> P7
```

</details>

権限は「ツール単位」ではなく「操作単位」で設計する。原則として、外部影響、データ更新、顧客影響、本番影響、不可逆操作がある場合は `P4: approval-required` 以上として扱う。

| レベル | AIができること | 代表例 | 基本制御 |
|---|---|---|---|
| P0 | アクセスしない | 本番DB、秘匿契約、給与情報 | 接続禁止 |
| P1 | 参照のみ | 社内FAQ検索、監視ログ参照 | read-only、ログ記録 |
| P2 | 下書きのみ | 顧客返信案、議事録案 | 人間レビュー |
| P3 | 変更案のみ | PR案、設定変更案 | 差分表示、レビュー |
| P4 | 承認後に実行 | チケット作成、CRM更新 | HITL承認 |
| P5 | 限定書き込み | 特定ラベル付与、限定Wiki更新 | スコープ制限、ロールバック |
| P6 | 広範な書き込み | 複数システム更新 | 強い承認、監査 |
| P7 | 管理者操作 | 権限変更、削除、課金変更 | 原則禁止または例外承認 |

第7章では、この梯子を使ってツール権限マトリクス、HITL承認フロー、Permission Testを設計する。
