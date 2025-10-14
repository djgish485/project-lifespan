Project Lifespan – Agent Notes
==============================

These notes capture working conventions and operational SOPs for agents contributing to this repository. Keep this file up to date as we standardize more sections and flows.

Remote Verification SOP (No Local Serve)
---------------------------------------

We do not run a local `mkdocs serve` in this repo. Always verify using the live GitHub Pages site.

1) Optional: strict build locally to catch issues early
   - `source .venv/bin/activate`
   - `mkdocs build --strict`

2) Commit and push changes to `main` (CI builds + deploys Pages)

3) Verify on GitHub Pages with a cache‑buster
   - Example: `curl -sSf "http://dangish.net/project-lifespan/?_cb=TIMESTAMP"`
   - Confirm expected new text renders on the target page(s).

Notes
- Do not keep any local dev servers running.
- If a stale local server is suspected, kill any `mkdocs serve` processes and delete `.mkdocs*.pid`, but do not start a new one.

Service Restart SOP (MkDocs dev server)
---------------------------------------

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

- The agent executes the full SOP on behalf of the user. Do not provide command instructions for the user to run; perform the actions directly and return verified links.
- After edits, always run a strict build, restart the server cleanly, and verify the exact page content with `curl` (e.g., confirm new sections or text). Use a cache‑buster query parameter (like `?_cb=TIMESTAMP`) to avoid browser cache artifacts when checking.
- If a stale or parallel server is suspected, kill any `mkdocs serve` process and the listener on port 8000 before starting a fresh serve, then confirm with `curl`.
- Only report success after the expected content is visible on the live page; otherwise, repeat the SOP until the content is correct.
- Default posture: whenever content changes, assume a full SOP run (build → kill stale → serve → verify) is required before handing back URLs.

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
- Agent policy: do not ask the user to run deploy commands; commit changes and rely on CI to publish. Provide the final Pages URL after CI completes.
- Repo settings: Pages → Build and deployment should be set to “GitHub Actions”. If this is not yet enabled, the agent should request access or note that the setting needs to be toggled once; after that, deploys are automatic.

Auto-Commit/Push Policy (Always)
---------------------------------

- After any content/config change that affects the site, the agent must:
  - Create a clear, concise commit on `main` (use conventional commits when obvious, e.g., `docs(theories): add Longevity Bottleneck page`).
  - Push immediately to `main` to trigger the Pages workflow.
  - Do not pause for manual approval unless repository protections prevent pushing; if blocked, request the needed permission.
- Post-push verification:
  - Poll the live Pages URL with a cache-buster (e.g., `?_cb=TIMESTAMP`) to confirm that the new content is visible.
  - Only return success after the expected content renders on the live page; otherwise, investigate and repeat build/serve/verify locally and re-push if needed.
- Local preview is optional: a strict build can help catch errors, but do not start a local dev server.

Formatting – Questions Sections
-------------------------------

- Location/order: place the `## Questions` section after the main content blocks (e.g., after Conflicts). Within that section, always append new questions at the bottom. Do not reorder existing items unless explicitly requested by the user.
- Structure: each question uses a `###` heading (single sentence), followed by a concise answer (1–2 paragraphs). Include hyperlinks or popover footnotes for key sources when available.
- Consistency: keep tone plain and accessible; avoid duplicating material covered elsewhere on the page. Link out to experiments or related sections when helpful.
