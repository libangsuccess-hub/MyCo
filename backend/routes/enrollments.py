from fastapi import APIRouter, HTTPException
from psycopg.errors import ForeignKeyViolation, UniqueViolation
from backend.models.enrollment import EnrollmentCreate
from backend.database.connection import get_connection
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