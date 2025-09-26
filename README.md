<<<<<<< HEAD
# Zippee Assessment - Task Management API

A Django REST Framework-based Task Management API with authentication, role-based permissions, and CRUD operations.

## 🚀 Features

- **Task Management**: Create, read, update, and delete tasks
- **User Authentication**: Custom user model with role-based access control
- **Permission System**: Role-based permissions (Admin, Manager, User)
- **Filtering & Search**: Filter tasks by completion status and search by title/description
- **Pagination**: Cursor-based pagination for efficient data loading
- **API Documentation**: RESTful API endpoints

## 🏗️ Project Structure

```
zippee_assessment/
├── authentication/           # User authentication app
│   ├── models.py            # Custom user model
│   ├── serializers.py       # User serializers
│   ├── views.py             # Authentication views
│   └── urls.py              # Authentication URLs
├── tasks/                   # Task management app
│   ├── models.py            # Task model
│   ├── serializers.py       # Task serializers
│   ├── views.py             # Task API views
│   ├── tests.py             # Unit tests
│   └── urls.py              # Task URLs
├── zippee_assessment/       # Main project directory
│   ├── settings.py          # Django settings
│   ├── permissions.py       # Custom permissions
│   └── urls.py              # Main URL configuration
├── manage.py                # Django management script
└── README.md                # This file
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- pip
- Virtual environment (recommended)

### 1. Clone the Repository
```bash
git clone <repository-url>
cd zippee_assessment
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 6. Run Development Server
```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

## 📚 API Endpoints

### Authentication
- `POST /auth/register/` - User registration
- `POST /auth/login/` - User login

### Tasks
| Method | Endpoint | Description | Permissions |
|--------|----------|-------------|-------------|
| `GET` | `/tasks/` | List all tasks (with filtering & pagination) | Public |
| `GET` | `/tasks/{id}/` | Get specific task | Public |
| `POST` | `/tasks/` | Create new task | Authenticated + UserPermission |
| `PUT` | `/tasks/{id}/` | Update task | Authenticated + ManagerPermission |
| `DELETE` | `/tasks/{id}/` | Delete task | Authenticated + ManagerPermission |

### Query Parameters for Task List
- `completed=true/false` - Filter by completion status
- `search=<term>` - Search in title and description

### Example API Response
```json
{
  "next": "http://localhost:8000/tasks/?cursor=cD0yMDI0LTA5LTI2KzA5%3A30%3A00",
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Sample Task",
      "description": "Task description",
      "completed": false,
      "created_at": "2024-09-26T09:30:00Z",
      "updated_at": "2024-09-26T09:30:00Z"
    }
  ],
  "task_summary": {
    "total_tasks": 10,
    "completed_tasks": 5,
    "incomplete_tasks": 5,
    "filtered_count": 1
  }
}
```

### TEST CASES
- To run test cases app wise

**TASK** - "python manage.py test tasks"


## 🔐 Authentication & Permissions

### User Roles
- **Admin**: Full access to all operations
- **Manager**: Can create, read, update, and delete tasks
- **User**: Can create and read tasks

### Permission Classes
- `AdminPermission`: Admin-only access
- `ManagerPermission`: Manager and Admin access
- `UserPermission`: All authenticated users



### Django Settings
Key settings in `settings.py`:
- Custom user model: `AUTH_USER_MODEL = 'authentication.CustomUser'`
- REST Framework configuration with pagination
- CORS settings (if needed for frontend)


### POSTMAN Collection JSON for all apis
 - zippee.postman_collection.json contains all the apis you can directly import that in postman and run the apis
=======
# zippee
zippee-assessment
>>>>>>> 276269e1fd920c3915e8fabbb0160bcf5d937f44
