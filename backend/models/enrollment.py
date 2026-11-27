from typing import Optional
from decimal import Decimal
from pydantic import BaseModel, Field


class EnrollmentCreate(BaseModel):
    student_id: int = Field(gt=0)
    course_id: int = Field(gt=0)
    semester_id: int = Field(gt=0)


class EnrolledCourseResponse(BaseModel):
    course_code: str
    course_title: str
    credit_units: int
    score: Optional[Decimal] = None
    grade: Optional[str] = None


class StudentCoursesResponse(BaseModel):
    student_id: int
    semester_id: int
    courses: list[EnrolledCourseResponse]