from fastapi import FastAPI
from pydantic import BaseModel
from app.db import conn, cursor

app = FastAPI()

# ===== DAY 1: Basic FastAPI Setup =====
# This was our first API to check if server is running

# @app.get("/")
# def home():
#     return {"message": "Leave Management System running"}


# ===== DAY 2: User CRUD Start (POST + GET) =====

# User Model (Request Body Structure)
class User(BaseModel):
    name: str
    email: str
    age: int





# POST(Create User) 

@app.post("/users")
def create_user(user: User):
    query = "INSERT INTO users ( name, email, age) VALUES ( %s, %s, %s)"
    values = ( user.name, user.email, user.age)
    cursor.execute(query, values)
    conn.commit()

    return {"message": "User added to LMS_db"}


# GET (Read Users)

@app.get("/users")
def get_users():
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    return data

# PUT (Update User)

@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):
    query = "UPDATE users SET name = %s, email = %s, age = %s WHERE id = %s"
    values = (updated_user.name, updated_user.email, updated_user.age, user_id)
    cursor.execute(query, values)
    conn.commit()
    return {"message": "User updated"}
    

# Delete User (DELETE)

@app.delete("/users/{user_id}") 
def delete_user(user_id:int):
    query = "DELETE FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    conn.commit()
    return {"message": "User deleted"}