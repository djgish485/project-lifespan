---
title: THEORY_NAME
summary: >-
  One-paragraph lay summary of the theory.
popper:
  scores:
    falsifiability: 0
    riskiness: 0
    precision: 0
    empirical_content: 0
    novel_predictions: 0
    severe_tests: 0
    exposure: 0
    rival_comparison: 0
    consilience: 0
tags:
  - example
---

# THEORY_NAME

{{ popper_card() }}

## Lay Summary

Explain in intuitive terms.

## Technical Summary

Mechanisms, pathways, formal statements.

## Evolutionary Context

What evolutionary pressures or tradeoffs are proposed?

## Core Claims

- {{ claim('c1', 'Core claim', 'Measurable prediction if applicable') }}
- {{ claim('c2', 'Another claim', '') }}

## Predictions (Operationalized)

- Specify endpoints (e.g., max lifespan +X%, clock age −Y%, hazard ratio).
- Define time frame and model organism.
- Note auxiliary assumptions required.

## Evidence

### For

- Briefly summarize key supporting studies with citations.

### Against / Disconfirmations

- Summarize failures, null results, boundary conditions.

## Rival Theories and Comparisons

- What rivals explain the same phenomena with fewer assumptions or stronger predictions?

## Proposed Experiments

- {{ experiment_box('Experiment title', 'Hypothesis...', 'Prediction...', 'Endpoints...', 'Controls...', '$', 'timeline') }}

## References

- Cite primary literature using [@citation_key].
- For web claims, add to `references/links.yaml` and cite as Web.

