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
        "student": student
    }

#Adds a course to a list of courses
courses = [{"name": "Calculus", "credit": 3, "course_code": 400},] # list of courses

@app.post("/courses")
def create_courses(course:dict):
    courses.append(course)

    return {
        "message": f"you have successfully added {course['name']}",
        "course": course
    }

@app.get("/courses")
def get_courses():
    return {
        courses
    }