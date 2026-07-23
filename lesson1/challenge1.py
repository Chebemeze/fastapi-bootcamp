from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

students = [{"id": 1, "name": "Chebem","age": 20, "state": "Enugu"},
            {"id": 2, "name": "Ada", "age": 30, "state": "Imo"},
            {"id": 3, "name": "Clinton", "age": 22, "state": "Delta"},
            {"id": 4, "name": "Chebem", "age": 20, "state": "Abia"}
            ]

@app.get("/students")
def get_student(name: Optional[str] = None, age: Optional[int] = None):
    student_list = []
    for student in students:
        if name and age:
            if student["name"].lower() == name.lower() and student["age"] == age:
                student_list.append(student)            
        elif name:
            if student["name"].lower() == name.lower():
                student_list.append(student)
        elif age:
            if student["age"] == age:
                student_list.append(student)
        else:
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

@app.post("/students")
def create_student(student: Student):
    students.append(student)
    return {
        "message": f"You've successfully added {student.name}"
    }

@app.put("/students/{student_id}")
def replace_student(student_id: int, updated_student: Student):
    for index, student in enumerate(students):
        if student["id"] == student_id:
            students[index] = updated_student.model_dump() #model_dump() converts a python object to dictionary
            return {
                "message": f"Successfully updated {students[index]['name']}",
                "detail": students[index]
            }
    raise HTTPException(status_code= 404, detail="Student not Found")

class StudentUpdate(BaseModel):
    name: Optional[str]= None
    age: Optional[int]= None
    state: Optional[str]= None

@app.patch("/students/{student_id}")
def patch_student(student_id:int, updates: StudentUpdate):
    update_data = updates.model_dump(exclude_unset= True) #exclude_unset= True only forms a dictionary of only the data passed by the user

    #dealing with a case where an empty list is passed in request body
    if not update_data:
        raise HTTPException(status_code=404, detail="At least one field must be provided for update")

    for student in students:
        if student["id"] == student_id:
            for key, value in update_data.items():
                student[key] = value
            return {
                "message": "Student successfully updated",
                "Student": student
            }
    raise HTTPException(status_code=404, detail="Student not Found")

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student["id"] == student_id:
            deleted_student = students.pop(index)
            return {
                "message": f"Successfully removed {student["name"]}",
                "student": delete_student
            }
    raise HTTPException(status_code=404, detail="Student not found")
