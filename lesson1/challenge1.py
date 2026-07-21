from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

students = [{"id": 1, "name": "Chebem","age": 20, "state": "Enugu"},
            {"id": 2, "name": "Ada", "age": 30, "state": "Imo"},
            {"id": 3, "name": "Clinton", "age": 22, "state": "Delta"},
            {"id": 4, "name": "Chebem", "age": 20, "state": "Abia"}
            ]


@app.get("/search")
def get_student(name: str, age: int):
    student_list = []
    for student in students:
        if student["name"].lower() == name.lower() and student["age"] == age:
            student_list.append(student)

    if student_list:
        return {
            "message": f"Search found {len(student_list)} student(s)",
           "student_list":  student_list
        }

    raise HTTPException(status_code=404, detail= "Student not Found")

class Student(BaseModel):
    id: int
    name: str
    age: int
    state: str

@app.post("/search")
def create_student(student: Student):
    students.append(student)
    return {
        "message": f"You've successfully added {student.name}"
    }
