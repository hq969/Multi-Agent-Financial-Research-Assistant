from orchestration.langgraph_orchestrator import run_pipeline
import argparse
import json

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ticker", "-t", default="AAPL", help="Ticker symbol to run pipeline for")
    args = parser.parse_args()

    out = run_pipeline(args.ticker)
    print("Pipeline output (JSON):")
    print(json.dumps(out, indent=2))
