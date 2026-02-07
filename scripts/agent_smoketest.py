#!/usr/bin/env python3
"""Smoke-test that Codex, Gemini, and (optionally) Claude CLIs are callable."""

import argparse
import shutil
import subprocess
import sys


def check_binary(name: str) -> bool:
    path = shutil.which(name)
    if path:
        print(f"  [OK] {name} found at {path}")
        return True
    print(f"  [MISSING] {name} not found on PATH")
    return False


def run_pong_test(name: str, cmd: list[str], timeout: int = 60) -> bool:
    print(f"  Running: {' '.join(cmd)}")
    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout
        )
        stdout = result.stdout.strip()
        stderr = result.stderr.strip()
        if "PONG" in stdout.upper():
            print(f"  [PASS] {name} returned PONG")
            return True
        print(f"  [FAIL] {name} stdout did not contain PONG")
        if stdout:
            print(f"         stdout: {stdout[:200]}")
        if stderr:
            print(f"         stderr: {stderr[:200]}")
        return False
    except subprocess.TimeoutExpired:
        print(f"  [FAIL] {name} timed out after {timeout}s")
        return False
    except Exception as e:
        print(f"  [FAIL] {name} error: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Smoke-test AI CLI tools")
    parser.add_argument(
        "--no-claude", action="store_true", help="Skip Claude test"
    )
    parser.add_argument(
        "--timeout", type=int, default=60, help="Timeout per test in seconds"
    )
    args = parser.parse_args()

    results: dict[str, bool] = {}

    print("\n=== Binary check ===")
    for name in ["codex", "gemini", "claude"]:
        if name == "claude" and args.no_claude:
            continue
        check_binary(name)

    print("\n=== PONG tests ===")

    # Codex
    print("\n[codex]")
    results["codex"] = run_pong_test(
        "codex",
        ["codex", "exec", "Respond with exactly: PONG"],
        timeout=args.timeout,
    )

    # Gemini
    print("\n[gemini]")
    results["gemini"] = run_pong_test(
        "gemini",
        ["gemini", "-p", "Respond with exactly: PONG"],
        timeout=args.timeout,
    )

    # Claude (optional)
    if not args.no_claude:
        print("\n[claude]")
        results["claude"] = run_pong_test(
            "claude",
            ["claude", "-p", "Respond with exactly: PONG", "--no-chrome"],
            timeout=args.timeout,
        )

    # Summary
    print("\n=== Summary ===")
    all_pass = True
    for name, passed in results.items():
        status = "PASS" if passed else "FAIL"
        print(f"  {name}: {status}")
        if not passed:
            all_pass = False

    if all_pass:
        print("\nAll tests passed.")
        return 0
    else:
        print("\nSome tests failed.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
