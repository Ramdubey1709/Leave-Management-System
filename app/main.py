from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"Leave-Management-System": "Welcome to the Leave Management System API!"}