from fastapi import APIRouter, HTTPException, Query
from typing import Optional
import re
from app.models.student import Student
from app.db.database import get_student, add_student, update_student_email

router = APIRouter()

@router.get("/students/{student_id}")
def get_student_info(
    student_id: int,
    include_grades: bool = False,
    semester: Optional[str] = None
):
    try:
        if not 1000 < student_id < 9999:
            raise ValueError("Student ID must be between 1000 and 9999")
        
        if semester:
            semester_pattern = r"^(Fall|Spring|Summer)\d{4}$"
            if not re.match(semester_pattern, semester):
                raise ValueError("Invalid semester format. Use Fall2024, Spring2025, etc.")
        
        student = get_student(student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        
        if include_grades:
            student["grades"] = {"Math": "A", "Physics": "B"}
            
        return student
            
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))

@router.post("/students/register")
def register_student(student: Student):
    try:
        if not all(c.isalpha() or c.isspace() for c in student.name):
            raise ValueError("Name must contain only alphabets and spaces")
        if len(student.name) > 50:
            raise ValueError("Name must be less than 50 characters")
            
        if not 18 <= student.age <= 30:
            raise ValueError("Age must be between 18 and 30")
            
        if "@" not in student.email:
            raise ValueError("Invalid email format")
            
        if not 1 <= len(student.courses) <= 5:
            raise ValueError("Number of courses must be between 1 and 5")
            
        for course in student.courses:
            if not 5 <= len(course) <= 30:
                raise ValueError("Course name must be between 5 and 30 characters")
                
        if len(set(student.courses)) != len(student.courses):
            raise ValueError("Duplicate courses are not allowed")
            
        student_data = student.dict()
        student_id = add_student(student_data)
        return {"student_id": student_id, **student_data}
        
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))

@router.put("/students/{student_id}/email")
def update_email(student_id: int, email: str):
    try:
        if not 1000 < student_id < 9999:
            raise ValueError("Student ID must be between 1000 and 9999")
            
        if "@" not in email:
            raise ValueError("Invalid email format")
            
        if not update_student_email(student_id, email):
            raise HTTPException(status_code=404, detail="Student not found")
            
        return {"message": "Email updated successfully"}
        
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))