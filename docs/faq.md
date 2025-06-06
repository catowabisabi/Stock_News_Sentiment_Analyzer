# 常見問題 FAQ

[English](#english) | [繁體中文](#traditional-chinese)

---

<a name="traditional-chinese"></a>
## 繁體中文

### 一般問題

1. **這個工具是如何工作的？**
   - 工具會自動從多個新聞來源收集股票相關新聞
   - 使用自然語言處理技術分析新聞內容
   - 計算整體情緒評分和趨勢
   - 生成可視化報告和警報

2. **支持哪些股票市場？**
   - 美國股市（NYSE, NASDAQ）
   - 香港股市（HKEX）
   - 其他主要市場（可配置）

3. **需要付費嗎？**
   - 基礎功能免費使用
   - 高級功能需要訂閱專業版
   - 可根據需求定制企業版

### 技術問題

1. **如何處理 API 限制？**
   - 實施請求限速
   - 使用數據緩存
   - 提供批量處理選項

2. **如何提高分析準確性？**
   - 調整情緒閾值
   - 配置來源權重
   - 使用自定義詞典

3. **數據存儲在哪裡？**
   - 本地文件系統
   - PostgreSQL 數據庫
   - 可配置雲存儲

### 使用問題

1. **如何開始使用？**
   - 安裝依賴
   - 配置 API 密鑰
   - 運行示例腳本

2. **如何設置警報？**
   - 配置觸發條件
   - 選擇通知方式
   - 設置監控週期

3. **如何導出數據？**
   - CSV 格式導出
   - PDF 報告生成
   - API 數據獲取

### 故障排除

1. **常見錯誤**
   - API 密鑰無效
   - 網絡連接問題
   - 數據格式錯誤

2. **性能問題**
   - 優化查詢頻率
   - 增加緩存
   - 減少數據量

3. **數據質量**
   - 過濾無關新聞
   - 處理重複內容
   - 改進分類準確性

---

<a name="english"></a>
## English

### General Questions

1. **How does this tool work?**
   - Automatically collects stock-related news from multiple sources
   - Analyzes news content using NLP technology
   - Calculates overall sentiment scores and trends
   - Generates visualization reports and alerts

2. **Which stock markets are supported?**
   - US markets (NYSE, NASDAQ)
   - Hong Kong market (HKEX)
   - Other major markets (configurable)

3. **Is it free to use?**
   - Basic features are free
   - Advanced features require professional subscription
   - Enterprise version available for customization

### Technical Questions

1. **How to handle API limits?**
   - Implement request rate limiting
   - Use data caching
   - Provide batch processing options

2. **How to improve analysis accuracy?**
   - Adjust sentiment thresholds
   - Configure source weights
   - Use custom dictionaries

3. **Where is data stored?**
   - Local file system
   - PostgreSQL database
   - Configurable cloud storage

### Usage Questions

1. **How to get started?**
   - Install dependencies
   - Configure API keys
   - Run example scripts

2. **How to set up alerts?**
   - Configure trigger conditions
   - Choose notification methods
   - Set monitoring periods

3. **How to export data?**
   - CSV format export
   - PDF report generation
   - API data retrieval

### Troubleshooting

1. **Common Errors**
   - Invalid API keys
   - Network connectivity issues
   - Data format errors

2. **Performance Issues**
   - Optimize query frequency
   - Increase caching
   - Reduce data volume

3. **Data Quality**
   - Filter irrelevant news
   - Handle duplicate content
   - Improve classification accuracy 