# SSAC27 Abstract Claim Map

This file maps the evidence-safe abstract draft to the current repository evidence.

| Abstract statement | Evidence status | Supporting artifact |
|---|---|---|
| 546 annotated candidate clips | Verified from parsed annotation source | `data/derived/annotation_candidate_records_deidentified.csv`; `evaluation/ANNOTATION_AUDIT.md` |
| 74 recorded match identifiers | Verified from parsed annotation source | annotation audit |
| one exact duplicate match/clip record | Verified | annotation audit and duplicate flag in released CSV |
| documented two-ID same-bout case | Verified source bookkeeping note | audit flags / `bout_cluster_id` |
| 545 canonical candidate records | Verified after exact deduplication | `annotation_candidate_records_audited.csv` |
| 449 human-validated true candidates; 96 false candidates | Verified from current source annotation table | audited CSV |
| 82.39% candidate-confirmation rate | Reproducible arithmetic: 449/545 | audited CSV; **not** labelled recall/F1/overall accuracy |
| 535/546 (97.99%) in four dominant joint patterns | Verified annotation-structure audit | `evaluation/ANNOTATION_AUDIT.md` |
| all 96 FP-labelled rows share Medium/Hard/uncertain/uncertain pattern | Verified | annotation audit |
| human annotation confidence is not model uncertainty | Methodological/provenance rule | evidence-audit protocol |
| current table cannot establish recall/F1 | Verified limitation: FN not independently enumerated | evidence-audit protocol / metric definitions |
| risk–coverage / defer-to-human evaluation | Registered evaluation method, **not yet an empirical result** | `evaluation/evaluate_predictions.py` |

## Excluded headline claims
The draft intentionally excludes the public FST.ai 2.0 headline figures (e.g. review-time reduction and referee trust) until their underlying populations and calculations are reconciled. See `evaluation/PUBLISHED_CLAIMS_AUDIT.md`.

## Word count
The draft contains **375 words including title and section headings as stored here**. Before upload, recount in the final exported file because formatting/tokenization may differ slightly across software.
