---
title: "Pre-Registration: Bottleneck-Clamp + SENS Add-on"
---

# Pre-Registration: Bottleneck-Clamp + SENS Add-on

**Protocol version:** 1.0
**Date:** 2026-02-08
**Status:** Draft — awaiting expert review and registry submission
**Parent:** [Research Agenda #3](research_agenda.md#3-bottleneck-clamp-sens-add-on)

---

## 1. Hypotheses

### Primary Hypotheses

| ID | Theory favored | Hypothesis | Threshold |
|----|---------------|------------|-----------|
| H1 | SENS | After verified bottleneck clamp, adding TERT or crosslink breaker yields significant additional max lifespan gain | Arms B/C/D yield ≥10% additional max lifespan over Arm A |
| H2 | Bottleneck | After verified bottleneck clamp, adding further repair classes yields negligible gain (saturation) | Arms B/C/D yield ≤3% additional max lifespan over Arm A |

### Secondary Hypotheses

| ID | Hypothesis | Threshold |
|----|------------|-----------|
| H3 | Multi-class stack shows synergy (super-additive interaction) | Arm D gain > Arm B gain + Arm C gain; interaction p < 0.05 |
| H4 | Gompertz doubling rate flattens after bottleneck clamp (Bottleneck slope-driver claim) | Gompertz β reduced by ≥20% in Arm A vs vehicle historical controls |
| H5 | Gompertz doubling rate further flattens with add-on repairs (SENS scope-driver claim) | Gompertz β in Arms B/C/D reduced by ≥10% beyond Arm A |
| H6 | Pathway Residual after clamp is <20% of pre-intervention variance (bottleneck-p2) | Residual hazard variance <20% in Arm A |

---

## 2. Study Design

**Type:** Two-phase sequential design with clamp verification gate
**Organism:** C57BL/6J mice, 20+ months old, male and female balanced

### Phase 1: Clamp Verification (all mice)

All enrolled mice receive rapamycin (14 ppm diet) + D+Q senolytic (dasatinib 5 mg/kg + quercetin 50 mg/kg, biweekly oral gavage) for 8 weeks.

**Clamp verification criteria** (all must be met at T = 8 weeks):

| Biomarker | Target | Method |
|-----------|--------|--------|
| p-S6K (mTOR readout) | ≤40% of baseline | Western blot, PBMCs |
| p16^INK4a expression | ≤50% of baseline | RT-qPCR, skin biopsy |
| Plasma IL-6 | ≤60% of baseline | ELISA |
| SA-β-gal+ cells (liver) | ≤50% of baseline | Histology (biopsy at T=0 and T=8wk) |

Mice failing ≥2 criteria are excluded from Phase 2 (expected ~15% failure rate).

### Phase 2: Randomization (clamp-verified mice only)

| Arm | Treatment | Purpose |
|-----|-----------|---------|
| A | Clamp only (continue rapamycin + D+Q) | Bottleneck-saturated baseline |
| B | Clamp + TERT activation (AAV9-mTERT, single IV dose, 10¹¹ vg) | Test telomere repair add-on |
| C | Clamp + crosslink breaker (alagebrium 10 mg/kg/day in diet) | Test ECM repair add-on |
| D | Clamp + TERT + crosslink breaker | Multi-class stack |

### Timeline

- **T = 0:** Enrollment at 20+ months; baseline biomarkers; Phase 1 clamp initiation
- **T = 8 weeks:** Clamp verification blood draw + skin biopsy; exclusion of non-responders
- **T = 8 weeks:** Phase 2 randomization for clamp-verified mice
- **T = 8 weeks onward:** Add-on treatments initiated; rapamycin + D+Q continue in all arms
- **T = death:** Lifetime follow-up; full necropsy on all natural deaths

---

## 3. Sample Size and Power Analysis

### Primary endpoint: Max lifespan (H1 vs H2)

- **Effect size to detect:** 10% max lifespan gain (Arm B/C/D over Arm A), ~90 days from expected ~900 days remaining at 20 months
- **Within-group SD:** Estimated 80 days (from ITP rapamycin cohorts)
- **Test:** Dunnett's (each add-on arm vs clamp-only), one-sided α = 0.05/3 = 0.017
- **Power:** 0.85
- **Required n per arm at Phase 2:** 28
- **Accounting for 15% Phase 1 exclusion:** Enroll 33 per arm

### Total animals

| Phase | N per arm | Arms | Total |
|-------|:-:|:-:|:-:|
| Phase 1 enrollment | 33 | 4 | 132 |
| Expected Phase 2 (post-clamp) | ~28 | 4 | ~112 |
| **Total enrolled** | | | **132** |

**Sex balance:** 50/50 male/female within each arm.

---

## 4. Randomization

- **Phase 1:** All mice receive identical clamp treatment (no randomization needed)
- **Phase 2:** Stratified block randomization of clamp-verified mice
- **Stratification:** Sex, clamp biomarker response quartile (composite of 4 markers)
- **Block size:** 4, randomly permuted
- **Allocation concealment:** Coded cage cards; add-on treatments prepared by unblinded pharmacist

---

## 5. Blinding

| Role | Blinded to |
|------|-----------|
| Animal care staff | Phase 2 arms (all mice on same rapamycin + D+Q base) |
| Necropsy pathologist | All arms — coded specimens |
| Gompertz model analyst | All arms — coded survival data |
| Biomarker technician | All arms — coded samples |
| Statistician | Treatment until pre-specified analysis code has run |
| AAV injection technician | NOT blinded (TERT vs vehicle injection). Mitigated: Arms A/C receive sham IV injection (saline) |

---

## 6. Endpoints

### Primary endpoint

1. **Maximum lifespan:** Wang-Allison 90th percentile survival, bootstrapped 95% CI

### Secondary endpoints

2. **Median lifespan:** Kaplan-Meier estimate per arm
3. **Gompertz parameters:** Mortality rate doubling time (β) and baseline mortality (α) from parametric survival fit
4. **Hazard interaction terms:** Test for super-additivity in Arm D vs Arms B + C (synergy test)
5. **Target engagement verification:**
   - Telomere length (qFISH, PBMCs at T=6 months post-randomization) — Arm B/D should show ≥15% increase
   - AGE crosslink density (skin fluorescence at T=6 months) — Arm C/D should show ≥20% reduction
6. **Pathway Residual:** Variance in mortality hazard explained by clamp biomarkers vs total variance (for bottleneck-p2)
7. **Tumor incidence:** Gross + histological at necropsy
8. **Cause of death:** Blinded pathologist classification into 8 categories (cancer, cardiac, renal, respiratory, infection, neurological, multi-organ, undetermined)

---

## 7. Statistical Analysis Plan

### 7.1 Primary analysis: Max lifespan (H1 vs H2)

**Model:** Cox proportional hazards

```
h(t) ~ Arm + Sex + ClampResponse_composite + BodyWeight_Phase2
```

- **H1 test:** Dunnett's: each of Arms B, C, D vs Arm A, one-sided (longer survival)
- **H2 test:** Equivalence: 90% CI for hazard ratio of each add-on arm vs Arm A. If upper bound of HR ≤1.05 (≤5% improvement), Bottleneck saturation supported
- **Decision rule:** If any add-on arm shows ≥10% max lifespan gain (p < 0.017), SENS supported. If all ≤3%, Bottleneck supported. Zone 3–10% is indeterminate.

### 7.2 Synergy test (H3)

**Interaction model:**

```
h(t) ~ TERT * CrosslinkBreaker + Sex + ClampResponse + BodyWeight
```

- SENS predicts: TERT × CrosslinkBreaker interaction HR < 1.0 (super-additive benefit)
- Test at α = 0.05, two-sided

### 7.3 Gompertz analysis (H4, H5)

**Parametric fit:** Gompertz-Makeham model to each arm's survival curve

```
μ(t) = c + α·exp(β·t)
```

- **H4:** Compare β(Arm A) vs β(historical vehicle). Bottleneck predicts ≥20% reduction in β
- **H5:** Compare β(Arms B/C/D) vs β(Arm A). SENS predicts further ≥10% reduction
- Bootstrap 95% CIs for β differences

### 7.4 Pathway Residual (H6)

**Variance decomposition:**

```
log(hazard) ~ ClampBiomarkers + Age + Sex
```

- Calculate R² of clamp biomarker panel in explaining mortality hazard variation in Arm A
- Bottleneck-p2 predicts: R² ≥0.80 (residual <20%)
- Report with 95% CI via bootstrap

### 7.5 Multiple comparison correction

| Family | Tests | Correction |
|--------|:-----:|-----------|
| Primary max lifespan (3 add-on vs clamp) | 3 | Dunnett, α = 0.05 |
| Synergy | 1 | α = 0.05 |
| Gompertz parameters | 2 | Bonferroni, α = 0.025 each |
| Pathway Residual | 1 | α = 0.05 |
| Target engagement | Descriptive | No correction |

---

## 8. Stopping Rules

### Interim analysis

- **Single interim look** at 50% expected deaths (approximately T = 12 months post-Phase 2)
- **O'Brien-Fleming:** Interim α = 0.005; final α = 0.048
- **Futility:** If conditional power for H1 < 10% at interim for all three add-on arms, declare Bottleneck saturation early

### Safety stopping

- If tumor incidence in TERT arms (B, D) exceeds 30% at any interim pathology review, halt TERT dosing
- Humane endpoints per IACUC: BW loss >20%, BCS ≤2, tumor >2 cm³

---

## 9. Decision Matrix

| Outcome | H1 | H2 | H3 | Verdict |
|---------|:--:|:--:|:--:|---------|
| ≥1 add-on arm gains ≥10% max LS over clamp | ✓ | ✗ | — | **Favors SENS**: multi-class repair extends beyond bottleneck |
| Stack (D) gains ≥10%, monos (B,C) gain <5% | ✓ | — | ✓ | **Strongly favors SENS**: synergy confirms multi-class necessity |
| All add-on arms gain ≤3% | ✗ | ✓ | ✗ | **Favors Bottleneck**: saturation after clamp confirmed |
| Add-on gains 3–10% | — | — | — | **Indeterminate**: clamp may have been incomplete |
| Gompertz β unchanged by clamp | — | — | — | **Challenges Bottleneck slope-driver** claim |

### Backlog items resolved

- **S1-SENS-BOTTLENECK-01** (missing severe test): This IS the multi-class necessity test
- **S2-BOTTLENECK-SENS-01** (missing severe test): This tests the saturation prediction
- **S1-SENS-BOTTLENECK-02** (missing severe test): Interaction terms from this design substitute for RMR1

---

## 10. Materials

| Item | Source | Details |
|------|--------|---------|
| C57BL/6J mice (20+ mo) | Jackson Labs / NIA | #000664 |
| Rapamycin diet (14 ppm) | TestDiet (ITP formulation) | Encapsulated |
| Dasatinib | LC Labs D-3307 | 5 mg/kg biweekly |
| Quercetin | Sigma Q4951 | 50 mg/kg biweekly |
| AAV9-mTERT | Vector Biolabs (custom) | ≥10¹³ vg/mL |
| Alagebrium (ALT-711) | Custom synthesis | 10 mg/kg/day in diet |
