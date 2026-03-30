from fastapi import FastAPI
import fastapi
from pydantic import BaseModel
from app.services.retrieval_service import retrieve_documents

app = FastAPI()

class QueryRequest(BaseModel):
    query: str


@app.post("/ask")
def ask_question(request: QueryRequest):
    docs = retrieve_documents(request.query)

    relevant_docs = "\n".join([obj.page_content for obj in docs])
    
    return {
        "question" : request.query,
        "retrieved_documents" : relevant_docs
    }

#uvicorn app.main:app --reload