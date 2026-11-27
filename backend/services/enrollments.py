from backend.database.connection import get_connection


def get_student_courses(student_id, semester_id):
    connection = get_connection()

    query = """
        SELECT
            courses.course_code,
            courses.course_title,
            courses.credit_units,
            enrollments.score,
            grading_rules.grade
        FROM enrollments
        JOIN courses
            ON enrollments.course_id = courses.id
        LEFT JOIN grading_rules
            ON enrollments.score BETWEEN grading_rules.min_score
            AND grading_rules.max_score
        AND grading_rules.policy_id = 1
        WHERE enrollments.student_id = %s
        AND enrollments.semester_id = %s
        ORDER BY courses.course_code;
    """

    try:
        with connection.cursor() as cursor:
            cursor.execute(query, (student_id, semester_id))
            records = cursor.fetchall()

        return [
            {
                "course_code": record[0],
                "course_title": record[1],
                "credit_units": record[2],
                "score": record[3],
                "grade": record[4]
            }
            for record in records
        ]

    finally:
        connection.close()