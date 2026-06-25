from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from agent import agent_response
from ingest import ingest_url

app = FastAPI(title="Agentic RAG Chatbot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    query: str

class UrlRequest(BaseModel):
    url: str

@app.get("/")
def home():
    return {
        "message": "Agentic RAG API Running Successfully"
    }

@app.post("/chat")
def chat(request: ChatRequest):
    answer = agent_response(request.query)
    return {
        "query": request.query,
        "answer": answer
    }

@app.post("/ingest")
def ingest(request: UrlRequest):
    ingest_url(request.url)
    return {
        "message": "URL added successfully"
    }
