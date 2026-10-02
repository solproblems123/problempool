from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from analyzers.japanese import analyze_text
from generators.japanese_qg import generate_questions

router = APIRouter()

class AnalyzeRequest(BaseModel):
    text: str = Field(min_length=1)
    max_questions: int = Field(default=5, ge=1, le=50)

@router.post("/analyze")
def analyze(req: AnalyzeRequest):
    try:
        analysis = analyze_text(req.text)
        questions = generate_questions(analysis, max_questions=req.max_questions)
        return {"analysis": analysis, "questions": questions}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
