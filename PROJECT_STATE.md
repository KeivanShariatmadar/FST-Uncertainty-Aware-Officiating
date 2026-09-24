# SSAC27 FST Research Package — Master State

**Last updated:** 2026-09-24

This file is the project-level source of truth for the SSAC27 FST.ai / FST.ai 2.0 submission. It is intended to prevent title, claim, dataset, and manuscript drift across later revisions.

## Scope

Included:
- FST.ai;
- FST.ai 2.0;
- uncertainty-aware, human-in-the-loop Taekwondo officiating/video review.

Excluded:
- APEX;
- Digital TA;
- WT-SCIP/SCIP;
- SILs;
- FST.ai 2.5 and unrelated broader platforms.

## Authors for SSAC27

1. Keivan Shariatmadar — htw saar – University of Applied Sciences, Saarbrücken, Germany
2. Ahmad Osman — htw saar – University of Applied Sciences, Saarbrücken, Germany
3. Ramin Rey — Austrian Taekwondo Federation (AUT), Austria

The FST.ai 2.0 arXiv citation-of-record uses the spelling **Ramin Ray**; the SSAC27 submission uses **Ramin Rey** as supplied by the authors.

## Authoritative SSAC27 title

**When Should AI Defer? An Evidence Audit of AI-Assisted Video Review in Competitive Taekwondo**

## Authoritative abstract

Use:
- 'paper/SSAC27_ABSTRACT_FINAL.md'

For direct form entry:
- 'paper/SSAC27_SUBMISSION_COPY_PASTE.txt'

The authoritative abstract contains 362 whitespace-delimited words including title and section headings.

Do not use the historical PDF as the current abstract:
- 'paper/SSAC27_FST_Competition_Abstract_Final.pdf'

## Authoritative current full paper

Use:
- 'paper/SSAC27_FULL_PAPER_MASTER.md'

This is the scientifically polished current-evidence manuscript. It is written around evidence that is currently auditable and should be upgraded, rather than replaced, if the frozen-model benchmark becomes available.

Scientific review memo:
- 'paper/FINAL_SCIENTIFIC_REVIEW.md'

## Verified current-study evidence

Raw annotation population:
- 546 candidate records;
- 74 recorded match IDs;
- 73 bout clusters after documented same-bout linkage;
- 450 TP-labelled and 96 FP-labelled raw candidates;
- one exact duplicate match+clip key.

Canonical exact-deduplicated population:
- 545 candidate records;
- 449 TP-labelled;
- 96 FP-labelled;
- candidate-confirmation fraction = 449/545 = 82.39%;
- delete-one-bout cluster-jackknife 95% CI = 81.16%–83.61%.

Annotation structure:
- 535/546 = 97.99% of raw rows occur in four dominant joint annotation patterns;
- visibility: 172 good, 152 moderate, 222 partial occlusion;
- canonical partial-occlusion stratum: 222 candidates = 126 TP-labelled + 96 FP-labelled;
- all 96 FP-labelled raw candidates share Medium human confidence / Hard / uncertain event / uncertain contact / partial occlusion.

Interpretation:
- human confidence is not FST model uncertainty;
- candidate-confirmation is not recall, F1, overall match accuracy, or a complete event-level model-performance estimate;
- recall/F1 require an independent reference-event census containing false negatives.

## Quarantined prior-public claims

Do not present the following as newly verified SSAC27 results unless source observations and denominators are reconstructed:
- 85% decision-review-time reduction;
- 93% referee trust;
- approximately 92.7–92.8% accuracy descriptions;
- 89.7/89.3 s to 4.6 s review-time descriptions;
- historical/pilot override-reduction descriptions.

See:
- 'evaluation/PUBLISHED_CLAIMS_AUDIT.md'
- 'evaluation/evidence_ledger.csv'

## Registered stronger benchmark

The manuscript-ready FST efficacy benchmark requires:
1. 'ground_truth_events.csv' — independently enumerated eligible reference events, including missed events;
2. 'fst_ssac_predictions.csv' — frozen predictions generated without access to reference labels;
3. deterministic one-to-one event matching;
4. TP/FP/FN, precision, recall, F1 with bout-level dependence handled;
5. genuine numerical model uncertainty/evidence;
6. risk-coverage/selective-deferral analysis at a clearly declared evaluation unit.

If uncertainty exists only for emitted candidates, the risk-coverage result is a selective candidate-precision analysis and does not cover false negatives. Decision/request-level uncertainty is preferred where available.

## Private FST v4.2 package

Supplied private file:
- 'FSTai_Competition_Platform_v4_2(1).zip'
- workspace file ID: 'file_00000000c9608210b39bcb6091e41efe'
- observed size: 17,841 bytes.

The ZIP was successfully read and statically inspected on 2026-09-24. Its CRC integrity check passed. The supplied implementation tracks people and assigns roles, supports manual scoring and annotation, and trains a role detector. It does not supply the automatic head-kick event classifier, bundled frozen weights, or event-level numerical uncertainty needed for the SSAC benchmark. This finding is limited to the inspected ZIP, not all FST implementations.

The championship clip archive was also located and inventoried: 541 videos (450 in training folders, 91 in test folders), with unresolved annotation/folder identifier discrepancies. A complete independent event census, source-time mapping, and frozen event predictions remain unavailable. No empirical event-matching, recall/F1, or risk–coverage result has been generated.

Verified findings, hashes, dataset inventory, fresh reproduction results, and the exact evidence needed to continue are in [the 2026-09-24 evidence audit](evaluation/audits/2026-09-24/README.md). Existing candidate data and manuscript claims are unchanged.

Additional G1 source files subsequently supplied by the author contain automatic heuristic head-kick candidate logic, alongside simulated and incomplete variants. The author identifies the historical script/settings as unknown. [The G1 follow-up](evaluation/audits/2026-09-24/G1_FOLLOWUP.md) records source verification, historical log and Austria recording inventories, runtime checks, score semantics, and the steps needed for a new frozen benchmark. These findings extend the available implementation evidence without changing the earlier ZIP-specific audit or establishing new performance metrics.

Initial offline replay development is now complete: 28 Austria recordings were fingerprinted; nine software tests passed; two short video windows were replayed, with an exact repeat of the separate single-camera run. Frequent athlete-role failures and the lack of independent event labels prevent promotion to a benchmark. No accuracy or deferral metrics were generated. See [the replay development report](evaluation/audits/2026-09-24/REPLAY_DEVELOPMENT.md).

Private/local audit tools:
- 'evaluation/inspect_fst_package.py'
- 'evaluation/LOCAL_IMPLEMENTATION_AUDIT.md'
- 'evaluation/IMPLEMENTATION_AUDIT_CHECKLIST.md'
- 'evaluation/FROZEN_MODEL_EXPORT_SPEC.md'
- 'evaluation/model_manifest_template.json'

Do not upload private production source, credentials, production model weights, or confidential configuration merely to satisfy the public research package.

## Reproducibility status

The repository includes:
- de-identified source-derived candidate data;
- canonical audited data;
- audit log and provenance;
- evidence ledger;
- statistical analysis plan;
- split/leakage policy;
- candidate-audit script;
- deterministic event matcher;
- metric evaluator;
- selective-prediction protocol;
- validators;
- automated GitHub Actions smoke testing.

GitHub Actions has produced successful reproducibility-smoke-test runs. The automated gate compiles the evaluation scripts and executes the public smoke test.

## Open-data / rights boundary

The data supporting the current annotation-audit results are public and de-identified.

Raw championship video is not automatically redistributable merely because FST is owned by the authors. Broadcast, event, federation, privacy, and athlete-likeness rights must be resolved before raw footage is placed in the public repository.

Model code is not required by the current SSAC27 rule; the public package prioritizes the data used for the current results and the reproducible evaluation logic.

## Licensing

Current repository state:
- public repository;
- 'CITATION.cff' license = 'NOASSERTION';
- no blanket software/data reuse license imposed;
- proprietary FST implementation boundary documented in 'IP_AND_LICENSING.md'.

Any future license must be chosen deliberately because the authors intend to permit research use while retaining commercial rights.

## SSAC27 competition dates

- Abstract deadline: October 1, 2026, 11:59 p.m. Eastern Time.
- Full manuscript if invited: December 4, 2026, 11:59 p.m. Eastern Time.
- Track: Other Sports.

## Final submission rule

No numerical claim enters the SSAC27 Results section unless its population, denominator, evaluation unit, provenance, calculation, and release status are identifiable in the evidence package.

When stronger evidence becomes available, update this master state first, then the evidence ledger, abstract claim map, abstract, manuscript, README, and submission checklist in that order.
