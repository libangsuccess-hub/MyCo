from fastapi import FastAPI
from backend.routes.courses import router as courses_router
from backend.routes.gpa import router as gpa_router
from backend.routes.enrollments import router as enrollments_router
app = FastAPI()

app.include_router(courses_router)
app.include_router(gpa_router)
app.include_router(enrollments_router)


@app.get("/")
def home():
    return {"message": "Welcome to MyCo"}


@app.get("/about")
def about():
    return {
        "name": "MyCo",
        "description": "A student academic and learning management platform",
        "status": "Under development",
        "version": "0.1.0"
    }