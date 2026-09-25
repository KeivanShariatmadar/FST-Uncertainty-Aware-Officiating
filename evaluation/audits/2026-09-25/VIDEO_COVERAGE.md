# Public video coverage follow-up

25 September 2026. Coordinator inspection only; no ground-truth event labels.

Source: [ÖTDV Court 7 Day 2 archive](https://www.youtube.com/watch?v=AHyTUvOil-Q). Times below are approximate displayed player times, not frame-exact source timestamps. Inspection used selected browser frames, not a continuous frame-by-frame audit. Loading/seek states were not treated as source-video gaps.

## Observations

| Player time | Observed state |
|---|---|
| 0:00–0:42, sampled | Athletes wait with the referee; blue holds the helmet. No first-round fighting was observed in these samples. |
| 0:52 | Athletes seated; scoreboard transitioning. |
| 1:04 and 1:12 | Scoreboard shows blue leading one round to zero, with round 1 indicated. |
| 1:32 and 1:37 | Athletes return and prepare with the referee. |
| 1:47 | Active round 2; scoreboard indicates round 2 and approximately 1:56 remaining. |
| 4:37 | Round 2 scoreboard shows red 12, blue 9, with a small amount of clock time remaining. |
| 4:47 | Round break; rounds tied 1–1. |
| 5:47 | Athletes preparing after the break. |
| 5:57 | Active round 3; red 4, blue 0, approximately 1:54 remaining. |
| 9:07 | Referee separates athletes; scoreboard partly obstructed. |
| 9:17 | Round 3 scoreboard red 17, blue 8, approximately 3 seconds remaining. |
| 9:27 | Blue moves toward the corner while referee and red remain on court. |
| 9:57 | Equipment attention for red; scoreboard shows a time-out state. |
| 10:57 | Different contest preparation; scoreboard round 1, 2:00. |

Score states and visible country markings corroborate the contest-702 hypothesis against the official result book. Athlete identities were not established by facial recognition. A fully legible identity slate or an independently documented cross-camera synchronization remains required before final canonical mapping.

## Working boundary brackets

- Round 2 start: approximately 1:37–1:47; end: 4:37–4:47.
- Round 3 start: approximately 5:47–5:57; apparent end transition: 9:17–9:27. The later equipment/time-out state needs continuous review before finalizing the end.
- Round 1 start and fighting: not established in the archive. Opening samples are consistent with a post-fighting review/wait, followed by a one-round lead. Do not declare a complete three-round source.

These brackets are navigation aids only. They are not observation-window releases, matching tolerances, event times, or confidence intervals. Do not label uninspected intervals as event-free. Do not infer contacts from score increments. No empirical prediction or ground-truth export was created.

## Release gate and concrete next work

1. Obtain a stable local research copy or original camera recording, retaining exact timestamps and provenance. Verify whether any preceding segment contains round 1.
2. Confirm contest identity and synchronize at least three distinct visible actions across local and public views; inspect residual drift and interruptions. No numerical synchronization offset is approved yet.
3. Review the whole proposed window continuously, finalize boundaries and visibility exclusions, and register them before inference. If only later rounds are available, disclose that restricted population and keep all views/rounds of this bout in one split.
4. Two independent qualified reviewers must enumerate contacts without viewing FST outputs, preserve separate first-pass labels, and adjudicate disagreement. The coordinator's source inspection is not a substitute for those labels. Reviewer assignments remain unconfirmed.
5. Freeze the actual executable detector, weights and settings for these windows, export predictions, then run matching and evaluation. A single bout cannot support a meaningful bout-clustered interval; collect additional independently reviewed bouts before that claim.

The public camera has no visible FST overlays in inspected frames, but an in-scene official scoreboard remains visible. Any masking for reviewer blinding must preserve athlete/contact evidence and be validated before release. No masking, inpainting or generated contact pixels were used.
