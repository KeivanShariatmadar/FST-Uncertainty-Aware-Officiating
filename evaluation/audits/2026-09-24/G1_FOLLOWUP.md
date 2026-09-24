# G1 detector and initial benchmark follow-up

## Status and scope

The author supplied additional G1 detector scripts after the v4.2 platform audit. These files establish that automatic head-kick candidate logic exists outside the inspected v4.2 ZIP. The earlier ZIP-specific finding remains valid; it must not be generalized to these additional implementations.

The author reports that the historical script and settings are unknown. The Austria Open 2026 recordings are treated as an initial benchmark candidate, pending bout/window identification. No claim links the new source files to the previous 545-candidate championship audit, and no historical performance is reconstructed by guessing a version.

Private files remain unchanged. This public addendum contains implementation findings and aggregate inventory only. Private source, raw logs, model weights, recording paths, and footage are not included.

## Source verification

All 13 supplied Python detector files parsed successfully. All six supplied shell launchers passed `bash -n`. Syntax success is not validation of detection accuracy or runtime behavior.

| Supplied file or family | Directly inspected behavior | Research use |
|---|---|---|
| `g1_headkick_PRODUCTION.py` | MediaPipe pose plus geometric/velocity candidate score; camera-only interface; manual initialization; CSV only after jury confirmation. | Actual candidate logic exists, but confirmed-only CSV cannot represent all automatic predictions. |
| `g1_two_person_n_cam_lock_prob_matchlog.py` | Pose-based candidate logic and automatic threshold/cooldown logging. | Potential benchmark implementation after an explicitly versioned offline adapter and complete provenance. |
| `g1_two_person_n_cam_lock_prob_matchlog_dashboard_good.py` | Pose-based implementation with jury-confirmation workflow. | Audit pre-review event capture before use; filename does not establish deployment provenance. |
| `g1_two_person_n_cam_lock_prob_matchlog_dashboard.py` and `g1_two_person_n_cam_lock_prob_matchlog_confirm.py` | Blank video canvas; `np.random.rand()` supplies directional scores and points. | Simulation demonstrations; exclude from empirical inference. This does not prove any historical dataset was simulated. |
| `g1_headkick_multicam_matchlog.py` | Approximates head and foot from bounding boxes; weighted distance/speed/height score; automatic session-relative event logging. No pose model is used in this implementation. | Distinct detector family. Its logger schema matches available nonempty logs, but schema agreement does not establish exact producing code or configuration. |
| `headkick_two_person_one_cam_matchlog.py` | MediaPipe Tasks PoseLandmarker, automatic candidate events, manually controlled round-running gate. | A bounded candidate for a new single-camera replay implementation; it is not yet a frozen historical model. |
| N-camera and two-camera fusion matchlog variants | Tasks pose inference, max-camera fusion and automatic events, with round-running gates and wall-clock/threaded processing. | Need synchronized source clocks and explicit evaluation windows before replay. |
| `headkick_two_person_two_cams_matchlog_field.py` | Worker leaves both directional scores at zero and explicitly notes missing multi-person support. | Incomplete detector stub; exclude from empirical performance evaluation. |
| Other field/solo/fast fusion variants | Tasks pose logic; no complete persistent benchmark prediction export established. Solo version is not a two-athlete contact detector. | Do not substitute displayed scores or counters for complete predictions. |

Key source locations for an authorized reviewer:

- Production score: lines 174–184. Pose setup: 304–322. Wall-clock velocity: 517–534. CSV confirmation: 704–715 and 933–939. Pending events: 870–902.
- Simulated dashboard: 176–185; simulated confirmation variant: 163–171.
- Bounding-box detector: head/foot approximation 280–289, score 292–319, relative-time logger 388–401, automatic trigger 803–816.
- One-camera Tasks detector: source interface 440–448, ROI/athlete initialization 463–493, model setup 496–505, wall-clock timing 537–552 and 648–659, trigger 705–718, round-gated logger 183–209.
- Two-camera field stub: 592–610 and 746–750.

Launcher mapping also matters: `run_g1_menu_v3.sh` selects the production script; `run_g1_menu_v2.sh` selects the simulated dashboard; `run_g1_menu_good.sh` references a filename ending `dashboard_.py`, which is absent from the supplied top-level folder. Launchers passed shell syntax checks but were not run or repaired.

## Confidence and uncertainty

The inspected automatic detectors generate numerical heuristic scores from distance, height and velocity. Production uses a product of sigmoid terms; the bounding-box detector uses a weighted sum. Camera fusion generally takes the maximum. These are actual system scores, but they are not established calibrated probabilities or estimates of epistemic uncertainty. No ensemble, credal interval, or comparable event-uncertainty mechanism was established in these paths.

A future confidence-ranking analysis could evaluate these scores after independent outcomes exist and the score direction, ties, thresholds and population are frozen. It would need to be named a heuristic-score selective analysis, not an epistemic-uncertainty result. Candidate-only scores cannot establish how missed events are handled. Human confirmation is not automatic uncertainty-based deferral.

## Historical logs and media

Read-only inventory found 159 CSV files in the supplied folder's log directory:

- 74 session-relative event-log files, 27 nonempty, containing 1,677 rows in total.
- 74 associated summary-schema files containing 177 rows.
- Four other event-schema files with zero data rows; four round-summary files with 12 rows.
- Three additional event/confirmation-schema files with zero data rows.

The 1,677 rows are historical logged candidates across the directory, not validated events, not necessarily unique bouts, and not necessarily all from Austria Open. They are not added to the 545-candidate audit. No complete code/configuration/recording lineage is recorded in the inspected event schema. Session-relative wall time is not automatically source-video time. Header-only logs cannot establish that no events occurred or no actions were missed.

The Austria folder contains 28 MOV recordings and eight PNG screenshots. A bounded metadata/first-frame probe opened 25 recordings and decoded their first frames. The other three timed out/failed to open during that probe. One earlier failed recording opened successfully on the later probe, so these observations do not establish permanent corruption. The 25 accessible files have an approximate summed media duration of 8,617.20 seconds (143.62 minutes). This is not deduplicated bout exposure and is not a statement of complete decode or full annotation coverage.

One sampled Austria frame visibly contains tiled camera feeds and detector overlays. The separately supplied comparison MP4 is about 26.7 seconds long; a sampled frame shows a filmed monitor/demo. Neither observation establishes a complete, independent event census. Unprocessed camera recordings are preferable. If screen recordings must be used, define that population explicitly and document how annotators are blinded to detector outputs without obscuring event evidence.

The field report is qualitative. Its statement that no obvious actions were missed lacks an independent event denominator and a timestamped adjudicated census; it cannot be converted into FN=0 or recall=1.

## Runtime evidence

The installed `headkick` environment reports Python 3.10.19, MediaPipe 0.10.32, OpenCV-Python 4.13.0 and NumPy 2.2.6. A direct probe found `mp.solutions` absent, so the production/base pose scripts cannot run unchanged in that environment.

The supplied general pose-model asset is present. Tasks PoseLandmarker initialization first failed in the restricted runtime because an OpenGL context could not be created. Initialization then passed on the host with a CPU delegate. No camera was opened and no head-kick inference was executed. Successful initialization verifies asset loadability, not detection performance or historical model identity.

All inspected older detector interfaces use camera IDs rather than prerecorded-video files. A Tasks `VIDEO` running mode does not itself provide file replay. Wall-clock-dependent velocity, cooldowns and session times mean that replacing a camera with a video without adapting the time base would change behavior with processing speed. Production also interleaves two athlete crops through one stateful pose object per camera; changing that behavior would be a new model version, not a transparent exporter change.

## Concrete next benchmark steps

1. Register every evaluation recording/window, bout, round, camera stream and source-time offset. Reconcile overlaps and unavailable files. Keep this Austria population separate from the original candidate audit. Record zero-event windows as coverage evidence.
2. Obtain an exhaustive event census over those windows using a declared event/contact definition, timestamp rule and independent annotation/adjudication procedure. Preserve ambiguity instead of forcing labels. The field report and detector-selected logs do not supply this census.
3. Select and freeze one functioning detector family for a **new** benchmark. Record unknown historical provenance explicitly. Freeze source, model asset where used, runtime, ROI/athlete initialization, preprocessing and thresholds before viewing test outcomes. For a single-camera pose baseline, the Tasks one-camera implementation is a candidate, not a completed selection or benchmark.
4. Implement and validate deterministic source-time replay as an explicit benchmark adaptation. Export every automatic event before human review, plus coverage/failure records and complete configuration provenance. Retain human decisions separately. Do not manufacture scores for missing rows.
5. Freeze both evidence layers and the matching tolerance/class rule, then run deterministic matching and bout-clustered evaluation. Only add selective analysis appropriate to the score actually implemented.

No `ground_truth_events.csv`, `fst_ssac_predictions.csv`, or empirical `matched_events.csv` was created from this intake. No TP/FP/FN, precision/recall/F1, or risk–coverage result is claimed. The public candidate data, manuscript and evaluation algorithms remain unchanged.
