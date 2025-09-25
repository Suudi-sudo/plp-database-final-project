# API Endpoints Documentation

## Base URL
`http://localhost:8000`

## Interactive Documentation
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Student Endpoints

### Create Student
- **POST** `/students/`
- **Body**: 
\`\`\`json
{
  "first_name": "string",
  "last_name": "string", 
  "email": "user@example.com",
  "age": 0
}
\`\`\`
- **Response**: Student object with ID and timestamps

### Get All Students
- **GET** `/students/`
- **Query Parameters**: 
  - `skip` (optional): Number of records to skip (default: 0)
  - `limit` (optional): Maximum number of records to return (default: 100)
- **Response**: Array of student objects

### Get Student by ID
- **GET** `/students/{student_id}`
- **Response**: Student object with enrolled courses

### Update Student
- **PUT** `/students/{student_id}`
- **Body**: 
\`\`\`json
{
  "first_name": "string (optional)",
  "last_name": "string (optional)",
  "email": "user@example.com (optional)",
  "age": 0,
  "is_active": true
}
\`\`\`
- **Response**: Updated student object

### Delete Student
- **DELETE** `/students/{student_id}`
- **Response**: Success message

## Course Endpoints

### Create Course
- **POST** `/courses/`
- **Body**: 
\`\`\`json
{
  "title": "string",
  "description": "string",
  "instructor": "string",
  "credits": 0
}
\`\`\`
- **Response**: Course object with ID and timestamps

### Get All Courses
- **GET** `/courses/`
- **Query Parameters**: 
  - `skip` (optional): Number of records to skip (default: 0)
  - `limit` (optional): Maximum number of records to return (default: 100)
- **Response**: Array of course objects

### Get Course by ID
- **GET** `/courses/{course_id}`
- **Response**: Course object with enrolled students

### Update Course
- **PUT** `/courses/{course_id}`
- **Body**: 
\`\`\`json
{
  "title": "string (optional)",
  "description": "string (optional)",
  "instructor": "string (optional)",
  "credits": 0,
  "is_active": true
}
\`\`\`
- **Response**: Updated course object

### Delete Course
- **DELETE** `/courses/{course_id}`
- **Response**: Success message

## Enrollment Endpoints

### Enroll Student in Course
- **POST** `/students/{student_id}/enroll/{course_id}`
- **Response**: Success message

### Unenroll Student from Course
- **DELETE** `/students/{student_id}/unenroll/{course_id}`
- **Response**: Success message

## Error Responses

### 400 Bad Request
\`\`\`json
{
  "detail": "Error message"
}
\`\`\`

### 404 Not Found
\`\`\`json
{
  "detail": "Resource not found"
}
\`\`\`

### 422 Validation Error
\`\`\`json
{
  "detail": [
    {
      "loc": ["field_name"],
      "msg": "Error message",
      "type": "error_type"
    }
  ]
}
\`\`\`

## Example Usage

### Create a Student
\`\`\`bash
curl -X POST "http://localhost:8000/students/" \
     -H "Content-Type: application/json" \
     -d '{
       "first_name": "John",
       "last_name": "Doe", 
       "email": "john.doe@example.com",
       "age": 20
     }'
\`\`\`

### Get All Students
\`\`\`bash
curl -X GET "http://localhost:8000/students/"
\`\`\`

### Enroll Student in Course
\`\`\`bash
curl -X POST "http://localhost:8000/students/1/enroll/1"
