import json
from orchestration.langgraph_orchestrator import run_pipeline

def handler(event, context):
    """
    AWS Lambda handler.
    Expected event: { "ticker": "AAPL" } or { "symbol": "AAPL" }
    """
    # support both "ticker" and "symbol"
    ticker = None
    if isinstance(event, dict):
        ticker = event.get("ticker") or event.get("symbol")
    ticker = ticker or "AAPL"

    try:
        result = run_pipeline(ticker)
        body = {
            "status": "ok",
            "result": result
        }
        return {"statusCode": 200, "body": json.dumps(body)}
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"status": "error", "message": str(e)})}
