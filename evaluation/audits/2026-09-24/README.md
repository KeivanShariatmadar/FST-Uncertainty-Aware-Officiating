# SSAC27 evidence availability and v4.2 implementation audit

Audit date: 2026-09-24. Public baseline: `dd28e31b98e9051b8aecb8ad7d06aca29d995e24`.

## Outcome

The private v4.2 ZIP is now readable and passes its ZIP CRC integrity check. This resolves the earlier access problem, but the supplied implementation does not provide the automatic head-kick event inference required by the registered benchmark. The available championship archive supplies candidate clips and annotations, not a verified independent census of events over a declared observation period. No ground-truth, prediction, or matched-event CSV has been manufactured.

The existing public candidate audit reproduces unchanged: 546 raw records, 545 canonical records, 449 TP-labelled and 96 FP-labelled candidates, 73 bout clusters, candidate-confirmation fraction 0.823853, and normal 95% cluster-jackknife interval 0.811628–0.836078. These remain descriptive candidate-annotation results. They are not newly measured model TP/FP/FN, precision, recall, or F1.

## Private implementation inspected

Package fingerprint and all 16 member fingerprints are in [v42/package_manifest.json](v42/package_manifest.json) and [v42/file_inventory.csv](v42/file_inventory.csv). The package is 17,841 bytes and contains seven Python files, six HTML templates, a README, dependency requirements, and a role-detector dataset YAML. It contains no weight files. Python files were inspected statically; the web application was not launched, trained, or used for inference.

Findings below describe this exact ZIP only, not every FST version or the capabilities claimed in publications. Private source is not released here. Source locations identify the inspected implementation for an authorized private reviewer.

| Component | Observed implementation | Benchmark implication |
|---|---|---|
| Model loading | `app/core/engine.py`, `JobConfig` (line 15) defaults to `yolo11n-pose.pt`; `HeadkickJob` (line 79) loads the configured YOLO model. | A model filename is not a frozen checkpoint hash. No checkpoint is bundled. |
| Detection | `SourceWorker.detect` (line 42) tracks class-0 person boxes and assigns CHUNG/HONG/REFEREE using HSV color heuristics. | Person/role detection is not a head-kick/contact/action event prediction. The returned records have tracking ID, box, color scores, and role. |
| Head-kick events | Full Python-source inspection found no head-kick action classification, contact inference, or temporal event aggregation path. | The class name `HeadkickJob` does not establish an implemented head-kick detector. An event exporter alone cannot fill this gap. |
| Scores and marks | `HeadkickJob.adj` (line 89), `mark` (line 118), and `control` (line 124) record operator score changes and marked snapshots. | Manual scores and training marks cannot be exported as independent frozen model predictions. |
| Time | `SourceWorker.loop` (line 64) increments a processed-frame counter while frame skipping can consume multiple source frames. Logged manual actions use wall-clock time. | Neither counter nor action time supplies a verified bout-relative event timestamp or clip offset. Measured display-loop FPS is not a source-video time base. |
| Confidence and uncertainty | Detection has a configurable person-detection confidence threshold and heuristic role-color scores. No numerical head-kick event uncertainty or automatic deferral path was found. | These quantities cannot be relabelled epistemic uncertainty or used as an FST event risk–coverage signal. |
| Training | `app/core/training.py` trains a role/object detector; the YAML lists athlete, referee, judge, coach, and other-person classes. | Training this component does not reproduce a frozen head-kick action model. |
| Reproducibility | Some requirements are lower bounds, and weights are referenced by filename. | A complete frozen runtime, weights, preprocessing, event logic, and training-history manifest remain required. |

The keyword signal report is inventory assistance only. Absence/presence of a keyword is not the basis for the semantic findings above.

## Championship dataset inspected

[dataset_inventory_summary.json](dataset_inventory_summary.json) records the archive SHA-256, byte size, aggregate inventory, and annotation-source fingerprints. Inventory excludes resource-fork entries and directory entries.

- 541 video files: 519 MOV and 22 MP4.
- Directory-labelled training population: 450 videos in 54 match folders.
- Directory-labelled test population: 91 videos in 17 match folders.
- No video files in the validation directory. There are also 54 PNG files in training folders, one ODS workbook, and one PDF.
- No literal train/test match-folder overlap was found. This does not prove independent bouts, independent athletes, or absence of training leakage.
- The attached CSV has 546 candidate-labelled rows (450 True Positive, 96 False Positive) and 74 source match IDs. The archive workbook has the same label counts; equality of counts alone is not proof of row-level equivalence.
- Five annotated source IDs lack an exactly matching video folder; two video folders lack an exactly matching annotation ID. These are unresolved identifier discrepancies, not five proven missing bouts or two proven extra bouts. Do not repair them by guessing.
- Annotation fields describe candidate clips, players, labels, human confidence, difficulty, event class, contact, visibility, and notes. There is no dedicated source-relative event timestamp field or complete-video coverage manifest.

The archive was inventoried from its ZIP directory and its annotation workbook inspected. Its 541 videos were not exhaustively decoded or independently annotated. A complete-bout event population and clip-to-bout offsets have not been established. An annotation-independent review of selected clips could support a specifically scoped clip benchmark later; it would not establish championship-wide detection recall or recover events outside those clips.

Other local repositories contain selected IVR/experimental clips, but their identity, provenance, and model lineage were not established as this championship's frozen FST benchmark. They were not substituted for missing benchmark inputs. Unmapped local screen recordings likewise do not establish a championship observation period.

## Requested outputs and evidence gaps

| Output | Status | Required evidence |
|---|---|---|
| `ground_truth_events.csv` | Not generated | Declared complete observation windows; source-to-bout/time mapping; exhaustive annotation independent of model candidates; event definition, ambiguity/adjudication procedure, and annotator provenance. Include missed events and record reviewed windows with no events. |
| `fst_ssac_predictions.csv` | Not generated | The actual frozen event-level FST implementation/checkpoint or a previously frozen complete export with provenance. Export every eligible prediction without reference-label access. |
| `matched_events.csv` | Not generated | Both frozen layers; reconciled identifiers; justified prespecified tolerance and class rule. No arbitrary tolerance was selected. |
| TP/FP/FN and precision/recall/F1 with bout-clustered intervals | Not estimable from inspected evidence | Above inputs plus a complete bout-cluster mapping for reference events and predictions, including false positives. The existing selected-candidate labels cannot reveal FN. |
| Risk–coverage/selective deferral | Not generated | Genuine event/decision model scores with documented meaning, direction, missingness, and frozen threshold-selection procedure. Human High/Medium labels, role-color scores, and filenames containing confidence are insufficient. |

Before a real benchmark run, ensure every matched row, including FP-only rows, receives the reconciled bout cluster. The current runner defaults to `match_id`; explicitly using the true cluster requires complete propagation to the matched table. The current matcher implements deterministic greedy nearest-time matching, so that rule must be named in the frozen protocol rather than described as maximum-cardinality assignment. Score ties also need an explicit threshold policy before selective-deferral results are interpreted. No evaluator changes were made in this audit.

For uncertainty recorded only on emitted candidates, a future curve measures selective candidate error. It cannot measure how deferral handles undetected events or establish improved human decisions without human-outcome evidence.

## Verification and preservation

Executed successfully against the baseline with the bundled Python runtime:

```text
python evaluation/inspect_fst_package.py <private-v42-zip> --out evaluation/audits/2026-09-24/v42
python evaluation/tests/smoke_test.py
python evaluation/tests/public_audit_repro_test.py
python evaluation/run_reproducibility.py --out <local-audit-output>
```

The smoke test exercises matching and evaluation on software fixtures. Those fixtures are not research evidence. The public reproduction test passes; the runner correctly reports that the independent event benchmark was not run because its two evidence files are absent.

This update adds metadata and audit documentation and updates the project-state access note. Candidate data, statistical outputs, evaluation algorithms, abstract, and manuscript are preserved. No private source, credentials, weights, athlete-name tables, or footage are published.
