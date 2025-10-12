import httpx
from app.core.config import settings

def online_available() -> bool:
    return bool(settings.OPENAI_API_KEY)

def call_online_openai(prompt: str) -> str:
    if not settings.OPENAI_API_KEY:
        raise RuntimeError("OpenAI key not configured")
    headers = {"Authorization": f"Bearer {settings.OPENAI_API_KEY}"}
    data = {"model": "gpt-3.5-turbo","messages":[{"role":"user","content":prompt}], "max_tokens": 512}
    with httpx.Client(timeout=10.0) as client:
        resp = client.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
        resp.raise_for_status()
        r = resp.json()
        return r["choices"][0]["message"]["content"].strip()

def offline_fallback(prompt: str) -> str:
    if "derive" in prompt.lower() or "differentiate" in prompt.lower():
        return "Offline helper: use /calculus/derivative endpoint with expression like sin(x)"
    return "Offline helper: try a specific calculator module."

def answer(prompt: str) -> str:
    if online_available():
        try:
            return call_online_openai(prompt)
        except Exception:
            return offline_fallback(prompt)
    else:
        return offline_fallback(prompt)
