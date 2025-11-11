from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    # Groq API
    groq_api_key: str

    # Database
    database_url: str = "sqlite+aiosqlite:///./portfolio.db"

    # ChromaDB
    chroma_persist_directory: str = "./app/data/chroma_db"

    # Models
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    llm_model: str = "llama-3.3-70b-versatile"
    stt_model: str = "whisper-large-v3"

    # CORS
    cors_origins: List[str] = ["http://localhost:5173", "http://localhost:3000"]

    # Server
    host: str = "0.0.0.0"
    port: int = 8000

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
