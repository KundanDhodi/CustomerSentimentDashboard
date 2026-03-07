from app.nlp.emotion_model import analyze_text

def analyze_multiple_emails(emails):

    results = []
    emotion_count = {}

    for email in emails:

        result = analyze_text(email)
        results.append(result)

        emotion = result["emotion"]

        if emotion not in emotion_count:
            emotion_count[emotion] = 0

        emotion_count[emotion] += 1

    dominant_emotion = max(emotion_count, key=emotion_count.get)

    return {
        "total_emails": len(emails),
        "dominant_emotion": dominant_emotion,
        "emotion_distribution": emotion_count,
        "individual_results": results
    }