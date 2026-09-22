# Data Dictionary

This dictionary distinguishes the **currently released candidate-annotation audit data** from the **target independent event benchmark** used for manuscript-ready model evaluation.

## Released candidate-annotation audit tables

Files:
- `data/derived/annotation_candidate_records_deidentified.csv`
- `data/derived/annotation_candidate_records_audited.csv`

| Field | Meaning |
|---|---|
| `record_id` | Repository-local non-identifying annotation record ID |
| `match_id` | Source match identifier retained for provenance |
| `bout_cluster_id` | Cluster identifier used when source bookkeeping indicates that multiple match IDs refer to one bout |
| `clip_name` | Source clip filename; athlete names are not included |
| `label` | Human candidate-validation label: True Positive or False Positive |
| `human_confidence` | Human/reference annotation confidence; **not FST model uncertainty** |
| `difficulty` | Human/contextual difficulty annotation |
| `event_label` | Human/contextual event label (turning head kick, non-turning head kick, uncertain) |
| `contact` | Human/contextual contact annotation |
| `duplicate_key` | Whether the match+clip key occurs more than once in the raw source |
| `canonical_record` | Whether this row is the retained canonical occurrence of the match+clip key |
| `bookkeeping_flag` | Source identity/bookkeeping issue identified by the audit |
| `analysis_inclusion` | Candidate-audit inclusion/exclusion state |
| `provenance_role` | Explicit statement that these are human candidate-validation/context fields |

The audited file removes only the one exact repeated match+clip occurrence. Other identity issues are flagged rather than silently rewritten.

## Target independent ground-truth table

Planned file: `ground_truth_events.csv`

Required core fields:
- `event_id`
- `match_id`
- `timestamp_s`
- `action_type`

Preferred contextual fields where independently annotated:
- `bout_cluster_id`
- `visibility`
- `contact_quality`
- `difficulty`
- `reference_ambiguity`
- adjudicator/provenance metadata in de-identified form.

## Target frozen-prediction table

Planned file: `fst_ssac_predictions.csv`

Required core fields:
- `prediction_id`
- `match_id`
- `timestamp_s`
- `predicted_action_type`

Preferred model fields:
- `model_confidence`
- `model_uncertainty`
- `model_version`
- `inference_config_id`
- scoring/recommendation output where releasable.

A model confidence or uncertainty field must originate from the frozen implementation, not from human annotation.

## Matched-event table

Planned/generated file: `matched_events.csv`

Produced only after independent ground truth and predictions are frozen. Key fields include:
- reference/prediction identifiers;
- `outcome` = TP, FP or FN;
- temporal localization error;
- reference and predicted action classes;
- model uncertainty/confidence;
- available contextual evidence fields.

TN is included only if a defensible negative evaluation unit is explicitly defined.

## Missing values
Empty values mean unavailable/not applicable. They must not be silently imputed for headline analysis.

## Units
All time fields ending in `_s` are seconds. Model confidence/uncertainty units must be documented with the implementation/export procedure because a numeric score is not assumed to be calibrated probability.
