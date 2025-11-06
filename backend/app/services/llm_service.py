"""
LLM Service - Mock implementation with hardcoded responses (No API keys needed!)
"""
from typing import Optional, List
import asyncio
import random
from PIL import Image

class LLMService:
    """
    Mock LLM service that provides realistic responses without API calls.
    Perfect for demo and development!
    """
    
    def __init__(self, preferred_provider: str = "mock"):
        self.preferred_provider = "mock"
        print("Mock LLM service initialized (no API keys needed!)")
    
    async def generate_text(
        self,
        prompt: str,
        max_tokens: int = 500,
        temperature: float = 0.7,
        provider: Optional[str] = None
    ) -> str:
        """
        Generate mock text responses based on prompt context.
        No API calls needed!
        """
        # Simulate API delay
        await asyncio.sleep(0.5)
        
        prompt_lower = prompt.lower()
        
        # Generate contextual hints
        if "hint" in prompt_lower or "guidance" in prompt_lower:
            hints = [
                "Remember the formula: (a-b)² = a² - 2ab + b²",
                "Try expanding step by step: first multiply (x-1)(x-1), then combine like terms",
                "What is x times x? What is x times -1? And -1 times -1? Now add them all together!",
                "Think about the distributive property. Multiply each term in the first bracket by each term in the second.",
                "Start by writing out: (x-1) × (x-1), then work through each multiplication systematically."
            ]
            return random.choice(hints)
        
        # Generate nudges
        elif "stuck" in prompt_lower or "nudge" in prompt_lower:
            nudges = [
                "This one's tricky! Try breaking it down step by step. What's the first operation you need to do?",
                "Don't give up! Start with the basics - what formula applies here?",
                "Take a deep breath. Sometimes drawing it out helps. Can you visualize this problem?",
                "You're close! Review the key concept and try again.",
                "Stuck? That's totally normal! Try approaching it from a different angle."
            ]
            return random.choice(nudges)
        
        # Generate success feedback
        elif "correct" in prompt_lower or "success" in prompt_lower:
            return """{
                "correct": true,
                "explanation": "Excellent work! You correctly expanded the binomial using (a-b)² = a² - 2ab + b². This formula is essential for many algebraic manipulations.",
                "nextSteps": "Ready to try a more challenging problem? Let's move on to trinomials!"
            }"""
        
        # Generate assessment
        elif "assess" in prompt_lower or "evaluate" in prompt_lower:
            return """{
                "correct": false,
                "confidence": 0.85,
                "error_type": "sign_error",
                "reasoning": "The structure is correct, but there's a sign error in the middle term. Check the -2ab part of the formula."
            }"""
        
        # Default response
        else:
            return "That's a great question! Let's work through this step by step."
    
    async def analyze_image(
        self,
        image: Image.Image,
        prompt: str,
        provider: Optional[str] = None
    ) -> str:
        """
        Mock image analysis - simulates handwriting recognition.
        Returns realistic mathematical expressions based on common problems.
        """
        # Simulate processing time
        await asyncio.sleep(0.8)
        
        prompt_lower = prompt.lower()
        
        # Return different mock answers based on context
        if "(x-1)" in prompt_lower or "(x - 1)" in prompt_lower:
            # For expanding (x-1)²
            mock_answers = [
                "x**2 - 2*x + 1",  # Correct
                "x^2 - 2x + 1",    # Correct (different notation)
                "x**2 - x + 1",    # Common error (wrong middle term)
                "x**2 + 2*x + 1",  # Sign error
            ]
            return random.choice(mock_answers)
        
        elif "2x" in prompt_lower and "=" in prompt_lower:
            # For solving 2x + 5 = 13
            mock_answers = [
                "x = 4",           # Correct
                "4",               # Correct (just the number)
                "x = 8",           # Calculation error
            ]
            return random.choice(mock_answers)
        
        elif "derivative" in prompt_lower or "3x" in prompt_lower:
            # For derivatives
            mock_answers = [
                "6*x + 2",         # Correct for f(x) = 3x² + 2x - 5
                "6x + 2",          # Correct (different notation)
                "6*x",             # Forgot constant term derivative
            ]
            return random.choice(mock_answers)
        
        # Default: return a generic mathematical expression
        return "x**2 - 2*x + 1"
    
    async def batch_generate(
        self,
        prompts: List[str],
        max_tokens: int = 500
    ) -> List[str]:
        """Generate mock completions for multiple prompts in parallel"""
        tasks = [
            self.generate_text(prompt, max_tokens=max_tokens)
            for prompt in prompts
        ]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        return [
            result if not isinstance(result, Exception) else "Demo response"
            for result in results
        ]

