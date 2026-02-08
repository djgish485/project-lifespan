# The Interactive Epistemology Engine: Implementation Plan

**Goal:** Transform *Project Lifespan* from a static documentation site into a "Living Knowledge Base" where users can debate theories, ask questions, and trigger content updates via AI mediation.

## Phase 1: The Local Epistemology Server (Development/Admin)
*Target: A "God Mode" interface for the site owner to browse, chat, and auto-refactor content locally.*

### 1. Frontend (The Interface)
*   **Files:** `docs/assets/css/chat.css`, `docs/assets/js/chat.js`
*   **Features:**
    *   **Contextual Trigger:** Highlighting text spawns a "Discuss" tooltip.
    *   **Global Trigger:** A Floating Action Button (FAB) for general Q&A.
    *   **Sidebar UI:** A sleek, sliding panel containing the chat history and input box.
    *   **Client Logic:** Captures selected text + file context, sends to `localhost:8002/chat`.

### 2. Backend (The Brain)
*   **File:** `scripts/local_server.py`
*   **Tech Stack:** Python (`FastAPI`, `Uvicorn`).
*   **Capabilities:**
    *   **Read Access:** Can read any markdown file in `docs/` to ground its answers.
    *   **Write Access:** Can overwrite files (locally) if instructed to "refactor this page."
    *   **LLM Integration:** Uses `GEMINI_API_KEY` or `OPENAI_API_KEY` to generate responses.
*   **Endpoints:**
    *   `POST /chat`: Takes {message, context, file_path}. Returns {reply}.
    *   `POST /edit`: Takes {file_path, new_content}. Writes to disk.

### 3. Integration
*   **MkDocs Config:** Update `mkdocs.yml` to inject the CSS/JS.
*   **Workflow:** Run `mkdocs serve` (port 8000) AND `python scripts/local_server.py` (port 8002) simultaneously.

---

## Phase 2: The Hybrid Public Architecture (Production)
*Target: A friction-free debate interface for the public that maintains scientific rigor.*

### 1. The "Real-Time" Layer (Serverless)
*   **Host:** Vercel / Netlify Functions (Free Tier).
*   **Role:** Handles the casual chat.
*   **Logic:** Same as `local_server.py` but **Read-Only**. It cannot write to disk.
*   **Value:** Instant answers. Users explore ideas without barriers.

### 2. The "Crystallization" Layer (GitHub Issues)
*   **Trigger:** When a debate reaches a critical insight, the AI suggests: *"This is a valid challenge. Click here to formalize it."*
*   **Action:** The button generates a `github.com/.../issues/new` link with a pre-filled, rigorously formatted argument derived from the chat history.
*   **Result:** The debate moves to GitHub Issues for peer review and permanent record.

### 3. The "Self-Correction" Layer (GitHub Actions)
*   **Trigger:** A "Authorized Maintainer" (you) comments `/concede` on the Issue.
*   **Action:** A GitHub Action triggers the AI to generate a Pull Request implementing the change discussed in the issue.

---

## Immediate Next Steps (Execution)
1.  Create the Phase 1 assets (`chat.css`, `chat.js`, `local_server.py`).
2.  Update `mkdocs.yml`.
3.  Launch the local stack for verification.
