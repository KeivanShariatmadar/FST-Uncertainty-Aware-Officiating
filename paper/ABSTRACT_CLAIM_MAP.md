# SSAC27 Final Polished Abstract Claim Map

This file maps the authoritative abstract in 'SSAC27_ABSTRACT_FINAL.md' to public/reproducible evidence.

| Abstract statement | Evidence status | Supporting artifact |
|---|---|---|
| 546 FST candidate clips | Verified | 'data/derived/annotation_candidate_records_deidentified.csv' |
| 74 recorded match identifiers | Verified | public candidate table / annotation audit |
| TP/FP semantics are human validation of system-detected candidates | Verified from supplied annotation manual | 'evaluation/ANNOTATION_AUDIT.md' |
| human confidence, difficulty, kick type, contact and row-aligned visibility available | Verified | public candidate table / category counts |
| one exact duplicate match/clip entry excluded | Verified | 'data/derived/audit_log.csv' |
| documented two-ID same-bout case treated as one clustering unit | Verified | audit log / 'bout_cluster_id' |
| 545 canonical candidate records | Verified | 'annotation_candidate_records_audited.csv' |
| 449 TP-labelled and 96 FP-labelled canonical candidates | Verified | audited CSV |
| 82.39% candidate-confirmation rate | Reproducible: 449/545 | deliberately not called recall/F1/overall accuracy |
| bout-cluster jackknife 95% CI 81.16%–83.61% | Reproducible from 73 canonical bout clusters | 'audit_candidate_annotations.py'; 'annotation_audit_summary.csv' |
| 535/546 (97.99%) in four repeated joint annotation patterns | Verified | 'annotation_joint_patterns.csv' |
| 222 partially occluded candidates: 126 TP-labelled + 96 FP-labelled | Verified | audited/public candidate data |
| 56.76% descriptive candidate-confirmation among partial-occlusion candidates | Reproducible: 126/222 | descriptive only; fields are structurally coupled |
| all 96 FP-labelled candidates share Medium/Hard/uncertain-event/uncertain-contact/partial-occlusion pattern | Verified | public candidate table / joint-pattern audit |
| structural coupling prevents treating human fields as independent uncertainty calibration | Methodological inference directly supported by joint pattern | 'evaluation/ANNOTATION_AUDIT.md' |
| current candidate table cannot establish recall/F1 | Verified limitation: FN not independently enumerated | evidence protocol / metric definitions |
| future FST uncertainty evaluation must use model-generated numerical uncertainty and risk-coverage | Registered method, not current empirical result | 'STATISTICAL_ANALYSIS_PLAN.md'; 'FROZEN_MODEL_EXPORT_SPEC.md' |

## Excluded headline claims

The final abstract intentionally excludes unreconciled prior-public FST.ai 2.0 figures such as the 85% decision-review-time reduction, 93% referee trust, and approximately 92.7–92.8% accuracy descriptions. Those claims remain tracked in 'evaluation/PUBLISHED_CLAIMS_AUDIT.md' and 'evaluation/evidence_ledger.csv' until their underlying observations, denominators and definitions are reconstructed.

## Word count

'SSAC27_ABSTRACT_FINAL.md' contains **362 whitespace-delimited words including the title and section headings**, below the SSAC27 limit of fewer than 500 words. The final online form should be recounted after copy/paste because platform tokenization may differ.
