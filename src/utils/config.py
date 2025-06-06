"""
Configuration management module.
"""

import os
from typing import Any, Dict
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

logger = logging.getLogger(__name__)

def get_api_key(key_name: str) -> str:
    """
    Get API key from environment variables.
    
    Args:
        key_name (str): Name of the API key in environment variables
        
    Returns:
        str: API key value
    
    Raises:
        ValueError: If the API key is not found
    """
    api_key = os.getenv(key_name)
    if not api_key:
        logger.error(f"Missing required API key: {key_name}")
        raise ValueError(f"Missing required API key: {key_name}")
    return api_key

def get_db_config() -> Dict[str, Any]:
    """
    Get database configuration from environment variables.
    
    Returns:
        Dict[str, Any]: Database configuration parameters
    """
    return {
        'host': os.getenv('DB_HOST', 'localhost'),
        'port': int(os.getenv('DB_PORT', 5432)),
        'database': os.getenv('DB_NAME', 'stock_news_db'),
        'user': os.getenv('DB_USER', ''),
        'password': os.getenv('DB_PASSWORD', '')
    }

def get_app_config() -> Dict[str, Any]:
    """
    Get application configuration from environment variables.
    
    Returns:
        Dict[str, Any]: Application configuration parameters
    """
    return {
        'debug': os.getenv('DEBUG', 'False').lower() == 'true',
        'log_level': os.getenv('LOG_LEVEL', 'INFO'),
        'port': int(os.getenv('PORT', 8000))
    }

def get_smtp_config() -> Dict[str, str]:
    """
    Get SMTP configuration for email alerts.
    
    Returns:
        Dict[str, str]: SMTP configuration parameters
    """
    return {
        'server': os.getenv('SMTP_SERVER', 'smtp.gmail.com'),
        'port': int(os.getenv('SMTP_PORT', 587)),
        'user': os.getenv('SMTP_USER', ''),
        'password': os.getenv('SMTP_PASSWORD', '')
    }

def setup_logging():
    """Configure logging for the application."""
    log_level = get_app_config()['log_level']
    
    logging.basicConfig(
        level=getattr(logging, log_level),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    ) 