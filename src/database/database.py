"""
Database Module
Responsible for data storage and retrieval
"""

from typing import List, Dict, Optional
import sqlite3
import pandas as pd
import logging
from datetime import datetime

class Database:
    """Database Class"""
    
    def __init__(self, config: Dict = None):
        """
        Initialize database
        
        Args:
            config: Configuration dictionary
        """
        self.config = config or {}
        self.db_path = self.config.get('db_path', 'stock_news.db')
        self.logger = logging.getLogger(__name__)
        self._init_db()
        
    def _init_db(self):
        """Initialize database tables"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Create news table
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS news (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    symbol TEXT NOT NULL,
                    title TEXT NOT NULL,
                    content TEXT,
                    source TEXT,
                    url TEXT,
                    published_at DATETIME,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
                """)
                
                # Create sentiment table
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS sentiment (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    news_id INTEGER,
                    compound REAL,
                    positive REAL,
                    neutral REAL,
                    negative REAL,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (news_id) REFERENCES news (id)
                )
                """)
                
                conn.commit()
                
        except Exception as e:
            self.logger.error(f"Error initializing database: {e}")
            raise
    
    def save_news(self, news: List[Dict]) -> bool:
        """
        Save news data
        
        Args:
            news: List of news articles
            
        Returns:
            Success status
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                for article in news:
                    # Insert news
                    cursor.execute("""
                    INSERT INTO news (symbol, title, content, source, url, published_at)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """, (
                        article['symbol'],
                        article['title'],
                        article.get('content'),
                        article.get('source'),
                        article.get('url'),
                        article.get('published_at')
                    ))
                    
                    # Get news ID
                    news_id = cursor.lastrowid
                    
                    # Insert sentiment
                    if 'sentiment' in article:
                        cursor.execute("""
                        INSERT INTO sentiment (news_id, compound, positive, neutral, negative)
                        VALUES (?, ?, ?, ?, ?)
                        """, (
                            news_id,
                            article['sentiment'].get('compound'),
                            article['sentiment'].get('pos'),
                            article['sentiment'].get('neu'),
                            article['sentiment'].get('neg')
                        ))
                
                conn.commit()
                return True
                
        except Exception as e:
            self.logger.error(f"Error saving news: {e}")
            return False
    
    def query_news(self, symbol: str, days: Optional[int] = None) -> List[Dict]:
        """
        Query news data
        
        Args:
            symbol: Stock symbol
            days: Number of days
            
        Returns:
            List of news articles
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                # Convert to DataFrame
                query = """
                SELECT n.*, s.compound, s.positive, s.neutral, s.negative
                FROM news n
                LEFT JOIN sentiment s ON n.id = s.news_id
                WHERE n.symbol = ?
                """
                
                params = [symbol]
                
                if days:
                    query += " AND n.published_at >= date('now', ?)"
                    params.append(f'-{days} days')
                
                df = pd.read_sql_query(
                    query,
                    conn,
                    params=params,
                    parse_dates=['published_at', 'created_at']
                )
                
                return df.to_dict('records')
                
        except Exception as e:
            self.logger.error(f"Error querying news: {e}")
            return []
    
    def clean_data(self, days: int) -> bool:
        """
        Clean old data
        
        Args:
            days: Days to keep
            
        Returns:
            Success status
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Delete old data
                cursor.execute("""
                DELETE FROM sentiment
                WHERE news_id IN (
                    SELECT id FROM news
                    WHERE published_at < date('now', ?)
                )
                """, (f'-{days} days',))
                
                cursor.execute("""
                DELETE FROM news
                WHERE published_at < date('now', ?)
                """, (f'-{days} days',))
                
                conn.commit()
                return True
                
        except Exception as e:
            self.logger.error(f"Error cleaning data: {e}")
            return False
