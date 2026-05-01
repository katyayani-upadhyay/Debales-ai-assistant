# 🤖 Debales AI Assistant

An intelligent chatbot built using LangGraph that answers queries about Debales AI using Retrieval-Augmented Generation (RAG) and handles external queries using a SERP API.

---

## 🚀 Features

* 🔍 **RAG-based answering** for Debales AI-related queries
* 🌐 **SERP API integration** for general/external queries
* 🔀 **Smart routing using LangGraph workflow**
* 🧠 **Multi-page web scraping** to build knowledge base
* 💻 Streamlit-based interactive UI
* ❌ **No hallucination fallback handling**
* ⚡ Clean, modular, and scalable code structure

---

## 🧱 Architecture

User Query
↓
LangGraph Router
↓            ↓
RAG        SERP API
↓            ↓
Final Response

---

## 📂 Project Structure

debales-ai-assistant/
│
├── app.py              # Main chatbot interface
├── graph.py            # LangGraph workflow logic
├── rag.py              # RAG pipeline (embeddings + vector DB)
├── scraper.py          # Web crawler for data collection
├── tools.py            # SERP API integration
│
├── data/
│   └── debales_docs.txt   # Scraped knowledge base
│
├── .env.example
├── requirements.txt
└── README.md

---

## ⚙️ Setup Instructions

### 1. Clone the repository

git clone <your-repo-link>
cd debales-ai-assistant

---

### 2. Create virtual environment

python -m venv venv
venv\Scripts\activate

---

### 3. Install dependencies

pip install -r requirements.txt

---

### 4. Add environment variables

Create a `.env` file in root directory:

SERP_API_KEY=your_serp_api_key

(Note: OpenAI key is optional if using HuggingFace embeddings)

---

### 5. Run scraper (build knowledge base)

python scraper.py

---

### 6. Run chatbot

python app.py

---

## 🧪 Example Queries

* What does Debales AI do?
* What is machine learning?
* Tell me about Debales AI and AI trends

---

## 🧠 Approach

* Built a **recursive crawler** to scrape multiple pages from the Debales AI website
* Extracted structured text (headings + paragraphs)
* Created embeddings using **HuggingFace models (free, no API required)**
* Stored data in **Chroma vector database**
* Designed a **LangGraph-based routing system** to decide:

  * Debales queries → RAG
  * External queries → SERP API
* Implemented **fallback handling** to avoid hallucinations

---

## 🎥 Demo

(Add your demo video link here)

---

## 💡 Future Improvements

* Add Streamlit UI for better user experience
* Improve query classification (semantic routing)
* Add conversation memory
* Hybrid search (keyword + vector search)

---

## 👩‍💻 Author

Katyayani Upadhyay

* Email: [katyayani1612@gmail.com](mailto:katyayani1612@gmail.com)
* LinkedIn: https://www.linkedin.com/in/katyayani-upadhyay
* GitHub: https://github.com/katyayani-upadhyay

---
