Project Lifespan
================

Goal: Build a Wikipedia-style site that explains human aging theories through a Popperian lens — clear claims, risky predictions, decisive experiments, and evidence tracking.

Quick start
-----------

- Requirements: Python 3.10+, `pip`
- Install: `pip install -r requirements.txt`
- Serve locally: `mkdocs serve`
- Build: `mkdocs build`

Structure
---------

- `mkdocs.yml` — site configuration
- `docs/` — Markdown content
  - `index.md` — overview
  - `theories/` — per-theory pages (Sinclair, Levin, de Grey, Fedichev, Lidsky, Longevity Bottleneck)
  - `evidence/` — evidence methodology and tables
  - `experiments/` — experiment blueprints and proposals
  - `concepts/` — glossary and background
  - `compare/` — compare theories and scores
- `data/` — structured data (claims, evidence)
- `references/` — BibTeX and web link registry
- `macros/` — mkdocs-macros for Popper scores and helpers
- `scripts/` — utilities (e.g., link archiving)

Popperian rubric
----------------

Criteria (0–5 each): Falsifiability, Riskiness, Precision, Empirical Content, Novel Predictions, Survived Severe Tests, Exposure to Refutation, Rival Comparison, Consilience. Weighted sum produces a Popper Score (0–100).

Contributing
------------

- Write content in `docs/` using the templates in `docs/theories/_template.md` and `docs/experiments/_template.md`.
- Add references to `references/references.bib` (preferred) and `references/links.yaml` for web links.
- Keep claims and evidence synced with `data/claims.yaml` and `data/evidence.csv`.

