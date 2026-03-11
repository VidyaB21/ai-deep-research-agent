# 🔎 AI Deep Research Agent

An AI-powered research assistant that automatically retrieves information from the web and generates structured research summaries with sources, confidence scoring, and downloadable reports.

This project demonstrates how **AI agents can combine information retrieval with language models** to create a lightweight research assistant similar to modern AI search systems.

---

# 🚀 Features

* 🔎 **Automated Web Research** – retrieves information from Wikipedia
* 🤖 **AI Generated Answers** – generates structured research summaries
* 📚 **Source Citations** – displays links used in the research
* 📊 **Research Confidence Score** – estimates reliability of results
* 🧾 **PDF Export** – download research report as a PDF
* 🕘 **Search History Sidebar** – keeps track of previous queries
* 🎨 **Modern Streamlit UI** – simple and interactive interface
* ⚡ **Lightweight Design** – optimized for low-RAM laptops

---

# 🧠 How It Works

The system follows a simple **AI research pipeline**:

User Query
↓
Wikipedia Retrieval
↓
Content Extraction
↓
Answer Generation
↓
Research Report + Sources + Confidence Score

The assistant retrieves information from Wikipedia and processes the content to generate a readable research explanation.

---

# 🖥️ Tech Stack

* **Python**
* **Streamlit**
* **Wikipedia API**
* **FPDF** (PDF export)
* **Scikit-learn**
* **Sentence Transformers**

---

🧠 System Architecture

The AI Deep Research Agent is designed using a modular multi-agent architecture that separates responsibilities into independent components.
This approach improves scalability, maintainability, and extensibility.

The system consists of multiple agents responsible for different stages of the research pipeline.

Architecture Flow
User Query
   │
   ▼
Query Expansion
   │
   ▼
Web Search + Scraping
   │
   ▼
Content Chunking
   │
   ▼
Embedding Generation
   │
   ▼
Vector Retrieval
   │
   ▼
Analysis Agent
   │
   ▼
Evaluation Agent
   │
   ▼
Report Generation
   │
   ▼
PDF Export + UI Display
```

---

# ⚙️ Installation

Clone the repository

```
git clone https://github.com/YOUR_USERNAME/ai-deep-research-agent.git
```

Move into the project folder

```
cd ai-deep-research-agent
```

Install dependencies

```
pip install -r requirements.txt
```

---

# ▶️ Run the Application

Start the Streamlit app

```
streamlit run app.py
```

The application will open in your browser.

---

# 💡 Example Query

```
Machine Learning Basics
```

Output includes:

* AI generated explanation
* Source links
* Research confidence score
* Downloadable PDF report

---

📷 Application Preview

![WhatsApp Image 2026-03-12 at 2 26 34 AM](https://github.com/user-attachments/assets/3fdac560-38d7-445e-87b0-d8b5edcc990e)
![WhatsApp Image 2026-03-12 at 2 26 34 AM](https://github.com/user-attachments/assets/3fdac560-38d7-445e-87b0-d8b5edcc990e)
-----
## 🚀 Live Application

You can access the deployed application here:

👉 [https://vidyab21-ai-deep-research-agent-deep-research-agentapp-qigcur.streamlit.app/]

Example:

assets/app-preview.png

Then include:

!<img width="1868" height="877" alt="Screenshot 2026-03-12 014728" src="https://github.com/user-attachments/assets/e763d1fb-1e48-4f3d-a6e5-6cbf3ccb33c1" />
<img width="1868" height="877" alt="Screenshot 2026-03-12 014728" src="https://github.com/user-attachments/assets/e763d1fb-1e48-4f3d-a6e5-6cbf3ccb33c1" />
(assets/app-preview.png)
```

---

# 🎯 Project Purpose

This project was built to demonstrate how **AI agents can combine information retrieval and natural language generation to assist research tasks**.

It is designed as a **portfolio project for learning AI application development using Python and Streamlit**.

---
📂 Project Architecture

ai-deep-research-agent
│
├── app.py                     # Main Streamlit application
├── requirements.txt           # Project dependencies
│
├── agents                     # Core AI agents
│   ├── research_agent.py      # Coordinates research pipeline
│   ├── retrieval_agent.py     # Handles document retrieval
│   ├── analysis_agent.py      # Analyzes retrieved information
│   ├── evaluation_agent.py    # Evaluates reliability of sources
│   └── report_agent.py        # Generates final research report
│
├── utils                      # Core utility modules
│   ├── search.py              # Web search engine
│   ├── scraper.py             # Extracts text from web pages
│   ├── query_expansion.py     # Expands user queries
│   ├── keyword_extractor.py   # Extracts important keywords
│   ├── chunking.py            # Splits text into smaller chunks
│   ├── embeddings.py          # Creates vector embeddings
│   └── retrieval.py           # Semantic retrieval logic
│
├── memory                     # Persistent memory storage
│   ├── memory_manager.py      # Handles research history
│   └── history.json           # Stored search history
│
├── exports                    # Export utilities
│   └── pdf_export.py          # Generate downloadable research PDF
│
├── research_report.pdf        # Generated report example
│
└── venv                       # Virtual environment (ignored in Git)

------

# 🔮 Future Improvements

Possible upgrades:

* Multi-source web search (Google / DuckDuckGo)
* Chat-style AI interface
* Better ranking of sources
* Advanced summarization models
* Cloud deployment with database storage

---

# 👨‍💻 Author

Developed as part of an AI learning journey focused on building practical AI applications.
