from fastapi import APIRouter
from app.nlp.email_analyzer import analyze_multiple_emails

router = APIRouter()

@router.post("/analyze-emails")
def analyze_emails(data: dict):

    emails = data.get("emails", [])

    result = analyze_multiple_emails(emails)

    return result