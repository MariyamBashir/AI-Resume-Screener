def build_resume_prompt(resume_text: str, job_description: str) -> str:
    return f"""
You are an AI Resume Screener.

Compare the resume against the job description.

Return ONLY valid JSON.

Use exactly this format:

{{
  "match_score": 0,
  "missing_keywords": [],
  "matched_skills": [],
  "suggestions": []
}}

Resume:
{resume_text}

Job Description:
{job_description}
"""