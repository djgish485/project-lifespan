# Tools (AI Debate Orchestration)

This folder contains small "phone call" scripts so an orchestrator agent (Codex) can:

- Load large local context (theory markdown files)
- Ask a model to defend/steelman that theory
- Ask a model to critique the argument

These scripts are intentionally *not* used by MkDocs or the GitHub Pages build.

## Defender: Gemini

Use the **Gemini CLI** (already installed and logged-in on this machine) for Defender calls.

Model: default to `gemini-3-flash-preview` (this is the available "Gemini 3 Flash" model id in the installed CLI).

Verify model used:

- Run with `-o json` and check `stats.models` in the output.
- Example (expects `stats.models.gemini-3-flash-preview`): `GEMINI_OUTPUT=json bash tools/ask_gemini.sh - "Return only OK"`

Wrappers:

- Preferred: `bash tools/ask_gemini.sh docs/theories/pathogen_control.md "Prompt..."`
- Legacy/compat: `python tools/ask_gemini.py docs/theories/pathogen_control.md "Prompt..."` (routes through the Gemini CLI)

Environment:

- `GEMINI_CLI_MODEL` (default: `gemini-3-flash-preview`)
- `GEMINI_OUTPUT` (default: `text`; set `json` to debug model usage)

## Critic: Claude or GitHub Models

`tools/ask_critic.sh` runs either:

- `claude` CLI (default), or
- `gh models run` (GitHub Models)

Environment:

- `CRITIC_BACKEND` = `claude` (default) or `gh`
- `CRITIC_CLAUDE_MODEL` (default: `sonnet`)
- `CRITIC_GH_MODEL` (default: `o3-mini`)
