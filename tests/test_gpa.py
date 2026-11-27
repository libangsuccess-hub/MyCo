import pytest
from backend.services.gpa import calculate_gpa


def test_normal_gpa():
    courses = [
        {"course_code": "CPE321", "credit_units": 3, "grade_point": 5},
        {"course_code": "CPE322", "credit_units": 2, "grade_point": 4},
        {"course_code": "GET321", "credit_units": 3, "grade_point": 3},
        {"course_code": "GST321", "credit_units": 2, "grade_point": 5},
    ]

def test_zero_credit_units_rejected():
    courses = [
        {"course_code": "CPE321", "credit_units": 0, "grade_point": 5}
    ]

    with pytest.raises(ValueError):
        calculate_gpa(courses)


def test_invalid_grade_point_rejected():
    courses = [
        {"course_code": "CPE321", "credit_units": 3, "grade_point": 7}
    ]

    with pytest.raises(ValueError):
        calculate_gpa(courses)


def test_negative_credit_units_rejected():
    courses = [
        {"course_code": "CPE321", "credit_units": -2, "grade_point": 5}
    ]

    with pytest.raises(ValueError):
        calculate_gpa(courses)    


def test_failed_course_counts():
    courses = [
        {"course_code": "CPE321", "credit_units": 3, "grade_point": 5},
        {"course_code": "CPE323", "credit_units": 3, "grade_point": 0},
    ]

    assert calculate_gpa(courses) == 2.5


def test_ungraded_course_is_excluded():
    courses = [
        {"course_code": "CPE321", "credit_units": 3, "grade_point": 5},
        {"course_code": "GET322", "credit_units": 2, "grade_point": None},
    ]

    assert calculate_gpa(courses) == 5.0


def test_no_graded_courses():
    courses = [
        {"course_code": "CPE321", "credit_units": 3, "grade_point": None},
        {"course_code": "GET322", "credit_units": 2, "grade_point": None},
    ]

    assert calculate_gpa(courses) == 0.0