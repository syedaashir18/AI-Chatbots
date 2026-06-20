# AI-Chatbots
# 🤖 AI Chatbots Collection
RAG based AI Chatbots using LangChain and Groq
A collection of intelligent AI chatbots built using 
Retrieval-Augmented Generation (RAG) and modern LLM technologies.

## 📌 Projects

| # | Project | Description | Notebook |
|---|---------|-------------|----------|
| 1 | Pakistan Air Force Chatbot | RAG chatbot about PAF using Wikipedia data | [Open](./pakistan-airforce-chatbot.ipynb) |

> More chatbots coming soon...

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| LangChain | RAG Framework |
| ChromaDB | Vector Database |
| Groq LLM | Language Model (Free) |
| HuggingFace | Embeddings Model |
| Google Colab | Development Environment |

## 📚 What is RAG?

RAG (Retrieval-Augmented Generation) works in 2 phases:

**Phase 1 — Indexing:**
1. Load documents (PDF, text, web)
2. Split into chunks
3. Convert to vectors (embeddings)
4. Store in vector database

**Phase 2 — Query:**
1. User asks a question
2. Question converted to vector
3. Similar chunks retrieved
4. LLM generates answer from context

## 🚀 How to Run Any Chatbot

1. Open notebook in Google Colab
2. Run Cell 1 — Install dependencies
3. Run Cell 2 — Upload your document
4. Run remaining cells in order
5. Ask questions in chat UI

## 📁 Project Structure
ai-chatbots/

├── pakistan-airforce-chatbot.ipynb

└── README.md
## 🔗 Connect
Made by Syed Aashir
