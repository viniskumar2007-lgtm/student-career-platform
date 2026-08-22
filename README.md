# Student Career Platform 🚀

A Student Career Platform built using **Python, FastAPI, and MongoDB** to manage student information and provide career recommendations.

## 📌 Project Overview

The Student Career Platform helps manage student details and recommend suitable career paths based on their skills and career goals.

## 🛠️ Technologies Used

- Python
- FastAPI
- MongoDB
- MongoDB Atlas
- PyMongo
- Pydantic
- REST API
- Swagger UI

## ✨ Features

- Add student details
- View student details
- Update student information
- Delete student information
- Store data in MongoDB Atlas
- Career goal management
- Career recommendation endpoint
- Interactive API documentation using Swagger UI

## 📂 Project Structure

```text
Student-career-platform/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   └── .env
│
├── README.md
└── ...
🚀 API Endpoints
Method	Endpoint	Description
GET	/	Check whether the API is running
POST	/student	Add a new student
GET	/student	Get student details
PUT	/student/{student_id}	Update a student
DELETE	/student/{student_id}	Delete a student
GET	/best-career/{student_id}	Get career recommendation
📖 API Documentation

After starting the FastAPI server, open:

http://127.0.0.1:8000/docs

This opens the interactive Swagger UI documentation.

🗄️ Database

The project uses MongoDB Atlas to store student information.

🔐 The MongoDB connection string is stored in a .env file and should never be uploaded to GitHub.
🎯 Future Improvements
Student skill assessment
AI-based career recommendations
User authentication
Student dashboard
Career roadmap generation
Skill-gap analysis
Frontend interface
👨‍💻 Author

Vinith S

Computer Science and Engineering Student