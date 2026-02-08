import subprocess
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Enable CORS so the browser can talk to this local server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for local dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    context: str | None = None
    file_path: str | None = None

SYSTEM_PROMPT_TEMPLATE = """
You are the Project Lifespan Gatekeeper. You are an expert Epistemologist managing a scientific documentation site.

CONTEXT:
User is viewing file: {file_path}
Highlight/Context: {context}

USER MESSAGE:
{message}

INSTRUCTIONS:
1. TRIAGE the user's intent:
   - QUESTION: Answer it using the documentation knowledge.
   - CHALLENGE: The user disagrees with the text. Switch to "General Critic" mode. Defend the current consensus but admit if their logic is sound.
   - NEW DATA: The user is providing a link/fact. Evaluate it against the "Grand Synthesis".

2. RESPONSE FORMAT:
   - Be concise.
   - If it's a valid challenge, say: "This is a strong point. I recommend we open a formal debate Issue."
   - Do not use markdown blocks for the whole response, just natural text.
"""

@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    print(f"Received: {req.message} | Context: {req.context}")
    
    # 1. Construct the prompt
    full_prompt = SYSTEM_PROMPT_TEMPLATE.format(
        file_path=req.file_path,
        context=req.context if req.context else "No specific text selected.",
        message=req.message
    )

    # 2. Call Gemini CLI
    # We use --yolo to bypass confirmations and -p to pass the prompt
    try:
        # Note: We are shelling out to the system's 'gemini' command.
        # This assumes 'gemini' is in the PATH and configured.
        result = subprocess.run(
            ["gemini", "--yolo", "--output-format", "text", "-p", full_prompt],
            capture_output=True,
            text=True,
            check=True
        )
        response_text = result.stdout.strip()
        
        # Fallback if empty (sometimes CLI might just do an action)
        if not response_text:
            response_text = "(Gemini CLI executed the action but returned no text output.)"

        return {"reply": response_text}

    except subprocess.CalledProcessError as e:
        print(f"Gemini Error: {e.stderr}")
        return {"reply": f"Error calling Gemini Brain: {e.stderr}"}
    except Exception as e:
        print(f"Server Error: {e}")
        return {"reply": f"Internal Server Error: {e}"}

if __name__ == "__main__":
    print("Starting Local Epistemology Server on port 8002...")
    uvicorn.run(app, host="127.0.0.1", port=8002)
