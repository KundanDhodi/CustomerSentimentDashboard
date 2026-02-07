from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

MODEL_NAME = "bhadresh-savani/distilbert-base-uncased-emotion"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

model.eval()

labels = model.config.id2label


def analyze_text(text: str):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True
    )

    with torch.no_grad():
        outputs = model(**inputs)
        scores = torch.softmax(outputs.logits, dim=1)

    confidence, predicted_class = torch.max(scores, dim=1)

    return {
        "emotion": labels[predicted_class.item()],
        "confidence": round(confidence.item(), 3)
    }
