from decimal import Decimal
from typing import Optional
from pydantic import BaseModel


class AcademicCourseResponse(BaseModel):
    course_code: str
    credit_units: int
    score: Optional[Decimal] = None
    grade: Optional[str] = None
    grade_point: Optional[Decimal] = None


class SemesterGPAResponse(BaseModel):
    student_id: int
    semester_id: int
    gpa: float
    courses: list[AcademicCourseResponse]