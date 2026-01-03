from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, EmailStr, Field
from uuid import UUID, uuid4
from typing import Dict, List, Optional

app = FastAPI(
    title="User CRUD API",
    description="A simple REST API to manage users with UUID, proper validation and error handling",
    version="1.0.0"
)

# In-memory database
users_db: Dict[UUID, dict] = {}

# Pydantic models
class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    age: int = Field(..., gt=0, lt=150)

class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=50)
    email: Optional[EmailStr] = None
    age: Optional[int] = Field(None, gt=0, lt=150)

class User(UserCreate):
    id: UUID

# Root endpoint
@app.get("/", summary="Check API status")
def root():
    return {"message": "User CRUD API is running"}


# CREATE
@app.post("/users", response_model=User, status_code=status.HTTP_201_CREATED, summary="Create a new user")
def create_user(user: UserCreate):
    user_id = uuid4()
    new_user = {
        "id": user_id,
        "name": user.name,
        "email": user.email,
        "age": user.age
    }
    users_db[user_id] = new_user
    return new_user


# READ ALL
@app.get("/users", response_model=List[User], summary="Get all users")
def get_all_users():
    return list(users_db.values())


# READ BY ID
@app.get("/users/{user_id}", response_model=User, summary="Get user by ID")
def get_user(user_id: UUID):
    if user_id not in users_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return users_db[user_id]


# UPDATE
@app.put("/users/{user_id}", response_model=User, summary="Update user by ID")
def update_user(user_id: UUID, user: UserUpdate):
    if user_id not in users_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    stored_user = users_db[user_id]

    if user.name is not None:
        stored_user["name"] = user.name
    if user.email is not None:
        stored_user["email"] = user.email
    if user.age is not None:
        stored_user["age"] = user.age

    return stored_user


# DELETE
@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete user by ID")
def delete_user(user_id: UUID):
    if user_id not in users_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    del users_db[user_id]
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content=None)


# CUSTOM VALIDATION ERROR HANDLER (optional, converts 422 to 400)
@app.exception_handler(RequestValidationError)
def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": exc.errors(), "body": exc.body}
    )
