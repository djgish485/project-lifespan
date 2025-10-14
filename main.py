from __future__ import annotations

from typing import Any, Dict

def define_env(env):
    """Hook for mkdocs-macros-plugin."""

    site_cfg = env.conf or {}
    extra = site_cfg.get('extra', {})
    criteria = extra.get('popper', {}).get('criteria', [])
    weights = {c['id']: float(c.get('weight', 1)) for c in criteria}
    labels = {c['id']: c.get('label', c['id'].title()) for c in criteria}

    def compute_popper_score(meta: Dict[str, Any]) -> Dict[str, Any]:
        pop = (meta or {}).get('popper', {})
        scores = pop.get('scores', {})
        # Normalize and clamp 0-5
        clamped = {}
        for cid in weights:
            val = float(scores.get(cid, 0))
            clamped[cid] = max(0.0, min(5.0, val))
        total_weight = sum(weights.values()) or 1.0
        weighted_sum = sum(clamped[cid] * weights[cid] for cid in weights)
        # Scale to 0-100
        score = round((weighted_sum / (5.0 * total_weight)) * 100.0, 1)
        return {
            'score': score,
            'scores': clamped,
            'labels': labels,
            'weights': weights,
        }

    @env.macro
    def popper_card(meta: Dict[str, Any] | None = None) -> str:
        """Render a compact Popper Score card for the current page."""
        page = env.page
        meta = meta or getattr(page, 'meta', {})
        result = compute_popper_score(meta)
        score = result['score']
        # Build simple HTML block; theme CSS can style `.popper-card`.
        items = []
        for cid, val in result['scores'].items():
            label = result['labels'][cid]
            items.append(f"<li><span>{label}</span> <strong>{val:.1f}</strong></li>")
        items_html = "\n".join(items)
        return f'''
<div class="popper-card">
  <div class="popper-card__header">Popper Score</div>
  <div class="popper-card__score">{score}</div>
  <details class="popper-card__details"><summary>Breakdown</summary>
    <ul class="popper-card__list">
      {items_html}
    </ul>
  </details>
</div>
'''

    @env.macro
    def claim(id: str, text: str, prediction: str | None = None) -> str:
        """Render a claim box with optional measurable prediction."""
        pred_html = f"<div class=\"claim__prediction\"><strong>Prediction:</strong> {prediction}</div>" if prediction else ""
        return f'''<div class="claim" id="{id}"><div class="claim__label">Claim</div><div class="claim__text">{text}</div>{pred_html}</div>'''

    @env.macro
    def experiment_box(title: str, hypothesis: str, prediction: str, endpoints: str, controls: str, cost: str, time: str) -> str:
        return f'''
<div class="experiment">
  <div class="experiment__title">{title}</div>
  <div class="experiment__body">
    <p><strong>Hypothesis:</strong> {hypothesis}</p>
    <p><strong>Prediction:</strong> {prediction}</p>
    <p><strong>Endpoints:</strong> {endpoints}</p>
    <p><strong>Controls:</strong> {controls}</p>
    <p><strong>Cost:</strong> {cost}</p>
    <p><strong>Time:</strong> {time}</p>
  </div>
</div>
'''

