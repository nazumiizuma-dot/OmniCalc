# OmniCalc-Pro (Final Prototype)
This is a ready-to-run prototype of OmniCalc Pro (FastAPI backend + Next.js frontend).
## Quickstart
1. Copy env:
   cp backend/.env.example backend/.env
   (edit backend/.env to add OPENAI_API_KEY if you want online AI)
2. Start:
   docker-compose up --build
3. Open frontend: http://localhost:3000
   API docs: http://localhost:8000/docs
## Notes
- The offline AI is a simple fallback. For production, integrate a proper local LLM or isolate execution for user-submitted code.
- No secrets are included. Put secrets in backend/.env or your secret manager.
