from groq import Groq
from typing import List, Dict, AsyncGenerator
from ..config import settings


class LLMService:
    def __init__(self):
        self.client = Groq(api_key=settings.groq_api_key)
        self.model = settings.llm_model

    async def generate_response(self, messages: List[Dict[str, str]], stream: bool = False):
        """
        Generate response using Groq LLM
        TODO: Implement streaming support and conversation context
        """
        if stream:
            return self._stream_response(messages)
        else:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=1024
            )
            return response.choices[0].message.content

    async def _stream_response(self, messages: List[Dict[str, str]]) -> AsyncGenerator[str, None]:
        """
        Stream response from Groq LLM
        TODO: Implement async streaming
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.7,
            max_tokens=1024,
            stream=True
        )

        for chunk in response:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content


llm_service = LLMService()
