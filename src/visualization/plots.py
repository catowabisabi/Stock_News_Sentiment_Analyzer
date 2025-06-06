"""
Data visualization module for sentiment analysis results.
"""

import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, List, Any
import pandas as pd
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

def plot_sentiment_trend(results: Dict[str, Any], stock_symbol: str) -> str:
    """
    Plot sentiment trend over time.
    
    Args:
        results (Dict[str, Any]): Sentiment analysis results
        stock_symbol (str): Stock symbol
        
    Returns:
        str: Path to saved plot
    """
    try:
        # Convert detailed sentiments to DataFrame
        df = pd.DataFrame(results['detailed_sentiments'])
        df['published_at'] = pd.to_datetime(df['published_at'])
        df = df.sort_values('published_at')
        
        # Create figure
        plt.figure(figsize=(12, 6))
        
        # Plot sentiment scores
        plt.plot(df['published_at'], df['sentiment_score'], 
                marker='o', linestyle='-', linewidth=2)
        
        # Customize plot
        plt.title(f'Sentiment Trend for {stock_symbol}')
        plt.xlabel('Date')
        plt.ylabel('Sentiment Score')
        plt.grid(True, linestyle='--', alpha=0.7)
        
        # Rotate x-axis labels
        plt.xticks(rotation=45)
        
        # Add horizontal lines for sentiment thresholds
        plt.axhline(y=0, color='gray', linestyle='-', alpha=0.3)
        plt.axhline(y=0.1, color='green', linestyle='--', alpha=0.3)
        plt.axhline(y=-0.1, color='red', linestyle='--', alpha=0.3)
        
        # Adjust layout
        plt.tight_layout()
        
        # Save plot
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        plot_path = f'data/plots/{stock_symbol}_sentiment_{timestamp}.png'
        plt.savefig(plot_path)
        plt.close()
        
        logger.info(f"Sentiment trend plot saved to {plot_path}")
        return plot_path
        
    except Exception as e:
        logger.error(f"Error creating sentiment trend plot: {str(e)}")
        return ""

def plot_sentiment_distribution(results: Dict[str, Any], stock_symbol: str) -> str:
    """
    Plot distribution of sentiment categories.
    
    Args:
        results (Dict[str, Any]): Sentiment analysis results
        stock_symbol (str): Stock symbol
        
    Returns:
        str: Path to saved plot
    """
    try:
        # Get sentiment distribution
        distribution = results['sentiment_distribution']
        
        # Create figure
        plt.figure(figsize=(8, 6))
        
        # Create bar plot
        colors = ['green', 'gray', 'red']
        plt.bar(distribution.keys(), distribution.values(), color=colors)
        
        # Customize plot
        plt.title(f'Sentiment Distribution for {stock_symbol}')
        plt.xlabel('Sentiment Category')
        plt.ylabel('Number of Articles')
        
        # Add value labels on bars
        for i, v in enumerate(distribution.values()):
            plt.text(i, v, str(v), ha='center', va='bottom')
            
        # Adjust layout
        plt.tight_layout()
        
        # Save plot
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        plot_path = f'data/plots/{stock_symbol}_distribution_{timestamp}.png'
        plt.savefig(plot_path)
        plt.close()
        
        logger.info(f"Sentiment distribution plot saved to {plot_path}")
        return plot_path
        
    except Exception as e:
        logger.error(f"Error creating sentiment distribution plot: {str(e)}")
        return ""

def plot_source_analysis(results: Dict[str, Any], stock_symbol: str) -> str:
    """
    Plot sentiment analysis by news source.
    
    Args:
        results (Dict[str, Any]): Sentiment analysis results
        stock_symbol (str): Stock symbol
        
    Returns:
        str: Path to saved plot
    """
    try:
        # Convert detailed sentiments to DataFrame
        df = pd.DataFrame(results['detailed_sentiments'])
        
        # Calculate average sentiment by source
        source_sentiment = df.groupby('source')['sentiment_score'].agg(['mean', 'count'])
        source_sentiment = source_sentiment.sort_values('mean', ascending=True)
        
        # Create figure
        plt.figure(figsize=(10, 6))
        
        # Create horizontal bar plot
        bars = plt.barh(source_sentiment.index, source_sentiment['mean'])
        
        # Color bars based on sentiment
        for bar in bars:
            if bar.get_width() > 0:
                bar.set_color('green')
            else:
                bar.set_color('red')
                
        # Customize plot
        plt.title(f'Average Sentiment by News Source for {stock_symbol}')
        plt.xlabel('Average Sentiment Score')
        plt.ylabel('News Source')
        
        # Add value labels
        for i, v in enumerate(source_sentiment['mean']):
            plt.text(v, i, f'{v:.2f} (n={source_sentiment["count"][i]})', 
                    ha='left' if v > 0 else 'right', va='center')
            
        # Add vertical line at zero
        plt.axvline(x=0, color='gray', linestyle='-', alpha=0.3)
        
        # Adjust layout
        plt.tight_layout()
        
        # Save plot
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        plot_path = f'data/plots/{stock_symbol}_sources_{timestamp}.png'
        plt.savefig(plot_path)
        plt.close()
        
        logger.info(f"Source analysis plot saved to {plot_path}")
        return plot_path
        
    except Exception as e:
        logger.error(f"Error creating source analysis plot: {str(e)}")
        return "" 