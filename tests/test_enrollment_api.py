from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_duplicate_enrollment():
    response = client.post(
        "/enrollments",
        json={
            "student_id": 1,
            "course_id": 4,
            "semester_id": 1
        }
    )

    assert response.status_code == 409


def test_invalid_student():
    response = client.post(
        "/enrollments",
        json={
            "student_id": 9999,
            "course_id": 4,
            "semester_id": 1
        }
    )

    assert response.status_code == 404


def test_invalid_course():
    response = client.post(
        "/enrollments",
        json={
            "student_id": 1,
            "course_id": 9999,
            "semester_id": 1
        }
    )

    assert response.status_code == 404


def test_invalid_semester():
    response = client.post(
        "/enrollments",
        json={
            "student_id": 1,
            "course_id": 1,
            "semester_id": 9999
        }
    )

def test_get_student_courses():
    response = client.get(
        "/students/1/semesters/1/courses"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["student_id"] == 1
    assert data["semester_id"] == 1
    assert len(data["courses"]) == 2


def test_get_courses_no_records():
    response = client.get(
        "/students/9999/semesters/1/courses"
    )

    assert response.status_code == 404    

    assert response.status_code == 404