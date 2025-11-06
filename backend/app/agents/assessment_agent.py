"""
Assessment Agent - Evaluates correctness of student answers
"""
from typing import Dict, Any, Optional
from app.services.math_parser import MathParser
from app.services.llm_service import LLMService

class AssessmentAgent:
    """Evaluates student answers for correctness"""
    
    def __init__(self):
        self.math_parser = MathParser()
        self.llm = LLMService()
    
    async def assess(
        self,
        student_answer: str,
        expected_answer: str,
        problem: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Assess if student answer is correct.
        
        Uses two-stage approach:
        1. Symbolic math comparison (SymPy) for exact correctness
        2. LLM reasoning for partial credit and error detection
        """
        
        # Stage 1: Symbolic comparison
        symbolic_result = self.math_parser.compare_expressions(
            student_answer,
            expected_answer
        )
        
        if symbolic_result["equivalent"]:
            return {
                "correct": True,
                "confidence": 0.95,
                "method": "symbolic",
                "reasoning": "Mathematically equivalent to expected answer"
            }
        
        # Stage 2: LLM assessment for partial credit or alternative forms
        llm_assessment = await self._llm_assess(
            student_answer=student_answer,
            expected_answer=expected_answer,
            problem=problem
        )
        
        return llm_assessment
    
    async def _llm_assess(
        self,
        student_answer: str,
        expected_answer: str,
        problem: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Use LLM to assess answer and identify errors.
        """
        
        prompt = f"""
        You are an expert mathematics teacher assessing a student's answer.
        
        Problem: {problem['question']}
        Expected answer: {expected_answer}
        Student's answer: {student_answer}
        
        Analyze the student's answer and respond in JSON format:
        {{
            "correct": true/false,
            "confidence": 0.0-1.0,
            "error_type": "sign_error" | "missing_term" | "wrong_operation" | "correct" | "alternative_form",
            "reasoning": "Brief explanation of your assessment",
            "partial_credit": 0-100 (if applicable)
        }}
        
        Consider:
        - Is it mathematically equivalent but in different form?
        - Is there a common misconception visible?
        - What type of error did they make?
        
        Return ONLY valid JSON.
        """
        
        response = await self.llm.generate_text(prompt, max_tokens=200)
        
        try:
            import json
            result = json.loads(response)
            return result
        except:
            # Fallback if JSON parsing fails
            return {
                "correct": False,
                "confidence": 0.5,
                "error_type": "unknown",
                "reasoning": "Could not assess answer"
            }

