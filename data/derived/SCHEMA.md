# Derived Evaluation Artifact Schemas

These schemas define the intended auditable interface between source evidence, frozen FST/FST 2.0 inference, and SSAC statistical analysis. They do not contain empirical results.

## `ground_truth_events.csv`
Recommended fields:
- `evaluation_id`
- `match_id`
- `clip_id`
- `event_id`
- `event_time_start`
- `event_time_end`
- `athlete_role_or_id` (only when legally/research appropriate)
- `reference_event_present`
- `reference_action_class`
- `reference_contact`
- `reference_visibility`
- `reference_difficulty`
- `reference_ambiguity`
- `annotator_count`
- `adjudication_method`
- `source_provenance`
- `audit_status`

## `fst_ssac_predictions.csv`
Recommended fields:
- `evaluation_id`
- `match_id`
- `clip_id`
- `prediction_id`
- `prediction_time_start`
- `prediction_time_end`
- `predicted_action_class`
- `raw_model_score`
- `decision_threshold`
- `uncertainty_value`
- `uncertainty_definition`
- `model_version`
- `weights_or_model_id`
- `inference_config_id`
- `runtime_ms`

Do not replace numerical FST uncertainty with human High/Medium confidence annotations.

## `matched_events.csv`
Generated from independent ground truth and model predictions using the declared event-matching protocol. Recommended fields:
- `evaluation_id`
- `match_id`
- `reference_event_id`
- `prediction_id`
- `match_status` (`TP`, `FP`, `FN` as applicable)
- `temporal_offset_ms`
- `class_match`
- `matching_tolerance_ms`
- `uncertainty_value`
- contextual reference fields needed for stratified analysis

TP/FP/FN are derived outcomes in this artifact; they should not be copied uncritically from a working annotation sheet.

## `audit_log.csv`
Recommended fields:
- `source_record_id`
- `canonical_id`
- `issue_type`
- `issue_description`
- `action`
- `included_in_primary_analysis`
- `rationale`
- `reviewer`
- `date`

The raw source is never overwritten by this audit layer.
