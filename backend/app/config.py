"""
Configuration settings for the portfolio backend.
"""
import os

from pydantic_settings import BaseSettings
from functools import lru_cache

from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Groq API
    groq_api_key: str = os.getenv("GROQ_API_KEY")

    # CORS
    cors_origins: str = "http://localhost:3000,http://localhost:5173,http://localhost:4321"

    # Server
    host: str = "0.0.0.0"
    port: int = 8000

    # Paths
    portfolio_data_path: str = "app/data/portfolio.json"
    vector_store_path: str = "app/data/vector_store"

    # RAG Configuration
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    chunk_size: int = 500
    chunk_overlap: int = 50
    top_k_results: int = 3

    # Groq Models
    llm_model: str = "llama-3.3-70b-versatile"
    stt_model: str = "whisper-large-v3"

    class Config:
        env_file = ".env"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()