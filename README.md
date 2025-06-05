# Kuraztech

# 📝 Task Manager API

A simple Django-based Task Manager API with CRUD support, filtering, validation, and a basic frontend info page. Built using Django REST Framework.

---

## 🚀 Features

- Full CRUD operations (`GET`, `POST`, `PUT`, `DELETE`)
- Task filtering by status (`finished`, `pending`)
- Title validation (must not be empty)
- Timestamp fields: `created_at` and `last_updated_at`
- Frontend info page listing all available API endpoints

---

## 📦 API Endpoints

| Method | Endpoint                     | Description                |
|--------|------------------------------|----------------------------|
| GET    | `/api/tasks/`                | List all tasks             |
| POST   | `/api/tasks/`                | Create a new task          |
| GET    | `/api/tasks/<id>/`           | Retrieve a task by ID      |
| PUT    | `/api/tasks/<id>/`           | Update a task completely   |
| PATCH  | `/api/tasks/<id>/`           | Partially update a task    |
| DELETE | `/api/tasks/<id>/`           | Delete a task              |
| GET    | `/api/tasks/?status=finished`| Filter tasks (finished)    |
| GET    | `/api/tasks/?status=pending` | Filter tasks (pending)     |
| GET    | `/api-info/`                 | Frontend API info page     |

---