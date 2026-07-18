from pydantic import BaseModel

class Student(BaseModel):
    id: str
    full_name: str
    major: str
    gpa: float
    extracurriculars: list[str]
    advising_history_notes: str