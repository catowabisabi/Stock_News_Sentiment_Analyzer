import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from GoogleNews import GoogleNews
from newspaper import Article
from newspaper import Config
from wordcloud import WordCloud, STOPWORDS
import deepl 

import config as cfg

from opencc import OpenCC



auth_key = cfg.my_deepl_API
target_language = "ZH"

translator = deepl.Translator(auth_key)

def translate_en(text):
    result = translator.translate_text(text, target_lang=target_language) 
    translated_text = result.text
    return translated_text


cc = OpenCC('s2hk')
def cn_to_hk(text):
    return cc.convert(text)





# 新聞提取的時間範圍，基本上是 1 天。
now = dt.date.today()
now = now.strftime('%m-%d-%Y')
yesterday = dt.date.today() - dt.timedelta(days = 1)
yesterday = yesterday.strftime('%m-%d-%Y')

# NLTK punkt 使用高級算法將文本分成句子列表
nltk.download('punkt')

# 設置user_agent變量
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0'
config = Config()
config.browser_user_agent = user_agent
# 防止超時
config.request_timeout = 10

# 拿公司名字 / Tickers
company_name = input("請提供股票名字或公司股票Tickers: ")


if company_name != '':
    print(f'下載和分析 {company_name} 的近期新聞中, 請等等, 實情應該係咁...')

    # 提取資料
    googlenews = GoogleNews(start=yesterday,end=now)
    googlenews.search(company_name)
    result = googlenews.result()
    # 保存資料
    df = pd.DataFrame(result)
    print(df)


try:
    list =[] #空白清單 
    for i in df.index:
        dict = {} # 用來放文章的dict
        article = Article(df['link'][i],config=config) # 文章link
        try:
          article.download() # 下載文章 
          article.parse() # 解析文章
          article.nlp() # 自然語言系統解析 (nlp)
        except:
           pass 
        # 再排過
        dict['Date']=df['date'][i] 
        dict['Media']=df['media'][i]
        dict['Title']=article.title
        dict['Article']=article.text
        dict['Summary']=article.summary
        print("\n\n\n")
        print (dict['Summary'])
        summary_cn = translate_en(dict['Summary'])
        summary_cn = cn_to_hk(summary_cn)
        print("\n")
        print (summary_cn)
        print("\n\n\n")
        dict['Key_words']=article.keywords
        list.append(dict)
    check_empty = not any(list)
    # print(check_empty)

    # 如果有資料
    if check_empty == False:
      news_df=pd.DataFrame(list) # 打印個DF出黎
      print("\n\n\n")
      print(news_df)
      print("\n\n\n")

except Exception as e:
    #exception handling
    print("出錯:" + str(e))
    print('睇黎.... 拎資料時有D問題wo... 再試過啦唔好意思....' )




# ===================自然語言系統 -- 文章情緒分析器==================

# 百份比計算器
def percentage(part,whole):
    return 100 * float(part)/float(whole)

# 分數一開波設定
positive = 0
negative = 0
neutral = 0

# 新聞, 句字, 清單
news_list = []
neutral_list = []
negative_list = []
positive_list = []

# 係df summary入邊所有的新聞中, 每一個新聞
for news in news_df['Summary']:
    news_list.append(news)
    # 評一評分先
    analyzer = SentimentIntensityAnalyzer().polarity_scores(news)
    neg = analyzer['neg']
    neu = analyzer['neu']
    pos = analyzer['pos']
    # 平均分
    comp = analyzer['compound']

    if neg > pos:
        negative_list.append(news) # 壞新聞放呢度
        negative += 1 # 加一分
    elif pos > neg:
        positive_list.append(news) # 好新聞放呢度
        positive += 1 # 加一分
    elif pos == neg:
        neutral_list.append(news) # 中性新聞放呢度
        neutral += 1 # 加一分

positive = percentage(positive, len(news_df)) #計百分比
negative = percentage(negative, len(news_df))
neutral = percentage(neutral, len(news_df))

# 變成pandas先
news_list = pd.DataFrame(news_list)
neutral_list = pd.DataFrame(neutral_list)
negative_list = pd.DataFrame(negative_list)
positive_list = pd.DataFrame(positive_list)

# 計下幾多好唔好新聞
print("好新聞:", '%.2f' % len(positive_list), end='\n')
print("中性新聞:", '%.2f' % len(neutral_list), end='\n')
print("壞新聞:", '%.2f' % len(negative_list), end='\n')

# 出返個繪圖先
labels = ['Positive ['+str(round(positive))+'%]' , 'Neutral ['+str(round(neutral))+'%]','Negative ['+str(round(negative))+'%]']
sizes = [positive, neutral, negative]
colors = ['yellowgreen', 'blue','red']
patches, texts = plt.pie(sizes,colors=colors, startangle=90)
plt.style.use('default')
plt.legend(labels)
plt.title("Sentiment Analysis Result for stock= "+company_name+"" )
plt.axis('equal')
plt.show()

# Word cloud visualization
def word_cloud(text):
    stopwords = set(STOPWORDS)
    allWords = ' '.join([nws for nws in text])
    wordCloud = WordCloud(background_color='black',width = 1600, height = 800,stopwords = stopwords,min_font_size = 20,max_font_size=150,colormap='prism').generate(allWords)
    fig, ax = plt.subplots(figsize=(20,10), facecolor='k')
    plt.imshow(wordCloud)
    ax.axis("off")
    fig.tight_layout(pad=0)
    plt.show()

print('Wordcloud for ' + company_name)
word_cloud(news_df['Summary'].values)