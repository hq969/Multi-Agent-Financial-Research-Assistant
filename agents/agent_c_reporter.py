import os
from typing import List, Dict, Any

# Use LangChain ChatOpenAI wrapper. If you prefer raw OpenAI client, swap accordingly.
try:
    from langchain.chat_models import ChatOpenAI
    from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
except Exception:
    ChatOpenAI = None  # graceful fallback for environments without langchain

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def _build_prompt(ticker: str, market_snapshot: Dict[str, Any], analyzed_articles: List[Dict[str, Any]]) -> str:
    articles_text = ""
    for a in analyzed_articles[:6]:
        title = a.get("title", "")
        polarity = a.get("sentiment", {}).get("polarity", 0)
        summary = a.get("summary", "")
        articles_text += f"- {title}\n  Sentiment: {polarity}\n  Summary: {summary}\n\n"

    prompt = f"""
You are a professional financial analyst assistant.

Ticker: {ticker}
Market snapshot: {market_snapshot}

Recent news (top items):
{articles_text}

Task:
1) Produce a concise investor-friendly 6-bullet summary (each bullet 1-2 sentences).
2) Provide an 'Actionability' section (what investors might watch next).
3) Provide a 2-line risk summary.

Use plain language, no marketing fluff, and keep it short.
"""
    return prompt

def generate_insight_report(ticker: str, market_snapshot: Dict[str, Any], analyzed_articles: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Generate a report using GPT-4 via LangChain ChatOpenAI if available.
    Returns dict { report: str }
    """
    prompt_text = _build_prompt(ticker, market_snapshot, analyzed_articles)

    if ChatOpenAI:
        llm = ChatOpenAI(model_name="gpt-4", temperature=0.0, openai_api_key=OPENAI_API_KEY)
        # Use a simple text prompt call. Different langchain versions vary APIs.
        try:
            # Try ChatOpenAI.predict if available
            resp = llm.predict(prompt_text)
            return {"report": resp}
        except Exception:
            # fallback to calling as __call__ with messages
            try:
                from langchain.schema import HumanMessage
                resp = llm([HumanMessage(content=prompt_text)])
                if hasattr(resp, "content"):
                    return {"report": resp.content}
                return {"report": str(resp)}
            except Exception as e:
                return {"report": f"LLM call failed: {e}\n\nPrompt:\n{prompt_text}"}
    else:
        # No LangChain installed — return a placeholder
        return {"report": "LangChain / ChatOpenAI not available in environment. Prompt:\n\n" + prompt_text}
