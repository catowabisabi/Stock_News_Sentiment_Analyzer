from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="stock_news_analyzer",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A stock news sentiment analysis tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/Stock_News_Sentiment_Analyzer",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Office/Business :: Financial :: Investment",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "stock-news-analyzer=stock_news_analyzer.cli:main",
        ],
    },
) 