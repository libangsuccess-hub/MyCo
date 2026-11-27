from fastapi import APIRouter, HTTPException
from backend.services.academic_records import get_academic_courses
from backend.services.gpa import calculate_gpa
from backend.models.gpa import SemesterGPAResponse

router = APIRouter()


@router.get(
    "/students/{student_id}/semesters/{semester_id}/gpa",
    response_model=SemesterGPAResponse
)
def get_semester_gpa(student_id: int, semester_id: int, policy_id: int):
    courses = get_academic_courses(student_id, semester_id, policy_id)

    if not courses:
        raise HTTPException(
            status_code=404,
            detail="No academic records found for this student and semester."
        )

    gpa = calculate_gpa(courses)

    return {
        "student_id": student_id,
        "semester_id": semester_id,
        "gpa": gpa,
        "courses": courses
    }