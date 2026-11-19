# Student Management CRUD API (Django + SQLite)

A clean, production-grade Django REST API for student management providing strictly the core CRUD operations: **POST**, **GET** (all), **GET by ID**, **PUT**, **PATCH**, and **DELETE**, powered by **SQLite**.

---

## 📁 Proper Folder Structure

```
simple_project_django/
│
├── manage.py                   # Django command-line execution entrypoint
├── requirements.txt            # Project dependencies (Django, Django REST Framework)
├── .gitignore                  # Git ignore rules for venv, sqlite db, cache files
├── db.sqlite3                  # SQLite Database (generated upon running migrations)
├── README.md                   # Complete documentation and API guide
│
├── student_management/         # Project Root Configuration
│   ├── __init__.py             # Marks the directory as a Python package
│   ├── asgi.py                 # ASGI configuration for async web servers
│   ├── settings.py             # Global settings (INSTALLED_APPS, DATABASES, etc.)
│   ├── urls.py                 # Root URL router (includes student API routes)
│   └── wsgi.py                 # WSGI configuration for production deployment
│
└── students/                   # Students Application
    ├── __init__.py             # Marks the directory as a Python package
    ├── admin.py                # Django Admin configuration for Student model
    ├── apps.py                 # Application configuration
    ├── models.py               # Student model schema (fields, table definition)
    ├── serializers.py          # Serializer for request validation & JSON conversion
    ├── urls.py                 # App-level endpoints (/students/, /students/<id>/)
    ├── views.py                # CRUD views (GET, POST, GET ID, PUT, PATCH, DELETE)
    ├── tests.py                # Unit test suite covering all 6 CRUD operations
    └── migrations/             # Database migration files
        ├── 0001_initial.py     # Initial migration creating the students table
        └── __init__.py
```

---

## 🗄️ Database Configuration (SQLite)

This project uses **SQLite 3**, configured directly in `student_management/settings.py`:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

No external database installation or setup is required. The database file `db.sqlite3` is automatically created and maintained in the project root directory.

---

## 📋 Student Model Fields

| Field Name | Type | Description | Constraints |
| :--- | :--- | :--- | :--- |
| `id` | BigAutoField | Primary Key | Auto-incrementing |
| `first_name` | CharField(100) | First name of the student | Required |
| `last_name` | CharField(100) | Last name of the student | Required |
| `email` | EmailField | Email address | Unique, Required |
| `roll_number` | CharField(50) | Student roll / registration number | Unique, Required |
| `course` | CharField(100) | Course or Department enrolled | Required |
| `age` | PositiveIntegerField | Age of the student | Required |
| `created_at` | DateTimeField | Creation timestamp | Auto-generated |
| `updated_at` | DateTimeField | Last updated timestamp | Auto-updated |

---

## 🚀 Setup & Installation Instructions

### 1. Clone / Navigate to the Project Directory
```bash
cd simple_project_django
```

### 2. Create and Activate a Virtual Environment

**On Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**On Windows (CMD):**
```cmd
python -m venv venv
.\venv\Scripts\activate.bat
```

**On Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations (Initialize SQLite DB)
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. (Optional) Create Superuser for Django Admin
```bash
python manage.py createsuperuser
```
Access Django Admin at: `http://127.0.0.1:8000/admin/`

### 6. Run the Development Server
```bash
python manage.py runserver
```
The server will start at: `http://127.0.0.1:8000/`

---

## 📡 API Endpoints Reference

Base URL: `http://127.0.0.1:8000/api/`

| HTTP Method | Endpoint | Operation | Success Code | Error Code |
| :--- | :--- | :--- | :--- | :--- |
| **GET** | `/api/students/` | Get list of all students | `200 OK` | `500 Internal Error` |
| **POST** | `/api/students/` | Create a new student | `201 Created` | `400 Bad Request` |
| **GET** | `/api/students/<id>/` | Get student details by ID | `200 OK` | `404 Not Found` |
| **PUT** | `/api/students/<id>/` | Full update of a student | `200 OK` | `400 Bad Request` / `404 Not Found` |
| **PATCH** | `/api/students/<id>/` | Partial update of a student | `200 OK` | `400 Bad Request` / `404 Not Found` |
| **DELETE** | `/api/students/<id>/` | Delete a student | `204 No Content`| `404 Not Found` |

---

## 🧪 Request & Response Examples (cURL & JSON)

### 1. POST - Create Student
- **Endpoint**: `POST http://127.0.0.1:8000/api/students/`
- **cURL**:
  ```bash
  curl -X POST http://127.0.0.1:8000/api/students/ \
    -H "Content-Type: application/json" \
    -d '{
      "first_name": "John",
      "last_name": "Doe",
      "email": "john.doe@example.com",
      "roll_number": "STU101",
      "course": "Computer Science",
      "age": 20
    }'
  ```
- **Response (201 Created)**:
  ```json
  {
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "roll_number": "STU101",
    "course": "Computer Science",
    "age": 20,
    "created_at": "2026-11-19T02:20:00Z",
    "updated_at": "2026-11-19T02:20:00Z"
  }
  ```

---

### 2. GET - List All Students
- **Endpoint**: `GET http://127.0.0.1:8000/api/students/`
- **cURL**:
  ```bash
  curl -X GET http://127.0.0.1:8000/api/students/
  ```
- **Response (200 OK)**:
  ```json
  [
    {
      "id": 1,
      "first_name": "John",
      "last_name": "Doe",
      "email": "john.doe@example.com",
      "roll_number": "STU101",
      "course": "Computer Science",
      "age": 20,
      "created_at": "2026-11-19T02:20:00Z",
      "updated_at": "2026-11-19T02:20:00Z"
    }
  ]
  ```

---

### 3. GET (by ID) - Retrieve Student by ID
- **Endpoint**: `GET http://127.0.0.1:8000/api/students/1/`
- **cURL**:
  ```bash
  curl -X GET http://127.0.0.1:8000/api/students/1/
  ```
- **Response (200 OK)**:
  ```json
  {
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "roll_number": "STU101",
    "course": "Computer Science",
    "age": 20,
    "created_at": "2026-11-19T02:20:00Z",
    "updated_at": "2026-11-19T02:20:00Z"
  }
  ```
- **Response (404 Not Found)** if student ID does not exist:
  ```json
  {
    "detail": "No Student matches the given query."
  }
  ```

---

### 4. PUT - Full Update Student
Updates **all** editable fields.
- **Endpoint**: `PUT http://127.0.0.1:8000/api/students/1/`
- **cURL**:
  ```bash
  curl -X PUT http://127.0.0.1:8000/api/students/1/ \
    -H "Content-Type: application/json" \
    -d '{
      "first_name": "Jonathan",
      "last_name": "Doe",
      "email": "jonathan.doe@example.com",
      "roll_number": "STU101",
      "course": "Software Engineering",
      "age": 21
    }'
  ```
- **Response (200 OK)**:
  ```json
  {
    "id": 1,
    "first_name": "Jonathan",
    "last_name": "Doe",
    "email": "jonathan.doe@example.com",
    "roll_number": "STU101",
    "course": "Software Engineering",
    "age": 21,
    "created_at": "2026-11-19T02:20:00Z",
    "updated_at": "2026-11-19T02:25:00Z"
  }
  ```

---

### 5. PATCH - Partial Update Student
Updates **only** specified fields without overwriting other fields.
- **Endpoint**: `PATCH http://127.0.0.1:8000/api/students/1/`
- **cURL**:
  ```bash
  curl -X PATCH http://127.0.0.1:8000/api/students/1/ \
    -H "Content-Type: application/json" \
    -d '{
      "course": "Artificial Intelligence"
    }'
  ```
- **Response (200 OK)**:
  ```json
  {
    "id": 1,
    "first_name": "Jonathan",
    "last_name": "Doe",
    "email": "jonathan.doe@example.com",
    "roll_number": "STU101",
    "course": "Artificial Intelligence",
    "age": 21,
    "created_at": "2026-11-19T02:20:00Z",
    "updated_at": "2026-11-19T02:30:00Z"
  }
  ```

---

### 6. DELETE - Delete Student
Deletes the student record from SQLite database.
- **Endpoint**: `DELETE http://127.0.0.1:8000/api/students/1/`
- **cURL**:
  ```bash
  curl -X DELETE http://127.0.0.1:8000/api/students/1/
  ```
- **Response**: `204 No Content` (Empty body)

---

## 🧪 Running Automated Tests

Run the pre-configured test suite verifying all 6 CRUD operations:
```bash
python manage.py test
```
**Expected output:**
```
Found 7 test(s).
Creating test database for alias 'default'...
.......
----------------------------------------------------------------------
Ran 7 tests in 0.139s

OK
Destroying test database for alias 'default'...
```
