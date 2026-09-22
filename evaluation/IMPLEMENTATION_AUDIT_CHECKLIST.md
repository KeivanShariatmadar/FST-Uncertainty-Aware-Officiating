# Frozen FST Implementation Audit Checklist

## Purpose
This checklist defines the source-code audit required before generating the SSAC27 frozen prediction table. It does not assert that the uploaded FST v4.2 archive has already passed these checks.

## Source package currently supplied to the research workspace
- filename: `FSTai_Competition_Platform_v4_2(1).zip`
- observed uploaded size: 17,841 bytes
- intended role: implementation reference for the FST competition platform v4.2
- cryptographic hash: pending byte-level runtime access

The public SSAC repository does not automatically publish this source package.

## Audit sequence

### 1. Identity and environment
Record:
- package/version label;
- source file inventory;
- Python/runtime version;
- dependency manifest;
- operating-system assumptions;
- hardware assumptions;
- model framework versions;
- external API/service dependencies, if any.

### 2. Entry points
Identify:
- command-line or UI entry point;
- batch-video inference path;
- live/video-stream inference path;
- configuration loading;
- model loading and weight paths.

### 3. Input processing
Trace:
- accepted video formats;
- frame decoding and FPS/time-base handling;
- resizing/cropping/normalization;
- deblurring or image enhancement actually implemented;
- athlete/head/foot/pose extraction actually implemented;
- temporal-window construction.

Paper descriptions are not substituted for code behavior.

### 4. Detection and event logic
Trace:
- candidate-generation threshold;
- action classes;
- turning/non-turning discrimination;
- contact/impact verification;
- temporal smoothing;
- duplicate/event suppression;
- event start/peak/end definition;
- point recommendation logic.

### 5. Confidence and uncertainty
For every numerical reliability output, determine:
- variable name and code location;
- mathematical definition;
- whether it is softmax/detector confidence, ensemble disagreement, interval/credal quantity, heuristic score, or another construct;
- range/orientation;
- calibration procedure, if any;
- threshold logic;
- whether it can trigger abstention/defer-to-human behavior.

A generic confidence score is not called epistemic uncertainty without implementation evidence.

### 6. Timing
Separate:
- per-frame compute time;
- model inference time;
- event aggregation time;
- end-to-end machine latency;
- human review latency.

Do not mix these quantities.

### 7. Logging/export
Identify what the implementation already records:
- timestamps/frame indices;
- event labels;
- confidence/uncertainty;
- overlays;
- referee confirmation/override;
- latency;
- model/config version.

Prefer adapting existing logging over reconstructing outputs manually.

### 8. Frozen evaluation configuration
Before running the test population, freeze:
- model weights/checksum;
- thresholds;
- event-matching-independent inference configuration;
- preprocessing settings;
- random seed(s);
- hardware/software environment;
- code/package fingerprint.

No final-test tuning.

### 9. Prediction export
Generate one immutable `fst_ssac_predictions.csv` conforming to `FROZEN_MODEL_EXPORT_SPEC.md`.

### 10. Audit outcome
Classify each component:
- verified in code;
- described in paper but not implemented;
- implemented differently from paper description;
- unavailable/external dependency;
- requires clarification.

Any mismatch between manuscript wording and actual v4.2 behavior should be resolved in favor of the inspected implementation for the SSAC experiment.
