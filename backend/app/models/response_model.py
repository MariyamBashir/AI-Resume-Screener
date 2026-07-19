from pydantic import BaseModel
from typing import List


class ResumeResponse(BaseModel):
    match_score: int
    matched_skills: List[str]
    missing_keywords: List[str]
    suggestions: List[str]