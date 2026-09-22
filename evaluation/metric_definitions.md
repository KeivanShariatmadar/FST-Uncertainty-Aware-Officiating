# Metric Definitions

The definitions below establish the reporting standard for the SSAC study. They do not themselves assert a numerical result.

## Classification metrics

For each declared task and positive class:

- **Precision** = TP / (TP + FP)
- **Recall (sensitivity)** = TP / (TP + FN)
- **F1** = 2 × precision × recall / (precision + recall)
- **Specificity**, where applicable = TN / (TN + FP)
- **Balanced accuracy**, where applicable = (sensitivity + specificity) / 2

The full paper must state whether metrics are binary, macro-averaged, micro-averaged, weighted, or class-specific.

## Expert agreement

Raw agreement is the proportion of evaluation units on which the AI-supported output and declared expert/reference decision agree.

Where the data permit, chance-corrected agreement (for example Cohen's kappa for an appropriate two-rater setting) should be reported in addition to raw agreement.

## Review latency

Latency must be tied to a precisely defined start and end event. Baseline and AI-assisted workflows must use comparable definitions.

Preferred reporting includes sample size, median, interquartile range, and distributional information. Mean and standard deviation may be added where appropriate.

If a relative reduction is reported:

`relative reduction = (baseline latency - assisted latency) / baseline latency`

The denominator and aggregation level must be explicit.

## Uncertainty/selective prediction

Where uncertainty outputs are available, the preferred analysis evaluates performance as a function of retained coverage. Cases below a declared evidence/reliability criterion may be deferred to human review.

Relevant outputs can include risk–coverage curves, accuracy at fixed coverage, coverage at a fixed error criterion, and characteristics of deferred cases.

## Human trust/acceptance

A trust or acceptance percentage must not be reported without specifying the respondent population, sample size, question wording or operational definition, response scale, aggregation rule, and study context.

## Confidence intervals

For the full paper, empirical proportions and principal latency effects should include uncertainty intervals where the underlying data permit a defensible calculation.
