from sqlalchemy.orm import Session
from sqlalchemy import and_
import models
import schemas

# Student CRUD operations
def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def get_student_by_email(db: Session, email: str):
    return db.query(models.Student).filter(models.Student.email == email).first()

def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(
        first_name=student.first_name,
        last_name=student.last_name,
        email=student.email,
        age=student.age
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def update_student(db: Session, student_id: int, student: schemas.StudentUpdate):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if db_student:
        update_data = student.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_student, field, value)
        db.commit()
        db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_id: int):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if db_student:
        db.delete(db_student)
        db.commit()
        return True
    return False

# Course CRUD operations
def get_course(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.id == course_id).first()

def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Course).offset(skip).limit(limit).all()

def create_course(db: Session, course: schemas.CourseCreate):
    db_course = models.Course(
        title=course.title,
        description=course.description,
        instructor=course.instructor,
        credits=course.credits
    )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def update_course(db: Session, course_id: int, course: schemas.CourseUpdate):
    db_course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if db_course:
        update_data = course.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_course, field, value)
        db.commit()
        db.refresh(db_course)
    return db_course

def delete_course(db: Session, course_id: int):
    db_course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if db_course:
        db.delete(db_course)
        db.commit()
        return True
    return False

# Enrollment operations
def enroll_student_in_course(db: Session, student_id: int, course_id: int):
    student = get_student(db, student_id)
    course = get_course(db, course_id)
    
    if not student or not course:
        return False
    
    # Check if already enrolled
    if course in student.courses:
        return False
    
    student.courses.append(course)
    db.commit()
    return True

def unenroll_student_from_course(db: Session, student_id: int, course_id: int):
    student = get_student(db, student_id)
    course = get_course(db, course_id)
    
    if not student or not course:
        return False
    
    # Check if enrolled
    if course not in student.courses:
        return False
    
    student.courses.remove(course)
    db.commit()
    return True
