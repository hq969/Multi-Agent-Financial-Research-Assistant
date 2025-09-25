from textblob import TextBlob
from typing import List, Dict, Any
import re

def _split_sentences(text: str) -> List[str]:
    # very simple splitter
    text = re.sub(r'\s+', ' ', (text or '')).strip()
    if not text:
        return []
    # split on period/question/exclamation
    parts = re.split(r'(?<=[.!?])\s+', text)
    return [p.strip() for p in parts if p.strip()]

def summarize_text(text: str, max_sentences: int = 3) -> str:
    """
    Naive summarizer: selects the first max_sentences sentences.
    For better results, replace with an LLM-based summarization.
    """
    sents = _split_sentences(text)
    if not sents:
        return ""
    summary = " ".join(sents[:max_sentences])
    return summary

def sentiment_score(text: str) -> Dict[str, float]:
    """
    Uses TextBlob to compute polarity and subjectivity.
    polarity: -1.0 (negative) to +1.0 (positive)
    subjectivity: 0.0 (objective) to 1.0 (subjective)
    """
    tb = TextBlob(text or "")
    return {
        "polarity": round(tb.sentiment.polarity, 4),
        "subjectivity": round(tb.sentiment.subjectivity, 4)
    }

def analyze_articles(articles: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    For each article produce a short summary and sentiment.
    """
    out = []
    for a in articles:
        title = a.get("title") or ""
        description = a.get("description") or ""
        content = a.get("content") or ""
        combined = " ".join([title, description, content]).strip()
        summary = summarize_text(combined, max_sentences=2)
        sentiment = sentiment_score(combined)
        out.append({
            "title": title,
            "summary": summary,
            "sentiment": sentiment,
            "source": a.get("source"),
            "url": a.get("url"),
            "publishedAt": a.get("publishedAt")
        })
    return out
