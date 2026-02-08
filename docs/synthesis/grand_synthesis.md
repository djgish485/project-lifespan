---
title: Grand Synthesis
---

# Grand Synthesis: The Current Map of Aging Theories

This page is a **conditional snapshot** — a map of what we currently know, what we don't, and exactly which measurements would change our minds. It is designed to be updated, not defended.

**Last updated:** 2026-02-08
**Verdict flip readiness:** 0 (no new severe-test data yet)
**Backlog:** 20 items tracked (18 open, 2 spec-resolved, 0 evidence-resolved)

---

## 1. What the project has established so far

After 15 structured Popperian debates (Seasons 1–3), bidirectional stress-testing, operationalization of all 7 theories into numeric predictions, and pre-registration of 5 decisive experiments, the system has converged on several stable findings:

**The critic always wins.** In every debate, the critic found real vulnerabilities in the defender. This is not a bug — it's the Popperian scoring working correctly as a gap-finder. Every theory has untested bridge assumptions, missing severe tests, or measurement gaps.

**No theory holds a stable lead.** After bidirectional testing (running debates in both directions), apparent "winners" from one-way tests collapsed. SENS and Sinclair show the strongest net Popperian scores (+2 each), but this reflects theoretical riskiness, not empirical vindication. No theory has survived a severe test that its rivals have failed.

**The debates are no longer the bottleneck.** The system has extracted the discriminating questions, written the protocols, and specified what each outcome would mean. Further debates without new evidence would mostly generate more backlog items, not more truth.

---

## 2. Theories as layers, not tribes

A critical insight from the debates: these theories operate at different explanatory levels, and many apparent "contradictions" dissolve when you track which level each claim addresses. The real disagreements are between theories making **competing predictions at the same level**.

### Ultimate layer (evolutionary: *why* does aging exist?)

| Theory | Core claim | Level |
|--------|-----------|-------|
| **Classic Models** (Medawar, Williams, Hamilton, Kirkwood) | Aging is an emergent byproduct of weakening selection with age — not adaptive | Ultimate |
| **Pathogen Control** (Lidsky) | Lifespan is an adaptive setpoint shaped by infectious disease dynamics | Ultimate |

**The crux:** Does population structure (dispersal, cohorting, contact networks) independently predict lifespan after controlling for extrinsic mortality? Classics say no; PC says yes.

### Proximate layer (mechanistic: *how* does aging proceed?)

| Theory | Core claim | Level |
|--------|-----------|-------|
| **SENS** (de Grey) | 7 classes of molecular damage accumulate; comprehensive multi-class repair is necessary and sufficient | Proximate |
| **Epigenetic Information** (Sinclair) | Loss of epigenetic information is the principal upstream cause | Proximate |
| **Longevity Bottleneck** | A small number of choke-point pathways (SASP, mTOR) dominate the hazard | Proximate |

**The crux:** After you clamp the dominant bottleneck pathway, does adding further repair classes yield significant additional lifespan gain? SENS says yes (≥10%); Bottleneck says no (≤3%).

### System-dynamics / control layer (how does the organism *coordinate* aging?)

| Theory | Core claim | Level |
|--------|-----------|-------|
| **Resilience / Criticality** (Fedichev) | Aging is loss of physiological resilience, measurable as critical slowing | Dynamics |
| **Bioelectric / Morphogenetic Control** (Levin) | Tissue-level pattern maintenance via bioelectric networks is upstream of molecular state | Control |

**The crux:** Does survival improvement flow through changes in system-level dynamics (DOSI/autocorrelation) or through changes in specific molecular pathways? The causal direction question.

---

## 3. The four true cruxes

Across 15 debates, the judge verdicts converged on four irreducible disagreements. Each maps to a specific pre-registered experiment with a decision matrix.

### Crux 1: The infection tradeoff

**Disagreement:** Do longevity interventions create an infection penalty in dirty environments?

| If... | Then... |
|-------|---------|
| Rapamycin + dirty → ≥2-fold pathogen burden increase; anti-pathogen package rescues it | **PC confirmed**: senescence is an anti-pathogen barrier |
| Rapamycin works equally in SPF and dirty; no infection penalty | **PC falsified**: aging is intrinsic, not infection-driven |
| Fitness costs appear regardless of pathogen status | **Classics confirmed**: tradeoffs are inevitable |

**Resolves:** 5 backlog items (S1-PC-CLASSICS-01, S1-PC-CLASSICS-02, S1-PC-SENS-01, S1-PC-FEDICHEV-01, S1-CLASSICS-PC-02)
**Protocol:** [Pre-Reg #1: Pathogen-Challenge Factorial](../experiments/prereg_pathogen_factorial.md)

### Crux 2: Epigenetic primacy vs morphogenetic control

**Disagreement:** Is epigenetic state (Sinclair) or bioelectric controller-state (Levin) upstream in determining tissue function during aging?

| If... | Then... |
|-------|---------|
| OSK alone restores function; gap-junction disruption has no effect | **Sinclair primacy**: epigenetic reset is sufficient and independent |
| Bioelectric modulation alone restores function with superior durability; OSK requires intact gap junctions | **Levin primacy**: controller-state is upstream |
| Both work; combo outperforms; gains require intact network | **Levin primacy with synergy** |

**Resolves:** 3 backlog items (S1-SINCLAIR-LEVIN-01, S1-SINCLAIR-LEVIN-02, S2-LEVIN-SINCLAIR-01)
**Protocol:** [Pre-Reg #2: OSK vs Bioelectric vs Combo](../experiments/prereg_osk_bioelectric_combo.md)

### Crux 3: Saturation vs multi-class necessity

**Disagreement:** After clamping the dominant bottleneck pathway, does adding further repair classes extend maximum lifespan?

| If... | Then... |
|-------|---------|
| Clamp + TERT or crosslink breaker yields ≥10% additional max lifespan | **SENS confirmed**: multiple damage classes matter |
| All add-ons yield ≤3% beyond clamp alone | **Bottleneck confirmed**: one pathway dominates |
| Stack shows synergy (super-additive) | **Strongly favors SENS**: multi-class necessity |

**Resolves:** 3 backlog items (S1-SENS-BOTTLENECK-01, S1-SENS-BOTTLENECK-02, S2-BOTTLENECK-SENS-01)
**Protocol:** [Pre-Reg #3: Bottleneck-Clamp + SENS Add-on](../experiments/prereg_bottleneck_clamp_sens.md)

### Crux 4: Dynamics-first vs pathway-first causality

**Disagreement:** Does survival improvement flow through changes in system-level resilience dynamics, or through specific molecular pathway changes?

| If... | Then... |
|-------|---------|
| Survival mediated ≥50% through DOSI/autocorrelation; <25% through bottleneck markers | **Fedichev confirmed**: resilience dynamics are primary |
| Survival mediated ≥50% through bottleneck biomarkers; <25% through DOSI | **Bottleneck confirmed**: pathway state drives everything |
| Both mediate independently ≥25% each | **Complementary**: different aspects of the same process |

**Resolves:** 2 backlog items (S1-FEDICHEV-BOTTLENECK-01, S3-BOTTLENECK-FEDICHEV-02)
**Protocol:** [Pre-Reg #4: Resilience vs Pathway Mediation](../experiments/prereg_resilience_mediation.md)

---

## 4. The decision tree of reality

```
START: Run pre-registered severe tests
│
├─ Experiment #1 (Pathogen Factorial)
│  ├─ Infection penalty + rescue → PC strengthened, Classics weakened
│  ├─ No infection penalty → PC falsified on core prediction
│  └─ Fitness costs regardless → Classics tradeoff confirmed
│
├─ Experiment #2 (OSK vs Bioelectric)
│  ├─ OSK works without gap junctions → Sinclair primacy
│  ├─ Bioelectric alone + durability → Levin primacy
│  └─ Combo + network-dependent → Levin primacy with synergy
│
├─ Experiment #3 (Clamp + Add-on)
│  ├─ Add-on gains ≥10% → SENS multi-class confirmed
│  ├─ Add-on gains ≤3% → Bottleneck saturation confirmed
│  └─ Synergy in stack → Strongly SENS
│
├─ Experiment #4 (Resilience Mediation)
│  ├─ DOSI mediates survival → Fedichev dynamics primary
│  ├─ Pathway markers mediate → Bottleneck pathways primary
│  └─ Both mediate → Complementary mechanisms
│
└─ Experiment #5 (RMR1 Analysis)
   ├─ Synergistic interactions → SENS necessity
   ├─ One component dominates → Bottleneck structure
   └─ Additive, all contribute → Weak SENS (additive, not synergistic)
```

Each branch has pre-specified thresholds, stopping rules, and decision matrices in the linked pre-registration documents.

---

## 5. Current score (Popperian, not truth)

This table reflects **theoretical exposure to refutation**, not empirical vindication. A high net score means the theory generates riskier predictions that survived debate criticism — not that the theory is correct.

| Theory | Won as Critic | Lost as Defender | Net | Biggest vulnerability |
|--------|:---:|:---:|:---:|----------------------|
| SENS | 3 | 1 | +2 | Multi-class necessity untested (S1-SENS-BOTTLENECK-01) |
| Sinclair | 3 | 1 | +2 | Temporal ordering of epigenetic drift vs controller-state unknown (S1-SINCLAIR-LEVIN-02) |
| Fedichev | 2 | 1 | +1 | DOSI causal independence unproven (S1-FEDICHEV-BOTTLENECK-01) |
| Levin | 2 | 1 | +1 | Three bridge assumptions untested in aged mammals (S2-LEVIN-SINCLAIR-01) |
| Bottleneck | 2 | 2 | 0 | Saturation prediction untested; Gompertz slope claim untested (S2-BOTTLENECK-SENS-01) |
| Classics | 1 | 1 | 0 | Cannot predict population-structure patterns (S1-CLASSICS-PC-02) |
| PC | 1 | 4 | -3 | Zero severe tests passed; all evidence is modeling/review (S1-PC-CLASSICS-01) |

**Key caveat:** These scores will change the moment any of the five decisive experiments produces data. The system is designed for that.

---

## 6. Open criticisms backlog

The full tracked backlog lives at [Open Criticisms Backlog](../debates/backlog.md).

**Current status:** 20 items total

| Type | Open | Spec-resolved | Evidence-resolved |
|------|:----:|:---:|:---:|
| Missing severe test | 5 | 0 | 0 |
| Bridge assumption | 5 | 0 | 0 |
| Measurement gap | 4 | 0 | 0 |
| Definitional escape | 4 | 2 | 0 |
| **Total** | **18** | **2** | **0** |

The zero in the "Evidence-resolved" column is the honest signal: **no theory has yet been tested severely enough to close an open criticism with data.**

---

## 7. How to read debate verdicts

Debates in this project are used as **epistemic maintenance tools**, not as truth-determiners:

- **What debates do:** Extract surviving criticisms, generate candidate severe tests, maintain consistency after new evidence, detect definitional escapes
- **What debates don't do:** Determine which theory is correct, provide empirical evidence, or substitute for experiments
- **When to run a debate:** Only when (a) new evidence appears, (b) a claim is operationalized/revised, or (c) a backlog item is marked spec-resolved and needs verification
- **How to interpret "critic wins":** The critic identified real gaps in the defender's position — this is the Popperian scoring working correctly as a gap-finder, not a truth-finder

---

## 8. What would change this page

This synthesis will be updated when:

1. **Any of the five decisive experiments produces data** — the decision matrices specify exactly how each outcome maps to theory updates
2. **RMR1 results become available** — the pre-registered analysis plan is ready to run immediately
3. **A backlog item moves from "open" to "evidence-resolved"** — the first evidence-resolved item will be a milestone for the project
4. **External severe-test data appears** (e.g., published studies that match our pre-registered predictions) — the claims registry specifies what counts

Until then, this page represents **the best current map of where the theories disagree and what would settle it** — not a verdict on which theory is right.
