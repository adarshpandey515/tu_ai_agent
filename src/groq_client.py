import os
import typing as t

class GroqError(Exception):
    pass

class GroqClient:
    """Minimal Groq client wrapper for text completions."""

    def __init__(self, api_key: t.Optional[str] = None, model: str = "meta-llama/llama-4-scout-17b-16e-instruct"):
        self.api_key = str(input("enter the api key ="))
        if not self.api_key:
            raise GroqError("GROQ_API_KEY not set. Export it before running.")
        self.model = model

        try:
            from groq import Groq  # type: ignore
        except Exception as e:
            raise GroqError(f"Groq SDK not installed. Add 'groq' to requirements. Details: {e}")

        self._client = Groq(api_key=self.api_key)

    def complete(self, prompt: str, temperature: float = 0.2, max_tokens: int = 1024) -> str:
        """Call Groq chat completions with a simple system+user message."""
        if not prompt or not prompt.strip():
            raise GroqError("Prompt cannot be empty.")

        # Using Chat Completions API
        resp = self._client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=temperature,
            max_tokens=max_tokens,
        )

        choice = resp.choices[0]
        content = choice.message.content if hasattr(choice, "message") else None
        if not content:
            raise GroqError("Empty response from model.")
        return content
