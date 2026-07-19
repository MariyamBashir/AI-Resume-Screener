from fastapi import FastAPI
from app.routes.upload import router as upload_router
from app.routes.job_description import router as job_description_router

app = FastAPI(
    title="AI Resume Screener API",
    description="Backend for AI Resume Screener",
    version="1.0.0"
)

app.include_router(upload_router)
app.include_router(job_description_router)

@app.get("/")
def home():
    return {
        "message": "AI Resume Screener Backend is Running!"
    }