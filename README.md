# AI-Powered Portfolio Website

A full-stack portfolio website with AI chat assistant, voice navigation, and RAG-powered content retrieval.

## 🚀 Features

### Backend (FastAPI)
- FastAPI REST API with async support
- RAG pipeline using ChromaDB for vector storage
- Groq API integration for LLM (Llama 3.3 70B) and STT (Whisper v3)
- Local sentence-transformers for embeddings (all-MiniLM-L6-v2)
- WebSocket support for streaming LLM responses
- SQLite database for structured content
- CORS configured for React frontend

### Frontend (React)
- Vite + React 18 + TypeScript
- Tailwind CSS for minimal, elegant styling
- Framer Motion for smooth animations
- AI Chat Widget with text + voice input
- Voice recorder with visual feedback
- Project cards with video embed support (Loom, YouTube)
- Experience timeline with animations
- Responsive navigation and routing

## 📁 Project Structure

```
portfolio-website/
├── backend/               # FastAPI backend
│   ├── app/
│   │   ├── api/          # API routes
│   │   ├── services/     # Business logic (RAG, LLM, STT)
│   │   ├── data/         # Seed data and ChromaDB
│   │   ├── config.py     # Configuration
│   │   ├── database.py   # Database setup
│   │   ├── models.py     # SQLAlchemy models
│   │   └── schemas.py    # Pydantic schemas
│   └── requirements.txt
└── frontend/             # React frontend
    ├── src/
    │   ├── components/   # Reusable components
    │   ├── pages/        # Page components
    │   ├── services/     # API and WebSocket clients
    │   ├── hooks/        # Custom React hooks
    │   └── types/        # TypeScript types
    └── package.json
```

## 🛠️ Setup Instructions

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file:
```bash
cp .env.example .env
```

5. Add your Groq API key to `.env`:
```
GROQ_API_KEY=your_actual_api_key_here
```

6. Run the server:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Backend will be available at `http://localhost:8000`
API documentation: `http://localhost:8000/docs`

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Create `.env` file:
```bash
cp .env.example .env
```

4. Start development server:
```bash
npm run dev
```

Frontend will be available at `http://localhost:5173`

## 🎯 Key Features to Implement

### Backend
- [ ] Complete RAG pipeline implementation
- [ ] Implement streaming LLM responses via WebSocket
- [ ] Add conversation history storage
- [ ] Implement semantic search over portfolio content
- [ ] Add authentication (optional)
- [ ] Seed database with actual portfolio data

### Frontend
- [ ] Integrate WebSocket for streaming responses
- [ ] Add voice command navigation
- [ ] Implement error boundaries
- [ ] Add loading skeletons
- [ ] Optimize performance
- [ ] Add accessibility features
- [ ] Implement dark mode (optional)

## 🔧 Technology Stack

### Backend
- **FastAPI** - Modern, fast web framework
- **ChromaDB** - Vector database for embeddings
- **Groq** - Fast LLM inference (Llama 3.3 70B) and STT (Whisper v3)
- **sentence-transformers** - Local embedding generation
- **SQLAlchemy** - ORM for SQLite
- **Pydantic** - Data validation

### Frontend
- **React 18** - UI library
- **TypeScript** - Type safety
- **Vite** - Fast build tool
- **Tailwind CSS** - Utility-first CSS
- **Framer Motion** - Animation library
- **React Router** - Client-side routing
- **Axios** - HTTP client

## 📝 API Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `POST /api/chat/` - Send chat message
- `POST /api/voice/transcribe` - Transcribe audio
- `GET /api/content/projects` - Get all projects
- `GET /api/content/projects/{id}` - Get specific project
- `GET /api/content/experiences` - Get work experiences
- `GET /api/content/achievements` - Get achievements
- `WS /api/ws/chat` - WebSocket for streaming chat

## 🚀 Deployment

### Backend
- Deploy to Railway, Render, or AWS
- Set environment variables
- Use PostgreSQL for production (update DATABASE_URL)

### Frontend
- Build: `npm run build`
- Deploy to Vercel, Netlify, or Cloudflare Pages
- Set VITE_API_URL to production backend URL

## 📄 License

MIT License

## 🤝 Contributing

Contributions welcome! Please open an issue or submit a pull request.
