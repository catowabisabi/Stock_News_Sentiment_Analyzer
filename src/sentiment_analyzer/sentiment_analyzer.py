"""
Sentiment Analysis Module
Responsible for analyzing sentiment in news text
"""

from typing import List, Dict
import nltk
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import logging

class SentimentAnalyzer:
    """Sentiment Analyzer Class"""
    
    def __init__(self, config: Dict = None):
        """
        Initialize analyzer
        
        Args:
            config: Configuration dictionary
        """
        self.config = config or {}
        self.vader = SentimentIntensityAnalyzer()
        self.logger = logging.getLogger(__name__)
        
    def analyze_sentiment(self, news: List[Dict]) -> List[Dict]:
        """
        Analyze news sentiment
        
        Args:
            news: List of news articles
            
        Returns:
            News list with sentiment scores
        """
        for article in news:
            try:
                article['sentiment'] = self._analyze_text(
                    title=article.get('title', ''),
                    content=article.get('content', ''),
                    comments=article.get('comments', [])
                )
            except Exception as e:
                self.logger.error(f"Error analyzing article {article.get('id')}: {e}")
                article['sentiment'] = {'compound': 0.0}
                
        return news
    
    def _analyze_text(self, title: str, content: str, comments: List[str]) -> Dict:
        """
        Analyze text sentiment
        
        Args:
            title: Title
            content: Content
            comments: Comments
            
        Returns:
            Sentiment scores
        """
        # Calculate weights for each part
        title_weight = 0.3
        content_weight = 0.5
        comments_weight = 0.2
        
        # Analyze each part
        title_sentiment = self._get_vader_sentiment(title)
        content_sentiment = self._get_vader_sentiment(content)
        comments_sentiment = self._analyze_comments(comments)
        
        # Calculate weighted average
        compound = (
            title_sentiment['compound'] * title_weight +
            content_sentiment['compound'] * content_weight +
            comments_sentiment['compound'] * comments_weight
        )
        
        return {
            'compound': compound,
            'title': title_sentiment,
            'content': content_sentiment,
            'comments': comments_sentiment
        }
    
    def _get_vader_sentiment(self, text: str) -> Dict:
        """Analyze sentiment using VADER"""
        return self.vader.polarity_scores(text)
    
    def _analyze_comments(self, comments: List[str]) -> Dict:
        """Analyze comments sentiment"""
        if not comments:
            return {'compound': 0.0}
            
        total = 0.0
        for comment in comments:
            total += self._get_vader_sentiment(comment)['compound']
            
        return {'compound': total / len(comments)}