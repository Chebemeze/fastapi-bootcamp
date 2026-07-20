from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

students = [{"id": 1, "name": "Chebem"},
            {"id": 2, "name": "Ada"},
            ]

#Student class utilizing pydantic base model
class Student(BaseModel):
    id: int
    name: str

@app.get("/students/{student_id}") #GET api
def get_students(student_id: int): #it gets student record
    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(status_code = 404,
        detail = "Student not found" 
    )

@app.post("/students") #POST api
def create_student(student:Student): #create new student record
    students.append(student)
    return {
        "message": f"{student.name} was successfully added",
        "student": student
    }

#Adds a course to a list of courses
courses = [{"name": "Calculus", "credit": 3, "course_code": 400},] # list of courses

#course class utilizing pydantic base model
class Course(BaseModel):
    name: str
    credit: int
    course_code: int

@app.get("/courses/{course_code}")
def get_courses(course_code: int):
    for course in courses:
        if course["course_code"] == course_code:
            return course
    raise HTTPException(
        status_code = 404,
        detail = "course not found"
    )

@app.post("/courses")
def create_courses(course:Course):
    courses.append(course)
    return {
        "message": f"you have successfully added {course.name}",
        "course": course
    }
