"""
Main FastAPI application for portfolio backend.
"""
import json
from contextlib import asynccontextmanager

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Any, Dict
from config import get_settings
from rag_service import get_rag_service
from groq_service import get_groq_service

# Initialize FastAPI app
app = FastAPI(
    title="Portfolio Backend API",
    description="Backend API for AI-powered portfolio with voice navigation",
    version="1.0.0"
)

# Configure CORS
settings = get_settings()
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins.split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request/Response Models
class ChatRequest(BaseModel):
    """Request model for text chat."""
    query: str


class ChatResponse(BaseModel):
    """Response model for chat endpoints."""
    query: str
    response: str
    navigate_to: Optional[str] = None
    context_sources: Optional[list] = None


class VoiceResponse(BaseModel):
    """Response model for voice endpoint."""
    transcript: str
    response: str
    navigate_to: Optional[str] = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager for FastAPI.
    Handles startup and shutdown events.
    """
    # Startup
    print("🚀 Initializing services...")
    print("📚 Loading RAG service...")
    get_rag_service()
    print("🤖 Initializing Groq service...")
    get_groq_service()
    print("✅ Backend ready!")

    yield

    # Shutdown (if needed in future)
    print("👋 Shutting down...")


@app.get("/")
async def root():
    """Health check endpoint."""
    return {
        "status": "ok",
        "message": "Portfolio Backend API",
        "version": "1.0.0"
    }


@app.get("/api/health")
async def health():
    """Detailed health check."""
    return {
        "status": "healthy",
        "services": {
            "rag": "ok",
            "groq": "ok"
        }
    }


@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Handle text-based chat queries.

    Uses RAG to find relevant portfolio content and generates
    AI response with optional navigation commands.
    """
    try:
        rag_service = get_rag_service()
        groq_service = get_groq_service()

        # Get relevant context
        context_results = rag_service.search(request.query)
        context_string = rag_service.get_context_string(request.query)

        # Generate AI response
        response_text, nav_command = groq_service.chat(request.query, context_string)

        # Prepare response
        return ChatResponse(
            query=request.query,
            response=response_text,
            navigate_to=nav_command,
            context_sources=[
                {
                    "type": r["metadata"].get("type"),
                    "id": r["metadata"].get("id")
                }
                for r in context_results
            ]
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing chat: {str(e)}")


@app.post("/api/voice", response_model=VoiceResponse)
async def voice_query(audio: UploadFile = File(...)):
    """
    Handle voice-based queries.

    Transcribes audio, then processes like a text chat query.
    """
    try:
        # Validate file type
        if not audio.content_type.startswith('audio/'):
            raise HTTPException(status_code=400, detail="File must be audio format")

        groq_service = get_groq_service()
        rag_service = get_rag_service()

        # Transcribe audio
        transcript = groq_service.transcribe(audio.file)

        if not transcript:
            raise HTTPException(status_code=400, detail="Could not transcribe audio")

        # Get relevant context
        context_string = rag_service.get_context_string(transcript)

        # Generate AI response
        response_text, nav_command = groq_service.chat(transcript, context_string)

        return VoiceResponse(
            transcript=transcript,
            response=response_text,
            navigate_to=nav_command
        )

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing voice: {str(e)}")


@app.get("/api/content")
async def get_content():
    """
    Get all portfolio content.

    This endpoint is used by SSG frontend to fetch content at build time.
    Returns the complete portfolio data for static site generation.
    """
    try:
        with open(settings.portfolio_data_path, 'r') as f:
            data = json.load(f)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading content: {str(e)}")


@app.get("/api/projects")
async def get_projects():
    """Get all projects."""
    try:
        with open(settings.portfolio_data_path, 'r') as f:
            data = json.load(f)
        return {"projects": data.get("projects", [])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading projects: {str(e)}")


@app.get("/api/projects/{project_id}")
async def get_project(project_id: str):
    """Get specific project by ID."""
    try:
        with open(settings.portfolio_data_path, 'r') as f:
            data = json.load(f)

        projects = data.get("projects", [])
        project = next((p for p in projects if p["id"] == project_id), None)

        if not project:
            raise HTTPException(status_code=404, detail="Project not found")

        return project
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading project: {str(e)}")


@app.get("/api/experience")
async def get_experience():
    """Get all work experience."""
    try:
        with open(settings.portfolio_data_path, 'r') as f:
            data = json.load(f)
        return {"experience": data.get("experience", [])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading experience: {str(e)}")


@app.get("/api/skills")
async def get_skills():
    """Get all skills."""
    try:
        with open(settings.portfolio_data_path, 'r') as f:
            data = json.load(f)
        return {"skills": data.get("skills", {})}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading skills: {str(e)}")


@app.get("/api/blog")
async def get_blog_posts():
    """Get all blog posts."""
    try:
        with open(settings.portfolio_data_path, 'r') as f:
            data = json.load(f)
        return {"posts": data.get("blog_posts", [])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading blog posts: {str(e)}")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=settings.host, port=settings.port)