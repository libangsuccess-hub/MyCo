from fastapi import APIRouter, HTTPException
from psycopg.errors import ForeignKeyViolation, UniqueViolation
from backend.models.enrollment import EnrollmentCreate
from backend.database.connection import get_connection
from backend.models.enrollment import StudentCoursesResponse
from backend.services.enrollments import get_student_courses

router = APIRouter()


@router.post("/enrollments")
def enroll_student(enrollment: EnrollmentCreate):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO enrollments (
                    student_id,
                    course_id,
                    semester_id
                )
                VALUES (%s, %s, %s)
                RETURNING id;
                """,
                (
                    enrollment.student_id,
                    enrollment.course_id,
                    enrollment.semester_id
                )
            )

            enrollment_id = cursor.fetchone()[0]

        connection.commit()

        return {
            "message": "Student enrolled successfully",
            "enrollment_id": enrollment_id,
            "enrollment": enrollment
        }

    except UniqueViolation:
        connection.rollback()
        raise HTTPException(
            status_code=409,
            detail="This student is already enrolled in this course for this semester."
        )
    except ForeignKeyViolation:
        connection.rollback()
        raise HTTPException(
            status_code=404,
            detail="Student, course, or semester not found."
        )


    finally:
        connection.close()

@router.get(
    "/students/{student_id}/semesters/{semester_id}/courses",
    response_model=StudentCoursesResponse
)
def get_enrolled_courses(student_id: int, semester_id: int):

    courses = get_student_courses(student_id, semester_id)

    if not courses:
        raise HTTPException(
            status_code=404,
            detail="No enrolled courses found for this student and semester."
        )

    return {
        "student_id": student_id,
        "semester_id": semester_id,
        "courses": courses
    }