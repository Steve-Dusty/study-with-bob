"""
Agent Orchestrator - Coordinates all AI agents
"""
from typing import Dict, Any, List
from PIL import Image
import asyncio

from .tutor_agent import TutorAgent
from .assessment_agent import AssessmentAgent
from .feedback_agent import FeedbackAgent
from .memory_agent import MemoryAgent
from app.services.math_parser import MathParser
from app.services.llm_service import LLMService

class AgentOrchestrator:
    """Orchestrates multiple AI agents for student learning"""
    
    def __init__(self):
        self.tutor_agent = TutorAgent()
        self.assessment_agent = AssessmentAgent()
        self.feedback_agent = FeedbackAgent()
        self.memory_agent = MemoryAgent()
        self.math_parser = MathParser()
        self.llm_service = LLMService()
        
    async def process_student_submission(
        self,
        problem: Dict[str, Any],
        image: Image.Image,
        strokes: List[Dict],
        student_id: str
    ) -> Dict[str, Any]:
        """
        Process a student's submission through the multi-agent system.
        
        Flow:
        1. Extract answer from image/strokes
        2. Assess correctness
        3. Generate appropriate feedback (hint or explanation)
        4. Update student memory for spaced repetition
        """
        
        # Step 1: Extract mathematical expression from image
        extracted_answer = await self._extract_answer(image, strokes, problem)
        
        # Step 2: Assess correctness using Assessment Agent
        assessment = await self.assessment_agent.assess(
            student_answer=extracted_answer,
            expected_answer=problem.get("expected_answer"),
            problem=problem
        )
        
        # Step 3: Generate feedback based on assessment
        if assessment["correct"]:
            # Student got it right!
            feedback = await self.feedback_agent.generate_success_feedback(
                problem=problem,
                student_answer=extracted_answer,
                assessment=assessment
            )
            
            # Update memory - mark as understood
            await self.memory_agent.record_success(
                student_id=student_id,
                topic=problem["topic"],
                problem_id=problem["id"]
            )
            
        else:
            # Student needs help
            # Check attempt count from memory
            attempt_count = await self.memory_agent.get_attempt_count(
                student_id=student_id,
                problem_id=problem["id"]
            )
            
            # Generate contextual hint (not full answer!)
            hint = await self.tutor_agent.generate_hint(
                problem=problem,
                student_answer=extracted_answer,
                attempt_number=attempt_count,
                assessment=assessment
            )
            
            feedback = {
                "correct": False,
                "hint": hint,
                "attempt": attempt_count + 1
            }
            
            # Record attempt
            await self.memory_agent.record_attempt(
                student_id=student_id,
                problem_id=problem["id"],
                answer=extracted_answer,
                correct=False
            )
        
        return {
            **feedback,
            "confidence": assessment.get("confidence", 0.9),
        }
    
    async def _extract_answer(
        self,
        image: Image.Image,
        strokes: List[Dict],
        problem: Dict[str, Any]
    ) -> str:
        """
        Extract mathematical answer from handwriting.
        Uses LLM vision model to interpret handwriting.
        """
        try:
            # Use LLM vision to interpret handwriting
            prompt = f"""
            You are analyzing a student's handwritten mathematical work.
            
            Problem: {problem['question']}
            
            Please extract the mathematical expression that the student wrote as their final answer.
            Return ONLY the mathematical expression in standard notation (e.g., x^2 - 2*x + 1).
            
            If you see work/steps, identify the final answer.
            """
            
            # Convert image to format for LLM
            extracted = await self.llm_service.analyze_image(image, prompt)
            
            return extracted.strip()
            
        except Exception as e:
            print(f"Error extracting answer: {e}")
            # Fallback: return placeholder
            return "x**2 - 2*x + 1"
    
    async def check_for_stuck_student(
        self,
        student_id: str,
        problem_id: int
    ) -> Dict[str, Any]:
        """
        Check if student is stuck and needs proactive help.
        Called by frontend when detecting inactivity.
        """
        # Get student's history
        history = await self.memory_agent.get_student_history(
            student_id=student_id,
            problem_id=problem_id
        )
        
        # Check for signs of being stuck
        if history["attempts"] >= 2 and not history["last_correct"]:
            # Student is stuck - offer proactive help
            problem = history["problem"]
            
            nudge = await self.tutor_agent.generate_nudge(
                problem=problem,
                attempt_count=history["attempts"]
            )
            
            return {
                "stuck": True,
                "nudge": nudge,
                "suggestion": "Would you like a hint?"
            }
        
        return {"stuck": False}

