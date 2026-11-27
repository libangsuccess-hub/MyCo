from backend.database.connection import get_connection


def update_student_score(enrollment_id, score):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                UPDATE enrollments
                SET score = %s
                WHERE id = %s
                RETURNING id;
                """,
                (score, enrollment_id)
            )

            result = cursor.fetchone()

        if result is None:
            connection.rollback()
            return None

        connection.commit()
        return result[0]

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()