from __future__ import annotations

import os

import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

async def ask_gpt(prompt: str) -> str:
    if not openai.api_key:
        return "OpenAI API key not configured."
    try:
        response = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content.strip()
    except Exception as exc:  # pragma: no cover - network calls
        return f"Error contacting OpenAI: {exc}"
