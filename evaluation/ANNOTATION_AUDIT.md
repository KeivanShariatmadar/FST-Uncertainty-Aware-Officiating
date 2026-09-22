# Annotation Evidence Audit

## Status

This document records the audit of the championship-derived FST candidate-annotation table. It is an evidence-governance artifact, not a full model-performance claim.

The source table contains **546 candidate-level records across 74 recorded match IDs**. The raw labels contain **450 True Positive** and **96 False Positive** candidate validations. One exact repeated match/clip key was found; retaining one canonical occurrence yields **545 auditable candidate records (449 TP, 96 FP)**.

The corresponding canonical candidate-confirmation fraction is **82.39% (449/545)**. Treating the 73 canonical bout clusters as the dependence units, a delete-one-bout cluster jackknife gives SE = **0.00624** and an approximate normal 95% interval of **81.16%–83.61%**. This quantity must **not** be described as recall, F1, overall match-level accuracy, or an unbiased estimate of full-system performance. The table contains system-detected/selected candidate clips and does not independently enumerate missed true events (FN).

## Provenance classification

The current fields are treated as:

- `label` (True Positive / False Positive): human validation of whether a system-detected candidate is a valid head-kick event, consistent with the supplied annotation manual;
- `human_confidence`: human/reference confidence, not FST epistemic uncertainty;
- `difficulty`, `event_label`, `contact`, and `visibility`: human/contextual annotations;
- TP/FP/FN in the final SSAC event benchmark: derived only after independent ground-truth/model-output matching.

The annotation manual explicitly defines True Positive as the system correctly detecting a valid head kick and False Positive as the system detecting a head kick that is not a real head kick. This supports interpreting the current table as candidate-validation evidence. It does **not** establish that the table contains every system candidate from a prespecified population, so the 82.39% fraction remains conservatively labelled a candidate-confirmation rate pending sampling-protocol verification.

## Category distributions

Raw candidate records:

| Field | Category | Count |
|---|---|---:|
| label | True Positive | 450 |
| label | False Positive | 96 |
| human confidence | High | 294 |
| human confidence | Medium | 252 |
| difficulty | Easy | 172 |
| difficulty | Medium | 152 |
| difficulty | Hard | 222 |
| event | turning_head_kick | 293 |
| event | non_turning_head_kick | 157 |
| event | uncertain | 96 |
| contact | clear_contact | 300 |
| contact | light_contact | 150 |
| contact | uncertain | 96 |
| visibility | good | 172 |
| visibility | moderate | 152 |
| visibility | partial_occlusion | 222 |

The complete row-aligned text export supplied with the research materials verifies the visibility field one-to-one with all 546 candidate rows. Visibility is therefore now included in the public de-identified candidate tables.

## Structural regularity

The annotation table is highly patterned. The four most common six-field annotation combinations account for **535/546 (97.99%)** of all raw candidate rows:

| Joint annotation pattern | Count |
|---|---:|
| True Positive / High / Easy / turning / clear / good | 164 |
| True Positive / Medium / Medium / non-turning / light / moderate | 149 |
| True Positive / High / Hard / turning / clear / partial occlusion | 126 |
| False Positive / Medium / Hard / uncertain / uncertain / partial occlusion | 96 |
| True Positive / Medium / Easy / non-turning / clear / good | 7 |
| True Positive / High / Medium / turning / clear / moderate | 3 |
| True Positive / High / Easy / non-turning / light / good | 1 |

All **96/96** False Positive-labelled rows are **Medium confidence / Hard / uncertain event / uncertain contact / partial occlusion**. All 172 `good` and all 152 `moderate` visibility rows are TP-labelled; among 222 `partial_occlusion` rows, 126 are TP-labelled and 96 are FP-labelled.

This near-deterministic structure means ordinary association tests between these contextual fields and TP/FP would be circular or scientifically weak unless the annotation procedure establishes that each field was assigned independently of correctness. The contextual fields are retained because they describe evidence conditions, but they are not substitutes for a model-generated uncertainty signal.

## Identity and bookkeeping findings

The audit identified:

1. one exact duplicate match/clip key: `624-506 / clip_001.mp4`;
2. a source note stating that match `624-548` and `624-549` represent the same bout under two match identifiers;
3. a note stating that `624-546` does not exist immediately before records labelled `624-546`;
4. a later note stating that `624-531` does not exist despite earlier records for `624-531`;
5. a source note stating that there is no match `624-530`;
6. repeated heading typo `MATH` instead of `MATCH` in part of the 625-series section.

These issues are retained in `data/derived/audit_log.csv` rather than silently corrected. The public derived CSVs include `bout_cluster_id`, `bookkeeping_flag`, and canonical/exclusion fields.

## What this dataset supports now

The de-identified candidate table supports:

- transparent accounting of the annotated candidate population;
- descriptive TP/FP candidate-validation counts under the source selection process;
- the 82.39% canonical candidate-confirmation rate, with its denominator explicitly stated, plus the bout-cluster jackknife uncertainty interval;
- descriptive stratification by action type, contact, difficulty and verified visibility;
- annotation-quality/provenance auditing;
- sensitivity analysis to exact duplicate removal.

It does **not yet** support:

- recall or F1 (no independently enumerated FN population);
- an unbiased claim of overall FST event-detection accuracy;
- calibration or risk-coverage using human `High/Medium` confidence;
- claims that human difficulty/visibility labels are FST epistemic uncertainty;
- a causal claim that occlusion produces errors, because visibility and correctness annotations are structurally coupled in this table.

## Reproducibility

The raw de-identified table and exact-deduplicated canonical table are public. The audit can be regenerated with:

```bash
python evaluation/audit_candidate_annotations.py \
  data/derived/annotation_candidate_records_deidentified.csv \
  --out candidate_audit_results
```

Machine-readable totals and joint patterns are committed under `data/derived/`.

## Final SSAC evaluation gate

The manuscript-ready model benchmark requires an independently enumerated ground-truth event inventory and frozen FST/FST 2.0 predictions. Only after deterministic event matching will TP, FP, FN, precision, recall, F1 and selective risk/coverage be reported as full FST performance.

The current candidate annotations remain valuable because they expose real system-detected cases and difficult/occluded evidence, but they are not allowed to stand in for the missing independent event census or model uncertainty output.
