import subprocess
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os
import uuid
import json
import asyncio

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory history store: {session_id: [messages]}
# Note: In a real app, use a DB. For local dev, RAM is fine.
SESSION_STORE = {}

class ChatRequest(BaseModel):
    message: str
    context: str | None = None
    file_path: str | None = None
    session_id: str

SYSTEM_PROMPT_TEMPLATE = """
You are the Project Lifespan Gatekeeper. You are an expert Epistemologist managing a scientific documentation site.

CONTEXT:
User is viewing file: {file_path}
Highlight/Context: {context}

INSTRUCTIONS:
1. TRIAGE the user's intent:
   - QUESTION: Answer it using the documentation knowledge.
   - CHALLENGE: The user disagrees with the text. Switch to "General Critic" mode. Defend the current consensus but admit if their logic is sound.
   - NEW DATA: The user is providing a link/fact. Evaluate it against the "Grand Synthesis".

2. ACTION PROTOCOL (CRITICAL):
   - If the user's argument/evidence is valid and requires a change to the documentation:
     **DO NOT EDIT THE FILE DIRECTLY.**
     Instead, follow these steps:
     1. Create a new git branch (e.g., `update/topic-name`).
     2. Make the edit in that branch.
     3. Use `gh pr create` to open a Pull Request with a clear summary of the debate as the description.
     4. Tell the user: "I have opened a Pull Request to incorporate this change: [Link]"

   - If no change is needed, just reply in the chat.

3. HISTORY:
   This is a continuing conversation. Refer to previous turns if relevant.

CHAT HISTORY:
{history}

USER MESSAGE:
{message}
"""

async def stream_gemini_output(session_id, full_prompt):
    """
    Generator that runs Gemini CLI and yields output line-by-line.
    Separates stderr (Thinking) from stdout (Content).
    """
    try:
        process = subprocess.Popen(
            ["gemini", "--yolo", "--output-format", "text", "-p", full_prompt],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,  # Capture stderr separately
            text=True,
            bufsize=1
        )

        full_response_accumulator = ""

        # We need to read two streams concurrently.
        # Simple approach for a generator: poll them.
        import select
        
        while True:
            reads = [process.stdout.fileno(), process.stderr.fileno()]
            ret = select.select(reads, [], [], 0.1)

            for fd in ret[0]:
                if fd == process.stdout.fileno():
                    line = process.stdout.readline()
                    if line:
                        full_response_accumulator += line
                        # Send as 'content' event
                        yield f"event: content\ndata: {json.dumps({'chunk': line})}\n\n"
                
                if fd == process.stderr.fileno():
                    line = process.stderr.readline()
                    if line:
                        # Send as 'thinking' event
                        yield f"event: thinking\ndata: {json.dumps({'chunk': line})}\n\n"

            if process.poll() is not None:
                # Process finished, drain remaining buffers
                for line in process.stdout:
                    full_response_accumulator += line
                    yield f"event: content\ndata: {json.dumps({'chunk': line})}\n\n"
                for line in process.stderr:
                    yield f"event: thinking\ndata: {json.dumps({'chunk': line})}\n\n"
                break
            
            await asyncio.sleep(0.01)

        # Save history
        if session_id not in SESSION_STORE:
            SESSION_STORE[session_id] = []
        SESSION_STORE[session_id].append(f"Agent: {full_response_accumulator}")

    except Exception as e:
        yield f"event: error\ndata: {json.dumps({'error': str(e)})}\n\n"

@app.post("/chat/stream")
async def chat_stream_endpoint(req: ChatRequest):
    print(f"Stream Req [{req.session_id}]: {req.message}")

    # 1. Get History
    if req.session_id not in SESSION_STORE:
        SESSION_STORE[req.session_id] = []
    
    # Add User message to history *now*
    SESSION_STORE[req.session_id].append(f"User: {req.message}")
    
    # Flatten history for the prompt
    history_text = "\n".join(SESSION_STORE[req.session_id][:-1]) # Exclude the just-added message to avoid duplication in template

    # 2. Construct Prompt
    full_prompt = SYSTEM_PROMPT_TEMPLATE.format(
        file_path=req.file_path,
        context=req.context if req.context else "No specific text selected.",
        history=history_text,
        message=req.message
    )

    # 3. Stream Response
    return StreamingResponse(
        stream_gemini_output(req.session_id, full_prompt),
        media_type="text/event-stream"
    )

@app.post("/chat/reset")
async def reset_endpoint(req: ChatRequest):
    if req.session_id in SESSION_STORE:
        del SESSION_STORE[req.session_id]
    return {"status": "cleared"}

if __name__ == "__main__":
    print("Starting Local Epistemology Server (Streaming) on port 8002...")
    uvicorn.run(app, host="127.0.0.1", port=8002)