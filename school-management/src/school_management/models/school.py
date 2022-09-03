from enum import Enum

from pydantic import BaseModel


class Student(BaseModel):
    id : int
    first_name: str
    family_name: str


class Grade(BaseModel):
    topic_id : int
    student_id : int
    grade : float 


class Topic(BaseModel):
    id : int
    name : str


class Group(BaseModel):
    students: list[Student]
    topics : list[Topic]
    topic_weights : dict[str, float]
    grades: list[Grade]
    
class Results(BaseModel):
    Mathematics: float
    Physics: float
    Geography: float
    global_grade: float
    success: bool
