# Selective-Prediction / Risk-Coverage Protocol

## Why the evaluation unit matters

A risk-coverage curve is meaningful only after defining what receives an uncertainty score. FST may expose uncertainty at different levels (frame, candidate event, IVR request, or final decision). These levels must not be mixed.

## Preferred SSAC unit: IVR decision/request

If the frozen implementation produces a reliability/uncertainty value for every eligible IVR decision request, define:

- **coverage** = fraction of IVR requests on which the AI issues a recommendation rather than deferring;
- **selective risk** = fraction of retained AI recommendations that disagree with the independent reference decision.

This is the preferred human-in-the-loop interpretation because a deferred request is explicitly handed to the referee/jury.

For threshold `tau` on an uncertainty score `U` where larger means more uncertain:

[
C(\tau)=P(U\le\tau),
qquad
R(\tau)=P(\text{decision error}\mid U\le\tau).
]

The final paper should state whether a missed head-kick event is represented as an erroneous IVR decision at this level.

## Candidate-event mode

If numerical uncertainty exists **only for emitted model detections**, the resulting curve has a narrower interpretation:

- coverage is the fraction of emitted candidates retained;
- risk is FP/(TP+FP) among retained candidates.

This is a **selective candidate-precision** analysis. It does not measure the effect of deferral on false negatives because undetected reference events have no emitted candidate uncertainty value.

The repository's current `evaluate_predictions.py` risk-coverage helper follows this candidate-event interpretation when it uses TP/FP rows carrying a model uncertainty/confidence value.

## Event-census mode

If the implementation produces a score for every temporal window or every independently enumerated event opportunity, an event-level selective analysis can include missed events. The construction must explicitly define:

- the eligible event/window population;
- how no-detection outputs receive a score;
- the reference label for each opportunity;
- what constitutes error after deferral.

This should be preferred over candidate-only selective precision when the implementation supports it.

## Threshold selection

Thresholds used for headline results must be fixed without optimizing on the final test population. Acceptable routes include:

- predefined operational threshold;
- development/validation-set selection;
- a threshold derived from a target risk/coverage criterion on validation data.

Report the selection rule.

## Outputs

For the declared evaluation unit, report:

- full risk-coverage curve;
- number of eligible cases;
- coverage at selected thresholds;
- risk at selected thresholds;
- baseline risk at 100% coverage;
- composition of deferred cases;
- uncertainty-score definition and orientation;
- confidence intervals where the sample supports them.

Area under the risk-coverage curve may be reported as a summary, but it should not replace the curve or fixed operating points.

## Contextual analysis of deferral

Where independently annotated, compare retained versus deferred cases by:

- visibility/occlusion;
- turning/non-turning action;
- contact quality;
- reference ambiguity;
- difficulty.

Because the current candidate annotation table is structurally patterned, these variables are descriptive context and are not themselves used as the FST uncertainty score.

## Human authority

Deferral is not counted as an autonomous AI error. It is a routing action: the system explicitly indicates insufficient evidence and leaves the decision to the authorized human official. The operational cost of deferral (review time/workload) should be reported alongside predictive risk when possible.
