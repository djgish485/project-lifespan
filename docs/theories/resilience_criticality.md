---
title: Resilience / Criticality (Fedichev)
summary: >-
  Aging as loss of resilience and approach to criticality in physiological networks; interventions that restore resilience shift mortality and health trajectories.
popper:
  scores:
    falsifiability: 3
    riskiness: 3
    precision: 3
    empirical_content: 3
    novel_predictions: 3
    severe_tests: 2
    exposure: 2
    rival_comparison: 3
    consilience: 3
tags:
  - resilience
  - criticality
---

# Resilience / Criticality (Fedichev)

{{ popper_card() }}

> Seed links: postings and debates with de Grey; collect primary papers modeling mortality dynamics and resilience metrics.

## Lay Summary

Physiology becomes fragile with age; small shocks cause bigger, longer-lasting deviations. If we can measure and restore resilience, we could slow or reverse aging dynamics.

## Technical Summary

- Hypothesis: aging is a stochastic dynamical process with increasing autocorrelation time and variance (critical slowing down). Predictable signatures appear in longitudinal biomarkers and physical activity fluctuations [@Pyrkov2021].

## Core Claims

- {{ claim('fed-c1', 'Resilience metrics predict mortality and intervention response.', 'Restoring resilience shifts the whole hazard curve, not just a subset of pathologies.') }}

## Predictions

- Pre-registered resilience interventions in mice reduce autocorrelation times in biomarkers and lower all-cause mortality.

## Evidence

- Longitudinal blood count trajectories suggest progressive loss of resilience with age, extrapolating to a limit on human lifespan due to divergence of recovery time and variance [@Pyrkov2021].

## Rivals

- Damage-first vs regulatory-dynamics-first; test discriminators.

## Critiques

### Outbound (Resilience/Criticality → others)

#### [Classic Models (Damage/AP/Disposable Soma)](classic_models.md)

- Classic Models emphasize repair budgets and tradeoffs; resilience proposes that system‑level dynamics (critical slowing down) are primary. If restoring resilience reduces hazard broadly without obvious tradeoff costs, that challenges a strict tradeoff‑only framing.

- Discriminator experiment(s):
  <ul>
    <li><a href="../experiments/resilience_training.md">Resilience Training</a> — Reduce autocorrelation time/variance in aged mice and check for hazard reduction beyond what Classic tradeoffs would predict. (12–24 months; $150k–$300k)</li>
  </ul>
- Sources: <a href="https://doi.org/10.1038/s41467-021-23014-1">Pyrkov2021</a>

#### [Pathogen Control (Lidsky)](pathogen_control.md)

- If infections are the main driver, reducing pathogen burden should dominate outcomes. Resilience claims improvements can occur independently of infection changes; pathogen control is not necessary for hazard shifts.

- Discriminator experiment(s):
  <ul>
    <li><a href="../experiments/pathogen_burden_resilience.md">Pathogen Burden vs Resilience</a> — Compare an anti‑pathogen plan to a resilience intervention in aged mice; if resilience matches or exceeds benefits without infection changes, that favors Resilience/Criticality. (6–12 months; $150k–$300k)</li>
  </ul>
- Sources: <a href="https://doi.org/10.1073/pnas.1920988117">PC modeling</a>; <a href="https://doi.org/10.1038/s41467-021-23014-1">Pyrkov2021</a>

#### [Epigenetic Information (Sinclair)](epigenetic_information.md) and [SENS Damage Repair (de Grey)](sens_damage_repair.md)

- Resilience predicts that tuning system dynamics can shift mortality hazard without targeting specific damages or epigenetic state. If resilience training yields hazard reductions comparable to OSK or stacked repairs, that supports a dynamics‑first view.

- Discriminator experiment(s):
  <ul>
    <li><a href="../experiments/resilience_training.md">Resilience Training</a> — Pre‑registered hazard reduction with improved DOSI metrics. (12–24 months; $150k–$300k)</li>
    <li><a href="../experiments/sens_stack_mouse.md">SENS Stacked Repairs</a> — Compare durability and breadth of hazard shifts vs resilience outcomes. (24–36 months; $1.2M–$2.5M)</li>
  </ul>
- Sources: <a href="https://doi.org/10.1038/s41467-021-23014-1">Pyrkov2021</a>; SENS/Sinclair primaries

### Inbound (from Pathogen Control (Lidsky))

- If infections drive aging dynamics, reducing pathogen burden should improve resilience and survival.
  - Discriminator experiment(s):
    <ul>
      <li><a href="../experiments/pathogen_burden_resilience.md">Reducing Pathogen Burden Improves Resilience Metrics</a> — Help older mice avoid/clear infections (vaccines/antivirals) and track day‑to‑day recovery and survival, compared to a standard longevity drug. Bigger gains from the anti‑infection plan support Pathogen Control; similar gains from the non‑infection drug support a resilience‑only view. (6–12 months; $150k–$300k)</li>
    </ul>
- Sources: [PC framework](https://doi.org/10.1073/pnas.1920988117), [Resilience metrics](https://doi.org/10.1038/s41467-021-23014-1)

### Inbound (from Sinclair (Epigenetic Information))

- Resetting epigenetic state may directly lower hazard beyond resilience adjustments; resilience training might be secondary.
- Discriminator experiment(s):
  <ul>
    <li><a href="../experiments/osk_mouse_lifespan.md">OSK Lifespan Study</a> — Compare hazard reductions to resilience interventions. (18–30 months; $600k–$1.2M)</li>
  </ul>
- Sources: <a href="https://doi.org/10.1038/s41586-020-2975-4">Lu2020</a>

### Inbound (from SENS (Damage Repair))

- Repairing concrete damages may be required; resilience without repair might give modest or transient gains.
- Discriminator experiment(s):
  <ul>
    <li><a href="../experiments/sens_stack_mouse.md">SENS Stacked Repairs</a> — Compare durability of hazard shifts vs resilience training. (24–36 months; $1.2M–$2.5M)</li>
  </ul>
- Sources: <a href="https://doi.org/10.1038/s41591-018-0092-9">Xu2018</a>

### Inbound (from Classic Models)

- Large, low‑cost hazard shifts would be surprising; expect tradeoffs or limited effects.
- Discriminator experiment(s):
  <ul>
    <li><a href="../experiments/resilience_training.md">Resilience Training</a> — Track side effects and durability. (12–24 months; $150k–$300k)</li>
  </ul>
- Sources: Foundational classics

## Proposed Experiments

- {{ experiment_box('Resilience training in aged mice', 'Loss of resilience is causal.', 'Improved resilience metrics lead to lower mortality hazard.', 'Time-series biomarkers, frailty index, lifespan.', 'Sham training; young baseline; rapamycin benchmark.', '$150k–$300k', '12–24 months') }}

## References

- Primary: [@Pyrkov2021]
