import os
import requests
from datetime import datetime
from typing import List, Dict, Any

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
MARKET_API_KEY = os.getenv("MARKET_API_KEY")

def fetch_latest_news(query: str = "stock market", page_size: int = 20) -> List[Dict[str, Any]]:
    """
    Fetch recent articles using NewsAPI.org (example).
    Replace URL/params if you use a different provider.
    """
    if not NEWS_API_KEY:
        raise EnvironmentError("NEWS_API_KEY not set in environment")
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "pageSize": page_size,
        "language": "en",
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY
    }
    resp = requests.get(url, params=params, timeout=15)
    resp.raise_for_status()
    data = resp.json()
    articles = data.get("articles", [])
    out = []
    for a in articles:
        out.append({
            "source": a.get("source", {}).get("name"),
            "title": a.get("title"),
            "description": a.get("description"),
            "content": a.get("content"),
            "url": a.get("url"),
            "publishedAt": a.get("publishedAt") or datetime.utcnow().isoformat()
        })
    return out

def fetch_market_price(symbol: str = "AAPL") -> Dict[str, Any]:
    """
    Example: Alpha Vantage GLOBAL_QUOTE
    Replace with your market data provider if needed.
    """
    if not MARKET_API_KEY:
        raise EnvironmentError("MARKET_API_KEY not set in environment")
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": MARKET_API_KEY
    }
    resp = requests.get(url, params=params, timeout=15)
    resp.raise_for_status()
    data = resp.json().get("Global Quote", {}) or {}
    return {
        "symbol": symbol,
        "price": data.get("05. price"),
        "volume": data.get("06. volume"),
        "change_percent": data.get("10. change percent"),
        "raw": data,
        "timestamp": datetime.utcnow().isoformat()
    }
