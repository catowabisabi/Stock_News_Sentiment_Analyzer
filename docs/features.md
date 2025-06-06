# 功能說明 Features Guide

[English](#english) | [繁體中文](#traditional-chinese)

---

<a name="traditional-chinese"></a>
## 繁體中文

### 核心功能

1. **新聞數據抓取**
   - 支持多個新聞來源（Reuters、Bloomberg、Yahoo Finance等）
   - 自動過濾重複新聞
   - 可配置的時間範圍
   - 支持多語言新聞（英文、中文）
   - 自動更新和緩存機制

2. **情緒分析**
   - 多層次文本分析
     * 標題分析
     * 內容分析
     * 關鍵字提取
   - 自適應權重系統
     * 新聞來源權重
     * 時間衰減權重
     * 文章影響力權重
   - 情緒分類
     * 正面/負面/中性分類
     * 情緒強度評分（-1 到 1）
     * 信心指數

3. **數據視覺化**
   - 即時趨勢圖
     * 情緒走勢
     * 新聞量變化
     * 來源分布
   - 互動式圖表
     * 可縮放時間軸
     * 自定義指標
     * 多股票對比
   - 報告生成
     * PDF報告
     * CSV數據導出
     * 郵件通知

4. **警報系統**
   - 自定義觸發條件
     * 情緒閾值
     * 新聞量突變
     * 特定關鍵字
   - 多種通知方式
     * 電子郵件
     * Webhook
     * API推送
   - 警報管理
     * 優先級設置
     * 靜默期設置
     * 歷史記錄

5. **API整合**
   - RESTful API
     * 數據查詢
     * 分析觸發
     * 結果獲取
   - WebSocket支持
     * 實時更新
     * 事件推送
   - 身份認證
     * API密鑰
     * OAuth2.0
     * 訪問控制

### 高級功能

1. **預測分析**
   - 情緒趨勢預測
   - 市場影響評估
   - 風險預警

2. **自定義模型**
   - 模型訓練接口
   - 參數優化
   - 效果評估

3. **數據管理**
   - 歷史數據存儲
   - 數據備份
   - 數據清理

---

<a name="english"></a>
## English

### Core Features

1. **News Data Crawling**
   - Multiple news sources support (Reuters, Bloomberg, Yahoo Finance, etc.)
   - Automatic duplicate filtering
   - Configurable time range
   - Multi-language support (English, Chinese)
   - Auto-update and caching mechanism

2. **Sentiment Analysis**
   - Multi-level text analysis
     * Title analysis
     * Content analysis
     * Keyword extraction
   - Adaptive weighting system
     * News source weights
     * Time decay weights
     * Article impact weights
   - Sentiment classification
     * Positive/Negative/Neutral
     * Sentiment score (-1 to 1)
     * Confidence index

3. **Data Visualization**
   - Real-time trend charts
     * Sentiment trends
     * News volume changes
     * Source distribution
   - Interactive charts
     * Zoomable timeline
     * Custom indicators
     * Multi-stock comparison
   - Report generation
     * PDF reports
     * CSV data export
     * Email notifications

4. **Alert System**
   - Custom triggers
     * Sentiment thresholds
     * News volume spikes
     * Specific keywords
   - Multiple notification methods
     * Email
     * Webhook
     * API push
   - Alert management
     * Priority settings
     * Quiet period settings
     * History tracking

5. **API Integration**
   - RESTful API
     * Data queries
     * Analysis triggers
     * Result retrieval
   - WebSocket support
     * Real-time updates
     * Event pushing
   - Authentication
     * API keys
     * OAuth2.0
     * Access control

### Advanced Features

1. **Predictive Analytics**
   - Sentiment trend prediction
   - Market impact assessment
   - Risk alerts

2. **Custom Models**
   - Model training interface
   - Parameter optimization
   - Performance evaluation

3. **Data Management**
   - Historical data storage
   - Data backup
   - Data cleanup 