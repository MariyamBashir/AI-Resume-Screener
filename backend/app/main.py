from fastapi import FastAPI

app = FastAPI(
    title="AI Resume Screener API",
    description="Backend for AI Resume Screener",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "AI Resume Screener Backend is Running!"
    }