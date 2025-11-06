from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from typing import Optional

router = APIRouter()

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class SignupRequest(BaseModel):
    email: EmailStr
    password: str
    name: str
    role: str  # "student" or "teacher"

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: dict

@router.post("/login", response_model=TokenResponse)
async def login(request: LoginRequest):
    """Login user with email and password"""
    # This would integrate with Supabase Auth
    # Mock response
    return TokenResponse(
        access_token="mock_token_123",
        user={
            "id": "user_1",
            "email": request.email,
            "role": "student"
        }
    )

@router.post("/signup", response_model=TokenResponse)
async def signup(request: SignupRequest):
    """Register new user"""
    # This would integrate with Supabase Auth
    # Mock response
    return TokenResponse(
        access_token="mock_token_123",
        user={
            "id": "user_new",
            "email": request.email,
            "name": request.name,
            "role": request.role
        }
    )

@router.post("/logout")
async def logout():
    """Logout current user"""
    return {"message": "Logged out successfully"}

@router.get("/me")
async def get_current_user():
    """Get current authenticated user"""
    # Mock response
    return {
        "id": "user_1",
        "email": "student@example.com",
        "name": "Demo Student",
        "role": "student"
    }

