careers = [
    {
        "career": "Software Developer",
        "skills": ["Python", "C++", "SQL", "Git", "Data Structures"]
    },
    {
        "career": "Data Scientist",
        "skills": ["Python", "SQL", "Machine Learning", "Statistics", "Pandas"]
    },
    {
        "career": "AI Engineer",
        "skills": ["Python", "Machine Learning", "AI", "Deep Learning", "TensorFlow"]
    },
    {
        "career": "Blockchain Developer",
        "skills": ["Python", "C++", "Blockchain", "Solidity", "Cryptography"]
    },
    {
        "career": "Web Developer",
        "skills": ["HTML", "CSS", "JavaScript", "React", "Node.js"]
    },
    {
        "career": "Mobile App Developer",
        "skills": ["Java", "Kotlin", "Swift", "Flutter", "REST APIs"]
    },
    {
        "career": "DevOps Engineer",
        "skills": ["Linux", "Docker", "Kubernetes", "CI/CD", "AWS"]
    },
    {
        "career": "Cybersecurity Analyst",
        "skills": [
            "Networking",
            "Linux",
            "Penetration Testing",
            "SQL",
            "Cryptography"
        ]
    },
    {
        "career": "Cloud Engineer",
        "skills": [
            "AWS",
            "Azure",
            "Docker",
            "Kubernetes",
            "Networking"
        ]
    },
    {
        "career": "Database Administrator",
        "skills": [
            "SQL",
            "PostgreSQL",
            "MongoDB",
            "Data Modeling",
            "Backup & Recovery"
        ]
    },
    {
        "career": "Game Developer",
        "skills": [
            "C++",
            "C#",
            "Unity",
            "Unreal Engine",
            "3D Math"
        ]
    },
    {
        "career": "UI/UX Designer",
        "skills": [
            "Figma",
            "HTML",
            "CSS",
            "User Research",
            "Prototyping"
        ]
    },
    {
        "career": "Embedded Systems Engineer",
        "skills": [
            "C",
            "C++",
            "Microcontrollers",
            "RTOS",
            "Circuit Design"
        ]
    },
    {
        "career": "Full Stack Developer",
        "skills": [
            "JavaScript",
            "React",
            "Node.js",
            "SQL",
            "HTML",
            "CSS"
        ]
    },
    {
        "career": "Machine Learning Engineer",
        "skills": [
            "Python",
            "Machine Learning",
            "AI",
            "MLOps",
            "TensorFlow"
        ]
    }
]


# Skill difficulty levels
skill_levels = {

    # Programming
    "Python": "Beginner",
    "C": "Beginner",
    "C++": "Intermediate",
    "C#": "Intermediate",
    "Java": "Beginner",
    "Kotlin": "Intermediate",
    "Swift": "Intermediate",

    # Software Development
    "SQL": "Beginner",
    "Git": "Beginner",
    "Data Structures": "Intermediate",

    # Data Science / AI
    "Statistics": "Intermediate",
    "Pandas": "Intermediate",
    "Machine Learning": "Advanced",
    "AI": "Advanced",
    "Deep Learning": "Advanced",
    "TensorFlow": "Advanced",

    # Blockchain
    "Blockchain": "Intermediate",
    "Solidity": "Intermediate",
    "Cryptography": "Advanced",

    # Web Development
    "HTML": "Beginner",
    "CSS": "Beginner",
    "JavaScript": "Intermediate",
    "React": "Intermediate",
    "Node.js": "Intermediate",

    # Mobile Development
    "Flutter": "Intermediate",
    "REST APIs": "Intermediate",

    # DevOps / Cloud
    "Linux": "Beginner",
    "Docker": "Intermediate",
    "Kubernetes": "Advanced",
    "CI/CD": "Intermediate",
    "AWS": "Intermediate",
    "Azure": "Intermediate",

    # Cybersecurity
    "Networking": "Intermediate",
    "Penetration Testing": "Advanced",

    # Database
    "PostgreSQL": "Intermediate",
    "MongoDB": "Intermediate",
    "Data Modeling": "Intermediate",
    "Backup & Recovery": "Advanced",

    # Game Development
    "Unity": "Intermediate",
    "Unreal Engine": "Advanced",
    "3D Math": "Advanced",

    # UI/UX
    "Figma": "Beginner",
    "User Research": "Intermediate",
    "Prototyping": "Intermediate",

    # Embedded Systems
    "Microcontrollers": "Intermediate",
    "RTOS": "Advanced",
    "Circuit Design": "Intermediate",

    # Machine Learning Operations
    "MLOps": "Advanced"
}



def recommend_careers(student_skills):

    recommendations = []

    # Convert student skills to set
    student_skills_set = set(student_skills)

    # Check every career
    for career in careers:

        # Keep original order
        required_skills = career["skills"]

        # Find matched skills in career order
        matched_skills = [
            skill
            for skill in required_skills
            if skill in student_skills_set
        ]

        # Find missing skills in career order
        missing_skills = [
            skill
            for skill in required_skills
            if skill not in student_skills_set
        ]

        # Calculate match percentage
        match_percentage = (
            len(matched_skills) /
            len(required_skills)
        ) * 100

        # Create roadmap
        roadmap = []

        priority = 1

        for skill in required_skills:

            # Student already has skill
            if skill in student_skills_set:

                roadmap.append({
                    "skill": skill,
                    "level": skill_levels.get(
                        skill,
                        "Beginner"
                    ),
                    "priority": 0,
                    "status": "Completed"
                })

            # Student needs skill
            else:

                roadmap.append({
                    "skill": skill,
                    "level": skill_levels.get(
                        skill,
                        "Beginner"
                    ),
                    "priority": priority,
                    "status": "Learn Next"
                })

                priority += 1

        # Add recommendation
        recommendations.append({
            "career": career["career"],
            "match_percentage": round(
                match_percentage,
                2
            ),
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "roadmap": roadmap
        })

    # Sort highest match first
    recommendations.sort(
        key=lambda x: x["match_percentage"],
        reverse=True
    )

    # Top 3 careers
    top_3 = recommendations[:3]

    # Best career
    best_career = top_3[0]

    # Count skills
    total_skills = (
        len(best_career["matched_skills"]) +
        len(best_career["missing_skills"])
    )

    matched_count = len(
        best_career["matched_skills"]
    )

    missing_count = len(
        best_career["missing_skills"]
    )

    # Create recommendation reason
    if missing_count == 0:

        reason = (
            f"You have all {total_skills} required skills "
            f"for {best_career['career']}. "
            f"You are highly suitable for this career."
        )

    else:

        missing_skill_names = ", ".join(
            best_career["missing_skills"]
        )

        reason = (
            f"You already have {matched_count} "
            f"out of {total_skills} required skills. "
            f"Focus on {missing_skill_names} "
            f"to improve your match."
        )

    # Final result
    return {
        "best_career": best_career["career"],
        "recommendation_reason": reason,
        "recommendations": top_3
    }