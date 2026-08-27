from fastapi import FastAPI, HTTPException
from backend.database import student_collection
from backend.models import Student
from bson import ObjectId
from backend.career_data import (
    recommend_careers,
    get_career_by_name
)


app = FastAPI()


# =========================================================
# HOME
# =========================================================

@app.get("/")
def home():

    return {
        "message": "Student career platform is running"
    }


# =========================================================
# CREATE ONE STUDENT
# =========================================================

@app.post("/student")
def create_student(student: Student):

    result = student_collection.insert_one(
        student.model_dump()
    )

    return {
        "message": "Student inserted successfully!",
        "id": str(result.inserted_id)
    }


# =========================================================
# CREATE MULTIPLE STUDENTS
# =========================================================

@app.post("/students/bulk")
def create_students(students: list[Student]):

    student_data = [
        student.model_dump()
        for student in students
    ]

    result = student_collection.insert_many(
        student_data
    )

    return {
        "message": "Students inserted successfully!",
        "count": len(result.inserted_ids),
        "ids": [
            str(student_id)
            for student_id in result.inserted_ids
        ]
    }


# =========================================================
# GET ALL STUDENTS
# =========================================================

@app.get("/student")
def get_students():

    students = list(
        student_collection.find()
    )

    for student in students:

        student["_id"] = str(
            student["_id"]
        )

    return students


# =========================================================
# DELETE STUDENT
# =========================================================

@app.delete("/student/{student_id}")
def delete_student(student_id: str):

    try:

        object_id = ObjectId(student_id)

    except Exception:

        raise HTTPException(
            status_code=400,
            detail="Invalid student ID"
        )

    result = student_collection.delete_one(
        {
            "_id": object_id
        }
    )

    if result.deleted_count == 0:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message": "Student deleted successfully!"
    }


# =========================================================
# UPDATE STUDENT
# =========================================================

@app.put("/student/{student_id}")
def update_student(
    student_id: str,
    student: Student
):

    try:

        object_id = ObjectId(student_id)

    except Exception:

        raise HTTPException(
            status_code=400,
            detail="Invalid student ID"
        )

    result = student_collection.update_one(
        {
            "_id": object_id
        },
        {
            "$set": student.model_dump()
        }
    )

    if result.matched_count == 0:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message": "Student updated successfully!",
        "matched": result.matched_count,
        "modified": result.modified_count,
        "data_sent": student.model_dump()
    }


# =========================================================
# SEARCH STUDENT BY NAME
# =========================================================

@app.get("/student/search/{name}")
def search_student(name: str):

    students = list(
        student_collection.find(
            {
                "name": {
                    "$regex": name,
                    "$options": "i"
                }
            }
        )
    )

    for student in students:

        student["_id"] = str(
            student["_id"]
        )

    return students


# =========================================================
# CAREER RECOMMENDATION
# =========================================================

@app.get("/career/recommend/{student_id}")
def career_recommend(student_id: str):

    # -----------------------------------------------------
    # Check student ID
    # -----------------------------------------------------

    try:

        object_id = ObjectId(student_id)

    except Exception:

        raise HTTPException(
            status_code=400,
            detail="Invalid student ID"
        )

    # -----------------------------------------------------
    # Find student
    # -----------------------------------------------------

    student = student_collection.find_one(
        {
            "_id": object_id
        }
    )

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    # -----------------------------------------------------
    # Get career recommendations
    # -----------------------------------------------------

    result = recommend_careers(
        student.get("skills", [])
    )

    # -----------------------------------------------------
    # Get career goal
    # -----------------------------------------------------

    career_goal = student.get(
        "career_goal",
        ""
    )

    # -----------------------------------------------------
    # Get best career
    # -----------------------------------------------------

    best_career = result["best_career"]

    # -----------------------------------------------------
    # Find student's goal career
    # -----------------------------------------------------

    goal_career_data = get_career_by_name(
        career_goal
    )

    # -----------------------------------------------------
    # Default goal values
    # -----------------------------------------------------

    goal_match_percentage = 0
    goal_missing_skills = []
    goal_matched_skills = []

    # -----------------------------------------------------
    # Calculate goal career match
    # -----------------------------------------------------

    if goal_career_data:

        required_skills = goal_career_data[
            "skills"
        ]

        student_skills = student.get(
            "skills",
            []
        )

        student_skills_set = set(
            student_skills
        )

        # Matched skills
        goal_matched_skills = [
            skill
            for skill in required_skills
            if skill in student_skills_set
        ]

        # Missing skills
        goal_missing_skills = [
            skill
            for skill in required_skills
            if skill not in student_skills_set
        ]

        # Calculate percentage
        if len(required_skills) > 0:

            goal_match_percentage = round(
                (
                    len(goal_matched_skills)
                    / len(required_skills)
                ) * 100,
                2
            )

    # -----------------------------------------------------
    # Compare goal with best recommendation
    # -----------------------------------------------------

    goal_match = (
        career_goal.lower()
        == best_career.lower()
    )

    # -----------------------------------------------------
    # Create goal analysis
    # -----------------------------------------------------

    if goal_match:

        goal_analysis = (
            f"Your current skills match "
            f"your career goal {career_goal}."
        )

    else:

        if goal_career_data:

            missing_skills = ", ".join(
                goal_missing_skills
            )

            goal_analysis = (
                f"Your goal is {career_goal}, "
                f"but your current skills match "
                f"{best_career} better. "
                f"To move toward {career_goal}, "
                f"focus on: {missing_skills}."
            )

        else:

            goal_analysis = (
                f"Your goal is {career_goal}. "
                f"This career is not currently "
                f"in our career database."
            )

    # -----------------------------------------------------
    # Final recommendation response
    # -----------------------------------------------------

    return {

        "student":
            student["name"],

        "career_goal":
            career_goal,

        "goal_match_percentage":
            goal_match_percentage,

        "goal_matched_skills":
            goal_matched_skills,

        "goal_missing_skills":
            goal_missing_skills,

        "best_career":
            best_career,

        "goal_matches_recommendation":
            goal_match,

        "goal_analysis":
            goal_analysis,

        "recommendation_reason":
            result["recommendation_reason"],

        "recommendations":
            result["recommendations"]
    }


# =========================================================
# CAREER ROADMAP
# PROGRESS + NEXT SKILL + COMPLETION STATUS
# =========================================================

@app.get("/career/roadmap/{student_id}")
def career_roadmap(student_id: str):

    # -----------------------------------------------------
    # Check student ID
    # -----------------------------------------------------

    try:

        object_id = ObjectId(student_id)

    except Exception:

        raise HTTPException(
            status_code=400,
            detail="Invalid student ID"
        )

    # -----------------------------------------------------
    # Find student
    # -----------------------------------------------------

    student = student_collection.find_one(
        {
            "_id": object_id
        }
    )

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    # -----------------------------------------------------
    # Get career recommendations
    # -----------------------------------------------------

    result = recommend_careers(
        student.get("skills", [])
    )

    # -----------------------------------------------------
    # Get best career
    # -----------------------------------------------------

    if not result["recommendations"]:

        raise HTTPException(
            status_code=404,
            detail="No career recommendations available"
        )

    best_career = result[
        "recommendations"
    ][0]

    # -----------------------------------------------------
    # Get roadmap
    # -----------------------------------------------------

    roadmap = best_career.get(
        "roadmap",
        []
    )

    # -----------------------------------------------------
    # Completed skills
    # -----------------------------------------------------

    completed_skills = [
        item
        for item in roadmap
        if item["status"] == "Completed"
    ]

    # -----------------------------------------------------
    # Skills still to learn
    # -----------------------------------------------------

    skills_to_learn = [
        item
        for item in roadmap
        if item["status"] != "Completed"
    ]

    # -----------------------------------------------------
    # Find next skill
    # -----------------------------------------------------

    next_skill = None

    for item in skills_to_learn:

        missing_prerequisites = item.get(
            "missing_prerequisites",
            []
        )

        # Skill can be learned immediately
        if len(missing_prerequisites) == 0:

            next_skill = {

                "skill":
                    item["skill"],

                "level":
                    item["level"],

                "learning_order":
                    item["learning_order"],

                "reason":
                    "This skill has no missing prerequisites."
            }

            break

    # -----------------------------------------------------
    # Progress calculation
    # -----------------------------------------------------

    total_skills = len(
        roadmap
    )

    completed_count = len(
        completed_skills
    )

    remaining_count = len(
        skills_to_learn
    )

    if total_skills > 0:

        progress_percentage = round(
            (
                completed_count
                / total_skills
            ) * 100,
            2
        )

    else:

        progress_percentage = 0

    # -----------------------------------------------------
    # Roadmap completion status
    # -----------------------------------------------------

    if total_skills == 0:

        roadmap_status = "No Skills"

    elif completed_count == total_skills:

        roadmap_status = "Completed"

    else:

        roadmap_status = "In Progress"

    # -----------------------------------------------------
    # Final roadmap response
    # -----------------------------------------------------

    return {

        "student":
            student["name"],

        "career":
            best_career["career"],

        "match_percentage":
            best_career["match_percentage"],

        "progress": {

            "total_skills":
                total_skills,

            "completed":
                completed_count,

            "remaining":
                remaining_count,

            "progress_percentage":
                progress_percentage,

            "roadmap_status":
                roadmap_status
        },

        "next_skill":
            next_skill,

        "completed_skills":
            completed_skills,

        "skills_to_learn":
            skills_to_learn
    }