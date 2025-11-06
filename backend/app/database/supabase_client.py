"""
Mock Database Client - In-memory storage (No Supabase needed!)
"""
from typing import Optional, Dict, Any, List
from datetime import datetime
import uuid

class SupabaseClient:
    """Mock database using in-memory storage"""
    
    def __init__(self):
        # In-memory storage
        self.students = {}
        self.teachers = {}
        self.problems = {}
        self.submissions = []
        self.assignments = {}
        self.client = None
        
        # Seed with demo data
        self._seed_demo_data()
        print("Mock database initialized (in-memory storage)")
    
    def _seed_demo_data(self):
        """Seed database with demo data"""
        # Demo problems
        self.problems = {
            1: {
                "id": 1,
                "question": "Expand: (x - 1)²",
                "expected_answer": "x**2 - 2*x + 1",
                "topic": "Algebra",
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
                "expected_answer": "x = 4",
                "topic": "Algebra",
                "difficulty": "easy",
                "hints": [
                    "Start by isolating the term with x",
                    "Subtract 5 from both sides",
                    "Then divide both sides by 2"
                ]
            },
            3: {
                "id": 3,
                "question": "Find the derivative: f(x) = 3x² + 2x - 5",
                "expected_answer": "6*x + 2",
                "topic": "Calculus",
                "difficulty": "medium",
                "hints": [
                    "Use the power rule: d/dx[xⁿ] = n·xⁿ⁻¹",
                    "Differentiate each term separately",
                    "Remember the derivative of a constant is 0"
                ]
            }
        }
        
        # Demo students
        demo_student_id = str(uuid.uuid4())
        self.students[demo_student_id] = {
            "id": demo_student_id,
            "user_id": "demo_user",
            "name": "Demo Student",
            "email": "student@demo.com",
            "total_score": 85,
            "problems_solved": 42,
            "accuracy": 82.0
        }
    
    # ==================== Authentication ====================
    
    async def sign_up(
        self,
        email: str,
        password: str,
        user_metadata: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """Mock sign up"""
        user_id = str(uuid.uuid4())
        user = {
            "id": user_id,
            "email": email,
            "user_metadata": user_metadata or {}
        }
        return {
            "user": user,
            "session": {"access_token": f"mock_token_{user_id}"}
        }
    
    async def sign_in(self, email: str, password: str) -> Dict[str, Any]:
        """Mock sign in"""
        user_id = "demo_user"
        user = {
            "id": user_id,
            "email": email,
            "user_metadata": {"role": "student"}
        }
        return {
            "user": user,
            "session": {"access_token": f"mock_token_{user_id}"}
        }
    
    async def sign_out(self, access_token: str):
        """Mock sign out"""
        pass
    
    async def get_user(self, access_token: str) -> Optional[Dict]:
        """Mock get user"""
        return {
            "id": "demo_user",
            "email": "demo@example.com",
            "user_metadata": {"role": "student"}
        }
    
    # ==================== Students ====================
    
    async def create_student(
        self,
        user_id: str,
        name: str,
        email: str,
        grade_level: Optional[int] = None
    ) -> Dict[str, Any]:
        """Create student record"""
        student_id = str(uuid.uuid4())
        data = {
            "id": student_id,
            "user_id": user_id,
            "name": name,
            "email": email,
            "grade_level": grade_level,
            "total_score": 0,
            "problems_solved": 0,
            "accuracy": 0.0
        }
        self.students[student_id] = data
        return data
    
    async def get_student(self, student_id: str) -> Optional[Dict]:
        """Get student by ID"""
        return self.students.get(student_id)
    
    async def update_student_progress(
        self,
        student_id: str,
        problems_solved: int,
        total_score: int,
        accuracy: float
    ):
        """Update student progress metrics"""
        if student_id in self.students:
            self.students[student_id].update({
                "problems_solved": problems_solved,
                "total_score": total_score,
                "accuracy": accuracy
            })
    
    # ==================== Problems ====================
    
    async def create_problem(
        self,
        question: str,
        expected_answer: str,
        topic: str,
        difficulty: str,
        hints: List[str]
    ) -> Dict[str, Any]:
        """Create new problem"""
        problem_id = max(self.problems.keys()) + 1 if self.problems else 1
        data = {
            "id": problem_id,
            "question": question,
            "expected_answer": expected_answer,
            "topic": topic,
            "difficulty": difficulty,
            "hints": hints
        }
        self.problems[problem_id] = data
        return data
    
    async def get_problem(self, problem_id: int) -> Optional[Dict]:
        """Get problem by ID"""
        return self.problems.get(problem_id)
    
    async def get_problems_by_topic(self, topic: str) -> List[Dict]:
        """Get all problems for a topic"""
        return [p for p in self.problems.values() if p["topic"].lower() == topic.lower()]
    
    # ==================== Submissions ====================
    
    async def create_submission(
        self,
        student_id: str,
        problem_id: int,
        answer: str,
        correct: bool,
        attempts: int,
        image_data: Optional[str] = None
    ) -> Dict[str, Any]:
        """Record student submission"""
        submission_id = str(uuid.uuid4())
        data = {
            "id": submission_id,
            "student_id": student_id,
            "problem_id": problem_id,
            "answer": answer,
            "correct": correct,
            "attempts": attempts,
            "image_data": image_data,
            "created_at": datetime.now().isoformat()
        }
        self.submissions.append(data)
        return data
    
    async def get_student_submissions(
        self,
        student_id: str,
        limit: int = 50
    ) -> List[Dict]:
        """Get student's submission history"""
        submissions = [s for s in self.submissions if s["student_id"] == student_id]
        submissions.sort(key=lambda x: x["created_at"], reverse=True)
        return submissions[:limit]
    
    # ==================== Assignments ====================
    
    async def create_assignment(
        self,
        teacher_id: str,
        class_id: str,
        title: str,
        description: str,
        due_date: str,
        problem_ids: List[int]
    ) -> Dict[str, Any]:
        """Create new assignment"""
        assignment_id = str(uuid.uuid4())
        data = {
            "id": assignment_id,
            "teacher_id": teacher_id,
            "class_id": class_id,
            "title": title,
            "description": description,
            "due_date": due_date,
            "problem_ids": problem_ids,
            "status": "active"
        }
        self.assignments[assignment_id] = data
        return data
    
    async def get_class_assignments(self, class_id: str) -> List[Dict]:
        """Get all assignments for a class"""
        assignments = [a for a in self.assignments.values() if a["class_id"] == class_id]
        assignments.sort(key=lambda x: x["due_date"])
        return assignments
    
    # ==================== Analytics ====================
    
    async def get_class_analytics(self, class_id: str) -> Dict[str, Any]:
        """Get analytics for a class"""
        # Mock: return all students for demo
        students = list(self.students.values())
        total_students = len(students)
        avg_score = sum(s.get("total_score", 0) for s in students) / max(total_students, 1)
        
        return {
            "total_students": total_students,
            "avg_score": avg_score,
            "students": students
        }

# Singleton instance
_supabase_client = None

def get_supabase_client() -> SupabaseClient:
    """Get or create Supabase client instance"""
    global _supabase_client
    if _supabase_client is None:
        _supabase_client = SupabaseClient()
    return _supabase_client

