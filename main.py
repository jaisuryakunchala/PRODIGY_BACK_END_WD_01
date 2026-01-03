from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr, Field
from uuid import UUID, uuid4
from typing import Dict

app = FastAPI(title="User CRUD API")

# In-memory database
users_db: Dict[UUID, dict] = {}

class UserCreate(BaseModel):
    name: str = Field(..., min_length=2)
    email: EmailStr
    age: int = Field(..., gt=0, lt=150)

class UserUpdate(BaseModel):
    name: str | None = Field(None, min_length=2)
    email: EmailStr | None = None
    age: int | None = Field(None, gt=0, lt=150)

class User(UserCreate):
    id: UUID

@app.post("/users", response_model=User, status_code=status.HTTP_201_CREATED)
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

@app.get("/users", response_model=list[User])
def get_all_users():
    return list(users_db.values())

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: UUID):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: UUID, user: UserUpdate):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")

    stored_user = users_db[user_id]
    if user.name is not None:
        stored_user["name"] = user.name
    if user.email is not None:
        stored_user["email"] = user.email
    if user.age is not None:
        stored_user["age"] = user.age

    return stored_user

@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: UUID):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del users_db[user_id]
