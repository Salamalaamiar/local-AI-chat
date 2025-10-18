from fastapi import FastAPI
from app.api import chat
from fastapi.middleware.cors import CORSMiddleware


app=FastAPI(title="Local chat ai")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], #for dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

app.include_router(chat.router)
@app.get("/")
def root():
    return {"message":"Welcome to your local AI chat"}