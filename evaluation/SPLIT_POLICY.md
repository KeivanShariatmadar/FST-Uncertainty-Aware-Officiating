# Benchmark Split and Leakage Policy

## Unit of separation

The FST SSAC benchmark must be separated at the **bout/match level**, not by randomly assigning individual clips from the same bout to different partitions.

Clips from one bout share athletes, camera geometry, lighting, venue context, temporal continuity and annotation conventions. A clip-level random split would therefore create optimistic dependence between training/development and evaluation data.

## Minimum rules

1. All clips/events associated with one canonical `bout_cluster_id` belong to exactly one split.
2. The linked source IDs `624-548` and `624-549` are treated as one bout for splitting.
3. Exact duplicate clips/records cannot appear in more than one split.
4. Model thresholds, uncertainty thresholds and temporal-matching design choices are fixed without optimizing on the final test split.
5. The final test split is not used for model training, calibration, threshold selection or manual error-driven tuning.
6. Any use of the current `train/test/val` archive organization must first be audited at bout level to confirm that these rules hold.

## Athlete leakage

The same athlete may appear in multiple bouts. Where athlete identity is available in the controlled source data, report whether athletes overlap across splits.

Two evaluation regimes can be informative:

- **bout-held-out:** no bout appears across splits; athlete overlap may remain;
- **athlete-held-out sensitivity analysis:** where sample size permits, no athlete represented in the final test population appears in training/development.

The latter tests generalization to unseen athletes but may be too restrictive for the available sample. It is a sensitivity analysis rather than an automatic primary split.

## Competition/day/site shift

If the source archive contains multiple competition days, courts, venues or camera configurations, preserve those identifiers in the controlled provenance layer. Where sample size permits, report performance under a held-out day/court/site condition to test distribution shift.

## Annotation leakage

Human contextual fields such as `difficulty`, `visibility`, `contact` and `human_confidence` must not be supplied to the FST inference pipeline unless they are genuine model inputs available at runtime. They are evaluation metadata.

TP/FP labels and independent ground-truth labels are never model inputs.

## Split manifest

Before the final benchmark run, create a machine-readable split manifest with:

- `evaluation_id`;
- `match_id`;
- `bout_cluster_id`;
- `split` (train/validation/test);
- optional controlled-source athlete IDs;
- competition/day/court/site identifiers where available;
- split-assignment rationale/version.

Hash/freeze this manifest before final test inference.

## Reporting

The paper should report the number of bouts, clips/events and, where possible, unique athletes in each split. If the existing archive partitions fail the bout-level leakage check, they should be rebuilt before headline model-performance results are produced.
