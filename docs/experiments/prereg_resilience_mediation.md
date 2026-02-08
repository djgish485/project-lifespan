---
title: "Pre-Registration: Resilience vs Pathway Mediation Study"
---

# Pre-Registration: Resilience vs Pathway Mediation Study

**Protocol version:** 1.0
**Date:** 2026-02-08
**Status:** Draft — awaiting expert review and registry submission
**Parent:** [Research Agenda #4](research_agenda.md#4-resilience-vs-pathway-mediation-study)

---

## 1. Hypotheses

### Primary Hypotheses

| ID | Theory favored | Hypothesis | Threshold |
|----|---------------|------------|-----------|
| H1 | Fedichev | Survival gains are primarily mediated through DOSI/autocorrelation improvement, not bottleneck biomarker changes | Indirect effect through DOSI ≥50% of total survival effect; indirect through bottleneck markers <25% |
| H2 | Bottleneck | Survival gains are primarily mediated through bottleneck biomarker reduction, not resilience metrics | Indirect effect through bottleneck markers ≥50% of total survival effect; indirect through DOSI <25% |
| H3 | Complementary | Both mediation pathways contribute independently | Both indirect effects ≥25% of total; joint mediation explains ≥70% |

### Secondary Hypotheses

| ID | Hypothesis | Threshold |
|----|------------|-----------|
| H4 | DOSI autocorrelation predicts mortality independently of bottleneck biomarkers (fedichev-p1) | HR ≥1.5 per SD increase in DOSI, maintained after adjusting for bottleneck panel |
| H5 | An intervention that improves DOSI without changing bottleneck markers still reduces hazard (fedichev-p2) | Resilience arm (Arm 3) shows ≥15% hazard reduction with no significant bottleneck marker change |
| H6 | Gompertz doubling rate (β) is modified by resilience intervention but not by senolytic alone | β reduction ≥15% in Arm 3/4; β unchanged (<5% change) in Arm 2 |
| H7 | Cross-species CSD universality: mouse autocorrelation dynamics parallel human DOSI patterns | Mouse DOSI trajectory shape (acceleration phase, plateau) matches Pyrkov2021 human pattern |

---

## 2. Study Design

**Type:** 4-arm randomized controlled trial with longitudinal biomarker collection and pre-specified mediation analysis
**Organism:** C57BL/6J mice, 18+ months old, male and female balanced

### Arms

| Arm | Treatment | Rationale |
|-----|-----------|-----------|
| 1 | Vehicle (standard diet + sham handling) | Negative control |
| 2 | D+Q senolytic (dasatinib 5 mg/kg + quercetin 50 mg/kg, biweekly) | Bottleneck-targeting intervention |
| 3 | Resilience protocol: treadmill exercise (30 min, 5x/week) + cold exposure (10°C 1hr, 3x/week) + caloric cycling (alternate-day 30% restriction) | Resilience-targeting intervention |
| 4 | Combination (D+Q + resilience protocol) | Joint intervention |

### Timeline

- **T = 0:** Enrollment at 18+ months; baseline phenotyping battery (2 weeks)
- **T = 2 weeks:** Randomization and treatment initiation
- **T = 2 weeks onward:** Biweekly blood draws + monthly perturbation-recovery battery
- **T = 6 months:** Comprehensive mid-study phenotyping
- **T = death:** Lifetime follow-up; full necropsy

---

## 3. Sample Size and Power Analysis

### Primary endpoint: Mediation proportion (H1, H2)

- **Effect size:** Detect ≥50% mediation proportion with 95% CI width ≤30%
- **Simulation-based power** (R `mediation` package, 1000 simulations): N = 30 per arm gives 80% power to detect mediation proportion ≥0.50 when total effect HR = 0.70
- **With 25% attrition (lifetime study):** 40 per arm

### Secondary endpoint: DOSI independence (H4)

- **Effect size:** HR ≥1.5 per SD in DOSI autocorrelation
- **Test:** Cox model with time-varying covariates
- **Power:** 0.85 at α = 0.05 with N = 160 total and ~50% events at interim
- **Already covered** by 40 per arm × 4 arms = 160

### Total animals

| Cohort | N per arm | Arms | Total |
|--------|:-:|:-:|:-:|
| Lifetime | 40 | 4 | 160 |

**Sex balance:** 50/50 male/female within each arm.

---

## 4. Randomization

- **Method:** Stratified block randomization
- **Stratification:** Sex, baseline DOSI tertile, baseline p16 tertile
- **Block size:** 4, randomly permuted
- **Allocation concealment:** Coded cage cards; exercise/cold protocols performed by dedicated staff

---

## 5. Blinding

| Role | Blinded to |
|------|-----------|
| Blood draw technician | Treatment — coded tubes |
| Biomarker lab analyst | All arms — coded samples |
| Perturbation-recovery assessor | All arms — coded mice |
| Necropsy pathologist | All arms — coded specimens |
| Statistician | Until pre-specified analysis code has run |
| Exercise/cold/diet staff | NOT blinded (different protocols). Mitigated: all downstream measurements blinded |
| D+Q gavage staff | NOT blinded (oral gavage vs sham). Mitigated: sham gavage with vehicle in Arms 1/3 |

---

## 6. Longitudinal Biomarker Protocol

### Resilience metrics (Fedichev readouts)

Collected **biweekly** from blood draws:

| Metric | Method | Sample |
|--------|--------|--------|
| DOSI (dynamic organism state indicator) | First principal component of CBC + metabolic panel (17 parameters) | 100 μL tail vein blood |
| Autocorrelation time (τ) | Lag-1 autocorrelation of DOSI over rolling 8-week window | Derived from DOSI time-series |
| DOSI variance | Rolling 8-week variance of DOSI | Derived from DOSI time-series |

### Perturbation-recovery battery (active resilience)

Collected **monthly**:

| Test | Protocol | Recovery metric |
|------|----------|-----------------|
| Glucose tolerance | 2 g/kg IP glucose; blood glucose at 0, 15, 30, 60, 120 min | AUC and time to return to ≤120% of baseline |
| Cold recovery | 4°C exposure for 2 hours; core temp at 0, 30, 60, 120 min post-return to 22°C | Time to return to ≤0.5°C of baseline core temp |
| Hypoxia recovery | 10% O₂ for 30 min; SpO₂ at 0, 5, 15, 30, 60 min post-return to normoxia | Time to return to ≥95% SpO₂ |

### Bottleneck biomarkers

Collected **monthly** from blood draws:

| Marker | Method | Tissue |
|--------|--------|--------|
| p16^INK4a | RT-qPCR (PBMCs) | Blood |
| IL-6 | ELISA | Plasma |
| TNF-α | ELISA | Plasma |
| MCP-1 | ELISA | Plasma |
| GDF-15 | ELISA | Plasma |
| p-S6K (mTOR readout) | Western blot (PBMCs) | Blood |

---

## 7. Endpoints

### Primary endpoint

1. **All-cause mortality** (time to event, lifetime follow-up)

### Secondary endpoints

2. **Maximum lifespan:** Wang-Allison 90th percentile, per arm
3. **Gompertz parameters:** α (baseline mortality) and β (doubling rate) per arm
4. **DOSI trajectory:** Mean DOSI and autocorrelation time trajectory per arm over study duration
5. **Perturbation-recovery composite:** Mean of standardized glucose/cold/hypoxia recovery times
6. **Bottleneck biomarker composite:** Mean of standardized p16, IL-6, TNF-α, MCP-1, GDF-15
7. **Cause of death:** Blinded classification

---

## 8. Statistical Analysis Plan

### 8.1 Primary analysis: Mediation (H1, H2, H3)

**Step 1: Total effect**

```
h(t) ~ Arm + Sex + BodyWeight_baseline + BaselineDOSI + BaselineP16
```

- Establish that Arm 2, 3, or 4 reduces mortality vs Arm 1

**Step 2: Mediator models**

```
DOSI_trajectory ~ Arm + Sex + BodyWeight + time + (1|Mouse)
Bottleneck_composite ~ Arm + Sex + BodyWeight + time + (1|Mouse)
```

**Step 3: Outcome model with mediators**

```
h(t) ~ Arm + DOSI_lagged + Bottleneck_lagged + Sex + BodyWeight
```

**Step 4: Causal mediation** (R `mediation` package)

- Proportion mediated via DOSI pathway
- Proportion mediated via bottleneck pathway
- Joint mediation
- 95% CIs via quasi-Bayesian bootstrap (2000 iterations)

**Decision rules:**

| DOSI mediation | Bottleneck mediation | Verdict |
|:-:|:-:|---------|
| ≥50% | <25% | **Favors Fedichev** |
| <25% | ≥50% | **Favors Bottleneck** |
| ≥25% | ≥25% | **Complementary** |
| <25% | <25% | **Neither pathway explains survival** (model mis-specification or missing mediator) |

### 8.2 DOSI independence (H4)

**Time-varying Cox model:**

```
h(t) ~ DOSI_tv + Bottleneck_composite_tv + Sex + BodyWeight + Age_enrollment
```

- Report DOSI HR per SD after adjustment for bottleneck panel
- Report incremental C-statistic: model with DOSI vs model without

### 8.3 Resilience-only effect (H5)

**Contrast:** Arm 3 vs Arm 1

- Primary: hazard ratio
- Secondary: verify no significant change in bottleneck markers (Arm 3 bottleneck composite within ±15% of Arm 1 at T=6 months, p > 0.10)
- If both conditions met (HR ≤0.85 AND no bottleneck change): fedichev-p2 supported

### 8.4 Gompertz analysis (H6)

**Parametric Gompertz-Makeham fit per arm:**

- Compare β between arms using likelihood ratio test
- H6 predicts: β(Arm 3) < β(Arm 1) by ≥15%; β(Arm 2) ≈ β(Arm 1) within 5%

### 8.5 Multiple comparison correction

| Family | Tests | Correction |
|--------|:-----:|-----------|
| Total effect (3 arms vs vehicle) | 3 | Dunnett |
| Mediation proportions | Exploratory | Report bootstrap CIs |
| DOSI independence | 1 | α = 0.05 |
| Arm 3 vs Arm 1 | 1 | α = 0.05 |
| Gompertz parameters | 2 | Bonferroni, α = 0.025 |

---

## 9. Stopping Rules

### Interim analysis

- **Single look** at 50% events (~T = 15 months post-enrollment)
- **O'Brien-Fleming:** Interim α = 0.005; final α = 0.048
- **Futility for H1:** If conditional power for detecting mediation <10%, declare mediation analysis underpowered but continue for survival endpoints

### Safety

- Humane endpoints: BW loss >20%, BCS ≤2
- Exercise protocol reduced if >10% of Arm 3/4 mice show exercise-related injuries

---

## 10. Decision Matrix

| Outcome pattern | H1 | H4 | H5 | Verdict |
|----------------|:--:|:--:|:--:|---------|
| Survival mediated through DOSI; DOSI independent of bottleneck markers | ✓ | ✓ | — | **Strongly favors Fedichev** |
| Survival mediated through bottleneck markers; DOSI adds <5% C-statistic | ✗ | ✗ | ✗ | **Strongly favors Bottleneck** |
| Resilience arm reduces hazard ≥15% without changing bottleneck markers | — | — | ✓ | **Favors Fedichev (p2 confirmed)** |
| Both pathways mediate independently | — | ✓ | — | **Complementary mechanisms** |
| No survival benefit in any arm | — | — | — | **Inconclusive** (underpowered or wrong interventions) |

### Backlog items resolved

- **S1-FEDICHEV-BOTTLENECK-01** (bridge assumption): Mediation analysis directly tests causal independence of DOSI
- **S3-BOTTLENECK-FEDICHEV-02** (missing severe test): Gompertz slope analysis included

---

## 11. Materials

| Item | Source | Details |
|------|--------|---------|
| C57BL/6J mice (18+ mo) | Jackson Labs / NIA | #000664 |
| Dasatinib | LC Labs D-3307 | 5 mg/kg biweekly |
| Quercetin | Sigma Q4951 | 50 mg/kg biweekly |
| Treadmill | Columbus Instruments Exer-6M | 12 m/min, 0° incline |
| Cold chamber | Custom (10°C controlled) | 1 hr sessions |
| CBC analyzer | Hemavet 950FS | 17-parameter panel |
| Metabolic panel | Beckman AU480 | Standard mouse panel |
