# Agentic RAG Chatbot

An Agentic Retrieval-Augmented Generation (RAG) chatbot built using FastAPI, LangChain, ChromaDB, and OpenAI.

## Features

- Upload PDFs
- Ingest Website URLs
- ChromaDB Vector Database
- Agent decides when to retrieve information
- Chat Interface
- FastAPI Backend
- Source Citations
- Conversation Memory

## Project Structure

```
agentic-rag/
│
├── backend/
├── frontend/
├── data/
├── requirements.txt
├── .env.example
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn backend.main:app --reload
```

Open:

http://127.0.0.1:8000
