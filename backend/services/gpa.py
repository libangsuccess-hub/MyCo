def calculate_gpa(courses):
    total_weighted_points = 0
    total_credit_units = 0

    for course in courses:
        credit_units = course["credit_units"]
        grade_point = course["grade_point"]

        if not isinstance(credit_units, int) or isinstance(credit_units, bool):
            raise ValueError("Credit units must be an integer.")

        if credit_units <= 0:
            raise ValueError("Credit units must be greater than zero.")

        if grade_point is None:
            continue

        if not isinstance(grade_point, (int, float)) or isinstance(grade_point, bool):
            raise ValueError("Grade point must be a number.")

        if grade_point < 0 or grade_point > 5:
            raise ValueError("Grade point must be between 0 and 5.")

        total_weighted_points += credit_units * grade_point
        total_credit_units += credit_units

    if total_credit_units == 0:
        return 0.0

    return round(total_weighted_points / total_credit_units, 2)