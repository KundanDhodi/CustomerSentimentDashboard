# Customer Sentiment Dashboard

An AI-powered system that analyzes customer emails and detects emotions such as anger, joy, sadness, fear, surprise, and love.

The project helps businesses understand customer sentiment from email communication using Natural Language Processing (NLP).

---

## Features

- Emotion detection from customer emails
- Customer persona analysis
- Sentiment classification
- FastAPI backend for API services
- Docker support for easy deployment
- Testing with multiple email samples

---

## Technologies Used

- Python
- FastAPI
- HuggingFace Transformers
- DistilBERT
- Docker
- NLP (Natural Language Processing)

---

## Project Structure
customer-sentiment-dashboard
│
├── app
│ ├── main.py
│ ├── sentiment_routes.py
│ └── nlp
│ ├── emotion_model.py
│ ├── persona_model.py
│ └── email_analyzer.py
│
├── frontend
├── dataset
├── model
├── results
│
├── train_model.py
├── test_emotion.py
├── test_multiple.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt


---

## How to Run the Project

### Run Locally

Install dependencies:

pip install -r requirements.txt

Run FastAPI server:

uvicorn app.main:app --reload

Server runs on:

http://localhost:8000

---

### Run with Docker

Build and start container:

docker-compose up --build

---

## Example Email Input

"I am extremely disappointed with the service. The delay and lack of response from support is unacceptable."

Output:

Emotion: Anger

---

## Future Improvements

- Better Hinglish support
- Larger training dataset
- Improved emotion classification accuracy
- Visualization dashboard

---

## Author

Kundan Dhodi  
Diploma in Computer Engineering