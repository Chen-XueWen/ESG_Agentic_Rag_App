# 🌱 ESG Agentic RAG App

This is a multi-agent AI system that:
- Automatically scrapes ESG-related news for any company
- Indexes that content into a vector database (Chroma)
- Uses agents (Environment, Social, Governance) to evaluate performance
- Aggregates scores into a final explainable ESG report
- Uses LLaMA 3.2 (local model)

## 🏗 Folder Structure
```
esg_agentic_rag_app/
├── app.py              # Streamlit frontend
├── agents.py           # ESG agent logic (Env/Soc/Gov/Aggregator)
├── vector_store.py     # Chroma DB setup
├── retriever.py        # LangChain retriever interface
├── news_scraper.py     # Google-based ESG news extractor
├── esg_docs/           # Temporary ESG .txt files
├── chroma_db/          # Persisted vector database
├── requirements.txt    # Pip dependencies
└── README.md           # Project overview
```

## 🚀 How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🧠 Features
- Scrapes real news for ESG grounding
- Uses LangChain + Chroma for retrieval
- Chain-of-thought LLaMA reasoning
- Fully local, transparent, and modifiable
