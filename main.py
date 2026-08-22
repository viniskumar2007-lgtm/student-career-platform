from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Student career platform is running!"}
@app.get("/student")
def get_student():
    return {"name": "Vinith S",
             "age": 18, 
             "major": "CSE","year":2
             }