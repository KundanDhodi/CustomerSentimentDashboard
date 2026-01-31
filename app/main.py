from fastapi import FastAPI
from app.nlp.dummy import analyze_text

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from Docker "}

@app.get("/analyze")
def analyze(text: str):
    return analyze_text(text)
