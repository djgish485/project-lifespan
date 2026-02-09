---
title: Debate Methodology
---

# Debate Methodology

How the debates were run, what models were used, and how the project was guided.

---

## 1. The debate engine

All debates are run by `scripts/run_debate.py`, a config-driven Python script that orchestrates three AI agents — a Defender, a Critic, and a Judge — in a structured Popperian format.

### Debate structure

Each debate follows a fixed 4-round protocol plus a judge verdict:

| Round | Role | Task |
|:-----:|----------|------|
| 0 | Defender | Opening steelman: strongest case for the theory, risky predictions, discriminating experiments |
| 1 | Critic | Strongest refutations from the rival theory's perspective, alternative explanations, falsifiers |
| 2 | Defender | Response to criticism: update claims (no ad hoc moves), revise falsifiers, propose experiments |
| 3 | Critic | Final assessment: which critiques survived? What decisive experiment should come next? |
| Final | Judge | Popperian verdict: winner, top 3 surviving criticisms, top 3 defenses, decisive next tests |

### Key rules enforced in all prompts

Every debater is bound by `COMMON_RULES` in the prompt:

- **Repo-grounded only:** Use only the provided repo context (theory pages, evidence.csv, references). If information is missing, say what's missing and propose a test.
- **No rhetoric; list falsifiers:** Every claim must come with what would disprove it.
- **Bridge-assumptions prompt:** Before arguing, state whether each claim is **ultimate (evolutionary)**, **proximate (mechanistic)**, or **measurement-level (biomarker/dynamics)**, and name the bridge assumptions connecting levels. This prevents cross-level talking past.
- **Structured JSON output:** All turns are valid JSON matching `debates/schemas/turn.schema.json` — no free-form text.

### Context pack

Each debate receives a context pack built from the YAML config, including:

- The defender's theory page (from `docs/theories/`)
- The opponent's theory page
- The Popperian comparison rubric (`docs/compare/rubric.md`)
- The claims registry (`data/claims.yaml`)
- Relevant evidence rows from `data/evidence.csv`
- References (`references/references.bib`, `references/links.yaml`)
- The criticisms backlog (`debates/backlog.yaml`) — added in Season 3 so the judge can reference prior debates

Context is truncated at 60,000 characters per file to stay within model context limits.

---

## 2. Models used

Three different AI models serve the three debate roles. The intent is model diversity — no single model's biases dominate the outcome.

### Seasons 1 and 2 (2026-02-07 to 2026-02-08)

| Role | Provider | Model | Configuration |
|------|----------|-------|--------------|
| **Defender** | Gemini CLI | `gemini-3-flash-preview` | Thinking: auto-enabled; output: JSON mode |
| **Critic** | Codex CLI (OpenAI) | `gpt-5.3-codex` | Reasoning effort: high; structured output via `--output-schema` |
| **Judge** | Claude CLI (Anthropic) | `claude-opus-4-6` | Extended thinking; JSON schema enforcement |

All three CLIs receive prompts via stdin to avoid shell argument length limits (prompts routinely exceed 50,000 characters).

### Season 3 reruns (2026-02-08)

| Role | Provider | Model | Configuration |
|------|----------|-------|--------------|
| **Defender** | Gemini CLI | `gemini-3-flash-preview` | Same as S1/S2 |
| **Critic** | Gemini CLI | `gemini-3-flash-preview` | **Changed from codex** — see below |
| **Judge** | Claude CLI | `claude-opus-4-6` | Same as S1/S2, plus new structured output fields |

**Why codex was replaced:** The OpenAI Codex CLI consistently rejected Season 3 critic prompts with exit code 1 and empty output. The adversarial framing ("You are the CRITIC attacking...") appears to trigger OpenAI's content safety filters. Symptoms: exit code 1, the prompt echoed back in stderr, no structured output produced. After multiple retries (sequential and parallel), the critic role was switched to Gemini for Season 3 reruns.

### Model details

**Gemini (gemini-3-flash-preview):** Google's Gemini 3 Flash model accessed via the `gemini` CLI. Invoked as `gemini -m gemini-3-flash-preview -p "" -o json` with prompt on stdin. The model name must be specified exactly — `gemini-3-flash` alone returns a 404. Output is wrapped in `{session_id, response, stats}` — the runner unwraps the `response` field.

**Codex (gpt-5.3-codex):** OpenAI's Codex model accessed via the `codex` CLI. Invoked as `codex exec --output-schema <schema> -o <outfile> -` with prompt on stdin. Structured output written to a file via `-o`. Used in Seasons 1–2 only.

**Claude (claude-opus-4-6):** Anthropic's Claude Opus 4.6 model accessed via the `claude` CLI. Invoked as `claude -p --no-chrome --output-format json --json-schema '<schema>'` with prompt on stdin. Extended thinking is enabled by default for this model.

---

## 3. Judge output format (Season 3+)

Starting in Season 3, the judge produces three additional structured fields beyond the standard verdict:

### Backlog edits

The judge proposes specific changes to `debates/backlog.yaml`:

| Action | Meaning |
|--------|---------|
| `create` | New criticism discovered in this debate |
| `update` | Existing criticism refined or re-scoped |
| `resolve` | Criticism closed by evidence or operationalization |

Each edit includes an ID (e.g., `S3-CLASSICS-PC-01`), a type (measurement-gap, bridge-assumption, missing-severe-test, or definitional-escape), and a statement.

### Claim edits

The judge proposes changes to `data/claims.yaml`:

| Action | Meaning |
|--------|---------|
| `propose` | New prediction should be registered |
| `strengthen` | Existing prediction is better supported after this debate |
| `weaken` | Existing prediction is undermined after this debate |

Each edit includes the theory ID, claim ID, and a rationale grounded in the debate transcript.

### Changes since prior debate

A markdown summary comparing this debate to any prior debates on the same theory pairing. Tracks which criticisms were previously raised, which have been addressed, and which are new.

These structured outputs are rendered as tables in the published debate transcript and enable automated backlog/claims tracking.

---

## 4. Bidirectional stress-testing

A key methodological innovation introduced in Season 2: for any debate where Theory A defends and Theory B criticizes, run the reverse (B defends, A criticizes) to detect **one-way artifacts**.

**Finding:** The critic wins in both directions for every pairing tested. This confirmed that the Popperian scoring is functioning as a gap-finder — every theory has vulnerabilities when defending, regardless of which rival is attacking.

**Consequence:** The apparent Season 1 "winners" (Bottleneck had a +2 net score) collapsed to 0 after reverse testing. The lead was an artifact of only being tested as critic.

---

## 5. Operationalization protocol (Season 3)

When the judge or expert review identifies a **definitional escape** (a claim so vague it can absorb any result), the resolution protocol is:

1. Convert the vague claim into a numeric prediction with explicit thresholds
2. Register it in `data/claims.yaml` with: measurable prediction, organism, timeframe, threshold, falsifier, decisive test
3. Mark the backlog item as `resolved` with `resolution_kind: spec` (specification fix, no new data)
4. Rerun the relevant debate to verify the fix increased falsifiability and didn't introduce new escapes

This is how two backlog items (S1-CLASSICS-PC-01 and S2-BOTTLENECK-FEDICHEV-01) were resolved without running new experiments.

---

## 6. Expert guidance: ChatGPT Pro (o1-pro / GPT-5.2)

This project was guided throughout by expert-level strategic feedback from **ChatGPT Pro** (OpenAI's o1-pro reasoning model, later GPT-5.2), operating as an external advisor to the project maintainer.

### What the expert provided

- **Season 1 roadmap:** The original 5-step plan (ship to main → bidirectional stress-tests → research agenda → criticism backlog → operationalization) that structured the entire debate pipeline
- **Season 3 strategy:** The shift from "more debates" to "close the backlog" — identifying that further debates without new evidence would generate diminishing returns
- **Season 4 direction:** The recommendation to stop debate-driven exploration and move to evidence-driven closure, including the prioritized checklist for pre-registration completion
- **Methodological corrections:** Identifying that resolved backlog items needed `spec` vs `evidence` labels to prevent confusing definitional fixes with empirical closure; flagging the backlog.md staleness issue
- **Grand Synthesis framing:** The recommendation to write a conditional synthesis page that presents the current map with explicit forks where reality will decide, rather than premature truth claims
- **Epistemic guardrails:** Repeatedly reinforcing that the system is a "gap-finder, not truth-determiner" and that "verdict flip readiness: 0" is the honest signal

### What the expert did not do

The expert did not write code, run debates, or produce any of the debate transcripts, claims, or backlog items. All execution — prompt engineering, CLI integration, debate running, artifact generation, and documentation — was performed by **Claude Code** (Anthropic's Claude Opus 4.6) operating as the implementation agent.

### The collaboration model

```
ChatGPT Pro (expert/strategist)
    ↓ strategic feedback, roadmaps, methodological corrections
Project maintainer (human)
    ↓ instructions, approvals, direction
Claude Code (implementation agent)
    ↓ code, debates, documentation, artifacts
Gemini + Codex + Claude (debate agents)
    ↓ debate turns, judge verdicts
```

This multi-model architecture means no single AI provider controls the entire pipeline. The strategic layer, implementation layer, and debate agents are all different models from different providers.

---

## 7. Artifacts and file structure

### Per-debate outputs

Each debate run produces:

| Artifact | Location | Purpose |
|----------|----------|---------|
| Raw JSONL | `debates/runs/{run_id}/{timestamp}/turns.jsonl` | Machine-readable transcript (gitignored) |
| Transcript markdown | `debates/runs/{run_id}/{timestamp}/transcript.md` | Archive copy (gitignored) |
| Published page | `docs/debates/{run_id}_{timestamp}.md` | MkDocs-rendered debate page (committed) |

### Project-wide tracking

| File | Purpose |
|------|---------|
| `data/claims.yaml` | 14 predictions across 7 theories with numeric thresholds and falsifiers |
| `debates/backlog.yaml` | 20 tracked criticisms with status and resolution tracking |
| `docs/debates/backlog.md` | Auto-generated from YAML; CI-checked for freshness |
| `docs/experiments/research_agenda.md` | 5 decisive experiments with links to pre-registration protocols |
| `docs/experiments/prereg_*.md` | 5 full pre-registration protocols with decision matrices |
| `docs/synthesis/grand_synthesis.md` | Conditional synthesis: current map + what would change it |
| `DEBATE_RESULTS_SEASON1.md` | Copy-pastable expert brief with all results and metrics |

### Config-driven design

Every debate is fully specified by a YAML config in `debates/configs/`. Configs specify:

- Which theory defends and which attacks
- Which AI provider handles each role
- Which repo files are included in the context pack
- Output directories for runs and published pages

This means any debate can be reproduced exactly by re-running its config.
