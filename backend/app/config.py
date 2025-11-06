from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    ENVIRONMENT: str = "development"
    
    # NO API KEYS NEEDED! Everything runs with mock data
    # These are kept for compatibility but are optional
    GEMINI_API_KEY: str = ""
    OPENAI_API_KEY: str = ""
    ANTHROPIC_API_KEY: str = ""
    SUPABASE_URL: str = ""
    SUPABASE_KEY: str = ""
    MATHPIX_APP_ID: str = ""
    MATHPIX_APP_KEY: str = ""
    
    # Agent Settings
    MAX_HINTS: int = 3
    HINT_DELAY_SECONDS: int = 30
    INACTIVITY_THRESHOLD_SECONDS: int = 60
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True
        # Don't require .env file
        extra = "ignore"

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()

