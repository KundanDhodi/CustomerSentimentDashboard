from app.nlp.emotion_model import analyze_text

text = "I am very angry about the delay in your service"

result = analyze_text(text)

print(result)