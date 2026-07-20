# AI Resume Screener

## Overview

AI Resume Screener is a web application that analyzes a resume against a job description using Google's Gemini API.

## Features

- Upload PDF or DOCX resume
- Enter a job description
- Extract resume text
- Analyze resume with AI
- Display AI response in the frontend

## Tech Stack

### Frontend
- Next.js
- React
- TypeScript
- Tailwind CSS

### Backend
- FastAPI
- Python
- Gemini API

## Project Structure

AI-Resume-Screener/
├── backend/
├── frontend/

## Run Backend

```bash
cd backend
uvicorn app.main:app --reload
```

## Run Frontend

```bash
cd frontend
npm run dev
```

## API Endpoints

- POST /upload-resume
- POST /job-description
- POST /analyze-resume

## Author

Maryam Bashir