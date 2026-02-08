---
title: "Pre-Registration: OSK vs Bioelectric vs Combo Aged Regeneration"
---

# Pre-Registration: OSK vs Bioelectric vs Combo Aged Regeneration

**Protocol version:** 1.0
**Date:** 2026-02-08
**Status:** Draft — awaiting expert review and registry submission
**Parent:** [Research Agenda #2](research_agenda.md#2-osk-vs-bioelectric-vs-combo-aged-regeneration)

---

## 1. Hypotheses

### Primary Hypotheses

| ID | Theory favored | Hypothesis | Threshold |
|----|---------------|------------|-----------|
| H1 | Sinclair | OSK alone restores function and resets epigenetic clocks; bioelectric metrics change only as a downstream consequence | Regrowth ≥60% of young baseline; DNAm clock reversal ≥30%; Vmem changes lag behind or are absent |
| H2 | Levin | Pattern-aware bioelectric modulation alone restores function with superior durability across re-injury, even without epigenetic reprogramming | Regrowth ≥60% of young baseline; re-injury recovery ≥50% of first recovery; DNAm reversal <15% |
| H3 | Levin primacy | OSK functional rescue requires intact bioelectric network communication (gap-junction disruption blocks OSK rescue) | OSK + gap-junction disruption yields <50% of OSK-alone rescue |
| H4 | Sinclair primacy | OSK works fully even with gap-junction disruption | OSK + disruption yields ≥80% of OSK-alone rescue |

### Secondary Hypotheses

| ID | Hypothesis | Threshold |
|----|------------|-----------|
| H5 | Combo (OSK + bioelectric) outperforms both monotherapies | Combo regrowth ≥20% above best monotherapy; interaction term p < 0.05 |
| H6 | Mediation analysis: functional rescue flows primarily through epigenetic state | Indirect effect through DNAm ≥50% of total effect on regrowth |
| H7 | Mediation analysis: functional rescue flows primarily through controller-state restoration | Indirect effect through Vmem/entropy metrics ≥50% of total effect on regrowth |

---

## 2. Study Design

**Type:** 5-arm + 1 disruption arm, randomized, blinded endpoint assessment
**Organism:** C57BL/6J mice, 20+ months old, male and female balanced
**Injury model:** Full-thickness 6mm ear punch (standardized, quantifiable regrowth)

### Arms

| Arm | Treatment | Purpose |
|-----|-----------|---------|
| 1 | Sham (injury + vehicle injection) | Negative control |
| 2 | Uniform electrical stimulation (non-patterned DC, same total charge as Arm 3) | Active control for electrical artifact |
| 3 | Pattern-aware bioelectric modulation (Vmem writing at lesion + 3-cell-diameter neighbor ring via ionophore cocktail) | Levin monotherapy |
| 4 | Local cyclic OSK (dox-inducible AAV9-OSK, 2 days on / 5 days off for 4 weeks) | Sinclair monotherapy |
| 5 | OSK + pattern-aware bioelectric combo | Combination |
| 6 | OSK + carbenoxolone (gap-junction blocker, 100 μM topical) | Sinclair vs Levin primacy test |

### Timeline

- **T = 0:** Ear punch in 20+ month mice; treatment initiation
- **T = 0–4 weeks:** Treatment period (OSK cycling, bioelectric modulation sessions 3x/week)
- **T = 4 weeks:** Carbenoxolone washout in Arm 6
- **T = 8 weeks:** Primary endpoint assessment (regrowth, morphology, tissue harvest for epigenetic/bioelectric readouts)
- **T = 8 weeks + 1 day:** Re-injury (second 6mm punch at same site) in subset (n=10/arm)
- **T = 16 weeks:** Durability endpoint (second regrowth assessment)

---

## 3. Sample Size and Power Analysis

### Primary endpoint: Regrowth area (H1, H2)

- **Effect size:** 30% difference in regrowth area between active arms and sham (young mice regrow ~80% of punch area; aged sham ~20%; target for treatment: ≥50%)
- **Within-group SD:** Estimated 15% of punch area (from pilot ear punch data in aged mice)
- **Test:** Dunnett's test (each active arm vs sham), one-sided α = 0.05/5 = 0.01 per comparison
- **Power:** 0.85
- **Required n per arm:** 15
- **With 15% attrition:** 18 per arm

### Gap-junction disruption test (H3, H4)

- **Effect size:** 50% reduction (OSK+carbenoxolone yields <50% of OSK-alone regrowth)
- **Test:** One-sided t-test comparing Arm 6 vs Arm 4
- **Power:** 0.90 at α = 0.025
- **Required n per arm:** 15 (already planned)

### Total animals

| Cohort | N per arm | Arms | Total |
|--------|:-:|:-:|:-:|
| Primary (8-week endpoint) | 18 | 6 | 108 |
| Re-injury subset | 10 | 6 | 60 (from primary cohort) |
| **Total unique animals** | | | **108** |

---

## 4. Randomization

- **Method:** Stratified block randomization
- **Stratification:** Sex, baseline body weight tertile
- **Block size:** 6 (one per arm), randomly permuted
- **Allocation concealment:** Coded cage cards; treatment prepared by unblinded technician, administered by blinded surgeon

---

## 5. Blinding

| Role | Blinded to |
|------|-----------|
| Surgeon (ear punch) | Treatment assignment — all mice receive identical wound |
| Histopathologist | All arms — coded specimens |
| Imaging technician (Vmem, regrowth photos) | Treatment — coded ear tags |
| DNAm clock analyst | Treatment — coded samples |
| Statistician (primary analysis) | Treatment — until pre-specified code has run |
| Treatment administrator | NOT blinded (different modalities require different equipment). Mitigated by blinding all downstream measurements |

---

## 6. Dual Readout Protocol (Critical)

### Epigenetic readouts (Sinclair metrics)

| Metric | Method | Tissue | Timepoint |
|--------|--------|--------|-----------|
| DNAm clock age | Thompson mouse multi-tissue clock (bisulfite sequencing, 319 CpGs) | Ear tissue biopsy (regenerated + adjacent) | T=8 weeks |
| Histone modification panel | H3K27me3, H3K4me3, H3K9me3 ChIP-seq | Ear tissue | T=8 weeks |
| p16^INK4a expression | RT-qPCR | Ear tissue | T=8 weeks |

### Controller-state readouts (Levin metrics)

| Metric | Method | Tissue | Timepoint |
|--------|--------|--------|-----------|
| Vmem spatial map | DiBAC4(3) voltage-sensitive dye + confocal imaging | Ear tissue in vivo | T=0, 2, 4, 8 weeks |
| Gap-junction connectivity | Fluorescence recovery after photobleaching (FRAP) with calcein-AM | Ear tissue | T=4, 8 weeks |
| Active information storage | Calculated from Vmem time-series (Lizier AIS algorithm) | Derived from Vmem maps | T=4, 8 weeks |
| Transfer entropy | Calculated from cell-to-cell Vmem signals | Derived from Vmem maps | T=4, 8 weeks |
| Spatial entropy | Shannon entropy of Vmem pattern across wound margin | Derived from Vmem maps | T=4, 8 weeks |

---

## 7. Endpoints

### Primary endpoints (T = 8 weeks)

1. **Regrowth area:** Percentage of original punch area regenerated (digital planimetry from standardized photographs, 3 blinded raters, ICC ≥0.85 required)
2. **Morphological correctness score:** 0–3 scale (0 = scar only, 1 = tissue mass without structure, 2 = partial cartilage + skin architecture, 3 = full ear-like structure). 3 blinded raters.
3. **Tumor/aberrant growth incidence:** Any mass >2mm not consistent with normal ear architecture, confirmed histologically

### Secondary endpoints

4. **Durability across re-injury** (T = 16 weeks): Second regrowth area as fraction of first regrowth
5. **DNAm clock reversal magnitude:** Difference in predicted age (weeks) between treated and sham tissue
6. **Vmem pattern restoration:** Spatial correlation of regenerated-tissue Vmem map with young-ear reference template
7. **Scarring index:** Masson's trichrome collagen density in regenerated tissue vs adjacent normal tissue

---

## 8. Statistical Analysis Plan

### 8.1 Primary analysis: Regrowth (H1, H2)

**Model:**

```
Regrowth_pct ~ Arm + Sex + BodyWeight_baseline + (1|Cage)
```

- Dunnett's test: each active arm (2–6) vs Arm 1 (sham)
- Pairwise contrasts: Arm 3 vs Arm 4 (bioelectric vs OSK), Arm 5 vs max(Arm 3, Arm 4) (combo vs best mono)
- α = 0.05 with Dunnett correction for the 5 active-vs-sham comparisons

### 8.2 Gap-junction disruption (H3, H4)

**Test:** One-sided t-test: Arm 6 regrowth < 50% of Arm 4 regrowth

- If Arm 6 / Arm 4 < 0.50 at p < 0.025 → **supports H3 (Levin primacy)**
- If Arm 6 / Arm 4 ≥ 0.80 at p < 0.025 → **supports H4 (Sinclair primacy)**
- If 0.50 ≤ ratio < 0.80 → **indeterminate** (partial dependence)

### 8.3 Mediation analysis (H6, H7)

**Causal mediation** (R `mediation` package):

- Mediator path A: Treatment → DNAm clock reversal → Regrowth
- Mediator path B: Treatment → Vmem pattern restoration → Regrowth
- Joint mediation: both mediators simultaneously
- Report: proportion mediated via each path, 95% CI via quasi-Bayesian bootstrap (1000 iterations)

### 8.4 Durability (re-injury)

**Model:**

```
Second_regrowth ~ Arm + First_regrowth + Sex + (1|Cage)
```

- Key contrast: Arm 3 (bioelectric) vs Arm 4 (OSK) on durability ratio
- Levin predicts: Arm 3 durability ratio ≥ Arm 4 (goal-state persists)
- Sinclair predicts: Arm 4 durability ratio ≥ Arm 3 (epigenetic reset persists)

### 8.5 Multiple comparison correction

| Family | Tests | Correction |
|--------|:-----:|-----------|
| Primary regrowth (5 arms vs sham) | 5 | Dunnett |
| Gap-junction disruption | 1 | α = 0.025 (one-sided) |
| Pairwise monotherapy contrasts | 2 | Bonferroni, α = 0.025 each |
| Mediation | Exploratory | Report bootstrap CIs |

---

## 9. Stopping Rules

- **No interim analysis planned** (8-week endpoint is short enough)
- **Futility:** If sham and all active arms show <10% regrowth at T=4 weeks (biopsy subset n=3/arm), injury model is inadequate — switch to digit tip amputation and restart
- **Safety:** If tumor incidence in any OSK arm exceeds 20% at any point, halt OSK dosing in affected arms; continue other arms

---

## 10. Decision Matrix

| Outcome pattern | Favors | Rationale |
|----------------|--------|-----------|
| OSK alone ≥60% regrowth; bioelectric alone <30%; gap-junction disruption has no effect | **Sinclair** | Epigenetic reset is sufficient and independent of bioelectric network |
| Bioelectric alone ≥60% regrowth with superior durability; OSK alone <30% OR poor durability | **Levin** | Controller-state restoration is primary; epigenetic changes are downstream |
| Both monotherapies work; combo outperforms; gap-junction disruption blocks OSK | **Levin primacy** | Bioelectric network is required even for epigenetic-based rescue |
| Both work; combo = additive; gap-junction disruption has no effect on OSK | **Complementary** | Independent mechanisms, neither primary |
| Neither monotherapy reaches ≥30% regrowth | **Inconclusive** | Injury model or dosing inadequate; no discrimination |

### Backlog items resolved

- **S1-SINCLAIR-LEVIN-01** (measurement gap): This experiment directly tests whether OSK requires intact bioelectric communication
- **S1-SINCLAIR-LEVIN-02** (bridge assumption): Dual readouts establish temporal ordering
- **S2-LEVIN-SINCLAIR-01** (bridge assumption): Tests Levin's three bridges in aged mammals

---

## 11. Materials

| Item | Source | Details |
|------|--------|---------|
| C57BL/6J mice (20+ mo) | Jackson Labs #000664 | Aged in-house or NIA Aged Rodent Colony |
| AAV9-TRE-OSK | Vector Biolabs (custom) | Dox-inducible, titer ≥10¹³ vg/mL |
| Doxycycline diet | Bio-Serv | 200 mg/kg, 2 days on / 5 days off |
| Ionophore cocktail (Vmem writing) | Custom: valinomycin + gramicidin + ouabain | Per Levin lab protocols |
| Carbenoxolone | Sigma C4790 | 100 μM in pluronic gel, topical |
| DiBAC4(3) voltage dye | Thermo D8189 | 5 μM in HBSS |
| Calcein-AM (FRAP) | Thermo C1430 | 2 μM |

---

## 12. Data Management

- Raw imaging data deposited in institutional repository
- Analysis scripts pre-registered in `scripts/analysis/osk_bioelectric/`
- Blinding key sealed with compliance office
- Protocol hash committed to repo before first animal randomized
