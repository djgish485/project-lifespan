#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF' 1>&2
Usage:
  bash tools/ask_critic.sh "argument to critique"
  cat argument.txt | bash tools/ask_critic.sh

Environment:
  CRITIC_BACKEND          Optional: "claude" (default) or "gh"
  CRITIC_CLAUDE_MODEL     Optional: default "sonnet"
  CRITIC_GH_MODEL         Optional: default "o3-mini"
EOF
}

ARGUMENT="$*"
if [[ -z "${ARGUMENT}" ]]; then
  if [[ -t 0 ]]; then
    usage
    exit 2
  fi
  ARGUMENT="$(cat)"
fi

if [[ -z "${ARGUMENT}" ]]; then
  usage
  exit 2
fi

SYSTEM_PROMPT=$'You are a Popperian/Deutschian CRITIC.\n\nTask:\n- Attack causal mechanism clarity (hard-to-vary).\n- Identify hidden assumptions and auxiliary hypotheses.\n- Propose 1-3 discriminator experiments that would strongly favor one rival over the other.\n\nStyle:\n- Short bullets.\n- No politeness padding.\n- If the argument is vague, say exactly what is missing.'

USER_PROMPT=$'Critique the following argument:\n\n'"${ARGUMENT}"$'\n\nReturn:\n1) Weak points\n2) Key missing details\n3) Discriminator experiment(s) (with predicted outcomes)'

BACKEND="${CRITIC_BACKEND:-claude}"
if [[ "${BACKEND}" == "claude" ]]; then
  if ! command -v claude >/dev/null 2>&1; then
    echo "Error: CRITIC_BACKEND=claude but 'claude' is not installed." 1>&2
    exit 2
  fi
  claude -p --model "${CRITIC_CLAUDE_MODEL:-sonnet}" --system-prompt "${SYSTEM_PROMPT}" "${USER_PROMPT}"
  exit $?
fi

if [[ "${BACKEND}" == "gh" ]]; then
  if ! command -v gh >/dev/null 2>&1; then
    echo "Error: CRITIC_BACKEND=gh but 'gh' is not installed." 1>&2
    exit 2
  fi
  gh models run "${CRITIC_GH_MODEL:-o3-mini}" --prompt "${SYSTEM_PROMPT}"$'\n\n'"${USER_PROMPT}"
  exit $?
fi

echo "Error: unknown CRITIC_BACKEND='${BACKEND}' (expected: claude|gh)" 1>&2
exit 2

