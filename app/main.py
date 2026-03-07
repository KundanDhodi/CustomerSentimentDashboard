from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.nlp.emotion_model import analyze_text
from app.nlp.persona_model import predict_persona
from app.nlp.email_analyzer import analyze_multiple_emails

app = FastAPI()

# Enable CORS so frontend (index.html) can call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Customer Sentiment Backend is running"}


# Single Email Analysis
@app.get("/analyze")
def analyze(text: str):

    # Persona prediction
    real_persona, email_style, persona_confidence = predict_persona(text)

    # Emotion prediction
    emotion_result = analyze_text(text)

    return {
        "real_persona_prediction": real_persona,
        "persona_confidence": persona_confidence,
        "email_style": email_style,
        "emotion_result": emotion_result
    }


# Multiple Email Analysis (Mentor Requirement)
@app.post("/analyze-emails")
def analyze_emails(data: dict):

    emails = data.get("emails", [])

    result = analyze_multiple_emails(emails)

    return result