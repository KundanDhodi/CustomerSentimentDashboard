from app.nlp.email_analyzer import analyze_multiple_emails

emails = [
    "I am extremely angry about the delay in your service",
    "This is the worst experience I have had",
    "Thank you for solving my issue quickly",
    "I am frustrated with your response time",
    "I appreciate your support team"
]

result = analyze_multiple_emails(emails)

print(result)