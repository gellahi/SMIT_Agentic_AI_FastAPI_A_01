from pydantic import BaseModel
from typing import List, Optional

class Student(BaseModel):
    name: str
    email: str
    age: int
    courses: List[str]