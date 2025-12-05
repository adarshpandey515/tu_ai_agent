import os


def get_api_key() -> str:
    key = os.getenv("GROQ_API_KEY", "")
    return key


def get_model() -> str:
    return os.getenv("GROQ_MODEL", "meta-llama/llama-4-scout-17b-16e-instruct")
