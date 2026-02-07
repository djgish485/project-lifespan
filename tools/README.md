# Tools (AI Debate Orchestration)

This folder contains small "phone call" scripts so an orchestrator agent (Codex) can:

- Load large local context (theory markdown files)
- Ask a model to defend/steelman that theory
- Ask a model to critique the argument

These scripts are intentionally *not* used by MkDocs or the GitHub Pages build.

## Defender: Gemini

`tools/ask_gemini.py` calls the Gemini REST API using a local markdown file as context.

Environment:

- `GEMINI_API_KEY` (or `GOOGLE_API_KEY`)
- `GEMINI_MODEL` (default: `gemini-2.0-flash`)

## Critic: Claude or GitHub Models

`tools/ask_critic.sh` runs either:

- `claude` CLI (default), or
- `gh models run` (GitHub Models)

Environment:

- `CRITIC_BACKEND` = `claude` (default) or `gh`
- `CRITIC_CLAUDE_MODEL` (default: `sonnet`)
- `CRITIC_GH_MODEL` (default: `o3-mini`)

