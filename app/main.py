from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# ===== DAY 1: Basic FastAPI Setup =====
# This was our first API to check if server is running

# @app.get("/")
# def home():
#     return {"message": "Leave Management System running"}


# ===== DAY 2: User CRUD Start (POST + GET) =====

# User Model (Request Body Structure)
class User(BaseModel):
    id: int
    name: str
    email: str
    age: int


# Temporary in-memory database (list)
users = []


# Create User (POST)
@app.post("/users")
def create_user(user: User):
    users.append(user)
    return {"message": "User added", "data": user}


# Get Users (GET)

@app.get("/users")
def get_users():
    return users
# Put User (Update)

@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):
    for index, user in enumerate(users):
        if user.id == user_id:
            users[index] = updated_user
            return {"message": "User updated", "data": updated_user}
    return {"error": "User not found"}

# Delete User (DELETE)
@app.delete("/users/{user_id}") 
def delete_user(user_id:int):
    for index, user in enumerate(users):
        if user.id == user_id:
            users.pop(index)
            return{"message": "user deleted"}
        return {"error": "User not found"}  