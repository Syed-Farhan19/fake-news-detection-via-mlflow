import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")

client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]

def store_prediction(input_text, prediction, confidence):
    document = {
        "input_text": input_text,
        "prediction": prediction,
        "confidence": confidence
    }
    collection.insert_one(document)
