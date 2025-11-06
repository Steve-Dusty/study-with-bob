from fastapi import APIRouter, HTTPException, BackgroundTasks
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import base64
from io import BytesIO
from PIL import Image

from app.agents.orchestrator import AgentOrchestrator
from app.services.math_parser import MathParser

router = APIRouter()

class Point(BaseModel):
    x: float
    y: float

class Stroke(BaseModel):
    points: List[Point]
    timestamp: int

class AnswerSubmission(BaseModel):
    problemId: int
    imageData: str
    strokes: List[Stroke]
    studentId: Optional[str] = None

class FeedbackResponse(BaseModel):
    correct: bool
    hint: Optional[str] = None
    explanation: Optional[str] = None
    nextSteps: Optional[str] = None
    confidence: float
    attempt: int

@router.post("/check-answer", response_model=FeedbackResponse)
async def check_answer(submission: AnswerSubmission, background_tasks: BackgroundTasks):
    """
    Check student's handwritten answer and provide feedback.
    Uses multi-agent system for comprehensive evaluation.
    """
    try:
        # Decode image
        image_data = submission.imageData.split(',')[1] if ',' in submission.imageData else submission.imageData
        image_bytes = base64.b64decode(image_data)
        image = Image.open(BytesIO(image_bytes))
        
        # Initialize orchestrator
        orchestrator = AgentOrchestrator()
        
        # Get problem details (mock for now)
        problem = {
            "id": submission.problemId,
            "question": "Expand: (x - 1)²",
            "expected_answer": "x**2 - 2*x + 1",
            "topic": "algebra",
            "difficulty": "easy"
        }
        
        # Process submission
        result = await orchestrator.process_student_submission(
            problem=problem,
            image=image,
            strokes=[s.dict() for s in submission.strokes],
            student_id=submission.studentId or "demo_student"
        )
        
        return FeedbackResponse(**result)
        
    except Exception as e:
        print(f"Error processing answer: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/problems/{problem_id}")
async def get_problem(problem_id: int):
    """Get problem details by ID"""
    # Mock implementation
    problems = {
        1: {
            "id": 1,
            "question": "Expand: (x - 1)²",
            "topic": "algebra",
            "difficulty": "easy",
            "hints": [
                "Remember the formula: (a-b)² = a² - 2ab + b²",
                "Try expanding step by step: (x-1)(x-1)",
                "Multiply each term: x·x + x·(-1) + (-1)·x + (-1)·(-1)"
            ]
        },
        2: {
            "id": 2,
            "question": "Solve for x: 2x + 5 = 13",
            "topic": "algebra",
            "difficulty": "easy",
            "hints": [
                "Start by isolating the term with x",
                "Subtract 5 from both sides",
                "Then divide both sides by 2"
            ]
        }
    }
    
    if problem_id not in problems:
        raise HTTPException(status_code=404, detail="Problem not found")
    
    return problems[problem_id]

@router.get("/review-queue/{student_id}")
async def get_review_queue(student_id: str):
    """Get spaced repetition review queue for student"""
    # Mock implementation
    return {
        "studentId": student_id,
        "items": [
            {
                "topic": "Quadratic Formula",
                "lastReviewed": "2025-11-05",
                "nextReview": "2025-11-08",
                "strength": 0.7,
                "priority": "high"
            },
            {
                "topic": "Trigonometry",
                "lastReviewed": "2025-11-04",
                "nextReview": "2025-11-10",
                "strength": 0.5,
                "priority": "medium"
            }
        ]
    }

@router.get("/progress/{student_id}")
async def get_student_progress(student_id: str):
    """Get detailed progress for a student"""
    return {
        "studentId": student_id,
        "overallScore": 85,
        "problemsSolved": 42,
        "accuracy": 82,
        "streak": 5,
        "topicScores": {
            "algebra": 88,
            "geometry": 90,
            "calculus": 75,
            "trigonometry": 80
        },
        "recentActivity": [
            {"date": "2025-11-08", "problems": 5, "score": 90},
            {"date": "2025-11-07", "problems": 8, "score": 85},
            {"date": "2025-11-06", "problems": 6, "score": 78}
        ]
    }

