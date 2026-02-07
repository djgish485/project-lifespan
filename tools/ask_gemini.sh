#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF' 1>&2
Usage:
  bash tools/ask_gemini.sh <context_path> "<prompt>"

Notes:
- Uses the installed `gemini` CLI (OAuth login on this machine).
- Context is sent on stdin; the prompt is appended via `gemini -p`.

Environment:
  GEMINI_CLI_MODEL   Default: gemini-3-flash-preview
  GEMINI_OUTPUT      Default: text   (set to json to inspect stats.models)
EOF
}

CONTEXT_PATH="${1:-}"
PROMPT="${2:-}"
if [[ -z "${CONTEXT_PATH}" || -z "${PROMPT}" ]]; then
  usage
  exit 2
fi

if ! command -v gemini >/dev/null 2>&1; then
  echo "Error: 'gemini' CLI not found in PATH." 1>&2
  exit 2
fi

MODEL="${GEMINI_CLI_MODEL:-gemini-3-flash-preview}"
OUTPUT="${GEMINI_OUTPUT:-text}"

if [[ "${CONTEXT_PATH}" == "-" ]]; then
  # stdin already contains context
  gemini -m "${MODEL}" -p "${PROMPT}" -o "${OUTPUT}"
  exit $?
fi

if [[ ! -f "${CONTEXT_PATH}" ]]; then
  echo "Error: context file not found: ${CONTEXT_PATH}" 1>&2
  exit 2
fi

cat "${CONTEXT_PATH}" | gemini -m "${MODEL}" -p "${PROMPT}" -o "${OUTPUT}"

