# ProcessAI MVP開発計画（UIフォーカス版）

## 1. MVP scope & 優先順位

### 🎯 MVP目標
**「AIなしでも価値のある業務フロー管理ツール」として機能し、デモ・営業・ユーザーフィードバック収集が可能な状態**

### 📋 機能優先度マトリックス

| 優先度                | 機能                           | 理由                   | 工数見積 |
| --------------------- | ------------------------------ | ---------------------- | -------- |
| **🔴 P0 (必須)**       | 階層的業務フロー一覧           | コア価値・デモ必須     | 3日      |
| **🔴 P0 (必須)**       | PlantUML エディタ & プレビュー | コア価値・差別化要素   | 5日      |
| **🔴 P0 (必須)**       | As-Is/To-Be デュアルビュー     | 最大の差別化機能       | 4日      |
| **🔴 P0 (必須)**       | 業務定義エディタ               | 実用性・営業での説得力 | 3日      |
| **🔴 P0 (必須)**       | LocalStorage データ永続化      | 実用性・デモ継続性     | 2日      |
| **🟡 P1 (重要)**       | 機能マッピング画面             | 将来性アピール         | 4日      |
| **🟡 P1 (重要)**       | バージョン管理UI               | エンタープライズ訴求   | 3日      |
| **🟡 P1 (重要)**       | エクスポート機能 (PDF/Word)    | 実用性・営業ツール     | 2日      |
| **🔵 P2 (あれば良い)** | 横串機能分析(静的)             | 技術力アピール         | 5日      |
| **🔵 P2 (あれば良い)** | ダッシュボード                 | 見た目の完成度         | 3日      |

## 2. 技術スタック（MVP版）

```json
{
  "frontend": {
    "framework": "React 18 + Vite",
    "language": "TypeScript",
    "ui": "Material-UI (MUI) v6",
    "routing": "React Router v6",
    "editor": "Monaco Editor",
    "state": "React Context + useState (Zustand は後回し)",
    "plantuml": "plantuml-encoder + 公開サーバー"
  },
  "mock_data": {
    "storage": "LocalStorage",
    "ai_responses": "静的なサンプルレスポンス",
    "sample_flows": "3-5個のリアルな業務フロー例"
  },
  "deployment": {
    "dev": "Vite dev server",
    "production": "Vercel/Netlify (静的ホスティング)"
  }
}
```

## 3. 開発スケジュール（3週間 = 15営業日）

### 📅 Week 1: 基盤構築
| 日    | タスク                            | 成果物             |
| ----- | --------------------------------- | ------------------ |
| Day 1 | プロジェクト初期化 + MUI設定      | 基本レイアウト     |
| Day 2 | ルーティング + 基本コンポーネント | ページ遷移         |
| Day 3 | LocalStorage + データ構造実装     | データ永続化       |
| Day 4 | PlantUML エディタ統合             | 図の表示・編集     |
| Day 5 | サンプルデータ作成 + テスト       | リアルなデモデータ |

### 📅 Week 2: コア機能実装
| 日     | タスク                          | 成果物         |
| ------ | ------------------------------- | -------------- |
| Day 6  | 業務フロー階層表示              | ツリービュー   |
| Day 7  | As-Is/To-Be デュアルビュー      | 分割表示・比較 |
| Day 8  | 業務定義エディタ                | フォームUI     |
| Day 9  | PlantUML リアルタイムプレビュー | エディタ完成   |
| Day 10 | 機能マッピング基本UI            | テーブル表示   |

### 📅 Week 3: 仕上げ・デモ準備
| 日     | タスク                          | 成果物       |
| ------ | ------------------------------- | ------------ |
| Day 11 | バージョン管理UI                | 履歴表示     |
| Day 12 | エクスポート機能                | PDF/Word出力 |
| Day 13 | UI/UX 仕上げ + レスポンシブ対応 | 完成度向上   |
| Day 14 | デモシナリオ作成 + バグ修正     | デモ準備完了 |
| Day 15 | デプロイ + ドキュメント整備     | 公開可能状態 |

## 4. コンポーネント設計

### 🏗️ アーキテクチャ概要
```
src/
├── components/
│   ├── layout/
│   │   ├── AppLayout.tsx          # MUI AppBar + Drawer
│   │   ├── Sidebar.tsx            # 業務階層ナビゲーション
│   │   └── Breadcrumbs.tsx        # パンくずリスト
│   ├── flow/
│   │   ├── FlowEditor.tsx         # As-Is/To-Be エディタ
│   │   ├── PlantUMLEditor.tsx     # Monaco + PlantUML
│   │   ├── FlowPreview.tsx        # 図のプレビュー
│   │   └── FlowComparison.tsx     # As-Is vs To-Be
│   ├── business/
│   │   ├── BusinessDefinition.tsx # 業務定義フォーム
│   │   ├── StakeholderEditor.tsx  # ステークホルダー管理
│   │   └── BusinessRuleEditor.tsx # 業務ルール編集
│   ├── function/
│   │   ├── FunctionMapping.tsx    # 機能マッピング
│   │   ├── FunctionList.tsx       # 機能一覧
│   │   └── CrossFunctional.tsx    # 横串分析（静的）
│   └── common/
│       ├── LoadingSpinner.tsx     # 共通ローディング
│       ├── ErrorBoundary.tsx      # エラーハンドリング
│       └── ExportButton.tsx       # エクスポート機能
├── pages/
│   ├── Dashboard.tsx              # ダッシュボード
│   ├── FlowDetail.tsx             # フロー詳細
│   ├── FunctionManagement.tsx     # 機能管理
│   └── Settings.tsx               # 設定画面
├── hooks/
│   ├── useFlowData.tsx            # フローデータ管理
│   ├── usePlantUML.tsx            # PlantUML処理
│   └── useLocalStorage.tsx        # ローカルストレージ
├── types/
│   ├── flow.ts                    # フロー関連型定義
│   ├── business.ts                # 業務定義型
│   └── function.ts                # 機能関連型
└── utils/
    ├── plantUMLUtils.ts           # PlantUML ユーティリティ
    ├── exportUtils.ts             # エクスポート処理
    └── mockAI.ts                  # AI レスポンスモック
```

## 5. モックAI機能実装

### 🤖 静的レスポンス例
```typescript
// utils/mockAI.ts
export const mockAIResponses = {
  improveProcess: (asIsCode: string) => {
    // PlantUMLコードを解析し、改善提案を返す
    return {
      suggestions: [
        "手動承認プロセスの自動化を推奨",
        "データ入力の重複を統合できます",
        "リアルタイム通知で待機時間を削減"
      ],
      toBeCode: generateImprovedPlantUML(asIsCode),
      estimatedImprovement: "処理時間40%削減、エラー率60%減少"
    };
  },
  
  generateBusinessDefinition: (flowTitle: string) => {
    return {
      purpose: `${flowTitle}の効率化と品質向上`,
      scope: "部門内での標準的な業務プロセス",
      stakeholders: [
        { name: "業務担当者", role: "実行者" },
        { name: "管理者", role: "承認者" }
      ]
    };
  },
  
  extractFunctions: (plantUMLCode: string) => {
    // PlantUMLから機能を抽出
    const activities = extractActivitiesFromPlantUML(plantUMLCode);
    return activities.map(activity => ({
      name: activity,
      type: "api",
      description: `${activity}の実装機能`,
      estimatedHours: Math.floor(Math.random() * 20) + 5
    }));
  }
};
```

## 6. デモシナリオ設計

### 🎬 営業デモフロー（10分間）
1. **業務フロー作成** (2分)
   - 「受注処理」を音声で説明 → As-Is自動生成
   - PlantUMLエディタでリアルタイム編集

2. **AI改善提案** (3分)
   - 改善ボタンクリック → To-Be自動生成
   - As-Is/To-Be比較表示
   - 定量的効果の表示

3. **詳細設計連携** (3分)
   - 機能マッピング画面
   - 実装工数の自動算出
   - 横串機能分析

4. **ドキュメント出力** (2分)
   - ワンクリックでPDF出力
   - 業務マニュアル自動生成

### 🎯 想定デモ相手
- **経営層:** ROI重視 → 効果測定画面を重点的に
- **IT部門:** 技術力重視 → PlantUML、詳細設計を中心に  
- **現場担当者:** 使いやすさ重視 → 直感的なUI操作を強調
- **コンサル:** 提案力向上 → 分析機能、レポート生成を訴求

## 7. 成功指標・評価基準

### 📊 MVP成功指標
- **機能完成度:** P0機能100%、P1機能80%以上
- **パフォーマンス:** PlantUML描画3秒以内
- **UI/UX:** SUS (System Usability Scale) スコア70以上
- **デモ効果:** 見込み客の80%が「導入検討したい」と回答

### 🔍 検証項目
- [ ] 5分以内で新規業務フローを作成できる
- [ ] As-Is → To-Be変換がスムーズに行える
- [ ] 非技術者でもPlantUMLエディタを使える
- [ ] モバイルデバイスでも基本操作が可能
- [ ] エクスポートしたドキュメントが実用レベル

## 8. リスク管理

### ⚠️ 技術リスク
| リスク                 | 影響度 | 対策                          |
| ---------------------- | ------ | ----------------------------- |
| PlantUMLサーバー不安定 | 高     | ローカルサーバー + CDN併用    |
| Monaco Editorの重さ    | 中     | 遅延ロード + 軽量エディタ併用 |
| ブラウザ互換性         | 中     | 主要ブラウザでの事前テスト    |

### 📅 スケジュールリスク
- **バッファ:** 各週末に1日のバッファを設定
- **早期検証:** Week1終了時点でコア機能の動作確認
- **代替案:** 間に合わない機能は静的モックで代替

---

**このMVP計画により、3週間でデモ可能な「ProcessAI」のプロトタイプを構築し、市場反応とユーザーフィードバックを効率的に収集できます。**