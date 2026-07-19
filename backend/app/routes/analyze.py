from fastapi import APIRouter, UploadFile, File, Form
import os
import shutil

from app.utils.document_reader import extract_text
from app.prompts.resume_prompt import build_resume_prompt
from app.services.gemini_service import analyze_resume as analyze_with_gemini

router = APIRouter()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/analyze-resume")
async def analyze_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume_text = extract_text(file_path)

    prompt = build_resume_prompt(resume_text, job_description)

    result = analyze_with_gemini(prompt)

    return {
        "response": result
    }