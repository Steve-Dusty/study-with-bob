"""
Tutor Agent - Generates hints and guidance without giving away answers
"""
from typing import Dict, Any
from app.services.llm_service import LLMService

class TutorAgent:
    """AI Tutor that provides hints and guidance"""
    
    def __init__(self):
        self.llm = LLMService()
    
    async def generate_hint(
        self,
        problem: Dict[str, Any],
        student_answer: str,
        attempt_number: int,
        assessment: Dict[str, Any]
    ) -> str:
        """
        Generate a contextual hint based on student's attempt.
        
        Rules:
        - NEVER give the full answer
        - Progressive hints: more specific with each attempt
        - Focus on conceptual understanding
        - Guide toward the solution method
        """
        
        # Progressive hint strategy
        hint_level = min(attempt_number, 3)
        
        prompt = f"""
        You are Bob, a patient and encouraging AI tutor. A student is working on this problem:
        
        Problem: {problem['question']}
        Expected approach: {problem.get('topic', 'mathematics')}
        
        The student submitted: {student_answer}
        This is attempt #{attempt_number}.
        
        Assessment notes: {assessment.get('error_type', 'incorrect')}
        
        Generate a hint that:
        1. NEVER reveals the complete answer
        2. Guides them toward the correct approach
        3. Is appropriate for attempt #{hint_level}:
           - Attempt 1: Very general guidance
           - Attempt 2: Point to specific concept/formula
           - Attempt 3+: More specific step-by-step guidance
        4. Is encouraging and builds confidence
        
        Return ONLY the hint text, no other commentary.
        """
        
        hint = await self.llm.generate_text(prompt, max_tokens=150)
        return hint.strip()
    
    async def generate_nudge(
        self,
        problem: Dict[str, Any],
        attempt_count: int
    ) -> str:
        """
        Generate a gentle nudge when student is inactive/stuck.
        """
        
        prompt = f"""
        A student has been working on this problem for a while and seems stuck:
        
        Problem: {problem['question']}
        Attempts so far: {attempt_count}
        
        Generate a gentle, encouraging nudge that:
        1. Acknowledges the challenge
        2. Suggests a way to approach the problem
        3. Is brief (1-2 sentences)
        4. Doesn't give away the answer
        
        Example: "This one's tricky! Try breaking it down step by step. What's the first operation you need to do?"
        
        Return ONLY the nudge text.
        """
        
        nudge = await self.llm.generate_text(prompt, max_tokens=100)
        return nudge.strip()
    
    async def generate_study_reminder(
        self,
        topic: str,
        last_reviewed: str,
        strength: float
    ) -> str:
        """
        Generate a reminder for spaced repetition review.
        """
        
        prompt = f"""
        Generate a friendly reminder for a student to review a topic:
        
        Topic: {topic}
        Last reviewed: {last_reviewed}
        Retention strength: {strength:.0%}
        
        Create a brief, motivating message (1-2 sentences) encouraging them to review.
        
        Example: "Time to refresh your {topic} skills! A quick review now will help you remember for the long term."
        
        Return ONLY the reminder text.
        """
        
        reminder = await self.llm.generate_text(prompt, max_tokens=80)
        return reminder.strip()

