"""
Sentiment analysis module for analyzing news article sentiment.
"""

from typing import List, Dict, Any
import logging
from textblob import TextBlob
import numpy as np
from datetime import datetime

logger = logging.getLogger(__name__)

class SentimentAnalyzer:
    """Sentiment analyzer for news articles."""
    
    def __init__(self):
        """Initialize the sentiment analyzer with default parameters."""
        self.sentiment_threshold = 0.1
        self.time_weight = False
        self.source_weight = {}
        
    def set_parameters(self, sentiment_threshold: float = 0.1,
                      time_weight: bool = False,
                      source_weight: Dict[str, float] = None):
        """
        Set analysis parameters.
        
        Args:
            sentiment_threshold (float): Threshold for sentiment classification
            time_weight (bool): Whether to apply time-based weighting
            source_weight (Dict[str, float]): Weights for different news sources
        """
        self.sentiment_threshold = sentiment_threshold
        self.time_weight = time_weight
        self.source_weight = source_weight or {}
        
    def analyze(self, news_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Analyze sentiment of news articles.
        
        Args:
            news_data (List[Dict]): List of news articles
            
        Returns:
            Dict: Sentiment analysis results
        """
        try:
            if not news_data:
                logger.warning("No news data provided for analysis")
                return self._empty_result()
                
            sentiments = []
            for article in news_data:
                sentiment = self._analyze_article(article)
                sentiments.append(sentiment)
                
            # Calculate aggregate metrics
            avg_sentiment = np.mean([s['sentiment_score'] for s in sentiments])
            std_sentiment = np.std([s['sentiment_score'] for s in sentiments])
            
            result = {
                'overall_sentiment': self._classify_sentiment(avg_sentiment),
                'sentiment_score': float(avg_sentiment),
                'sentiment_std': float(std_sentiment),
                'article_count': len(sentiments),
                'sentiment_distribution': self._get_sentiment_distribution(sentiments),
                'detailed_sentiments': sentiments
            }
            
            logger.info(f"Completed sentiment analysis for {len(news_data)} articles")
            return result
            
        except Exception as e:
            logger.error(f"Error in sentiment analysis: {str(e)}")
            return self._empty_result()
            
    def _analyze_article(self, article: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze sentiment of a single article.
        
        Args:
            article (Dict): News article data
            
        Returns:
            Dict: Article sentiment analysis
        """
        # Combine title and content for analysis
        text = f"{article['title']} {article['content']}"
        blob = TextBlob(text)
        
        # Calculate base sentiment
        sentiment_score = blob.sentiment.polarity
        
        # Apply source weighting if configured
        source = article['source'].lower()
        if self.source_weight and source in self.source_weight:
            sentiment_score *= self.source_weight[source]
            
        # Apply time weighting if enabled
        if self.time_weight:
            pub_date = datetime.strptime(article['published_at'], 
                                       '%Y-%m-%dT%H:%M:%SZ')
            time_factor = self._calculate_time_weight(pub_date)
            sentiment_score *= time_factor
            
        return {
            'title': article['title'],
            'sentiment_score': sentiment_score,
            'sentiment': self._classify_sentiment(sentiment_score),
            'source': article['source'],
            'url': article['url'],
            'published_at': article['published_at']
        }
        
    def _classify_sentiment(self, score: float) -> str:
        """
        Classify sentiment score into categories.
        
        Args:
            score (float): Sentiment score
            
        Returns:
            str: Sentiment classification
        """
        if score > self.sentiment_threshold:
            return 'positive'
        elif score < -self.sentiment_threshold:
            return 'negative'
        return 'neutral'
        
    def _calculate_time_weight(self, pub_date: datetime) -> float:
        """
        Calculate time-based weight for sentiment.
        
        Args:
            pub_date (datetime): Article publication date
            
        Returns:
            float: Time weight factor
        """
        time_diff = datetime.now() - pub_date
        days_old = time_diff.days
        
        # Exponential decay with half-life of 7 days
        return np.exp(-days_old * np.log(2) / 7)
        
    def _get_sentiment_distribution(self, sentiments: List[Dict]) -> Dict[str, int]:
        """
        Calculate distribution of sentiment categories.
        
        Args:
            sentiments (List[Dict]): List of sentiment results
            
        Returns:
            Dict[str, int]: Count of sentiments by category
        """
        distribution = {'positive': 0, 'neutral': 0, 'negative': 0}
        for sentiment in sentiments:
            distribution[sentiment['sentiment']] += 1
        return distribution
        
    def _empty_result(self) -> Dict[str, Any]:
        """
        Generate empty result structure.
        
        Returns:
            Dict: Empty sentiment analysis result
        """
        return {
            'overall_sentiment': 'neutral',
            'sentiment_score': 0.0,
            'sentiment_std': 0.0,
            'article_count': 0,
            'sentiment_distribution': {'positive': 0, 'neutral': 0, 'negative': 0},
            'detailed_sentiments': []
        } 