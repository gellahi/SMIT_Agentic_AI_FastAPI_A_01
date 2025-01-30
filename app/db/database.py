students_db = {}

def get_student(student_id: int):
    return students_db.get(student_id)

def add_student(student_data: dict):
    student_id = len(students_db) + 1001
    students_db[student_id] = student_data
    return student_id

def update_student_email(student_id: int, email: str):
    if student_id in students_db:
        students_db[student_id]["email"] = email
        return True
    return False