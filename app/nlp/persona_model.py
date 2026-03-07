import re

PERSONA_KEYWORDS = {
    "Dominant Extrovert": {
        "keywords": ["immediately", "unacceptable", "asap", "fix this", "right now", "seriously reconsider"],
        "weight": 2
    },
    "Emotional Sensitive": {
        "keywords": ["i feel", "hurt", "upset", "disappointed", "sad", "deeply"],
        "weight": 2
    },
    "Logical Thinker": {
        "keywords": ["according to", "timeline", "data", "evidence", "as discussed", "metrics"],
        "weight": 2
    },
    "Friendly Social": {
        "keywords": ["hey", "thanks", "appreciate", "just wanted", "hope you're well"],
        "weight": 1.5
    },
    "Calm Introvert": {
        "keywords": ["perhaps", "i think", "maybe", "could you", "would appreciate"],
        "weight": 1.5
    }
}


def predict_persona(email_text: str):
    text = email_text.lower()
    scores = {}

    for persona, config in PERSONA_KEYWORDS.items():
        score = 0
        for keyword in config["keywords"]:
            occurrences = len(re.findall(rf"\b{re.escape(keyword)}\b", text))
            score += occurrences * config["weight"]
        scores[persona] = score

    # Normalize scores
    total_score = sum(scores.values())
    if total_score == 0:
        return "Neutral Professional", "Balanced Formal", 0.0

    # Get best persona
    predicted_persona = max(scores, key=scores.get)
    confidence = scores[predicted_persona] / total_score

    # Map persona to email style
    persona_style_map = {
        "Dominant Extrovert": "Assertive Professional",
        "Emotional Sensitive": "Expressive Emotional",
        "Logical Thinker": "Structured Analytical",
        "Friendly Social": "Casual Friendly",
        "Calm Introvert": "Polite Professional"
    }

    email_style = persona_style_map.get(predicted_persona, "Balanced Formal")

    return predicted_persona, email_style, round(confidence, 2)