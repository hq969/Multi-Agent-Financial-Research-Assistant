# 📊 Multi-Agent Financial Research Assistant

A serverless, AI-powered assistant for financial research that fetches live market news and data, performs sentiment analysis, and generates investor-friendly reports. Built with **LangGraph**, **LangChain**, **Streamlit**, **AWS Lambda**, and **DynamoDB**.

---

## 🚀 Features
- **Agent A**: Fetches live market news & stock data via APIs.
- **Agent B**: Summarizes text and performs sentiment analysis.
- **Agent C**: Generates investor-friendly insights and reports using GPT-4.
- **LangGraph Orchestration**: Manages agent workflows.
- **AWS Lambda + DynamoDB**: Enables serverless execution & persistence.
- **Streamlit Dashboard**: User-friendly interface for exploring insights.

---

## 📂 Project Structure
```
├── agents
│   ├── agent_a_fetcher.py      # Fetch live financial data & news
│   ├── agent_b_analyzer.py     # Summarization & sentiment analysis
│   └── agent_c_reporter.py     # Report generation
├── orchestration
│   └── langgraph_orchestrator.py   # Orchestrates agent workflows
├── lambda
│   └── lambda_handler.py       # AWS Lambda handler
├── utils
│   └── dynamo.py               # DynamoDB helper functions
├── streamlit_app.py            # Streamlit dashboard
├── run_local.py                # Local runner for development
├── requirements.txt            # Python dependencies
├── .env.example                # Example environment variables
└── README.md                   # Project documentation
```

---

## ⚙️ Setup
### 1. Clone Repository
```bash
git clone https://github.com/hq969/multi-agent-financial-assistant.git
cd multi-agent-financial-assistant
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Copy `.env.example` to `.env` and update with your credentials:
```bash
OPENAI_API_KEY=your-openai-api-key
NEWS_API_KEY=your-newsapi-key
MARKET_API_KEY=your-alpha-vantage-key
DYNAMO_TABLE=FinancialReports
```

---

## ▶️ Usage
### Run Locally
```bash
python run_local.py
```

### Streamlit Dashboard
```bash
streamlit run streamlit_app.py
```
Then open [http://localhost:8501](http://localhost:8501) in your browser.

### Deploy to AWS Lambda
- Package with dependencies.
- Set environment variables in Lambda.
- Ensure DynamoDB table exists (`FinancialReports`).
- Deploy handler: `lambda/lambda_handler.lambda_handler`.

---

## 📊 Example Workflow
1. Agent A fetches **stock news + financial data**.
2. Agent B generates a **summary + sentiment analysis**.
3. Agent C compiles **reports for investors**.
4. Orchestrator pipelines results to **DynamoDB & UI**.

---

## 🛠️ Tech Stack
- **Frontend**: Streamlit
- **Backend**: AWS Lambda (Python)
- **Data Storage**: DynamoDB
- **AI/LLM**: OpenAI GPT-4 via LangChain
- **Workflow**: LangGraph
- **APIs**: NewsAPI, Alpha Vantage

---

## ✅ Next Steps
- Add **unit tests** in a `tests/` folder.
- Create **CI/CD pipeline** for Lambda + Streamlit.
- Add **Mermaid architecture diagram** to README.

---

## 👨‍💻 Author
Built by Harsh Sonkar ⚡

---

