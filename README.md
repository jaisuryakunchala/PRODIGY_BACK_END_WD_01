# User CRUD API

A simple **REST API** built with **FastAPI** to perform **CRUD operations** on users.  
Each user has a **UUID**, `name`, `email`, and `age`. The API uses an **in-memory database** (Python dictionary) and includes **validation** and **proper error handling**.

---
##  Features
**Create, Read, Update, Delete** users
- Unique **UUID** for each user
- Input validation:
  - Name: 2–50 characters
  - Email: Valid email format
  - Age: 1–149
- Proper HTTP **status codes**:
  - `201 Created` → User created
  - `200 OK` → Successful GET/PUT
  - `204 No Content` → Successful DELETE
  - `404 Not Found` → User not found
  - `400 Bad Request` → Invalid input
- **Swagger UI** for API documentation
- Lightweight, **in-memory storage** (good for testing/prototyping)

---

## Installation

1. Clone the repository:
  git clone https://github.com/your-username/user-crud-api.git
  cd user-crud-api
2.Create a virtual environment (optional but recommended):
  python -m venv venv
3. Activate the virtual environment:
   Windows:"venv\Scripts\activate"
   macOS/Linux:"source venv/bin/activate"
4. Install dependencies:
   pip install fastapi uvicorn pydantic[email]
5.Running the API:
  Start the FastAPI server: "python -m uvicorn main:app --reload"
6. Open in browser:
   Swagger UI: "http://127.0.0.1:8000/docs"
   Redoc documentation: "http://127.0.0.1:8000/redoc"

 
 
 END POINTS:
| Method | Endpoint           | Description       |
| ------ | ------------------ | ----------------- |
| GET    | `/`                | Check API status  |
| POST   | `/users`           | Create a new user |
| GET    | `/users`           | Get all users     |
| GET    | `/users/{user_id}` | Get user by ID    |
| PUT    | `/users/{user_id}` | Update user by ID |
| DELETE | `/users/{user_id}` | Delete user by ID |




