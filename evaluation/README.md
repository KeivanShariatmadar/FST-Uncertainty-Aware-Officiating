# Evaluation Framework

The SSAC evaluation treats FST.ai as human-in-the-loop decision support rather than autonomous officiating.

The principal evaluation dimensions are:

1. **Decision performance** — performance against a declared expert/reference standard.
2. **Review latency** — time required to reach or support a review decision under a defined baseline and assisted workflow.
3. **Human agreement and interaction** — agreement with expert decisions and, where separately measured, referee/user assessment of AI-supported decisions.
4. **Uncertainty-aware behavior** — whether ambiguous or insufficient-evidence cases can be identified and deferred rather than forced into unsupported binary decisions.
5. **Interpretability/auditability** — whether the evidence presented to officials can be inspected and associated with the recommendation.

Any full-paper table will state the evaluation population, denominator, baseline, and aggregation method next to the reported metric.

## Evidence discipline

See `EVIDENCE_AUDIT_PROTOCOL.md`. Original championship evidence and source annotations are not destructively edited. Ground truth, frozen FST/FST 2.0 outputs, independent contextual annotations, and derived variables are kept conceptually separate. Human annotation confidence must not be represented as FST epistemic uncertainty.

The current working annotations contain data-quality/provenance issues that must be resolved in the audit layer before headline metrics are calculated. Recall and F1 are not reported unless false negatives are observable from an independently enumerated reference-event population.

## Derived tables

The canonical schemas are documented in `../data/derived/SCHEMA.md`:

- `ground_truth_events.csv`
- `fst_ssac_predictions.csv`
- `matched_events.csv`
- `audit_log.csv`

The operational FST source code and production weights are not required in the public repository. Frozen model outputs used for reported research results should be released where rights and confidentiality permit.

## Reproducible scripts

`validate_derived_data.py` performs fail-fast structural checks before analysis.

`evaluate_predictions.py` consumes the audited `matched_events.csv` and produces:

- overall TP/FP/FN counts, precision, recall and F1 where supported;
- bout/match-cluster bootstrap confidence intervals;
- stratified tables for available action type, visibility, contact quality, difficulty and reference ambiguity fields; and
- risk–coverage output when a genuine numerical model uncertainty or confidence field is available.

Example:

```bash
python evaluation/validate_derived_data.py data/derived
python evaluation/evaluate_predictions.py data/derived/matched_events.csv --out results
```

No script should infer ground truth from model predictions or manufacture missing FN observations. Thresholds used for headline selective-prediction results must not be selected on the final test population.
