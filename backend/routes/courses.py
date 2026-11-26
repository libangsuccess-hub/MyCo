from fastapi import APIRouter
from backend.models.course import Course
from backend.database.connection import get_connection

router = APIRouter()


@router.post("/courses")
def add_course(course: Course):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO courses (course_code, course_title, credit_units)
                VALUES (%s, %s, %s)
                RETURNING id;
                """,
                (course.course_code, course.course_title, course.credit_units)
            )

            course_id = cursor.fetchone()[0]

        connection.commit()

        return {
            "message": "Course saved successfully",
            "course_id": course_id,
            "course": course
        }

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()