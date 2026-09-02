from pydantic import BaseModel, Field
class Student(BaseModel):
    name: str
    age: int = Field(ge=15, le=100)
    major: str
    year: int = Field(ge=1, le=4)
    skills: list[str] = Field(default_factory=list)
    interests: list[str] = Field(default_factory=list)
    career_goal: str = ""
class LearningHistory(BaseModel):

    skill: str
    status: str
    completed_at: str