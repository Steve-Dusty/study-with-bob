"""
Feedback Agent - Generates student-friendly feedback and explanations
"""
from typing import Dict, Any
from app.services.llm_service import LLMService

class FeedbackAgent:
    """Generates personalized feedback for students"""
    
    def __init__(self):
        self.llm = LLMService()
    
    async def generate_success_feedback(
        self,
        problem: Dict[str, Any],
        student_answer: str,
        assessment: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Generate encouraging feedback when student gets it right.
        Includes brief explanation of the reasoning.
        """
        
        prompt = f"""
        A student just solved this problem correctly:
        
        Problem: {problem['question']}
        Student's answer: {student_answer}
        
        Generate encouraging feedback that:
        1. Congratulates them (1 sentence)
        2. Briefly explains the key concept/reasoning (2-3 sentences)
        3. Suggests next steps or related topics (1 sentence)
        
        Keep it concise and encouraging. Use a friendly, supportive tone.
        
        Format as JSON:
        {{
            "correct": true,
            "explanation": "Your explanation here",
            "nextSteps": "Next step suggestion"
        }}
        
        Return ONLY valid JSON.
        """
        
        response = await self.llm.generate_text(prompt, max_tokens=200)
        
        try:
            import json
            result = json.loads(response)
            return result
        except:
            # Fallback
            return {
                "correct": True,
                "explanation": "Great job! You correctly solved the problem.",
                "nextSteps": "Ready for the next challenge?"
            }
    
    async def generate_error_feedback(
        self,
        problem: Dict[str, Any],
        student_answer: str,
        error_type: str
    ) -> str:
        """
        Generate specific feedback for common errors.
        More detailed than hints - used after multiple attempts.
        """
        
        prompt = f"""
        A student made this error:
        
        Problem: {problem['question']}
        Student's answer: {student_answer}
        Error type: {error_type}
        
        Provide constructive feedback that:
        1. Identifies what went wrong (without making them feel bad)
        2. Explains the correct concept
        3. Shows how to avoid this error in the future
        
        Keep it supportive and educational. 2-3 sentences.
        
        Return ONLY the feedback text.
        """
        
        feedback = await self.llm.generate_text(prompt, max_tokens=150)
        return feedback.strip()
    
    async def generate_rubric_feedback(
        self,
        submission: str,
        rubric: Dict[str, Any],
        score: int
    ) -> Dict[str, Any]:
        """
        Generate rubric-based feedback for teacher assignments.
        Used in auto-grading feature.
        """
        
        prompt = f"""
        Grade this student submission using the rubric:
        
        Rubric:
        {rubric}
        
        Student submission:
        {submission}
        
        Provide:
        1. Score for each rubric item
        2. Specific feedback on what was done well
        3. Specific feedback on what needs improvement
        
        Format as JSON:
        {{
            "scores": {{"item1": score, "item2": score}},
            "strengths": ["strength 1", "strength 2"],
            "improvements": ["improvement 1", "improvement 2"],
            "overall_feedback": "Summary feedback"
        }}
        
        Return ONLY valid JSON.
        """
        
        response = await self.llm.generate_text(prompt, max_tokens=400)
        
        try:
            import json
            return json.loads(response)
        except:
            return {
                "scores": {},
                "strengths": [],
                "improvements": [],
                "overall_feedback": "Good effort!"
            }

