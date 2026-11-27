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

    assert response.status_code == 404