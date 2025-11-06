"""
Memory Agent - Handles spaced repetition and student learning memory
"""
from typing import Dict, Any, List
from datetime import datetime, timedelta
import json

class MemoryAgent:
    """Manages student learning memory and spaced repetition scheduling"""
    
    def __init__(self):
        # In production, this would use a real database
        # For now, use in-memory storage
        self.student_memory = {}
        self.spaced_repetition_intervals = [1, 3, 7, 14, 30, 60]  # days
    
    async def record_success(
        self,
        student_id: str,
        topic: str,
        problem_id: int
    ):
        """Record successful problem completion"""
        
        if student_id not in self.student_memory:
            self.student_memory[student_id] = {}
        
        if topic not in self.student_memory[student_id]:
            self.student_memory[student_id][topic] = {
                "strength": 0,
                "level": 0,
                "last_reviewed": None,
                "next_review": None,
                "total_correct": 0,
                "total_attempts": 0
            }
        
        topic_data = self.student_memory[student_id][topic]
        topic_data["total_correct"] += 1
        topic_data["total_attempts"] += 1
        topic_data["strength"] = min(topic_data["strength"] + 0.2, 1.0)
        topic_data["level"] = min(topic_data["level"] + 1, len(self.spaced_repetition_intervals) - 1)
        topic_data["last_reviewed"] = datetime.now().isoformat()
        
        # Schedule next review based on spaced repetition
        next_interval = self.spaced_repetition_intervals[topic_data["level"]]
        topic_data["next_review"] = (datetime.now() + timedelta(days=next_interval)).isoformat()
    
    async def record_attempt(
        self,
        student_id: str,
        problem_id: int,
        answer: str,
        correct: bool
    ):
        """Record an attempt (correct or incorrect)"""
        
        if student_id not in self.student_memory:
            self.student_memory[student_id] = {}
        
        attempt_key = f"problem_{problem_id}"
        if attempt_key not in self.student_memory[student_id]:
            self.student_memory[student_id][attempt_key] = {
                "attempts": 0,
                "history": []
            }
        
        self.student_memory[student_id][attempt_key]["attempts"] += 1
        self.student_memory[student_id][attempt_key]["history"].append({
            "answer": answer,
            "correct": correct,
            "timestamp": datetime.now().isoformat()
        })
    
    async def get_attempt_count(
        self,
        student_id: str,
        problem_id: int
    ) -> int:
        """Get number of attempts for a problem"""
        
        if student_id not in self.student_memory:
            return 0
        
        attempt_key = f"problem_{problem_id}"
        if attempt_key not in self.student_memory[student_id]:
            return 0
        
        return self.student_memory[student_id][attempt_key]["attempts"]
    
    async def get_review_queue(
        self,
        student_id: str
    ) -> List[Dict[str, Any]]:
        """Get topics due for review based on spaced repetition"""
        
        if student_id not in self.student_memory:
            return []
        
        now = datetime.now()
        review_queue = []
        
        for topic, data in self.student_memory[student_id].items():
            if topic.startswith("problem_"):
                continue
            
            if data["next_review"]:
                next_review_date = datetime.fromisoformat(data["next_review"])
                
                if next_review_date <= now:
                    review_queue.append({
                        "topic": topic,
                        "strength": data["strength"],
                        "lastReviewed": data["last_reviewed"],
                        "nextReview": data["next_review"],
                        "priority": "high" if data["strength"] < 0.5 else "medium"
                    })
        
        # Sort by priority and due date
        review_queue.sort(key=lambda x: (x["strength"], x["nextReview"]))
        
        return review_queue
    
    async def get_student_history(
        self,
        student_id: str,
        problem_id: int
    ) -> Dict[str, Any]:
        """Get student's history with a specific problem"""
        
        if student_id not in self.student_memory:
            return {
                "attempts": 0,
                "history": [],
                "last_correct": False
            }
        
        attempt_key = f"problem_{problem_id}"
        if attempt_key not in self.student_memory[student_id]:
            return {
                "attempts": 0,
                "history": [],
                "last_correct": False
            }
        
        data = self.student_memory[student_id][attempt_key]
        last_correct = data["history"][-1]["correct"] if data["history"] else False
        
        return {
            "attempts": data["attempts"],
            "history": data["history"],
            "last_correct": last_correct,
            "problem": {"id": problem_id}  # Would fetch from database
        }
    
    async def get_topic_strength(
        self,
        student_id: str,
        topic: str
    ) -> float:
        """Get student's strength/mastery in a topic (0-1)"""
        
        if student_id not in self.student_memory:
            return 0.0
        
        if topic not in self.student_memory[student_id]:
            return 0.0
        
        return self.student_memory[student_id][topic]["strength"]
    
    async def identify_weak_topics(
        self,
        student_id: str,
        threshold: float = 0.6
    ) -> List[str]:
        """Identify topics where student needs more practice"""
        
        if student_id not in self.student_memory:
            return []
        
        weak_topics = []
        
        for topic, data in self.student_memory[student_id].items():
            if topic.startswith("problem_"):
                continue
            
            if data["strength"] < threshold:
                weak_topics.append(topic)
        
        return weak_topics

