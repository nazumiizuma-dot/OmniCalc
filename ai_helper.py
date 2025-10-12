from app.core.ai_manager import answer
def ask(q: str) -> str:
    if len(q) > 2000:
        return "Question too long"
    return answer(q)
