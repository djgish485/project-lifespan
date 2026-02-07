---
title: Debates
---

# Debates

Structured Popperian debates between aging theories, run by AI agents.

## How it works

Each debate pits a **Defender** (steelmanning a theory) against a **Critic**
(attacking it from a rival theory's perspective). An optional **Judge**
(Claude in print mode) evaluates which criticisms survived and which
defenses held up, applying Popperian criteria.

### Debate structure

| Round | Role     | Task |
|-------|----------|------|
| 0     | Defender | Opening steelman: best case, risky predictions, discriminators |
| 1     | Critic   | Strongest refutations, alternative explanations, falsifiers |
| 2     | Defender | Responses + revised claims (no ad hoc moves; must specify revised falsifiers) |
| 3     | Critic   | Final assessment: which critiques survived? What decisive experiment comes next? |
| Final | Judge    | Verdict: winner, top surviving criticisms, strongest defenses, decisive next tests |

### Running a debate

```bash
# Smoke-test CLI availability
python scripts/agent_smoketest.py

# Run a debate from config
python scripts/run_debate.py --config debates/configs/example_sinclair_vs_sens.yaml

# Skip the judge step
python scripts/run_debate.py --config debates/configs/example_sinclair_vs_sens.yaml --no-judge
```

## Completed runs

| Date | Debate | Winner | Decisive next test |
|------|--------|--------|--------------------|
| 2026-02-07 | [Sinclair vs SENS](example_sinclair_vs_sens_20260207T162356Z.md) | Critic (SENS) | Pre-registered factorial OSK vs repair stack vs combo in aged WT mice |
| 2026-02-07 | [PC vs Sinclair](pc_vs_sinclair_20260207T170732Z.md) | Critic (Sinclair) | OSK under chronic infection: does pathogen challenge penalize epigenetic reset? |

## Available configs

| Config | Defender | Critic | Focus |
|--------|----------|--------|-------|
| `example_sinclair_vs_sens.yaml` | Sinclair | SENS | Epigenetic reset vs damage repair primacy |
| `pc_vs_sinclair.yaml` | Pathogen Control | Sinclair | OSK under chronic infection tradeoff |
| `pc_vs_sens.yaml` | Pathogen Control | SENS | Stacked repairs under chronic infection |
| `pc_vs_fedichev.yaml` | Pathogen Control | Resilience | Anti-pathogen vs resilience metrics |
| `pc_vs_levin.yaml` | Pathogen Control | Bioelectric | Bioelectric regeneration under pathogen challenge |
