from groq import Groq
from ..config import settings


class STTService:
    def __init__(self):
        self.client = Groq(api_key=settings.groq_api_key)
        self.model = settings.stt_model

    async def transcribe_audio(self, audio_file) -> str:
        """
        Transcribe audio using Groq Whisper API
        TODO: Add error handling and audio format validation
        """
        transcription = self.client.audio.transcriptions.create(
            file=audio_file,
            model=self.model,
            response_format="json"
        )
        return transcription.text


stt_service = STTService()
