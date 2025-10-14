---
title: OSK Partial Reprogramming Lifespan Study in Aged Mice
---

# OSK Partial Reprogramming Lifespan Study in Aged Mice

Linked theory: [Epigenetic Information (Sinclair)](../theories/epigenetic_information.md)

## Hypothesis

Loss of epigenetic information is a principal driver of aging phenotypes; periodic, partial reprogramming (OSK) in adult mice restores youthful epigenetic state, lowers all-cause mortality hazard, and extends maximum lifespan without increasing tumor incidence.

## Prediction (Measurable)

- Max lifespan: ≥10% increase vs. doxycycline-off controls.
- Mortality: Hazard ratio ≤0.85 (post-randomization) vs. control, estimated by Cox model.
- Tumor incidence: No increase vs. control (non-inferiority margin 1.2x).
- Biomarkers: Epigenetic clock delta (liver, blood) ≥20% reduction sustained ≥6 months.

## Essentials Protocol

- Model: C57BL/6J, mixed sex, aged 20 months at randomization.
- N: 60/arm (power 80% to detect 10% max lifespan increase; alpha 0.05; assume Weibull hazard).
- Arms: OSK-cycles + doxycycline; doxycycline-off (vector); vehicle; positive control (rapamycin).
- Vectors: AAV9 or AAV2/9 TRE-OSK + tTA liver-wide (or tissue-prioritized protocol). Dose from [@Lu2020] preclinical ranges; pilot tolerability first.
- Regimen: 1 week on/2 weeks off cycles; adapt if toxicity signals appear. Blinded outcome assessment.
- Randomization/blinding: Cage-level blocking; independent data team for analyses; pre-registered endpoints.

## Controls

- OSK-off (doxycycline-withheld) to control for vector effects.
- Vehicle only.
- Positive control: rapamycin (14 ppm in chow) to benchmark hazard and lifespan effects.

## Endpoints and Analysis

- Primary: Maximum lifespan (top 10% age); secondary: median lifespan, all-cause hazard, epigenetic age (blood/liver), tumor incidence, clinical pathology.
- Analysis: Kaplan–Meier with log-rank; Cox proportional hazards; pre-specified censoring rules; competing-risk for tumor-first events.

## Cost/Time/Ethics

- Cost: $600k–$1.2M (AAV production dominates). Timeline: 18–30 months (aging cohort).
- Ethical: Tumor monitoring with humane endpoints; minimize discomfort; IACUC approval required.

## Falsifiers

- No improvement in hazard or maximum lifespan; or any significant increase in tumor incidence vs. control.

## References

- Background: [@Lu2020; @Ocampo2016; @Yang2023]
