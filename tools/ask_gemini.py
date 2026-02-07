#!/usr/bin/env python3
"""
Ask Gemini to respond using a local markdown file as context.

Usage:
  python tools/ask_gemini.py docs/theories/epigenetic_information.md "Steelman the theory..."

Environment:
  GEMINI_API_KEY (or GOOGLE_API_KEY)  Required.
  GEMINI_MODEL                        Default: gemini-2.0-flash
  GEMINI_TEMPERATURE                  Default: 0.2
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path


def _read_text(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    return Path(path).read_text(encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(
        prog="ask_gemini.py",
        description="Call the Gemini REST API with a local file as context.",
    )
    ap.add_argument("context_path", help='Path to a markdown file, or "-" for stdin.')
    ap.add_argument("prompt", help="Instruction for the model.")
    ap.add_argument(
        "--model",
        default=os.environ.get("GEMINI_MODEL", "gemini-2.0-flash"),
        help="Gemini model name (default: env GEMINI_MODEL or gemini-2.0-flash).",
    )
    ap.add_argument(
        "--temperature",
        type=float,
        default=float(os.environ.get("GEMINI_TEMPERATURE", "0.2")),
        help="Sampling temperature (default: env GEMINI_TEMPERATURE or 0.2).",
    )
    ap.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the composed prompt and exit without calling the API.",
    )
    args = ap.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY (or GOOGLE_API_KEY) is not set.", file=sys.stderr)
        return 2

    try:
        import requests  # type: ignore
    except Exception:
        print(
            "Error: Python package 'requests' is required (pip install requests).",
            file=sys.stderr,
        )
        return 2

    context = _read_text(args.context_path)

    full_prompt = (
        "ROLE: You are the DEFENDER of the theory described below.\n\n"
        "CONTEXT (verbatim):\n"
        f"{context}\n\n"
        "INSTRUCTION:\n"
        f"{args.prompt}\n\n"
        "CONSTRAINTS:\n"
        "- Be specific; avoid vague hedges.\n"
        "- Cite evidence from the context (quote short phrases as needed).\n"
        "- If you mention a discriminator experiment, state what outcome would favor which rival.\n"
    )

    if args.dry_run:
        print(full_prompt)
        return 0

    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"{args.model}:generateContent?key={api_key}"
    )
    body = {
        "contents": [{"role": "user", "parts": [{"text": full_prompt}]}],
        "generationConfig": {"temperature": args.temperature},
    }

    try:
        resp = requests.post(
            url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(body),
            timeout=120,
        )
    except Exception as e:
        print(f"Error: request failed: {e}", file=sys.stderr)
        return 1

    if resp.status_code != 200:
        print(
            f"Error: Gemini API returned HTTP {resp.status_code}",
            file=sys.stderr,
        )
        print(resp.text, file=sys.stderr)
        return 1

    try:
        data = resp.json()
    except Exception:
        print("Error: Gemini API returned non-JSON response.", file=sys.stderr)
        print(resp.text, file=sys.stderr)
        return 1

    try:
        parts = data["candidates"][0]["content"]["parts"]
        text = "".join(p.get("text", "") for p in parts)
    except Exception:
        print("Error: unexpected Gemini response shape:", file=sys.stderr)
        print(json.dumps(data, indent=2, ensure_ascii=True), file=sys.stderr)
        return 1

    print(text.strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

