# SSAC27 Abstract Claim Map

This file maps the current evidence-safe abstract draft to public/reproducible evidence.

| Abstract statement | Evidence status | Supporting artifact |
|---|---|---|
| 546 annotated candidate clips | Verified | `data/derived/annotation_candidate_records_deidentified.csv` |
| 74 recorded match identifiers | Verified | annotation audit / public candidate table |
| True/False Positive semantics describe system-detected candidates | Verified from supplied annotation manual | `evaluation/ANNOTATION_AUDIT.md` |
| human confidence, difficulty, action, contact and row-aligned visibility available | Verified | public candidate table / `annotation_category_counts.csv` |
| one exact duplicate match+clip occurrence | Verified | `audit_log.csv` / duplicate flags |
| one documented two-ID same-bout case | Verified | `audit_log.csv` / `bout_cluster_id` |
| 545 canonical records | Verified | `annotation_candidate_records_audited.csv` |
| 449 TP-labelled and 96 FP-labelled canonical candidates | Verified | audited CSV |
| 82.39% candidate-confirmation rate | Reproducible: 449/545 | audited CSV; deliberately not labelled recall/F1/overall accuracy |
| bout-cluster jackknife 95% CI 81.16%–83.61% | Reproducible from 73 canonical bout clusters | `audit_candidate_annotations.py`; `annotation_audit_summary.csv` |
| 535/546 (97.99%) in four dominant joint patterns | Verified | `annotation_joint_patterns.csv` |
| all 96 FP-labelled candidates are Medium/Hard/uncertain/uncertain/partial-occlusion | Verified | public candidate table / annotation audit |
| 222 partial-occlusion rows = 126 TP-labelled + 96 FP-labelled | Verified | public candidate table / annotation audit |
| human confidence/visibility are not model epistemic uncertainty | Provenance/methodological rule | `EVIDENCE_AUDIT_PROTOCOL.md` |
| current candidate table cannot establish recall/F1 | Verified limitation: FN not independently enumerated | evidence protocol / metric definitions |
| decision-to-defer / risk-coverage is the planned FST uncertainty evaluation | Registered method, **not yet an empirical result** | `STATISTICAL_ANALYSIS_PLAN.md`; `evaluate_predictions.py` |

## Excluded headline claims
The draft intentionally excludes unreconciled prior-public FST.ai 2.0 headline figures such as the 85% review-time reduction and 93% referee trust until their underlying populations/calculations are reconciled. See `evaluation/PUBLISHED_CLAIMS_AUDIT.md` and `evaluation/evidence_ledger.csv`.

## Word count
The current draft contains **381 words including title and section headings as stored in Markdown**, below the SSAC27 limit of fewer than 500 words. Recount after the final PDF/DOC export because software tokenization and visible formatting can differ.
