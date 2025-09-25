from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

# Association table for many-to-many relationship between students and courses
student_course_association = Table(
    'student_courses',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True),
    Column('enrolled_at', DateTime, default=func.now())
)

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    age = Column(Integer)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Many-to-many relationship with courses
    courses = relationship("Course", secondary=student_course_association, back_populates="students")

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    instructor = Column(String)
    credits = Column(Integer)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Many-to-many relationship with students
    students = relationship("Student", secondary=student_course_association, back_populates="courses")
