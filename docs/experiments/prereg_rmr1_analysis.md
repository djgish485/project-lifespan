---
title: "Pre-Registration: RMR1 Factorial Analysis Plan"
---

# Pre-Registration: RMR1 Factorial Analysis Plan

**Protocol version:** 1.0
**Date:** 2026-02-08
**Status:** Draft — pre-registered analysis plan for when RMR1 data become available
**Parent:** [Research Agenda #5](research_agenda.md#5-rmr1-factorial-publication)

---

## 1. Context

The Robust Mouse Rejuvenation Study 1 (RMR1) is being conducted by the LEV Foundation. This document pre-registers the analysis we will perform **the moment RMR1 data are publicly available**, to prevent post-hoc reinterpretation.

**Source:** [LEVF RMR1](https://www.levf.org/projects/robust-mouse-rejuvenation-study-1)

This is not a protocol for a new experiment — it is a pre-registered analysis plan for an existing study's data.

---

## 2. Hypotheses

### Primary Hypotheses

| ID | Theory favored | Hypothesis | Threshold |
|----|---------------|------------|-----------|
| H1 | SENS | Multi-class repair stack shows super-additive synergy on max lifespan | At least one pairwise interaction term HR < 0.85 (≥15% additional hazard reduction beyond additive), p < 0.05 |
| H2 | Bottleneck | Single best component captures ≥80% of the stack's max lifespan gain | Best single-component arm achieves ≥80% of full-stack arm's gain over vehicle |
| H3 | SENS | All-but-one arms show significant degradation vs full stack | Each "drop one" arm loses ≥10% of full-stack gain, for every component |
| H4 | Bottleneck | Dropping any single component (except the bottleneck-targeting one) has ≤5% effect | At least one "drop one" arm within 5% of full stack |

### Secondary Hypotheses

| ID | Hypothesis | Threshold |
|----|------------|-----------|
| H5 | Target engagement predicts survival contribution | Per-component target engagement level correlates with per-component survival contribution (r ≥0.5 across components) |
| H6 | Bottleneck pathway readouts explain most of the survival variance | SASP/mTOR panel R² ≥0.60 in survival model |
| H7 | Gompertz doubling rate changes with stack | Full-stack β differs from vehicle β by ≥20% |

---

## 3. Required Data Elements

We will only proceed with analysis when the following are available:

| Data element | Why required |
|-------------|-------------|
| Individual-level survival data (time to death, censoring) for all arms | Primary endpoint |
| Arm assignments including full stack, each single component, all-but-one arms, vehicle | Factorial structure |
| Maximum lifespan per arm (or raw data to calculate) | Wang-Allison method |
| Per-component target engagement biomarkers at ≥1 timepoint | Target verification |
| Bottleneck pathway readouts (p16, IL-6, SASP, mTOR activity) | Mediation/variance decomposition |
| Sample sizes per arm | Power verification |
| Blinding/randomization details | Bias assessment |
| Pathology data (cause of death, tumor incidence) | Safety and mechanistic interpretation |

---

## 4. Statistical Analysis Plan

### 4.1 Primary analysis: Interaction terms (H1)

**Model:** Factorial Cox proportional hazards

If RMR1 has K components (expected K = 4–6), the model includes all main effects and pairwise interactions:

```
h(t) ~ Component1 * Component2 * ... * ComponentK + Sex
```

For computational tractability with K > 4, fit:

```
h(t) ~ Σ(main effects) + Σ(pairwise interactions) + Sex
```

- **H1 test:** Any pairwise interaction HR < 0.85 at p < 0.05 (Holm-corrected for K*(K-1)/2 interactions)
- **H2 test:** Calculate ratio: best single-component arm gain / full-stack gain. If ≥0.80 → Bottleneck supported

### 4.2 All-but-one analysis (H3, H4)

For each component i:

```
ΔLS_i = (MaxLS_fullstack - MaxLS_drop_i) / (MaxLS_fullstack - MaxLS_vehicle)
```

- **H3 (SENS):** All ΔLS_i ≥ 0.10 (every component contributes ≥10%)
- **H4 (Bottleneck):** At least one ΔLS_i ≤ 0.05 (at least one component is dispensable)

Report with bootstrapped 95% CIs for each ΔLS_i.

### 4.3 Target engagement correlation (H5)

For each component i, define:
- Target engagement level: biomarker change from vehicle (standardized)
- Survival contribution: ΔLS_i as defined above

**Test:** Spearman correlation across components. H5 requires r ≥ 0.5.

### 4.4 Bottleneck pathway mediation (H6)

**Variance decomposition:**

```
log(hazard) ~ SASP_panel + mTOR_readout + p16 + Sex + Age
```

- Report R² of bottleneck panel in explaining survival variation
- H6: R² ≥ 0.60

### 4.5 Gompertz analysis (H7)

**Parametric fit per arm:**

```
μ(t) = c + α·exp(β·t)
```

- Compare β(full_stack) vs β(vehicle)
- H7: |β_stack - β_vehicle| / β_vehicle ≥ 0.20

### 4.6 Multiple comparison correction

| Family | Tests | Correction |
|--------|:-----:|-----------|
| Pairwise interactions | K*(K-1)/2 | Holm |
| All-but-one ΔLS | K | Report all with CIs; no formal correction (descriptive) |
| Target engagement correlation | 1 | α = 0.05 |
| Bottleneck mediation | 1 | α = 0.05 |
| Gompertz | 1 | α = 0.05 |

---

## 5. Decision Matrix

| Outcome pattern | H1 | H2 | H3 | Verdict |
|----------------|:--:|:--:|:--:|---------|
| ≥1 synergistic interaction; all components contribute ≥10% | ✓ | ✗ | ✓ | **Strongly favors SENS**: multi-class necessity confirmed |
| No synergy; best single component captures ≥80% of gain | ✗ | ✓ | ✗ | **Strongly favors Bottleneck**: one pathway dominates |
| No synergy; multiple components each contribute 10-30% | ✗ | ✗ | ✓ | **Weak SENS**: additive multi-class, not synergistic |
| Full stack shows no gain over vehicle | — | — | — | **Inconclusive**: interventions failed or model is wrong |
| Synergy present but one component dominates (≥60% of gain) | ✓ | — | ✗ | **Mixed**: synergy exists but bottleneck structure present |

---

## 6. Power Considerations

Since we don't control the sample size, we will:

1. **Report achieved power** for each analysis given the actual N
2. **Flag underpowered analyses** explicitly rather than drawing conclusions from null results
3. **Pre-specify minimum N:** We will not perform synergy analysis if any arm has N < 15 (insufficient for interaction detection)

---

## 7. Sensitivity Analyses

1. **Proportional hazards check:** Schoenfeld residual test; if violated, use restricted mean survival time (RMST) instead
2. **Competing risks:** Fine-Gray model treating cancer deaths as competing risk for non-cancer mortality
3. **Per-protocol vs ITT:** If RMR1 has treatment discontinuation, report both
4. **Winsorized max lifespan:** 90th and 95th percentile comparisons alongside Wang-Allison method

---

## 8. Reporting Commitment

- All pre-specified analyses will be reported regardless of outcome
- Exploratory analyses clearly labeled as post-hoc
- This document's hash will be committed to the repo before RMR1 data access
- Any deviations documented with rationale

### Backlog items resolved by RMR1 data

- **S1-SENS-BOTTLENECK-01** (missing severe test): Interaction terms directly test multi-class necessity
- **S1-SENS-BOTTLENECK-02** (missing severe test): All-but-one arms test each component's contribution
