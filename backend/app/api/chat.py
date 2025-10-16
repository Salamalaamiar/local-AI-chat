from fastapi import APIRouter
from app.models.chat_models import ChatRequest ,ChatResponse
from app.services.ollama_client import query_ollama

router=APIRouter(prefix="/chat")

#creates a POST endpoint at /chat/
@router.post("/",response_model=ChatResponse)
def chat(request:ChatRequest):
    reply=query_ollama(request.message)
    return ChatResponse(reply=reply)