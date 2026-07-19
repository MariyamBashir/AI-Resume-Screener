from fastapi import APIRouter
from app.models.job_description import JobDescriptionRequest

router = APIRouter()


@router.post("/job-description")
async def submit_job_description(data: JobDescriptionRequest):
    return {
        "message": "Job description received successfully",
        "job_description": data.job_description
    }