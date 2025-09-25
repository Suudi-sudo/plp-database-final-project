import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app, get_db
from database import Base
import models

# Create test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome to Student-Course Management API" in response.json()["message"]

def test_create_student():
    response = client.post(
        "/students/",
        json={
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "age": 20
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == "John"
    assert data["last_name"] == "Doe"
    assert data["email"] == "john.doe@example.com"
    assert data["age"] == 20
    assert "id" in data

def test_read_students():
    response = client.get("/students/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_course():
    response = client.post(
        "/courses/",
        json={
            "title": "Introduction to Python",
            "description": "Learn Python programming basics",
            "instructor": "Dr. Smith",
            "credits": 3
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Introduction to Python"
    assert data["instructor"] == "Dr. Smith"
    assert data["credits"] == 3
    assert "id" in data

def test_read_courses():
    response = client.get("/courses/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_student_not_found():
    response = client.get("/students/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Student not found"

def test_course_not_found():
    response = client.get("/courses/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Course not found"

def test_duplicate_email():
    # First student
    client.post(
        "/students/",
        json={
            "first_name": "Jane",
            "last_name": "Smith",
            "email": "jane.smith@example.com",
            "age": 22
        }
    )
    
    # Try to create another student with same email
    response = client.post(
        "/students/",
        json={
            "first_name": "John",
            "last_name": "Smith",
            "email": "jane.smith@example.com",
            "age": 25
        }
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"
