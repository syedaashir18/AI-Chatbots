# 🤖 AI Chatbots Collection

RAG based AI Chatbots using LangChain and Groq LLM.

A collection of intelligent AI chatbots built using Retrieval-Augmented Generation (RAG) and modern LLM technologies. Each chatbot is trained on real data and deployed with a proper web interface.

---

## 📌 Projects

| # | Project | Description | Notebook |
|---|---------|-------------|----------|
| 1 | 🛩️ Pakistan Air Force Chatbot | RAG chatbot about PAF — history, aircraft, operations & more | [Open Notebook](./paf-chatbot.ipynb) |
| 2 | 🏦 HBL Bank Customer Support | RAG chatbot for HBL bank customer queries | Coming Soon |

> More chatbots coming soon...

---

## ✨ Features

- 📄 Real data ingestion (Wikipedia, websites, PDFs)
- 🔍 Semantic search using FAISS vector database
- 🧠 MMR retrieval for diverse and accurate results
- 💬 Chat history — bot remembers previous messages
- 🌐 Streamlit web interface
- ⚡ Fast responses using Groq LLM (Free)

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| LangChain | RAG Framework |
| FAISS | Vector Database |
| Groq LLM (Llama 3.3 70B) | Language Model (Free) |
| HuggingFace Embeddings | Text to Vector Conversion |
| Streamlit | Web Interface |
| Cloudflare Tunnel | Public URL (Free) |
| Google Colab | Development Environment |

---

## 📚 What is RAG?

RAG (Retrieval-Augmented Generation) is an AI technique that combines document retrieval with language generation.

**Phase 1 — Indexing (done once):**
1. Load documents (Wikipedia, websites, PDFs)
2. Split into smaller chunks
3. Convert chunks to vectors (embeddings)
4. Store vectors in FAISS database

**Phase 2 — Query (every user message):**
1. User asks a question
2. Question converted to vector
3. Most similar chunks retrieved from database
4. LLM generates answer using retrieved context

**Key benefit:** Bot only answers from your documents — no hallucination!

---

## 🚀 How to Run

1. Open notebook in Google Colab
2. Run **Runtime → Run All**
3. Wait for Cloudflare tunnel URL
4. Open URL in browser
5. Start chatting!

---

## 📁 Project Structure
AI-Chatbots/

├── paf-chatbot.ipynb   ← Pakistan Air Force Chatbot

└── README.md
---

## 📊 Performance

| Metric | Value |
|--------|-------|
| Data Sources | Wikipedia (3+ articles) |
| Total Data | 294,000+ characters |
| Chunks | 300+ |
| Retrieval Method | MMR (Maximum Marginal Relevance) |
| LLM | Llama 3.3 70B via Groq |
| Response Time | ~2-3 seconds |

---

## 🔗 Connect

**Made by Syed Aashir**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://linkedin.com/in/syedaashir18)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/syedaashir18)
