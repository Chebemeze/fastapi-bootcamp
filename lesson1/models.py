from sqlmodel import SQLModel, Field
from typing import Optional

class Student(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int
    state: str

class StudentUpdate(SQLModel, table = True):
    name: Optional[str]= None
    age: Optional[int]= None
    state: Optional[str]= None