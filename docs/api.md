# API 文檔 API Documentation

[English](#english) | [繁體中文](#traditional-chinese)

---

<a name="traditional-chinese"></a>
## 繁體中文

### API 概述

股票新聞情緒分析器提供了完整的 RESTful API，允許您以程序化方式訪問所有功能。

### 認證

所有 API 請求都需要 API 密鑰進行認證。在請求頭中包含您的 API 密鑰：

```bash
Authorization: Bearer your_api_key_here
```

### 端點

#### 1. 新聞分析

##### 獲取股票新聞情緒
```http
GET /api/v1/sentiment/{stock_symbol}
```

參數：
- `stock_symbol`: 股票代碼
- `days` (可選): 分析天數，默認7天
- `language` (可選): 新聞語言，默認 'en'

響應示例：
```json
{
    "status": "success",
    "data": {
        "overall_sentiment": "positive",
        "sentiment_score": 0.75,
        "sentiment_std": 0.15,
        "article_count": 42,
        "sentiment_distribution": {
            "positive": 30,
            "neutral": 8,
            "negative": 4
        }
    }
}
```

##### 批量分析
```http
POST /api/v1/sentiment/batch
```

請求體：
```json
{
    "symbols": ["AAPL", "GOOGL", "MSFT"],
    "days": 7
}
```

#### 2. 警報管理

##### 創建警報
```http
POST /api/v1/alerts
```

請求體：
```json
{
    "stock_symbol": "AAPL",
    "conditions": {
        "sentiment_threshold": -0.5,
        "volume_threshold": 1000
    },
    "notification": {
        "type": "email",
        "target": "user@example.com"
    }
}
```

##### 獲取警報
```http
GET /api/v1/alerts
```

#### 3. 數據導出

##### 導出分析報告
```http
GET /api/v1/reports/{stock_symbol}
```

參數：
- `format`: 'pdf' 或 'csv'
- `start_date`: 開始日期
- `end_date`: 結束日期

### 錯誤處理

API 使用標準 HTTP 狀態碼：

- 200: 成功
- 400: 請求錯誤
- 401: 未認證
- 403: 未授權
- 404: 資源不存在
- 429: 請求過多
- 500: 服務器錯誤

錯誤響應格式：
```json
{
    "status": "error",
    "code": "error_code",
    "message": "錯誤描述"
}
```

### 速率限制

- 免費帳戶：60 請求/小時
- 專業帳戶：1000 請求/小時
- 企業帳戶：無限制

---

<a name="english"></a>
## English

### API Overview

The Stock News Sentiment Analyzer provides a complete RESTful API that allows programmatic access to all features.

### Authentication

All API requests require an API key for authentication. Include your API key in the request header:

```bash
Authorization: Bearer your_api_key_here
```

### Endpoints

#### 1. News Analysis

##### Get Stock News Sentiment
```http
GET /api/v1/sentiment/{stock_symbol}
```

Parameters:
- `stock_symbol`: Stock symbol
- `days` (optional): Number of days to analyze, default 7
- `language` (optional): News language, default 'en'

Response example:
```json
{
    "status": "success",
    "data": {
        "overall_sentiment": "positive",
        "sentiment_score": 0.75,
        "sentiment_std": 0.15,
        "article_count": 42,
        "sentiment_distribution": {
            "positive": 30,
            "neutral": 8,
            "negative": 4
        }
    }
}
```

##### Batch Analysis
```http
POST /api/v1/sentiment/batch
```

Request body:
```json
{
    "symbols": ["AAPL", "GOOGL", "MSFT"],
    "days": 7
}
```

#### 2. Alert Management

##### Create Alert
```http
POST /api/v1/alerts
```

Request body:
```json
{
    "stock_symbol": "AAPL",
    "conditions": {
        "sentiment_threshold": -0.5,
        "volume_threshold": 1000
    },
    "notification": {
        "type": "email",
        "target": "user@example.com"
    }
}
```

##### Get Alerts
```http
GET /api/v1/alerts
```

#### 3. Data Export

##### Export Analysis Report
```http
GET /api/v1/reports/{stock_symbol}
```

Parameters:
- `format`: 'pdf' or 'csv'
- `start_date`: Start date
- `end_date`: End date

### Error Handling

The API uses standard HTTP status codes:

- 200: Success
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 429: Too Many Requests
- 500: Server Error

Error response format:
```json
{
    "status": "error",
    "code": "error_code",
    "message": "Error description"
}
```

### Rate Limits

- Free accounts: 60 requests/hour
- Professional accounts: 1000 requests/hour
- Enterprise accounts: Unlimited 