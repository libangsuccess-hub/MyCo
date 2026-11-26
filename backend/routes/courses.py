from fastapi import APIRouter
from backend.models.course import Course

router = APIRouter()


@router.post("/courses")
def add_course(course: Course):
    return {
        "message": "Course received successfully",
        "course": course
    }