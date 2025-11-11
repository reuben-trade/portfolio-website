from fastapi import APIRouter, File, UploadFile, HTTPException
from ..schemas import VoiceTranscription

router = APIRouter()


@router.post("/transcribe", response_model=VoiceTranscription)
async def transcribe_audio(audio: UploadFile = File(...)):
    """
    Transcribe audio using Groq Whisper API
    TODO: Implement Groq STT integration
    """
    if not audio.content_type or not audio.content_type.startswith("audio/"):
        raise HTTPException(status_code=400, detail="Invalid audio file")

    return VoiceTranscription(
        text="Voice transcription placeholder - Groq STT to be implemented",
        confidence=0.95
    )
