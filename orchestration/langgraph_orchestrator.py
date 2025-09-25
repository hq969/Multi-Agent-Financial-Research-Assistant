from typing import Dict, Any
from agents.agent_a_fetcher import fetch_latest_news, fetch_market_price
from agents.agent_b_analyzer import analyze_articles
from agents.agent_c_reporter import generate_insight_report
from utils.dynamo import put_item
from datetime import datetime

def run_pipeline(ticker: str = "AAPL") -> Dict[str, Any]:
    """
    Simple synchronous pipeline that:
      1) fetches news & market data
      2) analyzes news (summary + sentiment)
      3) generates a GPT report
      4) persists result to DynamoDB
    """
    # 1) Fetch
    try:
        news = fetch_latest_news(query=f"{ticker} earnings OR {ticker} stock", page_size=15)
    except Exception as e:
        news = []
        print("Warning: fetch_latest_news failed:", e)

    try:
        market = fetch_market_price(symbol=ticker)
    except Exception as e:
        market = {"error": str(e)}

    # 2) Analyze
    analyzed = analyze_articles(news)

    # 3) Generate report
    report_obj = generate_insight_report(ticker, market, analyzed)
    report_text = report_obj.get("report") if isinstance(report_obj, dict) else str(report_obj)

    # 4) Persist
    item = {
        "pk": f"TICKER#{ticker}",
        "sk": f"REPORT#{datetime.utcnow().isoformat()}",
        "ticker": ticker,
        "market": market,
        "news_count": len(news),
        "report": report_text
    }
    try:
        put_item(item)
    except Exception as e:
        print("Warning: failed to persist to DynamoDB:", e)

    return item
