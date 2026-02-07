from app.nlp.emotion_model import analyze_text

if __name__ == "__main__":
    text = "I am very happy today"
"I am furious with this company"
"This was unexpected"
result = analyze_text(text)
print(result)
