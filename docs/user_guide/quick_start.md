# 快速入門指南 Quick Start Guide

[English](#english) | [繁體中文](#traditional-chinese)

---

<a name="traditional-chinese"></a>
## 繁體中文

### 5分鐘上手教學

1. **安裝軟體**
   ```bash
   # 下載專案
   git clone https://github.com/yourusername/Stock_News_Sentiment_Analyzer.git
   cd Stock_News_Sentiment_Analyzer

   # 安裝所需套件
   pip install -r requirements.txt
   ```

2. **設定API金鑰**
   - 複製設定範本：`cp env.example .env`
   - 在 `.env` 填入您的 API 金鑰

3. **開始分析**
   ```python
   # 範例程式碼
   from stock_analyzer import StockAnalyzer

   # 創建分析器
   analyzer = StockAnalyzer()

   # 分析股票
   results = analyzer.analyze("AAPL")
   
   # 顯示結果
   analyzer.show_results(results)
   ```

### 基本功能演示

1. **查看股票新聞情緒**
   ```python
   # 獲取最近7天的新聞情緒
   sentiment = analyzer.get_sentiment("TSLA", days=7)
   ```

2. **設置價格提醒**
   ```python
   # 設定當情緒分數低於-0.5時提醒
   analyzer.set_alert("GOOGL", sentiment_threshold=-0.5)
   ```

3. **導出分析報告**
   ```python
   # 導出PDF報告
   analyzer.export_report("AAPL", format="pdf")
   ```

### 進階使用技巧

- 使用批量分析節省時間
- 自定義分析參數
- 設置自動化任務

---

<a name="english"></a>
## English

### 5-Minute Tutorial

1. **Install Software**
   ```bash
   # Download project
   git clone https://github.com/yourusername/Stock_News_Sentiment_Analyzer.git
   cd Stock_News_Sentiment_Analyzer

   # Install requirements
   pip install -r requirements.txt
   ```

2. **Configure API Keys**
   - Copy settings template: `cp env.example .env`
   - Fill in your API keys in `.env`

3. **Start Analysis**
   ```python
   # Example code
   from stock_analyzer import StockAnalyzer

   # Create analyzer
   analyzer = StockAnalyzer()

   # Analyze stock
   results = analyzer.analyze("AAPL")
   
   # Show results
   analyzer.show_results(results)
   ```

### Basic Features Demo

1. **Check Stock News Sentiment**
   ```python
   # Get sentiment for last 7 days
   sentiment = analyzer.get_sentiment("TSLA", days=7)
   ```

2. **Set Price Alerts**
   ```python
   # Set alert when sentiment score drops below -0.5
   analyzer.set_alert("GOOGL", sentiment_threshold=-0.5)
   ```

3. **Export Analysis Report**
   ```python
   # Export PDF report
   analyzer.export_report("AAPL", format="pdf")
   ```

### Advanced Usage Tips

- Use batch analysis to save time
- Customize analysis parameters
- Set up automation tasks 