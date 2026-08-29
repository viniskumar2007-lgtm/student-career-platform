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
    # Default values
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

        # Percentage
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
    # Goal analysis
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
    # Final response
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
# =========================================================

@app.get("/career/roadmap/{student_id}")
def career_roadmap(student_id: str):

    # -----------------------------------------------------
    # 1. Validate Student ID
    # -----------------------------------------------------

    try:

        object_id = ObjectId(student_id)

    except Exception:

        raise HTTPException(
            status_code=400,
            detail="Invalid student ID"
        )

    # -----------------------------------------------------
    # 2. Find Student
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
    # 3. Get Student Skills
    # -----------------------------------------------------

    student_skills = student.get(
        "skills",
        []
    )

    # -----------------------------------------------------
    # 4. Get Career Recommendations
    # -----------------------------------------------------

    result = recommend_careers(
        student_skills
    )

    recommendations = result.get(
        "recommendations",
        []
    )

    if not recommendations:

        raise HTTPException(
            status_code=404,
            detail="No career recommendations available"
        )

    # -----------------------------------------------------
    # 5. Best Career
    # -----------------------------------------------------

    best_career = recommendations[0]

    # -----------------------------------------------------
    # 6. Get Roadmap
    # -----------------------------------------------------

    roadmap = best_career.get(
        "roadmap",
        []
    )

    if not roadmap:

        raise HTTPException(
            status_code=404,
            detail="Career roadmap is empty"
        )

    # -----------------------------------------------------
    # 7. Completed Skills
    # -----------------------------------------------------

    completed_skills = [
        item
        for item in roadmap
        if item["status"] == "Completed"
    ]

    # -----------------------------------------------------
    # 8. Skills To Learn
    # -----------------------------------------------------

    skills_to_learn = [
        item
        for item in roadmap
        if item["status"] != "Completed"
    ]

    # -----------------------------------------------------
    # 9. Find Next Skill
    # -----------------------------------------------------

    next_skill = None

    for item in skills_to_learn:

        missing_prerequisites = item.get(
            "missing_prerequisites",
            []
        )

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
    # 10. Progress Calculation
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
    # 11. Roadmap Status
    # -----------------------------------------------------

    if total_skills == 0:

        roadmap_status = "No Skills"

    elif completed_count == total_skills:

        roadmap_status = "Completed"

    else:

        roadmap_status = "In Progress"

    # -----------------------------------------------------
    # 12. Roadmap Summary - STEP 7.6
    # -----------------------------------------------------

    if roadmap_status == "Completed":

        roadmap_message = (
            "Congratulations! "
            "You have completed your roadmap."
        )

    elif roadmap_status == "No Skills":

        roadmap_message = (
            "No skills are available "
            "in the roadmap."
        )

    else:

        roadmap_message = (
            f"Keep learning! "
            f"You have {remaining_count} "
            f"skills remaining."
        )

    # -----------------------------------------------------
    # 13. Final Roadmap Response
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

        # -------------------------------------------------
        # STEP 7.6 SUMMARY
        # -------------------------------------------------

        "summary": {

            "message":
                roadmap_message,

            "completed_percentage":
                progress_percentage
        },

        "next_skill":
            next_skill,

        "completed_skills":
            completed_skills,

        "skills_to_learn":
            skills_to_learn
    }


# =========================================================
# COMPLETE SKILL
# DAY 7 - STEP 7.5
# SKILL + PREREQUISITE VALIDATION
# =========================================================

@app.post(
    "/career/roadmap/{student_id}/complete/{skill}"
)
def complete_skill(
    student_id: str,
    skill: str
):

    # -----------------------------------------------------
    # 1. Validate Student ID
    # -----------------------------------------------------

    try:

        object_id = ObjectId(student_id)

    except Exception:

        raise HTTPException(
            status_code=400,
            detail="Invalid student ID"
        )

    # -----------------------------------------------------
    # 2. Find Student
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
    # 3. Current Skills
    # -----------------------------------------------------

    current_skills = student.get(
        "skills",
        []
    )

    # -----------------------------------------------------
    # 4. Get Career Recommendation
    # -----------------------------------------------------

    recommendation_result = recommend_careers(
        current_skills
    )

    recommendations = recommendation_result.get(
        "recommendations",
        []
    )

    if not recommendations:

        raise HTTPException(
            status_code=404,
            detail="No career roadmap available"
        )

    # -----------------------------------------------------
    # 5. Best Career
    # -----------------------------------------------------

    best_career = recommendations[0]

    # -----------------------------------------------------
    # 6. Get Roadmap
    # -----------------------------------------------------

    roadmap = best_career.get(
        "roadmap",
        []
    )

    if not roadmap:

        raise HTTPException(
            status_code=404,
            detail="Career roadmap is empty"
        )

    # -----------------------------------------------------
    # 7. Clean Requested Skill
    # -----------------------------------------------------

    requested_skill = skill.strip()

    if not requested_skill:

        raise HTTPException(
            status_code=400,
            detail="Skill cannot be empty"
        )

    # -----------------------------------------------------
    # 8. Find Skill in Roadmap
    # Case-insensitive
    # -----------------------------------------------------

    roadmap_item = next(
        (
            item
            for item in roadmap
            if item["skill"].strip().lower()
            == requested_skill.lower()
        ),
        None
    )

    # -----------------------------------------------------
    # 9. Invalid Skill
    # -----------------------------------------------------

    if roadmap_item is None:

        raise HTTPException(
            status_code=400,
            detail=(
                f"Skill '{requested_skill}' "
                "not found in the career roadmap."
            )
        )

    # -----------------------------------------------------
    # 10. Official Skill Name
    # -----------------------------------------------------

    roadmap_skill = roadmap_item["skill"]

    # -----------------------------------------------------
    # 11. Already Completed
    # -----------------------------------------------------

    existing_skill = next(
        (
            existing
            for existing in current_skills
            if existing.strip().lower()
            == roadmap_skill.strip().lower()
        ),
        None
    )

    if existing_skill:

        return {

            "message":
                "Skill already completed!",

            "student":
                student["name"],

            "career":
                best_career["career"],

            "skill":
                roadmap_skill,

            "status":
                "Already Completed",

            "skills":
                current_skills
        }

    # -----------------------------------------------------
    # 12. Get Prerequisites
    # -----------------------------------------------------

    prerequisites = roadmap_item.get(
        "prerequisites",
        []
    )

    # -----------------------------------------------------
    # 13. Normalize Current Skills
    # -----------------------------------------------------

    current_skills_lower = {
        existing.strip().lower()
        for existing in current_skills
    }

    # -----------------------------------------------------
    # 14. Find Missing Prerequisites
    # -----------------------------------------------------

    missing_prerequisites = [
        prerequisite
        for prerequisite in prerequisites
        if prerequisite.strip().lower()
        not in current_skills_lower
    ]

    # -----------------------------------------------------
    # 15. Reject Missing Prerequisites
    # -----------------------------------------------------

    if missing_prerequisites:

        raise HTTPException(
            status_code=400,
            detail={
                "message": (
                    f"Cannot complete {roadmap_skill} "
                    "because prerequisites are incomplete."
                ),
                "skill":
                    roadmap_skill,
                "missing_prerequisites":
                    missing_prerequisites
            }
        )

    # -----------------------------------------------------
    # 16. Add Skill
    # -----------------------------------------------------

    current_skills.append(
        roadmap_skill
    )

    # -----------------------------------------------------
    # 17. Update MongoDB
    # -----------------------------------------------------

    update_result = student_collection.update_one(
        {
            "_id": object_id
        },
        {
            "$set": {
                "skills": current_skills
            }
        }
    )

    # -----------------------------------------------------
    # 18. Verify Update
    # -----------------------------------------------------

    if update_result.matched_count == 0:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    # -----------------------------------------------------
    # 19. Success
    # -----------------------------------------------------

    return {

        "message":
            "Skill completed successfully!",

        "student":
            student["name"],

        "career":
            best_career["career"],

        "skill":
            roadmap_skill,

        "status":
            "Completed",

        "skills":
            current_skills,

        "modified":
            update_result.modified_count
    }