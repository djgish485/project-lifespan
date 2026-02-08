---
title: Research Agenda
---

# Research Agenda: Decisive Experiments from Debate Convergence

These five experiments emerged independently across multiple judge verdicts in Season 1 and Season 2 debates. Each discriminates between two or more theories and was cited by judges as the highest-leverage next step. They are listed in order of discriminatory breadth (how many theory pairs each resolves).

**See also:** [Open Criticisms Backlog](../debates/backlog.md) for the tracked list of surviving criticisms that these experiments would help resolve.

---

## 1. Pathogen-Challenge Factorial (2x2x2)

**Status:** Upgraded to pre-registration grade — see [Full Pre-Registration Protocol](prereg_pathogen_factorial.md)

**Discriminates:** PC vs Classics, PC vs SENS, PC vs Fedichev

**Design:** Pre-registered factorial in aged C57BL/6J mice:

- Factor A: Longevity intervention (rapamycin or senolytics or partial reprogramming) vs control
- Factor B: Environment (SPF vs dirty/rewilded)
- Factor C: Anti-pathogen package (vaccination/antivirals/barrier housing) vs none

**Primary endpoints:** Maximum lifespan, hazard, pathogen burden/persistence, shedding/transmission proxies

**Secondary endpoints:** Reproduction, stress tolerance, senescence markers, energy expenditure

**Pre-registration requirements:**

- Specific pathogens (e.g., MHV, MNV, Helicobacter)
- Effect-size thresholds for each endpoint
- Dose/timing for longevity intervention
- Transmission measurement protocol (sentinel animals)

**What each outcome means:**

- Longevity intervention + dirty environment → increased infection persistence/transmission: **favors PC**
- Longevity intervention works equally in SPF and dirty: **favors Classics / intrinsic theories**
- Anti-pathogen package rescues infection penalty: **strongly favors PC**
- No infection penalty from any intervention: **challenges PC's core prediction**

**Related blueprints:**

- [Anti-pathogen Bottleneck](anti_pathogen_bottleneck.md)
- [OSK Infection Tradeoff](osk_infection_tradeoff.md)
- [SENS Stack Infection Tradeoff](sens_stack_infection_tradeoff.md)
- [Pathogen Burden Resilience](pathogen_burden_resilience.md)

**Cited in:** Classics vs PC, PC vs Classics, PC vs SENS, PC vs Fedichev, PC vs Levin

---

## 2. OSK vs Bioelectric vs Combo Aged Regeneration

**Status:** Upgraded to pre-registration grade — see [Full Pre-Registration Protocol](prereg_osk_bioelectric_combo.md)

**Discriminates:** Sinclair vs Levin

**Design:** Pre-registered factorial in aged C57BL/6J mice (digit tip or full-thickness skin wound):

- Arm 1: Sham
- Arm 2: Uniform stimulation control
- Arm 3: Pattern-aware bioelectric modulation (lesion + neighbor Vmem writing)
- Arm 4: Local cyclic OSK
- Arm 5: OSK + pattern-aware bioelectric combo

**Primary endpoints:**

- Regrowth size and morphological correctness
- Scarring index
- Tumor/aberrant growth incidence
- **Durability across re-injury** (the "goal reset persisted" test — re-injure at 8 weeks and measure second recovery)

**Dual readout requirement (critical):**

- Epigenetic: DNAm clocks (Horvath/Thompson), histone modification panels
- Controller-state: Vmem imaging, gap-junction connectivity, active information storage, transfer entropy, spatial entropy

This dual measurement enables **mediation analysis** to distinguish whether functional rescue flows through epigenetic state changes or controller-state restoration.

**What each outcome means:**

- OSK alone restores function + resets clocks, bioelectric metrics are downstream: **favors Sinclair**
- Pattern-aware modulation alone restores function + improves durability, DNAm changes are partial: **favors Levin**
- Combo outperforms both; gains require intact bioelectric network: **favors Levin primacy**
- OSK works even with gap-junction disruption (carbenoxolone or Cx43 dominant-negative): **strongly favors Sinclair**

**Related blueprints:**

- [Vmem Regeneration](vmem_regeneration.md)
- [OSK Mouse Lifespan](osk_mouse_lifespan.md)

**Cited in:** Sinclair vs Levin, Levin vs Sinclair

---

## 3. Bottleneck-Clamp + SENS Add-on

**Status:** Upgraded to pre-registration grade — see [Full Pre-Registration Protocol](prereg_bottleneck_clamp_sens.md)

**Discriminates:** SENS vs Longevity Bottleneck

**Design:** In aged C57BL/6J mice (20+ months):

- Phase 1 (clamp verification): Rapamycin + D+Q senolytic to pre-specified SASP/mTOR biomarker thresholds. Only mice meeting verified clamp criteria advance.
- Phase 2 (randomization): Clamp-verified mice randomized to:
  - Arm A: Clamp only (continue rapamycin + D+Q)
  - Arm B: Clamp + TERT activation
  - Arm C: Clamp + crosslink breaker
  - Arm D: Clamp + TERT + crosslink breaker

**Primary endpoint:** Maximum lifespan

**Pre-registered thresholds:**

- SENS predicts: Arms B/C/D yield ≥10% additional max-lifespan gain over Arm A
- Bottleneck predicts: Arms B/C/D yield ≤3% additional gain (saturation after clamp)

**Related blueprints:**

- [SENS Stack Mouse](sens_stack_mouse.md)

**Cited in:** SENS vs Bottleneck, Bottleneck vs SENS

---

## 4. Resilience vs Pathway Mediation Study

**Status:** Upgraded to pre-registration grade — see [Full Pre-Registration Protocol](prereg_resilience_mediation.md)

**Discriminates:** Fedichev vs Longevity Bottleneck

**Design:** Pre-registered 4-arm interventional mediation study in aged mice:

- Arm 1: Vehicle control
- Arm 2: D+Q senolytics (bottleneck-targeting)
- Arm 3: Resilience-optimized tuning protocol (exercise + cold exposure + caloric cycling)
- Arm 4: Combination (D+Q + resilience protocol)

**Endpoints (all collected longitudinally):**

- Survival / hazard
- Passive DOSI / autocorrelation time (resilience metrics)
- Active perturbation-recovery battery (glucose tolerance, cold recovery, hypoxia recovery)
- Bottleneck biomarkers (p16, IL-6, SASP panel, GDF-15)

**Critical analysis:** Pre-specified **mediation tests** for whether survival effects flow through resilience metrics or bottleneck biomarkers.

**What each outcome means:**

- Survival gain mediated primarily by DOSI/autocorrelation improvement: **favors Fedichev**
- Survival gain mediated primarily by bottleneck biomarker reduction: **favors Bottleneck**
- Both mediate independently: **complementary mechanisms**

**Cited in:** Fedichev vs Bottleneck, Bottleneck vs Fedichev

---

## 5. RMR1 Factorial Publication

**Status:** Upgraded to pre-registration grade — see [Pre-Registered Analysis Plan](prereg_rmr1_analysis.md)

**Discriminates:** SENS vs Longevity Bottleneck (directly, with existing data)

**What's needed:** Publication of the complete Robust Mouse Rejuvenation Study 1 (RMR1) results with:

- Maximum lifespan as primary endpoint
- Hazard interaction terms (synergy between repair classes)
- All-but-one arms (what happens when you drop each component?)
- Pre-specified target-engagement thresholds per repair component
- Blinded pathology
- Bottleneck pathway readouts alongside repair endpoints

**Why this is decisive:** This dataset already exists (or is being collected). Its interaction terms directly test SENS's "multi-class necessity" claim vs Bottleneck's "saturation" prediction.

**Source:** [LEVF RMR1](https://www.levf.org/projects/robust-mouse-rejuvenation-study-1)

**Cited in:** SENS vs Bottleneck, Bottleneck vs SENS
