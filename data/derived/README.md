# Derived Evaluation Data

This directory now contains the first audited, de-identified evidence artifacts for the SSAC27 study.

## Released
- `annotation_candidate_records_deidentified.csv` — de-identified raw candidate-level annotation records, preserving the source candidate population and audit flags;
- `annotation_candidate_records_audited.csv` — canonical exact-deduplicated version used for candidate-population auditing;
- `SCHEMA.md` — target schemas for the independent ground-truth, frozen-prediction and matched-event evaluation layers.

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
