---
title: Classic Models (Medawar, Williams, Hamilton, Kirkwood)
summary: >-
  Non-programmed evolutionary theories: aging arises as a byproduct of damage accumulation and selection tradeoffs (pleiotropy) with limited investment in repair (disposable soma).
popper:
  scores:
    falsifiability: 3
    riskiness: 2
    precision: 2
    empirical_content: 3
    novel_predictions: 1
    severe_tests: 1
    exposure: 3
    rival_comparison: 2
    consilience: 3
tags:
  - evolutionary
  - damage
  - pleiotropy
  - disposable-soma
---

# Classic Models (Medawar, Williams, Hamilton, Kirkwood)

{{ popper_card() }}

## Lay Summary

These theories say aging is not on purpose. Bodies slowly accumulate damage; evolution favors genes that help early life even if they hurt later; and organisms budget just enough repair to reproduce, not to keep working perfectly forever.

## Technical Summary

- Damage accumulation: stochastic molecular/cellular damage builds up and drives aging.
- Antagonistic pleiotropy (Williams): alleles beneficial early (fitness/reproduction) are selected even if late-life deleterious.
- Disposable soma (Kirkwood): finite resources trade off between reproduction and somatic maintenance; optimal strategy under selection leaves residual damage.

## Core Claims

- {{ claim('classic-c1', 'Aging is non-programmed; late-life decline results from damage and selection tradeoffs.', 'Increasing repair investment should generally trade off with reproduction across environments.') }}

## Predictions (Operationalized)

- Across species, repair/investment correlates with lifespan once confounders are controlled.
- Early-life fitness advantages predict late-life costs at the allele/trait level.
- No active, adaptive mechanism needed to limit lifespan; rejuvenation should be constrained by repair/maintenance budgets.

## Evidence

- Foundational theory: [@Williams1957; @Hamilton1966; @Kirkwood1977; @KirkwoodHolliday1979]; broad empirical support for tradeoffs in life-history.

## Rival Theories and Comparisons

- Adaptation/program: [Pathogen Control (Lidsky)](pathogen_control.md) posits lifespan setpoints selected to limit epidemics.
- Damage-repair (SENS): proposes direct repair can extend lifespan despite upstream causes.
- Epigenetic reset (Sinclair): emphasizes reprogrammability of state vs irreducible damage.

## Critiques

### Inbound (from Pathogen Control (Lidsky))

- Rejuvenation happens in nature and often under stress — hard to reconcile with Classic Models’ damage/tradeoff view. Pathogen Control explains it by epidemic risk costs of longevity.
  - Discriminator experiment(s):
    <ul>
      <li><a href="../experiments/rejuvenation_pathogen_tradeoff.md">Rejuvenation vs Pathogen Tradeoff</a> — Give older mice a rejuvenation treatment; half also get anti‑infection. If rejuvenation alone helps with no infection downside, that favors Classic Models; if the combo is needed, that favors Pathogen Control. (12–18 months; $400k–$800k)</li>
      <li>Comparative analysis (desk) — Compare species that rejuvenate under stress to their infection environments; if rejuvenators mostly face high infection pressure and flip back only when stressed, that supports Pathogen Control. (1–3 months; $5k–$25k)</li>
    </ul>
- Sources: [Tweet mirror](https://vxtwitter.com/lidskypeter/status/1962526281863508444), [Talk (Foresight)](https://foresight.org/resource/peter-lidsky-why-do-we-age-searching-for-a-paradigm/)

### Inbound (from Sinclair (Epigenetic Information))

- Reprogramming may circumvent tradeoff limits by resetting state; strong, low‑cost max‑lifespan gains would challenge Classics.
- Discriminator experiment(s):
  <ul>
    <li><a href="../experiments/osk_mouse_lifespan.md">OSK Lifespan Study</a> — Check for costs alongside gains. (18–30 months; $600k–$1.2M)</li>
  </ul>
- Sources: <a href="https://doi.org/10.1038/s41586-020-2975-4">Lu2020</a>

### Inbound (from SENS (Damage Repair))

- Engineered repairs could extend lifespan beyond budget expectations if carefully targeted and safe.
- Discriminator experiment(s):
  <ul>
    <li><a href="../experiments/sens_stack_mouse.md">SENS Stacked Repairs</a> — Look for large max‑lifespan gains without major fitness costs. (24–36 months; $1.2M–$2.5M)</li>
  </ul>
- Sources: <a href="https://doi.org/10.1038/s41591-018-0092-9">Xu2018</a>; <a href="https://doi.org/10.1038/nature10600">Baker2011</a>

### Inbound (from Peter Fedichev (Resilience/Criticality))

- System‑level resilience improvements can lower hazard broadly without requiring increased repair budgets or invoking infection ecology. Large, low‑cost hazard shifts would challenge strict tradeoff expectations.
- Discriminator experiment(s):
  <ul>
    <li><a href="../experiments/resilience_training.md">Resilience Training</a> — Reduce autocorrelation time/variance and hazard in aged mice; assess durability and costs. (12–24 months; $150k–$300k)</li>
  </ul>
- Sources: <a href="https://doi.org/10.1038/s41467-021-23014-1">Pyrkov2021</a>

### Inbound (from Michael Levin (Bioelectric / Morphogenetic))

- Restoring bioelectric pattern control could rejuvenate function without large repair budgets; strong, low‑cost gains would strain a damage/pleiotropy framing.
- Discriminator experiment(s):
  <ul>
    <li><a href="../experiments/vmem_regeneration.md">Bioelectric Modulation</a> — Improve regeneration/function in aged mice and track tradeoffs. (3–6 months; $100k–$200k)</li>
  </ul>
- Sources: <a href="https://doi.org/10.1016/j.cell.2021.02.034">Levin2021</a>

### Inbound (from Longevity Bottleneck)

- A specific chronic damage‑response bottleneck could dominate aging dynamics; relieving it might deliver gains beyond simple budget constraints.
- Discriminator experiment(s):
  <ul>
    <li><a href="../experiments/anti_pathogen_bottleneck.md">Resolve Damage‑Response Bottleneck</a> — Targeted relief vs non‑specific longevity control; check hazard and signaling normalization. (6–9 months; $100k–$220k)</li>
  </ul>
- Sources: <a href="https://doi.org/10.1038/s41574-018-0059-4">Franceschi2018</a>; <a href="https://doi.org/10.1038/s41467-025-64462-3">Ogrodnik2025</a>

### Outbound (Classics → others)

#### [Epigenetic Information (Sinclair)](epigenetic_information.md)

- Classics predict tradeoffs: powerful reprogramming should reveal costs (e.g., tumors, impaired function) or modest gains. If OSK extends maximum lifespan substantially with minimal costs, that challenges a strict tradeoff view.

- Discriminator experiment(s):
  <ul>
    <li><a href="../experiments/osk_mouse_lifespan.md">OSK Lifespan Study</a> — Look for hidden costs (tumors, frailty) alongside any lifespan gains. (18–30 months; $600k–$1.2M)</li>
  </ul>
- Sources: Foundational classics; Sinclair primary

#### [SENS Damage Repair (de Grey)](sens_damage_repair.md)

- Classics allow repair to help but expect diminishing returns and costs. If stacked repairs extend max lifespan >15% with acceptable safety and little fitness cost, that pushes beyond simple budget constraints.

- Discriminator experiment(s):
  <ul>
    <li><a href="../experiments/sens_stack_mouse.md">SENS Stacked Repairs</a> — Test for large gains vs toxicity/costs. (24–36 months; $1.2M–$2.5M)</li>
  </ul>
- Sources: Foundational classics; SENS primary

#### [Pathogen Control (Lidsky)](pathogen_control.md)

- Classics do not require infection penalties for longevity gains. If rejuvenation/extension routinely imposes infection downsides unless anti‑pathogen measures co‑apply, that favors PC over Classics.

- Discriminator experiment(s):
  <ul>
    <li><a href="../experiments/rejuvenation_pathogen_tradeoff.md">Rejuvenation vs Pathogen Tradeoff</a> — Probe whether gains require anti‑pathogen support. (12–18 months; $400k–$800k)</li>
  </ul>
- Sources: <a href="https://doi.org/10.1073/pnas.1920988117">PC modeling</a>; Foundational classics

#### [Resilience / Criticality (Fedichev)](resilience_criticality.md)

- If resilience training lowers hazard broadly without costs, that strains a pure tradeoff view; conversely, small or transient effects fit Classics.

- Discriminator experiment(s):
  <ul>
    <li><a href="../experiments/resilience_training.md">Resilience Training</a> — Check magnitude/durability vs side effects. (12–24 months; $150k–$300k)</li>
  </ul>
- Sources: <a href="https://doi.org/10.1038/s41467-021-23014-1">Pyrkov2021</a>; Foundational classics

#### [Bioelectric / Morphogenetic Control (Levin)](bioelectric_morphogenetic_control.md)

- If pattern control alone yields strong rejuvenation in aged mammals with minimal costs, that challenges a damage/repair budget framing.

- Discriminator experiment(s):
  <ul>
    <li><a href="../experiments/vmem_regeneration.md">Bioelectric Modulation</a> — Assess gains vs tradeoffs. (3–6 months; $100k–$200k)</li>
  </ul>
- Sources: <a href="https://doi.org/10.1016/j.cell.2021.02.034">Levin2021</a>; Foundational classics

## References

- Foundational: [@Medawar1952; @Williams1957; @Hamilton1966; @Kirkwood1977; @KirkwoodHolliday1979]
