"""
Logging configuration module.
"""

import logging
import logging.handlers
import os
from datetime import datetime
from typing import Optional

def setup_logger(name: str, 
                log_file: Optional[str] = None,
                level: int = logging.INFO) -> logging.Logger:
    """
    Set up a logger with file and console handlers.
    
    Args:
        name (str): Logger name
        log_file (str, optional): Path to log file
        level (int): Logging level
        
    Returns:
        logging.Logger: Configured logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Create formatters
    detailed_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    simple_formatter = logging.Formatter(
        '%(levelname)s: %(message)s'
    )
    
    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(simple_formatter)
    logger.addHandler(console_handler)
    
    # Create file handler if log file is specified
    if log_file:
        # Ensure log directory exists
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        
        # Create rotating file handler
        file_handler = logging.handlers.RotatingFileHandler(
            log_file,
            maxBytes=10485760,  # 10MB
            backupCount=5
        )
        file_handler.setLevel(level)
        file_handler.setFormatter(detailed_formatter)
        logger.addHandler(file_handler)
    
    return logger

def get_stock_logger(stock_symbol: str) -> logging.Logger:
    """
    Get a logger for a specific stock.
    
    Args:
        stock_symbol (str): Stock symbol
        
    Returns:
        logging.Logger: Stock-specific logger
    """
    log_dir = os.path.join('logs', 'stocks', stock_symbol)
    log_file = os.path.join(
        log_dir,
        f"{stock_symbol}_{datetime.now().strftime('%Y%m%d')}.log"
    )
    
    return setup_logger(
        name=f"stock.{stock_symbol}",
        log_file=log_file,
        level=logging.INFO
    )

def get_analysis_logger() -> logging.Logger:
    """
    Get a logger for sentiment analysis.
    
    Returns:
        logging.Logger: Analysis logger
    """
    log_dir = os.path.join('logs', 'analysis')
    log_file = os.path.join(
        log_dir,
        f"analysis_{datetime.now().strftime('%Y%m%d')}.log"
    )
    
    return setup_logger(
        name="sentiment_analysis",
        log_file=log_file,
        level=logging.INFO
    ) 