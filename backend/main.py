from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os
import re
import string
import numpy as np
from nltk.corpus import stopwords
import nltk
from datetime import datetime
from pymongo import MongoClient

# Download stopwords (only first run)
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

# FastAPI app
app = FastAPI(title="Fake News Detection API")

# MongoDB Setup (local)
#client = MongoClient("mongodb://localhost:27017/")
import os
mongo_url = os.getenv("MONGO_URL", "mongodb://localhost:27017/")
client = MongoClient(mongo_url)

db = client["fake_news_db"]
collection = db["predictions"]

# Model paths
MODEL_DIR = "model"
MODEL_PATH = os.path.join(MODEL_DIR, "model.pkl")
VECT_PATH = os.path.join(MODEL_DIR, "vectorizer.pkl")

# Load model + vectorizer
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECT_PATH)

# Label map
label_map = {
    0: "REAL",
    1: "FAKE"
}

class NewsItem(BaseModel):
    text: str

# Text cleaning
def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\d+", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

@app.get("/")
def read_root():
    return {"message": "Fake News Detection API is running."}

@app.post("/predict")
def predict(news: NewsItem):
    cleaned = clean_text(news.text)
    X = vectorizer.transform([cleaned])

    try:
        probs = model.predict_proba(X)[0]
        pred_idx = int(np.argmax(probs))
        confidence = float(np.max(probs))
    except AttributeError:
        pred_idx = int(model.predict(X)[0])
        confidence = None

    label = label_map.get(pred_idx, pred_idx)

    result = {
        "text": news.text,
        "prediction": label,
        "label_index": pred_idx,
        "confidence": confidence,
        "timestamp": datetime.utcnow()
    }

    # Store in MongoDB
    collection.insert_one(result)

    return {
        "prediction": label,
        "label_index": pred_idx,
        "confidence": confidence
    }
