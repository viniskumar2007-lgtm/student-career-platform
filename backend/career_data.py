# ============================================================
# CAREER DATA
# ============================================================

careers = [

    {
        "career": "Software Developer",
        "skills": [
            "Python",
            "C++",
            "SQL",
            "Git",
            "Data Structures"
        ]
    },

    {
        "career": "Data Scientist",
        "skills": [
            "Python",
            "SQL",
            "Machine Learning",
            "Statistics",
            "Pandas"
        ]
    },

    {
        "career": "AI Engineer",
        "skills": [
            "Python",
            "Machine Learning",
            "AI",
            "Deep Learning",
            "TensorFlow"
        ]
    },

    {
        "career": "Blockchain Developer",
        "skills": [
            "Python",
            "C++",
            "Blockchain",
            "Solidity",
            "Cryptography"
        ]
    },

    {
        "career": "Web Developer",
        "skills": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Node.js"
        ]
    },

    {
        "career": "Mobile App Developer",
        "skills": [
            "Java",
            "Kotlin",
            "Swift",
            "Flutter",
            "REST APIs"
        ]
    },

    {
        "career": "DevOps Engineer",
        "skills": [
            "Linux",
            "Docker",
            "Kubernetes",
            "CI/CD",
            "AWS"
        ]
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


# ============================================================
# SKILL DIFFICULTY LEVELS
# ============================================================

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
    "MLOps": "Advanced",

    # Additional dependency skill
    "Dart": "Beginner"
}


# ============================================================
# SKILL PRIORITY
# ============================================================

skill_priority = {
    "Beginner": 1,
    "Intermediate": 2,
    "Advanced": 3
}


# ============================================================
# SKILL DEPENDENCIES
# ============================================================

skill_dependencies = {

    # Programming
    "C++": ["C"],
    "C#": ["C++"],
    "Java": [],
    "Kotlin": ["Java"],
    "Swift": [],

    # Software Development
    "SQL": [],
    "Git": [],
    "Data Structures": ["C++"],

    # Data Science / AI
    "Pandas": ["Python"],
    "Statistics": [],
    "Machine Learning": [
        "Python",
        "Statistics"
    ],
    "AI": [
        "Python",
        "Machine Learning"
    ],
    "Deep Learning": [
        "Python",
        "Machine Learning",
        "AI"
    ],
    "TensorFlow": [
        "Python",
        "Machine Learning",
        "Deep Learning"
    ],

    # Blockchain
    "Blockchain": [
        "Python",
        "C++"
    ],
    "Solidity": [
        "Blockchain"
    ],
    "Cryptography": [
        "Python"
    ],

    # Web Development
    "HTML": [],
    "CSS": [
        "HTML"
    ],
    "JavaScript": [
        "HTML",
        "CSS"
    ],
    "React": [
        "JavaScript"
    ],
    "Node.js": [
        "JavaScript"
    ],

    # Mobile Development
    "Flutter": [
        "Dart"
    ],
    "REST APIs": [],

    # DevOps / Cloud
    "Linux": [],
    "Docker": [
        "Linux"
    ],
    "Kubernetes": [
        "Docker",
        "Linux"
    ],
    "CI/CD": [
        "Git",
        "Linux"
    ],
    "AWS": [
        "Linux",
        "Networking"
    ],
    "Azure": [
        "Linux",
        "Networking"
    ],

    # Cybersecurity
    "Networking": [],
    "Penetration Testing": [
        "Networking",
        "Linux"
    ],

    # Database
    "PostgreSQL": [
        "SQL"
    ],
    "MongoDB": [
        "Data Modeling"
    ],
    "Data Modeling": [
        "SQL"
    ],
    "Backup & Recovery": [
        "SQL"
    ],

    # Game Development
    "Unity": [
        "C#"
    ],
    "Unreal Engine": [
        "C++"
    ],
    "3D Math": [],

    # UI/UX
    "Figma": [],
    "User Research": [],
    "Prototyping": [
        "Figma",
        "User Research"
    ],

    # Embedded Systems
    "Microcontrollers": [
        "C",
        "C++"
    ],
    "RTOS": [
        "C",
        "Microcontrollers"
    ],
    "Circuit Design": [],

    # Machine Learning Operations
    "MLOps": [
        "Python",
        "Machine Learning",
        "Docker",
        "Git"
    ]
}


# ============================================================
# GET LEARNING ORDER
# ============================================================

def get_learning_order(required_skills, student_skills_set):

    learning_order = []
    visited = set()

    def add_skill(skill):

        # Already processed
        if skill in visited:
            return

        # Student already knows this skill
        if skill in student_skills_set:
            visited.add(skill)
            return

        # Get dependencies
        dependencies = skill_dependencies.get(
            skill,
            []
        )

        # Process missing dependencies first
        for dependency in dependencies:

            if dependency not in student_skills_set:
                add_skill(dependency)

        # Add skill after dependencies
        if skill not in learning_order:
            learning_order.append(skill)

        visited.add(skill)

    # Process required skills
    for skill in required_skills:
        add_skill(skill)

    return learning_order


# ============================================================
# RECOMMEND CAREERS
# ============================================================

def recommend_careers(student_skills):

    recommendations = []

    # Convert student skills to set
    student_skills_set = set(student_skills)

    # Check every career
    for career in careers:

        required_skills = career["skills"]

        # ----------------------------------------------------
        # MATCHED SKILLS
        # ----------------------------------------------------

        matched_skills = [
            skill
            for skill in required_skills
            if skill in student_skills_set
        ]

        # ----------------------------------------------------
        # MISSING SKILLS
        # ----------------------------------------------------

        missing_skills = [
            skill
            for skill in required_skills
            if skill not in student_skills_set
        ]

        # ----------------------------------------------------
        # MATCH PERCENTAGE
        # ----------------------------------------------------

        match_percentage = (
            len(matched_skills)
            / len(required_skills)
        ) * 100

        # ----------------------------------------------------
        # CREATE ROADMAP
        # ----------------------------------------------------

        roadmap = []

        # Dependency-aware learning order
        learning_order = get_learning_order(
            required_skills,
            student_skills_set
        )

        # Position of every skill
        learning_position = {
            skill: index + 1
            for index, skill in enumerate(
                learning_order
            )
        }

        # ----------------------------------------------------
        # BUILD ROADMAP
        # ----------------------------------------------------

        for skill in required_skills:

            # Student already knows skill
            if skill in student_skills_set:

                level = skill_levels.get(
                    skill,
                    "Beginner"
                )

                roadmap.append({
                    "skill": skill,
                    "level": level,
                    "priority": 0,
                    "status": "Completed",
                    "prerequisites": skill_dependencies.get(
                        skill,
                        []
                    ),
                    "missing_prerequisites": [],
                    "learning_order": 0
                })

            # Student does not know skill
            else:

                level = skill_levels.get(
                    skill,
                    "Beginner"
                )

                dependencies = skill_dependencies.get(
                    skill,
                    []
                )

                missing_dependencies = [
                    dependency
                    for dependency in dependencies
                    if dependency not in student_skills_set
                ]

                # Priority
                if len(missing_dependencies) == 0:

                    priority = 1
                    status = "Learn Next"

                else:

                    priority = 2
                    status = "Learn After Prerequisites"

                roadmap.append({
                    "skill": skill,
                    "level": level,
                    "priority": priority,
                    "status": status,
                    "prerequisites": dependencies,
                    "missing_prerequisites": missing_dependencies,
                    "learning_order": learning_position.get(
                        skill,
                        999
                    )
                })

        # ----------------------------------------------------
        # SORT ROADMAP
        # ----------------------------------------------------

        roadmap.sort(
            key=lambda x: (
                x["learning_order"] == 0,
                x["learning_order"]
            )
        )

        # ----------------------------------------------------
        # ADD CAREER RECOMMENDATION
        # ----------------------------------------------------

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

    # ========================================================
    # SORT CAREERS
    # ========================================================

    recommendations.sort(
        key=lambda x: x["match_percentage"],
        reverse=True
    )

    # Top 3 careers
    top_3 = recommendations[:3]

    # Best career
    best_career = top_3[0]

    # ========================================================
    # BEST CAREER STATISTICS
    # ========================================================

    total_skills = (
        len(best_career["matched_skills"])
        + len(best_career["missing_skills"])
    )

    matched_count = len(
        best_career["matched_skills"]
    )

    missing_count = len(
        best_career["missing_skills"]
    )

    # ========================================================
    # RECOMMENDATION REASON
    # ========================================================

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

    # ========================================================
    # FINAL RESULT
    # ========================================================

    return {
        "best_career": best_career["career"],
        "recommendation_reason": reason,
        "recommendations": top_3
    }


# ============================================================
# GET CAREER BY NAME
# ============================================================

def get_career_by_name(career_name):

    for career in careers:

        if (
            career["career"].lower()
            == career_name.lower()
        ):
            return career

    return None