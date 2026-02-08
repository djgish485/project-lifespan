---
title: "Pre-Registration: Pathogen-Challenge Factorial (2x2x2)"
---

# Pre-Registration: Pathogen-Challenge Factorial (2x2x2)

**Protocol version:** 1.0
**Date:** 2026-02-08
**Status:** Draft — awaiting expert review and registry submission
**Parent:** [Research Agenda #1](research_agenda.md#1-pathogen-challenge-factorial-2x2x2)

---

## 1. Hypotheses

All hypotheses are directional with pre-specified effect-size thresholds.

### Primary Hypotheses

| ID | Theory favored | Hypothesis | Threshold |
|----|---------------|------------|-----------|
| H1 | PC (Lidsky) | Longevity intervention in dirty environment increases pathogen burden relative to dirty+vehicle | ≥2-fold increase in qPCR titers for ≥1 of 3 target pathogens |
| H2 | PC (Lidsky) | Anti-pathogen package rescues infection penalty | Burden reduced to within 1.5x of vehicle arm |
| H3 | Classics | Any intervention achieving ≥15% max lifespan gain produces ≥1 measurable fitness cost | Tumor incidence ≥10% above controls, OR reproduction ≥20% decline, OR stress resistance ≥30% decline |
| H4 | Intrinsic theories (null for PC) | Longevity intervention works equally in SPF and dirty environments | Intervention × environment interaction term p > 0.05 for max lifespan |

### Secondary Hypotheses

| ID | Hypothesis | Threshold |
|----|------------|-----------|
| H5 | Population-structure variables (dispersal proxy via rewilding) predict lifespan variation beyond standard covariates | ≥5% incremental R² over body mass + extrinsic mortality |
| H6 | Senescence markers (p16, SASP) are reduced by intervention regardless of environment | Intervention main effect p < 0.01 for ≥2 markers |

---

## 2. Study Design

**Type:** 2×2×2 full factorial, randomized, blinded
**Organism:** C57BL/6J mice (Jackson Labs stock #000664), male and female balanced

### Factors

| Factor | Level 0 (control) | Level 1 (treatment) |
|--------|-------------------|---------------------|
| A: Longevity intervention | Vehicle (standard AIN-93G diet) | Rapamycin 14 ppm encapsulated in diet (ITP protocol) |
| B: Environment | SPF (standard barrier facility) | Dirty/rewilded (co-housing with pet-store mice per Beura et al. 2016 protocol) |
| C: Anti-pathogen package | None | MHV/MNV vaccination + cidofovir antiviral + metronidazole for Helicobacter + enhanced barrier bedding changes |

### Arms (8 total)

| Arm | Intervention (A) | Environment (B) | Anti-pathogen (C) | Abbreviation |
|-----|:-:|:-:|:-:|:--|
| 1 | Vehicle | SPF | None | V-SPF-NoAP |
| 2 | Rapamycin | SPF | None | R-SPF-NoAP |
| 3 | Vehicle | Dirty | None | V-D-NoAP |
| 4 | Rapamycin | Dirty | None | R-D-NoAP |
| 5 | Vehicle | SPF | Anti-pathogen | V-SPF-AP |
| 6 | Rapamycin | SPF | Anti-pathogen | R-SPF-AP |
| 7 | Vehicle | Dirty | Anti-pathogen | V-D-AP |
| 8 | Rapamycin | Dirty | Anti-pathogen | R-D-AP |

### Timeline

- **T = 0:** Mice aged 18 months, randomized and assigned to arms
- **T = 0–2 weeks:** Dirty-environment arms co-housed with pet-store mice for seroconversion; anti-pathogen arms receive vaccination series
- **T = 2 weeks onward:** Rapamycin diet initiated; longitudinal sampling begins
- **T = 6 months:** Primary pathogen burden endpoint (interim sacrifice cohort: n=8/arm)
- **T = death:** Lifetime follow-up for max lifespan; full necropsy on natural deaths

---

## 3. Sample Size and Power Analysis

### Primary endpoint: Pathogen burden (H1)

- **Effect size:** 2-fold increase (log₂ fold-change = 1.0) in qPCR titers
- **Within-group SD:** Estimated 0.8 log₂ units (from Beura et al. 2016 MNV data)
- **Test:** Two-sample t-test (dirty+rapa vs dirty+vehicle), one-sided α = 0.025 (Bonferroni for 2 primary comparisons)
- **Power:** 0.90
- **Required n per group:** 17 per comparison group
- **With 20% attrition:** 22 per arm for dirty arms

### Primary endpoint: Max lifespan (H4)

- **Effect size:** Interaction term detecting 10% max-lifespan difference (≈120 days from baseline ~1200 days)
- **Within-group SD:** Estimated 100 days (from ITP historical data)
- **Test:** Factorial ANOVA interaction term, α = 0.05
- **Power:** 0.80
- **Required n per arm:** 20 (for 8-arm factorial, total N = 160)
- **With 20% attrition for lifetime cohort:** 25 per arm

### Total animals

| Cohort | Purpose | N per arm | Arms | Total |
|--------|---------|:-:|:-:|:-:|
| Lifetime | Max lifespan, natural-death necropsy | 25 | 8 | 200 |
| Interim sacrifice (6 mo) | Pathogen burden, tissue biomarkers | 8 | 8 | 64 |
| Sentinel controls | Transmission monitoring | 4 | 4 dirty arms | 16 |
| **Total** | | | | **280** |

**Sex balance:** 50/50 male/female within each arm. Sex included as covariate in all models.

---

## 4. Randomization

- **Method:** Stratified block randomization
- **Stratification factors:** Sex, body weight quartile at 18 months
- **Block size:** 8 (one per arm), randomly permuted
- **Software:** R `blockrand` package, seed recorded and sealed before study start
- **Allocation concealment:** Cage cards coded with randomization ID only; treatment assignments in sealed envelopes opened by facility staff, not investigators

---

## 5. Blinding

| Role | Blinded to |
|------|-----------|
| Animal care staff | Intervention (A) — rapamycin vs vehicle diet indistinguishable by appearance |
| Pathologist (necropsy) | All factors — coded specimens only |
| qPCR technician | All factors — coded samples |
| Statistician (primary analysis) | Treatment assignments until pre-specified analysis code has been run |
| Environmental assignment (B) | NOT blinded — SPF vs dirty housing is visible. Mitigated by blinding all downstream measurements |
| Anti-pathogen assignment (C) | NOT blinded to care staff (vaccination requires handling). Mitigated by blinding all downstream measurements |

---

## 6. Target Pathogens and Measurement

### Pathogen panel (3 classes, pre-specified)

| Pathogen | Class | Measurement | Tissue | Detection threshold |
|----------|-------|-------------|--------|-------------------|
| Mouse hepatitis virus (MHV) | RNA virus | RT-qPCR (copies/μg RNA) | Liver, lung | 10² copies/μg |
| Murine norovirus (MNV) | RNA virus | RT-qPCR (copies/μg RNA) | Intestine, mesenteric LN | 10² copies/μg |
| *Helicobacter hepaticus* | Bacterium | 16S qPCR (copies/μg DNA) | Cecum, liver | 10³ copies/μg |

### Transmission proxies

- **Fecal shedding:** Weekly fecal pellet qPCR for MNV and Helicobacter
- **Sentinel seroconversion:** Naive sentinel mice (4 per dirty arm) co-housed from T=8 weeks; serology at T=12, 16, 20, 24 weeks for MHV/MNV
- **Contact rate normalization:** Video recording of cage behavior (2 hr/week) to quantify contact rates as denominator for transmission coefficient estimation

---

## 7. Endpoints

### Primary endpoints

1. **Pathogen burden** (6-month interim sacrifice): Log₂ qPCR titers per pathogen per tissue
2. **Maximum lifespan** (lifetime cohort): Age at death of last 10% of each arm (90th percentile survival)
3. **Hazard rate** (lifetime cohort): Gompertz parameters from Kaplan-Meier + parametric fits

### Secondary endpoints

4. **Tumor incidence:** Gross + histological at necropsy, classified by organ and grade
5. **Reproduction** (subset, n=10 females/arm bred at T=3 months): Litter size, pup survival to weaning
6. **Stress resistance:** Cold challenge (4°C for 6 hours, core temp recovery at 24 hours) at T=4 months
7. **Senescence biomarkers:** p16^INK4a (qPCR, skin + kidney), SA-β-gal (histology, liver), SASP panel (IL-6, TNF-α, MCP-1 in plasma) at 6-month sacrifice
8. **Fecal shedding kinetics:** Weekly time course for transmission modeling
9. **Body weight trajectory:** Weekly weights

---

## 8. Statistical Analysis Plan

### 8.1 Primary analysis: Pathogen burden (H1, H2)

**Model:** Three-way factorial ANOVA on log₂-transformed qPCR titers:

```
log₂(titer) ~ Intervention * Environment * AntiPathogen + Sex + (1|Cage)
```

- **H1 test:** A×B interaction contrast: (R-D-NoAP) vs (V-D-NoAP), one-sided t-test at α = 0.025
- **H2 test:** A×B×C three-way interaction: Does anti-pathogen rescue the A×B penalty? Contrast: (R-D-AP) vs (R-D-NoAP), one-sided at α = 0.025
- **Multiple pathogen adjustment:** Require ≥1 of 3 pathogens significant at α = 0.025 (most conservative: each pathogen tested at α = 0.025/3 = 0.0083 with Bonferroni, OR use Hochberg step-up)
- **Cage as random effect:** Mice within dirty cages share pathogen exposure; cage is random intercept

### 8.2 Primary analysis: Max lifespan (H3, H4)

**Model:** Cox proportional hazards with factorial terms:

```
h(t) ~ Intervention * Environment * AntiPathogen + Sex + BodyWeight_baseline
```

- **H4 test:** Intervention × Environment interaction HR, two-sided at α = 0.05
- **H3 test:** Conditional — only evaluated if any arm achieves ≥15% max lifespan gain over its environment-matched vehicle control. If triggered: compare tumor incidence (Fisher's exact), reproduction (Wilcoxon), stress resistance (t-test) between that arm and its control
- **Max lifespan definition:** Wang-Allison method — 90th percentile of survival distribution, bootstrapped 95% CI

### 8.3 Secondary analyses

- **Transmission modeling:** SIR-type model fit to sentinel seroconversion data; estimate basic reproduction number R₀ per arm. Compare R₀ between intervention and vehicle within dirty environment
- **Senescence mediation:** Test whether pathogen burden mediates the relationship between intervention and lifespan using causal mediation analysis (R `mediation` package)
- **Population structure proxy:** Dirty vs SPF as a binary "high contact/low contact" proxy; partial correlation with lifespan after controlling for intervention

### 8.4 Multiple comparison correction

| Family | Tests | Correction |
|--------|:-----:|-----------|
| Primary pathogen burden (H1, H2) | 2 per pathogen × 3 pathogens = 6 | Hochberg step-up within family, α = 0.05 |
| Primary lifespan (H3, H4) | 2 | Bonferroni, α = 0.025 each |
| Secondary endpoints | Exploratory | Report unadjusted p-values with FDR q-values |

---

## 9. Stopping Rules

### Interim analysis

- **Single interim look** at 50% of expected deaths in lifetime cohort (approximately T = 18 months post-start, when mice are ~36 months old)
- **O'Brien-Fleming spending function** for alpha: interim α = 0.005, final α = 0.048
- **Futility:** If conditional power for H1 < 10% at interim, consider stopping pathogen measurement (not survival follow-up)

### Humane endpoints

- Body weight loss >20% from peak sustained >7 days
- Body condition score ≤2 (IACUC protocol)
- Tumor burden >2 cm³ or ulcerated
- Severe respiratory distress, paralysis, or non-responsive

---

## 10. Decision Matrix

This table maps experimental outcomes to theory verdicts:

| Outcome pattern | H1 | H4 | H2 | Verdict |
|----------------|:--:|:--:|:--:|---------|
| Rapa + dirty → high burden; SPF → low burden | ✓ | ✗ | — | **Favors PC**: infection tradeoff confirmed |
| ... and anti-pathogen rescues | ✓ | ✗ | ✓ | **Strongly favors PC**: full prediction chain confirmed |
| Rapa works equally in SPF and dirty | ✗ | ✓ | — | **Favors Classics / intrinsic theories**: no infection tradeoff |
| Rapa + dirty → high burden BUT no lifespan penalty | ✓ | ✓ | — | **Mixed**: infection tradeoff exists but doesn't constrain lifespan |
| No infection changes in any arm | ✗ | ✓ | ✗ | **Challenges PC**: core prediction falsified |

### Backlog items resolved by this experiment

- **S1-PC-CLASSICS-01** (missing severe test): This IS the severe test
- **S1-PC-CLASSICS-02** (bridge assumption): H1 tests the inclusive-fitness bridge
- **S1-PC-SENS-01** (bridge assumption): Infection tradeoff under damage-repair intervention
- **S1-PC-FEDICHEV-01** (missing severe test): PC's proposed falsifiers are being tested
- **S1-CLASSICS-PC-02** (measurement gap): Dirty/rewilded co-housing provides population-structure variation

---

## 11. Materials and Reagents

| Item | Source | Catalog/Lot |
|------|--------|-------------|
| C57BL/6J mice | Jackson Labs | #000664 |
| Pet-store mice (dirty donors) | Local pet stores (3+ sources, pooled) | — |
| Rapamycin diet (14 ppm) | TestDiet (encapsulated, ITP formulation) | Pre-specified lot |
| D+Q senolytic (optional secondary arm) | Dasatinib: LC Labs; Quercetin: Sigma | TBD |
| MHV RT-qPCR primers | IDT (per Lavi et al.) | Sequences in Supplement |
| MNV RT-qPCR primers | IDT (per Baert et al.) | Sequences in Supplement |
| *H. hepaticus* 16S primers | IDT (per Fox et al.) | Sequences in Supplement |
| Cidofovir | Gilead (via pharmacy) | TBD |
| Metronidazole | Sigma | TBD |

---

## 12. Data Management

- **Raw data:** Deposited in institutional repository within 6 months of study completion
- **Analysis code:** Pre-registered R scripts in `scripts/analysis/pathogen_factorial/`; version-controlled in this repo
- **Blinding key:** Sealed with institutional compliance office; opened only after pre-specified primary analyses are run
- **Pre-registration timestamp:** SHA-256 hash of this document committed to repo before first animal randomized

---

## 13. Deviations Protocol

Any deviation from this pre-registration must be:

1. Documented with date and rationale
2. Classified as "minor" (no impact on primary analysis) or "major" (affects primary analysis interpretation)
3. Reported in final manuscript with transparent before/after comparison
4. Major deviations require sensitivity analysis showing robustness of conclusions

---

## 14. Expected Timeline

| Milestone | Timepoint |
|-----------|-----------|
| Protocol finalization and IACUC approval | T − 3 months |
| Animal ordering and aging to 18 months | T − 6 months (if starting from 12 mo) |
| Randomization and treatment start | T = 0 |
| Dirty co-housing and seroconversion | T = 0–2 weeks |
| 6-month interim sacrifice | T = 6 months |
| Interim survival analysis | T = 18 months post-start (~36 mo age) |
| Study completion (last death) | T ≈ 24–30 months post-start |
| Data lock and unblinding | Within 1 month of last death |
| Pre-print submission | Within 3 months of unblinding |
