from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome to BuildFlow AI"
    }

@app.get("/about")
def about():
    return {
        "Developer": "Eze Chebem",
        "role": "Mechanical Engineer turned AI Full stack Developer"
    }

@app.get("/age")
def age():
    return {
        "age": 10
    }