from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_gpa_endpoint():
    response = client.get(
        "/students/1/semesters/1/gpa?policy_id=1"
    )

    assert response.status_code == 200
    assert response.json()["gpa"] == 4.5

def test_gpa_endpoint_no_records():
    response = client.get(
        "/students/9999/semesters/1/gpa?policy_id=1"
    )

    assert response.status_code == 404
    assert response.json()["detail"] == (
        "No academic records found for this student and semester."
    )    