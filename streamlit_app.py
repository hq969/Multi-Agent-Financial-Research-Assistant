import streamlit as st
from utils.dynamo import query_by_pk
from orchestration.langgraph_orchestrator import run_pipeline
import os

st.set_page_config(page_title="Multi-Agent Financial Research Assistant", layout="wide")
st.title("📊 Multi-Agent Financial Research Assistant")

col1, col2 = st.columns([2, 1])
with col1:
    ticker = st.text_input("Ticker / Symbol", value="AAPL")
with col2:
    run_now = st.button("Run Pipeline (local)")

if run_now:
    with st.spinner("Running pipeline..."):
        item = run_pipeline(ticker)
        st.success("Pipeline run complete — persisted to DynamoDB (if configured).")
        st.json(item)

st.markdown("---")
st.header("Saved Reports (DynamoDB)")
pk = f"TICKER#{ticker}"
try:
    items = query_by_pk(pk)
except Exception as e:
    st.error(f"Failed to query DynamoDB: {e}")
    items = []

if not items:
    st.info("No saved reports found for this ticker. Run the pipeline to generate a report.")
else:
    # show latest 5
    for it in sorted(items, key=lambda x: x.get("sk", ""), reverse=True)[:5]:
        st.subheader(it.get("sk"))
        st.write("Market snapshot:")
        st.json(it.get("market", {}))
        st.write("Report:")
        st.text(it.get("report", ""))
