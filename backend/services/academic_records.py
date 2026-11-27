from backend.database.connection import get_connection


def get_academic_courses(student_id, semester_id, policy_id):
    connection = get_connection()

    query = """
        SELECT
            courses.course_code,
            courses.credit_units,
            enrollments.score,
            grading_rules.grade,
            grading_rules.grade_point
        FROM enrollments
        JOIN courses
            ON enrollments.course_id = courses.id
        LEFT JOIN grading_rules
            ON enrollments.score BETWEEN grading_rules.min_score AND grading_rules.max_score
            AND grading_rules.policy_id = %s
        WHERE enrollments.student_id = %s
            AND enrollments.semester_id = %s;
    """

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                query,
                (policy_id, student_id, semester_id)
            )

            records = cursor.fetchall()

        courses = []

        for record in records:
            courses.append({
                "course_code": record[0],
                "credit_units": record[1],
                "score": record[2],
                "grade": record[3],
                "grade_point": record[4]
            })

        return courses

    finally:
        connection.close()