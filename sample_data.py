"""
Sample data insertion script for testing the API
Run this script to populate the database with sample data
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def create_sample_students():
    students = [
        {
            "first_name": "Alice",
            "last_name": "Johnson",
            "email": "alice.johnson@university.edu",
            "age": 20
        },
        {
            "first_name": "Bob",
            "last_name": "Smith",
            "email": "bob.smith@university.edu",
            "age": 22
        },
        {
            "first_name": "Carol",
            "last_name": "Davis",
            "email": "carol.davis@university.edu",
            "age": 19
        },
        {
            "first_name": "David",
            "last_name": "Wilson",
            "email": "david.wilson@university.edu",
            "age": 21
        }
    ]
    
    created_students = []
    for student in students:
        response = requests.post(f"{BASE_URL}/students/", json=student)
        if response.status_code == 200:
            created_students.append(response.json())
            print(f"Created student: {student['first_name']} {student['last_name']}")
        else:
            print(f"Failed to create student: {student['first_name']} {student['last_name']}")
    
    return created_students

def create_sample_courses():
    courses = [
        {
            "title": "Introduction to Computer Science",
            "description": "Fundamental concepts of computer science and programming",
            "instructor": "Dr. Sarah Johnson",
            "credits": 4
        },
        {
            "title": "Data Structures and Algorithms",
            "description": "Study of data structures and algorithmic problem solving",
            "instructor": "Prof. Michael Brown",
            "credits": 3
        },
        {
            "title": "Database Systems",
            "description": "Design and implementation of database systems",
            "instructor": "Dr. Emily Chen",
            "credits": 3
        },
        {
            "title": "Web Development",
            "description": "Modern web development with HTML, CSS, and JavaScript",
            "instructor": "Prof. James Wilson",
            "credits": 3
        }
    ]
    
    created_courses = []
    for course in courses:
        response = requests.post(f"{BASE_URL}/courses/", json=course)
        if response.status_code == 200:
            created_courses.append(response.json())
            print(f"Created course: {course['title']}")
        else:
            print(f"Failed to create course: {course['title']}")
    
    return created_courses

def enroll_students_in_courses(students, courses):
    # Sample enrollments
    enrollments = [
        (0, 0),  # Alice in Computer Science
        (0, 2),  # Alice in Database Systems
        (1, 0),  # Bob in Computer Science
        (1, 1),  # Bob in Data Structures
        (1, 3),  # Bob in Web Development
        (2, 2),  # Carol in Database Systems
        (2, 3),  # Carol in Web Development
        (3, 1),  # David in Data Structures
        (3, 2),  # David in Database Systems
    ]
    
    for student_idx, course_idx in enrollments:
        if student_idx < len(students) and course_idx < len(courses):
            student_id = students[student_idx]['id']
            course_id = courses[course_idx]['id']
            response = requests.post(f"{BASE_URL}/students/{student_id}/enroll/{course_id}")
            if response.status_code == 200:
                print(f"Enrolled {students[student_idx]['first_name']} in {courses[course_idx]['title']}")
            else:
                print(f"Failed to enroll {students[student_idx]['first_name']} in {courses[course_idx]['title']}")

if __name__ == "__main__":
    print("Creating sample data...")
    print("\n1. Creating students...")
    students = create_sample_students()
    
    print("\n2. Creating courses...")
    courses = create_sample_courses()
    
    print("\n3. Enrolling students in courses...")
    enroll_students_in_courses(students, courses)
    
    print("\nSample data creation completed!")
    print(f"Visit {BASE_URL}/docs to explore the API documentation")
