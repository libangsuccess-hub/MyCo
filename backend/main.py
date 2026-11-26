from fastapi import FastAPI
from backend.routes.courses import router as courses_router

app = FastAPI()

app.include_router(courses_router)


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