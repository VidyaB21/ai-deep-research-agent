# 🔎 AI Deep Research Agent

An AI-powered research assistant that automatically gathers information from the web and generates structured research reports with sources, confidence scoring, and downloadable reports.

This project demonstrates how **AI agents, retrieval systems, and information pipelines** can be combined to build an intelligent research assistant similar to modern AI search platforms.

---

# 🚀 Live Application

👉 **Try the deployed application**

https://vidyab21-ai-deep-research-agent-deep-research-agentapp-qigcur.streamlit.app/

---

# 🧠 Project Overview

AI Deep Research Agent is designed to simulate the behavior of an intelligent research assistant.
Instead of manually browsing multiple websites, users can enter a research topic and receive:

* structured explanation
* relevant sources
* research confidence score
* downloadable research report

The system uses a **multi-agent architecture** to process research queries through multiple stages including search, extraction, analysis, and report generation.

---

# ✨ Key Features

• 🔎 Automated research from online sources
• 📚 Source citation with clickable references
• 📊 Research confidence scoring system
• 🧾 Downloadable PDF research report
• 🧠 Multi-agent research architecture
• 🕘 Persistent research history tracking
• ⚡ Lightweight AI pipeline suitable for low-RAM systems
• 🎨 Modern Streamlit interface

---

# 🏗️ System Architecture

The system follows a **modular AI agent architecture**, where each component handles a specific responsibility in the research pipeline.

### Research Pipeline

User Query
↓
Query Expansion
↓
Web Search
↓
Content Scraping
↓
Text Chunking
↓
Semantic Retrieval
↓
Analysis Agent
↓
Evaluation Agent
↓
Report Generation
↓
PDF Export + UI Display

---

# 📂 Project Architecture

```
AI Deep Research Agent
│
├── app.py                        # Main Streamlit application
├── requirements.txt              # Project dependencies
│
├── agents                        # AI agent modules
│   ├── research_agent.py         # Research orchestration
│   ├── retrieval_agent.py        # Semantic retrieval
│   ├── analysis_agent.py         # Content analysis
│   ├── evaluation_agent.py       # Confidence scoring
│   └── report_agent.py           # Research report generation
│
├── utils                         # Core utilities
│   ├── search.py                 # Web search module
│   ├── scraper.py                # Web content extraction
│   ├── query_expansion.py        # Query enhancement
│   ├── keyword_extractor.py      # Keyword extraction
│   ├── chunking.py               # Text chunking
│   ├── embeddings.py             # Embedding generation
│   └── retrieval.py              # Vector similarity retrieval
│
├── memory                        # Research memory
│   ├── memory_manager.py         # Handles search history
│   └── history.json              # Stored queries
│
├── exports                       # Export utilities
│   └── pdf_export.py             # PDF report generator
│
└── research_report.pdf           # Example output
```

---

# ⚙️ Technology Stack

**Language**

Python

**Framework**

Streamlit

**Libraries**

* Wikipedia API
* BeautifulSoup
* Scikit-learn
* Sentence Transformers
* FPDF
* Requests

---

# 📷 Application Screenshots

### Desktop Interface

![Desktop UI](![alt text](image.png))

---

### Research Result in PDF View / confidence level View

![Research Output](![alt text](image-1.png))

---

### Mobile Interface

![Mobile UI](![alt text](image-2.png))

---

# ▶️ Installation Guide

Clone the repository

```
git clone https://github.com/YOUR_USERNAME/ai-deep-research-agent.git
```

Navigate to the project directory

```
cd ai-deep-research-agent
```

Install dependencies

```
pip install -r requirements.txt
```

Run the application

```
streamlit run app.py
```

The application will open automatically in your browser.

---

# 💡 Example Query

```
Machine Learning Basics
```

The system will generate:

• structured explanation
• source references
• research confidence score
• downloadable research report

---

# 🎯 Project Motivation

The goal of this project is to demonstrate how **AI-driven research assistants** can automate the process of gathering and summarizing information.

Instead of manually exploring multiple sources, users can quickly obtain structured research insights through a unified interface.

---

# 🔮 Future Improvements

Possible enhancements for the system include:

• Integration with multiple search engines (Google / DuckDuckGo)
• Advanced LLM summarization
• Knowledge graph generation
• Vector database integration (FAISS / Pinecone)
• Chat-style conversational research interface
• Multi-document reasoning
• Improved ranking of research sources
• Research topic visualization

---

# 🧑‍💻 Author

Developed as part of a practical exploration into **AI application development, research automation, and intelligent agent systems**.

---



