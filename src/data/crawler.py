"""
News crawler module for fetching stock-related news from various sources.
"""

import requests
from datetime import datetime, timedelta
from typing import List, Dict, Any
import logging
from ..utils.config import get_api_key

logger = logging.getLogger(__name__)

class NewsCrawler:
    """News crawler for fetching stock-related news articles."""
    
    def __init__(self):
        """Initialize the news crawler with API configurations."""
        self.news_api_key = get_api_key('NEWS_API_KEY')
        self.alpha_vantage_key = get_api_key('ALPHA_VANTAGE_API_KEY')
        
    def fetch_news(self, symbol: str, days: int = 7) -> List[Dict[Any, Any]]:
        """
        Fetch news articles for a specific stock symbol.
        
        Args:
            symbol (str): Stock symbol (e.g., 'AAPL')
            days (int): Number of days to look back
            
        Returns:
            List[Dict]: List of news articles with metadata
        """
        try:
            end_date = datetime.now()
            start_date = end_date - timedelta(days=days)
            
            # Format dates for API
            from_date = start_date.strftime('%Y-%m-%d')
            to_date = end_date.strftime('%Y-%m-%d')
            
            # News API endpoint
            url = f"https://newsapi.org/v2/everything"
            
            params = {
                'q': f"{symbol} stock",
                'from': from_date,
                'to': to_date,
                'language': 'en',
                'sortBy': 'publishedAt',
                'apiKey': self.news_api_key
            }
            
            response = requests.get(url, params=params)
            response.raise_for_status()
            
            news_data = response.json()
            
            # Process and clean the news data
            processed_news = self._process_news_data(news_data.get('articles', []))
            
            logger.info(f"Successfully fetched {len(processed_news)} news articles for {symbol}")
            return processed_news
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching news for {symbol}: {str(e)}")
            return []
            
    def _process_news_data(self, articles: List[Dict]) -> List[Dict]:
        """
        Process and clean the raw news data.
        
        Args:
            articles (List[Dict]): Raw news articles
            
        Returns:
            List[Dict]: Processed news articles
        """
        processed_articles = []
        
        for article in articles:
            processed_article = {
                'title': article.get('title', ''),
                'description': article.get('description', ''),
                'content': article.get('content', ''),
                'source': article.get('source', {}).get('name', ''),
                'url': article.get('url', ''),
                'published_at': article.get('publishedAt', ''),
                'author': article.get('author', '')
            }
            
            # Only include articles with actual content
            if processed_article['content'] and processed_article['title']:
                processed_articles.append(processed_article)
                
        return processed_articles 