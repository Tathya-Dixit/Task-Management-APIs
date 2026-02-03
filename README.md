# Task Management APIs

A RESTful API for task management with user authentication, built with Django REST Framework.

**Live Demo:** [https://task-management-apis-vxzi.onrender.com](https://task-management-apis-vxzi.onrender.com)  
**GitHub:** [https://github.com/Tathya-Dixit/Task-Management-APIs](https://github.com/Tathya-Dixit/Task-Management-APIs)

## Features

- **User Authentication**
  - JWT-based authentication
  - User registration with email validation
  - Token refresh mechanism

- **Task Management**
  - Create, read, update, delete tasks
  - Task priorities (Low, Normal, High)
  - Task statuses (Pending, In Progress, Done, Archived)
  - Due dates with automatic done_date tracking
  - Category organization

- **Advanced Features**
  - Search tasks by title/description
  - Filter by status, priority, or category
  - Sort by due_date, created_at, or priority
  - Pagination (10 items per page)
  - Per-user data isolation

## Tech Stack

- Django 6.0.1
- Django REST Framework 3.16.1
- PostgreSQL (production) / SQLite (development)
- JWT Authentication
- WhiteNoise for static files

## Installation

1. Clone the repository
```bash
git clone https://github.com/Tathya-Dixit/Task-Management-APIs.git
cd Task-Management-APIs
```

2. Create virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
Create a `.env` file:
```
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOW_ALL_ORIGINS=True
ENVIRONMENT=development
```

5. Run migrations
```bash
python manage.py migrate
```

6. Create superuser (optional)
```bash
python manage.py createsuperuser
```

7. Run development server
```bash
python manage.py runserver
```

## API Endpoints

### Authentication
- `POST /api/v1/auth/register/` - Register new user
- `POST /api/v1/auth/login/` - Login (get tokens)
- `POST /api/v1/auth/refresh/` - Refresh access token
- `POST /api/v1/auth/verify/` - Verify token validity

### Categories
- `GET /api/v1/categories/` - List all categories
- `POST /api/v1/categories/` - Create category
- `GET /api/v1/categories/{id}/` - Get category details
- `PUT/PATCH /api/v1/categories/{id}/` - Update category
- `DELETE /api/v1/categories/{id}/` - Delete category

### Tasks
- `GET /api/v1/tasks/` - List all tasks
- `POST /api/v1/tasks/` - Create task
- `GET /api/v1/tasks/{id}/` - Get task details
- `PUT/PATCH /api/v1/tasks/{id}/` - Update task
- `DELETE /api/v1/tasks/{id}/` - Delete task

### Query Parameters
- **Search**: `?search=meeting`
- **Filter**: `?status=PE&priority=2&category=1`
- **Sort**: `?ordering=-due_date` (prefix with `-` for descending)
- **Pagination**: `?page=2`

## Request Examples

### Register User
```bash
POST /api/v1/auth/register/
Content-Type: application/json

{
  "username": "user",
  "email": "user@example.com",
  "password": "password",
  "password2": "password"
}
```

**Response:**
```json
{
  "user": {
    "username": "user",
    "email": "user@example.com"
  },
  "tokens": {
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
  }
}
```

### Login
```bash
POST /api/v1/auth/login/
Content-Type: application/json

{
  "username": "user",
  "password": "user"
}
```

**Response:**
```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Create Category
```bash
POST /api/v1/categories/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "name": "Work",
  "description": "Work related tasks"
}
```

### Create Task
```bash
POST /api/v1/tasks/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "title": "Complete project",
  "description": "Finish API development",
  "priority": 2,
  "status": "PE",
  "due_date": "2026-02-15T14:30:00Z",
  "category": 1
}
```

**Response:**
```json
{
  "id": 1,
  "title": "Complete project",
  "description": "Finish API development",
  "category": 1,
  "category_details": {
    "id": 1,
    "name": "Work",
    "description": "Work related tasks",
    "created_at": "2026-02-01T10:00:00Z"
  },
  "priority": 2,
  "status": "PE",
  "due_date": "2026-02-15T14:30:00Z",
  "done_date": null,
  "created_at": "2026-02-01T10:00:00Z"
}
```

### Filter & Search
```bash
GET /api/v1/tasks/?status=PE&search=project&ordering=-priority
Authorization: Bearer <access_token>
```

### Update Task Status
```bash
PATCH /api/v1/tasks/1/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "status": "DO"
}
```
*Note: When status is changed to "DO" (Done), the `done_date` field is automatically set.*

## Field Options

### Priority
- `0` - Low
- `1` - Normal (default)
- `2` - High

### Status
- `PE` - Pending (default)
- `IP` - In Progress
- `DO` - Done
- `AR` - Archived

## Authentication

All endpoints except `/api/v1/auth/register/` and `/api/v1/auth/login/` require authentication.

Include the access token in the Authorization header:
```
Authorization: Bearer <your_access_token>
```

**Token Expiry:**
- Access Token: 60 minutes
- Refresh Token: 1 day

**Refresh Access Token:**
```bash
POST /api/v1/auth/refresh/
Content-Type: application/json

{
  "refresh": "<your_refresh_token>"
}
```

## Test Users

- Username: `user1`
- Password: `user1`

## Project Structure

```
task_management/
├── accounts/              # Authentication app
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── tasks/                 # Tasks & Categories app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── task_management/       # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── requirements.txt
└── manage.py
```

## Deployment

For production deployment:

1. Set environment variables:
```
ENVIRONMENT=production
DEBUG=False
SECRET_KEY=your-production-secret-key
ALLOWED_HOSTS=yourdomain.com
DATABASE_URL=postgresql://user:password@host:port/database
CORS_ALLOW_ALL_ORIGINS=False
CORS_ALLOWED_ORIGINS=https://yourfrontend.com
```

2. Collect static files:
```bash
python manage.py collectstatic --no-input
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Use a production WSGI server (Gunicorn included):
```bash
gunicorn task_management.wsgi:application
```

## Error Handling

The API returns standard HTTP status codes:

- `200 OK` - Successful GET, PUT, PATCH
- `201 Created` - Successful POST
- `204 No Content` - Successful DELETE
- `400 Bad Request` - Validation errors
- `401 Unauthorized` - Missing or invalid token
- `403 Forbidden` - Insufficient permissions
- `404 Not Found` - Resource doesn't exist
- `500 Internal Server Error` - Server error

**Error Response Format:**
```json
{
  "field_name": ["Error message"]
}
```

## Author

Tathya Dixit

Project Link: [https://github.com/Tathya-Dixit/Task-Management-APIs](https://github.com/Tathya-Dixit/Task-Management-APIs)  
Live API: [https://task-management-apis-vxzi.onrender.com](https://task-management-apis-vxzi.onrender.com)
