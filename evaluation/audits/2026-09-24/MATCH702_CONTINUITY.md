# Contest 702 continuity and source audit

24 September 2026. Verified preparation findings; not a detector evaluation.

## Evidence inspected

Four local recordings were decoded sequentially: 34,721 decoded frames in total. Ninety timestamped samples were visually reviewed for continuity and overlays, not exhaustively annotated for contacts. Two files yielded one fewer decoded frame than their metadata counts; these discrepancies remain unresolved.

The official [World Taekwondo result book](https://web.worldtaekwondo.martial.services/resultbooks/2026-austrian-open-result-book-698f242a0e5b4.pdf), PDF pages 55 and 216, places contest 702 on 8 February 2026, Court 7, men's -74 kg, round of 64. Application labels and the historical log are consistent with that record. Official score aggregates do not supply timestamped visual-contact ground truth.

## Continuity findings

A historical application log contains 347 candidate rows. Eighteen visible cumulative-counter states, six per labelled round recording, admit consistent per-file offset intervals. Under constant-offset, synchronous-counter and no-reset assumptions, the three decoded spans are separated by approximately 149.8–150.7 seconds and 42.0–42.9 seconds. These are conditional gaps in the reconstructed application timeline, not measured missing active-play time or statistical confidence intervals. The offsets are not approved for final matching. The preceding placeholder recording remains potentially related.

The local recordings contain detector scores, counts, boxes and markers that overlap athletes. Simple cropping has not established blinded viewing while preserving contact evidence.

## Additional public source

Direct browser inspection located the federation's [Court 7 Day 2 video](https://www.youtube.com/watch?v=AHyTUvOil-Q), displayed duration 8:02:05. Opening footage and a frame around 5:04 show a court view without visible FST detector overlays. This is a candidate alternate view, not an approved annotation source. Exact contest identification, complete round coverage, interruptions, synchronization and contact visibility still require verification. An in-scene scoreboard is not an event census.

## Release decision

Keep the linked recordings together and unreleased for held-out evaluation. No independent ground-truth rows, frozen benchmark predictions, TP/FP/FN, precision/recall/F1, clustered intervals or risk–coverage results were produced by this audit. The historical candidate log cannot substitute for either required evidence file.

The private coordinator package retains source fingerprints, decode reports, visual samples, counter transcriptions and a prepared original-footage request. No request was sent. Private footage, screenshots, source code, logs and local paths are not part of this public update. Existing public candidate-audit data and numerical claims remain unchanged.

Next requirements: verify complete cue-free observation windows; obtain independent review and adjudication; freeze the executable model and settings before benchmark inference; then match and evaluate on the same approved windows. Genuine model uncertainty has not been established by this continuity audit.
