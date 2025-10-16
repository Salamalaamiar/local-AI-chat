from fastapi import FastAPI
from app.api import chat


app=FastAPI(title="Local chat ai")

app.include_router(chat.router)
@app.get("/")
def root():
    return {"message":"Welcome to your local AI chat"}