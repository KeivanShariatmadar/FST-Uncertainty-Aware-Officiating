# FST: Uncertainty-Aware AI-Assisted Officiating in Competitive Taekwondo

Public research package for the **SSAC27** submission:

**When Should AI Defer? Uncertainty-Aware Video Review for Human-in-the-Loop Officiating in Competitive Taekwondo**

**Authors:** Keivan Shariatmadar¹ · Ahmad Osman¹ · Ramin Rey²  
¹ htw saar – University of Applied Sciences, Saarbrücken, Germany  
² Austrian Taekwondo Federation (AUT), Austria

## Research question

FST.ai studies human-in-the-loop AI for difficult video-review decisions in competitive Taekwondo. The SSAC study asks a narrower question than the broader FST ecosystem:

> When visual evidence is incomplete or ambiguous, can an AI review system provide useful evidence while identifying the cases that should remain with the referee/jury?

This repository is restricted to the **FST.ai / FST.ai 2.0 officiating research line**. APEX, Digital TA, WT-SCIP/SCIP, SILs and other projects are out of scope.

## Public evidence at a glance

The current open candidate-annotation audit contains:

| Quantity | Audited value |
|---|---:|
| Raw candidate records | 546 |
| Recorded match IDs | 74 |
| Exact duplicate match+clip keys | 1 |
| Canonical candidate records | 545 |
| TP-labelled canonical candidates | 449 |
| FP-labelled canonical candidates | 96 |
| Canonical candidate-confirmation rate | 82.39% |
| Good visibility (raw) | 172 |
| Moderate visibility (raw) | 152 |
| Partial occlusion (raw) | 222 |
| Rows in four dominant joint annotation patterns | 535/546 (97.99%) |

**Interpretation boundary:** 82.39% is a descriptive candidate-confirmation fraction for the released selected candidate population. It is **not** reported as recall, F1, overall match accuracy, or a complete event-level FST performance estimate because the current candidate table does not independently enumerate false negatives.

The audit also shows that all 96 FP-labelled raw candidates share the same Medium-confidence / Hard / uncertain-event / uncertain-contact / partial-occlusion annotation pattern. Human confidence/difficulty/visibility are therefore treated as contextual reference annotations, **not** as FST model epistemic uncertainty.

## Reproduce the public audit

~~~bash
pip install -r evaluation/requirements.txt

python evaluation/audit_candidate_annotations.py \
  data/derived/annotation_candidate_records_deidentified.csv \
  --out candidate_audit_results
~~~

For the final independent event-level benchmark:

~~~bash
python evaluation/match_events.py \
  data/derived/ground_truth_events.csv \
  data/derived/fst_ssac_predictions.csv \
  --tolerance-s <declared_tolerance> \
  --class-mode exact \
  --output data/derived/matched_events.csv

python evaluation/validate_derived_data.py data/derived
python evaluation/evaluate_predictions.py data/derived/matched_events.csv --out results
~~~

The ground-truth and frozen-prediction files are intentionally not fabricated as placeholders. They will be released only when generated from verified source evidence.

## Human-in-the-loop principle

FST.ai is decision support. AI outputs are evidence/recommendations for authorized human officials; they are not autonomous competition decisions. Ambiguous or insufficient-evidence cases remain subject to human adjudication.

The planned FST 2.0 uncertainty analysis therefore focuses on **selective prediction / decision-to-defer** rather than forcing a binary answer in every case.

## Evidence discipline

Every quantitative claim is classified in `evaluation/evidence_ledger.csv`.

- Verified public candidate-audit results are linked to released data.
- Prior-public FST/FST 2.0 headline numbers that have not yet been independently reconstructed are quarantined in `evaluation/PUBLISHED_CLAIMS_AUDIT.md`.
- Human annotation confidence is never relabelled as model uncertainty.
- Recall/F1 are not reported until false negatives are independently observable.
- Bout/match clustering is used to avoid treating correlated clips as IID observations.

## Repository map

- `PROJECT_STATE.md` — authoritative title, files, evidence status, claim boundaries and remaining benchmark work
- `DATA_STATEMENT.md` — data provenance, release status and rights constraints
- `REPRODUCIBILITY.md` — what can currently be reproduced
- `IP_AND_LICENSING.md` — research/publication versus private FST implementation boundary
- `data/derived/` — de-identified annotation data, audit log, summaries and target schemas
- `evaluation/` — evidence audit, split policy, event matcher, metrics, statistical plan and uncertainty protocol
- `paper/` — SSAC27 abstract, claim map, readiness and open-source compliance review
- `references/` — FST.ai / FST.ai 2.0 publication record

## Open research and implementation boundary

SSAC requires the data used for the submitted research to be available through an open repository; model code is encouraged but not mandatory. This repository therefore prioritizes auditable data and evaluation logic.

Production FST source code, trained production weights, credentials and confidential deployment configuration are not automatically released. Third-party championship footage is not redistributed unless the necessary rights/privacy basis is verified.

See `paper/SSAC27_OPEN_SOURCE_COMPLIANCE.md` for the current compliance analysis.

## Current submission status

**Automated reproducibility check:** the public GitHub Actions `reproducibility-smoke-test` has completed successfully on the evaluation package (including script compilation and the evaluation smoke test).

The current final abstract candidate contains **393 words including title and section headings**, uses the required Introduction/Methods/Results/Conclusion structure, and is mapped claim-by-claim to public evidence. A fully rewritten 5,000+ word current-evidence manuscript is also provided in `paper/SSAC27_FULL_PAPER_CURRENT_EVIDENCE.md`.

The stronger manuscript-ready FST efficacy benchmark still requires:
1. an independent event census that observes false negatives;
2. a frozen FST/FST 2.0 prediction export;
3. actual model-generated numerical uncertainty;
4. reconciliation of latency and human-study source observations.

See `paper/SSAC27_SUBMISSION_READINESS.md`.

## Contact

Scientific correspondence: Keivan Shariatmadar, htw saar – University of Applied Sciences.
