"""
Groq API service for LLM chat and speech-to-text.
"""
import re
from groq import Groq
from typing import Optional, Tuple
from config import get_settings


class GroqService:
    """Handles Groq API calls for LLM and STT."""

    def __init__(self):
        self.settings = get_settings()
        self.client = Groq(api_key=self.settings.groq_api_key)

    def _build_system_prompt(self) -> str:
        """Build system prompt for the AI assistant."""
        return """You are an AI assistant for a software engineer's portfolio website. Your role is to:

1. Answer questions about their projects, work experience, and skills using the provided context
2. Be concise but informative
3. Highlight relevant achievements and technical details
4. Navigate users to appropriate pages when asked

When answering:
- Use the context provided to give accurate information
- If asked to "show", "navigate to", or "take me to" a page, include a navigation command
- Be friendly and professional
- Don't make up information not in the context

Navigation commands (use when appropriate):
- To show all projects: NAVIGATE:/projects
- To show ML/AI projects: NAVIGATE:/projects?category=ai-ml
- To show backend projects: NAVIGATE:/projects?category=backend
- To show work experience: NAVIGATE:/experience
- To show blog posts: NAVIGATE:/blog
- To show a specific project: NAVIGATE:/projects/[project-id]
- To go home: NAVIGATE:/

Examples:
User: "Show me your ML projects"
Response: "I've worked on several ML projects including an [get from resume]. NAVIGATE:/projects?category=ai-ml"

User: "What technologies do you know?"
Response: "I specialize in [get from resume]"

User: "Tell me about your work at x"
Response: "At x, I serve as a xyz leading backend development for xyz. [Key Metrics]. Would you like more details? NAVIGATE:/experience"
"""

    def chat(self, query: str, context: str) -> Tuple[str, Optional[str]]:
        """
        Generate AI response using Groq LLM with RAG context.

        Args:
            query: User's question
            context: Retrieved context from RAG

        Returns:
            Tuple of (response_text, navigation_command)
        """
        # Build the prompt
        user_message = f"""Context from portfolio:
{context}

User question: {query}

Please answer the question using the context provided. If the user wants to navigate somewhere, include the appropriate NAVIGATE: command."""

        # Call Groq API
        completion = self.client.chat.completions.create(
            model=self.settings.llm_model,
            messages=[
                {"role": "system", "content": self._build_system_prompt()},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
            max_tokens=500
        )

        response_text = completion.choices[0].message.content

        # Extract navigation command if present
        nav_command = self._extract_navigation(response_text)

        # Remove navigation command from response
        if nav_command:
            response_text = re.sub(r'NAVIGATE:[^\s]+', '', response_text).strip()

        return response_text, nav_command

    def _extract_navigation(self, text: str) -> Optional[str]:
        """Extract navigation command from LLM response."""
        match = re.search(r'NAVIGATE:(/[^\s]*)', text)
        if match:
            return match.group(1)
        return None

    def transcribe(self, audio_file) -> str:
        """
        Transcribe audio file using Groq Whisper.

        Args:
            audio_file: Audio file object (from FastAPI UploadFile)

        Returns:
            Transcribed text
        """
        transcription = self.client.audio.transcriptions.create(
            file=audio_file,
            model=self.settings.stt_model,
            response_format="text"
        )

        return transcription.strip()


# Global instance
_groq_service = None


def get_groq_service() -> GroqService:
    """Get or create Groq service singleton."""
    global _groq_service
    if _groq_service is None:
        _groq_service = GroqService()
    return _groq_service