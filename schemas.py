from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

# Student schemas
class StudentBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    age: int

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = None
    is_active: Optional[bool] = None

class Student(StudentBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime
    courses: List['CourseBase'] = []

    class Config:
        from_attributes = True

# Course schemas
class CourseBase(BaseModel):
    title: str
    description: str
    instructor: str
    credits: int

class CourseCreate(CourseBase):
    pass

class CourseUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    instructor: Optional[str] = None
    credits: Optional[int] = None
    is_active: Optional[bool] = None

class Course(CourseBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime
    students: List['StudentBase'] = []

    class Config:
        from_attributes = True

# Update forward references
Student.model_rebuild()
Course.model_rebuild()
