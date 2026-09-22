# Derived Annotation Data Provenance

## Source

The public candidate-annotation tables were derived from the research working file:

- source filename: `annotations.txt`;
- source size in the research workspace: **101,687 bytes**;
- structure: tab-separated text;
- source columns: `match_id, teams, clip_name, player, label, confidence, difficulty, event_label, contact, visibility, notes`.

The source file is not copied verbatim into the public repository because it contains athlete/team names and free-text notes.

## Transformation

The public transformation is intentionally minimal:

### Retained
- match identifier;
- source clip filename;
- TP/FP candidate-validation label;
- human annotation confidence;
- difficulty;
- event label;
- contact category;
- row-aligned visibility category.

### Removed
- team/opponent names;
- player/athlete names;
- free-text notes.

The free-text notes are excluded because they are unnecessary for the current statistical audit and may contain identifying names.

### Added audit fields
- repository-local `record_id`;
- `bout_cluster_id`;
- exact-duplicate flag;
- canonical-record flag;
- source-bookkeeping flag;
- audit inclusion state;
- provenance-role label.

No synthetic candidate observations are added.

## Record accounting

The source contains:
- **546** candidate rows;
- **74** recorded match IDs;
- **450** TP-labelled candidates;
- **96** FP-labelled candidates.

One exact repeated match+clip occurrence (`624-506 / clip_001.mp4`) yields:
- **545** canonical candidate rows;
- **449** TP-labelled candidates;
- **96** FP-labelled candidates.

A source note explicitly links match IDs `624-548` and `624-549` to the same bout; these rows are retained but share a common `bout_cluster_id`.

Other contradictory source notes are preserved as audit flags rather than silently repaired.

## Visibility verification

Unlike the earlier PDF-rendered extraction, the tab-separated source file provides a row-aligned visibility value for every candidate record:
- `good`: 172 raw rows;
- `moderate`: 152 raw rows;
- `partial_occlusion`: 222 raw rows.

Visibility is therefore included in the current public derived tables.

## Reproducibility

The released data transformation can be independently checked from the public tables using `evaluation/audit_candidate_annotations.py`. Because the original identifying source is not public, re-deriving the de-identification step itself requires controlled access to the source file.

The public repository does not assert that these candidate rows constitute a complete event census. In particular, no missing true-event/FN population is inferred from this source.

## Public artifacts

- `annotation_candidate_records_deidentified.csv` — all 546 de-identified source candidate rows;
- `annotation_candidate_records_audited.csv` — 545 canonical rows after exact duplicate removal;
- `audit_log.csv` — explicit audit decisions;
- `annotation_audit_summary.csv` — machine-readable totals;
- `annotation_category_counts.csv` — raw category distributions;
- `annotation_joint_patterns.csv` — joint structural patterns;
- `annotation_stratified_confirmation.csv` — canonical descriptive strata;
- `INTEGRITY.md` — committed-object integrity snapshot.
