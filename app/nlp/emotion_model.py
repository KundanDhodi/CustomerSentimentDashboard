from transformers import pipeline

emotion_classifier = pipeline(
    "text-classification",
    model="./model",
    tokenizer="./model",
    top_k=None
)

label_map = {
    "LABEL_0": "anger",
    "LABEL_1": "fear",
    "LABEL_2": "joy",
    "LABEL_3": "love",
    "LABEL_4": "sadness",
    "LABEL_5": "surprise"
}

def analyze_text(text: str):

    result = emotion_classifier(text)[0]

    emotions = {}

    for r in result:
        emotions[label_map[r["label"]]] = r["score"]

    dominant_emotion = max(emotions, key=emotions.get)
    confidence = emotions[dominant_emotion]

    return {
        "emotion": dominant_emotion,
        "confidence": round(confidence, 3),
        "scores": emotions
    }