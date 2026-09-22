# Frozen Model Prediction Export Specification

## Goal
Create a model-output table that is independent of human/reference labels and sufficient for deterministic SSAC event matching and uncertainty analysis.

## Required fields
| Field | Meaning |
|---|---|
| `prediction_id` | Stable unique prediction/event ID |
| `match_id` | Match/bout identifier used by the evaluation set |
| `timestamp_s` | Event timestamp in seconds on the declared time base |
| `predicted_action_type` | Frozen FST action prediction |

## Strongly preferred fields
| Field | Meaning |
|---|---|
| `clip_name` | Source clip/video filename where applicable |
| `frame_index` | Event frame index |
| `event_start_s` | Start of model event window |
| `event_end_s` | End of model event window |
| `recommended_points` | Jury-facing scoring recommendation, if produced |
| `model_confidence` | Raw model confidence/reliability score with method documented |
| `model_uncertainty` | Numerical uncertainty value only if genuinely implemented |
| `uncertainty_method` | e.g. ensemble disagreement, credal width, interval score; exact implementation name |
| `defer_flag` | Model/system defer-to-human recommendation if implemented |
| `compute_latency_ms` | Machine compute latency under a declared timing boundary |
| `model_version` | Frozen model/weights identifier |
| `inference_config_id` | Frozen configuration identifier |

## Independence rule
The export must be generated without loading:
- human TP/FP candidate labels;
- final ground-truth event labels;
- SSAC matched-event outcomes.

Reference data may be used only after this prediction file is frozen.

## Time base
Document:
- original video FPS;
- whether timestamps are source-video time, clip-relative time, or wall-clock competition time;
- treatment of variable-frame-rate video;
- any clip offset relative to the original bout.

## Confidence/uncertainty
For each released score, state:
- mathematical/algorithmic origin;
- range;
- whether higher means more certain or more uncertain;
- whether calibrated;
- threshold(s) and how selected.

Do not transform a human annotation confidence field into model confidence.

## Completeness
Export **all** predictions satisfying the frozen inference configuration. Do not export only predictions later found to be correct.

## Version manifest
The prediction export should be accompanied by a machine-readable manifest containing:
- FST package/version;
- model/weights fingerprint;
- configuration fingerprint;
- runtime/dependency versions;
- inference date;
- evaluation split identifier;
- relevant hardware.

## Privacy
Do not include athlete names unless scientifically necessary and explicitly cleared for release. Match IDs and non-identifying event IDs are preferred.
