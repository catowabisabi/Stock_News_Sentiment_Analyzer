# 安裝指南 Installation Guide

[English](#english) | [繁體中文](#traditional-chinese)

---

<a name="traditional-chinese"></a>
## 繁體中文

### 系統要求
- Python 3.8 或更高版本
- pip 包管理器
- Git（用於版本控制）
- PostgreSQL 數據庫（可選，用於數據存儲）

### 安裝步驟

1. **克隆專案**
   ```bash
   git clone https://github.com/yourusername/Stock_News_Sentiment_Analyzer.git
   cd Stock_News_Sentiment_Analyzer
   ```

2. **創建虛擬環境**
   ```bash
   # Windows
   python -m venv env
   .\env\Scripts\activate

   # Linux/Mac
   python3 -m venv env
   source env/bin/activate
   ```

3. **安裝依賴**
   ```bash
   pip install -r requirements.txt
   ```

4. **配置環境變數**
   ```bash
   # 複製環境變數模板
   cp env.example .env
   
   # 使用文本編輯器編輯 .env 文件
   # 填入您的 API 密鑰和其他設定
   ```

5. **初始化數據庫**（可選）
   ```bash
   # 如果使用 PostgreSQL
   createdb stock_news_db
   ```

6. **驗證安裝**
   ```bash
   # 運行測試
   python -m pytest tests/
   ```

### 故障排除

1. **依賴安裝問題**
   - 確保 Python 版本兼容
   - 嘗試更新 pip: `pip install --upgrade pip`
   - 檢查是否有系統特定的依賴要求

2. **數據庫連接問題**
   - 確認 PostgreSQL 服務正在運行
   - 驗證數據庫憑證
   - 檢查防火牆設置

3. **API 密鑰問題**
   - 確保所有必要的 API 密鑰都已正確配置
   - 驗證 API 密鑰的有效性

---

<a name="english"></a>
## English

### System Requirements
- Python 3.8 or higher
- pip package manager
- Git (for version control)
- PostgreSQL database (optional, for data storage)

### Installation Steps

1. **Clone the Project**
   ```bash
   git clone https://github.com/yourusername/Stock_News_Sentiment_Analyzer.git
   cd Stock_News_Sentiment_Analyzer
   ```

2. **Create Virtual Environment**
   ```bash
   # Windows
   python -m venv env
   .\env\Scripts\activate

   # Linux/Mac
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   ```bash
   # Copy environment template
   cp env.example .env
   
   # Edit .env file with your text editor
   # Fill in your API keys and other settings
   ```

5. **Initialize Database** (Optional)
   ```bash
   # If using PostgreSQL
   createdb stock_news_db
   ```

6. **Verify Installation**
   ```bash
   # Run tests
   python -m pytest tests/
   ```

### Troubleshooting

1. **Dependency Installation Issues**
   - Ensure Python version compatibility
   - Try updating pip: `pip install --upgrade pip`
   - Check for system-specific dependency requirements

2. **Database Connection Issues**
   - Confirm PostgreSQL service is running
   - Verify database credentials
   - Check firewall settings

3. **API Key Issues**
   - Ensure all necessary API keys are properly configured
   - Verify API key validity 