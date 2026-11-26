from pydantic import BaseModel, Field


class Course(BaseModel):
    course_code: str
    course_title: str
    credit_units: int = Field(gt=0)