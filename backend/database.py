import os
from pathlib import Path
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Find .env inside backend folder
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

uri = os.getenv("MONGO_URI")

print("Mongo URI loaded:", uri[:20] if uri else "None")
if not uri:
    raise Exception("MONGO_URI not found!")

client = MongoClient(uri, server_api=ServerApi("1"))

try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("MongoDB connection error:", e)

db = client["Student-career-platform"]
student_collection = db["std"]