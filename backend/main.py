from fastapi import FastAPI, HTTPException
from backend.database import student_collection
from backend.models import Student
from bson import ObjectId
from backend.career_data import recommend_careers

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Student career platform is running"}


@app.post("/student")
def create_student(student: Student):
    result = student_collection.insert_one(student.model_dump())

    return {
        "message": "Student inserted successfully!",
        "id": str(result.inserted_id)
    }
@app.post("/students/bulk")
def create_students(students: list[Student]):

    student_data = [
        student.model_dump()
        for student in students
    ]

    result = student_collection.insert_many(student_data)

    return {
        "message": "Students inserted successfully!",
        "count": len(result.inserted_ids),
        "ids": [str(student_id) for student_id in result.inserted_ids]
    }

@app.get("/student")
def get_students():
    students = list(student_collection.find())

    for student in students:
        student["_id"] = str(student["_id"])

    return students


@app.delete("/student/{student_id}")
def delete_student(student_id: str):
    result = student_collection.delete_one(
        {"_id": ObjectId(student_id)}
    )

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message": "Student deleted successfully!"
    }


@app.put("/student/{student_id}")
def update_student(student_id: str, student: Student):
    result = student_collection.update_one(
        {"_id": ObjectId(student_id)},
        {"$set": student.model_dump()}
    )

    if result.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message": "Student updated successfully!"
    }
@app.get("/student/search/{name}")
def search_student(name: str):
    students = list(
        student_collection.find(
            {"name": {"$regex": name, "$options": "i"}}
        )
    )

    for student in students:
        student["_id"] = str(student["_id"])

    return students

@app.get("/career/recommend/{student_id}")
def career_recommend(student_id: str):

    student = student_collection.find_one({
        "_id": ObjectId(student_id)
    })

    if not student:
        return {
            "message": "Student not found"
        }

    result = recommend_careers(
        student["skills"]
    )

    return {
        "student": student["name"],
        "best_career": result["best_career"],
        "recommendation_reason": result[
            "recommendation_reason"
        ],
        "recommendations": result[
            "recommendations"
        ]
    }