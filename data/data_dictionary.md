# Planned Data Dictionary

This schema is provisional until the evidence audit is complete. It defines the preferred structure for releasable derived evaluation records without asserting that every field can or will be released.

| Field | Meaning | Release condition |
|---|---|---|
| `record_id` | Non-identifying research record identifier | Release if non-identifying |
| `evaluation_unit` | Action, clip, review, bout, or other declared unit | Required |
| `action_class_reference` | Expert/reference action label | Rights/provenance cleared |
| `action_class_model` | Model-predicted action label | Rights/provenance cleared |
| `reference_decision` | Expert/officiating reference decision | De-identified and cleared |
| `model_recommendation` | AI decision-support output | Cleared |
| `uncertainty_measure` | Declared uncertainty/confidence quantity | Method documented |
| `baseline_review_time_s` | Baseline review duration in seconds | Measurement provenance verified |
| `assisted_review_time_s` | AI-assisted review duration in seconds | Measurement provenance verified |
| `agreement_indicator` | Agreement under the declared definition | Derivable from cleared labels |
| `study_split` | Evaluation partition or study subset | If applicable |

A final data dictionary will state units, admissible values, missing-value conventions, aggregation rules, and provenance for every released column.
