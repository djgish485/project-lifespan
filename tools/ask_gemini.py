#!/usr/bin/env python3
"""
Ask Gemini to respond using a local markdown file as context.

This tool intentionally uses the *installed Gemini CLI* (OAuth login) rather than
calling the Gemini REST API directly. That keeps auth/setup simple on machines
where `gemini` is already installed and logged in.

Usage:
  python tools/ask_gemini.py docs/theories/epigenetic_information.md "Steelman the theory..."

Environment:
  GEMINI_CLI_MODEL  Default: gemini-3-flash-preview
  GEMINI_OUTPUT     Default: text   (set to json to inspect stats.models)
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


def _read_text(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    return Path(path).read_text(encoding="utf-8")


def main() -> int:
    if len(sys.argv) < 3:
        print(
            'Usage: python tools/ask_gemini.py <context_path|-> "<prompt>"',
            file=sys.stderr,
        )
        return 2

    context_path = sys.argv[1]
    prompt = sys.argv[2]

    if subprocess.call(["bash", "-lc", "command -v gemini >/dev/null 2>&1"]) != 0:
        print("Error: 'gemini' CLI not found in PATH.", file=sys.stderr)
        return 2

    model = os.environ.get("GEMINI_CLI_MODEL", "gemini-3-flash-preview")
    output = os.environ.get("GEMINI_OUTPUT", "text")

    context = _read_text(context_path)
    full_prompt = (
        "ROLE: You are the DEFENDER of the theory described below.\n\n"
        "CONTEXT (verbatim):\n"
        f"{context}\n\n"
        "INSTRUCTION:\n"
        f"{prompt}\n\n"
        "CONSTRAINTS:\n"
        "- Be specific; avoid vague hedges.\n"
        "- Cite evidence from the context (quote short phrases as needed).\n"
        "- If you mention a discriminator experiment, state what outcome would favor which rival.\n"
    )

    try:
        p = subprocess.run(
            ["gemini", "-m", model, "-p", full_prompt, "-o", output],
            check=False,
            text=True,
            input="",
            capture_output=False,
        )
        return p.returncode
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
