# Initial replay development — 2026-09-24

These are software-development observations, not an event-level performance benchmark. No independent ground-truth census or empirical TP/FP/FN result has been produced.

## Evidence registration

All 28 supplied Austria recordings were fingerprinted locally and assigned stable accession IDs. Each yielded a first frame on the latest accessibility check. This supersedes the earlier three first-frame access failures; it does not establish full-file decoding or complete bout coverage. Private worklists retain source paths and fingerprints. Empty reference-event and reviewed-window templates were created; they contain no annotations and must not be interpreted as zero-event observations.

## New offline adaptation

A development-only adapter extracts the supplied single-camera Tasks detector's audited scoring logic after verifying its source fingerprint. It uses increasing source-video timestamps, fixed pane/court crops and initial athlete boxes, and the original normal parameters (threshold 0.52, directional cooldown 0.85 seconds). It replaces a hash-set tie with a deterministic rule and replaces the manual round gate with an explicit observation window. These adaptations are not a reconstruction of unknown historical settings or a frozen FST v4.2 benchmark.

Nine software fixture tests passed. The private run manifests record input, source, model, adapter, configuration and output fingerprints, runtime versions and coverage. Missing athlete roles and collisions are retained in frame output. All emitted candidates would be retained before human review and marked ineligible for the benchmark.

## Actual short-window runs

Each run covered source timestamps from 0 seconds up to, but excluding, 10 seconds. Selection and configuration preceded inference; parameters were not optimized against event labels.

| Development input | Processed frames | Both roles usable | Missing role | Same pose assigned to both roles | Emitted candidates |
|---|---:|---:|---:|---:|---:|
| Separate single-camera recording, outside Austria benchmark | 300 | 107 | 100 | 93 | 0 |
| Exact repeat of that run | 300 | 107 | 100 | 93 | 0 |
| First registered Austria recording, selected camera pane | 196 | 9 | 96 | 91 | 0 |

Frame and candidate output files were byte-identical across the two single-camera runs. This establishes repeatability for those two runs only. All processed timestamps were increasing and inside the requested window, and recorded output fingerprints were verified.

Zero emitted candidates does not mean zero true events, zero false negatives, or good detector performance. Frequent role failures make this implementation unsuitable for promotion to a benchmark without further development and verification. The Austria sample contains detector overlays, so independent blinded reference annotation has not been established. The complete first Austria recording and all linked material from its bout must be reserved for development and excluded from a held-out test.

## Remaining gates

1. Reconcile bout/round identities, source timing, overlapping views, replays and reviewed coverage; freeze a bout-level split.
2. Establish an independent annotation procedure with qualified review and adjudication. Obtain unoverlaid footage or verify a blinding procedure that preserves contact evidence. Exhaustively enumerate events, including detector misses.
3. Resolve role assignment and tracking limitations in a new version, then freeze the implementation and configuration before held-out inference. Historical logs cannot reconstruct unknown historical settings.
4. Finalize event definitions, ambiguity handling and a justified matching tolerance before test evaluation; verify the matching and bout-clustering implementation for the promoted export.
5. Only then calculate TP/FP/FN, precision/recall/F1 and bout-clustered intervals. Existing geometric heuristic scores are not calibrated probabilities or demonstrated epistemic uncertainty; no uncertainty-based deferral claim is supported by these runs.

The public candidate audit and manuscript results remain unchanged. Private source, footage, weights, local paths and raw replay outputs are not included in this publication.
