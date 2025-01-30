from fastapi import FastAPI
from app.api.students import router as student_router
from app.middleware.logging import logging_middleware

app = FastAPI(title="University Registration API")

# Use FastAPI's add_middleware directly
app.middleware("http")(logging_middleware)
app.include_router(student_router, tags=["students"])

@app.get("/")
def root():
    return {"message": "Welcome to University Registration System"}