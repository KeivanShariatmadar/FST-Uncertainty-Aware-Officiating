# Derived Evaluation Data

This directory now contains the first audited, de-identified evidence artifacts for the SSAC27 study.

## Released
- `annotation_candidate_records_deidentified.csv` — de-identified raw candidate-level annotation records, preserving the source candidate population and audit flags;
- `annotation_candidate_records_audited.csv` — canonical exact-deduplicated version used for candidate-population auditing;
- `SCHEMA.md` — target schemas for the independent ground-truth, frozen-prediction and matched-event evaluation layers.
- `audit_log.csv` — explicit exact-duplicate and source-bookkeeping decisions.
- `annotation_audit_summary.csv` — machine-readable audit totals.
- `annotation_category_counts.csv` — category distributions.
- `annotation_joint_patterns.csv` — joint annotation-pattern distribution.

The annotation release does **not** contain athlete names. It is an annotation/evidence audit artifact, not a substitute for an independently enumerated ground-truth event inventory.

## Key limitation
The candidate annotation table does not independently enumerate false negatives. It therefore does not, on its own, support recall or F1. Its human confidence field is also not FST model uncertainty.

See `../../evaluation/ANNOTATION_AUDIT.md` and `../../evaluation/EVIDENCE_AUDIT_PROTOCOL.md`.

## Planned evidence layers
The final evaluation package is designed around:
- `ground_truth_events.csv`;
- `fst_ssac_predictions.csv`;
- `matched_events.csv`;
- `audit_log.csv`.

These files will be populated only from verified source evidence. Synthetic or placeholder observations must not be used to support empirical claims.

## Reproducing the annotation audit

Run:

```bash
python evaluation/audit_candidate_annotations.py \
  data/derived/annotation_candidate_records_deidentified.csv \
  --out candidate_audit_results
```

The script regenerates audit summaries from the public de-identified source table. It does not infer recall/F1 or model uncertainty.
