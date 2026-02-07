from fastapi import FastAPI
from app.nlp.emotion_model import analyze_text

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Customer Sentiment Backend is running"}

@app.get("/analyze")
def analyze(text: str):
    return analyze_text(text)
