from pydantic import BaseModel
from typing import List,Optional

class Student(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None
    courses: Optional[List[str]] = None
