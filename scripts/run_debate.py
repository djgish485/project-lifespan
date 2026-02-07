#!/usr/bin/env python3
"""Config-driven debate runner: Defender vs Critic with optional Judge."""

import argparse
import csv
import io
import json
import os
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO_ROOT / "debates" / "schemas" / "turn.schema.json"


# ---------------------------------------------------------------------------
# Context building
# ---------------------------------------------------------------------------

def read_file_truncated(path: Path, max_chars: int) -> str:
    """Read a file, truncating to max_chars."""
    if not path.exists():
        return f"[FILE NOT FOUND: {path}]"
    text = path.read_text(encoding="utf-8", errors="replace")
    if len(text) > max_chars:
        text = text[:max_chars] + f"\n\n[...TRUNCATED at {max_chars} chars]"
    return text


def extract_evidence_rows(csv_path: Path, theory_ids: list[str]) -> str:
    """Extract rows from evidence.csv matching given theory_ids as a markdown table."""
    if not csv_path.exists():
        return "[evidence.csv not found]"
    text = csv_path.read_text(encoding="utf-8")
    reader = csv.DictReader(io.StringIO(text))
    rows = [r for r in reader if r.get("theory_id") in theory_ids]
    if not rows:
        return "[No matching evidence rows]"
    headers = list(rows[0].keys())
    lines = ["| " + " | ".join(headers) + " |"]
    lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
    for r in rows:
        lines.append("| " + " | ".join(r.get(h, "") for h in headers) + " |")
    return "\n".join(lines)


def build_context_pack(config: dict) -> str:
    """Build the repo context string from config-specified files."""
    ctx = config["context"]
    max_chars = ctx.get("max_chars_per_file", 60000)
    parts = []

    # Theory page
    theory_path = REPO_ROOT / config["theory"]["page"]
    parts.append(f"## THEORY PAGE: {config['theory']['id']}\n")
    parts.append(read_file_truncated(theory_path, max_chars))

    # Opponent page
    opponent_path = REPO_ROOT / config["opponent"]["page"]
    parts.append(f"\n## OPPONENT PAGE: {config['opponent']['id']}\n")
    parts.append(read_file_truncated(opponent_path, max_chars))

    # Extra files
    for fp in ctx.get("extra_files", []):
        full = REPO_ROOT / fp
        parts.append(f"\n## FILE: {fp}\n")
        parts.append(read_file_truncated(full, max_chars))

    # Evidence rows
    theory_ids = ctx.get("include_evidence_rows_for_theory_ids", [])
    if theory_ids:
        parts.append("\n## RELEVANT EVIDENCE (from data/evidence.csv)\n")
        parts.append(extract_evidence_rows(REPO_ROOT / "data" / "evidence.csv", theory_ids))

    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Prompt templates
# ---------------------------------------------------------------------------

COMMON_RULES = """\
RULES (you MUST follow all of these):
- Use ONLY the provided repo context. If information is missing, say what's missing and propose a decisive test.
- No rhetoric; list falsifiers.
- Prefer citations that already exist in this repo: DOIs in references.bib or URLs in references/links.yaml.
- Output ONLY valid JSON matching the provided schema. No markdown fences, no preamble."""

SCHEMA_INSTRUCTIONS = """\
Your output must be a single JSON object matching this schema:
{schema_text}"""


def make_defender_prompt(round_num: int, config: dict, context: str,
                         transcript: list[dict], schema_text: str) -> str:
    theory_id = config["theory"]["id"]
    opponent_id = config["opponent"]["id"]

    if round_num == 0:
        task = f"""\
You are the DEFENDER of the "{theory_id}" theory of aging.
Your opponent defends the "{opponent_id}" theory.

TASK (Round 0 - Opening Steelman):
Present the strongest possible case for your theory:
- 3-7 key_points: the core claims at their strongest
- 2-5 falsifiers: what specific observations would DISPROVE this theory?
- 2-5 proposed_experiments: risky predictions that discriminate your theory from {opponent_id}
Include repo_citations where available."""
    else:
        prev_critic = json.dumps(transcript[-1], indent=2) if transcript else "{}"
        task = f"""\
You are the DEFENDER of the "{theory_id}" theory of aging.
Your opponent defends the "{opponent_id}" theory.

TASK (Round {round_num} - Response to Criticism):
The critic's previous turn:
{prev_critic}

Respond to each criticism. You may update your core claims if needed, but:
- No ad hoc modifications (every update must generate new falsifiers)
- Must specify revised falsifiers
- 3-7 key_points (updated if needed)
- 2-5 falsifiers (revised)
- 2-5 proposed_experiments"""

    return f"""\
{task}

Set role="defender", round={round_num}, theory_id="{theory_id}", opponent_id="{opponent_id}".

{COMMON_RULES}

{SCHEMA_INSTRUCTIONS.format(schema_text=schema_text)}

## REPO CONTEXT

{context}"""


def make_critic_prompt(round_num: int, config: dict, context: str,
                       transcript: list[dict], schema_text: str) -> str:
    theory_id = config["theory"]["id"]
    opponent_id = config["opponent"]["id"]

    prev_defender = json.dumps(transcript[-1], indent=2) if transcript else "{}"

    if round_num == 1:
        task = f"""\
You are the CRITIC attacking the "{theory_id}" theory from the perspective of "{opponent_id}".

TASK (Round {round_num} - Attack):
The defender's opening:
{prev_defender}

Produce your strongest attack:
- 3-7 criticisms: strongest refutations, alternative explanations
- 2-5 falsifiers: what would falsify YOUR critique?
- 2-5 proposed_experiments: what decisive tests should come next?"""
    else:
        full_transcript = json.dumps(transcript, indent=2)
        task = f"""\
You are the CRITIC attacking the "{theory_id}" theory from the perspective of "{opponent_id}".

TASK (Round {round_num} - Final Assessment):
Full transcript so far:
{full_transcript}

Which of your critiques survived the defender's responses? What decisive experiment should come next?
- 3-7 criticisms (surviving + any new)
- 2-5 falsifiers
- 2-5 proposed_experiments"""

    return f"""\
{task}

Set role="critic", round={round_num}, theory_id="{theory_id}", opponent_id="{opponent_id}".

{COMMON_RULES}

{SCHEMA_INSTRUCTIONS.format(schema_text=schema_text)}

## REPO CONTEXT

{context}"""


def make_judge_prompt(config: dict, context: str, transcript: list[dict],
                      schema_text: str) -> str:
    theory_id = config["theory"]["id"]
    opponent_id = config["opponent"]["id"]
    full_transcript = json.dumps(transcript, indent=2)

    return f"""\
You are the JUDGE evaluating a Popperian debate between theories of aging.
Defender argued for "{theory_id}". Critic argued from the perspective of "{opponent_id}".

FULL TRANSCRIPT:
{full_transcript}

TASK:
Evaluate using Popperian criteria (falsifiability, severe testing, novel predictions, exposure to refutation).
Your message_markdown must include:
- winner: "defender", "critic", or "undecided"
- Top 3 surviving criticisms
- Top 3 strongest defenses
- "Decisive next tests" list

Set role="judge", round={len(transcript)}, theory_id="{theory_id}", opponent_id="{opponent_id}".
Include 3-7 key_points summarizing your verdict.

{COMMON_RULES}

{SCHEMA_INSTRUCTIONS.format(schema_text=schema_text)}

## REPO CONTEXT

{context}"""


# ---------------------------------------------------------------------------
# CLI callers
# ---------------------------------------------------------------------------

def call_codex(prompt: str, timeout: int = 300) -> dict:
    """Call codex exec with structured output. Prompt via stdin to avoid arg length limits."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        out_path = f.name
    try:
        cmd = [
            "codex", "exec",
            "--output-schema", str(SCHEMA_PATH),
            "-o", out_path,
            "-",  # read prompt from stdin
        ]
        result = subprocess.run(
            cmd, input=prompt, capture_output=True, text=True, timeout=timeout
        )
        if result.returncode != 0:
            print(f"  [WARN] codex exit code {result.returncode}", file=sys.stderr)
            if result.stderr:
                print(f"  stderr: {result.stderr[:500]}", file=sys.stderr)
        # Read structured output from -o file (cleanest source)
        if os.path.exists(out_path) and os.path.getsize(out_path) > 0:
            raw = Path(out_path).read_text().strip()
            if raw:
                return json.loads(raw)
        # Fallback: try to parse stdout (codex prints JSON to stdout too)
        return extract_json(result.stdout)
    finally:
        if os.path.exists(out_path):
            os.unlink(out_path)


def call_gemini(prompt: str, timeout: int = 300) -> dict:
    """Call gemini in headless mode. Prompt via stdin (gemini appends -p to stdin)."""
    cmd = ["gemini", "-p", "", "-o", "json"]
    result = subprocess.run(
        cmd, input=prompt, capture_output=True, text=True, timeout=timeout
    )
    if result.returncode != 0:
        print(f"  [WARN] gemini exit code {result.returncode}", file=sys.stderr)
        if result.stderr:
            print(f"  stderr: {result.stderr[:500]}", file=sys.stderr)
    return extract_json(result.stdout)


def call_claude(prompt: str, schema_text: str, timeout: int = 300) -> dict:
    """Call claude in print mode with JSON schema. Prompt via stdin."""
    cmd = [
        "claude", "-p",
        "--no-chrome",
        "--output-format", "json",
        "--json-schema", schema_text,
    ]
    result = subprocess.run(
        cmd, input=prompt, capture_output=True, text=True, timeout=timeout
    )
    if result.returncode != 0:
        print(f"  [WARN] claude exit code {result.returncode}", file=sys.stderr)
        if result.stderr:
            print(f"  stderr: {result.stderr[:500]}", file=sys.stderr)
    return extract_json(result.stdout)


def extract_json(text: str) -> dict:
    """Extract a JSON object from text, handling CLI wrappers, markdown fences, and preamble."""
    text = text.strip()
    # Try direct parse first
    try:
        parsed = json.loads(text)
        if isinstance(parsed, dict):
            # Unwrap CLI wrappers: Gemini {"response": ...}, Claude {"result": ...}
            for key in ("response", "result"):
                if key in parsed and isinstance(parsed[key], (str, dict)):
                    inner = parsed[key]
                    if isinstance(inner, str):
                        try:
                            return extract_json(inner)
                        except ValueError:
                            pass
                    elif isinstance(inner, dict):
                        return inner
            # Not a wrapper - return the parsed dict directly
            return parsed
    except json.JSONDecodeError:
        pass
    # Strip markdown fences
    if "```" in text:
        parts = text.split("```")
        for part in parts:
            part = part.strip()
            if part.startswith("json"):
                part = part[4:].strip()
            try:
                return json.loads(part)
            except json.JSONDecodeError:
                continue
    # Find first { ... last }
    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and end > start:
        try:
            return json.loads(text[start : end + 1])
        except json.JSONDecodeError:
            pass
    raise ValueError(f"Could not extract JSON from output:\n{text[:500]}")


PROVIDER_CALLERS = {
    "codex": call_codex,
    "gemini": call_gemini,
    "claude": lambda prompt, **kw: call_claude(prompt, kw.get("schema_text", "{}")),
}


# ---------------------------------------------------------------------------
# Debate runner
# ---------------------------------------------------------------------------

def run_debate(config: dict, no_judge: bool = False, timeout: int = 300):
    run_id = config["run_id"]
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    rounds = config.get("rounds", 4)

    print(f"\n{'='*60}")
    print(f"Debate: {run_id}")
    print(f"Theory: {config['theory']['id']} vs Opponent: {config['opponent']['id']}")
    print(f"Rounds: {rounds}  |  Timestamp: {timestamp}")
    print(f"{'='*60}\n")

    # Load schema
    schema_text = SCHEMA_PATH.read_text()

    # Build context
    print("Building context pack...")
    context = build_context_pack(config)
    print(f"  Context size: {len(context)} chars")

    # Output dirs
    runs_dir = REPO_ROOT / config["output"]["runs_dir"] / run_id / timestamp
    publish_dir = REPO_ROOT / config["output"]["publish_mkdocs_dir"]
    runs_dir.mkdir(parents=True, exist_ok=True)
    publish_dir.mkdir(parents=True, exist_ok=True)

    transcript: list[dict] = []
    roles_config = config["roles"]

    for round_num in range(rounds):
        if round_num % 2 == 0:
            # Defender turn
            role = "defender"
            provider = roles_config["defender"]["provider"]
            prompt = make_defender_prompt(round_num, config, context, transcript, schema_text)
        else:
            # Critic turn
            role = "critic"
            provider = roles_config["critic"]["provider"]
            prompt = make_critic_prompt(round_num, config, context, transcript, schema_text)

        print(f"\n--- Round {round_num} ({role}, provider={provider}) ---")
        print(f"  Prompt size: {len(prompt)} chars")

        caller = PROVIDER_CALLERS.get(provider)
        if not caller:
            print(f"  [ERROR] Unknown provider: {provider}", file=sys.stderr)
            sys.exit(1)

        try:
            if provider == "claude":
                turn = caller(prompt, schema_text=schema_text, timeout=timeout)
            else:
                turn = caller(prompt, timeout=timeout)
        except Exception as e:
            print(f"  [ERROR] {provider} call failed: {e}", file=sys.stderr)
            sys.exit(1)

        # Ensure required fields are set correctly
        turn["role"] = role
        turn["round"] = round_num
        turn["theory_id"] = config["theory"]["id"]
        turn["opponent_id"] = config["opponent"]["id"]

        transcript.append(turn)
        print(f"  Got {len(turn.get('key_points', []))} key_points, "
              f"{len(turn.get('criticisms', []))} criticisms, "
              f"{len(turn.get('falsifiers', []))} falsifiers")

    # Judge (optional)
    judge_turn = None
    if not no_judge and "judge" in roles_config:
        provider = roles_config["judge"]["provider"]
        print(f"\n--- Judge ({provider}) ---")
        prompt = make_judge_prompt(config, context, transcript, schema_text)
        print(f"  Prompt size: {len(prompt)} chars")

        caller = PROVIDER_CALLERS.get(provider)
        try:
            if provider == "claude":
                judge_turn = caller(prompt, schema_text=schema_text, timeout=timeout)
            else:
                judge_turn = caller(prompt, timeout=timeout)
        except Exception as e:
            print(f"  [ERROR] Judge call failed: {e}", file=sys.stderr)
            judge_turn = None

        if judge_turn:
            judge_turn["role"] = "judge"
            judge_turn["round"] = rounds
            judge_turn["theory_id"] = config["theory"]["id"]
            judge_turn["opponent_id"] = config["opponent"]["id"]
            transcript.append(judge_turn)
            print("  Judge verdict received.")

    # Write artifacts
    print(f"\n--- Writing artifacts ---")

    # JSONL
    if config["output"].get("write_raw_jsonl", True):
        jsonl_path = runs_dir / "turns.jsonl"
        with open(jsonl_path, "w") as f:
            for turn in transcript:
                f.write(json.dumps(turn) + "\n")
        print(f"  JSONL: {jsonl_path}")

    # Transcript markdown (run archive)
    transcript_md = format_transcript_md(config, timestamp, transcript, judge_turn)
    transcript_path = runs_dir / "transcript.md"
    transcript_path.write_text(transcript_md)
    print(f"  Transcript: {transcript_path}")

    # Published mkdocs page
    publish_path = publish_dir / f"{run_id}_{timestamp}.md"
    publish_path.write_text(transcript_md)
    print(f"  Published: {publish_path}")

    print(f"\nDebate complete. {len(transcript)} turns recorded.")
    return runs_dir, publish_path


def format_transcript_md(config: dict, timestamp: str,
                         transcript: list[dict], judge_turn: dict | None) -> str:
    theory_id = config["theory"]["id"]
    opponent_id = config["opponent"]["id"]
    run_id = config["run_id"]

    lines = [
        "---",
        f'title: "Debate: {theory_id} vs {opponent_id} ({timestamp})"',
        "---",
        "",
        f"# Debate: {theory_id} vs {opponent_id}",
        "",
        f"**Run ID:** {run_id}  ",
        f"**Timestamp:** {timestamp}  ",
        f"**Defender (theory):** [{theory_id}](../theories/{config['theory']['page'].split('/')[-1]})  ",
        f"**Critic (opponent):** [{opponent_id}](../theories/{config['opponent']['page'].split('/')[-1]})",
        "",
        "---",
        "",
    ]

    for turn in transcript:
        if turn["role"] == "judge":
            continue
        role_label = turn["role"].upper()
        lines.append(f"## Round {turn['round']} — {role_label}")
        lines.append("")
        lines.append(turn.get("message_markdown", "*No message provided.*"))
        lines.append("")

        if turn.get("key_points"):
            lines.append("**Key Points:**")
            for kp in turn["key_points"]:
                lines.append(f"- {kp}")
            lines.append("")

        if turn.get("criticisms"):
            lines.append("**Criticisms:**")
            for c in turn["criticisms"]:
                lines.append(f"- {c}")
            lines.append("")

        if turn.get("falsifiers"):
            lines.append("**Falsifiers:**")
            for f in turn["falsifiers"]:
                lines.append(f"- {f}")
            lines.append("")

        if turn.get("proposed_experiments"):
            lines.append("**Proposed Experiments:**")
            for e in turn["proposed_experiments"]:
                lines.append(f"- {e}")
            lines.append("")

        if turn.get("repo_citations"):
            lines.append("**Citations:**")
            for c in turn["repo_citations"]:
                lines.append(f"- {c}")
            lines.append("")

        lines.append("---")
        lines.append("")

    # Judge section
    if judge_turn:
        lines.append("## Judge Verdict")
        lines.append("")
        lines.append(judge_turn.get("message_markdown", "*No verdict provided.*"))
        lines.append("")

        if judge_turn.get("key_points"):
            lines.append("**Summary:**")
            for kp in judge_turn["key_points"]:
                lines.append(f"- {kp}")
            lines.append("")
    else:
        lines.append("## Judge Verdict")
        lines.append("")
        lines.append("*Judge was not run for this debate.*")
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Run a structured debate")
    parser.add_argument(
        "--config", "-c", required=True, help="Path to debate YAML config"
    )
    parser.add_argument(
        "--no-judge", action="store_true", help="Skip the judge step"
    )
    parser.add_argument(
        "--timeout", type=int, default=300,
        help="Timeout per CLI call in seconds (default 300)",
    )
    args = parser.parse_args()

    config_path = Path(args.config)
    if not config_path.is_absolute():
        config_path = REPO_ROOT / config_path

    if not config_path.exists():
        print(f"Config not found: {config_path}", file=sys.stderr)
        sys.exit(1)

    config = yaml.safe_load(config_path.read_text())
    runs_dir, publish_path = run_debate(config, no_judge=args.no_judge, timeout=args.timeout)

    print(f"\nArtifacts:")
    print(f"  Run dir:   {runs_dir}")
    print(f"  Published: {publish_path}")


if __name__ == "__main__":
    main()
