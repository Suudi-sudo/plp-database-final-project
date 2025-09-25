# Student-Course Management API

A complete CRUD (Create, Read, Update, Delete) application built with FastAPI that manages students and courses with enrollment functionality.

## Features

- **Student Management**: Create, read, update, and delete student records
- **Course Management**: Create, read, update, and delete course records  
- **Enrollment System**: Enroll/unenroll students in courses with many-to-many relationships
- **Data Validation**: Comprehensive input validation using Pydantic models
- **Interactive Documentation**: Auto-generated API docs with Swagger UI
- **Database Integration**: SQLite database with SQLAlchemy ORM
- **Testing Suite**: Comprehensive test coverage with pytest
- **Sample Data**: Script to populate database with sample data

## Database Schema


## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pipenv (Python dependency manager)

### Step 1: Install pipenv (if not already installed)
\`\`\`bash
pip install pipenv
\`\`\`

### Step 2: Clone the Repository
\`\`\`bash
git clone <your-repository-url>
cd fastapi-crud-app
\`\`\`

### Step 3: Install Dependencies
\`\`\`bash
pipenv install --dev

# Or install only production dependencies
pipenv install
\`\`\`

### Step 4: Activate Virtual Environment
\`\`\`bash
pipenv shell
\`\`\`

### Step 5: Run the Application
\`\`\`bash
pipenv run uvicorn main:app --reload

# Or if you're in the pipenv shell
uvicorn main:app --reload

# Or run directly with Python
pipenv run python main.py
\`\`\`

The API will be available at: `http://localhost:8000`

## API Documentation


## Testing

### Run Tests
\`\`\`bash
pipenv run pytest

# Run tests with verbose output
pipenv run pytest -v

# Run specific test file
pipenv run pytest test_main.py

# Or if you're in the pipenv shell
pytest
\`\`\`


## Sample Data

### Populate Database with Sample Data
\`\`\`bash
pipenv run uvicorn main:app --reload

# In another terminal, run the sample data script
pipenv run python sample_data.py
\`\`\`


## Project Structure

\`\`\`
fastapi-crud-app/
├── main.py              # FastAPI application and route definitions
├── models.py            # SQLAlchemy database models
├── schemas.py           # Pydantic models for request/response validation
├── crud.py              # Database CRUD operations
├── database.py          # Database connection and session management
├── test_main.py         # Test suite
├── sample_data.py       # Script to populate database with sample data
├── Pipfile              # pipenv dependencies and configuration
├── Pipfile.lock         # Locked dependency versions (auto-generated)
├── api_endpoints.md     # Detailed API documentation
└── README.md           # This file
\`\`\`


## Development Notes

### Dependencies Management
- Uses pipenv for dependency management and virtual environments
- Production dependencies in `[packages]` section
- Development dependencies in `[dev-packages]` section
- Pipfile.lock ensures reproducible builds

### Database
- Uses SQLite for simplicity and portability
- Database file: `student_course_management.db`
- Automatically created on first run

### Environment
- Development server runs on `http://localhost:8000`
- Auto-reload enabled for development
- CORS enabled for frontend integration

## Troubleshooting

### Common Issues

1. **Port already in use**
   \`\`\`bash
   pipenv run uvicorn main:app --reload --port 8001
   \`\`\`

2. **Database locked error**
   - Stop the server and restart
   - Delete the `.db` file to reset database

3. **Import errors**
   - Ensure pipenv environment is activated: `pipenv shell`
   - Reinstall dependencies: `pipenv install --dev`

4. **pipenv issues**
   \`\`\`bash
   # Clear pipenv cache if needed
   pipenv --clear
   
   # Reinstall all dependencies
   pipenv install --dev
   \`\`\`
