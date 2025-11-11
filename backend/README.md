# Portfolio Website Backend

FastAPI backend with RAG capabilities for an AI-powered portfolio website.

## Features

- **FastAPI** REST API with async support
- **ChromaDB** for vector storage
- **Groq API** integration for LLM (Llama 3.3 70B) and STT (Whisper v3)
- **Local embeddings** using sentence-transformers
- **WebSocket** support for streaming responses
- **SQLite** database for structured content

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create `.env` file:
```bash
cp .env.example .env
```

4. Add your Groq API key to `.env`:
```
GROQ_API_KEY=your_actual_api_key_here
```

## Running the Server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

API documentation: `http://localhost:8000/docs`

## API Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `POST /api/chat/` - Chat with AI assistant
- `POST /api/voice/transcribe` - Transcribe audio
- `GET /api/content/projects` - Get all projects
- `GET /api/content/experiences` - Get work experiences
- `GET /api/content/achievements` - Get achievements
- `WS /api/ws/chat` - WebSocket for streaming chat

## Project Structure

```
backend/
├── app/
│   ├── api/          # API routes
│   ├── services/     # Business logic (RAG, LLM, STT)
│   ├── data/         # Seed data and ChromaDB storage
│   ├── config.py     # Configuration
│   ├── database.py   # Database setup
│   ├── models.py     # SQLAlchemy models
│   └── schemas.py    # Pydantic schemas
└── requirements.txt
```
