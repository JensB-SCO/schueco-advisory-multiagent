from __future__ import annotations
import os
from openai import OpenAI

def get_client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY fehlt. Lege eine .env Datei an oder setze die Umgebungsvariable.")
    return OpenAI(api_key=api_key)

def get_model() -> str:
    return os.getenv("OPENAI_MODEL", "gpt-5.1")
