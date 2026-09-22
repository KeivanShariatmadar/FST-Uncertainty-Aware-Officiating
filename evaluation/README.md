# Evaluation Framework

The SSAC evaluation treats FST.ai as human-in-the-loop decision support rather than autonomous officiating.

## Evaluation dimensions
1. **Decision performance** — performance against an independent expert/reference standard.
2. **Review latency** — time to reach/support a review decision under comparable baseline and assisted workflows.
3. **Human agreement and interaction** — agreement plus separately defined referee/user-study outcomes.
4. **Uncertainty-aware behavior** — whether insufficient-evidence cases can be identified and deferred.
5. **Interpretability/auditability** — whether evidence and recommendations remain traceable.

## Evidence discipline
See `EVIDENCE_AUDIT_PROTOCOL.md`, `ANNOTATION_AUDIT.md`, and `PUBLISHED_CLAIMS_AUDIT.md`.

Original evidence and source annotations are not destructively edited. Ground truth, frozen FST/FST 2.0 outputs, independent contextual annotations, and derived variables are kept separate. Human annotation confidence must not be represented as FST epistemic uncertainty.

The released candidate annotation table cannot by itself establish recall or F1 because missed true events are not independently enumerated.

## End-to-end reproducible path
0. Audit the existing archive split at bout level using `SPLIT_POLICY.md` and `validate_split.py`; freeze a split manifest.
1. Freeze `ground_truth_events.csv`.
2. Freeze `fst_ssac_predictions.csv`.
3. Match the two layers using `match_events.py` with an explicitly declared temporal tolerance and class rule.
4. Validate derived files with `validate_derived_data.py`.
5. Compute performance, cluster-bootstrap intervals, contextual strata, and risk–coverage output with `evaluate_predictions.py`.
6. Record every manuscript headline result in the evidence ledger.

Example:

```bash
pip install -r evaluation/requirements.txt

python evaluation/match_events.py \
  data/derived/ground_truth_events.csv \
  data/derived/fst_ssac_predictions.csv \
  --tolerance-s 0.5 \
  --class-mode exact \
  --output data/derived/matched_events.csv

python evaluation/validate_derived_data.py data/derived
python evaluation/evaluate_predictions.py data/derived/matched_events.csv --out results
```

The 0.5 s value above is an **example invocation**, not a preregistered final tolerance. The manuscript must state the selected tolerance and sensitivity analyses.

## Statistical analysis
See `STATISTICAL_ANALYSIS_PLAN.md`. Principal confidence intervals use bout/match-level cluster resampling where appropriate. Thresholds for selective-prediction headline results must not be optimized on the final test set.

## Automated smoke test
`audit_candidate_annotations.py` regenerates the released annotation audit from the de-identified candidate table.

`inspect_fst_package.py` inventories the private FST source ZIP locally without emitting source-code snippets; see `LOCAL_IMPLEMENTATION_AUDIT.md`.

`evaluation/tests/smoke_test.py` verifies basic exact-class and class-agnostic event matching plus metric accounting. A GitHub Actions workflow is included under `.github/workflows/reproducibility.yml`.

If repository Actions are disabled at the account/repository level, the same smoke test can be run locally with Python 3.11+.

## Prohibited shortcuts
- Do not infer ground truth from FST predictions.
- Do not manufacture FN observations.
- Do not relabel human confidence as epistemic uncertainty.
- Do not silently remove difficult or contradictory records.
- Do not use an unreconciled public-paper number as a new SSAC empirical result.

## Selective prediction

See `SELECTIVE_PREDICTION_PROTOCOL.md` for the distinction between candidate-level risk–coverage and the preferred IVR decision-level defer-to-human analysis. Candidate-only uncertainty cannot account for undetected reference events unless the implementation produces a score on the corresponding eligible decision unit.
