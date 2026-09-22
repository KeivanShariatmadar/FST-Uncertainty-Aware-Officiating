# Annotation Evidence Audit

## Status

This document records the current audit of the championship-derived FST candidate-annotation table. It is an evidence-governance artifact, not a model-performance claim.

The source table was parsed as **546 candidate-level records across 74 recorded match IDs**. The raw labels contain **450 True Positive** and **96 False Positive** candidate validations. One exact repeated match/clip key was found; retaining one canonical occurrence yields **545 auditable candidate records (449 TP, 96 FP)**.

The corresponding canonical candidate-validation positive fraction is **82.39%**. This quantity must **not** be described as recall, F1, overall match-level accuracy, or an unbiased estimate of full-system performance. The table contains FST-proposed/selected candidate clips and does not independently enumerate missed true events (FN).

## Provenance classification

The current fields are treated as:

- `label` (True Positive / False Positive): human validation of a candidate event, pending confirmation of the original annotation procedure;
- `human_confidence`: human/reference confidence, not FST epistemic uncertainty;
- `difficulty`, `event_label`, and `contact`: contextual/reference annotations;
- TP/FP/FN used in the final SSAC evaluation: derived only after independent ground-truth/model-output matching.

No human confidence or contextual annotation is relabelled as model uncertainty.

## Structural regularity

The annotation table is highly patterned. The four most common joint annotation combinations account for **535/546 (97.99%)** of all raw candidate rows:

| Joint annotation pattern | Count |
|---|---:|
| True Positive / High / Easy / turning_head_kick / clear_contact | 164 |
| True Positive / Medium / Medium / non_turning_head_kick / light_contact | 149 |
| True Positive / High / Hard / turning_head_kick / clear_contact | 126 |
| False Positive / Medium / Hard / uncertain / uncertain | 96 |
| True Positive / Medium / Easy / non_turning_head_kick / clear_contact | 7 |
| True Positive / High / Medium / turning_head_kick / clear_contact | 3 |
| True Positive / High / Easy / non_turning_head_kick / light_contact | 1 |

All **96/96** currently labelled False Positive rows have the combination **Medium human confidence / Hard / uncertain event / uncertain contact**. Likewise, the table contains **96** `uncertain` event labels and **96** `uncertain` contact labels, numerically matching the FP count.

This near-deterministic structure means association tests between these fields and TP/FP would be circular or uninformative unless the annotation procedure establishes that the contextual variables were assigned independently of correctness. They can still be useful as descriptive evidence-condition metadata.

## Identity and bookkeeping findings

The audit identified:

1. one exact duplicate match/clip key: `624-506 / clip_001.mp4`;
2. a source note stating that match `624-548` and `624-549` represent the same bout under two match identifiers;
3. a note stating that `624-546` does not exist immediately before records labelled `624-546`;
4. a later note stating that `624-531` does not exist despite earlier records for `624-531`;
5. repeated heading typo `MATH` instead of `MATCH` in part of the 625-series section.

These issues are retained as audit flags rather than silently corrected. The derived CSV includes `bout_cluster_id`, `bookkeeping_flag`, and canonical/exclusion fields.

## Visibility layer

The separate visibility/notes section contains repeated `good`, `moderate`, and `partial_occlusion` entries. A simple token count does not map exactly one-to-one to the 546 candidate records, so visibility has **not** been merged into the public candidate table by positional assumption. It should be joined only after record-level identity is verified.

## What this dataset supports now

The de-identified candidate table can support:

- transparent accounting of the annotated candidate population;
- descriptive TP/FP candidate-validation counts under the original selection process;
- annotation-quality and provenance auditing;
- sensitivity analysis to exact duplicate removal;
- construction of a reference layer once the original annotation procedure is confirmed.

It does **not yet** support:

- recall or F1 (no independently enumerated FN population);
- an unbiased claim of overall FST accuracy;
- calibration or risk-coverage using human `High/Medium` confidence;
- claims about FST epistemic uncertainty.

## Final SSAC evaluation gate

The manuscript-ready benchmark requires an independent ground-truth event inventory and frozen FST/FST 2.0 predictions. Only after deterministic event matching will TP, FP, FN, precision, recall, F1 and selective risk/coverage be reported as FST performance.

The raw de-identified table is preserved separately from the canonical exact-deduplicated table so that every exclusion is auditable.
