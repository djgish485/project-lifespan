---
title: Debate Orchestrator Protocol (Codex)
---

# Debate Orchestrator Protocol (Codex)

This page defines a simple, repeatable workflow for running Popperian debates between two models:

- **Defender** (steelmans a theory)
- **Critic** (attacks it and demands hard-to-vary mechanism + discriminators)

The goal is not "who sounds smarter". The goal is to produce **discriminator experiments** that would clearly favor one theory (or set of auxiliaries) over rivals.

Unique marker for verification: `ORCHESTRATOR_PROTOCOL_V1`

## Workspace

- Transcript (published): `docs/debates/scratchpad.md`
- Defender tool (Gemini CLI): `bash tools/ask_gemini.sh "<THEORY_FILE>" "<PROMPT>"`
- Critic tool: `bash tools/ask_critic.sh "<ARGUMENT>"`
- Tool notes: `tools/README.md`

Defender model:

- Default: `gemini-3-flash-preview` (set `GEMINI_CLI_MODEL` to override).
- To confirm the actual model used, run with `GEMINI_OUTPUT=json` and check `stats.models` in the output.

## Coordination Loop

### 1) Initialization

Pick:

- Origin theory page (e.g. `docs/theories/epigenetic_information.md`)
- 1 rival to compare against

Write a debate header into `docs/debates/scratchpad.md`:

- Debate: A vs B
- Date
- Question: 1 sentence

### 2) Defender Opening Statement

Ask the Defender for a steelman that is *mechanistic* and *testable*:

- Core causal mechanism (what changes, where, in which cells, and why that causes aging)
- 2–4 risky predictions
- 1–2 "if this fails, we are wrong" failure modes

Logic check before accepting:

- Reject if it’s mostly vibes ("complex", "multi-factor", "more research").
- Reject if it doesn’t say what would falsify it.

### 3) Critic Attack

Send the strongest, most specific part of the Defender’s argument to the Critic.

Acceptable Critic output:

- Identifies missing mechanistic links
- Names hidden auxiliaries
- Proposes 1–3 discriminator experiments with predicted outcomes

Reject if it only lists generic objections ("correlation isn’t causation") without pointing to a concrete missing link.

### 4) Defender Rebuttal

Give the Defender a short summary of the Critic’s *best* objection(s), and ask for:

- A direct rebuttal (or an admission + narrowed claim)
- Updated predictions that are more precise
- Updated discriminator experiments (if needed)

### 5) Verdict (Orchestrator Writes This)

Without calling a model, write a short verdict section:

- What the debate resolved (if anything)
- What is still underspecified
- The **single best discriminator experiment**:
  - Model/system
  - Intervention
  - Readouts
  - Prediction under Theory A
  - Prediction under Theory B

## Output Format (Scratchpad)

Use consistent sections:

- `## Opening (Defender)`
- `## Critique (Critic)`
- `## Rebuttal (Defender)`
- `## Verdict (Orchestrator)`
- `## Discriminator Experiment`
