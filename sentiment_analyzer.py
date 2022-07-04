# Import libraries
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from urllib.request import urlopen
from urllib.request import Request
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from config import my_tickers, my_headers

# 需要下載的新聞的數目 
news_number = 3 
tickers = my_tickers

# 新聞的URL
finviz_url = 'https://finviz.com/quote.ashx?t='
news_tables = {}

for ticker in tickers:
    url = finviz_url + ticker
    req = Request(url=url,headers=my_headers) 
    # 拿HTML
    resp = urlopen(req)
    # 解讀成為HTML碼 
    html = BeautifulSoup(resp, features="lxml")
    # 拿news-table內容
    news_table = html.find(id='news-table')
    # 每個ticker都有自己的新聞
    news_tables[ticker] = news_table

# 使用 BeautifulSoup 和 requests 模塊從 FinViz 網站獲取新聞數據。
# 該代碼解析 HTML 新聞表的 URL，並遍歷代碼列表以收集每個代碼的最近標題。
# 對於每隻輸入的股票，都會打印出 n 個最近的標題，以便於查看數據。
try:
    for ticker in tickers:
        df = news_tables[ticker]
        df_tr = df.findAll('tr')
    
        print ('\n')
        print ('Recent News Headlines for {}: '.format(ticker))
        
        for i, table_row in enumerate(df_tr):
            a_text = table_row.a.text
            td_text = table_row.td.text
            td_text = td_text.strip()
            print(a_text,'(',td_text,')')
            if i == news_number-1:
                break
except KeyError:
    pass


# 為了執行情緒分析，數據必須採用正確的格式，因此這段代碼會遍歷收集到的新聞，
# 並將其分類為包含代碼、日期、時間和實際標題的列表。
parsed_news = []
for file_name, news_table in news_tables.items():
    for x in news_table.findAll('tr'):
        text = x.a.get_text() 
        date_scrape = x.td.text.split()

        if len(date_scrape) == 1:
            time = date_scrape[0]
            
        else:
            date = date_scrape[0]
            time = date_scrape[1]

        ticker = file_name.split('_')[0]
        
        parsed_news.append([ticker, date, time, text])


# 使用nltk，分析每個標題的極性分數，
# 範圍為 -1 到 1，-1 表示高度負面，高度 1 表示正面。
analyzer = SentimentIntensityAnalyzer()

columns = ['Ticker', 'Date', 'Time', 'Headline']
news = pd.DataFrame(parsed_news, columns=columns)
scores = news['Headline'].apply(analyzer.polarity_scores).tolist()

df_scores = pd.DataFrame(scores)
news = news.join(df_scores, rsuffix='_right')


# 數據已準備好以吸引人的方式進行操作和查看。
# 對於輸入列表中的每個代碼，將創建一個新的 DataFrame，其中包括其標題及其各自的分數。
# 創建一個最終的 DataFrame，其中包括每個股票代碼在所有最近解析的新聞中的平均情緒值。
news['Date'] = pd.to_datetime(news.Date).dt.date

unique_ticker = news['Ticker'].unique().tolist()
news_dict = {name: news.loc[news['Ticker'] == name] for name in unique_ticker}

values = []
for ticker in tickers: 
    dataframe = news_dict[ticker]
    dataframe = dataframe.set_index('Ticker')
    dataframe = dataframe.drop(columns = ['Headline'])
    print ('\n')
    print (dataframe.head())
    
    mean = round(dataframe['compound'].mean(), 2)
    values.append(mean)
    
df = pd.DataFrame(list(zip(tickers, values)), columns =['Ticker', 'Mean Sentiment']) 
df = df.set_index('Ticker')
df = df.sort_values('Mean Sentiment', ascending=False)
print ('\n')
print (df)