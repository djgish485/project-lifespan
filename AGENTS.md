Project Lifespan – Agent Notes
==============================

These notes capture working conventions and operational SOPs for agents contributing to this repository. Keep this file up to date as we standardize more sections and flows.

Remote Verification SOP (No Local Serve)
---------------------------------------

Default git flow in this repo is **branch + PR**. Do not push to `main` unless the user explicitly asks.

We do not run a local `mkdocs serve` in this repo. Verify using the live GitHub Pages site *after changes land on `main`*.

1) Optional: strict build locally to catch issues early
   - `source .venv/bin/activate`
   - `mkdocs build --strict`

2) Commit and push changes to your working branch (CI does not deploy Pages from branches by default)

3) If/when merged to `main`: verify on GitHub Pages with a cache‑buster
   - Example: `curl -sSf "http://dangish.net/project-lifespan/?_cb=TIMESTAMP"`
   - Confirm expected new text renders on the target page(s).

Notes
- Do not keep any local dev servers running.
- If a stale local server is suspected, kill any `mkdocs serve` processes and delete `.mkdocs*.pid`, but do not start a new one.

Local Dev Server SOP (Only If Explicitly Requested)
---------------------------------------------------

MkDocs Material sometimes leaves stale servers running. Always restart the dev server after edits so users see changes immediately.

1) Build strictly to catch issues early
   - `source .venv/bin/activate`
   - `mkdocs build --strict`

2) Stop any existing server before starting a new one
   - If we store a pid: `if [ -f .mkdocs.pid ] && ps -p $(cat .mkdocs.pid) >/dev/null 2>&1; then kill $(cat .mkdocs.pid); fi`
   - If the port is still in use: `kill $(lsof -iTCP:8000 -sTCP:LISTEN -t)`

3) Start a fresh server and verify
   - `nohup .venv/bin/mkdocs serve -a 127.0.0.1:8000 >/tmp/project_lifespan_mkdocs.log 2>&1 & echo $! > .mkdocs.pid`
   - `sleep 1.2 && curl -sSf http://127.0.0.1:8000/ >/dev/null`

4) Only hand back URLs after step (3) succeeds.

Agent-Run Policy (Do It For The User)
-------------------------------------

- The agent executes the SOP on behalf of the user. Do not provide command instructions for the user to run; perform the actions directly and return results.
- Default posture: do work on a branch. Do not push to `main` unless explicitly requested.
- After edits, always run a strict build (`mkdocs build --strict`) before pushing.
- For branch work: report the branch name and latest commit SHA.
- Only when changes land on `main`: verify the exact page content on GitHub Pages with `curl` using a cache‑buster query parameter (like `?_cb=TIMESTAMP`).

Formatting – Critiques Sections (Current Standard)
--------------------------------------------------

Applies to every theory page. We will extend AGENTS.md with standards for other sections (Evidence, Proposed Experiments, etc.) as we converge.

Structure
1) `## Critiques`
2) Outbound on origin theory page: `### Outbound (This Theory → others)`
   - For each rival: linked subheader to target theory page
     - `#### [Rival Name](relative/path/to/rival.md)`
     - 1–2 short bullets in plain English explaining the critique (no "Lay summary:" labels)
     - One bullet: `Discriminator experiment(s):`
       - Nested 1–3 experiment items, each:
         - A hyperlink to the experiment page
         - A one‑line, lay explanation of what the experiment does and why it discriminates
         - Duration and rough cost at the end in parentheses, e.g. `(12–18 months; $400k–$800k)`
     - One bullet: `Sources:` followed by inline hyperlinks only (e.g., tweet mirrors, talk pages, primary DOIs). Do not include plain IDs.
     - Do not add a `Rival page: ...` bullet; the header link covers this.

3) Inbound on target theory page: `### Inbound (from Origin Theory Name)`
   - 1 short bullet in plain English summarizing the inbound critique
   - One bullet: `Discriminator experiment(s):` with nested 1–2 experiment items (same style as above)
   - One bullet: `Sources:` with hyperlinks (tweet mirror, talk, primary DOIs)
   - Mirroring rule: for every Outbound rivalry you add on page A → B, add a matching Inbound block on page B titled `### Inbound (from A ...)` with the same discriminator experiment link(s) and appropriate sources.

Style
- Keep sentences short and understandable for non‑experts.
- No labels like "Lay summary:" – just write plainly.
- Keep to 1–3 experiments per rivalry to avoid clutter.
- Avoid duplicative links (e.g., don’t repeat links to the rival page in bullets – the header is already linked).

Naming/Navigation
- Lidsky’s theory page is titled and linked as: `Pathogen Control (Peter Lidsky)`.
- Rival headers should be linked to their pages (e.g., `#### [Classic Models (Damage/AP/Disposable Soma)](classic_models.md)`).

Notes
- As we refine formatting for other sections (Evidence, Predictions, Proposed Experiments, Sources), add those conventions here so future contributors align immediately.

GitHub Pages Deployment (CI)
----------------------------

- We deploy via GitHub Actions to GitHub Pages on every push to `main`.
- Workflow: `.github/workflows/pages.yml` builds the site with `mkdocs build --strict` and publishes the `site/` artifact using `actions/deploy-pages`.
- Agent policy: do not push to `main` unless explicitly requested. Prefer pushing to a branch and (if needed) opening a PR; only after changes land on `main` will CI publish to Pages. Provide the final Pages URL after the `main` deploy completes.
- Repo settings: Pages → Build and deployment should be set to “GitHub Actions”. If this is not yet enabled, the agent should request access or note that the setting needs to be toggled once; after that, deploys are automatic.

Auto-Commit/Push Policy (Branch Default)
----------------------------------------

- After any content/config change that affects the site, the agent must:
  - Create a clear, concise commit on the current working branch (use conventional commits when obvious, e.g., `docs(theories): add Longevity Bottleneck page`).
  - Push immediately to that branch.
  - Only push/merge to `main` when explicitly requested (or when a PR is approved/merged).
- Post-push verification:
  - For branch pushes: report the branch and commit SHA (Pages will not update yet).
  - For `main`: poll the live Pages URL with a cache-buster (e.g., `?_cb=TIMESTAMP`) to confirm that the new content is visible.
  - Only claim Pages success after the expected content renders on the live page; otherwise, investigate and repeat build/verify and re-push if needed.
- Local preview is optional: a strict build can help catch errors, but do not start a local dev server.

Formatting – Questions Sections
-------------------------------

- Location/order: place the `## Questions` section after the main content blocks (e.g., after Conflicts). Within that section, always append new questions at the bottom. Do not reorder existing items unless explicitly requested by the user.
- Structure: each question uses a `###` heading (single sentence), followed by a concise answer (1–2 paragraphs). Include hyperlinks or popover footnotes for key sources when available.
- Consistency: keep tone plain and accessible; avoid duplicating material covered elsewhere on the page. Link out to experiments or related sections when helpful.

Template Reference (Levin)
-------------------------

- Use `Bioelectric / Morphogenetic Control (Levin)` as the reference template for theory pages, especially for the `## Questions` section.
- Footnotes/links: prefer popover footnotes using `<sup><a class="ref-pop" href="..." data-ref-url="..." data-ref-summary="...">†</a></sup>` placed directly after the relevant sentence. Avoid bare URLs in the prose.
- Keep answers short (1–2 paragraphs), with superscripted DOIs or stable links (talk pages, mirrors) and a brief `data-ref-summary` for reader context.
