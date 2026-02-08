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

### Deep theory clashes (Season 1)

| Date | Debate | Clash axis | Winner | Decisive next test |
|------|--------|------------|--------|--------------------|
| 2026-02-07 | [Classics vs PC](classics_vs_pc_20260207T181720Z.md) | Ultimate cause | Critic (PC) | Pre-registered 2x2x2 factorial: longevity intervention x environment x anti-pathogen, with infection-ecology endpoints |
| 2026-02-07 | [PC vs Classics](pc_vs_classics_20260207T183126Z.md) | Ultimate cause (reversed) | Critic (Classics) | Same factorial; PC needs empirical base beyond modeling and review |
| 2026-02-07 | [Fedichev vs Bottleneck](fedichev_vs_bottleneck_20260207T184739Z.md) | What sets hazard | Critic (Bottleneck) | Resilience autocorrelation vs bottleneck pathway intervention head-to-head |
| 2026-02-07 | [Sinclair vs Levin](sinclair_vs_levin_20260207T185829Z.md) | Locus of control | Critic (Levin) | OSK vs bioelectric modulation vs combo, with durability-across-re-injury endpoint |
| 2026-02-07 | [SENS vs Bottleneck](sens_vs_bottleneck_20260207T191058Z.md) | What sets hazard | Critic (Bottleneck) | Single bottleneck fix vs multi-class repair stack on max lifespan |

### Bidirectional stress-tests (Season 2)

| Date | Debate | Clash axis | Winner | Decisive next test |
|------|--------|------------|--------|--------------------|
| 2026-02-08 | [Bottleneck vs SENS](bottleneck_vs_sens_20260208T120248Z.md) | What sets hazard (reversed) | Critic (SENS) | Bottleneck's "saturation after clamp" is untested; SENS has survival data |
| 2026-02-08 | [Bottleneck vs Fedichev](bottleneck_vs_fedichev_20260208T121235Z.md) | What sets hazard (reversed) | Critic (Fedichev) | Pathway Residual never operationalized with thresholds |
| 2026-02-08 | [Levin vs Sinclair](levin_vs_sinclair_20260208T121927Z.md) | Locus of control (reversed) | Critic (Sinclair) | Levin's bridge assumptions untested in aged mammals |

### Pathogen Control rivalries

| Date | Debate | Winner | Decisive next test |
|------|--------|--------|--------------------|
| 2026-02-07 | [PC vs SENS](pc_vs_sens_20260207T192144Z.md) | Critic (SENS) | Stacked repairs under infection challenge; does repair extend pathogen persistence? |
| 2026-02-07 | [PC vs Fedichev](pc_vs_fedichev_20260207T193345Z.md) | Critic (Fedichev) | Anti-pathogen intervention vs resilience-metric intervention on mortality hazard |
| 2026-02-07 | [PC vs Levin](pc_vs_levin_20260207T194909Z.md) | Critic (Levin) | Bioelectric regeneration under pathogen challenge for infection tradeoffs |

### Season 3 reruns (post-operationalization)

| Date | Debate | Clash axis | Winner | Key finding |
|------|--------|------------|--------|-------------|
| 2026-02-08 | [Classics vs PC (S3)](classics_vs_pc_20260208T160443Z.md) | Ultimate cause | Critic (PC) | Classics-p1 tradeoff thresholds resolved definitional escape, but disjunctive structure reduces riskiness; 2 new criticisms identified |
| 2026-02-08 | [Bottleneck vs Fedichev (S3)](bottleneck_vs_fedichev_20260208T161116Z.md) | What sets hazard | Critic (Fedichev) | Bottleneck-p2 Pathway Residual operationalized, but Gompertz slope invariance + incomplete panel escape are new vulnerabilities |

### Earlier runs

| Date | Debate | Winner | Decisive next test |
|------|--------|--------|--------------------|
| 2026-02-07 | [Sinclair vs SENS](example_sinclair_vs_sens_20260207T162356Z.md) | Critic (SENS) | Pre-registered factorial OSK vs repair stack vs combo in aged WT mice |
| 2026-02-07 | [PC vs Sinclair](pc_vs_sinclair_20260207T170732Z.md) | Critic (Sinclair) | OSK under chronic infection: does pathogen challenge penalize epigenetic reset? |

## Available configs

### Deep theory clashes (Season 1)

| Config | Defender | Critic | Clash axis | Focus |
|--------|----------|--------|------------|-------|
| `classics_vs_pc.yaml` | Classic Models | Pathogen Control | Ultimate cause (evolutionary) | Is aging adaptive or an emergent byproduct? |
| `pc_vs_classics.yaml` | Pathogen Control | Classic Models | Ultimate cause (role-reversed) | Twin run to detect prompt/role bias |
| `fedichev_vs_bottleneck.yaml` | Resilience/Criticality | Longevity Bottleneck | What sets hazard | Dynamical systems vs molecular choke points |
| `sinclair_vs_levin.yaml` | Sinclair | Levin | Locus of control | Nuclear epigenetic state vs morphogenetic goal |
| `sens_vs_bottleneck.yaml` | SENS | Longevity Bottleneck | What sets hazard | Multi-lesion repair stack vs few choke points |

### Bidirectional stress-tests (Season 2)

| Config | Defender | Critic | Focus |
|--------|----------|--------|-------|
| `bottleneck_vs_sens.yaml` | Longevity Bottleneck | SENS | Reverse: can Bottleneck cash out its own discriminator? |
| `bottleneck_vs_fedichev.yaml` | Longevity Bottleneck | Fedichev | Reverse: Pathway Residual operationalization |
| `levin_vs_sinclair.yaml` | Levin | Sinclair | Reverse: can Levin defend bridge assumptions in mammals? |

### Pathogen Control rivalries

| Config | Defender | Critic | Focus |
|--------|----------|--------|-------|
| `example_sinclair_vs_sens.yaml` | Sinclair | SENS | Epigenetic reset vs damage repair primacy |
| `pc_vs_sinclair.yaml` | Pathogen Control | Sinclair | OSK under chronic infection tradeoff |
| `pc_vs_sens.yaml` | Pathogen Control | SENS | Stacked repairs under chronic infection |
| `pc_vs_fedichev.yaml` | Pathogen Control | Resilience | Anti-pathogen vs resilience metrics |
| `pc_vs_levin.yaml` | Pathogen Control | Bioelectric | Bioelectric regeneration under pathogen challenge |
