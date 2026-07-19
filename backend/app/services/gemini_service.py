import os
import google.generativeai as genai
from dotenv import load_dotenv
import json
from app.models.response_model import ResumeResponse

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")


def analyze_resume(prompt: str):
    try:
        response = model.generate_content(prompt)

        data = json.loads(response.text)

        validated = ResumeResponse(**data)

        return validated.model_dump()

    except Exception as e:
        return {
        "error": str(e)
         }


