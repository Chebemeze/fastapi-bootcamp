from fastapi import FastAPI

app = FastAPI()

students = [{"id": 1, "name": "Chebem"},
            {"id": 2, "name": "Ada"},
            ]

@app.get("/students") #GET api
def get_students(): #it gets student record
    return students

@app.post("/students") #POST api
def create_student(student:dict): #create new student record
    students.append(student)
    return {
        "message": "student was successfully added",
        "name": student
    }
